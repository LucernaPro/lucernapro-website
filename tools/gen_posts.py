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
  /* ═══ MOBILE DRAWER MENU (ถอนได้: ลบ 3 บล็อกที่มี marker นี้: CSS/HTML/JS) ═══ */
  .mnav-btn,.mnav,.mnav-scrim{{display:none}}
  @media(max-width:860px){{
    .theme-toggle,.lang-switch{{display:none}}
    .mnav-scrim{{display:block}}
    .cta-chat{{display:inline-flex;margin-left:auto}}
    .mnav-btn{{display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:8px;padding:6px 10px;font-size:17px;line-height:1;cursor:pointer}}
    .mnav-btn:hover{{border-color:var(--orange)}}
    .mnav-scrim{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:98;opacity:0;pointer-events:none;transition:opacity .22s ease}}
    .mnav-scrim.open{{opacity:1;pointer-events:auto}}
    .mnav{{position:fixed;top:0;bottom:0;left:0;width:min(280px,82vw);z-index:99;background:var(--panel);border-right:1px solid var(--line);padding:20px 22px 18px;display:flex;flex-direction:column;transform:translateX(-105%);transition:transform .26s ease;overflow-y:auto}}
    .mnav.open{{transform:translateX(0)}}
    .mnav-head{{display:flex;align-items:center;justify-content:space-between}}
    .mnav-brand{{font-family:var(--disp);font-weight:700;font-size:16px;letter-spacing:.04em;color:var(--ink)}}
    .mnav-brand em{{color:var(--orange);font-style:normal}}
    .mnav-close{{background:none;border:none;color:var(--muted);font-size:19px;line-height:1;cursor:pointer;padding:4px}}
    .mnav-tag{{font-size:11.5px;color:var(--muted);margin-top:3px}}
    .mnav-k{{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;color:var(--orange);margin:22px 0 4px}}
    .mnav-links{{display:flex;flex-direction:column}}
    .mnav-links a{{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-bottom:1px solid var(--line);font-size:16.5px;color:var(--ink)}}
    .mnav-links a:last-child{{border-bottom:none}}
    .mnav-links a span{{color:var(--orange)}}
    .mnav-chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}}
    .mnav-chips a{{font-size:12.5px;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:6px 13px}}
    .mnav-util{{display:flex;align-items:center;gap:10px;padding:12px 0;border-top:1px solid var(--line);margin-top:auto}}
    .mnav-util .mnav-lang{{font-family:var(--mono);font-size:12px;letter-spacing:.08em;border:1px solid var(--line);border-radius:8px;padding:5px 12px;color:var(--muted)}}
    .mnav-util .mnav-theme{{background:none;border:1px solid var(--line);border-radius:8px;padding:4px 11px;font-size:14px;line-height:1.4;cursor:pointer;color:var(--ink)}}
    .mnav-chat{{background:#1877F2;border-radius:10px;text-align:center;padding:11px 0;font-size:14px;color:#fff;font-weight:600;margin-top:2px}}
  }}
  /* ═══ จบบล็อก CSS MOBILE DRAWER MENU ═══ */
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <button class="mnav-btn" id="mnavBtn" aria-label="เปิดเมนู" aria-expanded="false">☰</button>
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
    <a class="btn-chat" href="https://lin.ee/LpUR3Ld" style="background:#06C755"><span style="display:inline-grid;place-items:center;border-radius:5px;background:#fff;color:#06C755;font-weight:800;font-size:9px;font-family:Arial,sans-serif;line-height:1;padding:3px 4px;letter-spacing:.02em;margin-right:7px;vertical-align:1px">LINE</span>แอดไลน์</a>
  </div>
</header>

<!-- ═══ MOBILE DRAWER MENU: ลิ้นชัก (ถอนได้) ═══ -->
<div class="mnav-scrim" id="mnavScrim" aria-hidden="true"></div>
<aside class="mnav" id="mnav" aria-label="เมนูหลัก">
  <div class="mnav-head">
    <span class="mnav-brand"><img src="/img/logo.png" alt="" width="24" height="24" style="object-fit:contain;vertical-align:-6px;margin-right:8px">LUCERNA<em>PRO</em></span>
    <button class="mnav-close" id="mnavClose" aria-label="ปิดเมนู">✕</button>
  </div>
  <div class="mnav-tag" style="font-family:var(--mono);letter-spacing:.05em">Real deal or nothing</div>
  <div class="mnav-k">MENU</div>
  <nav class="mnav-links">
    <a href="/">หน้าแรก <span>→</span></a>
    <a href="/#finder">สินค้าทั้งหมด <span>→</span></a>
    <a href="/casestudy/">Case Study <span>→</span></a>
    <a href="/#contact">ติดต่อเรา <span>→</span></a>
  </nav>
  <div class="mnav-k">SHORTCUTS</div>
  <div class="mnav-chips">
    <a href="/#waterproof">กันซึม</a>
    <a href="/#flooring">งานพื้น</a>
    <a href="/#coating">เคลือบปกป้อง</a>
  </div>
  <div class="mnav-util">
    <button class="mnav-theme" id="mnavTheme" aria-label="สลับโหมดสี">🌙</button>
  </div>
  <a class="mnav-chat" href="https://m.me/lucernapro">f&nbsp; แชทเพจ — ตอบไว</a>
</aside>
<!-- ═══ จบลิ้นชัก MOBILE DRAWER MENU ═══ -->


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

