# -*- coding: utf-8 -*-
"""
build_selfcleaning_field_projects.py — โพสต์เดียวรวมผลงานจริงในสนามของสาย Self-Cleaning (Solar / Stone / Paint / Glass) 8 โครงการ
/post/self-cleaning-field-projects (+EN) — chrome-transplant จากโพสต์ solar feibo-lab เหมือน build_feibo_*_cases.py
รูป: /img/post/self-cleaning-field-projects-h1..h16.webp (จากหน้างานที่ Lilian ส่ง ก.ย. 2026)
กฎ: ระบุแหล่งที่มาครั้งเดียวในบล็อก SOURCE, เรียกโครงการด้วยชื่อสถานที่, ไม่แต่งเจตนา/ขั้นตอนที่ไม่ได้อยู่ในแหล่ง
รัน: python3 tools/build_selfcleaning_field_projects.py (จาก root ของ repo)
"""
import os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "self-cleaning-field-projects"

def dims(k):
    return Image.open(os.path.join(ROOT, "img", "post", f"{SLUG}-h{k}.webp")).size

def fig(k, alt, cap, hero=False):
    w, h = dims(k)
    cls = ' class="hero"' if hero else ''
    icls = ' class="tall"' if h > w else ''
    lazy = '' if hero else ' loading="lazy"'
    return (f'    <figure{cls}><img{icls} src="/img/post/{SLUG}-h{k}.webp" alt="{alt}"{lazy} '
            f'width="{w}" height="{h}"><figcaption>{cap}</figcaption></figure>\n')

def step(n, h2, paras, figs):
    return (f'    <section class="step">\n      <h2><span class="n">{n}</span>{h2}</h2>\n'
            + "".join(f"      <p>{p}</p>\n" for p in paras) + "".join(figs) + "    </section>\n")

