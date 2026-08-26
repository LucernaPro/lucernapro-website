# -*- coding: utf-8 -*-
"""Epoxy / PU Floor Coating TDS — house style, 1 page. Issue 1.1 (Aug 2026):
epoxy-grade values aligned to manufacturer spec (drying/recoat/service times,
film properties, 4 kg small set, moisture & dew-point limits).
Site doctrine: no raw material codes/ingredients published."""
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/epoxycoating-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro Epoxy / PU Floor Coating — Technical Data Sheet')


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
    c.drawString(L, base(815.0, 7.2), 'Tel 097-079-9547, 097-079-6583 \u00b7 Office 062-005-7933 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com/epoxycoating')


EN_FOOT = ('Given in good faith on the basis of our current knowledge and applying to the product as supplied. '
           'Site conditions, substrate condition and workmanship are outside our control and no warranty of result '
           'is given or implied; users should satisfy themselves that the product suits the intended use, by trial '
           'on site if necessary.')
TH_FOOT = ('\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e19\u0e35\u0e49\u0e43\u0e2b\u0e49\u0e44\u0e27\u0e49\u0e42\u0e14\u0e22\u0e2a\u0e38\u0e08\u0e23\u0e34\u0e15\u0e15\u0e32\u0e21\u0e04\u0e27\u0e32\u0e21\u0e23\u0e39\u0e49\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e41\u0e25\u0e30\u0e43\u0e0a\u0e49\u0e01\u0e31\u0e1a\u0e1c\u0e25\u0e34\u0e15\u0e20\u0e31\u0e13\u0e11\u0e4c\u0e15\u0e32\u0e21\u0e2a\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e08\u0e31\u0e14\u0e2a\u0e48\u0e07 \u0e2a\u0e20\u0e32\u0e1e\u0e2b\u0e19\u0e49\u0e32\u0e07\u0e32\u0e19 \u0e2a\u0e20\u0e32\u0e1e\u0e1e\u0e37\u0e49\u0e19\u0e1c\u0e34\u0e27 \u0e41\u0e25\u0e30\u0e1d\u0e35\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19\u0e2d\u0e22\u0e39\u0e48\u0e19\u0e2d\u0e01\u0e40\u0e2b\u0e19\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e04\u0e27\u0e1a\u0e04\u0e38\u0e21\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e25\u0e31\u0e1e\u0e18\u0e4c\u0e44\u0e21\u0e48\u0e27\u0e48\u0e32\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e42\u0e14\u0e22\u0e19\u0e31\u0e22 \u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e04\u0e27\u0e23\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e08\u0e23\u0e34\u0e07 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e27\u0e48\u0e32\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e02\u0e2d\u0e07\u0e15\u0e19')

header('Epoxy / PU Floor Coating',
       'TECHNICAL DATA SHEET  \u00b7  Issue 1.1  \u00b7  August 2026  \u00b7  Page 1 of 2',
       'Roller-applied and self-levelling 2K floor coatings for concrete')
y = 67.0


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


# ---------- content ----------
section('PRODUCT DESCRIPTION', gap=4.0)
para('LucernaPro Epoxy / PU Floor Coating is a two-component solvent-borne protective coating for concrete and '
     'cement floors, manufactured so that gloss level, film build, colour and anti-slip additions can be '
     'specified per project. The EPOXY grade \u2014 a high molecular weight epoxy cured with a polyamide hardener '
     '\u2014 cures to a dense, hard, high-build film with the highest resistance to compression, abrasion and '
     'chemicals, suitable in both atmospheric and immersed service: the standard choice for warehouses, '
     'production areas, workshops and garages. The POLYURETHANE (PU) grade is more flexible and markedly more '
     'resistant to UV and temperature cycling, and is preferred for loading bays, door thresholds and areas '
     'exposed to sunlight or machine vibration. Both are applied in two coats. A self-levelling EPOXY grade at '
     '1.5\u20133 mm is available to order where a seamless mirror-flat floor is required.')

