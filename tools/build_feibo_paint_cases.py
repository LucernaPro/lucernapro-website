# -*- coding: utf-8 -*-
"""
build_feibo_paint_cases.py — เคส Paint Coating จากโครงการของ Feibo (ผู้พัฒนาวัตถุดิบ, จีน)
สองเคส: ปั๊มน้ำมัน Sinopec (feibo-sinopec-canopy) และรถไฟ/รถไฟใต้ดิน/รถราง (feibo-rail-transit)
วิธี: chrome-transplant จากโพสต์ solar เหมือน build_silo_post.py — TH+EN
รูป: /img/post/{slug}-h*.webp (narrative) + -g*.webp (800x800 gallery) จากรูปที่ Lilian ส่ง ก.ย. 2026
รัน: python3 tools/build_feibo_paint_cases.py (จาก root ของ repo)
"""
import os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
GRID_STYLE = ("display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));"
              "gap:10px;margin-top:26px")

def dims(name):
    return Image.open(os.path.join(ROOT, "img", "post", name + ".webp")).size

def gallery_html(slug, n, alt_prefix):
    imgs = "".join(
        f'<img src="/img/post/{slug}-g{i:02d}.webp" alt="{alt_prefix} {i:02d}" loading="lazy" '
        f'width="800" height="800" style="border-radius:10px;border:1px solid var(--line)">\n'
        for i in range(1, n + 1))
    return '<div style="' + GRID_STYLE + '">\n' + imgs + '</div>'

def fig(slug, k, alt, cap, hero=False):
    w, h = dims(f"{slug}-h{k}")
    cls = ' class="hero"' if hero else ''
    icls = ' class="tall"' if h > w else ''
    lazy = '' if hero else ' loading="lazy"'
    return (f'    <figure{cls}><img{icls} src="/img/post/{slug}-h{k}.webp" alt="{alt}"{lazy} '
            f'width="{w}" height="{h}"><figcaption>{cap}</figcaption></figure>\n')

# ─────────────────────────── CASE 1: SINOPEC ───────────────────────────
S = "feibo-sinopec-canopy"
S_TH_TITLE = "เคลือบหลังคาและป้ายปั๊มน้ำมัน Sinopec — โครงการ Self-Cleaning บนแผงสีที่ล้างยากที่สุดของเมือง"
S_TH_DESC = ("โครงการของ Feibo ผู้พัฒนาวัตถุดิบ Paint Coating ของเรา: เคลือบแผงสีแดง-ขาวและป้ายโลโก้บนหลังคาปั๊มน้ำมัน "
             "Sinopec ด้วยฟิล์ม Self-Cleaning — มีภาพแผงเดียวกันครึ่งเคลือบครึ่งไม่เคลือบให้ดูผลจริง และงานเคลือบตั้งแต่ในโรงงานผลิตป้าย")
