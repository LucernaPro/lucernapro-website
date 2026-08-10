# -*- coding: utf-8 -*-
"""
build_pitchroof_post.py — สร้างโพสต์ cpac-metal-sheet-roof-leaks (TH+EN)
ด้วยวิธี chrome-transplant จากโพสต์ rooftop-concrete-or-tile
รัน: python3 tools/build_pitchroof_post.py (จาก root ของ repo)
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "rooftop-concrete-or-tile"
SLUG = "cpac-metal-sheet-roof-leaks"

# ─────────────────────────────────────────── TH
TH_TITLE = "หลังคากระเบื้อง CPAC กับเมทัลชีทรั่ว — แผนที่จุดตาย และทำไมต้องเริ่มที่ SpackleFlex"
TH_DESC = ("หลังคาลาดเอียงไม่รั่วทั้งผืน มันรั่วเป็นจุด — พาไล่แผนที่จุดตายของหลังคากระเบื้องคอนกรีต (CPAC): "
           "ปูนครอบสันร่อน กระเบื้องแตกจากการเหยียบ ตะเข้ราง / และเมทัลชีท: หัวสกรูยางเสื่อม รอยซ้อนแผ่น "
           "ทำไมงานหลังคาต้องเริ่มที่โป๊วรอยต่อรอยแตกด้วย SpackleFlex ก่อนเสมอ พร้อมคอมโบทับหน้าเลือกตามงบ")
TH_EYEBROW = "Case Study · เทคนิค / ความรู้"
TH_META = "เผยแพร่ ส.ค. 2026 · โดยทีมงาน LucernaPro"

TH_BODY = """  <article>
    <p>เคสที่แล้วเราคุยเรื่อง<a href="/post/rooftop-concrete-or-tile">ดาดฟ้า</a>กันไป คราวนี้ขยับขึ้นไปอีกชั้น: <b>หลังคาลาดเอียง</b> — กระเบื้องคอนกรีตอย่าง CPAC และเมทัลชีท สองวัสดุที่คลุมบ้านคนไทยมากที่สุด และเป็นต้นทางของข้อความ "หลังคารั่ว ซ่อมยังไงดี" ที่เข้ามาในแชทเพจแทบทุกวันช่วงหน้าฝน</p>
    <p>ข่าวดีที่หลายคนไม่รู้: หลังคาลาดเอียง<b>เกือบไม่เคยรั่วทั้งผืน</b> ความลาดเอียงรีดน้ำฝนทิ้งเร็วมาก น้ำไม่มีเวลาขังแช่แบบดาดฟ้า — มันรั่วเป็น <b>"จุด"</b> ตรงช่องที่น้ำผ่านได้: รอยแตก รอยต่อ รูสกรู แนวครอบ ดังนั้นเกมของหลังคาจึงไม่ใช่การทากันซึมทั้งผืนตั้งแต่แรก แต่คือ<b>ไล่หาช่องพวกนี้ให้ครบ แล้วอุดให้ถูกวิธี</b></p>
    <figure class="hero"><img src="/img/post/{slug}-hero.webp" alt="หลังคาเมทัลชีทความลาดเอียงต่ำของบ้านไทย เห็นแถวหัวสกรูเริ่มมีสนิมและรอยซ้อนแผ่นชัดเจนกลางผืน" width="1600" height="1200"><figcaption>หลังคาเมทัลชีทเอียงน้อยแบบนี้คือด่านพิเศษของเรื่องนี้ — น้ำไหลออกช้า รอยซ้อนแผ่นและหัวสกรูทุกตัวเลยโดนทดสอบหนักกว่าหลังคาชัน (มีวิธีเล่นเฉพาะในข้อ 04)</figcaption></figure>
    <section class="step">
      <h2><span class="n">01</span>ก่อนขึ้นไปไล่หา — กติกาการเหยียบหลังคา</h2>
      <p>ขอเบรกไว้ตรงนี้ก่อนหนึ่งย่อหน้า เพราะเราเจอบ่อยจนต้องพูด: ลูกค้าจำนวนไม่น้อยขึ้นไปซ่อมรอยรั่วหนึ่งจุด แล้วลงมาพร้อมรอยแตกใหม่อีกสามจุด — <b>กระเบื้องคอนกรีตรับน้ำหนักได้เฉพาะช่วงที่พาดอยู่บนระแนง</b> เหยียบกลางท้องแผ่นเมื่อไหร่มีสิทธิ์ร้าวทันที ให้เหยียบช่วงหัวแผ่นที่ซ้อนกัน (แนวเดียวกับระแนงข้างใต้) เดินช้าๆ ถ่ายน้ำหนักเบาๆ ส่วนเมทัลชีทให้เหยียบตามแนวแป (สังเกตแนวหัวสกรู) ไม่เหยียบกลางลอนระหว่างแป — และถ้าหลังคาชันหรือไม่มั่นใจ เรียกช่างเถอะครับ ค่าแรงถูกกว่าค่าโรงพยาบาลเสมอ</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>แผนที่จุดตาย — หลังคากระเบื้อง CPAC</h2>
      <p>ตัวกระเบื้องคอนกรีตเองทึบน้ำและอายุยืนมาก จุดที่พังจริงคือ "รอบๆ" มัน: <b>หนึ่ง — ปูนครอบสันและครอบข้าง</b> ปูนที่ยึดครอบไว้แตกลายงาและร่อนหลุดตามอายุ น้ำเข้าใต้ครอบแล้วไหลไปตามแปโผล่ในบ้านคนละจุด <b>สอง — กระเบื้องแตกร้าว</b> ที่สาเหตุอันดับหนึ่งคือการขึ้นไปเหยียบผิดจุดตามข้อ 01 ร้าวเส้นเดียวบางๆ ก็พอให้น้ำผ่านทุกครั้งที่ฝนตก <b>สาม — ตะเข้ราง (Valley)</b> จุดที่หลังคาสองผืนเทน้ำมารวมกัน ทั้งรอยต่อราง สนิม และใบไม้อุดตันให้น้ำเอ่อล้นข้ามขอบ <b>สี่ — แนวหลังคาชนผนัง</b> แผ่นปิด (Flashing) เผยอหรือยาแนวเดิมเสื่อม ฝนสาดเมื่อไหร่น้ำย้อนเข้าตามแนวชนเมื่อนั้น</p>
      <figure><img src="/img/post/{slug}-cpac-th.webp" alt="แผนผังผืนหลังคากระเบื้อง CPAC ชี้จุดตายสี่จุด: ปูนครอบสันแตกร่อน กระเบื้องแตกร้าวจากการเหยียบ ตะเข้ราง และแนวหลังคาชนผนัง" loading="lazy" width="1200" height="900"><figcaption>ไล่เช็คสี่จุดนี้ให้ครบก่อน — ส่วนใหญ่เจอตัวการภายในรอบเดียว</figcaption></figure>
      <p>เคล็ดจากหน้างาน: จุดที่เห็นคราบน้ำบนฝ้า ให้มองย้อนขึ้นไป<b>ตามแนวลาดด้านบน</b>ของจุดนั้นเสมอ เพราะน้ำที่ลอดกระเบื้องจะไหลตามแปลงมาก่อนหยด — หลักเดียวกับที่เราเขียนไว้ในเคส<a href="/post/finding-the-real-leak-point">หาจุดรั่วให้เจอก่อน</a></p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>แผนที่จุดตาย — หลังคาเมทัลชีท</h2>
      <p>เมทัลชีทตัวแผ่นคือเหล็กทั้งแผ่น น้ำผ่านไม่ได้แน่นอน — มันรั่วตรงทุกจุดที่ "ไม่ใช่แผ่น": <b>หนึ่ง — หัวสกรู</b> ตัวการอันดับหนึ่งแบบไม่มีคู่แข่ง ยางรองสกรูโดนแดดจนกรอบแตกตามอายุ หรือถูกขันเบี้ยว/แน่นเกินจนยางบี้เสียรูปตั้งแต่วันติดตั้ง หลังคาหนึ่งผืนมีสกรูหลายร้อยตัว และทุกตัวคือผู้ต้องสงสัย <b>สอง — รอยซ้อนแผ่น (Overlap)</b> แผ่นเหล็กยืดหดตามอุณหภูมิทั้งวัน รอยซ้อนจึงขยับตลอดเวลา ยิ่งหลังคาลาดน้อยยิ่งเสี่ยง เพราะลมแรงๆ ดันน้ำย้อนขึ้นตามรอยซ้อนได้ <b>สาม — รอบท่อและช่องเจาะ</b> ทุกรูที่เจาะทะลุหลังคาคือประตูถาวร ยาแนวเดิมที่ปิดไว้โดนแดดตรงจนกรอบเร็วกว่าจุดอื่น <b>สี่ — สนิมรูพรุน</b> เริ่มจากรอยขูดผิวเคลือบเล็กๆ ลามเป็นรูเข็ม</p>
      <figure><img src="/img/post/{slug}-metal-th.webp" alt="แผนผังผืนหลังคาเมทัลชีทชี้จุดตายสี่จุด: หัวสกรูยางรองเสื่อม รอยซ้อนแผ่น รอบท่อเจาะทะลุหลังคา และสนิมกินจนเป็นรูพรุน" loading="lazy" width="1200" height="900"><figcaption>แผ่นยังเงาสวยแค่ไหนก็รั่วได้ — เพราะจุดตายทั้งสี่ไม่ใช่ตัวแผ่น</figcaption></figure>
      <p><b>Straight Talk เรื่องสนิม:</b> รูเข็มเล็กๆ โป๊วปิดได้และอยู่จริง แต่แผ่นที่สนิมกินจนเนื้อเหล็กบางยุ่ยเป็นบริเวณกว้าง โป๊วคือการซื้อเวลา ไม่ใช่การซ่อม — เคสแบบนั้นเปลี่ยนแผ่นครับ เราขายเคมีก็จริง แต่จะไม่ขายให้กับงานที่รู้อยู่แล้วว่าไม่รอด</p>
    </section>
    <section class="step">
      <h2><span class="n">04</span>ด่านพิเศษ — หลังคาเมทัลชีทเอียงน้อย ต้องเล่นอีกเกม</h2>
      <p>หลังคาแบบในภาพเปิดเรื่องคือโจทย์ที่เราอยากแยกออกมาพูดตรงๆ: <b>ความลาดเอียงต่ำ</b> น้ำไหลออกช้า ฝนหนักๆ น้ำเอ่อเป็นแผ่นบนผืนหลังคาชั่วขณะ ลมกระโชกดันน้ำย้อนขึ้นตามรอยซ้อนได้สบาย — จุดตายทุกจุดจากข้อ 03 ยังอยู่ครบ แต่โดนทดสอบหนักขึ้นหลายเท่า การอุดเป็นจุดๆ แบบหลังคาชันจึงมักเอาไม่อยู่</p>
      <p>เกมของหลังคาเอียงน้อยคือ <b>เลิกอุดเป็นจุด — พอกเป็นแนวเต็มเส้น</b>: ไล่ปาด <a href="/spackleflex">SpackleFlex</a> ทับแนวรอยซ้อนแผ่น<b>เต็มความยาวทุกเส้น</b> ไม่ใช่เฉพาะช่วงที่เห็นคราบ และครอบหัวสกรู<b>ทุกตัว</b>ในโซนลาดน้อย เพราะบนผืนที่น้ำเอ่อได้ สกรูที่ยังไม่รั่ววันนี้คือสกรูที่รอคิวอยู่</p>
      <p>ส่วนใครอยากได้ทางที่แน่นกว่านั้น นี่คือสุดยอดของงานล็อกรอยต่อในสายเรา: <a href="/modernfiberglass">Modern Fiberglass</a> — ทาน้ำยา Advanced Polymer ส่วนผสมเดียว วาง<b>ผ้าใยแก้ว Woven คร่อมแนวรอยต่อ</b> แล้วทาน้ำยาทับให้ชุ่มทั้งผืนผ้า พอเซ็ตตัว รอยต่อทั้งเส้นจะถูกล็อกด้วยแผ่นไฟเบอร์เสริมแรงที่เหนียวยืดหยุ่น ไม่เปราะแตก ขยับตามแผ่นเหล็กได้ จากนั้นปิดหน้าด้วย <a href="/siliconepro">SiliconePro</a> ทาทับทั้งแนวกัน UV และได้ชั้นกันซึมเสริมอีกชั้น — สูตรเดียวกับที่เราเขียนไว้บนหน้า Modern Fiberglass ว่าเป็นสูตรสำเร็จของช่างสำหรับงานหลังคาและรอยต่อโหดๆ และตรงกับตัวเลขบนหน้า SiliconePro พอดี: เสริมผ้าไฟเบอร์กลาสแล้วอายุงานยืดจากราว 5 ปี เป็น 8–10 ปี</p>
      <p><b>วิธีทำทีละขั้น:</b> เริ่มจากเตรียมแนวให้พร้อม — เช็ดฝุ่น คราบน้ำมัน และสนิมที่หลุดร่อนออกให้หมด รอผิวแห้งสนิท จากนั้นทาน้ำยา Modern Fiberglass รองพื้นตามแนวรอยต่อหนึ่งรอบ ให้กว้างกว่าหน้าผ้าเล็กน้อย วางผ้าใยแก้ว Woven หน้ากว้างราว 6 นิ้วคร่อมแนวรอยต่อ ใช้แปรงกดรีดให้ผ้าแนบตามรูปลอนทุกสันทุกร่อง แล้วทาน้ำยาทับให้ชุ่มทั่วทั้งผืน — สังเกตง่ายมาก: ผ้าที่อิ่มน้ำยาแล้วจะเปลี่ยนจากสีขาวด้านเป็นใสจนมองเห็นลอนเหล็กข้างใต้ จุดไหนยังขาวอยู่คือยังทาไม่ถึง</p>
      <figure><img src="/img/post/{slug}-mf-step1.webp" alt="มือใส่ถุงมือใช้แปรงทาน้ำยา Modern Fiberglass สีใสอมเหลืองลงบนผ้าใยแก้ว Woven หน้ากว้าง 6 นิ้วที่วางพาดแนวรอยต่อเมทัลชีท ฝั่งที่ทาแล้วผ้าชุ่มจนใส ฝั่งที่ยังไม่ทายังเป็นสีขาวด้าน" loading="lazy" width="1600" height="1200"><figcaption>จังหวะสำคัญของขั้นนี้: ทาน้ำยาให้ผ้า Woven ชุ่มจน "ใส" — ฝั่งที่ยังขาวด้านคือยังไม่อิ่มน้ำยา ไล่ทาจนใสทั้งผืนแล้วค่อยถือว่าจบ รอเซ็ตตัวก่อนปิดหน้าด้วย SiliconePro</figcaption></figure>
      <p>สองจุดที่ชี้ขาดว่างานจะอยู่หรือไม่อยู่: <b>หนึ่ง ผ้าต้องแนบตามลอน</b> — แนวที่ทำเสร็จแล้วต้องยังเห็นรูปลอนของแผ่นเหล็กชัดๆ ทะลุผ้าออกมา ถ้าผ้าขึงตึงข้ามร่องลอนตรงไหน ใต้ผ้าตรงนั้นคือโพรงให้น้ำเดินในอนาคต กดรีดให้แนบตั้งแต่ตอนน้ำยายังเปียก <b>สอง ห้ามรีบ</b> — ปล่อยให้ผ้าที่อิ่มน้ำยาเซ็ตตัวเต็มที่ก่อน (น้ำยาตัวนี้แห้งช้าโดยตั้งใจ ไม่ต่ำกว่า 6 ชั่วโมง) ผ้าที่เซ็ตแล้วจะเป็นสีเหลืองใสสม่ำเสมอและแห้งด้าน แตะไม่ติดมือ ถึงตอนนั้นค่อยขึ้นชั้นถัดไป ห้ามทาทับตอนผ้ายังเปียกเด็ดขาด</p>
      <p>ขั้นสุดท้าย ทา <a href="/siliconepro">SiliconePro</a> ทับตลอดทั้งแนว ให้เนื้อสีคลุมเลยขอบผ้าออกไปทั้งสองข้าง เก็บขอบให้เรียบต่อเนื่องเป็นเนื้อเดียวกับแผ่นหลังคา — ชั้นนี้ทำสองหน้าที่พร้อมกัน: บังแดดให้ชั้นไฟเบอร์ข้างใต้ และเป็นชั้นกันซึมเสริมของทั้งแนว</p>
      <figure><img src="/img/post/{slug}-mf-step2.webp" alt="ผ้าใยแก้วที่อิ่มน้ำยาจนเป็นสีเหลืองใสและเซ็ตตัวแล้วบนแนวรอยต่อเมทัลชีท กำลังถูกทาทับด้วยกันซึมสีเทาเข้ม ส่วนที่ทาเสร็จแล้วยังเห็นรูปลอนเหล็กชัดเจน" loading="lazy" width="1600" height="1200"><figcaption>ขั้นปิดงาน: ผ้าที่เซ็ตตัวแล้วเป็นสีเหลืองใสทั้งผืน ทา SiliconePro ทับให้คลุมเลยขอบผ้า — สังเกตว่าแนวที่จบแล้วยังเห็นรูปลอนชัด นั่นคือสัญญาณว่าผ้าแนบสนิทกับแผ่นจริง</figcaption></figure>
      <p><b>Straight Talk ที่ต้องพูดให้ครบ:</b> หลังคาเอียงน้อยที่รั่วกระจายหลายแนว ซ่อมแล้วย้ายจุดรั่วไปเรื่อยๆ หรือแผ่นเสื่อมสภาพทั้งผืน — บางเคสคำตอบที่คุ้มที่สุด<b>ไม่ใช่เคมี</b> แต่คือเรียกช่างหลังคามาทำ<b>หลังคาซ้อน</b> (มุงแผ่นใหม่ครอบทับโครงเดิม) จ่ายหนักรอบเดียวแต่ได้ผืนใหม่ทั้งหลัง เราขายเคมีก็จริง แต่จะไม่เชียร์ให้คุณไล่อุดงานที่รู้อยู่แล้วว่าสู้ต้นเหตุไม่ไหว — ค่าหลังคาซ้อนหนึ่งรอบ ถูกกว่าค่าปีนขึ้นไปซ่อมซ้ำทุกปีแน่นอน</p>
    </section>
    <section class="step">
      <h2><span class="n">05</span>ทำไมทุกจุดข้างบนถึงเริ่มที่ SpackleFlex</h2>
      <p>สังเกตไหมครับว่าจุดตายเกือบทั้งหมด — ปูนครอบ รอยร้าว รอยซ้อน หัวสกรู แนวชนผนัง — มีธรรมชาติร่วมกันอย่างหนึ่ง: <b>มันขยับ</b> หลังคาโดนแดดเปรี้ยงตอนบ่ายแล้วเจอฝนเย็นตอนค่ำ วัสดุยืดหดสวนกันทุกวัน วัสดุอุดที่แข็งตายจะแตกตามภายในไม่กี่รอบร้อน-เย็น และซิลิโคนใสทั่วไปที่หลายบ้านชอบใช้ ก็แพ้ UV กลางแจ้งจนชอล์กร่อนเร็วกว่าที่คิด</p>
      <p><a href="/spackleflex">SpackleFlex</a> เกิดมาเพื่อสนามนี้ตรงๆ: <b>เคมีโป๊วชนิดยืดหยุ่น</b>ที่ขยับตามหลังคาได้โดยไม่ฉีก <b>พร้อมใช้ไม่ต้องผสม</b> เปิดมาปาดได้เลยบนหลังคา (สำคัญมาก — ไม่มีใครอยากชั่งตวงสองส่วนผสมบนสันหลังคา) ทนกลางแจ้งกว่าซิลิโคนทั่วไปด้วย UV Stabilization ในตัว และผ่านทดสอบแช่น้ำต่อเนื่องหลายเดือน — ใช้ได้ทั้งปาดแนวปูนครอบที่แตกลายงา อุดรอยร้าวกระเบื้อง ครอบหัวสกรูทีละตัว ยิงแนวรอยซ้อนแผ่น และเก็บรอบท่อเจาะ</p>
      <p>สองข้อแฟร์ๆ ก่อนลงมือ: <b>ปูนครอบที่ร่อนหลุดเป็นก้อนใหญ่</b> ต้องฉาบปูนยึดครอบกลับให้แน่นก่อน แล้วค่อยใช้ SpackleFlex กันรอยแตกลายงา — ตัวโป๊วไม่ใช่ปูนโครงสร้าง / <b>กระเบื้องที่แตกหักทั้งแผ่น</b> ถ้าหาแผ่นทดแทนได้ เปลี่ยนแผ่นคือทางที่ถูกกว่าและจบกว่า โป๊วเหมาะกับรอยร้าวและแผ่นที่ถอดเปลี่ยนไม่ได้แล้ว</p>
      <p>และ Straight Talk ข้อที่เราย้ำกับลูกค้าทุกราย: <b>ค่าเคมีไม่ใช่ต้นทุนแพงของงานหลังคา — ค่าแรงกับความเสี่ยงตอนปีนขึ้นไปต่างหาก</b> ฉะนั้นขึ้นไปรอบเดียว ไล่เก็บให้ครบทุกจุดตามแผนที่ข้อ 02–04 อย่าอุดแค่จุดที่คิดว่าใช่จุดเดียวแล้วลงมารอลุ้น เพราะถ้าพลาด เท่ากับจ่ายค่าปีนอีกรอบเต็มๆ</p>
    </section>
    <section class="step">
      <h2><span class="n">06</span>จบแค่โป๊ว หรือไปต่อ — คอมโบทับหน้าเลือกตามงบ</h2>
      <p>หลังคาลาดเอียงส่วนใหญ่ <b>จบที่โป๊วครบทุกจุดนั่นแหละครับ</b> ไม่ต้องเคลือบทั้งผืนเหมือนดาดฟ้า — แต่ถ้าอยากรีดอายุงานให้สุดทาง หรือหลังคาอายุมากมีจุดเสี่ยงกระจายทั่ว สูตรคอมโบของเราคือ: โป๊วเสร็จ<b>รอ 6 ชั่วโมง</b> แล้วทากันซึมทับแนวที่โป๊วอีกชั้น สายประหยัดใช้ <a href="/siliconepro">SiliconePro</a> ส่วนผสมเดียวเปิดฝาทาได้เลย สายจัดเต็มใช้ <a href="/exotic">Exotic</a> — Polyurea ส่วนผสมเดียวที่เราเรียกว่าโคตรคอมโบสำหรับงานหลังคา เพราะเกรดตัวท็อปแต่ตัดขั้นตอนผสมทิ้ง เปิดฝาทาบนหลังคาได้เลย</p>
      <p>ส่วนบ้านเมทัลชีทที่บ่นเรื่องร้อนพอๆ กับเรื่องรั่ว มีทางยิงนกสองตัว: <a href="/heatshield">HeatShield</a> กันซึมพร้อมลดความร้อนสูตรน้ำ ทาได้ทั้งเมทัลชีท กระเบื้อง และคอนกรีต ค่าสะท้อนแดด TSR เกิน 95% (ทดสอบโดยสำนักวิจัย มจธ.) ลดอุณหภูมิผิวหลังคาได้ 5°C ขึ้นไป — โป๊วจุดตายด้วย SpackleFlex ให้ครบก่อน แล้วเคลือบ HeatShield ทั้งผืน ได้ทั้งกันซึมเสริมและบ้านที่เย็นลงในรอบเดียว</p>
      <p>อีกจุดที่มักรั่วพร้อมหลังคาแต่คนละตำแหน่ง: <b>รางน้ำ</b> — ถ้าคราบน้ำอยู่แนวชายคา ไปอ่านเคส<a href="/post/metal-gutter-seam-repair">ซ่อมรอยต่อรางน้ำ</a>ที่เราเขียนแยกไว้ได้เลย</p>
    </section>
    <section class="step">
      <h2><span class="n">07</span>สรุป — หลังคาไม่ใช่ดาดฟ้า อย่าใช้แผนเดียวกัน</h2>
      <figure><img src="/img/post/{slug}-map-th.webp" alt="แผนที่จุดตายของหลังคากระเบื้องคอนกรีต CPAC (ปูนครอบสัน กระเบื้องแตก ตะเข้ราง แนวชนผนัง) และหลังคาเมทัลชีท (หัวสกรู รอยซ้อนแผ่น รอบท่อเจาะ สนิมรูพรุน)" loading="lazy" width="1200" height="900"><figcaption>สองวัสดุ สองแผนที่จุดตาย — เซฟภาพนี้ไว้เปิดดูตอนขึ้นหลังคาได้เลย</figcaption></figure>
      <p>ดาดฟ้าเรียบ = น้ำขังแช่ ต้องคิดเรื่องฟิล์มทั้งผืน / หลังคาลาดเอียง = น้ำไหลทิ้งเร็ว ต้องคิดเรื่อง "จุด" — ไล่แผนที่จุดตายให้ครบ อุดด้วยตัวที่ยืดหยุ่นและทนแดดจริงอย่าง <a href="/spackleflex">SpackleFlex</a> แล้วค่อยตัดสินใจว่าจะเสริมคอมโบทับหน้าหรือไม่ตามงบและอายุหลังคา</p>
      <p>ไม่แน่ใจว่าหลังคาบ้านคุณตัวการคือจุดไหน — ถ่ายรูปมุมที่สงสัยกับคราบบนฝ้าส่งมาทางแชทเพจได้เลย บอกด้วยว่ากระเบื้องหรือเมทัลชีท เราช่วยชี้เป้าให้ฟรีก่อนซื้อ จะได้ปีนขึ้นไปรอบเดียวแล้วจบ</p>
    </section>
  </article>
  <div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/spackleflex">SpackleFlex</a><a href="/modernfiberglass">Modern Fiberglass</a><a href="/siliconepro">SiliconePro</a><a href="/exotic">Exotic</a><a href="/heatshield">HeatShield</a></div>
  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>