section('KEY DATA')
kv([
    ('Type',              'Two-component (2K) solvent-borne floor coating \u2014 epoxy (polyamide-cured) and '
                          'polyurethane (PU) grades'),
    ('Mixing ratio',      'Part A : Part B = 4 : 1 by weight, both grades. Weigh the components; do not estimate '
                          'by eye. Individual formulations may differ \u2014 the product label always governs.'),
    ('Pot life',          'Approx. 30\u201340 minutes at 25\u00b0C, shorter when hotter. Mix only what can be '
                          'applied in that time.'),
    ('Touch dry',         'Epoxy grade: 2 hours at 25\u00b0C \u2014 longer in cool or humid conditions'),
    ('Overcoating',       'Epoxy grade: from 5 hours once cured through \u2014 typically 4\u20138 hours depending '
                          'on temperature, humidity and airflow; overnight recoat is also fine. Apply the second '
                          'coat cross-wise to the first.'),
    ('Coats',             'Two \u2014 quoted coverage assumes both coats are applied'),
    ('Coverage',          '16 kg set \u2248 50 m\u00b2 over two coats (\u2248 100 m\u00b2 per set per single '
                          'coat; \u2248 5\u20137 m\u00b2 per kg per coat)'),
    ('Return to service', 'Walk-on (careful foot access) 5 hours \u00b7 light foot traffic 2 days \u00b7 vehicle '
                          'traffic, heavy loading and full chemical resistance 7 days'),
    ('Film properties',   'Epoxy grade, typical: specular gloss 60\u00b0 > 80 GU \u00b7 pencil hardness '
                          'HB\u20132H \u00b7 cross-cut adhesion 100/100 \u00b7 solids 65 \u00b1 5 % \u00b7 '
                          'specific gravity 1.35 \u00b1 0.15'),
    ('Application',       'Roller, brush or notched trowel; cut in edges and column bases by brush first'),
    ('Substrate',         'Concrete or cement screed, min. 28 days cured, sound, moisture content below 10 %, '
                          'free of rising moisture. Mechanically prepared by grinding, diamond cup wheel or shot '
                          'blasting, then vacuumed \u2014 sweeping is not enough.'),
    ('Priming',           'Prime dusty or highly absorbent substrates with LucernaPro Marine Guard before coating'),
    ('Finish',            'Epoxy: gloss. PU: gloss, satin or matt to order.'),
    ('Colour',            'Any RAL shade to order \u2014 quote the RAL reference with the order'),
    ('Anti-slip',         'Graded aggregate can be broadcast into the final coat. Reduces slipperiness; a wet '
                          'floor is not non-slip.'),
    ('Packaging',         '16 kg set \u2014 Part A 12.8 kg + Part B 3.2 kg \u00b7 4 kg small set to order \u2014 '
                          'Part A 3.2 kg + Part B 0.8 kg'),
    ('Self-levelling',    'Epoxy, 1.5\u20133 mm, notched trowel then de-aerated with a spiked roller. Made to '
                          'order; application guidance provided to purchasers on request.'),
    ('Tool cleaning',     'Thinner, immediately while still wet \u2014 cured material cannot be removed. Clean '
                          'mixing containers before reuse: cured particles from a previous batch cause defects.'),
    ('Storage',           '12 months in unopened containers, tightly closed, in a cool, dry, well-ventilated '
                          'shaded place below 37\u00b0C, away from heat and ignition. Keep out of reach of children.'),
])

section('NOTE ON VALUES')
para('Typical values for the standard formulations at 25\u00b0C, given as guidance and not as a specification. '
     'Drying and cure times shorten in hot weather and lengthen in cool or humid conditions, and coverage '
     'depends strongly on substrate porosity. Where the product label differs from this sheet, the label governs.')

section('APPLICATION NOTES')
bullet('Surface preparation is the majority of the work. Grind or blast away polished laitance, oil, old paint '
       'and all friable material, then vacuum thoroughly. Coatings applied over dust or a weak surface layer '
       'delaminate, usually within the first year.', gap=5.0)
