#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""สร้างเฟรมคลิปโปรโมทเกม /finder — 1080x1920, 30fps, 15s = 450 เฟรม"""
import math, os, random, sys

W, H, FPS, DUR = 1080, 1920, 30, 15.0
N = int(FPS * DUR)
OUT = "/home/claude/frames"
os.makedirs(OUT, exist_ok=True)

# ---------- easing ----------
def clamp01(x): return max(0.0, min(1.0, x))
def P(t, t0, d): return clamp01((t - t0) / d)          # progress 0..1
def ease_out(t): return 1 - (1 - t) ** 3
def ease_in(t):  return t ** 3
def ease_io(t):  return t * t * (3 - 2 * t)
def ease_back(t):
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

# ---------- bubbles (deterministic) ----------
random.seed(7)
BUBS = [dict(x=random.uniform(40, W-40), s=random.uniform(9, 26),
             dur=random.uniform(7, 15), dly=random.uniform(0, 12)) for _ in range(12)]
def bubbles(t, tint="143,216,255"):
    out = []
    for b in BUBS:
        ph = ((t - b["dly"]) % b["dur"]) / b["dur"]
        if t < b["dly"] - 0.001: ph = ((t - b["dly"] + 60*b["dur"]) % b["dur"]) / b["dur"]
        y = H + 40 - ph * (H + 160)
        op = 0.55 * (1 if ph > 0.1 else ph / 0.1) * (1 - ph*0.55)
        out.append(f'<circle cx="{b["x"]+ph*30:.1f}" cy="{y:.1f}" r="{b["s"]:.1f}" '
                   f'fill="rgba({tint},.05)" stroke="rgba({tint},{op*0.6:.2f})" stroke-width="2.5"/>')
    return "".join(out)

# ---------- mascot ----------
def mascot(x, y, scale, arm_rot=0.0, hat_dy=None, hat_op=1.0, star=None, breathe=0.0):
    """วาดหยดหยดที่ (x,y)=มุมซ้ายบนของ viewBox 100x110 คูณ scale"""
    hat_dy = 0 if hat_dy is None else hat_dy
    sy = 1 - breathe; sx = 1 + breathe
    star_svg = ""
    if star:
        s, op = star
        star_svg = (f'<g transform="translate(76,24) scale({s:.2f}) rotate({40*s:.0f})" opacity="{op:.2f}">'
                    f'<path d="M0 0 l3 6 6 1 -4.5 4.5 1 6.5 -5.5 -3 -5.5 3 1 -6.5 -4.5 -4.5 6 -1z" '
                    f'transform="translate(-3,-10)" fill="#FFDE6B"/></g>')
    return f'''<g transform="translate({x:.1f},{y:.1f}) scale({scale:.3f})">
  <g transform="translate(50,100) scale({sx:.3f},{sy:.3f}) translate(-50,-100)">
    <path d="M50 14 q30 34 30 55 a30 30 0 1 1 -60 0 q0 -21 30 -55z" fill="#2FA8E8" stroke="#0E6FA8" stroke-width="3"/>
    <path d="M36 52 q-6 14 2 26" stroke="#8FD8FF" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"/>
    <circle cx="41" cy="56" r="4" fill="#071B33"/><circle cx="61" cy="56" r="4" fill="#071B33"/>
    <circle cx="42.5" cy="54.5" r="1.4" fill="#fff"/><circle cx="62.5" cy="54.5" r="1.4" fill="#fff"/>
    <path d="M43 68 q8 8 16 0" stroke="#071B33" stroke-width="3" fill="none" stroke-linecap="round"/>
    <ellipse cx="33" cy="64" rx="4.5" ry="3" fill="#FF9DB0" opacity=".55"/>
    <ellipse cx="69" cy="64" rx="4.5" ry="3" fill="#FF9DB0" opacity=".55"/>
    <g transform="rotate({arm_rot:.1f},78,62)">
      <path d="M78 62 q13 -7 15 -18" stroke="#0E6FA8" stroke-width="6" fill="none" stroke-linecap="round"/>
      <circle cx="94" cy="42" r="6" fill="#2FA8E8" stroke="#0E6FA8" stroke-width="2.5"/>
    </g>
    <g transform="translate(0,{hat_dy:.1f})" opacity="{hat_op:.2f}">
      <path d="M28 34 a22 16 0 0 1 44 0 z" fill="#FFC53D" stroke="#C98F00" stroke-width="2.5"/>
      <rect x="24" y="32" width="52" height="7" rx="3.5" fill="#FFC53D" stroke="#C98F00" stroke-width="2.5"/>
      <rect x="46" y="18" width="8" height="14" rx="3" fill="#FFD86B"/>
    </g>
    {star_svg}
  </g>
</g>'''

