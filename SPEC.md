# LucernaPro Website — SPEC & Campaign Doctrine

เอกสารกลางของโปรเจกต์ย้ายเว็บ lucernapro.com จาก Wix → Static Site
(อ่านไฟล์นี้ก่อนแก้อะไรทุกครั้ง — สำหรับทั้งคนและ Claude)

## สถาปัตยกรรม
- Static site: HTML/CSS/JS ล้วน ไม่มี framework, ไม่มี build step
- Source of truth: GitHub repo นี้ / Deploy อัตโนมัติผ่าน Cloudflare (Workers/Pages) ทุก commit
- หน้าเว็บ generate จากสคริปต์ฝั่ง Claude (template + product data) — แก้ข้อมูลสินค้า = regenerate ไม่แก้ HTML มือ
- การขายจบที่ Shopee/Lazada/Facebook — เว็บไม่มีตะกร้า ไม่มีระบบสมาชิก

## กฎเหล็ก (ห้ามละเมิด)
1. **URL สินค้าต้องตรงกับ Wix เดิมทุกเส้น** เช่น `/tilecoatpoly`, `/polypro` — สร้างเป็น `{slug}/index.html`
2. **เว็บเป็นสองภาษาเสมอ**: ไทยที่ราก `/` (ตลาดหลัก), อังกฤษที่ `/en/` โครงเดียวกันเป๊ะ — hreflang โยงถึงกัน (th, en, x-default=th) และปุ่มสลับภาษา (.lang-switch) บน topbar
   **ลำดับการทำ (มติ 25 ก.ค. 2026): ทำหน้าสินค้าภาษาไทยให้ครบและผ่านการตรวจจากเจ้าของก่อนทั้งหมด แล้วค่อยเปิด phase แปล EN เป็นชุดเดียวทีหลัง** — ระหว่างที่หน้า EN ของสินค้าตัวนั้นยังไม่มี: ห้ามใส่ hreflang en ชี้หน้าที่ไม่มีจริง และปุ่ม EN บนหน้าสินค้าไทยให้ชี้ `/en/` (Home อังกฤษ) ไปพลางก่อน
3. เว็บนี้ยังไม่ cutover — domain จริงยังชี้ Wix / ลิงก์ระหว่างหน้าใช้ relative หรือ root-relative path (`/img/...`, `/en/`) เพื่อให้ทำงานทั้ง sandbox และ domain จริง
4. ห้าม hardcode domain ในลิงก์ภายใน (ยกเว้น canonical/OG/hreflang ใน meta ที่ชี้ lucernapro.com)
5. รูปทุกรูปผ่าน pipeline: gallery กว้างสูงสุด 480px WebP q74 / รูปหลัก (hero/pack shot) 900px WebP **q85** (ฉลากมีตัวหนังสือ q74 ไม่พอ), ชื่อไฟล์ = slug (`{slug}-hero.webp`, `{slug}-gXX.webp`) — รูปใช้ร่วมกันทั้งสองภาษาจากโฟลเดอร์ `/img/` เดียว
   **Crop ให้พอดีกรอบตั้งแต่ขั้นแปลงรูป (มติ 25 ก.ค. 2026):** กรอบ template ล็อกสัดส่วนตายตัว (hero จัตุรัส 900×900, gallery 1:1 480×480) และรูปต้องถูก crop ให้พอดีกรอบ**ในขั้นแปลง** (Claude เป็นคน crop ตอนแปลง เช็คด้วยตาว่าตัวสินค้าไม่โดนตัด) — เจ้าของส่งรูป ratio ไหนก็ได้ / CSS ใส่ `object-fit:cover` ไว้เป็น safety net เท่านั้น ไม่ใช่กลไกหลัก
   **Workflow รูป (เจ้าของไม่ใช้ terminal):** เจ้าของส่งรูปในแชท → Claude แปลง+ตั้งชื่อตามกติกา → ส่งไฟล์พร้อมใช้กลับ → เจ้าของอัปโหลดผ่านหน้าเว็บ GitHub (Add file → Upload files) — สคริปต์ใน tools/ เป็นทางเลือกสำรอง ไม่ใช่ทางบังคับ
