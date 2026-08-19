#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""หยดหยดเล่า EP.2 — 'รางผุ ไม่ใช่เวรกรรม' 1080x1920 30fps 28s = 840 เฟรม (มติเจ้าของ: ยืดช่วงค้างตัวหนังสือ)"""
import math, os, random, sys
sys.path.insert(0, "/home/claude")
from gen_frames import (W, H, mascot, droplet, bubbles, clamp01, P,
                        ease_out, ease_in, ease_io, ease_back, esc)

FPS, DUR = 30, 28.0
N = int(FPS * DUR)
OUT = "/home/claude/frames_ep2"
os.makedirs(OUT, exist_ok=True)

INK = "#0B2239"; GOLD_HL = "#E8A200"
METAL = "#C3CDD6"; METAL_DK = "#8FA3B5"; RUST = "#B4652F"; RUST_DK = "#7E421C"
COAT = "#7D8A94"; COAT_HI = "#A7B4BD"

random.seed(21)
RUST_SPOTS = [(random.uniform(-70, 70), random.uniform(-10, 46), random.uniform(7, 20),
               random.uniform(0, 1)) for _ in range(14)]

def star(x, y, s, op, col="#FFC53D"):
    return (f'<g transform="translate({x:.0f},{y:.0f}) scale({s:.2f}) rotate({int(40*s)%360})" opacity="{op:.2f}">'
            f'<path d="M0 -10 l3 6 6 1 -4.5 4.5 1 6.5 -5.5 -3 -5.5 3 1 -6.5 -4.5 -4.5 6 -1z" fill="{col}"/></g>')

def txt(x, y, size, s, fill=INK, w="600", anchor="middle", op=1.0, dy=0.0):
    return (f'<text x="{x}" y="{y+dy:.0f}" text-anchor="{anchor}" font-family="Mitr" font-weight="{w}" '
            f'font-size="{size}" fill="{fill}" opacity="{op:.2f}">{esc(s)}</text>')

def fade_txt(t, t0, x, y, size, s, fill=INK, w="600"):
    p = P(t, t0, 0.4)
    if p <= 0: return ""
    e = ease_out(p)
    return txt(x, y, size, s, fill, w, op=e, dy=14*(1-e))

def sun(x, y, r=54):
    rays = "".join(f'<line x1="{x+math.cos(a)*(r+14):.0f}" y1="{y+math.sin(a)*(r+14):.0f}" '
                   f'x2="{x+math.cos(a)*(r+34):.0f}" y2="{y+math.sin(a)*(r+34):.0f}" '
                   f'stroke="#FFDE6B" stroke-width="9" stroke-linecap="round"/>'
                   for a in [k*math.pi/4 for k in range(8)])
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFDE6B"/>{rays}'

def gutter_run(x, y, w_, rusty=0.0, coat=0.0, drip_t=None):
    """รางน้ำมองด้านหน้า (แนวนอน) — rusty 0..1 = สนิม, coat 0..1 = แถบเคลือบเทา"""
    p = [f'<g transform="translate({x:.0f},{y:.0f})">']
    p.append(f'<rect x="0" y="-34" width="{w_}" height="20" fill="#C89B6C"/>')            # เชิงชายไม้
    p.append(f'<rect x="0" y="0" width="{w_}" height="92" rx="14" fill="{METAL}" stroke="{METAL_DK}" stroke-width="6"/>')
    p.append(f'<rect x="0" y="0" width="{w_}" height="18" fill="#DFE7ED" opacity=".8"/>')  # ขอบบนเงา
    for jx in (w_*0.33, w_*0.66):                                                          # รอยเชื่อม 2 จุด
        p.append(f'<line x1="{jx:.0f}" y1="2" x2="{jx:.0f}" y2="90" stroke="{METAL_DK}" stroke-width="6"/>')
    if coat > 0:
        cw = w_ * clamp01(coat)
        p.append(f'<rect x="0" y="-6" width="{cw:.0f}" height="104" rx="14" fill="{COAT}" opacity=".95"/>')
        p.append(f'<rect x="0" y="-6" width="{cw:.0f}" height="18" fill="{COAT_HI}" opacity=".9"/>')
    if rusty > 0:
        for jx in (w_*0.33, w_*0.66):
            for dx, dy, r, dl in RUST_SPOTS[:9]:
                a = clamp01((rusty - dl*0.5) / 0.5)
                if a <= 0: continue
                p.append(f'<circle cx="{jx+dx*0.9:.0f}" cy="{46+dy*0.75:.0f}" r="{r*1.15*a:.1f}" '
                         f'fill="{RUST if (r*10)%2<1 else RUST_DK}" opacity="{0.9*a:.2f}"/>')
    if drip_t is not None:
        for i, jx in enumerate((w_*0.33, w_*0.66)):
            ph = (drip_t*0.85 + i*0.45) % 1.0
            if ph < 0.28: p.append(droplet(jx, 100, 0.5 + ph*1.8, 0.9))
            else:         p.append(droplet(jx, 100 + (ph-0.28)/0.72*380, 1.05))
    p.append('</g>')
    return "".join(p)

