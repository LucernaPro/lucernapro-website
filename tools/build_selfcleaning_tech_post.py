# -*- coding: utf-8 -*-
"""
build_selfcleaning_tech_post.py — โพสต์อธิบายเทคโนโลยี Self-Cleaning (หน้า hub ของสาย Glass / Paint / Stone / Solar)
/post/self-cleaning-technology (+ /en/…)
วิธี: chrome-transplant จากโพสต์ solar-panel-defender-feibo-lab (เหมือน build_feibo_stone_cases.py) — TH+EN
เนื้อหา: หลักการสองเส้นทาง · ชุดทดสอบเทียบ · หน้างานทำครึ่ง/ไม่ทำครึ่ง · ตัวเลขโรงไฟฟ้า · เทียบวิธีเดิม · ผิวไหนใช้ตัวไหน
ที่มา: brochure ของผู้พัฒนาวัตถุดิบ (ก.ย. 2026) — เอาเฉพาะข้อมูลที่มีชื่อ-ปี-ตัวเลข ไม่เอาคำโฆษณาลอยๆ
รูป: /img/post/self-cleaning-technology-h1..h7.webp + -g01..g08.webp (800x800) และ /img/stonesurface-proof01.webp ที่มีอยู่แล้ว
รัน: python3 tools/build_selfcleaning_tech_post.py (จาก root ของ repo)
"""
import os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "self-cleaning-technology"
NGAL = 8
GRID_STYLE = ("display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));"
              "gap:10px;margin-top:26px")
TBL = ('style="width:100%;border-collapse:collapse;margin-top:18px;font-size:.92rem;line-height:1.5"')
TH_ = 'style="text-align:left;padding:10px 12px;border-bottom:2px solid var(--line);font-family:var(--mono);font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--steel)"'
TD_ = 'style="padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top"'
TDR = 'style="padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;text-align:right;font-family:var(--mono);font-weight:600;color:var(--signal);white-space:nowrap"'
TDB = 'style="padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;font-weight:700;white-space:nowrap"'


def dims(path):
    return Image.open(os.path.join(ROOT, path.lstrip("/"))).size


def fig(src, alt, cap, hero=False):
    w, h = dims(src)
    cls = ' class="hero"' if hero else ''
    icls = ' class="tall"' if h > w else ''
    lazy = '' if hero else ' loading="lazy"'
    return (f'    <figure{cls}><img{icls} src="{src}" alt="{alt}"{lazy} '
            f'width="{w}" height="{h}"><figcaption>{cap}</figcaption></figure>\n')


def H(k):
    return f"/img/post/{SLUG}-h{k}.webp"


def step(n, h2, parts):
    return (f'    <section class="step">\n      <h2><span class="n">{n}</span>{h2}</h2>\n'
            + "".join((f"      <p>{p}</p>\n" if not p.lstrip().startswith("<") else p) for p in parts)
            + "    </section>\n")


def table(head, rows, right_last=False, bold_first=False):
    out = [f'<table {TBL}><thead><tr>' + "".join(f"<th {TH_}>{h}</th>" for h in head) + "</tr></thead><tbody>"]
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            st = TDB if (bold_first and i == 0) else (TDR if (right_last and i == len(r) - 1) else TD_)
            cells.append(f"<td {st}>{c}</td>")
        out.append("<tr>" + "".join(cells) + "</tr>")
    out.append("</tbody></table>\n")
    return "".join(out)


def dcards(cards, go):
    h = '<div class="decision">\n'
    for tag, title, p, href in cards:
        h += (f'  <div class="dcard"><span class="tag">{tag}</span><h4>{title}</h4>'
              f'<p>{p}</p><a class="go" href="{href}">{go} {title} →</a></div>\n')
    return h + "</div>\n"


def gallery_html(alt_prefix):
    imgs = "".join(
        f'<img src="/img/post/{SLUG}-g{i:02d}.webp" alt="{alt_prefix} {i:02d}" loading="lazy" '
        f'width="800" height="800" style="border-radius:10px;border:1px solid var(--line)">\n'
        for i in range(1, NGAL + 1))
    return '<div style="' + GRID_STYLE + '">\n' + imgs + '</div>'


