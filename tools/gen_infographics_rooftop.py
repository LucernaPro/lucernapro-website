# -*- coding: utf-8 -*-
"""
gen_infographics_rooftop.py — infographic ประกอบโพสต์ rooftop-concrete-or-tile
ผลลัพธ์: /img/post/rooftop-concrete-or-tile-hero{,-en}.webp   (hero: ปูนเปลือย vs ปูกระเบื้อง)
         /img/post/rooftop-concrete-or-tile-path-{th,en}.webp  (น้ำเดินใต้กระเบื้อง)
         /img/post/rooftop-concrete-or-tile-decide-{th,en}.webp (แผนผังตัดสินใจ)
ต้องการ: rsvg-convert + ฟอนต์ตามหมายเหตุใน gen_infographics_cracks.py
รัน: python3 tools/gen_infographics_rooftop.py (จาก root ของ repo)
"""
import os, subprocess, html, random
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img", "post")
SLUG = "rooftop-concrete-or-tile"

PAPER = "#F2F2EF"; CARD = "#FFFFFF"; INK = "#191C1F"; STEEL = "#5E646A"
LINE = "#DCDCD6"; SIGNAL = "#D8571C"
CONCRETE = "#DDD9CF"; CONCRETE_DK = "#C9C4B7"; WATER = "#3E7CB1"
BAD = "#B23A2E"; GOOD = "#2E7D4F"; BAD_BG = "#F7ECEA"; GOOD_BG = "#EAF2ED"
TILE = "#EAE4D8"; TILE_DK = "#DCD4C2"; GROUT = "#4A4F55"; MORTAR = "#CFC8B8"
SKY = "#E8EDF1"

TH_R, TH_SB, TH_B = "AnuphanR", "AnuphanSB", "AnuphanB"
HEAD = "Chakra Petch"; MONO = "IBM Plex Mono"

def esc(s): return html.escape(s, quote=True)

def T(x, y, s, size, fam=TH_R, fill=INK, anchor="start", weight=None, spacing=None, opacity=None):
    w = f' font-weight="{weight}"' if weight else ""
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    op = f' opacity="{opacity}"' if opacity else ""
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}"'
            f' fill="{fill}" text-anchor="{anchor}"{w}{ls}{op}>{esc(s)}</text>\n')

def rrect(x, y, w, h, r, fill, stroke=None, sw=2, dash=None, opacity=None):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    op = f' opacity="{opacity}"' if opacity else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{st}{da}{op}/>\n'

def arrow_marker(mid, color):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" '
            f'markerHeight="6.5" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>\n')

def speckle(x, y, w, h, n, color, rmin=1.4, rmax=2.6, seed=7):
    rnd = random.Random(seed); s = ""
    for _ in range(n):
        s += (f'<circle cx="{x+rnd.uniform(6,w-6):.0f}" cy="{y+rnd.uniform(6,h-6):.0f}" '
              f'r="{rnd.uniform(rmin,rmax):.1f}" fill="{color}"/>\n')
    return s

def numdot(x, y, n, color=SIGNAL):
    return (f'<circle cx="{x}" cy="{y}" r="15" fill="{color}"/>'
            + T(x, y+6, str(n), 17, MONO, "#fff", "middle", "600"))

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

def tilegrid(x, y, w, h, cols, rows, hot=None):
    """ผืนกระเบื้อง มองบน — hot = (c,r) ร่องที่ไฮไลต์"""
    s = rrect(x, y, w, h, 0, GROUT)
    g = 6  # ความกว้างร่อง
    cw = (w - g*(cols+1)) / cols; rh = (h - g*(rows+1)) / rows
    for c in range(cols):
        for r in range(rows):
            tx = x + g + c*(cw+g); ty = y + g + r*(rh+g)
            fill = TILE if (c+r) % 2 == 0 else TILE_DK
            s += rrect(tx, ty, cw, rh, 2, fill)
    if hot:
        c, r = hot
        hx = x + g + c*(cw+g) + cw
        s += f'<rect x="{hx:.0f}" y="{y+4}" width="{g+1}" height="{h-8}" fill="{BAD}" opacity=".85"/>\n'
    return s

