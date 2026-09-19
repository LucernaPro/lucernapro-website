import {w,d,$,dirty,check,results,rows,idx,gh,sleep,reset} from './run.mjs';
let seed=Number(process.argv[2]||42); const rnd=()=>{ seed=(seed*1664525+1013904223)%4294967296; return seed/4294967296; };
const pick=a=>a[Math.floor(rnd()*a.length)]; const ri=(a,b)=>a+Math.floor(rnd()*(b-a+1));
const PRODUCTS=['PoolArmour','CorePrimer','Sentol Grout','กันซึมใส Lucerna Crystal Seal','Silicone Pro 5 kg','PatchPro','TileCoat 1 kg','BoundGravel 20 kg'];
const CUST=['บริษัท ทดสอบ จำกัด','ร้านช่างโจ','หจก.แวลู คอนสตรัคชั่น','คุณสมชาย ใจดี','นิติบุคคลอาคารชุด ไอดีล 24','บริษัท บี-เทค กรุ๊ป จำกัด'];
const price=()=>pick([110,335,590,780,1290.5,2040,2990,5890]);
const fmtN=n=>n.toLocaleString('en-US',{minimumFractionDigits:2});
function pasteFor(type){
  const n=ri(1,4); const lines=[];
  if(type==='CA'){ lines.push(pick(['บิลเงินสด','ออกใบกำกับภาษีอย่างย่อ']));
    if(rnd()<0.7) lines.push(pick(['01/09/2026','15/09/2026','11/08/2026','2/9/2569','19/09/2026']));
    for(let i=0;i<n;i++){ const p=price(), q=ri(1,3); lines.push(rnd()<0.5? `${pick(PRODUCTS)}\t${pick(['1 kg','5 kg','20 kg'])}\t${fmtN(p)}\t${q}` : `${pick(PRODUCTS)} ${fmtN(p)} x ${q}`); }
  } else {
    lines.push({QT:'ออกใบเสนอราคา',INV:'ออกใบกำกับภาษี',BL:'ออกใบวางบิล'}[type]+(rnd()<0.3?' รวมค่าส่ง':''));
    const c=pick(CUST); lines.push(rnd()<0.5? c+' 0105557027407' : c);
    if(rnd()<0.5) lines.push('เลขประจำตัวผู้เสียภาษี 0-1055-57027-40-7');
    lines.push(pick(['98/40 ถนนโพธิ์แก้ว แขวงนวมินทร์ เขตบึงกุ่ม กรุงเทพฯ 10240','55 ถ.มิตรภาพ ต.ในเมือง อ.เมือง จ.ขอนแก่น 40000','23 ซ.สุริยาตร์ 4 ต.ในเมือง อ.เมือง จ.อุบลราชธานี 34000']));
    if(rnd()<0.6) lines.push('โทร '+pick(['0812345678','02-509-1061','0646365352']));
    for(let i=0;i<n;i++) lines.push(`${pick(PRODUCTS)} ${fmtN(price())} x ${ri(1,5)}`);
    if(rnd()<0.3) lines.push('ค่าส่ง '+pick([100,200,350]));
    if(rnd()<0.2) lines.push('จัดส่งที่อยู่\nคุณประสงค์ 160 หมู่ 17 ต.เวียงชัย อ.เวียงชัย จ.เชียงราย 57210');
  }
  return lines.join('\n');
}
const ops={created:0,updated:0,cancelled:0,converted:0,replaced:0,blocked:0,errors:0};
const invariants=[];
function checkInvariants(tag){
  const ix=idx(); const nos=ix.map(r=>r.no); const dup=nos.filter((n,i)=>nos.indexOf(n)!==i);
  if(dup.length) invariants.push([tag,'DUP',dup]);
  const series={}; ix.forEach(r=>{ const m=r.no.match(/^(\w+-\d{6})-(\d{4})$/); (series[m[1]]=series[m[1]]||[]).push(+m[2]); });
  for(const [k,v] of Object.entries(series)){ const mx=Math.max(...v); for(let i=1;i<=mx;i++) if(!v.includes(i)) invariants.push([tag,'GAP',k,i]); }
  for(const r of ix){ const f=gh.read('docs/'+r.no.split('-')[1].slice(0,4)+'/'+r.no+'.json'); if(!f){ invariants.push([tag,'NOFILE',r.no]); continue; }
    if(f.no!==r.no) invariants.push([tag,'NO-MISMATCH',r.no]);
    if((f.status||'ออกแล้ว')!==r.status && !r.status.startsWith('แปลงเป็น')) invariants.push([tag,'STATUS-MISMATCH',r.no,f.status,r.status]);
    if(!/^\d{2}\/\d{2}\/\d{4}$/.test(f.date)) invariants.push([tag,'BADDATE',r.no,f.date]);
    if(!(f.totals&&f.totals.grand>0)) invariants.push([tag,'ZERO',r.no]);
    if(!f.items||!f.items.length) invariants.push([tag,'NOITEMS',r.no]);
    if(f.type==='CA'){ const m=f.no.match(/^CA-(\d{4})(\d{2})/); const dm=f.date.match(/^(\d{2})\/(\d{2})\/(\d{4})$/); if(dm && (dm[3]+dm[2])!==(m[1]+m[2])) invariants.push([tag,'CA-MONTH',f.no,f.date]); }
    if(f.type!=='CA' && (!f.customer||!f.customer.name||f.customer.name==='ชื่อลูกค้า')) invariants.push([tag,'NONAME',r.no]);
  }
}
const cancelledEver=new Set();
const N=Number(process.argv[3]||150);
for(let step=0;step<N;step++){
  const tag='step'+step; const op=pick(['new','new','new','new','edit','edit','cancel','convert','reprint','stale','fail']);
  try{
    if(op==='new'){ reset(); const t=pick(['QT','INV','CA','BL','INV','CA']); $('pasteArea').value=pasteFor(t); w.parsePaste();
      if(rnd()<0.15){ $('docDate').textContent=pick(['0209/2026','5/9/2026','31/13/2026','19-09-2026']); $('docDate').dispatchEvent(new w.Event('input',{bubbles:true})); }
      if(rnd()<0.1) gh.injectFail(pick([401,500,409]));
      const s=await w.ensureSaved(); if(s.ok) ops.created++; else { ops.blocked++; const dt=(d.querySelector('#segType button.on')||{}).dataset?.t; if((dt==='INV'||dt==='CA') && !w.outputBlocked(s)) invariants.push([tag,'INV/CA NOT BLOCKED',s]); }
    } else if(op==='edit'){ const r=pick(idx()); if(!r) continue; await w.viewDoc(r.no); await sleep(5);
      const trs=d.querySelectorAll('#tbody tr'); if(trs.length){ trs[0].querySelector('.price').textContent=fmtN(price()); } if(rnd()<0.3) $('custNameText').textContent=pick(CUST); dirty();
      const p=w.ensureSaved(); await sleep(20); if($('choiceModal').style.display==='flex') $('choiceBtns').children[ri(0,1)].click(); const s=await p;
      if(s.ok){ if(s.updated) ops.updated++; else ops.created++; if(cancelledEver.has(r.no) && s.updated) invariants.push([tag,'RESURRECT',r.no]); } else ops.blocked++;
    } else if(op==='cancel'){ await w.loadList(); await sleep(5); const r=pick(idx().filter(x=>x.status==='ออกแล้ว')); if(!r) continue; w.openSheet(r.no); if($('shCancel').style.display==='none') continue;
      $('shCancel').click(); await sleep(5); const p=$('shCancel').onclick.call($('shCancel')); await sleep(30);
      if($('reasonModal').style.display==='flex'){ $('reasonInput').value=pick(['ออกซ้ำ','ยอดผิด','ชื่อผิด']); $('reasonOk').click(); await sleep(30); const c=ri(0,1); $('choiceBtns').children[c].click(); await p; await sleep(30); cancelledEver.add(r.no); ops.cancelled++;
        if(c===1){ const s=await w.ensureSaved(); if(s.ok){ ops.replaced++; const old=idx().find(x=>x.no===r.no); if(old.replacedBy!==s.no) invariants.push([tag,'NO-REPLACE-LINK',r.no,s.no]); } } }
      else { await p; await sleep(30); cancelledEver.add(r.no); ops.cancelled++; }
    } else if(op==='convert'){ const r=pick(idx().filter(x=>x.type==='QT'&&x.status==='ออกแล้ว')); if(!r) continue; await w.convertDoc(r.no,pick(['INV','BL'])); await sleep(5); const s=await w.ensureSaved(); if(s.ok) ops.converted++; else ops.blocked++;
    } else if(op==='reprint'){ const r=pick(idx()); if(!r) continue; await w.viewDoc(r.no); await sleep(5); const before=JSON.stringify(gh.read('docs/2026/'+r.no+'.json')); const s=await w.ensureSaved(); const after=JSON.stringify(gh.read('docs/2026/'+r.no+'.json')); if(before!==after) invariants.push([tag,'REPRINT-MUTATED',r.no]);
    } else if(op==='stale'){ reset(); $('docDate').textContent='01/09/2026'; w.checkDate(); if($('docDate').textContent!=='19/09/2026') invariants.push([tag,'STALE-DATE']);
    } else if(op==='fail'){ reset(); $('pasteArea').value=pasteFor('INV'); w.parsePaste(); gh.injectFail(500); const s=await w.ensureSaved(); if(s.ok) invariants.push([tag,'SAVE OK DESPITE 500']); if(!$('docNo').textContent.includes('XXXX')) invariants.push([tag,'NUMBER SHOWN WITHOUT SAVE']); const s2=await w.ensureSaved(); if(!s2.ok) invariants.push([tag,'RETRY FAILED',s2]); else ops.created++; }
  }catch(e){ ops.errors++; invariants.push([tag,'EXCEPTION',op,e.message]); }
  checkInvariants(tag);
}
console.log('seed',process.argv[2]||42,'steps',N,'ops',JSON.stringify(ops),'docs',idx().length);
console.log('invariant violations:',invariants.length); invariants.slice(0,15).forEach(v=>console.log(' ',JSON.stringify(v)));
process.exit(0);
