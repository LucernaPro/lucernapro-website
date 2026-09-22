#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_easyclean_page.py — สร้าง /easyclean และ /en/easyclean จาก chrome ของ /paintcoating

หลักการ: ยกหัวเว็บ + ลิ้นชัก + ส่วนท้าย (explore/why/contact/footer/JS) มาจาก paintcoating ทั้งก้อน
แล้วใส่เนื้อหาของ EasyClean แทนช่วงกลาง — เนื้อหาตัวเลขทั้งหมดมาจาก TDS ของผู้ผลิต (22 มี.ค. 2025)

วิธีใช้:  python3 tools/build_easyclean_page.py   (รันจากรากรีโป)
สถานะ:   ยังไม่มีรูปสินค้า/คลิป — ใช้ภาพ placeholder img/easyclean-hero-sq.webp ไว้ก่อน
          ราคา 22 ก.ย. 2026 (Pist): 100 g 830 / 500 g 3,590 / 1 kg 6,600 ส่ง 70 — ลงด้วยลูกกลิ้งโฟม 4 นิ้ว
          หลัง build ต้องรัน tools/build_calculator_page.py ด้วย (ตารางมี data-calc)
"""
import io, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

EXTRA_CSS = """<style id="easyclean-css">
  .cmp{margin-top:20px;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--panel)}
  .cmp table{width:100%;border-collapse:collapse;font-size:14.5px}
  .cmp th{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-align:left;padding:12px 16px;border-bottom:1px solid var(--line);background:var(--panel-2)}
  .cmp td{padding:12px 16px;border-bottom:1px solid var(--line);vertical-align:top}
  .cmp tr:last-child td{border-bottom:0}
  .cmp td:first-child{color:var(--muted);white-space:nowrap}
  .cmp th:nth-child(2){color:var(--orange)}
  .cmp td:nth-child(2){font-weight:600}
  @media(max-width:600px){.cmp td:first-child{white-space:normal}}
  .vidgrid.vert.solo{max-width:320px;grid-template-columns:1fr}
  @media(max-width:759px){.vidgrid.vert.solo{display:grid}.vidgrid.vert.solo figure{flex:none}}