# ============================================================ HERO — ปูนเปลือย vs ปูกระเบื้อง
def hero(L):
    W, H = 1200, 900
    s = T(W/2, 68, L["t"], 41, HEAD, INK, "middle", "700")
    s += T(W/2, 108, L["ts"], 23, TH_R, STEEL, "middle")

    py, ph = 170, 560; pw = 520
    # ── ซ้าย: ปูนเปลือย
    x = 60
    s += rrect(x, py, pw, ph, 14, CARD, LINE, 2)
    s += T(x+26, py+46, L["cL"], 25, TH_B, INK, weight="700")
    s += T(x+26, py+78, L["cLs"], 18, TH_R, STEEL)
    # ผืนปูน
    cx, cy, cw2, ch2 = x+26, py+104, pw-52, 330
    s += rrect(cx, cy, cw2, ch2, 6, CONCRETE, LINE, 2)
    s += speckle(cx, cy, cw2, ch2, 110, CONCRETE_DK, seed=13)
    # รอยแตกลายงา
    s += (f'<path d="M{cx+70},{cy+40} l38,52 l-16,44 l42,58 l-10,46" stroke="{BAD}" '
          f'stroke-width="3" fill="none" stroke-linecap="round"/>\n')
    s += (f'<path d="M{cx+108},{cy+92} l52,18 l40,-12" stroke="{BAD}" '
          f'stroke-width="2.4" fill="none" stroke-linecap="round"/>\n')
    s += (f'<path d="M{cx+300},{cy+90} l30,60 l-12,50 l34,66" stroke="{BAD}" '
          f'stroke-width="3" fill="none" stroke-linecap="round"/>\n')
    s += (f'<path d="M{cx+330},{cy+150} l56,20" stroke="{BAD}" '
          f'stroke-width="2.4" fill="none" stroke-linecap="round"/>\n')
    s += T(x+26+ (pw-52)/2, cy+ch2+38, L["cLc"], 18.5, TH_SB, BAD, "middle")
    s += T(x+26+ (pw-52)/2, py+ph-28, L["cLb"], 18, TH_R, STEEL, "middle")

    # ── ขวา: ปูกระเบื้อง
    x = 60 + pw + 40  # 620
    s += rrect(x, py, pw, ph, 14, CARD, LINE, 2)
    s += T(x+26, py+46, L["cR"], 25, TH_B, INK, weight="700")
    s += T(x+26, py+78, L["cRs"], 18, TH_R, STEEL)
    s += tilegrid(x+26, py+104, pw-52, 330, 4, 3, hot=(1, 0))
    s += T(x+26+ (pw-52)/2, py+104+330+38, L["cRc"], 18.5, TH_SB, BAD, "middle")
    s += T(x+26+ (pw-52)/2, py+ph-28, L["cRb"], 18, TH_R, STEEL, "middle")

    # VS ตรงกลาง
    s += f'<circle cx="{W/2}" cy="{py+ph/2}" r="42" fill="{SIGNAL}"/>\n'
    s += T(W/2, py+ph/2+10, "VS", 30, HEAD, "#fff", "middle", "700")

    s += T(W/2, py+ph+58, L["foot"], 20, TH_SB, INK, "middle")
    s += brandbar(W, H, "CASE STUDY · ROOFTOP")
    return svg_doc(W, H, s)

