# -*- coding: utf-8 -*-
"""CorePrimer TDS — house style, EN page + TH page in one PDF. Issue 1.0
(Sep 2026): translated from the raw-material manufacturer's Chinese TDS for the
1K moisture-cure penetrating concrete primer; base resin never disclosed; values are the manufacturer's typical values. Site doctrine: no raw
material codes or supplier grade names published."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

_F = os.path.join(os.path.dirname(__file__), 'fonts')
pdfmetrics.registerFont(TTFont('Sarabun', os.path.join(_F, 'Sarabun-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Sarabun-Bold', os.path.join(_F, 'Sarabun-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Sarabun-Italic', os.path.join(_F, 'Sarabun-Italic.ttf')))

W, H = A4
L, R = 45.4, 549.9
CW = R - L
ORANGE = (0.847059, 0.341176, 0.109804)
BAR    = (0.937255, 0.937255, 0.925490)
RULE   = (0.862745, 0.862745, 0.839216)
BODY, LEAD = 7.2, 9.4
LABEL_W = 118.0
FR, FB, FI = 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique'
JUSTIFY = True

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/coreprimer-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro CorePrimer — Technical Data Sheet')


def base(bottom, size):
    return H - (bottom - 0.21 * size)


def wrap(text, font, size, width):
    out, line = [], ''
    for word in text.split(' '):
        t = (line + ' ' + word).strip()
        if stringWidth(t, font, size) <= width:
            line = t
        else:
            if line:
                out.append(line)
            line = word
    if line:
        out.append(line)
    return out


def header(title, issue_line, tagline):
    c.setFont('Helvetica-Bold', 15); c.setFillGray(0)
    c.drawString(L, base(46.5, 15), 'LUCERNAPRO')
    c.setFont(FB, 12)
    c.drawRightString(R, base(46.0, 12), title)
    c.setFont(FR, 7.6)
    c.drawString(L, base(56.0, 7.6), issue_line)
    c.drawRightString(R, base(56.0, 7.6), tagline)
    c.setStrokeColorRGB(*ORANGE); c.setLineWidth(1.6)
    c.line(L, H - 63.0, R, H - 63.0)


def footer(foot, disc_size=6.4, disc_lead=7.8):
    c.setFont(FI, disc_size); c.setFillGray(0.25)
    for i, ln in enumerate(wrap(foot, FI, disc_size, CW)):
        c.drawString(L, base(786.0 + i * disc_lead, disc_size), ln)
    c.setFont('Helvetica', 7.2); c.setFillGray(0)
    c.drawString(L, base(806.0, 7.2), 'Lucerna Co., Ltd. \u00b7 23 Suriyat Road Soi 4, Nai Mueang, Mueang, Ubon Ratchathani 34000, Thailand')
    c.drawString(L, base(815.0, 7.2), 'Tel 097-079-9547, 097-079-6583 \u00b7 Office 062-005-7933 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com/coreprimer')


EN_FOOT = ('Given in good faith on the basis of our current knowledge and applying to the product as supplied. '
           'Site conditions, substrate condition and workmanship are outside our control and no warranty of result '
           'is given or implied; users should satisfy themselves that the product suits the intended use, by trial '
           'on site if necessary.')
TH_FOOT = ('\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e19\u0e35\u0e49\u0e43\u0e2b\u0e49\u0e44\u0e27\u0e49\u0e42\u0e14\u0e22\u0e2a\u0e38\u0e08\u0e23\u0e34\u0e15\u0e15\u0e32\u0e21\u0e04\u0e27\u0e32\u0e21\u0e23\u0e39\u0e49\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e41\u0e25\u0e30\u0e43\u0e0a\u0e49\u0e01\u0e31\u0e1a\u0e1c\u0e25\u0e34\u0e15\u0e20\u0e31\u0e13\u0e11\u0e4c\u0e15\u0e32\u0e21\u0e2a\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e08\u0e31\u0e14\u0e2a\u0e48\u0e07 \u0e2a\u0e20\u0e32\u0e1e\u0e2b\u0e19\u0e49\u0e32\u0e07\u0e32\u0e19 \u0e2a\u0e20\u0e32\u0e1e\u0e1e\u0e37\u0e49\u0e19\u0e1c\u0e34\u0e27 \u0e41\u0e25\u0e30\u0e1d\u0e35\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19\u0e2d\u0e22\u0e39\u0e48\u0e19\u0e2d\u0e01\u0e40\u0e2b\u0e19\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e04\u0e27\u0e1a\u0e04\u0e38\u0e21\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e25\u0e31\u0e1e\u0e18\u0e4c\u0e44\u0e21\u0e48\u0e27\u0e48\u0e32\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e42\u0e14\u0e22\u0e19\u0e31\u0e22 \u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e04\u0e27\u0e23\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e08\u0e23\u0e34\u0e07 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e27\u0e48\u0e32\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e02\u0e2d\u0e07\u0e15\u0e19')



def section(title, gap=3.0):
    global y
    y += gap
    c.setFillColorRGB(*BAR)
    c.rect(L, H - (y + 11.5), CW, 11.5, stroke=0, fill=1)
    c.setFillGray(0); c.setFont(FB, 8.2)
    c.drawString(L + 4.0, base(y + 10.0, 8.2), title)
    y += 11.5


def para(text, gap=6.4, indent=2.0, width=None):
    global y
    y += gap
    c.setFillGray(0)
    w = (width or CW) - indent
    lines = wrap(text, FR, BODY, w)
    for i, ln in enumerate(lines):
        nsp = ln.count(' ')
        if JUSTIFY and i < len(lines) - 1 and nsp > 0:
            extra = (w - stringWidth(ln, FR, BODY)) / nsp
            t = c.beginText(L + indent, base(y + BODY, BODY))
            t.setFont(FR, BODY)
            t.setWordSpace(extra)
            t.textOut(ln)
            c.drawText(t)
        else:
            c.setFont(FR, BODY)
            c.drawString(L + indent, base(y + BODY, BODY), ln)
        y += LEAD
    y -= LEAD
    y += BODY + 0.6


def kv(rows, gap=5.0):
    global y
    y += gap
    for label, value in rows:
        lines = wrap(value, FR, BODY, CW - LABEL_W - 2.0)
        c.setFillGray(0); c.setFont(FR, BODY)
        for j, lln in enumerate(wrap(label, FR, BODY, LABEL_W - 6)):
            c.drawString(L + 2.0, base(y + BODY + j * LEAD, BODY), lln)
        for i, ln in enumerate(lines):
            c.drawString(L + LABEL_W, base(y + BODY + i * LEAD, BODY), ln)
        y += LEAD * len(lines) + 2.6
        c.setStrokeColorRGB(*RULE); c.setLineWidth(0.35)
        c.line(L, H - y, R, H - y)
        y += 1.4
    y += 1.0


def bullet(text, gap=3.4):
    global y
    y += gap
    c.setFillGray(0); c.setFont(FR, BODY)
    c.drawString(L + 3.0, base(y + BODY, BODY), '\u2022')
    lines = wrap(text, FR, BODY, CW - 14.0)
    for i, ln in enumerate(lines):
        c.drawString(L + 12.0, base(y + BODY + i * LEAD, BODY), ln)
    y += LEAD * (len(lines) - 1) + BODY



header('CorePrimer',
       'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  September 2026  \u00b7  Page 1 of 2',
       'Penetrating concrete primer for the PoolArmour system')
y = 67.0

section('PRODUCT DESCRIPTION', gap=4.0)
para('LucernaPro CorePrimer is a single-component, solvent-free, moisture-curing polymer-modified penetrating primer for concrete, '
     'cement render and other absorbent cementitious surfaces, developed as the primer coat of the PoolArmour pool '
     'coating system. The liquid soaks into the pores of the concrete and cures inside them, binding dusty, friable or '
     'highly absorbent render into a firm, consolidated base. Applied while the primer is still fresh, the first coat of '
     'PoolArmour bonds to it chemically rather than merely lying on top, so primer, render and coating cure into one '
     'system. It contains no solvent at all: everything applied stays in the substrate, with no evaporation, no shrinkage, '
     'no thinner smell and no fire risk. Supplied ready to use, with no second component, no mixing ratio and no pot life.')

section('KEY DATA')
kv([
    ('Type',              'Single-component (1K) moisture-curing polymer-modified penetrating primer, 100 % solvent-free, '
                          'supplied ready to use \u2014 do not dilute'),
    ('Appearance',        'Clear, low-viscosity liquid; dries to a thin, slightly glossy film on the surface once the '
                          'substrate is saturated'),
    ('Cure mechanism',    'Reacts with atmospheric and substrate moisture. Tolerates a damp surface; standing water or a '
                          'wet, shiny surface causes foaming and stops penetration.'),
    ('Cured binder',      'Tough, elastic polymer film \u2014 tensile strength about 33 MPa, elongation at break about 460 % '
                          '(free film of the binder resin)'),
    ('Substrates',        'Concrete, cement render, cementitious plaster and other porous mineral surfaces, cured at least '
                          '4 weeks. Not for glazed tile, polished stone or any non-absorbent surface \u2014 with nowhere to '
                          'soak in it gives no advantage there.'),
    ('Surface condition', 'Clean, free of algae, oil, pool chemicals and loose or flaking paint down to sound render; cracks '
                          'and holes repaired first (PatchPro). Damp is acceptable; no puddles. Do the water-drop test: a drop '
                          'must soak in within a minute \u2014 if it beads or sits on the surface, open the surface (acid '
                          'etch) before priming.'),
    ('Application',       'Brush or short-nap roller, one thin even coat, working the liquid into the render rather than '
                          'leaving a film on top. Where the render drinks it instantly and goes matt, re-wet that spot only.'),
    ('Consumption',       'About 1 kg per 10 m\u00b2 (5 kg \u2248 50 m\u00b2) in one coat on typical render. The primer works by '
                          'soaking in, so coverage falls on very porous render \u2014 budget with a margin.'),
    ('Coats',             'One. Do not build a thick film or leave pools: primer that cannot soak in becomes a weak layer '
                          'under the coating.'),
    ('Tack-free',         'About 5 minutes at site conditions, up to about 10 minutes \u2014 the surface turns from wet gloss '
                          'to matt and no longer sticks to a finger'),
    ('Recoat window',     'Apply the first coat of PoolArmour as soon as the primer is tack-free and still fresh (5\u201310 '
                          'minutes) for full chemical bonding. A primer left to dry hard can still be coated, but bond '
                          'strength is below peak; to recover it, sand the glossy film matt, dust off and re-prime thinly.'),
    ('Working method',    'Prime and coat zone by zone (a two-person crew: about 10\u201320 m\u00b2 per zone) so the first '
                          'coat always follows the primer within minutes. The second PoolArmour coat follows the coating\u2019s '
                          'own schedule, about 2\u20133 hours later.'),
    ('Cleaning',          'Brushes and rollers with thinner immediately after use \u2014 the primer hardens in the tools once '
                          'it takes up moisture'),
    ('Storage',           'Container tightly closed, cool, dry and shaded; moisture in the air is the curing agent, so an '
                          'opened can thickens and skins \u2014 use it up within the same job. Keep out of reach of children.'),
    ('Packaging',         '1 kg \u00b7 5 kg'),
])

section('NOTE ON VALUES')
para('Typical values, given as guidance and not as a specification. Tack-free and recoat times are measured on site in '
     'Thai conditions; coverage depends entirely on the porosity of the render. Where the product label differs from '
     'this sheet, the label governs. Full application steps, the water-drop test and the acid-etch procedure are on the '
     'product page.')

section('APPLICATION NOTES')
bullet('Prime every pool, not only the ones that look poor. A hand rubbed over the render tells you the surface is not '
       'dusty today; it tells you nothing about the mix, the water added or the curing of what was poured. The primer is '
       'the insurance for what the eye cannot see.', gap=5.0)
bullet('Sealed render will not take it. Trowel-polished render or render made with a heavy dose of integral '
       'waterproofer does not absorb; test with a drop of water first and acid-etch if it fails, then test again.')
bullet('Have the coating ready before opening the primer. The mistake that wastes the most material is priming the '
       'whole pool and then fetching the paint: the first coat must follow the primer while it is fresh.')
bullet('Thin and soaked in, not thick and glossy. One pass; top up only the spots that drink it instantly.')
bullet('Never on standing water. Damp is fine, wet is not \u2014 blot puddles and shiny-wet areas before priming.')
bullet('Fill the pool only after the coating has cured for its full stated time; the primer places no extra limit '
       'of its own.')

section('HEALTH AND SAFETY')
para('Solvent-free and non-flammable, so there is no thinner smell and no fire risk \u2014 but it is a reactive '
     'resin. Wear gloves and eye protection; avoid skin contact and wipe off any splash before it cures, '
     'then wash with soap and water. Work with normal ventilation. Keep the container closed and away from moisture, '
     'sunlight and heat. Refer to the Safety Data Sheet before use.')

print('EN page final y =', y)
assert y < 778, 'EN content overflows into footer: y=%s' % y
footer(EN_FOOT)
c.showPage()

# ================= PAGE 2 — THAI =================
FR, FB, FI = 'Sarabun', 'Sarabun-Bold', 'Sarabun-Italic'
BODY, LEAD = 7.9, 10.3
LABEL_W = 100.0
JUSTIFY = False

header('CorePrimer',
       'TECHNICAL DATA SHEET \u00b7 Issue 1.0 \u00b7 กันยายน 2026 \u00b7 หน้า 2 จาก 2',
       'รองพื้นซึมลึกส่วนผสมเดียว สำหรับคอนกรีตและปูนฉาบ ใต้ระบบ PoolArmour')
y = 67.0

section('ข้อมูลผลิตภัณฑ์', gap=4.0)
para('CorePrimer ของ LucernaPro เป็นรองพื้นซึมลึกสูตร polymer-modified ชนิดบ่มตัวด้วยความชื้น ส่วนผสมเดียว ไม่มีตัวทำละลาย สำหรับคอนกรีต ปูนฉาบ '
     'และผิวซีเมนต์ที่ดูดซึมได้ พัฒนาเป็นชั้นรองพื้นของระบบสีทาสระ PoolArmour / เนื้อน้ำยาซึมลงในรูพรุนของคอนกรีตแล้วบ่มตัวอยู่ในนั้น '
     'ประสานผิวปูนที่เป็นฝุ่น ร่วน หรือดูดน้ำจัดให้กลายเป็นฐานแข็งชิ้นเดียว / ทา PoolArmour รอบแรกทับตอนรองพื้นยังสด สองชั้นจะประสานกัน '
     'ด้วยปฏิกิริยาเคมี ไม่ใช่วางซ้อนกันเฉยๆ ปูน รองพื้น และสีจึงบ่มตัวเป็นระบบเดียว / ไม่มีตัวทำละลายเลย ทาลงไปเท่าไหร่ฝังอยู่ในปูนเท่านั้น '
     'ไม่ระเหย ไม่หด ไม่มีกลิ่นทินเนอร์ ไม่ติดไฟ / พร้อมทาจากกระป๋อง ไม่มี Part B ไม่มีอัตราผสม ไม่มี pot life')

section('ข้อมูลสำคัญ')
kv([
    ('ชนิด',              'รองพื้นซึมลึกสูตร polymer-modified บ่มตัวด้วยความชื้น ส่วนผสมเดียว (1K) ไม่มีตัวทำละลาย 100 % พร้อมใช้ — ห้ามเจือจาง'),
    ('ลักษณะ',            'ของเหลวใส ความหนืดต่ำ เมื่อปูนอิ่มตัวแล้วจะทิ้งฟิล์มบางกึ่งเงาไว้บนผิว'),
    ('กลไกบ่มตัว',         'ทำปฏิกิริยากับความชื้นในอากาศและในเนื้อปูน รับผิวชื้นหมาดได้ แต่น้ำขังหรือผิวเปียกเงาจะทำให้ฟิล์มเป็นฟองและซึมไม่ลง'),
    ('ฟิล์มหลังบ่มตัว',     'ฟิล์มพอลิเมอร์เหนียวและยืดหยุ่น — แรงดึงราว 33 MPa ยืดตัวได้ราว 460 % (ค่าฟิล์มอิสระของเรซินตัวประสาน)'),
    ('พื้นผิวที่ใช้ได้',      'คอนกรีต ปูนฉาบ ปูนซีเมนต์ และผิวแร่ที่มีรูพรุน บ่มตัวมาแล้วอย่างน้อย 4 สัปดาห์ / ไม่ใช้กับกระเบื้องเคลือบ หินขัดมัน '
                          'หรือผิวที่ไม่ดูดซึม — ไม่มีที่ให้ซึมจึงไม่ได้เปรียบอะไร'),
    ('สภาพผิวก่อนทา',      'สะอาด ไม่มีตะไคร่ คราบน้ำมัน คราบเคมีสระ และสีเก่าที่พองหรือลอก ขัดออกให้ถึงเนื้อปูน / ซ่อมรอยร้าวและหลุมให้จบก่อน (PatchPro) / '
                          'ชื้นหมาดได้ ห้ามมีน้ำขัง / ทดสอบหยดน้ำ: หยดต้องซึมหายภายใน 1 นาที ถ้าเป็นเม็ดหรือค้างบนผิว ต้องเปิดผิวด้วยกรดเกลือก่อนรองพื้น'),
    ('วิธีทา',             'แปรงหรือลูกกลิ้งขนสั้น ทาบางสม่ำเสมอรอบเดียว เน้นให้น้ำยาซึมลงเนื้อปูน ไม่ใช่ให้เงาอยู่บนผิว / ตรงไหนดูดเร็วจนด้านทันที เติมซ้ำเฉพาะจุดนั้น'),
    ('อัตราการใช้',         'ประมาณ 1 กก. ต่อ 10 ตร.ม. (5 กก. ≈ 50 ตร.ม.) รอบเดียว บนปูนสภาพทั่วไป / ตัวนี้ทำงานด้วยการซึม ปูนยิ่งพรุนยิ่งดูดมาก ตั้งงบเผื่อไว้'),
    ('จำนวนรอบ',          '1 รอบ — ห้ามทาหนาหรือปล่อยเป็นแอ่ง ส่วนที่ซึมไม่ลงคือชั้นอ่อนใต้สี'),
    ('แห้งสัมผัส',         'ราว 5 นาที ช้าสุดราว 10 นาที ที่หน้างาน — ผิวเปลี่ยนจากเปียกเงาเป็นหมาด แตะแล้วไม่ติดนิ้ว'),
    ('ช่วงทาทับ',          'ลง PoolArmour รอบแรกทันทีที่รองพื้นแตะไม่ติดนิ้วแต่ยังสด (5–10 นาที) จึงจะประสานเป็นเนื้อเดียวเต็มสเปค / '
                          'รองพื้นที่แห้งสนิทแล้วยังทาทับได้ แต่แรงยึดเกาะไม่ถึงจุดสูงสุด ถ้าต้องการเต็มสเปคให้ขัดฟิล์มเงาจนด้าน เช็ดฝุ่น แล้วรองพื้นบางๆ ใหม่'),
    ('วิธีทำงาน',          'รองพื้นและลงสีไล่ทีละโซน (ทีมสองคนราว 10–20 ตร.ม. ต่อโซน) ให้สีรอบแรกตามรองพื้นทันภายในไม่กี่นาที / '
                          'PoolArmour รอบสองทาตามระบบของสีเอง ราว 2–3 ชั่วโมงถัดมา'),
    ('ล้างเครื่องมือ',       'แปรงและลูกกลิ้งล้างด้วยทินเนอร์ทันทีหลังใช้ — น้ำยาจะแข็งคาเครื่องมือเมื่อโดนความชื้น'),
    ('การเก็บรักษา',        'ปิดฝาให้สนิท เก็บในที่ร่ม เย็น แห้ง ความชื้นในอากาศคือตัวเร่งบ่ม กระป๋องที่เปิดแล้วจะข้นและเป็นฝ้า ควรใช้ให้หมดภายในงานเดียว / เก็บพ้นมือเด็ก'),
    ('ขนาดบรรจุ',          '1 กก. · 5 กก.'),
])

section('หมายเหตุเรื่องค่าตัวเลข')
para('ค่าทั่วไป ให้ไว้เป็นแนวทาง ไม่ใช่ข้อกำหนดผูกพัน — เวลาแห้งสัมผัสและช่วงทาทับวัดจากหน้างานจริงในสภาพอากาศไทย ส่วนอัตราการใช้ขึ้นกับ '
     'ความพรุนของปูนล้วนๆ หากฉลากผลิตภัณฑ์ระบุต่างจากเอกสารนี้ ให้ยึดฉลากเป็นหลัก / ขั้นตอนใช้งานเต็ม การทดสอบหยดน้ำ และวิธีล้างกรด อยู่ที่หน้าสินค้า')

section('ข้อควรรู้ในการใช้งาน')
bullet('รองพื้นทุกสระ ไม่ใช่เฉพาะสระที่ดูไม่ดี — ลูบแล้วไม่มีผงติดมือบอกได้แค่ว่าผิวหน้าไม่ร่วนวันนี้ บอกไม่ได้ว่าปูนที่เทมาได้สเปคไหม ผสมน้ำเกินหรือเปล่า '
       'บ่มครบไหม รองพื้นคือประกันสำหรับสิ่งที่ตาเปล่ามองไม่เห็น', gap=5.0)
bullet('ปูนปิดหน้าไม่รับน้ำยา — ปูนขัดมัน หรือปูนผสมน้ำยากันซึมในเนื้อเยอะ จะไม่ดูดซึม ทดสอบหยดน้ำก่อนเสมอ ไม่ผ่านให้ล้างกรดแล้วทดสอบซ้ำ')
bullet('เตรียมสีให้พร้อมก่อนเปิดรองพื้น — ข้อผิดพลาดที่เสียของมากที่สุดคือรองพื้นทั้งสระแล้วค่อยไปหาสี สีรอบแรกต้องตามรองพื้นตอนยังสด')
bullet('บางและซึม ไม่ใช่หนาและเงา — ทารอบเดียว เติมซ้ำเฉพาะจุดที่ดูดจนด้านทันที')
bullet('ห้ามทาบนน้ำขัง — ชื้นได้ เปียกไม่ได้ ซับแอ่งน้ำและผิวเปียกเงาออกให้หมดก่อนรองพื้น')
bullet('เติมน้ำเมื่อสีบ่มตัวครบตามกำหนดของสีเท่านั้น — รองพื้นไม่ได้เพิ่มข้อจำกัดเวลาของตัวเอง')

section('ความปลอดภัย')
para('ไม่มีตัวทำละลายและไม่ติดไฟ จึงไม่มีกลิ่นทินเนอร์และไม่มีความเสี่ยงเรื่องไฟ — แต่เป็นเรซินที่ทำปฏิกิริยาได้ '
     'สวมถุงมือและแว่นตาป้องกันทุกครั้ง เลี่ยงไม่ให้โดนผิวหนัง โดนแล้วเช็ดออกก่อนบ่มตัวแล้วล้างด้วยสบู่และน้ำ ทำงานในที่อากาศถ่ายเทตามปกติ / '
     'ปิดฝาให้สนิท เก็บห่างความชื้น แสงแดด และความร้อน / อ่านเอกสารข้อมูลความปลอดภัย (SDS) ก่อนใช้งาน')

print('TH page final y =', y)
assert y < 778, 'TH content overflows into footer: y=%s' % y
footer(TH_FOOT, disc_size=6.8, disc_lead=8.4)
c.save()
print('written', os.environ.get('LP_OUT', 'files/coreprimer-tds.pdf'))
