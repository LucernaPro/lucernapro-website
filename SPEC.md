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
2. **เว็บเป็นสองภาษาเสมอ**: ไทยที่ราก `/` (ตลาดหลัก), อังกฤษที่ `/en/` โครงเดียวกันเป๊ะ — หน้าสินค้าใหม่ทุกหน้าต้องส่งมอบเป็นคู่ `/{slug}/` + `/en/{slug}/` พร้อม hreflang โยงถึงกันทั้งสองฝั่ง (th, en, x-default=th) และปุ่มสลับภาษา (.lang-switch) บน topbar
3. เว็บนี้ยังไม่ cutover — domain จริงยังชี้ Wix / ลิงก์ระหว่างหน้าใช้ relative หรือ root-relative path (`/img/...`, `/en/`) เพื่อให้ทำงานทั้ง sandbox และ domain จริง
4. ห้าม hardcode domain ในลิงก์ภายใน (ยกเว้น canonical/OG/hreflang ใน meta ที่ชี้ lucernapro.com)
5. รูปทุกรูปผ่าน pipeline: กว้างสูงสุด 480px (หน้าสินค้าใช้ 900px สำหรับรูปหลัก), WebP quality 74, ชื่อไฟล์ = slug — รูปใช้ร่วมกันทั้งสองภาษาจากโฟลเดอร์ `/img/` เดียว
6. มือถือมาก่อนเสมอ — ลูกค้าส่วนใหญ่คือมือถือ
7. ภาษาอังกฤษ: โทนเดียวกับไทย (มั่นใจ กวนนิดๆ) ไม่ใช่แปลตรงตัวแข็งทื่อ / tag ค้นหาไทยฝังใน data-search ของหน้า EN ด้วยเพื่อให้ปุ่มปัญหากรองได้ทั้งสองภาษา

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
- [ ] หน้าสินค้า pilot: TileCoat Polyurea (`/tilecoatpoly`) — เนื้อหาดึงจาก Wix เดิม แล้วเจ้าของตรวจแก้
- [ ] ปั๊มหน้าสินค้าที่เหลือตามหมวด (หนึ่งเซสชัน = หนึ่งชุด)
- [ ] Blog / Case study
- [ ] ตรวจ URL ครบทุกเส้น → cutover DNS → เฝ้าดู 1–2 สัปดาห์ → ยกเลิก Wix

## วิธีเปิดเซสชันใหม่กับ Claude
วางลิงก์ repo นี้ + บอกว่าจะทำด่านไหน — Claude อ่าน SPEC.md + index.html แล้วทำงานต่อได้ทันที
