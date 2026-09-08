#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_calculator_page.py — หน้า /calculator สำหรับแอดมิน (Pist ขอ 8 ก.ย. 2026)
  "ทุกหน้าที่มีระบบคำนวณพื้นที่ ให้ทำช่องข้อความแบบก๊อปปี้ออกมาส่งให้ลูกค้าได้ … ทำหน้าใหม่ชื่อ calculator
   เอาทุกตัวที่ใช้คำนวณมาลงในนี้หมด — หน้าเดียวแล้วแยกสินค้า"

หลักการ
- ไม่มีตัวเลขของตัวเอง: ดึงกล่อง .pricecard (ตารางราคา + data-sqm/data-price/data-shipping/data-tank/data-addon-*)
  จากหน้าสินค้า TH ทุกหน้าที่มี table[data-calc] มาฝังเป็น JSON ในหน้านี้ → ราคาบนหน้าสินค้าคือแหล่งเดียว
- ไม่มีเครื่องคำนวณของตัวเอง: หน้านี้โหลด /calc.js ตัวเดียวกับหน้าสินค้าแล้วรันใหม่ทุกครั้งที่เปลี่ยนสินค้า
  → ผลลัพธ์ตรงกับที่ลูกค้าเห็นบนหน้าสินค้าเป๊ะ (check_calc.js ชั้น 3 พิสูจน์ด้วยเคส poolarmour 9,770)
- ช่อง "ข้อความส่งลูกค้า": แปลงผลลัพธ์ที่ calc.js วาดใน #lcOut เป็นข้อความธรรมดา แก้ได้ กดคัดลอกได้
- chrome ยืมจาก /coreprimer เหมือน build_search_page.py; หน้าแอดมิน: noindex, ไม่มี canonical (ไม่เข้า sitemap),
  ไม่มีหน้า EN, ไม่มีสวิตช์ภาษา — check_parity นับเป็น APP_DIRS และตรวจว่า JSON ในหน้านี้ตรงกับหน้าสินค้าเสมอ

