# -*- coding: utf-8 -*-
"""
gen_infographics_floorseep.py — infographic ประกอบโพสต์ floor-seepage-negative-side
ผลลัพธ์: /img/post/floor-seepage-negative-side-00{,en}.webp  (hero: หน้าตัดน้ำดันจากใต้พื้น)
         /img/post/floor-seepage-negative-side-info-{th,en}.webp (กระเบื้องปูชิด → กรีดร่อง)
ต้องการ: rsvg-convert + ฟอนต์ตามหมายเหตุใน gen_infographics_cracks.py
รัน: python3 tools/gen_infographics_floorseep.py (จาก root ของ repo)
"""
import os, subprocess, html, random
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img", "post")
SLUG = "floor-seepage-negative-side"

PAPER = "#F2F2EF"; CARD = "#FFFFFF"; INK = "#191C1F"; STEEL = "#5E646A"
LINE = "#DCDCD6"; SIGNAL = "#D8571C"
CONCRETE = "#DDD9CF"; CONCRETE_DK = "#C9C4B7"; WATER = "#3E7CB1"
BAD = "#B23A2E"; GOOD = "#2E7D4F"; BAD_BG = "#F7ECEA"; GOOD_BG = "#EAF2ED"
SOIL = "#D8CBAF"; SOIL_DK = "#C2B08D"; TILE = "#EAE4D8"; GROUT = "#4A4F55"

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

# ============================================================ HERO — หน้าตัด negative side
def hero(L):
    W, H = 1200, 900
    s = f"<defs>{arrow_marker('aW', WATER)}{arrow_marker('aI', INK)}</defs>\n"
    s += T(W/2, 70, L["t"], 42, HEAD, INK, "middle", "700")
    s += T(W/2, 110, L["ts"], 23, TH_R, STEEL, "middle")

    x0, x1 = 120, 1080; w = x1 - x0
    # ห้อง (ในบ้าน)
    s += rrect(x0, 160, w, 240, 0, CARD, LINE, 2)
    s += rrect(x0, 160, 26, 240, 0, CONCRETE_DK)
    s += rrect(x1-26, 160, 26, 240, 0, CONCRETE_DK)
    s += T(x0+52, 194, L["room"], 21, TH_SB, STEEL)
    # คราบชื้นบนผิวพื้น
    for cx, rw in ((430, 92), (700, 70), (905, 84)):
        s += f'<ellipse cx="{cx}" cy="398" rx="{rw}" ry="10" fill="#A89F8E" opacity=".45"/>\n'
    # พื้นคอนกรีต
    s += rrect(x0, 400, w, 108, 0, CONCRETE, LINE, 2)
    s += speckle(x0, 400, w, 108, 80, CONCRETE_DK, seed=11)
    s += T(x0+52, 462, L["slab"], 21, TH_SB, "#8A8375")
    # ดิน
    s += rrect(x0, 508, w, 140, 0, SOIL)
    s += speckle(x0, 508, w, 140, 70, SOIL_DK, seed=5)
    s += T(x0+52, 560, L["soil"], 21, TH_SB, "#9A8760")
    # น้ำใต้ดิน
    s += rrect(x0, 648, w, 64, 0, WATER, opacity=".88")
    wave = " ".join(f"L{x},{648 + (4 if (x//40) % 2 else -4)}" for x in range(x0+40, x1, 40))
    s += f'<path d="M{x0},648 {wave} L{x1},648" stroke="#FFFFFF" stroke-width="2.5" fill="none" opacity=".7"/>\n'
    s += T(W/2, 688, L["gw"], 20, TH_SB, "#fff", "middle", opacity=".95")
    # ลูกศรน้ำดันขึ้น
    for ax in (300, 520, 745, 950):
        s += (f'<line x1="{ax}" y1="660" x2="{ax}" y2="385" stroke="{WATER}" '
              f'stroke-width="5" marker-end="url(#aW)" opacity=".92"/>\n')
    # รอยร้าว (①)
    zig = "M745,400 L737,418 L753,436 L739,454 L751,472 L741,490 L749,508"
    s += f'<path d="{zig}" stroke="{BAD}" stroke-width="3.5" fill="none"/>\n'
    s += numdot(792, 420, 1, BAD)
    # มุมพื้นชนผนัง (②)
    s += f'<circle cx="{x0+26}" cy="400" r="30" fill="none" stroke="{BAD}" stroke-width="3" stroke-dasharray="6 5"/>\n'
    s += numdot(x0+82, 356, 2, BAD)
    # คราบชื้น (③)
    s += numdot(430, 360, 3, STEEL)
    # ป้ายแรงดัน
    s += T(x1-46, 588, "NEGATIVE HYDROSTATIC PRESSURE", 16, MONO, "#7A6A45", "end", spacing="1")
    s += T(x1-46, 614, L["press"], 20, TH_SB, "#7A6A45", "end")
    # legend
    ly = 754
    s += numdot(150, ly-6, 1, BAD) + T(178, ly, L["l1"], 22, TH_R, INK)
    s += numdot(150, ly+36, 2, BAD) + T(178, ly+42, L["l2"], 22, TH_R, INK)
    s += numdot(660, ly-6, 3, STEEL) + T(688, ly, L["l3"], 22, TH_R, INK)
    s += T(688, ly+42, L["l4"], 22, TH_SB, SIGNAL)
    s += brandbar(W, H, "NEGATIVE SIDE / FLOOR")
    return svg_doc(W, H, s)

