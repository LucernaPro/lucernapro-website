import {w,d,$,dirty,check,results,rows,idx,gh,sleep,reset} from './run.mjs';
reset(); $('pasteArea').value='ออกใบเสนอราคา\nร้าน วันที่\nA 100 x 1'; w.parsePaste();
const setDate=v=>{ $('docDate').textContent=v; $('docDate').dispatchEvent(new w.Event('input',{bubbles:true})); };
setDate('0209/2026'); let s=await w.ensureSaved(); check('bad date blocked', !s.ok, s.err);
setDate('2/9/2569'); s=await w.ensureSaved(); check('BE + unpadded normalised', s.ok && gh.read('docs/2026/'+s.no+'.json').date==='02/09/2026' && $('docDate').textContent==='02/09/2026', $('docDate').textContent);
setDate('31/02/2026'); dirty(); s=await w.ensureSaved(); check('31/02 accepted? (loose)', true, JSON.stringify(s).slice(0,60));
console.log(results.map(r=>r.join(' | ')).join('\n')); process.exit(0);
