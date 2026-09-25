# -*- coding: utf-8 -*-
"""
build_solar_dust_post.py — โพสต์ "ฝุ่นบางๆ บนแผงโซลาร์กินไฟเท่าไหร่" (จากข้อความโฆษณา FB 25 ก.ย. 2026 ของ Pist)
/post/solar-dust-loss (+ /en/…)
วิธี: chrome-transplant จากโพสต์ solar-panel-defender-feibo-lab (เหมือน build_feibo_stone_cases.py) — TH+EN
รูป: /img/post/solar-dust-loss-h1.webp (ภาพประกอบ Gemini — นิ้วปาดฝุ่นบนแผง, แนวตั้ง) + reuse
     /img/post/self-cleaning-technology-h6.webp (แถวเดียวกัน เคลือบ/ไม่เคลือบ) และ -h7.webp (ทีมงานในโรงไฟฟ้า)
ตัวเลข: soiling loss 2% ขั้นต่ำ / เฉลี่ย 3–5% (คำพูดของ Pist) · 3–5% ของ 365 วัน = 11–18 วัน · 100 g ≈ 8 แผ่นใหญ่ 830.-
       อายุ ~5 ปี = ตัวเลขที่ผู้พัฒนาระบุ (TDS ไม่ให้อายุ) · SGS = มีรายงานทดสอบ — เขียนแบบ attribute ไม่ใช่เคลมเอง
รัน: python3 tools/build_solar_dust_post.py (จาก root ของ repo)
"""
import os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "solar-dust-loss"


def dims(src):
    return Image.open(os.path.join(ROOT, src.lstrip("/"))).size


def fig(src, alt, cap, hero=False):
    w, h = dims(src)
    cls = ' class="hero"' if hero else ''
    icls = ' class="tall"' if h > w else ''
    lazy = '' if hero else ' loading="lazy"'
    return (f'    <figure{cls}><img{icls} src="{src}" alt="{alt}"{lazy} '
            f'width="{w}" height="{h}"><figcaption>{cap}</figcaption></figure>\n')


def step(n, h2, parts):
    return (f'    <section class="step">\n      <h2><span class="n">{n}</span>{h2}</h2>\n'
            + "".join((f"      <p>{p}</p>\n" if not p.lstrip().startswith("<") else p) for p in parts)
            + "    </section>\n")


H1 = f"/img/post/{SLUG}-h1.webp"
H6 = "/img/post/self-cleaning-technology-h6.webp"
H7 = "/img/post/self-cleaning-technology-h7.webp"