# ============================================================ INFO — กระเบื้องปูชิด
def tiles_row(x, y, tw, gap, cut=False):
    """วาดกระเบื้องสองแผ่นบนปูนกาว คืน svg + พิกัดกลางร่อง"""
    s = rrect(x, y+34, tw*2+gap+24, 30, 0, CONCRETE)          # ปูนกาว/พื้น
    s += speckle(x, y+34, tw*2+gap+24, 30, 14, CONCRETE_DK, seed=3)
    for i, tx in enumerate((x+12, x+12+tw+gap)):
        s += rrect(tx, y, tw, 34, 3, TILE, "#CFC8B8", 2)
        s += f'<line x1="{tx+8}" y1="{y+8}" x2="{tx+tw-10}" y2="{y+8}" stroke="#FFFFFF" stroke-width="3" opacity=".7"/>\n'
    return s, x+12+tw+gap/2

def info(L):
    W, H = 1200, 900
    s = f"<defs>{arrow_marker('aB', BAD)}{arrow_marker('aG', GOOD)}{arrow_marker('aK', INK)}</defs>\n"
    s += T(W/2, 68, L["t"], 40, HEAD, INK, "middle", "700")
    s += T(W/2, 108, L["ts"], 23, TH_R, STEEL, "middle")

    cw, ch, cy = 346, 570, 150
    xs = (56, 427, 798)
    fills = (CARD, BAD_BG, GOOD_BG); strokes = (LINE, BAD, GOOD)
    bs = L.get("bs", 20.5)
    for i, (cx, tag, head1, head2) in enumerate(zip(xs, L["tags"], L["h1"], L["h2"])):
        s += rrect(cx, cy, cw, ch, 14, fills[i], strokes[i], 2)
        s += T(cx+24, cy+42, tag, 15, MONO, (STEEL, BAD, GOOD)[i], spacing="1.5")
        s += T(cx+24, cy+80, head1, 25, TH_B, INK)
        s += T(cx+24, cy+112, head2, 25, TH_B, INK)

    dy = cy + 190
    # ── การ์ด 1: ร่องแคบเกิน
    t1, g1 = tiles_row(xs[0]+38, dy+60, 122, 5)
    s += t1
    s += f'<line x1="{g1}" y1="{dy-8}" x2="{g1}" y2="{dy+52}" stroke="{INK}" stroke-width="3" marker-end="url(#aK)"/>\n'
    s += T(g1, dy-22, L["c1gap"], 19, TH_SB, INK, "middle")
    for j, r in enumerate(L["c1tx"]):
        s += T(xs[0]+24, dy+200+j*32, r, bs, TH_R, INK)
    # ── การ์ด 2: เท epoxy ทับหน้า → หลุด
    t2, g2 = tiles_row(xs[1]+38, dy+60, 122, 5)
    s += t2
    lx = xs[1]+44
    s += (f'<path d="M{lx},{dy+58} L{lx+218},{dy+58} L{lx+218},{dy+50} '
          f'Q{lx+252},{dy+30} {lx+262},{dy+6}" stroke="#7A8290" stroke-width="9" '
          f'fill="none" stroke-linecap="round"/>\n')
    s += f'<circle cx="{xs[1]+cw-52}" cy="{dy+10}" r="21" fill="{BAD}"/>' + T(xs[1]+cw-52, dy+18, "✕", 24, TH_B, "#fff", "middle")
    s += T(lx+8, dy+40, L["c2peel"], 18, TH_SB, BAD)
    for j, r in enumerate(L["c2tx"]):
        s += T(xs[1]+24, dy+200+j*32, r, bs, TH_R, INK)
    # ── การ์ด 3: กรีดร่องกว้าง + อัดเต็ม
    t3, g3 = tiles_row(xs[2]+38, dy+60, 108, 34)
    s += t3
    s += rrect(g3-17, dy+60, 34, 34, 0, GROUT)                        # epoxy grout เต็มร่อง
    s += f'<line x1="{g3-19}" y1="{dy+52}" x2="{g3-19}" y2="{dy+98}" stroke="{SIGNAL}" stroke-width="2.5" stroke-dasharray="5 4"/>\n'
    s += f'<line x1="{g3+19}" y1="{dy+52}" x2="{g3+19}" y2="{dy+98}" stroke="{SIGNAL}" stroke-width="2.5" stroke-dasharray="5 4"/>\n'
    s += T(g3, dy+40, L["c3cut"], 18, TH_SB, SIGNAL, "middle")
    s += f'<circle cx="{xs[2]+cw-52}" cy="{dy+10}" r="21" fill="{GOOD}"/>' + T(xs[2]+cw-52, dy+18, "✓", 24, TH_B, "#fff", "middle")
    for j, r in enumerate(L["c3tx"]):
        s += T(xs[2]+24, dy+200+j*32, r, bs, TH_R, INK)

    s += T(W/2, cy+ch+58, L["foot"], 23, TH_SB, INK, "middle")
    s += brandbar(W, H, "TIGHT TILE JOINTS")
    return svg_doc(W, H, s)