</style>
"""


def chrome(src):
    """คืน (head, drawer, tail) จากหน้า paintcoating: head=จนถึง </head>, drawer=<body>…จบลิ้นชัก, tail=explore…</html>"""
    s = io.open(src, encoding='utf-8').read()
    i_head = s.index('</head>')
    head = s[:i_head]
    i_body = s.index('<body>')
    i_drawer_end = s.index('<!-- ═══ จบลิ้นชัก MOBILE DRAWER MENU ═══ -->')
    drawer = s[i_body:i_drawer_end + len('<!-- ═══ จบลิ้นชัก MOBILE DRAWER MENU ═══ -->')]
    i_tail = s.index('<section class="explore">')
    tail = s[i_tail:]
    return head, drawer, tail


def build(lang):
    src = 'paintcoating/index.html' if lang == 'th' else 'en/paintcoating/index.html'
    head, drawer, tail = chrome(src)

    # ── head ──
    head = head.replace('/paintcoating', '/easyclean')
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE[lang], head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % DESC[lang], head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % OGT[lang], head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % OGD[lang], head)
    head = head.replace('img/paintcoating-hero-sq.webp', 'img/easyclean-hero-sq.webp')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', SCHEMA[lang], head, flags=re.S)
    head = head + EXTRA_CSS

    # ── drawer ──
    drawer = drawer.replace('/paintcoating', '/easyclean')

    body = BODY[lang]
    tail = tail.replace('/paintcoating', '/easyclean')
    out = head + '</head>\n' + drawer + '\n\n' + body + '\n' + tail
    dst = 'easyclean/index.html' if lang == 'th' else 'en/easyclean/index.html'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    io.open(dst, 'w', encoding='utf-8').write(out)
    print('wrote', dst, len(out))


TITLE = {
    'th': 'EasyClean น้ำยาเคลือบกันคราบ เช็ดง่าย ยับยั้งแบคทีเรีย — สำหรับผิวสีและโลหะ | LucernaPro',
    'en': 'EasyClean — Anti-Fouling, Easy-Clean, Antibacterial Coating for Painted and Metal Surfaces | LucernaPro',
}
DESC = {
    'th': 'EasyClean น้ำยาเคลือบกันคราบสาย Hydrophobic ฟิล์มใสแข็ง 4H มุมสัมผัสน้ำ ≥110° น้ำและคราบน้ำมันเกาะยาก เช็ดออกง่าย กันสีสเปรย์ ทนกรดด่าง ยับยั้งแบคทีเรีย สำหรับผนังสีน้ำ สีไม้ สีอบ และโลหะ ทั้งในและนอกอาคาร วัตถุดิบนำเข้าจาก Feibo ปรึกษาฟรีทางแชทเพจ',
    'en': 'EasyClean — a hydrophobic, easy-clean nano coating for painted and metal surfaces. Clear 4H film, water contact angle ≥110°, sheds water and oily grime, wipes clean, anti-graffiti, resists acid and alkali, inhibits bacterial growth. Interior and exterior. Raw material imported from Feibo.',
}
OGT = {
    'th': 'EasyClean น้ำยาเคลือบกันคราบ เช็ดง่าย ยับยั้งแบคทีเรีย — สำหรับผิวสีและโลหะ',
    'en': 'EasyClean — Anti-Fouling, Easy-Clean, Antibacterial Coating for Painted and Metal Surfaces',
}
OGD = {
    'th': 'ฟิล์มใสสาย Hydrophobic แข็ง 4H น้ำเด้ง คราบน้ำมันและสีสเปรย์เกาะยาก เช็ดออกง่าย ทนกรดด่าง — ผนังสีน้ำ สีไม้ สีอบ โลหะ ทั้งในและนอกอาคาร',
    'en': 'Clear hydrophobic 4H film — water beads off, oily grime and spray paint struggle to stick, wipes clean, resists acid and alkali. For latex-painted walls, wood finishes, baked enamel and metal, indoors and out.',
}
SCHEMA = {
    'th': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"EasyClean น้ำยาเคลือบกันคราบ เช็ดง่าย ยับยั้งแบคทีเรีย","brand":{"@type":"Brand","name":"LucernaPro"},"description":"น้ำยาเคลือบกันคราบสาย Hydrophobic ฟิล์มใสแข็ง 4H มุมสัมผัสน้ำ ≥110° สำหรับผิวสีและโลหะ — น้ำและคราบน้ำมันเกาะยาก เช็ดออกง่าย กันสีสเปรย์ ทนกรดด่าง ยับยั้งแบคทีเรีย","image":"https://www.lucernapro.com/img/easyclean-hero-sq.webp","url":"https://www.lucernapro.com/easyclean","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"830","highPrice":"6600","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
    'en': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"EasyClean — Anti-Fouling, Easy-Clean, Antibacterial Coating","brand":{"@type":"Brand","name":"LucernaPro"},"description":"Hydrophobic easy-clean nano coating for painted and metal surfaces — clear 4H film, water contact angle ≥110°, sheds water and oily grime, wipes clean, anti-graffiti, resists acid and alkali, inhibits bacterial growth.","image":"https://www.lucernapro.com/img/easyclean-hero-sq.webp","url":"https://www.lucernapro.com/en/easyclean","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"830","highPrice":"6600","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
}

BODY = {}

BODY['th'] = r'''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Protection <b>· เคลือบปกป้อง</b></div>
      <div class="flagtag">★ NEW — สินค้าใหม่</div>
      <h1>Easy<span class="o">Clean</span><br>น้ำยาเคลือบกันคราบ เช็ดง่าย ยับยั้งแบคทีเรีย</h1>
      <p class="lede">ผนังทาสีน้ำ ประตูและวงกบสีไม้ เฟอร์นิเจอร์สีอบ ตู้และผนังโลหะ — เคลือบครั้งเดียวเป็นฟิล์มใสบางแข็งระดับ 4H แล้ว<b>น้ำเด้ง คราบน้ำมันและสีสเปรย์เกาะยาก เช็ดออกด้วยผ้าชุบน้ำ</b> ทนกรดด่างและน้ำมันเบนซิน ลดไฟฟ้าสถิตให้ฝุ่นเกาะน้อยลง และยับยั้งการเจริญของแบคทีเรียบนผิว</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">สั่งซื้อ / ดูราคา</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>ปรึกษาหน้างานฟรี</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/easyclean-hero-sq.webp" alt="EasyClean น้ำยาเคลือบกันคราบ เช็ดง่าย — ผิวสาย Hydrophobic หยดน้ำเกาะเป็นเม็ด" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">ทำไมผิวที่เคลือบแล้วถึง <em>เช็ดง่าย</em></h2>
    <p class="sec-sub">ฟิล์มนาโนพอลิซิลอกเซนที่มีพลังงานผิวต่ำ — น้ำ น้ำมัน และคราบไม่ได้ "ซึม" เข้าผิว จึงเกาะอยู่แค่บนฟิล์มและเช็ดออกได้</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>น้ำเด้ง คราบไม่ซึมเข้าผิว</h4><p>มุมสัมผัสน้ำ ≥110° และมุมกลิ้ง 5–10° — หยดน้ำเกาะเป็นเม็ดแล้วกลิ้งหนี น้ำชา กาแฟ ซอส หมึก ที่หกใส่ผนังหรือโต๊ะไม่ทิ้งวงด่าง เพราะไม่ทันซึมเข้าสี</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>กันคราบน้ำมันและสีสเปรย์</h4><p>คราบไขมันจากมือ ควันครัว ปากกาเคมี และสีสเปรย์ เกาะบนฟิล์มแทนเกาะบนสี — เช็ดออกได้ด้วยผ้าชุบน้ำหรือน้ำยาฤทธิ์กลาง ผู้ผลิตทดสอบคุณสมบัติกันสีย้อมซึม (Anti-Graffiti) ไว้ในสเปค</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>แข็ง 4H ทนกรด ด่าง เบนซิน</h4><p>ฟิล์มหนา 8–12 ไมครอน ความแข็งดินสอ ≥4H แช่กรดซัลฟิวริก 10% และโซดาไฟ 10% 24 ชั่วโมง แช่น้ำมันเบนซิน 24 ชั่วโมง — ความแข็งและการยึดเกาะไม่เปลี่ยน ผิวสีข้างล่างจึงถูกปกป้องจากการล้างบ่อยและสารเคมีทำความสะอาด</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>ลดไฟฟ้าสถิต ยับยั้งแบคทีเรีย</h4><p>ฟิล์มลดประจุสะสมบนผิวสีและพลาสติก ฝุ่นและขุยผ้าเกาะน้อยลง — และเมื่อน้ำกับคราบอินทรีย์เกาะผิวได้ยาก แบคทีเรียก็ขาดที่ยึดและความชื้นที่ต้องใช้ในการเจริญ (คุณสมบัติที่ผู้ผลิตระบุ — ไม่ใช่น้ำยาฆ่าเชื้อ อ่าน STRAIGHT TALK ข้อ 5)</p></div></div>
    </div>
  </div>
</section>

<section class="howto" id="proof">
  <div class="wrap">
    <h2 class="sec-h">ดูของจริงก่อน — <em>กระเบื้องแผ่นเดียวกัน ครึ่งเคลือบ ครึ่งไม่เคลือบ</em></h2>
    <p class="sec-sub">ปากกา Permanent ขีดบนกระเบื้องทั้งสองฝั่ง แล้วเช็ดเทียบกัน — ฝั่งที่เคลือบ EasyClean หมึกเกาะอยู่บนฟิล์ม เช็ดออกง่ายกว่ามาก ฝั่งไม่เคลือบหมึกกัดติดผิว</p>
    <div class="vidgrid vert solo">
      <figure>
        <div class="fbv v916"><iframe src="https://www.facebook.com/plugins/video.php?height=476&href=https%3A%2F%2Fwww.facebook.com%2Freel%2F862710706836529%2F&show_text=false&width=267&t=0" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" loading="lazy" title="ทดสอบปากกา Permanent บนกระเบื้อง ฝั่งเคลือบ EasyClean เทียบฝั่งไม่เคลือบ"></iframe></div>
        <figcaption>ทดสอบปากกา Permanent — ขีดทั้งสองฝั่ง เช็ดเหมือนกัน ดูว่าฝั่งไหนออกก่อน</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="buybox" id="compare">
  <div class="wrap">
    <h2 class="sec-h">EasyClean กับ Paint Coating — <em>คนละหลักการ</em></h2>
    <p class="sec-sub">สองตัวนี้มาจากผู้พัฒนาวัตถุดิบเดียวกัน ใช้บนผิวสีเหมือนกัน แต่ทำงาน<b>ตรงข้ามกัน</b> — เลือกตามว่าใครจะเป็นคนล้าง: ฝน หรือคน</p>
    <div class="cmp">
      <table>
        <thead><tr><th></th><th>EasyClean (หน้านี้)</th><th>Paint Coating</th></tr></thead>
        <tbody>
          <tr><td>หลักการ</td><td>Hydrophobic — น้ำเด้งเป็นเม็ดกลิ้งหนี</td><td>Superhydrophilic — น้ำแผ่เป็นแผ่นไหลลงทั้งผืน</td></tr>
          <tr><td>มุมสัมผัสน้ำ</td><td>≥ 110°</td><td>&lt; 10°</td></tr>
          <tr><td>ใครล้าง</td><td>คน — คราบเช็ดออกง่ายด้วยผ้าชุบน้ำ</td><td>ฝนกับแดด — ฝนล้างไม่ทิ้งคราบ แดดย่อยคราบน้ำมัน</td></tr>
          <tr><td>ฟิล์ม</td><td>8–12 ไมครอน แข็ง ≥4H ทนกรดด่าง เบนซิน</td><td>บางระดับตามองไม่เห็น มีชั้น Photocatalytic</td></tr>
          <tr><td>เหมาะกับ</td><td>ผิวที่คนเช็ดถึงและโดนคราบบ่อย — ผนังภายใน ประตู เฟอร์นิเจอร์ ห้องครัว ห้องน้ำ โรงพยาบาล โรงเรียน ตู้และเครื่องจักร ผนังที่โดนสีสเปรย์</td><td>ผิวภายนอกที่ฝนโดนและล้างยาก — แผง ACP ป้ายและหลังคาปั๊ม ตัวถังรถบัส-รถไฟ</td></tr>
          <tr><td>วิธีลง</td><td>ลูกกลิ้งโฟม 4 นิ้ว ชั้นบางชั้นเดียว</td><td>ลูกกลิ้งขนสั้น / พ่น / ทา</td></tr>
          <tr><td>ใช้ทับกันได้ไหม</td><td colspan="2">ไม่ได้ — ผิวหนึ่งเลือกได้อย่างเดียว ฟิล์ม Hydrophobic จะทำให้ Paint Coating เกาะไม่ได้</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">ถ้าโจทย์คือ "ฝนล้างแทน" บนแผงหรือหลังคากลางแจ้ง ไปที่ <a href="/paintcoating" style="color:var(--orange)">Paint Coating</a> — ถ้าโจทย์คือ "เช็ดคราบให้ออกง่ายและปกป้องสีจากการล้างบ่อย" อยู่หน้านี้ถูกแล้ว</p>
  </div>
</section>

<section class="story">
  <div class="wrap">
    <div class="rdtag">SOURCE — วัตถุดิบมาจากไหน</div>
    <h2>เราเลือกนำเข้าวัตถุดิบหลัก<br>จากผู้พัฒนาเทคโนโลยีนี้<b>โดยตรง — Feibo</b></h2>
    <div class="story-grid">
      <div class="bignum">≥110°<small>WATER CONTACT ANGLE · HYDROPHOBIC</small></div>
      <div class="story-body">
        <p>ตัวนี้เรา<b>นำเข้าวัตถุดิบหลักจาก Feibo</b> (ฉางชา ประเทศจีน) ผู้พัฒนาวัตถุดิบเดียวกับ <a href="/glasscoating" style="color:var(--orange)">Glass Coating</a> และ <a href="/paintcoating" style="color:var(--orange)">Paint Coating</a> ของเรา แล้วมาบรรจุและควบคุมคุณภาพต่อในประเทศไทย — แต่ตัวนี้เป็น<b>คนละสาย</b>กับกลุ่ม Self-Cleaning: เป็นฟิล์มกันคราบสาย Hydrophobic ที่ออกแบบให้คนเช็ดถึง ไม่ได้รอฝน</p>
        <p>ในจีน สูตรนี้ใช้กับผิวที่โดนคราบและสารเคมีทำความสะอาดบ่อยจนสีเสียก่อนเวลา — และผ่านมาตรฐานความปลอดภัยด้านไฟสำหรับยานพาหนะระบบราง (EN 45545-2 ระดับ R1 HL3) จึงใช้ในตู้โดยสารและงานที่ต้องการวัสดุไม่ลามไฟได้</p>
        <div class="beats">
          <div class="beat"><div class="k">หลักการ</div><p>ฟิล์มนาโนพอลิซิลอกเซนโครงสร้างแฟรกทัล เติมนาโนทังสเตนไตรออกไซด์และนาโนทินออกไซด์ — พลังงานผิวต่ำ น้ำและน้ำมันไม่แผ่ตัวบนผิว จึงเกาะเป็นเม็ดและเช็ดออกได้ ผู้ผลิตระบุอายุฟิล์ม <b>2–3 ปี</b> โดยคุณสมบัติแทบไม่เปลี่ยน</p></div>
          <div class="beat"><div class="k">ผิวที่ใช้ได้</div><p>สีน้ำอะคริลิกผนังภายใน สีไม้ สีอบ (Baked Enamel) สีพ่นอุตสาหกรรม ผิวโลหะเปลือยและ Powder Coat — <b>ผิวสีที่แห้งและแข็งตัวสมบูรณ์แล้ว</b> ใช้ได้ทั้งในและนอกอาคาร (ทดสอบสภาพอากาศกลางแจ้ง 3,000 ชั่วโมง)</p></div>
          <div class="beat"><div class="k">ฟิล์มแข็งกว่าที่คิด</div><p>ความหนา 8–12 ไมครอน ความแข็งดินสอ ≥4H บนกระจกและโลหะ ยึดเกาะ Cross-cut เกรด 0 และยังเกรด 0–1 หลังสลับร้อน-เย็น −30°C ↔ 120°C 3 รอบ — เป็น<b>ชั้นปกป้อง</b>ผิวสีจากการขัดถูและน้ำยาล้าง ไม่ใช่แค่ชั้นกันน้ำ</p></div>
          <div class="beat"><div class="k">ลดไฟฟ้าสถิต</div><p>ผิวสีและพลาสติกสะสมประจุแล้วดูดฝุ่นแห้ง — ฟิล์มนี้ลดประจุบนผิว ฝุ่น ขุยผ้า และละอองน้ำมันเกาะน้อยลงตั้งแต่แรก จึงเช็ดน้อยลงด้วย</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">ตัวเลขจริงจาก<em>ผลทดสอบ</em></h2>
    <p class="sec-sub">สเปคจาก TDS ของผู้พัฒนาวัตถุดิบ — ไม่ใช่คำโฆษณา</p>
    <div class="speccard">
      <table>
        <thead><tr><th>คุณสมบัติ</th><th>ค่า</th></tr></thead>
        <tbody>
          <tr><td>มุมสัมผัสน้ำ (Water Contact Angle)</td><td>≥ 110°</td></tr>
          <tr><td>มุมกลิ้งของหยดน้ำ (Sliding Angle)</td><td>5–10°</td></tr>
          <tr><td>ความหนาฟิล์ม</td><td>8–12 ไมครอน · ใส ไม่เปลี่ยนสีผิวเดิม</td></tr>
          <tr><td>ความแข็งดินสอ</td><td>≥ 4H (บนกระจกหรือโลหะ)</td></tr>
          <tr><td>การยึดเกาะ Cross-cut</td><td>เกรด 0 · หลังสลับร้อน-เย็น −30°C / 120°C 3 รอบ เกรด 0–1</td></tr>
          <tr><td>เวลาแห้ง (25°C)</td><td>แห้งผิว ≤ 30 นาที · แห้งจริง ≤ 4 ชม. · แข็งตัวสมบูรณ์ 24 ชม.</td></tr>
          <tr><td>อบร้อน (งานโรงงาน)</td><td>75°C 1–2 ชม.</td></tr>
          <tr><td>ทนน้ำ</td><td>แช่น้ำกลั่น 40°C 240 ชม. — ความ Hydrophobic ไม่เปลี่ยน</td></tr>
          <tr><td>ทนน้ำมันเบนซิน</td><td>แช่เบนซิน 24 ชม. — ความแข็งและการยึดเกาะไม่เปลี่ยน</td></tr>
          <tr><td>ทนกรด-ด่าง</td><td>กรดซัลฟิวริก 10% และโซเดียมไฮดรอกไซด์ 10% 24 ชม. — ไม่เปลี่ยน</td></tr>
          <tr><td>ทนสภาพอากาศกลางแจ้ง</td><td>3,000 ชม. — ฟิล์มสมบูรณ์ เกรด 0–1 บนอะลูมิเนียม แทบไม่ด้านไม่เปลี่ยนสี</td></tr>
          <tr><td>ความปลอดภัยด้านไฟ</td><td>ผ่าน EN 45545-2 ระดับ R1 HL3 (ยานพาหนะระบบราง)</td></tr>
          <tr><td>ปริมาณใช้</td><td>ลูกกลิ้งโฟมชั้นบาง ≈ 160 ตร.ม./กก. · ผู้ผลิตระบุ 15–50 มล./ตร.ม. เมื่อพ่นหรือทาแปรง</td></tr>
          <tr><td>อายุการเก็บ</td><td>1 ปี ยังไม่เปิด · เก็บ 18–25°C พ้นแดดและประกายไฟ</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">ขนาดและราคา</h2>
    <div class="pricecard">
      <table data-calc="1" data-shipping="70">
        <thead><tr><th>ขนาด</th><th>พื้นที่ใช้งานโดยประมาณ</th><th>ราคา</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="16">100 g</td><td>≈ 16 ตร.ม.</td><td class="pr" data-price="830">830.-</td></tr>
          <tr><td class="sz" data-sqm="80">500 g</td><td>≈ 80 ตร.ม.</td><td class="pr" data-price="3590">3,590.-</td></tr>
          <tr><td class="sz" data-sqm="160">1 kg</td><td>≈ 160 ตร.ม.</td><td class="pr" data-price="6600">6,600.-</td></tr>
          <tr data-calc="skip"><td class="sz">งานโครงการ<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">อาคาร / โรงงาน / ฟลีท</small></td><td>พื้นที่ขนาดใหญ่</td><td class="pr">ราคาโครงการ — สอบถาม</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">ค่าจัดส่ง <b>70 บาท</b> · พื้นที่ต่อขวดคิดจากการลง<b>ชั้นบางชั้นเดียวด้วยลูกกลิ้งโฟม 4 นิ้ว</b>ตามขั้นตอนด้านล่าง — ยิ่งบางยิ่งดีทั้งผลลัพธ์และความคุ้ม · <b>งานใหญ่มีราคาโครงการ</b> แจ้งชนิดผิวและพื้นที่ (ตร.ม.) มาทางแชทเพจ เราเสนอราคาและคำนวณปริมาณให้ฟรีก่อนสั่งซื้อ</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">วิธีใช้งาน — <em>จบบนหน้านี้</em></h2>
    <p class="sec-sub">อ่านให้จบก่อนเปิดกระป๋อง — <b>ผิวสะอาดแห้งสนิท</b> กับ <b>กันน้ำโดนในชั่วโมงแรก</b> คือสองอย่างที่ตัดสินผลทั้งงาน</p>
    <ol class="flow">
      <li class="fstep"><h4>ล้างผิวให้สะอาด ปราศจากน้ำมัน และแห้งสนิท</h4><p>ขจัดฝุ่น คราบน้ำมัน คราบมือ และคราบน้ำออกให้หมด ถ้ามีไขมันหรือแว็กซ์เก่าต้องล้างขจัดไขมัน (Degrease) ก่อน — สีที่เพิ่งทาต้องรอให้แห้งและแข็งตัวสมบูรณ์ตามสเปคของสีนั้นก่อนเคลือบ</p></li>
      <li class="fstep"><h4>ทดสอบมุมเล็กก่อนลงจริง</h4><p>ลงบนมุมที่ไม่เด่นของผิวจริง รอแข็งตัว แล้วดูความใส การยึดเกาะ และหยดน้ำทดสอบ — โดยเฉพาะบนผิวมันสีเข้มและสีน้ำผนังที่มีฝุ่นชอล์ก</p></li>
      <li class="fstep"><h4>ลงเป็นชั้นบางสม่ำเสมอด้วยลูกกลิ้งโฟม 4 นิ้ว</h4><p>ใช้<b>ลูกกลิ้งโฟมขนาด 4 นิ้ว</b> ไล่ทางเดียวเป็นชั้นบางชั้นเดียว ไม่ให้ไหลย้อย ไม่ให้เว้น — บางคือหัวใจ ลงหนาไม่ได้ผลเพิ่มแต่เปลืองและอาจเห็นฟิล์มบนผิวมันสีเข้ม งานโรงงานพื้นที่ใหญ่พ่นด้วยกาพ่น HVLP หัว 1.0–1.2 มม. แรงดัน 0.2 MPa ได้ <b>เปิดกระป๋องแล้วมีแก๊สและกลิ่นคล้ายแอลกอฮอล์เล็กน้อยเป็นเรื่องปกติ</b></p><span class="fchip">ลูกกลิ้งโฟม 4 นิ้ว</span><span class="fchip">ชั้นบางชั้นเดียว</span><span class="fchip">งานโรงงาน: กาพ่น HVLP</span></li>
      <li class="fstep"><h4>ห้ามกลับไปถูซ้ำ — ผิวหน้าเซ็ตตัวทันที</h4><p>ผิวหน้าเริ่มแข็งทันทีที่ลงเสร็จ แห้งผิวใน 20–30 นาที — ลงแล้วปล่อย ไม่กลับไปกลิ้งซ้ำหรือทาซ้ำจุดเดิม ไม่งั้นฟิล์มจะเป็นรอย</p></li>
      <li class="fstep"><h4>กันน้ำโดนจนกว่าฟิล์มจะแข็งตัว</h4><p><b>ถ้าน้ำโดนผิวก่อนฟิล์มแข็งตัว จะเกิดรอยด่าง</b>ที่เช็ดไม่ออก ต้องล้างออกเคลือบใหม่ — ผู้ผลิตให้กันน้ำอย่างน้อย 1 ชั่วโมงแรก งานกลางแจ้งเช็คพยากรณ์ฝนก่อนเสมอ</p><span class="fchip">แห้งผิว 20–30 นาที</span><span class="fchip">แห้งจริง ≤ 4 ชม.</span></li>
      <li class="fstep"><h4>24 ชั่วโมง แข็งตัวสมบูรณ์ — ใช้งานได้</h4><p>ที่อุณหภูมิห้องฟิล์มแข็งตัวเต็มที่ใน 24 ชั่วโมง (งานโรงงานอบ 75°C 1–2 ชั่วโมงแทนได้) หลังจากนั้นเช็ดล้างได้ตามปกติด้วยผ้าชุบน้ำหรือน้ำยาฤทธิ์กลาง</p></li>
    </ol>

    <div class="warn"><b>⚠ ความปลอดภัย:</b> น้ำยามีส่วนผสมตัวทำละลายและติดไฟได้ — ทำงานในที่อากาศถ่ายเท ห่างจากประกายไฟและความร้อน สวมถุงมือ แว่นครอบตา และหน้ากากกรองไอระเหยอินทรีย์เมื่อพ่น เก็บที่ 18–25°C พ้นมือเด็กและแสงแดดตรง</div>
  </div>
</section>

<section class="story" id="straight">
  <div class="wrap">
    <div class="rdtag">STRAIGHT TALK — ความจริงที่ต้องพูด</div>
    <h2>ก่อนจ่ายเงิน อ่าน 6 ข้อนี้ก่อน —<br><b>ตัวนี้ไม่ใช่ของวิเศษ</b> และเราไม่อยากให้คุณเข้าใจผิด</h2>
    <div class="story-grid">
      <div class="bignum">6<small>สิ่งที่คนขายส่วนใหญ่ไม่บอก</small></div>
      <div class="story-body">
        <div class="beats">
          <div class="beat"><div class="k">1 · คราบยังต้องเช็ด — แค่เช็ดง่ายขึ้นมาก</div><p>ตัวนี้ไม่ใช่ Self-Cleaning ฝนไม่ได้ล้างแทนคุณ และผิวที่เคลือบแล้วยังเปื้อนได้ — ต่างกันตรงที่<b>คราบเกาะอยู่บนฟิล์ม ไม่ซึมเข้าสี</b> จึงเช็ดออกด้วยผ้าชุบน้ำแทนที่จะขัดหรือทาสีใหม่ ถ้าโจทย์คือแผงกลางแจ้งที่อยากให้ฝนดูแล ไปที่ <a href="/paintcoating" style="color:var(--orange)">Paint Coating</a></p></div>
          <div class="beat"><div class="k">2 · ชั่วโมงแรกคือจุดตาย</div><p>น้ำโดนผิวก่อนฟิล์มแข็งตัว = <b>รอยด่างที่เช็ดไม่ออก</b> ต้องล้างออกทำใหม่ งานกลางแจ้งเช็คพยากรณ์ฝน งานในบ้านกันคนเดินผ่านสาดน้ำและงดถูพื้นใกล้ผนังในชั่วโมงแรก</p></div>
          <div class="beat"><div class="k">3 · ลงหนา ไม่ได้ทนขึ้น</div><p>พื้นที่ต่อขวดในตารางคิดจาก<b>ชั้นบางชั้นเดียวด้วยลูกกลิ้งโฟม</b> — ลงหนาหรือลงสองรอบไม่ได้เพิ่มการกันคราบ แต่เปลืองน้ำยาและบนผิวมันสีเข้มอาจเห็นฟิล์ม ถ้าลูกกลิ้งเริ่มฝืดแปลว่าน้ำยาหมดหน้าลูกกลิ้ง ให้จุ่มเพิ่ม ไม่ใช่กดแรงขึ้น</p></div>
          <div class="beat"><div class="k">4 · ผิวสีต้องแข็งตัวสมบูรณ์ และทดสอบมุมก่อนเสมอ</div><p>สีที่เพิ่งทา สีที่ยังชอล์ก หรือสีน้ำผนังที่ลอกล่อน — ฟิล์มจะเกาะสีที่หลุด ไม่ได้เกาะผนัง ตัวนี้<b>ปกป้องสีที่ยังดี</b> ไม่ได้ซ่อมสีที่เสียแล้ว บนผิวมันสีเข้ม ลงหนาเกินอาจเห็นฟิล์ม ทดสอบมุมเล็กบนสีจริงก่อนทุกครั้ง</p></div>
          <div class="beat"><div class="k">5 · "ยับยั้งแบคทีเรีย" ไม่ใช่ "ฆ่าเชื้อ"</div><p>ผู้ผลิตระบุคุณสมบัติยับยั้งการเจริญของแบคทีเรียบนผิว ซึ่งมาจากการที่น้ำและคราบอินทรีย์เกาะผิวได้ยาก — <b>ไม่ใช่น้ำยาฆ่าเชื้อ ไม่แทนการทำความสะอาด</b> โรงพยาบาล ครัว และห้องน้ำยังต้องเช็ดล้างตามรอบเดิม แค่เช็ดง่ายขึ้น</p></div>
          <div class="beat"><div class="k">6 · ห้ามลงทับ Paint Coating และห้ามลงทับด้วยแว็กซ์</div><p>ผิวเดียวเลือกได้สายเดียว — ผิวที่เคย Paint Coating หรือแว็กซ์มาก่อน EasyClean จะเกาะไม่ดี และผิวที่เคลือบ EasyClean แล้วก็<b>ลง Paint Coating ทับไม่ได้</b> ดูแลด้วยน้ำเปล่าหรือน้ำยาฤทธิ์กลาง ห้ามขัดด้วยแปรงแข็งหรือฝอยขัด</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">ผิวของคุณ<em>ใช่งานของตัวนี้ไหม</em></h2>
    <p class="sec-sub">เทคโนโลยีเคลือบผิวไม่มีตัวไหนเก่งทุกงาน — สองตัวนี้อาจตรงกับงานคุณมากกว่า</p>
    <div class="altgrid">
      <a class="altcard" href="/paintcoating">
        <div class="k">แผงและหลังคากลางแจ้ง · สาย SELF-CLEANING</div>
        <h4>Paint Coating</h4>
        <p>ถ้าผิวคือแผง ACP ป้ายปั๊ม หรือตัวถังรถที่ฝนโดนและล้างยาก — ตัวนั้นให้ฝนล้างแทนคน เป็นคนละหลักการกับหน้านี้ ไปตัวนั้นตรงกว่า</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
      <a class="altcard" href="/schutznano9h">
        <div class="k">รถยนต์ส่วนตัว · เคลือบแก้ว</div>
        <h4>Schutz Nano 9H</h4>
        <p>สาย Hydrophobic เหมือนกัน แต่ปรับมาเพื่อสีรถบ้าน — เงาลึกและน้ำเด้งบนตัวถังรถ ถ้างานคือรถส่วนตัว ไปตัวนี้ถูกทาง</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">สั่งซื้อ <em>EasyClean</em></h2>
    <div class="ordercard">
      <h3>ช่วงเปิดตัว — สั่งผ่านแชทเท่านั้น</h3>
      <div class="sub">สินค้านำเข้าล็อตแรก ยังไม่ขึ้น Shopee / Lazada ในช่วงเปิดตัว — สั่งตรงผ่านแชทได้ราคาตามตารางด้านบน แจ้งชนิดผิวและพื้นที่ (ตร.ม.) มาได้เลย ทีมงานคำนวณปริมาณให้ฟรีก่อนสั่ง · <b>งานใหญ่มีราคาโครงการ</b></div>
      <div class="shoprow">
        <a class="shop" href="https://m.me/lucernapro"><span class="fbadge">f</span> แชทเพจ Facebook</a>
        <a class="shop shop-line" href="https://lin.ee/LpUR3Ld">💬 Line @lucerna</a>
        <a class="shop" href="tel:0970799547">📞 097-079-9547</a>
      </div>
    </div>
  </div>
</section>

<section class="reads">
  <div class="wrap">
    <h2 class="sec-h">ยังไม่รีบ? <em>อ่านต่ออีกหน่อย</em></h2>
    <p class="sec-sub">อยากรู้ว่าวัตถุดิบตัวนี้มาจากไหนและผ่านอะไรมาบ้าง — สองเรื่องนี้พาไปดูถึงต้นทาง</p>
    <div class="readgrid">
      <a class="readcard" href="/post/solar-panel-defender-feibo-lab">
        <div class="k">เบื้องหลังวัตถุดิบ</div>
        <h4>พาไปดูห้องแล็บ Feibo — ต้นทางวัตถุดิบเคลือบผิวของเรา</h4>
        <p>ห้องปฏิบัติการ เครื่องมือวิเคราะห์ และผลทดสอบจริงของผู้ผลิต Raw Material ที่เราเลือกนำเข้า — เห็นแล้วจะเข้าใจว่าทำไมเราถึงเลือกที่นี่</p>
        <div class="go">อ่านต่อ →</div>
      </a>
      <a class="readcard" href="/post/feibo-rail-transit">
        <div class="k">เคสหน้างาน · ระบบราง</div>
        <h4>รถไฟความเร็วสูง รถไฟใต้ดิน รถราง — งานที่ต้องผ่านมาตรฐานไฟ EN 45545-2</h4>
        <p>ตัวถังรถไฟใช้สาย Self-Cleaning ส่วน EasyClean ผ่านมาตรฐานไฟระดับเดียวกับวัสดุตู้โดยสาร — ภาพชุดจากหน้างานระบบรางที่ผู้พัฒนาวัตถุดิบทำจริง</p>
        <div class="go">อ่านต่อ →</div>
      </a>
    </div>
    <div class="readall"><a class="btn btn-orange" href="/casestudy">ดูเคสหน้างานทั้งหมด →</a></div>
  </div>
</section>
'''

BODY['en'] = r'''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Protection <b>· Coatings</b></div>
      <div class="flagtag">★ NEW</div>
      <h1>Easy<span class="o">Clean</span><br>Anti-Fouling, Easy-Clean, Antibacterial Coating</h1>
      <p class="lede">Latex-painted walls, wood-finished doors and frames, baked-enamel furniture, metal cabinets and panels — one application forms a clear, thin 4H-hard film, and from then on <b>water beads off, oily grime and spray paint struggle to stick, and stains wipe away with a damp cloth</b>. Resists acid, alkali and petrol, cuts static so less dust settles, and inhibits bacterial growth on the surface.</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">Order / pricing</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>Free site consultation</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/easyclean-hero-sq.webp" alt="EasyClean anti-fouling easy-clean coating — hydrophobic surface with water beading into droplets" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">Why a coated surface <em>wipes clean</em></h2>
    <p class="sec-sub">A low-surface-energy nano polysiloxane film — water, oil and grime don't soak into the surface, so they sit on the film and wipe off</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>Water beads off — stains don't soak in</h4><p>Water contact angle ≥110° and sliding angle 5–10° — droplets bead up and roll away. Tea, coffee, sauce or ink spilled on a wall or table leaves no ring, because it never gets into the paint.</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>Resists oily grime and spray paint</h4><p>Hand grease, kitchen fumes, marker pen and spray paint sit on the film instead of the paint — wipe them off with a damp cloth or a neutral cleaner. The manufacturer tests dye-penetration resistance (anti-graffiti) as part of the specification.</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>4H hard — resists acid, alkali and petrol</h4><p>An 8–12 µm film with ≥4H pencil hardness. 24 hours in 10% sulphuric acid and 10% caustic soda, 24 hours in petrol — hardness and adhesion unchanged, so the paint underneath is protected from frequent washing and cleaning chemicals.</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>Less static, inhibits bacteria</h4><p>The film reduces the charge that builds up on paint and plastics, so dust and lint settle less — and when water and organic grime can't get a grip, bacteria lose the foothold and moisture they need to grow (a manufacturer-stated property — not a disinfectant, see Straight Talk no. 5).</p></div></div>
    </div>
  </div>
</section>

<section class="howto" id="proof">
  <div class="wrap">
    <h2 class="sec-h">See it first — <em>one tile, half coated, half not</em></h2>
    <p class="sec-sub">Permanent marker on both halves of the same tile, then wiped the same way — on the EasyClean half the ink sits on the film and wipes off far more easily; on the bare half it bites into the surface</p>
    <div class="vidgrid vert solo">
      <figure>
        <div class="fbv v916"><iframe src="https://www.facebook.com/plugins/video.php?height=476&href=https%3A%2F%2Fwww.facebook.com%2Freel%2F862710706836529%2F&show_text=false&width=267&t=0" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" loading="lazy" title="Permanent-marker test on a tile — EasyClean-coated half vs uncoated half"></iframe></div>
        <figcaption>Permanent-marker test — marked on both halves, wiped the same way, see which side comes clean first</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="buybox" id="compare">
  <div class="wrap">
    <h2 class="sec-h">EasyClean vs Paint Coating — <em>opposite principles</em></h2>
    <p class="sec-sub">Both come from the same raw-material developer and both go on painted surfaces, but they work <b>in opposite ways</b> — choose by who does the washing: the rain, or a person</p>
    <div class="cmp">
      <table>
        <thead><tr><th></th><th>EasyClean (this page)</th><th>Paint Coating</th></tr></thead>
        <tbody>
          <tr><td>Principle</td><td>Hydrophobic — water beads and rolls away</td><td>Superhydrophilic — water sheets and runs off as one film</td></tr>
          <tr><td>Water contact angle</td><td>≥ 110°</td><td>&lt; 10°</td></tr>
          <tr><td>Who cleans</td><td>A person — grime wipes off with a damp cloth</td><td>Rain and sun — rain washes without streaks, sunlight breaks down oil</td></tr>
          <tr><td>Film</td><td>8–12 µm, ≥4H, resists acid, alkali, petrol</td><td>Invisibly thin, with a photocatalytic layer</td></tr>
          <tr><td>Best for</td><td>Surfaces people wipe and that get dirty often — interior walls, doors, furniture, kitchens, restrooms, hospitals, schools, cabinets and machinery, walls that get tagged</td><td>Exterior surfaces the rain reaches and that are hard to wash — ACP cladding, fuel-station signage and canopies, bus and train bodies</td></tr>
          <tr><td>Application</td><td>4-inch foam roller, one thin coat</td><td>Short-nap roller / spray / wipe</td></tr>
          <tr><td>Can they be layered?</td><td colspan="2">No — one surface, one family. A hydrophobic film stops Paint Coating from bonding</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">If the job is "let the rain do the washing" on exterior panels or a canopy, go to <a href="/paintcoating" style="color:var(--orange)">Paint Coating</a> — if the job is "make grime wipe off easily and protect the paint from frequent washing", you're on the right page.</p>
  </div>
</section>

<section class="story">
  <div class="wrap">
    <div class="rdtag">SOURCE — where the raw material comes from</div>
    <h2>We import the core raw material<br>directly from the technology's developer <b>— Feibo</b></h2>
    <div class="story-grid">
      <div class="bignum">≥110°<small>WATER CONTACT ANGLE · HYDROPHOBIC</small></div>
      <div class="story-body">
        <p>For this product we <b>import the core raw material from Feibo</b> (Changsha, China) — the same developer behind our <a href="/en/glasscoating" style="color:var(--orange)">Glass Coating</a> and <a href="/en/paintcoating" style="color:var(--orange)">Paint Coating</a> — and pack and quality-control it in Thailand. But this one is <b>a different family</b> from the Self-Cleaning range: a hydrophobic anti-fouling film designed for surfaces people wipe, not surfaces that wait for rain.</p>
        <p>In China this formulation goes on surfaces that get dirty and are cleaned with chemicals so often that the paint fails early — and it passes the rail-vehicle fire-safety standard (EN 45545-2, R1 HL3), so it can be used in passenger cars and other work that needs a non-flame-spreading material.</p>
        <div class="beats">
          <div class="beat"><div class="k">How it works</div><p>A nano polysiloxane film with a fractal structure, doped with nano tungsten trioxide and nano tin oxide — low surface energy, so water and oil don't spread on the surface; they bead up and wipe off. The manufacturer rates the film at <b>2–3 years</b> with virtually no change in properties.</p></div>
          <div class="beat"><div class="k">Surfaces it suits</div><p>Interior latex paint, wood finishes, baked enamel, industrial spray finishes, bare metal and powder coat — <b>paint that is fully dry and cured</b>. Interior and exterior (3,000 h outdoor weathering test).</p></div>
          <div class="beat"><div class="k">Harder than you'd expect</div><p>8–12 µm thick, ≥4H pencil hardness on glass and metal, cross-cut adhesion grade 0, and still grade 0–1 after three −30°C ↔ 120°C thermal cycles — a <b>protective layer</b> over the paint against scrubbing and cleaning agents, not just a water-repellent one.</p></div>
          <div class="beat"><div class="k">Less static</div><p>Paint and plastics build up charge and attract dry dust — this film reduces the surface charge, so dust, lint and oil mist settle less in the first place, which means less wiping too.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">The numbers from <em>the test data</em></h2>
    <p class="sec-sub">Specification from the raw-material developer's TDS — not advertising copy</p>
    <div class="speccard">
      <table>
        <thead><tr><th>Property</th><th>Value</th></tr></thead>
        <tbody>
          <tr><td>Water contact angle</td><td>≥ 110°</td></tr>
          <tr><td>Sliding angle</td><td>5–10°</td></tr>
          <tr><td>Film thickness</td><td>8–12 µm · clear, no colour change</td></tr>
          <tr><td>Pencil hardness</td><td>≥ 4H (on glass or metal)</td></tr>
          <tr><td>Cross-cut adhesion</td><td>Grade 0 · grade 0–1 after 3 thermal cycles −30°C / 120°C</td></tr>
          <tr><td>Drying time (25°C)</td><td>Surface dry ≤ 30 min · hard dry ≤ 4 h · full cure 24 h</td></tr>
          <tr><td>Heat cure (factory)</td><td>75°C for 1–2 h</td></tr>
          <tr><td>Water resistance</td><td>240 h in distilled water at 40°C — hydrophobicity unchanged</td></tr>
          <tr><td>Petrol resistance</td><td>24 h immersion — hardness and adhesion unchanged</td></tr>
          <tr><td>Acid and alkali resistance</td><td>10% H₂SO₄ and 10% NaOH, 24 h — unchanged</td></tr>
          <tr><td>Outdoor weathering</td><td>3,000 h — film intact, grade 0–1 on aluminium, minimal loss of gloss or colour</td></tr>
          <tr><td>Fire safety</td><td>Passes EN 45545-2, R1 HL3 (rail vehicles)</td></tr>
          <tr><td>Consumption</td><td>Thin foam-roller coat ≈ 160 m²/kg · manufacturer quotes 15–50 ml/m² for spray or brush</td></tr>
          <tr><td>Shelf life</td><td>1 year unopened · store at 18–25°C away from sunlight and sparks</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">Sizes and pricing</h2>
    <div class="pricecard">
      <table data-calc="1" data-shipping="70">
        <thead><tr><th>Size</th><th>Approximate coverage</th><th>Price</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="16">100 g</td><td>≈ 16 m²</td><td class="pr" data-price="830">830.-</td></tr>
          <tr><td class="sz" data-sqm="80">500 g</td><td>≈ 80 m²</td><td class="pr" data-price="3590">3,590.-</td></tr>
          <tr><td class="sz" data-sqm="160">1 kg</td><td>≈ 160 m²</td><td class="pr" data-price="6600">6,600.-</td></tr>
          <tr data-calc="skip"><td class="sz">Projects<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">buildings / factories / fleets</small></td><td>Large areas</td><td class="pr">Project pricing — ask us</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">Shipping <b>70 THB</b> · coverage per pack assumes <b>one thin coat with a 4-inch foam roller</b> as in the steps below — thinner is better for both the result and the cost · <b>Project pricing for large jobs</b>: tell us the surface type and area in m² via chat and we'll quote and work out the quantity for free before you order</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">How to apply — <em>everything on this page</em></h2>
    <p class="sec-sub">Read to the end before opening the can — <b>a clean, bone-dry surface</b> and <b>no water in the first hour</b> are the two things that decide the whole job</p>
    <ol class="flow">
      <li class="fstep"><h4>Clean, degrease and dry the surface completely</h4><p>Remove all dust, oil, hand grease and water marks. If there is old grease or wax, degrease first — fresh paint must be fully dry and cured to its own specification before coating.</p></li>
      <li class="fstep"><h4>Test a small corner first</h4><p>Apply to an inconspicuous corner of the actual surface, let it cure, then check clarity, adhesion and a water-drop test — especially on glossy dark paint and on chalky latex walls.</p></li>
      <li class="fstep"><h4>Apply one thin, even coat with a 4-inch foam roller</h4><p>Use a <b>4-inch foam roller</b>, working in one direction, one thin coat, no runs, no gaps — thin is the whole point: a thick coat adds nothing, wastes product and can show on glossy dark paint. For large factory jobs an HVLP gun with a 1.0–1.2 mm tip at 0.2 MPa works too. <b>A little gas and a faint alcohol smell on opening the can is normal.</b></p><span class="fchip">4-inch foam roller</span><span class="fchip">One thin coat</span><span class="fchip">Factory: HVLP gun</span></li>
      <li class="fstep"><h4>Never go back over it — the surface sets immediately</h4><p>The surface starts hardening as soon as it's applied and is touch-dry in 20–30 minutes — apply and leave it. Re-rolling or re-brushing a spot marks the film.</p></li>
      <li class="fstep"><h4>Keep water off until the film has hardened</h4><p><b>Water on the surface before the film hardens leaves marks</b> that won't wipe off — strip and recoat. The manufacturer says keep it dry for at least the first hour; outdoors, check the rain forecast first.</p><span class="fchip">Touch-dry 20–30 min</span><span class="fchip">Hard dry ≤ 4 h</span></li>
      <li class="fstep"><h4>24 hours — fully cured and in service</h4><p>Fully cured in 24 hours at room temperature (factory work can heat-cure at 75°C for 1–2 hours instead). After that, clean as normal with a damp cloth or a neutral cleaner.</p></li>
    </ol>

    <div class="warn"><b>⚠ Safety:</b> Solvent-based and flammable — work in a ventilated area away from sparks and heat, wear gloves, goggles and an organic-vapour respirator when spraying. Store at 18–25°C out of reach of children and direct sunlight.</div>
  </div>
</section>

<section class="story" id="straight">
  <div class="wrap">
    <div class="rdtag">STRAIGHT TALK — what needs saying</div>
    <h2>Before you pay, read these 6 points —<br><b>this is not a miracle product</b> and we don't want you to misunderstand it</h2>
    <div class="story-grid">
      <div class="bignum">6<small>things most sellers won't tell you</small></div>
      <div class="story-body">
        <div class="beats">
          <div class="beat"><div class="k">1 · You still wipe — it's just much easier</div><p>This is not self-cleaning; the rain won't do it for you, and a coated surface still gets dirty. The difference is that <b>grime sits on the film instead of soaking into the paint</b>, so it wipes off with a damp cloth instead of scrubbing or repainting. If the job is exterior panels you want the rain to look after, go to <a href="/en/paintcoating" style="color:var(--orange)">Paint Coating</a>.</p></div>
          <div class="beat"><div class="k">2 · The first hour is the danger zone</div><p>Water on the surface before the film hardens = <b>marks that won't wipe off</b> — strip and redo. Outdoors, check the rain forecast; indoors, keep splashes away and don't mop near the wall in the first hour.</p></div>
          <div class="beat"><div class="k">3 · A thicker coat is not a tougher coat</div><p>The coverage in the table assumes <b>one thin coat with a foam roller</b> — going thick or doing two coats adds no anti-fouling, wastes product and can show on glossy dark paint. If the roller starts to drag, it has run dry: reload it, don't press harder.</p></div>
          <div class="beat"><div class="k">4 · The paint must be fully cured, and always test a corner</div><p>Fresh paint, chalking paint or flaking latex — the film bonds to whatever is loose, not to the wall. This product <b>protects paint that is still good</b>; it doesn't repair paint that has failed. On glossy dark paint an over-thick coat can be visible, so test a small corner on the real colour every time.</p></div>
          <div class="beat"><div class="k">5 · "Inhibits bacteria" is not "kills germs"</div><p>The manufacturer states that the coating inhibits bacterial growth on the surface, which comes from water and organic grime struggling to stick — <b>it is not a disinfectant and doesn't replace cleaning</b>. Hospitals, kitchens and restrooms keep their normal cleaning schedule; it's just easier.</p></div>
          <div class="beat"><div class="k">6 · Don't put it over Paint Coating, and don't wax over it</div><p>One surface, one family — EasyClean won't bond well over a surface that has had Paint Coating or wax, and a surface coated with EasyClean <b>can't take Paint Coating on top</b>. Care with plain water or a neutral cleaner; no stiff brushes or scouring pads.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">Is this the <em>right product for your surface?</em></h2>
    <p class="sec-sub">No surface coating is best at everything — these two may fit your job better</p>
    <div class="altgrid">
      <a class="altcard" href="/en/paintcoating">
        <div class="k">Exterior panels and canopies · SELF-CLEANING</div>
        <h4>Paint Coating</h4>
        <p>If the surface is ACP cladding, a fuel-station sign or a vehicle body that the rain reaches and that's hard to wash — that one lets the rain do the washing. A different principle from this page, and the better fit there.</p>
        <div class="go">View details →</div>
      </a>
      <a class="altcard" href="/en/schutznano9h">
        <div class="k">Private cars · Ceramic coating</div>
        <h4>Schutz Nano 9H</h4>
        <p>Hydrophobic as well, but formulated for car paint — deep gloss and beading on a car body. If the job is your own car, that's the right one.</p>
        <div class="go">View details →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">Order <em>EasyClean</em></h2>
    <div class="ordercard">
      <h3>Launch period — order via chat only</h3>
      <div class="sub">First imported batch, not yet on Shopee / Lazada during launch — order directly via chat at the prices in the table above. Tell us the surface type and area in m² and we'll work out the quantity for free before you order · <b>Project pricing for large jobs</b></div>
      <div class="shoprow">
        <a class="shop" href="https://m.me/lucernapro"><span class="fbadge">f</span> Facebook chat</a>
        <a class="shop shop-line" href="https://lin.ee/LpUR3Ld">💬 Line @lucerna</a>
        <a class="shop" href="tel:0970799547">📞 097-079-9547</a>
      </div>
    </div>
  </div>
</section>

<section class="reads">
  <div class="wrap">
    <h2 class="sec-h">Not in a hurry? <em>Read a little more</em></h2>
    <p class="sec-sub">Where this raw material comes from and what it has been through — these two take you to the source</p>
    <div class="readgrid">
      <a class="readcard" href="/en/post/solar-panel-defender-feibo-lab">
        <div class="k">Behind the raw material</div>
        <h4>Inside the Feibo lab — the source of our surface-coating raw materials</h4>
        <p>The laboratory, the analytical equipment and the real test results of the raw-material producer we chose to import from — see it and you'll understand why we chose them.</p>
        <div class="go">Read on →</div>
      </a>
      <a class="readcard" href="/en/post/feibo-rail-transit">
        <div class="k">Site case · Rail</div>
        <h4>High-speed rail, metro, trams — work that has to pass the EN 45545-2 fire standard</h4>
        <p>Train bodies use the Self-Cleaning family, while EasyClean passes the same fire standard as passenger-car materials — a photo set from real rail work by the raw-material developer.</p>
        <div class="go">Read on →</div>
      </a>
    </div>
    <div class="readall"><a class="btn btn-orange" href="/en/casestudy">See all field cases →</a></div>
  </div>
</section>
'''

if __name__ == '__main__':
    build('th')
    build('en')