TH = dict(
    title="แผงโซลาร์ที่ดูสะอาดอยู่ — ลองเอานิ้วปาดดูสักที ฝุ่นบางๆ ที่มองจากพื้นไม่เห็น กินไฟปีละ 3–5%",
    desc="ฝุ่นบางบนกระจกแผงโซลาร์ที่มองจากพื้นไม่เห็น งานวิจัย soiling loss หลายชิ้นวัดได้อย่างต่ำ 2% ค่าเฉลี่ย 3–5% ของไฟที่แผงผลิตได้ เท่ากับปิดแผงทิ้ง 11–18 วันต่อปี และตัวเลขขยับขึ้นทุกวันที่ยังไม่มีใครขึ้นไปล้าง — ทำไมล้างบ่อยไม่ไหว ตัวเลขจากโรงไฟฟ้าที่เคลือบจริง และคิดเป็นเงินสำหรับบ้านหลังหนึ่ง",
    eyebrow="Case Study · โซลาร์ / Solar Panel Defender",
    meta="เผยแพร่ ก.ย. 2026 · ตัวเลขโรงไฟฟ้าจากผู้พัฒนาวัตถุดิบ · ภาพเปิดเป็นภาพประกอบ",
    intro=[
        'แผงบนหลังคาคุณดูสะอาดอยู่ใช่ไหมครับ ลองขึ้นไปเอานิ้วปาดดูสักที — ฝุ่นบางๆ ชั้นนั้นมองจากพื้นไม่เห็นเลย แต่มันอยู่บนกระจกทุกแผ่นที่ยังไม่มีใครขึ้นไปล้าง และมันกินไฟที่แผงผลิตได้อยู่เงียบๆ ทุกวัน',
        'หน้านี้ตอบสามคำถาม: ฝุ่นบางแค่นี้กินไฟเท่าไหร่ ทำไมวิธี "ขึ้นไปล้าง" ถึงไม่ใช่คำตอบ และสำหรับบ้านหลังหนึ่งมันคิดเป็นเงินกี่บาท',
    ],
    hero=("นิ้วปาดผ่านชั้นฝุ่นบางบนกระจกแผงโซลาร์ เห็นรอยปาดใสตัดกับผิวที่มีฝุ่น",
          "รอยนิ้วเดียวบนแผงที่ \"ดูสะอาด\" — ชั้นฝุ่นที่มองจากพื้นไม่เห็นเลย (ภาพประกอบ)"),
    steps=[
        ("01", "ฝุ่นบางแค่นี้ กินไฟเท่าไหร่", [
            'ค่าไฟที่หายไปเพราะฝุ่นบนกระจกมีชื่อเรียกของมันเอง — <b>soiling loss</b> — และมีคนวัดมาแล้วทั่วโลก งานวิจัยหลายชิ้นได้ตัวเลขไปทางเดียวกัน: อย่างต่ำ <b>2%</b> ของไฟที่แผงผลิตได้ ค่าเฉลี่ยจริงอยู่ที่ <b>3–5%</b> และในพื้นที่ฝุ่นเยอะหรือใกล้ถนนสูงกว่านั้น',
            '3–5% ต่อปีฟังดูน้อย ลองคิดอีกแบบ: มันเท่ากับ<b>ปิดแผงทิ้ง 11–18 วันต่อปี</b>โดยที่คุณไม่รู้ตัว และมันไม่หยุดแค่นั้น ฝุ่นสะสมขึ้นทุกวัน วันไหนยังไม่มีใครขึ้นไปล้าง ตัวเลขก็ขยับขึ้นเรื่อยๆ จนกว่าจะมีฝนใหญ่หรือมีคนขึ้นไปล้างจริง — และหลังล้างเสร็จ นาฬิกาก็เริ่มนับใหม่',
        ]),
        ("02", "ปัญหาไม่ใช่ล้างไม่ได้ — คือขึ้นไปล้างบ่อยๆ ไม่ไหว", [
            'ล้างแผงไม่ยาก น้ำเปล่ากับแปรงนุ่มก็จบ ที่ยากคือ<b>ความถี่</b>: จะให้ได้ผลจริงต้องล้างทุกไม่กี่สัปดาห์ในหน้าแล้ง แปลว่าขึ้นหลังคาซ้ำๆ ทั้งปี บ้านส่วนใหญ่จึงล้างปีละครั้งหรือไม่ล้างเลย แล้วยอมรับ 3–5% ไปเงียบๆ',
            'โรงไฟฟ้าขนาดใหญ่เจอปัญหาเดียวกันในสเกลที่ใหญ่กว่า จึงเป็นที่แรกที่ลองแก้ด้วยการ<b>เคลือบผิวกระจกให้ฝุ่นเกาะไม่ติด</b>แทนการล้างซ้ำ ผู้พัฒนาวัตถุดิบเก็บตัวเลขจากโรงไฟฟ้าที่เคลือบจริง 6 แห่งไว้ ไฟฟ้าเพิ่มขึ้น +2.9% ถึง +5% ต่างกันตามฝุ่นของแต่ละพื้นที่ — ตารางเต็มพร้อมปีส่งมอบอยู่ที่หน้า <a href="/post/self-cleaning-technology">หลักการ Self-Cleaning</a>',
            fig(H6, "แผงโซลาร์แถวเดียวกัน ฝั่งซ้ายเคลือบแล้วผิวใส ฝั่งขวาไม่เคลือบมีฝุ่นเกาะ",
                "แถวเดียวกัน วันเดียวกัน — ซ้าย: เคลือบแล้ว · ขวา: ยังไม่เคลือบ ฝุ่นเกาะจนสีแผงต่างกันเห็นชัด (ภาพจากผู้พัฒนาวัตถุดิบ)"),
        ]),
        ("03", "Solar Panel Defender ทำอะไรกับกระจก", [
            'เป็นฟิล์มนาโนบางใสที่ทำให้ผิวกระจก<b>เรียบและชอบน้ำ</b> ฝุ่นจึงเกาะไม่ติดแน่นเหมือนกระจกเปล่า ลมพัดหลุด ฝนตกล้างออกเป็นแผ่นไม่ทิ้งคราบวงน้ำ รอบที่ต้องขึ้นไปล้างเองจึงลดลงชัดเจน ที่หน้างานของเราเอง แผงที่เคลือบแล้วเป่าลมทีเดียวฝุ่นหลุด ส่วนแผงข้างๆ ที่ไม่ได้เคลือบยังเหลือฝุ่นบางเป็นฝ้าอยู่',
            'ทาบางๆ รอบเดียวด้วยฟองน้ำหรือผ้า (ไม่ใช่พ่น ไม่เทลงแผง) แห้งสัมผัสไม่กี่นาที ผู้พัฒนาระบุอายุใช้งานราว 5 ปี และมีรายงานทดสอบจากแล็บ SGS ประกอบ — รายละเอียดการทาและข้อจำกัดอยู่ที่หน้า <a href="/solarpaneldefender">Solar Panel Defender</a>',
            fig(H7, "ทีมงานเคลือบแผงโซลาร์ในโรงไฟฟ้ากลางแจ้ง", "งานโรงไฟฟ้า — เคลือบทีละแถวขณะโรงไฟฟ้ายังจ่ายไฟตามปกติ (ภาพจากผู้พัฒนาวัตถุดิบ)"),
        ]),
        ("04", "สำหรับบ้านหลังหนึ่ง คิดเป็นเงินเท่าไหร่", [
            'ตัวเลขประมาณการ ไม่ใช่คำสัญญา — บ้านที่ติดโซลาร์ 5 kW ผลิตไฟได้ราวปีละ 7,000 หน่วย ฝุ่น 3–5% คือ 210–350 หน่วยต่อปี คิดที่ค่าไฟบ้านราว 4.2 บาทต่อหน่วย = <b>900–1,500 บาทต่อปี</b>ที่หายไปโดยไม่เห็น ระบบ 5 kW มีแผงประมาณ 10–12 แผ่น Solar Panel Defender 100 g เคลือบได้ประมาณ 8 แผ่นใหญ่ ขวดละ 830.- ใช้ 2 ขวด = 1,660.-',
            'เอาแค่ค่าไฟที่ได้คืน ก็คืนทุนในปีที่ 1–2 ที่เหลือของอายุฟิล์มคือส่วนที่ได้เพิ่ม — แต่ตัวที่บ้านส่วนใหญ่รู้สึกจริงไม่ใช่ตัวเลขนี้ คือ<b>ไม่ต้องขึ้นหลังคาไปล้าง</b>อีกหลายรอบต่อปี พื้นที่ฝุ่นน้อย โดนฝนบ่อย ตัวเลขจะต่ำกว่านี้ ใกล้ถนนหรือหน้าแล้งยาวจะสูงกว่านี้',
        ]),
        ("05", "ไม่แน่ใจต้องใช้กี่ขวด", [
            'ส่งจำนวนแผ่น (หรือรูปหลังคา) มาทางแชทเพจ เราคำนวณจำนวนขวดให้ฟรีก่อนสั่ง ไม่ต้องเผื่อเอง',
        ]),
    ],
    prods='<div class="prods"><span class="lbl">สินค้าที่ใช้:</span><a href="/solarpaneldefender">Solar Panel Defender</a></div>\n  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>\n',
)