S_TH_EYEBROW = "Case Study · เคลือบปกป้อง / Paint Coating"
S_TH_META = "เผยแพร่ ก.ย. 2026 · งานปี 2022–2023 โดยทีม Feibo (ประเทศจีน) ผู้พัฒนาวัตถุดิบของเรา"
S_TH_BODY = f"""  <article>
    <p>เคสนี้ไม่ใช่งานของทีมเราในไทย — เป็นงานของ <b>Feibo</b> (ฉางชา ประเทศจีน) ผู้พัฒนาและผลิตวัตถุดิบหลักที่เราใช้ใน <a href="/paintcoating">Paint Coating</a> เราขอภาพชุดนี้มาลงเพราะมันตอบคำถามที่ลูกค้าถามบ่อยที่สุดได้ในภาพเดียว: <b>เคลือบแล้วต่างจากไม่เคลือบจริงไหม</b></p>
{fig(S,1,'ช่างสองคนบนรถกระเช้าใช้ลูกกลิ้งเคลือบ Self-Cleaning บนแผงสีขาวข้างป้ายโลโก้ปั๊มน้ำมัน','หน้างานจริง: ทีม Feibo บนรถกระเช้า ลงฟิล์มด้วยลูกกลิ้งขนสั้นบนแผงสีขาวรอบป้ายโลโก้ — ขวดน้ำยาวางอยู่บนกระเช้า ลงบางทีละแนว',hero=True)}
    <p>หลังคาปั๊มน้ำมันคือหน้างานที่โหดกับผิวสีที่สุดแบบหนึ่งในเมือง — ไอน้ำมันจากหัวจ่าย เขม่าท่อไอเสียของรถที่เข้าออกทั้งวัน ฝุ่นถนน แล้วฝนก็พัดทั้งหมดนั้นให้ไหลลงแผงเป็นทาง แทบทุกสาขามีคราบแบบเดียวกัน และต้องจ้างคนขึ้นกระเช้าล้างเป็นรอบๆ</p>
    <section class="step">
      <h2><span class="n">01</span>แผงเดียวกัน ครึ่งเคลือบ ครึ่งไม่เคลือบ</h2>
      <p>แผงหลังคาชิ้นนี้ฝั่งหนึ่งเคลือบแล้ว อีกฝั่งยังไม่ได้เคลือบ แล้วโดนแดดฝนมาด้วยกัน — ภาพนี้ไม่ได้ล้าง ไม่ได้แต่งภาพ เส้นแบ่งคือขอบเขตที่เคลือบ</p>
{fig(S,2,'แผงหลังคาปั๊มน้ำมัน ครึ่งซ้ายเคลือบ Self-Cleaning สะอาดเรียบ ครึ่งขวาไม่เคลือบมีคราบน้ำไหลเป็นทาง','ซ้าย: เคลือบแล้ว แผงเรียบสะอาด · ขวา: ไม่ได้เคลือบ คราบน้ำและฝุ่นไหลเป็นทางชัดเจน — แผงชิ้นเดียวกัน โดนแดดฝนเท่ากัน')}
{fig(S,3,'ระยะใกล้แผงสีแดงที่ยังไม่เคลือบ เห็นคราบน้ำฝนไหลเป็นทางบนผิวสี','ระยะใกล้ฝั่งที่ไม่ได้เคลือบ — ฝุ่นที่ฝนพัดมากองแล้วแห้งเป็นทาง นี่คือคราบที่ทำให้ปั๊ม "ดูเก่า" ทั้งที่แผงยังไม่เสีย')}
    </section>
    <section class="step">
      <h2><span class="n">02</span>ลงบนแผงสีแดงเงา — ผิวที่ต้องบางที่สุด</h2>
      <p>แผงสีแดงเงาคือผิวที่โชว์ความผิดพลาดง่ายที่สุด ถ้าลงหนา ฟิล์มจะเกิดคราบรุ้งให้เห็นเวลาสะท้อนแสง ทีมงานจึงใช้ลูกกลิ้งขนสั้นไล่ทีละแนว คุมให้ฟิล์มบางสม่ำเสมอ ไม่ย้อนกลับไปกลิ้งซ้ำจุดที่เริ่มเซ็ตตัวแล้ว — หลักการเดียวกับที่เราเขียนไว้ในวิธีใช้บนหน้าสินค้า</p>
{fig(S,4,'ช่างสองคนใช้ลูกกลิ้งเคลือบแผงสีแดงเงาหลังคาปั๊มน้ำมันช่วงเย็น','แผงสีแดงเงาช่วงเย็น — ลูกกลิ้งขนสั้น ลงบางทีละแนว สองคนไล่ต่อกันเพื่อไม่ให้รอยต่อระหว่างแนวแห้งก่อน')}
{fig(S,6,'ช่างใช้ลูกกลิ้งเคลือบรอบป้ายโลโก้บนหลังคาปั๊มน้ำมัน มีรถกระเช้าอีกคันทำงานด้านหลัง','รอบป้ายโลโก้ — จุดที่ต้องลงด้วยมืออย่างระวัง ด้านหลังมีอีกทีมบนกระเช้าอีกคัน ในภาพปั๊มยังเปิดบริการระหว่างทำงาน')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>เคลือบตั้งแต่ในโรงงานผลิตป้าย — ก่อนขึ้นติดตั้ง</h2>
      <p>ภาพชุดสุดท้ายคือสิ่งที่เราอยากให้ลูกค้าโครงการดูให้ดี — ทีม Feibo เข้าไปเคลือบ<b>ตัวอักษรและแผงป้ายในโรงงานผู้ผลิตป้าย</b> ก่อนที่ป้ายจะถูกส่งไปติดตั้ง ทำบนพื้นโรงงาน ไม่ต้องใช้กระเช้า คุมสภาพแวดล้อมได้ ไม่ต้องลุ้นฝน และถูกกว่าการขึ้นไปทำบนหลังคาทีหลังมาก</p>
{fig(S,5,'ทีมงานเคลือบตัวอักษรป้ายและแผงสีแดงในโรงงานผลิตป้ายก่อนติดตั้ง','ในโรงงานผลิตป้าย — ตัวอักษรและแผงวางราบบนพื้น ลงฟิล์มก่อนขึ้นติดตั้ง วิธีที่คุ้มและคุมคุณภาพง่ายที่สุดสำหรับงานป้ายใหม่')}
      <p>ถ้าคุณเป็นผู้รับเหมาป้าย หรือกำลังจะติดแผง ACP ชุดใหม่ นี่คือจังหวะที่ควรเคลือบ — ตอนที่แผงยังอยู่ในโรงงานหรือยังไม่ขึ้นนั่งร้าน</p>
    </section>
    <section class="step">
      <h2><span class="n">📷</span>ภาพหน้างานเพิ่มเติมทั้งชุด</h2>
      {gallery_html(S, 8, "งานเคลือบหลังคาและป้ายปั๊มน้ำมัน Sinopec โดยทีม Feibo — ภาพหน้างานจริง")}
    </section>
  </article>
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/paintcoating">Paint Coating</a></div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
"""

