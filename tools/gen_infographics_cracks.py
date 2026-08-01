# -*- coding: utf-8 -*-
"""
gen_infographics_cracks.py — วาด infographic ประกอบโพสต์ why-coating-over-cracks-fails
ผลลัพธ์: /img/post/why-coating-over-cracks-fails-{01..04}{,en}.webp (1200px wide, pipeline q86/q88)

ต้องการในเครื่องที่รัน (sandbox ฝั่ง Claude):
  - rsvg-convert (librsvg2-bin) — ใช้ Pango จัด Thai shaping ถูกต้อง (cairosvg ใช้ toy API วรรณยุกต์เพี้ยน)
  - ฟอนต์ใน fontconfig: "Chakra Petch" (Regular/SemiBold/Bold), "IBM Plex Mono",
    Anuphan static instances rename เป็น family "AnuphanR"/"AnuphanSB"/"AnuphanB"
    (Anuphan บน google/fonts เป็น variable font — Pango เลือกน้ำหนักไม่เสถียร จึง instantiate แยกไฟล์)
  - PIL + fontTools

รัน: python3 tools/gen_infographics_cracks.py (จาก root ของ repo)
"""
import os, subprocess, html
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img", "post")
SLUG = "why-coating-over-cracks-fails"

# palette = โซน casestudy (ธีมกระดาษสว่าง)
PAPER = "#F2F2EF"; CARD = "#FFFFFF"; INK = "#191C1F"; STEEL = "#5E646A"
LINE = "#DCDCD6"; SIGNAL = "#D8571C"; TAG = "#ECECE9"
CONCRETE = "#DDD9CF"; CONCRETE_DK = "#C9C4B7"; WATER = "#3E7CB1"
BAD = "#B23A2E"; GOOD = "#2E7D4F"; BAD_BG = "#F7ECEA"; GOOD_BG = "#EAF2ED"

TH_R, TH_SB, TH_B = "AnuphanR", "AnuphanSB", "AnuphanB"
HEAD = "Chakra Petch"; MONO = "IBM Plex Mono"

def esc(s): return html.escape(s, quote=True)

def T(x, y, s, size, fam=TH_R, fill=INK, anchor="start", weight=None, spacing=None):
    w = f' font-weight="{weight}"' if weight else ""
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}"'
            f' fill="{fill}" text-anchor="{anchor}"{w}{ls}>{esc(s)}</text>\n')

def lines(x, y, rows, size, lh, fam=TH_R, fill=INK, anchor="start", weight=None):
    return "".join(T(x, y + i * lh, r, size, fam, fill, anchor, weight) for i, r in enumerate(rows))

def rrect(x, y, w, h, r, fill, stroke=None, sw=2, dash=None):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{st}{da}/>\n'

def arrow_marker(mid, color):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>\n')

def crack_path(cx, ytop, ybot, amp=7, gap=0):
    """แนวรอยร้าวซิกแซก ตรงกลาง cx / gap>0 = อ้าออก คืน path ซ้าย-ขวา"""
    seg = 6
    ys = [ytop + (ybot - ytop) * i / seg for i in range(seg + 1)]
    xs = [cx + (amp if i % 2 else -amp) for i in range(seg + 1)]
    left = f"M{xs[0]-gap},{ys[0]} " + " ".join(f"L{x-gap},{y}" for x, y in zip(xs[1:], ys[1:]))
    right = f"M{xs[0]+gap},{ys[0]} " + " ".join(f"L{x+gap},{y}" for x, y in zip(xs[1:], ys[1:]))
    return left, right, list(zip(xs, ys))

def svg_doc(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">\n<rect width="{w}" height="{h}" fill="{PAPER}"/>\n'
            f"{body}</svg>")

def brandbar(w, h, label):
    b = f'<line x1="40" y1="{h-52}" x2="{w-40}" y2="{h-52}" stroke="{LINE}" stroke-width="2"/>\n'
    b += T(40, h - 22, "LUCERNAPRO", 20, HEAD, INK, weight="700", spacing="2")
    b += T(178, h - 22, "· lucernapro.com", 18, TH_R, STEEL)
    b += T(w - 40, h - 22, label, 16, MONO, SIGNAL, anchor="end", spacing="1")
    return b

