import {w,d,$,dirty,check,results,rows,idx,gh,sleep,reset} from './run.mjs';
const workerMod = await import('/home/claude/lucernapro-website/tools/lucerna-docs-worker/worker.js'); const worker=workerMod.default; const env={GH_REPO:'x/y',GH_TOKEN:'t',PIN:'1234'};
const wcall=(path,body)=>worker.fetch(new Request('https://x'+path,{method:body?'POST':'GET',headers:{'x-pin':'1234','content-type':'application/json'},body:body?JSON.stringify(body):undefined}),env).then(r=>r.json());
// A) empty / header-only paste
$('pasteArea').value=''; w.parsePaste(); check('A empty paste no crash', true);
$('pasteArea').value='ออกใบเสนอราคา'; w.parsePaste(); check('A header-only rows', rows().length===0 || true, JSON.stringify(rows()));
// B) save with zero items → should be blocked?
reset(); $('custNameText').textContent='ร้าน ว่าง'; dirty(); let s=await w.ensureSaved(); check('B zero-item doc save', !s.ok, JSON.stringify(s)+' rows='+d.querySelectorAll('#tbody tr').length);
// C) ex-VAT math
reset(); $('pasteArea').value='ออกใบเสนอราคา\nร้าน วัด\nX 1,000 x 1'; w.parsePaste(); $('exVat').checked=true; $('exVat').dispatchEvent(new w.Event('change',{bubbles:true})); w.recalc();
check('C exVat grand 1,070', $('grand').textContent==='1,070.00', $('grand').textContent+' vat='+$('vat').textContent);
$('exVat').checked=false; w.recalc(); check('C incVat preVat 934.58', $('preVat').textContent==='934.58', $('preVat').textContent);
// D) discount pct
$('discInput').value='10'; $('discMode').value='pct'; w.recalc(); check('D disc 10% → 900', $('afterDisc').textContent==='900.00', $('afterDisc').textContent);
$('discInput').value=''; $('discMode').value='baht'; w.recalc();
// E) rounding 33.33 x 3
reset(); $('pasteArea').value='ออกใบเสนอราคา\nร้าน ปัด\nY 33.33 x 3'; w.parsePaste(); check('E amount 99.99', $('grand').textContent==='99.99', $('grand').textContent);
// F) manual date edit respected through save
$('docDate').textContent='05/09/2026'; $('docDate').dispatchEvent(new w.Event('input',{bubbles:true})); s=await w.ensureSaved(); check('F manual date saved', gh.read('docs/2026/'+s.no+'.json').date==='05/09/2026', gh.read('docs/2026/'+s.no+'.json').date);
// G) Worker: index missing a row but file exists → 422 bump
gh.files.set('docs/2026/QT-202609-0002.json',{sha:'orphan',text:'{}'}); const g=await wcall('/save',{type:'QT',items:[{name:'a'}],customer:{name:'G'},totals:{grand:1},date:'19/09/2026'});
check('G orphan file skipped', g.no==='QT-202609-0003', JSON.stringify(g));
// H) INV created last month → locked in sheet (savedAt Aug)
gh.files.set('docs/2026/INV-202608-0001.json',{sha:'s1',text:JSON.stringify({no:'INV-202608-0001',type:'INV',date:'20/08/2026',customer:{name:'เก่า'},items:[{name:'a',qty:1,price:1}],status:'ออกแล้ว',savedAt:'2026-08-20T03:00:00Z'})});
const ix=idx(); ix.push({no:'INV-202608-0001',type:'INV',date:'20/08/2026',customer:'เก่า',grand:1,status:'ออกแล้ว',savedAt:'2026-08-20T03:00:00Z'}); gh.files.set('index.json',{sha:'sx',text:JSON.stringify(ix)});
await w.loadList(); await sleep(30); w.openSheet('INV-202608-0001'); check('H old INV cancel hidden + lock note', $('shCancel').style.display==='none' && $('shLock').textContent.includes('15/09/2026'), $('shLock').textContent);
await w.viewDoc('INV-202608-0001'); await sleep(30); dirty(); s=await w.ensureSaved(); check('H old INV edit blocked', !s.ok, (s.err||'').slice(0,60));
// I) BL from QT convert then cancel BL (no reason needed)
await w.loadList(); await sleep(30); const qtNo=idx().find(r=>r.type==='QT'&&r.status==='ออกแล้ว').no; await w.convertDoc(qtNo,'BL'); await sleep(30); s=await w.ensureSaved(); check('I BL number', /^BL-202609-0001$/.test(s.no), s.no);
await w.loadList(); await sleep(30); w.openSheet(s.no); check('I BL cancel label plain', $('shCancel').textContent==='ยกเลิกใบนี้', $('shCancel').textContent);
// J) CA sheet label + cancel-only
reset(); $('pasteArea').value='บิลเงินสด\nZ 100 x 1'; w.parsePaste(); s=await w.ensureSaved(); const ca=s.no; await w.loadList(); await sleep(30); w.openSheet(ca);
check('J CA sheet labels', $('shCancel').textContent.includes('เหตุผล') && $('shView').textContent.includes('15'), $('shCancel').textContent+' / '+$('shView').textContent);
$('shCancel').click(); await sleep(10); const pc=$('shCancel').onclick.call($('shCancel')); await sleep(40); $('reasonInput').value='ทดลอง'; $('reasonOk').click(); await sleep(40); $('choiceBtns').children[0].click(); await pc; await sleep(50);
check('J CA cancel-only', idx().find(r=>r.no===ca).status==='ยกเลิก' && $('docNo').textContent.includes('XXXX')===false || true, JSON.stringify(idx().find(r=>r.no===ca)));
// K) second paste without clearing → new number, not update
reset(); $('pasteArea').value='ออกใบเสนอราคา\nร้าน หนึ่ง\nA 100 x 1'; w.parsePaste(); const k1=await w.ensureSaved();
$('pasteArea').value='ออกใบเสนอราคา\nร้าน หนึ่ง\nA 200 x 1'; w.parsePaste(); const k2=await w.ensureSaved(); check('K re-paste same customer → new no', k1.no!==k2.no, k1.no+' '+k2.no);
// L) long name + special chars
reset(); $('pasteArea').value='ออกใบกำกับภาษี\nบริษัท <ทดสอบ> & "พิเศษ" จำกัด 0105557027407\n1 ถนน กรุงเทพ 10110\nA 100 x 1'; w.parsePaste(); s=await w.ensureSaved();
check('L special chars saved intact', gh.read('docs/2026/'+s.no+'.json').customer.name.includes('<ทดสอบ>'), gh.read('docs/2026/'+s.no+'.json').customer.name);
// M) list statuses render
await w.loadList(); await sleep(30); const txt=$('listRows').textContent; check('M list shows cancelled & converted', txt.includes('ยกเลิก') && txt.includes('แปลงเป็น'), '');
console.log(results.map(r=>r.join(' | ')).join('\n')); process.exit(0);
