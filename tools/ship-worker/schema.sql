-- Lucerna Ship — D1 schema
-- ข้อมูลที่เข้ามาถูก sanitize ตั้งแต่ต้นทาง: ไม่มีตัวเลขเงินเข้ามาในฐานข้อมูลนี้เลย

CREATE TABLE IF NOT EXISTS orders (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  ym         TEXT NOT NULL,              -- '2026-08' (partition รายเดือน)
  odate      TEXT NOT NULL,              -- '2026-08-25'
  customer   TEXT NOT NULL,              -- ชื่อตามบัญชี (คน/บริษัท) = คอลัมน์ I
  receiver   TEXT NOT NULL DEFAULT '',   -- ชื่อผู้รับพัสดุ (คอลัมน์ K — อนาคต)
  product    TEXT NOT NULL,              -- คอลัมน์ A
  qty        REAL NOT NULL DEFAULT 1,    -- คอลัมน์ C
  okey       TEXT NOT NULL UNIQUE,       -- 'Aug2026:r57' = ชีต:แถว กันซ้ำเวลา import ซ้ำ
  status     TEXT NOT NULL DEFAULT 'pending',  -- pending | shipped
  tracking   TEXT NOT NULL DEFAULT '',
  shipped_at TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_orders_date   ON orders(odate);
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);

-- เลขลอย: tracking ที่หาเจ้าของไม่ได้
CREATE TABLE IF NOT EXISTS orphans (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  tracking   TEXT NOT NULL,
  ems_name   TEXT NOT NULL DEFAULT '',   -- ชื่อ (ที่มักโดนตัด) จากลิสต์ ปณ
  status     TEXT NOT NULL DEFAULT 'open',  -- open | archived (ตัดทิ้ง/ของเก่า)
  note       TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- log ทุกการจับคู่/แก้ไข ไว้ตรวจย้อนหลัง
CREATE TABLE IF NOT EXISTS audit (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  action     TEXT NOT NULL,   -- match_auto | match_manual | unassign | orphan_keep | orphan_archive | import
  detail     TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
