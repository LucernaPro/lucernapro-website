#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""หยดหยดสอน EP.1 — 'ยาแนวคือฟองน้ำ' 1080x1920 30fps 22s = 660 เฟรม"""
import math, os, random, sys
sys.path.insert(0, "/home/claude")
from gen_frames import (W, H, mascot, droplet, bubbles, clamp01, P,
                        ease_out, ease_in, ease_io, ease_back, esc)

FPS, DUR = 30, 22.0
N = int(FPS * DUR)
OUT = "/home/claude/frames_ep1"
os.makedirs(OUT, exist_ok=True)

INK = "#0B2239"; GOLD = "#C98F00"; GOLD_HL = "#E8A200"
random.seed(11)
PORES = [(random.uniform(0.12,0.88), random.uniform(0.05,0.95), random.uniform(6,16)) for _ in range(26)]

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

def bounce_drop(t, t0, x0, y_land, dxs, scale=1.4):
    """หยดตกถึง y_land แล้วเด้งแตกเป็นหยดเล็กโค้งออก + ดาวติ๊ง"""
    out = []
    pF = P(t, t0, 0.55)
    if 0 < pF < 1:
        y = y_land - 320 + ease_in(pF) * 320
        out.append(droplet(x0, y, scale))
    pB = P(t, t0 + 0.55, 0.6)
    if 0 < pB < 1:
        e = ease_out(pB)
        for dx, vy in dxs:
            bx = x0 + dx * e
            by = y_land - vy * math.sin(min(1, pB) * math.pi)
            out.append(droplet(bx, by, scale * 0.55 * (1 - 0.5 * pB), 1 - pB))
        out.append(star(x0, y_land - 30, 0.8 + 2.0 * pB, 1 - pB))
    return "".join(out)

# ---------- ภาพตัดขวางพื้น (ฉาก 2 และ 4) ----------
TILES = [(60, 380), (432, 752), (804, 1020)]   # x0,x1 ต่อแผ่น
GROUTS = [(380, 432), (752, 804)]
Y_TOP, Y_TILE_B, Y_MORTAR_B, Y_SLAB_B = 690, 810, 950, 1080