<!-- ═══ MOBILE DRAWER MENU: JS (ถอนได้) ═══ -->
<script>
(function(){{
  var mn=document.getElementById('mnav'),sc=document.getElementById('mnavScrim'),
      bt=document.getElementById('mnavBtn'),cl=document.getElementById('mnavClose'),
      tb=document.getElementById('mnavTheme'),master=document.getElementById('themeToggle');
  if(!mn||!bt)return;
  function set(open){{
    mn.classList.toggle('open',open);sc.classList.toggle('open',open);
    bt.setAttribute('aria-expanded',open?'true':'false');
    document.body.style.overflow=open?'hidden':'';
  }}
  bt.addEventListener('click',function(){{set(true)}});
  cl.addEventListener('click',function(){{set(false)}});
  sc.addEventListener('click',function(){{set(false)}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')set(false)}});
  window.addEventListener('pageshow',function(){{set(false)}});
  mn.querySelectorAll('.mnav-links a,.mnav-chips a,.mnav-chat').forEach(function(a){{
    a.addEventListener('click',function(){{set(false)}});
  }});
  if(tb){{
    if(!master){{tb.style.display='none';}}
    else{{
      function syncT(){{tb.textContent=document.documentElement.dataset.theme==='dark'?'☀️':'🌙';}}
      tb.addEventListener('click',function(){{master.click();syncT();}});
      syncT();
    }}
  }}
}})();
</script>
<!-- ═══ จบ JS MOBILE DRAWER MENU ═══ -->
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
  "slug": "why-coating-over-cracks-fails",
  "cat": "joint tips",
  "date_th": "ส.ค. 2026", "date_en": "Aug 2026",
  "thumb": "why-coating-over-cracks-fails-00.webp",
  "th": {
   "title": "มีรอยร้าวแล้วไม่โป๊วก่อนทากันซึม — ทำไมถึงไม่รอด",
   "desc": "จากประสบการณ์หน้างานของเรา งานที่ทากันซึมทับรอยร้าวตรงๆ โดยไม่โป๊วก่อน จบด้วยการรั่วซ้ำตามแนวเดิมแทบทุกครั้ง — นี่คือเหตุผลเชิงกลไกว่าทำไม และขั้นตอนที่ทำให้จบในรอบเดียว",
   "cat_label": "รอยต่อ / รอยร้าว",
   "hero": ("why-coating-over-cracks-fails-00.webp", "สภาพแบบนี้เห็นแล้วทุกคนรู้ว่าต้องโป๊วก่อน — แต่ประเด็นจริงคือ รอยที่เล็กกว่านี้หลายเท่าก็ต้องโป๊วก่อนเหมือนกัน และนั่นคือจุดที่งานส่วนใหญ่พลาด"),
   "intro": [
    "มีคำถามหนึ่งที่เราเจอบ่อยมาก: \u201cพื้นหรือกำแพงมีรอยร้าวนิดหน่อย ทากันซึมทับเลยได้ไหม สเปกก็บอกว่ายืดหยุ่นสูง\u201d คำตอบจากประสบการณ์ตรงของเราคือ ไม่แนะนำเด็ดขาด เพราะงานแบบนี้ทำแล้วก็ไม่จบ — ลูกค้าที่ข้ามขั้นตอนโป๊ว เกือบทั้งหมดกลับมาหาเราอีกครั้งด้วยอาการเดิม รั่วตามแนวรอยเดิมเป๊ะ",
    "เคสนี้จะอธิบายเหตุผลเชิงกลไกให้เห็นภาพว่าทำไมฟิล์มกันซึมถึงแพ้รอยร้าวเสมอถ้าไม่โป๊วก่อน และขั้นตอนที่ถูกต้องที่ทำให้งานจบในรอบเดียว ไม่ต้องกลับมาทาซ้ำทุกครึ่งปี",
   ],
   "steps": [
    {"h":"รอยร้าวไม่ใช่แค่รอยบนผิว — มันคือจุดที่โครงสร้างขยับ",
     "text":["คอนกรีตกับปูนขยายตัวเมื่อร้อนและหดตัวเมื่อเย็น สลับกันแบบนี้ทุกวัน และรอยร้าวก็คือจุดที่โครงสร้างเลือกแล้วว่าจะปลดปล่อยการขยับทั้งหมดตรงนั้น ต่อให้มองด้วยตาเปล่าเห็นนิ่งสนิท จริงๆ มันกำลังอ้า-หุบระดับเสี้ยวมิลลิเมตรอยู่ตลอด กลางวันแดดเผาผนังหรือดาดฟ้าจนร้อนจัด กลางคืนเย็นลง วนแบบนี้ปีละสามร้อยกว่ารอบ ฟิล์มกันซึมที่ทาพาดข้ามรอยไว้เฉยๆ ต้องรับการขยับทั้งหมดนี้ไว้ที่เส้นเดียว"],
     "figs":[("why-coating-over-cracks-fails-01.webp","วันแรกดูเรียบร้อย แต่ฟิล์มแค่พาดข้ามรอยร้าว ไม่ได้อุดข้างใน — พอโครงสร้างขยับ การยืดทั้งหมดกระจุกที่เส้นเดียวจนฟิล์มขาดตามแนวรอยเดิม")]},
    {"h":"ทำไมฟิล์ม \u201cยืดหยุ่นสูง\u201d ก็ยังขาด — เลขมันฟ้อง",
     "text":["สเปกการยืดตัวหลายร้อยเปอร์เซ็นต์บนฉลาก วัดจากการดึงแผ่นฟิล์มอิสระทั้งผืนในครั้งเดียว แต่หน้างานจริงฟิล์มถูกยึดติดแน่นกับปูนทั้งสองฝั่งของรอยร้าว ช่วงที่ยืดได้จริงจึงเหลือแค่ความกว้างของรอยเส้นเดียว สมมติรอยกว้าง 0.5 มม. อ้าเพิ่มอีกแค่ 0.5 มม. ฟิล์มตรงเส้นนั้นต้องยืดถึง 100% ทันที แล้วโดนดึง-หดแบบนี้ซ้ำทุกวันไม่ใช่ครั้งเดียวเหมือนตอนเทสต์ วัสดุอะไรก็ล้าและขาดในที่สุด จุดที่ขาดก็คือแนวรอยเดิมเป๊ะ นี่คือเหตุผลที่หลายคนเห็นรอยเดิมค่อยๆ ลางๆ ขึ้นมาบนผิวกันซึมหลังผ่านไปไม่กี่เดือน"],
     "figs":[]},
    {"h":"ขาดแล้วเรื่องไม่จบแค่นั้น — น้ำเดินใต้ฟิล์ม โผล่คนละที่กับรอย",
     "text":["พอฟิล์มขาดหรือน้ำหาทางเข้าได้จากฝั่งไหนก็ตาม น้ำจะเดินตามโพรงในเนื้อปูนและช่องว่างใต้ฟิล์มไปได้ไกลเป็นเมตร จุดที่เห็นน้ำหยดหรือฟิล์มพองเป็นถุงน้ำ จึงมักไม่ใช่จุดที่ร้าวจริง หลายคนทาซ้ำตรงจุดที่เห็นหยดแล้วก็ไม่หายสักที เพราะรอยร้าวตัวจริงอยู่อีกที่หนึ่ง ถ้าเจออาการแบบนี้ให้กลับไปหาจุดรั่วตัวจริงให้เจอก่อนเสมอ — เรามีเทคนิคกั้นดินน้ำมันขังน้ำหาจุดรั่วอยู่ในเคส <a href=\"/post/finding-the-real-leak-point\">หาจุดรั่วให้เจอก่อน แล้วค่อยทากันซึม</a>"],
     "figs":[("why-coating-over-cracks-fails-03.webp","น้ำเข้าที่รอยร้าวจุดหนึ่ง เดินตามโพรงในเนื้อปูน แล้วไปโผล่เป็นหยดน้ำห่างออกไปได้เป็นเมตร — ทาทับตรงจุดหยดจึงไม่มีวันหาย")]},
    {"h":"จากหน้างานจริง: วงจร \u201cทำแล้วไม่จบ\u201d",
     "text":["ลำดับเหตุการณ์ที่เราเจอซ้ำจนเดาตอนจบได้: ทาทับรอยร้าวเลยเพราะอยากประหยัดเวลา เดือนแรกทุกอย่างดูเรียบร้อยดี พอผ่านหน้าร้อนจัดหรือฝนหนักรอบแรก รอยเดิมเริ่มลางๆ ขึ้นมาบนผิวกันซึม แล้วก็รั่วซ้ำจุดเดิม สุดท้ายต้องซื้อมาทาใหม่อีกรอบทั้งที่ต้นเหตุยังอยู่ครบ วนแบบนี้ไปได้เรื่อยๆ ค่าของรวมค่าแรงแซงค่าโป๊วตั้งแต่รอบที่สองแล้ว — โป๊วเพิ่มงานแค่วันเดียว แต่ตัดวงจรนี้ทิ้งทั้งเส้น"],
     "figs":[("why-coating-over-cracks-fails-02.webp","เทียบกันชัดๆ: ทาทับเลยคือจ่ายค่าของกับค่าแรงวนลูป ส่วนโป๊วก่อนทาเพิ่มงานวันเดียวแล้วจบถาวร")]},
    {"h":"ขั้นตอนที่ถูก: โป๊วให้จบก่อน แล้วค่อยทา",
     "text":["หนึ่ง เปิดร่องรอยร้าวก่อน โดยเฉพาะรอยร้าวเส้นผมต้องเจียรเปิดร่องให้กว้างพอที่เนื้อโป๊วจะลงไปเต็ม อย่าโป๊วปิดแค่ปากรอย สอง โป๊วให้เต็มร่องแล้วปาดเรียบเสมอผิวเดิม สาม รอให้เซ็ตตัวเต็มที่ตามคู่มือของตัวโป๊วที่ใช้ แล้วค่อยลงกันซึมตามระบบปกติเป็นขั้นตอนสุดท้าย",
             "ส่วนจะโป๊วด้วยตัวไหน เลือกให้ตรงหน้างาน: งานพื้นและดาดฟ้าคอนกรีตใช้ PatchPro งานผนังปูน-คอนกรีตใช้ FillerAce หลังคาเมทัลชีทใช้ SpackleFlex ส่วนรอยต่อโหดพิเศษอย่างแผ่น Smartboard ผิวลื่นหรืองานใต้น้ำถึงจะเป็นคิวของ DeepStick ไม่แน่ใจว่าหน้างานตัวเองเข้าเคสไหน ส่งรูปมาถามในแชทได้เลย ทีมงานช่วยเลือกให้ฟรี"],
     "figs":[("why-coating-over-cracks-fails-04.webp","เลือกตัวโป๊วให้ตรงหน้างาน: พื้น-ดาดฟ้า PatchPro / ผนังปูน FillerAce / หลังคาเมทัลชีท SpackleFlex / รอยต่อโหดพิเศษ DeepStick")]},
   ],
   "prods":[("PatchPro","/patchpro"),("FillerAce","/fillerace"),
            ("SpackleFlex","/spackleflex"),("DeepStick","/deepstick")],
  },
  "en": {
   "title": "Coating Over Cracks Without Filling First — Why It Never Holds",
   "desc": "In our experience, waterproofing applied straight over cracks ends the same way almost every time: a repeat leak along the exact same line. Here's the mechanics of why, and how to finish the job in one pass.",
   "cat_label": "Joints / Cracks",
   "hero": ("why-coating-over-cracks-fails-00.webp", "Cracks this size — anyone can tell they need filling first. The real point: cracks many times smaller need exactly the same treatment, and that's where most jobs go wrong."),
   "intro": [
    "Here's a question we get all the time: \u201cThe floor or wall has a small crack — can I just coat over it? The spec says high elongation.\u201d Our answer, from direct job-site experience: absolutely not recommended. This kind of job never ends. Nearly every customer who skips the filling step comes back to us with the same symptom — leaking along the exact same crack line.",
    "This case walks through the mechanics of why a waterproofing film always loses to an unfilled crack, and the correct sequence that gets the job done in one pass instead of a recoat every six months.",
   ],
   "steps": [
    {"h":"A crack isn't a surface blemish — it's where the structure moves",
     "text":["Concrete and render expand when hot and shrink when cool, every single day. A crack is the spot the structure has already chosen to release all of that movement. It can look perfectly still to the naked eye while it's actually opening and closing by fractions of a millimeter around the clock — sun-baked by day, cooling at night, three-hundred-plus cycles a year. A film simply draped across that line has to absorb all of it in one place."],
     "figs":[("why-coating-over-cracks-fails-01en.webp","Day one looks fine, but the film only bridges the crack — it never filled the void. Once the structure moves, all the stretch concentrates on one line and the film tears along it.")]},
    {"h":"Why even a \u201chigh-elongation\u201d film still tears — the numbers tell on it",
     "text":["That several-hundred-percent elongation figure on the label is measured by pulling a whole free film, once. On site, the film is bonded tight to the concrete on both sides of the crack, so the only part that can actually stretch is the crack width itself. Say the crack is 0.5 mm wide and opens another 0.5 mm — the film on that line is instantly at 100% strain. Now repeat that pull-and-release every day instead of once like the test. Every material fatigues and eventually tears, and it tears exactly along the original crack. That's why people watch the old line slowly ghost back through their waterproofing within months."],
     "figs":[]},
    {"h":"And it doesn't end there — water travels under the film and surfaces somewhere else",
     "text":["Once the film tears, or water finds a way in from anywhere at all, it travels through voids in the concrete and gaps under the film — easily meters away. The spot where you see a drip or a water-filled blister usually isn't where the crack is. That's why recoating the drip spot never works: the real crack is somewhere else entirely. If this sounds like your job, go find the real leak point first — our putty-dam ponding technique is covered in the case <a href=\"/en/post/finding-the-real-leak-point\">Find the Real Leak Point First, Then Waterproof</a>."],
     "figs":[("why-coating-over-cracks-fails-03en.webp","Water enters at one crack, travels through voids in the slab, and surfaces as a drip meters away — which is why coating the drip spot never fixes anything")]},
    {"h":"From real jobs: the \u201cnever-ending\u201d loop",
     "text":["The sequence we see so often we can predict the ending: coat straight over the crack to save time, the first month looks great, then the first heatwave or heavy rain passes and the old line starts ghosting through — then the same leak returns, and it's off to buy more product for another round while the root cause sits there untouched. This loop runs forever. By the second round, materials plus labor have already overtaken the cost of filling. Filling adds one day of work — and cuts the entire loop."],
     "figs":[("why-coating-over-cracks-fails-02en.webp","Side by side: coat straight over and you pay for materials and labor on a loop — fill first and one extra day ends it permanently")]},
    {"h":"The correct sequence: fill it properly first, then coat",
     "text":["One: open up the crack first — hairline cracks especially must be ground open wide enough for the filler to go in full-depth, not just capping the mouth. Two: fill the groove completely and trowel it flush with the original surface. Three: let it fully set per the filler's manual, and only then apply your waterproofing system as the final step.",
             "As for which filler: match it to the surface. Floors and concrete decks take PatchPro. Cement and concrete walls take FillerAce. Metal-sheet roofs take SpackleFlex. And the truly brutal joints — slick surfaces like Smartboard, underwater work — that's when DeepStick comes off the bench. Not sure which case your job falls into? Send us photos in chat and the team will pick for you, free."],
     "figs":[("why-coating-over-cracks-fails-04en.webp","Match the filler to the surface: floors and decks PatchPro / cement walls FillerAce / metal-sheet roofs SpackleFlex / brutal joints DeepStick")]},
   ],
   "prods":[("PatchPro","/en/patchpro"),("FillerAce","/en/fillerace"),
            ("SpackleFlex","/en/spackleflex"),("DeepStick","/en/deepstick")],
  },
 },
 {
  "slug": "pool-leak-level-test",
  "cat": "pool tips",
  "date_th": "ส.ค. 2026", "date_en": "Aug 2026",
  "thumb": "pool-leak-level-test-01.webp",
  "th": {
   "title": "สระรั่วอย่าเพิ่งรื้อ — หยุดเติมน้ำ แล้วให้น้ำบอกจุดรั่วเอง",
   "desc": "สระว่ายน้ำรั่วไม่ต้องรีบจ้างทีมหาจุดรั่วหรือรื้อกระเบื้องทั้งสระ — หยุดเติมน้ำ ปล่อยให้ระดับลด น้ำหยุดนิ่งระดับไหน จุดรั่วอยู่ระดับนั้น พร้อมวิธีอ่านผลทีละระดับและอินโฟกราฟิกสรุป",
   "cat_label": "สระว่ายน้ำ · เทคนิค / ความรู้",
   "intro": [
    "สระรั่วทีไร คนส่วนใหญ่ควักเงินก้อนโตทันที — ไม่จ้างทีมหาจุดรั่วพร้อมเครื่องมือเต็มรถ ก็ใจร้อนถึงขั้นรื้อกระเบื้องทำใหม่ทั้งสระ ทั้งที่ความจริงสระทุกสระมีวิธีบอกจุดรั่วของตัวเองอยู่แล้ว และวิธีนั้นฟรี",
    "หลักการมีบรรทัดเดียว: หยุดเติมน้ำ แล้วปล่อยให้ระดับน้ำลดลงเอง น้ำจะลดไปเรื่อยๆ จนถึงระดับของรูรั่ว แล้วหยุดนิ่งอยู่ตรงนั้น — เพราะน้ำที่อยู่ต่ำกว่ารูรั่วไม่มีแรงดันดันมันออกไปไหนได้อีก ระดับที่น้ำหยุดนิ่งจึงเท่ากับระดับของจุดรั่วพอดี เหลือแค่ไล่ตรวจตามแนวนั้นแนวเดียว ไม่ต้องเดาสุ่มทั้งสระ",
   ],
   "steps": [
    {"h":"เช็คก่อนว่ารั่วจริง ไม่ใช่แค่น้ำระเหย (Bucket Test)",
     "text":["หน้าร้อนแดดจัดๆ น้ำสระระเหยได้เป็นเซนต่อวันโดยไม่ต้องรั่วสักรู อย่าเพิ่งตกใจ ทดสอบง่ายๆ ก่อน: เอาถังใส่น้ำวางบนขั้นบันไดสระให้ปากถังโผล่พ้นน้ำ เติมน้ำในถังให้ระดับใกล้เคียงกับระดับน้ำสระ ขีดมาร์คระดับทั้งในถังและขอบสระ ปิดปั๊มแล้วทิ้งไว้ 24 ชั่วโมง — ถ้าน้ำลดลงพอๆ กันทั้งคู่ นั่นคือการระเหยธรรมดา ไม่ต้องซ่อมอะไร แต่ถ้าน้ำสระลดมากกว่าน้ำในถังชัดเจน อันนี้รั่วจริง ไปขั้นถัดไปได้เลย"],
     "figs":[]},
    {"h":"หยุดเติมน้ำ ปิดระบบ แล้วปล่อยให้ระดับลดเอง",
     "text":["ตัดใจหยุดเติมน้ำ ปิดปั๊มและระบบกรองทั้งหมด งดใช้สระชั่วคราว แล้วปล่อยให้ธรรมชาติทำงาน จดระดับน้ำวันละครั้งเวลาเดิม ช่วงแรกระดับจะลดทุกวัน จนวันหนึ่งมันจะหยุดนิ่ง — นั่นแหละคือคำตอบที่รอ",
      "ข้อควรระวังข้อเดียวของวิธีนี้: ถ้าเป็นสระคอนกรีตฝังดินในพื้นที่น้ำใต้ดินสูงหรือช่วงหน้าฝน อย่าปล่อยน้ำลดจนสระแห้งสนิทเด็ดขาด เพราะน้ำใต้ดินรอบสระอาจดันโครงสระให้ลอยขึ้นทั้งตัวได้ ถ้าระดับลดลึกมากแล้วยังไม่หยุด ให้ถือว่าได้ข้อมูลพอแล้ว (จุดรั่วอยู่โซนก้นสระหรือแนวท่อล่าง) แล้วเติมน้ำกลับได้เลย"],
     "figs":[]},
    {"h":"อ่านผล: น้ำหยุดนิ่งระดับไหน จุดรั่วอยู่ระดับนั้น",
     "text":["เทียบระดับที่น้ำหยุดนิ่งกับอุปกรณ์บนผนังสระ แล้วอ่านผลตามนี้ — หยุดแถวปาก Skimmer แปลว่ารั่วที่ตัว Skimmer หรือแนวท่อระดับนั้น / หยุดตรงระดับหัวจ่ายน้ำ (Return) แปลว่าแนวท่อ Return / หยุดที่ระดับไฟใต้น้ำ แปลว่ารอบกล่องไฟหรือแนวเดินสาย / ลดลงจนเกือบแห้งก้นสระ แปลว่ารั่วที่พื้นสระหรือท่อสะดือสระ ยิ่งจุดรั่วอยู่ลึก งานยิ่งใหญ่ขึ้น — แต่อย่างน้อยตอนนี้รู้แล้วว่ากำลังสู้กับอะไร ไม่ได้สู้กับผี"],
     "figs":[("pool-leak-level-test-info-th.svg","อินโฟกราฟิกสรุปการอ่านผล: ระดับที่น้ำลดลงแล้วหยุดนิ่ง ชี้ตรงไปที่ระดับของจุดรั่ว — ไล่ตรวจแค่แนวนั้นแนวเดียว")]},
    {"h":"ยืนยันจุดด้วยสีย้อม แล้วซ่อมให้ตรงจุด",
     "text":["ได้แนวระดับแล้ว ไล่ตรวจตามแนวนั้นด้วยตา: รอยแตกร้าว ยาแนวหลุดร่อน ขอบรอบอุปกรณ์ทุกชิ้น เจอจุดสงสัยให้ยืนยันด้วยสีผสมอาหาร — รอให้น้ำนิ่งสนิท หยดสีใกล้ๆ จุดสงสัย ถ้าสีถูกดูดวิ่งเข้ารอยนั้น ยินดีด้วย เจอตัวการแล้ว",
      "รอยแตก รอยต่อ หรือขอบอุปกรณ์ที่ยืนยันแล้ว โป๊วปิดด้วย DeepStick ได้เลย — ตัวนี้ทำงานใต้น้ำได้ แปลว่าไม่ต้องสูบน้ำทิ้งทั้งสระเพื่อซ่อมจุดเดียว ประหยัดทั้งค่าน้ำและเวลา ส่วนสระที่ผิวโดยรวมหมดสภาพจนถึงเวลาทำใหม่ทั้งใบ ค่อยขยับไปคุยเรื่องทาเคลือบใหม่ด้วย PoolArmour — แต่นั่นคือการตัดสินใจหลังจากรู้ความจริงแล้ว ไม่ใช่การเดาเพราะหาจุดรั่วไม่เจอ"],
     "figs":[]},
   ],
   "prods":[("DeepStick","/deepstick"),("PoolArmour","/poolarmour")],
  },
  "en": {
   "title": "Pool Leaking? Don't Demolish Anything Yet — Stop Filling and Let the Water Talk",
   "desc": "A leaking pool doesn't mean hiring a leak-detection crew or re-tiling the whole thing. Stop topping up, let the level drop, and wherever the water stands still — that's the level of your leak. Full reading guide with an infographic.",
   "cat_label": "Pool · Tips / Know-how",
   "intro": [
    "The moment a pool starts leaking, most owners reach for their wallet — either a leak-detection crew with a truck full of equipment, or worse, ripping out every tile to rebuild the whole shell. Meanwhile every pool already knows how to point out its own leak, and that method costs nothing.",
    "The whole principle fits in one line: stop topping up the water and let the level fall on its own. It will keep dropping until it reaches the level of the hole, then stand perfectly still — because water sitting below the hole has no pressure left to push it out. The standstill level equals the leak level. Now you inspect one band of the pool instead of guessing across all of it.",
   ],
   "steps": [
    {"h":"First, confirm it's a leak and not just evaporation (the Bucket Test)",
     "text":["On a hot sunny week a pool can lose a centimeter a day to evaporation alone, no hole required. So test before you panic: place a bucket of water on a pool step with its rim above the surface, fill it to roughly match the pool's water level, mark both levels, switch off the pump, and wait 24 hours. If both drop about the same, that's plain evaporation — nothing to fix. If the pool drops clearly more than the bucket, you have a real leak. Move on."],
     "figs":[]},
    {"h":"Stop filling, switch everything off, and let the level fall",
     "text":["Commit to it: no topping up, pump and filtration off, no swimming for now. Let nature run the test. Note the water level once a day at the same time. It will drop day after day — until one day it stops. That standstill is the answer you've been waiting for.",
      "One caution with this method: for an in-ground concrete pool in an area with a high water table, or during the rainy season, never let it drain completely dry. Groundwater around the shell can lift the entire structure out of the ground. If the level has fallen very deep and still hasn't stopped, treat that as your answer (the leak is in the floor zone or the lower plumbing), and refill."],
     "figs":[]},
    {"h":"Read the result: where the water stands still is where the leak lives",
     "text":["Compare the standstill level against the fittings on your pool wall. Stops near the skimmer mouth — the leak is at the skimmer or the piping at that level. Stops at the return jet — the return line. Stops at the underwater light — around the light niche or its conduit. Drops to near empty — the floor or the main-drain line. The deeper the leak, the bigger the job — but at least now you know exactly what you're fighting, instead of fighting a ghost."],
     "figs":[("pool-leak-level-test-info-en.svg","Reading the result: the level where the water drops and then stands still points straight at the level of the leak — inspect that one band only")]},
    {"h":"Confirm the spot with dye, then fix that spot specifically",
     "text":["With the band identified, inspect along it: cracks, failed grout lines, the edge of every fitting. Found a suspect? Confirm it with food coloring — wait until the water is dead calm, drop a little dye next to the spot, and if the color gets pulled into the crack, congratulations, you've caught the culprit.",
      "Confirmed cracks, joints, and fitting edges can be sealed with DeepStick — it works underwater, which means you don't drain a whole pool to fix one spot. That saves the water bill and the downtime. And if the overall surface is genuinely at the end of its life, that's when you talk about recoating the shell with PoolArmour — a decision made after knowing the truth, not a guess made because nobody could find the leak."],
     "figs":[]},
   ],
   "prods":[("DeepStick","/en/deepstick"),("PoolArmour","/en/poolarmour")],
  },
 },
 {
  "slug": "finding-the-real-leak-point",
  "cat": "tips",
  "date_th": "ก.ค. 2026", "date_en": "Jul 2026",
  "thumb": "finding-the-real-leak-point-02.webp",
  "th": {
   "title": "หาจุดรั่วให้เจอก่อน แล้วค่อยทากันซึม",
   "desc": "ทากันซึมรอบสองรอบสามแล้วน้ำก็ยังซึมอยู่ดี ปัญหาไม่ได้อยู่ที่สินค้า อยู่ที่ไม่เคยหาจุดรั่วจริงเจอก่อนทา — เทคนิคกั้นดินน้ำมันแบ่งโซนขังน้ำหาจุดรั่ว",
   "cat_label": "เทคนิค / ความรู้",
   "intro": [
    "ทากันซึมไปแล้วรอบสองรอบสาม น้ำก็ยังซึมเข้ามาอยู่ดี หลายคนโทษว่าสินค้าไม่ดี แต่ปัญหาจริงๆ ส่วนใหญ่ไม่ได้อยู่ที่เนื้อสี — อยู่ที่ยังไม่เคยหาจุดรั่วตัวจริงเจอเลย แล้วไปทาสุ่มทั้งพื้นที่",
    "วิธีที่ได้ผลจริงคือแบ่งพื้นที่สงสัยเป็นโซนย่อยด้วยดินน้ำมัน ขังน้ำทดสอบทีละโซน แล้วดูว่าโซนไหนซึมทะลุจริง เมื่อเจอจุดจริงแล้วค่อยเลือกวิธีซ่อมให้ตรงจุด งานจะจบในรอบเดียว ไม่ต้องเสียเวลาทาซ้ำไปเรื่อยๆ",
   ],
   "steps": [
    {"h":"กั้นโซนด้วยดินน้ำมันแล้วขังน้ำทีละโซน",
     "text":["ใช้ดินน้ำมันกั้นเป็นแนวแบ่งพื้นที่สงสัยออกเป็นโซนย่อย ต้องกั้นให้แนบสนิทไม่ให้น้ำไหลข้ามโซนกัน จากนั้นเติมน้ำขังไว้ในโซนแรกก่อน ปล่อยทิ้งไว้สังเกต แล้วไล่ทำทีละโซนจนครบทุกโซนที่สงสัย วิธีนี้ช่วยแยกตัวแปรออกทีละส่วน ไม่ต้องเดาสุ่มทั้งพื้นที่"],
     "figs":[("finding-the-real-leak-point-02.webp","แบ่งพื้นที่สงสัยเป็นโซนด้วยดินน้ำมัน ขังน้ำทดสอบทีละโซนเพื่อหาว่าโซนไหนซึมจริง"),
             ("finding-the-real-leak-point-04.webp","ลำดับขั้นตอนทั้งหมด: กั้นโซน ขังน้ำ สังเกตจุดรั่ว แล้วค่อยทากันซึมตรงจุด")]},
    {"h":"จุดที่พบรั่วบ่อยที่สุด: มุมที่ผนังชนพื้น",
     "text":["จากการทดสอบหลายๆ งาน จุดที่รั่วบ่อยที่สุดคือรอยต่อระหว่างผนังกับพื้น เพราะเป็นจุดที่วัสดุสองชนิดต่างกันมาเจอกัน ขยับตัวไม่เท่ากันเวลาอุณหภูมิเปลี่ยน รอยต่อจึงแตกก่อนจุดอื่นเสมอ แม้ผิวด้านบนจะมองดูเรียบร้อยดีก็ตาม น้ำก็ยังซึมลอดตามรอยแตกที่ซ่อนอยู่ได้"],
     "figs":[("finding-the-real-leak-point-03.webp","ภาพตัดขวางจุดต่อผนัง-พื้น แสดงรอยแตกจากการขยับตัวต่างกัน จุดที่น้ำซึมลอดเข้าไปได้แม้ผิวบนดูเรียบร้อย")]},
    {"h":"หลักฐานจากหน้างานจริง",
     "text":["ภาพนี้คือดินน้ำมันที่ใช้กั้นแบ่งโซนตามแนวร่องยืดตัวของพื้นกระเบื้อง หลังแกะออกจากการทดสอบขังน้ำแต่ละโซน เพื่อยืนยันให้แน่ใจก่อนว่าจุดรั่วอยู่ตรงไหนจริงๆ ก่อนตัดสินใจซ่อม"],
     "figs":[("finding-the-real-leak-point-01.webp","ดินน้ำมันที่ใช้กั้นแบ่งโซนตามร่องยืดตัว หลังแกะออกจากการทดสอบขังน้ำหาจุดรั่วจริง")]},
    {"h":"เจอจุดจริงแล้วค่อยเลือกวิธีซ่อมให้ตรงจุด",
     "text":["พอยืนยันจุดรั่วจริงแล้ว ถ้าเป็นรอยต่อหรือรอยแตกที่ต้องโป๊วก่อน จะใช้ PatchPro หรือ DeepStick ก็ได้ แล้วแต่ลักษณะรอยต่อหน้างานจริง ปล่อยให้เซ็ตตัวเต็มที่ก่อน แล้วค่อยเคลือบทับด้วยกันซึมที่เหมาะกับหน้างานนั้นๆ อีกชั้น ถ้าไม่แน่ใจว่าหน้างานแบบนี้ควรใช้ตัวไหน ทักแชทให้ทีมงานช่วยเลือกให้ตรงกับหน้างานได้ หลักการคือหาให้เจอก่อนทา ไม่ใช่ทาสุ่มทั้งพื้นที่แล้วหวังว่าจะหาย"],
     "figs":[]},
   ],
   "prods":[("PatchPro","/patchpro"),("DeepStick","/deepstick")],
  },
  "en": {
   "title": "Find the Real Leak Point First, Then Waterproof",
   "desc": "Coated it twice, three times, and it still leaks? The product usually isn't the problem — nobody ever found the real leak point before coating. Here's the putty-dam water test technique.",
   "cat_label": "Tips / Know-how",
   "intro": [
    "Coated it a second time, a third time, and water still gets in. Most people blame the product, but the real problem is usually that nobody ever found the actual leak point — they just coated the whole area and hoped.",
    "The method that actually works: section off the suspect area with plumber's putty, pond water in each zone one at a time, and see which zone actually leaks through. Once you find the real spot, you fix that spot — the job gets done in one pass instead of endless recoating.",
   ],
   "steps": [
    {"h":"Dam off zones with putty, then pond water one zone at a time",
     "text":["Use plumber's putty to build dams across the suspect area, dividing it into smaller zones. The seal has to be tight so water can't cross between zones. Fill the first zone with water and leave it to observe, then work through each zone in turn. This isolates one variable at a time instead of guessing across the whole area."],
     "figs":[("finding-the-real-leak-point-02.webp","Putty dams divide the suspect floor into zones, each ponded separately to find which zone actually leaks"),
             ("finding-the-real-leak-point-04.webp","The full sequence: dam the zones, pond the water, watch for the leak, then coat exactly where it is")]},
    {"h":"The most common leak point: where the wall meets the floor",
     "text":["Across many jobs, the wall-to-floor joint is the spot that leaks most often. It's where two different materials meet, and they expand and contract at different rates as temperature changes — so that joint cracks before anywhere else does. The surface on top can look perfectly fine while water is still seeping through the hidden crack underneath."],
     "figs":[("finding-the-real-leak-point-03.webp","Cross-section of a wall-floor joint showing the crack caused by differential movement — where water seeps through even when the top surface looks fine")]},
    {"h":"Evidence from an actual job",
     "text":["This is the putty used to dam off zones along the floor's expansion joint, pulled off after the ponding test on each section — confirming exactly where the leak was before deciding how to fix it."],
     "figs":[("finding-the-real-leak-point-01.webp","Putty dams along the expansion joint, removed after the water-ponding test confirmed the real leak point")]},
    {"h":"Found the real spot? Now fix that spot specifically",
     "text":["Once the leak point is confirmed, fill the joint or crack with either PatchPro or DeepStick, depending on what that particular joint needs. Let it fully set, then coat over it with whichever waterproofing product actually fits that job site. Not sure which one fits your case? Message the team and we'll help you pick. The whole principle: find it before you coat it — don't coat the whole area and hope."],
     "figs":[]},
   ],
   "prods":[("PatchPro","/en/patchpro"),("DeepStick","/en/deepstick")],
  },
 },
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
 {
  "slug": "mixing-ratio-matters",
  "cat": "tips coat",
  "date_th": "ก.ค. 2026", "date_en": "Jul 2026",
  "thumb": "mixing-ratio-matters-01.webp",
  "th": {
   "title": "ทำไมทาสีแล้วชอบไม่แห้ง",
   "desc": "นี่คือคำถามที่เราพบบ่อยมากสำหรับสีแบบสองส่วนผสม — ชั่งด้วยเครื่องชั่ง ปั่นด้วยสว่านถ้าปริมาณเยอะ กวาดข้างถัง ตวงด้วยถ้วยถ้าไม่มีเครื่องชั่ง และคนด้วยมือให้ทั่วอย่างน้อย 1 นาที",
   "cat_label": "เทคนิค / ความรู้",
   "intro": [
    "นี่คือคำถามที่เราพบบ่อยมากสำหรับการใช้งานสีแบบสองส่วนผสม",
    "อยากให้ชมวิธีให้เข้าใจก่อนใช้งานนะครับ",
   ],
   "steps": [
    {"h":"ชั่งด้วยเครื่องชั่งดิจิทัลให้ตรงตามอัตราส่วน",
     "text":["อัตราส่วนที่แน่นอนต่างกันไปในแต่ละสูตร (ตัวอย่างในภาพคือ Marine Guard ผสม A 2 ส่วน : B 1 ส่วน โดยน้ำหนัก) แต่หลักการเดียวกันคือห้ามกะด้วยสายตาเด็ดขาด วางภาชนะบนเครื่องชั่งดิจิทัล ชั่ง Part A ก่อน แล้วค่อยเติม Part B ตามอัตราส่วนที่คู่มือของรุ่นนั้นกำหนด"],
     "figs":[("mixing-ratio-matters-01.webp","ชั่ง Part A และ Part B ด้วยเครื่องชั่งดิจิทัลก่อนผสมทุกครั้ง")]},
    {"h":"ผสมทีละมาก ใช้สว่านปั่นแทนคนด้วยมือ",
     "text":["ถ้าผสมทีเดียวปริมาณมาก ให้ใช้สว่านพร้อมหัวปั่นแทนการคนด้วยมือ ปั่นด้วยความเร็วต่ำ-กลางต่อเนื่องประมาณ 2-3 นาที จนเนื้อเข้ากันเป็นสีเดียวทั่วทั้งถัง คนด้วยมือเพียงอย่างเดียวมักปั่นไม่ทั่วถึงเมื่อปริมาณเยอะ"],
     "figs":[("mixing-ratio-matters-02.webp","ผสมปริมาณมากใช้สว่านพร้อมหัวปั่นแทนคนด้วยมือ ปั่นจนเนื้อเข้ากันทั่วถึง")]},
    {"h":"กวาดข้างถังและก้นถังทุกครั้งก่อนใช้งาน",
     "text":["จุดที่พลาดบ่อยที่สุดคือน้ำยาที่เกาะข้างถังหรือกองอยู่ก้นถังไม่โดนปั่นเข้าเนื้อ ส่วนนี้แหละที่มักไม่แห้งทั้งที่ภาพรวมดูเข้ากันดีแล้ว ใช้ไม้พายหรือเกรียงกวาดข้างถังและก้นถังลงมาปั่นซ้ำอีกรอบก่อนเทใช้งานทุกครั้ง"],
     "figs":[("mixing-ratio-matters-03.webp","กวาดน้ำยาที่เกาะข้างถังและก้นถังลงมาปั่นซ้ำ ก่อนเทใช้งาน")]},
    {"h":"ไม่มีเครื่องชั่ง ใช้ถ้วยตวงแทนได้ (ตามอัตราส่วนโดยปริมาตร)",
     "text":["ถ้าไม่มีเครื่องชั่งหน้างาน ใช้ถ้วยตวงที่มีขีดบอกปริมาตรแทนได้ แต่ต้องตวงให้ตรงตามอัตราส่วนที่คู่มือของรุ่นนั้นกำหนด (ตัวอย่างในภาพคือ 2:1 โดยปริมาตร) ห้ามกะเอาเองเด็ดขาด — ตวงผิดแม้เพียงเล็กน้อยก็ทำให้น้ำยาไม่แห้งได้เหมือนกัน"],
     "figs":[("mixing-ratio-matters-04.webp","ไม่มีเครื่องชั่ง ใช้ถ้วยตวงที่มีขีดบอกปริมาตรตวงตามอัตราส่วนแทนได้")]},
    {"h":"ผสมทีละน้อย คนด้วยมือให้ทั่วอย่างน้อย 1 นาที",
     "text":["ผสมปริมาณน้อยไม่จำเป็นต้องใช้สว่าน คนด้วยไม้พายหรือแท่งคนก็เพียงพอ แต่ต้องคนต่อเนื่องอย่างน้อย 1 นาทีจนเนื้อเข้ากันจริงๆ ทั้งสี เนื้อ และความหนืด ขั้นนี้สำคัญที่สุดในทุกขั้นตอน เพราะถ้าคนไม่เข้ากันดีพอ น้ำยาจะไม่แห้ง ไม่ว่าจะชั่งอัตราส่วนแม่นแค่ไหนก็ตาม",
              "ตัวอย่างจาก Marine Guard: ผสมแล้วต้องทาให้หมดภายใน 15 นาที (pot life) และถ้าน้ำยาหนืดเกินไปเจือทินเนอร์เพิ่มได้ไม่เกิน 10% — ตัวเลขที่แน่นอนของแต่ละสูตรให้ยึดตามหน้าเว็บหรือคู่มือของสินค้านั้นๆ เป็นหลัก เพราะแต่ละสูตรไม่เหมือนกัน"],
     "figs":[("mixing-ratio-matters-05.webp","ผสมปริมาณน้อยคนด้วยมือให้ทั่วต่อเนื่องอย่างน้อย 1 นาที ขั้นตอนที่สำคัญที่สุด")]},
   ],
   "prods":[("Marine Guard","/marineguard")],
  },
  "en": {
   "title": "Why Two-Part Coatings Sometimes Never Dry",
   "desc": "This is one of the most common questions we get about two-part coatings — weigh it, drill-mix large batches, scrape the sides, use measuring cups if you have no scale, and hand-mix small batches for at least a minute.",
   "cat_label": "Tips / Know-how",
   "intro": [
    "This is one of the most common questions we get about using two-part coatings.",
    "Here is the mixing procedure explained step by step — watch it before you start the job.",
   ],
   "steps": [
    {"h":"Weigh it out on a digital scale to hit the exact ratio",
     "text":["The exact ratio varies by product (the example shown is Marine Guard, mixed 2 parts A : 1 part B by weight) — but the rule is always the same: never eyeball it. Set the container on a digital scale, weigh out Part A first, then add Part B to hit the ratio in that product's manual."],
     "figs":[("mixing-ratio-matters-01.webp","Weigh Part A and Part B on a digital scale before every mix")]},
    {"h":"Large batch? Use a drill mixer, not your arm",
     "text":["For a large batch, mix with a drill and paddle attachment instead of stirring by hand. Run it at low-to-medium speed for about 2-3 minutes until the color and texture are completely uniform throughout the container. Hand-stirring alone rarely reaches every part of a big batch."],
     "figs":[("mixing-ratio-matters-02.webp","Large batches get a drill and paddle attachment instead of hand-stirring, mixed until fully uniform")]},
    {"h":"Scrape the sides and bottom every single time",
     "text":["The most common mistake: material clinging to the sides or settled at the bottom never gets folded into the mix. That unmixed pocket is usually exactly where it stays wet, even when the rest looks perfectly blended. Use a spatula or scraper to pull everything off the sides and bottom back into the mix before you pour."],
     "figs":[("mixing-ratio-matters-03.webp","Scrape material clinging to the sides and bottom back into the mix before pouring")]},
    {"h":"No scale? Measuring cups work too (by volume ratio)",
     "text":["If there's no scale on site, graduated measuring cups work as a substitute — but you still have to hit the exact ratio in the manual (the example shown is 2:1 by volume). Never estimate by eye. Even a small error in the volume can leave the coating from drying properly."],
     "figs":[("mixing-ratio-matters-04.webp","No scale on site? Graduated measuring cups can hit the same ratio by volume")]},
    {"h":"Small batch: hand-mix thoroughly for at least a minute",
     "text":["Small batches don't need a drill — a stir stick or spatula is enough. But keep stirring continuously for at least a full minute until the color, texture, and consistency are genuinely uniform. This is the single most important step in the whole process: mix it poorly and it won't dry, no matter how precisely you weighed the ratio.",
              "Marine Guard, as an example: once mixed, you have a 15-minute pot life to use it up, and if it's too thick you can add up to 10% thinner. The exact numbers vary by product — always check that product's own page or manual, since every formula is different."],
     "figs":[("mixing-ratio-matters-05.webp","Small batches get hand-mixed continuously for at least a minute — the single most important step")]},
   ],
   "prods":[("Marine Guard","/en/marineguard")],
  },
 },
 {
  "slug": "waterproofing-coverage-tips",
  "cat": "tips coat",
  "date_th": "ก.ค. 2026", "date_en": "Jul 2026",
  "thumb": "waterproofing-coverage-tips-04.webp",
  "th": {
   "title": "วิธีทากันซึมให้ประหยัด",
   "desc": "ซื้อกันซึมมาถังเดียวแต่ทาไม่ทั่วพื้นที่ตามป้าย ปัญหาไม่ได้อยู่ที่เนื้อสี แต่อยู่ที่เทคนิค — เตรียมผิว ผสมให้ถูก ทาชั้นแรกให้บาง แล้วค่อยเก็บชั้นที่สอง",
   "cat_label": "เทคนิค / ความรู้",
   "intro": [
    "หลายคนซื้อกันซึมมาถังเดียว คำนวณจากป้ายว่าครอบคลุมกี่ตารางเมตร แต่ทาไปได้ไม่ถึงครึ่งพื้นที่สีก็หมดถังซะแล้ว หลายคนโทษว่าสีคุณภาพไม่ตรงป้าย ทั้งที่จริงๆ แล้วสาเหตุเกือบทั้งหมดมาจากเทคนิคการทา ไม่ใช่ตัวเนื้อสี",
    "จุดที่กินสีเยอะที่สุดคือรอบแรกบนพื้นผิวที่ยังไม่ผ่านการเตรียมให้ดี พื้นผิวแบบนี้ดูดสีไม่เท่ากันเป็นหย่อมๆ แทนที่จะกระจายเป็นฟิล์มบางสม่ำเสมอ กลายเป็นเสียสีไปกับจุดที่ดูดมากเกินจำเป็น แก้ตรงเทคนิคจุดนี้ ถังเดียวก็ทาได้พื้นที่มากขึ้นชัดเจน",
   ],
   "steps": [
    {"h":"เตรียมพื้นผิวให้สะอาด",
     "text":["ฝุ่น คราบมัน หรือเศษปูนที่หลุดร่อนคือตัวการที่ทำให้พื้นผิวดูดสีไม่สม่ำเสมอ จุดไหนมีฝุ่นเกาะ สีจะซึมลงไปเคลือบฝุ่นแทนที่จะยึดกับเนื้อปูนจริง เสียสีไปฟรีๆ และยังหลุดร่อนตามฝุ่นได้ง่ายในภายหลัง ถ้ามีเครื่องขัดผิวคอนกรีตให้ใช้เครื่องขัดจะดีที่สุด ถ้าไม่มีก็ล้างทำความสะอาดฝุ่นและคราบสกปรกออกให้ทั่วตามปกติ แล้วปล่อยให้แห้งสนิทก่อนเริ่มขั้นถัดไป — ยิ่งพื้นผิวสะอาดเท่าไหร่ สีก็ยิ่งได้พื้นที่คุ้มค่าและยึดเกาะได้ทนขึ้นเท่านั้น"],
     "figs":[("waterproofing-coverage-tips-01.webp","พลาดขั้นตอนเตรียมพื้นผิวไป พื้นที่ที่ทาได้จริงจะน้อยกว่าที่คำนวณไว้จากป้ายเยอะ"),
             ("waterproofing-coverage-tips-02.webp","มีเครื่องขัดผิวใช้เครื่องขัดจะดีที่สุด ถ้าไม่มีก็ล้างทำความสะอาดตามปกติให้ทั่วทั้งพื้นที่")]},
    {"h":"ผสมสีให้เข้ากันตามคู่มือ",
     "text":["ถ้าเป็นกันซึมชนิดสองส่วนผสม ต้องตวงอัตราส่วนตามคู่มือของรุ่นนั้นให้ตรงเป๊ะแล้วกวนให้เข้ากันจริงถึงก้นถัง (ตัวอย่างจากกันซึม Polyurea Standard ของเรา: ผสม Part A : Part B ที่ 2:1 โดยน้ำหนัก กวนอย่างน้อย 1 นาทีเต็ม แล้วใช้ให้หมดภายในเวลาที่คู่มือกำหนด ราว 10 นาที) ถ้าเป็นชนิดส่วนผสมเดียวเปิดถังแล้วใช้งานได้เลย ไม่ต้องผสมอะไรเพิ่ม ผสมอัตราส่วนผิดไม่ใช่แค่เสี่ยงสีไม่แห้ง แต่เท่ากับเสียสีทั้งถังที่ผสมไปฟรีๆ — ผสมผิดครั้งเดียวแพงกว่าเสียเวลาตวงใหม่เยอะ"],
     "figs":[("waterproofing-coverage-tips-03.webp","ถ้าเป็นสีหรือกันซึมแบบสองส่วนผสมต้องตวงและกวนให้เข้ากันตามคู่มือก่อนใช้งานทุกครั้ง")]},
    {"h":"ทาชั้นแรกให้บางที่สุด",
     "text":["ลืมวิธีทาสีแบบเดิมที่รีดให้หนาตั้งแต่รอบแรกไปก่อน ชั้นแรกต้องทาด้วยลูกกลิ้งโฟมรีดแรงๆ ให้ฟิล์มบางที่สุดเท่าที่จะทำได้ หน้าที่ของรอบนี้ไม่ใช่ความสวยงาม แต่คือการกันไม่ให้พื้นผิวที่ยังดิบดูดสีรอบต่อไปมากเกินจำเป็น — ทารอบแรกหนาเท่าไหร่ พื้นก็ยิ่งดูดสีทิ้งไปเท่านั้นโดยไม่ได้ความหนาฟิล์มเพิ่มขึ้นจริง ทาย้ำๆ อยู่ที่เดิมเพื่อให้ดูสวยตั้งแต่รอบแรก คือสาเหตุอันดับหนึ่งที่ทำให้สีหมดถังเร็วกว่าที่ควร (ตัวอย่างจากกันซึม Polyurea Standard: เว้นระยะจากรอบแรกประมาณ 2 ชั่วโมงก่อนทารอบถัดไป ตัวเลขจริงให้ยึดตามคู่มือของรุ่นที่ใช้)"],
     "figs":[("waterproofing-coverage-tips-04.webp","ทาชั้นแรกด้วยลูกกลิ้งโฟมรีดแรงๆ ให้บางที่สุด กันไม่ให้พื้นผิวดูดสีรอบต่อไปมากเกินไป")]},
    {"h":"ทาชั้นที่สองให้สวยงาม",
     "text":["พอถึงรอบสุดท้ายค่อยเก็บงานให้สวยงามตามต้องการ เพราะพื้นผิวถูกซีลไปแล้วตั้งแต่รอบแรก รอบนี้สีจะกระจายเป็นฟิล์มสม่ำเสมอโดยไม่ถูกดูดหายไปกับพื้นผิวเหมือนรอบแรก ได้ทั้งพื้นที่คุ้มค่าและสีสม่ำเสมอทั่วทั้งผืน ยิ่งทาหลายชั้นภายในจำนวนที่คู่มือแนะนำ ก็ยิ่งได้ความหนาฟิล์มที่ทนทานขึ้นตามไปด้วย ทารอบสุดท้ายเสร็จแล้วอย่าเพิ่งรีบใช้งานพื้นที่ ปล่อยให้ฟิล์มเซ็ตตัวตามเวลาที่คู่มือกำหนดก่อนเสมอ"],
     "figs":[("waterproofing-coverage-tips-05.webp","รอบสุดท้ายทาเก็บงานให้สวยงามได้ตามต้องการ ยิ่งทาหลายชั้นภายในจำนวนที่แนะนำ ยิ่งทน")]},
   ],
   "prods":[("กันซึม Polyurea Standard","/polyurea"),("กันซึม SiliconePro","/siliconepro"),
            ("TileCoat Polyurea","/tilecoatpoly")],
  },
  "en": {
   "title": "How to Make Your Waterproofing Paint Go Further",
   "desc": "One bucket, half the coverage the label promised? The paint usually isn't the problem — the technique is. Prep the surface, mix it right, keep the first coat thin, then finish with the second.",
   "cat_label": "Tips / Know-how",
   "intro": [
    "Plenty of people buy one bucket of waterproofing coating, work out the coverage from the label, and still run out before finishing the area. Most blame the product for underperforming its rated coverage. In practice, the cause is almost always technique, not the coating itself.",
    "The coat that eats the most paint is the first one, applied to a surface that hasn't been properly prepped. An untreated surface drinks up coating unevenly in patches instead of spreading into a thin, uniform film — and that uneven absorption is where the paint actually disappears. Fix the technique and the same bucket covers noticeably more ground.",
   ],
   "steps": [
    {"h":"Clean the surface first",
     "text":["Dust, grease, or loose render is what makes a surface absorb paint unevenly. Wherever dust sits, the coating soaks into the dust instead of bonding with the real substrate underneath — that's paint wasted for nothing, and it flakes off along with the dust later. If you have access to a concrete grinder, use it; if not, wash the surface thoroughly the normal way and let it dry fully before the next step. The cleaner the surface, the more area you actually cover per bucket, and the longer the film holds."],
     "figs":[("waterproofing-coverage-tips-01.webp","Skip the surface prep and the area you actually cover ends up well short of what the label promised"),
             ("waterproofing-coverage-tips-02.webp","A grinder does the best job; without one, wash the surface thoroughly across the whole area instead")]},
    {"h":"Mix it exactly to the manual",
     "text":["For two-component coatings, measure the ratio in that product's manual precisely and mix until it's genuinely uniform right down to the bottom of the bucket (our Polyurea Standard, as an example: Part A to Part B at 2:1 by weight, mixed for a full minute, used within the pot life stated in the manual — about 10 minutes). Single-component coatings need no mixing at all — just open and apply. Getting the ratio wrong doesn't just risk a coat that never cures — it wastes the entire mixed batch. One bad mix costs more than the couple of extra minutes it takes to measure properly."],
     "figs":[("waterproofing-coverage-tips-03.webp","Two-component coatings must be measured and mixed to the manual before every application")]},
    {"h":"First coat: as thin as possible",
     "text":["Forget the old habit of laying it on thick from the first pass. The first coat needs a foam roller pressed hard, stretching the film as thin as it will go. This coat's job isn't to look finished — it's to stop the still-raw surface from soaking up the next coat more than it needs to. The thicker that first pass goes on, the more of it the surface simply drinks away without adding any real film thickness. Trying to make it look good on the first pass is the number one reason a bucket empties faster than it should (our Polyurea Standard, as an example: wait about 2 hours after the first coat before the next — check your product's manual for the exact figure)."],
     "figs":[("waterproofing-coverage-tips-04.webp","Roll the first coat hard and thin with a foam roller — this stops the surface from over-absorbing the next coat")]},
    {"h":"Second coat: finish it properly",
     "text":["By the final coat, the surface has already been sealed by the first pass, so go ahead and finish it to the look you want. This coat spreads as an even film instead of disappearing into the surface the way the first one did — you get both better coverage and a uniform finish across the whole area. Within the number of coats your product recommends, more coats simply means a thicker, more durable film. Once the last coat is down, don't rush back onto the surface — let the film cure for the time stated in the manual first."],
     "figs":[("waterproofing-coverage-tips-05.webp","The final coat gets finished to a clean, even look — more coats within the recommended count means a tougher film")]},
   ],
   "prods":[("Polyurea Standard Waterproofing","/en/polyurea"),("SiliconePro Waterproofing","/en/siliconepro"),
            ("TileCoat Polyurea","/en/tilecoatpoly")],
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
.step p a{{color:var(--signal);font-weight:600;text-decoration:underline;text-underline-offset:3px}}
.step figure{{margin-top:18px}}
figure.hero{{margin:22px 0 0}}
figure.hero img{{width:100%;border-radius:12px;border:1px solid var(--line);background:#E9E7E1}}
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
  /* ═══ MOBILE DRAWER MENU (ถอนได้: ลบ 3 บล็อกที่มี marker นี้: CSS/HTML/JS) ═══ */
  .mnav-btn,.mnav,.mnav-scrim{{display:none}}
  @media(max-width:860px){{
    .theme-toggle,.lang-switch{{display:none}}
    .mnav-scrim{{display:block}}
    .cta-chat{{display:inline-flex;margin-left:auto}}
    .mnav-btn{{display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:8px;padding:6px 10px;font-size:17px;line-height:1;cursor:pointer}}
    .mnav-btn:hover{{border-color:var(--orange)}}
    .mnav-scrim{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:98;opacity:0;pointer-events:none;transition:opacity .22s ease}}
    .mnav-scrim.open{{opacity:1;pointer-events:auto}}
    .mnav{{position:fixed;top:0;bottom:0;left:0;width:min(280px,82vw);z-index:99;background:var(--panel);border-right:1px solid var(--line);padding:20px 22px 18px;display:flex;flex-direction:column;transform:translateX(-105%);transition:transform .26s ease;overflow-y:auto}}
    .mnav.open{{transform:translateX(0)}}
    .mnav-head{{display:flex;align-items:center;justify-content:space-between}}
    .mnav-brand{{font-family:var(--disp);font-weight:700;font-size:16px;letter-spacing:.04em;color:var(--ink)}}
    .mnav-brand em{{color:var(--orange);font-style:normal}}
    .mnav-close{{background:none;border:none;color:var(--muted);font-size:19px;line-height:1;cursor:pointer;padding:4px}}
    .mnav-tag{{font-size:11.5px;color:var(--muted);margin-top:3px}}
    .mnav-k{{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;color:var(--orange);margin:22px 0 4px}}
    .mnav-links{{display:flex;flex-direction:column}}
    .mnav-links a{{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-bottom:1px solid var(--line);font-size:16.5px;color:var(--ink)}}
    .mnav-links a:last-child{{border-bottom:none}}
    .mnav-links a span{{color:var(--orange)}}
    .mnav-chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}}
    .mnav-chips a{{font-size:12.5px;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:6px 13px}}
    .mnav-util{{display:flex;align-items:center;gap:10px;padding:12px 0;border-top:1px solid var(--line);margin-top:auto}}
    .mnav-util .mnav-lang{{font-family:var(--mono);font-size:12px;letter-spacing:.08em;border:1px solid var(--line);border-radius:8px;padding:5px 12px;color:var(--muted)}}
    .mnav-util .mnav-theme{{background:none;border:1px solid var(--line);border-radius:8px;padding:4px 11px;font-size:14px;line-height:1.4;cursor:pointer;color:var(--ink)}}
    .mnav-chat{{background:#1877F2;border-radius:10px;text-align:center;padding:11px 0;font-size:14px;color:#fff;font-weight:600;margin-top:2px}}
  }}
  /* ═══ จบบล็อก CSS MOBILE DRAWER MENU ═══ */
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <button class="mnav-btn" id="mnavBtn" aria-label="เปิดเมนู" aria-expanded="false">☰</button>
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
    <a class="btn-chat" href="https://lin.ee/LpUR3Ld" style="background:#06C755"><span style="display:inline-grid;place-items:center;border-radius:5px;background:#fff;color:#06C755;font-weight:800;font-size:9px;font-family:Arial,sans-serif;line-height:1;padding:3px 4px;letter-spacing:.02em;margin-right:7px;vertical-align:1px">LINE</span>แอดไลน์</a>
  </div>
</header>

<!-- ═══ MOBILE DRAWER MENU: ลิ้นชัก (ถอนได้) ═══ -->
<div class="mnav-scrim" id="mnavScrim" aria-hidden="true"></div>
<aside class="mnav" id="mnav" aria-label="เมนูหลัก">
  <div class="mnav-head">
    <span class="mnav-brand"><img src="/img/logo.png" alt="" width="24" height="24" style="object-fit:contain;vertical-align:-6px;margin-right:8px">LUCERNA<em>PRO</em></span>
    <button class="mnav-close" id="mnavClose" aria-label="ปิดเมนู">✕</button>
  </div>
  <div class="mnav-tag" style="font-family:var(--mono);letter-spacing:.05em">Real deal or nothing</div>
  <div class="mnav-k">MENU</div>
  <nav class="mnav-links">
    <a href="/">หน้าแรก <span>→</span></a>
    <a href="/#finder">สินค้าทั้งหมด <span>→</span></a>
    <a href="/casestudy/">Case Study <span>→</span></a>
    <a href="/#contact">ติดต่อเรา <span>→</span></a>
  </nav>
  <div class="mnav-k">SHORTCUTS</div>
  <div class="mnav-chips">
    <a href="/#waterproof">กันซึม</a>
    <a href="/#flooring">งานพื้น</a>
    <a href="/#coating">เคลือบปกป้อง</a>
  </div>
  <div class="mnav-util">
    <button class="mnav-theme" id="mnavTheme" aria-label="สลับโหมดสี">🌙</button>
  </div>
  <a class="mnav-chat" href="https://m.me/lucernapro">f&nbsp; แชทเพจ — ตอบไว</a>
</aside>
<!-- ═══ จบลิ้นชัก MOBILE DRAWER MENU ═══ -->


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

<!-- ═══ MOBILE DRAWER MENU: JS (ถอนได้) ═══ -->
<script>
(function(){{
  var mn=document.getElementById('mnav'),sc=document.getElementById('mnavScrim'),
      bt=document.getElementById('mnavBtn'),cl=document.getElementById('mnavClose'),
      tb=document.getElementById('mnavTheme'),master=document.getElementById('themeToggle');
  if(!mn||!bt)return;
  function set(open){{
    mn.classList.toggle('open',open);sc.classList.toggle('open',open);
    bt.setAttribute('aria-expanded',open?'true':'false');
    document.body.style.overflow=open?'hidden':'';
  }}
  bt.addEventListener('click',function(){{set(true)}});
  cl.addEventListener('click',function(){{set(false)}});
  sc.addEventListener('click',function(){{set(false)}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')set(false)}});
  window.addEventListener('pageshow',function(){{set(false)}});
  mn.querySelectorAll('.mnav-links a,.mnav-chips a,.mnav-chat').forEach(function(a){{
    a.addEventListener('click',function(){{set(false)}});
  }});
  if(tb){{
    if(!master){{tb.style.display='none';}}
    else{{
      function syncT(){{tb.textContent=document.documentElement.dataset.theme==='dark'?'☀️':'🌙';}}
      tb.addEventListener('click',function(){{master.click();syncT();}});
      syncT();
    }}
  }}
}})();
</script>
<!-- ═══ จบ JS MOBILE DRAWER MENU ═══ -->
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
  /* ═══ MOBILE DRAWER MENU (removable: delete the 3 blocks carrying this marker: CSS/HTML/JS) ═══ */
  .mnav-btn,.mnav,.mnav-scrim{{display:none}}
  @media(max-width:860px){{
    .theme-toggle,.lang-switch{{display:none}}
    .mnav-scrim{{display:block}}
    .cta-chat{{display:inline-flex;margin-left:auto}}
    .mnav-btn{{display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:8px;padding:6px 10px;font-size:17px;line-height:1;cursor:pointer}}
    .mnav-btn:hover{{border-color:var(--orange)}}
    .mnav-scrim{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:98;opacity:0;pointer-events:none;transition:opacity .22s ease}}
    .mnav-scrim.open{{opacity:1;pointer-events:auto}}
    .mnav{{position:fixed;top:0;bottom:0;left:0;width:min(280px,82vw);z-index:99;background:var(--panel);border-right:1px solid var(--line);padding:20px 22px 18px;display:flex;flex-direction:column;transform:translateX(-105%);transition:transform .26s ease;overflow-y:auto}}
    .mnav.open{{transform:translateX(0)}}
    .mnav-head{{display:flex;align-items:center;justify-content:space-between}}
    .mnav-brand{{font-family:var(--disp);font-weight:700;font-size:16px;letter-spacing:.04em;color:var(--ink)}}
    .mnav-brand em{{color:var(--orange);font-style:normal}}
    .mnav-close{{background:none;border:none;color:var(--muted);font-size:19px;line-height:1;cursor:pointer;padding:4px}}
    .mnav-tag{{font-size:11.5px;color:var(--muted);margin-top:3px}}
    .mnav-k{{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;color:var(--orange);margin:22px 0 4px}}
    .mnav-links{{display:flex;flex-direction:column}}
    .mnav-links a{{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-bottom:1px solid var(--line);font-size:16.5px;color:var(--ink)}}
    .mnav-links a:last-child{{border-bottom:none}}
    .mnav-links a span{{color:var(--orange)}}
    .mnav-chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}}
    .mnav-chips a{{font-size:12.5px;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:6px 13px}}
    .mnav-util{{display:flex;align-items:center;gap:10px;padding:12px 0;border-top:1px solid var(--line);margin-top:auto}}
    .mnav-util .mnav-lang{{font-family:var(--mono);font-size:12px;letter-spacing:.08em;border:1px solid var(--line);border-radius:8px;padding:5px 12px;color:var(--muted)}}
    .mnav-util .mnav-theme{{background:none;border:1px solid var(--line);border-radius:8px;padding:4px 11px;font-size:14px;line-height:1.4;cursor:pointer;color:var(--ink)}}
    .mnav-chat{{background:#1877F2;border-radius:10px;text-align:center;padding:11px 0;font-size:14px;color:#fff;font-weight:600;margin-top:2px}}
  }}
  /* ═══ end of CSS block MOBILE DRAWER MENU ═══ */
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <button class="mnav-btn" id="mnavBtn" aria-label="Open menu" aria-expanded="false">☰</button>
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
    <a class="btn-chat" href="https://lin.ee/LpUR3Ld" style="background:#06C755"><span style="display:inline-grid;place-items:center;border-radius:5px;background:#fff;color:#06C755;font-weight:800;font-size:9px;font-family:Arial,sans-serif;line-height:1;padding:3px 4px;letter-spacing:.02em;margin-right:7px;vertical-align:1px">LINE</span>Add LINE</a>
  </div>
</header>

<!-- ═══ MOBILE DRAWER MENU: drawer (removable) ═══ -->
<div class="mnav-scrim" id="mnavScrim" aria-hidden="true"></div>
<aside class="mnav" id="mnav" aria-label="Main menu">
  <div class="mnav-head">
    <span class="mnav-brand"><img src="/img/logo.png" alt="" width="24" height="24" style="object-fit:contain;vertical-align:-6px;margin-right:8px">LUCERNA<em>PRO</em></span>
    <button class="mnav-close" id="mnavClose" aria-label="Close menu">✕</button>
  </div>
  <div class="mnav-tag" style="font-family:var(--mono);letter-spacing:.05em">Real deal or nothing</div>
  <div class="mnav-k">MENU</div>
  <nav class="mnav-links">
    <a href="/en/">Home <span>→</span></a>
    <a href="/en/#finder">All products <span>→</span></a>
    <a href="/en/casestudy/">Case Study <span>→</span></a>
    <a href="/en/#contact">Contact <span>→</span></a>
  </nav>
  <div class="mnav-k">SHORTCUTS</div>
  <div class="mnav-chips">
    <a href="/en/#waterproof">Waterproofing</a>
    <a href="/en/#flooring">Flooring</a>
    <a href="/en/#coating">Coatings</a>
  </div>
  <div class="mnav-util">
    <button class="mnav-theme" id="mnavTheme" aria-label="Toggle color theme">🌙</button>
  </div>
  <a class="mnav-chat" href="https://m.me/lucernapro">f&nbsp; Facebook chat — fast replies</a>
</aside>
<!-- ═══ end of drawer MOBILE DRAWER MENU ═══ -->


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

<!-- ═══ MOBILE DRAWER MENU: JS (removable) ═══ -->
<script>
(function(){{
  var mn=document.getElementById('mnav'),sc=document.getElementById('mnavScrim'),
      bt=document.getElementById('mnavBtn'),cl=document.getElementById('mnavClose'),
      tb=document.getElementById('mnavTheme'),master=document.getElementById('themeToggle');
  if(!mn||!bt)return;
  function set(open){{
    mn.classList.toggle('open',open);sc.classList.toggle('open',open);
    bt.setAttribute('aria-expanded',open?'true':'false');
    document.body.style.overflow=open?'hidden':'';
  }}
  bt.addEventListener('click',function(){{set(true)}});
  cl.addEventListener('click',function(){{set(false)}});
  sc.addEventListener('click',function(){{set(false)}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')set(false)}});
  window.addEventListener('pageshow',function(){{set(false)}});
  mn.querySelectorAll('.mnav-links a,.mnav-chips a,.mnav-chat').forEach(function(a){{
    a.addEventListener('click',function(){{set(false)}});
  }});
  if(tb){{
    if(!master){{tb.style.display='none';}}
    else{{
      function syncT(){{tb.textContent=document.documentElement.dataset.theme==='dark'?'☀️':'🌙';}}
      tb.addEventListener('click',function(){{master.click();syncT();}});
      syncT();
    }}
  }}
}})();
</script>
<!-- ═══ end of JS MOBILE DRAWER MENU ═══ -->
</body>
</html>
"""

# รูปแนวตั้ง (สูงกว่ากว้าง) — จำกัดความกว้างด้วย class .tall กันภาพล้นจอ
V2_TALL = {"waterproofing-techniques-07.webp","waterproofing-techniques-08.webp","waterproofing-techniques-11.webp"}



root_img = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "post")

def _img_dims(path):
    """Real pixel dims for width/height attrs (กฎกันภาพยืด). WebP via header, SVG via viewBox."""
    if path.endswith(".svg"):
        import re as _re
        m = _re.search(r'viewBox="0 0 (\d+) (\d+)"', open(path, encoding="utf-8").read())
        return int(m.group(1)), int(m.group(2))
    from PIL import Image as _Image
    with _Image.open(path) as im:
        return im.size

def render_v2_body(lang_data, alt_prefix):
    intro = "\n".join(f"    <p>{t}</p>" for t in lang_data["intro"])
    if lang_data.get("hero"):
        fn, cap = lang_data["hero"]
        w, h = _img_dims(os.path.join(root_img, fn))
        intro += (f'\n    <figure class="hero"><img src="/img/post/{fn}" alt="{alt_prefix} — {cap}" width="{w}" height="{h}">'
                  f'<figcaption>{cap}</figcaption></figure>')
    blocks = []
    for i, s in enumerate(lang_data["steps"], 1):
        b  = f'    <section class="step">\n'
        b += f'      <h2><span class="n">{i:02d}</span>{s["h"]}</h2>\n'
        for t in s.get("text", []):
            b += f'      <p>{t}</p>\n'
        for fn, cap in s.get("figs", []):
            tall = ' class="tall"' if fn in V2_TALL else ""
            w, h = _img_dims(os.path.join(root_img, fn))
            b += (f'      <figure><img{tall} src="/img/post/{fn}" alt="{alt_prefix} — {cap}" loading="lazy" width="{w}" height="{h}">'
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
        thumb = p.get("thumb_en", p["thumb"]) if lang == "en" else p["thumb"]
        intro, steps = render_v2_body(d, d["title"])
        prod_links = "".join(f'<a href="{u}">{n}</a>' for n, u in d["prods"])
        html = tpl.format(title=d["title"], desc=d["desc"], slug=p["slug"], base=BASE,
                          thumb=thumb, cat_label=d["cat_label"], date=date,
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
