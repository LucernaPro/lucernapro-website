#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_anchor_page.py — สร้าง /anchor และ /en/anchor

⚠ REWRITE 26 ก.ย. 2026 (รอบ 7, มติเจ้าของ "ไม่ขายละ เน้นมันเป็นกาวเท่านั้น ชื่อ anchor นี่แหละ"): Anchor = กาวเรซิน 2 ส่วนผสมมีเนื้อ (สีเขียว, tile adhesive ของโรงงาน) ขายเป็น "กาว" ติดหิน กระเบื้อง กระจก โลหะ คอนกรีต — ไม่ใช่ระบบปูกระเบื้องแผ่นใหญ่อีกต่อไป · ตัด: ปูนกาว/wet-on-wet, #slabs, ตาราง ตร.ม., spec ของ interface agent สีฟ้า, data-calc · รู้แน่: 2K 1:1 มีทราย กันน้ำ (ตู้ปลา) ใช้เดี่ยว รับน้ำหนัก (คลิป) 0.7 ตร.ม./กก. ที่ 1 มม. · ยังไม่รู้ (รอ Lilian): เวลาเซ็ต pot life ทนอุณหภูมิ UV

Lucerna Anchor — กาวรองหลังกระเบื้อง 2 ส่วนผสม (reaction resin, Type R) สำหรับกระเบื้องแผ่นใหญ่ / sintered stone / ผิวเงา
ที่มา (26 ก.ย. 2026): Pist เจอกาวเขียวที่โรงงานจีน ทดสอบเหยียบบันไดกระเบื้องและปีนผนังเอง แล้วได้ TDS ของผู้ผลิต
  · A = silane-modified resin prepolymer (ขาว) / B = aliphatic amine prepolymer (ฟ้า) · 1:1 โดยน้ำหนัก · set 20 kg (10+10)
  · ปาดหลังแผ่น 1 มม. แล้วกดลงปูนกาวซีเมนต์ตอนยังเปียก (wet-on-wet) · coverage 25–30 ตร.ม./set · open time 120–150 นาที
  · JC/T 547-2017 Type R · ต้ม 100°C / แช่แข็ง −30°C · ฟิล์ม 1 มม. งอ 360° · shelf 12 เดือน
  · เคลม "ไม่ต้องล้าง mold release agent" ของผู้ผลิต — Pist สั่งทดสอบเองก่อน ห้ามใช้บนหน้า ("อันนี้บรรลัย")
  · D7 (SPEC): ห้ามพิมพ์ตัวเลขแรงยึดเกาะ (≥2.0 MPa ในเอกสารผู้ผลิตจึงไม่ลงหน้า — ลงแค่ class Type R) + ต้องมีข้อห้าม "อย่าใช้ยึดของหนักโดยไม่มีพุก/สกรู"
  · คำ "Epoxy" ไม่ใช้บนหน้า (ชื่อสินค้าไม่มีคำนี้) — เรียก "เรซิน 2 ส่วนผสม ประเภท Reaction Resin"