S_EN_TITLE = "Coating Sinopec Fuel-Station Canopies and Signage — Self-Cleaning on the Hardest-to-Wash Painted Panels in Town"
S_EN_DESC = ("A project by Feibo, the developer of our Paint Coating raw material: red-and-white canopy panels and logo signage at "
             "Sinopec fuel stations coated with a self-cleaning film — including the same panel half-coated, half-uncoated as proof, "
             "and coating done inside the sign factory before installation")
S_EN_EYEBROW = "Case Study · Coatings / Paint Coating"
S_EN_META = "Published Sept 2026 · Work from 2022–2023 by the Feibo team (China), developer of our raw material"
S_EN_BODY = f"""  <article>
    <p>This case is not our own crew in Thailand — it is the work of <b>Feibo</b> (Changsha, China), the developer and producer of the core raw material in our <a href="/en/paintcoating">Paint Coating</a>. We asked for this photo set because it answers the question customers ask most, in a single picture: <b>is coated really different from uncoated?</b></p>
{fig(S,1,'Two applicators on a boom lift rolling self-cleaning coating onto white panels beside a fuel-station logo sign','On site: the Feibo crew on a boom lift, rolling the film onto the white panels around the logo with a short-nap roller — bottle on the platform, one thin pass at a time',hero=True)}
    <p>A fuel-station canopy is one of the harshest environments for paint in any city — fuel vapour from the pumps, exhaust soot from cars all day, road dust, and then rain pushing all of it down the panels in streaks. Almost every branch shows the same marks and pays a crew on a lift to wash them off, round after round.</p>
    <section class="step">
      <h2><span class="n">01</span>Same panel, half coated, half not</h2>
      <p>One side of this canopy panel had been coated, the other not yet, and both had taken the same sun and rain. Not washed, not retouched. The line is the edge of the coated area.</p>
{fig(S,2,'Fuel-station canopy panel — left half coated with self-cleaning film and clean, right half uncoated with water streaks','Left: coated, panel smooth and clean · Right: not coated, clear water and dust streaks — one panel, identical exposure')}
{fig(S,3,'Close-up of an uncoated red panel with rain streaks running down the painted surface','Close-up of the uncoated side — dust pushed into streaks by rain and left to dry. This is what makes a station look old while the panel itself is still fine')}
    </section>
    <section class="step">
      <h2><span class="n">02</span>Glossy red panels — the surface that needs the thinnest coat</h2>
      <p>Glossy red is the surface that shows mistakes fastest: apply too thick and the film shows a rainbow sheen in reflected light. So the crew works line by line with a short-nap roller, keeps the film thin and even, and never goes back over a spot that has started to set — the same rules we spell out in the how-to on the product page.</p>
{fig(S,4,'Two applicators rolling coating onto glossy red fuel-station canopy panels at dusk','Glossy red panels at dusk — short-nap roller, thin coat, one line at a time; two applicators work in sequence so the joins between lines never dry first')}
{fig(S,6,'Applicator rolling coating around a fuel-station logo sign with a second lift working behind','Around the logo — done carefully by hand; a second crew on another lift behind, with the station still serving customers in the photo')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>Coated inside the sign factory — before installation</h2>
      <p>The last set is the one we want project customers to look at closely — the Feibo crew went into the <b>sign manufacturer's factory</b> and coated the letters and panels before they shipped for installation. Done on the factory floor: no lift, controlled conditions, no watching the rain forecast, and far cheaper than going up onto the canopy afterwards.</p>
{fig(S,5,'Crew coating sign letters and red panels inside a sign-fabrication workshop before installation','Inside the sign factory — letters and panels laid flat on the floor, film applied before installation: the cheapest, most controllable way to do new signage')}
      <p>If you fabricate signs, or are about to install a new set of ACP panels, this is the moment to coat — while the panels are still in the factory or not yet on the scaffold.</p>
    </section>
    <section class="step">
      <h2><span class="n">📷</span>More Site Photos — the Whole Set</h2>
      {gallery_html(S, 8, "Sinopec fuel-station canopy and signage coating by the Feibo crew — site photo")}
    </section>
  </article>
  <div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/paintcoating">Paint Coating</a></div>
  <a class="back" href="/en/casestudy/">← Back to all case studies</a>
"""

