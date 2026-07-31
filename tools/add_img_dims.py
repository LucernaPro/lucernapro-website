#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_img_dims.py — เติม width/height ให้ <img> ทุกหน้า (กัน layout shift → Core Web Vitals)

ทำสองชั้นตามมติ SPEC 29 ก.ค. 2026 (บทเรียน ironlock):
1. Safety net: หน้าไหนที่มี <img> แต่ไม่มีกฎ global `img{...height:auto...}`
   → เติม `img{height:auto}` ต่อท้าย <style> บล็อกแรก
   (bare selector specificity ต่ำสุด — class rule ที่จงใจตั้ง height ชนะเสมอ
    จึงไม่กระทบ layout เดิม แต่กันภาพยืดในเคสที่ CSS บีบ width อย่างเดียว)
2. เติม width/height attribute จากขนาด pixel จริงของไฟล์ใน /img
   - ข้าม <img> ที่มี width+height ครบแล้ว
   - ข้าม src ที่ไม่ใช่ไฟล์ local (hotlink wixstatic — รอรอบ image pipeline)
   - ข้าม src ที่ไฟล์ไม่มีจริง (รายงานเป็น dead src)

วิธีใช้:  python3 tools/add_img_dims.py          # ทั้งรีโป
          python3 tools/add_img_dims.py flexgrip # เฉพาะบางโฟลเดอร์
"""
import glob, os, re, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

GLOBAL_IMG = re.compile(r'(?<![\w.#-])img\s*\{[^}]*\}')
IMG_TAG = re.compile(r'<img\b[^>]*>')
dims_cache = {}


def img_dims(src):
    path = src.lstrip('/')
    if path in dims_cache:
        return dims_cache[path]
    d = None
    if os.path.exists(path):
        try:
            with Image.open(path) as im:
                d = im.size
        except Exception:
            d = None
    dims_cache[path] = d
    return d


def process(page):
    html = open(page, encoding='utf-8').read()
    orig = html
    report = {'added': 0, 'skipped_hotlink': 0, 'dead': [], 'safety': False}

    tags = IMG_TAG.findall(html)
    if not tags:
        return None

    # 1) safety net
    gl = GLOBAL_IMG.search(html)
    if not (gl and 'height:auto' in gl.group(0).replace(' ', '')):
        html = html.replace('</style>', 'img{height:auto}\n</style>', 1)
        report['safety'] = True

    # 2) attributes
    def fix(m):
        tag = m.group(0)
        if re.search(r'\bwidth=', tag) and re.search(r'\bheight=', tag):
            return tag
        sm = re.search(r'src="([^"]+)"', tag)
        if not sm:
            return tag
        src = sm.group(1)
        if not (src.startswith('/img/') or src.startswith('img/')):
            report['skipped_hotlink'] += 1
            return tag
        d = img_dims(src)
        if not d:
            report['dead'].append(src)
            return tag
        w, h = d
        inject = f' width="{w}" height="{h}"'
        # แทรกก่อนตัวปิด (รองรับทั้ง > และ />)
        if tag.endswith('/>'):
            new = tag[:-2].rstrip() + inject + '/>'
        else:
            new = tag[:-1] + inject + '>'
        report['added'] += 1
        return new

    html = IMG_TAG.sub(fix, html)

    if html != orig:
        open(page, 'w', encoding='utf-8').write(html)
    return report


def main():
    targets = sys.argv[1:]
    pages = sorted(glob.glob('**/index.html', recursive=True))
    if targets:
        pages = [p for p in pages if p.split('/')[0] in targets or
                 (p.startswith('en/') and p.split('/')[1] in targets)]
    tot_add = tot_safety = 0
    all_dead = {}
    for p in pages:
        r = process(p)
        if not r:
            continue
        tot_add += r['added']
        tot_safety += 1 if r['safety'] else 0
        if r['dead']:
            all_dead[p] = r['dead']
    print(f"เติม width/height: {tot_add} รูป / เติม safety net img{{height:auto}}: {tot_safety} หน้า")
    if all_dead:
        print("dead src (ไฟล์ไม่มีจริง — ไม่แตะ):")
        for p, ds in all_dead.items():
            for d in ds:
                print(f"  {p}: {d}")


if __name__ == '__main__':
    main()