EN = dict(
    title="Your Panels Look Clean — Run a Finger Across One. The Thin Dust You Can't See From the Ground Costs 3–5% a Year",
    desc="A thin layer of dust on solar glass, invisible from the ground: soiling-loss studies measure at least 2% and typically 3–5% of what the panels generate — the same as switching them off for 11–18 days a year, and rising every day nobody climbs up to wash. Why washing isn't the answer, measured gains at coated plants, and what it means in money for one house",
    eyebrow="Case Study · Solar / Solar Panel Defender",
    meta="Published Sept 2026 · Plant figures from the raw-material developer · Opening photo is an illustration",
    intro=[
        'The panels on your roof look clean, right? Climb up and run a finger across one. That thin layer of dust is invisible from the ground, but it is on every panel nobody has washed — and it quietly eats into what the panels generate, every day.',
        'This page answers three questions: how much that thin dust costs, why "just wash them" isn\'t the answer, and what it adds up to in money for a single house.',
    ],
    hero=("A finger swiped through a thin layer of dust on solar-panel glass, leaving a clear streak against the dusty surface",
          "One finger swipe on a panel that \"looks clean\" — the dust layer you cannot see from the ground (illustration)"),
    steps=[
        ("01", "How much does dust this thin actually cost", [
            'Output lost to dust on the glass has its own name — <b>soiling loss</b> — and it has been measured all over the world. Study after study lands in the same range: at least <b>2%</b> of what the panels generate, typically <b>3–5%</b>, and higher in dusty areas or near roads.',
            '3–5% a year sounds small. Look at it another way: it is the same as <b>switching the panels off for 11–18 days a year</b> without knowing it. And it doesn\'t stop there — dust builds up daily, so every day nobody climbs up to wash, the number creeps higher, until a heavy rain or a real wash resets it. Then the clock starts again.',
        ]),
        ("02", "The problem isn't that you can't wash — it's that you can't keep climbing up", [
            'Washing a panel is easy: plain water and a soft brush. The hard part is <b>frequency</b>. To actually keep the loss down you need to wash every few weeks through the dry season, which means going up on the roof again and again all year. So most houses wash once a year or never, and quietly accept the 3–5%.',
            'Large plants face the same problem at a larger scale, which is why they were the first to try <b>coating the glass so dust cannot cling</b> instead of washing over and over. The raw-material developer recorded gains at six plants it coated: +2.9% to +5% more output, depending on how dusty each site is — the full table with delivery dates is on the <a href="/en/post/self-cleaning-technology">Self-Cleaning technology</a> page.',
            fig(H6, "Same row of solar panels, left side coated and clear, right side uncoated with dust settled",
                "Same row, same day — left: coated · right: not yet coated, dust settled enough to change the panel colour (photo from the raw-material developer)"),
        ]),
        ("03", "What Solar Panel Defender does to the glass", [
            'It is a thin, clear nano film that makes the glass <b>smooth and water-loving</b>, so dust cannot grip the way it does on bare glass — wind knocks it off, rain washes it away as a sheet without leaving water rings, and the number of times you have to climb up and wash drops sharply. On our own panels, one puff of breath clears the dust from a coated panel, while the uncoated one next to it keeps a faint powder film.',
            'One thin coat applied with a sponge or cloth (not sprayed, never poured onto the panel), touch-dry in minutes. The developer states a service life of around 5 years and provides SGS lab test reports — application details and limits are on the <a href="/en/solarpaneldefender">Solar Panel Defender</a> page.',
            fig(H7, "Crew coating solar panels at an outdoor power plant", "Plant work — coated row by row while the plant kept generating (photo from the raw-material developer)"),
        ]),
        ("04", "What it means in money for one house", [
            'An estimate, not a promise — a house with a 5 kW system generates roughly 7,000 kWh a year. Dust at 3–5% is 210–350 kWh a year; at a household tariff of about 4.2 baht per kWh that is <b>900–1,500 baht a year</b> disappearing unseen. A 5 kW system has about 10–12 panels; one 100 g bottle of Solar Panel Defender coats about 8 large panels at 830.-, so two bottles = 1,660.-',
            'On recovered electricity alone it pays back in year 1–2, and the rest of the film\'s life is the gain — but what most households actually feel is not this number. It is <b>not climbing onto the roof to wash</b> several times a year. Low-dust areas with frequent rain will come in below these figures; near a road or through a long dry season, above them.',
        ]),
        ("05", "Not sure how many bottles", [
            'Send the number of panels (or a photo of the roof) on the page chat and we work out the bottle count for you, free, before you order — no guessing the margin yourself.',
        ]),
    ],
    prods='<div class="prods"><span class="lbl">Product used:</span><a href="/en/solarpaneldefender">Solar Panel Defender</a></div>\n  <a class="back" href="/en/casestudy/">← Back to all case studies</a>\n',
)


def render(d):
    hero_fig = fig(H1, d["hero"][0], d["hero"][1], hero=True)
    steps = "".join(step(n, h2, parts) for n, h2, parts in d["steps"])
    return ("  <article>\n" + f'    <p>{d["intro"][0]}</p>\n' + hero_fig
            + "".join(f"    <p>{p}</p>\n" for p in d["intro"][1:]) + steps
            + "  </article>\n  " + d["prods"])


def transplant(src_path, out_path, title, desc, eyebrow, meta, body_html, og_img):
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
                f'  <p class="meta">{meta}</p>\n' + body_html)
    h = h[:i] + new_main + h[j:]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(h)
    print("built:", out_path)


if __name__ == "__main__":
    og = f"https://www.lucernapro.com{H1}"
    transplant(os.path.join(ROOT, "post", SRC, "index.html"), os.path.join(ROOT, "post", SLUG, "index.html"),
               TH["title"], TH["desc"], TH["eyebrow"], TH["meta"], render(TH), og)
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"), os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN["title"], EN["desc"], EN["eyebrow"], EN["meta"], render(EN), og)
