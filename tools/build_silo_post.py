# -*- coding: utf-8 -*-
"""
build_silo_post.py — เปิดเคสไซโล (V1 "ชมพลังของ-deepstick-กันชัดๆ") กลับขึ้น /casestudy
ด้วยวิธี chrome-transplant จากโพสต์ solar (dark theme + favicon ครบ)
เนื้อหาไทย = คำต่อคำจาก V1 (Wix migration) / EN = แปลจากต้นฉบับ
รูป: hotlink wixstatic ชั่วคราว (งาน salvage ยังค้างตาม SPEC — sandbox ต่อ wixstatic ไม่ได้)
รัน: python3 tools/build_silo_post.py (จาก root ของ repo)
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "deepstick-factory-silo-joints"

WIX = "https://static.wixstatic.com/media/"
def hero_url(mid): return f"{WIX}{mid}/v1/fill/w_1200,h_900,al_c,q_90/{mid}"
def gal_url(mid):  return f"{WIX}{mid}/v1/fill/w_720,h_720,al_c,q_85/{mid}"

GALLERY = [
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
]

GRID_STYLE = ("display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));"
              "gap:10px;margin-top:26px")

def gallery_html(alt_prefix):
    imgs = "".join(
        f'<img src="{gal_url(m)}" alt="{alt_prefix} {i+1:02d}" loading="lazy" '
        f'width="720" height="720" style="border-radius:10px;border:1px solid var(--line)">\n'
        for i, m in enumerate(GALLERY))
    return f'<div style="{GRID_STYLE}">\n{imgs}</div>'

TH_TITLE = "ชมพลังของ DeepStick กันชัดๆ — งานรอยต่อไซโลบนดาดฟ้าโรงงานใหญ่ระดับประเทศ"
TH_DESC = ("งานรอยต่อที่โหดที่สุดที่เราเคยเจอ: ไซโลบนดาดฟ้าโรงงานใหญ่อันดับต้นๆ ของไทย เจาะทะลุพื้นปูน "
           "แรงสั่นสะเทือนตลอดเวลา ตัวโป๊วและซิลิโคนทั่วไปเอาไม่อยู่ — โป๊วจบด้วย DeepStick แล้วเคลือบทับด้วย "
           "Polyurea Gen3 สามรอบ พร้อมภาพหน้างานจริงกว่า 40 ภาพ")
TH_EYEBROW = "Case Study · รอยต่อ / รอยร้าว"
TH_META = "เผยแพร่ ก.พ. 2024 · โดยทีมงาน LucernaPro"

TH_BODY = f"""  <article>
    <p>งานรอยต่อที่ยากมากๆ สำหรับเราคงไม่มีงานไหนเกินงานนี้แล้ว</p>
    <figure class="hero"><img src="{hero_url(GALLERY[0])}" alt="งานรอยต่อไซโลบนดาดฟ้าโรงงาน — หน้างานจริง" width="1200" height="900"><figcaption>หน้างานจริง: ไซโลเจาะทะลุขึ้นมาจากพื้นดาดฟ้าโรงงาน</figcaption></figure>
    <p>เป็นไซโลในโรงงานที่ใหญ่อันดับต้นๆ ของไทย ตั้งอยู่บนดาดฟ้าเจาะทะลุขึ้นมาจากพื้นปูน มีแรงสั่นสะเทือนตลอดเวลา งานนี้มีการทำปูนโอบไว้อย่างดีก็ยังมีรอยรั่วลงไปชั้นล่าง ใช้ตัวโป๊วหรือซิลิโคนทั่วไปไม่ได้เลย</p>
    <p>งานนี้ DeepStick แก้ปัญหาได้เรียบร้อยด้วยคุณสมบัติที่ไม่เหมือนใคร เป็นตัวโป๊วที่ยืดหยุ่นแต่มีความเหนียวแน่นในตัวและแรงยึดเกาะสูงมากแม้บนพื้นผิวแปลกๆ แทบจะเรียกว่าพื้นผิวแบบไหนก็โป๊วได้</p>
    <p>หลังจากโป๊วให้ทั่วแล้วก็ทาทับพื้นที่ด้วยกันซึมตัว Top ของเราด้วย Polyurea Gen3 ปกติทาเพียง 2 รอบก็พอแต่งานนี้ทา 3 รอบไปเลยเพื่อให้ใช้งานได้ยาวนานยิ่งกว่าเดิม</p>
    <section class="step">
      <h2><span class="n">📷</span>ภาพหน้างานจริงทั้งชุด — ไล่ดูทีละขั้นได้เลย</h2>
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
    <figure class="hero"><img src="{hero_url(GALLERY[0])}" alt="Silo joint repair on a factory rooftop — real jobsite" width="1200" height="900"><figcaption>The real site: silos punching up through the factory's rooftop concrete deck</figcaption></figure>
    <p>These are silos at one of Thailand's largest factories, mounted on the rooftop and punching through the concrete deck, vibrating constantly. Even with concrete collars cast carefully around them, water still leaked to the floor below — ordinary fillers and silicone sealants stood no chance here.</p>
    <p>DeepStick closed this job with a property set nothing else has: a filler that is flexible yet dense and tenacious in body, with extremely high adhesion even on unusual surfaces — you could almost say there is no surface it won't bond to.</p>
    <p>After every joint was sealed, the whole area was coated over with our top waterproofing, Polyurea Gen3. Two coats are normally enough — this job got three, for an even longer service life.</p>
    <section class="step">
      <h2><span class="n">📷</span>The Full Jobsite Photo Set — Step Through the Whole Job</h2>
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
    og = hero_url(GALLERY[0])
    transplant(os.path.join(ROOT, "post", SRC, "index.html"),
               os.path.join(ROOT, "post", SLUG, "index.html"),
               TH_TITLE, TH_DESC, TH_EYEBROW, TH_TITLE, TH_META, TH_BODY, og)
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"),
               os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN_TITLE, EN_DESC, EN_EYEBROW, EN_TITLE, EN_META, EN_BODY, og)
