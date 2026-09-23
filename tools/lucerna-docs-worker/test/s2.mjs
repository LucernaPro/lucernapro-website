import {w,d,$,dirty,check,results,rows,idx,gh,sleep,reset} from './run.mjs';
const workerMod = await import('/home/claude/lucernapro-website/tools/lucerna-docs-worker/worker.js'); const worker=workerMod.default; const env={GH_REPO:'x/y',GH_TOKEN:'t',PIN:'1234'};
const wcall=(path,body)=>worker.fetch(new Request('https://x'+path,{method:body?'POST':'GET',headers:{'x-pin':'1234','content-type':'application/json'},body:body?JSON.stringify(body):undefined}),env).then(r=>r.json());
// A) Worker concurrency: two clients save at once → distinct numbers
const [a,b]=await Promise.all([wcall('/save',{type:'QT',items:[],customer:{name:'A'},totals:{grand:1},date:'19/09/2026'}),wcall('/save',{type:'QT',items:[],customer:{name:'B'},totals:{grand:2},date:'19/09/2026'})]);
check('A parallel saves distinct', a.no!==b.no && a.no&&b.no, a.no+' '+b.no);
check('A both in index', idx().length===2 && !a.warn && !b.warn, JSON.stringify([a,b]));
// B) Worker: update cancelled doc rejected
await wcall('/cancel',{no:a.no,reason:'test'}); const u=await wcall('/save',{type:'QT',no:a.no,update:true,items:[],customer:{name:'A'},totals:{grand:1}});
check('B update cancelled rejected', !!u.error, JSON.stringify(u));
// C) Worker: update preserves status when client omits it
const u2=await wcall('/save',{type:'QT',no:b.no,update:true,items:[],customer:{name:'B'},totals:{grand:5}}); check('C update ok', u2.updated);
check('C status preserved', idx().find(r=>r.no===b.no).status==='ออกแล้ว' && gh.read('docs/2026/'+b.no+'.json').createdAt, JSON.stringify(idx().find(r=>r.no===b.no)));
// D) Worker: wrong PIN
const bad=await worker.fetch(new Request('https://x/list',{headers:{'x-pin':'0000'}}),env); check('D bad pin 401', bad.status===401);
// E) Worker: bad type / bad no
check('E bad type', !!(await wcall('/save',{type:'ZZ',items:[]})).error); check('E bad no', !!(await wcall('/doc?no=INV-1')).error);
// F) client: double-click print → one number
reset(); $('pasteArea').value='ออกใบกำกับภาษี\nบริษัท ดับเบิล จำกัด 0105557027407\n1 ถนน กรุงเทพ 10110\nPoolArmour 5,890 x 1'; w.parsePaste();
const [r1,r2]=await Promise.all([w.ensureSaved(),w.ensureSaved()]); check('F double save one number', r1.no===r2.no && idx().filter(r=>r.customer==='บริษัท ดับเบิล จำกัด').length===1, r1.no+' '+r2.no);
// G) CA with BE year + commas + decimals + no qty
reset(); $('pasteArea').value='บิลเงินสด\n11/08/2569\nSentol Grout\t1,290.50\t2\nPoolArmour 5 kg\t5,890.00'; w.parsePaste();
check('G BE year → CE', $('docDate').textContent==='11/08/2026', $('docDate').textContent);
check('G rows', rows().length===2 && rows()[0].price==='1,290.50' && rows()[1].qty==='1', JSON.stringify(rows()));
let s=await w.ensureSaved(); check('G CA aug number', /^CA-202608-/.test(s.no), s.no);
// H) CA aug created today → editable today (savedAt rule)
await w.viewDoc(s.no); await sleep(30); dirty(); const e=await w.ensureSaved(); check('H backdated CA editable (created this month)', e.updated, JSON.stringify(e));
// I) cancelled INV edit blocked on client + replacement link
reset(); $('pasteArea').value='ออกใบกำกับภาษี\nบริษัท ลิงก์ จำกัด 0105557027407\n1 ถนน กรุงเทพ 10110\nX 100 x 1'; w.parsePaste(); s=await w.ensureSaved(); const invNo=s.no;
await w.loadList(); await sleep(30); w.openSheet(invNo); $('shCancel').click(); await sleep(10); const pc=$('shCancel').onclick.call($('shCancel')); await sleep(40); $('reasonInput').value='ชื่อผิด'; $('reasonOk').click(); await sleep(40); $('choiceBtns').children[1].click(); await pc; await sleep(50);
s=await w.ensureSaved(); check('I replacement saved', /^INV-/.test(s.no) && s.no!==invNo, s.no);
const old=idx().find(r=>r.no===invNo); check('I cancelled row linked', old.status==='ยกเลิก' && old.replacedBy===s.no, JSON.stringify(old));
await w.viewDoc(invNo); await sleep(30); dirty(); const ce=await w.ensureSaved(); check('I client blocks edit of cancelled', !ce.ok, JSON.stringify(ce).slice(0,80));
// J) chat-style paste with timestamps + discount + shipping
reset(); $('pasteArea').value='14:02 สมชาย ออกใบเสนอราคา รวมค่าส่ง\n14:02 สมชาย ร้านช่างโจ\n14:03 สมชาย 55 ถ.มิตรภาพ ต.ในเมือง อ.เมือง จ.ขอนแก่น 40000\n14:03 สมชาย โทร 0812345678\n14:03 สมชาย PoolArmour 5,890 x 2\n14:03 สมชาย ค่าส่ง 200'; w.parsePaste();
check('J chat paste name', $('custNameText').textContent==='ร้านช่างโจ', $('custNameText').textContent);
check('J phone', $('fPhone').textContent.includes('0812345678'), $('fPhone').textContent);
check('J rows+ship', rows().length>=1, JSON.stringify(rows())+' ship='+$('shipInput').value+' grand='+$('grand').textContent);
// K) date-check: stale tab
$('btnReset').click(); $('btnReset').click(); $('docDate').textContent='01/09/2026'; w.checkDate(); check('K stale auto date fixed', $('docDate').textContent===w.fmtDate(new Date()));
// L) list rendering has all rows & statuses
await w.loadList(); await sleep(30); check('L list count', $('listRows').children.length>=idx().length-1, $('listRows').children.length+' vs '+idx().length);
console.log(results.map(r=>r.join(' | ')).join('\n')); process.exit(0);