TH_HERO = dict(
    t="ดาดฟ้ารั่ว — คำถามแรกจากเราไม่ใช่ราคา",
    ts="แต่คือ: ดาดฟ้าของคุณเป็นปูนเปลือย หรือปูกระเบื้อง?",
    cL="ดาดฟ้าปูนเปลือย", cLs="น้ำซึมผ่านรอยแตกและรอยต่อโดยตรง",
    cLc="ทางน้ำเข้า: รอยแตกลายงา · รอยต่อ · ปากท่อ",
    cLb="จุดรั่วกับจุดที่เห็นน้ำ มักอยู่ใกล้กัน",
    cR="ดาดฟ้าปูกระเบื้อง", cRs="หน้ากระเบื้องกันน้ำ แต่ร่องยาแนวไม่กัน",
    cRc="ทางน้ำเข้า: ร่องยาแนวที่เสื่อม",
    cRb="น้ำมุดลงไปเดินใต้กระเบื้อง — โผล่คนละจุดกับที่เข้า",
    foot="สองพื้นผิว = สองแผนงาน — ตอบคำถามนี้ก่อน ถึงจะเลือกระบบถูก",
)
EN_HERO = dict(
    t="Leaking rooftop? Our first question isn't the price",
    ts="It's this: bare concrete deck, or tiled deck?",
    cL="Bare concrete deck", cLs="Water goes straight through cracks and joints",
    cLc="Entry points: hairline cracks · joints · drains",
    cLb="The leak and the drip are usually close together",
    cR="Tiled deck", cRs="Tiles block water — grout lines don't",
    cRc="Entry point: failing grout lines",
    cRb="Water travels under the tiles — and exits somewhere else",
    foot="Two surfaces = two different game plans. Answer this first, then pick the system.",
)