ราคา (เจ้าของเคาะ 26 ก.ย. 2026 "เล่นราคา อยากให้ช่างใช้" — ทุนถึงมือ 220/kg + package 100/200/50): 1 kg 590 ส่ง 70 · 5 kg 1,990 ส่ง 130 · 20 kg 6,500 ส่งตามจริง · section #cost คิดเงินต่อห้อง/ต่อแผ่นให้ช่าง
ขาย: แชท + Line + โทร ก่อน (8.6-B) — ยังไม่มี listing Shopee/Lazada
รูป: img/anchor-hero-sq.webp (ถังกาวผสมแล้ว ถ่ายโดย Pist) · anchor-card.webp · anchor-g01 (ตักด้วยเกรียง) · anchor-g02 (ปาดเกรียงหวีบนหลังแผ่น) · anchor-step1/step2 (ภาพ Gemini ที่ Pist gen 26 ก.ย.: ปาด Anchor / โปะปูนกาว wet-on-wet — section #howworks) · anchor-lobby.webp (ภาพ Gemini โถงอาคารติดแผ่น 120×240 ด้วยเครื่องดูด — section #slabs 'ทำไมงานแผ่นใหญ่ต้องมี', 1024×560 ไม่ upscale) · anchor-g03 (ฉาบบนผนัง — วิธี B, Pist ส่ง 26 ก.ย.: "ฉาบบนผนัง แล้วเอากระเบื้องที่ใส่ปูนกาวแล้วมาติดทับ")
คลิป: YouTube Shorts O0LgqwvKovU (แนวตั้ง — บันไดกระเบื้องที่ติดด้วยกาวตัวนี้)
chrome ยกมาจาก paintcoating ผ่าน build_easyclean_page.chrome() — เปลี่ยน --cat เป็นสีหมวด chem
วิธีใช้: python3 tools/build_anchor_page.py แล้วรัน tools/build_calculator_page.py (ตารางราคามี data-calc)
"""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_easyclean_page import chrome, EXTRA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def build(lang):
    src = 'paintcoating/index.html' if lang == 'th' else 'en/paintcoating/index.html'
    head, drawer, tail = chrome(src)
    head = head.replace('/paintcoating', '/anchor')
    head = head.replace('--cat:#8FA6B8; /* สีหมวด coating/PROTECTION ตาม SPEC */', '--cat:#7FBF8E; /* สีหมวด chem/กาว ตาม SPEC */')
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE[lang], head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % DESC[lang], head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % OGT[lang], head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % OGD[lang], head)
    head = head.replace('img/paintcoating-hero-sq.webp', 'img/anchor-hero-sq.webp')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', SCHEMA[lang], head, flags=re.S)
    head = head + EXTRA_CSS.replace('id="easyclean-css"', 'id="anchor-css"') + '''
<style id="anchor-steps-css">#howworks .gph .im{aspect-ratio:auto}#howworks .gph img{height:auto;object-fit:contain}#howworks .gph:hover img{transform:none}#howworks .ggrid{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}</style>'''
    drawer = drawer.replace('/paintcoating', '/anchor')
    tail = tail.replace('/paintcoating', '/anchor')
    out = head + '</head>\n' + drawer + '\n\n' + BODY[lang] + '\n' + tail
    dst = 'anchor/index.html' if lang == 'th' else 'en/anchor/index.html'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    io.open(dst, 'w', encoding='utf-8').write(out)
    print('wrote', dst, len(out))


TITLE = {
    'th': 'Lucerna Anchor กาวเรซิน 2 ส่วนผสม มีเนื้อ กันน้ำ — ติดหิน กระเบื้อง กระจก โลหะ คอนกรีต ไม่ต้องเจาะ | LucernaPro',
    'en': 'Lucerna Anchor — Two-Part Sand-Filled Resin Adhesive, Waterproof — Bonds Stone, Tile, Glass, Metal, Concrete Without Drilling | LucernaPro',
}
DESC = {
    'th': 'Lucerna Anchor กาวเรซิน 2 ส่วนผสม เนื้อครีมข้นมีทราย ติดผิวเงาที่กาวทั่วไปจับไม่อยู่ กระเบื้อง กระจก หิน โลหะ คอนกรีต ติดของบนกระเบื้องไม่ต้องเจาะ ซ่อมกระเบื้องร่อน ติดหินในบ่อและน้ำตก อุดช่องว่างพร้อมติด กันน้ำในตัว ใช้กลางแจ้งได้ 1 กก. 590',
    'en': 'Lucerna Anchor — a two-part sand-filled resin adhesive with real body. Bonds glossy surfaces ordinary glue cannot hold: tile, glass, stone, metal, concrete. Mount fixtures on tile without drilling, re-fix loose tiles, bond rocks in ponds and waterfalls, fill and bond in one go. Waterproof, usable outdoors. 1 kg 590.',
}
OGT = {
    'th': 'Lucerna Anchor กาวเรซินมีเนื้อ ติดหิน กระเบื้อง กระจก โลหะ กันน้ำ',
    'en': 'Lucerna Anchor — Sand-Filled Resin Adhesive for Stone, Tile, Glass, Metal',
}
OGD = {
    'th': 'ติดผิวเงาที่กาวทั่วไปจับไม่อยู่ ติดของบนกระเบื้องไม่ต้องเจาะ ซ่อมกระเบื้องร่อน ติดหินในน้ำ กันน้ำในตัว ใช้กลางแจ้ง 1 กก. 590',
    'en': 'Bonds glossy surfaces ordinary glue cannot hold. Fixtures on tile without drilling, loose-tile repairs, rocks under water. Waterproof, outdoor-safe. 1 kg 590.',
}
SCHEMA = {
    'th': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"Lucerna Anchor กาวเรซิน 2 ส่วนผสม มีเนื้อ กันน้ำ","brand":{"@type":"Brand","name":"LucernaPro"},"description":"กาวเรซิน 2 ส่วนผสมมีทราย ติดกระเบื้อง กระจก หิน โลหะ คอนกรีต ติดของบนกระเบื้องไม่ต้องเจาะ ซ่อมกระเบื้องร่อน กันน้ำในตัว ใช้กลางแจ้ง","image":"https://www.lucernapro.com/img/anchor-hero-sq.webp","url":"https://www.lucernapro.com/anchor","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"590","highPrice":"1990","offerCount":"2","availability":"https://schema.org/InStock"}}\n</script>',
    'en': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"Lucerna Anchor — Two-Part Sand-Filled Resin Adhesive","brand":{"@type":"Brand","name":"LucernaPro"},"description":"Two-part sand-filled resin adhesive that bonds tile, glass, stone, metal and concrete; mounts fixtures on tile without drilling, re-fixes loose tiles; waterproof, outdoor-safe.","image":"https://www.lucernapro.com/img/anchor-hero-sq.webp","url":"https://www.lucernapro.com/en/anchor","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"590","highPrice":"1990","offerCount":"2","availability":"https://schema.org/InStock"}}\n</script>',
}

YT = 'O0LgqwvKovU'

BODY = {}

BODY['th'] = r'''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Adhesive <b>· กาว</b></div>
      <h1>Lucerna <span class="o">Anchor</span><br>กาวเรซิน 2 ส่วนผสม มีเนื้อ กันน้ำ</h1>
      <p class="lede">กาวหลอดทั่วไปแพ้ผิวเงา แพ้น้ำ แพ้ช่องว่าง — พอจะติดตะขอบนกระเบื้องห้องน้ำ ซ่อมกระเบื้องที่ร่อน หรือติดหินในบ่อน้ำ ก็ได้แต่เจาะหรือทุบ Anchor คือ<b>กาวเรซิน 2 ส่วนผสมเนื้อครีมข้นมีทราย</b> ผสมแล้วโปะ กดยึด ทิ้งไว้ให้แข็ง — เกาะกระเบื้องเงา กระจก หิน โลหะ คอนกรีต ด้วยปฏิกิริยาเคมีไม่ต้องอาศัยรูพรุน มีเนื้ออุดช่องว่างพร้อมติดในครั้งเดียว กันน้ำในตัว ใช้กลางแจ้งและใต้น้ำได้ ถูกกว่าอีพ็อกซี่พัตตี้แบบแท่งหลายเท่าต่อกรัม</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">สั่งซื้อ / ดูราคา</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>ส่งรูปงานมาถามก่อนได้</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/anchor-hero-sq.webp" alt="Lucerna Anchor ผสมสองส่วนเข้ากันแล้วเป็นเนื้อครีมสีเขียวสม่ำเสมอในถัง" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">ทำไมกาวตัวนี้ <em>ติดในที่กาวอื่นไม่ติด</em></h2>
    <p class="sec-sub">กาวติดของทั่วไปเกาะด้วยการซึมเข้าผิวหรือแห้งตัวเป็นฟิล์มบาง — ผิวเงาซึมไม่ได้ ช่องว่างกว้างฟิล์มบางไม่ถึง Anchor ทำงานคนละแบบ</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>เกาะผิวเงาด้วยปฏิกิริยาเคมี</h4><p>กระเบื้องเคลือบ พอร์ซเลน กระจก สแตนเลส เหล็ก หินขัด — ผิวที่ไม่มีรูพรุนให้กาวอื่นฝังตัว Anchor เกิดปฏิกิริยากับผิวโดยตรงตอนแข็งตัว ที่จับปีนผาที่ติดบนกระเบื้องเงาแล้วคนโหนได้ในคลิปข้างล่าง ใช้กาวตัวนี้ล้วนๆ</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>มีเนื้อ อุดช่องว่างพร้อมติด</h4><p>เนื้อครีมข้นมีทรายละเอียด โปะแล้วอยู่ ไม่ไหลย้อย ผิวไม่เรียบ ผิวโค้ง หินก้อนต่อหินก้อน ช่องว่าง 2–5 มม. — กาวหลอดต้องอุดก่อนค่อยติด ตัวนี้ทำสองอย่างในทีเดียว</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>กันน้ำในตัว ใช้กลางแจ้งและใต้น้ำ</h4><p>แข็งตัวแล้วน้ำไม่ซึม ไม่ละลาย ไม่พองตัว — ติดหินน้ำตก ก้อนหินในบ่อ ขอบสระ ราวในห้องน้ำ ป้ายกลางแดดฝน ตู้ปลากระจก 5 ด้านที่ต่อด้วยกาวตัวนี้อย่างเดียวใส่น้ำได้จริง</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>1 กิโล ติดได้เป็นร้อยชิ้น</h4><p>ฐานตะขอ 5×5 ซม. หนา 2 มม. ใช้กาวราว 5 กรัม — ชุด 1 กก. ทำได้ราว 200 ครั้ง หรือปาดเป็นชั้น 1 มม. ได้ 0.7 ตร.ม. ต่อกรัมถูกกว่าอีพ็อกซี่พัตตี้แท่ง 3–4 เท่า และผสมได้ทีละเท่าที่ใช้</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">ดูของจริงก่อน — <em>คลิปและภาพ</em></h2>
    <p class="sec-sub">บันไดกระเบื้องที่ยึดกันด้วยกาวตัวนี้ล้วนๆ และเนื้อกาวหลังผสม</p>
    <div class="vidgrid vert solo">
      <figure style="margin:0">
        <div class="fbv v916"><iframe loading="lazy" src="https://www.youtube.com/embed/''' + YT + r'''" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="Lucerna Anchor — บันไดกระเบื้องที่ยึดด้วยกาวตัวนี้ รับน้ำหนักคนเดินขึ้น"></iframe></div>
        <figcaption><b>บันไดกระเบื้องที่ยึดด้วยกาวตัวนี้</b> — สันกระเบื้องหนา 1 ซม. ติดเข้ากับผิวเงาของกระเบื้องแผ่นใหญ่ ต่อกันเป็นขั้นบันไดแล้วเดินขึ้นจริง เป็นการสาธิตแรงยึด ไม่ใช่วิธีติดตั้งที่แนะนำ</figcaption>
      </figure>
    </div>
    <div class="ggrid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:18px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g01.webp" alt="เนื้อกาว Lucerna Anchor บนเกรียง — เนื้อครีมข้นสีเขียวมีเม็ดทรายละเอียด ไม่ไหลย้อย" width="720" height="720"></div><figcaption><span class="no">01</span>เนื้อกาวหลังผสม — ครีมข้นมีทรายละเอียด เกาะเกรียงไม่ไหล</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g02.webp" alt="ปาด Lucerna Anchor บนหลังกระเบื้องด้วยเกรียงหวี เห็นร่องกาวเรียบสม่ำเสมอ" width="720" height="720"></div><figcaption><span class="no">02</span>ปาดหลังกระเบื้องที่จะติดซ่อม — เต็มแผ่นถึงขอบ</figcaption></figure>
    </div>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">ใช้กับ<em>งานไหน</em></h2>
    <p class="sec-sub">งานที่ "ติดไม่ได้ ต้องเจาะ" หรือ "ติดแล้วโดนน้ำหลุด"</p>
    <div class="pts">
      <div class="pt"><span class="ic">🪝</span><div><h4>ติดของบนกระเบื้องโดยไม่เจาะ</h4><p>ตะขอ ที่แขวนผ้า ที่ใส่สบู่ ป้าย ที่จับเล็ก ชั้นวางของเบา บนกระเบื้องห้องน้ำหรือครัวที่เจาะแล้วเสี่ยงแตก ทาเต็มหน้าสัมผัสแล้วกดยึด <b>งานรับน้ำหนักจริงยังต้องใช้พุกหรือสกรู</b> อ่านข้อจำกัดด้านล่าง</p></div></div>
      <div class="pt"><span class="ic">🧱</span><div><h4>ซ่อมกระเบื้องร่อน ทีละแผ่น</h4><p>แผ่นที่เคาะแล้วกลวงหรือหลุดออกมาแล้ว ไม่ต้องรื้อทั้งผืน แซะแผ่นออก เก็บปูนกาวเก่าออกให้เรียบ ปาด Anchor หลังแผ่นเต็มแผ่นแล้วกดกลับเข้าที่ กาวเกาะทั้งหลังแผ่นพอร์ซเลนเงาและปูนเดิม</p></div></div>
      <div class="pt"><span class="ic">🪨</span><div><h4>หิน คอนกรีต โลหะ กระจก — โดยเฉพาะที่เปียก</h4><p>ก้อนหินน้ำตก หินขอบบ่อ กระเบื้องสระที่ร่อน แผ่นเหล็กกับปูน กระจกกับกระจก ป้ายสแตนเลสบนหินแกรนิต — งานกลางแจ้ง โดนน้ำ โดนแดด ที่กาวซิลิโคนหรือกาวหลอดอยู่ได้ไม่นาน</p></div></div>
      <div class="pt"><span class="ic">🔧</span><div><h4>ทั้งอุดทั้งติด ในครั้งเดียว</h4><p>ผิวไม่เรียบเสมอกัน ชิ้นงานโค้ง มุมที่ต้องเสริมเนื้อ ฐานที่ต้องเติมให้เต็มก่อนวาง — เนื้อกาวมีทราย อุดช่องว่างได้ถึงหลายมิลลิเมตร แข็งแล้วขัดแต่งได้เหมือนปูน</p></div></div>
    </div>
    <div class="warn"><b>⚠ อย่าใช้ยึดของหนัก:</b> ชั้นวางที่จะวางของหนัก ราวจับที่คนโหนหรือพยุงตัว ทีวี ตู้ ของที่แขวนเหนือหัวคนหรือเหนือเตียง ต้องยึดด้วยพุกหรือสกรูเชิงกลเสมอ กาวเป็นตัวเสริม ไม่ใช่ตัวรับน้ำหนักหลัก — ตราบใดที่ยังไม่มีตัวเลขรับน้ำหนักที่เราวัดเองบนหน้านี้ ให้ถือว่ารับน้ำหนักไม่ได้ไว้ก่อน งานที่ไม่แน่ใจ ทักมาถามพร้อมรูป</div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">สเปคทางเทคนิค <em>ตัวเลขจากการทดสอบ</em></h2>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>รายการ</th><th>ค่า</th><th>หมายเหตุ</th></tr></thead>
        <tbody>
          <tr><td>ชนิด</td><td>กาวเรซิน 2 ส่วนผสม แข็งตัวด้วยปฏิกิริยา</td><td>ไม่ใช่กาวแห้งด้วยอากาศ ไม่ต้องใช้ความชื้น</td></tr>
          <tr><td>อัตราส่วนผสม</td><td>A : B = 1 : 1 โดยน้ำหนัก</td><td>ชุดเราชั่งมาให้แล้ว</td></tr>
          <tr><td>ลักษณะ</td><td>ครีมข้นมีทรายละเอียด ผสมแล้วสีเขียว</td><td>โปะได้ ไม่ไหลย้อย</td></tr>
          <tr><td>ผิวที่ติดได้</td><td>กระเบื้องเคลือบ พอร์ซเลน กระจก หิน คอนกรีต ปูนฉาบ อิฐ เหล็ก สแตนเลส อลูมิเนียม</td><td>ไม่เหมาะกับพลาสติกอ่อน PE/PP ยาง</td></tr>
          <tr><td>ความหนาที่ใช้</td><td>1–3 มม. ตามงาน</td><td>หนากว่านี้ทำเป็นชั้นๆ</td></tr>
          <tr><td>ปริมาณการใช้</td><td>1 กก. ≈ 0.7 ตร.ม. ที่ 1 มม.</td><td>ฐานตะขอ 5×5 ซม. ≈ 5 กรัม</td></tr>
          <tr><td>กันน้ำ</td><td>แช่น้ำถาวรได้หลังแข็งตัวเต็มที่</td><td>ตู้ปลา บ่อ น้ำตก</td></tr>
          <tr><td>บรรจุ</td><td>1 กก. (A 500 g + B 500 g) · 5 กก. (A 2.5 + B 2.5)</td><td>จำนวนมากทักแชท</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">ขนาดและราคา</h2>
    <p class="sec-sub">ชุด A + B ชั่งมาให้ตรง 1:1 แล้ว ผสมทีละเท่าที่ใช้</p>
    <div class="pricecard">
      <table>
        <thead><tr><th>ขนาด</th><th>เหมาะกับ</th><th>ราคา</th><th>ค่าส่ง</th></tr></thead>
        <tbody>
          <tr><td class="sz">1 กก.<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 500 g + B 500 g</small></td><td>ติดของทั่วบ้าน ซ่อมกระเบื้อง 5–10 แผ่น ตะขอเป็นร้อยตัว</td><td class="pr">590.-</td><td class="pr">70.-</td></tr>
          <tr><td class="sz">5 กก.<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 2.5 kg + B 2.5 kg</small></td><td>ช่างบ่อ ช่างสระ งานหิน งานซ่อมทั้งห้อง</td><td class="pr">1,990.-</td><td class="pr">130.-</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">ราคารวม VAT · เปิดถังแล้วใช้ให้หมดภายในอายุที่แนะนำ ส่วน B ไม่ชอบอากาศ ปิดฝาให้สนิททุกครั้ง · <b>ช่างและงานโครงการมีราคาจำนวนมาก</b> ทักแชทมาได้เลย</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">วิธีใช้งาน — <em>จบบนหน้านี้</em></h2>
    <p class="sec-sub">ผสม โปะ กด รอ — สี่ขั้น ไม่ต้องมีเครื่องมือพิเศษ</p>
    <ol class="flow">
      <li class="fstep"><h4>ผิวสะอาด แห้ง แน่น</h4><p>เช็ดฝุ่น คราบสบู่ คราบมัน ออกจากทั้งสองผิว กระเบื้องห้องน้ำล้างแล้วเช็ดแห้ง หินและปูนเก่าปัดฝุ่นและเศษร่วนออกให้หมด ผิวเงามากเช็ดด้วยแอลกอฮอล์อีกรอบ — กาวเกาะสิ่งที่อยู่บนผิว ถ้าผิวมีฝุ่นมันเกาะฝุ่น</p><span class="fchip">สะอาด แห้ง</span></li>
      <li class="fstep"><h4>ผสม A : B = 1 : 1 จนเป็นสีเขียวเดียวทั่ว</h4><p>ตัก A และ B น้ำหนักเท่ากันลงภาชนะเดียว คนด้วยเกรียงหรือไม้จน<b>ไม่เหลือริ้วขาวหรือฟ้า</b> ขูดก้นและข้างภาชนะด้วย สีเขียวสม่ำเสมอ = ผสมเข้ากันแล้ว ผสมทีละเท่าที่ใช้หมดในรอบเดียว กาวที่ผสมแล้วเก็บไม่ได้</p><span class="fchip">1:1 โดยน้ำหนัก</span><span class="fchip">สีเดียว ไม่มีริ้ว</span></li>
      <li class="fstep"><h4>โปะให้เต็มหน้าสัมผัส แล้วกดยึด</h4><p>ทากาวลงบนหน้าสัมผัสให้เต็มถึงขอบ หนา 1–3 มม. ตามความไม่เรียบของผิว กดชิ้นงานลงจนกาวปลิ้นออกรอบขอบเล็กน้อย = เต็มหน้าแล้ว ขยับปรับตำแหน่งได้ในช่วงที่กาวยังนิ่ม เช็ดส่วนที่ปลิ้นออกทันทีขณะเปียก แข็งแล้วต้องขูดหรือขัด ของที่จะไหลหรือเลื่อนให้ใช้เทปกาวหรือค้ำไว้</p><span class="fchip">เต็มหน้า ถึงขอบ</span><span class="fchip">ค้ำไว้</span></li>
      <li class="fstep"><h4>ทิ้งไว้ให้แข็งตัว ก่อนแขวนของหรือโดนน้ำ</h4><p>ค้ำหรือเทปไว้จนกาวแข็ง อากาศร้อนแข็งเร็วขึ้น อากาศเย็นช้าลง ทิ้งข้ามคืนก่อนแขวนของหรือปล่อยน้ำ งานในน้ำ (บ่อ ตู้ปลา) รอให้แข็งเต็มที่ก่อนเติมน้ำ</p><span class="fchip">ทิ้งข้ามคืน</span></li>
    </ol>

    <div class="warn"><b>⚠ ความปลอดภัย:</b> เป็นกาวเรซิน 2 ส่วนผสม ส่วน B มีสารบ่มที่ระคายผิวหนังและอาจทำให้แพ้เมื่อสัมผัสซ้ำ — สวมถุงมือไนไตรล์ทุกครั้ง ทำงานในที่อากาศถ่ายเท ถ้าเปื้อนผิวเช็ดออกแล้วล้างด้วยสบู่และน้ำทันที (ไม่ใช้ทินเนอร์ล้างมือ) เข้าตาล้างน้ำต่อเนื่องหลายนาทีแล้วพบแพทย์ กาวที่ผสมแล้วเหลือ ปล่อยให้แข็งในภาชนะก่อนทิ้ง เก็บให้พ้นมือเด็ก</div>
  </div>
</section>

<section class="story" id="straight">
  <div class="wrap">
    <div class="rdtag">STRAIGHT TALK — ความจริงที่ต้องพูด</div>
    <h2>ก่อนจ่ายเงิน อ่าน 5 ข้อนี้ก่อน —<br><b>ตัวนี้ไม่ใช่กาวสารพัดนึก</b> และเราไม่อยากให้คุณเข้าใจผิด</h2>
    <div class="story-grid">
      <div class="bignum">5<small>สิ่งที่คนขายส่วนใหญ่ไม่บอก</small></div>
      <div class="story-body">
        <div class="beats">
          <div class="beat"><div class="k">1 · ไม่สวย และไม่ตั้งใจจะสวย</div><p>เนื้อหยาบมีทราย สีเขียว รอยกาวที่ปลิ้นออกมาเห็นชัด — ตัวนี้เกิดมาเพื่อยึด ไม่ใช่เพื่อโชว์รอยต่อ งานที่รอยกาวต้องเนียนหรือใส ใช้กาวใสหรือ FlexGrip แล้วยอมได้แรงยึดน้อยกว่า</p></div>
          <div class="beat"><div class="k">2 · แข็ง ไม่ยืด</div><p>แข็งตัวแล้วเป็นเหมือนหิน ไม่ยืดตามชิ้นงาน — รอยต่อที่ขยับ ไม้ที่บิดตามความชื้น พลาสติกอ่อน ยาง จะแยกออกจากกาว ไม่ใช่กาวแตก แต่ชิ้นงานหนี ผิวที่ขยับใช้กาวยืดหยุ่น</p></div>
          <div class="beat"><div class="k">3 · ต้องผสม ต้องรอ</div><p>ไม่ใช่กาวรีบ ต้องชั่ง 1:1 ผสมให้ทั่ว กดค้ำไว้ แล้วรอข้ามคืน ซ่อมด่วนที่อยากได้ผลใน 5 นาทีไม่ใช่ตัวนี้ แต่สิ่งที่ได้แลกมาคือรอยต่อที่ทนน้ำทนแดดไปอีกหลายปี</p></div>
          <div class="beat"><div class="k">4 · ส่วน B เปิดแล้วต้องใช้</div><p>สารบ่มโดนอากาศและความชื้นแล้วค่อยๆ เปลี่ยนสภาพ กระปุกที่ปิดไม่สนิททิ้งไว้เป็นเดือน ผสมแล้วอาจแข็งช้าหรือไม่แข็ง ซื้อขนาดที่ใช้หมดในเวลาไม่นาน ปิดฝาให้แน่นทันทีทุกครั้ง</p></div>
          <div class="beat"><div class="k">5 · แกะออกยาก</div><p>ติดแล้วคือติดถาวร แกะออกต้องใช้แรงจนเคลือบกระเบื้องหรือผิวหินอาจติดออกมาด้วย ของที่จะย้ายที่ในอนาคต หรือห้องเช่าที่ต้องคืนสภาพ คิดก่อนติด</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">งานของคุณ<em>ใช่ตัวนี้ไหม</em></h2>
    <p class="sec-sub">ถ้าโจทย์คือรอยต่อสวย ยืดหยุ่น หรือร่องยาแนว สองตัวนี้ตรงกว่า</p>
    <div class="altgrid">
      <a class="altcard" href="/flexgrip">
        <div class="k">ติดชิ้นเล็ก · รอยต่อที่ขยับ · ไม่ต้องผสม</div>
        <h4>กาวบ้าพลัง FlexGrip</h4>
        <p>กาวขวดเดียวไม่ต้องผสม ยืดหยุ่น ติดได้แทบทุกวัสดุ เหมาะกับงานที่รอยต่อต้องเนียนหรือชิ้นงานขยับ</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
      <a class="altcard" href="/carbontilegrout">
        <div class="k">ร่องยาแนว · สระว่ายน้ำ · ห้องน้ำ</div>
        <h4>ยาแนว Carbon</h4>
        <p>ร่องระหว่างกระเบื้องไม่ใช่งานของกาว — ยาแนวสองส่วนผสมสำหรับที่เปียกตลอด ไม่ดำ ไม่ร่อน</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">สั่งซื้อ <em>Lucerna Anchor</em></h2>
    <div class="ordercard">
      <h3>สั่งตรงผ่านแชท</h3>
      <div class="sub">ไม่แน่ใจว่างานของคุณติดได้ไหม ส่งรูปมาก่อนได้ เราตอบตรงๆ ว่าใช่หรือไม่ใช่ · <b>ช่างและร้านค้า มีราคาจำนวนมาก</b></div>
      <div class="shoprow">
        <a class="shop" href="https://m.me/lucernapro"><span class="fbadge">f</span> แชทเพจ Facebook</a>
        <a class="shop shop-line" href="https://lin.ee/LpUR3Ld">💬 Line @lucerna</a>
        <a class="shop" href="tel:0970799547">📞 097-079-9547</a>
      </div>
    </div>
  </div>
</section>
'''

BODY['en'] = r'''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Adhesive <b>· Adhesives</b></div>
      <h1>Lucerna <span class="o">Anchor</span><br>Two-Part Sand-Filled Resin Adhesive</h1>
      <p class="lede">Tube glues lose to glossy surfaces, to water and to gaps — so a hook on bathroom tile, a loose tile, or a rock in a pond ends up drilled or demolished. Anchor is a <b>two-part resin adhesive with a thick, sand-filled body</b>: mix, dab on, press, leave to harden. It bonds glazed tile, glass, stone, metal and concrete by chemical reaction, needs no pores to grip, fills a gap and bonds in the same stroke, is waterproof when cured and works outdoors and under water — at a fraction of the per-gram price of epoxy putty sticks.</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">Order / Prices</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>Send a photo and ask first</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/anchor-hero-sq.webp" alt="Lucerna Anchor after mixing the two parts — a uniform green cream in the bucket" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">Why it holds <em>where other glues don't</em></h2>
    <p class="sec-sub">Ordinary adhesives grip by soaking into a surface or drying to a thin film. Glossy surfaces don't absorb, and a thin film can't bridge a gap. Anchor works differently.</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>Bonds glossy surfaces chemically</h4><p>Glazed tile, porcelain, glass, stainless, steel, polished stone — surfaces with no pores for a glue to key into. Anchor reacts with the surface as it cures. The climbing holds bonded to glossy tile that a grown man hangs from in the clip below use nothing but this.</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>Has body — fills and bonds in one</h4><p>A thick cream with fine sand: it stays where you put it and doesn't sag. Uneven faces, curved parts, rock on rock, gaps of 2–5 mm — where a tube glue needs a filler first, this does both at once.</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>Waterproof — outdoors and under water</h4><p>Once cured, water doesn't get in, dissolve it or swell it. Waterfall rocks, pond stones, pool edges, bathroom rails, signs in sun and rain — a five-sided glass aquarium joined with this adhesive alone holds water.</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>One kilo does hundreds of jobs</h4><p>A 5×5 cm hook base at 2 mm takes about 5 g — a 1 kg set is roughly 200 of those, or a 1 mm layer over 0.7 m². Three to four times cheaper per gram than epoxy putty sticks, and you mix only what you need.</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">See it first — <em>clip and photos</em></h2>
    <p class="sec-sub">A tile staircase held together by nothing but this adhesive, and the mixed material itself</p>
    <div class="vidgrid vert solo">
      <figure style="margin:0">
        <div class="fbv v916"><iframe loading="lazy" src="https://www.youtube.com/embed/''' + YT + r'''" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="Lucerna Anchor — a tile staircase held by this adhesive, taking a person's weight"></iframe></div>
        <figcaption><b>A staircase held by this adhesive</b> — 1 cm tile edges bonded to the glossy face of a large slab, built into steps and walked up. A strength demonstration, not a recommended way to build anything.</figcaption>
      </figure>
    </div>
    <div class="ggrid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:18px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g01.webp" alt="Lucerna Anchor on a trowel — a thick green cream with fine sand that holds its shape" width="720" height="720"></div><figcaption><span class="no">01</span>The mixed adhesive — a thick cream with fine sand, holds on the trowel without sagging</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g02.webp" alt="Lucerna Anchor combed onto the back of a tile with a notched trowel in even ridges" width="720" height="720"></div><figcaption><span class="no">02</span>Spread over the back of a tile being re-fixed — full coverage to the edges</figcaption></figure>
    </div>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">Which jobs <em>is it for</em></h2>
    <p class="sec-sub">Jobs that "can't be glued, must be drilled" or "were glued and came off in the wet"</p>
    <div class="pts">
      <div class="pt"><span class="ic">🪝</span><div><h4>Fixtures on tile without drilling</h4><p>Hooks, towel holders, soap dishes, signs, small handles, light shelves on bathroom or kitchen tile where a drill risks a crack. Coat the full contact face and press on. <b>Anything that genuinely carries load still needs anchors or screws</b> — read the limit below.</p></div></div>
      <div class="pt"><span class="ic">🧱</span><div><h4>Re-fix loose tiles, one at a time</h4><p>A tile that sounds hollow or has already come away — no need to rip out the wall. Lift it, clean the old adhesive back to a flat base, spread Anchor over the whole back and press it home. It bonds to the glossy porcelain back and to the old render alike.</p></div></div>
      <div class="pt"><span class="ic">🪨</span><div><h4>Stone, concrete, metal, glass — especially in the wet</h4><p>Waterfall rocks, pond-edge stones, loose pool tiles, steel plate to render, glass to glass, a stainless sign on granite — outdoor work in water and sun where silicone or tube glue doesn't last.</p></div></div>
      <div class="pt"><span class="ic">🔧</span><div><h4>Fill and bond in one go</h4><p>Faces that don't meet flat, curved parts, corners that need building up, bases that need packing before setting — the sand-filled body bridges several millimetres and, once hard, can be shaped like mortar.</p></div></div>
    </div>
    <div class="warn"><b>⚠ Do not use it to hold heavy things:</b> shelves that will carry weight, grab rails people pull on, TVs, cabinets, anything hanging above heads or beds must be fixed with wall anchors or screws — adhesive is a helper, not the primary load path. Until this page shows a load figure we have measured ourselves, treat it as not load-bearing. If in doubt, message us with a photo.</div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">Technical specification <em>test figures</em></h2>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>Item</th><th>Value</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Type</td><td>Two-part reaction-curing resin adhesive</td><td>Not air-drying, needs no moisture to cure</td></tr>
          <tr><td>Mixing ratio</td><td>A : B = 1 : 1 by weight</td><td>Our sets come pre-weighed</td></tr>
          <tr><td>Consistency</td><td>Thick cream with fine sand, mixes to green</td><td>Stays put, no sag</td></tr>
          <tr><td>Bonds to</td><td>Glazed tile, porcelain, glass, stone, concrete, render, brick, steel, stainless, aluminium</td><td>Not for soft plastics (PE/PP) or rubber</td></tr>
          <tr><td>Applied thickness</td><td>1–3 mm depending on the job</td><td>Build thicker in layers</td></tr>
          <tr><td>Consumption</td><td>1 kg ≈ 0.7 m² at 1 mm</td><td>A 5×5 cm hook base ≈ 5 g</td></tr>
          <tr><td>Water</td><td>Permanent immersion once fully cured</td><td>Aquariums, ponds, waterfalls</td></tr>
          <tr><td>Packaging</td><td>1 kg (A 500 g + B 500 g) · 5 kg (A 2.5 + B 2.5)</td><td>Bulk on chat</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">Sizes and prices</h2>
    <p class="sec-sub">A + B come pre-weighed 1:1 — mix only what you'll use</p>
    <div class="pricecard">
      <table>
        <thead><tr><th>Size</th><th>Good for</th><th>Price</th><th>Shipping</th></tr></thead>
        <tbody>
          <tr><td class="sz">1 kg<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 500 g + B 500 g</small></td><td>Fixtures around the house, 5–10 loose tiles, hooks by the hundred</td><td class="pr">590.-</td><td class="pr">70.-</td></tr>
          <tr><td class="sz">5 kg<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 2.5 kg + B 2.5 kg</small></td><td>Pond and pool trades, stonework, whole-room repairs</td><td class="pr">1,990.-</td><td class="pr">130.-</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">Prices include VAT · Once opened, use within the recommended life — part B doesn't like air, seal the tub tightly every time · <b>Volume pricing for trades and projects</b> — message us</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">How to use — <em>all on this page</em></h2>
    <p class="sec-sub">Mix, dab, press, wait — four steps, no special tools</p>
    <ol class="flow">
      <li class="fstep"><h4>Clean, dry, sound surfaces</h4><p>Wipe dust, soap film and grease off both faces. Wash bathroom tile and dry it; brush loose grit off stone and old render. Wipe very glossy surfaces once more with alcohol — the adhesive bonds to whatever is on the surface, and if that's dust, it bonds to dust.</p><span class="fchip">Clean and dry</span></li>
      <li class="fstep"><h4>Mix A : B = 1 : 1 to a single green</h4><p>Put equal weights of A and B in one container and stir with a trowel or stick until <b>no white or blue streaks remain</b>, scraping the bottom and sides. One even green means it's mixed. Mix only what you'll use in one go — mixed adhesive can't be kept.</p><span class="fchip">1:1 by weight</span><span class="fchip">One colour, no streaks</span></li>
      <li class="fstep"><h4>Coat the full contact face, then press</h4><p>Spread it over the whole contact face out to the edges, 1–3 mm thick depending on how uneven the surfaces are. Press the part on until a little squeezes out all round — that means full contact. Reposition while it's still soft. Wipe squeeze-out at once while wet; once hard it has to be scraped or ground. Tape or prop anything that could slide or sag.</p><span class="fchip">Full face, to the edges</span><span class="fchip">Prop it</span></li>
      <li class="fstep"><h4>Leave it to harden before loading or wetting</h4><p>Keep it propped or taped until hard — faster in heat, slower in cold. Leave overnight before hanging anything on it or letting water at it. For work under water (ponds, aquariums), wait for a full cure before filling.</p><span class="fchip">Overnight</span></li>
    </ol>

    <div class="warn"><b>⚠ Safety:</b> a two-part resin adhesive. Part B contains a curing agent that irritates skin and can sensitise with repeated contact — nitrile gloves every time, work in ventilated space. Wipe skin contact off and wash with soap and water at once (never thinner). Eyes: flush with water for several minutes and see a doctor. Let leftover mixed adhesive harden in the container before disposal. Keep away from children.</div>
  </div>
</section>

<section class="story" id="straight">
  <div class="wrap">
    <div class="rdtag">STRAIGHT TALK — what has to be said</div>
    <h2>Before you pay, read these 5 —<br><b>this is not a do-everything glue</b>, and we don't want you misled</h2>
    <div class="story-grid">
      <div class="bignum">5<small>things most sellers don't say</small></div>
      <div class="story-body">
        <div class="beats">
          <div class="beat"><div class="k">1 · It isn't pretty and doesn't try to be</div><p>Coarse, sandy, green; squeeze-out shows. It exists to hold, not to make a joint look good. Where the glue line must be neat or clear, use a clear glue or FlexGrip and accept less strength.</p></div>
          <div class="beat"><div class="k">2 · Rigid, not flexible</div><p>Cured, it's like stone and won't move with the part. Moving joints, wood that swells with humidity, soft plastics and rubber will separate from it — not the glue breaking, the part walking away. Moving surfaces want a flexible adhesive.</p></div>
          <div class="beat"><div class="k">3 · You mix and you wait</div><p>Not a quick fix: weigh 1:1, mix thoroughly, prop it and leave it overnight. If you need a result in five minutes, this isn't it. What you get in return is a joint that shrugs off water and sun for years.</p></div>
          <div class="beat"><div class="k">4 · Part B doesn't like air — open it, use it</div><p>The curing agent slowly changes with air and humidity. A tub sealed badly and left for a month may cure slowly or not at all. Buy the size you'll finish soon and seal the lid tightly every time.</p></div>
          <div class="beat"><div class="k">5 · Hard to remove</div><p>Bonded is bonded for good. Removing it takes enough force that the tile glaze or the stone face may come with it. Anything you might move later, or a rental you have to hand back as found — think before you stick.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">Is this <em>the right product for your job?</em></h2>
    <p class="sec-sub">If the job is a neat glue line, movement or a grout joint, one of these fits better</p>
    <div class="altgrid">
      <a class="altcard" href="/en/flexgrip">
        <div class="k">Small parts · moving joints · no mixing</div>
        <h4>FlexGrip</h4>
        <p>A one-bottle glue with no mixing — flexible, bonds almost any material, for jobs where the joint must look neat or the part moves.</p>
        <div class="go">View details →</div>
      </a>
      <a class="altcard" href="/en/carbontilegrout">
        <div class="k">Grout joints · pools · bathrooms</div>
        <h4>Carbon Tile Grout</h4>
        <p>The gaps between tiles are not a glue job — a two-part grout for permanently wet places that doesn't blacken or crumble.</p>
        <div class="go">View details →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">Order <em>Lucerna Anchor</em></h2>
    <div class="ordercard">
      <h3>Order directly on chat</h3>
      <div class="sub">Not sure your job will bond? Send a photo first — we'll tell you straight, yes or no · <b>Volume pricing for trades and shops</b></div>
      <div class="shoprow">
        <a class="shop" href="https://m.me/lucernapro"><span class="fbadge">f</span> Facebook chat</a>
        <a class="shop shop-line" href="https://lin.ee/LpUR3Ld">💬 Line @lucerna</a>
        <a class="shop" href="tel:0970799547">📞 097-079-9547</a>
      </div>
    </div>
  </div>
</section>
'''

if __name__ == '__main__':
    build('th')
    build('en')
