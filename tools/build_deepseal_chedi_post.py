# -*- coding: utf-8 -*-
"""
build_deepseal_chedi_post.py — เคส DeepSeal บนรอยต่อภายในองค์เจดีย์ จ.กาฬสินธุ์ (ก.ย. 2026)
ภาพจากทีมผู้รับเหมาที่ใช้งานจริง ส่งผ่าน Pist 5 ก.ย. 2026 — เปิดเป็นเคสของตัวเอง ไม่รวมกับภาพผู้ใช้อื่น
วิธี: chrome-transplant จากโพสต์ solar เหมือน build_silo_post.py — TH+EN
รูป: /img/post/{slug}-h*.webp (narrative, ไม่ upscale — ต้นฉบับยาวสุด 1280) + -g*.webp (800x800)
จุดยืนเจ้าของ (บันทึกไว้ในเนื้อหา): ภายในคือสนามของ DeepSeal / ด้านนอกลูกค้าใช้ตรงรอยต่อกระเบื้องเอง
เราไม่แนะนำ ถ้าใช้ต้องทาสีหรือกันซึมทับเพื่อกันแดด
รัน: python3 tools/build_deepseal_chedi_post.py (จาก root ของ repo)
"""
import os, re
from PIL import Image, ImageOps, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "deepseal-chedi-joints-kalasin"
UP = "/mnt/user-data/uploads"

