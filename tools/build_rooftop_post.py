# -*- coding: utf-8 -*-
"""
build_rooftop_post.py — สร้างโพสต์ rooftop-concrete-or-tile (TH+EN)
ด้วยวิธี chrome-transplant จากโพสต์ล่าสุด floor-seepage-negative-side
รัน: python3 tools/build_rooftop_post.py (จาก root ของ repo)
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "floor-seepage-negative-side"
SLUG = "rooftop-concrete-or-tile"

# ─────────────────────────────────────────── TH
TH_TITLE = "ดาดฟ้ารั่ว — ทำไมเราต้องถามก่อนเสมอว่า ดาดฟ้าปูนเปลือย หรือปูกระเบื้อง"
TH_DESC = ("คำถามเดียวที่ตัดสินว่างานกันซึมดาดฟ้าจะอยู่หลายปีหรือลอกในไม่กี่เดือน — "
           "ปูนเปลือย: น้ำเข้าตรงรอยแตก อุด PatchPro แล้วเคลือบ PolyPro / "
           "ปูกระเบื้อง: น้ำเดินใต้กระเบื้อง จุดหยดไม่ตรงจุดเข้า ทางจบสุดคือเปลี่ยนยาแนวเป็น Epoxy "
           "แต่ของจริงคือรื้อยาแนวเดิมโหดมาก — เคสนี้เล่าครบทั้งสองทาง")
TH_EYEBROW = "Case Study · เทคนิค / ความรู้"
TH_META = "เผยแพร่ ส.ค. 2026 · โดยทีมงาน LucernaPro"

TH_BODY = """  <article>
    <p>ทุกวันจะมีข้อความหน้าตาแบบนี้เข้ามาในแชทเพจ: <b>"ดาดฟ้ารั่วครับ น้ำหยดลงฝ้า ใช้ตัวไหนดี"</b> — และคำตอบแรกจากทีมเราเหมือนกันทุกครั้ง ไม่ใช่ชื่อสินค้า ไม่ใช่ราคา แต่เป็นคำถามกลับสั้นๆ ว่า <b>ดาดฟ้าเป็นปูนเปลือย หรือปูกระเบื้อง?</b></p>
    <p>บางท่านอาจนึกในใจว่าถามทำไม รั่วก็คือรั่ว ทากันซึมเหมือนกันไม่ใช่หรือ — ไม่เหมือนครับ สองพื้นผิวนี้ <b>น้ำเข้าคนละทาง เดินคนละเส้น และแผนซ่อมที่ได้ผลก็คนละแผน</b> เลือกระบบผิดตั้งแต่คำถามแรก คือจ่ายสองรอบ: รอบแรกค่าของกับค่าแรงที่เสียเปล่า รอบสองค่ารื้อของที่ลอกออกก่อนทำใหม่</p>
    <p>เคสนี้เลยขอเล่ายาวรอบเดียวให้จบ ว่าคำถามข้อนี้เปลี่ยนแผนงานยังไง — อ่านจบแล้วดูดาดฟ้าตัวเองออกเลยว่าต้องเดินทางไหน</p>
    <figure class="hero"><img src="/img/post/{slug}-hero.webp" alt="ดาดฟ้าบ้านพักอาศัยปูกระเบื้องเต็มผืน เห็นร่องยาแนวชัดทั่วพื้น มีราวระเบียงไม้ กระถางต้นไม้ และชุดโต๊ะนั่งเล่น" width="1600" height="1200"><figcaption>ดาดฟ้าปูกระเบื้องหน้าตาดีแบบนี้แหละ ที่พอรั่วแล้วหาจุดเข้าของน้ำยากที่สุด — เพราะทางเข้าคือร่องยาแนวที่มองผ่านตลอด</figcaption></figure>
    <section class="step">
      <h2><span class="n">01</span>อาการเดียวกัน — แต่คนละโรค</h2>
      <p>ลองดูลูกค้าสองรายที่ทักเข้ามาในสัปดาห์เดียวกัน อาการภายนอกเหมือนกันทุกอย่าง: น้ำหยดจากฝ้าห้องชั้นบนสุด คราบวงเหลืองลามบนฝ้า หน้าฝนหนักขึ้นชัด</p>
      <p><b>รายแรก — ดาดฟ้าปูนเปลือย:</b> ขึ้นไปดูเจอรอยแตกลายงากระจายทั้งผืน กับรอยต่อโคนผนังกันตกที่ปูนแยกตัว น้ำฝนซึมผ่านรอยพวกนี้ลงไปตรงๆ จุดที่หยดข้างล่างอยู่ใกล้เคียงกับจุดที่น้ำเข้าด้านบน — เจอง่าย ชี้ถูก ซ่อมตรงจุด</p>
      <p><b>รายที่สอง — ดาดฟ้าปูกระเบื้อง:</b> หน้ากระเบื้องสภาพดี ไม่มีรอยแตกให้เห็นเลยสักจุด แต่ยาแนวเสื่อม แข็งกรอบ หลุดร่อนเป็นช่วง น้ำซึมเข้าทางร่องยาแนว แล้ว<b>ไหลเดินอยู่ใต้แผ่นกระเบื้อง</b>ไปตามความลาดเอียง ก่อนหาทางลงผ่านรอยร้าวของพื้นปูนอีกฟากหนึ่ง — จุดที่น้ำหยดในบ้าน ห่างจากจุดที่น้ำเข้าจริงหลายเมตร</p>
      <figure><img src="/img/post/{slug}-compare-th.webp" alt="เปรียบเทียบดาดฟ้าปูนเปลือยที่น้ำเข้าทางรอยแตกลายงา กับดาดฟ้าปูกระเบื้องที่น้ำเข้าทางร่องยาแนวแล้วเดินใต้กระเบื้อง" loading="lazy" width="1200" height="900"><figcaption>สองพื้นผิว สองกลไกการรั่ว — คำถามข้อเดียวนี้คือจุดเริ่มของแผนงานที่ถูกต้อง</figcaption></figure>
      <p>อาการเหมือนกันเป๊ะ แต่กลไกคนละเรื่อง — และนี่คือเหตุผลข้อแรกที่เราต้องถาม เพราะถ้าวินิจฉัยผิดตั้งแต่ต้น ยาที่จ่ายจะถูกแค่ไหนก็รักษาไม่หาย</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>ดาดฟ้าปูนเปลือย — เกมตรงไปตรงมา: อุดก่อน แล้วเคลือบทั้งผืน</h2>
      <p>ทางน้ำเข้าของปูนเปลือยชัดเจน: <b>รอยแตกลายงา รอยต่อโคนผนังกันตก และรอบปากท่อระบายน้ำ</b> ลำดับงานจึงตายตัวและห้ามสลับ — ไล่หารอยพวกนี้ให้ครบก่อน แล้วอุดด้วย <a href="/patchpro">PatchPro</a> ให้เต็มเสมอผิว เหตุผลเดียวกับที่เราย้ำใน<a href="/post/why-coating-over-cracks-fails">เคสรอยร้าว</a>: กันซึมทุกตัวคือฟิล์มบางๆ ไม่ใช่วัสดุอุดร่อง ทาข้ามรอยร้าวไปคือรอวันฟิล์มขาดตามแนวเดิม</p>
      <p>รอตัวโป๊วเซ็ตตัวตามคู่มือ แล้วค่อยเคลือบทั้งผืนด้วย <a href="/polypro">PolyPro</a> — กันซึม Polyurea Gen3 ตัวท็อปของสายเรา และเป็นตัวที่เราเชียร์สุดสำหรับดาดฟ้าโดยเฉพาะ เพราะดาดฟ้าคือสนามที่โหดที่สุดของงานกันซึม: <b>โดนแดด UV เต็มวันทั้งปี บวกน้ำขังหลังฝนทุกครั้ง</b> — PolyPro ทน UV ไม่เหลือง แช่น้ำได้ถาวร และให้ฟิล์มหนากว่ากันซึมทาทั่วไปหลายเท่า สเปคตรงข้อสอบของดาดฟ้าทุกข้อ</p>
      <p>งบยังไม่ถึงตัวท็อป ไม่ต้องฝืนครับ — สนามปูนเปลือยมีตัวเริ่มต้นที่เราแนะนำเต็มปากคือ <a href="/siliconepro">SiliconePro</a> กันซึมซิลิโคนส่วนผสมเดียว เปิดฝาแล้วทาได้เลยไม่ต้องผสม เนื้อทนน้ำขังได้สบาย แลกกับอายุงานที่สั้นกว่าตัวท็อป (ราว 5 ปีทาเปลือย ยืดเป็น 8–10 ปีเมื่อเสริมผ้าไฟเบอร์กลาส) — สำหรับดาดฟ้าบ้านทั่วไปที่ไม่ได้โดนโจทย์โหดพิเศษ แค่นี้ก็ทำหน้าที่ครบแล้ว</p>
      <p>และเลือกสเกลการทาได้ตามงบอีกชั้น: <b>ทาเฉพาะแผล</b> — เฉพาะแนวรอยที่อุดไว้ รอยต่อโคนผนัง และรอบปากท่อ คือหมากเปิดเกมที่ฉลาด ปิดประตูบานหนักสุดด้วยเงินน้อยสุด รอฝนจริงตกแล้วเช็คผล ค่อยตัดสินใจลงทุนต่อ — หรือ<b>เอาให้ชัวร์ก็ทาทั้งผืน</b> จบรอบเดียว ไม่ต้องลุ้นว่าน้ำจะย้ายไปหาทางเข้าใหม่ที่ยังไม่ได้ปิด</p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>ดาดฟ้าปูกระเบื้อง — กับดักชื่อ "น้ำเดินใต้กระเบื้อง"</h2>
      <p>ตัวกระเบื้องเองน้ำผ่านไม่ได้ครับ ปัญหาอยู่ที่ร่องระหว่างแผ่น — <b>ยาแนวปูนทั่วไปคือฟองน้ำดีๆ นี่เอง</b> พอเสื่อม แตก หรือหลุดร่อน น้ำฝนทั้งผืนดาดฟ้าจะเลือกลงทางร่องพวกนี้ แล้วไปสะสมในชั้นปูนกาวใต้กระเบื้อง ไหลเดินตามความลาดเอียงจนกว่าจะเจอรอยร้าวหรือจุดอ่อนของพื้นปูนให้มุดลงไป</p>
      <figure><img src="/img/post/{slug}-path-th.webp" alt="หน้าตัดดาดฟ้าปูกระเบื้อง แสดงน้ำเข้าทางร่องยาแนวที่เสื่อม เดินในชั้นปูนกาวใต้กระเบื้อง แล้วลงผ่านรอยร้าวของพื้นไปหยดที่ฝ้าอีกจุดหนึ่งซึ่งห่างจากจุดน้ำเข้าหลายเมตร" loading="lazy" width="1200" height="900"><figcaption>เส้นทางเต็มๆ ของน้ำ: เข้าที่ร่องยาแนวจุดหนึ่ง — โผล่หยดอีกจุดหนึ่ง สองจุดห่างกันได้หลายเมตร</figcaption></figure>
      <p>ผลคือกับดักคลาสสิกของดาดฟ้ากระเบื้อง: เจ้าของบ้านเห็นน้ำหยดตรงไหน ก็ขึ้นไปทากันซึมตรงหัวเป๊ะๆ ของจุดนั้น — แล้วก็รั่วเหมือนเดิม เพราะ<b>จุดที่หยดไม่ใช่จุดที่น้ำเข้า</b> มันคือแค่ทางออกของน้ำที่เดินมาไกลแล้ว หลักการไล่หาจุดรั่วจริงเราเขียนแยกไว้ในเคส <a href="/post/finding-the-real-leak-point">หาจุดรั่วให้เจอก่อน แล้วค่อยทากันซึม</a> — อ่านคู่กันแล้วภาพจะครบ</p>
    </section>
    <section class="step">
      <h2><span class="n">04</span>Straight Talk — ทางที่จบที่สุดของกระเบื้อง คือเปลี่ยนยาแนว แต่เราจะไม่โกหกว่ามันง่าย</h2>
      <p>ในเชิงระบบ ทางแก้ที่ตรงต้นเหตุที่สุดของดาดฟ้ากระเบื้องมีทางเดียว: <b>เอายาแนวปูนที่เป็นฟองน้ำออก แล้วยาแนวใหม่ทุกร่องด้วย<a href="/epoxygrout">ยาแนวกันซึม Epoxy TileGrout</a></b> เนื้อ Epoxy ทึบน้ำ ไม่ดูดซึม — ปิดประตูน้ำเข้าที่ต้นทางเลย ไม่ต้องไปตามเช็ดปลายทาง ใครกลัวผสมพลาดมี<a href="/carbontilegrout">รุ่นปืนยิง Carbon</a> ที่ผสมเองที่ปลายหลอด</p>
      <p>แต่ตรงนี้ขอพูดแบบคนเคยลงมือจริง: <b>ความยากไม่ได้อยู่ที่ยาแนวใหม่ — อยู่ที่รื้อยาแนวเดิม</b> ยาแนวใหม่จะเกาะได้ต้องเปิดร่องเดิมออกจริง ไม่ใช่ขูดแค่ผิวหน้าแล้วอัดทับ ลองคิดภาพดาดฟ้า 40 ตร.ม. ปูกระเบื้อง 60×60 — ร่องยาแนวรวมกันยาว<b>ร่วมๆ 130 เมตร</b> ที่ต้องนั่งขูดหรือใช้เครื่องเจียรกรีดเปิดทีละร่อง กลางแดดดาดฟ้า ฝุ่นเต็มตัว นี่คืองานที่ทำให้คนส่วนใหญ่ถอยตั้งแต่ยังไม่เริ่ม และเราเข้าใจร้อยเปอร์เซ็นต์</p>
      <p>ใครถึกพอทำไหว นี่คือทางที่<b>ทำรอบเดียวแล้วจบจริง</b> — แลกเหงื่อกับการไม่ต้องกลับมาแตะดาดฟ้าอีกนาน แต่ถ้าอ่านย่อหน้าบนแล้วส่ายหัว ข้อถัดไปคือทางของคุณ</p>
    </section>
    <section class="step">
      <h2><span class="n">05</span>ทางที่คนส่วนใหญ่เลือก — เคลือบทับทั้งผืนด้วย PolyPro</h2>
      <p>ก่อนอื่นต้องเคลียร์ก่อนว่าทำไม<b>สีกันซึมทั่วไปทาทับกระเบื้องแล้วพัง</b>: ผิวเคลือบกระเบื้องทั้งลื่นทั้งไม่ดูดซึม ฟิล์มที่ออกแบบมาเกาะผิวปูนจะแค่ "วางอยู่บน" กระเบื้อง โดนแดดจัดสลับฝนไม่กี่รอบก็ลอกเป็นแผ่น — ปัญหาไม่ใช่ยี่ห้อไหนดีกว่ากัน ปัญหาคือเอาระบบผิดพื้นผิวมาใช้</p>
      <p><a href="/polypro">PolyPro</a> ถูกออกแบบมาปิดจุดนี้ตรงๆ: <b>ยึดเกาะได้จริงทั้งบนกระเบื้องเคลือบและคอนกรีต</b> บวกความทน UV กับการแช่น้ำถาวรที่ดาดฟ้าต้องการอยู่แล้ว — เคลือบทั้งผืนรอบเดียว ปิดทั้งหน้ากระเบื้องและร่องยาแนวพร้อมกัน น้ำไม่มีร่องให้เลือกลงอีก</p>
      <p>แต่ก่อนเปิดกระป๋อง มีเงื่อนไขบังคับสามข้อที่ห้ามข้าม: <b>ข้อแรก เคาะหากระเบื้องร่อน</b> — ไล่เคาะทั้งผืน เสียงกลวงคือกระเบื้องที่หลุดจากพื้นแล้ว ต้องจัดการก่อน เพราะจุดที่ขยับตัวได้จะฉีกฟิล์มที่ทาทับทีหลัง ทาปิดปัญหาไว้ใต้ฟิล์มคือระเบิดเวลา <b>ข้อสอง ร่องยาแนวที่แหว่งหรือเป็นโพรง เติมให้เต็มเสมอผิวก่อน</b> — ฟิล์มที่แขวนข้ามร่องว่างจะแตกตรงนั้นพอดี หลักเดียวกับที่เราผ่าให้ดูในเคส<a href="/post/why-bathroom-grout-leaks-recur">ห้องน้ำรั่วซ้ำ</a> <b>ข้อสาม แนวพื้นชนผนังกันตก</b> — จุดที่สองระนาบขยับไม่เท่ากัน อุดด้วย <a href="/patchpro">PatchPro</a> ให้จบก่อนเคลือบ รายละเอียดเต็มๆ อยู่ในเคส<a href="/post/wall-to-floor-joint-leak">มุมกำแพงชนพื้น</a></p>
    </section>
    <section class="step">
      <h2><span class="n">06</span>สรุปทั้งกระดาน — คำถามเดียว สองแผนงาน</h2>
      <figure><img src="/img/post/{slug}-decide-th.webp" alt="แผนผังตัดสินใจซ่อมดาดฟ้ารั่ว: ปูนเปลือยอุดรอยร้าวด้วย PatchPro แล้วเคลือบ PolyPro ส่วนปูกระเบื้องเช็คกระเบื้องร่อนก่อน แล้วเลือกระหว่างเปลี่ยนยาแนวเป็น Epoxy หรือเคลือบทับด้วย PolyPro" loading="lazy" width="1200" height="900"><figcaption>ทั้งเคสย่อเหลือภาพเดียว — เซฟเก็บไว้เปิดดูวันขึ้นดาดฟ้าได้เลย</figcaption></figure>
      <p>ถึงตรงนี้น่าจะเห็นแล้วว่าคำถาม "ปูนหรือกระเบื้อง" ไม่ใช่การถามให้ยุ่งยาก และไม่ใช่ลูกเล่นขายของแพงขึ้น — มันคือการ<b>วินิจฉัยก่อนจ่ายยา</b> เพราะคำตอบเปลี่ยนตั้งแต่จุดที่ต้องหา วิธีเตรียมผิว ไปจนถึงระบบที่ใช้</p>
      <p>ไม่แน่ใจว่าดาดฟ้าตัวเองเข้าเคสไหน หรือเจอทั้งสองอย่างผสมกัน — ถ่ายรูปหน้างานส่งมาทางแชทเพจได้เลย บอกแค่ว่าปูนหรือกระเบื้อง เราช่วยวางแผนให้ฟรีก่อนตัดสินใจซื้อ เพราะงานกันซึมที่ดีที่สุด คืองานที่ทำครั้งเดียวแล้วไม่ต้องคุยกันอีกนานๆ</p>
    </section>
  </article>
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/polypro">PolyPro</a><a href="/siliconepro">SiliconePro</a><a href="/patchpro">PatchPro</a><a href="/epoxygrout">ยาแนว Epoxy TileGrout</a><a href="/carbontilegrout">รุ่นปืนยิง Carbon</a></div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
""".replace("{slug}", SLUG)

# ─────────────────────────────────────────── EN
EN_TITLE = "Leaking Rooftop — Why We Always Ask First: Bare Concrete, or Tiled?"
EN_DESC = ("One question decides whether your rooftop waterproofing lasts years or peels in months. "
           "Bare concrete: water enters at cracks — seal with PatchPro, coat with PolyPro. "
           "Tiled: water travels under the tiles, and the drip point is never the entry point. "
           "The definitive fix is re-grouting with Epoxy — but tearing out old grout is brutal work. Full story inside.")
EN_EYEBROW = "Case Study · Tips / Knowledge"
EN_META = "Published Aug 2026 · by the LucernaPro team"

EN_BODY = """  <article>
    <p>Every day a message like this lands in our page chat: <b>"My rooftop is leaking, water's dripping through the ceiling — which product do I need?"</b> And every time, our first reply is the same. Not a product name. Not a price. A question: <b>is your deck bare concrete, or tiled?</b></p>
    <p>You might be thinking: why does it matter? A leak is a leak. Except it isn't — on these two surfaces, water <b>enters differently, travels differently, and the repair plan that actually works is different</b>. Get the answer wrong at step one and you pay twice: once for the materials and labour that peel off, and again to strip it all before doing it properly.</p>
    <p>So here's the whole story in one sitting — read to the end and you'll know exactly which path your own rooftop is on.</p>
    <figure class="hero"><img src="/img/post/{slug}-hero.webp" alt="A fully tiled residential rooftop deck with grout lines visible across the floor, a wooden railing, potted plants and a small seating set" width="1600" height="1200"><figcaption>A good-looking tiled deck exactly like this is the hardest kind to trace once it leaks — because the entry is the grout line everyone looks straight past</figcaption></figure>
    <section class="step">
      <h2><span class="n">01</span>Same symptom — different disease</h2>
      <p>Take two customers who messaged us in the same week. Identical symptoms: water dripping from the top-floor ceiling, a yellow ring spreading across it, clearly worse in the rainy season.</p>
      <p><b>Customer one — bare concrete deck:</b> up on the roof we found hairline cracks spread across the slab, plus a separated joint at the base of the parapet wall. Rainwater goes straight down through them. The drip below sits close to the entry above — easy to find, easy to point at, easy to fix at the source.</p>
      <p><b>Customer two — tiled deck:</b> the tile faces looked fine, not a crack in sight. But the grout had gone — hard, brittle, crumbling in stretches. Water slips in through the grout lines, then <b>travels along under the tiles</b> with the slope, until it finds a crack in the slab on the far side to drop through. The drip inside the house was metres away from where the water actually got in.</p>
      <figure><img src="/img/post/{slug}-compare-en.webp" alt="Comparison of a bare concrete rooftop where water enters through hairline cracks versus a tiled rooftop where water enters through grout lines and travels under the tiles" loading="lazy" width="1200" height="900"><figcaption>Two surfaces, two leak mechanisms — this one question is where the right game plan starts</figcaption></figure>
      <p>Same symptom, completely different mechanism — and that's the first reason we ask. Misdiagnose at the start, and no medicine works, however good it is.</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>Bare concrete deck — the straightforward game: seal first, then coat the lot</h2>
      <p>On bare concrete the entry points are clear: <b>hairline cracks, the parapet-wall joint, and around the drains</b>. The work order is fixed and non-negotiable — hunt every one of them down first, then fill flush with <a href="/en/patchpro">PatchPro</a>. Same principle we hammer in <a href="/en/post/why-coating-over-cracks-fails">our crack case study</a>: every waterproofing product is a thin film, not a gap filler. Coat straight over a crack and you're just waiting for the film to tear along the same line.</p>
      <p>Let the filler cure per the manual, then coat the whole deck with <a href="/en/polypro">PolyPro</a> — our top-of-the-line Polyurea Gen3, and the one we push hardest for rooftops specifically. A rooftop is the most hostile arena waterproofing ever plays in: <b>full UV all day, every day, plus standing water after every storm</b>. PolyPro is UV-stable, doesn't yellow, handles permanent immersion, and lays down a far thicker film than ordinary brush-on waterproofing. It answers every question a rooftop asks.</p>
      <p>Budget not stretching to the top shelf? No need to force it — on bare concrete we happily recommend a starter: <a href="/en/siliconepro">SiliconePro</a>, a single-component silicone waterproofer you open and roll straight away, no mixing, comfortable with standing water. The trade is service life: around 5 years bare, stretching to 8–10 with a fibreglass mesh layer — and for an ordinary house rooftop with no extreme demands, that does the whole job.</p>
      <p>You can also scale the coat itself to the budget: <b>spot-coat the wounds only</b> — just the sealed crack lines, the parapet joint and around the drains. A smart opening move: close the heaviest door with the least money, wait for real rain, check the result, then decide on the next investment. Or <b>coat the whole deck and be certain</b> — one round, done, no wondering whether the water will find a new door you left open.</p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>Tiled deck — the trap called "water travels under the tiles"</h2>
      <p>The tiles themselves are watertight. The problem is the lines between them — <b>ordinary cement grout is basically a sponge</b>. Once it ages, cracks or crumbles, the rain landing on the entire deck funnels down through those lines, pools in the adhesive bed under the tiles, and travels along the slope until it finds a crack or weak spot in the slab to drop through.</p>
      <figure><img src="/img/post/{slug}-path-en.webp" alt="Cross-section of a tiled rooftop showing water entering at a failed grout line, travelling through the adhesive bed under the tiles, then dropping through a slab crack to drip from the ceiling metres away from the entry point" loading="lazy" width="1200" height="900"><figcaption>The water's full journey: in at one grout line — out at a drip point metres away</figcaption></figure>
      <p>Which sets up the classic tiled-deck trap: the owner sees where the drip is, climbs up, and coats the deck directly above that exact spot — and it leaks exactly like before, because <b>the drip point is not the entry point</b>. It's just the exit of water that has already travelled a long way. We wrote up the full method for tracking a real leak in <a href="/en/post/finding-the-real-leak-point">Find the Real Leak Point First</a> — read the two together and the picture is complete.</p>
    </section>
    <section class="step">
      <h2><span class="n">04</span>Straight talk — the definitive tiled-deck fix is re-grouting, and we won't pretend it's easy</h2>
      <p>System-wise, there is exactly one fix that attacks the root cause: <b>take out the sponge-like cement grout and re-grout every line with <a href="/en/epoxygrout">Epoxy TileGrout</a></b> — dense, non-absorbent, watertight. It shuts the door where the water comes in, instead of mopping up where it comes out. Worried about mixing it wrong on your first go? The <a href="/en/carbontilegrout">Carbon gun-cartridge version</a> mixes itself at the nozzle.</p>
      <p>But let us say this as people who have actually done the work: <b>the hard part isn't the new grout — it's removing the old grout</b>. New grout only bonds if the old line is genuinely opened up, not surface-scratched and packed over. Picture a 40 m² deck laid with 60×60 tiles — that's <b>around 130 running metres</b> of grout line to scrape or grind open, one line at a time, in full rooftop sun, covered in dust. This is the job that makes most people walk away before starting, and honestly, we get it.</p>
      <p>If you've got the grit, this is the route that is <b>done once and genuinely finished</b> — sweat traded for not touching that rooftop again for a long time. If you read that paragraph and shook your head, the next section is your route.</p>
    </section>
    <section class="step">
      <h2><span class="n">05</span>What most people choose — coat the whole deck with PolyPro</h2>
      <p>First, let's be clear about why <b>ordinary waterproofing paint fails on tile</b>: a glazed tile surface is slick and non-absorbent, so a film designed to grip porous concrete just sits on top of it. A few rounds of harsh sun and rain and it peels off in sheets. The problem was never which brand is better — it's using a system built for the wrong surface.</p>
      <p><a href="/en/polypro">PolyPro</a> was designed to close exactly that gap: it <b>genuinely bonds to both glazed tile and concrete</b>, on top of the UV resistance and permanent-immersion tolerance a rooftop demands anyway. One coat campaign over the whole deck seals tile faces and grout lines together — the water runs out of doors to pick.</p>
      <p>Before you open the can, though, three non-negotiable conditions: <b>One — tap-test for hollow tiles.</b> Work across the whole deck; a hollow sound means the tile has already let go of the slab. Deal with it first, because anything that moves will tear the film coated over it. Coating over a problem just sets a timer on it. <b>Two — fill any chipped or hollow grout lines flush before coating.</b> Film suspended over an empty groove cracks precisely there — the same principle we dissected in <a href="/en/post/why-bathroom-grout-leaks-recur">the recurring bathroom leak case</a>. <b>Three — the floor-to-parapet joint.</b> Two planes that move at different rates: seal it with <a href="/en/patchpro">PatchPro</a> before coating. The full breakdown lives in <a href="/en/post/wall-to-floor-joint-leak">the wall-meets-floor case</a>.</p>
    </section>
    <section class="step">
      <h2><span class="n">06</span>The whole board — one question, two game plans</h2>
      <figure><img src="/img/post/{slug}-decide-en.webp" alt="Decision map for a leaking rooftop: bare concrete gets cracks sealed with PatchPro then a full PolyPro coat, while a tiled deck gets tap-tested first, then either re-grouted with Epoxy or coated over with PolyPro" loading="lazy" width="1200" height="900"><figcaption>The entire case in one image — save it for the day you climb up there</figcaption></figure>
      <p>By now it should be clear that "concrete or tiled?" isn't us being difficult, and it isn't a trick to sell you something pricier — it's a <b>diagnosis before the prescription</b>, because the answer changes everything from where to look, to how to prep, to which system goes down.</p>
      <p>Not sure which case your rooftop is — or facing a mix of both? Snap some photos and send them to our page chat. Just tell us: concrete or tiled. We'll help you plan it for free before you spend a baht — because the best waterproofing job is the one you do once and then don't have to talk about for a very long time.</p>
    </section>
  </article>
  <div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/polypro">PolyPro</a><a href="/en/siliconepro">SiliconePro</a><a href="/en/patchpro">PatchPro</a><a href="/en/epoxygrout">Epoxy TileGrout</a><a href="/en/carbontilegrout">Carbon gun-cartridge</a></div>
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
               TH_TITLE, TH_DESC, TH_EYEBROW, TH_TITLE, TH_META, TH_BODY, f"{SLUG}-hero.webp")
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"),
               os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN_TITLE, EN_DESC, EN_EYEBROW, EN_TITLE, EN_META, EN_BODY, f"{SLUG}-hero.webp")