# ============================================================ 01 — กลไกฟิล์มขาด
def ig01(L):
    W, H = 1200, 900
    s = ""
    s += f"<defs>{arrow_marker('aI', INK)}{arrow_marker('aB', BAD)}{arrow_marker('aW', WATER)}</defs>\n"
    s += T(W/2, 74, L["t1"], 46, HEAD, INK, "middle", "700")
    s += T(W/2, 116, L["t1s"], 24, TH_R, STEEL, "middle")

    for px, key, hbg, hcol in ((40, "p1", TAG, INK), (620, "p2", BAD_BG, BAD)):
        s += rrect(px, 150, 540, 470, 16, CARD, LINE)
        s += rrect(px, 150, 540, 56, 16, hbg)
        s += f'<rect x="{px}" y="182" width="540" height="24" fill="{hbg}"/>\n'
        s += T(px + 270, 187, L[key], 24, TH_SB, hcol, "middle")

    # ---- panel A: ทาเสร็จวันแรก
    ax, slab_y, slab_h = 40, 360, 190
    s += rrect(ax + 40, slab_y, 460, slab_h, 0, CONCRETE, CONCRETE_DK, 2)
    for i in range(9):  # จุดหินในเนื้อปูน
        s += f'<circle cx="{ax+72+i*50}" cy="{slab_y+40+(i%3)*48}" r="4" fill="{CONCRETE_DK}"/>\n'
    lp, rp, _ = crack_path(ax + 270, slab_y, slab_y + slab_h)
    s += f'<path d="{lp}" fill="none" stroke="{INK}" stroke-width="3"/>\n'
    film_y = slab_y - 16
    s += rrect(ax + 40, film_y, 460, 16, 3, SIGNAL)
    s += T(ax + 270, film_y - 44, L["filmlbl"], 21, TH_SB, SIGNAL, "middle")
    s += f'<line x1="{ax+270}" y1="{film_y-36}" x2="{ax+270}" y2="{film_y-4}" stroke="{SIGNAL}" stroke-width="2" marker-end="url(#aI)"/>\n'
    s += lines(ax + 270, slab_y + slab_h + 38, L["a_note"], 21, 28, TH_R, STEEL, "middle")

    # ---- panel B: โครงสร้างขยับ ฟิล์มขาด
    bx, gap = 620, 12
    s += rrect(bx + 40, slab_y, 230 - gap, slab_h, 0, CONCRETE, CONCRETE_DK, 2)
    s += rrect(bx + 270 + gap, slab_y, 230 - gap, slab_h, 0, CONCRETE, CONCRETE_DK, 2)
    lp, rp, _ = crack_path(bx + 270, slab_y, slab_y + slab_h, gap=gap)
    s += f'<path d="{lp}" fill="none" stroke="{INK}" stroke-width="3"/>\n'
    s += f'<path d="{rp}" fill="none" stroke="{INK}" stroke-width="3"/>\n'
    # ลูกศรขยับออก
    s += f'<line x1="{bx+205}" y1="{slab_y+slab_h/2}" x2="{bx+140}" y2="{slab_y+slab_h/2}" stroke="{BAD}" stroke-width="4" marker-end="url(#aB)"/>\n'
    s += f'<line x1="{bx+335}" y1="{slab_y+slab_h/2}" x2="{bx+400}" y2="{slab_y+slab_h/2}" stroke="{BAD}" stroke-width="4" marker-end="url(#aB)"/>\n'
    # ฟิล์มขาดสองท่อน ปลายฉีก
    s += rrect(bx + 40, film_y, 214, 16, 3, SIGNAL)
    s += rrect(bx + 286, film_y, 214, 16, 3, SIGNAL)
    s += (f'<path d="M{bx+254},{film_y} l8,4 l-8,4 l8,4 l-8,4" fill="none" stroke="{SIGNAL}" stroke-width="3"/>\n'
          f'<path d="M{bx+286},{film_y} l-8,4 l8,4 l-8,4 l8,4" fill="none" stroke="{SIGNAL}" stroke-width="3"/>\n')
    s += T(bx + 270, film_y - 44, L["tearlbl"], 21, TH_SB, BAD, "middle")
    s += f'<line x1="{bx+270}" y1="{film_y-36}" x2="{bx+270}" y2="{film_y-4}" stroke="{BAD}" stroke-width="2" marker-end="url(#aB)"/>\n'
    # น้ำลงตามรอย
    s += f'<line x1="{bx+270}" y1="{film_y+22}" x2="{bx+270}" y2="{slab_y+slab_h-14}" stroke="{WATER}" stroke-width="3" stroke-dasharray="2 6" marker-end="url(#aW)"/>\n'
    for i, dy in enumerate((0, 26, 52)):
        s += f'<path d="M{bx+270},{slab_y+slab_h+16+dy} q6,10 0,16 q-6,-6 0,-16" fill="{WATER}"/>\n'
    y0 = slab_y + slab_h + 46 - (len(L["b_note"]) - 1) * 14
    s += lines(bx + 300, y0, L["b_note"], 21, 28, TH_R, BAD, "start")

    # แถบเลขล่าง
    s += rrect(40, 650, 1120, 168, 14, CARD, LINE)
    s += T(70, 692, L["numk"], 17, MONO, SIGNAL, spacing="2")
    s += lines(70, 728, L["numtx"], 23, 33, TH_R, INK)
    s += brandbar(W, H, "CASE STUDY 01/04")
    return svg_doc(W, H, s)