# ─────────────────────────── TH ───────────────────────────
PV_ROWS = [
    ("โรงไฟฟ้าหนิงเซี่ย หย่งหนิง กั๋วกวง 100 MW", "2024.07", "+3.10%"),
    ("โรงไฟฟ้าเสฉวน ว่านเจียซาน 30 MW", "2023.10", "+3.94%"),
    ("โรงไฟฟ้าเหอจิ้ง อี้ซิน 30 MW", "2023.10", "+2.94%"),
    ("โรงไฟฟ้ามองโกเลียใน ซินปาเอ่อร์หู่จั่วฉี 40 MW", "2021.10", "+5.00%"),
    ("โรงไฟฟ้าหูเป่ย สุยโจว อู่หวน", "2019.10", "+5.00%"),
    ("โรงไฟฟ้าอานฮุย หม่าอานซาน ทงโฮ่ว", "2022.10", "+3.47%"),
]
PV_ROWS_EN = [
    ("Ningxia Yongning Guoguang 100 MW", "2024.07", "+3.10%"),
    ("Sichuan Wanjiashan 30 MW", "2023.10", "+3.94%"),
    ("Hejing Yixin 30 MW", "2023.10", "+2.94%"),
    ("New Barag Left Banner 40 MW", "2021.10", "+5.00%"),
    ("Hubei Suizhou Wuhuan", "2019.10", "+5.00%"),
    ("Anhui Ma'anshan He County Tonghou", "2022.10", "+3.47%"),
]

