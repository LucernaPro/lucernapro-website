# คลังข้อมูลหน้า Wix เดิม — สินค้าที่ยังไม่ได้สร้างหน้าใหม่

**วันที่ดึง: 29 ก.ค. 2026** — ดึงด้วย Claude ผ่าน web fetch จาก `https://www.lucernapro.com/{slug}`

> ⚠️ **เหตุผลที่ต้องมีไฟล์ชุดนี้:** `lucernapro.com` กำลังย้าย domain จาก Wix มา Cloudflare
> เมื่อชี้ nameserver ไป Cloudflare เมื่อไหร่ **หน้า Wix เดิมจะหายทันทีและดึงกลับมาไม่ได้อีก**
> ไฟล์ชุดนี้คือสำเนาถาวรของเนื้อหา ราคา ลิงก์ร้าน และ URL รูปต้นฉบับทั้งหมด

## สถานะรวม

- เมนู Wix มีสินค้าทั้งหมด **55 ตัว**
- สร้างหน้าใหม่แล้ว **40 ตัว**
- **เหลือ 15 ตัว** (ไม่ใช่ 12 ตามที่ `_redirects` จดไว้)

### 🔴 สามตัวที่ไม่มีทั้งใน repo และใน `_redirects` — หลุดจากลิสต์
| slug | ชื่อ | หมวด |
|---|---|---|
| `goldmine` | Gold Mine สีทอง Goldleaf | Painting (หมวดนี้มีสินค้าตัวเดียว) |
| `sightsaver` | SightSaver เคลือบกระจกส่องหลัง | Automotive |
| `drypro` | DryPro น้ำยาปกป้องคราบน้ำ | Protection Coating |

**ต้องเพิ่ม 3 บรรทัดนี้เข้า `_redirects` ทั้ง TH และ EN ทันที** ไม่งั้นลิงก์จากเมนูเก่า/Google จะ 404

### 12 ตัวที่อยู่ใน `_redirects` อยู่แล้ว
`americaniron` · `anchoringepoxy` · `blast` · `compositecore` · `epoxycatridge` ·
`nanoceramic` · `polyasparticadhesive` · `prolatex` · `schutznano` · `schutznano9h` ·
`splatter` · `swiftset`

## บันทึกที่เจอระหว่างดึง

1. **ตระกูล Polysilazane มี 4 ตัวที่เนื้อหาเว็บเดิมก๊อปกันเกือบทั้งท่อน**
   (`schutznano`, `schutznano9h`, `americaniron`, + `schutzfirearm` ที่ทำไปแล้ว)
   — บล็อก "Technical Information" ของ `americaniron` **ยังเขียนว่า "SCHUTZ NANO"** ค้างอยู่เลย
   ตอนทำหน้าใหม่ต้องเขียนแยกกันจริงๆ ไม่งั้น Google มองว่า duplicate content ทั้งกลุ่ม

2. **🔴 ลิงก์ร้านของ `schutznano9h` ซ้ำกับ `schutznano` เป๊ะทั้ง Shopee และ Lazada**
   (`29159897692` / `i5331355106`) — อันใดอันหนึ่งผิดแน่นอน **ต้องให้เจ้าของเช็ค**

3. **🔴 ปุ่ม TDS ของ `schutznano9h` ชี้ไปไฟล์ `.png` ไม่ใช่ `.pdf`** — ลิงก์เสียบนเว็บเดิม

4. **`Si-N-Si` / `Si-O-Si` / คำว่า `polysilazane` โผล่บนหน้าเว็บเดิมทุกตัวของตระกูลนี้**
   ขัดกับกติกาห้ามเปิดเผยชนิดเคมี — ตอนทำหน้าใหม่ต้องขอมติเจ้าของว่าจะคงไว้หรือถอด
   (บันทึกเดิมของ `plastibright` เขียนไว้ว่า polysilazane เป็น background ไม่พิมพ์ลงหน้าเว็บ
   → **ค่า default คือถอด** จนกว่าเจ้าของจะสั่งเป็นอย่างอื่น)

5. **`americaniron` เคลม "Temperature Resistance: Up to 400°C"** — ตัวเลขนี้มาจาก TDS วัตถุดิบ
   ยังไม่มีหลักฐานว่าทดสอบเองที่ 400°C ต้องเคาะก่อนขึ้นหน้า

## ไฟล์ในโฟลเดอร์นี้

หนึ่งไฟล์ต่อสินค้า ตั้งชื่อตาม slug — เนื้อหาดิบจาก Wix + สิ่งที่ต้องเคาะก่อนสร้างหน้า
