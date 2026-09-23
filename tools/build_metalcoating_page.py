#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_metalcoating_page.py — สร้าง /metalcoating และ /en/metalcoating

สินค้าตัวเดียวกับ EasyClean (สูตร/สเปค/ราคาเดียวกัน — Pist 23 ก.ย. 2026) แต่แยกหน้าเพื่อโลหะ:
สุขภัณฑ์ห้องน้ำ (ก๊อก ฝักบัว ราวสแตนเลส) และผิวนอกของปืน มีด เครื่องมือ — มีผิวด้านและเงา ราคาเดียวกัน
chrome ยกมาจาก paintcoating ผ่าน build_easyclean_page.chrome() · ตัวเลขทั้งหมดจาก TDS ผู้ผลิต
ยกเว้น salt spray 96 ชม. ที่มาจากเอกสารสรุป (Overview) ของผู้ผลิต — Pist อนุมัติให้ใช้ (งานไม่แช่น้ำ)

วิธีใช้: python3 tools/build_metalcoating_page.py แล้วรัน tools/build_calculator_page.py (ตารางมี data-calc)
รูป: hero/การ์ด = ภาพก๊อกโครเมียม (AI-generated, Pist 23 ก.ย. 2026) · -shower / -rail = ภาพประกอบ AI ในแกลเลอรี · -rust-panel = รูปแผ่นทดสอบจริงของ Pist
"""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_easyclean_page import chrome, EXTRA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def build(lang):
    src = 'paintcoating/index.html' if lang == 'th' else 'en/paintcoating/index.html'
    head, drawer, tail = chrome(src)
    head = head.replace('/paintcoating', '/metalcoating')
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE[lang], head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % DESC[lang], head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % OGT[lang], head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % OGD[lang], head)
    head = head.replace('img/paintcoating-hero-sq.webp', 'img/metalcoating-hero-sq.webp')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', SCHEMA[lang], head, flags=re.S)
    head = head + EXTRA_CSS.replace('id="easyclean-css"', 'id="metalcoating-css"')
    drawer = drawer.replace('/paintcoating', '/metalcoating')
    tail = tail.replace('/paintcoating', '/metalcoating')
    out = head + '</head>\n' + drawer + '\n\n' + BODY[lang] + '\n' + tail
    dst = 'metalcoating/index.html' if lang == 'th' else 'en/metalcoating/index.html'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    io.open(dst, 'w', encoding='utf-8').write(out)
    print('wrote', dst, len(out))


TITLE = {
    'th': 'Metal Coating น้ำยาเคลือบโลหะ ชะลอสนิม กันคราบน้ำ กันรอย — สุขภัณฑ์ ก๊อก สแตนเลส ปืน เครื่องมือ | LucernaPro',
    'en': 'Metal Coating — Rust-Delaying, Anti-Fouling, Scratch-Resistant Coating for Bathroom Fittings, Stainless, Firearms and Tools | LucernaPro',
}
DESC = {
    'th': 'Metal Coating น้ำยาเคลือบโลหะสาย Hydrophobic ฟิล์มใสแข็ง 4H มุมสัมผัสน้ำ ≥110° ชะลอสนิม คราบน้ำกระด้างและรอยนิ้วมือเช็ดออกง่าย ทนกรดด่างและน้ำมัน เลือกผิวด้านหรือเงา กลิ่นน้อยมาก สำหรับก๊อก ฝักบัว ราวสแตนเลส ผิวนอกปืน มีด เครื่องมือ วัตถุดิบนำเข้าจาก Feibo',
    'en': 'Metal Coating — a hydrophobic nano coating for metal. Clear 4H film, water contact angle ≥110°, delays rust, hard-water marks and fingerprints wipe off, resists acid, alkali and oil. Matte or gloss finish, very low odour. For taps, showers, stainless rails, firearm exteriors, knives and tools. Raw material imported from Feibo.',
}
OGT = {
    'th': 'Metal Coating น้ำยาเคลือบโลหะ ชะลอสนิม กันคราบน้ำ กันรอย — สุขภัณฑ์ สแตนเลส ปืน เครื่องมือ',
    'en': 'Metal Coating — Rust-Delaying, Anti-Fouling, Scratch-Resistant Coating for Metal',
}
OGD = {
    'th': 'ฟิล์มใสแข็ง 4H น้ำเด้ง คราบน้ำกระด้างและรอยนิ้วมือเช็ดออกง่าย ชะลอสนิม เลือกผิวด้านหรือเงา กลิ่นน้อยมาก — ก๊อก ฝักบัว ราวสแตนเลส ผิวนอกปืน มีด เครื่องมือ',
    'en': 'Clear hydrophobic 4H film — water beads off, hard-water marks and fingerprints wipe away, delays rust. Matte or gloss, very low odour — taps, showers, stainless rails, firearm exteriors, knives, tools.',
}
SCHEMA = {
    'th': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"Metal Coating น้ำยาเคลือบโลหะ ชะลอสนิม กันคราบน้ำ กันรอย","brand":{"@type":"Brand","name":"LucernaPro"},"description":"น้ำยาเคลือบโลหะสาย Hydrophobic ฟิล์มใสแข็ง 4H มุมสัมผัสน้ำ ≥110° ชะลอสนิม คราบน้ำกระด้างและรอยนิ้วมือเช็ดออกง่าย ทนกรดด่างและน้ำมัน เลือกผิวด้านหรือเงา สำหรับสุขภัณฑ์ สแตนเลส ผิวนอกปืน มีด เครื่องมือ","image":"https://www.lucernapro.com/img/metalcoating-hero-sq.webp","url":"https://www.lucernapro.com/metalcoating","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"830","highPrice":"6600","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
    'en': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"Metal Coating — Rust-Delaying, Anti-Fouling, Scratch-Resistant Coating for Metal","brand":{"@type":"Brand","name":"LucernaPro"},"description":"Hydrophobic nano coating for metal — clear 4H film, water contact angle ≥110°, delays rust, hard-water marks and fingerprints wipe off, resists acid, alkali and oil. Matte or gloss. For bathroom fittings, stainless, firearm exteriors, knives and tools.","image":"https://www.lucernapro.com/img/metalcoating-hero-sq.webp","url":"https://www.lucernapro.com/en/metalcoating","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"830","highPrice":"6600","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
}

PRICE_ROWS = '''          <tr><td class="sz" data-sqm="16">100 g</td><td>≈ 16 %(sqm)s</td><td class="pr" data-price="830">830.-</td></tr>
          <tr><td class="sz" data-sqm="80">500 g</td><td>≈ 80 %(sqm)s</td><td class="pr" data-price="3590">3,590.-</td></tr>
          <tr><td class="sz" data-sqm="160">1 kg</td><td>≈ 160 %(sqm)s</td><td class="pr" data-price="6600">6,600.-</td></tr>'''

BODY = {}

BODY['th'] = r'''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Protection <b>· เคลือบปกป้อง</b></div>
      <div class="flagtag">★ NEW — สินค้าใหม่</div>
      <h1>Metal <span class="o">Coating</span><br>น้ำยาเคลือบโลหะ ชะลอสนิม กันคราบน้ำ กันรอย</h1>
      <p class="lede">ก๊อกน้ำ ฝักบัว ราวแขวนสแตนเลส บานพับ ลูกบิด — ไปจนถึงผิวนอกของปืน มีด และเครื่องมือช่าง เคลือบครั้งเดียวเป็นฟิล์มใสบางแข็งระดับ 4H แล้ว<b>น้ำเด้ง คราบน้ำกระด้างและรอยนิ้วมือเช็ดออกง่าย เหล็กเป็นสนิมช้าลงมาก</b> ทนกรดด่างและน้ำมัน เลือกได้ทั้ง<b>ผิวด้านและผิวเงา</b> กลิ่นน้อยมากจนทำในห้องน้ำได้</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">สั่งซื้อ / ดูราคา</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>ปรึกษาหน้างานฟรี</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/metalcoating-hero-sq.webp" alt="ก๊อกโครเมียมที่เคลือบ Metal Coating — หยดน้ำเกาะเป็นเม็ดกลมบนผิวโลหะ ไม่แผ่ ไม่ทิ้งคราบ" width="1200" height="1200">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">โลหะที่เคลือบแล้ว <em>ต่างจากเดิมตรงไหน</em></h2>
    <p class="sec-sub">ฟิล์มนาโนพอลิซิลอกเซนพลังงานผิวต่ำ ปิดผิวโลหะไว้ทั้งผืน — น้ำ ความชื้น น้ำมัน และคราบ เกาะอยู่บนฟิล์ม ไม่ถึงเนื้อโลหะ</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>สนิมช้าลงมาก</h4><p>สนิมต้องการน้ำและอากาศแตะเนื้อเหล็ก — ฟิล์มปิดผิวไว้และไล่น้ำออกจากผิว (มุมสัมผัสน้ำ ≥110°) ความชื้นในห้องน้ำและเหงื่อจากมือจึงไม่ค้างบนเหล็ก ผ่านทดสอบ Salt Spray 96 ชั่วโมงไม่ลอกไม่เป็นสนิม — เหลือเฟือสำหรับสุขภัณฑ์และของใช้ที่ไม่ได้แช่น้ำ</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>คราบน้ำกระด้างและรอยนิ้วมือเช็ดออก</h4><p>ก๊อกโครเมียมและสแตนเลสที่หมองเพราะคราบหินปูนกับรอยนิ้วมัน — เมื่อน้ำเกาะเป็นเม็ดกลิ้งหนี หินปูนก็ไม่มีที่ตกค้าง คราบมือเกาะบนฟิล์มไม่กัดผิว เช็ดผ้าแห้งทีเดียวกลับเงา</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>แข็ง 4H ทนกรด ด่าง น้ำมัน</h4><p>ฟิล์มหนา 8–12 ไมครอน ความแข็งดินสอ ≥4H เล็บขูดไม่ออก แช่กรดซัลฟิวริก 10% และโซดาไฟ 10% 24 ชั่วโมง แช่น้ำมันเบนซิน 24 ชั่วโมง — ความแข็งและการยึดเกาะไม่เปลี่ยน น้ำยาล้างหินปูนและน้ำมันหล่อลื่นทำอะไรฟิล์มไม่ได้</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>กลิ่นน้อยมาก ด้านหรือเงาเลือกได้</h4><p>กลิ่นน้อยกว่าน้ำยาเคลือบโลหะสาย Polysilazane ทั่วไปมาก ลงในห้องน้ำหรือในบ้านได้โดยไม่ต้องอพยพ — เลือกผิวเงาสำหรับโครเมียมและสแตนเลสขัดเงา ผิวด้านสำหรับปืน เครื่องมือ และงานที่ไม่ต้องการแสงสะท้อน</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="fittings">
  <div class="wrap">
    <h2 class="sec-h">ผิวที่เคลือบแล้ว <em>หน้าตาเป็นแบบนี้</em></h2>
    <p class="sec-sub">น้ำเกาะเป็นเม็ดกลมแล้วกลิ้งหนี — ไม่แผ่เป็นแผ่น ไม่แห้งเป็นวงขาว นี่คือสิ่งเดียวที่ต้องดูเวลาเช็คว่าฟิล์มยังทำงานอยู่ (ภาพประกอบ)</p>
    <div class="ggrid" style="grid-template-columns:repeat(2,1fr)">
      <div class="gph"><img loading="lazy" decoding="async" src="/img/metalcoating-shower.webp" alt="ฝักบัวเรนชาวเวอร์และวาล์วโครเมียมบนผนังหินอ่อน หยดน้ำเกาะเป็นเม็ดบนโลหะ (ภาพประกอบ)" width="1200" height="1200"></div>
      <div class="gph"><img loading="lazy" decoding="async" src="/img/metalcoating-rail.webp" alt="วาล์วโครเมียมของราวแขวนผ้าสแตนเลส หยดน้ำเกาะเป็นเม็ดกลมทั่วผิว (ภาพประกอบ)" width="1200" height="1200"></div>
    </div>
    <p class="pricenote">ฝักบัว วาล์ว และราวแขวนผ้า คือสามจุดที่คราบหินปูนขึ้นเร็วที่สุดในห้องน้ำ เพราะโดนน้ำทุกวันแต่ไม่มีใครเช็ดให้แห้ง — เคลือบทีเดียวแล้วน้ำที่เหลือค้างจะกลิ้งลงเอง ไม่แห้งเป็นคราบ</p>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">ดูของจริงก่อน — <em>เหล็กแผ่นเดียวกัน ครึ่งเคลือบ ครึ่งไม่เคลือบ</em></h2>
    <p class="sec-sub">แผ่นเหล็กทดสอบจากห้องแล็บของเรา — ครึ่งบนเคลือบ Metal Coating ครึ่งล่างปล่อยเปลือย แล้วโดนความชื้นเท่ากัน</p>
    <figure class="packshot" style="max-width:520px;margin-top:20px">
      <img loading="lazy" decoding="async" src="/img/metalcoating-rust-panel.webp" alt="แผ่นเหล็กทดสอบ — ครึ่งบนเคลือบ Metal Coating ยังเงาเรียบ ครึ่งล่างไม่เคลือบเป็นสนิมทั่วแผ่น" width="1200" height="1600">
      <figcaption>ครึ่งบนที่เคลือบยังเรียบเงาเหมือนวันแรก ครึ่งล่างที่ไม่เคลือบเป็นสนิมทั่วแผ่น — เส้นแบ่งคือขอบเทปกาว ฟิล์มบนครึ่งบนใช้เล็บขูดไม่ออก</figcaption>
    </figure>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">ใช้กับ<em>อะไรได้บ้าง</em></h2>
    <p class="sec-sub">โลหะทุกชนิดที่ผิวสะอาดและยังไม่เป็นสนิม — เหล็ก สแตนเลส โครเมียม อะลูมิเนียม ทองเหลือง รวมถึงผิว Powder Coat และสีอบบนโลหะ</p>
    <div class="pts">
      <div class="pt"><span class="ic">🚿</span><div><h4>สุขภัณฑ์ห้องน้ำ</h4><p>ก๊อกน้ำ ฝักบัวและสายอ่อน ราวแขวนผ้า ตะแกรงวางของ ที่ใส่กระดาษ บานพับและมือจับกระจกกั้นอาบน้ำ — จุดที่โดนน้ำทุกวันแต่ไม่เคยแห้งสนิท คราบหินปูนไม่เกาะ สแตนเลสไม่ขึ้นจุดสนิม เช็ดครั้งเดียวกลับเงา</p></div></div>
      <div class="pt"><span class="ic">🎯</span><div><h4>ผิวนอกของปืนและอุปกรณ์ยิงปืน</h4><p>โครง สไลด์ ลำกล้องด้านนอก และชิ้นส่วนภายนอกที่โดนเหงื่อจากมือทุกครั้งที่จับ — ฟิล์มกันความชื้นและรอยนิ้วมือ ทนน้ำมันปืนและน้ำยาล้าง เล็บขูดไม่ออก <b>ลงเฉพาะผิวนอกเท่านั้น</b> ไม่ลงในลำกล้อง กลไก และผิวสัมผัสที่เลื่อนชนกัน</p></div></div>
      <div class="pt"><span class="ic">🔧</span><div><h4>มีด เครื่องมือ และของโลหะในบ้าน</h4><p>มีดครัวเหล็กคาร์บอน เครื่องมือช่าง ลูกบิด ราวบันได รั้วและประตูเหล็กที่ทาสีแล้ว แผงเครื่องจักร — ปกป้องผิวที่ยังดีให้ดีต่อไปอีกนาน ผู้ผลิตระบุอายุฟิล์ม 2–3 ปี</p></div></div>
    </div>
  </div>
</section>

<section class="story">
  <div class="wrap">
    <div class="rdtag">SOURCE — วัตถุดิบมาจากไหน</div>
    <h2>เราเลือกนำเข้าวัตถุดิบหลัก<br>จากผู้พัฒนาเทคโนโลยีนี้<b>โดยตรง — Feibo</b></h2>
    <div class="story-grid">
      <div class="bignum">4H<small>PENCIL HARDNESS · ON METAL</small></div>
      <div class="story-body">
        <p>ตัวนี้เรา<b>นำเข้าวัตถุดิบหลักจาก Feibo</b> (ฉางชา ประเทศจีน) ผู้พัฒนาวัตถุดิบเดียวกับ <a href="/glasscoating" style="color:var(--orange)">Glass Coating</a> และ <a href="/paintcoating" style="color:var(--orange)">Paint Coating</a> ของเรา แล้วมาบรรจุและควบคุมคุณภาพต่อในประเทศไทย — เป็นฟิล์มปกป้องโลหะสาย Hydrophobic ที่เราคัดมาสำหรับโจทย์ของโลหะโดยเฉพาะ: <b>ความชื้นกับสนิม</b> ไม่ใช่แค่คราบ</p>
        <p>ในจีน สูตรนี้ใช้กับผิวโลหะและผิวสีที่โดนคราบและสารเคมีทำความสะอาดบ่อย — และผ่านมาตรฐานความปลอดภัยด้านไฟสำหรับยานพาหนะระบบราง (EN 45545-2 ระดับ R1 HL3)</p>
        <div class="beats">
          <div class="beat"><div class="k">หลักการ</div><p>ฟิล์มนาโนพอลิซิลอกเซนโครงสร้างแฟรกทัล เติมนาโนทังสเตนไตรออกไซด์และนาโนทินออกไซด์ — ยึดเกาะโลหะเกรด 0 (Cross-cut) และเป็นชั้นกั้นน้ำกับอากาศไม่ให้ถึงเนื้อโลหะ ผู้ผลิตระบุอายุฟิล์ม <b>2–3 ปี</b></p></div>
          <div class="beat"><div class="k">ผิวโลหะที่ใช้ได้</div><p>เหล็ก สแตนเลส โครเมียม อะลูมิเนียม ทองเหลือง ผิว Powder Coat และสีอบบนโลหะ — <b>ผิวต้องสะอาด ปราศจากน้ำมัน และยังไม่เป็นสนิม</b> สนิมเดิมต้องขจัดออกก่อน</p></div>
          <div class="beat"><div class="k">ด้านหรือเงา</div><p>ผิวเงาสำหรับโครเมียม สแตนเลสขัดเงา และสุขภัณฑ์ที่ต้องการความวาว ผิวด้านสำหรับปืน เครื่องมือ และงานที่ไม่ต้องการแสงสะท้อน — สเปค ราคา และวิธีลงเหมือนกัน แจ้งตอนสั่ง</p></div>
          <div class="beat"><div class="k">ทนร้อน-เย็นสลับ</div><p>ยึดเกาะยังเกรด 0–1 หลังสลับ −30°C ↔ 120°C 3 รอบ และแช่น้ำ 40°C 240 ชั่วโมงความ Hydrophobic ไม่เปลี่ยน — ก๊อกน้ำร้อนและของที่ตากแดดใช้ได้</p></div>
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
          <tr><td>ความหนาฟิล์ม</td><td>8–12 ไมครอน · ใส · ผิวด้านหรือเงา</td></tr>
          <tr><td>ความแข็งดินสอ</td><td>≥ 4H (บนกระจกหรือโลหะ)</td></tr>
          <tr><td>การยึดเกาะ Cross-cut</td><td>เกรด 0 · หลังสลับร้อน-เย็น −30°C / 120°C 3 รอบ เกรด 0–1</td></tr>
          <tr><td>ทนละอองน้ำเกลือ (Salt Spray)</td><td>96 ชม. — ไม่ลอก ไม่แตก ไม่เปลี่ยนสี ไม่เป็นสนิม (เอกสารสรุปของผู้ผลิต)</td></tr>
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
''' + PRICE_ROWS % {'sqm': 'ตร.ม.'} + r'''
          <tr data-calc="skip"><td class="sz">งานโครงการ<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">โรงแรม / โรงงาน / ฟลีท</small></td><td>พื้นที่ขนาดใหญ่</td><td class="pr">ราคาโครงการ — สอบถาม</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote"><b>ผิวด้านหรือผิวเงา ราคาเดียวกัน — แจ้งตอนสั่ง</b> · ค่าจัดส่ง <b>70 บาท</b> · พื้นที่ต่อขวดคิดจากการลงชั้นบางชั้นเดียวด้วยลูกกลิ้งโฟม 4 นิ้ว — ขวด 100 g เคลือบสุขภัณฑ์ทั้งห้องน้ำได้หลายห้อง · <b>งานใหญ่มีราคาโครงการ</b> แจ้งชนิดผิวและพื้นที่มาทางแชทเพจ</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">วิธีใช้งาน — <em>จบบนหน้านี้</em></h2>
    <p class="sec-sub">อ่านให้จบก่อนเปิดกระป๋อง — <b>ผิวสะอาดปราศจากน้ำมันและสนิม</b> กับ <b>กันน้ำโดนในชั่วโมงแรก</b> คือสองอย่างที่ตัดสินผลทั้งงาน</p>
    <ol class="flow">
      <li class="fstep"><h4>ขจัดน้ำมัน คราบ และสนิมเดิมออกให้หมด</h4><p>ล้างขจัดไขมัน (Degrease) เช็ดคราบหินปูนและรอยนิ้วมือออก ถ้ามีจุดสนิมต้องขัดออกจนถึงเนื้อโลหะ — ฟิล์มเกาะสิ่งที่อยู่บนผิว ถ้าลงทับสนิมก็ได้ฟิล์มที่เกาะสนิม ปืนให้เช็ดน้ำมันปืนออกให้แห้งสนิทก่อน</p></li>
      <li class="fstep"><h4>ทดสอบชิ้นเล็กหรือมุมที่ไม่เด่นก่อน</h4><p>ลงบนมุมที่ไม่เด่นของชิ้นจริง รอแข็งตัว แล้วดูความใส ความเงาหรือด้านที่ได้ และหยดน้ำทดสอบ — โดยเฉพาะโครเมียมเงาที่ผิวใดๆ ก็เห็นชัด</p></li>
      <li class="fstep"><h4>ลงเป็นชั้นบางสม่ำเสมอด้วยลูกกลิ้งโฟม 4 นิ้ว</h4><p>ใช้<b>ลูกกลิ้งโฟมขนาด 4 นิ้ว</b> ไล่ทางเดียวเป็นชั้นบางชั้นเดียว ไม่ให้ไหลย้อย ไม่ให้เว้น — บางคือหัวใจ ลงหนาไม่ได้กันสนิมเพิ่มแต่เปลืองและอาจเห็นฟิล์ม ชิ้นเล็กรูปทรงซับซ้อน (ก๊อก ฝักบัว ชิ้นส่วนปืน) สอบถามวิธีลงทางแชทก่อน งานโรงงานพ่น HVLP หัว 1.0–1.2 มม. 0.2 MPa ได้ <b>เปิดกระป๋องแล้วมีแก๊สและกลิ่นเล็กน้อยเป็นเรื่องปกติ</b></p><span class="fchip">ลูกกลิ้งโฟม 4 นิ้ว</span><span class="fchip">ชั้นบางชั้นเดียว</span><span class="fchip">งานโรงงาน: กาพ่น HVLP</span></li>
      <li class="fstep"><h4>ห้ามกลับไปถูซ้ำ — ผิวหน้าเซ็ตตัวทันที</h4><p>ผิวหน้าเริ่มแข็งทันทีที่ลงเสร็จ แห้งผิวใน 20–30 นาที — ลงแล้วปล่อย ไม่กลับไปกลิ้งซ้ำหรือทาซ้ำจุดเดิม ไม่งั้นฟิล์มจะเป็นรอย</p></li>
      <li class="fstep"><h4>กันน้ำโดนจนกว่าฟิล์มจะแข็งตัว</h4><p><b>ถ้าน้ำโดนผิวก่อนฟิล์มแข็งตัว จะเกิดรอยด่าง</b>ที่เช็ดไม่ออก ต้องล้างออกเคลือบใหม่ — ผู้ผลิตให้กันน้ำอย่างน้อย 1 ชั่วโมงแรก ห้องน้ำให้เคลือบตอนที่จะไม่มีใครใช้ เช่น ก่อนนอน</p><span class="fchip">แห้งผิว 20–30 นาที</span><span class="fchip">แห้งจริง ≤ 4 ชม.</span></li>
      <li class="fstep"><h4>24 ชั่วโมง แข็งตัวสมบูรณ์ — ใช้งานได้</h4><p>ที่อุณหภูมิห้องฟิล์มแข็งตัวเต็มที่ใน 24 ชั่วโมง (งานโรงงานอบ 75°C 1–2 ชั่วโมงแทนได้) หลังจากนั้นเช็ดล้างได้ตามปกติด้วยผ้าชุบน้ำหรือน้ำยาฤทธิ์กลาง ปืนเช็ดน้ำมันได้ตามปกติ</p></li>
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
          <div class="beat"><div class="k">1 · "ชะลอสนิม" ไม่ใช่ "กันสนิมตลอดชีพ"</div><p>ฟิล์มหนา 8–12 ไมครอน กันความชื้นได้ตราบที่ฟิล์มยังปิดผิวอยู่ — <b>รอยขูดลึกที่ทะลุฟิล์ม สนิมเริ่มได้ตรงนั้น</b> ของที่โดนกระแทกขูดหนักต้องตรวจและซ่อมจุดที่เสีย ผู้ผลิตระบุอายุฟิล์ม 2–3 ปี ไม่ใช่ตลอดไป</p></div>
          <div class="beat"><div class="k">2 · ไม่ใช่สีทับสนิม และไม่ใช่สีรองพื้นกันสนิมงานโครงสร้าง</div><p>ตัวนี้<b>ปกป้องโลหะที่ยังดี</b> ลงทับสนิมเดิมได้ฟิล์มที่เกาะสนิม ไม่ได้หยุดสนิม และงานเหล็กโครงสร้างที่โดนฝนโดนดินตลอดเวลาต้องใช้สีรองพื้นกันสนิมและสีทับหน้าตามระบบ ตัวนี้เป็นฟิล์มใสสำหรับผิวที่อยากให้เห็นเนื้อโลหะเดิม</p></div>
          <div class="beat"><div class="k">3 · Salt Spray 96 ชั่วโมง คือของที่ไม่ได้แช่น้ำ</div><p>ตัวเลขนี้เหลือเฟือสำหรับก๊อก ฝักบัว ปืน เครื่องมือ และของใช้ในบ้าน แต่ไม่ใช่สเปคสำหรับเรือ ท่าเทียบเรือ หรือโลหะที่แช่น้ำเกลือตลอดเวลา — งานแบบนั้นถามเราก่อน เราจะบอกตรงๆ ว่าไม่เหมาะ</p></div>
          <div class="beat"><div class="k">4 · ปืน: ผิวนอกเท่านั้น</div><p>ลงได้ที่โครง สไลด์ และผิวนอกที่มือจับ — <b>ห้ามลงในลำกล้อง กลไกลั่นไก ราง และผิวสัมผัสที่เลื่อนชนกัน</b> ฟิล์ม 8–12 ไมครอนบนผิวที่ต้องพอดีกัน คือความฝืดที่ไม่ควรมี และไม่ลงส่วนที่ร้อนจัดต่อเนื่องเกิน 120°C</p></div>
          <div class="beat"><div class="k">5 · ชั่วโมงแรกคือจุดตาย และห้องน้ำคือที่ที่น้ำมาเร็วที่สุด</div><p>น้ำโดนผิวก่อนฟิล์มแข็งตัว = <b>รอยด่างที่เช็ดไม่ออก</b> ต้องล้างออกทำใหม่ — เคลือบสุขภัณฑ์ตอนที่ห้องน้ำจะว่างอย่างน้อย 1 ชั่วโมง เช่น ก่อนนอน แล้วปิดประตูกันไอน้ำจากห้องข้างๆ</p></div>
          <div class="beat"><div class="k">6 · เลือกด้าน/เงาให้ถูกก่อนลง และห้ามทับด้วยแว็กซ์</div><p>ผิวด้านลงบนโครเมียมเงาจะลดความวาวลงถาวร ลงแล้วเอาออกไม่ได้ง่ายๆ — ไม่แน่ใจให้ทดสอบชิ้นเล็กก่อน ผิวที่เคลือบแล้วดูแลด้วยน้ำเปล่าหรือน้ำยาฤทธิ์กลาง ห้ามขัดด้วยฝอยขัดหรือผงขัด และไม่ต้องลงแว็กซ์หรือน้ำยาเคลือบอื่นทับ</p></div>
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
      <a class="altcard" href="/easyclean">
        <div class="k">ผนังสีน้ำ · ประตู · เฟอร์นิเจอร์</div>
        <h4>EasyClean</h4>
        <p>สำหรับผิวสีทาผนัง สีไม้ และเฟอร์นิเจอร์ที่โจทย์คือคราบและสีสเปรย์ — ถ้างานคือผนังหรือเฟอร์นิเจอร์ ไปหน้านั้นตรงกว่า</p>
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
    <h2 class="sec-h">สั่งซื้อ <em>Metal Coating</em></h2>
    <div class="ordercard">
      <h3>ช่วงเปิดตัว — สั่งผ่านแชทเท่านั้น</h3>
      <div class="sub">สินค้านำเข้าล็อตแรก ยังไม่ขึ้น Shopee / Lazada ในช่วงเปิดตัว — สั่งตรงผ่านแชทได้ราคาตามตารางด้านบน แจ้ง<b>ผิวด้านหรือเงา</b> ชนิดโลหะ และชิ้นงานที่จะเคลือบมาได้เลย ทีมงานคำนวณปริมาณและแนะนำวิธีลงให้ฟรีก่อนสั่ง · <b>งานใหญ่มีราคาโครงการ</b></div>
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
        <p>ตัวถังรถไฟใช้สาย Self-Cleaning ส่วน Metal Coating ผ่านมาตรฐานไฟระดับเดียวกับวัสดุตู้โดยสาร — ภาพชุดจากหน้างานระบบรางที่ผู้พัฒนาวัตถุดิบทำจริง</p>
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
      <h1>Metal <span class="o">Coating</span><br>Rust-Delaying, Anti-Fouling, Scratch-Resistant Coating for Metal</h1>
      <p class="lede">Taps, showers, stainless towel rails, hinges, door handles — and the exterior of firearms, knives and hand tools. One application forms a clear, thin 4H-hard film, and from then on <b>water beads off, hard-water marks and fingerprints wipe away, and steel rusts far more slowly</b>. Resists acid, alkali and oil, comes in <b>matte or gloss</b>, and the odour is low enough to apply in a bathroom.</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">Order / pricing</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>Free site consultation</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/metalcoating-hero-sq.webp" alt="Chrome tap coated with Metal Coating — water beading into spheres on the metal, no spreading, no marks" width="1200" height="1200">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">What changes <em>once metal is coated</em></h2>
    <p class="sec-sub">A low-surface-energy nano polysiloxane film seals the whole surface — water, humidity, oil and grime sit on the film and never reach the metal</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>Rust slows right down</h4><p>Rust needs water and air touching the steel — the film seals the surface and sheds water (contact angle ≥110°), so bathroom humidity and sweat from hands don't linger on the metal. Passes a 96-hour salt-spray test with no peeling or corrosion — more than enough for fittings and objects that are never submerged.</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>Hard-water marks and fingerprints wipe off</h4><p>Chrome taps and stainless dull from limescale and greasy fingerprints — once water beads and rolls away, limescale has nowhere to settle, and hand grease sits on the film without etching the surface. One pass with a dry cloth and it's bright again.</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>4H hard — resists acid, alkali and oil</h4><p>An 8–12 µm film at ≥4H pencil hardness; a fingernail won't mark it. 24 hours in 10% sulphuric acid and 10% caustic soda, 24 hours in petrol — hardness and adhesion unchanged, so descalers and lubricants do nothing to the film.</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>Very low odour, matte or gloss</h4><p>Far less odour than typical polysilazane metal coatings — apply in a bathroom or indoors without clearing the house. Choose gloss for chrome and polished stainless, matte for firearms, tools and anything that shouldn't reflect light.</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="fittings">
  <div class="wrap">
    <h2 class="sec-h">What a coated surface <em>looks like</em></h2>
    <p class="sec-sub">Water beads into spheres and rolls away — it doesn't sheet, and it doesn't dry into white rings. That's the one thing to look for when checking the film is still working (illustration)</p>
    <div class="ggrid" style="grid-template-columns:repeat(2,1fr)">
      <div class="gph"><img loading="lazy" decoding="async" src="/img/metalcoating-shower.webp" alt="Chrome rain shower head and valve on a marble wall, water beading on the metal (illustration)" width="1200" height="1200"></div>
      <div class="gph"><img loading="lazy" decoding="async" src="/img/metalcoating-rail.webp" alt="Chrome valve on a stainless towel rail, water beading into spheres across the surface (illustration)" width="1200" height="1200"></div>
    </div>
    <p class="pricenote">Shower heads, valves and towel rails are the three spots where limescale builds fastest, because they get wet every day and nobody dries them — coat them once and the water that's left rolls off on its own instead of drying into a mark.</p>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">See it first — <em>one steel panel, half coated, half bare</em></h2>
    <p class="sec-sub">A test panel from our lab — top half coated with Metal Coating, bottom half left bare, both exposed to the same humidity</p>
    <figure class="packshot" style="max-width:520px;margin-top:20px">
      <img loading="lazy" decoding="async" src="/img/metalcoating-rust-panel.webp" alt="Steel test panel — coated top half still smooth and bright, bare bottom half rusted across" width="1200" height="1600">
      <figcaption>The coated top half is as smooth and bright as day one; the bare bottom half has rusted across — the dividing line is the edge of the masking tape. The film on the top half can't be scratched off with a fingernail.</figcaption>
    </figure>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">What it's <em>for</em></h2>
    <p class="sec-sub">Any metal that is clean and not yet rusted — steel, stainless, chrome, aluminium, brass, plus powder-coated and baked-enamel metal</p>
    <div class="pts">
      <div class="pt"><span class="ic">🚿</span><div><h4>Bathroom fittings</h4><p>Taps, shower heads and hoses, towel rails, shelves, paper holders, hinges and handles on shower screens — the spots that get wet every day and never fully dry. No limescale build-up, no rust specks on stainless, one wipe and it's bright.</p></div></div>
      <div class="pt"><span class="ic">🎯</span><div><h4>Firearm exteriors and shooting gear</h4><p>Frames, slides, barrel exteriors and any outer part that meets sweat every time it's handled — the film keeps moisture and fingerprints off, stands up to gun oil and cleaning solvents, and a fingernail won't mark it. <b>Exterior surfaces only</b> — never inside the bore, the action, or on mating surfaces that slide against each other.</p></div></div>
      <div class="pt"><span class="ic">🔧</span><div><h4>Knives, tools and metal around the home</h4><p>Carbon-steel kitchen knives, hand tools, door handles, stair rails, painted steel gates and fences, machine panels — keeps metal that is still good in good condition for years. The manufacturer rates the film at 2–3 years.</p></div></div>
    </div>
  </div>
</section>

<section class="story">
  <div class="wrap">
    <div class="rdtag">SOURCE — where the raw material comes from</div>
    <h2>We import the core raw material<br>directly from the technology's developer <b>— Feibo</b></h2>
    <div class="story-grid">
      <div class="bignum">4H<small>PENCIL HARDNESS · ON METAL</small></div>
      <div class="story-body">
        <p>For this product we <b>import the core raw material from Feibo</b> (Changsha, China) — the same developer behind our <a href="/en/glasscoating" style="color:var(--orange)">Glass Coating</a> and <a href="/en/paintcoating" style="color:var(--orange)">Paint Coating</a> — and pack and quality-control it in Thailand. It is a hydrophobic protective film we selected specifically for the problem metal has: <b>humidity and rust</b>, not just grime.</p>
        <p>In China this formulation goes on metal and painted surfaces that get dirty and are cleaned with chemicals often — and it passes the rail-vehicle fire-safety standard (EN 45545-2, R1 HL3).</p>
        <div class="beats">
          <div class="beat"><div class="k">How it works</div><p>A nano polysiloxane film with a fractal structure, doped with nano tungsten trioxide and nano tin oxide — grade 0 cross-cut adhesion on metal, forming a barrier that keeps water and air off the metal itself. The manufacturer rates the film at <b>2–3 years</b>.</p></div>
          <div class="beat"><div class="k">Metals it suits</div><p>Steel, stainless, chrome, aluminium, brass, powder coat and baked enamel on metal — <b>the surface must be clean, oil-free and not yet rusted</b>; existing rust has to be removed first.</p></div>
          <div class="beat"><div class="k">Matte or gloss</div><p>Gloss for chrome, polished stainless and fittings that should shine; matte for firearms, tools and anything that shouldn't reflect — same specification, same price, same application. Tell us which when you order.</p></div>
          <div class="beat"><div class="k">Handles heat and cold</div><p>Adhesion still grade 0–1 after three −30°C ↔ 120°C cycles, and hydrophobicity unchanged after 240 hours in 40°C water — hot-water taps and objects left in the sun are fine.</p></div>
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
          <tr><td>Film thickness</td><td>8–12 µm · clear · matte or gloss</td></tr>
          <tr><td>Pencil hardness</td><td>≥ 4H (on glass or metal)</td></tr>
          <tr><td>Cross-cut adhesion</td><td>Grade 0 · grade 0–1 after 3 thermal cycles −30°C / 120°C</td></tr>
          <tr><td>Salt spray</td><td>96 h — no peeling, cracking, discolouration or corrosion (manufacturer's summary sheet)</td></tr>
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
''' + PRICE_ROWS % {'sqm': 'm²'} + r'''
          <tr data-calc="skip"><td class="sz">Projects<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">hotels / factories / fleets</small></td><td>Large areas</td><td class="pr">Project pricing — ask us</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote"><b>Matte or gloss, same price — tell us which when you order</b> · Shipping <b>70 THB</b> · coverage per pack assumes one thin coat with a 4-inch foam roller — a 100 g pack does the fittings of several bathrooms · <b>Project pricing for large jobs</b>: tell us the metal and the area via chat</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">How to apply — <em>everything on this page</em></h2>
    <p class="sec-sub">Read to the end before opening the can — <b>a clean, oil-free, rust-free surface</b> and <b>no water in the first hour</b> are the two things that decide the whole job</p>
    <ol class="flow">
      <li class="fstep"><h4>Remove oil, grime and any existing rust</h4><p>Degrease, wipe off limescale and fingerprints, and sand any rust spots back to bare metal — the film bonds to whatever is on the surface, so coating over rust gives you a film stuck to rust. On firearms, wipe off gun oil until bone dry.</p></li>
      <li class="fstep"><h4>Test a small part or an inconspicuous corner</h4><p>Apply to an inconspicuous spot on the real piece, let it cure, then check clarity, the gloss or matte you got, and a water-drop test — especially on bright chrome, where any film shows.</p></li>
      <li class="fstep"><h4>Apply one thin, even coat with a 4-inch foam roller</h4><p>Use a <b>4-inch foam roller</b>, working in one direction, one thin coat, no runs, no gaps — thin is the whole point: a thick coat adds no rust protection, wastes product and can show. For small, complex shapes (taps, shower heads, firearm parts) ask us about application via chat first. Factory jobs can spray with an HVLP gun, 1.0–1.2 mm tip, 0.2 MPa. <b>A little gas and a faint smell on opening the can is normal.</b></p><span class="fchip">4-inch foam roller</span><span class="fchip">One thin coat</span><span class="fchip">Factory: HVLP gun</span></li>
      <li class="fstep"><h4>Never go back over it — the surface sets immediately</h4><p>The surface starts hardening as soon as it's applied and is touch-dry in 20–30 minutes — apply and leave it. Re-rolling or re-brushing a spot marks the film.</p></li>
      <li class="fstep"><h4>Keep water off until the film has hardened</h4><p><b>Water on the surface before the film hardens leaves marks</b> that won't wipe off — strip and recoat. The manufacturer says keep it dry for at least the first hour; in a bathroom, coat when nobody will use it, such as before bed.</p><span class="fchip">Touch-dry 20–30 min</span><span class="fchip">Hard dry ≤ 4 h</span></li>
      <li class="fstep"><h4>24 hours — fully cured and in service</h4><p>Fully cured in 24 hours at room temperature (factory work can heat-cure at 75°C for 1–2 hours instead). After that, clean as normal with a damp cloth or a neutral cleaner; firearms can be oiled as usual.</p></li>
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
          <div class="beat"><div class="k">1 · "Delays rust" is not "rust-proof for life"</div><p>An 8–12 µm film keeps moisture off for as long as it seals the surface — <b>a deep scratch through the film is where rust can start</b>. Objects that take hard knocks and scrapes need the damaged spot checked and repaired. The manufacturer rates the film at 2–3 years, not forever.</p></div>
          <div class="beat"><div class="k">2 · Not a paint-over-rust, and not a structural rust primer</div><p>This <b>protects metal that is still good</b>. Coating over existing rust gives a film stuck to rust; it doesn't stop it. Structural steel that sits in rain and soil needs a proper rust-primer-and-topcoat system — this is a clear film for surfaces where you want to see the metal.</p></div>
          <div class="beat"><div class="k">3 · 96-hour salt spray is for things that aren't submerged</div><p>That figure is more than enough for taps, showers, firearms, tools and household metal, but it is not a specification for boats, jetties or metal that sits in salt water. For that kind of job, ask first — we'll tell you plainly that it isn't the right product.</p></div>
          <div class="beat"><div class="k">4 · Firearms: exterior only</div><p>Frames, slides and the outer surfaces you handle — <b>never inside the bore, the trigger group, rails, or mating surfaces that slide against each other</b>. An 8–12 µm film on surfaces that need to fit is friction that shouldn't be there, and don't coat parts that run continuously above 120°C.</p></div>
          <div class="beat"><div class="k">5 · The first hour is the danger zone, and bathrooms are where water arrives fastest</div><p>Water on the surface before the film hardens = <b>marks that won't wipe off</b> — strip and redo. Coat bathroom fittings when the room will be unused for at least an hour, such as before bed, and keep the door closed against steam from next door.</p></div>
          <div class="beat"><div class="k">6 · Pick matte or gloss before you apply, and don't wax over it</div><p>Matte on bright chrome permanently reduces its shine and isn't easily removed — if in doubt, test a small piece first. Care for a coated surface with plain water or a neutral cleaner, no scouring pads or abrasive powders, and don't add wax or another coating on top.</p></div>
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
      <a class="altcard" href="/en/easyclean">
        <div class="k">Painted walls · doors · furniture</div>
        <h4>EasyClean</h4>
        <p>For painted walls, wood finishes and furniture, where the problem is grime and spray paint — if the job is a wall or furniture, that page is the better fit.</p>
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
    <h2 class="sec-h">Order <em>Metal Coating</em></h2>
    <div class="ordercard">
      <h3>Launch period — order via chat only</h3>
      <div class="sub">First imported batch, not yet on Shopee / Lazada during launch — order directly via chat at the prices in the table above. Tell us <b>matte or gloss</b>, the metal, and what you're coating, and we'll work out the quantity and advise on application for free before you order · <b>Project pricing for large jobs</b></div>
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
        <p>Train bodies use the Self-Cleaning family, while Metal Coating passes the same fire standard as passenger-car materials — a photo set from real rail work by the raw-material developer.</p>
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
