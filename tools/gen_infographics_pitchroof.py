# -*- coding: utf-8 -*-
"""
gen_infographics_pitchroof.py — infographic ประกอบโพสต์ cpac-metal-sheet-roof-leaks
ผลลัพธ์: /img/post/cpac-metal-sheet-roof-leaks-hero{,-en}.webp  (hero: สองหลังคา + จุดตาย)
         /img/post/cpac-metal-sheet-roof-leaks-cpac-{th,en}.webp  (แผนที่จุดตาย CPAC)
         /img/post/cpac-metal-sheet-roof-leaks-metal-{th,en}.webp (แผนที่จุดตายเมทัลชีท)
ต้องการ: rsvg-convert + ฟอนต์ตามหมายเหตุใน gen_infographics_cracks.py
รัน: python3 tools/gen_infographics_pitchroof.py (จาก root ของ repo)
"""
import os, subprocess, html, random
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img", "post")
SLUG = "cpac-metal-sheet-roof-leaks"

PAPER = "#F2F2EF"; CARD = "#FFFFFF"; INK = "#191C1F"; STEEL = "#5E646A"
LINE = "#DCDCD6"; SIGNAL = "#D8571C"
BAD = "#B23A2E"; WATER = "#3E7CB1"
TERRA = "#C97A52"; TERRA_DK = "#AE6340"; TERRA_HI = "#D68A63"
METAL = "#DADDE0"; METAL_DK = "#B7BCC2"; RUST = "#8A5A3B"
WALL = "#CFCBC0"

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

def speckle(x, y, w, h, n, color, rmin=1.4, rmax=2.6, seed=7):
    rnd = random.Random(seed); s = ""
    for _ in range(n):
        s += (f'<circle cx="{x+rnd.uniform(6,w-6):.0f}" cy="{y+rnd.uniform(6,h-6):.0f}" '
              f'r="{rnd.uniform(rmin,rmax):.1f}" fill="{color}"/>\n')
    return s

def numdot(x, y, n, color=BAD, r=15):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="#fff" stroke-width="2.5"/>'
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