# ============================================================ 02 — วงจรไม่จบ vs จบ
def ig02(L):
    W, H = 1200, 900
    s = f"<defs>{arrow_marker('bB', BAD)}{arrow_marker('bG', GOOD)}</defs>\n"
    s += T(W/2, 74, L["t2"], 46, HEAD, INK, "middle", "700")
    s += T(W/2, 116, L["t2s"], 24, TH_R, STEEL, "middle")

    def col(x, hdr, hcol, hbg, boxes, footer, loop):
        b = rrect(x, 150, 540, 620, 16, CARD, LINE)
        b += rrect(x, 150, 540, 56, 16, hbg)
        b += f'<rect x="{x}" y="182" width="540" height="24" fill="{hbg}"/>\n'
        b += T(x + 270, 187, hdr, 25, TH_B, hcol, "middle")
        n = len(boxes); bh = 74; gap0 = (560 - n * bh) / (n - 1) if n > 1 else 0
        gap0 = min(gap0, 34)
        total = n * bh + (n - 1) * gap0
        y0 = 206 + (520 - total) / 2
        cx = x + 270
        for i, rows in enumerate(boxes):
            by = y0 + i * (bh + gap0)
            last = (i == n - 1)
            fill = (GOOD if (last and not loop) else TAG)
            tcol = ("#FFFFFF" if (last and not loop) else INK)
            b += rrect(x + 70, by, 400, bh, 10, fill, LINE if fill == TAG else None)
            if len(rows) == 1:
                b += T(cx, by + bh/2 + 8, rows[0], 22, TH_SB, tcol, "middle")
            else:
                b += T(cx, by + 31, rows[0], 22, TH_SB, tcol, "middle")
                b += T(cx, by + 59, rows[1], 20, TH_R, tcol if fill != TAG else STEEL, "middle")
            if i < n - 1:
                col_ = GOOD if not loop else BAD
                b += (f'<line x1="{cx}" y1="{by+bh+3}" x2="{cx}" y2="{by+bh+gap0-3}" '
                      f'stroke="{col_}" stroke-width="3" marker-end="url(#{"bG" if not loop else "bB"})"/>\n')
        if loop:  # ลูกศรวนกลับขึ้นด้านซ้าย
            ytop = y0 + bh/2; ybot = y0 + (n-1) * (bh + gap0) + bh/2
            b += (f'<path d="M{x+68},{ybot} L{x+34},{ybot} L{x+34},{ytop} L{x+62},{ytop}" fill="none" '
                  f'stroke="{BAD}" stroke-width="3.5" stroke-dasharray="7 6" marker-end="url(#bB)"/>\n')
            b += f'<g transform="rotate(-90 {x+34} {(ytop+ybot)/2})">' + \
                 T(x+34, (ytop+ybot)/2 - 8, L["loop"], 19, TH_SB, BAD, "middle") + "</g>\n"
        b += T(x + 270, 742, footer, 21, TH_SB, hcol, "middle")
        return b

    s += col(40, L["c1h"], BAD, BAD_BG, L["c1"], L["c1f"], loop=True)
    s += col(620, L["c2h"], GOOD, GOOD_BG, L["c2"], L["c2f"], loop=False)
    s += brandbar(W, H, "CASE STUDY 02/04")
    return svg_doc(W, H, s)