bullet('Moisture limits. Do not apply to wet or green concrete, or over polymer-modified patches, above 5 % '
       'moisture; do not apply when air or substrate temperature is within 3\u00b0C of the dew point; protect '
       'the substrate from condensation from pipes or overhead leaks during application. Moisture trapped under '
       'the film is the classic cause of blistering and delamination.')
bullet('This is a coating, not a levelling product. The finished film follows the profile of the substrate: '
       'waviness, hollows and joints remain visible, and gloss can make them more obvious. Repair before '
       'coating \u2014 fill cracks and spalls (PatchPro / CreteRevive), level hollows (LevelPro) and allow '
       'repairs to cure first.')
bullet('Build thickness with mortar, not with resin. For several millimetres of build, trowel a '
       'resin-and-graded-quartz epoxy mortar first and finish thin on top \u2014 thick pours of neat resin '
       'generate exotherm, shrink and crack. A dry, sound, non-chemically-exposed slab can be levelled far more '
       'cheaply with a cementitious screed.')
bullet('Mix thoroughly to a single uniform colour, scraping the sides and base of the container. Incomplete '
       'mixing is the most common cause of patchy, soft or tacky areas.')
bullet('Do not thin to extend coverage. Small additions of thinner to adjust viscosity are acceptable; heavier '
       'thinning reduces film build and durability proportionally.')
bullet('The epoxy grade discolours and dulls under prolonged UV exposure and is intended for interior use. '
       'Specify the PU grade for areas exposed to sunlight.')

section('HEALTH AND SAFETY')
para('These products contain organic solvent: they are flammable and give off vapour during application and '
     'drying. Apply only with genuinely effective ventilation, use forced-air extraction in enclosed areas, and '
     'eliminate all sources of ignition, including smoking, from the work area and adjacent spaces \u2014 never '
     'work in a sealed room. Wear rubber gloves, safety glasses and an organic-vapour respirator. The hardener '
     'may cause skin sensitisation: avoid skin contact and wash off immediately with soap and water, never with '
     'thinner. Refer to the Safety Data Sheet for the grade supplied before use.')

print('EN page final y =', y)
assert y < 778, 'EN content overflows into footer: y=%s' % y
footer(EN_FOOT)
c.showPage()

# ================= PAGE 2 — THAI =================
FR, FB, FI = 'Sarabun', 'Sarabun-Bold', 'Sarabun-Italic'
BODY, LEAD = 7.9, 10.3
LABEL_W = 100.0
JUSTIFY = False

header('\u0e2a\u0e35\u0e17\u0e32\u0e1e\u0e37\u0e49\u0e19 Epoxy / PU',
       'TECHNICAL DATA SHEET \u00b7 Issue 1.1 \u00b7 \u0e2a\u0e34\u0e07\u0e2b\u0e32\u0e04\u0e21 2026 \u00b7 \u0e2b\u0e19\u0e49\u0e32 2 \u0e08\u0e32\u0e01 2',
       '\u0e2a\u0e35\u0e17\u0e32\u0e1e\u0e37\u0e49\u0e19\u0e2a\u0e2d\u0e07\u0e2a\u0e48\u0e27\u0e19\u0e1c\u0e2a\u0e21 (2K) \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e1e\u0e37\u0e49\u0e19\u0e04\u0e2d\u0e19\u0e01\u0e23\u0e35\u0e15 \u2014 \u0e41\u0e1a\u0e1a\u0e25\u0e39\u0e01\u0e01\u0e25\u0e34\u0e49\u0e07\u0e41\u0e25\u0e30 self-levelling')
y = 67.0

