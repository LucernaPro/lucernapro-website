/* =========================================================================
   Lucerna Ship — Worker backend (Cloudflare Worker + D1)
   คู่กับหน้า /ship บนเว็บ — พนักงานเห็นแค่ ชื่อ/สินค้า/จำนวน/วันที่ ไม่มีเงิน

   Bindings ที่ต้องตั้ง:
     D1:      DB           (database: lucerna-ship)
     Secret:  PIN          รหัสพนักงาน (หน้า /ship ใช้)
     Secret:  IMPORT_KEY   รหัสสำหรับสคริปต์ import จาก Google Sheet (คนละตัวกับ PIN)

   Endpoints:
     POST /import          x-key: IMPORT_KEY   upsert orders (สคริปต์ lucerna_push.py)
     GET  /orders?date=    x-pin               รายการของวันนั้น (จัดกลุ่มต่อลูกค้า)
     GET  /pending         x-pin               ค้างส่งทุกวัน (เก่าสุดก่อน)
     POST /parse-match     x-pin               {text, date} → parse เลข ปณ + จับคู่ (ยังไม่บันทึก)
     POST /confirm         x-pin               บันทึกผลที่พนักงานยืนยันแล้ว
     POST /assign          x-pin               {tracking, gid} จับคู่เอง (จาก pending/เลขลอย)
     POST /unassign        x-pin               {gid} ถอนเลขออก (กดผิด)
     GET  /orphans         x-pin               เลขลอยที่ยังเปิดอยู่
     POST /orphan-archive  x-pin               {id} ตัดทิ้ง (ของเก่าที่ส่งไปก่อนเริ่มระบบ)
   ========================================================================= */

const J = (obj, status = 200) =>
  new Response(JSON.stringify(obj), {
    status,
    headers: {
      'content-type': 'application/json;charset=utf-8',
      'access-control-allow-origin': '*',
      'access-control-allow-headers': 'content-type,x-pin,x-key',
      'access-control-allow-methods': 'GET,POST,OPTIONS',
    },
  });

/* ---------- normalize ชื่อ (หัวใจของการจับคู่) ----------
   หลักการ: precision ก่อน recall — auto-match เฉพาะที่ชัวร์ ที่เหลือให้คนตัดสิน */
const TITLE_RE = new RegExp(
  '^(นาย|นางสาว|นาง|น\\.ส\\.|ดร\\.|ด\\.ช\\.|ด\\.ญ\\.|ผศ\\.|รศ\\.|ศ\\.|คุณ|ครูบา|ครู|อ\\.|' +
  'พล\\.[ตอรท]\\.[ตอ]?\\.?|พ\\.ต\\.[ตอท]\\.?|ร\\.ต\\.[ตอท]?\\.?|จ\\.ส\\.[ตอ]\\.|ส\\.[ตอ]\\.|' +
  'ว่าที่\\s*ร\\.?ต\\.?|' +
  'บริษัทจำกัด|บริษัท|บจก\\.?|บมจ\\.?|หจก\\.?|ห้างหุ้นส่วนจำกัด|ห้างหุ้นส่วน|ร้าน|บ\\.)\\s*'
);
const TAIL_RE = /\s*(จำกัด\s*\(?มหาชน\)?|จำกัด|co\.?,?\s*ltd\.?|ltd\.?|limited|company)\s*$/i;

function norm(s) {
  s = String(s || '')
    .replace(/[\u200b-\u200f\ufeff]/g, '')
    .trim();
  // ตัด emoji/สัญลักษณ์ เหลือตัวอักษร ตัวเลข จุด ช่องว่าง
  s = s.replace(/[^\p{L}\p{M}\p{N}\s.]/gu, ' ').replace(/\s+/g, ' ').trim();
  let prev = '';
  while (prev !== s) { prev = s; s = s.replace(TITLE_RE, '').trim(); }
  s = s.replace(TAIL_RE, '').trim();
  return s.replace(/[\s.]+/g, '').toLowerCase();
}

/* คู่ชื่อถือว่า "เข้าเค้า" เมื่อ: เท่ากันเป๊ะ หรือฝั่งหนึ่งเป็น prefix ของอีกฝั่ง (ปณ ชอบตัดท้ายชื่อ)
   ต้องยาวอย่างน้อย 3 ตัวอักษรกันชนมั่ว */