# ============================================================ PATH — น้ำเดินใต้กระเบื้อง (หน้าตัด)
def path(L):
    W, H = 1200, 900
    s = f"<defs>{arrow_marker('aW', WATER)}{arrow_marker('aB', BAD)}</defs>\n"
    s += T(W/2, 64, L["t"], 40, HEAD, INK, "middle", "700")
    s += T(W/2, 102, L["ts"], 22, TH_R, STEEL, "middle")

    x0, x1 = 100, 1100; w = x1 - x0
    # ฟ้า/ฝน
    s += rrect(x0, 140, w, 120, 0, SKY)
    rnd = random.Random(3)
    for _ in range(26):
        rx = x0 + rnd.uniform(16, w-16); ry = 152 + rnd.uniform(0, 84)
        s += (f'<line x1="{rx:.0f}" y1="{ry:.0f}" x2="{rx-5:.0f}" y2="{ry+15:.0f}" '
              f'stroke="{WATER}" stroke-width="2.4" stroke-linecap="round" opacity=".55"/>\n')
    s += T(x0+18, 172, L["rain"], 18, TH_SB, STEEL)

    # ชั้นกระเบื้อง
    ty, th = 260, 46
    g = 7; cols = 8; cw = (w - g*(cols+1)) / cols
    s += rrect(x0, ty, w, th, 0, GROUT)
    entry_i = 2
    for c in range(cols):
        tx = x0 + g + c*(cw+g)
        s += rrect(tx, ty+4, cw, th-8, 2, TILE if c % 2 == 0 else TILE_DK)
    entry_x = x0 + g + entry_i*(cw+g) + cw + g/2
    s += f'<rect x="{entry_x-5:.0f}" y="{ty+2}" width="10" height="{th-4}" fill="{BAD}"/>\n'
    s += T(x0+w-8, ty+30, L["tile"], 17, TH_SB, "#8A8375", "end")

    # ชั้นปูนกาว (ทางเดินน้ำ)
    my, mh = ty+th, 46
    s += rrect(x0, my, w, mh, 0, MORTAR)
    s += speckle(x0, my, w, mh, 46, "#BCB49F", seed=9)
    s += T(x0+w-8, my+30, L["mortar"], 17, TH_SB, "#9A8F72", "end")

    # พื้นคอนกรีต
    sy, sh = my+mh, 120
    s += rrect(x0, sy, w, sh, 0, CONCRETE, LINE, 2)
    s += speckle(x0, sy, w, sh, 90, CONCRETE_DK, seed=11)
    s += T(x0+w-8, sy+34, L["slab"], 17, TH_SB, "#8A8375", "end")
    # รอยร้าวในพื้น ฝั่งขวา
    exit_x = x0 + w - 250
    s += (f'<path d="M{exit_x},{sy} l8,34 l-10,30 l9,32 l-6,24" stroke="{BAD}" '
          f'stroke-width="3" fill="none" stroke-linecap="round"/>\n')

    # ฝ้าเพดานห้องข้างล่าง
    cy2 = sy + sh + 44
    s += rrect(x0, cy2, w, 10, 0, "#B9B3A4")
    s += T(x0+8, cy2+40, L["ceil"], 17, TH_SB, STEEL)
    # หยดน้ำ + วงคราบ
    s += f'<ellipse cx="{exit_x}" cy="{cy2+5}" rx="60" ry="7" fill="#A89F8E" opacity=".5"/>\n'
    for k, dy in enumerate((26, 58, 92)):
        s += (f'<path d="M{exit_x},{cy2+dy} q6,9 0,17 q-6,-8 0,-17" '
              f'fill="{WATER}" opacity="{0.9-0.2*k}"/>\n')

    # เส้นทางน้ำ: ลงร่อง → เดินขวาใต้กระเบื้อง → ลงรอยร้าว → หยด
    midm = my + mh/2
    s += (f'<path d="M{entry_x},{ty-24} L{entry_x},{midm}" stroke="{WATER}" '
          f'stroke-width="6" marker-end="url(#aW)" fill="none"/>\n')
    s += (f'<path d="M{entry_x},{midm} L{exit_x-14},{midm}" stroke="{WATER}" '
          f'stroke-width="6" stroke-dasharray="14 9" marker-end="url(#aW)" fill="none"/>\n')
    s += (f'<path d="M{exit_x},{midm} L{exit_x},{cy2-8}" stroke="{WATER}" '
          f'stroke-width="6" marker-end="url(#aW)" fill="none"/>\n')

    # ป้ายกำกับสองจุด
    s += numdot(entry_x, ty-52, 1, BAD)
    s += T(entry_x+26, ty-46, L["p1"], 19, TH_B, BAD, weight="700")
    s += numdot(exit_x, cy2+140, 2, SIGNAL)
    s += T(exit_x-26, cy2+146, L["p2"], 19, TH_B, SIGNAL, "end", "700")
    # ระยะห่าง
    by = cy2 + 176
    s += (f'<line x1="{entry_x}" y1="{by}" x2="{exit_x}" y2="{by}" stroke="{INK}" '
          f'stroke-width="2.4" marker-start="url(#aB)" marker-end="url(#aB)"/>\n')
    s += T((entry_x+exit_x)/2, by+30, L["gap"], 19, TH_SB, INK, "middle")

    s += brandbar(W, H, "CASE STUDY · ROOFTOP")
    return svg_doc(W, H, s)

TH_PATH = dict(
    t="กับดักของดาดฟ้าปูกระเบื้อง: น้ำเดินใต้กระเบื้อง",
    ts="จุดที่เห็นน้ำหยดในบ้าน แทบไม่เคยตรงกับจุดที่น้ำเข้า",
    rain="ฝนตกทั้งผืน", tile="กระเบื้อง + ร่องยาแนว", mortar="ชั้นปูนกาว — ทางเดินน้ำ",
    slab="พื้นคอนกรีตดาดฟ้า", ceil="ฝ้าห้องชั้นบนสุด",
    p1="จุดที่น้ำเข้า: ร่องยาแนวที่เสื่อม",
    p2="จุดที่เห็นน้ำหยด: รอยร้าวอีกฝั่ง",
    gap="สองจุดนี้ห่างกันได้หลายเมตร — ซ่อมเฉพาะจุดที่หยดจึงมักไม่จบ",
)
EN_PATH = dict(
    t="The tiled-deck trap: water travels under the tiles",
    ts="The spot dripping into your house is almost never where the water got in",
    rain="Rain over the whole deck", tile="Tiles + grout lines", mortar="Adhesive bed — the water highway",
    slab="Concrete roof slab", ceil="Top-floor ceiling",
    p1="Entry point: a failing grout line",
    p2="Drip point: a crack on the far side",
    gap="These two points can be metres apart — patching the drip spot rarely ends it",
)