section('ข้อมูลผลิตภัณฑ์', gap=4.0)
para('สีทาพื้น Epoxy / PU ของ LucernaPro เป็นสีเคลือบปกป้องพื้นชนิดสองส่วนผสม (2K) สูตร solvent สำหรับพื้นคอนกรีตและพื้นปูน '
     'กำหนดระดับความเงา ความหนาฟิล์ม เฉดสี และการเติมสารกันลื่นได้ตามลักษณะงาน / เกรด EPOXY — อีพ็อกซีโมเลกุลสูง '
     'บ่มด้วยฮาร์ดเดนเนอร์ชนิด polyamide — แห้งตัวเป็นฟิล์มแน่น แข็ง และหนา ทนแรงกด การเสียดสี และสารเคมีได้สูงสุด '
     'ใช้ได้ทั้งสภาพแวดล้อมทั่วไปและงานแช่น้ำ เป็นตัวเลือกมาตรฐานของโกดัง พื้นที่ผลิต โรงงาน และโรงรถ / '
     'เกรด POLYURETHANE (PU) ยืดหยุ่นกว่า ทนแดดและการเปลี่ยนอุณหภูมิได้ดีกว่ามาก เหมาะกับลานโหลดของ ธรณีประตู '
     'และพื้นที่โดนแดดหรือแรงสั่นสะเทือนของเครื่องจักร / ทั้งสองเกรดทา 2 รอบ และมีเกรด self-levelling (Epoxy หนา 1.5–3 มม.) '
     'สั่งผลิตได้สำหรับงานที่ต้องการพื้นเรียบเนียนไร้รอยต่อ')