# ─────────────────────────── CASE 2: RAIL ───────────────────────────
R = "feibo-rail-transit"
R_TH_TITLE = "รถไฟความเร็วสูง รถไฟใต้ดิน รถราง — เคลือบตัวถังที่ต้องล้างทุก 4,000 กม. ให้ล้างน้อยลง"
R_TH_DESC = ("โครงการของ Feibo ผู้พัฒนาวัตถุดิบ Paint Coating ของเรา บนตัวถังรถไฟความเร็วสูง รถไฟใต้ดิน และรถราง — "
             "ภาพหัวรถไฟที่แบ่งครึ่งด้วยเทป ฝั่งทำแล้วกับฝั่งยังไม่ทำ กระโปรงข้างรถไฟใต้ดินก่อน-หลัง และงานในโรงซ่อมบำรุงจริง")
R_TH_EYEBROW = "Case Study · เคลือบปกป้อง / Paint Coating"
R_TH_META = "เผยแพร่ ก.ย. 2026 · ภาพหน้างานจากทีม Feibo (ประเทศจีน) ผู้พัฒนาวัตถุดิบของเรา"
R_TH_BODY = f"""  <article>
    <p>สูตร Paint Coating ที่เรานำเข้าวัตถุดิบมา มีกลุ่มลูกค้าหลักกลุ่มหนึ่งคือ <b>ผู้ให้บริการระบบราง</b> ในจีน ที่ตัวถังรถไฟความเร็วสูงต้องเข้าล้างทุกๆ 4,000 กิโลเมตร ผิวสีดูดเขม่า ผงเหล็กจากราง ฟิล์มน้ำมัน และซากแมลงตลอดทาง ยิ่งล้างบ่อยยิ่งกัดสี และค่าล้างต่อรอบของขบวนรถทั้งขบวนไม่ใช่เงินเล็ก</p>
{fig(R,1,'หัวรถไฟความเร็วสูงสีขาวในโรงซ่อมบำรุง ผิวสีมีจุดคราบสกปรกกระจายทั่ว','หัวรถไฟความเร็วสูงในโรงซ่อมบำรุง — สภาพก่อนทำ ผิวสีขาวมีจุดคราบและซากแมลงกระจายทั่ว นี่คือหลังวิ่งมาไม่กี่พันกิโลเมตร',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>หัวรถไฟความเร็วสูง — แบ่งครึ่งด้วยเทป ทำฝั่งเดียว</h2>
      <p>ภาพที่เราชอบที่สุดในชุดนี้ ทีมงานติดเทปแบ่งกึ่งกลางหัวรถ แล้วทำเฉพาะฝั่งซ้าย (ล้างเชิงลึกแล้วลงฟิล์ม Self-Cleaning) ปล่อยฝั่งขวาไว้ตามสภาพเดิม — ผิวสีเดียวกัน แสงเดียวกัน ถ่ายในวินาทีเดียวกัน</p>
{fig(R,2,'หัวรถไฟความเร็วสูงแบ่งครึ่งด้วยเทปสีเหลือง ฝั่งซ้ายทำแล้วเรียบเงา ฝั่งขวายังไม่ทำมีจุดคราบทั่ว','ซ้ายของเทป: ทำแล้ว ผิวเรียบเงาสะอาด · ขวาของเทป: ยังไม่ทำ จุดคราบและซากแมลงเต็มผิว')}
{fig(R,3,'ระยะใกล้แนวเทปบนหัวรถไฟ ฝั่งซ้ายสะอาดเงา ฝั่งขวามีจุดคราบสีดำกระจาย','ซูมที่แนวเทป — ต่างกันแบบไม่ต้องอธิบาย ผิวฝั่งที่ทำแล้วเงาและลื่นจนสิ่งสกปรกไม่มีที่เกาะ')}
      <p>จุดที่อยากให้สังเกต: ฝั่งที่ทำแล้วไม่ได้แค่สะอาด ณ ตอนถ่าย แต่ผิวเปลี่ยนไป — ฟิล์ม Superhydrophilic + Anti-Static ทำให้ซากแมลงและเขม่าเกาะยากขึ้นตั้งแต่แรก และเมื่อเข้าเครื่องล้าง คราบหลุดด้วยน้ำเปล่าโดยไม่ต้องขัดแรง นี่คือกลไกที่ทำให้ "ล้างน้อยลง" ไม่ใช่แค่ "ล้างครั้งนี้สะอาด"</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>รถไฟใต้ดิน — กระโปรงข้างและตัวตู้</h2>
      <p>รถไฟใต้ดินเจอปัญหาคนละแบบ: ไม่มีแดดช่วย แต่มีผงเหล็กจากล้อและเบรกที่ละเอียดมาก เกาะผิวสีชั้นล่างของตู้จนออกสีน้ำตาลหม่น ภาพคู่นี้คือกระโปรงข้างชิ้นเดียวกันก่อนและหลังทำ</p>
{fig(R,4,'กระโปรงข้างรถไฟใต้ดินก่อนทำ ผิวสีขาวออกน้ำตาลหม่นจากผงเหล็กและคราบน้ำมัน','ก่อนทำ — กระโปรงข้างสีขาวออกน้ำตาลหม่นทั้งชิ้น ผงเหล็กและฟิล์มน้ำมันฝังลงในผิวสี')}
{fig(R,5,'กระโปรงข้างรถไฟใต้ดินชิ้นเดียวกันหลังทำ ผิวสีขาวสะอาด','หลังทำ — ชิ้นเดียวกัน ล้างเชิงลึกแล้วลงฟิล์ม กลับมาขาวเหมือนสีเดิมโดยไม่ต้องทำสีใหม่')}
{fig(R,6,'ตู้รถไฟใต้ดินสองตู้ติดกัน ตู้ซ้ายมีคราบเหลืองสะสม ตู้ขวาขาวสะอาด','สองตู้ติดกัน สีผิวต่างกันชัด — ตู้ซ้ายคราบเหลืองสะสม ตู้ขวาขาวสะอาด (ภาพเทียบจากทีมงานหน้างาน)')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>รถราง — สีตัวถังคือหน้าตาของบริการ</h2>
      <p>รถรางในเมืองวิ่งช้ากว่าแต่โดนมากกว่า — ฝุ่นถนน ควันรถ และมือคนที่สัมผัสทุกวัน สีตัวถังคือสิ่งแรกที่ผู้โดยสารเห็น ทีมงานเข้าทำในโรงจอดช่วงที่รถพักจากการให้บริการ</p>
{fig(R,7,'หัวรถรางสีเขียวขาวในโรงจอด ทีมงานกำลังทำงานที่กระจกหน้า','รถรางในโรงจอด — ทีมงานทำที่หัวรถและกระจกหน้า รถอีกคันรอคิวด้านหลัง')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>แล้วเกี่ยวอะไรกับงานในไทย</h2>
      <p>รถไฟความเร็วสูงในไทยยังอยู่ระหว่างก่อสร้าง แต่<b>รถบัสประจำทาง รถทัวร์ รถขนส่งของบริษัทโลจิสติกส์ รถบรรทุกฟลีท</b> เจอปัญหาเดียวกันทุกข้อ — ล้างบ่อยไม่ไหว ล้างแล้วสีด้าน ค่าล้างต่อคันคูณจำนวนคันแล้วเป็นเงินก้อนใหญ่ทุกเดือน สูตรที่ผ่านงานระดับรถไฟความเร็วสูงมาแล้ว ใช้กับฟลีทรถในไทยได้ทันที ปรึกษาเราก่อนได้ทางแชท</p>
    </section>
    <section class="step">
      <h2><span class="n">📷</span>ภาพหน้างานเพิ่มเติมทั้งชุด</h2>
      {gallery_html(R, 11, "งานเคลือบตัวถังรถไฟความเร็วสูง รถไฟใต้ดิน และรถราง โดยทีม Feibo — ภาพหน้างานจริง")}
    </section>
  </article>
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/paintcoating">Paint Coating</a></div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
"""

