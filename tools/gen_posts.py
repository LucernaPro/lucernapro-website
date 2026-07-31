# -*- coding: utf-8 -*-
"""
gen_posts.py — สร้างหน้า /post/{slug}/index.html สำหรับเคสจากหน้า /casestudy
เนื้อหา migrate มาจาก Wix (lucernapro.com/post/...) แบบคำต่อคำ
รูป/วิดีโอ: hotlink wixstatic ชั่วคราว (ดู SPEC หัวข้อ Post Migration — ต้อง salvage ก่อนปิดบัญชี Wix)
รัน: python3 tools/gen_posts.py (จาก root ของ repo)
"""
import os, urllib.parse

WIX_IMG = "https://static.wixstatic.com/media/"

def hero(mid, w=1200, h=900, q=90):
    return f"{WIX_IMG}{mid}/v1/fill/w_{w},h_{h},al_c,q_{q}/{mid}"

def gal(mid, w=720, q=85):
    return f"{WIX_IMG}{mid}/v1/fill/w_{w},h_{w},al_c,q_{q}/{mid}"

CAT_LABEL = {"pool":"สระว่ายน้ำ","bath":"ห้องน้ำ","roof":"หลังคา / ดาดฟ้า",
             "joint":"รอยต่อ / รอยร้าว","coat":"เคลือบปกป้อง / กาว","tips":"เทคนิค / ความรู้"}