TH = dict(
 title="ผลงานจริงในสนาม 8 โครงการ — โซลาร์ฟาร์ม รูปปั้นแลนด์มาร์ก ผนังอาคาร และกระจก ที่ให้ฝนดูแลแทนคน",
 desc="รวมหน้างานจริงของสาย Self-Cleaning ในหน้าเดียว — โซลาร์ฟาร์มบนเขาและบนน้ำ รูปปั้นเกาะส้มและรูปปั้นจอมพลเหอหลง ศูนย์ศิลปะจี๋โส่ว ป้ายเขตใหม่เซียงเจียง หน้าต่างโค้งบ้านพัก และอาคารกระจกดาดฟ้า พร้อมว่าแต่ละงานตอบโจทย์งานไทยแบบไหน",
 eyebrow="Case Study · เคลือบปกป้อง / Self-Cleaning",
 meta="เผยแพร่ ก.ย. 2026 · ภาพหน้างานจากทีมผู้พัฒนาวัตถุดิบของเรา (ประเทศจีน)",
 intro=[
  'ทุกโครงการในหน้านี้เป็นงานของ <b>Feibo</b> (ฉางชา ประเทศจีน) ผู้พัฒนาและผลิตวัตถุดิบหลักของ <a href="/solarpaneldefender">Solar Panel Defender</a> <a href="/stonesurface">Stone Coating</a> <a href="/paintcoating">Paint Coating</a> และ <a href="/glasscoating">Glass Coating</a> — ไม่ใช่งานของทีมเราในไทย เรารวมไว้หน้าเดียวเพราะเป็นคำถามแรกที่ลูกค้าถามเสมอ: "ใช้ที่ไหนแล้วบ้าง"',
  'หลักการเดียวกันทั้ง 8 งาน: ผิวที่เคลือบแล้วเป็น Superhydrophilic — น้ำไม่เกาะเป็นหยดแต่แผ่เป็นแผ่นบาง พาฝุ่นลงไปกับฝน แดดช่วยย่อยคราบอินทรีย์ ถ้าอยากรู้ว่าทำไมถึงเลือกเส้นทางนี้ อ่านได้ที่ <a href="/post/self-cleaning-technology">Self-Cleaning ทำงานยังไง</a>',
 ],
 hero=("ทีมงานเคลือบแผงโซลาร์บนโรงไฟฟ้าโซลาร์ฟาร์มบนเนินเขา", "โซลาร์ฟาร์มบนเนินเขา — ทีมงานล้างแล้วพ่นเคลือบแผงทีละแถว งานประเภทที่ล้างด้วยคนยากที่สุด"),
 steps=[
  ("01","โซลาร์ฟาร์มบนเนินเขา — ฝุ่นและมูลนกกดกำลังผลิต",
   ["แผงบนเขาโดนฝุ่นลมและมูลนกสะสม แสงส่องถึงเซลล์น้อยลงและเกิดจุดร้อน ภูมิประเทศทำให้ล้างด้วยคนช้าและแพง ทีมงานเลือกแถวทดสอบเทียบก่อน ล้างแผงด้วยน้ำเปล่าผสมน้ำยาล้าง แล้วพ่นเคลือบเมื่อแห้ง ผิวแผงที่เคลือบแล้วกันไฟฟ้าสถิต ฝุ่นเกาะน้อยลงและฝนพาลงเอง ผลจากโครงการนี้: กำลังผลิตเพิ่มประมาณ 3% ขึ้นไป และรอบล้างลดลงมาก",
    "ในไทย: โซลาร์ฟาร์มและหลังคาโรงงานที่จ้างล้างเป็นรอบ — สิ่งที่ได้จริงคือขึ้นหลังคาน้อยลงหลายเท่า ตัวเลขระดับบ้านอยู่ในหน้า <a href=\"/solarpaneldefender\">Solar Panel Defender</a>"],
   [(2,"ทีมงานแบ่งโซนเคลือบแผงโซลาร์บนเนินเขา","ไล่ทำทีละโซน — แผงต้องแห้งสนิทก่อนพ่น และพ่นต่อเนื่องไม่ให้ขอบแนวแห้งก่อน")]),
  ("02","โซลาร์ฟาร์มบนผิวน้ำ — ล้างต้องใช้เรือ เคลือบครั้งเดียวจบ",
   ["แผงบนน้ำเจอความชื้นสูงและนกจำนวนมาก มูลนกกับคราบน้ำเกาะหนา การล้างต้องใช้เรือหรือแพทำงานซึ่งทั้งแพงและเสี่ยง ทีมงานใช้แพทำงานเข้าไปล้างและพ่นเคลือบ หลังเคลือบ ฝนพาคราบลงได้เอง มูลนกไม่เกาะแน่นเหมือนเดิม รอบล้างบนน้ำลดลงมาก"],
   [(3,"ทีมงานบนแพทำงานพ่นเคลือบแผงโซลาร์บนผิวน้ำ","แพทำงานเข้าถึงแผงบนน้ำ — พ่นเคลือบหลังล้างและแห้งสนิท"),(4,"เปรียบเทียบแผงโซลาร์ที่เคลือบและไม่เคลือบหลัง 12 เดือน","12 เดือนต่อมาในโรงไฟฟ้าเดียวกัน — แผงที่เคลือบยังใส แผงที่ไม่เคลือบมีฝุ่นเกาะชัด")]),
  ("03","รูปปั้นเกาะส้ม ฉางชา — แลนด์มาร์กที่ล้างไม่ได้",
   ["รูปปั้นหินขนาดยักษ์กลางแม่น้ำ โดนฝน ควันรถ และตะไคร่ตลอดปี ผิวหินดำและเป็นด่าง รูปทรงซับซ้อนและสูงจนการล้างต้องโรยตัว ทีมงานสำรวจความพรุนของหิน ทดสอบมุมเล็ก ล้างคราบเดิมออก แล้วลงระบบ 2 ชั้น: รองพื้นซึมลึกปิดรูพรุนกันน้ำเข้า และเคลือบผิว Self-Cleaning ให้ฝนกับแดดดูแลข้างนอก",
    "ในไทย: พระพุทธรูปกลางแจ้ง อนุสาวรีย์ ฐานหิน — งานที่ล้างด้วยแรงดันสูงทุกปีจนผิวหินสึก ทำระบบครั้งเดียวแล้วล้างด้วยน้ำเปล่าพอ"],
   [(5,"รูปปั้นหินขนาดใหญ่บนเกาะส้ม ฉางชา","รูปปั้นเกาะส้ม — หินพรุนกลางแจ้ง ต้องกันน้ำจากข้างในก่อนถึงเคลือบผิวได้ผล"),(6,"ภาพมุมสูงรูปปั้นเกาะส้มกับแม่น้ำ","ที่ตั้งกลางแม่น้ำ — ความชื้นสูงตลอดปี ตะไคร่ขึ้นเร็วกว่าที่อื่น")]),
  ("04","รูปปั้นจอมพลเหอหลงขี่ม้า ซางจื้อ — ทำจากรถกระเช้า",
   ["รูปปั้นสูงบนฐานหินขาว ตัวรูปปั้นสะสมฝุ่น ฐานหินเหลืองและดำจากน้ำฝน ทีมงานใช้รถกระเช้าเข้าถึงทุกด้าน ล้างและเคลือบทีละโซน ฐานหินลงระบบ 2 ชั้นเหมือนงานหินทั่วไป หลังทำ น้ำฝนแผ่เป็นแผ่นแล้วพาฝุ่นลง ฐานไม่ดูดน้ำจึงไม่เกิดคราบด่างจากข้างใน"],
   [(7,"รูปปั้นจอมพลเหอหลงขี่ม้าบนฐานหินขาว","รูปปั้นกับฐานหินขาวหลังทำ — ฐานคือส่วนที่เหลืองเร็วที่สุดเพราะเป็นหินพรุนรับน้ำฝนจากตัวรูปปั้น"),(8,"ทีมงานบนรถกระเช้าเคลือบรูปปั้นขี่ม้า","รถกระเช้ายกทีมงานขึ้นทำส่วนบนของรูปปั้น — งานสูงที่ต้องทำครั้งเดียวให้ครบ")]),
  ("05","ศูนย์ศิลปะภาพยนตร์จี๋โส่ว — ผนังขาวโค้งกับทีมโรยตัว",
   ["อาคารมีผนังโค้งสีขาวเป็นเอกลักษณ์ ฝุ่นกับทางน้ำฝนบนผนังขาวเห็นชัดกว่าสีอื่น รูปทรงซับซ้อนทำให้ล้างได้ทางเดียวคือโรยตัว ทีมงานทดสอบมุมเล็กให้เห็นว่าผิวไม่เปลี่ยนสี แล้วโรยตัวล้างและพ่นเคลือบทีละโซน หลังทำ ฝนแผ่เป็นแผ่นบนผนังโค้งพาฝุ่นลงโดยไม่ทิ้งทางน้ำ",
    "ในไทย: ผนังอลูมิเนียมคอมโพสิตและผนังพ่นสีของอาคารพาณิชย์ ที่นิติบุคคลจ้างโรยตัวล้างทุกปี"],
   [(9,"อาคารศูนย์ศิลปะภาพยนตร์จี๋โส่ว ผนังโค้งสีขาวลายเพชร","ผนังโค้งสีขาว — ทุกทางน้ำฝนเห็นชัด และล้างได้ทางเดียวคือโรยตัว"),(10,"ทีมงานโรยตัวเคลือบผนังโค้งสีขาว","ทีมโรยตัวไล่ทำทีละโซนจากบนลงล่าง")]),
  ("06","ป้ายเขตใหม่เซียงเจียง ฉางชา — ป้ายหน้าเมืองที่ต้องเช็ดบ่อย",
   ["ป้ายตั้งพื้นพร้อมตัวอักษรโลหะสีทองอยู่ตรงทางเข้าเมือง โดนฝุ่น ฝน และแดดตลอดปี ผิวสีเก็บฝุ่นเป็นคราบน้ำ ตัวอักษรซีดจาง ทีมงานล้างคราบเดิมออก แล้วเคลือบฐานและตัวอักษรทีละด้านด้วยแปรงและกาพ่นมือ หลังทำ ฝนล้างเอง ผิวสีและตัวอักษรคงสีสด ไม่ต้องเช็ดถี่เหมือนเดิม",
    "ในไทย: ป้ายชื่อโครงการหมู่บ้าน ป้ายหน้าโรงงาน ซุ้มทางเข้า — ของที่เห็นก่อนสิ่งอื่นและเปื้อนเร็วที่สุด"],
   [(11,"ป้ายเขตใหม่เซียงเจียงตัวอักษรโลหะสีทอง","ป้ายหน้าเมือง — ตัวอักษรโลหะสีทองบนฐานสีขาว"),(12,"ทีมงานเคลือบตัวอักษรโลหะบนป้าย","เคลือบตัวอักษรทีละด้านด้วยกาพ่นมือ — ซอกรอบตัวอักษรคือที่เก็บฝุ่นมากที่สุด")]),
  ("07","หน้าต่างโค้งบ้านพักสไตล์ยุโรป — ทำครึ่งไม่ทำครึ่งให้ดู",
   ["บ้านใช้หน้าต่างโค้งบานใหญ่ในที่สูง ล้างต้องใช้บันได หลังฝนกระจกเป็นหยดน้ำเต็มบานแล้วแห้งเป็นคราบ ทีมงานล้างกระจก ขึ้นบันไดเคลือบทีละบาน แล้วทดสอบพ่นน้ำ ฝั่งที่เคลือบน้ำแผ่เป็นแผ่นเรียบ ฝั่งที่ไม่เคลือบเป็นหยดเต็ม — ภาพเดียวกัน กระจกบานเดียวกัน",
    "ในไทย: กระจกบ้านที่ล้างไม่ถึง กระจกอาคารชั้นสอง หลังคากระจก — ดูหน้า <a href=\"/glasscoating\">Glass Coating</a> ว่ากระจกแบบไหนเหมาะ"],
   [(13,"ทีมงานขึ้นบันไดเคลือบหน้าต่างโค้งบานใหญ่","หน้าต่างโค้งในที่สูง — ทำทีละบานจากบันได"),(14,"กระจกบานเดียวกัน ฝั่งซ้ายเป็นหยดน้ำ ฝั่งขวาน้ำแผ่เป็นแผ่น","ทดสอบพ่นน้ำ — ซ้าย: ไม่เคลือบ หยดน้ำเต็ม · ขวา: เคลือบแล้ว น้ำแผ่เป็นแผ่นบาง")]),
  ("08","อาคารกระจกบนดาดฟ้า — กระจกเอียงที่ล้างไม่ได้เอง",
   ["ห้องกระจกบนดาดฟ้า กระจกเอียงรับฝนและฝุ่นตรงๆ ขึ้นไปล้างเสี่ยงและไม่มีใครทำ ทีมงานล้างกระจกด้วยน้ำยากลาง ปล่อยแห้ง แล้วพ่นเคลือบด้านนอกทั้งหมด เปรียบเทียบทันทีหลังทำ ฝั่งที่เคลือบใสกว่าอย่างเห็นได้ชัด และหลังจากนั้นฝนเป็นคนล้าง"],
   [(15,"ทีมงานพ่นเคลือบกระจกอาคารบนดาดฟ้า","อาคารกระจกบนดาดฟ้า — พ่นเคลือบด้านนอกหลังล้างและแห้งสนิท"),(16,"กระจกเอียงบนดาดฟ้า ฝั่งเคลือบใสกว่าฝั่งไม่เคลือบ","กระจกเอียงบานเดียวกัน — ฝั่งเคลือบแล้วใส ฝั่งไม่เคลือบขุ่น")]),
 ],
 outro='ระบบนี้ <b>ป้องกัน ไม่ใช่ล้าง</b> — คราบที่ฝังอยู่ก่อนต้องล้างออกก่อนเคลือบ และผิวที่ฝนไม่ถึงแดดไม่ส่องจะได้ผลน้อยกว่าผิวกลางแจ้ง ข้อจำกัดของแต่ละพื้นผิวอยู่ในส่วน "พูดตรงๆ" ของหน้าสินค้าแต่ละตัว',
 prods='<div class="prods"><span class="lbl">สินค้าในสายนี้:</span><a href="/solarpaneldefender">Solar Panel Defender</a><a href="/stonesurface">Stone Coating</a><a href="/paintcoating">Paint Coating</a><a href="/glasscoating">Glass Coating</a></div>\n  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>\n',
)

