#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_feed.py — สร้าง /feed.csv (Meta product catalog) + รูปสี่เหลี่ยม img/feed/<slug>.jpg

ทำไม: Catalog ads / retargeting ของ Facebook ต้องมีรายการสินค้าทั้งร้านในไฟล์เดียว
       ที่ Facebook ดึงเองทุกวัน (Commerce Manager → data source → scheduled feed URL)

แหล่งความจริง (ไม่มีตัวเลขของตัวเอง — หลักเดียวกับ /calculator):
- ทุกหน้า <slug>/index.html (TH) ที่ไม่ noindex และมี .pricecard ที่เป็นตารางราคาจริง
  (ทุกแถวมี <td class="pr"> — ราคา = pr ตัวแรกของแถว, ค่าส่งไม่นับ; ขนาด = ข้อความก่อน <br>/<small>) → กล่องแรกที่เข้าเกณฑ์เท่านั้น (กล่องเทียบราคา/รองพื้นแยกไม่เอา)
- ชื่อสินค้า = <h1> บรรทัดแรก · คำอธิบาย = <meta name="description"> · รูป = og:image (สำรอง img/<slug>-hero.webp)
- 1 แถวราคา = 1 item   id = <slug>-<ขนาดปกติ>   item_group_id = <slug>   link = https://www.lucernapro.com/<slug>
  → track.js ยิง ViewContent {content_ids:[slug], content_type:'product_group'} ตรงกับ item_group_id นี้

รูป: Meta ต้องการอย่างน้อย 500×500 และแนะนำสี่เหลี่ยมจัตุรัส → ครอปกลาง 1000×1000 เป็น JPG ที่ img/feed/<slug>.jpg
     (ทำเฉพาะเมื่อไฟล์ต้นทางใหม่กว่า — รันซ้ำได้ไม่เปลืองเวลา)

วิธีใช้:  python3 tools/gen_feed.py           (รันใหม่ทุกครั้งที่ราคา/สินค้าเปลี่ยน — check_parity เตือนถ้าลืม)
          python3 tools/gen_feed.py --check   (ไม่เขียนไฟล์ แค่คืน CSV ที่ควรเป็น — ใช้ใน check_parity)
"""
import os, re, io, csv, sys, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DOMAIN = "https://www.lucernapro.com"
OUT = "feed.csv"
IMG_DIR = "img/feed"
SKIP_DIRS = {'en', 'post', 'casestudy', 'search', 'finder', 'account', 'ship', 'calculator', 'test',
             'notes', 'files', 'img', 'tools'}
COLS = ['id', 'title', 'description', 'availability', 'condition', 'price', 'link', 'image_link',
        'brand', 'item_group_id', 'size']


def strip(s):
    s = re.sub(r'<br\s*/?>', ' ', s or '')
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()


def size_key(sz):
    """'1 กก.' → '1kg', '350 g' → '350g', 'ขวด 200 กรัม' → '200g', 'ซอง 20 มล.' → '20ml' (สำหรับ id คงที่)"""
    s = sz.lower()
    s = re.sub(r'กก\.?|กิโลกรัม', 'kg', s)
    s = re.sub(r'กรัม', 'g', s)
    s = re.sub(r'มล\.?|มิลลิลิตร', 'ml', s)
    s = re.sub(r'ลิตร', 'l', s)
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*(kg|g|ml|l)\b', s)
    if m:
        return (m.group(1).replace(',', '') + m.group(2)).replace('.', 'p')
    k = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return k[:40] or 'x'


def price_of(cell):
    m = re.search(r'(\d[\d,]*)(?:\.\d+)?\s*\.?-?', strip(cell))
    return int(m.group(1).replace(',', '')) if m else None


def pricecards(h):
    out = []
    for m in re.finditer(r'<div class="pricecard', h):
        s = m.start(); e = h.find('</table>', s)
        if e < 0: continue
        seg = h[s:e]
        rows = []
        for r in re.findall(r'<tr>(.*?)</tr>', seg, re.S):
            tds = re.findall(r'(<td[^>]*>)(.*?)</td>', r, re.S)
            if not tds: continue
            rows.append(tds)
        # ตารางราคาจริง = ทุกแถวมี <td class="pr"> (ค่าส่งเป็นคอลัมน์ pr ตัวที่สอง — เอาตัวแรกเสมอ)
        if rows and all(any('class="pr"' in td[0] for td in r) for r in rows):
            out.append(rows)
    return out


def items():
    out = []
    for f in sorted(glob.glob('*/index.html')):
        slug = f.split('/')[0]
        if slug in SKIP_DIRS: continue
        h = open(f, encoding='utf-8').read()
        if re.search(r'<meta[^>]+name="robots"[^>]+noindex', h): continue
        cards = pricecards(h)
        if not cards: continue
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S)
        if not h1: continue
        name = strip(h1.group(1).split('<br')[0])
        desc = re.search(r'<meta name="description" content="([^"]*)"', h)
        desc = html.unescape(desc.group(1)) if desc else name
        og = re.search(r'property="og:image" content="([^"]+)"', h)
        src = og.group(1).replace(DOMAIN, '') if og else f'/img/{slug}-hero.webp'
        src = src.lstrip('/')
        if not os.path.exists(src): continue
        seen = set()
        for tds in cards[0]:
            sz = strip(re.split(r'<br|<small', tds[0][1])[0])
            pr = price_of(next(td[1] for td in tds if 'class="pr"' in td[0]))
            if not sz or pr is None: continue
            key = size_key(sz)
            n = 2
            while key in seen:
                key = f'{size_key(sz)}-{n}'; n += 1
            seen.add(key)
            out.append(dict(
                id=f'{slug}-{key}', title=f'{name} {sz}', description=desc[:4999],
                availability='in stock', condition='new', price=f'{pr}.00 THB',
                link=f'{DOMAIN}/{slug}', image_link=f'{DOMAIN}/{IMG_DIR}/{slug}.jpg',
                brand='LucernaPro', item_group_id=slug, size=sz, _src=src, _slug=slug))
    return out


def csv_text(rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLS, extrasaction='ignore', lineterminator='\n')
    w.writeheader()
    for r in rows: w.writerow(r)
    return buf.getvalue()


def make_images(rows):
    from PIL import Image
    os.makedirs(IMG_DIR, exist_ok=True)
    done = set(); n = 0
    for r in rows:
        slug, src = r['_slug'], r['_src']
        if slug in done: continue
        done.add(slug)
        dst = f'{IMG_DIR}/{slug}.jpg'
        if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): continue
        im = Image.open(src).convert('RGB')
        w, h = im.size; s = min(w, h)
        im = im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
        if s > 1000: im = im.resize((1000, 1000), Image.LANCZOS)
        elif s < 500: im = im.resize((500, 500), Image.LANCZOS)
        im.save(dst, 'JPEG', quality=88, optimize=True)
        n += 1
    return n


if __name__ == '__main__':
    rows = items()
    if '--check' in sys.argv:
        sys.stdout.write(csv_text(rows)); sys.exit(0)
    n = make_images(rows)
    open(OUT, 'w', encoding='utf-8', newline='').write(csv_text(rows))
    groups = len({r['_slug'] for r in rows})
    print(f'feed.csv: {len(rows)} items / {groups} products · รูปใหม่ {n} ไฟล์ใน {IMG_DIR}/')
