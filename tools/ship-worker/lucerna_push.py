# -*- coding: utf-8 -*-
"""
lucerna_push.py — ดึงข้อมูลจาก Google Sheet (เล่มเดียวกับ LucernaOne) ส่งให้ระบบพนักงาน
ส่งแค่ 4 อย่าง: ลูกค้า / สินค้า / จำนวน / วันที่ (+ ผู้รับ ถ้ามีคอลัมน์ K ในอนาคต)
ตัวเลขเงินไม่ถูกอ่านออกไปจากเครื่องนี้เลย

ใช้:
    python lucerna_push.py                # วันนี้
    python lucerna_push.py 25/8/2026      # วันเดียว
    python lucerna_push.py 25/8/2026 -    # ตั้งแต่วันนั้นถึงวันนี้ (ทั้งช่วง)

รันซ้ำได้ไม่พัง: แถวเดิม (ชีต+เลขแถวเดิม) จะถูกอัพเดต ไม่สร้างซ้ำ
และจะไม่ล้างสถานะ "ส่งแล้ว" ที่พนักงานจับคู่ไปแล้ว
"""

import sys, json, datetime, urllib.request

# ===== CONFIG — แก้ 2 บรรทัดนี้หลัง deploy worker =====
WORKER_URL = "https://lucerna-ship.lekvtwin.workers.dev"
IMPORT_KEY = "ใส่ IMPORT_KEY ที่ตั้งไว้ตอน wrangler secret put"

SPREADSHEET_ID = "1gmdoVX9Oa18zEXBJUNhW1PjRTGaw7PcjkgSK0_YG1RM"
SERVICE_ACCOUNT_FILE = "service_account.json"   # ไฟล์เดียวกับที่ LucernaOne ใช้

# กันระบบมั่ว: ไม่ import ก่อนวันเริ่มระบบเด็ดขาด (ของเก่าส่งไปแล้ว จับคู่ไม่ได้อยู่แล้ว)
START_DATE = datetime.date(2026, 8, 25)

MONTH_ABBRS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def month_sheet_name(d): return f"{MONTH_ABBRS[d.month-1]}{d.year}"

def parse_thai_date(s):
    """'25/8/2026' -> date (รูปแบบเดียวกับคอลัมน์ J ของ LucernaOne)"""
    p = [int(x) for x in s.strip().split("/")]
    return datetime.date(p[2], p[1], p[0])

def fetch_rows(dates):
    import gspread
    from google.oauth2.service_account import Credentials
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    ss = gspread.authorize(creds).open_by_key(SPREADSHEET_ID)

    want = {d.strftime("%-d/%-m/%Y") if sys.platform != "win32" else f"{d.day}/{d.month}/{d.year}"
            for d in dates}
    want |= {f"{d.day}/{d.month}/{d.year}" for d in dates}   # กันเรื่อง platform format

    out = []
    for title in sorted({month_sheet_name(d) for d in dates}):
        try:
            ws = ss.worksheet(title)
        except Exception:
            print(f"  [ข้าม] ไม่พบชีต {title}")
            continue
        values = ws.get_all_values()
        for idx, row in enumerate(values, start=1):
            row = row + [""] * 12
            product, qty_s, customer, date_s, receiver = \
                row[0].strip(), row[2].strip(), row[8].strip(), row[9].strip(), row[10].strip()
            if date_s not in want:
                continue
            # กรองแถวที่ไม่ใช่ออเดอร์จริง
            if not product or not customer:
                continue
            if product.startswith("ยอดขาย") or "ส่วนลด" in product:
                continue
            try:
                qty = float(qty_s.replace(",", "")) if qty_s else 1.0
            except ValueError:
                qty = 1.0
            if qty <= 0:
                continue
            d = parse_thai_date(date_s)
            out.append({
                "okey": f"{title}:r{idx}",
                "odate": d.isoformat(),
                "customer": customer,
                "receiver": receiver,          # คอลัมน์ K — ตอนนี้ยังว่าง อนาคต parser จะเติมให้
                "product": product,
                "qty": qty,
            })
    return out

def push(rows):
    req = urllib.request.Request(
        WORKER_URL.rstrip("/") + "/import",
        data=json.dumps({"rows": rows}).encode(),
        headers={"content-type": "application/json", "x-key": IMPORT_KEY},
        method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def main():
    today = datetime.date.today()
    args = [a for a in sys.argv[1:] if a.strip()]
    if not args:
        dates = [today]
    elif len(args) >= 2 and args[1] == "-":
        start = parse_thai_date(args[0])
        dates = [start + datetime.timedelta(days=i) for i in range((today - start).days + 1)]
    else:
        dates = [parse_thai_date(args[0])]

    dates = [d for d in dates if d >= START_DATE]
    if not dates:
        print(f"ไม่มีวันที่ให้ทำ (ระบบเริ่มนับจาก {START_DATE.strftime('%d/%m/%Y')} — ก่อนหน้านั้นไม่ import)")
        return

    print(f"อ่านชีต: {', '.join(d.strftime('%d/%m/%Y') for d in dates[:5])}{' ...' if len(dates) > 5 else ''}")
    rows = fetch_rows(dates)
    print(f"เจอออเดอร์ {len(rows)} แถว")
    if not rows:
        return
    for r in rows[:8]:
        print(f"   {r['odate']}  {r['customer']:<22.22}  {r['product']:<28.28} x{r['qty']:g}")
    if len(rows) > 8:
        print(f"   ... อีก {len(rows)-8} แถว")
    res = push(rows)
    print(f"ส่งเข้าเว็บแล้ว: ใหม่ {res.get('added',0)} / อัพเดต {res.get('updated',0)} / ข้าม {res.get('skipped',0)}")

if __name__ == "__main__":
    main()