EN = dict(
 title="8 Real Field Projects — Solar Farms, Landmark Statues, Facades and Glass That Let the Rain Do the Cleaning",
 desc="Every real site of our Self-Cleaning family on one page — hillside and floating solar farms, the Orange Isle statue and the Marshal He Long statue, the Jishou arts centre, the Xiangjiang New Area sign, villa arched windows and a rooftop glass room — and what each one means for a Thai job",
 eyebrow="Case Study · Coatings / Self-Cleaning",
 meta="Published Sept 2026 · Site photos from the team that develops our raw material (China)",
 intro=[
  'Every project on this page is the work of <b>Feibo</b> (Changsha, China), the developer and producer of the core raw material in our <a href="/en/solarpaneldefender">Solar Panel Defender</a>, <a href="/en/stonesurface">Stone Coating</a>, <a href="/en/paintcoating">Paint Coating</a> and <a href="/en/glasscoating">Glass Coating</a> — not our own crew in Thailand. We collected them on one page because it is the first question every customer asks: "where has it been used?"',
  'One principle runs through all eight: the treated surface is superhydrophilic — water does not bead but spreads into a thin sheet that carries dust down with the rain, and sunlight breaks down organic grime. Why we chose this route is explained in <a href="/en/post/self-cleaning-technology">How Self-Cleaning Works</a>.',
 ],
 hero=("Crew coating solar panels at a hillside solar farm", "Hillside solar farm — panels washed, then coated row by row; the kind of site that is hardest to wash by hand"),
 steps=[
  ("01","Hillside solar farm — dust and bird droppings cut the output",
   ["Panels on the hillside collected wind-blown dust and bird droppings; less light reached the cells and hot spots formed, and the terrain made manual washing slow and costly. The crew chose a comparison test row, washed the panels with plain water and cleaner, and sprayed the coating once dry. The coated surface is anti-static, so less dust settles and the rain carries it off. Result from this plant: output up by about 3% or more, and far fewer washing rounds.",
    "In Thailand: solar farms and factory roofs that pay for washing rounds — what you actually get is far fewer trips onto the roof. Home-scale figures are on the <a href=\"/en/solarpaneldefender\">Solar Panel Defender</a> page."],
   [(2,"Crew coating hillside solar panels zone by zone","Zone by zone — panels must be fully dry before spraying, applied continuously so no edge dries first")]),
  ("02","Floating solar farm — washing needs a boat, coating is done once",
   ["Panels over water face high humidity and many birds; droppings and water marks build up thickly, and washing needs a boat or work platform — costly and risky. The crew used a work platform to wash and spray the panels. After coating, rain carries the grime off and droppings no longer bond as they did; washing rounds on the water dropped sharply."],
   [(3,"Crew on a work platform spraying floating solar panels","A work platform reaches the panels over water — sprayed after washing and full drying"),(4,"Coated and uncoated solar panels compared after 12 months","Twelve months later at the same plant — the coated panel still clear, the uncoated one visibly dusty")]),
  ("03","Orange Isle statue, Changsha — a landmark that cannot be washed",
   ["A giant stone statue in the middle of a river takes rain, exhaust and algae all year; the stone blackened and stained, and the complex, tall form meant any washing needed rope access. The crew surveyed the stone's porosity, tested a small patch, cleaned off the old staining, then applied the two-layer system: a penetrating primer to close the pores against water, and a self-cleaning topcoat so rain and sun look after the outside.",
    "In Thailand: outdoor Buddha images, monuments, stone bases — jobs pressure-washed every year until the stone wears. One application, then plain water is enough."],
   [(5,"Giant stone statue on Orange Isle, Changsha","The Orange Isle statue — porous stone outdoors has to be sealed from inside before a topcoat can work"),(6,"Aerial view of the Orange Isle statue and the river","Set in the middle of the river — high humidity all year, algae grows faster than anywhere else")]),
  ("04","Marshal He Long equestrian statue, Sangzhi — done from a boom lift",
   ["A tall statue on a white stone plinth: dust on the figure, the plinth yellowed and blackened by rain run-off. The crew used a boom lift to reach every side, washing and coating zone by zone, with the plinth given the same two-layer system as any stone job. After treatment, rain sheets off and carries dust away, and the plinth no longer absorbs water, so no staining pushes out from inside."],
   [(7,"Marshal He Long equestrian statue on a white stone plinth","Statue and white plinth after treatment — the plinth is what yellows fastest, porous stone taking the run-off from the figure"),(8,"Crew on a boom lift coating the equestrian statue","Boom lift raising the crew to the upper part of the statue — high work done once, completely")]),
  ("05","Jishou Film and TV Arts Centre — a white curved facade and a rope-access team",
   ["The building's signature is its white curved facade, where dust and rain streaks show more than on any other colour, and the shape leaves only one way to clean it: rope access. The crew tested a small patch to show the surface would not change colour, then abseiled to wash and spray zone by zone. After treatment, rain sheets over the curve and carries dust down without leaving streaks.",
    "In Thailand: aluminium-composite and spray-painted facades of commercial buildings that building management pays rope-access teams to wash every year."],
   [(9,"Jishou Film and TV Arts Centre, white curved facade with diamond windows","The white curved facade — every rain streak shows, and rope access is the only way to clean it"),(10,"Rope-access team coating the white curved facade","The rope-access team working zone by zone from the top down")]),
  ("06","Xiangjiang New Area sign, Changsha — the gateway sign that needed constant wiping",
   ["A freestanding sign with gold metal lettering at the entrance to the district, in dust, rain and sun all year: the painted surfaces held dust as water marks and the letters faded. The crew cleaned off the old grime and coated the base and letters face by face with brush and hand sprayer. After treatment the rain does the washing, the paint and lettering keep their colour, and the frequent wiping stopped.",
    "In Thailand: housing-estate name signs, factory entrance signs, gateway arches — the first thing anyone sees and the fastest to get dirty."],
   [(11,"Xiangjiang New Area sign with gold metal lettering","The gateway sign — gold metal letters on a white base"),(12,"Crew coating the metal letters on the sign","Coating the letters face by face with a hand sprayer — the recesses around the letters hold the most dust")]),
  ("07","Arched windows of a European-style villa — half treated, half not",
   ["The house has large arched windows high up that can only be washed from a ladder; after rain the glass was covered in droplets that dried into marks. The crew washed the glass, coated it pane by pane from the ladder, then ran a spray test: on the treated side water spreads into a smooth sheet, on the untreated side it beads all over — same photo, same pane.",
    "In Thailand: house glass you can't reach to wash, second-floor glazing, glass roofs — see the <a href=\"/en/glasscoating\">Glass Coating</a> page for which glass suits it."],
   [(13,"Crew on a ladder coating a large arched window","Arched windows high up — done pane by pane from a ladder"),(14,"Same pane of glass, left side beaded with droplets, right side water in a sheet","Spray test — left: untreated, full of droplets · right: treated, water spread into a thin sheet")]),
  ("08","Rooftop glass room — sloped glass that cannot wash itself",
   ["A glass room on a rooftop, its sloped glass taking rain and dust head-on, and nobody willing to climb up to wash it. The crew washed the glass with neutral cleaner, let it dry, then sprayed the whole exterior. Compared straight after the work, the treated side is visibly clearer — and from then on the rain does the washing."],
   [(15,"Crew spraying the glass of a rooftop glass room","Rooftop glass room — exterior sprayed after washing and full drying"),(16,"Sloped rooftop glass, treated side clearer than untreated","The same sloped pane — treated side clear, untreated side hazy")]),
 ],
 outro='This system <b>protects, it does not clean</b> — staining already embedded has to be removed before application, and a surface that rain never reaches and sun never hits gets far less of the effect than an outdoor one. The limits for each surface are in the "Straight Talk" section of each product page.',
 prods='<div class="prods"><span class="lbl">Products in this family:</span><a href="/en/solarpaneldefender">Solar Panel Defender</a><a href="/en/stonesurface">Stone Coating</a><a href="/en/paintcoating">Paint Coating</a><a href="/en/glasscoating">Glass Coating</a></div>\n  <a class="back" href="/en/casestudy/">← Back to all case studies</a>\n',
)

def render(d):
    hero_fig = fig(1, d["hero"][0], d["hero"][1], hero=True)
    steps = [step(n, h2, paras, [fig(k, alt, cap) for k, alt, cap in figs]) for n, h2, paras, figs in d["steps"]]
    return ("  <article>\n" + f'    <p>{d["intro"][0]}</p>\n' + hero_fig + f'    <p>{d["intro"][1]}</p>\n'
            + "".join(steps) + f'    <p>{d["outro"]}</p>\n' + "  </article>\n  " + d["prods"])

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
