#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_purebreeze_page.py — สร้าง /purebreeze และ /en/purebreeze

PureBreeze — น้ำยาเคลือบใสระดับนาโนสำหรับแผงฟินคอยล์เย็นและคอยล์ร้อนของเครื่องปรับอากาศ ป้องกันฝุ่นเกาะสะสม
ย้ายมาจากหน้า Wix เดิม (lekvtwin.wixsite.com/lucerna/purebreeze) — Pist 25 ก.ย. 2026 "ไปเอาข้อมูลมาลงก่อน สร้างหน้าใหม่เลย"
อัตราใช้จริง (Pist พ่นจริง 25 ก.ย. 2026): ~20 ml ต่อแอร์บ้าน 1 ตัว → 100 g ≈ 5 ตัว · เนื้อหาหลักการ/ยับยั้งเชื้อ ≥99%/ทดสอบฝุ่น จาก feibotech.com/en/airconditioner (ระบุเป็นข้อมูลผู้ผลิต) · Pist 25 ก.ย. 2026 "เอาตามของเขาเลย" + "≥99% (ตามผู้ผลิต) เสล่อ จะเขียนทำไม" → ตัดคำกันตัว "ตามผู้ผลิต/ไม่ได้ทดสอบเอง" ออกทั้งหน้า พูดตัวเลขตรงๆ → ขั้นตอนใช้ตาม Feibo (ล้างลึก → แห้ง → พ่น → เซ็ตตัวที่อุณหภูมิห้อง ไม่มีตัวเลขเวลา/ระยะพ่นที่เราแต่งเอง) · ตารางแบคทีเรีย 1 สัปดาห์–1 ปี และรูปทดสอบ (crop จากสไลด์ของ Feibo ตัดตัวหนังสือจีนออก: img/purebreeze-dust1/3, -petri-coated/-bare) จากหน้าเดียวกัน
ราคาตามหน้า Wix: น้ำยา 100 g 690 / 8 ตร.ม., 500 g 2,990 / 40, 1 kg 5,500 / 80 ส่ง 40 · (สเปรย์ 100 ml 790 เลิกขาย — Pist 25 ก.ย. 2026 "จะไม่มีสเปรย์อีกแล้ว จะเป็นแบบไปบรรจุเครื่องพ่นเอง พ่นด้วยแรงต่ำ"; คลิปทดสอบ XZUhhF2gLpY เป็นของ solar เอาออก)
TDS (Feibo KT01/FBq301, จีน — Pist ส่ง 26 ก.ย. 2026) → ตารางสเปค #spec + files/purebreeze-tds.pdf (tools/mk_purebreeze_tds.py, EN+TH) · MSDS SNTEK202401061-3 (ม.ค. 2024, KT01) = files/purebreeze-sds.pdf ตามต้นฉบับ · เวลาแห้งในขั้นตอนใช้งานเป็นค่า TDS (แห้งสัมผัส 5 นาที / แข็งตัว ~1 ชม. / เซ็ตตัวเต็ม 6–20 ชม.) · ข้อขัดกัน: TDS 30–50 ml/m² แต่ตารางราคาระบุ 8 ตร.ม./100 g (จาก Wix) — รอ Pist ตัดสิน
hero/การ์ด = ภาพห้องนั่งเล่นที่ Pist generate เอง (Gemini, 25 ก.ย. 2026) img/purebreeze-hero-sq.webp / -card.webp
รายงานจุลชีพ Gmicro 2020SPS942R01D (E. coli / S. aureus >99%, รา ระดับ 0) — Pist ส่งสไลด์ 25 ก.ย. 2026, crop 3 หน้า upscale 2× = img/purebreeze-report-p1..p3.webp (+ -zoom-* ยังไม่ใช้) section #certs ก่อนราคา
วิดีโอจาก Wix: วิธีใช้ rAH-kRWLcZg · คลิปแนวตั้งของ Pist (Pure_breeze2.mov, 25 ก.ย. 2026 — พ่นคอยล์ร้อนด้วยกาพ่น + ฟินครึ่งเคลือบ) = YouTube Shorts d4kNlcm259c (Pist: ใช้ลิงก์แทนไฟล์ในเว็บ จะได้ไม่หนัก — ไฟล์ mp4/poster ที่เคย encode ลบออกจาก repo แล้ว) · การทดสอบ XZUhhF2gLpY (YouTube) · Shopee: 392415703/28808079817
chrome ยกมาจาก paintcoating ผ่าน build_easyclean_page.chrome()
วิธีใช้: python3 tools/build_purebreeze_page.py แล้วรัน tools/build_calculator_page.py (ตารางน้ำยามี data-calc)
"""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_easyclean_page import chrome, EXTRA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def build(lang):
    src = 'paintcoating/index.html' if lang == 'th' else 'en/paintcoating/index.html'
    head, drawer, tail = chrome(src)
    head = head.replace('/paintcoating', '/purebreeze')
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE[lang], head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % DESC[lang], head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % OGT[lang], head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % OGD[lang], head)
    head = head.replace('img/paintcoating-hero-sq.webp', 'img/purebreeze-hero-sq.webp')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', SCHEMA[lang], head, flags=re.S)
    head = head + EXTRA_CSS.replace('id="easyclean-css"', 'id="purebreeze-css"') + '''
<style id="purebreeze-deal-css">#certs .gph .im{aspect-ratio:auto;background:#fff}#certs .gph img{height:auto;object-fit:contain}#certs .gph:hover img{transform:none}.direct-deal{font-size:14.5px;color:var(--ink);border:1px solid rgba(237,106,47,.45);background:rgba(237,106,47,.08);border-radius:9px;padding:10px 14px;margin:14px 0 4px;line-height:1.55}</style>'''
    drawer = drawer.replace('/paintcoating', '/purebreeze')
    tail = tail.replace('/paintcoating', '/purebreeze')
    out = head + '</head>\n' + drawer + '\n\n' + BODY[lang] + '\n' + tail
    dst = 'purebreeze/index.html' if lang == 'th' else 'en/purebreeze/index.html'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    io.open(dst, 'w', encoding='utf-8').write(out)
    print('wrote', dst, len(out))


TITLE = {
    'th': 'PureBreeze น้ำยาเคลือบกันฝุ่นแผงคอยล์แอร์ — คอยล์เย็น คอยล์ร้อน ฝุ่นเกาะน้อยลง ล้างแอร์ห่างขึ้น | LucernaPro',
    'en': 'PureBreeze — Dust-Repellent Nano Coating for Air-Conditioner Coil Fins (Evaporator & Condenser) | LucernaPro',
}
DESC = {
    'th': 'PureBreeze น้ำยาเคลือบใสระดับนาโนสำหรับแผงฟินคอยล์เย็นและคอยล์ร้อนของเครื่องปรับอากาศ ฟิล์มบางใสทำให้ฝุ่นเกาะสะสมยากขึ้น ลมผ่านฟินได้เต็มที่ ยืดรอบล้างแอร์ให้ห่างขึ้น น้ำยาสำหรับบรรจุเครื่องพ่น พ่นแรงดันต่ำ สำหรับบ้าน ร้านล้างแอร์ โรงแรม ออฟฟิศ',
    'en': 'PureBreeze — a clear nano coating for the coil fins of air conditioners (evaporator and condenser). A thin clear film makes dust much harder to settle and build up, keeps air flowing through the fins and stretches the time between cleanings. A liquid for your own low-pressure sprayer — homes, A/C cleaning services, hotels and offices.',
}
OGT = {
    'th': 'PureBreeze น้ำยาเคลือบกันฝุ่นแผงคอยล์แอร์ — ล้างแอร์ห่างขึ้น',
    'en': 'PureBreeze — Dust-Repellent Nano Coating for A/C Coil Fins',
}
OGD = {
    'th': 'ฟิล์มใสบางบนฟินคอยล์เย็นและคอยล์ร้อน ฝุ่นเกาะสะสมยากขึ้น ลมผ่านเต็มที่ ยืดรอบล้างแอร์ — บรรจุเครื่องพ่นเอง 100 g ทำแอร์ได้ราว 5 ตัว',
    'en': 'A thin clear film on evaporator and condenser fins — dust struggles to build up, air flows freely, cleanings get further apart. Load your own sprayer; 100 g does about 5 units.',
}
SCHEMA = {
    'th': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"PureBreeze น้ำยาเคลือบกันฝุ่นแผงคอยล์แอร์","brand":{"@type":"Brand","name":"LucernaPro"},"description":"น้ำยาเคลือบใสระดับนาโนสำหรับแผงฟินคอยล์เย็นและคอยล์ร้อนของเครื่องปรับอากาศ ฟิล์มบางใสทำให้ฝุ่นเกาะสะสมยากขึ้น ยืดรอบล้างแอร์ให้ห่างขึ้น น้ำยาสำหรับบรรจุเครื่องพ่น พ่นแรงดันต่ำ","image":"https://www.lucernapro.com/img/purebreeze-hero-sq.webp","url":"https://www.lucernapro.com/purebreeze","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"690","highPrice":"5500","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
    'en': '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"Product","name":"PureBreeze — Dust-Repellent Nano Coating for A/C Coil Fins","brand":{"@type":"Brand","name":"LucernaPro"},"description":"Clear nano coating for evaporator and condenser coil fins of air conditioners. A thin clear film makes dust much harder to build up and stretches the time between cleanings. A liquid for your own low-pressure sprayer.","image":"https://www.lucernapro.com/img/purebreeze-hero-sq.webp","url":"https://www.lucernapro.com/en/purebreeze","offers":{"@type":"AggregateOffer","priceCurrency":"THB","lowPrice":"690","highPrice":"5500","offerCount":"3","availability":"https://schema.org/InStock"}}\n</script>',
}

BODY = {}

BODY['th'] = r'''<section class="phero">
  <div class="wrap phero-grid">
    <div>
      <div class="crumb"><span class="dot"></span>Protection <b>· เคลือบปกป้อง</b></div>
      <h1>Pure<span class="o">Breeze</span><br>น้ำยาเคลือบกันฝุ่นแผงคอยล์แอร์</h1>
      <p class="lede">แอร์ที่เพิ่งล้างเสร็จ ลมแรง เย็นเร็ว — แล้วอีกไม่กี่เดือนก็กลับมาอืดเพราะฝุ่นอุดฟินอีกรอบ PureBreeze คือฟิล์มใสบางระดับนาโนที่เคลือบลงบน<b>ฟินคอยล์เย็นและคอยล์ร้อน</b>หลังล้างเสร็จ ทำให้ฝุ่นเกาะสะสมยากขึ้นมาก ลมผ่านฟินได้เต็มที่นานกว่าเดิม รอบล้างแอร์จึงห่างออกไป — เป็นน้ำยาสำหรับ<b>บรรจุเครื่องพ่นเอง พ่นด้วยแรงดันต่ำ</b> ขวดเล็ก 100 g ทำแอร์บ้านได้ราว 5 ตัว (พ่นจริงใช้ราว 20 ml ต่อตัว)</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">สั่งซื้อ / ดูราคา</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>ปรึกษาหน้างานฟรี</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/purebreeze-hero-sq.webp" alt="ห้องนั่งเล่นที่ติดแอร์ผนัง — อากาศสะอาดคือสิ่งที่ PureBreeze ดูแลให้ที่ฟินแอร์" width="1200" height="1200">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">แอร์ที่เคลือบแล้ว <em>ต่างจากเดิมตรงไหน</em></h2>
    <p class="sec-sub">ฝุ่นในอากาศไม่ได้ลดลง แต่ผิวฟินที่มันจะเกาะเปลี่ยนไป — ฟิล์มใสสาย <b>Superhydrophilic</b> ทำให้น้ำที่กลั่นตัวบนคอยล์เย็นแผ่เป็นแผ่นบางแล้วพาฝุ่นไหลลงถาดน้ำทิ้ง แอร์จึงล้างฟินให้ตัวเองทุกครั้งที่ทำงาน</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>น้ำกลั่นตัวกลายเป็นน้ำล้างฟิน</h4><p>คอยล์เย็นมีน้ำกลั่นตัวบนฟินตลอดเวลาที่แอร์ทำงาน บนฟินเปล่าน้ำเกาะเป็นหยดแล้วหยดลง ฝุ่นอยู่ที่เดิม — ฟิล์ม PureBreeze ลดมุมสัมผัสน้ำบนโลหะลงจนน้ำ<b>แผ่เป็นแผ่นบางคลุมทั้งฟิน</b> แผ่นน้ำนั้นแทรกใต้ฝุ่นแล้วพาไหลลงถาดน้ำทิ้ง — คือ self-cleaning ระหว่างทำงาน ฝุ่นที่เหลือเกาะไม่แน่น ล้างครั้งถัดไปหลุดง่าย</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>ลมแรง เย็นเร็ว นานกว่าเดิม</h4><p>แอร์อืดหลังล้างไม่กี่เดือนเพราะฟินอุด ไม่ใช่เพราะน้ำยาแอร์หมด — เมื่อฟินโล่งนานขึ้น ลมผ่านคอยล์เย็นได้เต็มที่ คอมเพรสเซอร์ทำงานสั้นลงต่อรอบ อาการ "เปิด 25 แต่ไม่เย็น" มาช้ากว่าเดิมมาก</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>ล้างแอร์ห่างขึ้น ล้างง่ายขึ้น</h4><p>ฝุ่นที่เกาะน้อยและเกาะไม่แน่น ล้างครั้งถัดไปแค่น้ำแรงดันเบาก็หลุด ไม่ต้องขัดฟินจนล้ม — บ้านที่เคยล้างทุก 3–4 เดือนยืดออกไปได้ ร้านล้างแอร์ใช้เป็นบริการเสริมที่ลูกค้าเห็นผลจริงในรอบถัดไป</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>ยับยั้งแบคทีเรียและราบนฟินมากกว่า 99%</h4><p>ฟินคือจุดที่เปียกชื้นตลอดเวลาและไม่มีใครถอดล้าง จึงเป็นที่เพาะเชื้อราและแบคทีเรียที่ปล่อยกลิ่นอับออกมากับลม — ฟิล์มมีชั้นนาโนยับยั้งเชื้อ อัตรายับยั้งแบคทีเรียมากกว่า 99% และยังเกิน 99% หลังใช้ครบ 1 ปี กลิ่นอับจึงลดลง ฟิล์มใสบางระดับนาโน ไม่ขวางการแลกเปลี่ยนความร้อน ไม่เปลี่ยนสีฟิน</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">ดูของจริงก่อน — <em>คลิปวิธีใช้และภาพทดสอบ</em></h2>
    <p class="sec-sub">คลิปพ่นคอยล์เย็นและคอยล์ร้อนจริง และภาพจากห้องทดสอบฝุ่นกับจานเพาะเชื้อ</p>
    <div class="ggrid" style="grid-template-columns:1fr;max-width:880px">
      <figure class="packshot" style="margin:0">
        <div class="fbv"><iframe loading="lazy" src="https://www.youtube.com/embed/rAH-kRWLcZg" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="วิธีใช้ PureBreeze บนแผงฟินแอร์"></iframe></div>
        <figcaption>วิธีใช้ — พ่นบนแผงฟินคอยล์เย็นหลังล้างและเป่าแห้งแล้ว</figcaption>
      </figure>
    </div>
    <div class="vidgrid vert solo" style="margin:18px 0 0">
      <figure style="margin:0">
        <div class="fbv v916"><iframe loading="lazy" src="https://www.youtube.com/embed/d4kNlcm259c" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="PureBreeze — พ่นคอยล์ร้อนด้วยกาพ่นสี และฟินที่เคลือบครึ่งเดียว"></iframe></div>
        <figcaption><b>พ่นคอยล์ร้อนด้วยกาพ่นสี</b> — บรรจุน้ำยาลงกาพ่น พ่นเป็นละอองบางทั่วแผงฟินคอนเดนซิ่ง แล้วดูฟินที่เคลือบครึ่งเดียวหลังใช้งานกลางแจ้ง ครึ่งไม่เคลือบฝุ่นเกาะหนา ครึ่งเคลือบยังโล่ง</figcaption>
      </figure>
    </div>
    <div class="ggrid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin-top:18px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-dust1.webp" alt="คอยล์เย็นในห้องทดสอบฝุ่น — ครึ่งบนเคลือบยังโล่ง ครึ่งล่างไม่เคลือบมีฝุ่นเกาะหนา" width="407" height="444"></div><figcaption><span class="no">01</span>ห้องทดสอบฝุ่น — ครึ่งบนเคลือบ ครึ่งล่างไม่เคลือบ</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-dust3.webp" alt="แผงฟินในห้องทดสอบฝุ่น — ฝั่งซ้ายไม่เคลือบเป็นสีน้ำตาลจากฝุ่น ฝั่งขวาเคลือบยังเป็นสีโลหะ" width="422" height="480"></div><figcaption><span class="no">02</span>แผงฟินเดียวกัน — ซ้ายไม่เคลือบ ขวาเคลือบ</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-petri-coated.webp" alt="จานเพาะเชื้อจากฟอยล์อะลูมิเนียมที่เคลือบ มีโคโลนีเล็ก" width="462" height="464"></div><figcaption><span class="no">03</span>เพาะเชื้อจากฟอยล์ที่เคลือบ</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-petri-bare.webp" alt="จานเพาะเชื้อจากฟอยล์อะลูมิเนียมที่ไม่เคลือบ มีเชื้อราขึ้นเป็นกลุ่ม" width="469" height="464"></div><figcaption><span class="no">04</span>เพาะเชื้อจากฟอยล์ที่ไม่เคลือบ</figcaption></figure>
    </div>
    <p class="pricenote">การทดสอบเร่งสภาพในห้องฝุ่น และการเพาะเชื้อจากฟอยล์อะลูมิเนียมที่เคลือบกับไม่เคลือบ</p>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">ใช้กับ<em>อะไรได้บ้าง</em></h2>
    <p class="sec-sub">ฟินอะลูมิเนียมของคอยล์ทุกชนิดที่ล้างสะอาดและเป่าแห้งแล้ว — แอร์บ้าน แอร์ฝังฝ้า แอร์ตู้ตั้ง คอนเดนซิ่งยูนิตนอกบ้าน</p>
    <div class="pts">
      <div class="pt"><span class="ic">❄️</span><div><h4>คอยล์เย็น (ในห้อง)</h4><p>ฟินหลังหน้ากากแอร์ที่ฝุ่นในห้องมาเกาะทุกวัน — จุดที่กำหนดว่าลมจะแรงหรืออืด เคลือบหลังล้างเสร็จรอบใหญ่ แล้วรอบถัดไปจะเห็นเองว่าฟินยังโล่ง</p></div></div>
      <div class="pt"><span class="ic">🌡️</span><div><h4>คอยล์ร้อน (คอนเดนซิ่งนอกบ้าน)</h4><p>ฟินนอกบ้านที่โดนฝุ่นถนน ใบไม้ และละอองฝนจนตัน ระบายความร้อนไม่ทัน กินไฟและคอมเพรสเซอร์ร้อน — เคลือบให้ฝุ่นหลุดตามลมและฝน ฉีดน้ำล้างครั้งถัดไปหลุดง่าย</p></div></div>
      <div class="pt"><span class="ic">🧰</span><div><h4>ร้านล้างแอร์ · ช่างแอร์</h4><p>ใส่เครื่องพ่นของร้านเป็นบริการเสริมต่อจากการล้าง — ลูกค้าจ่ายเพิ่มครั้งเดียวแล้วเห็นผลในรอบล้างถัดไป เป็นเหตุผลให้กลับมาใช้ร้านเดิม 1 กก. ทำแอร์ได้ราว 80 ตร.ม. ของพื้นที่ฟิน</p></div></div>
      <div class="pt"><span class="ic">🏨</span><div><h4>โรงแรม · ออฟฟิศ · ร้านอาหาร</h4><p>แอร์หลายสิบตัวที่ต้องจ้างล้างตามรอบ — เคลือบทั้งอาคารรอบเดียวแล้วยืดรอบล้างออกไป ค่าล้างที่ประหยัดได้ต่อปีมากกว่าค่าน้ำยา สั่งจำนวนมากมีราคาโครงการ</p></div></div>
    </div>
  </div>
</section>

<section class="story">
  <div class="wrap">
    <div class="rdtag">SOURCE — วัตถุดิบมาจากไหน</div>
    <h2>เราเลือกนำเข้าวัตถุดิบหลัก<br>จากผู้พัฒนาเทคโนโลยีนี้<b>โดยตรง — Feibo</b></h2>
    <div class="story-grid">
      <div class="bignum">≥99%<small>ANTIBACTERIAL RATE · 1 YEAR IN USE</small></div>
      <div class="story-body">
        <p>ตัวนี้เรา<b>นำเข้าวัตถุดิบหลักจาก Feibo</b> (ฉางชา ประเทศจีน) ผู้พัฒนาวัตถุดิบเดียวกับ <a href="/glasscoating" style="color:var(--orange)">Glass Coating</a> และ <a href="/solarpaneldefender" style="color:var(--orange)">Solar Panel Defender</a> ของเรา — เป็นสูตรที่เขาพัฒนาสำหรับฟินและชิ้นส่วนโลหะภายในเครื่องปรับอากาศโดยเฉพาะ ใช้ในอาคารสาธารณะและอาคารพาณิชย์ในจีน แล้วเรามาบรรจุและควบคุมคุณภาพต่อในประเทศไทย</p>
        <p>เหตุผลที่แอร์ควรได้ฟิล์มนี้: การล้างแอร์ทั่วไปเน้นแผ่นกรอง แต่ฟินที่ถอดไม่ได้คือที่ที่สิ่งสกปรกซ่อนอยู่มากที่สุด — จากการสุ่มตรวจ ตัวอย่างฟินกว่า 80% พบแบคทีเรียหรือราสูงกว่าเกณฑ์</p>
        <div class="beats">
          <div class="beat"><div class="k">หลักการ</div><p>ฟิล์มบางใสจากซิลิกอนออกไซด์อนินทรีย์ + สารยับยั้งเชื้อ + พอลิเมอร์อินทรีย์ — ทำผิวฟินเป็น <b>Superhydrophilic</b> น้ำกลั่นตัวแผ่เป็นแผ่นพาฝุ่นและคราบไหลออก และเป็นชั้นกันคราบน้ำมันกับคราบอินทรีย์เกาะฟิน</p></div>
          <div class="beat"><div class="k">ยับยั้งเชื้อ</div><p>ชั้นนาโนบนฟินยับยั้งแบคทีเรีย รา และเชื้อก่อโรคทั่วไป อัตราการยับยั้งแบคทีเรียมากกว่า 99% ลดเชื้อที่ฟุ้งไปกับลมและลดกลิ่นอับ</p></div>
          <div class="beat"><div class="k">ผลทดสอบฝุ่น</div><p>ในการทดสอบเร่งสภาพในห้องฝุ่น พื้นที่ที่เคลือบมีฝุ่นเกาะน้อยกว่าพื้นที่ไม่เคลือบอย่างเห็นได้ชัด ประสิทธิภาพเครื่องจึงตกช้าลงและล้างห่างขึ้น</p></div>
          <div class="beat"><div class="k">ไม่รบกวนเครื่อง</div><p>ฟิล์มบางระดับนาโนและใส ไม่มีผลต่อการถ่ายเทความร้อนและการทำงานของเครื่อง — ขั้นตอนใช้งาน: ล้างลึก → แห้งสนิท → พ่นบางสม่ำเสมอ → ปล่อยให้เซ็ตตัวที่อุณหภูมิห้อง ตรงกับที่เราเขียนไว้ด้านล่าง</p></div>
        </div>
        <div class="speccard" style="margin-top:14px">
          <table>
            <thead><tr><th>จำนวนแบคทีเรียบนฟิน (ต่อ mL)</th><th>ใช้ 1 สัปดาห์</th><th>1 เดือน</th><th>ครึ่งปี</th><th>1 ปี</th></tr></thead>
            <tbody>
              <tr><td>ก่อนล้าง</td><td>5.83 × 10⁶</td><td>1.19 × 10⁷</td><td>1.46 × 10⁷</td><td>2.06 × 10⁷</td></tr>
              <tr><td>30 นาทีหลังล้าง</td><td>381</td><td>1,560</td><td>3,578</td><td>9,360</td></tr>
              <tr><td>หลังพ่นเคลือบ — อัตรายับยั้ง</td><td>&gt; 99.91%</td><td>&gt; 99.85%</td><td>&gt; 99.52%</td><td>&gt; 99.13%</td></tr>
            </tbody>
          </table>
        </div>
        <p style="font-size:13px;color:var(--muted);margin-top:8px">ผลทดสอบในห้องแล็บบนฟินคอยล์เย็นแอร์ที่ไม่ล้างต่อเนื่อง — อัตรายับยั้งยังเกิน 99% หลังใช้ครบ 1 ปี</p>
      </div>
    </div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">สเปคทางเทคนิค <em>ตัวเลขจาก TDS</em></h2>
    <p class="sec-sub">ค่าทั่วไปของน้ำยาและฟิล์มหลังเซ็ตตัว — ฉบับเต็มดาวน์โหลดได้ด้านล่าง พร้อมเอกสารข้อมูลความปลอดภัย</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>รายการ</th><th>ค่า</th><th>วิธีทดสอบ / หมายเหตุ</th></tr></thead>
        <tbody>
          <tr><td>ชนิด</td><td>นาโนเคลือบส่วนผสมเดียว สูตรแอลกอฮอล์ผสมน้ำ พร้อมใช้</td><td>ห้ามเจือจาง</td></tr>
          <tr><td>ลักษณะ</td><td>ของเหลวกึ่งใส ฟ้าอ่อนถึงขาวอ่อน</td><td>กลิ่นเอทานอลเล็กน้อย</td></tr>
          <tr><td>เนื้อสาร (solids)</td><td>10 ± 2 % โดยน้ำหนัก</td><td>DIN EN ISO 3251</td></tr>
          <tr><td>ความหนาแน่น (20°C)</td><td>0.88–0.92 g/cm³</td><td>DIN EN ISO 2811-2</td></tr>
          <tr><td>pH</td><td>4.0–6.0</td><td>DIN ISO 976</td></tr>
          <tr><td>จุดวาบไฟ</td><td>26.5°C</td><td>ISO 13736 — ของเหลวไวไฟ</td></tr>
          <tr><td>มุมสัมผัสน้ำ (ฟิล์ม)</td><td>≤ 7°</td><td>Superhydrophilic — น้ำแผ่เป็นแผ่น</td></tr>
          <tr><td>ความต้านทานผิว</td><td>10⁹ Ω</td><td>กันไฟฟ้าสถิต ฝุ่นไม่ถูกดูดเกาะ</td></tr>
          <tr><td>ความแข็งดินสอ</td><td>6H</td><td></td></tr>
          <tr><td>การยึดเกาะ (cross-cut)</td><td>เกรด 0</td><td>GB/T 9286-1998, GB/T 31815-2015</td></tr>
          <tr><td>ทนกรด</td><td>ไม่พบรอยแตกหรือฟองพอง</td><td></td></tr>
          <tr><td>ยับยั้งแบคทีเรีย / รา</td><td>&gt; 99% · ระดับ 0</td><td>GB 21551.2-2010 — ดูรายงานด้านล่าง</td></tr>
          <tr><td>วิธีพ่น</td><td>HVLP หัว 1.0–1.2 มม. แรงดันลม ~0.2 MPa</td><td>หรือเครื่องพ่นละอองละเอียดแรงดันต่ำ</td></tr>
          <tr><td>อัตราการใช้</td><td>30–50 มล./ตร.ม.</td><td>แอร์บ้าน 1 ตัว ≈ 20 มล. จากการพ่นจริงของเรา</td></tr>
          <tr><td>แห้งสัมผัส / แข็งตัว</td><td>5 นาที / ~1 ชั่วโมง</td><td>เร่งด้วยความร้อน 50°C ≈ 2 นาที · 70°C ≈ 1 นาที</td></tr>
          <tr><td>เซ็ตตัวเต็มที่</td><td>6 ชม. (อากาศร้อน) – 20 ชม. (อากาศเย็น)</td><td>ห้ามให้ฟิล์มโดนน้ำก่อนแข็งตัว</td></tr>
          <tr><td>การเก็บ / อายุ</td><td>−10 ถึง 45°C · 12 เดือนไม่เปิด</td><td>เปิดแล้วใช้ให้หมดโดยเร็ว</td></tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:18px;display:flex;gap:10px;flex-wrap:wrap">
      <a class="btn btn-ghost" href="/files/purebreeze-tds.pdf" target="_blank" rel="noopener">📑 TDS ข้อมูลเทคนิค</a>
      <a class="btn btn-ghost" href="/files/purebreeze-sds.pdf" target="_blank" rel="noopener">📄 เอกสารข้อมูลความปลอดภัย (MSDS)</a>
    </div>
  </div>
</section>

<section class="gallery" id="certs">
  <div class="wrap">
    <h2 class="sec-h">รายงานทดสอบจุลชีพ <em>จากห้องแล็บที่ได้รับการรับรอง</em></h2>
    <p class="sec-sub">ตัวเลข "มากกว่า 99%" บนหน้านี้มาจากรายงานฉบับนี้ — Guangdong Detection Center of Microbiology (Gmicro Testing) กว่างโจว แล็บที่ได้รับการรับรอง CMA และ CNAS · รายงานเลขที่ 2020SPS942R01D · เอกสารต้นฉบับเป็นภาษาจีน-อังกฤษ คำอธิบายภาษาไทยอยู่ใต้แต่ละหน้า</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>รายการทดสอบ</th><th>วิธี</th><th>ผล</th></tr></thead>
        <tbody>
          <tr><td>ต้านแบคทีเรีย <i>Escherichia coli</i> (เชื้อในลำไส้)</td><td>GB 21551.2-2010 ภาคผนวก A · สัมผัส 24 ชม.</td><td><b>&gt; 99%</b> — จาก 2.4 × 10⁵ เหลือน้อยกว่า 20 cfu</td></tr>
          <tr><td>ต้านแบคทีเรีย <i>Staphylococcus aureus</i> (สแตฟ ทอง)</td><td>GB 21551.2-2010 ภาคผนวก A · สัมผัส 24 ชม.</td><td><b>&gt; 99%</b> — จาก 3.4 × 10⁵ เหลือน้อยกว่า 20 cfu</td></tr>
          <tr><td>ต้านเชื้อรา 5 สายพันธุ์มาตรฐาน (<i>Aspergillus niger</i>, <i>Penicillium funiculosum</i>, <i>Chaetomium globosum</i>, <i>Aureobasidium pullulans</i>, <i>Paecilomyces variotii</i>)</td><td>GB 21551.2-2010 ภาคผนวก C</td><td><b>ระดับ 0</b> — ดีที่สุด ไม่มีราขึ้นแม้ดูด้วยกล้องขยาย 50 เท่า</td></tr>
        </tbody>
      </table>
    </div>
    <div class="ggrid" style="margin-top:22px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-report-p1.webp" alt="หน้าปกรายงานวิเคราะห์ทดสอบ Guangdong Detection Center of Microbiology เลขที่ 2020SPS942R01D ตัวอย่าง Self-cleaning antibacterial coating" width="804" height="1364"></div><figcaption><span class="no">01</span><b>หน้าปกรายงาน</b> — ประเภท commissioned test ตัวอย่าง "Self-cleaning antibacterial coating" ผู้ส่งตรวจคือผู้พัฒนาวัตถุดิบของเรา</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-report-p2.webp" alt="หน้าผลทดสอบต้านแบคทีเรีย — E. coli และ Staphylococcus aureus อัตรายับยั้งมากกว่า 99%" width="808" height="1364"></div><figcaption><span class="no">02</span><b>ผลต้านแบคทีเรีย</b> — <i>E. coli</i> และ <i>S. aureus</i> ยับยั้งได้มากกว่า 99% หลังสัมผัส 24 ชั่วโมง เกณฑ์มาตรฐานอยู่ที่ 90%</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-report-p3.webp" alt="หน้าผลทดสอบต้านเชื้อรา — ระดับป้องกันรา 0" width="752" height="1364"></div><figcaption><span class="no">03</span><b>ผลต้านเชื้อรา</b> — ระดับ 0 กับเชื้อรามาตรฐาน 5 สายพันธุ์ คือระดับดีที่สุดของมาตรฐานนี้</figcaption></figure>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">ขนาดและราคา</h2>
    <p class="sec-sub">น้ำยาสำหรับ<b>บรรจุเครื่องพ่นเอง</b> — กรอกพื้นที่ฟินให้ระบบจัดชุดที่ถูกที่สุดให้ได้</p>
    <div class="pricecard">
      <table data-calc="1" data-shipping="40">
        <thead><tr><th>ขนาด</th><th>พื้นที่ฟินโดยประมาณ</th><th>ราคา</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="8">100 g</td><td>≈ 8 ตร.ม. · แอร์บ้านราว 5 ตัว</td><td class="pr" data-price="690">690.-</td></tr>
          <tr><td class="sz" data-sqm="40">500 g</td><td>≈ 40 ตร.ม. · ราว 25 ตัว</td><td class="pr" data-price="2990">2,990.-</td></tr>
          <tr><td class="sz" data-sqm="80">1 kg</td><td>≈ 80 ตร.ม. · ราว 50 ตัว</td><td class="pr" data-price="5500">5,500.-</td></tr>
          <tr data-calc="skip"><td class="sz">จำนวนมาก<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">โรงแรม / ออฟฟิศ / ร้านล้างแอร์</small></td><td>หลายเครื่องต่อรอบ</td><td class="pr">ราคาโครงการ — สอบถาม</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">ค่าจัดส่ง <b>40 บาท</b> · จากที่เราพ่นจริง แอร์บ้านหนึ่งตัวใช้น้ำยาราว <b>20 ml</b> เมื่อพ่นแรงดันต่ำเป็นละอองบาง — ขวด 100 g จึงทำได้ราว 5 ตัว 1 กก. ราว 50 ตัว ตัวเลขนี้เป็นงานพ่นมือ ถ้าพ่นหนาหรือแอร์ตัวใหญ่ใช้มากกว่านี้ · ไม่แน่ใจว่าต้องใช้เท่าไหร่ บอกจำนวนแอร์และขนาด BTU มาทางแชท เราคำนวณให้ฟรีก่อนสั่ง</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">วิธีใช้งาน — <em>จบบนหน้านี้</em></h2>
    <p class="sec-sub">หลักเดียวที่ตัดสินทั้งงาน: <b>เคลือบบนฟินที่ล้างสะอาดและแห้งสนิทเท่านั้น</b> — ฟิล์มเกาะสิ่งที่อยู่บนผิว ถ้าพ่นทับฝุ่นเดิม ก็ได้ฟิล์มที่เคลือบฝุ่นไว้กับฟิน</p>
    <ol class="flow">
      <li class="fstep"><h4>ปิดเครื่อง ตัดไฟ แล้วล้างแอร์ให้สะอาดตามปกติ</h4><p>ถอดหน้ากากและแผ่นกรอง ล้างฟินคอยล์เย็นด้วยน้ำยาล้างคอยล์และน้ำแรงดันเบาตามที่ช่างทำ ล้างคราบน้ำยาออกให้หมด — คราบน้ำยาล้างคอยล์ที่เหลืออยู่จะขวางฟิล์มเท่ากับฝุ่น คอยล์ร้อนนอกบ้านฉีดน้ำล้างจากด้านในออกด้านนอก</p></li>
      <li class="fstep"><h4>เป่าให้แห้งสนิท</h4><p>เป่าลมหรือปล่อยให้แห้งจนฟินไม่มีหยดน้ำค้างและไม่ชื้น — ตัวนี้เคลือบบนผิวแห้ง น้ำที่ค้างในร่องฟินจะเจือน้ำยาจนฟิล์มไม่ต่อกัน ถ้าเร่งเวลา ใช้เครื่องเป่าลมไล่จากบนลงล่าง</p><span class="fchip">แห้งสนิท ไม่มีหยดน้ำ</span></li>
      <li class="fstep"><h4>บรรจุเครื่องพ่น แล้วพ่นด้วยแรงดันต่ำเป็นละอองบางทั่วแผงฟิน</h4><p>เทน้ำยาลงเครื่องพ่นที่สะอาดและแห้ง — ดีที่สุดคือกาพ่นสี HVLP หัว 1.0–1.2 มม. แรงดันลมราว 0.2 MPa หรือเครื่องพ่นใดก็ได้ที่ให้ละอองละเอียด <b>ใช้แรงดันต่ำ</b> ให้ออกเป็นละอองละเอียด ไม่ใช่เป็นสาย — แรงดันสูงจะทำให้ฟินล้มและน้ำยาเด้งออก พ่นซ้ายไปขวาทีละแถวให้ผิวฟินเปียกบางสม่ำเสมอทั่วทั้งแผง ไม่พ่นจนไหลย้อย เนื้อยาที่ไหลรวมกันที่ด้านล่างคือของที่เสียเปล่า แอร์บ้านหนึ่งตัวใช้เวลาไม่ถึง 2 นาที ทำทั้งคอยล์เย็นและคอยล์ร้อน</p><span class="fchip">แรงดันต่ำ ละอองละเอียด</span><span class="fchip">ชั้นบางชั้นเดียว</span></li>
      <li class="fstep"><h4>ปล่อยให้แข็งตัวที่อุณหภูมิห้องราว 1 ชั่วโมง</h4><p>ผิวฟิล์มแห้งสัมผัสใน 5 นาที และแข็งตัวทั่วทั้งฟิล์มในราว 1 ชั่วโมงที่อุณหภูมิห้อง ไม่ต้องเป่า ไม่ต้องอบ ระหว่างนี้<b>ห้ามให้น้ำโดนฟิน</b> — น้ำบนฟิล์มที่ยังไม่แข็งจะทิ้งรอยคราบถาวร แล้วค่อยใส่แผ่นกรองและหน้ากากกลับ</p><span class="fchip">แห้งสัมผัส 5 นาที</span><span class="fchip">แข็งตัว ~1 ชม.</span></li>
      <li class="fstep"><h4>ครบ 1 ชั่วโมงแล้วเปิดใช้งานได้ตามปกติ</h4><p>เปิดแอร์ใช้งานได้หลังฟิล์มแข็งตัว (ฟิล์มเซ็ตตัวเต็มที่ใน 6 ชั่วโมงในอากาศร้อน ถึง 20 ชั่วโมงในอากาศเย็น แต่ไม่ต้องรอถึงตอนนั้น) ครั้งแรกอาจมีกลิ่นน้ำยาจางๆ ไม่กี่นาทีแล้วหาย — รอบล้างถัดไปให้ล้างด้วยน้ำเปล่าแรงดันเบาก่อน ถ้าฟินยังโล่งไม่ต้องใช้น้ำยาล้างคอยล์ ถ้าต้องใช้ให้เลือกสูตรกลางหรือกรดอ่อน — <b>น้ำยาล้างคอยล์ที่เป็นด่าง pH 11 ขึ้นไปทำลายฟิล์ม</b> และเคลือบซ้ำหลังการล้างใหญ่ทุกครั้ง</p></li>
    </ol>

    <div class="warn"><b>⚠ ความปลอดภัย:</b> เป็นของเหลวไวไฟ (จุดวาบไฟ 26.5°C) มีแอลกอฮอล์หลายชนิดรวมถึงเมทานอล — ปิดเครื่องและตัดไฟก่อนพ่นทุกครั้ง ห่างประกายไฟและบุหรี่ พ่นในที่อากาศถ่ายเท <b>สวมหน้ากากกรองไอสารอินทรีย์</b> แว่นครอบตา และถุงมือ เข้าตาให้ล้างน้ำต่อเนื่องหลายนาทีแล้วพบแพทย์ ไม่พ่นเข้าแผงวงจร มอเตอร์พัดลม และเซ็นเซอร์ เก็บขวดปิดสนิทพ้นมือเด็กและแสงแดดตรง รายละเอียดใน MSDS ด้านบน</div>
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
          <div class="beat"><div class="k">1 · ไม่ได้ทำให้ไม่ต้องล้างแอร์อีกเลย</div><p>มันทำให้<b>ฝุ่นเกาะน้อยลงและล้างออกง่ายขึ้น</b> รอบล้างจึงห่างออกไป — แต่แผ่นกรองยังต้องล้างตามปกติ และฟินยังต้องล้างเมื่อถึงรอบ ใครขายว่าเคลือบแล้วลืมแอร์ไปได้เลย ไม่จริง</p></div>
          <div class="beat"><div class="k">2 · ฟินที่ยังสกปรกหรือชื้น เคลือบไปก็เสียเปล่า</div><p>ฟิล์มเกาะสิ่งที่อยู่บนผิว พ่นทับฝุ่นก็ได้ฟิล์มที่ยึดฝุ่นไว้กับฟิน พ่นบนฟินเปียกน้ำยาก็เจือจนไม่ต่อกัน — ล้างสะอาดและเป่าแห้งก่อนคือ 80% ของงาน ไม่ใช่ตัวน้ำยา</p></div>
          <div class="beat"><div class="k">3 · แอร์ที่มีราดำหรือเมือกในถาดน้ำทิ้ง ต้องจัดการก่อน</div><p>ตัวนี้เป็นฟิล์มกันฝุ่นบนฟิน ไม่ใช่น้ำยาฆ่าเชื้อ — ราและเมือกในถาดน้ำทิ้ง ท่อน้ำทิ้ง และโบลเวอร์ต้องล้างออกก่อน ถ้ากลิ่นอับมาจากตรงนั้น เคลือบฟินไม่ช่วยเรื่องกลิ่น</p></div>
          <div class="beat"><div class="k">4 · ไม่แก้แอร์ที่ไม่เย็นเพราะสาเหตุอื่น</div><p>น้ำยาแอร์รั่ว คอมเพรสเซอร์อ่อน คาปาซิเตอร์เสื่อม พัดลมคอยล์ร้อนไม่หมุน — อาการเหมือน "ฟินตัน" แต่ต้องซ่อม ถ้าล้างแอร์แล้วยังไม่เย็น ให้ช่างเช็คระบบก่อน ไม่ต้องรีบซื้อตัวนี้</p></div>
          <div class="beat"><div class="k">5 · ต้องเคลือบซ้ำหลังการล้างใหญ่</div><p>การล้างด้วยน้ำยาล้างคอยล์และแรงดันน้ำสูงจะเอาฟิล์มออกไปด้วยส่วนหนึ่ง — ทุกครั้งที่ล้างใหญ่ ให้พ่นซ้ำหลังเป่าแห้ง คิดค่าน้ำยาต่อครั้งไว้ในต้นทุนการล้าง ไม่ใช่ทำครั้งเดียวตลอดอายุแอร์</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">งานของคุณ<em>ใช่ตัวนี้ไหม</em></h2>
    <p class="sec-sub">ถ้าโจทย์ไม่ใช่ฝุ่นบนฟินแอร์ สองตัวนี้อาจตรงกว่า</p>
    <div class="altgrid">
      <a class="altcard" href="/bioshield">
        <div class="k">ราดำ · ตะไคร่ · เมือก</div>
        <h4>BioShield</h4>
        <p>ถ้าปัญหาคือราดำ ตะไคร่ หรือกลิ่นอับ ไม่ใช่ฝุ่น — ล้างและยับยั้งการกลับมาของราด้วยตัวนี้ก่อน แล้วค่อยกันฝุ่น</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
      <a class="altcard" href="/easyclean">
        <div class="k">ผนัง · ประตู · เฟอร์นิเจอร์</div>
        <h4>EasyClean</h4>
        <p>สำหรับผิวสีทาผนังและโลหะที่โจทย์คือคราบน้ำมันและรอยเปื้อน ไม่ใช่ฟินแอร์ — เช็ดครั้งเดียวออก</p>
        <div class="go">ดูรายละเอียด →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">สั่งซื้อ <em>PureBreeze</em></h2>
    <div class="ordercard">
      <h3>สั่งตรงผ่านแชท</h3>
      <div class="sub">บอกจำนวนแอร์และขนาด BTU มาได้เลย ทีมงานคำนวณปริมาณให้ฟรีก่อนสั่ง · <b>โรงแรม ออฟฟิศ ร้านล้างแอร์ มีราคาโครงการ</b></div>
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
      <div class="crumb"><span class="dot"></span>Protection <b>· Protective Coatings</b></div>
      <h1>Pure<span class="o">Breeze</span><br>Dust-Repellent Coating for A/C Coil Fins</h1>
      <p class="lede">A freshly cleaned air conditioner blows hard and cools fast — and a few months later it is sluggish again because dust has choked the fins. PureBreeze is a thin, clear nano film applied to the <b>evaporator and condenser fins</b> right after cleaning. Dust finds it much harder to settle and build up, air keeps flowing through the fins for longer, and cleanings get further apart — a liquid you <b>load into your own sprayer and apply at low pressure</b>; the 100 g bottle does about 5 home units (about 20 ml each in our own application).</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">Order / Prices</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>Free advice on chat</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/purebreeze-hero-sq.webp" alt="Living room with a wall-mounted air conditioner — clean air is what PureBreeze protects at the fins" width="1200" height="1200">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">What changes <em>once the fins are coated</em></h2>
    <p class="sec-sub">There is no less dust in the air — but the surface it lands on is different. A clear <b>superhydrophilic</b> film makes the condensate on the evaporator spread into a thin sheet that carries dust down into the drain pan, so the unit rinses its own fins every time it runs.</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>Condensate becomes the fin wash</h4><p>An evaporator coil has water condensing on its fins the whole time the unit runs. On bare fins it beads and drips, and the dust stays put — the PureBreeze film drops the water contact angle on the metal so far that the condensate <b>spreads into a thin sheet over the whole fin</b>, slides in under the dust and carries it down to the drain pan. That is self-cleaning in operation; what dust remains isn't stuck fast and comes off easily at the next wash.</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>Strong airflow and fast cooling, for longer</h4><p>An air conditioner goes sluggish a few months after cleaning because the fins clog, not because the refrigerant ran out. With the fins open for longer, air passes the evaporator freely, the compressor runs shorter cycles, and the "set to 25 but never cold" stage arrives much later.</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>Cleanings further apart, and easier</h4><p>Less dust, and dust that isn't stuck fast: the next wash needs only low-pressure water, no scrubbing that flattens the fins. Homes that washed every 3–4 months can stretch that out; A/C services offer it as an add-on the customer sees paying off at the next visit.</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>Inhibits bacteria and mould on the fins by more than 99%</h4><p>The fins are wet all the time and nobody takes them out to wash, so they are where mould and bacteria breed and send that musty smell out with the air — the film carries a nano antibacterial layer with an antibacterial rate above 99% — still above 99% after a full year in use — so the musty smell drops away. The film is nano-thin and clear, no barrier to heat exchange, no change to the fin colour.</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">See it first — <em>application clip and test photos</em></h2>
    <p class="sec-sub">Real evaporator and condenser coils being sprayed, plus dust-chamber and culture-dish photos</p>
    <div class="ggrid" style="grid-template-columns:1fr;max-width:880px">
      <figure class="packshot" style="margin:0">
        <div class="fbv"><iframe loading="lazy" src="https://www.youtube.com/embed/rAH-kRWLcZg" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="How to apply PureBreeze on A/C fins"></iframe></div>
        <figcaption>Application — sprayed onto the evaporator fins after washing and blow-drying</figcaption>
      </figure>
    </div>
    <div class="vidgrid vert solo" style="margin:18px 0 0">
      <figure style="margin:0">
        <div class="fbv v916"><iframe loading="lazy" src="https://www.youtube.com/embed/d4kNlcm259c" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="PureBreeze — spray-gun application on a condenser coil and half-coated fins"></iframe></div>
        <figcaption><b>Spraying a condenser coil with a spray gun</b> — the liquid loaded into a gravity gun and misted thinly over the condensing-unit fins, then a look at fins coated on one half only after outdoor use: the uncoated half thick with dust, the coated half still clear</figcaption>
      </figure>
    </div>
    <div class="ggrid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin-top:18px">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-dust1.webp" alt="Evaporator coil in a dust chamber — coated upper half still clear, uncoated lower half thick with dust" width="407" height="444"></div><figcaption><span class="no">01</span>Dust chamber — upper half coated, lower half uncoated</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-dust3.webp" alt="Fin block in a dust chamber — uncoated left side browned with dust, coated right side still bare metal" width="422" height="480"></div><figcaption><span class="no">02</span>Same fin block — left uncoated, right coated</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-petri-coated.webp" alt="Culture dish from coated aluminium foil, small colony" width="462" height="464"></div><figcaption><span class="no">03</span>Culture from coated foil</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-petri-bare.webp" alt="Culture dish from uncoated aluminium foil, mould colony spreading" width="469" height="464"></div><figcaption><span class="no">04</span>Culture from uncoated foil</figcaption></figure>
    </div>
    <p class="pricenote">An accelerated dust-chamber test, and cultures grown from coated and uncoated aluminium foil</p>
  </div>
</section>

<section class="buybox" id="uses">
  <div class="wrap">
    <h2 class="sec-h">What it <em>works on</em></h2>
    <p class="sec-sub">Aluminium fins of any coil that has been washed clean and blown dry — wall splits, ceiling cassettes, floor-standing units, outdoor condensing units</p>
    <div class="pts">
      <div class="pt"><span class="ic">❄️</span><div><h4>Evaporator coil (indoor)</h4><p>The fins behind the front panel that room dust lands on every day — the part that decides whether the airflow is strong or weak. Coat it after the next full wash and you will see the fins still open at the wash after that.</p></div></div>
      <div class="pt"><span class="ic">🌡️</span><div><h4>Condenser coil (outdoor unit)</h4><p>Outdoor fins choked by road dust, leaves and rain spray shed heat poorly, burn more electricity and run the compressor hot — coated, the dust is carried off by wind and rain, and the next hose-down clears it easily.</p></div></div>
      <div class="pt"><span class="ic">🧰</span><div><h4>A/C cleaning services · technicians</h4><p>Load the shop sprayer and offer it as an add-on after the wash — the customer pays once and sees the difference at the next visit, which is a reason to call the same shop again. 1 kg covers roughly 80 m² of fin area.</p></div></div>
      <div class="pt"><span class="ic">🏨</span><div><h4>Hotels · offices · restaurants</h4><p>Dozens of units on a contract cleaning cycle — coat the whole building once and push the cycle out; the cleaning saved per year is worth more than the liquid. Project pricing for volume.</p></div></div>
    </div>
  </div>
</section>

<section class="story">
  <div class="wrap">
    <div class="rdtag">SOURCE — where the raw material comes from</div>
    <h2>We import the core raw material<br>directly from the developer of this technology — <b>Feibo</b></h2>
    <div class="story-grid">
      <div class="bignum">≥99%<small>ANTIBACTERIAL RATE · 1 YEAR IN USE</small></div>
      <div class="story-body">
        <p>For this product we <b>import the core raw material from Feibo</b> (Changsha, China), the same developer behind our <a href="/en/glasscoating" style="color:var(--orange)">Glass Coating</a> and <a href="/en/solarpaneldefender" style="color:var(--orange)">Solar Panel Defender</a> — a formulation they developed specifically for the fins and internal metal parts of air-conditioning systems, used in public and commercial buildings in China, packed and quality-controlled here in Thailand.</p>
        <p>Why the fins need it: routine cleaning concentrates on the filter mesh and ignores the fins, where dirt hides most — in sampling, more than 80% of fins carried bacteria or mould far above the limit.</p>
        <div class="beats">
          <div class="beat"><div class="k">Principle</div><p>A thin clear film of inorganic silicon oxides + functional antibacterial materials + organic polymers — it makes the fin surface <b>superhydrophilic</b>, so condensate spreads into a sheet that carries dust and grime away, and forms a barrier against oil and organic contaminants sticking to the fins</p></div>
          <div class="beat"><div class="k">Antibacterial</div><p>The nano layer on the fins inhibits bacteria, mould and common pathogens — antibacterial rate above 99%, fewer microbes carried out on the airflow and less odour</p></div>
          <div class="beat"><div class="k">Dust test</div><p>In an accelerated dust-chamber test the coated area showed clearly less deposition than the uncoated area, so performance declines more slowly and cleanings can be spaced further apart</p></div>
          <div class="beat"><div class="k">No effect on the unit</div><p>Nano-thin and transparent, no effect on heat transfer or equipment operation — the process: deep clean → fully dry → spray evenly → ambient cure, which is exactly what we describe below</p></div>
        </div>
        <div class="speccard" style="margin-top:14px">
          <table>
            <thead><tr><th>Bacteria on the fins (per mL)</th><th>1 week in use</th><th>1 month</th><th>6 months</th><th>1 year</th></tr></thead>
            <tbody>
              <tr><td>Before cleaning</td><td>5.83 × 10⁶</td><td>1.19 × 10⁷</td><td>1.46 × 10⁷</td><td>2.06 × 10⁷</td></tr>
              <tr><td>30 min after cleaning</td><td>381</td><td>1,560</td><td>3,578</td><td>9,360</td></tr>
              <tr><td>After coating — inhibition rate</td><td>&gt; 99.91%</td><td>&gt; 99.85%</td><td>&gt; 99.52%</td><td>&gt; 99.13%</td></tr>
            </tbody>
          </table>
        </div>
        <p style="font-size:13px;color:var(--muted);margin-top:8px">Lab test on evaporator fins not cleaned in between — the inhibition rate is still above 99% after a full year in use</p>
      </div>
    </div>
  </div>
</section>

<section class="buybox" id="spec">
  <div class="wrap">
    <h2 class="sec-h">Technical specification <em>figures from the TDS</em></h2>
    <p class="sec-sub">Typical values for the liquid and the cured film — the full sheet and the Safety Data Sheet are below</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>Item</th><th>Value</th><th>Method / note</th></tr></thead>
        <tbody>
          <tr><td>Type</td><td>Single-component nano coating, alcohol- and water-borne, ready to use</td><td>Do not dilute</td></tr>
          <tr><td>Appearance</td><td>Pale blue to pale white translucent liquid</td><td>Slight ethanol odour</td></tr>
          <tr><td>Solids</td><td>10 ± 2 % by weight</td><td>DIN EN ISO 3251</td></tr>
          <tr><td>Density (20°C)</td><td>0.88–0.92 g/cm³</td><td>DIN EN ISO 2811-2</td></tr>
          <tr><td>pH</td><td>4.0–6.0</td><td>DIN ISO 976</td></tr>
          <tr><td>Flash point</td><td>26.5°C</td><td>ISO 13736 — flammable liquid</td></tr>
          <tr><td>Water contact angle (film)</td><td>≤ 7°</td><td>Superhydrophilic — water spreads into a sheet</td></tr>
          <tr><td>Surface resistance</td><td>10⁹ Ω</td><td>Anti-static — dust is not attracted</td></tr>
          <tr><td>Pencil hardness</td><td>6H</td><td></td></tr>
          <tr><td>Adhesion (cross-cut)</td><td>Grade 0</td><td>GB/T 9286-1998, GB/T 31815-2015</td></tr>
          <tr><td>Acid resistance</td><td>No visible cracking or blistering</td><td></td></tr>
          <tr><td>Antibacterial / anti-mould</td><td>&gt; 99% · grade 0</td><td>GB 21551.2-2010 — see the report below</td></tr>
          <tr><td>Spraying</td><td>HVLP, 1.0–1.2 mm nozzle, ~0.2 MPa</td><td>or any fine-mist sprayer at low pressure</td></tr>
          <tr><td>Consumption</td><td>30–50 ml/m²</td><td>one home unit ≈ 20 ml in our own application</td></tr>
          <tr><td>Tack-free / hardened</td><td>5 min / ~1 hour</td><td>heat: 50°C ≈ 2 min · 70°C ≈ 1 min</td></tr>
          <tr><td>Full cure</td><td>6 h (warm) – 20 h (cool)</td><td>keep water off the film until hardened</td></tr>
          <tr><td>Storage / shelf life</td><td>−10 to 45°C · 12 months unopened</td><td>use up soon after opening</td></tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:18px;display:flex;gap:10px;flex-wrap:wrap">
      <a class="btn btn-ghost" href="/files/purebreeze-tds.pdf" target="_blank" rel="noopener">📑 Technical Data Sheet (TDS)</a>
      <a class="btn btn-ghost" href="/files/purebreeze-sds.pdf" target="_blank" rel="noopener">📄 Safety Data Sheet (MSDS)</a>
    </div>
  </div>
</section>

<section class="gallery" id="certs">
  <div class="wrap">
    <h2 class="sec-h">Microbial test report <em>from an accredited laboratory</em></h2>
    <p class="sec-sub">The "above 99%" figures on this page come from this report — Guangdong Detection Center of Microbiology (Gmicro Testing), Guangzhou, a CMA- and CNAS-accredited laboratory · report no. 2020SPS942R01D · the original is bilingual Chinese–English; English notes under each page</p>
    <div class="speccard" style="margin-top:20px">
      <table>
        <thead><tr><th>Test</th><th>Method</th><th>Result</th></tr></thead>
        <tbody>
          <tr><td>Antibacterial — <i>Escherichia coli</i></td><td>GB 21551.2-2010 Appendix A · 24 h contact</td><td><b>&gt; 99%</b> — from 2.4 × 10⁵ to fewer than 20 cfu</td></tr>
          <tr><td>Antibacterial — <i>Staphylococcus aureus</i></td><td>GB 21551.2-2010 Appendix A · 24 h contact</td><td><b>&gt; 99%</b> — from 3.4 × 10⁵ to fewer than 20 cfu</td></tr>
          <tr><td>Anti-mould — 5 standard strains (<i>Aspergillus niger</i>, <i>Penicillium funiculosum</i>, <i>Chaetomium globosum</i>, <i>Aureobasidium pullulans</i>, <i>Paecilomyces variotii</i>)</td><td>GB 21551.2-2010 Appendix C</td><td><b>Grade 0</b> — the best grade: no growth even at 50× magnification</td></tr>
        </tbody>
      </table>
    </div>
    <div class="ggrid" style="margin-top:22px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-report-p1.webp" alt="Cover page of the analysis report, Guangdong Detection Center of Microbiology, no. 2020SPS942R01D, sample: self-cleaning antibacterial coating" width="804" height="1364"></div><figcaption><span class="no">01</span><b>Cover page</b> — commissioned test, sample "Self-cleaning antibacterial coating", applicant is the developer of our raw material</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-report-p2.webp" alt="Antibacterial results page — E. coli and Staphylococcus aureus inhibition above 99%" width="808" height="1364"></div><figcaption><span class="no">02</span><b>Antibacterial results</b> — <i>E. coli</i> and <i>S. aureus</i> inhibited above 99% after 24 h contact; the standard's pass mark is 90%</figcaption></figure>
      <figure class="gph"><div class="im"><img loading="lazy" decoding="async" src="/img/purebreeze-report-p3.webp" alt="Anti-mould results page — mould-proof grade 0" width="752" height="1364"></div><figcaption><span class="no">03</span><b>Anti-mould results</b> — grade 0 against 5 standard strains, the best grade in the standard</figcaption></figure>
    </div>
  </div>
</section>

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">Sizes and prices</h2>
    <p class="sec-sub">Liquid for <b>your own sprayer</b> — enter the fin area and the calculator picks the cheapest set</p>
    <div class="pricecard">
      <table data-calc="1" data-shipping="40">
        <thead><tr><th>Size</th><th>Approx. fin area</th><th>Price</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="8">100 g</td><td>≈ 8 m² · about 5 home units</td><td class="pr" data-price="690">690.-</td></tr>
          <tr><td class="sz" data-sqm="40">500 g</td><td>≈ 40 m² · about 25 units</td><td class="pr" data-price="2990">2,990.-</td></tr>
          <tr><td class="sz" data-sqm="80">1 kg</td><td>≈ 80 m² · about 50 units</td><td class="pr" data-price="5500">5,500.-</td></tr>
          <tr data-calc="skip"><td class="sz">Volume<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">hotels / offices / A/C services</small></td><td>Many units per round</td><td class="pr">Project pricing — ask</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">Shipping <b>40 baht</b> · From our own application, one home unit takes about <b>20 ml</b> sprayed as a fine low-pressure mist — so a 100 g bottle does about 5 units and 1 kg about 50. That is hand-spraying; a heavy coat or a large unit uses more · Not sure how much you need: send the number of units and their BTU on chat and we work it out for you, free, before you order</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">How to apply — <em>all on this page</em></h2>
    <p class="sec-sub">One rule decides the whole job: <b>coat only fins that are washed clean and completely dry</b> — the film bonds to whatever is on the surface, so sprayed over old dust you get a film that glues the dust to the fins</p>
    <ol class="flow">
      <li class="fstep"><h4>Switch off, cut the power, and wash the unit as usual</h4><p>Remove the front panel and filter, wash the evaporator fins with coil cleaner and low-pressure water the way a technician does, and rinse every trace of cleaner off — leftover coil cleaner blocks the film just as dust does. Hose the outdoor condenser from the inside out.</p></li>
      <li class="fstep"><h4>Blow completely dry</h4><p>Blow or air-dry until there are no droplets left in the fins and no dampness — this coats a dry surface, and water sitting in the fin channels dilutes the liquid until the film doesn't join up. In a hurry, use a blower top to bottom.</p><span class="fchip">Bone dry, no droplets</span></li>
      <li class="fstep"><h4>Load your sprayer and apply a fine, thin mist at low pressure over the whole fin pack</h4><p>Pour the liquid into a clean, dry sprayer — ideally an HVLP gun with a 1.0–1.2 mm nozzle at about 0.2 MPa, or any sprayer that gives a fine mist — and <b>use low pressure</b> so it comes out as a fine mist, not a jet — high pressure flattens the fins and bounces the liquid off. Work left to right, row by row, until the whole fin surface is evenly and thinly wet, never to the point of running; liquid that runs and pools at the bottom is wasted. One home unit takes under 2 minutes, both coils.</p><span class="fchip">Low pressure, fine mist</span><span class="fchip">One thin coat</span></li>
      <li class="fstep"><h4>Let it harden at room temperature, about 1 hour</h4><p>The film is tack-free in 5 minutes and hardened through in about 1 hour at room temperature — no blowing, no heating. <b>Keep water off the fins meanwhile</b>: water on an unhardened film leaves permanent marks. Then put the filter and front panel back.</p><span class="fchip">Tack-free 5 min</span><span class="fchip">Hardened ~1 h</span></li>
      <li class="fstep"><h4>After 1 hour, run the unit as normal</h4><p>Run the unit once the film has hardened (it reaches full cure in 6 hours in warm weather to 20 hours in cool conditions, but you need not wait for that). There may be a faint smell for the first few minutes, then it goes — at the next cleaning, try low-pressure plain water first; if the fins are still open, skip the coil cleaner, and if you need one choose neutral or mildly acidic — <b>alkaline coil cleaners of pH 11 and above destroy the film</b>. Re-coat after every full wash.</p></li>
    </ol>

    <div class="warn"><b>⚠ Safety:</b> Flammable liquid (flash point 26.5°C) containing several alcohols including methanol — switch off and isolate the power before every job, keep away from sparks and cigarettes, spray in a ventilated space and wear <b>an organic-vapour respirator</b>, eye protection and gloves. If in eyes, rinse with water for several minutes and seek medical attention. Do not spray into the control board, fan motor or sensors. Keep the bottle tightly closed, out of reach of children and direct sun. Details in the MSDS above.</div>
  </div>
</section>

<section class="story" id="straight">
  <div class="wrap">
    <div class="rdtag">STRAIGHT TALK</div>
    <h2>Before you pay, read these 5 points —<br><b>this is not a miracle product</b>, and we don't want you misled</h2>
    <div class="story-grid">
      <div class="bignum">5<small>things most sellers don't tell you</small></div>
      <div class="story-body">
        <div class="beats">
          <div class="beat"><div class="k">1 · It does not mean never cleaning the unit again</div><p>It makes <b>less dust stick, and what sticks come off more easily</b>, so cleanings get further apart — but the filter still gets washed as usual and the fins still get washed when the time comes. Anyone selling "coat it and forget the unit" is wrong.</p></div>
          <div class="beat"><div class="k">2 · Dirty or damp fins waste the whole bottle</div><p>The film bonds to whatever is on the surface: sprayed over dust it glues the dust to the fins; sprayed on fins wet with cleaner it dilutes until it doesn't join up. Washing clean and blowing dry is 80% of the job, not the liquid.</p></div>
          <div class="beat"><div class="k">3 · Black mould or slime in the drain pan must be dealt with first</div><p>This is a dust film for the fins, not a disinfectant — mould and slime in the drain pan, drain line and blower have to be cleaned out first. If the musty smell comes from there, coating the fins does nothing for the smell.</p></div>
          <div class="beat"><div class="k">4 · It does not fix a unit that isn't cooling for other reasons</div><p>Refrigerant leak, weak compressor, failing capacitor, outdoor fan not spinning — they look like "clogged fins" but need repair. If the unit still isn't cold after a wash, have the system checked before buying this.</p></div>
          <div class="beat"><div class="k">5 · Re-coat after every full wash</div><p>Coil cleaner and high-pressure water take part of the film off with the dirt — after every full wash, spray again once the fins are dry. Budget the liquid per wash as part of the cleaning cost, not as a one-off for the life of the unit.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="sec-h">Is this <em>the right product for your job?</em></h2>
    <p class="sec-sub">If the problem isn't dust on A/C fins, one of these may fit better</p>
    <div class="altgrid">
      <a class="altcard" href="/en/bioshield">
        <div class="k">Black mould · algae · slime</div>
        <h4>BioShield</h4>
        <p>If the problem is black mould, algae or a musty smell rather than dust — wash and hold the mould back with this first, then deal with dust.</p>
        <div class="go">View details →</div>
      </a>
      <a class="altcard" href="/en/easyclean">
        <div class="k">Walls · doors · furniture</div>
        <h4>EasyClean</h4>
        <p>For painted walls and metal where the problem is oily grime and stains, not A/C fins — one wipe and it's off.</p>
        <div class="go">View details →</div>
      </a>
    </div>
  </div>
</section>

<section class="order" id="order">
  <div class="wrap">
    <h2 class="sec-h">Order <em>PureBreeze</em></h2>
    <div class="ordercard">
      <h3>Order directly on chat</h3>
      <div class="sub">Tell us the number of units and their BTU and we work out the quantity for you, free, before you order · <b>Project pricing for hotels, offices and A/C services</b></div>
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