def droplet(x, y, s, op=1.0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) scale({s:.3f})" opacity="{op:.2f}">'
            f'<path d="M0 -22 q13 17 13 26 a13 13 0 1 1 -26 0 q0 -9 13 -26z" '
            f'fill="#45C6F0" stroke="#8FD8FF" stroke-width="2"/></g>')

# ---------- house (ฉาก B) ----------
HOTSPOTS = [(200,80,20,0.0),(124,160,20,0.3),(290,212,18,0.6),(352,322,18,0.9),(62,352,18,1.2)]
def house(t_scene):
    hs = []
    for cx, cy, r, dly in HOTSPOTS:
        bobd = -6 * abs(math.sin((t_scene - dly) * math.pi / 0.8))
        ph = ((t_scene - dly) % 1.8) / 1.8
        ring_s = 0.4 + 1.4 * ph
        ring_op = 0.8 * (1 - ph)
        tipy = cy - 22
        hs.append(f'''<g>
  <circle cx="{cx}" cy="{cy}" r="{r*ring_s:.1f}" fill="none" stroke="#0E7CC4" stroke-width="2" opacity="{ring_op:.2f}"/>
  <g transform="translate(0,{bobd:.1f})">
    <path d="M{cx} {tipy} q12 15 12 23 a12 12 0 1 1 -24 0 q0 -8 12 -23z" fill="#1E9BE0" stroke="#fff" stroke-width="2.5"/>
    <text x="{cx}" y="{cy+8}" text-anchor="middle" font-size="11" fill="#fff" font-family="Mitr" font-weight="700">!</text>
  </g>
</g>''')
    return f'''<g transform="translate(20,340) scale(2.6)">
<circle cx="52" cy="46" r="22" fill="#FFDE6B"/><circle cx="52" cy="46" r="28" fill="#FFDE6B" opacity=".3"/>
<g fill="#fff" opacity=".9"><ellipse cx="300" cy="40" rx="34" ry="13"/><ellipse cx="326" cy="34" rx="24" ry="11"/><ellipse cx="130" cy="26" rx="26" ry="10"/></g>
<rect x="-10" y="330" width="420" height="110" fill="#A8D8A0"/>
<ellipse cx="60" cy="332" rx="46" ry="8" fill="#93C98B"/>
<rect x="78" y="96" width="184" height="16" rx="4" fill="#B9C6D2"/>
<rect x="74" y="88" width="10" height="24" rx="3" fill="#8FA3B5"/><rect x="256" y="88" width="10" height="24" rx="3" fill="#8FA3B5"/>
<rect x="78" y="86" width="184" height="5" rx="2.5" fill="#8FA3B5"/>
<line x1="100" y1="88" x2="100" y2="98" stroke="#8FA3B5" stroke-width="4"/><line x1="135" y1="88" x2="135" y2="98" stroke="#8FA3B5" stroke-width="4"/><line x1="170" y1="88" x2="170" y2="98" stroke="#8FA3B5" stroke-width="4"/><line x1="205" y1="88" x2="205" y2="98" stroke="#8FA3B5" stroke-width="4"/><line x1="240" y1="88" x2="240" y2="98" stroke="#8FA3B5" stroke-width="4"/>
<ellipse cx="200" cy="104" rx="30" ry="5" fill="#5FB7E8" opacity=".85"/>
<circle cx="196" cy="122" r="3" fill="#5FB7E8"/><circle cx="206" cy="130" r="2.4" fill="#5FB7E8"/>
<rect x="78" y="112" width="184" height="100" fill="#FFF6E8" stroke="#D9C6A8" stroke-width="3"/>
<rect x="81" y="115" width="86" height="94" fill="#E4F4FB"/>
<g stroke="#BFE2F2" stroke-width="1.6"><line x1="81" y1="140" x2="167" y2="140"/><line x1="81" y1="165" x2="167" y2="165"/><line x1="81" y1="190" x2="167" y2="190"/><line x1="105" y1="115" x2="105" y2="209"/><line x1="130" y1="115" x2="130" y2="209"/><line x1="155" y1="115" x2="155" y2="209"/></g>
<path d="M92 122 v12 h14" stroke="#7C93A8" stroke-width="4" fill="none" stroke-linecap="round"/>
<g fill="#5FB7E8"><circle cx="102" cy="142" r="2"/><circle cx="108" cy="150" r="2"/><circle cx="104" cy="158" r="2"/></g>
<rect x="120" y="186" width="42" height="18" rx="8" fill="#fff" stroke="#B9C6D2" stroke-width="2.5"/>
<rect x="190" y="176" width="52" height="33" rx="4" fill="#C89B6C"/><rect x="194" y="168" width="20" height="14" rx="4" fill="#EAD7BC"/>
<circle cx="228" cy="140" r="12" fill="#FFDE6B" opacity=".8"/>
<rect x="78" y="212" width="184" height="118" fill="#FFF9F0" stroke="#D9C6A8" stroke-width="3"/>
<rect x="96" y="288" width="64" height="24" rx="9" fill="#E86F1F"/><rect x="92" y="278" width="14" height="34" rx="6" fill="#D45F12"/><rect x="150" y="278" width="14" height="34" rx="6" fill="#D45F12"/>
<rect x="196" y="268" width="46" height="28" rx="3" fill="#22384E"/><rect x="214" y="296" width="10" height="10" fill="#8FA3B5"/>
<rect x="238" y="288" width="20" height="42" rx="3" fill="#B07B45"/>
<rect x="262" y="112" width="14" height="218" fill="#E8DCC8"/>
<path d="M269 190 l-4 14 l6 10 l-5 13 l4 12" stroke="#8A7455" stroke-width="2.8" fill="none" stroke-linecap="round"/>
<ellipse cx="338" cy="352" rx="52" ry="24" fill="#7A8B6E"/><ellipse cx="338" cy="348" rx="44" ry="19" fill="#4FA8DC"/>
<g fill="#FF8A3D"><ellipse cx="330" cy="352" rx="9" ry="4.5"/><path d="M338 352 l8 -5 v10 z"/></g>
<rect x="28" y="292" width="12" height="42" rx="5" fill="#8A5A32"/><circle cx="34" cy="272" r="30" fill="#6FBF63"/><circle cx="16" cy="288" r="20" fill="#7ECB71"/><circle cx="54" cy="288" r="20" fill="#7ECB71"/>
<rect x="10" y="366" width="116" height="56" rx="16" fill="#93B7CC"/><rect x="17" y="373" width="102" height="42" rx="11" fill="#4FA8DC"/>
<path d="M26 384 q8 -4 16 0 t16 0 t16 0 t16 0 t16 0" stroke="#8FD0F0" stroke-width="3" fill="none" opacity=".85"/>
{''.join(hs)}
</g>'''