def xsec(seep=0.0, epoxy=0.0):
    p = [f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>']
    # ห้องชั้นล่าง
    p.append(f'<rect x="0" y="{Y_SLAB_B}" width="{W}" height="{1560-Y_SLAB_B}" fill="#FFF9F0"/>')
    p.append(f'<rect x="0" y="1560" width="{W}" height="360" fill="#EADFCC"/>')
    # โครงสร้างพื้น
    p.append(f'<rect x="0" y="{Y_TILE_B}" width="{W}" height="{Y_MORTAR_B-Y_TILE_B}" fill="#E8DCC8"/>')
    p.append(f'<rect x="0" y="{Y_MORTAR_B}" width="{W}" height="{Y_SLAB_B-Y_MORTAR_B}" fill="#C9CFD6"/>')
    for i in range(24):
        p.append(f'<circle cx="{45*i+20}" cy="{Y_MORTAR_B+30+(i%3)*28}" r="4" fill="#AEB6C0"/>')
    # กระเบื้อง
    for x0, x1 in TILES:
        p.append(f'<rect x="{x0}" y="{Y_TOP}" width="{x1-x0}" height="{Y_TILE_B-Y_TOP}" '
                 f'fill="#DCEFF8" stroke="#9FBFD4" stroke-width="6"/>')
        p.append(f'<line x1="{x0+18}" y1="{Y_TOP+14}" x2="{x1-18}" y2="{Y_TOP+14}" '
                 f'stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".85"/>')
    # ร่องยาแนว
    for gx0, gx1 in GROUTS:
        p.append(f'<rect x="{gx0}" y="{Y_TOP}" width="{gx1-gx0}" height="{Y_TILE_B-Y_TOP}" fill="#D9CDB6"/>')
        if seep > 0:
            hh = (Y_TILE_B - Y_TOP) * clamp01(seep)
            p.append(f'<rect x="{gx0}" y="{Y_TOP}" width="{gx1-gx0}" height="{hh:.0f}" fill="#2E86BD" opacity=".9"/>')
        if epoxy > 0:
            hh = (Y_TILE_B - Y_TOP) * clamp01(epoxy)
            p.append(f'<rect x="{gx0}" y="{Y_TILE_B-hh:.0f}" width="{gx1-gx0}" height="{hh:.0f}" fill="#1E4E74"/>')
    return "".join(p)

# ---------- เฟรมหลัก ----------
def frame(t):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    p.append('''<defs>
<radialGradient id="deep" cx="50%" cy="115%" r="110%">
  <stop offset="0%" stop-color="#0E3557"/><stop offset="65%" stop-color="#071B33"/>
</radialGradient>
<linearGradient id="cta" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#FF8A3D"/><stop offset="100%" stop-color="#E86F1F"/>
</linearGradient>
</defs>''')

    # ================= ฉาก 1 (0-3) ห้องน้ำบน / เพดานหยดล่าง =================
    if t < 3.0:
        p.append(f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>')
        # ห้องน้ำ (บน)
        p.append(f'<rect x="60" y="180" width="960" height="620" fill="#E4F4FB" stroke="#B9D6E6" stroke-width="6"/>')
        for gy in (330, 480, 630):
            p.append(f'<line x1="60" y1="{gy}" x2="1020" y2="{gy}" stroke="#CFE7F2" stroke-width="4"/>')
        for gx in (300, 540, 780):
            p.append(f'<line x1="{gx}" y1="180" x2="{gx}" y2="800" stroke="#CFE7F2" stroke-width="4"/>')
        # ฝักบัว + ละอองน้ำ
        p.append('<path d="M170 240 v90 h100" stroke="#7C93A8" stroke-width="18" fill="none" stroke-linecap="round"/>')
        for k in range(6):
            ph = (t*2 + k*0.35) % 1.0
            p.append(droplet(285 + k*16, 350 + ph*330, 0.75, 1-ph*0.4))
        # แอ่งน้ำบนพื้น (โตขึ้น)
        wgrow = 150 + 250 * ease_out(P(t, 0.2, 2.0))
        p.append(f'<ellipse cx="420" cy="792" rx="{wgrow:.0f}" ry="18" fill="#5FB7E8" opacity=".85"/>')
        p.append(f'<rect x="60" y="800" width="960" height="70" fill="#C9CFD6"/>')
        # ห้องล่าง + เพดานหยด
        p.append(f'<rect x="60" y="870" width="960" height="560" fill="#FFF9F0" stroke="#E3D6BE" stroke-width="6"/>')
        for i, dx in enumerate((430, 520, 610)):
            ph = (t*0.9 + i*0.33) % 1.0
            if ph < 0.25:   # หยดกำลังก่อตัวที่เพดาน
                p.append(droplet(dx, 890, 0.5 + ph*2.2, 0.9))
            else:           # หยดตก
                fall = (ph-0.25)/0.75
                p.append(droplet(dx, 890 + fall*440, 1.05, 1))
        # กะละมัง
        p.append('<path d="M400 1340 a120 60 0 0 0 240 0 z" fill="#FF8A3D" stroke="#D45F12" stroke-width="6"/>')
        p.append('<ellipse cx="520" cy="1340" rx="120" ry="24" fill="#FFB37A"/>')
        p.append('<ellipse cx="520" cy="1340" rx="92" ry="16" fill="#5FB7E8"/>')
        # คำถามเปิด
        p.append(fade_txt(t, 0.3, 540, 1580, 62, "กระเบื้องก็ไม่แตกสักแผ่น..."))
        p.append(fade_txt(t, 1.3, 540, 1690, 74, "แล้วน้ำลงไปได้ไง?", fill=GOLD_HL))

    # ================= ฉาก 2 (3-9) ผ่าพื้น: เด้ง vs มุด =================
    elif t < 9.0:
        seep = ease_out(P(t, 6.9, 1.8))
        p.append(xsec(seep=seep))
        p.append(fade_txt(t, 3.1, 540, 300, 58, "มาดูใต้พื้นกันครับ", fill=INK))
        # หยดตกใส่กระเบื้อง -> เด้ง
        p.append(bounce_drop(t, 3.5, 220, Y_TOP-10, [(-120, 160), (115, 140)], scale=1.9))
        p.append(fade_txt(t, 4.7, 540, 430, 68, "น้ำไม่ได้มุดกระเบื้อง"))
        # หยดตกใส่ร่องยาแนว -> มุดหาย
        pF = P(t, 6.0, 0.55)
        if 0 < pF < 1:
            p.append(droplet(778, Y_TOP-330 + ease_in(pF)*320, 1.9))
        pS = P(t, 6.55, 0.5)
        if 0 < pS < 1:
            p.append(droplet(778, Y_TOP-10 + pS*70, 1.9*(1-0.5*pS), 1-pS))
        p.append(fade_txt(t, 6.9, 540, 550, 80, "มันมุดร่องยาแนว!", fill=GOLD_HL))
        if 6.6 < t < 9.0:
            for gx0, gx1 in GROUTS:
                pu = 0.5 + 0.5*math.sin(t*5)
                p.append(f'<rect x="{gx0-8}" y="{Y_TOP-8}" width="{gx1-gx0+16}" height="{Y_TILE_B-Y_TOP+16}" '
                         f'fill="none" stroke="#E8A200" stroke-width="6" opacity="{0.3+0.5*pu:.2f}" rx="8"/>')

    # ================= ฉาก 3 (9-14) ซูมร่อง = ฟองน้ำ =================
    elif t < 14.0:
        ts = t - 9.0
        p.append(f'<rect width="{W}" height="{H}" fill="#EEF5FA"/>')
        # กระเบื้องซ้าย-ขวา (ขยายใหญ่)
        p.append(f'<rect x="0" y="240" width="390" height="600" fill="#DCEFF8" stroke="#9FBFD4" stroke-width="6"/>')
        p.append(f'<rect x="690" y="240" width="390" height="600" fill="#DCEFF8" stroke="#9FBFD4" stroke-width="6"/>')
        # ร่องยาแนวยักษ์ + รูพรุน
        p.append(f'<rect x="390" y="240" width="300" height="600" fill="#D9CDB6"/>')
        for fx, fy, fr in PORES:
            p.append(f'<circle cx="{390+fx*300:.0f}" cy="{240+fy*600:.0f}" r="{fr:.0f}" fill="#C3B394"/>')
        # น้ำซึมไหลลงตามรู
        prog = ease_io(P(ts, 0.2, 2.4))
        if prog > 0:
            depth = 240 + prog * 600
            p.append(f'<rect x="390" y="240" width="300" height="{depth-240:.0f}" fill="#4FA8DC" opacity=".45"/>')
            for k, (fx, fy, fr) in enumerate(PORES):
                cy = 240 + fy*600
                if cy < depth:
                    p.append(f'<circle cx="{390+fx*300:.0f}" cy="{cy:.0f}" r="{fr:.0f}" fill="#2E86BD" opacity=".8"/>')
            wig = 540 + 34*math.sin(ts*4)
            p.append(droplet(wig, min(depth, 828), 0.9, 0.95))
        # ชั้นปูนใต้กระเบื้อง + น้ำขังสะสม
        p.append(f'<rect x="0" y="840" width="{W}" height="140" fill="#E8DCC8"/>')
        pool = ease_out(P(ts, 2.2, 1.6))
        if pool > 0:
            p.append(f'<ellipse cx="540" cy="905" rx="{60+380*pool:.0f}" ry="{16+22*pool:.0f}" fill="#4FA8DC" opacity=".85"/>')
        p.append(f'<rect x="0" y="980" width="{W}" height="90" fill="#C9CFD6"/>')
        # ห้องล่าง + หยดทะลุเพดาน
        p.append(f'<rect x="0" y="1070" width="{W}" height="620" fill="#FFF9F0"/>')
        if ts > 3.0:
            ph = ((ts-3.0)*0.8) % 1.0
            if ph < 0.3: p.append(droplet(540, 1082, 0.5+ph*2.0, 0.9))
            else:        p.append(droplet(540, 1082 + (ph-0.3)/0.7*420, 1.05))
            p.append('<ellipse cx="540" cy="1560" rx="110" ry="20" fill="#5FB7E8" opacity=".7"/>')
        # หยดหยดชี้ + ป้าย
        pM = P(ts, 1.2, 0.5)
        if pM > 0:
            e = ease_back(pM)
            arm = -20 - 8*math.sin(ts*3)
            p.append(f'<g transform="translate(40,{1150+30*(1-e):.0f}) scale({e:.2f})">' +
                     mascot(0, 0, 2.6, arm) + '</g>')
        pB = P(ts, 1.6, 0.45)
        if pB > 0:
            e = ease_out(pB)
            p.append(f'<g opacity="{e:.2f}" transform="translate(0,{14*(1-e):.0f})">'
                     f'<rect x="330" y="1210" width="700" height="150" rx="28" fill="#12365C" stroke="#45C6F0" stroke-width="6"/>'
                     + txt(680, 1268, 50, "ยาแนวปูนเนื้อพรุน", fill="#EAF6FF")
                     + txt(680, 1334, 56, "= ฟองน้ำดีๆ นี่เอง!", fill="#FFC53D") + '</g>')

    # ================= ฉาก 4 (14-18) เปลี่ยนร่อง = น้ำเด้งหมด =================
    elif t < 18.0:
        ts = t - 14.0
        ep = ease_out(P(ts, 0.2, 1.0))
        p.append(xsec(epoxy=ep))
        if 1.1 < ts < 1.9:
            pu = P(ts, 1.1, 0.8)
            for gx0, gx1 in GROUTS:
                p.append(star((gx0+gx1)/2, Y_TOP-26, 0.5+1.3*pu, 1-pu))
        p.append(bounce_drop(t, 15.5, 778, Y_TOP-10, [(-110, 150), (95, 130)], scale=1.9))
        p.append(bounce_drop(t, 16.3, 406, Y_TOP-10, [(-100, 140), (115, 155)], scale=1.9))
        p.append(fade_txt(t, 14.5, 540, 360, 66, "เปลี่ยนแค่ร่องยาแนว"))
        p.append(fade_txt(t, 15.1, 540, 470, 78, "ไม่ต้องรื้อกระเบื้อง!", fill=GOLD_HL))
        p.append(fade_txt(t, 16.0, 540, 1300, 46, "ยาแนวกันซึม Epoxy — เนื้อทึบ น้ำไม่ผ่าน", fill="#3D566E", w="500"))

    # ================= ฉาก 5 (18-22) การ์ดปิดซีรีส์ =================
    else:
        ts = t - 18.0
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
                     + txt(540, 1119, 50, "หยดหยดสอน EP.1", fill="#5C3A00") + '</g>')
        pU = P(ts, 1.0, 0.45)
        if pU > 0:
            e = ease_out(pU)
            pulse = 0.5 + 0.5*math.sin((ts-1.5)*2*math.pi/1.4) if ts > 1.5 else 0
            glow = 0.0 + 0.35*pulse
            p.append(f'<g opacity="{e:.2f}" transform="translate(0,{14*(1-e):.0f})">'
                     f'<rect x="160" y="1220" width="760" height="138" rx="69" fill="#FFC53D" opacity="{glow:.2f}"/>'
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
