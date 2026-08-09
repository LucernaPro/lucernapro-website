# -*- coding: utf-8 -*-
"""
build_silo_post.py — เปิดเคสไซโล (V1 "ชมพลังของ-deepstick-กันชัดๆ") กลับขึ้น /casestudy
ด้วยวิธี chrome-transplant จากโพสต์ solar (dark theme + favicon ครบ)
เนื้อหาไทย = คำต่อคำจาก V1 (Wix migration) / EN = แปลจากต้นฉบับ
รูป: ไฟล์ local ทั้งหมด (ต้นฉบับจาก Pist ส.ค. 2026 — เลิกพึ่ง wixstatic แล้ว)
รัน: python3 tools/build_silo_post.py (จาก root ของ repo)
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "deepstick-factory-silo-joints"

LOCAL_GALLERY = [
 "deepstick-factory-silo-joints-g01",
 "deepstick-factory-silo-joints-g02",
 "deepstick-factory-silo-joints-g03",
 "deepstick-factory-silo-joints-g04",
 "deepstick-factory-silo-joints-g05",
 "deepstick-factory-silo-joints-g06",
 "deepstick-factory-silo-joints-g07",
 "deepstick-factory-silo-joints-g08",
 "deepstick-factory-silo-joints-g09",
 "deepstick-factory-silo-joints-g10",
 "deepstick-factory-silo-joints-g11",
 "deepstick-factory-silo-joints-g12",
 "deepstick-factory-silo-joints-g13",
 "deepstick-factory-silo-joints-g14",
 "deepstick-factory-silo-joints-g15",
 "deepstick-factory-silo-joints-g16",
 "deepstick-factory-silo-joints-g17",
 "deepstick-factory-silo-joints-g18",
 "deepstick-factory-silo-joints-g19",
 "deepstick-factory-silo-joints-g20",
 "deepstick-factory-silo-joints-g21",
 "deepstick-factory-silo-joints-g22",
 "deepstick-factory-silo-joints-g23",
 "deepstick-factory-silo-joints-g24",
 "deepstick-factory-silo-joints-g25",
 "deepstick-factory-silo-joints-g26",
 "deepstick-factory-silo-joints-g27",
 "deepstick-factory-silo-joints-g28",
 "deepstick-factory-silo-joints-g29",
 "deepstick-factory-silo-joints-g30",
 "deepstick-factory-silo-joints-g31",
 "deepstick-factory-silo-joints-g32",
 "deepstick-factory-silo-joints-g33",
 "deepstick-factory-silo-joints-g34",
 "deepstick-factory-silo-joints-g35",
 "deepstick-factory-silo-joints-g36",
 "deepstick-factory-silo-joints-g37",
 "deepstick-factory-silo-joints-g38",
]

GRID_STYLE = ("display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));"
              "gap:10px;margin-top:26px")

def gallery_html(alt_prefix):
    imgs = "".join(
        f'<img src="/img/post/{n}.webp" alt="{alt_prefix} {i+1:02d}" loading="lazy" '
        f'width="800" height="800" style="border-radius:10px;border:1px solid var(--line)">\n'
        for i, n in enumerate(LOCAL_GALLERY))
    return '<div style="' + GRID_STYLE + '">\n' + imgs + '</div>'

TH_TITLE = "ชมพลังของ DeepStick กันชัดๆ — งานรอยต่อไซโลบนดาดฟ้าโรงงานใหญ่ระดับประเทศ"
TH_DESC = ("งานรอยต่อที่โหดที่สุดที่เราเคยเจอ: ไซโลบนดาดฟ้าโรงงานใหญ่อันดับต้นๆ ของไทย เจาะทะลุพื้นปูน "
           "แรงสั่นสะเทือนตลอดเวลา ตัวโป๊วและซิลิโคนทั่วไปเอาไม่อยู่ — โป๊วจบด้วย DeepStick แล้วเคลือบทับด้วย "
           "Polyurea Gen3 สามรอบ พร้อมภาพหน้างานจริงกว่า 40 ภาพ")
TH_EYEBROW = "Case Study · รอยต่อ / รอยร้าว"
TH_META = "เผยแพร่ ก.พ. 2024 · โดยทีมงาน LucernaPro"

TH_BODY = f"""  <article>
    <p>งานรอยต่อที่ยากมากๆ สำหรับเราคงไม่มีงานไหนเกินงานนี้แล้ว</p>
    <figure class="hero"><img src="/img/post/{SLUG}-h1.webp" alt="ไซโลสเตนเลสบนดาดฟ้าโรงงาน แนวโป๊ว DeepStick รอบฐานปูนโอบก่อนเคลือบระบบทับ" width="1600" height="1200"><figcaption>หน้างานจริง: รอบฐานไซโล อัด DeepStick ตามแนวรอยต่อปูนโอบให้เต็มก่อนเคลือบระบบทับ</figcaption></figure>
    <p>เป็นไซโลในโรงงานที่ใหญ่อันดับต้นๆ ของไทย ตั้งอยู่บนดาดฟ้าเจาะทะลุขึ้นมาจากพื้นปูน มีแรงสั่นสะเทือนตลอดเวลา งานนี้มีการทำปูนโอบไว้อย่างดีก็ยังมีรอยรั่วลงไปชั้นล่าง ใช้ตัวโป๊วหรือซิลิโคนทั่วไปไม่ได้เลย</p>
    <figure><img src="/img/post/{SLUG}-h2.webp" alt="แนวพื้นชนผนังปูนโอบและขาโครงเหล็ก อัด DeepStick เต็มแนวแล้วเคลือบ Polyurea Gen3 ทับ" loading="lazy" width="1600" height="1200"><figcaption>แนวพื้นชนผนังและขาโครงเหล็ก — จุดที่รับแรงสั่นตลอดเวลา อัด DeepStick ให้เต็มแนวก่อนเคลือบทับ</figcaption></figure>
    <p>งานนี้ DeepStick แก้ปัญหาได้เรียบร้อยด้วยคุณสมบัติที่ไม่เหมือนใคร เป็นตัวโป๊วที่ยืดหยุ่นแต่มีความเหนียวแน่นในตัวและแรงยึดเกาะสูงมากแม้บนพื้นผิวแปลกๆ แทบจะเรียกว่าพื้นผิวแบบไหนก็โป๊วได้</p>
    <figure><img class="tall" src="/img/post/{SLUG}-h3.webp" alt="ซูมแนวโป๊ว DeepStick อัดแน่นเต็มร่องบนแนวตาข่ายเสริมแรง" loading="lazy" width="1200" height="1600"><figcaption>ซูมแนวโป๊ว: เนื้อ DeepStick อัดแน่นต่อเนื่องเต็มร่องบนแนวตาข่ายเสริมแรงของระบบ</figcaption></figure>
    <figure><img class="tall" src="/img/post/{SLUG}-h4.webp" alt="รอยต่อรูปตัว T บนพื้นดาดฟ้า อัด DeepStick เต็มแนว" loading="lazy" width="1200" height="1600"><figcaption>รอยต่อรูปตัว T บนพื้น — โป๊วให้เต็มทุกแนว ไม่ขาดช่วง</figcaption></figure>
    <figure><img class="tall" src="/img/post/{SLUG}-h5.webp" alt="แนวโค้งรอบปูนโอบฐานไซโล โป๊ว DeepStick ต่อเนื่องตลอดแนว" loading="lazy" width="1200" height="1600"><figcaption>แนวโค้งรอบปูนโอบ — โป๊วต่อเนื่องตลอดแนวโค้ง ไม่มีจุดเริ่ม-จุดจบให้น้ำแทรก</figcaption></figure>
    <p>หลังจากโป๊วให้ทั่วแล้วก็ทาทับพื้นที่ด้วยกันซึมตัว Top ของเราด้วย Polyurea Gen3 ปกติทาเพียง 2 รอบก็พอแต่งานนี้ทา 3 รอบไปเลยเพื่อให้ใช้งานได้ยาวนานยิ่งกว่าเดิม</p>
    <figure><img class="tall" src="/img/post/{SLUG}-h6.webp" alt="ทางเดินระหว่างไซโลหลังเคลือบ Polyurea Gen3 ทั้งผืน" loading="lazy" width="1200" height="1600"><figcaption>งานจบ: ทางเดินระหว่างไซโลเคลือบ Polyurea Gen3 ต่อเนื่องทั้งผืน จบทุกแนวรอยต่อในระบบเดียว</figcaption></figure>
    <section class="step">
      <h2><span class="n">📷</span>ภาพหน้างานเพิ่มเติมทั้งชุด — ไล่ดูทีละขั้นได้เลย</h2>
      {gallery_html("งานรอยต่อไซโล DeepStick — ภาพหน้างานจริง")}
    </section>
  </article>
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/deepstick">DeepStick</a><a href="/polypro">Polyurea Gen3</a></div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
"""

EN_TITLE = "DeepStick at Full Power — Silo Joints on a Factory Rooftop, Our Hardest Joint Job Ever"
EN_DESC = ("The hardest joint repair we have ever taken on: silos at one of Thailand's largest factories, punching "
           "through a rooftop concrete deck with constant vibration. Ordinary fillers and silicone stood no chance — "
           "sealed with DeepStick, then coated with three coats of Polyurea Gen3. 40+ real jobsite photos.")
EN_EYEBROW = "Case Study · Joints / Cracks"
EN_META = "Published Feb 2024 · by the LucernaPro team"

EN_BODY = f"""  <article>
    <p>Of all the joint repairs we have ever taken on, nothing has come close to this one.</p>
    <figure class="hero"><img src="/img/post/{SLUG}-h1.webp" alt="Stainless silos on a factory rooftop, DeepStick sealed along the concrete collar joint before topcoating" width="1600" height="1200"><figcaption>The real site: DeepStick packed full along the collar joint around the silo base, before the topcoat system goes on</figcaption></figure>
    <p>These are silos at one of Thailand's largest factories, mounted on the rooftop and punching through the concrete deck, vibrating constantly. Even with concrete collars cast carefully around them, water still leaked to the floor below — ordinary fillers and silicone sealants stood no chance here.</p>
    <figure><img src="/img/post/{SLUG}-h2.webp" alt="Wall-to-floor joint and steel bracket sealed full with DeepStick, coated over with Polyurea Gen3" loading="lazy" width="1600" height="1200"><figcaption>The wall-to-floor line and a steel support leg — under constant vibration, packed full with DeepStick before coating over</figcaption></figure>
    <p>DeepStick closed this job with a property set nothing else has: a filler that is flexible yet dense and tenacious in body, with extremely high adhesion even on unusual surfaces — you could almost say there is no surface it won't bond to.</p>
    <figure><img class="tall" src="/img/post/{SLUG}-h3.webp" alt="Close-up of the DeepStick bead packed full over the reinforcing mesh line" loading="lazy" width="1200" height="1600"><figcaption>Close-up: DeepStick packed dense and continuous over the system's reinforcing mesh line</figcaption></figure>
    <figure><img class="tall" src="/img/post/{SLUG}-h4.webp" alt="T-shaped joint on the deck sealed full with DeepStick" loading="lazy" width="1200" height="1600"><figcaption>A T-shaped joint on the deck — every line filled, no breaks</figcaption></figure>
    <figure><img class="tall" src="/img/post/{SLUG}-h5.webp" alt="The curved collar joint around the silo base sealed continuously with DeepStick" loading="lazy" width="1200" height="1600"><figcaption>The curved collar line — sealed in one continuous run, no start-stop points for water to find</figcaption></figure>
    <p>After every joint was sealed, the whole area was coated over with our top waterproofing, Polyurea Gen3. Two coats are normally enough — this job got three, for an even longer service life.</p>
    <figure><img class="tall" src="/img/post/{SLUG}-h6.webp" alt="Walkway between silos after full Polyurea Gen3 coating" loading="lazy" width="1200" height="1600"><figcaption>Finished: the walkway between silos coated wall-to-wall in Polyurea Gen3, every joint closed in one system</figcaption></figure>
    <section class="step">
      <h2><span class="n">📷</span>More Jobsite Photos — Step Through the Whole Job</h2>
      {gallery_html("DeepStick silo joint job — real jobsite photo")}
    </section>
  </article>
  <div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/deepstick">DeepStick</a><a href="/en/polypro">Polyurea Gen3</a></div>
  <a class="back" href="/en/casestudy/">← Back to all case studies</a>
"""

def transplant(src_path, out_path, title, desc, eyebrow, h1, meta, body, og_img):
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
                f"  <h1>{h1}</h1>\n"
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
               TH_TITLE, TH_DESC, TH_EYEBROW, TH_TITLE, TH_META, TH_BODY, og)
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"),
               os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN_TITLE, EN_DESC, EN_EYEBROW, EN_TITLE, EN_META, EN_BODY, og)