def gutter_xsec(cx, cy, s=1.0, coat=0.0):
    """ภาพผ่ารางรูปตัว U — coat>0 วาดชั้นเคลือบตามผิวใน-นอก"""
    p = [f'<g transform="translate({cx},{cy}) scale({s})">']
    p.append(f'<path d="M-190 -120 v120 a190 150 0 0 0 380 0 v-120" fill="none" stroke="{METAL}" stroke-width="34"/>')
    p.append(f'<path d="M-190 -120 v120 a190 150 0 0 0 380 0 v-120" fill="none" stroke="{METAL_DK}" stroke-width="6" opacity=".5"/>')
    p.append(f'<line x1="0" y1="132" x2="0" y2="166" stroke="{METAL_DK}" stroke-width="8"/>')   # แนวรอยเชื่อมก้นราง
    p.append(f'<circle cx="-14" cy="149" r="4.5" fill="{METAL_DK}"/><circle cx="14" cy="149" r="4.5" fill="{METAL_DK}"/>')
    if coat > 0:
        # เคลือบไล่จากปากรางซ้าย วนตามตัว U ไปปากขวา (คุม stroke-dash)
        length = 1150   # ประมาณความยาว path
        vis = length * clamp01(coat)
        p.append(f'<path d="M-209 -122 v122 a209 168 0 0 0 418 0 v-122" fill="none" stroke="#5C6B77" '
                 f'stroke-width="24" stroke-linecap="round" stroke-dasharray="{vis:.0f} {length}"/>')
        p.append(f'<path d="M-209 -122 v122 a209 168 0 0 0 418 0 v-122" fill="none" stroke="#8DA0AE" '
                 f'stroke-width="7" stroke-linecap="round" stroke-dasharray="{vis:.0f} {length}" opacity=".9"/>')
    p.append('</g>')
    return "".join(p)

def speech(x, y, w_, lines, name_drop=True, op=1.0, dy=0.0):
    h = 96 + 66*len(lines)
    p = [f'<g opacity="{op:.2f}" transform="translate(0,{dy:.1f})">']
    p.append(f'<rect x="{x}" y="{y}" width="{w_}" height="{h}" rx="28" fill="#12365C" stroke="#45C6F0" stroke-width="6"/>')
    p.append(f'<rect x="{x+30}" y="{y-30}" width="220" height="56" rx="28" fill="#FFC53D" stroke="#fff" stroke-width="4"/>')
    if name_drop: p.append(droplet(x+66, y-2, 0.72))
    p.append(txt(x+140, y+8, 30, "หยดหยด", fill="#5C3A00"))
    for i, (s, col, sz) in enumerate(lines):
        p.append(txt(x+w_/2, y+78+66*i, sz, s, fill=col))
    p.append('</g>')
    return "".join(p)

