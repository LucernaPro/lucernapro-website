#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_search_page.py — สร้างหน้า /search และ /en/search (ช่องค้นหาสินค้า + เคสหน้างาน)

- โครงหน้า (head CSS, topbar, ลิ้นชักมือถือ, footer, สคริปต์ธีม) ยืมจาก /coreprimer และ /en/coreprimer
  → หน้า search หน้าตาเหมือน fleet เสมอ ถ้า chrome เปลี่ยน ให้รันสคริปต์นี้ใหม่
- ข้อมูลที่ค้นมาจาก /search-index.json (สร้างด้วย tools/gen_search_index.py)
- ค้นแบบ substring ทุกคำต้องเจอ (AND) บนชื่อ + คำอธิบาย + คีย์เวิร์ด ไม่แยกตัวพิมพ์

วิธีใช้:  python3 tools/gen_search_index.py && python3 tools/build_search_page.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DOMAIN = "https://www.lucernapro.com"

TXT = {
 "th": dict(title="ค้นหาสินค้าและเคสหน้างาน — LucernaPro",
            desc="พิมพ์ชื่อสินค้า ปัญหาที่เจอ หรือชนิดงาน — ค้นหาสินค้า LucernaPro ทั้ง 50+ ตัว และเคสหน้างานจริงได้จากช่องเดียว",
            h1="ค้นหา", h1b="สินค้าและเคสหน้างาน",
            ph="พิมพ์ชื่อสินค้า / ปัญหา / ชนิดงาน เช่น กันซึม, ห้องน้ำรั่ว, epoxy…",
            gp="สินค้า", gc="เคสหน้างาน", none="ไม่พบผลลัพธ์สำหรับ",
            help="ไม่เจอที่ต้องการ? บอกงานที่จะทำมาทางแชทเพจ เราแนะนำตัวที่ตรงให้",
            chat="แชทเพจ Facebook", all="แสดงทั้งหมด", cnt=("รายการ",),
            lang="th", canon="/search", alt="/en/search", back="← หน้าแรก", backhref="/"),
 "en": dict(title="Search products and case studies — LucernaPro",
            desc="Type a product name, a problem or a job type — search all 50+ LucernaPro products and real job-site case studies in one box",
            h1="Search", h1b="products and case studies",
            ph="Product name / problem / job type, e.g. waterproofing, leaking bathroom, epoxy…",
            gp="Products", gc="Case studies", none="No results for",
            help="Can't find it? Tell us about the job on Facebook chat and we'll point you to the right product",
            chat="Facebook chat", all="Show all", cnt=("results",),
            lang="en", canon="/en/search", alt="/search", back="← Home", backhref="/en/"),
}

CSS = """
  .srch{padding:36px 0 30px}
  .srch h1{font-family:var(--disp);font-weight:700;font-size:clamp(28px,4.4vw,42px);line-height:1.18}
  .srch h1 .o{color:var(--orange)}
  .srch .lede{margin-top:8px;color:var(--muted);font-size:15.5px}
  .sbox{margin-top:18px;position:relative;max-width:720px}
  .sbox input{width:100%;font-family:var(--body);font-size:17px;padding:15px 16px 15px 50px;border:1.5px solid var(--line);border-radius:12px;background:var(--panel);color:var(--ink);outline:none}
  .sbox input::placeholder{color:var(--muted)}
  .sbox input:focus{border-color:var(--orange);box-shadow:0 0 0 3px rgba(237,106,47,.22)}
  .sbox .icon{position:absolute;left:17px;top:50%;transform:translateY(-50%);width:18px;height:18px;opacity:.6}
  .sbox .icon svg{width:18px;height:18px;display:block;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round}
  .smeta{margin-top:10px;font-family:var(--mono);font-size:12px;letter-spacing:.08em;color:var(--muted)}
  .sgroup{padding:8px 0 26px}
  .sgroup h2{font-family:var(--disp);font-weight:600;font-size:20px;margin:0 0 12px;display:flex;align-items:center;gap:10px}
  .sgroup h2 .n{font-family:var(--mono);font-size:12px;color:var(--muted);font-weight:400;letter-spacing:.06em}
  .sgrid{display:grid;grid-template-columns:1fr;gap:12px}
  @media(min-width:640px){.sgrid{grid-template-columns:1fr 1fr}}
  @media(min-width:980px){.sgrid{grid-template-columns:1fr 1fr 1fr}}
  .sitem{display:grid;grid-template-columns:88px 1fr;gap:12px;align-items:center;border:1px solid var(--line);border-radius:12px;background:var(--panel);padding:10px;color:inherit;text-decoration:none;transition:border-color .15s}
  .sitem:hover{border-color:var(--orange)}
  .sitem .th{aspect-ratio:1/1;border-radius:8px;overflow:hidden;background:var(--panel-2)}
  .sitem .th img{width:100%;height:100%;object-fit:cover;display:block}
  .sitem .nm{font-family:var(--disp);font-weight:600;font-size:15.5px;line-height:1.3}
  .sitem .ds{margin-top:4px;font-size:13px;color:var(--muted);line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .sitem.case .nm{font-size:14.5px}
  .snone{margin:20px 0;padding:18px;border:1px dashed var(--line);border-radius:12px;color:var(--muted);font-size:15px}
  .shelp{margin:6px 0 30px;padding:18px;border:1px solid var(--line);border-radius:12px;background:var(--panel);display:flex;gap:14px;align-items:center;flex-wrap:wrap;justify-content:space-between}
  .shelp p{margin:0;font-size:15px}
  .shelp .btn{white-space:nowrap}
"""