R_EN_TITLE = "High-Speed Rail, Metro and Trams — Coating Train Bodies That Get Washed Every 4,000 km So They Need Washing Less"
R_EN_DESC = ("A project by Feibo, the developer of our Paint Coating raw material, on high-speed train, metro and tram bodies — "
             "a train nose split down the middle with tape, treated side vs untreated side, metro skirt panels before and after, and real depot work")
R_EN_EYEBROW = "Case Study · Coatings / Paint Coating"
R_EN_META = "Published Sept 2026 · Site photos from the Feibo team (China), developer of our raw material"
R_EN_BODY = f"""  <article>
    <p>The Paint Coating formulation whose raw material we import has one of its main customer groups in <b>rail operators</b> in China, where high-speed train bodies go through the wash every 4,000 kilometres. The paint collects soot, iron dust from the rails, oil film and insect remains the whole way; every wash wears the paint a little more, and washing a whole trainset is not cheap.</p>
{fig(R,1,'Nose of a white high-speed train in a maintenance depot, paint speckled with dirt','A high-speed train nose in the depot — before treatment, the white paint speckled with grime and insect remains. This is after only a few thousand kilometres',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>The train nose — taped down the middle, one side treated</h2>
      <p>Our favourite picture in the set. The crew taped a line down the centre of the nose and treated only the left side (deep clean, then the self-cleaning film), leaving the right side as it was — same paint, same light, one photo.</p>
{fig(R,2,'High-speed train nose split by yellow tape, left side treated and glossy, right side untreated and speckled','Left of the tape: treated, smooth and glossy · Right of the tape: untreated, speckled with grime and insect remains')}
{fig(R,3,'Close-up of the tape line on the train nose, left side clean and glossy, right side with dark specks','Close-up on the tape line — no explanation needed. The treated surface is glossy and slick, with nothing for dirt to hold on to')}
      <p>Worth noticing: the treated side is not just clean at the moment of the photo — the surface has changed. The superhydrophilic, anti-static film makes insects and soot harder to stick in the first place, and in the wash the residue lifts with plain water instead of scrubbing. That is the mechanism behind "washing less", not just "clean this time".</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>Metro — skirt panels and car bodies</h2>
      <p>Metro trains face a different problem: no sunlight to help, but very fine iron dust from wheels and brakes that settles into the lower paint and turns it a dull brown. This pair is the same skirt panel before and after treatment.</p>
{fig(R,4,'Metro train skirt panel before treatment, white paint turned dull brown by iron dust and oil','Before — the white skirt panel a dull brown across the whole piece, iron dust and oil film bedded into the paint')}
{fig(R,5,'The same metro skirt panel after treatment, white and clean','After — the same panel, deep-cleaned and coated, back to its original white without repainting')}
{fig(R,6,'Two adjacent metro cars, the left one with a yellowed surface, the right one clean white','Two adjacent cars, clearly different surfaces — yellowed build-up on the left car, clean white on the right (comparison photo from the site crew)')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>Trams — the paintwork is the face of the service</h2>
      <p>City trams run slower but take more: road dust, traffic fumes and hands on the body every day. The paint is the first thing a passenger sees. The crew worked in the depot while the vehicles were out of service.</p>
{fig(R,7,'Green and white tram in a depot with the crew working at the windscreen','Tram in the depot — the crew at the nose and windscreen, the next vehicle waiting behind')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>What this means for work in Thailand</h2>
      <p>High-speed rail in Thailand is still under construction, but <b>city buses, coaches, logistics fleets and truck fleets</b> face every one of the same problems — can't wash often enough, washing dulls the paint, and the per-vehicle wash cost multiplied by the fleet is real money every month. A formulation proven at high-speed-rail level goes straight onto a Thai fleet. Ask us in chat before you start.</p>
    </section>
    <section class="step">
      <h2><span class="n">📷</span>More Site Photos — the Whole Set</h2>
      {gallery_html(R, 11, "High-speed rail, metro and tram body coating by the Feibo crew — site photo")}
    </section>
  </article>
  <div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/paintcoating">Paint Coating</a></div>
  <a class="back" href="/en/casestudy/">← Back to all case studies</a>
"""