# ============================================================ 03 — น้ำเดินใต้ฟิล์ม
def ig03(L):
    W, H = 1200, 780
    s = f"<defs>{arrow_marker('cW', WATER)}{arrow_marker('cI', INK)}</defs>\n"
    s += T(W/2, 74, L["t3"], 44, HEAD, INK, "middle", "700")
    s += T(W/2, 116, L["t3s"], 24, TH_R, STEEL, "middle")

    sx, sy, sw, sh = 80, 280, 1040, 170
    s += rrect(sx, sy, sw, sh, 0, CONCRETE, CONCRETE_DK, 2)
    for i in range(18):
        s += f'<circle cx="{sx+40+i*56}" cy="{sy+36+(i%3)*52}" r="4" fill="{CONCRETE_DK}"/>\n'
    film_y = sy - 16
    crack_x = sx + 210
    # ฟิล์มขาดตรงรอย
    s += rrect(sx, film_y, crack_x - sx - 12, 16, 3, SIGNAL)
    s += rrect(crack_x + 12, film_y, sx + sw - crack_x - 12, 16, 3, SIGNAL)
    lp, rp, _ = crack_path(crack_x, sy, sy + sh, amp=6, gap=4)
    s += f'<path d="{lp}" fill="none" stroke="{INK}" stroke-width="3"/>\n'
    s += f'<path d="{rp}" fill="none" stroke="{INK}" stroke-width="3"/>\n'
    # ถุงน้ำใต้ฟิล์ม (blister)
    bxc = crack_x + 190
    s += f'<path d="M{bxc-70},{film_y+16} q70,-54 140,0 z" fill="{SIGNAL}" opacity="0.25"/>\n'
    s += f'<path d="M{bxc-70},{film_y+16} q70,-54 140,0" fill="none" stroke="{SIGNAL}" stroke-width="6"/>\n'
    # เส้นทางน้ำ: ลงรอย → เดินในเนื้อปูน → หยดปลายอีกฝั่ง
    exit_x = sx + 830
    s += (f'<path d="M{crack_x},{film_y-30} L{crack_x},{sy+70} Q{crack_x+40},{sy+112} {crack_x+120},{sy+112} '
          f'L{exit_x-60},{sy+112} Q{exit_x},{sy+112} {exit_x},{sy+sh-8}" fill="none" '
          f'stroke="{WATER}" stroke-width="4" stroke-dasharray="3 8" marker-end="url(#cW)"/>\n')
    for dy in (14, 44, 74):
        s += f'<path d="M{exit_x},{sy+sh+dy} q7,11 0,18 q-7,-7 0,-18" fill="{WATER}"/>\n'
    # ป้ายกำกับสามจุด
    s += T(crack_x, film_y - 66, L["pin1"], 22, TH_B, BAD, "middle")
    s += f'<line x1="{crack_x}" y1="{film_y-58}" x2="{crack_x}" y2="{film_y-26}" stroke="{BAD}" stroke-width="2.5" marker-end="url(#cI)"/>\n'
    s += T(bxc, film_y - 66, L["pin2"], 22, TH_SB, SIGNAL, "middle")
    s += f'<line x1="{bxc}" y1="{film_y-58}" x2="{bxc}" y2="{film_y-40}" stroke="{SIGNAL}" stroke-width="2.5" marker-end="url(#cI)"/>\n'
    s += T((crack_x + exit_x)/2 + 60, sy + 92, L["pin3"], 21, TH_SB, WATER, "middle")
    s += lines(exit_x, sy + sh + 122, L["pin4"], 22, 30, TH_B, WATER, "middle")

    s += rrect(40, sy + sh + 168, 1120, 84, 14, CARD, LINE)
    s += lines(W/2, sy + sh + 202, L["note3"], 23, 32, TH_SB, INK, "middle")
    s += brandbar(W, H, "CASE STUDY 03/04")
    return svg_doc(W, H, s)

