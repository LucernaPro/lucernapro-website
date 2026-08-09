# -*- coding: utf-8 -*-
"""
build_floorseep_post.py — สร้างโพสต์ floor-seepage-negative-side (TH+EN)
ด้วยวิธี chrome-transplant จากโพสต์ล่าสุด solar-panel-defender-feibo-lab
(ดูเหตุผลใน gen_posts.py: template ในไฟล์นั้นล้าหลังกว่าหน้า live แล้ว)
รัน: python3 tools/build_floorseep_post.py (จาก root ของ repo)
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "floor-seepage-negative-side"

# ─────────────────────────────────────────── TH
TH_TITLE = "น้ำซึมขึ้นจากพื้นบ้าน — ทางซ่อมพื้นปูนเปลือย และพื้นกระเบื้องที่ยาแนวอัดไม่ลง"
TH_DESC = ("พื้นบ้านชื้น สีโป่ง คราบเกลือขาว — น้ำดันขึ้นจากใต้พื้นคือสนาม Negative Side ของแท้ "
           "พาไล่ทางซ่อมทั้งพื้นปูนเปลือย (PatchPro + MarineGuard) และพื้นกระเบื้อง (เปลี่ยนยาแนวเป็น Epoxy ทุกร่อง) "
           "รวมด่านโหดสุด: กระเบื้องปูชิดจนร่องแคบเกิน ที่ต้องกรีดร่องก่อนถึงจะอัดได้")
TH_EYEBROW = "Case Study · เทคนิค / ความรู้"
TH_META = "เผยแพร่ ส.ค. 2026 · โดยทีมงาน LucernaPro"

TH_BODY = """  <article>
    <p>อาการหน้าตาแบบนี้: พื้นบ้านชื้นทั้งที่ไม่มีน้ำหก สีทาพื้นโป่งพองเป็นหย่อมๆ คราบเกลือขาว (Efflorescence) ผุดตามผิวปูนหรือร่องยาแนว และพอเข้าหน้าฝนอาการหนักขึ้นชัดเจน — นี่ไม่ใช่น้ำจากด้านบน แต่คือ <b>ความชื้นและน้ำใต้ดินดันขึ้นมาจากใต้พื้น</b></p>
    <p>ถ้าเคยอ่านเคส <a href="/post/negative-side-waterproofing">ทากันซึมจากด้านในบ้าน</a> ของเรามาก่อน จะจำหลักข้อเดียวกันได้: กันซึมที่ถูกหลักต้องทา <b>ฝั่งที่น้ำมา</b> — และเคสพื้นบ้านคือเวอร์ชันที่โหดที่สุดของหลักข้อนี้ เพราะฝั่งที่น้ำมาคือ <b>ดินใต้บ้าน</b> ไม่มีใครขุดบ้านทั้งหลังลงไปทากันซึมข้างล่างได้ งานนี้จึงเป็นสนาม Negative Side เต็มรูปแบบตั้งแต่ยังไม่เริ่มทำอะไรเลย</p>
    <figure class="hero"><img src="/img/post/{slug}-00.webp" alt="น้ำดันขึ้นจากใต้พื้นบ้าน — หน้าตัดแสดงน้ำใต้ดินดันผ่านพื้นคอนกรีตขึ้นมาทางรอยร้าว มุมห้อง และผิวปูน" width="1200" height="900"><figcaption>หน้าตัดของปัญหา: น้ำและความชื้นใต้ดินดันขึ้นตลอดเวลา — ทางเข้าหลักคือรอยร้าว มุมห้อง และเนื้อปูนเอง</figcaption></figure>
    <section class="step">
      <h2><span class="n">01</span>พื้นไม่เหมือนผนัง — โจทย์บวกเพิ่มอีกหนึ่งข้อ: ต้องเดินเหยียบได้</h2>
      <p>แรงดันย้อน (Negative Hydrostatic Pressure) ที่พยายามถีบฟิล์มออกจากผิวคือศัตรูตัวเดียวกับเคสผนัง แต่พื้นมีเงื่อนไขเพิ่มที่ผนังไม่มี: <b>มันต้องรับการเดินเหยียบ ขัดถู และลากเฟอร์นิเจอร์ทุกวัน</b></p>
      <p>เงื่อนไขข้อนี้ทำให้ตัวเลือกเปลี่ยน — <a href="/deepseal">DeepSeal</a> ตัวกันซึมฝั่ง Negative เฉพาะทางของเรา เกิดมาเพื่อผนังและจุดที่ไม่มีการเดินเหยียบ เนื้อสารถูกออกแบบให้เน้นซึมลงรูพรุนคอนกรีตเป็นหลัก ไม่ได้เน้นสร้างผิวแข็งไว้รับรองเท้าและขาโต๊ะ</p>
      <p>พื้นที่ใช้งานจริงจึงต้องการอีกแบบ: ฟิล์มที่แห้งแล้ว <b>แข็ง เดินได้จริง</b> และแรงยึดเกาะสูงพอจะสู้แรงดันจากด้านล่าง — ตัวที่เราใช้คือ <a href="/marineguard">MarineGuard</a> Epoxy สองส่วนผสมเนื้อ 100% Solids (Curing system powered by Huntsman) ที่มีจุดแข็งตรงสเปคเคสนี้สองข้อพอดี: <b>แรงยึดเกาะสูงมาก</b> และ <b>เกาะได้แม้ปูนหมาด</b> ซึ่งสำคัญ เพราะพื้นแบบนี้เนื้อปูนมีความชื้นสะสมอยู่แล้วแทบตลอดเวลา ระบบที่ต้องรอพื้นแห้งสนิทถึงจะเกาะ แทบไม่มีวันได้เริ่มงาน</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>เคสที่หนึ่ง — พื้นปูนเปลือย: อุดให้จบก่อน แล้วค่อยเคลือบทั้งผืน</h2>
      <p>ลำดับงานห้ามสลับ: ไล่หา <b>รอยร้าว มุมห้อง และแนวพื้นชนผนัง</b> ให้ครบก่อน แล้วอุดด้วย <a href="/patchpro">PatchPro</a> ให้เต็มเสมอผิว — เนื้อโป๊ว Polymer Modified สองส่วนผสมที่เกิดมาเพื่อรอยร้าวพื้นปูนโดยเฉพาะ เหตุผลเดียวกับที่เราย้ำทุกเคส: กันซึมทุกตัวคือฟิล์มบางๆ ไม่ใช่วัสดุอุดร่อง ทาข้ามรอยร้าวไปคือรอวันฟิล์มขาดตามแนวเดิม</p>
      <p>รอวัสดุอุดเซ็ตตัวเต็มที่ตามคู่มือ แล้วเคลือบ MarineGuard ทั้งผืน 2 รอบด้วยลูกกลิ้ง (เนื้อน้ำยา 1 กก. ≈ 5 ตร.ม. ครบสองรอบ) ชั่ง A:B ตรงอัตรา กวนให้เข้ากันจริง และทาให้หมดภายในเวลา — วินัยสามข้อของระบบสองส่วนผสม</p>
      <p><b>Straight Talk สองข้อก่อนตัดสินใจ:</b> ข้อแรก ผิว MarineGuard โดนแสงสะสมแล้วจะเหลืองตัว งานอยู่อาศัยที่อยากได้พื้นสีสวย ให้ทาสีพื้น PU ทับหน้า ได้ทั้งสีที่ต้องการและอายุการใช้งานที่ยาวขึ้น ข้อสอง <b>งานฝั่ง Negative ไม่มีใครการันตี 100% ได้</b> — แรงดันน้ำจริงของหน้างานคุณคือตัวตัดสิน สิ่งที่เราให้ได้คือระบบที่แรงยึดเกาะสูงที่สุดเท่าที่ทาเองได้จริง ไม่ใช่คำสัญญาลอยๆ</p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>เคสที่สอง — พื้นปูกระเบื้อง: ทากันซึมทับทั้งผืนไม่ใช่ทางเลือก</h2>
      <p>ผิวเคลือบของกระเบื้องลื่นจนฟิล์มกันซึมยึดยาก และต่อให้ยึดได้ ก็คงไม่มีใครอยากได้พื้นกระเบื้องทั้งบ้านที่โดนทาสีทับจนมองไม่เห็นลาย — แต่ข่าวดีคือ น้ำเองก็ผ่านตัวกระเบื้องไม่ได้เหมือนกัน มันขึ้นมาทาง <b>ร่องยาแนว</b> กับ <b>มุมห้อง</b> เป็นหลัก เพราะยาแนวปูนทั่วไปคือฟองน้ำดีๆ นี่เอง</p>
      <p>ทางซ่อมจึงชัด: ขูดยาแนวเดิมออก แล้วยาแนวใหม่ทุกร่องด้วย <a href="/epoxygrout">ยาแนวกันซึม Epoxy TileGrout</a> เนื้อ Epoxy ทึบน้ำ ไม่ดูดซึม ส่วนมุมห้อง แนวพื้นชนผนัง และขอบสุขภัณฑ์ อุดปิดด้วย PatchPro ให้จบในรอบเดียวกัน — ใครใช้งานเองครั้งแรกแล้วกลัวผสมพลาด มี<a href="/carbontilegrout">รุ่นปืนยิง Carbon</a> ที่ผสมเองที่ปลายหลอด ตัดโอกาสพลาดทิ้ง</p>
    </section>
    <section class="step">
      <h2><span class="n">04</span>ด่านสุดท้าย — กระเบื้องปูชิดจนร่องแคบเกินกว่ายาแนวจะลง</h2>
      <p>บางบ้านช่างปูกระเบื้องชิดกันมาก ร่องเหลือแค่มิลสองมิล — อัดยาแนวใหม่ยังไงเนื้อวัสดุก็ลงไปไม่ถึงก้นร่อง และพื้นที่ให้มันยึดเกาะก็น้อยเกินกว่าจะอยู่ได้จริง นี่คือจุดที่หลายคนหันไปหาทางลัด</p>
      <p><b>Straight Talk: ทางลัดนั้นเราลองให้แล้วด้วยเงินของเราเอง</b> — เทระบบ Epoxy Self-Leveling บางๆ ทับหน้ากระเบื้องทั้งผืน ผลคือ <b>ไม่อยู่</b> ผิวเคลือบกระเบื้องลื่นและพื้นที่ยึดเกาะน้อยเกินไป ใช้งานได้ไม่นานขอบเริ่มเผยอ แล้วล่อนตามกันทั้งแผ่น เสียทั้งค่าของและค่าเวลารื้อ</p>
      <p>ทางที่เราเห็นว่าจบจริงมีทางเดียว: ใช้เครื่องเจียรใส่ใบตัด <b>กรีดร่องยาแนวให้กว้างและลึกขึ้น</b> เปิดพื้นที่ยึดเกาะให้วัสดุ แล้วอัด Epoxy TileGrout ให้เต็มเสมอผิว — งานฝุ่นเยอะและเหนื่อยกว่าเทข้ามหน้ากระเบื้องแน่นอน แต่เป็นการแลกที่คุ้ม เพราะทำรอบเดียวแล้วไม่ต้องกลับมารื้อซ้ำ</p>
      <figure><img src="/img/post/{slug}-info-th.webp" alt="กระเบื้องปูชิด ร่องแคบเกิน — เปรียบเทียบทางลัดเท Epoxy ทับหน้าที่หลุดล่อน กับการกรีดร่องให้กว้างขึ้นแล้วอัดยาแนว Epoxy ให้เต็ม" loading="lazy" width="1200" height="900"><figcaption>สามช็อตจบ: ร่องแคบเกิน → ทางลัดที่เราลองแล้วพัง → ทางที่จบจริง</figcaption></figure>
    </section>
    <section class="step">
      <h2><span class="n">05</span>พูดตรงๆ เรื่องผลลัพธ์ — งานฝั่ง Negative คือเกมไล่ปิดทีละประตู</h2>
      <p>ปิดทางหลักแล้ว น้ำที่ยังมีแรงดันอยู่อาจย้ายไปโผล่ทางรองที่ยังเปิดอยู่ — ถ้าเจอแบบนั้น ไม่ได้แปลว่าระบบที่ทำไปพัง แปลว่า <b>ถึงคิวประตูบานถัดไป</b> วิธีทำงานที่ถูกและประหยัดที่สุดคือปิดจุดหนักสุดก่อน รอฝนตกจริงแล้วเช็คผล ค่อยไล่ปิดจุดต่อไป ดีกว่าเหมาทำทุกอย่างพร้อมกันโดยไม่รู้ว่าตัวไหนได้ผล</p>
      <p>และถ้าลดน้ำที่ต้นทางได้ ให้ทำควบคู่เสมอ: จัดระบายน้ำรอบบ้านไม่ให้น้ำฝนขังชิดตัวบ้าน — ยิ่งแรงดันใต้พื้นต่ำลง ระบบที่ทาไว้ยิ่งอยู่ยาว ไม่แน่ใจว่าบ้านคุณเข้าเคสไหน ส่งรูปหน้างานมาทางแชทเพจ เราดูให้ฟรีก่อนตัดสินใจซื้อ</p>
    </section>
  </article>
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/marineguard">MarineGuard</a><a href="/patchpro">PatchPro</a><a href="/epoxygrout">ยาแนว Epoxy TileGrout</a><a href="/deepseal">DeepSeal</a></div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
""".replace("{slug}", SLUG)

# ─────────────────────────────────────────── EN
EN_TITLE = "Water Rising Through the Floor — Fixing Bare Concrete and Tiled Floors from the Wrong Side"
EN_DESC = ("A damp floor, blistered paint, white salt stains — water pushing up from under the slab is true negative-side "
           "territory. The repair path for bare concrete (PatchPro + MarineGuard) and tiled floors (re-grout every joint "
           "with epoxy), plus the hardest case: tiles laid so tight the joints must be cut wider before grout can go in.")
EN_EYEBROW = "Case Study · Tips / Know-how"
EN_META = "Published Aug 2026 · by the LucernaPro team"

EN_BODY = """  <article>
    <p>The symptoms look like this: a floor that stays damp with nothing spilled on it, floor paint blistering in patches, white salt stains (efflorescence) blooming on the concrete or along grout lines — and everything getting worse in the rainy season. This is not water from above. It is <b>moisture and groundwater pushing up from underneath the slab</b>.</p>
    <p>If you have read our case on <a href="/en/post/negative-side-waterproofing">waterproofing from inside the house</a>, you know the one rule that matters: proper waterproofing goes on <b>the side the water comes from</b>. A house floor is the most brutal version of that rule, because the water side is <b>the soil under your home</b> — nobody can dig up a house to coat underneath it. This job is full negative-side territory before you even start.</p>
    <figure class="hero"><img src="/img/post/{slug}-00en.webp" alt="Water pushing up from under a house floor — cross-section showing groundwater forcing through a concrete slab via cracks, room corners and the slab itself" width="1200" height="900"><figcaption>The problem in cross-section: groundwater and moisture push upward constantly — the main entry points are cracks, room corners, and the concrete itself</figcaption></figure>
    <section class="step">
      <h2><span class="n">01</span>A Floor Is Not a Wall — One Extra Requirement: You Walk on It</h2>
      <p>Negative hydrostatic pressure — water trying to shove the film off the surface — is the same enemy as in the wall case. But a floor adds a condition a wall never has: <b>it takes foot traffic, scrubbing, and furniture being dragged across it every day</b>.</p>
      <p>That changes the pick. <a href="/en/deepseal">DeepSeal</a>, our dedicated negative-side sealer, was built for walls and areas with no foot traffic — its whole design is about soaking deep into the concrete's pores, not building a hard wearing surface for shoes and table legs.</p>
      <p>A floor you actually live on needs the other kind: a film that dries <b>hard and genuinely walkable</b>, with adhesion strong enough to fight pressure from below. Our pick is <a href="/en/marineguard">MarineGuard</a> — a two-part, 100% solids epoxy (curing system powered by Huntsman) whose two headline strengths happen to be exactly what this case demands: <b>extremely high adhesion</b>, and <b>the ability to bond to damp concrete</b>. That last one matters, because a floor like this almost never fully dries out — a system that needs bone-dry concrete before it can grip would never get to start.</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>Case One — Bare Concrete: Seal Every Opening First, Then Coat the Whole Slab</h2>
      <p>The order is non-negotiable: hunt down every <b>crack, room corner, and wall-to-floor joint</b> first, and fill them flush with <a href="/en/patchpro">PatchPro</a> — a two-part polymer-modified filler made specifically for concrete floor cracks. Same reason we repeat in every case: any waterproofing coat is a thin film, not a gap filler. Coat straight over a crack and you are waiting for the film to tear along that exact line.</p>
      <p>Let the filler fully cure per the manual, then roll on two coats of MarineGuard across the whole slab (1 kg ≈ 5 m² for both coats). Weigh A:B exactly, mix until truly uniform, and apply within the working time — the three disciplines of any two-part system.</p>
      <p><b>Two pieces of Straight Talk before you decide:</b> first, MarineGuard ambers with accumulated light — for living areas where looks matter, topcoat it with a PU floor paint and get both the color you want and a longer service life. Second, <b>nobody can guarantee 100% on the negative side</b> — the real water pressure under your slab is the referee. What we can give you is the highest-adhesion system you can realistically apply yourself, not an empty promise.</p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>Case Two — Tiled Floors: Coating Over the Tiles Is Not an Option</h2>
      <p>Glazed tile is too slick for a waterproofing film to grip well — and even if it gripped, nobody wants a tiled floor painted over until the pattern disappears. The good news: water can't pass through the tile body either. It comes up through the <b>grout lines</b> and the <b>room corners</b>, because ordinary cement grout is essentially a sponge.</p>
      <p>So the repair is clear: rake out the old grout and re-grout every joint with <a href="/en/epoxygrout">Epoxy TileGrout</a> — a dense, non-absorbent epoxy body — then seal the room corners, wall-to-floor lines, and fixture edges with PatchPro in the same round. First-timers worried about mixing errors can use the <a href="/en/carbontilegrout">Carbon gun-grade version</a>, which mixes itself at the nozzle tip.</p>
    </section>
    <section class="step">
      <h2><span class="n">04</span>The Final Boss — Tiles Laid So Tight the Grout Can't Go In</h2>
      <p>In some houses the tiler laid the tiles nearly touching — joints of a millimeter or two. No matter how you pack new grout, the material can't reach the bottom of the joint, and the bonding area is too small for it to survive anyway. This is where people reach for a shortcut.</p>
      <p><b>Straight Talk: we tried that shortcut with our own money</b> — pouring a thin self-leveling epoxy system across the whole tiled surface. The result: <b>it didn't hold</b>. Glazed tile is slick and the bonding area is simply too small; before long the edges lifted and it peeled off in sheets. You pay for the material, then pay again to strip it.</p>
      <p>The only route we have seen genuinely finish the job: take an angle grinder with a cutting disc and <b>cut the grout lines wider and deeper</b>, opening up real bonding area, then pack Epoxy TileGrout in flush. It is dustier and harder work than pouring over the top — and worth every minute, because you do it once and never come back to redo it.</p>
      <figure><img src="/img/post/{slug}-info-en.webp" alt="Tiles laid too tight — comparing the failed shortcut of pouring epoxy over the surface with cutting the joints wider and packing them full of epoxy grout" loading="lazy" width="1200" height="900"><figcaption>Three frames: joints too narrow → the shortcut we tried and lost → the fix that actually finishes the job</figcaption></figure>
    </section>
    <section class="step">
      <h2><span class="n">05</span>Straight Talk on Results — Negative-Side Work Is a Game of Closing Doors</h2>
      <p>Close the main path, and water still under pressure may resurface at a smaller path that's still open. If that happens, it does not mean your work failed — it means <b>the next door is up</b>. The right and cheapest way to work is: close the worst point first, wait for real rain, check the result, then move to the next — far better than doing everything at once with no idea which fix actually worked.</p>
      <p>And whenever you can reduce the water at its source, do it in parallel: manage drainage around the house so rainwater never ponds against the building. The lower the pressure under the slab, the longer everything you applied will last. Not sure which case your house is? Send us photos over chat — we'll take a look for free before you spend anything.</p>
    </section>
  </article>
  <div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/marineguard">MarineGuard</a><a href="/en/patchpro">PatchPro</a><a href="/en/epoxygrout">Epoxy TileGrout</a><a href="/en/deepseal">DeepSeal</a></div>
  <a class="back" href="/en/casestudy/">← Back to all case studies</a>
""".replace("{slug}", SLUG)

def transplant(src_path, out_path, title, desc, eyebrow, h1, meta, body, og_img):
    h = open(src_path, encoding="utf-8").read()
    h = h.replace(SRC, SLUG)                                    # canonical/hreflang/lang-switch
    h = re.sub(r"<title>.*?</title>", f"<title>{title} | Case Study LucernaPro</title>", h, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title} | Case Study LucernaPro">', h, flags=re.S)
    h = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="https://www.lucernapro.com/img/post/{og_img}">', h, flags=re.S)
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
    transplant(os.path.join(ROOT, "post", SRC, "index.html"),
               os.path.join(ROOT, "post", SLUG, "index.html"),
               TH_TITLE, TH_DESC, TH_EYEBROW, TH_TITLE, TH_META, TH_BODY, f"{SLUG}-00.webp")
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"),
               os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN_TITLE, EN_DESC, EN_EYEBROW, EN_TITLE, EN_META, EN_BODY, f"{SLUG}-00en.webp")