6. มือถือมาก่อนเสมอ — ลูกค้าส่วนใหญ่คือมือถือ
7. **สองโหมดสีเสมอ**: สว่างเป็นค่าเริ่มต้น (:root = light), มืดคือ [data-theme="dark"] สลับด้วยปุ่ม .theme-toggle จำค่าใน localStorage key `lucerna-theme` — **ห้ามฝังสีตายตัวในโค้ด ทุกสีต้องผ่าน CSS variable เท่านั้น** (ยกเว้นสีแบรนด์คงที่: fbadge น้ำเงิน #1877F2, ตัวหนังสือบนปุ่มส้ม #16130F, Line เขียว #06C755) และทุกหน้าที่ทำใหม่ต้องตรวจตาทั้งสองโหมดก่อนถือว่าเสร็จ
8.4 **Explore band ท้ายหน้า (มติ 26 ก.ค. 2026):** ทุกหน้าสินค้าต้องมี section "นี่แค่ 1 ใน 50+" หลังส่วนสั่งซื้อ ก่อน contact — ลูกค้าที่ได้ลิงก์ตรงมักไม่รู้ว่าเรามีสินค้าอื่น ป้ายนี้คือทางเข้าสู่ catalog (chips 7 หมวด + ปุ่มดูสินค้าทั้งหมด) / ต้นแบบ: /polypro
8.5 **วิธีใช้งานจบบนหน้าเว็บเสมอ (มติ 25 ก.ค. 2026):** ทุกหน้าสินค้าใส่ขั้นตอนใช้งานเป็น timeline บนหน้า พร้อมตัวเลขจริงครบ (อัตราผสม, เวลารอ, จำนวนรอบ) — ลูกค้าอ่านหน้าเดียวลงมือได้ ห้ามลิงก์ไฟล์คู่มือแยก อย่างมากมีปุ่ม TDS ตัวเดียว (เอกสารเทคนิคใน `/files/{slug}-tds.pdf`) / ต้นแบบ: `/tilecoatpoly`
8. ภาษาอังกฤษ: โทนเดียวกับไทย (มั่นใจ กวนนิดๆ) ไม่ใช่แปลตรงตัวแข็งทื่อ / tag ค้นหาไทยฝังใน data-search ของหน้า EN ด้วยเพื่อให้ปุ่มปัญหากรองได้ทั้งสองภาษา

## Design Tokens (ธีมดำ-ส้ม Lucerna)
- --bg: #0B0B0D (ดำหลัก) / --panel: #151518 / --panel-2: #1B1B1F / --line: #28282E
- --ink: #F4F4F2 (ตัวหนังสือ) / --muted: #9BA0A6
- --orange: #ED6A2F (ส้มโลโก้ = สีหลัก) / --orange-hi: #FF8A4C
- ปุ่ม Facebook: พื้น graphite (--panel-2 + border --line) + ตรา f น้ำเงิน #1877F2 ดวงเล็ก (.fbadge) — ห้ามปุ่มน้ำเงินเต็มแผ่น
- Line: สีเขียว #06C755 ใช้ได้ (chip .shop-line)
- ฟอนต์: Chakra Petch (หัวข้อ/display), Anuphan (เนื้อหา), IBM Plex Mono (โค้ด/ตัวเลขกำกับ)
- สีหมวด: waterproof #4FA3D1, flooring #E0A458, wall #D1766B, coating #8FA6B8, chem #7FBF8E, auto #B48FD1

## เสียงของแบรนด์
- Slogan: "Leave the Ordinary Behind" (hero kicker + footer)
- โทน: มั่นใจ กวนนิดๆ ตรงไปตรงมา — เก็บ copy เด็ดเดิมไว้ เช่น "กาวบ้าพลัง", "ซ่อมเท่าไหร่ก็ไม่จบ ต้องชม", "เหมาะสำหรับคนขี้เกียจ"
- แชทหลัก = Facebook (m.me/lucernapro) / Line @lucerna เป็นรอง แต่ต้องมีเสมอ

## ข้อมูลบริษัท
บริษัท ลูเซอน่า จำกัด — 23 ถ.สุริยาตร์ ซอย 4 ต.ในเมือง อ.เมือง จ.อุบลราชธานี 34000
โทร 097-079-9547, 097-079-6583 / Office 062-005-7933 / Lucernapro@yahoo.com / 08.00–19.00 จ–ส
Facebook: facebook.com/lucernapro (100k+ followers) / Shopee: shopee.co.th/lucernapro / Lazada: lazada.co.th/shop/lucernapro

## สินค้า (52 ตัว, 6 หมวด) — สถานะพิเศษ
- เลิกขายแล้ว ห้ามโชว์: DryPro, Gold Mine, SightSaver
- Ladder กันซึม (เรียงตามศักดิ์): PMMA → Polyurea Gen3 → Exotic (=Gen3 แต่ไม่ต้องผสม) → Polyurea (สาย Poly รุ่นประหยัด) → SiliconePro (มาใหม่ แช่น้ำได้เป็นปี) → HeatShield (ประหยัด+ลดร้อน)
- DeepStick = ซ่อมรอยต่อสารพัดงาน (ใต้น้ำ/กันซึม/Smartboard) อยู่หมวด Wall ตาม Wix เดิมไปก่อน
- สินค้าใหม่ยังไม่มีหน้า: hydroglide, epoxyputty, ecobind, Liquid Membrane, flake set (รอเจ้าของ confirm)

## Campaign Roadmap
- [x] หน้า Home ไทย (index.html) — ขึ้น production แล้ว
- [x] หน้า Home อังกฤษ (en/index.html) — สองภาษาครบ
- [x] หน้าสินค้า pilot: TileCoat Polyurea (`/tilecoatpoly`) — เสร็จ + เจ้าของตรวจผ่าน 25 ก.ค. 2026 (ราคาจริง, pack shot, timeline วิธีใช้, TDS ในบ้านตัวเอง — ตัดขาดจาก Wix สมบูรณ์)
- [x] หน้า EN pilot: `/en/tilecoatpoly` (มติแก้ไข 25 ก.ค. 2026: pilot ทำคู่สองภาษาเพื่อเป็น template EN ด้วย — hreflang ผูกครบทั้งคู่) / **สินค้าที่เหลือยังยึดมติเดิม: ไทยครบก่อน แล้วค่อย batch แปล EN**
- [ ] ปั๊มหน้าสินค้าไทยที่เหลือตามหมวด (หนึ่งเซสชัน = หนึ่งชุด)
- [ ] Phase แปล EN หน้าสินค้าทั้งหมด (หลังไทยครบ + เจ้าของตรวจแล้ว)
- [ ] Blog / Case study
- [ ] ตรวจ URL ครบทุกเส้น → cutover DNS → เฝ้าดู 1–2 สัปดาห์ → ยกเลิก Wix

## วิธีเปิดเซสชันใหม่กับ Claude
วางลิงก์ repo นี้ + บอกว่าจะทำด่านไหน — Claude อ่าน SPEC.md + index.html แล้วทำงานต่อได้ทันที