# ต้นฉบับ → ชื่อไฟล์ (h = narrative ตามลำดับเล่าเรื่อง, g = gallery 800x800)
NARR = [
 ("9E4DB15D-63EF-4B6F-B4B4-DBABBD7AF978.jpeg", 1),  # องค์เจดีย์
 ("B69A4F8D-DC3E-4AE5-A4D4-09D329F4E1A0.jpeg", 2),  # รอยแยกแนวรอยต่อผนัง-เสา
 ("C1995A94-19E5-4F84-9E77-EEEC9DC20149.jpeg", 3),  # แปรงทาแนวรอยต่อตั้ง
 ("F1902B01-34D7-4976-B5C9-BFA5D385BDE3.jpeg", 4),  # รอยต่อเพดาน-คาน
 ("648D02DA-39FA-4B43-A186-DF3C11E5EE27.jpeg", 5),  # แนวผนังชนพื้นใต้หน้าต่าง
 ("F9661D10-93B7-408D-B21C-CAE52881CD67.jpeg", 6),  # ด้านนอก ทาบนกระเบื้ององค์เจดีย์
 ("6577F823-DBA0-4C15-9766-9B62E057BD19.jpeg", 7),  # โรยตัวบนองค์เจดีย์
 ("9FF30F51-877A-4049-81C6-9E00F94B9D41.jpeg", 8),  # จุดตั้งอุปกรณ์บนยอด
]
GAL = [
 "48EDE73F-5A47-4069-98C8-C1A03988E3FD.jpeg",
 "B729CC58-B72B-43A0-A198-5FD169EFA1B6.jpeg",
 "402C06EC-4087-4C2D-B41F-0662083B8EEA.jpeg",
 "45F61B11-EA15-44F8-AC46-5317866D2AD8.jpeg",
 "AFF4A267-A805-4137-97DF-C6B3B6DDE0F6.jpeg",
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

# รูปต้องพร้อมก่อน เพราะ f-string ของ body อ่านขนาดรูปตอนโหลดโมดูล
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
TH_TITLE = "DeepSeal บนรอยต่อภายในองค์เจดีย์ กาฬสินธุ์ — งานรอยต่อบนที่สูงที่ทีมช่างเลือกทาจากด้านใน"
TH_DESC = ("ภาพหน้างานจริงจากทีมผู้รับเหมา: องค์เจดีย์สูงใน จ.กาฬสินธุ์ รอยต่อระหว่างผนังกับเสา แนวผนังชนพื้น และรอยต่อคาน-เพดานภายใน "
           "ทา DeepSeal ด้วยแปรงจากด้านใน — พร้อมภาพงานด้านนอกบนกระเบื้ององค์เจดีย์ที่ทีมช่างเลือกใช้เอง และเหตุผลที่เราแนะนำให้ทาทับเสมอเมื่อใช้กลางแจ้ง")
TH_EYEBROW = "Case Study · รอยต่อ / รอยร้าว"
TH_META = "เผยแพร่ ก.ย. 2026 · ภาพหน้างาน 4–5 ก.ย. 2026 จากทีมผู้รับเหมาที่ใช้งาน"

TH_BODY = f"""  <article>
    <p>เคสนี้เป็นภาพที่ทีมผู้รับเหมาส่งมาให้เราหลังใช้ <a href="/deepseal">DeepSeal</a> กับงานรอยต่อบนองค์เจดีย์สูงใน จ.กาฬสินธุ์ — เราลงทั้งชุดตามที่ภาพบอก ไม่แต่ง ไม่เพิ่มเรื่อง และจะบอกตรงๆ ด้วยว่าส่วนไหนคือสนามของ DeepSeal จริง และส่วนไหนที่เราไม่แนะนำ</p>
{fig(1,'องค์เจดีย์สีอิฐสูงใหญ่ มองจากฐานขึ้นไปถึงยอด ท้องฟ้ามีเมฆ','องค์เจดีย์ที่เป็นหน้างานของเคสนี้ — ภายในมีทางเดินและช่องหน้าต่างหลายชั้น ด้านนอกกรุกระเบื้องทั้งองค์',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>ปัญหาอยู่ที่รอยต่อ ไม่ใช่ที่ผนัง</h2>
      <p>ภาพระยะใกล้จากภายใน: แนวรอยต่อระหว่างผนังกับเสามีรอยแยกเป็นเส้นยาวตลอดแนว ผิวปูนสองฝั่งยังแน่นดี แต่จุดที่สองชิ้นมาชนกันคือช่องที่น้ำจะหาเจอเสมอ — สิ่งก่อสร้างสูงและกว้างแบบนี้ ผนัง เสา คาน ขยับตัวไม่เท่ากันตามอุณหภูมิ รอยต่อจึงเป็นจุดแรกที่เปิด</p>
{fig(2,'รอยแยกแนวตั้งยาวตลอดแนวรอยต่อระหว่างผนังปูนกับเสาภายในองค์เจดีย์','แนวรอยต่อผนัง-เสาภายใน — รอยแยกเป็นเส้นต่อเนื่องตลอดความสูง นี่คือจุดที่ทีมช่างไล่ทา')}
      <p><b>กติกาข้อแรกที่ต้องย้ำก่อนพูดถึงน้ำยาตัวไหนทั้งนั้น: รอยต่อที่แยกเป็นร่องแบบนี้ ต้องโป๊วอุดให้เต็มก่อนเสมอ — ไม่โป๊วก่อน ทาอะไรทับไปก็เอาไม่อยู่</b> DeepSeal เป็นน้ำยาซึม มีไว้ปิดรูพรุนและรอยร้าวเส้นผมในเนื้อปูน มันไม่ใช่ตัวถมร่อง ร่องที่มองเห็นเป็นช่องคือช่องที่ฟิล์มบางๆ จะแขวนข้ามแล้วขาดในที่สุด รอยต่อผนังทั่วไปโป๊วด้วย <a href="/fillerace">FillerAce</a> · รอยต่อที่ขยับตัวหรือเป็นจุดยากอย่างผนังชนเสาบนที่สูงแบบนี้ ใช้ <a href="/deepstick">DeepStick</a> อัดให้เต็มแนว — รอแห้งเรียบร้อยแล้วค่อยทา DeepSeal ทับให้ชุ่มทั้งแนว</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>ภายใน — ทาด้วยแปรง ไล่ตามแนวรอยต่อ</h2>
      <p>ภาพชุดนี้คือสนามของ DeepSeal ตรงๆ: <b>งานภายในอาคาร บนปูนเปลือย ทาให้ชุ่มตามแนวรอยต่อ</b> ทีมช่างใช้แปรงทาไล่ตามรอยต่อผนัง-เสา แนวผนังชนพื้นใต้หน้าต่าง และรอยต่อคาน-เพดาน ในภาพเห็นเนื้อน้ำยาใสอมเหลืองซึมลงตามแนวรอยแยก ซึ่งเป็นสีจริงของฟิล์ม DeepSeal ตามที่เราเขียนไว้บนหน้าสินค้า</p>
{fig(3,'มือถือแปรงทา DeepSeal ตามแนวรอยต่อตั้งระหว่างผนังกับเสา เห็นน้ำยาใสอมเหลืองซึมตามรอยแยก','ทาให้ชุ่มตามแนวรอยแยก — น้ำยาใสอมเหลืองซึมลงในร่อง ไม่ใช่เคลือบอยู่บนผิว')}
{fig(4,'ช่างสวมสายรัดนิรภัยยืนบนที่สูงใช้แปรงทาแนวรอยต่อระหว่างคานกับเพดานภายใน ผนังด้านล่างมีคราบน้ำ','รอยต่อคาน-เพดาน — ผนังด้านล่างมีคราบน้ำไหลเป็นทางให้เห็น ทีมช่างรัดสายนิรภัยขึ้นทาที่แนวรอยต่อด้านบน')}
{fig(5,'ช่างนั่งยองใช้แปรงทา DeepSeal แนวผนังชนพื้นใต้แนวหน้าต่างกระจกภายในองค์เจดีย์','แนวผนังชนพื้นใต้แนวหน้าต่าง — มุมฉากที่ผนังตั้งชนพื้นราบคือรอยต่ออันดับต้นๆ ที่เรารู้จักดี')}
      <p>วิธีใช้ที่ถูกต้องบนหน้างานแบบนี้คือแบบเดียวกับที่เขียนไว้บนหน้า <a href="/deepseal">DeepSeal</a>: เปิดผิวถึงปูนเปลือย ห้ามมีน้ำขัง ทาให้ชุ่มเน้นรอยต่อและมุม ถ้าผิวพรุนจัดทารอบสองตัดขวางตอนรอบแรกเริ่มหมาด แล้วปล่อยเซ็ตตัวข้ามคืน 12–24 ชั่วโมงก่อนทำอะไรทับ — และย้ำอีกครั้ง: แนวที่แยกเป็นร่องต้องโป๊วให้เต็มก่อนถึงขั้นนี้ ไม่ใช่หวังให้น้ำยาถมร่องเอง</p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>ด้านนอกบนกระเบื้ององค์เจดีย์ — ทีมช่างเลือกใช้เอง และเราต้องพูดตรงๆ</h2>
      <p>ทีมช่างชุดเดียวกันโรยตัวลงไปทาตามแนวรอยต่อกระเบื้องด้านนอกองค์เจดีย์ด้วย ภาพสวยและงานเสี่ยงมาก — แต่เราจะไม่เขียนเชียร์ส่วนนี้ เพราะ<b>เราไม่แนะนำให้ใช้ DeepSeal กลางแจ้งแบบเปลือย</b> ฟิล์มระบบนี้โดนแดดโดยตรง<b>ไม่ใช่แค่เหลืองขึ้น — มันเสื่อมสภาพเร็วขึ้นด้วย</b> รังสี UV กัดเนื้อฟิล์มให้แข็งกรอบและอ่อนแรงลงเรื่อยๆ จนสิ่งที่ทาไปทำงานได้ไม่นานอย่างที่ควร มันถูกจูนมาเพื่องานภายในโดยเฉพาะ</p>
      <p><b>ถ้าจำเป็นต้องใช้กลางแจ้งจริงๆ กติกามีข้อเดียว: ต้องทาสีหรือกันซึมทับเสมอเพื่อกันแดด</b> ทาทับได้ตามปกติเมื่อแห้งสนิท — ชั้นทับคือสิ่งที่ทำให้ DeepSeal ข้างใต้อยู่ได้ยาว ปล่อยเปลือยไว้คือเอาของที่เกิดมาเพื่อในร่มไปยืนตากแดดทั้งปี แล้วรอวันที่มันหมดแรง</p>
      <p><b>แล้วงานด้านนอกแบบนี้ควรใช้อะไร?</b> ถ้าโจทย์คือรอยต่อกระเบื้องกลางแจ้งและต้องการความใสไม่เปลี่ยนหน้าตาองค์เจดีย์ เราแนะนำ <a href="/crystalseal">CrystalSeal</a> ตรงๆ — เคลือบใสสาย ClearFlex Polymer ที่เกิดมาเพื่อกระเบื้องกลางแจ้งโดยเฉพาะ ทนแดดฝน ยืดหยุ่นตามรอยต่อ และเหลืองช้ามาก ไม่ต้องหาอะไรมาทาทับอีกชั้น</p>
{fig(6,'ช่างสวมสายรัดนิรภัยคุกเข่าบนผิวกระเบื้องโค้งขององค์เจดีย์ ใช้แปรงทาตามแนวรอยต่อกระเบื้อง มีทุ่งนาอยู่ด้านล่าง','ด้านนอก: ทาตามแนวรอยต่อกระเบื้องบนผิวโค้ง — ส่วนนี้ทีมช่างเลือกใช้เอง เราแนะนำให้เคลือบทับเสมอ')}
{fig(7,'ช่างโรยตัวด้วยเชือกบนผิวกระเบื้องโค้งขององค์เจดีย์ มองเห็นทุ่งนาและบ้านเรือนด้านล่าง','งานโรยตัวบนองค์เจดีย์ — สายรัดนิรภัยและเชือกยึดจากยอด')}
{fig(8,'ช่างนั่งบนยอดองค์เจดีย์ข้างราวสเตนเลส จัดเชือกและอุปกรณ์ มีถังน้ำยาและแกลลอนวางอยู่','จุดตั้งอุปกรณ์บนยอด — ถังน้ำยา แกลลอน และเชือกยึดกับราวสเตนเลส')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>สรุปสำหรับคนที่มีงานคล้ายกัน</h2>
      <p><b>รอยต่อภายในอาคาร บนปูน ที่ออกไปซ่อมข้างนอกไม่ได้</b> — นี่คือสนามของ DeepSeal ทาด้วยแปรงตามแนวรอยต่อและมุม ให้ชุ่ม เซ็ตตัวข้ามคืน แล้วฉาบหรือทาสีทับได้ · <b>รอยต่อกลางแจ้ง</b> — ถ้าจะใช้ ต้องมีชั้นทับกันแดดเสมอ ไม่งั้นทั้งเหลืองและเสื่อมเร็ว — รอยต่อกระเบื้องกลางแจ้งที่เน้นความใส ใช้ <a href="/crystalseal">CrystalSeal</a> แทนตั้งแต่แรกจะตรงงานกว่า หรือถามเราก่อน · <b>รอยต่อที่แยกเป็นร่อง — โป๊วให้เต็มก่อนเสมอ ไม่โป๊วก่อน ทายังไงก็เอาไม่อยู่</b> น้ำยาซึมมีไว้ปิดรูพรุนและรอยร้าวเล็ก ไม่ใช่ถมร่อง</p>
      <p>งานลักษณะเดียวกันบนอาคารสูง วัด หรือโครงสร้างที่ขึ้นไปทำยาก ส่งรูปรอยต่อกับบอกว่าอยู่ด้านในหรือด้านนอกมาทางแชทเพจได้เลย เราชี้ให้ว่าจุดไหนใช้ตัวนี้ จุดไหนควรใช้ตัวอื่น</p>
{gallery_html('งานทา DeepSeal บนรอยต่อภายในและภายนอกองค์เจดีย์ กาฬสินธุ์ — ภาพหน้างานจริงจากทีมผู้รับเหมา')}
    </section>
  </article>
"""

# ─────────────────────────── EN ───────────────────────────
EN_TITLE = "DeepSeal on the Interior Joints of a Chedi in Kalasin — High-Level Joint Work the Crew Chose to Seal from Inside"
EN_DESC = ("Real site photos from a contractor crew: a tall chedi in Kalasin province, with wall-to-column joints, wall-to-floor lines and beam-to-ceiling joints "
           "brushed with DeepSeal from the inside — plus the exterior work on the chedi's tile cladding that the crew chose themselves, and why we always recommend coating over it outdoors")
EN_EYEBROW = "Case Study · Joints / Cracks"
EN_META = "Published Sep 2026 · Site photos 4–5 Sep 2026 from the contractor crew who used the product"

EN_BODY = f"""  <article>
    <p>These photos came to us from the contractor crew after they used <a href="/en/deepseal">DeepSeal</a> on the joints of a tall chedi (Buddhist stupa) in Kalasin province, north-east Thailand. We are publishing the set as the photos show it — no retouching, no added story — and we will say plainly which part is DeepSeal's home ground and which part we do not recommend.</p>
{fig(1,'Tall terracotta-coloured chedi seen from the base up to the spire against a cloudy sky','The chedi of this case — walkways and windows on several levels inside, tile cladding over the whole exterior',hero=True)}
    <section class="step">
      <h2><span class="n">01</span>The problem is the joint, not the wall</h2>
      <p>A close-up from inside: the joint between a wall panel and a column has opened into a continuous line along its full height. The render on both sides is still sound, but where two elements meet is the gap water will always find — on a structure this tall and wide, walls, columns and beams move differently with temperature, so the joints open first.</p>
{fig(2,'Long vertical gap along the joint between a rendered wall and a column inside the chedi','The interior wall-to-column joint — a continuous gap the full height. This is the line the crew worked along')}
      <p><b>Rule number one, before any product is mentioned: a joint that has opened into a gap like this must be filled full first — skip the filling and nothing you brush over it will hold.</b> DeepSeal is a penetrating liquid; it closes pores and hairline cracks in the render. It is not a gap filler. A gap you can see is a gap a thin film will bridge and eventually tear across. Ordinary wall joints: fill with <a href="/en/fillerace">FillerAce</a> · joints that move or are awkward, like a wall-to-column line at height, pack full with <a href="/en/deepstick">DeepStick</a> — let it dry properly, then brush DeepSeal generously over the whole line.</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>Inside — brushed along the joint lines</h2>
      <p>This set is DeepSeal's home ground, exactly as intended: <b>interior work, on bare render, brushed generously along the joints</b>. The crew brushed along the wall-to-column joint, the wall-to-floor line under the windows, and the beam-to-ceiling joint. In the photos you can see the clear amber liquid soaking into the gap — that is the real colour of the DeepSeal film, as stated on the product page.</p>
{fig(3,'Hand holding a brush applying DeepSeal along a vertical wall-to-column joint, clear amber liquid soaking into the gap','Brushed generously along the gap — the clear amber liquid soaks into the joint rather than sitting on the surface')}
{fig(4,'Worker in a safety harness standing at height brushing the beam-to-ceiling joint inside, water stains on the wall below','The beam-to-ceiling joint — the wall below shows water streaks. The crew clipped into a harness to work the joint line overhead')}
{fig(5,'Worker crouching, brushing DeepSeal along the wall-to-floor line below a run of windows inside the chedi','The wall-to-floor line below the windows — the right-angle where a wall meets a floor is one of the joints we know best')}
      <p>The correct method on a job like this is the one on the <a href="/en/deepseal">DeepSeal</a> page: open the surface to bare concrete, no standing water, brush generously with emphasis on joints and corners, add a second cross-wise coat while the first is going tacky if the surface is very porous, then leave it to set overnight — 12 to 24 hours — before doing anything over it. And once more: a line that has opened into a gap must be filled full before this step — do not expect the liquid to fill the trench.</p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>Outside, on the chedi's tiles — the crew's own choice, and we have to be straight about it</h2>
      <p>The same crew also abseiled down the outside and brushed along the tile joints of the chedi. Striking photos, and dangerous work — but we will not cheer this part, because <b>we do not recommend DeepSeal outdoors left bare</b>. In direct sun this film <b>does not just yellow — it degrades faster too</b>: UV attacks the film, making it brittle and progressively weaker, so what was applied stops doing its job well before it should. It is tuned specifically for interior work.</p>
      <p><b>If it must be used outdoors, there is one rule: always paint or waterproof over it to keep the sun off.</b> It takes a topcoat normally once fully dry — the covering layer is what lets the DeepSeal underneath last. Leaving it bare means taking a product born for indoor work, standing it in the sun all year, and waiting for it to give out.</p>
      <p><b>So what should exterior work like this use?</b> For outdoor tile joints where clarity matters — where the chedi must look untouched — our straight answer is <a href="/en/crystalseal">CrystalSeal</a>: a clear ClearFlex Polymer coating made specifically for outdoor tile, weather-resistant, flexible across the joint, and very slow to yellow, with no extra covering layer needed.</p>
{fig(6,'Worker in a harness kneeling on the curved tiled surface of the chedi, brushing along the tile joints, rice fields far below','Outside: brushing along the tile joints on the curved surface — the crew\'s own choice here; we recommend coating over it every time')}
{fig(7,'Worker on a rope on the curved tiled surface of the chedi, fields and houses far below','Rope work on the chedi — harness and rope anchored from the top')}
{fig(8,'Worker sitting at the top of the chedi beside a stainless rail, sorting ropes, with a bucket of liquid and a jerrycan','The set-up point at the top — bucket, jerrycan and the rope anchored to the stainless rail')}
    </section>
    <section class="step">
      <h2><span class="n">04</span>In short, for anyone with a similar job</h2>
      <p><b>Interior joints on render or concrete that cannot be repaired from outside</b> — DeepSeal's home ground: brush generously along joints and corners, let it set overnight, then skim or paint over · <b>Exterior joints</b> — if you use it, it needs a covering layer against the sun every time, otherwise it both yellows and degrades early — for outdoor tile joints where clarity matters, <a href="/en/crystalseal">CrystalSeal</a> from the start is the better fit; or ask us first · <b>Joints that have opened into a gap — fill them full first, every time; skip the filling and nothing brushed over will hold.</b> A penetrating liquid closes pores and fine cracks; it does not fill a trench.</p>
      <p>Similar work on tall buildings, temples or structures that are hard to reach: send photos of the joints and tell us whether they are inside or outside, and we will point out where this product fits and where another one should go.</p>
{gallery_html('DeepSeal work on the interior and exterior joints of a chedi in Kalasin — real site photos from the contractor crew')}
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