section('ข้อมูลสำคัญ')
kv([
    ('ชนิด',              'สีทาพื้นสองส่วนผสม (2K) สูตร solvent — เกรด Epoxy (บ่มด้วย polyamide) และเกรด PU'),
    ('อัตราส่วนผสม',       'Part A : Part B = 4 : 1 โดยน้ำหนัก ทั้งสองเกรด ต้องชั่งน้ำหนัก ห้ามกะด้วยตา — สูตรเฉพาะบางรุ่นอาจต่างไป '
                          'ให้ยึดฉลากข้างกระปุกเป็นหลักเสมอ'),
    ('Pot life',          'ประมาณ 30–40 นาที ที่ 25°C อากาศร้อนยิ่งสั้นลง — ผสมทีละเท่าที่ทาทันเท่านั้น'),
    ('แห้งสัมผัส',         'เกรด Epoxy: 2 ชั่วโมง ที่ 25°C — อากาศเย็นหรือชื้นใช้เวลานานขึ้น'),
    ('ทาทับรอบถัดไป',      'เกรด Epoxy: เร็วสุด 5 ชั่วโมงเมื่อฟิล์มเซ็ตตัวทั่วแล้ว — โดยทั่วไป 4–8 ชั่วโมง ตามอุณหภูมิ ความชื้น '
                          'และการระบายอากาศ ทิ้งข้ามคืนก็ได้ ทารอบสองในทิศตัดขวางกับรอบแรก'),
    ('จำนวนรอบ',          '2 รอบ — ตัวเลขพื้นที่ครอบคลุมคิดจากการทาครบสองรอบแล้ว'),
    ('พื้นที่ครอบคลุม',     'ชุด 16 กก. ≈ 50 ตร.ม. เมื่อทา 2 รอบ (≈ 100 ตร.ม. ต่อชุดต่อรอบเดียว หรือ ≈ 5–7 ตร.ม. ต่อ กก. ต่อรอบ)'),
    ('เปิดใช้งาน',         'เหยียบเข้าไปทำงานเบาๆ 5 ชั่วโมง · เปิดเดินใช้งานจริง 2 วัน · รถวิ่ง วางของหนัก '
                          'และทนสารเคมีเต็มที่ 7 วัน'),
    ('คุณสมบัติฟิล์ม',      'เกรด Epoxy (ค่าทั่วไป): ความเงา 60° > 80 GU · ความแข็งดินสอ HB–2H · การยึดเกาะ cross-cut 100/100 · '
                          'เนื้อสี 65 ± 5 % · ความถ่วงจำเพาะ 1.35 ± 0.15'),
    ('วิธีทา',             'ลูกกลิ้ง แปรง หรือเกรียงหยัก — เก็บขอบมุมและขาเสาด้วยแปรงก่อน แล้วค่อยกลิ้งพื้นใหญ่'),
    ('พื้นผิว',            'คอนกรีตหรือพื้นปูน บ่มครบอย่างน้อย 28 วัน แข็งแรง ความชื้นต่ำกว่า 10 % ไม่มีความชื้นดันขึ้นจากใต้พื้น '
                          'เตรียมผิวด้วยเครื่องเจียร ใบขัดเพชร หรือยิงทราย แล้วดูดฝุ่นให้สะอาด — กวาดอย่างเดียวไม่พอ'),
    ('รองพื้น',            'พื้นที่เป็นฝุ่นหรือดูดซึมจัด ให้รองพื้นด้วย LucernaPro Marine Guard ก่อนทาสีทาพื้น'),
    ('ผิวงาน',             'Epoxy: เงา / PU: เงา กึ่งเงา หรือด้าน สั่งได้'),
    ('เฉดสี',              'สั่งได้ทุกเบอร์ RAL — แจ้งรหัส RAL มาพร้อมออเดอร์'),
    ('กันลื่น',             'โรยเม็ดทรายคัดเบอร์ลงในรอบสุดท้ายได้ ช่วยลดความลื่น — แต่พื้นเปียกไม่มีทางกันลื่นได้สนิท'),
    ('ขนาดบรรจุ',          'ชุด 16 กก. — Part A 12.8 กก. + Part B 3.2 กก. · ชุดเล็ก 4 กก. สั่งได้ — Part A 3.2 กก. + Part B 0.8 กก.'),
    ('Self-levelling',    'Epoxy หนา 1.5–3 มม. ปาดด้วยเกรียงหยักแล้วไล่ฟองด้วยลูกกลิ้งหนาม — สั่งผลิต '
                          'พร้อมคำแนะนำการทำงานสำหรับผู้ซื้อ'),
    ('ล้างเครื่องมือ',       'ทินเนอร์ ล้างทันทีขณะยังไม่แห้ง — แข็งแล้วล้างไม่ออก / ล้างถังผสมให้สะอาดก่อนใช้ซ้ำ '
                          'เศษที่แข็งตัวจากรอบก่อนทำให้ฟิล์มเป็นตำหนิ'),
    ('การเก็บรักษา',        '12 เดือนในภาชนะที่ยังไม่เปิด ปิดฝาสนิท เก็บที่แห้ง เย็น อากาศถ่ายเท อุณหภูมิต่ำกว่า 37°C '
                          'ห่างความร้อนและประกายไฟ เก็บพ้นมือเด็ก'),
])

section('หมายเหตุเรื่องค่าตัวเลข')
para('ค่าทั่วไปของสูตรมาตรฐานที่ 25°C ให้ไว้เป็นแนวทาง ไม่ใช่ข้อกำหนดผูกพัน — อากาศร้อนแห้งเร็วขึ้น อากาศเย็นหรือชื้นช้าลง '
     'และพื้นที่ครอบคลุมขึ้นกับความพรุนของพื้นอย่างมาก หากฉลากผลิตภัณฑ์ระบุต่างจากเอกสารนี้ ให้ยึดฉลากเป็นหลัก')

section('ข้อควรรู้ในการใช้งาน')
bullet('การเตรียมผิวคืองานส่วนใหญ่ของทั้งระบบ — เจียรหรือยิงทรายเอาผิวปูนขัดมัน คราบน้ำมัน สีเก่า และส่วนที่หลุดร่อน '
       'ออกให้หมด แล้วดูดฝุ่นให้สะอาด ทาทับฝุ่นหรือผิวที่อ่อนแอ ฟิล์มจะหลุดล่อน มักภายในปีแรก', gap=5.0)