TH = dict(
    title="Self-Cleaning ทำงานยังไง — ฝนล้าง แดดย่อย และพิสูจน์อะไรมาแล้วบ้าง",
    desc="เทคโนโลยีเบื้องหลัง Glass / Paint / Stone / Solar Coating ของเรา อธิบายครั้งเดียวจบ — ทำไมถึงเลือกเส้นทาง Superhydrophilic ไม่ใช่ใบบัว ชุดทดสอบเทียบฝุ่น-ฝน-น้ำมัน หน้างานทำครึ่งไม่ทำครึ่ง และตัวเลขจากโรงไฟฟ้าโซลาร์ 6 แห่ง",
    eyebrow="Case Study · เคลือบปกป้อง / Self-Cleaning",
    meta="เผยแพร่ ก.ย. 2026 · ภาพทดสอบและข้อมูลโครงการจากผู้พัฒนาวัตถุดิบ (ฉางชา ประเทศจีน)",
    intro=[
        'สายเคลือบผิว Self-Cleaning ของเรามี 4 ตัว — <a href="/glasscoating">Glass Coating</a> <a href="/paintcoating">Paint Coating</a> <a href="/stonesurface">Stone Coating</a> และ <a href="/solarpaneldefender">Solar Panel Defender</a> — ต่างกันที่ผิวที่ใช้ แต่หลักการเดียวกันหมด หน้านี้อธิบายหลักการนั้นครั้งเดียว แล้วพาไปดูว่ามันผ่านการทดสอบและหน้างานอะไรมาบ้าง ก่อนที่เราจะเลือกนำเข้าวัตถุดิบหลักจากผู้พัฒนาเทคโนโลยีนี้โดยตรง (Feibo ฉางชา ประเทศจีน) ภาพทดสอบและข้อมูลโครงการในหน้านี้เป็นของเขา เราคัดมาเฉพาะที่มีชื่อสถานที่ ปี และตัวเลขกำกับ',
        'คำว่า "เคลือบแล้วสะอาดเอง" ฟังดูเหมือนคำโฆษณา จนกว่าจะเข้าใจว่าน้ำฝนกับแดดถูกใช้เป็นเครื่องมือยังไง — เริ่มจากหยดน้ำหยดเดียวในภาพข้างบน',
    ],
    hero=("หยดน้ำกลมบนผิวเคลือบกันน้ำ เทียบกับน้ำที่แผ่เป็นแผ่นบางบนผิวเคลือบ Self-Cleaning",
          "ผิวเดียวกัน สองแบบ — ซ้าย: น้ำเกาะเป็นหยดกลม (Hydrophobic) · ขวา: น้ำแผ่ออกเป็นแผ่นบาง (Superhydrophilic) สายของเราคือแบบขวา"),
    steps=[
        ("01", "สองเส้นทางของคำว่า Self-Cleaning — และทำไมเราไม่เลือกใบบัว", [
            'เทคโนโลยีผิวสะอาดเองแบ่งตาม "น้ำทำอะไรบนผิว" มีสองทาง ทางแรกคือ <b>Superhydrophobic</b> — ทำผิวให้เกลียดน้ำสุดขั้ว มุมสัมผัสน้ำเกิน 150° น้ำเกาะเป็นหยดกลมแล้วกลิ้งลง (Lotus effect แบบใบบัว) ทางที่สองคือ <b>Superhydrophilic</b> — ตรงข้ามกันเลย ทำผิวให้ชอบน้ำสุดขั้ว มุมสัมผัสต่ำกว่า 10° น้ำไม่เป็นหยดแต่แผ่ออกเป็นแผ่นบางคลุมทั้งผิว',
            'ใบบัวฟังดูเท่กว่า แต่บนผนังอาคารมันมีสองจุดอ่อน หนึ่ง หยดน้ำกลิ้งพาได้แค่ฝุ่นแห้ง คราบน้ำมัน เขม่ารถ และคราบเหนียวยังเกาะอยู่ที่เดิม สอง หยดเล็กๆ ที่ไม่หนักพอจะกลิ้ง จะแห้งคาผิวเป็นจุดวงน้ำ ส่วนแบบแผ่นน้ำบาง น้ำฝนจะไหลแทรกเข้า<b>ใต้</b>คราบ ยกคราบขึ้นแล้วพาลงไปทั้งแผ่น ไม่เหลือหยดให้แห้งเป็นจุด นี่คือเหตุผลที่ทั้ง 4 ตัวของเราอยู่ฝั่ง Superhydrophilic',
            'ในฟิล์มยังมีอีกสองกลไกทำงานร่วม — <b>Photocatalytic</b> นาโนไทเทเนียมไดออกไซด์ที่แดดกระตุ้นให้ย่อยคราบอินทรีย์ (น้ำมัน เขม่า รา) บนผิวอย่างต่อเนื่อง และ<b>กันไฟฟ้าสถิต</b> ฝุ่นจึงเกาะยากตั้งแต่แรก ผลรวมคือฝุ่นเกาะน้อยลง แดดย่อยคราบที่เกาะ ฝนล้างที่เหลือ',
            fig(H(2), "เครื่องวัดมุมสัมผัสน้ำ พร้อมหน้าจอแสดงหยดน้ำบนชิ้นทดสอบ",
                "เครื่องวัดมุมสัมผัสน้ำ (Contact angle) — ตัวเลขเดียวที่บอกได้ว่าฟิล์มอยู่ฝั่งไหน ต่ำกว่า 10° คือ Superhydrophilic เกิน 150° คือใบบัว"),
        ]),
        ("02", "ชุดทดสอบเทียบ — ฝุ่น ฝน น้ำมัน บนแผ่นเดียวกัน", [
            'วิธีทดสอบที่พูดแทนได้ทุกอย่างคือเอาแผ่นสีเดียวกันสองแผ่น แผ่นหนึ่งเคลือบ Self-Cleaning อีกแผ่นเคลือบแบบกันน้ำทั่วไป แล้วทำสามอย่างกับมันพร้อมกัน',
            '<b>A · โรยเถ้าลอย</b> — ใช้เถ้าลอยจากโรงไฟฟ้าซึ่งเกาะแน่นกว่าฝุ่นทั่วไป แผ่น Self-Cleaning ที่กันไฟฟ้าสถิตเกาะฝุ่นน้อยกว่าเห็นได้ชัด <b>B · รดน้ำจำลองฝน</b> — บนแผ่น Self-Cleaning น้ำแผ่เป็นแผ่นบาง ยกฝุ่นขึ้นแล้วพาลงทั้งหมด ส่วนแผ่นกันน้ำหยดใหญ่กลิ้งลงแต่หยดเล็กค้างแล้วแห้งเป็นจุด <b>C · หยดน้ำมันแล้วรดน้ำ</b> — ผิว Superhydrophilic เลือกจับน้ำก่อนน้ำมัน น้ำจึงแทรกใต้น้ำมันแล้วยกลอยออกไป ผิวกันน้ำทั่วไปกันน้ำมันเหนียวไม่ได้ และล้างด้วยน้ำเปล่าไม่ออก',
            fig(H(3), "ชุดทดสอบเทียบสามภาพ: โรยเถ้าลอย รดน้ำจำลองฝน และหยดน้ำมันบนแผ่นสีแดงสองแผ่น",
                "ซ้ายไปขวา: A โรยเถ้าลอย · B รดน้ำ · C หยดน้ำมัน — แต่ละภาพคือแผ่นเคลือบสองแบบวางคู่กัน ทำพร้อมกัน เงื่อนไขเดียวกัน"),
            fig(H(4), "ห้องทดสอบ: การวัดมุมสัมผัส เครื่องทดสอบการขัดถู และการโรยฝุ่นบนแผงโซลาร์",
                "การทดสอบในแล็บของผู้พัฒนาวัตถุดิบ — วัดมุมสัมผัส ทดสอบการขัดถู และโรยฝุ่นบนแผงโซลาร์แล้วรดน้ำ"),
        ]),
        ("03", "หน้างานจริง — วิธีพิสูจน์ที่โกงไม่ได้คือทำครึ่งเดียว", [
            'การทดสอบในแล็บบอกได้ว่ากลไกทำงาน แต่สิ่งที่ลูกค้าอยากรู้คือมันอยู่ได้นานแค่ไหนกลางแดดฝนจริง วิธีที่ตรงที่สุดคือ<b>ทำผิวเดียวกันแค่ครึ่งเดียว</b> แล้วปล่อยให้โดนอากาศด้วยกันหลายเดือน เส้นแบ่งที่เห็นคือขอบเขตที่ทำ ไม่ได้ล้าง ไม่ได้แต่งภาพ',
            fig("/img/stonesurface-proof01.webp", "ผนัง GRC ศูนย์ศิลปะ ฝั่งซ้ายเคลือบแล้วขาวสะอาด ฝั่งขวาไม่เคลือบเหลืองหม่นมีคราบน้ำไหล",
                'ผนัง GRC ศูนย์ศิลปะเหมยซีหู ฉางชา — แผงต่อเนื่องชิ้นเดียวกัน ซ้ายทำ ขวาไม่ทำ (<a href="/post/feibo-meixihu-grc">อ่านเคสเต็ม →</a>)'),
            'แบบเดียวกันนี้ทำกับผิวอีกหลายชนิด — หินแกรนิต แผ่น ACP ประตูลิฟต์สแตนเลส ครีบอลูมิเนียมแอร์ สีพ่นทราย หัวรถไฟความเร็วสูง และแผงโซลาร์ — ดูรวมได้ที่แกลเลอรีท้ายหน้า ส่วนงานที่ใหญ่ที่สุดในชุดคือรูปสลักหินบนเกาะส้ม (จวีจื่อโจว) ฉางชา งานบำรุงรักษาเดือนตุลาคม 2023 ผิวหินที่เคยมีคราบฝนไหลเป็นทางและคราบซึม หลังทำระบบยังคงสะอาด',
            fig(H(5), "นั่งร้านรอบรูปสลักหินขนาดใหญ่ระหว่างงานบำรุงรักษา และรูปสลักหลังงานเสร็จ",
                "รูปสลักหินเกาะส้ม ฉางชา — ซ้าย: ระหว่างงาน ต.ค. 2023 ขึ้นนั่งร้านล้างและเคลือบ · ขวา: หลังงานเสร็จ"),
        ]),
        ("04", "ตัวเลขที่วัดได้จริง — โรงไฟฟ้าโซลาร์ 6 แห่ง", [
            'ผิวที่วัดผลได้เป็นตัวเลขตรงที่สุดคือแผงโซลาร์ เพราะฝุ่นที่เกาะแปลเป็นไฟฟ้าที่หายไปได้ทันที ผู้พัฒนาวัตถุดิบเก็บตัวเลขจากโรงไฟฟ้าที่ทำจริงไว้ 6 แห่ง พร้อมปีที่ส่งมอบ',
            table(["โรงไฟฟ้า", "ส่งมอบ", "ไฟฟ้าเพิ่ม"], PV_ROWS, right_last=True),
            'ช่วง +2.9% ถึง +5% ต่างกันตามฝุ่นของแต่ละพื้นที่ — ที่ 1 GW ตัวเลขต่ำสุดก็ยังคุ้มค่าเคลือบในปีแรก ส่วนบ้านและโรงงานในไทยที่มีแผงไม่กี่สิบแผง สิ่งที่ได้จริงคือ<b>ไม่ต้องขึ้นหลังคาไปล้าง</b>บ่อยเท่าเดิม ตัวเลขสำหรับงานสเกลบ้านอยู่ที่หน้า <a href="/solarpaneldefender">Solar Panel Defender</a>',
            fig(H(6), "แผงโซลาร์แถวเดียวกัน ฝั่งซ้ายเคลือบแล้วผิวใส ฝั่งขวาไม่เคลือบมีฝุ่นเกาะ",
                "แถวเดียวกัน วันเดียวกัน — ซ้าย: เคลือบแล้ว · ขวา: ยังไม่เคลือบ ฝุ่นเกาะจนสีแผงต่างกันเห็นชัด"),
            fig(H(7), "ทีมงานเคลือบแผงโซลาร์ในโรงไฟฟ้ากลางแจ้ง", "งานโรงไฟฟ้า — เคลือบทีละแถวขณะโรงไฟฟ้ายังจ่ายไฟตามปกติ"),
        ]),
        ("05", "เทียบกับสองวิธีที่ใช้กันอยู่", [
            'ผนังอาคารที่เปื้อนมีทางเลือกอยู่สองทางมาตลอด — จ้างล้าง หรือทาสีใหม่ ตารางนี้วางระบบ Self-Cleaning ไว้ข้างกัน',
            table(["", "ล้างซ้ำเป็นรอบ", "ทาสีทับใหม่", "เคลือบ Self-Cleaning"], [
                ("อายุผล", "ล้างครั้งหนึ่งอยู่ได้ไม่กี่เดือน น้ำยากรดที่ใช้ซ้ำๆ ทำผิวหินและสีเหลืองและเสื่อมเร็วขึ้น", "2–3 ปีเริ่มลอก พอง และคราบฝนกลับมาหลังฝนไม่กี่ครั้ง", "ผู้พัฒนาระบบระบุ 3–5 ปีต่อการทำหนึ่งครั้ง ฟิล์มใสไม่เปลี่ยนสีและผิวสัมผัส"),
                ("ขั้นตอน", "ต้องปีนหรือโรยตัวทุกรอบ แต่ละรอบใช้เวลาเป็นสัปดาห์ และมีความเสี่ยงงานบนที่สูงทุกครั้ง", "ล้าง ขัด รองพื้น สีชั้นกลาง สีทับหน้า — หลายวัน หลายทีม", "ล้างผิวให้สะอาดแล้วเคลือบชั้นบางชั้นเดียว (หินมีรองพื้นเพิ่มหนึ่งชั้น) ที่เหลือฝนกับแดดทำต่อ"),
                ("ทำซ้ำ", "ยิ่งล้างยิ่งสึก ค่าใช้จ่ายเพิ่มทุกปี", "ครั้งถัดไปต้องขูดสีเก่าออกก่อน", "ครบรอบทำทับบนผิวเดิมได้ แค่ล้างฝุ่นออกก่อน"),
            ], bold_first=True),
            'สิ่งที่ตารางไม่ได้บอกและเราอยากให้รู้ก่อน — ระบบนี้<b>ป้องกัน ไม่ใช่ล้าง</b> คราบที่ฝังอยู่แล้วต้องล้างออกก่อนทำ และผิวในร่มที่ฝนไม่โดนแดดไม่ส่องจะได้ผลน้อยกว่างานกลางแจ้งมาก รายละเอียดข้อจำกัดของแต่ละผิวอยู่ในหัวข้อ "ความจริงที่ต้องพูด" ของหน้าสินค้าแต่ละตัว',
        ]),
        ("06", "ผิวของคุณคือแบบไหน — ไปตัวไหน", [
            'หลักการเดียวกัน แต่ผิวต่างกันต้องการสูตรต่างกัน กระจกไม่ดูดน้ำ สีโรงงานบน ACP ไม่ดูดน้ำ แต่หินกับคอนกรีตดูดน้ำ จึงต้องมีรองพื้นซึมลึกเพิ่มอีกชั้น ส่วนแผงโซลาร์ต้องคงแสงผ่านให้ได้มากที่สุด',
            dcards([
                ("กระจก", "Glass Coating", "กระจกอาคาร หน้าต่าง ราวกระจก — ฟิล์มใสให้ฝนล้างกระจกแทน แสงผ่านเท่าเดิม", "/glasscoating"),
                ("ผิวสี · ACP · โลหะพ่นสี", "Paint Coating", "แผง ACP ป้ายปั๊ม เมทัลชีท ตัวถังรถ — ผิวไม่ดูดน้ำ ชั้นเดียวจบ", "/paintcoating"),
                ("หิน · คอนกรีต · GRC", "Stone Coating", "แกรนิต หินอ่อน GRC คอนกรีตเปลือย — ระบบ 2 ชั้น รองพื้นซึมลึกก่อนแล้วเคลือบผิว", "/stonesurface"),
                ("แผงโซลาร์", "Solar Panel Defender", "แผงบนหลังคาบ้านถึงโซลาร์ฟาร์ม — ลดฝุ่นเกาะ ลดรอบล้าง", "/solarpaneldefender"),
            ], "ดู"),
        ]),
    ],
    gal_h="ทำครึ่ง ไม่ทำครึ่ง — ผิวอื่นๆ ทั้งชุด",
    gal_alt="ภาพเทียบผิวที่เคลือบ Self-Cleaning ครึ่งเดียว หลังโดนอากาศจริง",
    prods='<div class="prods"><span class="lbl">สินค้าในสายนี้:</span><a href="/glasscoating">Glass Coating</a><a href="/paintcoating">Paint Coating</a><a href="/stonesurface">Stone Coating</a><a href="/solarpaneldefender">Solar Panel Defender</a></div>\n  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>\n',
)