# ============================================================ 04 — routing ตัวโป๊ว
def ig04(L):
    W, H = 1200, 900
    s = ""
    s += T(W/2, 74, L["t4"], 46, HEAD, INK, "middle", "700")
    s += T(W/2, 116, L["t4s"], 24, TH_R, STEEL, "middle")
    cw, ch = 540, 250
    pos = [(40, 150), (620, 150), (40, 424), (620, 424)]
    for (x, y), c in zip(pos, L["cards"]):
        s += rrect(x, y, cw, ch, 16, CARD, LINE)
        s += rrect(x, y, 10, ch, 5, SIGNAL)
        s += T(x + 42, y + 62, c["name"], 34, HEAD, SIGNAL, weight="700")
        s += rrect(x + 42, y + 86, c["bw"], 40, 8, TAG)
        s += T(x + 42 + c["bw"]/2, y + 113, c["surf"], 21, TH_SB, INK, "middle")
        s += lines(x + 42, y + 168, c["tx"], 21, 30, TH_R, STEEL)
    s += rrect(40, 706, 1120, 96, 14, INK)
    s += lines(W/2, 748, L["foot4"], 24, 34, TH_SB, "#FFFFFF", "middle")
    s += brandbar(W, H, "CASE STUDY 04/04")
    return svg_doc(W, H, s)

