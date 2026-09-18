var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });

// worker.js — Lucerna Docs (ออกเลข + เก็บเอกสารใน GitHub repo GH_REPO)
// ชนิดเอกสาร: QT ใบเสนอราคา / BL ใบวางบิล / INV ใบกำกับภาษี / CA ใบกำกับภาษีอย่างย่อ (บิลเงินสด Shopee-Lazada)
var TYPES = ["QT", "BL", "INV", "CA"];
var NO_RE = /^(QT|BL|INV|CA)-(\d{4})(\d{2})-\d{4}$/;
var CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  "Access-Control-Allow-Headers": "content-type,x-pin"
};
var J = /* @__PURE__ */ __name((obj, status = 200) => new Response(JSON.stringify(obj), { status, headers: { "content-type": "application/json", ...CORS } }), "J");
var worker_default = {
  async fetch(req, env) {
    if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
    if (req.headers.get("x-pin") !== env.PIN) return J({ error: "PIN \u0E44\u0E21\u0E48\u0E16\u0E39\u0E01\u0E15\u0E49\u0E2D\u0E07" }, 401);
    const url = new URL(req.url);
    try {
      if (req.method === "POST" && url.pathname === "/save") return await save(req, env);
      if (req.method === "POST" && url.pathname === "/cancel") return await cancel(req, env);
      if (req.method === "GET" && url.pathname === "/list") return await list(env);
      if (req.method === "GET" && url.pathname === "/doc") return await getDoc(url.searchParams.get("no"), env);
      return J({ error: "\u0E44\u0E21\u0E48\u0E23\u0E39\u0E49\u0E08\u0E31\u0E01 endpoint" }, 404);
    } catch (e) {
      return J({ error: e.message }, 500);
    }
  }
};
function gh(env, path, init = {}) {
  return fetch(`https://api.github.com/repos/${env.GH_REPO}/contents/${path}`, {
    ...init,
    headers: {
      "Authorization": `Bearer ${env.GH_TOKEN}`,
      "Accept": "application/vnd.github+json",
      "User-Agent": "lucerna-docs-worker",
      ...init.headers || {}
    }
  });
}
__name(gh, "gh");
var b64enc = /* @__PURE__ */ __name((s) => btoa(String.fromCharCode(...new TextEncoder().encode(s))), "b64enc");
var b64dec = /* @__PURE__ */ __name((s) => new TextDecoder().decode(Uint8Array.from(atob(s), (c) => c.charCodeAt(0))), "b64dec");
async function readFile(env, path) {
  const r = await gh(env, path);
  if (r.status === 404) return null;
  if (!r.ok) throw new Error("\u0E2D\u0E48\u0E32\u0E19 " + path + " \u0E44\u0E21\u0E48\u0E44\u0E14\u0E49 (" + r.status + ")");
  const j = await r.json();
  return { sha: j.sha, text: b64dec(j.content.replace(/\n/g, "")) };
}
__name(readFile, "readFile");
async function save(req, env) {
  const d = await req.json();
  if (!d || !d.type || !Array.isArray(d.items)) return J({ error: "\u0E02\u0E49\u0E2D\u0E21\u0E39\u0E25\u0E40\u0E2D\u0E01\u0E2A\u0E32\u0E23\u0E44\u0E21\u0E48\u0E04\u0E23\u0E1A" }, 400);
  const TYPE = String(d.type).toUpperCase();
  if (!TYPES.includes(TYPE)) return J({ error: "\u0E1B\u0E23\u0E30\u0E40\u0E20\u0E17\u0E40\u0E2D\u0E01\u0E2A\u0E32\u0E23\u0E44\u0E21\u0E48\u0E16\u0E39\u0E01\u0E15\u0E49\u0E2D\u0E07" }, 400);
  const now = /* @__PURE__ */ new Date();
  let ym = now.getFullYear() + String(now.getMonth() + 1).padStart(2, "0");
  // CA (บิลเงินสด) คีย์ย้อนหลังได้ → เลขชุดตามเดือนของ "วันที่ในใบ" (dd/mm/yyyy) ไม่ใช่เดือนที่คีย์; QT/BL/INV ยังตามเดือนที่คีย์เหมือนเดิม
  if (TYPE === "CA") {
    const dm = String(d.date || "").match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
    if (dm) ym = dm[3] + dm[2].padStart(2, "0");
  }
  if (d.update) {
    const m = String(d.no || "").match(NO_RE);
    if (m) {
      const path = `docs/${m[2]}/${d.no}.json`;
      const cur = await readFile(env, path);
      if (cur) {
        d.savedAt = now.toISOString();
        const r = await gh(env, path, {
          method: "PUT",
          body: JSON.stringify({ message: "update " + d.no, sha: cur.sha, content: b64enc(JSON.stringify(d, null, 1)) })
        });
        if (!r.ok) return J({ error: "\u0E2D\u0E31\u0E1E\u0E40\u0E14\u0E15\u0E44\u0E1F\u0E25\u0E4C\u0E44\u0E21\u0E48\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08 (" + r.status + ")" }, 502);
        for (let a = 0; a < 4; a++) {
          const idx2 = await readFile(env, "index.json");
          const rows2 = idx2 ? JSON.parse(idx2.text) : [];
          const i = rows2.findIndex((r2) => r2.no === d.no);
          const e2 = {
            no: d.no,
            type: m[1],
            date: d.date || "",
            customer: d.customer && d.customer.name || "",
            grand: d.totals && d.totals.grand || 0,
            status: d.status || "\u0E2D\u0E2D\u0E01\u0E41\u0E25\u0E49\u0E27",
            ref: d.ref || "",
            savedAt: d.savedAt
          };
          if (i >= 0) rows2[i] = e2;
          else rows2.push(e2);
          const body2 = { message: "index update " + d.no, content: b64enc(JSON.stringify(rows2, null, 1)) };
          if (idx2) body2.sha = idx2.sha;
          const r2r = await gh(env, "index.json", { method: "PUT", body: JSON.stringify(body2) });
          if (r2r.ok) return J({ no: d.no, updated: true });
          if (r2r.status !== 409 && r2r.status !== 422) break;
        }
        return J({ no: d.no, updated: true, warn: "\u0E2D\u0E31\u0E1E\u0E40\u0E14\u0E15\u0E43\u0E1A\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08 \u0E41\u0E15\u0E48\u0E2A\u0E32\u0E23\u0E1A\u0E31\u0E0D\u0E2D\u0E31\u0E1E\u0E40\u0E14\u0E15\u0E44\u0E21\u0E48\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08" });
      }
    }
  }
  const idx = await readFile(env, "index.json");
  const rows = idx ? JSON.parse(idx.text) : [];
  const prefix = `${TYPE}-${ym}-`;
  let seq = rows.filter((r) => (r.no || "").startsWith(prefix)).reduce((m, r) => Math.max(m, parseInt(r.no.slice(prefix.length), 10) || 0), 0) + 1;
  let docNo = null, docPath = null;
  for (let attempt = 0; attempt < 15 && !docNo; attempt++) {
    const no = prefix + String(seq).padStart(4, "0");
    const path = `docs/${ym.slice(0, 4)}/${no}.json`;
    d.no = no;
    d.savedAt = now.toISOString();
    const r = await gh(env, path, {
      method: "PUT",
      body: JSON.stringify({ message: "save " + no, content: b64enc(JSON.stringify(d, null, 1)) })
    });
    if (r.status === 201) {
      docNo = no;
      docPath = path;
      break;
    } else if (r.status === 422) {
      seq++;
    } else if (r.status === 409) {
      await new Promise((x) => setTimeout(x, 250 + Math.random() * 350));
    } else return J({ error: "\u0E1A\u0E31\u0E19\u0E17\u0E36\u0E01\u0E44\u0E1F\u0E25\u0E4C\u0E44\u0E21\u0E48\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08 (" + r.status + ")" }, 502);
  }
  if (!docNo) return J({ error: "\u0E2D\u0E2D\u0E01\u0E40\u0E25\u0E02\u0E44\u0E21\u0E48\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08 \u0E25\u0E2D\u0E07\u0E43\u0E2B\u0E21\u0E48\u0E2D\u0E35\u0E01\u0E04\u0E23\u0E31\u0E49\u0E07" }, 503);
  const entry = {
    no: docNo,
    type: TYPE,
    date: d.date || "",
    customer: d.customer && d.customer.name || "",
    grand: d.totals && d.totals.grand || 0,
    status: d.status || "\u0E2D\u0E2D\u0E01\u0E41\u0E25\u0E49\u0E27",
    ref: d.ref || "",
    savedAt: d.savedAt
  };
  for (let attempt = 0; attempt < 4; attempt++) {
    const cur = await readFile(env, "index.json");
    const curRows = cur ? JSON.parse(cur.text) : [];
    curRows.push(entry);
    if (d.ref) {
      const ri = curRows.findIndex((r2) => r2.no === d.ref);
      if (ri >= 0) curRows[ri].status = "\u0E41\u0E1B\u0E25\u0E07\u0E40\u0E1B\u0E47\u0E19 " + docNo;
    }
    const body = { message: "index " + docNo, content: b64enc(JSON.stringify(curRows, null, 1)) };
    if (cur) body.sha = cur.sha;
    const r = await gh(env, "index.json", { method: "PUT", body: JSON.stringify(body) });
    if (r.ok) return J({ no: docNo, path: docPath });
    if (r.status !== 409 && r.status !== 422) break;
  }
  return J({ no: docNo, path: docPath, warn: "\u0E1A\u0E31\u0E19\u0E17\u0E36\u0E01\u0E43\u0E1A\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08 \u0E41\u0E15\u0E48\u0E2A\u0E32\u0E23\u0E1A\u0E31\u0E0D\u0E2D\u0E31\u0E1E\u0E40\u0E14\u0E15\u0E44\u0E21\u0E48\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08" });
}
__name(save, "save");
async function cancel(req, env) {
  const b = await req.json();
  const m = String(b.no || "").match(NO_RE);
  if (!m) return J({ error: "\u0E40\u0E25\u0E02\u0E40\u0E2D\u0E01\u0E2A\u0E32\u0E23\u0E44\u0E21\u0E48\u0E16\u0E39\u0E01\u0E15\u0E49\u0E2D\u0E07" }, 400);
  const path = `docs/${m[2]}/${b.no}.json`;
  const cur = await readFile(env, path);
  if (!cur) return J({ error: "\u0E44\u0E21\u0E48\u0E1E\u0E1A\u0E40\u0E2D\u0E01\u0E2A\u0E32\u0E23 " + b.no }, 404);
  const d = JSON.parse(cur.text);
  d.status = "\u0E22\u0E01\u0E40\u0E25\u0E34\u0E01";
  d.cancelledAt = (/* @__PURE__ */ new Date()).toISOString();
  if (b.reason) d.cancelReason = String(b.reason).slice(0, 300); // เหตุผลที่ยกเลิก (ใบกำกับภาษีต้องเก็บไว้)
  const r = await gh(env, path, {
    method: "PUT",
    body: JSON.stringify({ message: "cancel " + b.no, sha: cur.sha, content: b64enc(JSON.stringify(d, null, 1)) })
  });
  if (!r.ok) return J({ error: "\u0E22\u0E01\u0E40\u0E25\u0E34\u0E01\u0E44\u0E21\u0E48\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08 (" + r.status + ")" }, 502);
  for (let a = 0; a < 4; a++) {
    const idx = await readFile(env, "index.json");
    const rows = idx ? JSON.parse(idx.text) : [];
    const i = rows.findIndex((x) => x.no === b.no);
    if (i >= 0) { rows[i].status = "\u0E22\u0E01\u0E40\u0E25\u0E34\u0E01"; if (d.cancelReason) rows[i].reason = d.cancelReason; }
    const body = { message: "index cancel " + b.no, content: b64enc(JSON.stringify(rows, null, 1)) };
    if (idx) body.sha = idx.sha;
    const r2 = await gh(env, "index.json", { method: "PUT", body: JSON.stringify(body) });
    if (r2.ok) return J({ no: b.no, cancelled: true });
    if (r2.status !== 409 && r2.status !== 422) break;
  }
  return J({ no: b.no, cancelled: true, warn: "\u0E22\u0E01\u0E40\u0E25\u0E34\u0E01\u0E43\u0E1A\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08 \u0E41\u0E15\u0E48\u0E2A\u0E32\u0E23\u0E1A\u0E31\u0E0D\u0E2D\u0E31\u0E1E\u0E40\u0E14\u0E15\u0E44\u0E21\u0E48\u0E2A\u0E33\u0E40\u0E23\u0E47\u0E08" });
}
__name(cancel, "cancel");
async function list(env) {
  const idx = await readFile(env, "index.json");
  return J(idx ? JSON.parse(idx.text) : []);
}
__name(list, "list");
async function getDoc(no, env) {
  const m = (no || "").match(NO_RE);
  if (!m) return J({ error: "\u0E40\u0E25\u0E02\u0E40\u0E2D\u0E01\u0E2A\u0E32\u0E23\u0E44\u0E21\u0E48\u0E16\u0E39\u0E01\u0E15\u0E49\u0E2D\u0E07" }, 400);
  const f = await readFile(env, `docs/${m[2]}/${no}.json`);
  if (!f) return J({ error: "\u0E44\u0E21\u0E48\u0E1E\u0E1A\u0E40\u0E2D\u0E01\u0E2A\u0E32\u0E23 " + no }, 404);
  return J(JSON.parse(f.text));
}
__name(getDoc, "getDoc");
export {
  worker_default as default
};
