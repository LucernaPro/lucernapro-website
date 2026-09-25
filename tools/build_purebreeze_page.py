#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_purebreeze_page.py — สร้าง /purebreeze และ /en/purebreeze

PureBreeze — น้ำยาเคลือบใสระดับนาโนสำหรับแผงฟินคอยล์เย็นและคอยล์ร้อนของเครื่องปรับอากาศ ป้องกันฝุ่นเกาะสะสม
ย้ายมาจากหน้า Wix เดิม (lekvtwin.wixsite.com/lucerna/purebreeze) — Pist 25 ก.ย. 2026 "ไปเอาข้อมูลมาลงก่อน สร้างหน้าใหม่เลย"
ราคาตามหน้า Wix: น้ำยา 100 g 690 / 8 ตร.ม., 500 g 2,990 / 40, 1 kg 5,500 / 80 ส่ง 40 · (สเปรย์ 100 ml 790 เลิกขาย — Pist 25 ก.ย. 2026 "จะไม่มีสเปรย์อีกแล้ว จะเป็นแบบไปบรรจุเครื่องพ่นเอง พ่นด้วยแรงต่ำ"; คลิปทดสอบ XZUhhF2gLpY เป็นของ solar เอาออก)
ไม่มี TDS ในมือ → ไม่มีตารางสเปค · เวลาแห้งในขั้นตอนใช้งานเป็นตัวเลขรอ Pist ยืนยัน (ดูหมายเหตุใน BODY)
hero/การ์ด = ภาพ placeholder ที่ Claude ทำ (img/purebreeze-hero-sq.webp / -card.webp) — Pist ไม่เอารูป Wix เดิม
วิดีโอจาก Wix: วิธีใช้ rAH-kRWLcZg · การทดสอบ XZUhhF2gLpY (YouTube) · Shopee: 392415703/28808079817
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
<style id="purebreeze-deal-css">.direct-deal{font-size:14.5px;color:var(--ink);border:1px solid rgba(237,106,47,.45);background:rgba(237,106,47,.08);border-radius:9px;padding:10px 14px;margin:14px 0 4px;line-height:1.55}</style>'''
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
    'th': 'ฟิล์มใสบางบนฟินคอยล์เย็นและคอยล์ร้อน ฝุ่นเกาะสะสมยากขึ้น ลมผ่านเต็มที่ ยืดรอบล้างแอร์ — บรรจุเครื่องพ่นเอง 100 g ทำแอร์ได้ 2–3 ตัว',
    'en': 'A thin clear film on evaporator and condenser fins — dust struggles to build up, air flows freely, cleanings get further apart. Load your own sprayer; 100 g does 2–3 units.',
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
      <p class="lede">แอร์ที่เพิ่งล้างเสร็จ ลมแรง เย็นเร็ว — แล้วอีกไม่กี่เดือนก็กลับมาอืดเพราะฝุ่นอุดฟินอีกรอบ PureBreeze คือฟิล์มใสบางระดับนาโนที่เคลือบลงบน<b>ฟินคอยล์เย็นและคอยล์ร้อน</b>หลังล้างเสร็จ ทำให้ฝุ่นเกาะสะสมยากขึ้นมาก ลมผ่านฟินได้เต็มที่นานกว่าเดิม รอบล้างแอร์จึงห่างออกไป — เป็นน้ำยาสำหรับ<b>บรรจุเครื่องพ่นเอง พ่นด้วยแรงดันต่ำ</b> ขวดเล็ก 100 g ทำแอร์บ้านได้ 2–3 ตัว</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">สั่งซื้อ / ดูราคา</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>ปรึกษาหน้างานฟรี</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/purebreeze-hero-sq.webp" alt="PureBreeze น้ำยาเคลือบกันฝุ่นแผงคอยล์แอร์ — ฟินคอยล์ที่ฝุ่นเกาะไม่ติด" width="1200" height="1200">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">แอร์ที่เคลือบแล้ว <em>ต่างจากเดิมตรงไหน</em></h2>
    <p class="sec-sub">ฝุ่นในอากาศไม่ได้ลดลง แต่ผิวฟินที่มันจะเกาะเปลี่ยนไป — ฟิล์มเรียบใสทำให้ฝุ่นที่ปะทะฟินหลุดตามลมแทนที่จะเกาะแล้วสะสมเป็นชั้น</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>ฝุ่นเกาะสะสมยากขึ้น</h4><p>ฟินอะลูมิเนียมเปล่ามีผิวหยาบระดับไมครอนที่ฝุ่นเกาะได้ทันที ฝุ่นชั้นแรกเป็นที่เกาะของชั้นถัดไป จนกลายเป็นแผ่นสักหลาดปิดลม — ฟิล์ม PureBreeze ปิดผิวหยาบนั้นไว้ ฝุ่นที่ปะทะไม่มีที่ยึด ส่วนใหญ่หลุดตามลมไปที่แผ่นกรอง ซึ่งล้างง่ายกว่าฟินหลายเท่า</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>ลมแรง เย็นเร็ว นานกว่าเดิม</h4><p>แอร์อืดหลังล้างไม่กี่เดือนเพราะฟินอุด ไม่ใช่เพราะน้ำยาแอร์หมด — เมื่อฟินโล่งนานขึ้น ลมผ่านคอยล์เย็นได้เต็มที่ คอมเพรสเซอร์ทำงานสั้นลงต่อรอบ อาการ "เปิด 25 แต่ไม่เย็น" มาช้ากว่าเดิมมาก</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>ล้างแอร์ห่างขึ้น ล้างง่ายขึ้น</h4><p>ฝุ่นที่เกาะน้อยและเกาะไม่แน่น ล้างครั้งถัดไปแค่น้ำแรงดันเบาก็หลุด ไม่ต้องขัดฟินจนล้ม — บ้านที่เคยล้างทุก 3–4 เดือนยืดออกไปได้ ร้านล้างแอร์ใช้เป็นบริการเสริมที่ลูกค้าเห็นผลจริงในรอบถัดไป</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>ใส บาง ไม่ขวางการแลกเปลี่ยนความร้อน</h4><p>ฟิล์มบางระดับนาโน ไม่เปลี่ยนสีฟิน ไม่เพิ่มความหนาจนกันความร้อน คอยล์ร้อนนอกบ้านที่โดนฝุ่นถนนและละอองฝนก็เคลือบได้ — ผู้ผลิตระบุคุณสมบัติยับยั้งแบคทีเรียบนผิวฟิล์มด้วย เราเขียนไว้ตามเอกสารผู้ผลิต ไม่ได้ทดสอบเอง</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">ดูของจริงก่อน — <em>คลิปวิธีใช้</em></h2>
    <p class="sec-sub">พ่นบนแผงฟินคอยล์เย็นจริง หลังล้างและเป่าแห้งแล้ว</p>
    <div class="ggrid" style="grid-template-columns:1fr;max-width:880px">
      <figure class="packshot" style="margin:0">
        <div class="fbv"><iframe loading="lazy" src="https://www.youtube.com/embed/rAH-kRWLcZg" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="วิธีใช้ PureBreeze บนแผงฟินแอร์"></iframe></div>
        <figcaption>วิธีใช้ — พ่นบนแผงฟินคอยล์เย็นหลังล้างและเป่าแห้งแล้ว</figcaption>
      </figure>
    </div>
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

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">ขนาดและราคา</h2>
    <p class="sec-sub">น้ำยาสำหรับ<b>บรรจุเครื่องพ่นเอง</b> — กรอกพื้นที่ฟินให้ระบบจัดชุดที่ถูกที่สุดให้ได้</p>
    <div class="pricecard">
      <table data-calc="1" data-shipping="40">
        <thead><tr><th>ขนาด</th><th>พื้นที่ฟินโดยประมาณ</th><th>ราคา</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="8">100 g</td><td>≈ 8 ตร.ม.</td><td class="pr" data-price="690">690.-</td></tr>
          <tr><td class="sz" data-sqm="40">500 g</td><td>≈ 40 ตร.ม.</td><td class="pr" data-price="2990">2,990.-</td></tr>
          <tr><td class="sz" data-sqm="80">1 kg</td><td>≈ 80 ตร.ม.</td><td class="pr" data-price="5500">5,500.-</td></tr>
          <tr data-calc="skip"><td class="sz">จำนวนมาก<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">โรงแรม / ออฟฟิศ / ร้านล้างแอร์</small></td><td>หลายเครื่องต่อรอบ</td><td class="pr">ราคาโครงการ — สอบถาม</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">ค่าจัดส่ง <b>40 บาท</b> · แอร์บ้านขนาด 9,000–18,000 BTU หนึ่งตัว คอยล์เย็นกับคอยล์ร้อนรวมกันคือพื้นที่ฟินราว 2–4 ตร.ม. — ขวด 100 g จึงทำได้ 2–3 ตัว ส่วน 1 กก. ทำได้ราว 20–30 ตัว · ไม่แน่ใจว่าต้องใช้เท่าไหร่ บอกจำนวนแอร์และขนาด BTU มาทางแชท เราคำนวณให้ฟรีก่อนสั่ง</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">วิธีใช้งาน — <em>จบบนหน้านี้</em></h2>
    <p class="sec-sub">หลักเดียวที่ตัดสินทั้งงาน: <b>เคลือบบนฟินที่ล้างสะอาดและแห้งสนิทเท่านั้น</b> — ฟิล์มเกาะสิ่งที่อยู่บนผิว ถ้าพ่นทับฝุ่นเดิม ก็ได้ฟิล์มที่เคลือบฝุ่นไว้กับฟิน</p>
    <ol class="flow">
      <li class="fstep"><h4>ปิดเครื่อง ตัดไฟ แล้วล้างแอร์ให้สะอาดตามปกติ</h4><p>ถอดหน้ากากและแผ่นกรอง ล้างฟินคอยล์เย็นด้วยน้ำยาล้างคอยล์และน้ำแรงดันเบาตามที่ช่างทำ ล้างคราบน้ำยาออกให้หมด — คราบน้ำยาล้างคอยล์ที่เหลืออยู่จะขวางฟิล์มเท่ากับฝุ่น คอยล์ร้อนนอกบ้านฉีดน้ำล้างจากด้านในออกด้านนอก</p></li>
      <li class="fstep"><h4>เป่าให้แห้งสนิท</h4><p>เป่าลมหรือปล่อยให้แห้งจนฟินไม่มีหยดน้ำค้างและไม่ชื้น — ตัวนี้เคลือบบนผิวแห้ง น้ำที่ค้างในร่องฟินจะเจือน้ำยาจนฟิล์มไม่ต่อกัน ถ้าเร่งเวลา ใช้เครื่องเป่าลมไล่จากบนลงล่าง</p><span class="fchip">แห้งสนิท ไม่มีหยดน้ำ</span></li>
      <li class="fstep"><h4>บรรจุเครื่องพ่น แล้วพ่นด้วยแรงดันต่ำเป็นละอองบางทั่วแผงฟิน</h4><p>เทน้ำยาลงเครื่องพ่นที่สะอาดและแห้ง (กระบอกฉีดฝอย เครื่องพ่นแบบปั๊มมือ หรือกาพ่นสีปรับแรงดันต่ำ) <b>ใช้แรงดันต่ำ</b> ให้ออกเป็นละอองละเอียด ไม่ใช่เป็นสาย — แรงดันสูงจะทำให้ฟินล้มและน้ำยาเด้งออก พ่นห่างราว 15–20 ซม. ซ้ายไปขวาทีละแถวให้ผิวฟินเปียกบางสม่ำเสมอ ไม่พ่นจนไหลย้อย เนื้อยาที่ไหลรวมกันที่ด้านล่างคือของที่เสียเปล่า แอร์บ้านหนึ่งตัวใช้เวลาไม่ถึง 2 นาที ทำทั้งคอยล์เย็นและคอยล์ร้อน</p><span class="fchip">แรงดันต่ำ ละอองละเอียด</span><span class="fchip">ชั้นบางชั้นเดียว</span><span class="fchip">ห่าง 15–20 ซม.</span></li>
      <li class="fstep"><h4>รอให้ผิวแห้งก่อนประกอบเครื่อง</h4><p>ปล่อยให้ฟิล์มเซ็ตตัวบนฟินอย่างน้อย <b>30 นาที</b> ก่อนใส่แผ่นกรองและหน้ากากกลับ ระหว่างนี้ไม่ให้น้ำหรือฝุ่นโดนฟิน</p><span class="fchip">เซ็ตตัว 30 นาที</span></li>
      <li class="fstep"><h4>เปิดใช้งานได้หลัง 1 ชั่วโมง</h4><p>หลังฟิล์มแห้งครบ <b>1 ชั่วโมง</b> เปิดแอร์ใช้งานได้ตามปกติ ครั้งแรกอาจมีกลิ่นน้ำยาจางๆ ไม่กี่นาทีแล้วหาย — รอบล้างถัดไปให้ล้างด้วยน้ำเปล่าแรงดันเบาก่อน ถ้าฟินยังโล่งไม่ต้องใช้น้ำยาล้างคอยล์ และเคลือบซ้ำหลังการล้างใหญ่ทุกครั้ง</p></li>
    </ol>

    <div class="warn"><b>⚠ ความปลอดภัย:</b> พ่นในที่อากาศถ่ายเท สวมถุงมือและแว่นครอบตา ปิดเครื่องและตัดไฟก่อนทำงานทุกครั้ง ไม่พ่นเข้าแผงวงจร มอเตอร์พัดลม และเซ็นเซอร์ เก็บขวดพ้นมือเด็กและแสงแดดตรง</div>
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
      <p class="lede">A freshly cleaned air conditioner blows hard and cools fast — and a few months later it is sluggish again because dust has choked the fins. PureBreeze is a thin, clear nano film applied to the <b>evaporator and condenser fins</b> right after cleaning. Dust finds it much harder to settle and build up, air keeps flowing through the fins for longer, and cleanings get further apart — a liquid you <b>load into your own sprayer and apply at low pressure</b>; the 100 g bottle does 2–3 home units.</p>
      <div class="hero-cta">
        <a class="btn btn-orange" href="#price">Order / Prices</a>
        <a class="btn btn-fb" href="https://m.me/lucernapro"><span class="fbadge">f</span>Free advice on chat</a>
      </div>
    </div>
    <figure class="packshot">
      <img src="/img/purebreeze-hero-sq.webp" alt="PureBreeze dust-repellent nano coating for air-conditioner coil fins" width="1200" height="1200">
    </figure>
  </div>
</section>

<section class="sellpts">
  <div class="wrap">
    <h2 class="sec-h">What changes <em>once the fins are coated</em></h2>
    <p class="sec-sub">There is no less dust in the air — but the surface it lands on is different. A smooth clear film means dust that hits the fins is carried on by the airflow instead of sticking and stacking up in layers.</p>
    <div class="pts">
      <div class="pt"><span class="ic">01</span><div><h4>Dust struggles to build up</h4><p>Bare aluminium fins have a micron-rough surface that dust grips instantly; the first layer becomes the anchor for the next until the fins wear a felt blanket that blocks the air. The PureBreeze film seals that rough surface, so incoming dust has nothing to hold — most of it moves on to the filter, which is far easier to wash than the fins.</p></div></div>
      <div class="pt"><span class="ic">02</span><div><h4>Strong airflow and fast cooling, for longer</h4><p>An air conditioner goes sluggish a few months after cleaning because the fins clog, not because the refrigerant ran out. With the fins open for longer, air passes the evaporator freely, the compressor runs shorter cycles, and the "set to 25 but never cold" stage arrives much later.</p></div></div>
      <div class="pt"><span class="ic">03</span><div><h4>Cleanings further apart, and easier</h4><p>Less dust, and dust that isn't stuck fast: the next wash needs only low-pressure water, no scrubbing that flattens the fins. Homes that washed every 3–4 months can stretch that out; A/C services offer it as an add-on the customer sees paying off at the next visit.</p></div></div>
      <div class="pt"><span class="ic">04</span><div><h4>Clear, thin, no barrier to heat exchange</h4><p>A nano-thin film that does not change the colour of the fins or add thickness that would insulate them. Outdoor condenser fins that take road dust and rain can be coated too — the manufacturer also states an antibacterial property on the film surface; we quote it from the manufacturer's documents and have not tested it ourselves.</p></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="proof">
  <div class="wrap">
    <h2 class="sec-h">See it first — <em>application clip</em></h2>
    <p class="sec-sub">Sprayed onto real evaporator fins after washing and blow-drying</p>
    <div class="ggrid" style="grid-template-columns:1fr;max-width:880px">
      <figure class="packshot" style="margin:0">
        <div class="fbv"><iframe loading="lazy" src="https://www.youtube.com/embed/rAH-kRWLcZg" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="How to apply PureBreeze on A/C fins"></iframe></div>
        <figcaption>Application — sprayed onto the evaporator fins after washing and blow-drying</figcaption>
      </figure>
    </div>
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

<section class="buybox" id="price">
  <div class="wrap">
    <h2 class="sec-h">Sizes and prices</h2>
    <p class="sec-sub">Liquid for <b>your own sprayer</b> — enter the fin area and the calculator picks the cheapest set</p>
    <div class="pricecard">
      <table data-calc="1" data-shipping="40">
        <thead><tr><th>Size</th><th>Approx. fin area</th><th>Price</th></tr></thead>
        <tbody>
          <tr><td class="sz" data-sqm="8">100 g</td><td>≈ 8 m²</td><td class="pr" data-price="690">690.-</td></tr>
          <tr><td class="sz" data-sqm="40">500 g</td><td>≈ 40 m²</td><td class="pr" data-price="2990">2,990.-</td></tr>
          <tr><td class="sz" data-sqm="80">1 kg</td><td>≈ 80 m²</td><td class="pr" data-price="5500">5,500.-</td></tr>
          <tr data-calc="skip"><td class="sz">Volume<br><small style="font-family:var(--body);font-weight:400;font-size:12.5px;color:var(--muted)">hotels / offices / A/C services</small></td><td>Many units per round</td><td class="pr">Project pricing — ask</td></tr>
        </tbody>
      </table>
    </div>
    <p class="pricenote">Shipping <b>40 baht</b> · One 9,000–18,000 BTU home unit, evaporator and condenser together, is roughly 2–4 m² of fin area — so the 100 g bottle does 2–3 units and 1 kg about 20–30 · Not sure how much you need: send the number of units and their BTU on chat and we work it out for you, free, before you order</p>
  </div>
</section>

<section class="howto">
  <div class="wrap">
    <h2 class="sec-h">How to apply — <em>all on this page</em></h2>
    <p class="sec-sub">One rule decides the whole job: <b>coat only fins that are washed clean and completely dry</b> — the film bonds to whatever is on the surface, so sprayed over old dust you get a film that glues the dust to the fins</p>
    <ol class="flow">
      <li class="fstep"><h4>Switch off, cut the power, and wash the unit as usual</h4><p>Remove the front panel and filter, wash the evaporator fins with coil cleaner and low-pressure water the way a technician does, and rinse every trace of cleaner off — leftover coil cleaner blocks the film just as dust does. Hose the outdoor condenser from the inside out.</p></li>
      <li class="fstep"><h4>Blow completely dry</h4><p>Blow or air-dry until there are no droplets left in the fins and no dampness — this coats a dry surface, and water sitting in the fin channels dilutes the liquid until the film doesn't join up. In a hurry, use a blower top to bottom.</p><span class="fchip">Bone dry, no droplets</span></li>
      <li class="fstep"><h4>Load your sprayer and apply a fine, thin mist at low pressure over the whole fin pack</h4><p>Pour the liquid into a clean, dry sprayer (a trigger mist bottle, a hand-pump sprayer or a spray gun turned down) and <b>use low pressure</b> so it comes out as a fine mist, not a jet — high pressure flattens the fins and bounces the liquid off. Hold about 15–20 cm away, left to right, row by row, until the fin surface is evenly and thinly wet, never to the point of running; liquid that runs and pools at the bottom is wasted. One home unit takes under 2 minutes, both coils.</p><span class="fchip">Low pressure, fine mist</span><span class="fchip">One thin coat</span><span class="fchip">15–20 cm away</span></li>
      <li class="fstep"><h4>Let it set before reassembling</h4><p>Leave the film to set on the fins for at least <b>30 minutes</b> before the filter and front panel go back. Keep water and dust off the fins meanwhile.</p><span class="fchip">Sets in 30 min</span></li>
      <li class="fstep"><h4>Switch on after 1 hour</h4><p>Once the film has dried for <b>1 hour</b>, run the unit normally. There may be a faint smell for the first few minutes, then it goes — at the next cleaning, try low-pressure plain water first; if the fins are still open, skip the coil cleaner, and re-coat after every full wash.</p></li>
    </ol>

    <div class="warn"><b>⚠ Safety:</b> Spray in a ventilated space, wear gloves and eye protection, and switch off and isolate the power before every job. Do not spray into the control board, fan motor or sensors. Keep the bottle out of reach of children and direct sun.</div>
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