function nameHit(a, b) {
  if (!a || !b) return 0;
  if (a === b) return 2;                                   // exact
  const min = Math.min(a.length, b.length);
  if (min >= 3 && (a.startsWith(b) || b.startsWith(a))) return 1; // prefix
  return 0;
}

/* ---------- parse ข้อความที่ ปณ ส่งมา ---------- */
const TRACK_RE = /\b([A-Z]{2}\s?\d{9}\s?TH)\b/i;
function parseEmsText(text) {
  const out = [];
  for (const raw of String(text || '').split(/\r?\n/)) {
    const line = raw.trim();
    if (!line) continue;
    const m = line.match(TRACK_RE);
    if (!m) continue;
    const tracking = m[1].replace(/\s+/g, '').toUpperCase();
    const name = line.replace(m[0], '').replace(/[|,;\t]/g, ' ').trim();
    out.push({ tracking, ems_name: name });
  }
  return out;
}

/* ---------- จัดกลุ่มออเดอร์: 1 กลุ่ม = ลูกค้า 1 คน 1 วัน = 1 กล่อง ---------- */
function groupRows(rows) {
  const map = new Map();
  for (const r of rows) {
    const key = `${r.odate}|${r.customer}|${r.receiver || ''}`;
    if (!map.has(key)) {
      map.set(key, {
        gid: r.id, // ใช้ id แถวแรกเป็นตัวแทนกลุ่ม
        odate: r.odate,
        customer: r.customer,
        receiver: r.receiver || '',
        status: r.status,
        tracking: r.tracking || '',
        items: [],
        _ids: [],
      });
    }
    const g = map.get(key);
    g.items.push({ product: r.product, qty: r.qty });
    g._ids.push(r.id);
    if (r.status === 'shipped') { g.status = 'shipped'; g.tracking = r.tracking || g.tracking; }
  }
  return [...map.values()];
}

async function loadGroup(env, gid) {
  const row = await env.DB.prepare('SELECT * FROM orders WHERE id=?').bind(gid).first();
  if (!row) return null;
  const rows = await env.DB.prepare(
    'SELECT * FROM orders WHERE odate=? AND customer=? AND receiver=?'
  ).bind(row.odate, row.customer, row.receiver).all();
  return groupRows(rows.results)[0];
}

async function setGroupTracking(env, gid, tracking, how) {
  const g = await loadGroup(env, gid);
  if (!g) return { error: 'ไม่พบออเดอร์' };
  const now = new Date().toISOString();
  for (const id of g._ids) {
    await env.DB.prepare(
      "UPDATE orders SET tracking=?, status=?, shipped_at=? WHERE id=?"
    ).bind(tracking, tracking ? 'shipped' : 'pending', tracking ? now : '', id).run();
  }
  await env.DB.prepare('INSERT INTO audit(action,detail) VALUES(?,?)')
    .bind(how, `${tracking || '(ถอนเลข)'} -> ${g.customer} ${g.odate}`).run();
  return { ok: true, customer: g.customer };
}

/* ---------- matching engine ---------- */
function matchOne(emsName, groups) {
  const q = norm(emsName);
  if (!q) return { match: null, reason: 'none', candidates: [] };
  let exact = [], prefix = [];
  for (const g of groups) {
    if (g.status === 'shipped') continue;
    const s = Math.max(nameHit(q, norm(g.customer)), nameHit(q, norm(g.receiver)));
    if (s === 2) exact.push(g);
    else if (s === 1) prefix.push(g);
  }
  if (exact.length === 1) return { match: exact[0], reason: 'exact', candidates: [] };
  if (exact.length > 1) return { match: null, reason: 'ambiguous', candidates: exact };
  if (prefix.length === 1) return { match: prefix[0], reason: 'prefix', candidates: [] };
  if (prefix.length > 1) return { match: null, reason: 'ambiguous', candidates: prefix };
  return { match: null, reason: 'none', candidates: [] };
}

/* ---------- Google Sheets sync (แทน lucerna_push.py — ไม่ต้องมีไฟล์บนเครื่องใคร) ----------
   ต้องมี Secret: GOOGLE_SA = เนื้อหา service_account.json ทั้งไฟล์
   scope = spreadsheets.READONLY — เส้นทางนี้เขียนกลับชีตไม่ได้ทางกายภาพ
   อ่านเฉพาะคอลัมน์ A(สินค้า) C(จำนวน) I(ลูกค้า) J(วันที่) K(ผู้รับ) — คอลัมน์เงินไม่ถูก request */