bullet('ขีดจำกัดความชื้น — ห้ามทาบนปูนเปียก ปูนที่ยังบ่มไม่ครบ หรือรอยซ่อมชนิด polymer-modified ที่ความชื้นเกิน 5 % / '
       'ห้ามทาเมื่ออุณหภูมิอากาศหรือพื้นห่างจากจุดน้ำค้าง (dew point) ไม่ถึง 3°C / ระวังหยดน้ำจากท่อหรือรอยรั่วเหนือหัว '
       'ระหว่างทำงาน — ความชื้นที่ถูกขังใต้ฟิล์มคือสาเหตุคลาสสิกของสีพองและหลุดล่อน')
bullet('นี่คือสีเคลือบ ไม่ใช่วัสดุปรับระดับ — ฟิล์มบางและวิ่งตามผิวเดิม รอยคลื่น หลุม และรอยต่อจะยังมองเห็น ผิวเงายิ่งเห็นชัด / '
       'ซ่อมก่อนทาเสมอ: รอยร้าวและหลุมบ่อ (PatchPro / CreteRevive) ปรับระดับ (LevelPro) และรอให้งานซ่อมเซ็ตตัวก่อน')
bullet('สร้างความหนาด้วยมอร์ตาร์ ไม่ใช่เรซินล้วน — ต้องการความหนาหลายมิลลิเมตร ให้ปาด epoxy mortar (เรซินผสมทรายควอตซ์ '
       'คัดเบอร์) ปรับระดับก่อน แล้วเคลือบบางทับ เทเรซินล้วนหนาๆ จะเกิดความร้อน หดตัว และแตก / พื้นที่แห้งดี ไม่โดนเคมี '
       'ใช้ปูนปรับระดับธรรมดาถูกกว่าหลายเท่าและเพียงพอ')
bullet('กวนให้เข้ากันจนเป็นเนื้อเดียวสีเดียวทั้งถัง ขูดข้างถังและก้นถังด้วย — กวนไม่ทั่วคือสาเหตุอันดับหนึ่งของพื้นด่าง '
       'นิ่ม หรือเหนียวเป็นจุดๆ')
bullet('ห้ามผสมทินเนอร์เพื่อยืดปริมาณสี — เจือได้เล็กน้อยเพื่อปรับความหนืดเท่านั้น เจือเยอะฟิล์มบางลงและอ่อนแอลงตรงๆ')
bullet('เกรด Epoxy โดนแดดนานจะเหลืองและด้าน ออกแบบสำหรับงานในร่ม — พื้นที่โดนแดดให้เลือกเกรด PU')

section('ความปลอดภัย')
para('ผลิตภัณฑ์นี้มีตัวทำละลายอินทรีย์ (solvent): ติดไฟได้ และมีไอระเหยระหว่างทาและระหว่างแห้งตัว ทำงานในที่อากาศถ่ายเทดีจริง '
     'เท่านั้น พื้นที่ปิดต้องใช้พัดลมดูดอากาศ และกำจัดแหล่งประกายไฟทั้งหมดรวมถึงการสูบบุหรี่ออกจากพื้นที่ทำงานและพื้นที่ติดกัน — '
     'ห้ามทำงานในห้องปิดตายเด็ดขาด / สวมถุงมือยาง แว่นตานิรภัย และหน้ากากกันไอสารอินทรีย์ (organic vapor) / '
     'ฮาร์ดเดนเนอร์อาจทำให้แพ้ทางผิวหนัง เลี่ยงการสัมผัส โดนแล้วล้างด้วยสบู่และน้ำทันที ห้ามใช้ทินเนอร์ล้างมือ / '
     'อ่านเอกสารข้อมูลความปลอดภัย (SDS) ของรุ่นที่ได้รับก่อนใช้งาน')

print('TH page final y =', y)
assert y < 778, 'TH content overflows into footer: y=%s' % y
footer(TH_FOOT, disc_size=6.8, disc_lead=8.4)
c.save()
print('written', os.environ.get('LP_OUT', 'files/epoxycoating-tds.pdf'))
