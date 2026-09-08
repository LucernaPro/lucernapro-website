# -*- coding: utf-8 -*-
"""
build_boundgravel_restroom_post.py — เคส BoundGravel พื้นชานและบันไดอาคารห้องน้ำกลางแจ้ง
ภาพส่งจากลูกค้าผ่าน Pist 8 ก.ย. 2026 พร้อมข้อความ "ใช้งานได้ดีครับ" (ไม่ระบุที่ตั้ง ไม่ระบุผู้ทำ)
เคสนี้เปิดเป็นโพสต์ของตัวเอง ตามกติกา: งานที่ลูกค้าส่งมาแยกเคส ไม่รวมกับแกลเลอรีรวมบนหน้า /boundgravel
วิธี: chrome-transplant จากโพสต์ solar เหมือน build_laundry_pu_floor_post.py — TH+EN
รูป: /img/post/{slug}-h*.webp (narrative) + -g*.webp (800x800)
รัน: python3 tools/build_boundgravel_restroom_post.py (จาก root ของ repo)
"""
import os, re
from PIL import Image, ImageOps, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "boundgravel-outdoor-restroom-deck"
UP = "/mnt/user-data/uploads"

NARR = [
 ("800862922_1112276197811009_3780747901353162126_n.jpg", 1),  # หน้าตรง แดดจัด ชาน+บันได
 ("800153515_1083628604069121_3879200177609206719_n.jpg", 2),  # มุมเฉียง เห็นบันไดสามขั้น
 ("799264475_2133053484086028_8754952897157643877_n.jpg", 3),  # ฝั่งชาย หลังฝน ดินโคลนรอบ
 ("800945955_1629457598753020_4765865607264742228_n.jpg", 4),  # ฝั่งหญิง หลังฝน พื้นชาน
 ("800260200_1050863831068675_501774559677976284_n.jpg", 5),  # ฝั่งชาย ขอบชานกับหินโรยรอบ
 ("799724571_39477782391820533_1766341719879367490_n.jpg", 6),  # ฝั่งหญิง แดด ขอบชาน
 ("800540423_3614873568662958_5631985738558491897_n.jpg", 7),  # ข้อความลูกค้า "ใช้งานได้ดีครับ"
]
GAL = [
 "800862922_1112276197811009_3780747901353162126_n.jpg",
 "800153515_1083628604069121_3879200177609206719_n.jpg",
 "799264475_2133053484086028_8754952897157643877_n.jpg",
 "800945955_1629457598753020_4765865607264742228_n.jpg",
 "800260200_1050863831068675_501774559677976284_n.jpg",
 "799724571_39477782391820533_1766341719879367490_n.jpg",
]
def sharpen(im):
    return im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=60, threshold=2))

def prep_images():
    out = os.path.join(ROOT, "img", "post")
    for src, k in NARR:
        im = ImageOps.exif_transpose(Image.open(os.path.join(UP, src))).convert("RGB")
        w, h = im.size
        if max(w, h) > 1600:
            r = 1600 / max(w, h); im = im.resize((round(w * r), round(h * r)), Image.LANCZOS)
        sharpen(im).save(os.path.join(out, f"{SLUG}-h{k}.webp"), "WEBP", quality=88, method=6)
    for i, src in enumerate(GAL, 1):
        im = ImageOps.exif_transpose(Image.open(os.path.join(UP, src))).convert("RGB")
        s = min(im.size); w, h = im.size
        im = im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
        if s > 800: im = im.resize((800, 800), Image.LANCZOS)
        sharpen(im).save(os.path.join(out, f"{SLUG}-g{i:02d}.webp"), "WEBP", quality=85, method=6)

if os.path.isdir(UP):
    prep_images()

def dims(name):
    return Image.open(os.path.join(ROOT, "img", "post", name + ".webp")).size

def fig(k, alt, cap, hero=False):
    w, h = dims(f"{SLUG}-h{k}")
    cls = ' class="hero"' if hero else ''
    icls = ' class="tall"' if h > w else ''
    lazy = '' if hero else ' loading="lazy"'
    return (f'    <figure{cls}><img{icls} src="/img/post/{SLUG}-h{k}.webp" alt="{alt}"{lazy} '
            f'width="{w}" height="{h}"><figcaption>{cap}</figcaption></figure>\n')

GRID_STYLE = ("display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));"
              "gap:10px;margin-top:26px")