def transplant(src_path, out_path, slug, title, desc, eyebrow, h1, meta, body, og_img):
    h = open(src_path, encoding="utf-8").read()
    h = h.replace(SRC, slug)
    h = re.sub(r"<title>.*?</title>", f"<title>{title} | Case Study LucernaPro</title>", h, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title} | Case Study LucernaPro">', h, flags=re.S)
    h = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{og_img}">', h, flags=re.S)
    i = h.find('<main class="wrap">'); j = h.find("</main>")
    crumb = re.search(r'<p class="crumb">.*?</p>', h[i:j], flags=re.S).group(0)
    new_main = ('<main class="wrap">\n  ' + crumb + "\n"
                f'  <span class="eyebrow">{eyebrow}</span>\n'
                f"  <h1>{h1}</h1>\n"
                f'  <p class="meta">{meta}</p>\n' + body)
    h = h[:i] + new_main + h[j:]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(h)
    print("built:", out_path)

if __name__ == "__main__":
    for slug, th, en in [
        (S, (S_TH_TITLE, S_TH_DESC, S_TH_EYEBROW, S_TH_META, S_TH_BODY), (S_EN_TITLE, S_EN_DESC, S_EN_EYEBROW, S_EN_META, S_EN_BODY)),
        (R, (R_TH_TITLE, R_TH_DESC, R_TH_EYEBROW, R_TH_META, R_TH_BODY), (R_EN_TITLE, R_EN_DESC, R_EN_EYEBROW, R_EN_META, R_EN_BODY)),
    ]:
        og = f"https://www.lucernapro.com/img/post/{slug}-h1.webp"
        transplant(os.path.join(ROOT, "post", SRC, "index.html"), os.path.join(ROOT, "post", slug, "index.html"),
                   slug, th[0], th[1], th[2], th[0], th[3], th[4], og)
        transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"), os.path.join(ROOT, "en", "post", slug, "index.html"),
                   slug, en[0], en[1], en[2], en[0], en[3], en[4], og)