# ---------- typing ----------
MSG1 = 'สวัสดีครับ! ผม "หยดหยด"'
MSG2 = 'บ้านรั่ว... แต่ไม่รู้ใช้ตัวไหน?'
def typed(msg, t, t0, cps=32):
    n = int(max(0, (t - t0)) * 1000 / cps)
    return msg[:n]

def esc(s): return s.replace("&","&amp;").replace("<","&lt;")

# ---------- frame ----------
def frame(t):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    parts.append('''<defs>
<radialGradient id="deep" cx="50%" cy="115%" r="110%">
  <stop offset="0%" stop-color="#0E3557"/><stop offset="65%" stop-color="#071B33"/>
</radialGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#8ED8F8"/><stop offset="58%" stop-color="#DFF4FE"/>
  <stop offset="58.2%" stop-color="#CBE9C9"/><stop offset="100%" stop-color="#B9DFB6"/>
</linearGradient>
<linearGradient id="cta" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#FF8A3D"/><stop offset="100%" stop-color="#E86F1F"/>
</linearGradient>
<filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
  <feGaussianBlur stdDeviation="18"/>
</filter>
</defs>''')

    if t < 8.8:
        # ================= SCENE A =================
        parts.append(f'<rect width="{W}" height="{H}" fill="url(#deep)"/>')
        parts.append(bubbles(t))
        # falling drop
        pF = P(t, 0.4, 0.9)
        if 0 < pF < 1 or (pF >= 1 and t < 1.55):
            y = -60 + ease_in(pF) * (620 + 60)
            op = 1.0 if t < 1.30 else 1 - P(t, 1.30, 0.25)
            if op > 0: parts.append(droplet(540, min(y, 620), 1.55, op))
        # splash rings + sparks
        for dly, col in ((1.30, "#45C6F0"), (1.42, "#8FD8FF")):
            pR = P(t, dly, 0.55)
            if 0 < pR < 1:
                parts.append(f'<ellipse cx="540" cy="640" rx="{14+pR*150:.0f}" ry="{6+pR*60:.0f}" '
                             f'fill="none" stroke="{col}" stroke-width="6" opacity="{0.9*(1-pR):.2f}"/>')
        for sx, sy_ in ((-110,-80),(100,-95),(-42,-125),(58,-52)):
            pS = P(t, 1.30, 0.6)
            if 0 < pS < 1:
                e = ease_out(pS)
                parts.append(droplet(540+sx*e, 640+sy_*e, 0.7*(1-0.6*pS), 1-pS))
        # mascot pop  (กลาง x=540, กว้าง 440)
        pM = P(t, 1.40, 0.55)
        if pM > 0:
            sc = ease_back(pM)
            br = 0.03 * math.sin((t-2.8)*2*math.pi/3) if t > 2.8 else 0.0
            hat_p = P(t, 2.10, 0.35)
            hat_dy = -110*(1-ease_in(hat_p)) if hat_p < 1 else (4*(1-P(t,2.38,0.07)) if t<2.45 else 0)
            hat_op = 0.0 if t < 2.10 else 1.0
            star = None
            pStar = P(t, 2.45, 0.5)
            if 0 < pStar < 1: star = (0.3+1.4*pStar, 1-pStar)
            arm = 0.0
            pW = P(t, 2.6, 1.4)
            if 0 < pW < 1: arm = -24 * abs(math.sin(pW * 2 * math.pi))
            mw = 440 * sc
            parts.append(mascot(540 - mw/2/ (440/100) * (440/100), 0, 0, 0))  # placeholder removed below
            parts.pop()
            s = 4.4 * sc
            parts.append(f'<g transform="translate({540-50*s:.1f},{440 + 40*(1-pM):.1f})">' +
                         mascot(0, 0, s, arm, hat_dy, hat_op, star, br) + '</g>')
        # presents + title
        pP2 = P(t, 2.80, 0.5)
        if pP2 > 0:
            e = ease_out(pP2)
            parts.append(f'<text x="540" y="{1080+14*(1-e):.0f}" text-anchor="middle" font-family="Mitr" '
                         f'font-weight="500" font-size="34" letter-spacing="6" fill="#8FD8FF" opacity="{e:.2f}">'
                         f'LUCERNAPRO นำเสนอ</text>')
        pT = P(t, 3.05, 0.45)
        if pT > 0:
            e = ease_back(pT); op = min(1, pT*2)
            parts.append(f'<g transform="translate(540,1220) scale({1.4-0.4*e:.3f})" opacity="{op:.2f}">'
                         f'<text x="0" y="0" text-anchor="middle" font-family="Mitr" font-weight="600" font-size="100" fill="#fff">ภารกิจตามหา</text>'
                         f'<text x="0" y="128" text-anchor="middle" font-family="Mitr" font-weight="600" font-size="100" fill="#FFC53D">อาวุธลับ</text></g>')
        # dialogue
        pD = P(t, 3.60, 0.30)
        if pD > 0:
            e = ease_out(pD)
            gy = 14*(1-e)
            msg = typed(MSG1, t, 3.62) if t < 6.30 else typed(MSG2, t, 6.32)
            hint_op = 0.3 + 0.7*abs(math.sin(t*math.pi))
            parts.append(f'''<g transform="translate(0,{gy:.1f})" opacity="{e:.2f}">
<rect x="70" y="1490" width="940" height="240" rx="40" fill="#12365C" stroke="#45C6F0" stroke-width="7"/>
<rect x="105" y="1458" width="250" height="62" rx="31" fill="#FFC53D" stroke="#fff" stroke-width="4"/>
{droplet(145, 1495, 0.85)}
<text x="175" y="1500" font-family="Mitr" font-weight="600" font-size="32" fill="#5C3A00">หยดหยด</text>
<text x="115" y="1610" font-family="Mitr" font-weight="500" font-size="52" fill="#EAF6FF">{esc(msg)}</text>
<text x="965" y="1706" font-family="Mitr" font-size="32" fill="#45C6F0" opacity="{hint_op:.2f}">▼</text>
</g>''')

    elif t < 12.3:
        # ================= SCENE B =================
        ts = t - 8.8
        parts.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
        pH = P(ts, 0.15, 0.4)
        if pH > 0:
            e = ease_out(pH)
            parts.append(f'<text x="540" y="{230+14*(1-e):.0f}" text-anchor="middle" font-family="Mitr" '
                         f'font-weight="600" font-size="76" fill="#0B2239" opacity="{e:.2f}">บ้านคุณรั่วตรงไหน?</text>')
        parts.append(house(ts))
        # tap indicator: ลอยเข้ามาจิ้มดาดฟ้า (จุดดาดฟ้าจริง = 20+200*2.6=540, 340+80*2.6=548)
        tx, ty = 540, 548
        pTap = P(ts, 0.8, 1.0)
        if 0 < pTap <= 1:
            e = ease_io(pTap)
            x = 820 + (tx-820)*e; y = 1240 + (ty-1240)*e
            parts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="rgba(255,255,255,.55)" '
                         f'stroke="#fff" stroke-width="5" opacity="{min(1,pTap*3):.2f}"/>')
        pPress = P(ts, 1.8, 0.22)
        if 0 < pPress < 1:
            r = 46 - 14*math.sin(pPress*math.pi)
            parts.append(f'<circle cx="{tx}" cy="{ty}" r="{r:.0f}" fill="rgba(255,255,255,.65)" stroke="#fff" stroke-width="5"/>')
        pRing = P(ts, 2.0, 0.55)
        if 0 < pRing < 1:
            parts.append(f'<circle cx="{tx}" cy="{ty}" r="{20+pRing*120:.0f}" fill="none" stroke="#fff" '
                         f'stroke-width="8" opacity="{1-pRing:.2f}"/>')
            for sx, sy_ in ((-90,-70),(84,-84),(-30,-110)):
                e = ease_out(pRing)
                parts.append(droplet(tx+sx*e, ty+sy_*e, 0.8*(1-0.5*pRing), 1-pRing))
        if 2.0 < ts < 3.5 and int(ts*6) % 2 == 0:
            pass  # จังหวะพัก
        # ค้าง indicator เบาๆ หลังจิ้ม
        if 2.22 <= ts < 3.2:
            parts.append(f'<circle cx="{tx}" cy="{ty}" r="46" fill="rgba(255,255,255,.35)" stroke="#fff" stroke-width="4" opacity="{1-P(ts,2.7,0.5):.2f}"/>')

    else:
        # ================= SCENE C =================
        ts = t - 12.3
        parts.append(f'<rect width="{W}" height="{H}" fill="url(#deep)"/>')
        parts.append(bubbles(t))
        pM = P(ts, 0.15, 0.45)
        if pM > 0:
            e = ease_out(pM)
            arm = 0.0
            pW = P(ts, 0.7, 2.0)
            if 0 < pW < 1: arm = -24*abs(math.sin(pW*3*math.pi))
            parts.append(f'<g transform="translate(0,{14*(1-e):.1f})" opacity="{e:.2f}">'
                         + mascot(540-50*3.1, 480, 3.1, arm) + '</g>')
        def fadeline(t0, y, svg_text):
            p = P(ts, t0, 0.45)
            if p <= 0: return
            e = ease_out(p)
            parts.append(f'<g transform="translate(0,{14*(1-e):.1f})" opacity="{e:.2f}">{svg_text}</g>')
        fadeline(0.5, 0, f'<text x="540" y="960" text-anchor="middle" font-family="Mitr" font-weight="600" font-size="44" letter-spacing="4" fill="#EAF6FF">LUCERNAPRO</text>')
        fadeline(0.8, 0, f'<text x="540" y="1080" text-anchor="middle" font-family="Mitr" font-weight="600" font-size="82" fill="#fff">หาตัวที่ใช่ให้บ้านคุณ</text>'
                          f'<text x="540" y="1195" text-anchor="middle" font-family="Mitr" font-weight="600" font-size="82" fill="#FFC53D">จบใน 20 วินาที</text>')
        pU = P(ts, 1.15, 0.45)
        if pU > 0:
            e = ease_out(pU)
            pulse = 0.5 + 0.5*math.sin((ts-1.7)*2*math.pi/1.4) if ts > 1.7 else 0
            parts.append(f'<g transform="translate(0,{14*(1-e):.1f})" opacity="{e:.2f}">'
                         f'<rect x="150" y="1290" width="780" height="130" rx="65" fill="#FFC53D" filter="url(#glow)" opacity="{0.25+0.3*pulse:.2f}"/>'
                         f'<rect x="160" y="1300" width="760" height="112" rx="56" fill="url(#cta)" stroke="#fff" stroke-width="5"/>'
                         f'<text x="540" y="1374" text-anchor="middle" font-family="Mitr" font-weight="600" font-size="56" fill="#fff">lucernapro.com/finder</text></g>')
        fadeline(1.5, 0, f'<text x="540" y="1530" text-anchor="middle" font-family="Mitr" font-weight="500" font-size="38" fill="#9FC6DD">เล่นฟรี · ไม่ต้องรู้จักเคมีสักตัว</text>')

    parts.append('</svg>')
    return "".join(parts)

# ---------- main ----------
if __name__ == "__main__":
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    b = int(sys.argv[2]) if len(sys.argv) > 2 else N
    for i in range(a, b):
        t = i / FPS
        with open(f"{OUT}/f_{i:04d}.svg", "w") as f:
            f.write(frame(t))
    print(f"frames {a}..{b-1} written")
