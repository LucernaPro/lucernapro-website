#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_floorarmour_page.py — สร้าง /floorarmour และ /en/floorarmour

FloorArmour — สีทากระเบื้องห้องน้ำกันซึม รุ่นประหยัด (DIY tier ใต้ TileCoat Polyurea)
Pist 26 ก.ย. 2026: "ประโยชน์ทุกอย่างเหมือน tilecoat แหละ แต่บอกตรงๆ ไปเลยว่ายังไงก็กันลื่นเท่ากระเบื้องหยาบไม่ได้
มีเม็ดกันลื่นก็จริง … data ทุกอย่างคือเหมือน pondmax เลย … แต่ชื่อเคมีห้ามบอกเด็ดขาดว่าคือ epoxy"
→ เรียกเคมีว่า "Polymer 2 ส่วนผสม" (คำ fallback ของเว็บ) · ตัวเลขใช้งาน = ผสม 2:1 โดยน้ำหนัก, pot life ~15 นาที,
  ทา 2 รอบ ห่าง ~6 ชม., 1 kg ≈ 5 ตร.ม. (2 รอบ), Full cure 2–3 วัน, ทาบนผิวชื้น/หมาดได้ (ห้ามน้ำขัง)
🔴 Pist: "ห้ามเขียนโยงเด็ดขาด" — ห้ามเอ่ยชื่อสินค้าตัวอื่นที่ใช้เคมีเดียวกัน ห้ามพูดถึงบ่อปลา ห้ามคำ Epoxy ทั้งหน้า
ขนาด/ราคา: 1 kg 990 บาท ขนาดเดียว · ค่าส่ง 130 · สีเทากลางสีเดียว (ไม่ทำหลายสี)
🔴 ห้ามเล่าประวัติชื่อเก่า/รุ่นแรก (Pist 26 ก.ย. 2026 "ใส่มาทำไมเนี่ย") — section story ถูกตัดออกทั้ง TH/EN
รูป: hero/card เป็น placeholder ที่ Claude ทำ (แผ่นสีเทา+เม็ดกันลื่น) รอรูปจริงจาก Pist · ยังไม่มีแกลเลอรี/คลิป
ช่องทางสั่งซื้อ: แชทเพจ + Line + โทร (ยังไม่มี listing Shopee/Lazada — ทวง Pist)
chrome ยกจาก /tilecoatpoly (golden master) — CSS ครบทุก class ที่ใช้
วิธีใช้: python3 tools/build_floorarmour_page.py → python3 tools/build_calculator_page.py → python3 tools/gen_search_index.py → python3 tools/gen_sitemap.py
"""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def chrome(src):
    s = io.open(src, encoding='utf-8').read()
    head = s[:s.index('</head>')]
    i_body = s.index('<body>')
    # ตัดตรงก่อน hero: ลิ้นชักปิดด้วย marker คนละข้อความใน TH/EN
    drawer = s[i_body:s.index('<section class="phero">')].rstrip() + '\n'
    tail = s[s.index('<section class="explore">'):]
    return head, drawer, tail


def build(lang):
    src = 'tilecoatpoly/index.html' if lang == 'th' else 'en/tilecoatpoly/index.html'
    head, drawer, tail = chrome(src)
    head = head.replace('/tilecoatpoly', '/floorarmour')
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE[lang], head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % DESC[lang], head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % OGT[lang], head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % OGD[lang], head)
    head = head.replace('img/tilecoatpoly-hero.webp', 'img/floorarmour-hero.webp')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', SCHEMA[lang], head, flags=re.S)
    # HIDDEN 26 ก.ย. 2026 (มติเจ้าของ "ซ่อนจาก public ก่อน เข้าได้เฉพาะคนมี link"): noindex + ถอดการ์ดหน้าแรก/finder/sitemap/search — ลบบรรทัดถัดไปเมื่อจะเปิด public แล้วใส่การ์ด/finder กลับ
    head = head.replace('<meta name="viewport"', '<meta name="robots" content="noindex,nofollow">\n<meta name="viewport"', 1)
    head += EXTRA_CSS
    drawer = drawer.replace('/tilecoatpoly', '/floorarmour')
    tail = tail.replace('/tilecoatpoly', '/floorarmour')
    out = head + '</head>\n' + drawer + '\n\n' + BODY[lang] + '\n' + tail
    dst = 'floorarmour/index.html' if lang == 'th' else 'en/floorarmour/index.html'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    io.open(dst, 'w', encoding='utf-8').write(out)
    print('wrote', dst, len(out))


EXTRA_CSS = '''
<style id="floorarmour-css">
  .cmp{margin-top:26px;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--panel)}
  .cmp table{width:100%;border-collapse:collapse;font-size:14px}
  .cmp th,.cmp td{padding:11px 14px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
  .cmp th{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;color:var(--muted);font-weight:600}
  .cmp tr:last-child td{border-bottom:0}
  .cmp td:first-child{color:var(--muted);white-space:nowrap}
  .cmp td b{color:var(--ink)}
  .cmp .me{color:var(--orange);font-weight:700}
  .cmp-h{font-family:var(--disp);font-size:17px;margin:26px 0 0}
  .cmp-sub{font-size:13.5px;color:var(--muted);margin:4px 0 0;line-height:1.55}
  @media(max-width:600px){.cmp th,.cmp td{padding:9px 10px;font-size:13px}.cmp td:first-child{white-space:normal}}
</style>'''

TITLE = {
    'th': 'FloorArmour สีทากระเบื้องห้องน้ำกันซึม รุ่นประหยัด 1 กก. 990 บาท — ไม่ต้องรื้อกระเบื้อง | LucernaPro',
    'en': 'FloorArmour — Budget Waterproof Bathroom Tile Coating, 1 kg 990 THB, No Tile Removal | LucernaPro',
}
DESC = {
    'th': 'FloorArmour สีทากระเบื้องห้องน้ำกันซึมรุ่นประหยัด — Polymer 2 ส่วนผสมที่เราใช้ทับกระเบื้องมาหลายปี ทนชื้น ทาบนผิวหมาดได้ ยึดเกาะกระเบื้องเคลือบ กันซึมในตัว มีเม็ดกันลื่น สีเทากลาง 1 กก. ทาได้ 5 ตร.ม. ราคา 990 บาท ทำเองได้',
    'en': 'FloorArmour — the budget waterproof bathroom tile coating. A two-part polymer we have used over tile for years: moisture-tolerant, applies on damp surfaces, bonds to glazed tile, waterproof in itself, anti-slip grit included. Mid grey, 1 kg covers 5 m², 990 THB. Do it yourself.',
}
OGT = {
    'th': 'FloorArmour สีทากระเบื้องห้องน้ำกันซึม รุ่นประหยัด — 1 กก. 990 บาท',
    'en': 'FloorArmour — Budget Waterproof Bathroom Tile Coating, 990 THB',
}
OGD = {
    'th': 'ห้องน้ำรั่ว กระเบื้องเก่า ไม่ต้องรื้อ — Polymer 2 ส่วนผสม ทนชื้น ทาบนผิวหมาดได้ กันซึมในตัว มีเม็ดกันลื่น สีเทากลาง 1 กก. ≈ 5 ตร.ม.',
    'en': 'Leaking bathroom, tired tile, no demolition — a moisture-tolerant two-part polymer, waterproof in itself, anti-slip grit included. Mid grey, 1 kg ≈ 5 m².',
}
SCHEMA = {
    'th': '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Product","name":"FloorArmour สีทากระเบื้องห้องน้ำกันซึม รุ่นประหยัด","brand":{"@type":"Brand","name":"LucernaPro"},"description":"สีทากระเบื้องห้องน้ำกันซึมรุ่นประหยัด Polymer 2 ส่วนผสม ทนชื้น ทาบนผิวหมาดได้ ยึดเกาะกระเบื้องเคลือบ กันซึมในตัว มีเม็ดกันลื่น สีเทากลาง 1 กก. ≈ 5 ตร.ม.","image":"https://www.lucernapro.com/img/floorarmour-hero.webp","url":"https://www.lucernapro.com/floorarmour","color":"Grey","offers":{"@type":"Offer","priceCurrency":"THB","price":"990","availability":"https://schema.org/InStock","url":"https://www.lucernapro.com/floorarmour"}}
</script>''',
    'en': '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Product","name":"FloorArmour Budget Waterproof Bathroom Tile Coating","brand":{"@type":"Brand","name":"LucernaPro"},"description":"Budget waterproof bathroom tile coating — a moisture-tolerant two-part polymer that bonds to glazed tile, waterproof in itself, anti-slip grit included. Mid grey, 1 kg ≈ 5 m².","image":"https://www.lucernapro.com/img/floorarmour-hero.webp","url":"https://www.lucernapro.com/en/floorarmour","color":"Grey","offers":{"@type":"Offer","priceCurrency":"THB","price":"990","availability":"https://schema.org/InStock","url":"https://www.lucernapro.com/en/floorarmour"}}
</script>''',
}

BODY = {}

BODY['th'] = '''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Waterproof <b>· กันซึม</b></div>
      <div class="flagtag">รุ่นประหยัด · ทำเองได้</div>
      <h1>FloorArmour <span class="o">สีทากระเบื้องห้องน้ำ</span><br>กันซึม รุ่นประหยัด</h1>
      <p class="lede">ห้องน้ำรั่ว กระเบื้องเก่าดูโทรม — ไม่ต้องทุบ ไม่ต้องรื้อ ทาทับกระเบื้องเดิมได้เลย ด้วย Polymer 2 ส่วนผสมที่เราใช้ทับกระเบื้องมาหลายปี <b>ทนชื้นระดับทาบนผิวหมาดได้</b> กันซึมในตัว มีเม็ดกันลื่น สีเทากลาง 1 กก. ทาได้ 5 ตร.ม. — <b>990 บาท</b></p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#order">สั่งซื้อ / ดูราคา</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>ปรึกษาหน้างานฟรี</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/floorarmour-hero.webp" alt="FloorArmour สีเทากลาง — ตัวอย่างเฉดสีพร้อมเม็ดกันลื่นกระจายทั่วผืน" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">ทำไมต้อง <em>FloorArmour</em> — ไม่ใช่สีทั่วไป</h2>
    <p class="sec-sub">สีธรรมดาทาบนกระเบื้องเคลือบแล้วลอก เพราะมันไม่ได้เกิดมาเพื่อห้องน้ำเปียก FloorArmour ใช้ระบบ Polymer 2 ส่วนผสมที่ทนชื้นตั้งแต่ขั้นตอนบ่มตัว</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>ไม่ต้องรื้อกระเบื้อง</h4><p>ข้ามขั้นตอนทุบ-รื้อ-ขนเศษ-ปูใหม่ไปทั้งยวง ประหยัดทั้งเวลา ค่าแรง และไม่ต้องปิดห้องน้ำเป็นอาทิตย์</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>ทนชื้น ทาบนผิวหมาดได้</h4><p>ระบบบ่มตัวทนความชื้นสูง — ห้องน้ำที่ล้างแล้วผิวยังหมาดๆ ทาต่อได้เลยไม่ต้องรอแห้งสนิท ขอแค่ไม่มีน้ำขังเป็นแอ่ง และหลังเซ็ตตัวแล้วเจอความชื้นตลอดวันแบบห้องน้ำเปียกได้สบาย</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>ยึดเกาะกระเบื้องเคลือบ — ใช้จริงมาหลายปี</h4><p>Polymer ตัวนี้เราทาทับกระเบื้องมาหลายปีก่อนจะเอามาทำ FloorArmour ไม่ใช่สูตรใหม่ที่เพิ่งออกจากแล็บ — เกาะผิวเคลือบมันวาวได้จริงโดยไม่ต้องมีรองพื้นแยก</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>กันซึมในตัว จบที่ 990</h4><p>ไม่ใช่แค่เปลี่ยนสีกระเบื้อง แต่ได้ชั้นกันซึมต่อเนื่องปิดทั้งหน้ากระเบื้องและร่องยาแนวไปพร้อมกัน — ห้องน้ำขนาดทั่วไป 1 กก. เดียวเอาอยู่</p></div></div>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">ขนาดและราคา</h2>
    <div class="pricecard">
      <table data-calc="1" data-shipping="130">
        <thead><tr><th>ขนาด</th><th>พื้นที่ใช้งานโดยประมาณ</th><th>ราคา</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="5">1 kg</td><td>≈ 5 ตร.ม. (ทา 2 รอบ)</td><td class="pr" data-price="990">990.-</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">ขนาดเดียว 1 กก. — น้ำหนักรวม Part A + Part B ตวงมาให้ลงตัวกับอัตราผสม 2:1 แล้ว · ค่าจัดส่ง 130 บาท · ห้องน้ำใหญ่กว่า 5 ตร.ม. สั่งหลายกระป๋องได้ ส่งขนาดพื้นที่มาทางแชทเพจ เราคำนวณให้ฟรีก่อนสั่งซื้อครับ</p>

    <div class="colors">
      <h3 class="colors-h">สีเดียว — เทากลาง</h3>
      <div class="swatches">
        <div class="swx"><span class="sw" style="background:#8A8F94"></span>เทากลาง</div>
      </div>
      <p class="colornote">FloorArmour ทำสีเดียวเพื่อคุมราคา — เทากลางเข้าได้กับกระเบื้องผนังแทบทุกโทน และซ่อนคราบได้ดีกว่าขาว · เฉดบนหน้าจอเป็นค่าโดยประมาณ · อยากได้สีอื่น ดู <a href="/tilecoatpoly" style="color:var(--orange)">TileCoat Polyurea</a> ที่มีให้เลือก 6 สี</p>
    </div>

    <h3 class="cmp-h">FloorArmour กับ TileCoat Polyurea ต่างกันตรงไหน</h3>
    <p class="cmp-sub">งานเดียวกัน ทาทับกระเบื้องห้องน้ำเหมือนกัน — ต่างกันที่ของที่ให้มาและงบ ไม่ใช่ที่ความตั้งใจ</p>
    <div class="cmp">
      <table>
        <thead><tr><th></th><th>FLOORARMOUR</th><th>TILECOAT POLYUREA</th></tr></thead>
        <tbody>
          <tr><td>ราคาเริ่มต้น</td><td><b class="me">990.-</b> / 1 กก.</td><td><b>1,190.-</b> / 0.5 กก.</td></tr>
          <tr><td>สี</td><td><b>เทากลาง</b> สีเดียว</td><td><b>6 สี</b> ขาว ครีม เทาอ่อน เทาเข้ม ฟ้าอ่อน ดำ</td></tr>
          <tr><td>รองพื้น</td><td>ไม่มี — <b>ทาตรงได้</b> อยากทนขั้นสุดให้ขัดผิวก่อน</td><td>แถมรองพื้นมาในกล่อง</td></tr>
          <tr><td>เนื้อวัสดุ</td><td>Polymer 2 ส่วนผสม ทนชื้น</td><td>Polyurea สายเรือธง</td></tr>
          <tr><td>เหมาะกับ</td><td>ซ่อมห้องน้ำรั่วเอง คุมงบ</td><td>งานรีโนเวทที่อยากเลือกสี และงานที่พลาดไม่ได้</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">วิธีใช้งาน</h2>
    <p class="sec-sub">จบบนหน้านี้ครบทุกตัวเลข — หัวใจของระบบ Polymer 2 ส่วนผสมมีสองข้อ: ตวงให้เป๊ะ กับ ทำงานให้ทันเวลา ที่เหลือระบบจัดการเอง</p>
    <ol class="flow">
      <li class="fstep"><h4>เตรียมพื้นผิว</h4><p>ล้างคราบสบู่ คราบไขมัน และตะไคร่ให้เกลี้ยง — ผิวชื้นหรือหมาดๆ ทาได้เลย แต่<b>ห้ามมีน้ำขังเป็นแอ่งเด็ดขาด</b> / อยากให้ทนขั้นสุด: ขัดผิวกระเบื้องให้สากด้วยกระดาษทรายก่อนทา ลูบแล้วสากมือ ไม่มีผงติดมือ — FloorArmour เกาะได้อยู่แล้ว แต่ผิวสากคือเปอร์เซ็นต์ที่เพิ่มให้งานสมบูรณ์แบบ</p></li>
      <li class="fstep"><h4>ซ่อมยาแนวให้เต็มทุกร่อง</h4><p>จุดที่ยาแนวแหว่ง หลุด หรือแตกร้าว ต้องซ่อมให้เต็มเรียบร้อยก่อน<b>เสมอ</b> — ข้ามขั้นนี้ไป ต่อให้สีดีแค่ไหนระบบกันซึมก็ไม่ได้ผล</p></li>
      <li class="fstep"><h4>ใส่ถุงมือและแว่นตาก่อนเปิดกระป๋อง</h4><p>Part B ก่อนเซ็ตตัวเป็นสารระคายเคืองต่อผิวหนังและดวงตา — ใส่ถุงมือและแว่นตาทุกครั้งที่ผสมและทา ทำงานในที่อากาศถ่ายเท (พอเซ็ตตัวเต็มที่แล้วปลอดภัยตามปกติ)</p></li>
      <li class="fstep"><h4>เขย่า Part A แล้วตวง 2:1 กวนให้เข้ากันจริงๆ</h4><p><b>ก่อนเท: ในกระป๋อง Part A มีเม็ดกันลื่นผสมอยู่ เม็ดจะตกไปกองก้นกระป๋อง — เขย่าเบาๆ ให้เม็ดกระจายก่อนเททุกครั้ง</b> แล้วผสม A 2 ส่วน : B 1 ส่วน โดยน้ำหนัก ตวงด้วยตาชั่ง ห้ามกะด้วยสายตา กวนให้เข้าเป็นเนื้อเดียว กวาดก้นและขอบภาชนะให้ทั่ว — เนื้อที่ผสมไม่ทั่วคือจุดที่สีไม่แห้ง</p><span class="fchip">Part A : Part B = 2 : 1 โดยน้ำหนัก</span></li>
      <li class="fstep"><h4>ทารอบแรก — แข่งกับเวลา</h4><p>ผสมเสร็จมีเวลาทำงาน ~15 นาที — ลงลูกกลิ้งหรือแปรงทันที ไล่แนวไปข้างหน้าให้ฟิล์มต่อเนื่อง เก็บมุม ร่องยาแนว และรอบท่อระบายน้ำให้ครบ อย่าผสมทีเดียวทั้งกระป๋องถ้าทาไม่ทัน แบ่งผสมทีละชุด</p><span class="fchip">เวลาทำงาน ~15 นาที</span></li>
      <li class="fstep"><h4>รอ ~6 ชม. แล้วทารอบสอง</h4><p>ปล่อยรอบแรกแห้งประมาณ 6 ชั่วโมง แล้วทาทับรอบที่สอง — มาตรฐานคือ 2 รอบ (1 กก. ≈ 5 ตร.ม. คือตัวเลขแบบครบ 2 รอบแล้ว) เขย่ากระป๋องก่อนเทอีกครั้งเหมือนเดิม</p><span class="fchip">ห่างกัน ~6 ชั่วโมง</span></li>
      <li class="fstep"><h4>รอเซ็ตตัวเต็มที่ แล้วค่อยใช้น้ำ</h4><p>เดินเบาๆ ได้เมื่อฟิล์มแห้งสนิท แต่แนะนำให้รอ Full Cure 2–3 วันก่อนกลับมาใช้ห้องน้ำแบบเปียกตามปกติ — ความใจเย็น 2–3 วันคือของขวัญให้ฟิล์มแกร่งเต็มกำลัง</p><span class="fchip">Full Cure 2–3 วัน</span></li>
    </ol>
    <div class="note"><b>เรื่องกันลื่น — พูดกันตรงๆ:</b> เนื้อสีมีเม็ดกันลื่นช่วยเพิ่มแรงเสียดทานอยู่แล้ว แต่<b>ยังไงก็หนืดไม่เท่ากระเบื้องผิวหยาบ</b> — พื้นเปียกยังต้องเดินอย่างระมัดระวังเช่นเดิม และเม็ดพวกนี้ตกก้นกระป๋อง <b>เขย่ากระป๋องเบาๆ ก่อนเททุกครั้ง</b> ไม่งั้นเม็ดค้างอยู่ก้น ทาไปแล้วไม่ได้กันลื่น</div>
    <div class="warn"><b>⚠ ข้อควรระวัง:</b> ไม่เหมาะกับผู้ที่แพ้สารเคมี/เคมีภัณฑ์ — หากมีอาการแพ้ ไม่ควรทาด้วยตัวเอง แนะนำให้ช่างเป็นผู้ดำเนินการ และทำงานในที่อากาศถ่ายเทเสมอ</div>
  </div>
</section>

<section class="chemfaq">
  <div class="wrap">
    <h2 class="sec-h">คำถามยอดฮิต: <em>ทนน้ำยาล้างห้องน้ำไหม?</em></h2>
    <p class="sec-sub">น้ำยาล้างห้องน้ำส่วนใหญ่เป็นกรดแรง — แรงขนาดที่ผิวกระเบื้องกับยาแนวแท้ๆ ยังโดนกัดจนด้าน คำตอบสั้นๆ คือ "ใช้เป็นครั้งคราวได้" แต่เรื่องที่อยากให้รู้มากกว่านั้นคือ ทาแล้วคุณแทบไม่ต้องใช้มันอีกเลย</p>
    <div class="chemgrid">
      <div class="chembox">
        <div class="k">ข่าวดีที่สุด</div>
        <h4>ทาแล้วแทบไม่ต้องใช้น้ำยากรดอีก</h4>
        <p>ผิวเคลือบ FloorArmour ต่อเนื่องทั้งผืน ปิดทั้งหน้ากระเบื้องและร่องยาแนวไว้ใต้ฟิล์มเดียวกัน ไม่เหลือร่องให้คราบฝังตัว คราบส่วนใหญ่แปรงออกด้วยน้ำเปล่าหรือน้ำสบู่อ่อนๆ — ต้นเหตุที่ทำให้ต้องพึ่งกรดแรงหายไปตั้งแต่แรก</p>
      </div>
      <div class="chembox">
        <div class="k">ถ้าอยากใช้จริงๆ</div>
        <h4>ใช้เป็นครั้งคราวได้ แล้วราดน้ำตาม</h4>
        <p>ฟิล์ม Polymer 2 ส่วนผสมทนสารเคมีทำความสะอาดในบ้านได้ดี ใช้น้ำยาล้างห้องน้ำเป็นครั้งคราวแล้วราดน้ำล้างให้สะอาดได้ตามปกติ ไม่ต้องแช่ทิ้งไว้</p>
      </div>
      <div class="chembox">
        <div class="k">พูดกันตรงๆ</div>
        <h4>โดนกรดแรงบ่อยๆ อายุฟิล์มสั้นลง</h4>
        <p>กรดแรงกัดทุกพื้นผิวที่เจอ ไม่เว้นแม้แต่กระเบื้อง โดนซ้ำบ่อยๆ ฟิล์มเคลือบก็เสื่อมเร็วกว่าปกติเช่นกัน ถ้าอยากให้อยู่ด้วยกันนานที่สุด น้ำยาทำความสะอาดทั่วไปสูตร pH เป็นกลางก็เอาอยู่แล้ว</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">ไม่ใช่งานของ FloorArmour? <em>มีทางเลือกอื่น</em></h2>
    <p class="sec-sub">อยากได้สีอื่น อยากเก็บลายกระเบื้องเดิม หรือแค่ยาแนวเสีย — สามตัวนี้รับช่วงต่อ</p>
    <div class="altgrid">
      <a class="altcard" href="/tilecoatpoly">
        <div class="k">อยากเลือกสี · ตัวเรือธง</div>
        <h4>TileCoat Polyurea</h4>
        <p>สีทากระเบื้องกันซึมตัวเรือธง 6 สี แถมรองพื้นมาในกล่อง — งานรีโนเวทที่อยากเลือกโทนเอง เริ่ม 1,190 บาท</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
      <a class="altcard" href="/epoxygrout">
        <div class="k">แก้ที่ยาแนว</div>
        <h4>ยาแนวกันซึม Epoxy</h4>
        <p>เปลี่ยนแค่ยาแนวเดิมเป็นยาแนวกันซึม ก็ปิดทางน้ำซึมได้โดยกระเบื้องเดิมอยู่ครบทุกแผ่น</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
      <a class="altcard" href="/polyaspartic">
        <div class="k">กันซึมแบบใส ระดับ TOP</div>
        <h4>กันซึมใส Polyaspartic</h4>
        <p>เคลือบกันซึมใสทับกระเบื้องเดิม มองไม่เห็นชั้นเคลือบ ได้กันซึมระดับท็อปโดยลายกระเบื้องโชว์เต็มๆ</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">สั่งซื้อ <em>FloorArmour</em></h2>
    <div class="ordercard">
      <h3>สั่งผ่านแชทได้เลย — ทีมงานตอบไว</h3>
      <div class="sub">1 กก. 990 บาท ค่าส่ง 130 บาท — ไม่แน่ใจว่าห้องน้ำของคุณต้องใช้กี่กระป๋อง ส่งขนาดพื้นที่หรือรูปหน้างานมาก่อนได้เลย เราคำนวณและวิเคราะห์ให้ฟรีก่อนโอนครับ</div>
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
    <p class="sec-sub">สามเรื่องที่คนทำงานกระเบื้องถามเราบ่อยที่สุด — เขียนจากหน้างานจริง ไม่ใช่บทความขายของ</p>
    <div class="readgrid">
      <a class="readcard" href="/post/finding-the-real-leak-point">
        <div class="k">ก่อนจะทา</div>
        <h4>หาจุดรั่วให้เจอก่อน แล้วค่อยทากันซึม</h4>
        <p>ทาไปแล้วสองสามรอบน้ำก็ยังซึมอยู่ดี — ปัญหาส่วนใหญ่<b>ไม่ได้อยู่ที่สินค้า</b> แต่อยู่ที่ยังไม่เคยหาจุดรั่วจริงเจอก่อนลงมือ</p>
        <div class="go">อ่านต่อ →</div>
      </a>
      <a class="readcard" href="/post/waterproofing-techniques">
        <div class="k">ทำให้ถูกขั้นตอน</div>
        <h4>เทคนิคการใช้งานกันซึมให้ได้ผลดี</h4>
        <p>กันซึมไม่ใช่ยาวิเศษ — ไล่ตั้งแต่ตรวจหน้างาน ซ่อมรอยร้าว เสริมไฟเบอร์กลาส จนถึงเทคนิคทาสองรอบให้ฟิล์มต่อเนื่องจริง</p>
        <div class="go">อ่านต่อ →</div>
      </a>
      <a class="readcard" href="/post/waterproofing-coverage-tips">
        <div class="k">คุมงบ</div>
        <h4>วิธีทากันซึมให้ประหยัด</h4>
        <p>ซื้อมาถังเดียวแต่ทาไม่ทั่วตามที่ป้ายบอก — ไม่ใช่เพราะเนื้อสีน้อย แต่เป็นเรื่องการเตรียมผิวและเทคนิคทาล้วนๆ</p>
        <div class="go">อ่านต่อ →</div>
      </a>
    </div>
    <div class="readall"><a class="btn btn-orange" href="/casestudy">ดูเคสหน้างานทั้งหมด →</a></div>
  </div>
</section>
'''

BODY['en'] = '''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Waterproof <b>· Waterproofing</b></div>
      <div class="flagtag">BUDGET TIER · DIY</div>
      <h1>FloorArmour <span class="o">Bathroom Tile Coating</span><br>Waterproof, budget tier</h1>
      <p class="lede">Leaking bathroom, tired old tile — no jackhammer, no demolition. Paint straight over the existing tile with a two-part polymer we have used over tile for years. <b>Moisture-tolerant enough to apply on a damp surface</b>, waterproof in itself, anti-slip grit included. Mid grey, 1 kg covers 5 m² — <b>990 THB</b>.</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#order">Order / See price</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>Free on-site advice</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/floorarmour-hero.webp" alt="FloorArmour mid grey — colour sample with anti-slip grit spread across the surface" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">Why <em>FloorArmour</em> — not ordinary paint</h2>
    <p class="sec-sub">Ordinary paint peels off glazed tile because it was never made for a wet bathroom. FloorArmour is built on a two-part polymer system that tolerates moisture from the moment it leaves the can.</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>No tile removal</h4><p>Skip the whole break-remove-haul-retile cycle. Save the time, the labour, and the week with the bathroom out of action.</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>Moisture-tolerant — applies on a damp surface</h4><p>A curing system built for high humidity — wash the bathroom, let it drain, and coat while the surface is still damp. Just no standing puddles. Once set, an all-day-wet bathroom is nothing to it.</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>Bonds to glazed tile — proven over years</h4><p>We had been coating tile with this polymer for years before it became FloorArmour. Not a fresh lab formula — it grips glossy glazed tile for real, with no separate primer.</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>Waterproof in itself, done at 990</h4><p>More than a colour change: one continuous waterproof film over the tile faces and the grout lines together — a typical bathroom floor is covered by a single 1 kg pack.</p></div></div>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">Sizes &amp; prices</h2>
    <div class="pricecard">
      <table data-calc="1" data-shipping="130">
        <thead><tr><th>Size</th><th>Approx. coverage</th><th>Price</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="5">1 kg</td><td>≈ 5 m² (two coats)</td><td class="pr" data-price="990">990.-</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">One size only, 1 kg — that is Part A + Part B together, pre-weighed to the 2:1 mix ratio · Shipping 130 THB · Bathroom bigger than 5 m²? Order more packs, or send us the floor size on Messenger and we'll work it out for free before you buy.</p>

    <div class="colors">
      <h3 class="colors-h">One colour — mid grey</h3>
      <div class="swatches">
        <div class="swx"><span class="sw" style="background:#8A8F94"></span>Mid grey</div>
      </div>
      <p class="colornote">FloorArmour comes in one colour to keep the price down — mid grey suits almost any wall tile and hides marks better than white · On-screen shade is approximate · Want another colour? See <a href="/en/tilecoatpoly" style="color:var(--orange)">TileCoat Polyurea</a>, which comes in six.</p>
    </div>

    <h3 class="cmp-h">FloorArmour vs TileCoat Polyurea</h3>
    <p class="cmp-sub">Same job, same paint-over-the-tile idea — the difference is what comes in the box and the budget, not the intent.</p>
    <div class="cmp">
      <table>
        <thead><tr><th></th><th>FLOORARMOUR</th><th>TILECOAT POLYUREA</th></tr></thead>
        <tbody>
          <tr><td>Starting price</td><td><b class="me">990.-</b> / 1 kg</td><td><b>1,190.-</b> / 0.5 kg</td></tr>
          <tr><td>Colours</td><td><b>Mid grey</b> only</td><td><b>6 colours</b> — white, cream, light grey, dark grey, light blue, black</td></tr>
          <tr><td>Primer</td><td>None — <b>coat directly</b>; sand first for maximum durability</td><td>Primer included in the box</td></tr>
          <tr><td>Material</td><td>Two-part polymer, moisture-tolerant</td><td>Polyurea, our flagship line</td></tr>
          <tr><td>Best for</td><td>Fixing your own leaking bathroom on a budget</td><td>Renovations where you want to pick the colour, and jobs that cannot fail</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">How to apply</h2>
    <p class="sec-sub">Every number is on this page — a two-part polymer comes down to two things: weigh it exactly, and work within the time. The system does the rest.</p>
    <ol class="flow">
      <li class="fstep"><h4>Prepare the surface</h4><p>Wash off soap scum, grease and algae completely — a damp or moist surface is fine, but <b>no standing water anywhere</b>. For maximum durability: rough up the tile with sandpaper first until it feels gritty and leaves no dust on your hand. FloorArmour bonds as it is — a roughened surface is the extra percent that makes the job perfect.</p></li>
      <li class="fstep"><h4>Fill every grout line</h4><p>Any grout that is chipped, missing or cracked must be filled flush <b>first, every time</b> — skip this and no coating on earth will keep the water out.</p></li>
      <li class="fstep"><h4>Gloves and goggles before you open the can</h4><p>Uncured Part B irritates skin and eyes — wear gloves and eye protection whenever you mix and apply, and work with the air moving (fully cured, it is safe as normal).</p></li>
      <li class="fstep"><h4>Shake Part A, weigh 2:1, then really mix</h4><p><b>Before pouring: Part A contains anti-slip grit that settles to the bottom of the can — shake it gently to spread the grit before every pour.</b> Then mix 2 parts A to 1 part B by weight — use a scale, never eyeball it — and stir to one uniform mass, scraping the bottom and sides. Unmixed patches are the spots that never dry.</p><span class="fchip">Part A : Part B = 2 : 1 by weight</span></li>
      <li class="fstep"><h4>First coat — against the clock</h4><p>Once mixed you have about 15 minutes of working time — roller or brush straight away, working forward in one direction for a continuous film, covering corners, grout lines and around the drain. Don't mix the whole can if you can't lay it in time; mix in batches.</p><span class="fchip">~15 min working time</span></li>
      <li class="fstep"><h4>Wait ~6 h, then the second coat</h4><p>Let the first coat dry for about 6 hours, then apply the second — two coats is the standard (1 kg ≈ 5 m² already counts both coats). Shake the can before pouring again, as before.</p><span class="fchip">~6 hours between coats</span></li>
      <li class="fstep"><h4>Let it fully cure before the water goes back on</h4><p>Light foot traffic is fine once the film is dry to the touch, but allow a full cure of 2–3 days before using the bathroom wet as normal — that patience is what gives the film its full strength.</p><span class="fchip">Full cure 2–3 days</span></li>
    </ol>
    <div class="note"><b>On slip resistance — straight talk:</b> the coating contains anti-slip grit that adds real friction, but <b>it will never grip like a textured tile</b> — a wet floor still needs the same care as before. And that grit settles to the bottom of the can: <b>shake gently before every pour</b>, or it stays at the bottom and the coat goes on without it.</div>
    <div class="warn"><b>⚠ Caution:</b> not suitable for anyone sensitive to chemicals — if you react, don't apply it yourself; have a contractor do it. Always work in a well-ventilated space.</div>
  </div>
</section>

<section class="chemfaq">
  <div class="wrap">
    <h2 class="sec-h">Top question: <em>can it take bathroom cleaner?</em></h2>
    <p class="sec-sub">Most bathroom cleaners are strong acids — strong enough to etch real tile and grout. Short answer: "occasional use is fine". The longer answer is that once coated, you barely need it any more.</p>
    <div class="chemgrid">
      <div class="chembox">
        <div class="k">The best news</div>
        <h4>You barely need acid cleaner any more</h4>
        <p>FloorArmour forms one continuous surface over the tile faces and the grout lines alike — no grooves left for grime to settle in. Most marks brush off with plain water or a mild soap solution, so the reason you reached for acid in the first place is gone.</p>
      </div>
      <div class="chembox">
        <div class="k">If you really want to</div>
        <h4>Occasional use is fine — rinse afterwards</h4>
        <p>A two-part polymer film stands up well to household cleaners. Use a bathroom cleaner now and then and rinse it off with water as usual — just don't leave it sitting on the surface.</p>
      </div>
      <div class="chembox">
        <div class="k">Straight talk</div>
        <h4>Frequent strong acid shortens the film's life</h4>
        <p>Strong acid attacks every surface it meets, tile included. Hit the coating with it often and it ages faster too. For the longest life together, an ordinary pH-neutral cleaner does the job.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">Not quite FloorArmour's job? <em>Other options</em></h2>
    <p class="sec-sub">Want another colour, want to keep the tile pattern, or is it only the grout that's failing — these three take over.</p>
    <div class="altgrid">
      <a class="altcard" href="/en/tilecoatpoly">
        <div class="k">Pick a colour · the flagship</div>
        <h4>TileCoat Polyurea</h4>
        <p>Our flagship waterproof tile coating in six colours, primer included in the box — for renovations where you want to choose the tone. From 1,190 THB.</p>
        <div class="go">View details →</div>
      </a>
      <a class="altcard" href="/en/epoxygrout">
        <div class="k">Fix the grout</div>
        <h4>Waterproof Epoxy Grout</h4>
        <p>Replace only the old grout with waterproof grout and the water path is closed, with every original tile still in place.</p>
        <div class="go">View details →</div>
      </a>
      <a class="altcard" href="/en/polyaspartic">
        <div class="k">Clear waterproofing · top tier</div>
        <h4>Clear Polyaspartic Waterproofing</h4>
        <p>A clear waterproof coat over the existing tile — invisible film, top-tier waterproofing, with the tile pattern on full display.</p>
        <div class="go">View details →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">Order <em>FloorArmour</em></h2>
    <div class="ordercard">
      <h3>Order by chat — fast replies</h3>
      <div class="sub">1 kg 990 THB, shipping 130 THB — not sure how many packs your bathroom needs? Send the floor size or a photo first and we'll work it out and check the job for free before you pay.</div>
      <div class="shoprow">
        <a class="shop" href="https://m.me/lucernapro"><span class="fbadge">f</span> Facebook Messenger</a>
        <a class="shop shop-line" href="https://lin.ee/LpUR3Ld">💬 Line @lucerna</a>
        <a class="shop" href="tel:0970799547">📞 097-079-9547</a>
      </div>
    </div>
  </div>
</section>

<section class="reads">
  <div class="wrap">
    <h2 class="sec-h">Not in a hurry? <em>Read a little more</em></h2>
    <p class="sec-sub">The three things tile-job customers ask us most — written from real sites, not sales copy</p>
    <div class="readgrid">
      <a class="readcard" href="/en/post/finding-the-real-leak-point">
        <div class="k">Before you coat</div>
        <h4>Find the real leak first, then waterproof</h4>
        <p>Two or three coats on and it still leaks — most of the time the problem <b>isn't the product</b>, it's that the real leak point was never found before starting.</p>
        <div class="go">Read on →</div>
      </a>
      <a class="readcard" href="/en/post/waterproofing-techniques">
        <div class="k">Do it in the right order</div>
        <h4>Waterproofing techniques that actually work</h4>
        <p>Waterproofing isn't magic — from inspecting the site and repairing cracks to fibreglass reinforcement and laying two coats so the film is truly continuous.</p>
        <div class="go">Read on →</div>
      </a>
      <a class="readcard" href="/en/post/waterproofing-coverage-tips">
        <div class="k">Control the budget</div>
        <h4>How to make waterproofing go further</h4>
        <p>One tin didn't cover what the label said — not because there's less in the can, but because of surface prep and technique.</p>
        <div class="go">Read on →</div>
      </a>
    </div>
    <div class="readall"><a class="btn btn-orange" href="/en/casestudy">See all case studies →</a></div>
  </div>
</section>
'''

if __name__ == '__main__':
    build('th')
    build('en')
