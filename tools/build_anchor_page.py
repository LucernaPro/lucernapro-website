#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_anchor_page.py — สร้าง /anchor และ /en/anchor

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
    # HIDDEN 26 ก.ย. 2026 (มติเจ้าของ "ซ่อนหน้าเว็บนี้ก่อน"): TDS ที่ใช้เป็นของ interface agent (สีฟ้า) แต่ของที่ซื้อคือ tile adhesive (สีเขียว) + MOQ สีฟ้า 1,500 กก. — noindex, ถอดการ์ดหน้าแรก/sitemap/search จนกว่าแผนสินค้าจะนิ่ง
    head = head.replace('<meta name="viewport"', '<meta name="robots" content="noindex,nofollow">\n<meta name="viewport"', 1)
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
    'th': 'Lucerna Anchor กาวรองหลังกระเบื้อง 2 ส่วนผสม — แผ่นใหญ่ ผิวเงา ปูทับกระเบื้องเดิม ไม่กลวง ไม่ร่อน | LucernaPro',
    'en': 'Lucerna Anchor — Two-Part Reaction-Resin Tile Back Adhesive for Large-Format Slabs, Glossy and Difficult Substrates | LucernaPro',
}
DESC = {
    'th': 'Lucerna Anchor กาวเรซิน 2 ส่วนผสม ประเภท Reaction Resin (Type R) ปาดหลังกระเบื้องบางแค่ 1 มม. แล้วกดลงปูนกาว — ยึดกระเบื้องแผ่นใหญ่ sintered stone และผิวเงาที่ปูนกาวจับไม่อยู่ ปูทับกระเบื้องเดิม กระจก โลหะ ผนังกันซึม ทนน้ำ ทนร้อน ยืดหยุ่น เวลาเปิดนาน 2 ชั่วโมง',
    'en': 'Lucerna Anchor — a two-part reaction-resin (Type R) tile back adhesive. A 1 mm skim on the back of the tile, then bed it into cement adhesive as usual — holds large-format slabs, sintered stone and glossy backs that cement alone cannot grip. Tile-over-tile, glass, metal, waterproofed walls. Water and heat resistant, flexible, 2-hour open time.',
}
OGT = {
    'th': 'Lucerna Anchor กาวรองหลังกระเบื้อง 2 ส่วนผสม — แผ่นใหญ่ ผิวเงา ไม่ร่อน',
    'en': 'Lucerna Anchor — Two-Part Tile Back Adhesive for Large Slabs and Glossy Backs',
}
OGD = {
    'th': 'ปาดหลังแผ่น 1 มม. แล้วปูด้วยปูนกาวตามปกติ — กระเบื้องแผ่นใหญ่ sintered stone ผิวเงา ปูทับกระเบื้องเดิม ทนน้ำ ทนร้อน ยืดหยุ่น 1 กก. ราว 1.2 ตร.ม.',
    'en': 'Skim 1 mm on the back of the tile, then bed it in cement adhesive as usual — large slabs, sintered stone, glossy backs, tile-over-tile. Water and heat resistant, flexible. 1 kg does about 1.2 m².',
}
SCHEMA = {
    'th': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"Lucerna Anchor กาวรองหลังกระเบื้อง 2 ส่วนผสม","brand":{"@type":"Brand","name":"LucernaPro"},"description":"กาวเรซิน 2 ส่วนผสม ประเภท Reaction Resin สำหรับปาดหลังกระเบื้องแผ่นใหญ่ sintered stone และผิวเงา ก่อนปูด้วยปูนกาว — ทนน้ำ ทนร้อน ยืดหยุ่น","image":"https://www.lucernapro.com/img/anchor-hero-sq.webp","url":"https://www.lucernapro.com/anchor","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"590","highPrice":"6500","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
    'en': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"Lucerna Anchor — Two-Part Reaction-Resin Tile Back Adhesive","brand":{"@type":"Brand","name":"LucernaPro"},"description":"Two-part reaction-resin tile back adhesive for large-format slabs, sintered stone and glossy tile backs, applied 1 mm on the tile before bedding in cement adhesive — water and heat resistant, flexible.","image":"https://www.lucernapro.com/img/anchor-hero-sq.webp","url":"https://www.lucernapro.com/en/anchor","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"590","highPrice":"6500","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
}

YT = 'O0LgqwvKovU'

BODY = {}