def gallery_html(alt_prefix):
    imgs = "".join(
        f'<img src="/img/post/{SLUG}-g{i:02d}.webp" alt="{alt_prefix} {i:02d}" loading="lazy" '
        f'width="800" height="800" style="border-radius:10px;border:1px solid var(--line)">\n'
        for i in range(1, len(GAL) + 1))
    return '<div style="' + GRID_STYLE + '">\n' + imgs + '</div>'

# ─────────────────────────── TH ───────────────────────────
TH_TITLE = "ชานและบันไดห้องน้ำกลางแจ้ง พื้นทรายล้าง BoundGravel — ลูกค้าส่งภาพกลับมาพร้อมคำว่า “ใช้งานได้ดีครับ”"
TH_DESC = ("ภาพงานจริงจากลูกค้า: อาคารห้องน้ำกลางแจ้งท่ามกลางต้นไม้ ชานหน้าอ่างล้างมือและบันไดทางขึ้นเป็นพื้นทรายล้างไม่ใช้ปูน BoundGravel — "
           "ทำไมพื้นพรุนระบายน้ำเข้ากับจุดที่เปียกทั้งวัน บันไดทำได้เฉพาะหน้าขั้น และเรื่องสีหินที่ควรรู้ก่อนเลือก")
TH_EYEBROW = "Case Study · BoundGravel พื้นทรายล้างไม่ใช้ปูน"
TH_META = "เผยแพร่ ก.ย. 2026 · ภาพจากลูกค้าหลังใช้งานจริง"

