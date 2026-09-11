#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""หยดหยดเล่า EP.3 — 'ทาแล้วยังหยด' 1080x1920 30fps 32s = 960 เฟรม
ความจริงหนึ่งข้อ: จุดที่หยด ไม่ใช่จุดที่น้ำเข้า — รู้จุดจริง ดินน้ำมันก็อุดอยู่"""
import math, os, sys
sys.path.insert(0, "/home/claude")
from gen_frames import (W, H, mascot, droplet, bubbles, clamp01, P,
                        ease_out, ease_in, ease_io, ease_back, esc)

FPS, DUR = 30, 32.0
N = int(FPS * DUR)
OUT = "/home/claude/frames_ep3"
os.makedirs(OUT, exist_ok=True)

INK = "#0B2239"; GOLD_HL = "#E8A200"
SLAB = "#B9C6D2"; SLAB_DK = "#8FA3B5"; COAT = "#3D6B7A"; COAT_HI = "#6FA0AE"
WALL = "#FFF6E8"; WALL_LN = "#D9C6A8"; WATER = "#5FB7E8"; RED = "#E0533F"; CLAY = "#B48A68"

# ---------- helpers ----------
def txt(x, y, size, s, fill=INK, w="600", anchor="middle", op=1.0, dy=0.0):
    return (f'<text x="{x}" y="{y+dy:.0f}" text-anchor="{anchor}" font-family="Mitr" font-weight="{w}" '
            f'font-size="{size}" fill="{fill}" opacity="{op:.2f}">{esc(s)}</text>')

def fade_txt(t, t0, x, y, size, s, fill=INK, w="600"):
    p = P(t, t0, 0.4)
    if p <= 0: return ""
    e = ease_out(p)
    return txt(x, y, size, s, fill, w, op=e, dy=14*(1-e))

def star(x, y, s, op, col="#FFC53D"):
    return (f'<g transform="translate({x:.0f},{y:.0f}) scale({s:.2f}) rotate({int(40*s)%360})" opacity="{op:.2f}">'
            f'<path d="M0 -10 l3 6 6 1 -4.5 4.5 1 6.5 -5.5 -3 -5.5 3 1 -6.5 -4.5 -4.5 6 -1z" fill="{col}"/></g>')

def rain(t, x0, x1, y0, y1, n=9, seed=0, speed=1.0):
    p = []
    for i in range(n):
        x = x0 + (x1-x0) * ((i*0.618 + seed*0.37) % 1.0)
        ph = (t*speed*0.8 + i*0.173 + seed*0.11) % 1.0
        y = y0 + ph*(y1-y0)
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x-6:.0f}" y2="{y+46:.0f}" stroke="{WATER}" '
                 f'stroke-width="7" stroke-linecap="round" opacity="{0.85*(1-ph*0.4):.2f}"/>')
    return "".join(p)

def drip(t, x, y, period=1.4, phase=0.0, fall=420, s=1.1):
    """หยดจากเพดานที่ (x,y) ลงมา fall px"""
    ph = ((t + phase) % period) / period
    if ph < 0.3:
        return droplet(x, y + 4, s*(0.45 + ph/0.3*0.55), 0.95)
    e = (ph-0.3)/0.7
    return droplet(x, y + 4 + ease_in(e)*fall, s, 1 - max(0, e-0.85)/0.15)

def bucket(x, y, water=0.0):
    p = [f'<path d="M{x-62} {y} L{x+62} {y} L{x+50} {y+150} L{x-50} {y+150} Z" fill="#E86F1F"/>']
    if water > 0:
        wy = y + 150 - 130*clamp01(water)
        p.append(f'<path d="M{x-62+12*water:.0f} {wy:.0f} L{x+62-12*water:.0f} {wy:.0f} L{x+50} {y+150} L{x-50} {y+150} Z" fill="{WATER}" opacity=".8"/>')
    p.append(f'<ellipse cx="{x}" cy="{y}" rx="62" ry="14" fill="#FF8A3D"/>')
    return "".join(p)

def speech(x, y, w_, lines, op=1.0, dy=0.0):
    h = 96 + 66*len(lines)
    p = [f'<g opacity="{op:.2f}" transform="translate(0,{dy:.1f})">']
    p.append(f'<rect x="{x}" y="{y}" width="{w_}" height="{h}" rx="28" fill="#12365C" stroke="#45C6F0" stroke-width="6"/>')
    p.append(f'<rect x="{x+30}" y="{y-30}" width="220" height="56" rx="28" fill="#FFC53D" stroke="#fff" stroke-width="4"/>')
    p.append(droplet(x+66, y-2, 0.72))
    p.append(txt(x+140, y+8, 30, "หยดหยด", fill="#5C3A00"))
    for i, (s, col, sz) in enumerate(lines):
        p.append(txt(x+w_/2, y+78+66*i, sz, s, fill=col))
    p.append('</g>')
    return "".join(p)

def house_xsec(y, coat=1.0, shine_t=None):
    """บ้านผ่าข้าง: ดาดฟ้า (แผ่นพื้น+กันซึม) และห้องข้างล่าง — คืน y ของเพดาน"""
    p = []
    p.append(f'<rect x="120" y="{y+70}" width="840" height="620" fill="{WALL}" stroke="{WALL_LN}" stroke-width="6"/>')
    p.append(f'<rect x="200" y="{y+300}" width="150" height="220" fill="#E4F4FB" stroke="#BFE2F2" stroke-width="6"/>')
    p.append(f'<rect x="90" y="{y}" width="900" height="76" fill="{SLAB}" stroke="{SLAB_DK}" stroke-width="6"/>')
    p.append(f'<rect x="90" y="{y-80}" width="34" height="86" fill="{SLAB}" stroke="{SLAB_DK}" stroke-width="6"/>')
    p.append(f'<rect x="956" y="{y-80}" width="34" height="86" fill="{SLAB}" stroke="{SLAB_DK}" stroke-width="6"/>')
    if coat > 0:
        cw = 832*clamp01(coat)
        p.append(f'<rect x="124" y="{y-22}" width="{cw:.0f}" height="24" rx="6" fill="{COAT}"/>')
        p.append(f'<rect x="124" y="{y-22}" width="{cw:.0f}" height="8" rx="4" fill="{COAT_HI}" opacity=".9"/>')
        if shine_t is not None:
            sx = 124 + ((shine_t*0.35) % 1.0) * 832
            p.append(f'<rect x="{sx:.0f}" y="{y-22}" width="70" height="24" rx="6" fill="#fff" opacity=".35"/>')
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

    # ================= ฉาก 1 (0-5) เพิ่งทา ฝนตก ยังหยด =================
    if t < 5.0:
        p.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
        cy = 720
        p.append(house_xsec(cy, coat=1.0, shine_t=t))
        if t > 1.2: p.append(rain(t, 60, 1020, 120, cy-60, n=11, seed=1))
        if t > 2.4:
            p.append(f'<ellipse cx="620" cy="{cy+80}" rx="90" ry="16" fill="#C9B58A"/>')
            p.append(drip(t, 620, cy+84, period=1.3))
            p.append(bucket(620, cy+560, water=0.25))
        p.append(fade_txt(t, 0.3, 540, 1520, 62, "เพิ่งทากันซึมได้ 3 วัน... ฝนตก"))
        p.append(fade_txt(t, 1.6, 540, 1640, 80, "ทำไมยังหยด?", fill=GOLD_HL))

    # ================= ฉาก 2 (5-12) มีแค่สองแบบ =================
    elif t < 12.0:
        ts = t - 5.0
        p.append(f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>')
        p.append(fade_txt(ts, 0.1, 540, 250, 62, "มันมีแค่ 2 แบบครับ"))
        # สองห้อง
        for i, x0 in enumerate((0, 550)):
            p.append(f'<rect x="{x0}" y="400" width="530" height="900" fill="{WALL}"/>')
            p.append(f'<rect x="{x0}" y="400" width="530" height="70" fill="{SLAB}"/>')
            cx = x0 + 265
            p.append(f'<ellipse cx="{cx}" cy="470" rx="{80 if i==0 else 110}" ry="14" fill="#C9B58A"/>')
            if i == 0:
                p.append(drip(ts, cx, 474, period=3.0, fall=560))
                p.append(bucket(cx, 1040, water=0.15))
            else:
                p.append(drip(ts, cx, 474, period=0.75, fall=560))
                p.append(drip(ts, cx, 474, period=0.75, phase=0.37, fall=560))
                p.append(bucket(cx, 1040, water=0.75))
        p.append(f'<rect x="530" y="400" width="20" height="900" fill="{INK}" opacity=".25"/>')
        p.append(fade_txt(ts, 0.9, 265, 1380, 54, "ดีขึ้นนิดหน่อย", fill="#3D566E"))
        p.append(fade_txt(ts, 2.2, 815, 1380, 54, "ไม่ดีขึ้นเลย", fill="#7E421C"))
        p.append(fade_txt(ts, 3.4, 540, 1560, 66, "สองแบบนี้"))
        p.append(fade_txt(ts, 3.9, 540, 1670, 76, "บอกคนละเรื่องกันเลย", fill=GOLD_HL))

    # ================= ฉาก 3 (12-18.5) ดีขึ้นนิดหน่อย = ทายังไม่ครบ =================
    elif t < 18.5:
        ts = t - 12.0
        p.append(f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>')
        p.append(fade_txt(ts, 0.1, 540, 230, 62, "ดีขึ้นนิดหน่อย = กันซึมทำงานครับ"))
        # ดาดฟ้ามองจากบน
        p.append(f'<rect x="90" y="330" width="900" height="820" fill="{SLAB_DK}"/>')
        p.append(f'<rect x="150" y="390" width="780" height="700" fill="{SLAB}"/>')
        p.append(f'<rect x="150" y="450" width="780" height="640" fill="{COAT}"/>')      # ไม่ขึ้นขอบด้านบน
        p.append(f'<rect x="590" y="820" width="220" height="180" fill="{COAT_HI}" opacity=".6"/>')  # บางไป
        p.append(f'<path d="M280 560 q40 -26 80 0 q14 40 -26 60 q-54 6 -54 -60z" fill="{SLAB}"/>')  # พลาดจุด
        p.append(f'<circle cx="640" cy="620" r="6" fill="{SLAB}"/>')                      # pinhole
        flaws = [(0.9, 320, 590, 80), (1.8, 640, 620, 44), (2.7, 700, 910, 130)]
        for t0, cx, cy, r in flaws:
            pf = P(ts, t0, 0.35)
            if pf > 0:
                e = ease_back(min(1, pf))
                p.append(f'<circle cx="{cx}" cy="{cy}" r="{r*e:.0f}" fill="none" stroke="{RED}" stroke-width="9"/>')
        pf = P(ts, 3.6, 0.35)
        if pf > 0:
            e = ease_out(pf)
            p.append(f'<rect x="140" y="380" width="800" height="80" rx="16" fill="none" stroke="{RED}" stroke-width="9" opacity="{e:.2f}"/>')
        pw = P(ts, 4.0, 0.8)
        if pw > 0:
            p.append(f'<rect x="150" y="392" width="780" height="58" fill="{WATER}" opacity="{0.8*ease_out(pw):.2f}"/>')
        p.append(fade_txt(ts, 0.9, 540, 1300, 62, "แค่ทายังไม่ครบ"))
        p.append(fade_txt(ts, 1.8, 540, 1410, 52, "พลาดจุด · รูเข็ม · บางไป", fill="#3D566E", w="500"))
        p.append(fade_txt(ts, 3.6, 540, 1530, 72, "หรือทาไม่ถึงขอบ", fill=GOLD_HL))
        # หยดหยดชี้จากมุมล่างซ้าย
        arm = -22 - 7*math.sin(ts*3)
        p.append(f'<g transform="translate(40,1580)">' + mascot(0, 0, 2.4, arm) + '</g>')

    # ================= ฉาก 4 (18.5-25) ไม่ดีขึ้นเลย = ทาผิดจุด =================
    elif t < 25.0:
        ts = t - 18.5
        p.append(f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>')
        p.append(fade_txt(ts, 0.1, 540, 230, 62, "ไม่ดีขึ้นเลย = ทาผิดจุดครับ"))
        cy = 560
        p.append(house_xsec(cy, coat=1.0))
        # รอยร้าวใกล้ขอบซ้าย
        p.append(f'<path d="M200 {cy-22} l10 30 l-14 30 l12 36" stroke="{INK}" stroke-width="5" fill="none"/>')
        p.append(rain(ts, 150, 260, 200, cy-60, n=4, seed=3))
        # น้ำเดินทางในแผ่นพื้น → ไปหยดฝั่งขวา
        length = 900
        vis = length * ease_io(P(ts, 0.6, 2.2))
        p.append(f'<path d="M205 {cy-10} L212 {cy+40} Q540 {cy+58} 800 {cy+58} L800 {cy+76}" fill="none" stroke="{WATER}" '
                 f'stroke-width="18" stroke-linecap="round" stroke-dasharray="{vis:.0f} {length}"/>')
        if P(ts, 2.6, 0.1) > 0:
            p.append(f'<ellipse cx="800" cy="{cy+80}" rx="90" ry="16" fill="#C9B58A"/>')
            p.append(drip(ts, 800, cy+84, period=1.2))
        # แปรงไปทาฝั่งที่หยด (ผิดจุด)
        pb = P(ts, 3.0, 0.7)
        if pb > 0:
            e = ease_out(pb)
            p.append(f'<rect x="{800-140*e:.0f}" y="{cy-30}" width="{280*e:.0f}" height="30" rx="8" fill="{RED}" opacity=".9"/>')
            bx = 800 + 140*e
            p.append(f'<g transform="translate({bx:.0f},{cy-34})"><rect x="-34" y="-20" width="68" height="22" rx="6" fill="{RED}"/>'
                     f'<rect x="-8" y="-110" width="16" height="92" rx="6" fill="#8A5A32"/></g>')
        # หยดหยด + กล่องพูด
        pM = P(ts, 0.4, 0.5)
        if pM > 0:
            e = ease_back(pM)
            arm = -22 - 7*math.sin(ts*3)
            p.append(f'<g transform="translate(50,{1290+30*(1-min(1,pM)):.0f}) scale({min(1,e):.2f})">' +
                     mascot(0, 0, 2.5, arm) + '</g>')
        pB = P(ts, 1.0, 0.45)
        if pB > 0:
            e = ease_out(pB)
            p.append(speech(320, 1370, 700, [("น้ำหยดตรงนี้...", "#EAF6FF", 48),
                                             ("แต่เข้าตรงโน้นครับ", "#FFC53D", 52)], op=e, dy=14*(1-e)))
        p.append(fade_txt(ts, 3.8, 540, 1720, 66, "ทาตรงที่หยด เลยไม่ดีขึ้น", fill=GOLD_HL))

    # ================= ฉาก 5 (25-29.5) รู้จุดจริง ดินน้ำมันก็อยู่ =================
    elif t < 29.5:
        ts = t - 25.0
        p.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
        cy = 640
        p.append(house_xsec(cy, coat=1.0))
        p.append(f'<path d="M200 {cy-22} l10 30 l-14 30 l12 36" stroke="{INK}" stroke-width="5" fill="none"/>')
        # หยดฝั่งขวายังหยดจนกว่าดินน้ำมันจะกด
        p.append(f'<ellipse cx="800" cy="{cy+80}" rx="90" ry="16" fill="#C9B58A"/>')
        stop = P(ts, 1.4, 0.01) > 0
        if not stop:
            p.append(drip(ts, 800, cy+84, period=1.2))
        else:
            fo = 1 - P(ts, 1.4, 0.9)
            if fo > 0: p.append(droplet(800, cy+88, 0.8, fo*0.9))
        # ดินน้ำมัน + มือ กดลงบนรอยร้าว
        pp = P(ts, 0.3, 1.2)
        if pp > 0:
            e = ease_io(pp)
            y = cy - 260 + 236*e
            sq = 1 + 0.5*clamp01((pp-0.85)/0.15); sy_ = 1 - 0.45*clamp01((pp-0.85)/0.15)
            p.append(f'<g transform="translate(205,{y:.0f}) scale({sq:.2f},{sy_:.2f})"><ellipse rx="64" ry="46" fill="{CLAY}" stroke="#8A6448" stroke-width="5"/></g>')
            # มือแบบการ์ตูน: ฝ่ามือ + นิ้ว 4 กดลงมาจากบน
            hy = y - 18
            p.append(f'<g transform="translate(205,{hy:.0f})">'
                     f'<rect x="-70" y="-190" width="140" height="150" rx="46" fill="#F2C9A3" stroke="#C99A70" stroke-width="5"/>'
                     f'<rect x="-88" y="-120" width="44" height="24" rx="12" fill="#F2C9A3" stroke="#C99A70" stroke-width="5"/>'
                     + "".join(f'<rect x="{-62+34*k}" y="-70" width="30" height="{58 if k in (1,2) else 46}" rx="15" fill="#F2C9A3" stroke="#C99A70" stroke-width="5"/>' for k in range(4))
                     + '</g>')
        if 0 < P(ts, 1.45, 0.6) < 1:
            pu = P(ts, 1.45, 0.6)
            p.append(star(205, cy-60, 0.6+1.6*pu, 1-pu))
        arm = -20 - 8*math.sin(ts*2.6)
        p.append(f'<g transform="translate(720,1120)">' + mascot(0, 0, 2.4, arm) + '</g>')
        p.append(fade_txt(ts, 0.4, 540, 1480, 62, "รู้จุดจริง ดินน้ำมันก็อุดอยู่ครับ"))
        p.append(fade_txt(ts, 1.5, 540, 1590, 48, "ต่างกันแค่อยู่ได้นานแค่ไหน", fill="#3D566E", w="500"))
        p.append(fade_txt(ts, 2.3, 540, 1710, 80, "หาจุดน้ำเข้าให้เจอก่อน", fill=GOLD_HL))

    # ================= ฉาก 6 (29.5-32) เฟรมปิดซีรีส์ (มาตรฐาน) =================
    else:
        ts = t - 29.5
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
                     + txt(540, 1119, 50, "หยดหยดเล่า EP.3", fill="#5C3A00") + '</g>')
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
