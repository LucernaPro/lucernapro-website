import {w,d,$,dirty,check,results,rows,idx,gh,sleep,reset} from './run.mjs';
// ---- S1: QT basic → number, update, rename ----
$('pasteArea').value='ออกใบเสนอราคา\nบริษัท ทดสอบ จำกัด\n1 ถนนสุขุมวิท กรุงเทพ 10110\nPoolArmour 5,890 x 2\nCorePrimer 2,990 x 1'; w.parsePaste();
let s=await w.ensureSaved(); check('S1 QT number', s.no==='QT-202609-0001', s.no);
check('S1 stored doc', !!gh.read('docs/2026/QT-202609-0001.json'));
dirty(); s=await w.ensureSaved(); check('S1 same-customer edit → update', s.no==='QT-202609-0001' && s.updated, JSON.stringify(s));
check('S1 index single row', idx().length===1, idx().length);
// rename → new doc
$('custNameText').textContent='บริษัท อื่น จำกัด'; dirty(); const p=w.ensureSaved(); await sleep(50); $('choiceBtns').children[1].click(); s=await p;
check('S1 rename→new number', s.no==='QT-202609-0002', s.no);
// ---- S2: INV blocked print when Worker fails ----
reset(); $('pasteArea').value='ออกใบกำกับภาษี\nบริษัท บี-เทค กรุ๊ป จำกัด\nเลขประจำตัวผู้เสียภาษีอากร\n0-1055-57027-40-7\n98/40 ถนนโพธิ์แก้ว แขวงนวมินทร์ เขตบึงกุ่ม กรุงเทพฯ 10240\nโทร. 02-509-1061\nPoolArmour 5,890 x 1'; w.parsePaste();
check('S2 tax parsed', $('fTax').textContent.includes('0105557027407'), $('fTax').textContent);
gh.injectFail(401); s=await w.ensureSaved(); check('S2 INV save fails → blocked', !s.ok && w.outputBlocked(s), JSON.stringify(s));
check('S2 docNo still XXXX', $('docNo').textContent.includes('XXXX'), $('docNo').textContent);
s=await w.ensureSaved(); check('S2 retry ok', s.no==='INV-202609-0001', JSON.stringify(s));
// ---- S3: INV edit same month allowed; cancel with reason; replacement ----
dirty(); s=await w.ensureSaved(); check('S3 INV edit in-place (same month)', s.updated && s.no==='INV-202609-0001', JSON.stringify(s));
await w.loadList(); await sleep(30); w.openSheet('INV-202609-0001');
$('shCancel').click(); await sleep(10); const pc=$('shCancel').onclick.call($('shCancel')); await sleep(40); $('reasonInput').value='ยอดผิด'; $('reasonOk').click(); await sleep(40); $('choiceBtns').children[1].click(); await pc; await sleep(50);
const cdoc=gh.read('docs/2026/INV-202609-0001.json'); check('S3 cancelled + reason stored', cdoc.status==='ยกเลิก' && cdoc.cancelReason==='ยอดผิด', JSON.stringify([cdoc.status,cdoc.cancelReason]));
check('S3 index reason', idx().find(r=>r.no==='INV-202609-0001').reason==='ยอดผิด');
check('S3 replacement opened', $('refV').textContent.includes('INV-202609-0001') && $('docNo').textContent.includes('XXXX'), $('refV').textContent);
s=await w.ensureSaved(); check('S3 replacement number', s.no==='INV-202609-0002', s.no);
check('S3 old INV marked แปลงเป็น?', idx().find(r=>r.no==='INV-202609-0001').status, idx().find(r=>r.no==='INV-202609-0001').status);
// ---- S4: CA backdated ----
reset(); $('pasteArea').value='บิลเงินสด\n11/08/2026\nกันซึมใส Lucerna Crystal Seal\t1 kg\t780.00\t1'; w.parsePaste();
s=await w.ensureSaved(); check('S4 CA aug number', s.no==='CA-202608-0001', s.no);
check('S4 CA file in 2026 folder', !!gh.read('docs/2026/CA-202608-0001.json'));
reset(); $('pasteArea').value='บิลเงินสด\n12/08/2026\nSentol Grout 590 x 2'; w.parsePaste(); s=await w.ensureSaved(); check('S4 CA aug #2', s.no==='CA-202608-0002', s.no);
reset(); $('pasteArea').value='บิลเงินสด\nSilicone Pro 5 kg   2,040.00   1'; w.parsePaste(); s=await w.ensureSaved(); check('S4 CA sep (today) #1', s.no==='CA-202609-0001', s.no);
// CA edit: doc is CA-202608 (aug) → after Sep 15 locked
await w.viewDoc('CA-202608-0001'); await sleep(30); dirty(); s=await w.ensureSaved(); check('S4 CA aug edit allowed (created this month)', s.updated, JSON.stringify(s).slice(0,80));
await w.viewDoc('CA-202609-0001'); await sleep(30); dirty(); s=await w.ensureSaved(); check('S4 CA sep edit ok', s.updated, JSON.stringify(s));
check('S4 CA getDoc works', (gh.read('docs/2026/CA-202609-0001.json')||{}).type==='CA');
// ---- S5: convert QT→INV ----
await w.convertDoc('QT-202609-0002','INV'); await sleep(30); check('S5 convert date today', $('docDate').textContent===w.fmtDate(new Date()), $('docDate').textContent);
s=await w.ensureSaved(); check('S5 converted number', s.no==='INV-202609-0003', s.no);
check('S5 QT marked converted', idx().find(r=>r.no==='QT-202609-0002').status.startsWith('แปลงเป็น'), idx().find(r=>r.no==='QT-202609-0002').status);
// ---- S6: cancel QT no reason ----
await w.loadList(); await sleep(30); w.openSheet('QT-202609-0001'); $('shCancel').click(); await sleep(10); await $('shCancel').onclick.call($('shCancel')); await sleep(30);
check('S6 QT cancelled', idx().find(r=>r.no==='QT-202609-0001').status==='ยกเลิก');
// ---- S7: reprint cancelled? viewDoc cancelled INV then print should not update ----
await w.viewDoc('INV-202609-0001'); await sleep(30); s=await w.ensureSaved(); check('S7 reprint cancelled INV w/o edit → no save', s.ok && s.no==='INV-202609-0001', JSON.stringify(s));
dirty(); s=await w.ensureSaved(); check('S7 edit cancelled INV → should be blocked', !s.ok, JSON.stringify(s).slice(0,90));
console.log(results.map(r=>r.join(' | ')).join('\n')); process.exit(0);