# ─────────────────────────── EN ───────────────────────────
EN = dict(
    title="How Self-Cleaning Works — Rain Washes, Sun Digests, and What It Has Proven So Far",
    desc="The technology behind our Glass, Paint, Stone and Solar coatings, explained once — why we chose the superhydrophilic route over the lotus effect, the dust-rain-oil comparison tests, half-treated surfaces in the field, and measured gains at six solar plants",
    eyebrow="Case Study · Coatings / Self-Cleaning",
    meta="Published Sept 2026 · Test photos and project data from the raw-material developer (Changsha, China)",
    intro=[
        'Our self-cleaning family has four products — <a href="/en/glasscoating">Glass Coating</a>, <a href="/en/paintcoating">Paint Coating</a>, <a href="/en/stonesurface">Stone Coating</a> and <a href="/en/solarpaneldefender">Solar Panel Defender</a>. They differ in the surface they are made for, but the principle is the same. This page explains that principle once, then shows what it went through in the lab and on site before we chose to import the core raw material directly from the developer of the technology (Feibo, Changsha, China). The test photos and project data here are theirs; we kept only what comes with a place, a year and a number.',
        '"Coat it and it cleans itself" sounds like ad copy until you see how rain and sunlight are put to work — starting with the single drop of water in the photo above.',
    ],
    hero=("A round water droplet on a water-repellent coating next to water spread into a thin sheet on a self-cleaning coating",
          "Same surface, two behaviours — left: water beads up (hydrophobic) · right: water spreads into a thin sheet (superhydrophilic). Our family is the one on the right"),
    steps=[
        ("01", "Two routes to \"self-cleaning\" — and why we didn't pick the lotus leaf", [
            'Self-cleaning surfaces are classified by what water does on them. Route one is <b>superhydrophobic</b> — make the surface repel water to the extreme, contact angle above 150°, water beads up and rolls off (the lotus effect). Route two is <b>superhydrophilic</b> — the exact opposite: make the surface love water, contact angle below 10°, so water never beads but spreads into a thin sheet over the whole face.',
            'The lotus leaf sounds cooler, but on a building it has two weak points. First, a rolling droplet only carries dry dust — oil film, exhaust soot and sticky grime stay where they are. Second, droplets too small to roll dry in place and leave spot marks. With the thin-sheet route, rain flows in <b>under</b> the dirt, lifts it and carries it down as one sheet, leaving no droplets to dry into spots. That is why all four of our products sit on the superhydrophilic side.',
            'Two more mechanisms work inside the film — <b>photocatalysis</b>: nano titanium dioxide that sunlight activates to keep breaking down organic grime (oil, soot, mould) on the surface, and an <b>anti-static</b> effect so dust struggles to settle in the first place. The net result: less dust lands, sunlight digests what does, rain washes off the rest.',
            fig(H(2), "Contact-angle instrument with a screen showing a water droplet on a test piece",
                "The contact-angle instrument — the one number that tells you which side a film is on: below 10° is superhydrophilic, above 150° is lotus"),
        ]),
        ("02", "The comparison set — dust, rain and oil on the same panel", [
            'The test that says it all: take two panels of the same colour, one with the self-cleaning coating, one with an ordinary water-repellent coating, and do three things to them side by side.',
            '<b>A · Fly ash</b> — power-station fly ash, which clings harder than ordinary dust. The anti-static self-cleaning panel holds visibly less. <b>B · Simulated rain</b> — on the self-cleaning panel water spreads into a sheet, lifts the dust and carries all of it down; on the repellent panel large drops roll off but small ones stay and dry into spots. <b>C · Oil then rain</b> — the superhydrophilic surface grabs water before oil, so water slides under the oil and floats it away; an ordinary repellent surface cannot stop sticky oil adhering and plain water will not shift it.',
            fig(H(3), "Three comparison test photos: fly ash, simulated rain and oil drops on two red panels",
                "Left to right: A fly ash · B rain · C oil — each photo is the two coatings side by side, run at the same time under the same conditions"),
            fig(H(4), "Test lab: contact-angle measurement, abrasion tester, and dust sprinkled on a solar panel",
                "In the raw-material developer's lab — contact-angle measurement, abrasion testing, and dust sprinkled on a solar panel before rinsing"),
        ]),
        ("03", "In the field — the proof you can't fake is treating only half", [
            'Lab tests show the mechanism works; what a customer wants to know is how long it lasts in real sun and rain. The most direct answer is to <b>treat only half of the same surface</b> and let both halves take the weather together for months. The line you see is the edge of the treated area — not washed, not retouched.',
            fig("/img/stonesurface-proof01.webp", "GRC wall of an arts centre, left side coated and clean white, right side uncoated, yellowed with water streaks",
                'GRC facade, Meixihu Arts Centre, Changsha — one continuous panel, left treated, right not (<a href="/en/post/feibo-meixihu-grc">read the full case →</a>)'),
            'The same was done on many other surfaces — granite, ACP panels, stainless lift doors, air-conditioner aluminium fins, textured paint, a high-speed train nose and solar panels — collected in the gallery at the end of this page. The largest job in the set is the stone sculpture on Orange Isle (Juzizhou), Changsha, maintained in October 2023: a rock face that used to carry rain streaks and penetrating stains, still clean after the system went on.',
            fig(H(5), "Scaffolding around a large stone sculpture during maintenance, and the sculpture after the work",
                "Orange Isle stone sculpture, Changsha — left: during the work, Oct 2023, scaffolded for cleaning and coating · right: after completion"),
        ]),
        ("04", "Numbers you can measure — six solar plants", [
            'The surface where the result turns into a hard number is a solar panel, because settled dust translates directly into lost electricity. The raw-material developer recorded gains at six plants it treated, with the delivery date of each.',
            table(["Solar plant", "Delivered", "Extra output"], PV_ROWS_EN, right_last=True),
            'The spread from +2.9% to +5% follows how dusty each site is — at 1 GW even the lowest figure pays for the coating within the first year. For a Thai home or factory with a few dozen panels, what you actually get is <b>far fewer trips onto the roof to wash</b>. Home-scale figures are on the <a href="/en/solarpaneldefender">Solar Panel Defender</a> page.',
            fig(H(6), "Same row of solar panels, left side coated and clear, right side uncoated with dust settled",
                "Same row, same day — left: coated · right: not yet coated, dust settled enough to change the panel colour"),
            fig(H(7), "Crew coating solar panels at an outdoor power plant", "Plant work — coated row by row while the plant kept generating"),
        ]),
        ("05", "Against the two methods everyone uses today", [
            'A stained facade has always had two options — hire a wash, or repaint. This table puts the self-cleaning system next to them.',
            table(["", "Repeated washing", "Repainting", "Self-cleaning coating"], [
                ("How long it lasts", "One wash holds for a few months; the acidic cleaners used round after round yellow stone and paint and age them faster", "Peeling and blistering within 2–3 years, and rain streaks return after a few rains", "The developer specifies 3–5 years per application; a clear film that changes neither colour nor texture"),
                ("The work", "Climbing or abseiling every round, each taking weeks, with height risk every time", "Wash, sand, primer, mid-coat, top-coat — days, several crews", "Clean the surface and apply one thin coat (stone gets one extra primer layer); rain and sun do the rest"),
                ("Doing it again", "Every wash wears the surface a little more; cost rises every year", "Next time the old paint has to be stripped first", "At the end of the cycle, re-apply over the same surface after washing off the dust"),
            ], bold_first=True),
            'What the table does not say, and we want you to know first — this system <b>protects, it does not clean</b>: staining already embedded has to be removed before application, and a sheltered surface that rain never reaches and sun never hits gets far less of the effect than an outdoor one. The limits for each surface are in the "Straight Talk" section of each product page.',
        ]),
        ("06", "Which surface is yours — and which product", [
            'Same principle, but different surfaces need different formulations. Glass does not absorb water; factory paint on ACP does not absorb water; stone and concrete do, so they need an extra penetrating primer; and a solar panel has to keep light transmission as high as possible.',
            dcards([
                ("Glass", "Glass Coating", "Building glass, windows, glass balustrades — a clear film that lets rain wash the glass for you, light transmission unchanged", "/en/glasscoating"),
                ("Paint · ACP · coated metal", "Paint Coating", "ACP panels, fuel-station signage, metal sheet, vehicle bodies — non-absorbent surfaces, one coat", "/en/paintcoating"),
                ("Stone · concrete · GRC", "Stone Coating", "Granite, marble, GRC, fair-faced concrete — a two-layer system, penetrating primer first, then the topcoat", "/en/stonesurface"),
                ("Solar panels", "Solar Panel Defender", "From a house roof to a solar farm — less dust settling, fewer washing rounds", "/en/solarpaneldefender"),
            ], "See"),
        ]),
    ],
    gal_h="Half Treated, Half Not — the Rest of the Set",
    gal_alt="Surface coated with self-cleaning on one half only, after real weather exposure",
    prods='<div class="prods"><span class="lbl">Products in this family:</span><a href="/en/glasscoating">Glass Coating</a><a href="/en/paintcoating">Paint Coating</a><a href="/en/stonesurface">Stone Coating</a><a href="/en/solarpaneldefender">Solar Panel Defender</a></div>\n  <a class="back" href="/en/casestudy/">← Back to all case studies</a>\n',
)


def render(d):
    hero_fig = fig(H(1), d["hero"][0], d["hero"][1], hero=True)
    steps = "".join(step(n, h2, parts) for n, h2, parts in d["steps"])
    return ("  <article>\n" + f'    <p>{d["intro"][0]}</p>\n' + hero_fig
            + "".join(f"    <p>{p}</p>\n" for p in d["intro"][1:]) + steps
            + f'    <section class="step">\n      <h2><span class="n">📷</span>{d["gal_h"]}</h2>\n      {gallery_html(d["gal_alt"])}\n    </section>\n'
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
    og = f"https://www.lucernapro.com/img/post/{SLUG}-h1.webp"
    transplant(os.path.join(ROOT, "post", SRC, "index.html"), os.path.join(ROOT, "post", SLUG, "index.html"),
               TH["title"], TH["desc"], TH["eyebrow"], TH["meta"], render(TH), og)
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"), os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN["title"], EN["desc"], EN["eyebrow"], EN["meta"], render(EN), og)
