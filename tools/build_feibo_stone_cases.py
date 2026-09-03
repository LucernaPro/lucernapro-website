# -*- coding: utf-8 -*-
"""
build_feibo_stone_cases.py — เคส Stone Coating จากโครงการของ Feibo (ผู้พัฒนาวัตถุดิบ, จีน) 4 เคส
feibo-meixihu-grc / feibo-minmetals-granite / feibo-jishou-station-marble / feibo-xiangxi-plaza-stone
วิธี: chrome-transplant จากโพสต์ solar (เหมือน build_feibo_paint_cases.py) — TH+EN
รูป: /img/post/{slug}-h*.webp (narrative) + -g*.webp (800x800) จากรูปที่ Lilian ส่ง ก.ย. 2026
รัน: python3 tools/build_feibo_stone_cases.py (จาก root ของ repo)
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

def step(n, h2, paras, figs):
    return (f'    <section class="step">\n      <h2><span class="n">{n}</span>{h2}</h2>\n'
            + "".join(f"      <p>{p}</p>\n" for p in paras) + "".join(figs) + "    </section>\n")

def body(slug, lang, intro, hero_fig, steps, ngal, gal_alt):
    prods = ('<div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/stonesurface">Stone Coating</a></div>\n  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>\n'
             if lang == "th" else
             '<div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/stonesurface">Stone Coating</a></div>\n  <a class="back" href="/en/casestudy/">← Back to all case studies</a>\n')
    galh = ("ภาพหน้างานเพิ่มเติมทั้งชุด" if lang == "th" else "More Site Photos — the Whole Set")
    return ("  <article>\n" + "".join(f"    <p>{p}</p>\n" for p in intro[:1]) + hero_fig
            + "".join(f"    <p>{p}</p>\n" for p in intro[1:]) + "".join(steps)
            + f'    <section class="step">\n      <h2><span class="n">📷</span>{galh}</h2>\n      {gallery_html(slug, ngal, gal_alt)}\n    </section>\n'
            + "  </article>\n  " + prods)

EYE_TH = "Case Study · เคลือบปกป้อง / Stone Coating"
EYE_EN = "Case Study · Coatings / Stone Coating"
META_TH = "เผยแพร่ ก.ย. 2026 · ภาพหน้างานจากทีม Feibo (ประเทศจีน) ผู้พัฒนาวัตถุดิบของเรา"
META_EN = "Published Sept 2026 · Site photos from the Feibo team (China), developer of our raw material"
DISC_TH = 'เคสนี้เป็นงานของ <b>Feibo</b> (ฉางชา ประเทศจีน) ผู้พัฒนาและผลิตวัตถุดิบหลักที่เราใช้ใน <a href="/stonesurface">Stone Coating</a> — ไม่ใช่งานของทีมเราในไทย เราลงไว้เพราะเป็นหน้างานประเภทที่ลูกค้าไทยถามถึงบ่อยที่สุด'
DISC_EN = 'This case is the work of <b>Feibo</b> (Changsha, China), the developer and producer of the core raw material in our <a href="/en/stonesurface">Stone Coating</a> — not our own crew in Thailand. We show it because it is exactly the kind of site Thai customers ask about most.'

CASES = []

# ───────── 1. Meixihu GRC ─────────
s = "feibo-meixihu-grc"
CASES.append(dict(slug=s, ngal=4,
 th=dict(title="ผนัง GRC ศูนย์ศิลปะเหมยซีหู — ผนังขาวโค้งที่เจ้าของไม่ยอมให้เหลือง",
  desc="โครงการของ Feibo บนผนัง GRC ของศูนย์ศิลปะเหมยซีหู ฉางชา — พ่นระบบ 2 ชั้นจากพื้นด้วยก้านยาว และแผง GRC เดียวกันทำครึ่ง/ไม่ทำครึ่ง ให้เห็นว่าเหลืองต่างกันแค่ไหน",
  intro=[DISC_TH, "GRC (คอนกรีตเสริมใยแก้ว) คือวัสดุที่สถาปนิกชอบเพราะหล่อเป็นผิวโค้งได้ไร้รอยต่อ — แต่มันพรุน ดูดน้ำ และเหลืองเร็วมากเมื่อเจอฝนกับฝุ่นเมือง ผนังสีขาวล้วนยิ่งฟ้องทุกคราบ"],
  hero=("ช่างใช้ก้านพ่นยาวเคลือบผนัง GRC สีขาวโค้งของศูนย์ศิลปะ","พ่นจากพื้นด้วยก้านยาว — ผนัง GRC โค้งขึ้นนั่งร้านยาก การพ่นจากพื้นคือวิธีที่ทั้งเร็วและปลอดภัยกว่า"),
  steps=[
   ("01","แผง GRC เดียวกัน ทำครึ่ง ไม่ทำครึ่ง",["ทีมงานทำระบบ 2 ชั้นไว้ฝั่งเดียวเป็นตัวเทียบแล้วปล่อยตามธรรมชาติ — ภาพนี้ไม่ได้ล้าง ไม่ได้แต่ง เส้นแบ่งคือขอบเขตที่ทำ"],[(2,"ผนัง GRC ฝั่งซ้ายเคลือบระบบ 2 ชั้นขาวสะอาด ฝั่งขวาไม่เคลือบเหลืองหม่นมีคราบน้ำไหล","ซ้าย: ทำแล้ว ขาวเรียบ · ขวา: ไม่ทำ เหลืองหม่นและคราบน้ำไหลเป็นทาง — GRC ต่อเนื่องชิ้นเดียวกัน")]),
   ("02","ทำไม GRC ต้องรองพื้นก่อนเคลือบผิว",["GRC ดูดน้ำเข้าไปในเนื้อ แล้วดันความชื้นและด่างออกมาเป็นคราบขาวและเหลืองจากข้างใน ถ้าเคลือบผิวอย่างเดียว คราบจะผุดทะลุขึ้นมาอยู่ดี — รองพื้นซึมลึกปิดรูพรุนก่อน แล้วเคลือบผิว Self-Cleaning ให้ฝนดูแลข้างนอก"],[(3,"ผนัง GRC สีขาวโค้งหลังทำระบบ","ผนังหลังทำ — ขาวเรียบทั้งผืน ผิว GRC ยังด้านเหมือนเดิม ไม่มีเงาแปลกปลอม"),(4,"ช่างพ่นผนัง GRC ด้วยก้านยาวจากพื้น มุมมองด้านข้าง","ไล่พ่นทีละแนวจากพื้น — ผนังโค้งยาวต้องต่อเนื่อง ไม่ให้ขอบแนวแห้งก่อน")]),
   ("03","ในไทยงานแบบนี้อยู่ตรงไหน",["ผนัง GRC ประดับอาคาร คิ้วบัว หัวเสาหล่อ ผนังคอนกรีตเปลือยของบ้านสไตล์ลอฟต์ รั้วปูนขัดมัน — ทั้งหมดคือวัสดุพรุนที่เหลืองและขึ้นราแบบเดียวกัน ระบบเดียวกันนี้ใช้ได้ตรงๆ"],[]),
  ], gal_alt="งานผนัง GRC ศูนย์ศิลปะเหมยซีหู โดยทีม Feibo — ภาพหน้างานจริง"),
 en=dict(title="The GRC Facade of Meixihu Arts Centre — Curved White Walls the Owner Would Not Let Turn Yellow",
  desc="A Feibo project on the GRC facade of the Meixihu Arts Centre, Changsha — the two-layer system sprayed from the ground with long poles, and one GRC panel half treated, half not, showing how much the yellowing differs",
  intro=[DISC_EN, "GRC (glass-fibre reinforced concrete) is loved by architects because it can be cast into seamless curves — but it is porous, absorbs water, and yellows fast under rain and city dust. On a pure white wall every mark shows."],
  hero=("Applicator using a long spray pole on the curved white GRC facade of an arts centre","Sprayed from the ground with long poles — curved GRC is hard to scaffold, and spraying from the ground is faster and safer"),
  steps=[
   ("01","Same GRC panel, half treated, half not",["The crew applied the two-layer system to one side as a control and left it to the weather — this photo is not washed or retouched; the line is the edge of the treated area."],[(2,"GRC wall, left side coated with the two-layer system and clean white, right side uncoated, yellowed with water streaks","Left: treated, smooth white · Right: untreated, dull yellow with water streaks — one continuous piece of GRC")]),
   ("02","Why GRC has to be primed before the topcoat",["GRC soaks water into its body, then pushes moisture and alkali back out as white and yellow staining from inside. A topcoat alone would simply be pushed through — so the penetrating primer closes the pores first, and the self-cleaning topcoat lets the rain look after the outside."],[(3,"Curved white GRC wall after treatment","The wall after treatment — smooth white across the whole face, the GRC still matt, no foreign gloss"),(4,"Applicator spraying the GRC wall with a long pole from the ground, side view","Working line by line from the ground — a long curved wall needs continuous application so no edge dries first")]),
   ("03","Where this applies in Thailand",["GRC decorative cladding, cast cornices and capitals, the fair-faced concrete walls of loft-style houses, polished-render fences — all porous materials that yellow and grow mould the same way, and the same system goes straight on."],[]),
  ], gal_alt="Meixihu Arts Centre GRC facade by the Feibo crew — site photo")))

# ───────── 2. Minmetals granite ─────────
s = "feibo-minmetals-granite"
CASES.append(dict(slug=s, ngal=5,
 th=dict(title="ผนังหินแกรนิตอาคารพักอาศัย — ซุ้มทางเข้าและป้ายชื่อ จุดที่คราบไหลลงเห็นก่อนใคร",
  desc="โครงการของ Feibo บนผนังหินแกรนิตของอาคารพักอาศัยระดับบน — ทำระบบ 2 ชั้นที่ซุ้มทางเข้าและป้ายชื่ออาคาร ด้วยรถกระเช้าขากรรไกรและนั่งร้าน โดยไม่เปลี่ยนสีหินแม้แต่นิดเดียว",
  intro=[DISC_TH, "อาคารพักอาศัยระดับบนใช้แกรนิตขัดหยาบทั้งผนัง — สวยและแพง แต่แกรนิตขัดหยาบดูดน้ำมากกว่าที่คิด คราบจากขอบบนไหลลงมาเป็นทางเหนือซุ้มทางเข้าและรอบตัวอักษรป้ายชื่อ ซึ่งเป็นจุดที่ทุกคนที่เดินเข้าอาคารมองเห็นก่อน"],
  hero=("รถกระเช้าขากรรไกรหน้าซุ้มทางเข้าอาคารพักอาศัยผนังหินแกรนิต ช่างกำลังเคลือบ","ซุ้มทางเข้า — เริ่มจากจุดที่คราบเห็นชัดที่สุด ใช้รถกระเช้าขากรรไกรเข้าถึงขอบบนของซุ้ม"),
  steps=[
   ("01","รอบตัวอักษรป้ายชื่อ — งานที่ต้องใช้มือ",["ตัวอักษรโลหะยึดกับผนังแกรนิต ซอกรอบตัวอักษรคือที่สะสมฝุ่นและคราบไหล ทีมงานขึ้นนั่งร้านพ่นทีละแนวรอบตัวอักษรให้รองพื้นซึมทั่วก่อน แล้วเคลือบผิวทับ"],[(2,"ช่างบนนั่งร้านใช้ก้านพ่นเคลือบผนังหินแกรนิตรอบตัวอักษรป้ายอาคาร","รอบตัวอักษรป้าย — พ่นทีละแนว หินขัดหยาบดูดน้ำยาเร็ว ต้องดูให้ผิวอิ่มทั่วโดยไม่ทิ้งส่วนเยิ้ม"),(3,"ช่างสองคนบนนั่งร้านเคลือบผนังหินแกรนิต","สองคนไล่ต่อกัน — ผนังหินต้องทำต่อเนื่อง ไม่ให้ขอบแนวแห้งก่อนแนวถัดไป")]),
   ("02","เจ้าของงานมีเงื่อนไขเดียว: หินต้องเป็นสีเดิม",["นี่คือเหตุผลที่ระบบหินต้องใส ไม่เงา ไม่เปลี่ยนสี — เจ้าของอาคารระดับนี้ยอมให้ผนังสกปรกดีกว่ายอมให้ผนังดูเป็นพลาสติก ทีมงานทดสอบมุมเล็กก่อน ยืนยันว่าแกรนิตขัดหยาบสีนี้ไม่เข้มขึ้น แล้วจึงลงทั้งซุ้ม"],[(4,"ช่างบนรถกระเช้าเคลือบใต้ขอบซุ้มทางเข้าอาคารหินแกรนิต ระยะใกล้","ใต้ขอบซุ้ม — จุดที่ฝนไหลย้อนเข้ามาทิ้งคราบเป็นแนว ทำให้ครบทั้งด้านบนและด้านใต้ของขอบ")]),
   ("03","ในไทยงานแบบนี้อยู่ตรงไหน",["คอนโดและโรงแรมที่ใช้แกรนิต หินอ่อน หรือหินทรายที่ซุ้มทางเข้า ป้ายชื่อโครงการ และผนังล็อบบี้ด้านนอก — จุดที่นิติบุคคลจ้างล้างทุกปีเพราะเป็นหน้าตาโครงการ ทำระบบครั้งเดียวแล้วลดรอบล้างได้หลายปี"],[]),
  ], gal_alt="งานผนังหินแกรนิตอาคารพักอาศัย โดยทีม Feibo — ภาพหน้างานจริง"),
 en=dict(title="Granite Facade of a Residential Tower — the Entrance Portico and Name Sign, Where Run-off Shows First",
  desc="A Feibo project on the granite facade of an upmarket residential building — the two-layer system applied at the entrance portico and name sign from a scissor lift and scaffold, without changing the colour of the stone at all",
  intro=[DISC_EN, "Upmarket residential towers use flamed granite across the whole facade — beautiful and expensive, but flamed granite absorbs far more water than people expect. Run-off from the top edge streaks down over the entrance portico and around the name-sign lettering — the first thing everyone walking in sees."],
  hero=("Scissor lift in front of the entrance portico of a granite-clad residential building, applicator coating","The entrance portico — starting where the marks show most, using a scissor lift to reach the top edge"),
  steps=[
   ("01","Around the sign lettering — hand work",["Metal letters fixed to the granite; the recesses around them collect dust and run-off. The crew worked from scaffolding, spraying line by line around the letters so the primer soaked in everywhere before the topcoat went on."],[(2,"Applicator on scaffolding spraying granite cladding around a building's sign lettering","Around the lettering — sprayed line by line; flamed granite drinks product fast, so the surface has to be saturated evenly without leaving excess"),(3,"Two applicators on scaffolding coating a building's granite cladding","Two applicators in sequence — stone facades need continuous application so no edge dries before the next pass")]),
   ("02","The owner had one condition: the stone stays the same colour",["This is why the stone system is clear, non-gloss and colour-neutral — an owner at this level would rather have a dirty wall than a wall that looks like plastic. The crew tested a small patch first, confirmed this flamed granite did not darken, and only then treated the whole portico."],[(4,"Applicator on a lift coating the underside of the entrance portico of a granite building, close view","Under the portico edge — where rain wraps back and leaves a line of staining; treated above and below the edge")]),
   ("03","Where this applies in Thailand",["Condominiums and hotels with granite, marble or sandstone at the entrance, the project name sign and the outer lobby walls — the spots the building management pays to wash every year because they are the face of the project. One application cuts the washing rounds for years."],[]),
  ], gal_alt="Residential granite facade by the Feibo crew — site photo")))

# ───────── 3. Jishou station marble ─────────
s = "feibo-jishou-station-marble"
CASES.append(dict(slug=s, ngal=4,
 th=dict(title="ราวหินอ่อนสลักลายหน้าสถานีรถไฟจี๋โส่ว — หินขาวที่ดำเร็วที่สุดเมื่อเจอฝุ่นถนน",
  desc="โครงการของ Feibo บนราวหินอ่อนขาวสลักลายหน้าสถานีรถไฟจี๋โส่ว — ล้างด้วยเครื่องขัดพื้นก่อน แล้วลงระบบ 2 ชั้นด้วยมือทีละช่วง ให้ลวดลายสลักลึกได้รองพื้นซึมถึงทุกร่อง",
  intro=[DISC_TH, "หินอ่อนขาวคือวัสดุที่สถานที่ราชการชอบใช้กับราวและบันไดหน้าอาคาร — และเป็นหินที่ \"ดำ\" เร็วที่สุด เพราะพรุน ดูดน้ำ และอยู่ระดับเดียวกับฝุ่นถนน ควันรถ และมือคน ลวดลายสลักลึกยิ่งเก็บคราบ"],
  hero=("ช่างเคลือบราวหินอ่อนสลักลายหน้าสถานีรถไฟ มีกรวยกั้นและถังน้ำยา","หน้าสถานีรถไฟจี๋โส่ว — ทำงานบนลานหน้าสถานีที่เปิดใช้ปกติ กั้นพื้นที่ทีละช่วง"),
  steps=[
   ("01","ล้างก่อน — ระบบนี้ป้องกัน ไม่ใช่ล้าง",["คราบดำและตะไคร่ที่ฝังในหินอ่อนต้องออกก่อน ไม่งั้นรองพื้นซึมไม่เข้าและคราบจะถูกล็อคไว้ใต้ระบบ ทีมงานใช้เครื่องขัดพื้นกับน้ำยาล้างหินโดยเฉพาะ แล้วรอให้หินแห้งสนิทก่อนลงชั้นแรก"],[(2,"ช่างใช้เครื่องขัดพื้นล้างราวหินอ่อนหน้าสถานีรถไฟ ก่อนเคลือบ","ขั้นล้าง — เครื่องขัดกับน้ำยาล้างหิน ขจัดคราบดำที่ฝังในผิวหินอ่อนก่อน หินต้องแห้งสนิทก่อนลงรองพื้น")]),
   ("02","ลงด้วยมือทีละช่วง — ลวดลายสลักลึกคือโจทย์",["ราวสลักลายไม่มีทางพ่นให้ทั่วจากระยะไกล ทีมงานลงรองพื้นด้วยมือทีละช่วง ไล่ให้ซึมเข้าทุกร่องของลวดลาย เช็ดส่วนที่เยิ้มออกก่อนเซ็ต แล้วจึงลงเคลือบผิว Self-Cleaning บางๆ ทับ"],[(3,"ถังน้ำยารองพื้นวางบนราวหินอ่อน ช่างทาด้วยมือด้านหลัง","งานมือทีละช่วง — ถังรองพื้นวางบนราว ทาไล่เข้าร่องลาย ก่อนเคลือบผิวทับ")]),
   ("03","ในไทยงานแบบนี้อยู่ตรงไหน",["ราวบันไดหินอ่อนหน้าศาลากลาง วัด โรงแรม รูปปั้นหินและฐานอนุสาวรีย์ ราวสะพานหิน — งานที่หน่วยงานจ้างล้างด้วยแรงดันสูงทุกปีจนผิวหินสึกและลายจาง ทำระบบครั้งเดียวแล้วล้างด้วยน้ำเปล่าพอ"],[]),
  ], gal_alt="งานราวหินอ่อนหน้าสถานีรถไฟจี๋โส่ว โดยทีม Feibo — ภาพหน้างานจริง"),
 en=dict(title="Carved Marble Balustrades at Jishou Railway Station — the White Stone That Goes Black Fastest in Road Dust",
  desc="A Feibo project on the carved white marble balustrades outside Jishou railway station — machine-cleaned first, then the two-layer system applied by hand section by section so the primer reaches every groove of the carving",
  intro=[DISC_EN, "White marble is what public buildings love for balustrades and entrance steps — and it is the stone that goes \"black\" fastest, because it is porous, absorbs water, and sits at the level of road dust, exhaust and hands. Deep carving holds even more grime."],
  hero=("Applicator treating a carved marble balustrade outside a railway station, with cones and product containers","Outside Jishou railway station — working on the forecourt while the station stayed open, coning off one section at a time"),
  steps=[
   ("01","Clean first — this system protects, it doesn't clean",["Black staining and algae already in the marble have to come out first, or the primer can't penetrate and the stain is locked under the system. The crew used a floor machine with a dedicated stone cleaner, then let the stone dry fully before the first layer."],[(2,"Applicator using a floor machine to clean a marble balustrade outside a railway station before coating","The cleaning step — machine and stone cleaner to lift the black staining from the marble; the stone must be completely dry before priming")]),
   ("02","By hand, section by section — the deep carving is the challenge",["A carved balustrade cannot be sprayed evenly from a distance. The crew primed by hand one section at a time, working it into every groove of the pattern, wiped off the excess before it set, then applied a thin self-cleaning topcoat over it."],[(3,"Primer container on a marble balustrade with an applicator working by hand behind","Hand work, section by section — primer on the balustrade, worked into the carving before the topcoat")]),
   ("03","Where this applies in Thailand",["Marble stair balustrades at provincial halls, temples and hotels, stone statues and monument bases, stone bridge railings — the jobs an agency pressure-washes every year until the surface wears and the carving fades. One application, then plain water is enough."],[]),
  ], gal_alt="Jishou railway station marble balustrades by the Feibo crew — site photo")))

# ───────── 4. Xiangxi plaza stone ─────────
s = "feibo-xiangxi-plaza-stone"
CASES.append(dict(slug=s, ngal=6,
 th=dict(title="ลานกลองเซียงซี — หินสลัก ราวสะพาน และประติมากรรมกลางแจ้งที่ต้องอยู่ได้เอง",
  desc="โครงการของ Feibo ในลานสาธารณะที่เซียงซี — หินสลักรูปมังกร ฐานประติมากรรมกลอง และราวหินสะพานยาวทั้งแนว ทำระบบ 2 ชั้นให้ร่องสลักลึกไม่เก็บตะไคร่และเทศบาลไม่ต้องล้างทุกปี",
  intro=[DISC_TH, "ลานสาธารณะคือหน้างานที่ไม่มีใครดูแลรายวัน — หินสลัก ราวสะพาน ฐานประติมากรรม โดนฝน ฝุ่น นก และมือคนตลอดปี แล้วเทศบาลก็ล้างด้วยแรงดันสูงปีละครั้ง ซึ่งกัดผิวหินและทำลายลายสลักไปเรื่อยๆ"],
  hero=("ช่างพ่นเคลือบหินสลักรูปหน้ามังกรในลานสาธารณะ","หินสลักรูปมังกร — พ่นให้รองพื้นซึมถึงก้นร่องสลักทุกร่อง ที่ที่ตะไคร่ชอบขึ้นก่อน"),
  steps=[
   ("01","ประติมากรรมกลอง — สีสดที่ต้องไม่หม่น",["ฐานหินและตัวประติมากรรมกลองสีสดกลางลาน ทีมงานใช้บันไดพับกับกาพ่นมือ ทำทีละด้าน — ระบบใสไม่กลบสี และผล Self-Cleaning ช่วยให้สีไม่หม่นจากฝุ่นสะสม"],[(2,"ช่างบนบันไดเคลือบประติมากรรมกลองสีสดบนฐานหินในลานสาธารณะ","ประติมากรรมกลอง — บันไดพับกับกาพ่นมือ ทำทีละด้าน ฐานหินสลักด้านล่างทำระบบ 2 ชั้นเต็ม")]),
   ("02","ราวหินสะพาน — ยาวทั้งแนว ทำจากรถตู้",["ราวหินสลักลายทั้งสองฝั่งสะพาน ทีมงานจอดรถตู้อุปกรณ์ตามแนวแล้วไล่ทำทีละช่วง ราวแบบนี้คือสิ่งที่เทศบาลล้างด้วยแรงดันสูงทุกปี — หลังทำระบบ ฝนล้างให้เอง"],[(3,"ช่างเคลือบราวหินสะพาน มีรถตู้อุปกรณ์จอดข้าง","ไล่ทำราวสะพานทีละช่วงจากรถตู้อุปกรณ์ — กั้นทางเดินเป็นช่วงสั้นๆ คนยังเดินผ่านได้"),(4,"ราวหินสลักลายบนสะพานในเมือง","ราวสะพานยาวทั้งแนวหลังทำ — ลายสลักยังคมเหมือนเดิม เพราะไม่ต้องโดนแรงดันสูงอีก")]),
   ("03","ในไทยงานแบบนี้อยู่ตรงไหน",["สวนสาธารณะ ลานอนุสาวรีย์ ราวสะพานหินของเทศบาล ฐานพระพุทธรูปกลางแจ้ง กำแพงวัด — งานที่งบดูแลมีจำกัดและไม่มีใครขึ้นล้างบ่อยๆ ยิ่งเหมาะกับระบบที่ให้ฝนดูแลแทน"],[]),
  ], gal_alt="งานหินสลักและราวสะพานลานกลองเซียงซี โดยทีม Feibo — ภาพหน้างานจริง"),
 en=dict(title="Xiangxi Drum Plaza — Stone Carvings, Bridge Balustrades and Outdoor Sculpture That Have to Look After Themselves",
  desc="A Feibo project in a public plaza in Xiangxi — a carved stone dragon, the base of a drum sculpture and a full run of stone bridge balustrade, treated with the two-layer system so the deep carving stops collecting algae and the municipality stops pressure-washing every year",
  intro=[DISC_EN, "A public plaza is the site nobody looks after daily — carvings, balustrades and sculpture bases take rain, dust, birds and hands all year, and then the municipality pressure-washes once a year, which eats the stone surface and wears the carving away a little more each time."],
  hero=("Applicator spraying a carved stone dragon head in a public plaza","The carved stone dragon — sprayed so the primer reaches the bottom of every groove, where algae takes hold first"),
  steps=[
   ("01","The drum sculpture — bright colours that must not go dull",["The stone base and the brightly coloured drum sculpture in the middle of the plaza: the crew worked one face at a time with a folding ladder and a hand sprayer. The system is clear, so it doesn't cover the colours, and the self-cleaning effect keeps them from dulling under settled dust."],[(2,"Applicator on a ladder coating a brightly coloured drum sculpture on a stone base in a public plaza","The drum sculpture — folding ladder and hand sprayer, one face at a time; the carved stone base below got the full two-layer system")]),
   ("02","The bridge balustrade — the whole run, from the van",["Carved stone balustrade on both sides of the bridge: the crew parked the equipment van along the line and worked section by section. This is exactly what a municipality pressure-washes every year — after the system, the rain does it."],[(3,"Applicator coating a stone bridge balustrade with the equipment van parked alongside","Working the balustrade section by section from the equipment van — short stretches coned off, pedestrians still passing"),(4,"Carved stone balustrade along a city bridge","The full run of balustrade after treatment — the carving stays crisp because it never has to face a pressure washer again")]),
   ("03","Where this applies in Thailand",["Public parks, monument plazas, municipal stone bridge railings, outdoor Buddha image bases, temple walls — jobs with limited maintenance budgets and nobody to wash them often, which is exactly where a system that lets the rain do the work fits best."],[]),
  ], gal_alt="Xiangxi Drum Plaza stone carvings and balustrades by the Feibo crew — site photo")))

def transplant(src_path, out_path, slug, title, desc, eyebrow, meta, body_html, og_img):
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
                f"  <h1>{title}</h1>\n"
                f'  <p class="meta">{meta}</p>\n' + body_html)
    h = h[:i] + new_main + h[j:]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(h)
    print("built:", out_path)

def render(c, lang):
    slug = c["slug"]; d = c[lang]
    hero_fig = fig(slug, 1, d["hero"][0], d["hero"][1], hero=True)
    steps = []
    for n, h2, paras, figs in d["steps"]:
        fs = []
        for k, alt, cap in figs:
            kk = f"{k}en" if (lang == "en" and os.path.exists(os.path.join(ROOT, "img", "post", f"{slug}-h{k}en.webp"))) else str(k)
            fs.append(fig(slug, kk, alt, cap))
        steps.append(step(n, h2, paras, fs))
    return body(slug, lang, d["intro"], hero_fig, steps, c["ngal"], d["gal_alt"])

if __name__ == "__main__":
    for c in CASES:
        slug = c["slug"]; og = f"https://www.lucernapro.com/img/post/{slug}-h1.webp"
        transplant(os.path.join(ROOT, "post", SRC, "index.html"), os.path.join(ROOT, "post", slug, "index.html"),
                   slug, c["th"]["title"], c["th"]["desc"], EYE_TH, META_TH, render(c, "th"), og)
        transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"), os.path.join(ROOT, "en", "post", slug, "index.html"),
                   slug, c["en"]["title"], c["en"]["desc"], EYE_EN, META_EN, render(c, "en"), og)
