# -*- coding: utf-8 -*-
"""PoolArmour TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page).
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
BODY, LEAD = 8.6, 12.2
LABEL_W = 156.7

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/poolarmour-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro PoolArmour — Technical Data Sheet')


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


TOTAL = 1


def header(page):
    c.setFont('Helvetica-Bold', 15); c.setFillGray(0)
    c.drawString(L, base(48.5, 15), 'LUCERNAPRO')
    c.setFont('Helvetica-Bold', 13)
    c.drawRightString(R, base(48.0, 13), 'PoolArmour')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'One-component Waterproof Swimming Pool Paint')
    c.setStrokeColorRGB(*ORANGE); c.setLineWidth(1.6)
    c.line(L, H - 66.2, R, H - 66.2)


def footer():
    c.setFont('Helvetica', 7.5); c.setFillGray(0)
    c.drawString(L, base(782.0, 7.5),
                 'Lucerna Co., Ltd. \u00b7 23 Suriyat Rd. Soi 4, Nai Mueang, Mueang, Ubon Ratchathani 34000, Thailand')
    c.drawString(L, base(791.0, 7.5),
                 'Tel 097-079-9547, 097-079-6583 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com')
    c.setFont('Helvetica-Oblique', 6.8); c.setFillGray(0.25)
    foot = ('The information herein is given in good faith based on our current knowledge and practical experience. '
            'Performance depends on substrate, surface preparation, film thickness and site conditions; '
            'values are typical guidance only and do not constitute a specification. Users must verify suitability '
            'for their intended application. Made in Thailand.')
    for i, ln in enumerate(wrap(foot, 'Helvetica-Oblique', 6.8, CW)):
        c.drawString(L, base(800.3 + i * 8.4, 6.8), ln)


header(1)
y = 70.9


def section(title):
    global y
    c.setFillColorRGB(*BAR)
    c.rect(L, H - (y + 13), CW, 13, stroke=0, fill=1)
    c.setFillGray(0); c.setFont('Helvetica-Bold', 9.0)
    c.drawString(L + 4.0, base(y + 11.3, 9.0), title)
    y += 13


def para(text, gap=14.2, indent=2.0):
    """Justified paragraph (มติ QA 18 ส.ค.: information paragraphs = justify) —
    กระจายช่องว่างด้วย word spacing ทุกบรรทัดยกเว้นบรรทัดสุดท้ายของย่อหน้า"""
    global y
    y += gap
    c.setFillGray(0)
    lines = wrap(text, 'Helvetica', BODY, CW - indent)
    for i, ln in enumerate(lines):
        nsp = ln.count(' ')
        if i < len(lines) - 1 and nsp > 0:
            extra = (CW - indent - stringWidth(ln, 'Helvetica', BODY)) / nsp
            t = c.beginText(L + indent, base(y + 8.6, BODY))
            t.setFont('Helvetica', BODY)
            t.setWordSpace(extra)
            t.textOut(ln)
            c.drawText(t)
        else:
            c.setFont('Helvetica', BODY)
            c.drawString(L + indent, base(y + 8.6, BODY), ln)
        y += LEAD
    y -= LEAD
    y += 8.6


def kv(rows, gap=12.0):
    global y
    y += gap
    for label, value in rows:
        lines = wrap(value, 'Helvetica', BODY, CW - LABEL_W - 2.0)
        c.setFillGray(0); c.setFont('Helvetica', BODY)
        c.drawString(L + 2.0, base(y + 8.6, BODY), label)
        for i, ln in enumerate(lines):
            c.drawString(L + LABEL_W, base(y + 8.6 + i * LEAD, BODY), ln)
        y += LEAD * len(lines) + 5.7
        c.setStrokeColorRGB(*RULE); c.setLineWidth(0.4)
        c.line(L, H - y, R, H - y)
    y += 3.0


# ---------- content ----------
section('PRODUCT DESCRIPTION')
para('PoolArmour is a one-component, water-based swimming pool paint with built-in waterproofing, for concrete '
     'pools. It is a single-phase system: no Part B, no mixing ratio, no pot life \u2014 stir and apply, which '
     'removes the classic failure of two-component pool paints, where a small measuring error leaves the whole '
     'pool uncured. The dried film is tough and flexible, engineered for continuous immersion and standing water '
     'pressure without embrittlement or blistering, and is built for outdoor pools: UV-stable colour, resistant '
     'to chlorine and salt-chlorinator water. Genuinely water-based and low-VOC, it is far safer to apply inside '
     'an empty pool \u2014 a naturally confined space \u2014 than solvent-borne systems.')

section('KEY DATA')
kv([
    ('Type',              'One-component water-based waterproof pool paint \u2014 single phase, ready to use'),
    ('Colours',           'White \u00b7 Blue \u00b7 Grey (colour of the water changes once the pool is filled '
                          '\u2014 see product page for filled-pool references)'),
    ('Coverage',          '1 kg \u2248 5 m\u00b2 for the complete 2-coat system, applied in steady forward '
                          'passes at even film thickness'),
    ('Coats',             'Minimum 2. First coat thin \u2014 concrete is absorbent, so let the first coat seal '
                          'the surface; build full film in the second.'),
    ('Drying',            'Touch dry 1\u20132 h \u00b7 recoat 2\u20133 h \u00b7 full set 24\u201348 h'),
    ('Filling the pool',  'Not before 3\u20135 days after the final coat \u2014 the film must reach full '
                          'adhesion and waterproofing strength first'),
    ('Application',       'Roller, brush or spray; keep the film continuous over corners and joints'),
    ('Substrate',         'Concrete pools. Apply direct to sound concrete. Weak or aged surfaces: prime with '
                          'LucernaPro Pool Primer or Core Primer only \u2014 never a primer or additive from '
                          'outside the system; a foreign layer under the film is a future delamination.'),
    ('Pack sizes',        '1 kg (\u2248 5 m\u00b2) \u00b7 5 kg (\u2248 25 m\u00b2) \u00b7 18 kg (\u2248 90 m\u00b2)'),
    ('Clean-up',          'Plain water, before the paint dries'),
    ('Storage',           'Keep tightly closed in a cool, shaded place. Protect from direct sun, heat build-up '
                          'and freezing. Keep out of reach of children.'),
])

section('SURFACE PREPARATION')
para('The surface must be clean, dry and free of dust, algae and oil; scrape blistered or peeling old paint '
     'back to a firm substrate \u2014 the film holds only as well as the surface beneath it. Repair all cracks '
     'and holes flush before painting; skipping repairs defeats the waterproofing no matter how good the paint. '
     'Concrete varies from pool to pool \u2014 hidden moisture, alkalinity and laitance (a weak cement-dust '
     'skin) all attack adhesion. Sound concrete: paint directly. Aged or uncertain concrete: prime first, '
     'within the system only.')

section('APPLICATION')
para('Stir thoroughly to the bottom of the container until fully uniform \u2014 the material settled at the '
     'bottom is an essential part of the formulation. Apply the first coat thin to seal the absorbent concrete, '
     'wait 2\u20133 hours, then apply the second coat at full film. Avoid application in intense direct sun or '
     'when rain is expected, and ventilate well when working in deep pools. Before committing to a large '
     'quantity, a pre-application adhesion test is recommended: coat the unglazed back of a spare ceramic tile '
     '(2 coats, cure 24\u201348 hours), then immerse it \u2014 the film must stay bonded without blistering or '
     'peeling. A pass proves the coating itself; any later failure in the pool then points to surface '
     'preparation or substrate condition, not the material.')

section('SERVICE & LIMITATIONS')
para('After filling: always dissolve chlorine before dosing \u2014 never throw tablets or powder directly into '
     'the pool, as concentrated chlorine sitting on the film attacks the colour \u2014 and keep water pH at '
     '7.0\u20137.8. Persistently acidic water degrades any pool coating. Designed for concrete pools; structural '
     'movement or active leaks must be corrected before coating.')

section('HEALTH & SAFETY')
para('Water-based, non-flammable, low odour and low VOC. Avoid contact with eyes and prolonged contact with '
     'skin; rinse with plenty of water. Do not ingest. Ensure good ventilation when working in the confined '
     'space of an empty pool. Keep out of reach of children. Dispose of residues in accordance with local '
     'regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written files/poolarmour-tds.pdf')