""".replace("{slug}", SLUG)

# ─────────────────────────────────────────── EN
EN_TITLE = "CPAC Tile & Metal Sheet Roof Leaks — The Kill-Spot Map, and Why SpackleFlex Comes First"
EN_DESC = ("A pitched roof almost never leaks everywhere — it leaks at points. The kill-spot map for concrete-tile "
           "(CPAC) roofs: crumbling ridge mortar, tiles cracked by foot traffic, the valley / and metal sheet: "
           "degraded screw washers, overlap seams. Why every pitched-roof job starts with SpackleFlex on the joints "
           "and cracks — plus the coat-over combo by budget.")
EN_EYEBROW = "Case Study · Tips / Knowledge"
EN_META = "Published Aug 2026 · by the LucernaPro team"

EN_BODY = """  <article>
    <p>Last case we covered <a href="/en/post/rooftop-concrete-or-tile">flat rooftop decks</a>. This time we climb one level up: <b>pitched roofs</b> — concrete tiles like CPAC, and metal sheet, the two materials covering most Thai homes and the source of the "my roof leaks, how do I fix it" messages that hit our page chat almost daily once the rain starts.</p>
    <p>Here's the good news most people don't know: a pitched roof <b>almost never leaks as a whole surface</b>. The slope sheds rain fast — water never gets to sit and soak the way it does on a flat deck. It leaks at <b>points</b>: cracks, joints, screw holes, capping lines. So the pitched-roof game isn't coating the whole plane from the start — it's <b>hunting down every one of those gaps and sealing them properly</b>.</p>
    <figure class="hero"><img src="/img/post/{slug}-hero.webp" alt="A low-pitch metal sheet roof on a Thai house, with rows of screw heads showing early rust and a clear sheet overlap seam running up the middle" width="1600" height="1200"><figcaption>A low-pitch metal sheet roof exactly like this is this story's special stage — water drains slowly, so every overlap seam and screw head gets tested far harder than on a steep roof (its own playbook is in section 04)</figcaption></figure>
    <section class="step">
      <h2><span class="n">01</span>Before you climb — the rules of stepping on a roof</h2>
      <p>One paragraph of brakes first, because we see this too often: a customer goes up to fix one leak and comes down having created three new cracks. <b>Concrete tiles only carry weight where they rest on the battens</b> — step mid-span and they can crack instantly. Step on the head of the tile where courses overlap (directly above the batten line), move slowly, transfer weight gently. On metal sheet, step along the purlin lines (follow the screw rows), never mid-span between purlins. And if the roof is steep or you're not confident — call a roofer. Labour is always cheaper than a hospital.</p>
    </section>
    <section class="step">
      <h2><span class="n">02</span>The kill-spot map — CPAC concrete-tile roof</h2>
      <p>The concrete tile itself is watertight and lasts decades. What actually fails is everything <i>around</i> it: <b>One — ridge and hip cap mortar.</b> The bedding mortar cracks and crumbles with age; water slips under the caps and runs along the battens to surface somewhere else entirely. <b>Two — cracked tiles</b>, with foot traffic from section 01 as the number-one cause. A single hairline is enough, every single rain. <b>Three — the valley</b>, where two roof planes dump their water into one channel: seams, rust, and leaf litter that dams the flow over the edge. <b>Four — the roof-to-wall junction.</b> Flashing lifts or the old sealant gives up, and every wind-driven shower backs water in along the line.</p>
      <figure><img src="/img/post/{slug}-cpac-en.webp" alt="Diagram of a CPAC concrete-tile roof plane marking four kill spots: crumbling ridge cap mortar, tiles cracked by foot traffic, the valley, and the roof-to-wall junction" loading="lazy" width="1200" height="900"><figcaption>Work through these four before blaming the whole roof — most culprits turn up in one pass</figcaption></figure>
      <p>A jobsite trick: from the stain on the ceiling, always look <b>upslope</b> — water that slips past a tile runs along the battens before it drops. Same principle we laid out in <a href="/en/post/finding-the-real-leak-point">Find the Real Leak Point First</a>.</p>
    </section>
    <section class="step">
      <h2><span class="n">03</span>The kill-spot map — metal sheet roof</h2>
      <p>A metal sheet is solid steel — water isn't getting through the sheet. It gets through everything that <i>isn't</i> the sheet: <b>One — screw heads</b>, the undisputed number-one culprit. The rubber washers bake brittle in the sun, or were driven crooked or over-tight and deformed from day one. One roof carries hundreds of screws, and every one is a suspect. <b>Two — overlap seams.</b> Steel expands and contracts all day, so the seams never stop moving — and the lower the pitch, the higher the risk, because strong wind pushes water back uphill along the lap. <b>Three — pipe and duct penetrations.</b> Every hole through the roof is a permanent doorway, and the old sealant around it bakes brittle faster than anywhere else. <b>Four — pinhole rust</b>, starting from a small coating scratch and spreading into needle holes.</p>
      <figure><img src="/img/post/{slug}-metal-en.webp" alt="Diagram of a metal sheet roof plane marking four kill spots: screw heads with degraded washers, sheet overlap seams, pipe penetrations, and pinhole rust" loading="lazy" width="1200" height="900"><figcaption>The sheet can shine like new and still leak — because none of the four kill spots is the sheet</figcaption></figure>
      <p><b>Straight talk on rust:</b> small pinholes can be sealed with filler and it genuinely holds. But a sheet eaten thin over a wide area? Filler there is buying time, not repairing. That's a sheet replacement — we sell chemicals, but we won't sell them into a job we already know won't survive.</p>
    </section>
    <section class="step">
      <h2><span class="n">04</span>The special stage — a low-pitch metal sheet roof plays a different game</h2>
      <p>The roof in the opening photo is the case we want to call out on its own: <b>low pitch</b>. Water drains slowly, heavy rain briefly sheets across the plane, and gusts push water back up the laps with ease — every kill spot from section 03 is still there, just tested several times harder. Spot-sealing the way you would on a steep roof usually doesn't hold.</p>
      <p>The low-pitch game is: <b>stop sealing points — seal full lines.</b> Run <a href="/en/spackleflex">SpackleFlex</a> along <b>the entire length of every overlap seam</b>, not just the stretch with the stain, and cap <b>every screw head</b> in the low-pitch zone — on a plane where water can pool and sheet, the screw that isn't leaking today is simply the one waiting its turn.</p>
      <p>And for those who want the stronger lock, this is the top of our joint-locking game: <a href="/en/modernfiberglass">Modern Fiberglass</a> — brush on the single-component Advanced Polymer resin, lay the <b>woven fiberglass cloth across the seam line</b>, then saturate it with another coat. Once set, the entire seam is locked under a reinforced fiberglass strip that stays tough and flexible, moving with the steel instead of cracking. Then finish with <a href="/en/siliconepro">SiliconePro</a> coated over the whole line — UV protection plus an extra waterproofing layer. It's the same formula written on the Modern Fiberglass page as the pro crews' go-to for brutal roof and joint work, and it matches the SiliconePro numbers exactly: reinforced with fiberglass cloth, service life stretches from around 5 years to 8–10.</p>
      <p><b>Step by step:</b> Start by getting the line ready — wipe off dust, oil and any flaking rust, and let the surface dry completely. Brush a bed coat of Modern Fiberglass resin along the seam, slightly wider than the cloth. Lay the roughly 6-inch woven fiberglass strip across the seam, press it down with the brush so it follows every rib and valley of the profile, then saturate the whole strip with resin. The check is easy to see: saturated cloth turns from matte white to translucent, with the metal ribs showing through — anywhere still white hasn't had enough.</p>
      <figure><img src="/img/post/{slug}-mf-step1.webp" alt="A gloved hand brushing amber-tinted Modern Fiberglass resin onto a 6-inch woven fiberglass cloth strip laid along a metal sheet roof seam, the coated half saturated and translucent while the dry half is still matte white" loading="lazy" width="1600" height="1200"><figcaption>The moment that matters in this step: saturate the woven cloth until it turns clear — anywhere still matte white has not drunk enough resin. Work it until the whole strip is translucent, let it set, then cap it with SiliconePro</figcaption></figure>
      <p>Two things decide whether this repair lives or dies: <b>One — the cloth must hug the profile.</b> A finished line should still show the metal's rib shape clearly through the strip. Anywhere the cloth spans tight across a valley, the gap underneath it is a future water channel — press it in while the resin is still wet. <b>Two — don't rush.</b> Let the saturated strip cure fully (this resin dries slowly on purpose: at least 6 hours). A cured strip is an even translucent amber, dry and matte, no tack when touched — only then move to the next layer. Never coat over wet cloth.</p>
      <p>Final step: coat <a href="/en/siliconepro">SiliconePro</a> over the entire line, carrying the color past both edges of the cloth and feathering it smooth into the sheet — this layer does two jobs at once: it shields the fiberglass underneath from the sun, and adds a full extra waterproofing layer along the seam.</p>
      <figure><img src="/img/post/{slug}-mf-step2.webp" alt="A cured amber-translucent fiberglass strip along a metal sheet roof seam being coated over with dark grey waterproofing, the finished section still clearly showing the rib profile of the metal underneath" loading="lazy" width="1600" height="1200"><figcaption>The closing step: the cured strip is an even translucent amber, and SiliconePro goes on past the cloth edges — notice the finished section still shows the rib profile clearly. That is the sign the cloth is truly bonded to the sheet</figcaption></figure>
      <p><b>Straight talk, said in full:</b> a low-pitch roof leaking along multiple lines, repairs that keep chasing the leak from spot to spot, or sheets degraded across the whole plane — in some of those cases the best-value answer <b>isn't a chemical at all</b>. It's calling a roofing crew to install an <b>overlay roof</b> (new sheets over the existing frame): one heavy payment, one brand-new plane. We sell chemicals — and we still won't cheer you into patching a roof we can both see is losing to its root cause. One overlay bill beats a climbing bill every single year.</p>
    </section>
    <section class="step">
      <h2><span class="n">05</span>Why every one of those spots starts with SpackleFlex</h2>
      <p>Notice what almost all the kill spots — cap mortar, cracks, overlaps, screw heads, wall junctions — have in common? <b>They move.</b> A roof gets blasted by afternoon sun and then hit by cool evening rain; the materials expand and contract against each other every single day. A rigid filler cracks along with them within a few heat cycles, and the clear silicone most households reach for chalks and peels under outdoor UV faster than anyone expects.</p>
      <p><a href="/en/spackleflex">SpackleFlex</a> was built for exactly this arena: a <b>flexible repair compound</b> that moves with the roof without tearing, <b>ready to use with no mixing</b> — open and trowel, right there on the roof (this matters: nobody wants to weigh out a two-part mix straddling a ridge) — tougher outdoors than ordinary silicone thanks to built-in UV stabilization, and tested under continuous water immersion for months. Use it to strike over crazed cap mortar, fill tile cracks, cap screw heads one by one, run the overlap seams, and dress around pipe penetrations.</p>
      <p>Two fair warnings before you start: <b>cap mortar that has come off in chunks</b> needs to be re-bedded with mortar first — then SpackleFlex guards the hairlines; filler is not structural mortar. And <b>a tile broken clean through</b> is better replaced if you can source one; filler is for cracks and for tiles that can no longer be swapped out.</p>
      <p>And the straight talk we give every customer: <b>the chemical is not the expensive part of a roof job — the labour and the risk of climbing up there is.</b> So make it one climb: work through the full map from sections 02–04 and seal everything, instead of patching the one spot you suspect and coming down to hope. Miss it, and you pay the full climbing fee all over again.</p>
    </section>
    <section class="step">
      <h2><span class="n">06</span>Stop at the filler, or go further — the coat-over combo by budget</h2>
      <p>Most pitched roofs <b>genuinely finish at "every spot sealed"</b> — no full-surface coat needed, unlike a flat deck. But if you want to squeeze out maximum service life, or the roof is old with risk spread everywhere, our combo formula is: filler done, <b>wait 6 hours</b>, then coat over the repaired lines. Budget lane: <a href="/en/siliconepro">SiliconePro</a>, single-component, open and roll. Full-send lane: <a href="/en/exotic">Exotic</a> — a single-component Polyurea we call the ultimate roof combo, top-shelf grade with the mixing step deleted, opened and applied right on the roof.</p>
      <p>And for metal sheet homes that complain about heat as much as leaks, there's a two-birds option: <a href="/en/heatshield">HeatShield</a>, a waterbase waterproofer that also cuts heat — applies to metal sheet, tile and concrete, solar reflectance (TSR) above 95% (tested by the KMUTT research institute), dropping roof surface temperature by 5°C or more. Seal the kill spots with SpackleFlex first, then coat the plane with HeatShield: extra waterproofing and a cooler house in one round.</p>
      <p>One more spot that often leaks alongside the roof but sits elsewhere: <b>the gutter</b>. If the stains run along the eaves line, head to our separate case on <a href="/en/post/metal-gutter-seam-repair">gutter seam repair</a>.</p>
    </section>
    <section class="step">
      <h2><span class="n">07</span>The wrap — a roof is not a deck; don't run the same play</h2>
      <figure><img src="/img/post/{slug}-map-en.webp" alt="Kill-spot map for a CPAC concrete-tile roof (ridge cap mortar, cracked tiles, the valley, wall junction) and a metal sheet roof (screw heads, overlap seams, pipe penetrations, pinhole rust)" loading="lazy" width="1200" height="900"><figcaption>Two materials, two kill-spot maps — save this one for the day you climb up</figcaption></figure>
      <p>Flat deck = standing water, think whole-surface film. Pitched roof = fast-shedding water, think <b>points</b> — work the kill-spot map to the end, seal with something genuinely flexible and sun-proof like <a href="/en/spackleflex">SpackleFlex</a>, then decide on the coat-over combo based on budget and the roof's age.</p>
      <p>Not sure which spot is your culprit? Photograph the suspect angles and the ceiling stains and send them to our page chat — tell us tile or metal sheet, and we'll call the target for you free, before you buy. One climb, done.</p>
    </section>
  </article>
  <div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/spackleflex">SpackleFlex</a><a href="/en/modernfiberglass">Modern Fiberglass</a><a href="/en/siliconepro">SiliconePro</a><a href="/en/exotic">Exotic</a><a href="/en/heatshield">HeatShield</a></div>
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