# ============================================================ DECIDE — แผนผังเลือกระบบ
def card(x, y, w, h, title, lines, tone, L, tag=None):
    bg = {"good": GOOD_BG, "bad": BAD_BG, "plain": CARD}[tone]
    bd = {"good": GOOD, "bad": BAD, "plain": LINE}[tone]
    s = rrect(x, y, w, h, 12, bg, bd, 2)
    ty = y + 40
    if tag:
        s += T(x+22, ty, tag, 14, MONO, SIGNAL, spacing="1"); ty += 32
    s += T(x+22, ty, title, 21, TH_B, INK, weight="700"); ty += 32
    for ln in lines:
        s += T(x+22, ty, ln, 17.5, TH_R, STEEL); ty += 27
    return s

def decide(L):
    W, H = 1200, 900
    s = f"<defs>{arrow_marker('aI', INK)}</defs>\n"
    s += T(W/2, 62, L["t"], 40, HEAD, INK, "middle", "700")
    s += T(W/2, 100, L["ts"], 22, TH_R, STEEL, "middle")

    # กล่องคำถามบนสุด
    qw, qh = 560, 64; qx, qy = (W-qw)/2, 130
    s += rrect(qx, qy, qw, qh, 12, INK)
    s += T(W/2, qy+40, L["q"], 22, TH_B, "#fff", "middle", "700")

    # เส้นแยกซ้าย/ขวา
    lx, rx = 330, 870; by = 250
    s += (f'<path d="M{W/2},{qy+qh} L{W/2},{qy+qh+18} L{lx},{qy+qh+18} L{lx},{by-10}" '
          f'stroke="{INK}" stroke-width="2.6" fill="none" marker-end="url(#aI)"/>\n')
    s += (f'<path d="M{W/2},{qy+qh+18} L{rx},{qy+qh+18} L{rx},{by-10}" '
          f'stroke="{INK}" stroke-width="2.6" fill="none" marker-end="url(#aI)"/>\n')

    colw = 470
    # ── ซ้าย: ปูนเปลือย
    x = lx - colw/2
    s += T(lx, by+30, L["cL"], 24, TH_B, INK, "middle", "700")
    s += card(x, by+52, colw, 150, L["l1t"], L["l1"], "plain", L, tag="STEP 1")
    s += (f'<line x1="{lx}" y1="{by+202}" x2="{lx}" y2="{by+226}" stroke="{INK}" '
          f'stroke-width="2.6" marker-end="url(#aI)"/>\n')
    s += card(x, by+230, colw, 178, L["l2t"], L["l2"], "good", L, tag="STEP 2")

    # ── ขวา: ปูกระเบื้อง
    x = rx - colw/2
    s += T(rx, by+30, L["cR"], 24, TH_B, INK, "middle", "700")
    s += card(x, by+52, colw, 122, L["r0t"], L["r0"], "plain", L, tag="STEP 0")
    s += (f'<line x1="{rx}" y1="{by+174}" x2="{rx}" y2="{by+198}" stroke="{INK}" '
          f'stroke-width="2.6" marker-end="url(#aI)"/>\n')
    s += card(x, by+202, colw, 168, L["rAt"], L["rA"], "good", L, tag=L["rAtag"])
    s += card(x, by+386, colw, 168, L["rBt"], L["rB"], "good", L, tag=L["rBtag"])

    s += brandbar(W, H, "CASE STUDY · ROOFTOP")
    return svg_doc(W, H, s)