POSTS = [
 {
  "slug": "basement-solution-center",
  "title": "Basement Solution Center",
  "date": "12 ม.ค. 2024", "cat": "roof",
  "desc": "ห้องใต้ดินและพื้นที่ต่ำกว่าระดับดิน — ทำกันซึมด้านนอกให้ดีตั้งแต่ก่อนถมดิน ประหยัดกว่ามาแก้ทีหลังมาก",
  "hero": "00cbb9_7cbf31cd08d94ee0901d079f6227fc59~mv2.jpg",
  "body": [
   "ห้องที่อยู่ระดับต่ำกว่าพื้นดินแนะนำว่าควรทำระบบกันซึมด้านนอกให้ดีไว้ตั้งแต่ก่อนจะถมดินจะประหยัดกว่ามาแก้ไขทีหลังมาก และควรเลือกกันซึมที่ทนรับงานหนักโดยเฉพาะดีกว่าเพราะงานนี้ต้องรับมือกับความชื้นต่อเนื่องเป็นเวลายาวนาน",
   "แต่ถ้าทำไปแล้วเกิดปัญหาตามหลังเราก็มีครบทุก Solution การแก้ปัญหายากๆ แบบนี้ และทุกทางเลือกใช้งานง่ายเป็นหลัก ไม่ว่าจะกันซึมจากภายใน ป้องกันความชื้น สีทนน้ำ โป๊วรอยต่องาน Heavy Duty เรามีครบ",
   "เคมีสำหรับงานพิเศษ นึกถึง Lucerna ได้เลย",
  ],
  "prods": [("DeepSeal กันซึม Negative","/deepseal"),("DryGard","/drygard"),("DeepStick","/deepstick")],
 },
 {
  "slug": "คิดให้ดีก่อนจะรื้อ",
  "title": "คิดให้ดีก่อนจะรื้อ",
  "date": "9 มิ.ย. 2023", "cat": "bath",
  "desc": "อ่านก่อนรื้อกระเบื้องแล้วปูใหม่ — เข้าใจธรรมชาติของคอนกรีตและยาแนว จะได้คุยกับช่างรู้เรื่องและจบงานในรอบเดียว",
  "hero": "00cbb9_bb6ab1a9745547f7ba734a4ddc6fc0fe~mv2.jpg",
  "body": [
   "อยากให้อ่านก่อนที่จะรื้อกระเบื้องแล้วปูใหม่ อย่างน้อยเวลาคุยกับช่างจะได้เข้าใจง่ายและจบงานได้ในรอบเดียว",
   "การปูกระเบื้องใหม่เพื่อป้องกันการรั่วซึมอย่างแรกเลยอย่าไว้ใจคอนกรีต เพราะธรรมชาติของคอนกรีตดูดซึมน้ำได้ดีมากและแตกร้าวได้ง่ายเลยต้องใช้กันซึมผสมคอนกรีตช่วย แต่เราน่าจะเห็นกันมาเป็นเวลายาวนานแล้วว่าใส่ไปยังไงก็ไม่มีใครกล้าการันตีว่าจะไม่รั่วซึม เรื่องนี้ทดลองถามช่างได้เลยว่าการันตีให้ได้หรือไม่ เพราะฉะนั้นเราแนะนำให้ทากันซึมดีๆ อีกหนึ่งชั้นเพื่อป้องกันอีกขั้นจะได้สบายใจ และยิ่งประกอบกับการใช้ยาแนวทั่วๆ ไปที่โดนน้ำไม่นานก็สึกกร่อน น้ำก็ไหลลงไปอยู่ใต้กระเบื้องก็เลยเกิดปัญหาตามกันมาอย่างต่อเนื่อง",
   "คำแนะนำที่ดีที่สุดจากเราคืออย่าหวังมาซ่อมในอนาคตเพราะมันแพงกว่าการป้องกันตั้งแต่เริ่มต้นมาก พื้นที่สำคัญก็แค่ทากันซึมก่อนเทปูนก็ช่วยได้เยอะมากแล้ว",
   "ถึงแม้กันซึมที่ทาทับกระเบื้องจะดีแค่ไหนก็ไม่มีทางทนเท่าการทากันซึมด้านใต้พื้นที่ไม่ต้องโดนแดดเพราะอายุจะยาวนานกว่าปกติมาก แต่ก็ต้องเลือกกันซึมที่ทนการแช่น้ำได้ดีไม่เช่นนั้นก็จะเปื่อยหมดสภาพโดยเราแก้ไขอีกครั้งไม่ได้แล้ว",
  ],
  "prods": [("TileCoat Polyurea","/tilecoatpoly"),("Polyurea Gen3","/polypro")],
 },
 {
  "slug": "seamless-house",
  "title": "Seamless House",
  "date": "3 เม.ย. 2024", "cat": "joint",
  "desc": "ตัวอย่างการใช้ DeepStick และ FillerAce กับงานบ้านไร้รอยต่อ จบปัญหาแตกร้าว ขัดแต่งทำสีได้ตามปกติ",
  "video": "https://video.wixstatic.com/video/00cbb9_7f2c2109fff8483c909ffb3a4adc8f6a/1080p/mp4/file.mp4",
  "body": [
   "ตัวอย่างการใช้ DeepStick และ FillerAce กับงานบ้านไร้รอยต่อ จบปัญหาแตกร้าว ขัดแต่งทำสีได้ตามปกติ",
  ],
  "prods": [("DeepStick","/deepstick"),("FillerAce","/fillerace")],
 },
 {
  "slug": "ชมพลังของ-deepstick-กันชัดๆ",
  "title": "ชมพลังของ DeepStick กันชัดๆ",
  "date": "26 ก.พ. 2024", "cat": "joint",
  "desc": "งานรอยต่อไซโลบนดาดฟ้าโรงงานใหญ่อันดับต้นๆ ของไทย แรงสั่นสะเทือนตลอดเวลา — โป๊วด้วย DeepStick ทับด้วย Polyurea Gen3",
  "body": [
   "งานรอยต่อที่ยากมากๆ สำหรับเราคงไม่มีงานไหนเกินงานนี้แล้ว",
   "เป็นไซโลในโรงงานที่ใหญ่อันดับต้นๆ ของไทย ตั้งอยู่บนดาดฟ้าเจาะทะลุขึ้นมาจากพื้นปูน มีแรงสั่นสะเทือนตลอดเวลา งานนี้มีการทำปูนโอบไว้อย่างดีก็ยังมีรอยรั่วลงไปชั้นล่าง ใช้ตัวโป๊วหรือซิลิโคนทั่วไปไม่ได้เลย",
   "งานนี้ DeepStick แก้ปัญหาได้เรียบร้อยด้วยคุณสมบัติที่ไม่เหมือนใคร เป็นตัวโป๊วที่ยืดหยุ่นแต่มีความเหนียวแน่นในตัวและแรงยึดเกาะสูงมากแม้บนพื้นผิวแปลกๆ แทบจะเรียกว่าพื้นผิวแบบไหนก็โป๊วได้",
   "หลังจากโป๊วให้ทั่วแล้วก็ทาทับพื้นที่ด้วยกันซึมตัว Top ของเราด้วย Polyurea Gen3 ปกติทาเพียง 2 รอบก็พอแต่งานนี้ทา 3 รอบไปเลยเพื่อให้ใช้งานได้ยาวนานยิ่งกว่าเดิม",
  ],
  "gallery": [
   "00cbb9_65ca1f944fe648f9b283d17d835d5a4d~mv2.jpg","00cbb9_44a7aa2d692a49b0b753e1bb79ddf234~mv2.jpg",
   "00cbb9_c16d0d9934f048e79772a195b6641759~mv2.jpg","00cbb9_295478c6800f4c6c9b9dd6a762da88b2~mv2.jpg",
   "00cbb9_64a18ad5a8184d9a8306e042370c2a03~mv2.jpg","00cbb9_6fdfedab5a25474fb11cb7e2365c343b~mv2.jpg",
   "00cbb9_7612f67eb9d64d3bb66778e77f895cd8~mv2.jpg","00cbb9_1d49d77d5c5849aabf4b868f9b16a1a6~mv2.jpg",
   "00cbb9_128a9edf4852455c8bc6b147b223d2dc~mv2.jpg","00cbb9_2e410ba6a5a340209ae348d437d7a441~mv2.jpg",
   "00cbb9_6d6032e5e7d6460395f75f9e88d77512~mv2.jpg","00cbb9_a286b062a3ee4bb09e7855116f8f61a2~mv2.jpg",
   "00cbb9_832992b4c91144c69d375735c9106cb1~mv2.jpg","00cbb9_777193f9d3184279940a8db993b76c1a~mv2.jpg",
   "00cbb9_502b6d4df96f4d60869e8318b13f317f~mv2.jpg","00cbb9_7507e0954c284f21bf16f76ef4cbbdc0~mv2.jpg",
   "00cbb9_031476a4f2c5416c9c8f6681fb6c81ca~mv2.jpg","00cbb9_5b7a26670bb54a0cb4d8da65dd922de5~mv2.jpg",
   "00cbb9_478e3fb99c78479d8591f4f8f663d0c5~mv2.jpg","00cbb9_e4178964b78940bf86e2d2da38e37164~mv2.jpg",
   "00cbb9_2fcf6c54f8eb46cfa6c1352667b66d3e~mv2.jpg","00cbb9_38e08de72e1f4a9c913d0ea51f260389~mv2.jpg",
   "00cbb9_7661c96754fe4254b09a19a47f5334b1~mv2.jpg","00cbb9_ba4d52d621f74e3bbbef18b06d23380a~mv2.jpg",
   "00cbb9_4aaa15198939479aac054308f973cf46~mv2.jpg","00cbb9_ea2660d121764dc4946d79e6142c9c66~mv2.jpg",
   "00cbb9_72ed1fa28aca47258274333be5591d2d~mv2.jpg","00cbb9_1bb8f8f1435f4f01bdc7df37c471acb4~mv2.jpg",
   "00cbb9_03cac759ac8b4048a7a545fe65e7e78e~mv2.jpg","00cbb9_76eb4231d88c462aad354dc21bde83b5~mv2.jpg",
   "00cbb9_7246e10e19a2423b9679d5d6781d69ae~mv2.jpg","00cbb9_c35321e6eb344cb79d3b8430b3d1ac97~mv2.jpg",
   "00cbb9_ae49edd513c44a1d9ac3ab5972e87d58~mv2.jpg","00cbb9_2c86ea9e8c2b4d0387a098be8d838f28~mv2.jpg",
   "00cbb9_933617812f01477e8ef8d6f378cb2cdc~mv2.jpg","00cbb9_97246794009544bcaba4d4c43b1cea39~mv2.jpg",
   "00cbb9_43be01ce672d450a82a3dc36dbe24319~mv2.jpg","00cbb9_5dc56f1c695440fdad9282cb23af43ff~mv2.jpg",
   "00cbb9_af72d92987874154bbaaf2969e6648dd~mv2.jpg","00cbb9_721a3b9b329448dbaa54cd80c68e53da~mv2.jpg",
   "00cbb9_6cc7ebb32e6f4770ac83c1dbac2d21bb~mv2.jpg",
  ],
  "prods": [("DeepStick","/deepstick"),("Polyurea Gen3","/polypro")],
 },
 {
  "slug": "ซ่อมสระว่ายน้ำด้วย-polypro",
  "title": "ซ่อมสระว่ายน้ำด้วย PolyPro",
  "date": "22 ก.พ. 2023", "cat": "pool",
  "desc": "สระรั่วแค่ช่วงบน ไม่ต้องรื้อทั้งสระ — ทาเฉพาะบริเวณที่เกิดปัญหาก็แก้ได้ ประหยัดกว่า เห็นผลทันที ทำเองได้",
  "hero": "00cbb9_967c2d8cef7d41b281a1c7907245669b~mv2.jpg",
  "body": [
   "สระว่ายน้ำรั่วแค่ช่วงบน ไม่ต้องรื้อทั้งสระอีกแล้ว ทาแค่บริเวณที่เกิดปัญหาก็แก้ได้ ประหยัดกว่าและเห็นผลได้ทันที ที่สำคัญทำเองได้เลย",
  ],
  "prods": [("Polyurea Gen3","/polypro")],
 },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Case Study LucernaPro</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://www.lucernapro.com/post/{slug_enc}">
<meta property="og:title" content="{title} | Case Study LucernaPro">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
{og_image}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Anuphan:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{{
  --paper:#F2F2EF; --card:#FFFFFF; --ink:#191C1F; --steel:#5E646A;
  --line:#DCDCD6; --signal:#D8571C; --signal-dark:#ED6A2F; --tag-bg:#ECECE9;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'Anuphan',system-ui,sans-serif;background:var(--paper);color:var(--ink);line-height:1.75;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}}
img{{display:block;max-width:100%;height:auto}}
h1,.brand,.cta h2{{font-family:'Chakra Petch','Anuphan',sans-serif}}
.eyebrow{{font-family:'IBM Plex Mono',monospace}}
.topbar{{position:sticky;top:0;z-index:50;background:rgba(245,244,241,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}}
.topbar-inner{{max-width:1200px;margin:0 auto;padding:12px 20px;display:flex;align-items:center;gap:20px}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:700;letter-spacing:.06em;font-size:1.05rem}}
.brand img{{width:34px;height:34px}}
.brand em{{font-style:normal;color:var(--signal)}}
.topnav{{margin-left:auto;display:flex;gap:22px;font-size:.92rem;font-weight:500;color:var(--steel)}}
.topnav a:hover{{color:var(--ink)}}
.topnav .active{{color:var(--signal);font-weight:600}}
@media(max-width:720px){{.topnav{{display:none}}}}
.btn-chat{{margin-left:auto;display:none;background:var(--signal);color:#fff;font-weight:600;font-size:.88rem;padding:8px 14px;border-radius:8px}}
@media(max-width:720px){{.btn-chat{{display:inline-block}}}}
.wrap{{max-width:820px;margin:0 auto;padding:36px 20px 60px}}
.crumb{{font-size:.86rem;color:var(--steel);margin-bottom:22px}}
.crumb a{{color:var(--signal);font-weight:600}}
.eyebrow{{display:inline-block;font-size:.76rem;font-weight:700;letter-spacing:.16em;color:var(--signal);text-transform:uppercase;margin-bottom:12px}}
h1{{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:700;line-height:1.3;letter-spacing:-.01em}}
.meta{{margin-top:10px;font-size:.86rem;color:var(--steel)}}
.hero-img{{margin:26px 0 6px;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#E9E7E1}}
.hero-img img{{width:100%}}
.postvid{{margin:26px 0 6px;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#000}}
.postvid video{{display:block;width:100%;max-height:78vh}}
article p{{margin-top:20px;font-size:1.02rem}}
.gal{{margin-top:30px;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}}
.gal img{{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:10px;border:1px solid var(--line);background:#E9E7E1}}
.prods{{margin-top:34px;padding-top:22px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.prods .lbl{{font-size:.84rem;color:var(--steel);font-weight:600;margin-right:4px}}
.prods a{{background:var(--tag-bg);border:1px solid var(--line);font-size:.86rem;font-weight:600;color:var(--ink);padding:6px 14px;border-radius:8px;transition:all .15s}}
.prods a:hover{{background:var(--signal);border-color:var(--signal);color:#fff}}
.back{{display:inline-block;margin-top:30px;font-weight:600;color:var(--signal)}}
.back:hover{{color:var(--signal-dark)}}
.cta{{background:var(--ink);color:#fff}}
.cta-inner{{max-width:1200px;margin:0 auto;padding:52px 20px;text-align:center}}
.cta h2{{font-size:clamp(1.4rem,3vw,2rem);font-weight:700}}
.cta p{{color:#B9BFC9;margin:12px auto 24px;max-width:560px}}
.cta-btns{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}}
.btn{{display:inline-block;padding:13px 26px;border-radius:10px;font-weight:600;font-size:.98rem;transition:all .18s}}
.btn-primary{{background:var(--signal);color:#fff}}
.btn-primary:hover{{background:var(--signal-dark)}}
.btn-ghost{{border:1.5px solid #444B57;color:#fff}}
.btn-ghost:hover{{border-color:#fff}}
footer{{background:var(--ink);border-top:1px solid #2A2F38;color:#8A93A1;font-size:.85rem}}
.foot-inner{{max-width:1200px;margin:0 auto;padding:26px 20px;display:flex;flex-wrap:wrap;gap:10px 30px;justify-content:space-between}}
footer a{{color:#B9BFC9}}
footer a:hover{{color:#fff}}
@media (prefers-reduced-motion:reduce){{*,*::before,*::after{{transition:none!important;animation:none!important}}}}
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="/">
      <img src="/img/logo.png" alt="LucernaPro logo" width="34" height="34">
      LUCERNA<em>PRO</em>
    </a>
    <nav class="topnav">
      <a href="/#finder">ค้นหาสินค้า</a>
      <a href="/#waterproof">กันซึม</a>
      <a href="/#flooring">งานพื้น</a>
      <a href="/#coating">เคลือบปกป้อง</a>
      <a class="active" href="/casestudy/">Case Study</a>
      <a href="/#contact">ติดต่อเรา</a>
    </nav>
    <a class="btn-chat" href="https://m.me/lucernapro">แชทเพจ</a>
  </div>
</header>

<main class="wrap">
  <p class="crumb"><a href="/casestudy/">← Case Study ทั้งหมด</a></p>
  <span class="eyebrow">Case Study · {cat_label}</span>
  <h1>{title}</h1>
  <p class="meta">เผยแพร่ {date} · โดยทีมงาน LucernaPro</p>
{media}
  <article>
{paragraphs}
  </article>
{gallery}
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span>{prod_links}</div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
</main>

<section class="cta">
  <div class="cta-inner">
    <h2>หน้างานของคุณคล้ายเคสนี้?</h2>
    <p>ส่งรูปหน้างานหรือเล่าอาการมาได้เลย ทีมงานช่วยวิเคราะห์และแนะนำระบบที่เหมาะกับงบและหน้างานของคุณ ก่อนตัดสินใจซื้อ</p>
    <div class="cta-btns">
      <a class="btn btn-primary" href="https://m.me/lucernapro">💬 ทักแชทเพจ ปรึกษาฟรี</a>
      <a class="btn btn-ghost" href="/#finder">🔎 ค้นหาสินค้าตามปัญหา</a>
    </div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <span>© 2026 บริษัท ลูเซอน่า จำกัด · โทร <a href="tel:0620057933">062-005-7933</a></span>
    <span><a href="/">หน้าแรก</a> · <a href="https://lin.ee/LpUR3Ld">Line @lucerna</a> · <a href="https://www.facebook.com/lucernapro">Facebook</a></span>
  </div>
</footer>

</body>
</html>
"""

def build(p, root):
    slug_enc = urllib.parse.quote(p["slug"], safe="-")
    media = ""
    og_image = ""
    if p.get("video"):
        media = f'  <div class="postvid"><video src="{p["video"]}" controls playsinline preload="metadata"></video></div>'
    elif p.get("hero"):
        media = f'  <div class="hero-img"><img src="{hero(p["hero"])}" alt="{p["title"]}" width="1200" height="900" loading="eager"></div>'
        og_image = f'<meta property="og:image" content="{hero(p["hero"])}">'
    elif p.get("gallery"):
        og_image = f'<meta property="og:image" content="{gal(p["gallery"][0])}">'

    paragraphs = "\n".join(f"    <p>{t}</p>" for t in p["body"])
    gallery = ""
    if p.get("gallery"):
        imgs = "\n".join(
            f'    <img src="{gal(m)}" alt="{p["title"]} — ภาพหน้างานที่ {i+1}" width="720" height="720" loading="lazy">'
            for i, m in enumerate(p["gallery"]))
        gallery = f'  <div class="gal">\n{imgs}\n  </div>'
    prod_links = "".join(f'<a href="{u}">{n}</a>' for n, u in p["prods"])

    html = TEMPLATE.format(
        title=p["title"], desc=p["desc"], slug_enc=slug_enc, og_image=og_image,
        cat_label=CAT_LABEL[p["cat"]], date=p["date"], media=media,
        paragraphs=paragraphs, gallery=gallery, prod_links=prod_links)

    out = os.path.join(root, "post", p["slug"])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("built:", out)

# ============================================================================
# V2 (31 ก.ค. 2026 — มติเจ้าของ): ซีรีส์ case study ใหม่
#   - slug ภาษาอังกฤษเท่านั้น
#   - สองภาษา: /post/{slug} (TH) + /en/post/{slug} (EN) + hreflang ผูกกัน
#   - รูป self-host ใน /img/post/ (ไม่ hotlink wixstatic)
#   - โครงเนื้อหาแบบ step: หัวข้อ + ย่อหน้า + figure พร้อม figcaption
#   - โพสต์เก่า 5 หน้า (POSTS ด้านบน) ใช้ TEMPLATE เดิม regenerate แล้ว byte-identical
# ============================================================================

BASE = "https://www.lucernapro.com"

POSTS_V2 = [
 {
  "slug": "waterproofing-techniques",
  "cat": "roof tips",
  "date_th": "ก.ค. 2026", "date_en": "Jul 2026",
  "thumb": "waterproofing-techniques-02.webp",
  "th": {
   "title": "เทคนิคการใช้งานกันซึมให้ได้ผลดี",
   "desc": "กันซึมไม่ใช่ยาวิเศษ — ขั้นตอนลงกันซึมแบบละเอียดตั้งแต่ตรวจหน้างาน ซ่อมรอยร้าว เสริมไฟเบอร์กลาส ไปจนถึงเทคนิคทาสองรอบให้ทนจริง",
   "cat_label": "เทคนิค / ความรู้",
   "intro": [
    "กันซึมไม่ใช่ยาวิเศษ ถ้าคิดว่าซื้อไปแล้วแค่ทาให้ทั่วพื้นที่ก็จบปัญหา ถ้าทำแบบนี้อาจจะเสียเงินทิ้งโดยไม่เกิดประโยชน์ นี่คือขั้นตอนการลงกันซึมแบบละเอียด แนะนำให้ศึกษาขั้นตอนให้เข้าใจก่อนการซ่อมแซมครับ",
    "หลักคิดสั้นๆ คือ กันซึมที่ดีแค่ไหนก็ช่วยไม่ได้ถ้าพื้นผิวด้านล่างไม่พร้อม งานที่ได้ผลจริงคืองานที่เตรียมพื้นผิวดี ซ่อมจุดอ่อนให้ครบ แล้วค่อยลงกันซึมเป็นขั้นตอนสุดท้าย",
   ],
   "steps": [
    {"h":"ตรวจสอบพื้นที่ก่อนเริ่มงาน",
     "text":["เดินสำรวจให้ทั่วทั้งพื้นที่ก่อน มองหารอยแตกร้าว จุดที่สีหรือปูนหลุดร่อน แนวรอยต่อ และจุดน้ำขัง จดให้ครบว่ามีจุดไหนต้องซ่อมบ้าง เพราะทุกจุดต้องเก็บให้เรียบร้อยก่อนถึงจะลงกันซึมได้"],
     "figs":[("waterproofing-techniques-01.webp","สภาพหน้างานจริงก่อนเริ่ม — ดาดฟ้าเก่า ผิวหน้าแตกลายงาและมีรอยร้าวหลายแนว แบบนี้ทากันซึมทับทันทีไม่ได้")]},
    {"h":"ทำความสะอาดพื้นผิวให้ดี",
     "text":["ล้างด้วยเครื่องฉีดน้ำแรงดันสูงพร้อมขัดคราบฝุ่น ตะไคร่ และสิ่งสกปรกออกให้หมด ส่วนที่หลุดร่อนต้องเอาออกให้เกลี้ยง — กันซึมยึดเกาะได้แค่เท่าที่ผิวสะอาด ถ้าทาทับฝุ่นก็เท่ากับทาอยู่บนฝุ่น เสร็จแล้วปล่อยให้พื้นแห้งก่อนเริ่มขั้นถัดไป"],
     "figs":[("waterproofing-techniques-02.webp","ฉีดล้างแรงดันสูงและกวาดขัดไปพร้อมกัน จุดหลุดร่อนเก็บออกให้หมดในขั้นนี้")]},
    {"h":"รอยแตกร้าวต้องซ่อมก่อน — ห้ามมองข้ามเด็ดขาด",
     "text":["กันซึมชนิดทาไม่ได้ออกแบบมาเพื่ออุดรอยร้าว ถ้าทาทับรอยร้าวตรงๆ พื้นขยับตัวนิดเดียวฟิล์มก็ฉีกตามรอยเดิม โป๊วรอยร้าวให้เต็มและปาดให้เรียบเสมอผิวก่อนเสมอ"],
     "figs":[("waterproofing-techniques-03.webp","โป๊วรอยร้าวบนพื้นให้เต็มร่อง ปาดให้เรียบเสมอผิวเดิม"),
             ("waterproofing-techniques-04.webp","แนวรอยต่อขอบผนังกันตกก็ต้องเก็บให้เรียบร้อยเช่นกัน")]},
    {"h":"รอยต่อพื้น–ผนัง เสริมแรงด้วยไฟเบอร์กลาส",
     "text":["จุดที่พื้นชนผนังคือจุดที่โครงสร้างขยับตัวมากที่สุดและเป็นจุดรั่วยอดนิยม ทากันซึมเปล่าๆ ไม่พอ ให้วางแผ่นไฟเบอร์กลาสคาดแนวรอยต่อแล้วทาน้ำยาทับให้ชุ่มจนแผ่นใสแนบไปกับผิว ส่วนงานเข้ามุมใช้ตาข่ายเสริมแรงช่วยให้เข้ารูปง่ายขึ้น"],
     "figs":[("waterproofing-techniques-05.webp","วางแผ่นไฟเบอร์กลาสคาดแนวรอยต่อพื้น–ผนัง"),
             ("waterproofing-techniques-06.webp","ทาน้ำยาทับจนแผ่นไฟเบอร์อิ่มตัว ใสแนบไปกับพื้นผิว"),
             ("waterproofing-techniques-07.webp","เก็บแนวรอยต่อรอบขอบผนังให้ต่อเนื่องกันทั้งแนว"),
             ("waterproofing-techniques-08.webp","งานเข้ามุมใช้ตาข่ายเสริมแรงร่วมด้วย มุมจะแข็งแรงและเข้ารูปสวย")]},
    {"h":"สีสองส่วนผสม ต้องตวงให้ตรงตามคู่มือ",
     "text":["ห้ามกะด้วยสายตาเด็ดขาด ใช้เครื่องชั่งหรือถ้วยตวงตามอัตราส่วนในคู่มือของแต่ละรุ่น ผสมแล้วกวนให้เข้ากันจริงๆ อย่างน้อย 1 นาที กวาดเนื้อที่เกาะข้างถังลงมากวนด้วย — เกือบทุกเคส \u201cทาแล้วไม่แห้ง\u201d ที่เราเจอ มาจากตวงผิดหรือกวนไม่เข้ากัน"],
     "figs":[("waterproofing-techniques-09.webp","ตวงสองส่วนด้วยถ้วยตวงตามอัตราส่วนที่คู่มือกำหนดเป๊ะๆ"),
             ("waterproofing-techniques-10.webp","ผสมเสร็จเริ่มงานได้ทันที อย่าผสมทิ้งไว้เกินเวลาที่คู่มือกำหนด")]},
    {"h":"รอบแรกทาให้บางที่สุด",
     "text":["ใช้ลูกกลิ้งรีดแรงๆ ให้ฟิล์มบางที่สุด รอบนี้ไม่ต้องเน้นสวย หน้าที่ของมันคือยึดเกาะกับพื้นผิวและกันไม่ให้พื้นดูดสีรอบถัดไปมากเกินไป"],
     "figs":[("waterproofing-techniques-11.webp","รอบแรกรีดลูกกลิ้งให้บางและทั่วถึง")]},
    {"h":"รอบสองเก็บความหนาให้สม่ำเสมอ",
     "text":["เว้นระยะจากรอบแรกประมาณ 2 ชั่วโมง (ดูตัวเลขจริงจากคู่มือของรุ่นที่ใช้) รอบนี้เก็บงานให้สีสม่ำเสมอทั่วกันและทาให้ได้ความหนา เพราะความหนาของฟิล์มคือความทนทานของงาน"],
     "figs":[("waterproofing-techniques-12.webp","รอบสองเก็บเนื้อให้เต็มและสม่ำเสมอทั้งผืน")]},
    {"h":"เสร็จแล้วอย่าเพิ่งรีบใช้งาน",
     "text":["ปล่อยให้ฟิล์มเซ็ตตัวเต็มที่ก่อนเดินใช้งานหรือให้โดนน้ำ พื้นทั่วไปเริ่มที่ราว 6 ชั่วโมงหลังทารอบสุดท้าย และยึดตัวเลขจากคู่มือของรุ่นที่ใช้เป็นหลัก ใจเย็นอีกนิดเดียว แลกกับงานที่อยู่ได้อีกหลายปี"],
     "figs":[("waterproofing-techniques-13.webp","งานเสร็จสมบูรณ์ — ผิวเรียบต่อเนื่องไร้รอยต่อทั้งดาดฟ้า")]},
   ],
   "prods":[("PatchPro","/patchpro"),("Modern Fiberglass","/modernfiberglass"),
            ("กันซึม SiliconePro","/siliconepro"),("กันซึม Polyurea","/polyurea")],
  },
  "en": {
   "title": "Waterproofing Techniques That Actually Work",
   "desc": "Waterproofing isn't magic in a bucket. The full step-by-step: inspection, crack repair, fiberglass reinforcement, proper mixing, and the two-coat technique.",
   "cat_label": "Tips / Know-how",
   "intro": [
    "Waterproofing is not a magic potion. If you think you can buy a bucket, roll it over the whole area and call the problem solved — that is how money gets wasted. Here is the full, detailed procedure. Study it before you start the repair, not after.",
    "The short version: the best coating in the world cannot save a badly prepared surface. Jobs that last are jobs where the prep was done properly, every weak spot was fixed first, and the waterproofing went on last.",
   ],
   "steps": [
    {"h":"Inspect the area before you start",
     "text":["Walk the entire surface first. Look for cracks, flaking paint or render, joint lines and spots where water ponds. Note every problem point — each one has to be dealt with before any coating goes down."],
     "figs":[("waterproofing-techniques-01.webp","The job as found — an aged deck with alligator cracking across the surface. You do not coat over this as-is.")]},
    {"h":"Clean the surface properly",
     "text":["Pressure-wash and scrub off dust, algae and grime. Anything loose or flaking must come off completely — a coating only bonds as well as the surface is clean. Paint over dust and you are standing on dust. Let the surface dry before moving on."],
     "figs":[("waterproofing-techniques-02.webp","High-pressure washing and brushing in one pass. Loose material gets removed at this stage.")]},
    {"h":"Repair every crack first — no exceptions",
     "text":["Roll-on waterproofing is not a crack filler. Coat straight over a crack and the film tears along the same line the moment the slab moves. Fill cracks completely and trowel them flush before anything else."],
     "figs":[("waterproofing-techniques-03.webp","Floor cracks filled and troweled flush with the original surface"),
             ("waterproofing-techniques-04.webp","The parapet joint line gets the same treatment before coating")]},
    {"h":"Reinforce floor-to-wall joints with fiberglass",
     "text":["Where the floor meets the wall is where the structure moves most — and where leaks love to start. Coating alone is not enough here. Lay fiberglass mat across the joint and saturate it with the liquid until it turns transparent and hugs the surface. For corners, reinforcing mesh makes the shape much easier to form."],
     "figs":[("waterproofing-techniques-05.webp","Fiberglass mat laid across the floor-to-wall joint"),
             ("waterproofing-techniques-06.webp","Saturate until the mat turns transparent and sits tight against the surface"),
             ("waterproofing-techniques-07.webp","Run the reinforcement continuously along the full parapet line"),
             ("waterproofing-techniques-08.webp","Corners get reinforcing mesh — strong, and much easier to shape")]},
    {"h":"Two-part products: measure exactly as the manual says",
     "text":["Never eyeball the ratio. Use a scale or measuring cups, mix for at least a full minute, and scrape the material clinging to the sides of the bucket back into the mix. Nearly every \u201cit never dried\u201d case we see comes down to a wrong ratio or lazy mixing."],
     "figs":[("waterproofing-techniques-09.webp","Both parts measured out exactly per the manual"),
             ("waterproofing-techniques-10.webp","Once mixed, start working — do not let it sit past the pot life in the manual")]},
    {"h":"First coat: as thin as possible",
     "text":["Press the roller hard and stretch the film as thin as you can. This coat is not supposed to look pretty — its job is to grip the surface and stop it drinking up the next coat."],
     "figs":[("waterproofing-techniques-11.webp","First coat rolled out thin and even across the whole area")]},
    {"h":"Second coat: build even thickness",
     "text":["Wait about 2 hours after the first coat (check your product's manual for the exact figure). This is the coat where you build uniform color and full film thickness — and film thickness is what durability is made of."],
     "figs":[("waterproofing-techniques-12.webp","Second coat builds the film to full, even thickness")]},
    {"h":"Done? Don't rush back onto it",
     "text":["Let the film cure fully before foot traffic or water. For typical floors that starts at around 6 hours after the final coat — follow your product's manual for the real number. A little patience here buys you years of service."],
     "figs":[("waterproofing-techniques-13.webp","Finished — one continuous, seamless surface across the entire deck")]},
   ],
   "prods":[("PatchPro","/en/patchpro"),("Modern Fiberglass","/en/modernfiberglass"),
            ("SiliconePro Waterproofing","/en/siliconepro"),("Polyurea Waterproofing","/en/polyurea")],
  },
 },
]

V2_CSS = """:root{{
  --paper:#F2F2EF; --card:#FFFFFF; --ink:#191C1F; --steel:#5E646A;
  --line:#DCDCD6; --signal:#D8571C; --signal-dark:#ED6A2F; --tag-bg:#ECECE9;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'Anuphan',system-ui,sans-serif;background:var(--paper);color:var(--ink);line-height:1.75;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}}
img{{display:block;max-width:100%;height:auto}}
h1,h2,.brand,.cta h2{{font-family:'Chakra Petch','Anuphan',sans-serif}}
.eyebrow{{font-family:'IBM Plex Mono',monospace}}
.topbar{{position:sticky;top:0;z-index:50;background:rgba(245,244,241,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}}
.topbar-inner{{max-width:1200px;margin:0 auto;padding:12px 20px;display:flex;align-items:center;gap:20px}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:700;letter-spacing:.06em;font-size:1.05rem}}
.brand img{{width:34px;height:34px}}
.brand em{{font-style:normal;color:var(--signal)}}
.topnav{{margin-left:auto;display:flex;gap:22px;font-size:.92rem;font-weight:500;color:var(--steel)}}
.topnav a:hover{{color:var(--ink)}}
.topnav .active{{color:var(--signal);font-weight:600}}
@media(max-width:720px){{.topnav{{display:none}}}}
.btn-chat{{margin-left:auto;display:none;background:var(--signal);color:#fff;font-weight:600;font-size:.88rem;padding:8px 14px;border-radius:8px}}
@media(max-width:720px){{.btn-chat{{display:inline-block}}}}
.wrap{{max-width:820px;margin:0 auto;padding:36px 20px 60px}}
.crumb{{font-size:.86rem;color:var(--steel);margin-bottom:22px;display:flex;justify-content:space-between;gap:12px}}
.crumb a{{color:var(--signal);font-weight:600}}
.crumb .lang{{color:var(--steel);font-weight:500}}
.crumb .lang:hover{{color:var(--ink)}}
.eyebrow{{display:inline-block;font-size:.76rem;font-weight:700;letter-spacing:.16em;color:var(--signal);text-transform:uppercase;margin-bottom:12px}}
h1{{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:700;line-height:1.3;letter-spacing:-.01em}}
.meta{{margin-top:10px;font-size:.86rem;color:var(--steel)}}
article p{{margin-top:20px;font-size:1.02rem}}
.step{{margin-top:44px}}
.step h2{{font-size:clamp(1.15rem,2.6vw,1.45rem);font-weight:700;line-height:1.35;display:flex;gap:12px;align-items:baseline}}
.step .n{{font-family:'IBM Plex Mono',monospace;font-size:.82rem;font-weight:600;color:var(--signal);letter-spacing:.08em;flex:none}}
.step p{{margin-top:12px}}
.step figure{{margin-top:18px}}
.step img{{width:100%;border-radius:12px;border:1px solid var(--line);background:#E9E7E1}}
.step img.tall{{max-width:560px;margin:0 auto}}
.step figcaption{{margin-top:8px;font-size:.88rem;color:var(--steel)}}
.prods{{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.prods .lbl{{font-size:.84rem;color:var(--steel);font-weight:600;margin-right:4px}}
.prods a{{background:var(--tag-bg);border:1px solid var(--line);font-size:.86rem;font-weight:600;color:var(--ink);padding:6px 14px;border-radius:8px;transition:all .15s}}
.prods a:hover{{background:var(--signal);border-color:var(--signal);color:#fff}}
.back{{display:inline-block;margin-top:30px;font-weight:600;color:var(--signal)}}
.back:hover{{color:var(--signal-dark)}}
.cta{{background:var(--ink);color:#fff}}
.cta-inner{{max-width:1200px;margin:0 auto;padding:52px 20px;text-align:center}}
.cta h2{{font-size:clamp(1.4rem,3vw,2rem);font-weight:700}}
.cta p{{color:#B9BFC9;margin:12px auto 24px;max-width:560px}}
.cta-btns{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}}
.btn{{display:inline-block;padding:13px 26px;border-radius:10px;font-weight:600;font-size:.98rem;transition:all .18s}}
.btn-primary{{background:var(--signal);color:#fff}}
.btn-primary:hover{{background:var(--signal-dark)}}
.btn-ghost{{border:1.5px solid #444B57;color:#fff}}
.btn-ghost:hover{{border-color:#fff}}
footer{{background:var(--ink);border-top:1px solid #2A2F38;color:#8A93A1;font-size:.85rem}}
.foot-inner{{max-width:1200px;margin:0 auto;padding:26px 20px;display:flex;flex-wrap:wrap;gap:10px 30px;justify-content:space-between}}
footer a{{color:#B9BFC9}}
footer a:hover{{color:#fff}}
@media (prefers-reduced-motion:reduce){{*,*::before,*::after{{transition:none!important;animation:none!important}}}}"""

TEMPLATE_V2_TH = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Case Study LucernaPro</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}/post/{slug}">
<link rel="alternate" hreflang="th" href="{base}/post/{slug}">
<link rel="alternate" hreflang="en" href="{base}/en/post/{slug}">
<link rel="alternate" hreflang="x-default" href="{base}/post/{slug}">
<meta property="og:title" content="{title} | Case Study LucernaPro">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:image" content="{base}/img/post/{thumb}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Anuphan:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<style>
""" + V2_CSS + """
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="/">
      <img src="/img/logo.png" alt="LucernaPro logo" width="34" height="34">
      LUCERNA<em>PRO</em>
    </a>
    <nav class="topnav">
      <a href="/#finder">ค้นหาสินค้า</a>
      <a href="/#waterproof">กันซึม</a>
      <a href="/#flooring">งานพื้น</a>
      <a href="/#coating">เคลือบปกป้อง</a>
      <a class="active" href="/casestudy/">Case Study</a>
      <a href="/#contact">ติดต่อเรา</a>
    </nav>
    <a class="btn-chat" href="https://m.me/lucernapro">แชทเพจ</a>
  </div>
</header>

<main class="wrap">
  <p class="crumb"><a href="/casestudy/">← Case Study ทั้งหมด</a><a class="lang" href="/en/post/{slug}">English</a></p>
  <span class="eyebrow">Case Study · {cat_label}</span>
  <h1>{title}</h1>
  <p class="meta">เผยแพร่ {date} · โดยทีมงาน LucernaPro</p>
  <article>
{intro}
{steps}
  </article>
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span>{prod_links}</div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
</main>

<section class="cta">
  <div class="cta-inner">
    <h2>หน้างานของคุณคล้ายเคสนี้?</h2>
    <p>ส่งรูปหน้างานหรือเล่าอาการมาได้เลย ทีมงานช่วยวิเคราะห์และแนะนำระบบที่เหมาะกับงบและหน้างานของคุณ ก่อนตัดสินใจซื้อ</p>
    <div class="cta-btns">
      <a class="btn btn-primary" href="https://m.me/lucernapro">💬 ทักแชทเพจ ปรึกษาฟรี</a>
      <a class="btn btn-ghost" href="/#finder">🔎 ค้นหาสินค้าตามปัญหา</a>
    </div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <span>© 2026 บริษัท ลูเซอน่า จำกัด · โทร <a href="tel:0620057933">062-005-7933</a></span>
    <span><a href="/">หน้าแรก</a> · <a href="https://lin.ee/LpUR3Ld">Line @lucerna</a> · <a href="https://www.facebook.com/lucernapro">Facebook</a></span>
  </div>
</footer>

</body>
</html>
"""

TEMPLATE_V2_EN = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Case Study LucernaPro</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}/en/post/{slug}">
<link rel="alternate" hreflang="th" href="{base}/post/{slug}">
<link rel="alternate" hreflang="en" href="{base}/en/post/{slug}">
<link rel="alternate" hreflang="x-default" href="{base}/post/{slug}">
<meta property="og:title" content="{title} | Case Study LucernaPro">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:image" content="{base}/img/post/{thumb}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Anuphan:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<style>
""" + V2_CSS + """
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="/">
      <img src="/img/logo.png" alt="LucernaPro logo" width="34" height="34">
      LUCERNA<em>PRO</em>
    </a>
    <nav class="topnav">
      <a href="/#finder">Products</a>
      <a href="/#waterproof">Waterproofing</a>
      <a href="/#flooring">Flooring</a>
      <a href="/#coating">Protection</a>
      <a class="active" href="/en/casestudy/">Case Study</a>
      <a href="/#contact">Contact</a>
    </nav>
    <a class="btn-chat" href="https://m.me/lucernapro">Chat</a>
  </div>
</header>

<main class="wrap">
  <p class="crumb"><a href="/en/casestudy/">← All case studies</a><a class="lang" href="/post/{slug}">ภาษาไทย</a></p>
  <span class="eyebrow">Case Study · {cat_label}</span>
  <h1>{title}</h1>
  <p class="meta">Published {date} · by the LucernaPro team</p>
  <article>
{intro}
{steps}
  </article>
  <div class="prods"><span class="lbl">Products used on this job:</span>{prod_links}</div>
  <a class="back" href="/en/casestudy/">← Back to all case studies</a>
</main>

<section class="cta">
  <div class="cta-inner">
    <h2>Facing something similar?</h2>
    <p>Send us photos of your site or describe the problem. Our team will analyze it and recommend the right system for your job and budget — before you spend a baht.</p>
    <div class="cta-btns">
      <a class="btn btn-primary" href="https://m.me/lucernapro">💬 Chat with us — free advice</a>
      <a class="btn btn-ghost" href="/#finder">🔎 Find a product by problem</a>
    </div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <span>© 2026 Lucerna Co., Ltd. · Tel <a href="tel:+66620057933">+66 62-005-7933</a></span>
    <span><a href="/">Home</a> · <a href="https://lin.ee/LpUR3Ld">Line @lucerna</a> · <a href="https://www.facebook.com/lucernapro">Facebook</a></span>
  </div>
</footer>

</body>
</html>
"""

# รูปแนวตั้ง (สูงกว่ากว้าง) — จำกัดความกว้างด้วย class .tall กันภาพล้นจอ
V2_TALL = {"waterproofing-techniques-07.webp","waterproofing-techniques-08.webp","waterproofing-techniques-11.webp"}

def render_v2_body(lang_data, alt_prefix):
    intro = "\n".join(f"    <p>{t}</p>" for t in lang_data["intro"])
    blocks = []
    for i, s in enumerate(lang_data["steps"], 1):
        b  = f'    <section class="step">\n'
        b += f'      <h2><span class="n">{i:02d}</span>{s["h"]}</h2>\n'
        for t in s.get("text", []):
            b += f'      <p>{t}</p>\n'
        for fn, cap in s.get("figs", []):
            tall = ' class="tall"' if fn in V2_TALL else ""
            b += (f'      <figure><img{tall} src="/img/post/{fn}" alt="{alt_prefix} — {cap}" loading="lazy">'
                  f'<figcaption>{cap}</figcaption></figure>\n')
        b += "    </section>"
        blocks.append(b)
    return intro, "\n".join(blocks)

def build_v2(p, root):
    for lang, tpl, outdir, date in (
        ("th", TEMPLATE_V2_TH, os.path.join(root, "post", p["slug"]), p["date_th"]),
        ("en", TEMPLATE_V2_EN, os.path.join(root, "en", "post", p["slug"]), p["date_en"]),
    ):
        d = p[lang]
        intro, steps = render_v2_body(d, d["title"])
        prod_links = "".join(f'<a href="{u}">{n}</a>' for n, u in d["prods"])
        html = tpl.format(title=d["title"], desc=d["desc"], slug=p["slug"], base=BASE,
                          thumb=p["thumb"], cat_label=d["cat_label"], date=date,
                          intro=intro, steps=steps, prod_links=prod_links)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("built:", outdir)

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for p in POSTS:
        build(p, root)
    for p in POSTS_V2:
        build_v2(p, root)