const SPREADSHEET_ID = '1gmdoVX9Oa18zEXBJUNhW1PjRTGaw7PcjkgSK0_YG1RM';
const START_DATE = '2026-08-25'; // guard: ไม่ import ก่อนวันเริ่มระบบ (ของเก่าส่งไปแล้ว จับคู่ไม่ได้)
const MONTH_ABBRS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

const b64u = s => btoa(s).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
const b64uBytes = buf => b64u(String.fromCharCode(...new Uint8Array(buf)));

async function googleToken(env) {
  const sa = JSON.parse(env.GOOGLE_SA);
  const now = Math.floor(Date.now() / 1000);
  const header = b64u(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const claim = b64u(JSON.stringify({
    iss: sa.client_email,
    scope: 'https://www.googleapis.com/auth/spreadsheets.readonly',
    aud: 'https://oauth2.googleapis.com/token',
    iat: now, exp: now + 3600,
  }));
  const pem = sa.private_key.replace(/-----[^-]+-----/g, '').replace(/\s+/g, '');
  const der = Uint8Array.from(atob(pem), c => c.charCodeAt(0));
  const key = await crypto.subtle.importKey('pkcs8', der,
    { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('RSASSA-PKCS1-v1_5', key,
    new TextEncoder().encode(header + '.' + claim));
  const jwt = `${header}.${claim}.${b64uBytes(sig)}`;
  const r = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    body: 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=' + jwt,
  });
  const j = await r.json();
  if (!j.access_token) throw new Error('Google auth ล้มเหลว: ' + JSON.stringify(j).slice(0, 200));
  return j.access_token;
}

function bkkToday() { // วันที่ตามเวลาไทย (Worker รันเป็น UTC)
  return new Date(Date.now() + 7 * 3600 * 1000).toISOString().slice(0, 10);
}
function parseSheetDate(s) { // '25/8/2026' หรือ '25/08/2026' -> '2026-08-25'
  const m = String(s || '').trim().match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
  if (!m) return null;
  return `${m[3]}-${String(+m[2]).padStart(2, '0')}-${String(+m[1]).padStart(2, '0')}`;
}

async function syncFromSheet(env, daysBack = 3) {
  // หน้าต่างเลื่อน: วันนี้ย้อนหลัง daysBack วัน (คลุมเคสลงบิลย้อนหลัง) แต่ไม่ก่อน START_DATE
  const today = bkkToday();
  const want = new Set();
  const months = new Set();
  for (let i = 0; i < daysBack; i++) {
    const d = new Date(Date.parse(today) - i * 86400000).toISOString().slice(0, 10);
    if (d < START_DATE) break;
    want.add(d);
    const [y, mo] = d.split('-');
    months.add(`${MONTH_ABBRS[+mo - 1]}${y}`);
  }
  if (!want.size) return { ok: true, added: 0, updated: 0, note: 'ยังไม่ถึงวันเริ่มระบบ' };

  const token = await googleToken(env);
  let added = 0, updated = 0, scanned = 0;
  for (const title of months) {
    const ranges = ['A', 'C', 'I', 'J', 'K']
      .map(c => 'ranges=' + encodeURIComponent(`${title}!${c}1:${c}3000`)).join('&');
    const r = await fetch(
      `https://sheets.googleapis.com/v4/spreadsheets/${SPREADSHEET_ID}/values:batchGet?${ranges}`,
      { headers: { authorization: 'Bearer ' + token } });
    if (r.status === 400 || r.status === 404) continue; // เดือนนั้นยังไม่มีชีต
    const j = await r.json();
    if (!j.valueRanges) throw new Error('อ่านชีตไม่ได้: ' + JSON.stringify(j).slice(0, 200));
    const [colA, colC, colI, colJ, colK] = j.valueRanges.map(v => v.values || []);
    const cell = (col, i) => ((col[i] || [])[0] || '').toString().trim();
    const nRows = Math.max(colA.length, colI.length, colJ.length);

    for (let i = 0; i < nRows; i++) {
      const product = cell(colA, i), customer = cell(colI, i);
      const odate = parseSheetDate(cell(colJ, i));
      if (!odate || !want.has(odate)) continue;
      if (!product || !customer) continue;
      if (product.startsWith('ยอดขาย') || product.includes('ส่วนลด')) continue;
      let qty = parseFloat(cell(colC, i).replace(/,/g, '')) || 1;
      if (qty <= 0) continue;
      scanned++;
      const okey = `${title}:r${i + 1}`; // ฟอร์แมตเดียวกับ lucerna_push.py — รันปนกันได้ไม่ซ้ำ
      const receiver = cell(colK, i);
      const ex = await env.DB.prepare('SELECT id FROM orders WHERE okey=?').bind(okey).first();
      if (ex) {
        await env.DB.prepare(
          'UPDATE orders SET odate=?, ym=?, customer=?, receiver=?, product=?, qty=? WHERE okey=?'
        ).bind(odate, odate.slice(0, 7), customer, receiver, product, qty, okey).run();
        updated++;
      } else {
        await env.DB.prepare(
          'INSERT INTO orders(ym,odate,customer,receiver,product,qty,okey) VALUES(?,?,?,?,?,?,?)'
        ).bind(odate.slice(0, 7), odate, customer, receiver, product, qty, okey).run();
        added++;
      }
    }
  }
  await env.DB.prepare('INSERT INTO audit(action,detail) VALUES(?,?)')
    .bind('import', `sync +${added} ~${updated} (scan ${scanned}, ${[...want].join(',')})`).run();
  return { ok: true, added, updated, days: [...want] };
}

export default {
  async scheduled(event, env, ctx) { // cron: sync อัตโนมัติ
    ctx.waitUntil(syncFromSheet(env, 3).catch(() => {}));
  },
  async fetch(req, env) {
    if (req.method === 'OPTIONS') return J({ ok: true });
    const url = new URL(req.url);
    const path = url.pathname.replace(/\/$/, '');

    /* ---- import (สคริปต์ฝั่ง Pist เท่านั้น) ---- */
    if (path === '/import' && req.method === 'POST') {
      if (req.headers.get('x-key') !== env.IMPORT_KEY) return J({ error: 'unauthorized' }, 401);
      const body = await req.json();
      let added = 0, updated = 0, skipped = 0;
      for (const r of body.rows || []) {
        if (!r.okey || !r.odate || !r.customer || !r.product) { skipped++; continue; }
        const ex = await env.DB.prepare('SELECT id,status FROM orders WHERE okey=?').bind(r.okey).first();
        if (ex) {
          // อัพเดตข้อมูลออเดอร์ได้ แต่ห้ามล้างสถานะ shipped ที่พนักงานทำไปแล้ว
          await env.DB.prepare(
            'UPDATE orders SET odate=?, ym=?, customer=?, receiver=?, product=?, qty=? WHERE okey=?'
          ).bind(r.odate, r.odate.slice(0, 7), r.customer, r.receiver || '', r.product, r.qty || 1, r.okey).run();
          updated++;
        } else {
          await env.DB.prepare(
            'INSERT INTO orders(ym,odate,customer,receiver,product,qty,okey) VALUES(?,?,?,?,?,?,?)'
          ).bind(r.odate.slice(0, 7), r.odate, r.customer, r.receiver || '', r.product, r.qty || 1, r.okey).run();
          added++;
        }
      }
      await env.DB.prepare('INSERT INTO audit(action,detail) VALUES(?,?)')
        .bind('import', `+${added} ~${updated} skip ${skipped}`).run();
      return J({ ok: true, added, updated, skipped });
    }

    /* ---- ทุก endpoint ที่เหลือ: PIN พนักงาน ---- */
    if (req.headers.get('x-pin') !== env.PIN) return J({ error: 'PIN ไม่ถูกต้อง' }, 401);

    if (path === '/sync' && req.method === 'POST') {
      // พนักงานกดได้ ปลอดภัย: อ่านชีตแบบ readonly เฉพาะคอลัมน์ที่ไม่ใช่เงิน แล้ว upsert ลง D1
      try { return J(await syncFromSheet(env, 3)); }
      catch (e) { return J({ error: String(e.message || e) }, 500); }
    }

    if (path === '/orders' && req.method === 'GET') {
      const d = url.searchParams.get('date') || '';
      const rows = await env.DB.prepare('SELECT * FROM orders WHERE odate=? ORDER BY id').bind(d).all();
      return J({ groups: groupRows(rows.results).map(({ _ids, ...g }) => g) });
    }

    if (path === '/pending' && req.method === 'GET') {
      const rows = await env.DB.prepare(
        "SELECT * FROM orders WHERE status='pending' ORDER BY odate, id"
      ).all();
      return J({ groups: groupRows(rows.results).filter(g => g.status === 'pending').map(({ _ids, ...g }) => g) });
    }

    if (path === '/parse-match' && req.method === 'POST') {
      const { text } = await req.json();
      const parsed = parseEmsText(text);
      if (!parsed.length) return J({ error: 'ไม่พบเลข tracking ในข้อความ (รูปแบบ EDxxxxxxxxxTH)' }, 400);
      // จับคู่กับ "ค้างส่งทั้งหมด" (รวมวันก่อน ๆ ที่เพิ่งพร้อมส่งวันนี้)
      const rows = await env.DB.prepare("SELECT * FROM orders WHERE status='pending' ORDER BY odate, id").all();
      const groups = groupRows(rows.results);
      const usedGid = new Set();
      const results = parsed.map(p => {
        // เลขซ้ำในลิสต์เดียวกัน / เลขที่เคยบันทึกแล้ว
        const r = matchOne(p.ems_name, groups.filter(g => !usedGid.has(g.gid)));
        if (r.match) usedGid.add(r.match.gid);
        const strip = g => g && { gid: g.gid, odate: g.odate, customer: g.customer, receiver: g.receiver, items: g.items };
        return {
          tracking: p.tracking,
          ems_name: p.ems_name,
          reason: r.reason,
          match: strip(r.match),
          candidates: r.candidates.slice(0, 6).map(strip),
        };
      });
      // เช็คว่าเลขไหนเคยใช้ไปแล้ว
      for (const res of results) {
        const dup = await env.DB.prepare('SELECT customer FROM orders WHERE tracking=? LIMIT 1').bind(res.tracking).first();
        if (dup) { res.reason = 'already_used'; res.match = null; res.used_by = dup.customer; }
      }
      return J({ results, pending_count: groups.filter(g => g.status === 'pending').length });
    }

    if (path === '/confirm' && req.method === 'POST') {
      const { assigns = [], orphans = [] } = await req.json();
      let ok = 0;
      for (const a of assigns) {
        const r = await setGroupTracking(env, a.gid, a.tracking, a.auto ? 'match_auto' : 'match_manual');
        if (r.ok) ok++;
      }
      for (const o of orphans) {
        await env.DB.prepare('INSERT INTO orphans(tracking,ems_name,status,note) VALUES(?,?,?,?)')
          .bind(o.tracking, o.ems_name || '', o.action === 'archive' ? 'archived' : 'open',
                o.action === 'archive' ? 'ตัดทิ้ง (ของที่ส่งไปก่อนเริ่มระบบ)' : '').run();
        await env.DB.prepare('INSERT INTO audit(action,detail) VALUES(?,?)')
          .bind(o.action === 'archive' ? 'orphan_archive' : 'orphan_keep', `${o.tracking} ${o.ems_name || ''}`).run();
      }
      return J({ ok: true, saved: ok, orphaned: orphans.length });
    }

    if (path === '/assign' && req.method === 'POST') {
      const { tracking, gid, orphan_id } = await req.json();
      if (!tracking || !gid) return J({ error: 'ข้อมูลไม่ครบ' }, 400);
      const r = await setGroupTracking(env, gid, tracking, 'match_manual');
      if (r.error) return J(r, 400);
      if (orphan_id) await env.DB.prepare("UPDATE orphans SET status='archived', note='จับคู่แล้ว' WHERE id=?").bind(orphan_id).run();
      return J(r);
    }

    if (path === '/unassign' && req.method === 'POST') {
      const { gid } = await req.json();
      return J(await setGroupTracking(env, gid, '', 'unassign'));
    }

    if (path === '/orphans' && req.method === 'GET') {
      const rows = await env.DB.prepare("SELECT * FROM orphans WHERE status='open' ORDER BY id DESC").all();
      return J({ orphans: rows.results });
    }

    if (path === '/orphan-archive' && req.method === 'POST') {
      const { id } = await req.json();
      await env.DB.prepare("UPDATE orphans SET status='archived', note='ตัดทิ้ง' WHERE id=?").bind(id).run();
      return J({ ok: true });
    }

    return J({ error: 'not found' }, 404);
  },
};
