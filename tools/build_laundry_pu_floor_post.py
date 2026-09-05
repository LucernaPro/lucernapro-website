# -*- coding: utf-8 -*-
"""
build_laundry_pu_floor_post.py — เคสสีทาพื้น PU (ระบบ 2K จากหน้า /epoxycoating) สี RAL 7040 ร้านสะดวกซัก
ภาพส่งจาก Pist 5 ก.ย. 2026 (ไม่มี watermark/สถานที่ — ไม่ระบุที่ตั้ง ไม่ระบุผู้ทำ)
วิธี: chrome-transplant จากโพสต์ solar เหมือน build_deepseal_chedi_post.py — TH+EN
รูป: /img/post/{slug}-h*.webp (narrative, ไม่ upscale — ต้นฉบับกว้าง 1280) + -g*.webp (800x800)
รัน: python3 tools/build_laundry_pu_floor_post.py (จาก root ของ repo)
"""
import os, re
from PIL import Image, ImageOps, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "laundromat-pu-floor-ral7040"
UP = "/mnt/user-data/uploads"

NARR = [
 ("F5946B28-6463-4D64-8E6D-C8CABC0B847C.jpeg", 1),  # มุมกว้าง หน้าร้านเปิดโล่ง แดดส่องถึงพื้น
 ("8D1CF43C-6063-4046-9D2C-D94E341E20E4.jpeg", 2),  # พื้นระยะใกล้ + ขอบฐานเครื่อง
 ("64066AB2-5893-480B-A446-A159F178B006.jpeg", 3),  # ระเบียงหน้าร้านใต้หลังคา แดดเต็ม
 ("D0906CAA-856E-4ED1-BB9E-A8AE2BB19E1B.jpeg", 4),  # ฐานยกเครื่องอบ + โซนเปิด
 ("AB7572DA-F32E-4034-BAB8-A4BBAA69B426.jpeg", 5),  # โต๊ะนั่งรอบนพื้น
]
GAL = [
 "C614C927-8BFE-497C-A35B-22BFB19A2BC2.jpeg",
 "F70693B6-82E8-4107-94AE-8503DB30D157.jpeg",
 "9892C77F-183D-4518-977A-F9B01CCF0680.jpeg",
 "CF0E55FD-5555-4B21-8A01-F88810E14FCE.jpeg",
 "7DF71AF1-8AA8-4F2B-ABB7-83BABFBBAEDD.jpeg",
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
TH_TITLE = "พื้นร้านสะดวกซัก สีทาพื้น PU เฉด RAL 7040 — พื้นเปิดโล่งที่โดนแดดทุกวัน เลยเลือกสาย PU"
TH_DESC = ("ภาพงานจริง: ร้านสะดวกซักหน้าร้านเปิดโล่ง แดดส่องถึงพื้นทั้งวัน ทาด้วยสีทาพื้น PU ระบบสองส่วนผสมสั่งผลิตเฉด RAL 7040 เทาอ่อน — "
           "ทำไมงานแบบนี้เลือก PU ไม่ใช่ Epoxy, ฐานยกเครื่องและระเบียงหน้าร้านทาต่อเนื่องในระบบเดียว และเรื่องผิวที่ต้องพูดตรงๆ ก่อนสั่ง")
TH_EYEBROW = "Case Study · สีทาพื้น / Epoxy-PU"
TH_META = "เผยแพร่ ก.ย. 2026 · ภาพงานจริงหลังทาเสร็จ"

TH_BODY = f"""  <article>
    <p>ร้านสะดวกซักคือพื้นที่ใช้งานหนักแบบเงียบๆ — เครื่องซักเครื่องอบตั้งเรียง คนเดินเข้าออกทั้งวัน น้ำและผงซักฟอกหยดลงพื้นเป็นประจำ และร้านแบบนี้ส่วนใหญ่<b>หน้าร้านเปิดโล่ง แดดส่องถึงพื้นทุกวัน</b> เคสนี้ทาด้วย<a href="/epoxycoating">สีทาพื้น PU ระบบสองส่วนผสม</a>ของเรา สั่งผลิตเฉด <b>RAL 7040</b> (เทาอ่อนโทนเย็น) ภาพชุดนี้คือหลังทาเสร็จ</p>
{fig(1,'ร้านสะดวกซักหน้าร้านเปิดโล่ง พื้นสีเทา RAL 7040 เงาสะท้อนแสงแดดที่ส่องผ่านราวระเบียง เครื่องซักเรียงชิดผนังซ้าย เครื่องอบซ้อนสองชั้นด้านใน','หน้าร้านเปิดโล่ง แดดส่องผ่านราวระเบียงลงมาถึงพื้น — นี่คือเหตุผลข้อแรกที่งานนี้เป็น PU ไม่ใช่ Epoxy',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>ทำไมเป็น PU — เพราะพื้นนี้โดนแดด</h2>
      <p>สีทาพื้นสองส่วนผสมของเรามีสองสาย: <b>Epoxy</b> แข็งแน่น ทนแรงกดที่สุด ราคาคุ้มที่สุด แต่โดนแดดนานๆ จะเหลืองและฝืดผิว จึงเหมาะพื้นในอาคาร · <b>PU</b> ยืดหยุ่นกว่า <b>ทน UV ดีกว่า ไม่เหลืองง่าย</b> เหมาะพื้นใกล้ประตู ลานโหลด และพื้นที่โดนแดดบ้าง — ร้านสะดวกซักที่หน้าร้านเปิดโล่งแบบนี้เข้าเกณฑ์ข้อหลังเต็มๆ แดดยามบ่ายพาดลงพื้นครึ่งร้านทุกวัน ถ้าเป็น Epoxy ครึ่งที่โดนแดดจะเหลืองต่างจากครึ่งในร่มภายในเวลาไม่นาน</p>
{fig(3,'ระเบียงหน้าร้านใต้หลังคาเมทัลชีท พื้นสีเทาเงา แดดเต็มพื้น โต๊ะเก้าอี้พลาสติกขาว ถนนและบ้านเรือนด้านนอก','ระเบียงหน้าร้านใต้หลังคา — โซนที่โดนแดดเต็มที่สุดของร้าน ทาต่อเนื่องระบบเดียวกับพื้นด้านใน')}
    </section>
    <section class="step">
      <h2><span class="n">02</span>ฐานยกเครื่องและขอบ — ทาให้ต่อเนื่องเป็นผืนเดียว</h2>
      <p>ร้านสะดวกซักมักหล่อฐานปูนยกเครื่องซักเครื่องอบขึ้นจากพื้น ในภาพจะเห็นว่าสีทาต่อเนื่องจากพื้นขึ้นขอบฐานและหน้าฐานเป็นผืนเดียวกัน — <b>ขอบและมุมคือจุดที่น้ำและผงซักฟอกไปกองสะสม</b> การทาให้ฟิล์มต่อเนื่องขึ้นไปปิดถึงฐาน ทำให้ล้างพื้นได้ทีเดียวจบ ไม่มีร่องปูนเปลือยให้คราบเข้าไปฝัง</p>
{fig(2,'พื้นสีเทา RAL 7040 ระยะใกล้ เงาสะท้อนหน้าต่าง ฟิล์มทาต่อเนื่องขึ้นขอบฐานปูนที่ยกเครื่องซัก มีร่องระบายน้ำเล็กตามแนวฐาน','ฟิล์มทาต่อเนื่องจากพื้นขึ้นขอบฐานเครื่อง — ร่องระบายน้ำเล็กตามแนวฐานยังอยู่ครบ')}
{fig(4,'มุมโซนเครื่องอบผ้าซ้อนสองชั้นบนฐานปูนยก พื้นและฐานทาสีเทาเดียวกัน ด้านขวาเปิดโล่งเห็นหลังคาเมทัลชีทและต้นไม้','ฐานยกเครื่องอบทาสีเดียวกับพื้น — โซนนี้ติดด้านเปิดโล่ง แดดเข้าเต็ม')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>เรื่องผิว — พูดตรงๆ เหมือนที่เขียนบนหน้าสินค้า</h2>
      <p>ดูภาพระยะใกล้ให้ดี: ผิวที่ได้<b>เงา แต่ไปตามผิวปูนเดิม</b> จุดที่ปูนขัดมันไม่เท่ากันหรือรอยเกรียงยังเห็นเป็นเงาไม่สม่ำเสมอบ้าง — นี่คือธรรมชาติของสีทาพื้นแบบทา (Coating) ฟิล์มบางระดับสีทาบ้านหนาๆ ไม่ได้ทำหน้าที่ปรับระดับ ถ้าอยากได้เรียบเงาเหมือนกระจกต้องเป็นระบบ Self-leveling คนละราคาคนละความยาก เราเขียนเรื่องนี้ไว้บนหน้าสินค้าก่อนขายเสมอ และงานนี้ก็เป็นตัวอย่างที่ดีว่าของจริงหน้าตาเป็นแบบไหน</p>
{fig(5,'โซนนั่งรอกลางร้าน โต๊ะพับขาวและเก้าอี้พลาสติกขาวบนพื้นสีเทา RAL 7040 เครื่องซักเรียงด้านซ้าย เครื่องอบด้านใน','พื้นเทาอ่อนกับเฟอร์นิเจอร์ขาว — RAL 7040 ทำให้ร้านดูสว่างและสะอาด แต่สีอ่อนโชว์คราบไวกว่าสีเข้ม ต้องล้างบ่อยตามจริง')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>สรุปสำหรับร้านสะดวกซัก ร้านค้า และพื้นที่หน้าร้านเปิดโล่ง</h2>
      <p><b>พื้นในอาคารล้วนๆ ไม่โดนแดด รับของหนัก</b> → Epoxy แบบทา คุ้มที่สุด · <b>หน้าร้านเปิดโล่ง โดนแดดบ้าง หรือกลัวสีเหลือง</b> → PU แบบทา เหมือนเคสนี้ · <b>สี</b> — สั่งผลิตได้ทุกเฉด RAL ส่งรหัสมาได้เลย เทาอ่อนอย่าง 7040 ทำให้ร้านสว่างแต่โชว์คราบไว เทาเข้มเก็บคราบเก่งกว่า · <b>ก่อนทา</b> — พื้นต้องแห้งจริงถึงเนื้อใน ขัดเปิดผิว ดูดฝุ่น ซ่อมหลุมด้วย <a href="/patchpro">PatchPro</a> ให้เรียบก่อน 80% ของงานอยู่ตรงนี้</p>
      <p>ชุด 16 กก. ทาได้ราว 50 ตร.ม. ครบ 2 รอบ — ส่งขนาดร้านกับรูปพื้นมาทางแชทเพจ เราคำนวณจำนวนชุดและบอกตรงๆ ว่าพื้นของคุณควรเป็นสายไหน</p>
{gallery_html('พื้นร้านสะดวกซักทาสีทาพื้น PU เฉด RAL 7040 — ภาพงานจริงหลังทาเสร็จ')}
    </section>
  </article>
"""

# ─────────────────────────── EN ───────────────────────────
EN_TITLE = "A Laundromat Floor in PU Floor Coating, RAL 7040 — an Open-Fronted Floor in Daily Sun, So It Had to Be the PU System"
EN_DESC = ("Real job photos: a coin laundromat with an open front and sun on the floor every day, coated with our two-component PU floor coating, made to order in RAL 7040 light grey — "
           "why this job is PU rather than Epoxy, the machine plinths and the front terrace coated as one continuous system, and the straight talk about the finish before you order")
EN_EYEBROW = "Case Study · Floor Coating / Epoxy-PU"
EN_META = "Published Sep 2026 · Real job photos after completion"

EN_BODY = f"""  <article>
    <p>A laundromat is a quietly hard-working floor — rows of washers and dryers, people in and out all day, water and detergent dripping onto the floor as a matter of routine, and most of these shops have an <b>open front with sun reaching the floor every day</b>. This one was coated with our <a href="/en/epoxycoating">two-component PU floor coating</a>, made to order in <b>RAL 7040</b> (a cool light grey). The photos are after completion.</p>
{fig(1,'Open-fronted laundromat, glossy RAL 7040 grey floor reflecting sunlight through the balustrade, washers along the left wall, stacked dryers at the back','The open front, with sun coming through the balustrade onto the floor — the first reason this job is PU, not Epoxy',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>Why PU — because this floor gets sun</h2>
      <p>Our two-component floor coating comes in two families: <b>Epoxy</b> — hardest, best under load, best value, but it yellows and dulls under prolonged sun, so it belongs indoors · <b>PU</b> — more flexible, <b>better UV resistance, slow to yellow</b>, right for floors near doors, loading bays and areas that see some sun. An open-fronted laundromat like this one is squarely the second case: afternoon sun lies across half the shop floor every day. In Epoxy, the sunlit half would yellow away from the shaded half within a fairly short time.</p>
{fig(3,'Front terrace of the shop under a metal roof, glossy grey floor in full sun, white plastic tables and stools, street and houses beyond','The front terrace under the roof — the sunniest zone of the shop, coated continuously in the same system as the interior')}
    </section>
    <section class="step">
      <h2><span class="n">02</span>Machine plinths and edges — coated as one continuous surface</h2>
      <p>Laundromats usually cast concrete plinths to raise the washers and dryers off the floor. In the photos the coating runs continuously from the floor up the edge and face of the plinth — <b>edges and corners are where water and detergent collect</b>, and a film that continues up onto the plinth means the floor washes in one go, with no strip of bare concrete for grime to soak into.</p>
{fig(2,'Close view of the RAL 7040 grey floor reflecting the windows, the film continuing up the edge of the concrete plinth under the washers, a small drainage channel along the plinth','The film runs continuously from the floor up the plinth edge — the small drainage channel along the plinth is kept intact')}
{fig(4,'Corner with stacked dryers on a raised concrete plinth, floor and plinth coated the same grey, the right side open to a metal roof and trees','Dryer plinth coated the same as the floor — this corner sits on the open side, in full sun')}
    </section>
    <section class="step">
      <h2><span class="n">03</span>The finish — said plainly, as on the product page</h2>
      <p>Look closely at the close-up: the finish is <b>glossy, but it follows the original concrete</b>. Where the trowelled surface was uneven you can still see some variation in the sheen — that is the nature of a roll-on floor coating: a film about as thick as heavy house paint, which does not level anything. A mirror-flat floor is a self-levelling system, a different price and a different level of difficulty. We put this on the product page before selling, and this job is a good example of what the real thing looks like.</p>
{fig(5,'Waiting area in the middle of the shop, white folding table and white plastic stools on the RAL 7040 grey floor, washers along the left, dryers at the back','Light grey floor with white furniture — RAL 7040 makes the shop look bright and clean, but a light colour shows dirt sooner than a dark one and gets washed more often, honestly')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>In short, for laundromats, shops and open-fronted floors</h2>
      <p><b>Fully indoor, no sun, heavy loads</b> → roll-on Epoxy, best value · <b>Open front, some sun, or you don't want yellowing</b> → roll-on PU, as in this case · <b>Colour</b> — any RAL shade is made to order, just send the code; a light grey like 7040 brightens the shop but shows dirt early, a darker grey hides it better · <b>Before coating</b> — the slab must be dry through, ground open, vacuumed, and holes repaired flat with <a href="/en/patchpro">PatchPro</a>; 80% of the job is here.</p>
      <p>A 16 kg set covers about 50 m² in two coats — send the shop size and floor photos via chat and we will work out the number of sets and tell you straight which family your floor should be.</p>
{gallery_html('Laundromat floor coated in PU floor coating, RAL 7040 — real job photos after completion')}
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
