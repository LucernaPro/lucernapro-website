#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/check_parity.py — ตรวจ "ความครบถ้วนเหมือนกันทุกหน้า" ของเว็บ LucernaPro

รันก่อน push ทุกครั้ง:  python3 tools/check_parity.py
exit code 0 = ผ่าน / 1 = มีหน้าตกขบวน

ทำไมต้องมีไฟล์นี้: เว็บมีหัวเว็บ 2 ชุด (หน้าสินค้า vs casestudy+post) ที่ถูกก็อปกันไปมา
ทุกครั้งที่เพิ่มฟีเจอร์ที่หัวเว็บ จะมีหน้าตกขบวนเงียบๆ โดยไม่มี error ให้เห็น
(เคยเกิดมาแล้ว 3 รอบ: ลิ้นชักโปร่งแสง / ไม่มี dark mode / ไม่มีปุ่มสลับภาษา)
ไฟล์นี้เปลี่ยนการ "เปิดเจอเอง" ให้เป็นการตรวจอัตโนมัติ

เพิ่มฟีเจอร์ใหม่ที่หัวเว็บเมื่อไหร่ → เพิ่มบรรทัดใน REQUIRED ด้วยทุกครั้ง
"""
import io, os, re, sys, glob
from collections import defaultdict
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# ── ชิ้นส่วนที่ทุกหน้าต้องมี "พอดี 1 ชิ้น" ──────────────────────────────
REQUIRED = [
    ('id="mnavBtn"',        'ปุ่มเปิดลิ้นชักมือถือ'),
    ('id="mnavClose"',      'ปุ่มปิดลิ้นชัก'),
    ('id="mnavScrim"',      'ฉากหลังลิ้นชัก'),
    ('id="themeToggle"',    'ปุ่มสลับธีม (เดสก์ท็อป)'),
    ('id="mnavTheme"',      'ปุ่มสลับธีม (ลิ้นชัก)'),
    ('class="lang-switch"', 'ปุ่มสลับภาษา (เดสก์ท็อป)'),
    ('class="mnav-lang"',   'ปุ่มสลับภาษา (ลิ้นชัก)'),
]
# ต้องมีอย่างน้อย 1 (ปรากฏซ้ำได้)
REQUIRED_ANY = [
    ('[data-theme="dark"]',  'ชุดสีโหมดมืด'),
    ('lucerna-theme',        'สคริปต์จำค่าธีมใน <head>'),
    ('track.js',             'ระบบวัดผล'),
    ('rel="canonical"',      'canonical'),
    ('hreflang=',            'hreflang'),
]

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Struct(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.err=[]; self.ids=[]
    def handle_starttag(self, t, attrs):
        d = dict(attrs)
        if 'id' in d: self.ids.append(d['id'])
        if t not in VOID: self.stack.append(t)
    def handle_endtag(self, t):
        if t in VOID: return
        if t in self.stack:
            i = len(self.stack)-1-self.stack[::-1].index(t)
            if i != len(self.stack)-1: self.err.append('ปิดแท็กสลับลำดับใกล้ </%s>' % t)
            del self.stack[i:]
        else:
            self.err.append('</%s> เกินมา' % t)

def url_to_file(href, files):
    """แปลง href ในเว็บ -> path ไฟล์จริง คืน None ถ้าไม่ใช่ลิงก์ภายใน"""
    if not href.startswith('/') or href.startswith('//'): return None
    p = href.split('#')[0].split('?')[0].strip('/')
    cand = (p + '/index.html') if p else 'index.html'
    return cand if cand in files else False

def main():
    files = sorted(glob.glob('**/index.html', recursive=True))
    fileset = set(files)
    problems = defaultdict(list)
    ids_by_page, meta = {}, {}

    for p in files:
        s = io.open(p, encoding='utf-8').read()
        add = lambda m: problems[p].append(m)

        # 1) โครงสร้าง HTML + id ซ้ำ
        st = Struct(); st.feed(s); st.close()
        for e in st.err: add('HTML: ' + e)
        for t in st.stack: add('HTML: <%s> ไม่ถูกปิด' % t)
        dup = {i for i in st.ids if st.ids.count(i) > 1}
        for d in sorted(dup): add('id ซ้ำ: %s' % d)
        ids_by_page[p] = set(st.ids)

        # 2) ชิ้นส่วนบังคับ
        for needle, label in REQUIRED:
            n = s.count(needle)
            if n != 1: add('%s (%s) ควรมี 1 พบ %d' % (label, needle, n))
        for needle, label in REQUIRED_ANY:
            if needle not in s: add('ขาด %s' % label)

        # 3) ตัวแปร CSS ที่ใช้แต่ไม่เคยประกาศ (ต้นเหตุลิ้นชักโปร่งแสง)
        # ประกาศที่ไหนก็นับ รวม scoped เช่น .v-fast{--tc:...} ซึ่งถูกต้องตามหลัก CSS
        # แต่ถ้าประกาศ "เฉพาะในบล็อก [data-theme=dark]" = โหมดสว่างพังเงียบๆ ต้องจับ
        # var(--x, fallback) ข้ามไป เพราะมีค่าสำรองอยู่แล้ว
        dark = [m.span() for m in re.finditer(r'\[data-theme="[^"]+"\][^{]*\{[^}]*\}', s)]
        in_dark = lambda i: any(a <= i < b for a, b in dark)
        decl = defaultdict(list)
        for m in re.finditer(r'(--[a-z0-9-]+)\s*:', s):
            decl[m.group(1)].append(m.start())
        for used in set(re.findall(r'var\((--[a-z0-9-]+)\s*\)', s)):
            spots = decl.get(used, [])
            if not spots:
                add('ตัวแปร CSS ไม่มีนิยาม: %s' % used)
            elif all(in_dark(i) for i in spots):
                add('ตัวแปร CSS %s ประกาศเฉพาะในโหมดมืด — โหมดสว่างจะพัง' % used)

        # 4) ปุ่มสลับภาษาต้องตรงกับ hreflang ของหน้านั้น และไฟล์ต้องมีจริง
        alt = dict(re.findall(r'hreflang="([a-z-]+)" href="([^"]+)"', s))
        is_en = p.startswith('en/')
        want = alt.get('th' if is_en else 'en')
        for cls in ('lang-switch', 'mnav-lang'):
            m = re.search(r'class="%s" href="([^"]+)"' % cls, s)
            if not m: continue
            href = m.group(1)
            if url_to_file(href, fileset) is False:
                add('%s ชี้ไปหน้าที่ไม่มีอยู่: %s' % (cls, href))
            if want and re.sub(r'^https?://[^/]+', '', want).rstrip('/') != href.rstrip('/'):
                add('%s ไม่ตรงกับ hreflang (ปุ่ม=%s / hreflang=%s)' % (cls, href, want))

        meta[p] = dict(
            title=(re.search(r'<title>(.*?)</title>', s, re.S) or [None, ''])[1].strip(),
            canon=(re.search(r'rel="canonical" href="([^"]+)"', s) or [None, ''])[1],
            src=s, alt=alt)

    # 5) ลิงก์ anchor ต้องมี id ปลายทางอยู่จริง (บั๊ก "สินค้าทั้งหมด" ตรวจเจอด้วยข้อนี้)
    for p in files:
        s = meta[p]['src']
        for href in set(re.findall(r'href="((?:/[a-z/]*)?#[A-Za-z][\w-]*)"', s)):
            page, frag = href.split('#', 1)
            tgt = p if page == '' else url_to_file(page if page.endswith('/') else page + '/', fileset)
            if tgt is False:
                problems[p].append('anchor ชี้หน้าที่ไม่มี: %s' % href); continue
            if tgt and frag not in ids_by_page.get(tgt, set()):
                problems[p].append('anchor #%s ไม่มีอยู่ใน %s' % (frag, tgt))

    # 6) hreflang ต้องจับคู่กลับหากันได้
    for p in files:
        a = meta[p]['alt']
        # หน้าที่ยังไม่มีคู่แปล (เช่น /epoxycoating ที่ /en/ ยังไม่ถูกสร้าง) ถือว่าถูกต้อง
        # ถ้ามันไม่ประกาศ hreflang en ทิ้งไว้ลอยๆ — แต่ถ้ามีไฟล์คู่แล้วต้องประกาศให้ครบ
        mate = ('' if p.startswith('en/') else 'en/') + (p[3:] if p.startswith('en/') else p)
        if mate in fileset:
            if 'th' not in a or 'en' not in a:
                problems[p].append('มีหน้าคู่ %s แล้วแต่ hreflang ไม่ครบคู่' % mate); continue
        else:
            if 'en' in a and 'th' in a and a['en'] != a['th']:
                problems[p].append('ประกาศ hreflang en ทั้งที่ยังไม่มีหน้า %s' % mate)
            continue
        other = url_to_file(re.sub(r'^https?://[^/]+', '', a['th' if p.startswith('en/') else 'en']), fileset)
        if other and meta[other]['alt'] != a:
            problems[p].append('hreflang ไม่ตรงกับหน้าคู่ %s' % other)

    # 7) title / canonical ห้ามซ้ำข้ามหน้า
    for key in ('title', 'canon'):
        seen = defaultdict(list)
        for p in files:
            if meta[p][key]: seen[meta[p][key]].append(p)
        for v, ps in seen.items():
            if len(ps) > 1:
                for p in ps: problems[p].append('%s ซ้ำกับ %s' % (key, [x for x in ps if x != p][0]))

    # 8) ตารางของเครื่องคำนวณต้องอ่านได้จริง
    for p in files:
        s = meta[p]['src']
        if 'data-calc' not in s: continue
        if 'calc.js' not in s: problems[p].append('มี data-calc แต่ไม่ได้โหลด calc.js')

        # หน้าเดียวมีหลาย .pricecard ได้ (เช่น HeatShield มีตัวหลัก + Primer คนละสินค้า)
        # calc.js อ่านเฉพาะตารางที่มี data-calc — annotation ที่หลุดไปติดตารางอื่นคือบั๊ก
        cards = re.findall(r'<div class="pricecard">.*?</table>', s, re.S)
        calc_card = None
        for c in cards:
            if 'data-calc="1"' in c:
                if calc_card is not None:
                    problems[p].append('มีตารางที่ติด data-calc มากกว่า 1 ตาราง — calc.js อ่านแค่ตารางแรก')
                calc_card = c
            elif 'data-sqm="' in c or 'data-price="' in c or 'data-ship="' in c:
                problems[p].append('ตารางที่ไม่มี data-calc แต่มี data-sqm/data-price ติดอยู่ (คนละสินค้า?)')
        if calc_card is None:
            problems[p].append('มี data-calc แต่หาตารางไม่เจอ'); continue
        s = calc_card
        # ตรวจทีละแถว ไม่ใช่แค่ "มีอย่างน้อยหนึ่ง" — แถวที่ตกหล่นจะหายไปจากผลคำนวณเงียบๆ
        # แถวที่ตั้งใจไม่ให้เข้าระบบคำนวณ (เช่น "สอบถาม") ต้องประกาศ data-calc="skip" ให้ชัด
        ok_rows = 0
        for r in re.findall(r'<tr>(?:(?!</tr>).)*?</tr>', s, re.S):
            if 'class="sz"' not in r: continue
            if 'data-calc="skip"' in r: continue
            txt = re.sub(r'<[^>]+>', ' ', r).strip()[:40]
            if 'data-sqm="' not in r:
                problems[p].append('แถวราคาขาด data-sqm (หรือใส่ data-calc="skip"): %s' % txt)
            elif 'data-price="' not in r:
                problems[p].append('แถวมี data-sqm แต่ไม่มี data-price สักช่อง: %s' % txt)
            else:
                # หลายราคาในแถวเดียวได้เฉพาะกรณีเป็นคนละรุ่น (ต้องมี data-variant)
                # ไม่งั้นมักเป็นการเผลอติด data-price ให้ช่อง "ค่าส่ง" ซึ่งจะบวกเข้าราคาสินค้า
                npr = r.count('data-price="')
                if npr > 1 and r.count('data-variant="') != npr:
                    problems[p].append('แถวมี data-price %d ช่องแต่ไม่ได้ประกาศ data-variant ครบ (เผลอติดช่องค่าส่ง?): %s' % (npr, txt))
                ok_rows += 1
        if not ok_rows:
            problems[p].append('มี data-calc แต่ไม่มีแถวที่ใช้งานได้เลย')

    bad = {p: v for p, v in problems.items() if v}
    print('ตรวจ %d หน้า' % len(files))
    if not bad:
        print('ผ่านทั้งหมด — ไม่มีหน้าตกขบวน')
        return 0
    total = sum(len(v) for v in bad.values())
    print('พบปัญหา %d จุด ใน %d หน้า\n' % (total, len(bad)))
    for p in sorted(bad):
        print('  %s' % p)
        for m in bad[p][:8]:
            print('      - %s' % m)
        if len(bad[p]) > 8: print('      - ... อีก %d จุด' % (len(bad[p]) - 8))
    return 1

if __name__ == '__main__':
    sys.exit(main())
