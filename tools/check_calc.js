/* tools/check_calc.js — ตัวตรวจ runtime ของเครื่องคำนวณ (คู่กับ tools/check_parity.py)
 *
 * ทำไมต้องมี: check_parity.py ตรวจ HTML แบบ static เท่านั้น จับ ReferenceError ใน calc.js ไม่ได้
 * (บั๊ก shipSum ไม่ประกาศ 3 ส.ค. 2026 ทำเครื่องคำนวณตายเงียบทั้ง 45 หน้า — เจ้าของเจอก่อนตัวตรวจ)
 *
 * วิธีรัน:  cd repo && npm i jsdom --no-save && node tools/check_calc.js   (exit 1 = มีปัญหา)
 *
 * ตรวจ 2 ชั้น:
 *  1) smoke ทุกหน้าที่มี data-calc: โหลดหน้า + รัน calc.js + กรอกพื้นที่ → ต้องได้ยอดรวมหรือข้อความ "ใหญ่เกินตาราง"
 *  2) เคสค่าคงที่ที่เจ้าของเคยยืนยันเอง — ยอดรวมต้องตรงเป๊ะ (กันพฤติกรรมเพี้ยนเงียบๆ ตอนแก้อัลกอริทึม)
 */
'use strict';
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const calcSrc = fs.readFileSync(path.join(ROOT, 'calc.js'), 'utf8');

function load(file, area) {
  const dom = new JSDOM(fs.readFileSync(file, 'utf8'), { runScripts: 'outside-only' });
  const w = dom.window;
  w.eval(calcSrc); // โยน error = fail ทันที
  const A = w.document.getElementById('lcA');
  if (!A) return { err: 'กล่องคำนวณไม่ขึ้น' };
  A.value = String(area);
  A.dispatchEvent(new w.Event('input', { bubbles: true }));
  const out = w.document.getElementById('lcOut');
  const tot = out.querySelector('.tot .o');
  return {
    total: tot ? tot.textContent.replace(/[^0-9,]/g, '') : null,
    big: /ทักมาขอใบเสนอราคา|message us for a quote/.test(out.innerHTML),
    note: /คิดเต็มทุกถัง|charged in full/.test(out.innerHTML),
  };
}

let fails = 0;
const bad = (f, msg) => { console.log('  ✗ ' + f.replace(ROOT + '/', '') + ' — ' + msg); fails++; };

/* ชั้น 1: smoke ทุกหน้า */
const pages = execSync(`grep -rl 'data-calc="1"' --include=index.html ${ROOT}`)
  .toString().trim().split('\n').filter(Boolean);
for (const f of pages) {
  try {
    const r = load(f, 12);
    if (r.err) bad(f, r.err);
    else if (!r.total && !r.big) bad(f, 'กรอกพื้นที่แล้วไม่มีผลลัพธ์');
  } catch (e) { bad(f, e.constructor.name + ': ' + e.message); }
}

/* ชั้น 2: เคสค่าคงที่ (เจ้าของยืนยัน 3 ส.ค. 2026 + มติค่าส่งต่อชิ้น)
 * ⚠️ ถ้าราคา/พื้นที่บนหน้าเว็บเปลี่ยน ต้องอัปเดตเคสตรงนี้พร้อมกัน — ห้ามลบทิ้งเฉยๆ */
const KNOWN = [
  { f: 'tilecoatpoly/index.html',    area: 7,  total: '2,890',  note: false }, // 1.5kg + ส่ง 130
  { f: 'crystalseal/index.html',     area: 33, total: '4,560',  note: true  }, // 5kg+1kg×2 + ส่ง 270
  { f: 'tilecoatpoly/index.html',    area: 40, total: '16,320', note: true  }, // 1kg×8 + ส่งต่อชิ้น 130×8
  { f: 'en/tilecoatpoly/index.html', area: 7,  total: '2,890',  note: false },
  { f: 'thermaglaze/index.html',     area: 80, total: '4,980',  note: true  }, // แบบสี 15kg+1kg = 4,610 + ส่ง 300+70 (มติ 3 ส.ค.)
  { f: 'boundgravel/index.html',     area: 10, total: '2,410',  note: false }, // 5kg = 2,280 + ส่ง 130 ทุกขนาด (มติ 3 ส.ค.)
];
for (const k of KNOWN) {
  const f = path.join(ROOT, k.f);
  try {
    const r = load(f, k.area);
    if (r.total !== k.total) bad(f, `พื้นที่ ${k.area}: ยอดรวม ${r.total} ≠ ${k.total} ที่ยืนยันไว้`);
    if (r.note !== k.note) bad(f, `พื้นที่ ${k.area}: โน้ตค่าส่ง ${r.note} ≠ ${k.note}`);
  } catch (e) { bad(f, e.message); }
}

console.log(fails === 0
  ? `ผ่านครบ ${pages.length} หน้า + เคสค่าคงที่ ${KNOWN.length} เคส`
  : `\nพบปัญหา ${fails} จุด`);
process.exit(fails ? 1 : 0);