# ============================================================ texts
TH_HERO = {
 "t": "น้ำดันขึ้นจากใต้พื้นบ้าน — สนาม Negative Side ของแท้",
 "ts": "ฝั่งที่น้ำมาคือดินใต้บ้าน — ไม่มีใครขุดบ้านลงไปทากันซึมข้างล่างได้",
 "room": "ในบ้าน", "slab": "พื้นคอนกรีต", "soil": "ดินใต้บ้าน", "gw": "น้ำ / ความชื้นใต้ดิน",
 "press": "แรงดันย้อน ดันขึ้นตลอดเวลา",
 "l1": "รอยร้าวพื้น — ทางด่วนสายหลักของน้ำ",
 "l2": "มุมห้อง-รอยต่อพื้นชนผนัง — จุดรั่วยอดฮิต",
 "l3": "ผลที่เห็น: พื้นชื้น สีโป่ง คราบเกลือขาว",
 "l4": "ออกไปทาฝั่งที่น้ำมาไม่ได้ = ต้องสู้ฝั่ง Negative",
}
EN_HERO = {
 "t": "Water Pushing Up Through the Floor — True Negative Side",
 "ts": "The water comes from the soil under the house — nobody can dig under a home to coat that side",
 "room": "Indoors", "slab": "Concrete slab", "soil": "Soil under the house", "gw": "Groundwater / moisture",
 "press": "Pushing upward, all the time",
 "l1": "Floor cracks — water's main highway",
 "l2": "Room corners & wall-floor joints — top leak spots",
 "l3": "What you see: damp floor, blistered paint, white salt",
 "l4": "Can't reach the water side = fighting on the negative side",
}
TH_INFO = {
 "t": "กระเบื้องปูชิด ร่องแคบเกิน — ยาแนวอัดไม่ลง แก้ยังไง",
 "ts": "Straight Talk: ทางลัดเราลองให้แล้วด้วยเงินตัวเอง — ไม่รอด",
 "tags": ("THE PROBLEM", "THE SHORTCUT — FAILED", "THE FIX"),
 "h1": ("ร่องแคบเกินไป", "เท Epoxy ทับหน้า", "กรีดร่องให้กว้างขึ้น"),
 "h2": ("อัดยาแนวใหม่ไม่ได้", "เราลองแล้ว — หลุด", "แล้วค่อยอัดให้เต็ม"),
 "c1gap": "ร่องแค่ ~1-2 มม.",
 "c1tx": ["กระเบื้องปูชิดกันมาก ร่องยาแนว", "แคบจนวัสดุใหม่ลงไปไม่ถึงก้นร่อง", "พื้นที่ให้ยาแนวยึดเกาะน้อยเกินไป"],
 "c2peel": "ขอบเผยอ หลุดล่อน",
 "c2tx": ["เท Epoxy Self-Leveling บางๆ ทับหน้า", "อยู่ได้ไม่นาน — ผิวเคลือบกระเบื้องลื่น", "พื้นที่ยึดเกาะน้อยเกินกว่าฟิล์มจะเกาะอยู่"],
 "c3cut": "แนวกรีดด้วยใบตัด",
 "c3tx": ["ใช้ลูกหมู/ใบตัด กรีดร่องยาแนว", "ให้กว้างและลึกขึ้น เปิดพื้นที่ยึดเกาะ", "แล้วอัด Epoxy Grout ให้เต็มเสมอผิว"],
 "foot": "มุมห้องและขอบสุขภัณฑ์ — อุดปิดด้วย PatchPro ให้จบก่อนเก็บงานเสมอ",
}
EN_INFO = {
 "t": "Tiles Laid Too Tight — Grout Won't Go In. Now What?",
 "ts": "Straight Talk: we paid for the shortcut ourselves — it failed",
 "tags": ("THE PROBLEM", "THE SHORTCUT — FAILED", "THE FIX"),
 "h1": ("Joints too narrow", "Epoxy poured on top", "Cut the joints wider"),
 "h2": ("for new grout to enter", "we tried it — it peeled", "then pack them full"),
 "c1gap": "Joint only ~1-2 mm",
 "bs": 19.5,
 "c1tx": ["Tiles laid nearly touching —", "new grout can't reach the bottom", "and has too little surface to grip"],
 "c2peel": "Edges lift & peel",
 "c2tx": ["Thin self-leveling epoxy on top", "doesn't last — glazed tile is slick,", "bonding area far too small"],
 "c3cut": "Cutting line (grinder)",
 "c3tx": ["Angle-grind the joints wider and", "deeper to open real bonding area,", "then pack epoxy grout in flush"],
 "foot": "Room corners and fixture edges — always seal off with PatchPro before finishing",
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
    render(f"{SLUG}-00", hero(TH_HERO), 88)
    render(f"{SLUG}-00en", hero(EN_HERO), 86)
    render(f"{SLUG}-info-th", info(TH_INFO), 88)
    render(f"{SLUG}-info-en", info(EN_INFO), 86)