def body(T):
    return f"""
<section class="srch" id="search">
  <div class="wrap">
    <h1>{T['h1']} <span class="o">{T['h1b']}</span></h1>
    <p class="lede">{T['desc']}</p>
    <div class="sbox">
      <span class="icon"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.8-3.8"/></svg></span>
      <input type="search" id="q" placeholder="{T['ph']}" autocomplete="off" autofocus>
    </div>
    <div class="smeta" id="meta"></div>
  </div>
</section>
<section class="wrap" id="results"></section>
<section class="wrap">
  <div class="shelp"><p>{T['help']}</p><a class="btn btn-orange" href="https://m.me/lucernapro">{T['chat']}</a></div>
</section>
<script>
(function(){{
  var L='{T['lang']}',q=document.getElementById('q'),R=document.getElementById('results'),M=document.getElementById('meta'),DATA=[];
  var GP='{T['gp']}',GC='{T['gc']}',NONE='{T['none']}',CNT='{T['cnt'][0]}';
  function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c];}});}}
  function norm(s){{return String(s||'').toLowerCase().replace(/\\s+/g,' ');}}
  function card(it){{
    var img=it.i?'<div class="th"><img src="'+esc(it.i)+'" alt="" loading="lazy" decoding="async" width="88" height="88"></div>':'<div class="th"></div>';
    return '<a class="sitem '+(it.t==='c'?'case':'')+'" href="'+esc(it.u)+'">'+img+'<div><div class="nm">'+esc(it.n)+'</div><div class="ds">'+esc(it.d)+'</div></div></a>';
  }}
  function group(title,items){{
    if(!items.length)return '';
    return '<div class="sgroup"><h2>'+title+' <span class="n">'+items.length+' '+CNT+'</span></h2><div class="sgrid">'+items.map(card).join('')+'</div></div>';
  }}
  function run(){{
    var s=norm(q.value).trim(),toks=s?s.split(' '):[];
    var hits=DATA.filter(function(it){{
      if(it.l!==L)return false;
      if(!toks.length)return true;
      var hay=norm(it.n+' '+it.d+' '+it.k);
      return toks.every(function(t){{return hay.indexOf(t)>-1;}});
    }});
    var p=hits.filter(function(x){{return x.t==='p';}}),c=hits.filter(function(x){{return x.t==='c';}});
    R.innerHTML=hits.length?group(GP,p)+group(GC,c):'<div class="snone">'+NONE+' "'+esc(q.value)+'"</div>';
    M.textContent=s?(hits.length+' '+CNT):'';
    try{{var u=new URL(location.href);if(s)u.searchParams.set('q',q.value);else u.searchParams.delete('q');history.replaceState(null,'',u);}}catch(e){{}}
  }}
  try{{var q0=new URL(location.href).searchParams.get('q');if(q0)q.value=q0;}}catch(e){{}}
  fetch('/search-index.json',{{cache:'no-cache'}}).then(function(r){{return r.json();}}).then(function(d){{DATA=d;run();}});
  q.addEventListener('input',run);
}})();
</script>
"""

def build(lang):
    T = TXT[lang]
    donor = "en/coreprimer/index.html" if lang == "en" else "coreprimer/index.html"
    t = open(donor, encoding="utf-8").read()
    head, rest = t.split("</head>", 1)
    # ── head: rewrite page meta, drop product-specific bits ──
    head = re.sub(r"<title>.*?</title>", f"<title>{T['title']}</title>", head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{T["desc"]}">', head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{T["title"]}">', head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{T["desc"]}">', head)
    head = head.replace('<meta property="og:type" content="product">', '<meta property="og:type" content="website">')
    head = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{DOMAIN}{T["canon"]}">', head)
    head = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{DOMAIN}/img/logo.png">', head)
    th, en = ("/search", "/en/search")
    head = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{DOMAIN}{T["canon"]}">', head)
    head = re.sub(r'<link rel="alternate" hreflang="th" href="[^"]*">', f'<link rel="alternate" hreflang="th" href="{DOMAIN}{th}">', head)
    head = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">', f'<link rel="alternate" hreflang="en" href="{DOMAIN}{en}">', head)
    head = re.sub(r'<link rel="alternate" hreflang="x-default" href="[^"]*">', f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{th}">', head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)
    head = head.replace('<script src="/calc.js" defer></script>\n', "")
    head = head.replace("</style>", CSS + "</style>", 1)
    # ── body: keep topbar + drawer, drop product content, keep footer + scripts ──
    m = re.search(r"<!-- ═══ จบลิ้นชัก MOBILE DRAWER MENU ═══ -->\s*", rest)
    f = rest.find("<footer")
    assert m and f > 0, donor
    top = rest[:m.end()]
    top = re.sub(r'<a class="backlink" href="[^"]*">[^<]*</a>', f'<a class="backlink" href="{T["backhref"]}">{T["back"]}</a>', top)
    top = re.sub(r'<a class="lang-switch" href="[^"]*">', f'<a class="lang-switch" href="{T["alt"]}">', top)
    top = re.sub(r'<a class="mnav-lang" href="[^"]*">', f'<a class="mnav-lang" href="{T["alt"]}">', top)
    tail = rest[f:]
    out = head + "</head>" + top + body(T) + "\n" + tail
    dst = "en/search/index.html" if lang == "en" else "search/index.html"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(out)
    print("built", dst, len(out) // 1024, "KB")

if __name__ == "__main__":
    build("th"); build("en")