วิธีใช้:  python3 tools/build_calculator_page.py   (รันใหม่ทุกครั้งที่ราคา/ตารางบนหน้าสินค้าเปลี่ยน — check_parity เตือนถ้าลืม)
"""
import os, re, json, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DOMAIN = "https://www.lucernapro.com"
DST = "calculator/index.html"
MARK_A, MARK_B = '<script id="lcData" type="application/json">', '</script>'

def _pricecard_of(h, tpos):
    """คืน outerHTML ของ <div class="pricecard…"> ที่ครอบตารางที่ตำแหน่ง tpos"""
    s = h.rfind('<div class="pricecard', 0, tpos)
    assert s >= 0
    depth, i = 0, s
    for m in re.finditer(r'<div\b|</div>', h[s:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return h[s:s + m.end()]
    raise AssertionError("pricecard ไม่ปิด")

def extract():
    """[{slug, name, card}] จากหน้าสินค้า TH ทุกหน้าที่มีตารางคำนวณ — เรียงตามชื่อ"""
    out = []
    for f in sorted(glob.glob('*/index.html')):
        slug = f.split('/')[0]
        if slug in ('en', 'post', 'casestudy', 'search', 'finder', 'account', 'ship', 'calculator'): continue
        h = open(f, encoding='utf-8').read()
        m = re.search(r'<table[^>]*data-calc="1"', h)
        if not m: continue
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S).group(1).split('<br')[0]
        name = html.unescape(re.sub(r'<[^>]+>', ' ', h1))
        name = re.sub(r'\s+', ' ', name).strip()
        out.append(dict(slug=slug, name=name, card=_pricecard_of(h, m.start())))
    out.sort(key=lambda p: p['name'].lower())
    return out

def data_json():
    return json.dumps(extract(), ensure_ascii=False, separators=(',', ':'))

CSS = """
  .adm{padding:34px 0 40px}
  .adm h1{font-family:var(--disp);font-weight:700;font-size:clamp(26px,4vw,38px);line-height:1.2}
  .adm h1 .o{color:var(--orange)}
  .adm .lede{margin-top:8px;color:var(--muted);font-size:15px;max-width:720px}
  .psel{margin-top:18px;display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;max-width:720px}
  .psel .f{display:flex;flex-direction:column;gap:5px;flex:1 1 260px}
  .psel label{font-size:12px;color:var(--muted)}
  .psel select{font-family:var(--body);font-size:16px;padding:11px 12px;border:1.5px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);width:100%}
  .psel select:focus{border-color:var(--orange);outline:none}
  .psel a.go{font-size:13.5px;color:var(--orange);padding-bottom:12px;white-space:nowrap}
  #calcHost{max-width:720px}
  .msgbox{margin-top:18px;border:1px solid var(--line);border-radius:14px;background:var(--panel);padding:16px 18px 18px;max-width:720px}
  .msgbox h3{font-family:var(--disp);font-size:16.5px;font-weight:700;margin-bottom:3px}
  .msgbox .sub{font-size:13px;color:var(--muted);margin-bottom:12px}
  .msgbox textarea{width:100%;min-height:260px;font-family:var(--body);font-size:15px;line-height:1.6;padding:12px 14px;border:1.5px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);resize:vertical}
  .msgbox textarea:focus{border-color:var(--orange);outline:none}
  .msgbox .bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:10px}
  .msgbox button{font-family:var(--body);font-size:14.5px;font-weight:600;padding:10px 18px;border:1.5px solid var(--orange);border-radius:999px;background:var(--orange);color:#16130F;cursor:pointer}
  .msgbox button.ghost{background:var(--bg);color:var(--ink);border-color:var(--line)}
  .msgbox .ok{font-size:13px;color:var(--muted)}
  .msgbox .opts{display:flex;gap:14px;flex-wrap:wrap;margin-top:10px;font-size:13.5px;color:var(--muted)}
  .msgbox .opts label{display:flex;align-items:center;gap:6px}
"""

BODY = r"""
<main class="wrap adm">
  <h1>เครื่องคำนวณ <span class="o">ทุกสินค้า</span> <small style="font-family:var(--mono);font-size:12px;color:var(--muted);letter-spacing:.08em;vertical-align:middle">ADMIN</small></h1>
  <p class="lede">เลือกสินค้า กรอกขนาดพื้นที่ (หรือขนาดบ่อ) ระบบใช้เครื่องคำนวณตัวเดียวกับหน้าสินค้า แล้วเรียบเรียงเป็นข้อความพร้อมส่งให้ลูกค้าด้านล่าง — แก้ข้อความก่อนคัดลอกได้</p>

  <div class="psel">
    <div class="f"><label>สินค้า</label><select id="pSel"></select></div>
    <a class="go" id="pLink" href="/" target="_blank" rel="noopener">เปิดหน้าสินค้า →</a>
  </div>

  <div id="calcHost"></div>

  <div class="msgbox">
    <h3>ข้อความส่งลูกค้า</h3>
    <div class="sub">สร้างอัตโนมัติจากผลคำนวณด้านบน — พิมพ์แก้ในช่องได้เลย แล้วกดคัดลอก</div>
    <div class="opts">
      <label><input type="checkbox" id="oShip" checked> ใส่บรรทัดค่าส่ง</label>
      <label><input type="checkbox" id="oNote" checked> ใส่หมายเหตุท้ายข้อความ</label>
      <label><input type="checkbox" id="oLink" checked> ใส่ลิงก์หน้าสินค้า</label>
    </div>
    <textarea id="msg" placeholder="กรอกขนาดพื้นที่ด้านบนก่อน ข้อความจะขึ้นตรงนี้"></textarea>
    <div class="bar">
      <button type="button" id="copyBtn">คัดลอกข้อความ</button>
      <button type="button" class="ghost" id="regenBtn">สร้างใหม่จากผลคำนวณ</button>
      <span class="ok" id="copyOk"></span>
    </div>
  </div>
</main>

__DATA__
<script>
(function(){
  'use strict';
  var DATA = JSON.parse(document.getElementById('lcData').textContent);
  var SEL = document.getElementById('pSel'), HOST = document.getElementById('calcHost'),
      LINK = document.getElementById('pLink'), MSG = document.getElementById('msg'),
      OS = document.getElementById('oShip'), ON = document.getElementById('oNote'), OL = document.getElementById('oLink');
  var calcSrc = null, cur = null, edited = false;

  DATA.forEach(function (p, i) {
    var o = document.createElement('option'); o.value = i; o.textContent = p.name; SEL.appendChild(o);
  });
  var q = (location.hash || '').replace('#', '');
  DATA.some(function (p, i) { if (p.slug === q) { SEL.value = i; return true; } });

  function getCalc(cb) {
    if (calcSrc) return cb(calcSrc);
    (window.__calcSrc ? Promise.resolve(window.__calcSrc)
      : fetch('/calc.js', { cache: 'no-store' }).then(function (r) { return r.text(); }))
      .then(function (t) { calcSrc = t; cb(t); });
  }

  function mount() {
    cur = DATA[parseInt(SEL.value, 10)] || DATA[0];
    location.hash = cur.slug;
    LINK.href = '/' + cur.slug;
    HOST.innerHTML = cur.card;
    edited = false; MSG.value = '';
    getCalc(function (src) {
      new Function(src)();            /* calc.js: หา .pricecard table[data-calc] ในหน้า → มีตัวเดียวคือของสินค้าที่เลือก */
      var out = document.getElementById('lcOut');
      if (out) new MutationObserver(function () { if (!edited) MSG.value = compose(); }).observe(out, { childList: true, subtree: true });
    });
  }

  function txt(el) {
    var h = el.innerHTML.replace(/<br\s*\/?>/gi, '\n');
    var d = document.createElement('div'); d.innerHTML = h;
    return d.textContent.replace(/\u00a0/g, ' ').replace(/[ \t]+/g, ' ').trim();
  }
  function v(id) { var e = document.getElementById(id); return e && parseFloat(e.value) > 0 ? parseFloat(e.value) : 0; }

  function compose() {
    var out = document.getElementById('lcOut');
    if (!out || !out.querySelector('.tot')) return '';
    var w = v('lcW'), l = v('lcL'), d = v('lcD'), a = v('lcA');
    var B = document.getElementById('lcB'), lines = [];
    var size = w && l ? (w + ' × ' + l + (d ? ' × ลึก ' + d : '') + ' ม.') : (a + ' ตร.ม.');
    lines.push('สรุปปริมาณ ' + cur.name + ' สำหรับ' + (d ? 'สระ/บ่อ ' : 'พื้นที่ ') + size + (B && B.checked ? ' (เผื่อ 10%)' : ''));
    var short = (cur.name.match(/^[A-Za-z0-9 .+\/-]+/) || [cur.name])[0].trim() || cur.name;
    var vs = document.querySelector('#lcV button.on');
    if (vs) lines.push('แบบ: ' + vs.textContent.trim());
    lines.push('');
    [].forEach.call(out.querySelectorAll('.row'), function (r) {
      var isTot = r.classList.contains('tot'), s = r.children[0], b = r.children[1];
      if (!s || !b) return;
      var label = txt(s), amt = txt(b).replace(/\.-$/, '') + ' บาท';
      if (!isTot && label === 'ค่าจัดส่ง') { if (OS.checked) lines.push('ค่าจัดส่ง ' + amt); return; }
      if (isTot) { lines.push(''); lines.push('รวม ' + amt); return; }
      /* แถวสีไม่มีชื่อสินค้านำหน้า (ตารางบนหน้าสินค้ารู้อยู่แล้วว่าสินค้าอะไร) — แถว add-on รองพื้นมีชื่อ+ลิงก์ของมันเอง */
      lines.push('• ' + (s.querySelector('a') ? '' : short + ' ') + label + ' = ' + amt);
    });
    var meta = out.querySelector('.meta');
    if (meta) { lines.push(''); lines.push(txt(meta)); }
    if (ON.checked) {
      [].forEach.call(out.querySelectorAll('.calcnote'), function (n) {
        var t = txt(n);
        if (t.indexOf('คิดเต็มทุกถัง') >= 0) t = 'ค่าส่งข้างต้นคิดเต็มทุกชิ้น สั่งจริงเราเหมาค่าส่งให้ถูกกว่านี้ครับ';
        lines.push(''); lines.push(t);
      });
      var hint = out.querySelector('.hint'); if (hint) { lines.push(''); lines.push(txt(hint)); }
    }
    if (OL.checked) { lines.push(''); lines.push('รายละเอียดสินค้า: __DOMAIN__/' + cur.slug); }
    return lines.join('\n');
  }

  function copy() {
    var t = MSG.value; if (!t) return;
    var done = function () { document.getElementById('copyOk').textContent = 'คัดลอกแล้ว ✓'; setTimeout(function () { document.getElementById('copyOk').textContent = ''; }, 2200); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, function () { MSG.select(); document.execCommand('copy'); done(); });
    else { MSG.select(); document.execCommand('copy'); done(); }
  }

  SEL.addEventListener('change', mount);
  MSG.addEventListener('input', function () { edited = true; });
  [OS, ON, OL].forEach(function (o) { o.addEventListener('change', function () { edited = false; MSG.value = compose(); }); });
  document.getElementById('regenBtn').addEventListener('click', function () { edited = false; MSG.value = compose(); });
  document.getElementById('copyBtn').addEventListener('click', copy);
  mount();
})();
</script>
"""

def build():
    t = open("coreprimer/index.html", encoding="utf-8").read()
    head, rest = t.split("</head>", 1)
    title = "เครื่องคำนวณทุกสินค้า (แอดมิน) — LucernaPro"
    head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="หน้าคำนวณปริมาณสินค้าทุกตัวสำหรับแอดมิน">', head)
    head = re.sub(r'<meta property="og:[^"]*" content="[^"]*">\s*', "", head)
    head = re.sub(r'<link rel="canonical" href="[^"]*">\s*', '<meta name="robots" content="noindex,nofollow">\n', head)
    head = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*', "", head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)
    head = head.replace('<script src="/calc.js" defer></script>\n', "")
    head = head.replace("</style>", CSS + "</style>", 1)
    m = re.search(r"<!-- ═══ จบลิ้นชัก MOBILE DRAWER MENU ═══ -->\s*", rest)
    f = rest.find("<footer")
    assert m and f > 0
    top = rest[:m.end()]
    top = re.sub(r'<a class="backlink" href="[^"]*">[^<]*</a>', '<a class="backlink" href="/">← หน้าแรก</a>', top)
    top = re.sub(r'<a class="lang-switch" href="[^"]*">.*?</a>', "", top, flags=re.S)
    top = re.sub(r'<a class="mnav-lang" href="[^"]*">.*?</a>', "", top, flags=re.S)
    body = BODY.replace("__DATA__", MARK_A + data_json() + MARK_B).replace("__DOMAIN__", DOMAIN)
    out = head + "</head>" + top + body + "\n" + rest[f:]
    os.makedirs("calculator", exist_ok=True)
    open(DST, "w", encoding="utf-8").write(out)
    print("built", DST, len(out) // 1024, "KB —", len(extract()), "products")

if __name__ == "__main__":
    build()