TH_BODY = f"""  <article>
    <p>ลูกค้าส่งภาพชุดนี้กลับมาพร้อมข้อความสั้นๆ ว่า <b>“ใช้งานได้ดีครับ”</b> — เป็นอาคารห้องน้ำกลางแจ้งหลังหนึ่งตั้งอยู่ท่ามกลางต้นไม้ โครงเหล็ก หลังคาเมทัลชีทสลับแผ่นใส ผนังระแนงลายไม้ อ่างล้างมือเรียงอยู่ด้านนอกอาคาร และส่วนที่เกี่ยวกับเราคือ <b>พื้นชานหน้าอ่างล้างมือกับบันไดทางขึ้น</b> ซึ่งฉาบด้วย<a href="/boundgravel">BoundGravel น้ำยาทรายล้างไม่ใช้ปูน</a> เราไม่ได้อยู่หน้างาน จึงเล่าเฉพาะสิ่งที่เห็นในภาพและสิ่งที่ระบบนี้เป็น</p>
{fig(1,'อาคารห้องน้ำกลางแจ้งหน้าตรง แดดจัด อ่างล้างมือสี่อ่างเรียงกลางอาคาร ประตูไม้ซ้ายขวา พื้นชานและบันไดสามขั้นเป็นทรายล้างโทนอ่อน ป่าไผ่ด้านหลัง','หน้าตรงของอาคาร — ชานหน้าอ่างล้างมือและบันไดสามขั้นเป็นพื้นทรายล้าง BoundGravel โทนอ่อน',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>จุดที่เปียกทั้งวัน — พื้นต้องปล่อยน้ำผ่าน ไม่ใช่กักไว้</h2>
      <p>ชานหน้าห้องน้ำแบบนี้คือพื้นที่ที่โดนน้ำหลายทางพร้อมกัน: น้ำจากอ่างล้างมือที่ตั้งอยู่กลางแจ้ง ฝนที่สาดเข้าใต้ชายคา และรองเท้าเปื้อนดินของคนที่เดินขึ้นมา พื้นทรายล้างแบบผสมปูนจะอุ้มน้ำและมีน้ำเจิ่งเป็นแอ่งตามจุดที่เทไม่ได้ระดับ ส่วน BoundGravel เป็นระบบ <b>Resin Bound</b> — น้ำยาเคลือบผิวหินทุกเม็ดแล้วเชื่อมกันเป็นผืนเดียวโดยไม่มีปูนอุดช่องว่าง <b>น้ำจึงซึมผ่านลงพื้นด้านล่างได้</b> ในภาพหลังฝนจะเห็นดินโคลนและน้ำขังรอบอาคาร แต่บนผืนชานไม่มีแอ่งน้ำให้เห็น</p>
{fig(3,'มุมด้านข้างฝั่งห้องน้ำชาย หลังฝนตก ดินรอบอาคารเป็นโคลนและมีน้ำขัง พื้นชานทรายล้างโทนอ่อนใต้ชายคา อ่างล้างมือสามอ่างและกระจก','ฝั่งห้องน้ำชายหลังฝน — ดินรอบอาคารเป็นโคลน ผืนชานทรายล้างใต้ชายคาไม่มีแอ่งน้ำขัง')}
{fig(4,'มุมด้านข้างฝั่งห้องน้ำหญิง พื้นชานทรายล้างโทนอ่อนเปียกจากฝน ทางเดินดินมีน้ำขังด้านหน้า ผนังระแนงลายไม้ อ่างล้างมือสี่อ่าง','ฝั่งห้องน้ำหญิงมุมเดียวกัน — ผิวชานเปียกจากฝนแต่ไม่ขังเป็นแอ่ง ต่างจากทางเดินดินด้านหน้า')}
    </section>
    <section class="step">
      <h2><span class="n">02</span>บันได — ฉาบได้เฉพาะหน้าขั้น ลูกตั้งปล่อยเป็นปูน</h2>
      <p>BoundGravel รุ่นนี้ออกแบบมาสำหรับ<b>พื้นแนวนอนเท่านั้น</b> ฉาบแนวตั้งไม่ได้ ในภาพจะเห็นว่างานนี้ทำถูกตามข้อนี้: หน้าขั้นบันไดทั้งสามขั้นเป็นทรายล้างผืนเดียวกับชาน ส่วน<b>ลูกตั้ง (หน้าตั้งของขั้น) ปล่อยเป็นปูนทาสีขาว</b> ทำให้ขอบขั้นชัดเจน มองเห็นระดับได้ง่ายเวลาเดินขึ้นลงตอนเปียก และไม่ต้องฝืนฉาบแนวตั้งซึ่งรุ่นนี้ทำไม่ได้</p>
{fig(2,'มุมเฉียงของอาคารห้องน้ำ เห็นบันไดสามขั้นหน้าขั้นเป็นทรายล้างโทนอ่อน ลูกตั้งสีขาว ประตูไม้ ป้ายสัญลักษณ์ชายบนแผ่นระแนง ป่าไผ่ด้านหลัง','บันไดสามขั้น — หน้าขั้นเป็นทรายล้าง ลูกตั้งเป็นปูนสีขาว ตรงกับกติกา “แนวนอนเท่านั้น” ของรุ่นนี้')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>ขอบชานกับหินโรยรอบ — ระบบเดียวกันเลือกหน้าที่คนละอย่าง</h2>
      <p>รอบชานในหลายภาพมีการโรยหินคละไว้บนดิน ตรงนั้นเป็นหินหลวมธรรมดา ไม่ได้ผ่านน้ำยา และไม่จำเป็นต้องผ่าน — <b>ผืนที่ต้องรับการเดิน รับน้ำ และต้องล้างได้</b>คือชานกับบันได จึงเป็น BoundGravel ส่วนที่เหลือปล่อยเป็นหินโรยเพื่อไม่ให้ดินเลอะขึ้นมา นี่คือการแบ่งงบที่ถูกจุด: น้ำยาทำงานตรงที่พื้นต้องแข็ง ที่เหลือใช้หินเปล่า</p>
{fig(5,'ฝั่งห้องน้ำชาย พื้นชานทรายล้างโทนอ่อนใต้ชายคา ขอบชานเป็นปูน ด้านนอกโรยหินคละบนดิน อ่างล้างมือสี่อ่างและกระจกบานใหญ่','ขอบชานฝั่งชาย — ผืนชานเป็น BoundGravel ด้านนอกเป็นหินโรยธรรมดาบนดิน')}
{fig(6,'ฝั่งห้องน้ำหญิง แดดจัด พื้นชานทรายล้างโทนอ่อน ขอบชานล้อมด้วยหินโรยสีเทา ผนังระแนงลายไม้ยาว ป้ายสัญลักษณ์หญิง ต้นไม้ดอกชมพูด้านหลัง','ฝั่งหญิงวันแดดจัด — เห็นผืนชานกับแนวหินโรยรอบชัดๆ')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>เรื่องสีหิน — พูดตรงๆ เหมือนบนหน้าสินค้า</h2>
      <p>งานนี้ใช้หินโทนอ่อน ครีมออกเทา เข้ากับผนังระแนงลายไม้และตัวอาคารสีขาว ดูสว่างสะอาดตา แต่มีเรื่องที่เราเขียนไว้บนหน้าสินค้าและต้องย้ำอีกครั้ง: <b>ห้ามใช้หินสีขาวแท้</b> เพราะโดนแดดแล้วงานจะออกเหลือง โทนอ่อนที่ปลอดภัยคือครีม เบจ หรือเหลืองทอง ส่วนโทนดำซ่อนคราบเก่งที่สุดสำหรับจุดที่รองเท้าเปื้อนดินเดินขึ้นบ่อยๆ หินโทนอ่อนสวยแต่ต้องยอมรับว่าโชว์รอยดินไวกว่า — ล้างน้ำได้เพราะพื้นปล่อยน้ำผ่าน</p>
{fig(7,'ภาพรวมหกภาพของอาคารห้องน้ำที่ลูกค้าส่งมา พร้อมข้อความในแชทว่า ใช้งานได้ดีครับ','ข้อความและภาพชุดที่ลูกค้าส่งมาหลังใช้งาน')}
    </section>
    <section class="step">
      <h2><span class="n">05</span>สรุปสำหรับชาน ทางเดิน และพื้นรอบอาคารกลางแจ้ง</h2>
      <p><b>พื้นที่เปียกบ่อยและอยากให้แห้งไว</b> → พื้นพรุนแบบ BoundGravel น้ำผ่านลงไม่ขัง · <b>บันได</b> → ฉาบเฉพาะหน้าขั้น ลูกตั้งปล่อยเป็นปูนหรือทาสี · <b>สีหิน</b> → ครีม เบจ เหลืองทอง หรือดำ ห้ามขาวแท้ · <b>ก่อนคลุก</b> → ล้างหินแล้วตากให้แห้งสนิท ขั้นนี้ตัดสินอายุงานทั้งหมด</p>
      <p>ปริมาณ: น้ำยา 5 kg คลุกหินได้ 100 kg ฉาบหนาราว 1 ซม. ได้ประมาณ 8–10 ตร.ม. — ส่งขนาดพื้นและรูปหน้างานมาทางแชทเพจ เราคำนวณจำนวนน้ำยาให้ พร้อมบอกตรงๆ ว่าจุดไหนใช้รุ่นนี้ได้และจุดไหนไม่ควร</p>
{gallery_html('ชานและบันไดห้องน้ำกลางแจ้ง พื้นทรายล้าง BoundGravel — ภาพจากลูกค้า')}
    </section>
  </article>
"""

