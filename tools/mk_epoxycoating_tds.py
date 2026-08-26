# -*- coding: utf-8 -*-
"""Epoxy / PU Floor Coating TDS — house style, 1 page. Issue 1.1 (Aug 2026):
epoxy-grade values aligned to manufacturer spec (drying/recoat/service times,
film properties, 4 kg small set, moisture & dew-point limits).
Site doctrine: no raw material codes/ingredients published."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
import os

W, H = A4
L, R = 45.4, 549.9
CW = R - L
ORANGE = (0.847059, 0.341176, 0.109804)
BAR    = (0.937255, 0.937255, 0.925490)
RULE   = (0.862745, 0.862745, 0.839216)
BODY, LEAD = 7.2, 9.4
LABEL_W = 118.0

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


def header():
    c.setFont('Helvetica-Bold', 15); c.setFillGray(0)
    c.drawString(L, base(46.5, 15), 'LUCERNAPRO')
    c.setFont('Helvetica-Bold', 12)
    c.drawRightString(R, base(46.0, 12), 'Epoxy / PU Floor Coating')
    c.setFont('Helvetica', 7.6)
    c.drawString(L, base(56.0, 7.6), 'TECHNICAL DATA SHEET  \u00b7  Issue 1.1  \u00b7  August 2026')
    c.drawRightString(R, base(56.0, 7.6),
                      'Roller-applied and self-levelling 2K floor coatings for concrete')
    c.setStrokeColorRGB(*ORANGE); c.setLineWidth(1.6)
    c.line(L, H - 63.0, R, H - 63.0)


def footer():
    c.setFont('Helvetica-Oblique', 6.4); c.setFillGray(0.25)
    foot = ('Given in good faith on the basis of our current knowledge and applying to the product as supplied. '
            'Site conditions, substrate condition and workmanship are outside our control and no warranty of result '
            'is given or implied; users should satisfy themselves that the product suits the intended use, by trial '
            'on site if necessary.')
    for i, ln in enumerate(wrap(foot, 'Helvetica-Oblique', 6.4, CW)):
        c.drawString(L, base(786.0 + i * 7.8, 6.4), ln)
    c.setFont('Helvetica', 7.2); c.setFillGray(0)
    c.drawString(L, base(806.0, 7.2), 'Lucerna Co., Ltd. \u00b7 23 Suriyat Road Soi 4, Nai Mueang, Mueang, Ubon Ratchathani 34000, Thailand')
    c.drawString(L, base(815.0, 7.2), 'Tel 097-079-9547, 097-079-6583 \u00b7 Office 062-005-7933 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com/epoxycoating')


header()
y = 67.0


def section(title, gap=3.0):
    global y
    y += gap
    c.setFillColorRGB(*BAR)
    c.rect(L, H - (y + 11.5), CW, 11.5, stroke=0, fill=1)
    c.setFillGray(0); c.setFont('Helvetica-Bold', 8.2)
    c.drawString(L + 4.0, base(y + 10.0, 8.2), title)
    y += 11.5


def para(text, gap=6.4, indent=2.0, width=None):
    global y
    y += gap
    c.setFillGray(0)
    w = (width or CW) - indent
    lines = wrap(text, 'Helvetica', BODY, w)
    for i, ln in enumerate(lines):
        nsp = ln.count(' ')
        if i < len(lines) - 1 and nsp > 0:
            extra = (w - stringWidth(ln, 'Helvetica', BODY)) / nsp
            t = c.beginText(L + indent, base(y + BODY, BODY))
            t.setFont('Helvetica', BODY)
            t.setWordSpace(extra)
            t.textOut(ln)
            c.drawText(t)
        else:
            c.setFont('Helvetica', BODY)
            c.drawString(L + indent, base(y + BODY, BODY), ln)
        y += LEAD
    y -= LEAD
    y += BODY + 0.6


def kv(rows, gap=5.0):
    global y
    y += gap
    for label, value in rows:
        lines = wrap(value, 'Helvetica', BODY, CW - LABEL_W - 2.0)
        c.setFillGray(0); c.setFont('Helvetica', BODY)
        for j, lln in enumerate(wrap(label, 'Helvetica', BODY, LABEL_W - 6)):
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
    c.setFillGray(0); c.setFont('Helvetica', BODY)
    c.drawString(L + 3.0, base(y + BODY, BODY), '\u2022')
    lines = wrap(text, 'Helvetica', BODY, CW - 14.0)
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

print('final y =', y)
assert y < 778, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written', os.environ.get('LP_OUT', 'files/epoxycoating-tds.pdf'))