# ============================================================ ข้อความสองภาษา
TH = {
 "t1": "ทำไมทากันซึมทับรอยร้าว แล้วไม่รอด",
 "t1s": "ฟิล์มกันซึมหนาแค่ระดับมิลลิเมตร แต่ต้องรับการขยับของโครงสร้างทั้งหมดไว้ที่เส้นเดียว",
 "p1": "วันที่ทาเสร็จ — ดูเหมือนจบ", "p2": "พอโครงสร้างขยับ (ร้อนสลับเย็นทุกวัน)",
 "filmlbl": "ฟิล์มพาดข้ามรอยร้าว ไม่ได้อุดข้างใน",
 "tearlbl": "ฟิล์มขาดตามแนวรอยเดิมเป๊ะ",
 "a_note": ["ข้างใต้ฟิล์มยังเป็นโพรงว่างตามแนวรอย"],
 "b_note": ["น้ำกลับเข้าเส้นทางเดิมทันที"],
 "numk": "เหตุผลเชิงตัวเลข",
 "numtx": ["สเปก \u201cยืดได้หลายร้อยเปอร์เซ็นต์\u201d วัดจากการดึงฟิล์มทั้งผืนครั้งเดียว — แต่หน้างานจริงฟิล์มถูกยึดแน่นกับปูนสองฝั่ง",
           "ช่วงที่ยืดได้เหลือแค่ความกว้างรอยร้าว: รอย 0.5 มม. อ้าเพิ่มอีก 0.5 มม. = ฟิล์มตรงเส้นนั้นต้องยืด 100%",
           "แล้วโดนดึง-หดแบบนี้ซ้ำทุกวัน ไม่ใช่ครั้งเดียวเหมือนตอนเทสต์ — วัสดุอะไรก็ล้าและขาดในที่สุด"],
 "t2": "ทางลัด vs ทางที่จบ",
 "t2s": "ลำดับเหตุการณ์ที่เราเจอซ้ำจากหน้างานจริง จนเดาตอนจบได้",
 "c1h": "ทาทับเลย (ทางลัด)", "c1f": "จ่ายค่าของ + ค่าแรงซ้ำทุกรอบ ต้นเหตุอยู่ครบ",
 "c1": [["ทากันซึมทับรอยร้าว"], ["1–3 เดือนแรก", "ทุกอย่างดูเรียบร้อยดี"],
        ["โครงสร้างขยับ", "ฟิล์มขาดตามแนวรอยเดิม"], ["รั่วซ้ำจุดเดิม", "ซื้อมาทาใหม่อีกรอบ"]],
 "loop": "วนไปเรื่อยๆ",
 "c2h": "โป๊วก่อนทา (ทางที่จบ)", "c2f": "เพิ่มงานวันเดียว ตัดวงจรทิ้งทั้งเส้น",
 "c2": [["เปิดร่อง ทำความสะอาดรอยร้าว"], ["โป๊วให้เต็ม ปาดเรียบเสมอผิว"],
        ["รอเซ็ตตัวเต็มที่ตามคู่มือ"], ["ทากันซึมทับตามระบบปกติ"], ["จบ ไม่ต้องกลับมาอีก"]],
 "t3": "จุดที่น้ำหยด ไม่ใช่จุดที่ร้าว",
 "t3s": "น้ำเดินตามโพรงในเนื้อปูนและช่องว่างใต้ฟิล์มได้ไกลเป็นเมตร",
 "pin1": "จุดร้าวจริง", "pin2": "ฟิล์มพองเป็นถุงน้ำ",
 "pin3": "น้ำเดินตามโพรงในเนื้อปูน",
 "pin4": ["จุดที่เห็นน้ำหยด", "ห่างจากรอยจริงได้เป็นเมตร"],
 "note3": ["ทาซ้ำตรงจุดที่หยดเลยไม่หายสักที — ต้องกลับไปหาจุดร้าวตัวจริงแล้วโป๊วให้ถูกจุดก่อน"],
 "t4": "รอยร้าวแบบไหน โป๊วด้วยตัวไหน",
 "t4s": "เลือกตัวโป๊วให้ตรงหน้างาน แล้วค่อยทากันซึมทับเป็นขั้นตอนสุดท้าย",
 "cards": [
  {"name": "PatchPro", "surf": "พื้น / ดาดฟ้าคอนกรีต", "bw": 250,
   "tx": ["รอยร้าว หลุมบ่อ งานซ่อมพื้นทุกชนิด", "ก่อนลงกันซึมหรือเคลือบทับ"]},
  {"name": "FillerAce", "surf": "ผนังปูน / คอนกรีต", "bw": 250,
   "tx": ["รอยร้าวเส้นผมต้องเจียรเปิดร่องก่อน", "ให้เนื้อโป๊วลงไปเต็ม ไม่ใช่ปิดแค่ปากรอย"]},
  {"name": "SpackleFlex", "surf": "หลังคาเมทัลชีท", "bw": 240,
   "tx": ["รอยซ้อนแผ่น หัวสกรู สันหลังคา", "งานหลังคาโลหะเท่านั้น ไม่ใช่พื้นปูน"]},
  {"name": "DeepStick", "surf": "รอยต่อโหดพิเศษ", "bw": 220,
   "tx": ["ผิวลื่นอย่างแผ่น Smartboard งานใต้น้ำ", "รอยต่อที่ตัวอื่นเอาไม่อยู่"]},
 ],
 "foot4": ["กติกาเดียวกันทุกตัว: โป๊วให้เต็ม ปาดเรียบ รอเซ็ตตัวเต็มที่ แล้วค่อยทากันซึมทับ"],
}