# ─────────────────────────── EN ───────────────────────────
EN_TITLE = "An Outdoor Restroom Deck and Steps in BoundGravel — the Customer Sent the Photos Back With “Works Well”"
EN_DESC = ("Real photos from a customer: an outdoor restroom block among the trees, with the deck in front of the wash basins and the entry steps done in BoundGravel cement-free resin-bound gravel — "
           "why a permeable floor suits a spot that gets wet all day, why the steps are treads only, and what to know about gravel colour before choosing")
EN_EYEBROW = "Case Study · BoundGravel resin-bound gravel"
EN_META = "Published Sep 2026 · Customer photos after use"

EN_BODY = f"""  <article>
    <p>A customer sent this set of photos back with a short message — <b>“works well”</b>. It is an outdoor restroom block set among trees: steel frame, metal roof with clear panels, wood-look slatted screens, wash basins in a row on the outside of the building. The part that concerns us is the <b>deck in front of the basins and the entry steps</b>, which are finished in <a href="/en/boundgravel">BoundGravel, our cement-free resin-bound gravel binder</a>. We were not on site, so this tells only what the photos show and what the system is.</p>
{fig(1,'Outdoor restroom block seen head-on in bright sun, four wash basins in the middle, timber doors left and right, the deck and three steps in light-toned bound gravel, bamboo forest behind','Head-on view — the deck in front of the basins and the three steps are BoundGravel in a light gravel',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>A spot that gets wet all day — the floor has to let water through, not hold it</h2>
      <p>A deck like this takes water from several directions at once: the outdoor basins, rain blowing in under the eaves, and muddy shoes coming up from the ground. A cement-based gravel wash holds water and ponds wherever the pour isn't level. BoundGravel is a <b>resin-bound</b> system — the binder coats every stone and bonds them into one slab with no cement filling the gaps, so <b>water drains straight through to the ground below</b>. In the after-rain photos the soil around the building is mud with standing water; on the deck itself there is no puddle to be seen.</p>
{fig(3,'Side view of the men\'s side after rain, mud and standing water on the ground around the building, the light-toned bound-gravel deck under the eaves, three basins and mirrors','Men\'s side after rain — mud around the building, no standing water on the bound-gravel deck under the eaves')}
{fig(4,'Side view of the women\'s side, the light-toned bound-gravel deck wet from rain, standing water on the dirt path in front, wood-look slatted screen, four basins','Women\'s side from the same angle — the deck surface is wet from rain but not ponding, unlike the dirt path in front')}
    </section>
    <section class="step">
      <h2><span class="n">02</span>The steps — treads only; the risers stay concrete</h2>
      <p>This grade of BoundGravel is for <b>horizontal surfaces only</b>; it cannot be trowelled vertically. The photos show the job done right on that point: the treads of all three steps are the same bound gravel as the deck, and the <b>risers are left as white-painted concrete</b>. That gives a clear edge to each step, easy to read when wet, and avoids forcing a vertical application this grade can't do.</p>
{fig(2,'Three-quarter view of the restroom block, three steps with light-toned bound-gravel treads and white risers, timber doors, a men\'s pictogram on the slatted panel, bamboo behind','Three steps — bound-gravel treads, white concrete risers, exactly as the “horizontal only” rule for this grade requires')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>The deck edge and the loose gravel around it — one material, two different jobs</h2>
      <p>In several photos there is loose mixed gravel spread on the soil around the deck. That is plain loose stone, not bound, and it doesn't need to be — <b>the surface that has to take foot traffic, water and washing</b> is the deck and the steps, so that is BoundGravel; the rest is loose gravel to keep the mud down. It's the right way to spend the budget: the binder goes where the floor must be solid, bare stone everywhere else.</p>
{fig(5,'Men\'s side, light-toned bound-gravel deck under the eaves, concrete deck edge, loose mixed gravel on the soil outside, four basins and a large mirror','Deck edge on the men\'s side — BoundGravel on the deck, plain loose gravel on the soil outside')}
{fig(6,'Women\'s side in bright sun, light-toned bound-gravel deck, the edge bordered by grey loose gravel, a long wood-look slatted screen, women\'s pictogram, pink-flowering tree behind','Women\'s side on a sunny day — the deck and the ring of loose gravel around it, clearly seen')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>Gravel colour — said plainly, as on the product page</h2>
      <p>This job uses a light gravel, cream leaning grey, which suits the wood-look screens and the white building and reads bright and clean. But there is a rule on the product page worth repeating: <b>never use pure white stone</b> — it yellows in sun. Safe light tones are cream, beige and golden yellow; black hides dirt best where muddy shoes come up often. A light gravel is handsome but will show mud marks sooner — and it hoses clean, because the floor lets water through.</p>
{fig(7,'Collage of six photos of the restroom block sent by the customer, with a chat message in Thai saying it works well','The message and photo set the customer sent after use')}
    </section>
    <section class="step">
      <h2><span class="n">05</span>In short, for decks, paths and ground around outdoor buildings</h2>
      <p><b>Often wet, want it to dry fast</b> → a permeable floor like BoundGravel, water goes through, nothing ponds · <b>Steps</b> → treads only; leave risers as concrete or paint · <b>Gravel colour</b> → cream, beige, golden yellow or black; never pure white · <b>Before mixing</b> → wash the stone and dry it completely; this step decides the life of the whole job.</p>
      <p>Quantities: 5 kg of binder mixes 100 kg of stone, about 8–10 m² at roughly 1 cm thick — send the floor size and site photos via chat and we will work out the binder needed and tell you straight where this grade fits and where it doesn't.</p>
{gallery_html('Outdoor restroom deck and steps in BoundGravel resin-bound gravel — customer photos')}
    </section>
  </article>
"""