BODY['th'] = r'''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Adhesive <b>· กาว</b></div>
      <h1>Lucerna <span class="o">Anchor</span><br>กาวรองหลังกระเบื้อง 2 ส่วนผสม</h1>
      <p class="lede">กระเบื้องแผ่นใหญ่ sintered stone และกระเบื้องหลังเรียบเงา คือกลุ่มที่ปูนกาวธรรมดาจับไม่อยู่ — ปูเสร็จสวย เคาะแล้วกลวง อีกปีร่อนทั้งแผ่น Anchor คือ<b>กาวเรซิน 2 ส่วนผสม ประเภท Reaction Resin</b> ปาดหลังแผ่น<b>บางแค่ 1 มม.</b> แล้วปูด้วยปูนกาวตามปกติ ชั้นบางนี้คือตัวจับระหว่างหลังกระเบื้องกับปูนกาว — ผิวไหนที่ปูนไม่เกาะ กระจก โลหะ ผนังกันซึม กระเบื้องเดิม มันเกาะให้ ทนน้ำ ทนร้อน ยืดหยุ่น และให้เวลาทำงานนานถึง 2 ชั่วโมง</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">สั่งซื้อ / ดูราคา</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>ปรึกษาหน้างานฟรี</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/anchor-hero-sq.webp" alt="Lucerna Anchor ผสมสองส่วนเข้ากันแล้วเป็นเนื้อครีมสีเขียวสม่ำเสมอในถัง" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">ทำไมกระเบื้องแผ่นใหญ่ <em>ถึงต้องมีชั้นนี้</em></h2>
    <p class="sec-sub">ปูนกาวเกาะด้วยการซึมเข้าผิว — หลังแผ่นใหญ่รุ่นใหม่ทำมาแน่นและเรียบจนปูนซึมไม่ได้ Anchor เกาะด้วยปฏิกิริยาเคมีกับผิวโดยตรง ไม่ต้องอาศัยรูพรุน</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>จับผิวที่ปูนกาวจับไม่อยู่</h4><p>หลัง sintered stone หลังกระเบื้องพอร์ซเลนดูดซึมน้ำต่ำ กระจก โลหะ แผ่นไฟเบอร์ซีเมนต์ OSB และผนังที่ทากันซึมไว้แล้ว — ผิวที่ปูนกาวได้แค่ "วางทับ" Anchor เกาะเป็นเนื้อเดียวกับผิว แล้วปูนกาวเกาะ Anchor อีกที</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>บางแค่ 1 มม. ไม่เปลี่ยนวิธีปู</h4><p>ไม่ใช่กาวปูเต็มแผ่น ปาดหลังแผ่นบางๆ (ผนังลื่นก็ฉาบผนังด้วย) ที่เหลือคือปูนกาวและเกรียงหวีเหมือนเดิม ช่างไม่ต้องเรียนวิธีใหม่ 1 กก. ทำได้ราว 1.2 ตร.ม. ต้นทุนเพิ่มต่อตารางเมตรถูกกว่าค่ารื้อกระเบื้องที่ร่อนหลายเท่า</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>ทนน้ำ ทนร้อน และยืดหยุ่น</h4><p>ผ่านทดสอบต้มในน้ำเดือด 100°C และแช่แข็ง −30°C โดยไม่หลุด ฟิล์ม 1 มม. งอได้ 360° ไม่แตก — กระเบื้องแผ่นใหญ่ตากแดดขยายตัวมากกว่าแผ่นเล็ก ชั้นที่ยืดตามได้คือชั้นที่ไม่ร่อน ใช้ได้ทั้งผนังภายนอก ห้องน้ำ และรอบสระ</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>เวลาทำงาน 2 ชั่วโมง ไม่ต้องรีบ</h4><p>เวลาเปิด 120–150 นาทีที่ 23°C ปาดหลังแผ่นทีละหลายแผ่นแล้วค่อยปูก็ทัน (อากาศร้อนของบ้านเราสั้นลง — ผสมทีละเท่าที่ใช้ทันในหนึ่งชั่วโมง) ไม่มีฝุ่นปูน ไม่มีกลิ่นฟอร์มาลดีไฮด์ ผสมด้วยเกรียงในถังได้เลย</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="howworks">
  <div class="wrap">
    <h2 class="sec-h">ทำงานยังไง — <em>2 ชั้น เปียกชนเปียก</em></h2>
    <p class="sec-sub">ไม่ต้องรอแห้ง ไม่ต้องรองพื้นก่อน — ปาด Anchor แล้วโปะปูนกาวตามได้ทันที สองชั้นแข็งตัวไปพร้อมกันเป็นชั้นเดียว</p>
    <div class="ggrid" style="margin-top:20px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-step1.webp" alt="ขั้นที่ 1 — ปาด Lucerna Anchor สีฟ้าอมเขียวบางๆ ด้วยเกรียงเรียบลงบนหลังกระเบื้องที่มีร่องหวีจากโรงงาน" width="1200" height="630"></div><figcaption><span class="no">01</span><b>ปาด Anchor บาง 1 มม. บนหลังแผ่น</b> — ใช้เกรียงเรียบรีดให้เต็มแผ่นถึงขอบ ชั้นนี้เกาะเป็นเนื้อเดียวกับหลังกระเบื้องที่แน่นและเรียบจนปูนกาวธรรมดาจับไม่อยู่</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-step2.webp" alt="ขั้นที่ 2 — โปะปูนกาวสีเทาลงบนชั้น Lucerna Anchor ที่ยังเปียก ด้วยเกรียงตัก" width="1200" height="630"></div><figcaption><span class="no">02</span><b>โปะปูนกาวตามทันที ขณะ Anchor ยังเปียก</b> — ไม่ต้องรอแห้ง ใช้เกรียงตักปูนกาวโปะลงไปเลย แล้วเกลี่ยให้ทั่วแผ่นเหมือนปูปกติ ก่อนยกไปติดผนัง ปูนกาวฝังตัวลงในชั้น Anchor ที่ยังเปียก ทั้งสองชั้นแข็งตัวไปด้วยกัน</figcaption></figure>
    </div>
    <p class="pricenote">ทำไมต้องเปียกชนเปียก: ถ้าปล่อยให้ Anchor แห้งก่อน ผิวจะเรียบเป็นฟิล์ม ปูนกาวจะได้แค่วางทับ — โปะขณะยังเปียก ปูนกาวจึงประสานเข้าไปในเนื้อ Anchor และ Anchor ประสานเข้าไปในหลังแผ่น กระเบื้อง → Anchor → ปูนกาว → ผนัง กลายเป็นชั้นเดียวที่ไม่มีรอยต่อให้ร่อน · ผนังที่ลื่นด้วย (ปูทับกระเบื้องเดิม ผนังกันซึม) ฉาบ Anchor ที่ผนังเพิ่มอีกฝั่ง</p>
  </div>
</section>

<section class="story" id="slabs">
  <div class="wrap">
    <div class="rdtag">LARGE FORMAT — งานที่ Anchor เกิดมาเพื่อสิ่งนี้</div>
    <h2>แผ่นละหลายพัน ยกด้วยเครื่องดูด ติดครั้งเดียว —<br><b>งานแบบนี้ไม่มีโอกาสแก้ตัว</b></h2>
    <figure class="packshot" style="max-width:960px;margin:18px 0 22px">
      <img loading="lazy" decoding="async" src="/img/anchor-lobby.webp" alt="ช่างสองคนยกแผ่นหินสังเคราะห์ 120×240 ด้วยเครื่องดูดสุญญากาศเข้าติดผนังโถงอาคาร ข้างๆ มีรถ A-frame วางแผ่นที่หลังเคลือบ Anchor สีฟ้าอมเขียวไว้แล้ว" width="1024" height="559">
      <figcaption>โถงอาคารระหว่างติดตั้งแผ่นหินสังเคราะห์ 120×240 — แผ่นบนรถ A-frame ปาด Anchor ที่หลังแผ่นรอไว้แล้ว ยกด้วยเครื่องดูดสุญญากาศเข้าติดผนังที่ปาดปูนกาว ตัวหนอนสีส้มกำหนดร่องบางตามแบบ</figcaption>
    </figure>
    <div class="story-grid">
      <div class="bignum">2.88<small>ตร.ม. ต่อแผ่น 120 × 240 — ANCHOR ≈ 750 บาท</small></div>
      <div class="story-body">
        <p>หินสังเคราะห์และกระเบื้องแผ่นใหญ่ 120×240 คือของที่โครงการคอนโด โรงแรม และหน้าร้านเลือกใช้เพราะร่องน้อย ดูเป็นผืนเดียว — แต่สิ่งที่ทำให้มันสวยคือสิ่งเดียวกับที่ทำให้มันร่อน: <b>หลังแผ่นเผาจนแน่นและเรียบ ดูดซึมน้ำแทบเป็นศูนย์</b> ปูนกาวซีเมนต์ที่เกาะด้วยการซึมเข้าผิว จึงได้แค่วางทับ พอแผ่นขยายตัวจากแดดหรือความร้อน ชั้นปูนกับหลังแผ่นก็แยกกันทีละนิดจนกลวง</p>
        <div class="beats">
          <div class="beat"><div class="k">ทำไมงานนี้ต้องมี</div><p>แผ่นหนึ่งหนักหลายสิบกิโล ราคาหลายพันถึงหลักหมื่น ยกด้วยเครื่องดูดสุญญากาศ ติดแล้วยาแนวเสร็จ ถ้าปีถัดไปเคาะแล้วกลวง ทางแก้เดียวคือรื้อ ซื้อแผ่นใหม่ ปูใหม่ และไปอธิบายเจ้าของโครงการ — ค่า Anchor แผ่นละราว 750 บาท เทียบกับตัวเลขนั้นคือเศษเงิน</p></div>
          <div class="beat"><div class="k">ทำงานกับขั้นตอนเดิม</div><p>ปาด Anchor ที่หลังแผ่นตอนแผ่นพิงอยู่บนรถ A-frame แล้วโปะปูนกาวตามทันที ยกขึ้นติดผนังตามปกติ ไม่ต้องเปลี่ยนปูนกาว ไม่ต้องเปลี่ยนเครื่องมือ เวลาเปิดสองชั่วโมงพอให้ปาดรอไว้ทีละหลายแผ่น</p></div>
          <div class="beat"><div class="k">ยืดตามแผ่นได้</div><p>แผ่น 240 ซม. ขยายตัวมากกว่ากระเบื้องเล็กหลายเท่า ชั้น Anchor ยืดหยุ่น งอได้ 360° ไม่แตก จึงรับการขยับของแผ่นแทนที่จะแยกออกจากมัน — ผนังภายนอกที่โดนแดดครึ่งวันคือที่ที่ต่างกันชัดที่สุด</p></div>
          <div class="beat"><div class="k">ผนังที่ปูนกาวไม่ชอบ</div><p>โถงที่ผนังทากันซึมไว้แล้ว ผนังยิปซัมหรือไฟเบอร์ซีเมนต์ ผนังกระเบื้องเดิมของอาคารรีโนเวต — ฉาบ Anchor บนผนังเพิ่มจากหลังแผ่น แล้วปูตามปกติ ผนังแบบนี้กลายเป็นผนังที่ปูนกาวเกาะได้</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">ดูของจริงก่อน — <em>คลิปและภาพ</em></h2>
    <p class="sec-sub">บันไดกระเบื้องที่ยึดกันด้วยกาวตัวนี้ล้วนๆ เนื้อกาวหลังผสม และการฉาบฝั่งผนัง</p>
    <div class="vidgrid vert solo">
      <figure style="margin:0">
        <div class="fbv v916"><iframe loading="lazy" src="https://www.youtube.com/embed/''' + YT + r'''" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="Lucerna Anchor — บันไดกระเบื้องที่ยึดด้วยกาวตัวนี้ รับน้ำหนักคนเดินขึ้น"></iframe></div>
        <figcaption><b>บันไดกระเบื้องที่ยึดด้วยกาวตัวนี้</b> — สันกระเบื้องหนา 1 ซม. ติดเข้ากับผิวเงาของกระเบื้องแผ่นใหญ่ ต่อกันเป็นขั้นบันไดแล้วเดินขึ้นจริง เป็นการสาธิตแรงยึด ไม่ใช่วิธีติดตั้งที่แนะนำ</figcaption>
      </figure>
    </div>
    <div class="ggrid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:18px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g01.webp" alt="เนื้อกาว Lucerna Anchor บนเกรียง — เนื้อครีมข้นสีเขียวมีเม็ดทรายละเอียด ไม่ไหลย้อย" width="720" height="720"></div><figcaption><span class="no">01</span>เนื้อกาวหลังผสม — ครีมข้นมีทรายละเอียด เกาะเกรียงไม่ไหล</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g02.webp" alt="ปาด Lucerna Anchor บนหลังกระเบื้องด้วยเกรียงหวี เห็นร่องกาวเรียบสม่ำเสมอ" width="720" height="720"></div><figcaption><span class="no">02</span>ปาดหลังแผ่นด้วยเกรียงหวี — ชั้นบางสม่ำเสมอ ไม่ต้องหนา</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g03.webp" alt="ฉาบ Lucerna Anchor ด้วยเกรียงหวีลงบนผนังข้างกระเบื้องเดิม ก่อนนำกระเบื้องที่ปาดปูนกาวแล้วมาติดทับ" width="720" height="720"></div><figcaption><span class="no">03</span>ผนังลื่น (ปูทับกระเบื้องเดิม ผนังกันซึม) — ฉาบ Anchor บนผนังด้วย เพิ่มจากที่ปาดหลังแผ่น</figcaption></figure>
    </div>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">ใช้กับ<em>งานไหน</em></h2>
    <p class="sec-sub">ทุกงานที่หลังกระเบื้องหรือผนัง "เรียบเกินไป" สำหรับปูนกาว</p>
    <div class="pts">
      <div class="pt"><span class="ic">🧱</span><div><h4>กระเบื้องแผ่นใหญ่ · sintered stone บนผนัง</h4><p>แผ่น 60×120 ขึ้นไปจนถึง 120×240 ที่น้ำหนักมากและหลังแผ่นแน่น — ชั้น Anchor หลังแผ่นทำให้ปูนกาวจับแผ่นได้เต็มหน้า ลดจุดกลวงและการร่อนในปีต่อๆ ไป ใช้ร่วมกับปูนกาวชนิดสำหรับแผ่นใหญ่ตามปกติ</p></div></div>
      <div class="pt"><span class="ic">🔁</span><div><h4>ปูทับกระเบื้องเดิม ไม่ต้องรื้อ</h4><p>ห้องน้ำ ห้องครัว ที่อยากเปลี่ยนหน้าใหม่แต่ไม่อยากทุบ — ปาด Anchor บนหลังแผ่นใหม่ แล้วปูลงบนกระเบื้องเดิมที่ล้างสะอาดด้วยปูนกาว ผิวเงาของกระเบื้องเก่าไม่ใช่ปัญหาอีก</p></div></div>
      <div class="pt"><span class="ic">🪟</span><div><h4>ผิวยาก — กระจก โลหะ ไฟเบอร์ซีเมนต์ ผนังกันซึม</h4><p>ผนังที่ทากันซึมไว้แล้ว แผ่นไฟเบอร์ซีเมนต์ OSB แผ่นเหล็ก กระจก — ผิวที่ช่างส่วนใหญ่ต้องหาทางออกด้วยตะแกรงหรือรองพื้นหลายชั้น — ผนังแบบนี้ฉาบ Anchor ลงบนผนังทั้งผืนเพิ่มจากที่ปาดหลังแผ่น ลื่นสองฝั่งก็ปาดสองฝั่ง</p></div></div>
      <div class="pt"><span class="ic">🪝</span><div><h4>ติดของชิ้นเล็กบนกระเบื้องโดยไม่เจาะ</h4><p>ตะขอ ที่จับ ป้าย ชั้นวางของเบา บนกระเบื้องผิวเงาที่เจาะแล้วเสี่ยงแตก — ทาทั้งหน้าสัมผัสแล้วกดยึด <b>งานรับน้ำหนักจริงยังต้องยึดด้วยพุกหรือสกรู</b> อ่านข้อจำกัดด้านล่างก่อนใช้</p></div></div>
    </div>
    <div class="warn"><b>⚠ อย่าใช้ยึดของหนัก:</b> ชั้นวางที่จะวางของหนัก ราวจับที่คนโหน ของที่แขวนเหนือหัวคนหรือเหนือเตียง ต้องยึดด้วยพุกหรือสกรูเชิงกลเสมอ กาวเป็นตัวเสริม ไม่ใช่ตัวรับน้ำหนักหลัก — ตราบใดที่ยังไม่มีตัวเลขรับน้ำหนักที่เราวัดเองบนหน้านี้ ให้ถือว่ารับน้ำหนักไม่ได้ไว้ก่อน งานที่ไม่แน่ใจ ทักมาถามพร้อมรูปหน้างาน</div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">สเปคทางเทคนิค <em>ตัวเลขจากการทดสอบ</em></h2>
    <p class="sec-sub">ค่าทั่วไปของกาวและฟิล์มหลังแข็งตัว</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>รายการ</th><th>ค่า</th><th>หมายเหตุ</th></tr></thead>
        <tbody>
          <tr><td>ชนิด</td><td>กาวเรซิน 2 ส่วนผสม ประเภท Reaction Resin</td><td>มาตรฐาน JC/T 547-2017 Type R</td></tr>
          <tr><td>ส่วน A</td><td>เรซินพรีโพลิเมอร์ดัดแปลงด้วยซิเลน (ครีมขาว)</td><td></td></tr>
          <tr><td>ส่วน B</td><td>สารบ่มพรีโพลิเมอร์กลุ่มเอมีน (ครีมฟ้า)</td><td>ผสมแล้วเป็นสีเขียวสม่ำเสมอ</td></tr>
          <tr><td>อัตราส่วนผสม</td><td>A : B = 1 : 1 โดยน้ำหนัก</td><td>ชั่งให้ตรง</td></tr>
          <tr><td>ความหนาที่ใช้</td><td>1 มม. บนหลังแผ่น</td><td>ปูด้วยปูนกาวตามปกติ</td></tr>
          <tr><td>อัตราการใช้</td><td>ชุด 20 กก. ≈ 25–30 ตร.ม.</td><td>1 กก. ≈ 1.2 ตร.ม.</td></tr>
          <tr><td>เวลาเปิด (open time)</td><td>120–150 นาที</td><td>ที่ 23°C — อากาศร้อนสั้นลง</td></tr>
          <tr><td>ทนอุณหภูมิ</td><td>ต้ม 100°C / แช่แข็ง −30°C ไม่หลุด</td><td>ทดสอบต้มน้ำเดือดและวัฏจักรแช่แข็ง-ละลาย</td></tr>
          <tr><td>ความยืดหยุ่น</td><td>ฟิล์ม 1 มม. งอ 360° ไม่แตก</td><td></td></tr>
          <tr><td>ทนสารเคมี</td><td>ทนน้ำ ทนด่าง ทนความร้อน ทนการเสื่อมสภาพ</td><td></td></tr>
          <tr><td>ฟอร์มาลดีไฮด์ / VOC</td><td>ไม่พบ / ไม่มี</td><td></td></tr>
          <tr><td>บรรจุ</td><td>1 กก. (A 500 g + B 500 g) · 5 กก. · ชุด 20 กก.</td><td></td></tr>
          <tr><td>อายุการเก็บ</td><td>12 เดือน ไม่เปิดถัง</td><td>เก็บในร่ม ปิดฝาสนิท</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">ขนาดและราคา</h2>
    <p class="sec-sub">ชุด A + B ชั่งมาให้ตรง 1:1 แล้ว — กรอกพื้นที่ปูให้ระบบจัดชุดที่ถูกที่สุดให้ได้</p>
    <div class="pricecard">
      <table data-calc="1" data-shipping="70">
        <thead><tr><th>ขนาด</th><th>พื้นที่ปูโดยประมาณ</th><th>ราคา</th><th>ค่าส่ง</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="1.25" data-ship="70">1 กก.<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 500 g + B 500 g</small></td><td>≈ 1.2 ตร.ม. · ซ่อมแผ่นร่อน ติดของชิ้นเล็ก</td><td class="pr" data-price="590">590.-</td><td class="pr">70.-</td></tr>
          <tr><td class="sz" data-sqm="6.25" data-ship="130">5 กก.<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 2.5 kg + B 2.5 kg</small></td><td>≈ 6 ตร.ม. · ห้องน้ำหนึ่งห้อง</td><td class="pr" data-price="1990">1,990.-</td><td class="pr">130.-</td></tr>
          <tr data-calc="skip"><td class="sz">ชุด 20 กก.<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 10 kg + B 10 kg</small></td><td>≈ 25 ตร.ม. · งานผู้รับเหมา</td><td class="pr">6,500.-</td><td class="pr">ตามจริง — สอบถาม</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">ราคารวม VAT · พื้นที่คิดจากการปาดหลังแผ่น 1 มม. (ชุด 20 กก. ≈ 25–30 ตร.ม. เราคิดด้านต่ำไว้ก่อน) · ผิวหลังแผ่นที่มีร่องลึกใช้มากกว่านี้ · <b>สั่งจำนวนมากมีราคาผู้รับเหมา</b> ส่งขนาดแผ่นและพื้นที่มาทางแชท เราคำนวณให้ฟรีก่อนสั่ง</p>
  </div>
</section>

<section class="buybox" id="cost">
  <div class="wrap">
    <h2 class="sec-h">คิดเงินให้เห็นก่อน — <em>งานนี้เพิ่มเท่าไหร่</em></h2>
    <p class="sec-sub">สำหรับช่างที่ต้องบวกลงใบเสนอราคา — ตัวเลขคิดจากปาดหลังแผ่น 1 มม. ที่ 1.2 ตร.ม./กก. (ด้านต่ำ) ราคารวม VAT ยังไม่รวมค่าส่ง</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>งาน</th><th>พื้นที่</th><th>ใช้ Anchor</th><th>เป็นเงิน</th><th>ตกตร.ม.ละ</th></tr></thead>
        <tbody>
          <tr><td>ซ่อมแผ่นร่อน / ติดของชิ้นเล็ก</td><td>ไม่เกิน 1 ตร.ม.</td><td>1 กก.</td><td><b>590</b></td><td>—</td></tr>
          <tr><td>ห้องน้ำ 1 ห้อง (ผนัง)</td><td>≈ 6 ตร.ม.</td><td>5 กก.</td><td><b>1,990</b></td><td>≈ 330</td></tr>
          <tr><td>ผนังครัว + ห้องน้ำ</td><td>≈ 12 ตร.ม.</td><td>5 กก. × 2</td><td><b>3,980</b></td><td>≈ 330</td></tr>
          <tr><td>ผนังโถง / หน้าร้าน แผ่นใหญ่</td><td>≈ 25 ตร.ม.</td><td>ชุด 20 กก.</td><td><b>6,500</b></td><td>≈ 260</td></tr>
          <tr><td>อาคาร / โครงการ</td><td>≈ 50 ตร.ม.</td><td>ชุด 20 กก. × 2</td><td><b>13,000</b></td><td>≈ 260</td></tr>
        </tbody>
      </table>
    </div>
    <div class="speccard" style="margin-top:14px">
      <table>
        <thead><tr><th>คิดเป็นต่อแผ่น (ที่ราคาชุด 20 กก.)</th><th>พื้นที่แผ่น</th><th>Anchor ต่อแผ่น</th><th>เป็นเงินต่อแผ่น</th></tr></thead>
        <tbody>
          <tr><td>กระเบื้อง 60 × 120 ซม.</td><td>0.72 ตร.ม.</td><td>≈ 0.6 กก.</td><td><b>≈ 190 บาท</b></td></tr>
          <tr><td>กระเบื้อง 80 × 160 ซม.</td><td>1.28 ตร.ม.</td><td>≈ 1.0 กก.</td><td><b>≈ 330 บาท</b></td></tr>
          <tr><td>sintered stone 120 × 240 ซม.</td><td>2.88 ตร.ม.</td><td>≈ 2.3 กก.</td><td><b>≈ 750 บาท</b></td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">แผ่น 60×120 บวกไปแผ่นละไม่ถึง 200 บาท แผ่นใหญ่ 120×240 ราว 750 — เทียบกับค่าแผ่นและค่าแรงปูแผ่นนั้น และค่ารื้อทำใหม่ถ้าแผ่นร่อน ตัวเลขนี้คือประกันที่ถูกที่สุดในงาน · หลังแผ่นที่มีร่องลึกหรือลายนูนใช้มากกว่านี้ เผื่อไว้ 10–20% · วิธีฉาบบนผนังใช้มากกว่าปาดหลังแผ่นตามความลึกฟันเกรียง ส่งขนาดงานมาทางแชท เราคิดปริมาณให้</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">วิธีใช้งาน — <em>จบบนหน้านี้</em></h2>
    <p class="sec-sub">ขั้นตอนเดียวที่เพิ่มจากการปูปกติคือชั้น Anchor บางๆ ที่หลังแผ่น — ที่เหลือคือปูนกาวและเกรียงหวีเหมือนเดิม</p>
    <div class="warn" style="margin:0 0 22px;border-color:var(--orange);background:rgba(237,106,47,.08);color:var(--ink)"><b>กฎข้อเดียว — Anchor อยู่ฝั่งที่ลื่น:</b> ปูนกาวเกาะได้เฉพาะผิวที่ดูดซึม กระเบื้องแผ่นใหญ่ที่หลุด ส่วนใหญ่หลุดฝั่งหลังแผ่น (ปูนกาวยังติดผนังเป็นร่องหวี หลังแผ่นเกลี้ยง) ดังนั้น<b>ปาดหลังแผ่นเสมอ</b> · ถ้าผนังก็ลื่นด้วย — ปูทับกระเบื้องเดิม ผนังกันซึม กระจก โลหะ แผ่นไฟเบอร์ซีเมนต์ — <b>ปาดทั้งสองฝั่ง</b> หลังแผ่นและผนัง · ส่วนผนังปูนฉาบต้องแน่น ไม่มีฝุ่น ไม่มีคราบน้ำปูน แผ่นที่หลุดพร้อมผิวปูนฉาบติดมาด้วยคือผนังผุ ไม่ใช่เรื่องกาว</div>
    <ol class="flow">
      <li class="fstep"><h4>เตรียมผิว — ผนังแข็งแรง แห้ง หลังแผ่นสะอาด</h4><p>ผนังต้องแน่น ไม่มีฝุ่นหรือชั้นสีร่อน กระเบื้องเดิมที่จะปูทับให้ล้างคราบสบู่และคราบมันออก เคาะหาแผ่นกลวงแล้วซ่อมก่อน หลังแผ่นใหม่ให้เช็ดฝุ่นและคราบผงจากโรงงานออกด้วยผ้าหมาด — อยากให้ทนขั้นสุด ล้างหลังแผ่นแล้วเช็ดแห้งก่อนปาด</p><span class="fchip">หลังแผ่นสะอาด แห้ง</span></li>
      <li class="fstep"><h4>ผสม A : B = 1 : 1 โดยน้ำหนัก จนเป็นสีเขียวเดียวทั่วถัง</h4><p>ตักส่วน A และ B น้ำหนักเท่ากันลงถังเดียว กวนด้วยเกรียงหรือหัวปั่นรอบต่ำจน<b>ไม่เหลือริ้วสีขาวหรือฟ้า</b> ทั้งก้นถังและข้างถัง สีเขียวสม่ำเสมอคือสัญญาณว่าผสมเข้ากันแล้ว — ชุดเล็ก 1 กก. ที่เราชั่งมาให้ เทรวมกันทั้งสองกระปุกได้เลย ผสมทีละเท่าที่ปูทันในราวหนึ่งชั่วโมง</p><span class="fchip">1:1 โดยน้ำหนัก</span><span class="fchip">สีเดียวทั่ว ไม่มีริ้ว</span></li>
      <li class="fstep"><h4>ปาด Anchor บาง 1 มม. ที่หลังแผ่น — ผนังลื่นก็ฉาบผนังด้วย</h4><p>ใช้เกรียงเรียบหรือเกรียงหวีฟันเล็ก ปาดกาวลงหลังกระเบื้องให้เต็มแผ่นถึงขอบ ความหนาราว 1 มม. ทำทีละหลายแผ่นแล้วพิงไว้รอปูได้ภายในเวลาเปิด · <b>ถ้าผนังลื่น</b> (ปูทับกระเบื้องเดิม ผนังกันซึม กระจก โลหะ ไฟเบอร์ซีเมนต์) ฉาบ Anchor บนผนังด้วยเกรียงหวีเป็นผืนเพิ่มอีกฝั่ง เหมือนในภาพที่ 03 ฉาบทีละผืนเท่าที่ปูทันในเวลาเปิด ฝั่งผนังใช้กาวมากกว่าหลังแผ่นตามความลึกฟันเกรียง · ไม่ต้องหนา หนาไปเปลืองและไม่ได้แข็งแรงขึ้น</p><span class="fchip">หลังแผ่นเสมอ</span><span class="fchip">ผนังลื่น = ทั้งสองฝั่ง</span></li>
      <li class="fstep"><h4>โปะปูนกาวทับ แล้วกดแผ่นเข้าผนังขณะ Anchor ยังเปียก</h4><p>ปาดปูนกาวชนิดสำหรับแผ่นใหญ่บนผนังด้วยเกรียงหวีตามปกติ (หรือโปะลงบนหลังแผ่นที่ปาด Anchor ไว้แล้วเกลี่ย) แล้วยกแผ่นกดเข้าผนัง · ไม่ต้องรอ Anchor แห้ง — โปะปูนกาวทับได้ทันที แต่ต้องประกบ<b>ก่อนที่ชั้น Anchor จะแห้งผิว</b> (ภายใน 120–150 นาทีที่ 23°C — กลางแดดหรืออากาศร้อนจัดให้เผื่อสั้นกว่านั้นมาก) กดและเคาะไล่อากาศเหมือนงานปูทั่วไป ปรับระดับได้ตามเวลาเปิดของปูนกาว</p><span class="fchip">wet-on-wet</span><span class="fchip">ภายในเวลาเปิด</span></li>
      <li class="fstep"><h4>ปล่อยให้แข็งตัวตามรอบปูนกาว แล้วยาแนวตามปกติ</h4><p>เวลารอยาแนวและเปิดใช้งานเป็นไปตามข้อกำหนดของปูนกาวที่ใช้ — ชั้น Anchor แข็งตัวไปพร้อมกันโดยไม่ต้องทำอะไรเพิ่ม กาวที่เลอะหน้าแผ่นเช็ดออกทันทีขณะยังเปียก แข็งแล้วต้องขูด · <b>งานติดของชิ้นเล็กโดยตรง:</b> ทาให้เต็มหน้าสัมผัสทั้งสองด้าน กดยึดแล้วค้ำไว้ ทิ้งข้ามคืนก่อนแขวนของ</p></li>
    </ol>

    <div class="warn"><b>⚠ ความปลอดภัย:</b> เป็นกาวเรซิน 2 ส่วนผสม ส่วน B มีสารบ่มกลุ่มเอมีนที่ระคายผิวหนังและอาจทำให้แพ้เมื่อสัมผัสซ้ำ — สวมถุงมือไนไตรล์และแว่นครอบตาทุกครั้ง ทำงานในที่อากาศถ่ายเท ถ้าเปื้อนผิวเช็ดออกแล้วล้างด้วยสบู่และน้ำทันที (ไม่ใช้ทินเนอร์ล้างมือ) เข้าตาล้างน้ำต่อเนื่องหลายนาทีแล้วพบแพทย์ กาวที่ผสมแล้วเหลือ ปล่อยให้แข็งในถังก่อนทิ้ง เก็บถังปิดสนิทพ้นมือเด็กและแสงแดด</div>
  </div>
</section>

<section class="story" id="straight">
  <div class="wrap">
    <div class="rdtag">STRAIGHT TALK — ความจริงที่ต้องพูด</div>
    <h2>ก่อนจ่ายเงิน อ่าน 5 ข้อนี้ก่อน —<br><b>ตัวนี้ไม่ใช่ของวิเศษ</b> และเราไม่อยากให้คุณเข้าใจผิด</h2>
    <div class="story-grid">
      <div class="bignum">5<small>สิ่งที่คนขายส่วนใหญ่ไม่บอก</small></div>
      <div class="story-body">
        <div class="beats">
          <div class="beat"><div class="k">1 · ไม่ได้มาแทนปูนกาว</div><p>ตัวนี้เป็น<b>ชั้นรองหลังแผ่น</b> ยังต้องปูด้วยปูนกาวเต็มแผ่นตามปกติ ถ้าเอามาปาดแทนปูนกาวทั้งแผ่นจะแพงมากและไม่ได้ช่วยเรื่องระดับ — งานปูเต็มแผ่นด้วยเรซินล้วนเป็นงานอีกแบบ ทักมาคุยก่อน</p></div>
          <div class="beat"><div class="k">2 · อากาศร้อนกินเวลาทำงานไปครึ่งหนึ่ง</div><p>ตัวเลข 120–150 นาทีวัดที่ 23°C บ้านเราหน้างานกลางแจ้ง 35°C ให้คิดว่าเหลือราวชั่วโมงเดียว ผสมทีละไม่มาก ปาดแล้วปูให้จบเป็นล็อต อย่าผสมทั้งถังตอนเช้าแล้วใช้ทั้งวัน</p></div>
          <div class="beat"><div class="k">3 · ผิวสกปรกและผนังผุ คือสาเหตุอันดับหนึ่งของงานพัง</div><p>กาวเกาะสิ่งที่อยู่บนผิว ฝุ่นปูน คราบมัน ผงจากโรงงานหลังแผ่น — เกาะแน่นกับสิ่งสกปรก แล้วสิ่งสกปรกหลุดจากแผ่น ผลคือดูเหมือนกาวไม่ติด ทั้งที่กาวติดดีมาก เช็ดหลังแผ่นทุกแผ่นก่อนปาด · และ Anchor ไม่ซ่อมผนังผุ — ถ้าปูนฉาบร่วน มีฝุ่น หรือมีคราบน้ำปูน แผ่นจะหลุดพร้อมผิวปูนติดมาด้วย ผนังต้องแน่นก่อน</p></div>
          <div class="beat"><div class="k">4 · ส่วน B แพ้อากาศ เปิดแล้วต้องใช้</div><p>สารบ่มกลุ่มเอมีนโดนอากาศและความชื้นแล้วค่อยๆ เปลี่ยนสภาพ กระปุกที่เปิดแล้วปิดไม่สนิท ทิ้งไว้เป็นเดือน ผสมแล้วอาจแข็งช้าหรือไม่แข็ง — ซื้อขนาดที่ใช้หมดในงานเดียว เราถึงแบ่งชุด 1 กก. ไว้ให้</p></div>
          <div class="beat"><div class="k">5 · ไม่ใช่ยาแนว ไม่ใช่ตัวอุดร่อง</div><p>มันคือกาวชั้นบาง ไม่ใช่วัสดุเติมช่องว่างหรือกันซึมรอยต่อ ร่องยาแนวใช้ยาแนว รอยต่อที่ขยับใช้ซีลแลนต์ พื้นที่ต้องกันซึมทากันซึมก่อนแล้วค่อยปูทับ — Anchor เกาะผนังกันซึมได้ดี แต่ไม่ได้ทำหน้าที่แทน</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">งานของคุณ<em>ใช่ตัวนี้ไหม</em></h2>
    <p class="sec-sub">ถ้าโจทย์ไม่ใช่หลังกระเบื้องกับผนัง สองตัวนี้อาจตรงกว่า</p>
    <div class="altgrid">
      <a class="altcard" href="/carbontilegrout">
        <div class="k">ร่องยาแนว · สระว่ายน้ำ · ห้องน้ำ</div>
        <h4>ยาแนว Carbon</h4>
        <p>ปูเสร็จแล้วร่องระหว่างแผ่นคือด่านต่อไป — ยาแนวสองส่วนผสมสำหรับที่เปียกตลอด ไม่ดำ ไม่ร่อน</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
      <a class="altcard" href="/flexgrip">
        <div class="k">ซ่อมของ · ติดวัสดุต่างชนิด</div>
        <h4>กาวบ้าพลัง FlexGrip</h4>
        <p>งานติดชิ้นเล็กทั่วบ้านที่ต้องการกาวขวดเดียวไม่ต้องผสม ยืดหยุ่น ติดได้แทบทุกวัสดุ</p>
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
      <div class="sub">บอกขนาดแผ่น พื้นที่ และผนังที่จะปูมาได้เลย ทีมงานคำนวณปริมาณให้ฟรีก่อนสั่ง · <b>ผู้รับเหมาและร้านกระเบื้อง มีราคาจำนวนมาก</b></div>
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
      <h1>Lucerna <span class="o">Anchor</span><br>Two-Part Tile Back Adhesive</h1>
      <p class="lede">Large-format porcelain, sintered stone and tiles with smooth, glossy backs are the ones ordinary cement adhesive cannot grip — they look perfect on day one, sound hollow when tapped, and let go a year later. Anchor is a <b>two-part reaction-resin adhesive</b>: skim it <b>just 1 mm</b> on the back of the tile, then bed the tile in cement adhesive exactly as you always do. That thin layer is the grip between the tile and the mortar — and it grips what cement won't: glass, metal, waterproofed walls, old tiles. Water and heat resistant, flexible, with a 2-hour working window.</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">Order / Prices</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>Free advice on chat</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/anchor-hero-sq.webp" alt="Lucerna Anchor after mixing the two parts — a uniform green cream in the bucket" width="900" height="900">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">Why large slabs <em>need this layer</em></h2>
    <p class="sec-sub">Cement adhesive holds by soaking into the surface. The backs of modern large-format tiles are so dense and smooth that there is nothing for it to soak into. Anchor bonds to the surface chemically — no pores needed.</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>Grips what cement cannot</h4><p>Sintered stone, low-absorption porcelain backs, glass, metal, fibre-cement board, OSB and walls already coated with waterproofing — surfaces cement adhesive merely sits against. Anchor bonds to the surface itself, and the cement adhesive bonds to Anchor.</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>1 mm thick — nothing else changes</h4><p>Not a full-bed adhesive. Skim the back of the tile (and the wall too if it is smooth); the rest is cement adhesive and a notched trowel as usual, and the tiler learns nothing new. 1 kg covers about 1.2 m², and the extra cost per square metre is a fraction of ripping out tiles that let go.</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>Water, heat and movement</h4><p>Survives boiling at 100°C and freezing at −30°C without releasing; a 1 mm film bends 360° without cracking. Large slabs in the sun move more than small tiles, and the layer that moves with them is the layer that doesn't let go — exterior walls, bathrooms, pool surrounds.</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>A 2-hour window — no rush</h4><p>Open time of 120–150 minutes at 23°C, so you can skim several tiles ahead and lay them at your pace (Thai heat shortens it — mix what you can lay within an hour). No cement dust, no formaldehyde, mixes with a trowel in the bucket.</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="howworks">
  <div class="wrap">
    <h2 class="sec-h">How it works — <em>two layers, wet on wet</em></h2>
    <p class="sec-sub">No waiting, no primer — skim Anchor, then put the cement adhesive straight on top. The two layers cure together as one.</p>
    <div class="ggrid" style="margin-top:20px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-step1.webp" alt="Step 1 — a thin teal layer of Lucerna Anchor skimmed with a flat trowel over the factory-ribbed back of a tile" width="1200" height="630"></div><figcaption><span class="no">01</span><b>Skim 1 mm of Anchor on the tile back</b> — a flat trowel, edge to edge. This layer bonds into a tile back so dense and smooth that ordinary cement adhesive cannot grip it.</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-step2.webp" alt="Step 2 — grey cement adhesive dropped from a margin trowel onto the still-wet Lucerna Anchor layer" width="1200" height="630"></div><figcaption><span class="no">02</span><b>Cement adhesive straight on top, while Anchor is still wet</b> — no drying time. Drop the mortar on with a margin trowel, spread it over the tile as usual and lift the tile onto the wall. The mortar keys into the wet Anchor and the two cure together.</figcaption></figure>
    </div>
    <p class="pricenote">Why wet on wet: let Anchor dry first and its surface skins into a smooth film the mortar can only sit on. Applied while wet, the mortar keys into the Anchor and the Anchor keys into the tile — tile → Anchor → mortar → wall becomes one layer with no interface left to let go · If the wall is smooth as well (tile over tile, waterproofed wall), coat the wall with Anchor too.</p>
  </div>
</section>

<section class="story" id="slabs">
  <div class="wrap">
    <div class="rdtag">LARGE FORMAT — the job Anchor exists for</div>
    <h2>Thousands of baht a slab, lifted by vacuum, set once —<br><b>this job gives you no second chance</b></h2>
    <figure class="packshot" style="max-width:960px;margin:18px 0 22px">
      <img loading="lazy" decoding="async" src="/img/anchor-lobby.webp" alt="Two tilers lift a 120×240 sintered stone slab with a vacuum lifter onto a lobby wall; slabs with teal Anchor-coated backs wait on an A-frame cart beside them" width="1024" height="559">
      <figcaption>A building lobby mid-installation of 120×240 sintered stone — slabs on the A-frame cart already skimmed with Anchor on the back, lifted by vacuum cups onto the wall combed with cement adhesive, orange spacers setting the thin joints</figcaption>
    </figure>
    <div class="story-grid">
      <div class="bignum">2.88<small>M² PER 120 × 240 SLAB — ANCHOR ≈ 750 THB</small></div>
      <div class="story-body">
        <p>Sintered stone and 120×240 porcelain slabs are what condominiums, hotels and shopfronts specify for the near-seamless look — but what makes them beautiful is what makes them let go: <b>a back fired so dense and smooth that water absorption is close to zero</b>. Cement adhesive, which holds by soaking into a surface, can only sit against it. As the slab expands in sun or heat, mortar and slab part a little at a time until the wall sounds hollow.</p>
        <div class="beats">
          <div class="beat"><div class="k">Why this job needs it</div><p>One slab weighs tens of kilos, costs thousands to tens of thousands of baht, is lifted by vacuum, set and grouted. If it sounds hollow a year later the only fix is rip-out, a new slab, re-laying and a conversation with the project owner — Anchor at about 750 THB per slab is small change against that.</p></div>
          <div class="beat"><div class="k">Fits the existing workflow</div><p>Skim Anchor on the back while the slab leans on the A-frame cart, put the cement adhesive straight on, lift and set as normal. Same adhesive, same tools; a two-hour open time lets you skim several slabs ahead.</p></div>
          <div class="beat"><div class="k">Moves with the slab</div><p>A 240 cm slab expands several times more than a small tile. The Anchor layer is flexible — bends 360° without cracking — so it follows the slab's movement instead of separating from it. Exterior walls in half-day sun are where the difference shows most.</p></div>
          <div class="beat"><div class="k">Walls cement adhesive doesn't like</div><p>Lobbies already waterproofed, gypsum or fibre-cement walls, the old tiled walls of a renovation — comb Anchor over the wall in addition to the tile back, then tile as normal, and the wall becomes one cement adhesive can hold.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">See it first — <em>clip and photos</em></h2>
    <p class="sec-sub">A tile staircase held together by nothing but this adhesive, the mixed material itself, and coating the wall side</p>
    <div class="vidgrid vert solo">
      <figure style="margin:0">
        <div class="fbv v916"><iframe loading="lazy" src="https://www.youtube.com/embed/''' + YT + r'''" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="Lucerna Anchor — a tile staircase held by this adhesive, taking a person's weight"></iframe></div>
        <figcaption><b>A staircase held by this adhesive</b> — 1 cm tile edges bonded to the glossy face of a large slab, built into steps and walked up. A strength demonstration, not a recommended way to build anything.</figcaption>
      </figure>
    </div>
    <div class="ggrid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:18px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g01.webp" alt="Lucerna Anchor on a trowel — a thick green cream with fine sand that holds its shape" width="720" height="720"></div><figcaption><span class="no">01</span>The mixed adhesive — a thick cream with fine sand, holds on the trowel without sagging</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g02.webp" alt="Lucerna Anchor combed onto the back of a tile with a notched trowel in even ridges" width="720" height="720"></div><figcaption><span class="no">02</span>Combed onto the back of the tile — a thin, even layer is all it takes</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/anchor-g03.webp" alt="Lucerna Anchor combed onto a wall next to existing tiles, before tiles spread with cement adhesive are pressed on" width="720" height="720"></div><figcaption><span class="no">03</span>Smooth wall (tile over tile, waterproofed wall) — Anchor combed onto the wall as well as the tile back</figcaption></figure>
    </div>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">Which jobs <em>is it for</em></h2>
    <p class="sec-sub">Any job where the back of the tile or the wall is "too smooth" for cement adhesive</p>
    <div class="pts">
      <div class="pt"><span class="ic">🧱</span><div><h4>Large-format tiles · sintered stone on walls</h4><p>60×120 up to 120×240 slabs that are heavy and dense on the back — a skim of Anchor lets the cement adhesive hold the whole face, cutting hollow spots and the delamination that shows up years later. Used together with a large-format cement adhesive as normal.</p></div></div>
      <div class="pt"><span class="ic">🔁</span><div><h4>Tile over tile, no demolition</h4><p>A bathroom or kitchen that needs a new face without the noise and rubble — skim Anchor on the new tile and bed it with cement adhesive onto the old, well-cleaned tiles. The glossy old surface stops being a problem.</p></div></div>
      <div class="pt"><span class="ic">🪟</span><div><h4>Difficult substrates — glass, metal, fibre cement, waterproofed walls</h4><p>Walls already coated with waterproofing, fibre-cement board, OSB, steel plate, glass — the surfaces most tilers have to work around with mesh or several primer coats — on walls like these, comb Anchor over the wall as well as skimming the tile back. Two smooth sides, two coats.</p></div></div>
      <div class="pt"><span class="ic">🪝</span><div><h4>Small fixtures on tile without drilling</h4><p>Hooks, handles, signs, light shelves on glossy tile where drilling risks a crack — coat the full contact face and press on. <b>Anything that genuinely carries load still needs anchors or screws</b>; read the limit below before you use it this way.</p></div></div>
    </div>
    <div class="warn"><b>⚠ Do not use it to hold heavy things:</b> shelves that will carry weight, grab rails people pull on, anything hanging above heads or beds must be fixed with wall anchors or screws — adhesive is a helper, not the primary load path. Until this page shows a load figure we have measured ourselves, treat it as not load-bearing. If you are not sure, message us with a photo of the job.</div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">Technical specification <em>test figures</em></h2>
    <p class="sec-sub">Typical values for the adhesive and the cured film</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>Item</th><th>Value</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Type</td><td>Two-part reaction-resin tile adhesive</td><td>JC/T 547-2017 Type R</td></tr>
          <tr><td>Part A</td><td>Silane-modified resin prepolymer (white paste)</td><td></td></tr>
          <tr><td>Part B</td><td>Amine-type curing prepolymer (blue paste)</td><td>Mixes to a uniform green</td></tr>
          <tr><td>Mixing ratio</td><td>A : B = 1 : 1 by weight</td><td>Weigh it</td></tr>
          <tr><td>Applied thickness</td><td>1 mm on the back of the tile</td><td>Then bed in cement adhesive as usual</td></tr>
          <tr><td>Coverage</td><td>20 kg set ≈ 25–30 m²</td><td>1 kg ≈ 1.2 m²</td></tr>
          <tr><td>Open time</td><td>120–150 minutes</td><td>At 23°C — shorter in heat</td></tr>
          <tr><td>Temperature resistance</td><td>Boiling at 100°C / freezing at −30°C without release</td><td>Boiling-water and freeze–thaw tests</td></tr>
          <tr><td>Flexibility</td><td>1 mm film bends 360° without cracking</td><td></td></tr>
          <tr><td>Chemical resistance</td><td>Water, alkali, heat and ageing resistant</td><td></td></tr>
          <tr><td>Formaldehyde / VOC</td><td>None detected / zero</td><td></td></tr>
          <tr><td>Packaging</td><td>1 kg (A 500 g + B 500 g) · 5 kg · 20 kg set</td><td></td></tr>
          <tr><td>Shelf life</td><td>12 months unopened</td><td>Keep sealed, out of the sun</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">Sizes and prices</h2>
    <p class="sec-sub">A + B come pre-weighed 1:1 — enter your area and the calculator picks the cheapest combination</p>
    <div class="pricecard">
      <table data-calc="1" data-shipping="70">
        <thead><tr><th>Size</th><th>Approx. coverage</th><th>Price</th><th>Shipping</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="1.25" data-ship="70">1 kg<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 500 g + B 500 g</small></td><td>≈ 1.2 m² · loose-tile repairs, small fixtures</td><td class="pr" data-price="590">590.-</td><td class="pr">70.-</td></tr>
          <tr><td class="sz" data-sqm="6.25" data-ship="130">5 kg<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 2.5 kg + B 2.5 kg</small></td><td>≈ 6 m² · one bathroom</td><td class="pr" data-price="1990">1,990.-</td><td class="pr">130.-</td></tr>
          <tr data-calc="skip"><td class="sz">20 kg set<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">A 10 kg + B 10 kg</small></td><td>≈ 25 m² · contractor jobs</td><td class="pr">6,500.-</td><td class="pr">Actual cost — ask</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">Prices include VAT · Coverage is based on a 1 mm skim on the tile back (20 kg ≈ 25–30 m²; we quote the low end) · Deeply ribbed tile backs use more · <b>Volume pricing for contractors</b> — send tile size and area on chat and we work out the quantity for you before you order</p>
  </div>
</section>

<section class="buybox" id="cost">
  <div class="wrap">
    <h2 class="sec-h">The money first — <em>what this adds to the job</em></h2>
    <p class="sec-sub">For tilers pricing a quote — figures based on a 1 mm skim at 1.2 m²/kg (low end), prices incl. VAT, shipping not included</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>Job</th><th>Area</th><th>Anchor needed</th><th>Cost</th><th>Per m²</th></tr></thead>
        <tbody>
          <tr><td>Loose-tile repair / small fixtures</td><td>up to 1 m²</td><td>1 kg</td><td><b>590</b></td><td>—</td></tr>
          <tr><td>One bathroom (walls)</td><td>≈ 6 m²</td><td>5 kg</td><td><b>1,990</b></td><td>≈ 330</td></tr>
          <tr><td>Kitchen + bathroom walls</td><td>≈ 12 m²</td><td>5 kg × 2</td><td><b>3,980</b></td><td>≈ 330</td></tr>
          <tr><td>Lobby / shopfront in large slabs</td><td>≈ 25 m²</td><td>20 kg set</td><td><b>6,500</b></td><td>≈ 260</td></tr>
          <tr><td>Building / project</td><td>≈ 50 m²</td><td>20 kg set × 2</td><td><b>13,000</b></td><td>≈ 260</td></tr>
        </tbody>
      </table>
    </div>
    <div class="speccard" style="margin-top:14px">
      <table>
        <thead><tr><th>Per tile (at 20 kg set pricing)</th><th>Tile area</th><th>Anchor per tile</th><th>Cost per tile</th></tr></thead>
        <tbody>
          <tr><td>60 × 120 cm tile</td><td>0.72 m²</td><td>≈ 0.6 kg</td><td><b>≈ 190 THB</b></td></tr>
          <tr><td>80 × 160 cm tile</td><td>1.28 m²</td><td>≈ 1.0 kg</td><td><b>≈ 330 THB</b></td></tr>
          <tr><td>120 × 240 cm sintered stone</td><td>2.88 m²</td><td>≈ 2.3 kg</td><td><b>≈ 750 THB</b></td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">Under 200 THB added per 60×120 tile, about 750 per 120×240 slab — set against the cost of the slab, the labour to lay it, and the rip-out if it lets go, this is the cheapest insurance on the job · Deeply ribbed or textured backs use more; allow 10–20% extra · Combing onto the wall uses more than skimming the tile back, depending on notch depth — send the job size on chat and we work out the quantity</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">How to use — <em>all on this page</em></h2>
    <p class="sec-sub">The only step added to a normal tiling job is a thin Anchor layer on the back of the tile — the rest is cement adhesive and a notched trowel as always</p>
    <div class="warn" style="margin:0 0 22px;border-color:var(--orange);background:rgba(237,106,47,.08);color:var(--ink)"><b>One rule — Anchor goes on the smooth side:</b> cement adhesive only grips absorbent surfaces. Large tiles that fail mostly fail at the tile back (the adhesive is still on the wall in neat ridges, the tile back comes off clean), so <b>always skim the tile back</b> · If the wall is smooth too — tile over tile, waterproofed walls, glass, metal, fibre-cement board — <b>coat both sides</b>, tile back and wall · A rendered wall must be sound, dust-free and free of laitance; a tile that comes off with a skin of render attached is a failed wall, not a failed adhesive</div>
    <ol class="flow">
      <li class="fstep"><h4>Prepare — sound, dry wall; clean tile back</h4><p>The wall must be solid with no dust or flaking paint. Old tiles being tiled over get washed free of soap film and grease; tap for hollow ones and fix them first. Wipe factory dust and powder off the back of every new tile with a damp cloth — for maximum durability, wash the backs and dry them before skimming.</p><span class="fchip">Clean, dry tile back</span></li>
      <li class="fstep"><h4>Mix A : B = 1 : 1 by weight to a single green</h4><p>Put equal weights of A and B in one bucket and stir with a trowel or a slow mixer until <b>no white or blue streaks remain</b>, scraping the bottom and sides. One uniform green means it is mixed. Our 1 kg set is pre-weighed — just pour both tubs together. Mix only what you can lay in about an hour.</p><span class="fchip">1:1 by weight</span><span class="fchip">One colour, no streaks</span></li>
      <li class="fstep"><h4>Skim 1 mm of Anchor on the tile back — and on the wall too if the wall is smooth</h4><p>With a flat or fine-notched trowel, spread it over the entire back out to the edges, about 1 mm thick; skim several tiles and lean them ready to lay within the open time · <b>If the wall is smooth</b> (tile over tile, waterproofed walls, glass, metal, fibre cement) also comb Anchor over the wall in sections, as in photo 03 — only as much as you can tile within the open time; the wall side uses more than the tile back depending on notch depth · Thicker is waste, not strength.</p><span class="fchip">Tile back, always</span><span class="fchip">Smooth wall = both sides</span></li>
      <li class="fstep"><h4>Cement adhesive on top, then press the tile to the wall while Anchor is wet</h4><p>Comb a large-format cement adhesive onto the wall with a notched trowel as normal (or drop it onto the skimmed tile back and spread it), then lift the tile and press it to the wall · No need to let Anchor dry — the cement adhesive goes straight on top, but join them <b>before the Anchor layer skins over</b> (within 120–150 minutes at 23°C — in direct sun or serious heat allow much less). Press and tap out air as with any tiling; adjust within the cement adhesive's own open time.</p><span class="fchip">wet-on-wet</span><span class="fchip">Within open time</span></li>
      <li class="fstep"><h4>Let it cure on the cement adhesive's schedule, then grout as usual</h4><p>Grouting and walk-on times follow the cement adhesive you used — the Anchor layer cures along with it, nothing extra to do. Wipe adhesive off the tile face immediately while wet; once hard it has to be scraped. · <b>Bonding small fixtures directly:</b> coat the full contact face on both parts, press together, support in place and leave overnight before hanging anything on it.</p></li>
    </ol>

    <div class="warn"><b>⚠ Safety:</b> a two-part resin adhesive. Part B contains an amine curing agent that irritates skin and can sensitise with repeated contact — nitrile gloves and eye protection every time, work in ventilated space. Wipe skin contact off and wash with soap and water at once (never thinner). Eyes: flush with water for several minutes and see a doctor. Let leftover mixed adhesive harden in the bucket before disposal. Keep tubs sealed, away from children and direct sun.</div>
  </div>
</section>

<section class="story" id="straight">
  <div class="wrap">
    <div class="rdtag">STRAIGHT TALK — what has to be said</div>
    <h2>Before you pay, read these 5 —<br><b>this is not magic</b>, and we don't want you misled</h2>
    <div class="story-grid">
      <div class="bignum">5<small>things most sellers don't say</small></div>
      <div class="story-body">
        <div class="beats">
          <div class="beat"><div class="k">1 · It does not replace cement adhesive</div><p>This is a <b>back-of-tile layer</b>; you still bed the tile in a full bed of cement adhesive. Skimming it on instead of cement costs a fortune and does nothing for levelling — a full resin bed is a different job. Message us first.</p></div>
          <div class="beat"><div class="k">2 · Heat eats half the working time</div><p>The 120–150 minutes are measured at 23°C. On a Thai site at 35°C, count on about an hour. Mix small amounts and finish each batch; never mix the whole bucket in the morning to use all day.</p></div>
          <div class="beat"><div class="k">3 · Dirty surfaces and weak walls are the number-one cause of failure</div><p>Adhesive bonds to whatever is on the surface. Cement dust, grease, factory powder on the tile back — it grips the dirt perfectly and the dirt lets go of the tile. It looks like the adhesive failed when it held fine. Wipe every tile back before skimming · And Anchor does not fix a weak wall — if the render is crumbly, dusty or has laitance, the tile comes off with a skin of render attached. The wall must be sound first.</p></div>
          <div class="beat"><div class="k">4 · Part B doesn't like air — open it, use it</div><p>The amine curing agent slowly changes with air and humidity. A tub opened, closed badly and left for a month may cure slowly or not at all. Buy the size you will finish in one job — that is why we pack a 1 kg set.</p></div>
          <div class="beat"><div class="k">5 · Not a grout, not a gap filler</div><p>It is a thin bonding layer, not a void filler or a joint waterproofer. Joints get grout, moving joints get sealant, wet areas get waterproofing first and tiles on top — Anchor bonds to a waterproofed wall well, but it doesn't do that wall's job.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">Is this <em>the right product for your job?</em></h2>
    <p class="sec-sub">If the problem isn't tile-to-wall, one of these may fit better</p>
    <div class="altgrid">
      <a class="altcard" href="/en/carbontilegrout">
        <div class="k">Grout joints · pools · bathrooms</div>
        <h4>Carbon Tile Grout</h4>
        <p>Once the tiles are down, the joints are the next battle — a two-part grout for permanently wet places that doesn't blacken or crumble.</p>
        <div class="go">View details →</div>
      </a>
      <a class="altcard" href="/en/flexgrip">
        <div class="k">Repairs · bonding mixed materials</div>
        <h4>FlexGrip</h4>
        <p>Small jobs around the house that want a one-bottle glue with no mixing — flexible, bonds almost any material.</p>
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
      <div class="sub">Tell us the tile size, the area and the wall you are tiling and we work out the quantity for you, free, before you order · <b>Volume pricing for contractors and tile shops</b></div>
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