# ---------- เฟรมหลัก ----------
def frame(t):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    p.append('''<defs>
<radialGradient id="deep" cx="50%" cy="115%" r="110%">
  <stop offset="0%" stop-color="#0E3557"/><stop offset="65%" stop-color="#071B33"/>
</radialGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#8ED8F8"/><stop offset="100%" stop-color="#DFF4FE"/>
</linearGradient>
<linearGradient id="cta" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#FF8A3D"/><stop offset="100%" stop-color="#E86F1F"/>
</linearGradient>
</defs>''')

    # ================= ฉาก 1 (0-3) รางสองเส้น เทียบกัน =================
    if t < 4.5:
        p.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
        # ครึ่งซ้าย: รางผุ + คราบผนัง | ครึ่งขวา: รางสวย
        p.append(f'<rect x="0" y="300" width="530" height="1000" fill="#F4EFE4"/>')
        p.append(f'<rect x="550" y="300" width="530" height="1000" fill="#FBF7EE"/>')
        # คราบสนิมไหลบนผนังซ้าย
        for sx in (150, 320):
            p.append(f'<path d="M{sx} 560 q-8 130 6 260 q8 120 -4 240" stroke="#B4652F" stroke-width="16" fill="none" opacity=".45" stroke-linecap="round"/>')
        p.append(gutter_run(30, 480, 470, rusty=1.0, drip_t=t))
        p.append(gutter_run(580, 480, 470, rusty=0.0))
        p.append(f'<rect x="530" y="300" width="20" height="1000" fill="#0B2239" opacity=".25"/>')
        # ป้ายกำกับเบาๆ
        p.append(txt(265, 1250, 44, "เส้นซ้าย", fill="#7E421C", w="500"))
        p.append(txt(815, 1250, 44, "เส้นขวา", fill="#3D566E", w="500"))
        p.append(fade_txt(t, 0.3, 540, 1500, 62, "รางสองเส้น ติดวันเดียวกัน..."))
        p.append(fade_txt(t, 1.4, 540, 1615, 76, "ทำไมผุอยู่เส้นเดียว?", fill=GOLD_HL))

    # ================= ฉาก 2 (3-8) ผ่าเส้นซ้าย: โลหะเปลือย =================
    elif t < 11.5:
        ts = t - 4.5
        p.append(f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>')
        p.append(fade_txt(ts, 0.1, 540, 250, 58, "มาดูเส้นซ้ายใกล้ๆ ครับ"))
        p.append(sun(920, 420))
        # แดดส่องลงราง
        for k in range(3):
            p.append(f'<line x1="{880-26*k}" y1="{486+16*k}" x2="{660-40*k}" y2="{760+20*k}" stroke="#FFDE6B" '
                     f'stroke-width="8" opacity=".6" stroke-linecap="round"/>')
        p.append(gutter_xsec(540, 900, 1.15))
        # ฝนตกใส่โลหะตรงๆ (ตกแล้วเกาะ ไม่เด้ง)
        for i, dx in enumerate((-120, 0, 115)):
            ph = (ts*0.7 + i*0.31) % 1.0
            if ph < 0.62:
                p.append(droplet(540+dx, 300 + (ph/0.62)*(1000+dx*0.35-300), 1.15))
            else:
                p.append(f'<ellipse cx="{540+dx}" cy="{1004+dx*0.35:.0f}" rx="{26*(1-(ph-0.62)/0.38*0.3):.0f}" ry="9" '
                         f'fill="#5FB7E8" opacity="{0.9*(1-(ph-0.62)/0.38):.2f}"/>')
        # สนิมบานจากรอยเชื่อมก้นราง
        rp = ease_io(P(ts, 2.4, 2.2))
        if rp > 0:
            for dx, dy, r, dl in RUST_SPOTS:
                a = clamp01((rp - dl*0.55) / 0.45)
                if a <= 0: continue
                p.append(f'<circle cx="{540+dx:.0f}" cy="{1032+dy*0.8:.0f}" r="{r*a:.1f}" '
                         f'fill="{RUST if (r*10)%2<1 else RUST_DK}" opacity="{0.92*a:.2f}"/>')
            pu = 0.5 + 0.5*math.sin(ts*4.5)
            p.append(f'<circle cx="540" cy="1046" r="{74+10*pu:.0f}" fill="none" stroke="{GOLD_HL}" '
                     f'stroke-width="6" opacity="{(0.25+0.45*pu)*min(1,rp*2):.2f}"/>')
        p.append(fade_txt(ts, 1.2, 540, 1400, 62, "โลหะเปลือย เจอฝนเจอแดดตรงๆ"))
        p.append(fade_txt(ts, 2.8, 540, 1515, 74, "สนิมเริ่มที่รอยเชื่อมก่อนเสมอ", fill=GOLD_HL))

    # ================= ฉาก 3 (8-13) ผ่าเส้นขวา: มีชั้นเคลือบ =================
    elif t < 18.5:
        ts = t - 11.5
        p.append(f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>')
        p.append(fade_txt(ts, 0.1, 540, 250, 58, "ส่วนเส้นขวา..."))
        coat = ease_io(P(ts, 0.5, 1.1))
        p.append(gutter_xsec(540, 860, 1.0, coat=coat))
        if 0 < P(ts, 1.55, 0.6) < 1:
            pu = P(ts, 1.55, 0.6)
            p.append(star(540, 660, 0.6+1.5*pu, 1-pu))
        # ฝนตกแล้วเด้งออกจากชั้นเคลือบ
        if ts > 1.9:
            for i, dx in enumerate((-140, 40, 150)):
                ph = ((ts-1.9)*0.75 + i*0.33) % 1.0
                land_y = 964 + abs(dx)*0.28
                if ph < 0.5:
                    p.append(droplet(540+dx, 300 + (ph/0.5)*(land_y-300), 1.15))
                else:
                    e = (ph-0.5)/0.5
                    p.append(droplet(540+dx+ (60 if dx>=0 else -60)*e, land_y - 150*math.sin(e*math.pi), 1.0*(1-0.4*e), 1-e*0.85))
        # หยดหยดชี้ + กล่องพูด
        pM = P(ts, 0.9, 0.5)
        if pM > 0:
            e = ease_back(pM)
            arm = -22 - 7*math.sin(ts*3)
            p.append(f'<g transform="translate(50,{1180+30*(1-min(1,pM)):.0f}) scale({min(1,e):.2f})">' +
                     mascot(0, 0, 2.5, arm) + '</g>')
        pB = P(ts, 1.4, 0.45)
        if pB > 0:
            e = ease_out(pB)
            p.append(speech(320, 1260, 700, [("มีชั้นเคลือบบางๆ รับไว้ครับ", "#EAF6FF", 48),
                                             ("เนื้อโลหะข้างใน ไม่โดนเลย", "#FFC53D", 52)], op=e, dy=14*(1-e)))

    # ================= ฉาก 4 (13-17) ทางแก้: ทาตั้งแต่วันแรก =================
    elif t < 24.0:
        ts = t - 18.5
        p.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
        p.append(f'<rect x="0" y="330" width="{W}" height="900" fill="#FBF7EE"/>')
        prog = ease_io(P(ts, 0.5, 2.2))
        p.append(gutter_run(60, 620, 960, rusty=0.0, coat=prog))
        # ลูกกลิ้งวิ่งตามขอบหน้าเคลือบ
        rx = 60 + 960*min(prog, 0.985)
        if prog > 0:
            p.append(f'<g transform="translate({rx:.0f},640)">'
                     f'<line x1="0" y1="-26" x2="60" y2="-140" stroke="#C98F00" stroke-width="12" stroke-linecap="round"/>'
                     f'<rect x="-26" y="-46" width="52" height="86" rx="22" fill="{COAT}" stroke="{COAT_HI}" stroke-width="5"/></g>')
        if prog >= 1 and P(ts, 2.75, 0.6) < 1:
            pu = P(ts, 2.75, 0.6)
            p.append(star(1010, 600, 0.6+1.6*pu, 1-pu))
        # หยดหยดยืนเชียร์ข้างราง
        arm = -20 - 8*math.sin(ts*2.6)
        p.append(f'<g transform="translate(60,830)">' + mascot(0, 0, 2.9, arm) + '</g>')
        p.append(fade_txt(ts, 1.1, 540, 1400, 66, "ทาเคลือบไว้ตั้งแต่วันแรก"))
        p.append(fade_txt(ts, 1.8, 540, 1520, 80, "ตอนรางยังใหม่", fill=GOLD_HL))
        p.append(fade_txt(ts, 2.7, 540, 1620, 44, "ง่ายกว่า ประหยัดกว่า มาตามแก้ทีหลังเยอะครับ", fill="#3D566E", w="500"))

    # ================= ฉาก 5 (17-21) เฟรมปิดซีรีส์ (มาตรฐาน) =================
    else:
        ts = t - 24.0
        p.append(f'<rect width="{W}" height="{H}" fill="url(#deep)"/>')
        p.append(bubbles(t))
        pM = P(ts, 0.1, 0.45)
        if pM > 0:
            e = ease_back(pM)
            arm = -16.0
            pW = P(ts, 0.6, 2.2)
            if 0 < pW < 1: arm = -24*abs(math.sin(pW*3*math.pi))
            p.append(f'<g transform="translate({540-50*3.6:.0f},{520+40*(1-min(1,pM)):.0f}) scale({min(1,e):.2f})">'
                     + mascot(0, 0, 3.6, arm) + '</g>')
        pB = P(ts, 0.6, 0.4)
        if pB > 0:
            e = ease_out(pB)
            p.append(f'<g opacity="{e:.2f}" transform="translate(0,{14*(1-e):.0f})">'
                     f'<rect x="270" y="1050" width="540" height="104" rx="52" fill="#FFC53D" stroke="#fff" stroke-width="5"/>'
                     + txt(540, 1119, 50, "หยดหยดเล่า EP.2", fill="#5C3A00") + '</g>')
        pU = P(ts, 1.0, 0.45)
        if pU > 0:
            e = ease_out(pU)
            pulse = 0.5 + 0.5*math.sin((ts-1.5)*2*math.pi/1.4) if ts > 1.5 else 0
            p.append(f'<g opacity="{e:.2f}" transform="translate(0,{14*(1-e):.0f})">'
                     f'<rect x="160" y="1220" width="760" height="138" rx="69" fill="#FFC53D" opacity="{0.35*pulse:.2f}"/>'
                     f'<rect x="170" y="1230" width="740" height="118" rx="59" fill="url(#cta)" stroke="#fff" stroke-width="5"/>'
                     + txt(540, 1307, 56, "lucernapro.com", fill="#fff") + '</g>')

    p.append('</svg>')
    return "".join(p)

if __name__ == "__main__":
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    b = int(sys.argv[2]) if len(sys.argv) > 2 else N
    for i in range(a, b):
        with open(f"{OUT}/f_{i:04d}.svg", "w") as f:
            f.write(frame(i / FPS))
    print(f"frames {a}..{b-1} written")