# ── ผืนหลังคา CPAC (มองบนเอียง): แถวกระเบื้องซ้อน + ครอบสัน + ตะเข้ราง + แนวชนผนัง
def cpac_plane(x, y, w, h, dots=None, crack=True):
    s = rrect(x, y, w, h, 4, TERRA, TERRA_DK, 2)
    rows = 6
    rh = h / rows
    for r in range(rows):
        ry = y + r*rh
        # เงาชายแถว (การซ้อนแผ่น)
        s += f'<rect x="{x}" y="{ry+rh-7:.0f}" width="{w}" height="7" fill="{TERRA_DK}" opacity=".55"/>\n'
        # เส้นแบ่งแผ่นในแถว (สลับครึ่งแผ่น)
        off = 0 if r % 2 == 0 else 42
        gx = x + off
        while gx < x + w:
            s += f'<line x1="{gx:.0f}" y1="{ry:.0f}" x2="{gx:.0f}" y2="{ry+rh:.0f}" stroke="{TERRA_DK}" stroke-width="1.6" opacity=".6"/>\n'
            gx += 84
        # ไฮไลต์ขอบบนแถว
        s += f'<rect x="{x}" y="{ry:.0f}" width="{w}" height="3" fill="{TERRA_HI}" opacity=".5"/>\n'
    # ครอบสันบนสุด
    for i in range(int(w // 56)):
        cx = x + 28 + i*56
        s += f'<ellipse cx="{cx:.0f}" cy="{y}" rx="30" ry="13" fill="{TERRA_DK}" stroke="{TERRA_HI}" stroke-width="1.5"/>\n'
    # ปูนครอบแตก (บนสัน)
    s += (f'<path d="M{x+w*0.42:.0f},{y-8} l14,6 l12,-5 l14,6" stroke="{BAD}" stroke-width="3" '
          f'fill="none" stroke-linecap="round"/>\n')
    # ตะเข้ราง (ซ้าย)
    s += rrect(x-16, y, 16, h, 0, METAL_DK)
    s += f'<line x1="{x-8}" y1="{y}" x2="{x-8}" y2="{y+h}" stroke="{WATER}" stroke-width="3" stroke-dasharray="8 7" opacity=".8"/>\n'
    # แนวชนผนัง (ขวา)
    s += rrect(x+w, y, 16, h, 0, WALL)
    # กระเบื้องแตก
    if crack:
        cxx, cyy = x + w*0.55, y + h*0.52
        s += (f'<path d="M{cxx:.0f},{cyy:.0f} l16,14 l-6,16 l18,14" stroke="{BAD}" '
              f'stroke-width="3.4" fill="none" stroke-linecap="round"/>\n')
    if dots:
        for (dx, dy, n) in dots:
            s += numdot(x + w*dx, y + h*dy, n)
    return s

# ── ผืนหลังคาเมทัลชีท: ลอนตั้ง + แถวสกรู + รอยซ้อนแผ่น + ท่อเจาะ + สนิม
def metal_plane(x, y, w, h, dots=None):
    s = rrect(x, y, w, h, 4, METAL, METAL_DK, 2)
    # ลอน
    gx = x + 20
    while gx < x + w - 6:
        s += f'<line x1="{gx:.0f}" y1="{y}" x2="{gx:.0f}" y2="{y+h}" stroke="{METAL_DK}" stroke-width="2"/>\n'
        s += f'<line x1="{gx+5:.0f}" y1="{y}" x2="{gx+5:.0f}" y2="{y+h}" stroke="#FFFFFF" stroke-width="1.4" opacity=".8"/>\n'
        gx += 38
    # รอยซ้อนแผ่น (เส้นหนากลางผืน)
    ox = x + w*0.52
    s += f'<line x1="{ox:.0f}" y1="{y}" x2="{ox:.0f}" y2="{y+h}" stroke="{METAL_DK}" stroke-width="7"/>\n'
    s += f'<line x1="{ox:.0f}" y1="{y}" x2="{ox:.0f}" y2="{y+h}" stroke="{BAD}" stroke-width="2" stroke-dasharray="10 8" opacity=".9"/>\n'
    # แถวสกรูตามแนวแป
    for i, ry in enumerate((0.16, 0.5, 0.84)):
        gy = y + h*ry
        gx = x + 20
        while gx < x + w - 6:
            s += f'<circle cx="{gx:.0f}" cy="{gy:.0f}" r="4.2" fill="{STEEL}" stroke="#fff" stroke-width="1.2"/>\n'
            gx += 76
    # หัวสกรูปัญหา (แดง)
    s += f'<circle cx="{x + w*0.28:.0f}" cy="{y + h*0.5:.0f}" r="7" fill="{BAD}" stroke="#fff" stroke-width="2"/>\n'
    # ท่อเจาะหลังคา
    px, py = x + w*0.78, y + h*0.3
    s += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="17" fill="{STEEL}"/>\n'
    s += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="24" fill="none" stroke="{BAD}" stroke-width="2.4" stroke-dasharray="6 5"/>\n'
    # สนิมมุมล่าง
    s += speckle(x + w*0.06, y + h*0.78, w*0.2, h*0.16, 26, RUST, seed=4)
    if dots:
        for (dx, dy, n) in dots:
            s += numdot(x + w*dx, y + h*dy, n)
    return s

# ============================================================ HERO — สองหลังคา + จุดตาย
def hero(L):
    W, H = 1200, 900
    s = T(W/2, 66, L["t"], 40, HEAD, INK, "middle", "700")
    s += T(W/2, 106, L["ts"], 22.5, TH_R, STEEL, "middle")

    py, ph = 168, 566; pw = 520
    # ── ซ้าย: CPAC
    x = 60
    s += rrect(x, py, pw, ph, 14, CARD, LINE, 2)
    s += T(x+26, py+46, L["cL"], 25, TH_B, INK, weight="700")
    s += T(x+26, py+77, L["cLs"], 17.5, TH_R, STEEL)
    s += cpac_plane(x+46, py+118, pw-112, 300,
                    dots=[(0.42, -0.03, 1), (0.58, 0.55, 2), (-0.028, 0.22, 3), (1.028, 0.75, 4)])
    ly = py+458
    for i, ln in enumerate(L["cLl"]):
        s += numdot(x+38, ly + i*27 - 6, i+1, BAD, r=11)
        s += T(x+58, ly + i*27, ln, 16.5, TH_R, STEEL)
    # ── ขวา: เมทัลชีท
    x = 620
    s += rrect(x, py, pw, ph, 14, CARD, LINE, 2)
    s += T(x+26, py+46, L["cR"], 25, TH_B, INK, weight="700")
    s += T(x+26, py+77, L["cRs"], 17.5, TH_R, STEEL)
    s += metal_plane(x+30, py+118, pw-60, 300,
                     dots=[(0.28, 0.5, 1), (0.52, 0.14, 2), (0.78, 0.3, 3), (0.1, 0.84, 4)])
    ly = py+458
    for i, ln in enumerate(L["cRl"]):
        s += numdot(x+38, ly + i*27 - 6, i+1, BAD, r=11)
        s += T(x+58, ly + i*27, ln, 16.5, TH_R, STEEL)

    s += T(W/2, py+ph+52, L["foot"], 20, TH_SB, INK, "middle")
    s += brandbar(W, H, "CASE STUDY · ROOF")
    return svg_doc(W, H, s)

TH_HERO = dict(
    t="หลังคารั่ว ไม่ใช่ทั้งผืน — มันรั่วเป็น \"จุด\"",
    ts="แผนที่จุดตายของหลังคากระเบื้องคอนกรีต (CPAC) และเมทัลชีท",
    cL="หลังคากระเบื้อง CPAC", cLs="จุดตายอยู่ที่รอยแตกและแนวครอบ",
    cLl=["ปูนครอบสัน/ครอบข้าง แตกร่อน", "กระเบื้องแตกร้าว (มักจากการเหยียบ)", "ตะเข้ราง — รอยต่อและสนิม", "แนวหลังคาชนผนัง (Flashing)"],
    cR="หลังคาเมทัลชีท", cRs="จุดตายอยู่ที่รูสกรูและรอยซ้อน",
    cRl=["หัวสกรู — ยางรองเสื่อม/ขันเบี้ยว", "รอยซ้อนแผ่น (Overlap)", "รอบท่อ/ช่องเจาะทะลุหลังคา", "สนิมกินจนเป็นรูพรุน"],
    foot="เกมของหลังคาลาดเอียงคือไล่หาช่องพวกนี้ให้ครบ — ไม่ใช่ทากันซึมทั้งผืน",
)
EN_HERO = dict(
    t="A pitched roof doesn't leak everywhere — it leaks at points",
    ts="The kill-spot map for concrete-tile (CPAC) and metal sheet roofs",
    cL="CPAC concrete-tile roof", cLs="Kill spots: cracks and capping lines",
    cLl=["Ridge/hip cap mortar — cracked, crumbling", "Cracked tiles (usually from foot traffic)", "The valley — joints and rust", "Roof-to-wall junction (flashing)"],
    cR="Metal sheet roof", cRs="Kill spots: screw holes and overlaps",
    cRl=["Screw heads — degraded washers, bad angles", "Sheet overlap seams", "Pipe and duct penetrations", "Rust eaten through to pinholes"],
    foot="The pitched-roof game is hunting down every one of these gaps — not coating the whole plane",
)

# ============================================================ CPAC — แผนที่จุดตายละเอียด
def detail(L, plane_fn):
    W, H = 1200, 900
    s = T(W/2, 64, L["t"], 40, HEAD, INK, "middle", "700")
    s += T(W/2, 102, L["ts"], 22, TH_R, STEEL, "middle")

    # ผืนหลังคาใหญ่ ซ้าย
    s += plane_fn(120, 170, 560, 470, dots=L["dots"])
    s += T(400, 690, L["cap"], 18, TH_SB, STEEL, "middle")

    # legend ขวา
    x = 760; y = 190
    for i, (head, sub) in enumerate(L["items"]):
        s += numdot(x, y+8, i+1, BAD, r=14)
        s += T(x+28, y+14, head, 20.5, TH_B, INK, weight="700")
        s += T(x+28, y+42, sub[0], 17, TH_R, STEEL)
        if len(sub) > 1:
            s += T(x+28, y+66, sub[1], 17, TH_R, STEEL)
        y += 78 + (20 if len(sub) > 1 else 0)

    s += brandbar(W, H, "CASE STUDY · ROOF")
    return svg_doc(W, H, s)

TH_CPAC = dict(
    t="แผนที่จุดตาย — หลังคากระเบื้อง CPAC",
    ts="สี่จุดที่ต้องไล่เช็คก่อนโทษกระเบื้องทั้งผืน",
    dots=[(0.42, -0.03, 1), (0.58, 0.55, 2), (-0.028, 0.22, 3), (1.028, 0.75, 4)],
    cap="ผืนหลังคามุมมองจากด้านบน — ครอบสันอยู่แนวบน ตะเข้รางซ้าย แนวชนผนังขวา",
    items=[
        ("ปูนครอบสัน / ครอบข้าง", ["ปูนยึดครอบแตกลายงา ร่อนหลุดเป็นก้อน", "น้ำเข้าใต้ครอบแล้วไหลตามแป"]),
        ("กระเบื้องแตกร้าว", ["สาเหตุอันดับหนึ่ง: การขึ้นไปเหยียบผิดจุด", "ร้าวเส้นเดียวก็พอให้น้ำผ่านทุกฝน"]),
        ("ตะเข้ราง (Valley)", ["จุดรวมน้ำสองผืนหลังคา — งานหนักสุด", "รอยต่อราง สนิม และเศษใบไม้อุดตัน"]),
        ("แนวหลังคาชนผนัง", ["แผ่นปิด (Flashing) เผยอ ยาแนวเดิมเสื่อม", "น้ำย้อนเข้าตามแนวชนทุกครั้งที่ฝนสาด"]),
    ],
)
EN_CPAC = dict(
    t="Kill-spot map — CPAC concrete-tile roof",
    ts="Four spots to check before blaming the whole roof",
    dots=[(0.42, -0.03, 1), (0.58, 0.55, 2), (-0.028, 0.22, 3), (1.028, 0.75, 4)],
    cap="Roof plane seen from above — ridge caps along the top, valley left, wall junction right",
    items=[
        ("Ridge / hip cap mortar", ["Bedding mortar cracks and crumbles off", "Water slips under the caps and runs the battens"]),
        ("Cracked tiles", ["Cause number one: stepping in the wrong spot", "A single hairline is enough, every single rain"]),
        ("The valley", ["Where two planes dump their water — hardest duty", "Seams, rust, and leaf-litter blockages"]),
        ("Roof-to-wall junction", ["Flashing lifts, old sealant gives up", "Wind-driven rain backs in along the junction"]),
    ],
)

TH_METAL = dict(
    t="แผนที่จุดตาย — หลังคาเมทัลชีท",
    ts="สี่จุดที่พังก่อนเสมอ ทั้งที่แผ่นยังสภาพดี",
    dots=[(0.28, 0.5, 1), (0.52, 0.14, 2), (0.78, 0.3, 3), (0.1, 0.84, 4)],
    cap="ผืนเมทัลชีทมุมมองจากด้านบน — ลอนตั้งตามแนวลาด สกรูเรียงตามแนวแป",
    items=[
        ("หัวสกรู", ["ยางรองสกรูกรอบแตกตามอายุ/ความร้อน", "ขันเบี้ยวหรือแน่นเกิน = ยางบี้เสียรูปตั้งแต่วันแรก"]),
        ("รอยซ้อนแผ่น (Overlap)", ["แผ่นยืดหดตามอุณหภูมิทั้งวัน รอยซ้อนขยับตลอด", "ลาดน้อยยิ่งเสี่ยง — น้ำย้อนกลับตามแรงลม"]),
        ("รอบท่อ / ช่องเจาะ", ["ทุกรูที่เจาะทะลุหลังคาคือประตูถาวร", "ยาแนวเดิมกรอบแตกเร็วเพราะโดนแดดตรง"]),
        ("สนิมรูพรุน", ["เริ่มจากรอยขูดผิวเคลือบ ลามเป็นรูเข็ม", "โป๊วปิดได้เฉพาะรูเล็ก — ผุทั้งแผ่นต้องเปลี่ยน"]),
    ],
)
EN_METAL = dict(
    t="Kill-spot map — metal sheet roof",
    ts="The four spots that fail first while the sheet still looks fine",
    dots=[(0.28, 0.5, 1), (0.52, 0.14, 2), (0.78, 0.3, 3), (0.1, 0.84, 4)],
    cap="Metal sheet plane seen from above — ribs run with the slope, screws follow the purlin lines",
    items=[
        ("Screw heads", ["Rubber washers crack with age and heat", "Driven crooked or too tight = deformed from day one"]),
        ("Sheet overlap seams", ["Sheets expand and contract all day — seams keep moving", "Low pitch is riskiest: wind pushes water back uphill"]),
        ("Pipe / duct penetrations", ["Every hole through the roof is a permanent doorway", "Old sealant bakes brittle in direct sun"]),
        ("Pinhole rust", ["Starts at a coating scratch, spreads to pinholes", "Filler seals small holes — a rotten sheet needs replacing"]),
    ],
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
    render(f"{SLUG}-hero", hero(TH_HERO), 88)
    render(f"{SLUG}-hero-en", hero(EN_HERO), 86)
    render(f"{SLUG}-cpac-th", detail(TH_CPAC, cpac_plane), 88)
    render(f"{SLUG}-cpac-en", detail(EN_CPAC, cpac_plane), 86)
    render(f"{SLUG}-metal-th", detail(TH_METAL, metal_plane), 88)
    render(f"{SLUG}-metal-en", detail(EN_METAL, metal_plane), 86)