def transplant(src_path, out_path, title, desc, eyebrow, meta, body, og_img):
    h = open(src_path, encoding="utf-8").read()
    h = h.replace(SRC, SLUG)
    h = re.sub(r"<title>.*?</title>", f"<title>{title} | Case Study LucernaPro</title>", h, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title} | Case Study LucernaPro">', h, flags=re.S)
    h = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{og_img}">', h, flags=re.S)
    i = h.find('<main class="wrap">'); j = h.find("</main>")
    crumb = re.search(r'<p class="crumb">.*?</p>', h[i:j], flags=re.S).group(0)
    new_main = ('<main class="wrap">\n  ' + crumb + "\n"
                f'  <span class="eyebrow">{eyebrow}</span>\n'
                f"  <h1>{title}</h1>\n"
                f'  <p class="meta">{meta}</p>\n' + body)
    h = h[:i] + new_main + h[j:]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(h)
    print("built:", out_path)

if __name__ == "__main__":
    og = f"https://www.lucernapro.com/img/post/{SLUG}-h1.webp"
    transplant(os.path.join(ROOT, "post", SRC, "index.html"),
               os.path.join(ROOT, "post", SLUG, "index.html"),
               TH_TITLE, TH_DESC, TH_EYEBROW, TH_META, TH_BODY, og)
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"),
               os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN_TITLE, EN_DESC, EN_EYEBROW, EN_META, EN_BODY, og)