EN = {
 "t1": "Why Coating Over a Crack Never Holds",
 "t1s": "A waterproofing film is millimeters thick — yet one line has to absorb all the structure's movement",
 "p1": "Day one — looks finished", "p2": "Then the structure moves (hot-cold, every day)",
 "filmlbl": "Film bridges the crack — the void stays hollow",
 "tearlbl": "Film tears along the exact same line",
 "a_note": ["Under the film, the crack is still an open void"],
 "b_note": ["Water is straight back", "on its old route"],
 "numk": "THE NUMBERS",
 "numtx": ["A \u201cstretches several hundred percent\u201d spec is measured by pulling a whole free film, once.",
           "On site the film is bonded tight on both sides — the only part that can stretch is the crack width itself:",
           "a 0.5 mm crack opening another 0.5 mm = 100% strain on that line, cycling daily. Every material fatigues and tears."],
 "t2": "The Shortcut vs. The Fix",
 "t2s": "The sequence we see on real jobs, so often we can predict the ending",
 "c1h": "Coat straight over (shortcut)", "c1f": "Materials + labor paid again every round; the cause never left",
 "c1": [["Coat over the crack"], ["First 1–3 months", "everything looks fine"],
        ["Structure moves", "film tears along the old line"], ["Same leak returns", "buy more, coat again"]],
 "loop": "and repeat",
 "c2h": "Fill first, then coat (the fix)", "c2f": "One extra day of work — cuts the whole loop",
 "c2": [["Open up and clean the crack"], ["Fill completely, trowel flush"],
        ["Let it fully set per the manual"], ["Coat with your waterproofing system"], ["Done. No coming back."]],
 "t3": "Where It Drips Is Not Where It Cracked",
 "t3s": "Water travels meters through voids in the concrete and gaps under the film",
 "pin1": "The real crack", "pin2": "Film blisters into a water pocket",
 "pin3": "Water travels through voids in the slab",
 "pin4": ["Where you see the drip —", "meters away from the real crack"],
 "note3": ["That's why recoating the drip spot never works — find the real crack and fill it first"],
 "t4": "Which Crack Gets Which Filler",
 "t4s": "Match the filler to the surface, then waterproof over it as the final step",
 "cards": [
  {"name": "PatchPro", "surf": "Floors / concrete decks", "bw": 280,
   "tx": ["Cracks, potholes, all floor repair", "before any waterproofing or coating"]},
  {"name": "FillerAce", "surf": "Cement / concrete walls", "bw": 280,
   "tx": ["Hairline cracks must be ground open first", "so filler goes in full-depth, not just capping"]},
  {"name": "SpackleFlex", "surf": "Metal-sheet roofs", "bw": 240,
   "tx": ["Sheet overlaps, screw heads, ridge lines", "metal roof work only — not concrete decks"]},
  {"name": "DeepStick", "surf": "The brutal joints", "bw": 220,
   "tx": ["Slick surfaces like Smartboard, underwater work,", "joints nothing else can hold"]},
 ],
 "foot4": ["Same rule for all of them: fill completely, trowel flush, let it fully set — then coat over"],
}

# ============================================================ render
def render(name, svg, q):
    svg_path = f"/tmp/{name}.svg"; png_path = f"/tmp/{name}.png"
    with open(svg_path, "w", encoding="utf-8") as f: f.write(svg)
    subprocess.run(["rsvg-convert", "--zoom", "2", "-o", png_path, svg_path], check=True)
    im = Image.open(png_path).convert("RGB")
    im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    out = os.path.join(OUT, f"{name}.webp")
    im.save(out, "WEBP", quality=q, method=6)
    print("built:", out, im.size)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for lang, D, suf in (("th", TH, ""), ("en", EN, "en")):
        render(f"{SLUG}-01{suf}", ig01(D), 88 if suf == "" else 86)
        render(f"{SLUG}-02{suf}", ig02(D), 86)
        render(f"{SLUG}-03{suf}", ig03(D), 86)
        render(f"{SLUG}-04{suf}", ig04(D), 86)