TH_DECIDE = dict(
    t="ตอบคำถามเดียว แผนงานเปลี่ยนทั้งกระดาน",
    ts="สรุปทางซ่อมดาดฟ้ารั่วของทั้งสองพื้นผิว",
    q="ดาดฟ้าเป็นแบบไหน?",
    cL="ปูนเปลือย", cR="ปูกระเบื้อง",
    l1t="อุดรอยร้าวให้จบก่อน — PatchPro",
    l1=["ไล่หารอยแตก มุม และแนวพื้นชนผนังให้ครบ", "อุดให้เต็มเสมอผิว รอเซ็ตตัวตามคู่มือ"],
    l2t="เคลือบทั้งผืน — PolyPro (Polyurea Gen3)",
    l2=["ฟิล์มหนา ทน UV ไม่เหลือง แช่น้ำถาวร", "เกิดมาเพื่องานกลางแจ้งที่โดนแดดทั้งวัน", "งบน้อย: เริ่มที่ SiliconePro — ทาเฉพาะแผลก็ได้"],
    r0t="เช็คสภาพก่อนเสมอ",
    r0=["เคาะหากระเบื้องร่อน/โพรง — เจอต้องแก้ก่อน", "ห้ามทาทับปิดปัญหาไว้ใต้ฟิล์ม"],
    rAtag="ทางที่จบที่สุด (งานหนัก)",
    rAt="เปลี่ยนยาแนวทุกร่องเป็น Epoxy",
    rA=["ปิดประตูน้ำเข้าที่ต้นทางโดยตรง", "ของจริงคือรื้อยาแนวเดิมออกก่อนทุกร่อง", "เหนื่อย ฝุ่นเยอะ — แต่ทำรอบเดียวจบ"],
    rBtag="ทางที่คนส่วนใหญ่เลือก",
    rBt="เคลือบทับทั้งผืน — PolyPro",
    rB=["ยึดเกาะบนกระเบื้องเคลือบได้จริง", "ปิดทั้งหน้ากระเบื้องและร่องยาแนวพร้อมกัน", "เติมร่องยาแนวที่เป็นโพรงให้เต็มก่อนทา"],
)
EN_DECIDE = dict(
    t="One answer changes the whole game plan",
    ts="The repair map for both rooftop surfaces",
    q="Which deck do you have?",
    cL="Bare concrete", cR="Tiled",
    l1t="Seal the cracks first — PatchPro",
    l1=["Hunt down every crack, corner and wall joint", "Fill flush with the surface, let it cure"],
    l2t="Coat the whole deck — PolyPro (Polyurea Gen3)",
    l2=["Thick film, UV-stable, handles standing water", "Built for full-sun outdoor duty", "On a budget? Start with SiliconePro — spot-coat only"],
    r0t="Inspect before anything else",
    r0=["Tap-test for hollow or debonded tiles — fix first", "Never coat over a problem to hide it"],
    rAtag="The definitive fix (hard work)",
    rAt="Re-grout every line with Epoxy",
    rA=["Shuts the water out right at the entry point", "Reality: old grout must come out first, every line", "Dusty, tiring — but it's a one-time job"],
    rBtag="What most people choose",
    rBt="Coat the whole deck — PolyPro",
    rB=["Actually bonds to glazed tile surfaces", "Seals tile faces and grout lines in one go", "Fill any hollow grout lines before coating"],
)

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
    render(f"{SLUG}-compare-th", hero(TH_HERO), 88)
    render(f"{SLUG}-compare-en", hero(EN_HERO), 86)
    render(f"{SLUG}-path-th", path(TH_PATH), 88)
    render(f"{SLUG}-path-en", path(EN_PATH), 86)
    render(f"{SLUG}-decide-th", decide(TH_DECIDE), 88)
    render(f"{SLUG}-decide-en", decide(EN_DECIDE), 86)
