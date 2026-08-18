# -*- coding: utf-8 -*-
"""SurfaceGuard TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page)."""
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/surfaceguard-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro SurfaceGuard — Technical Data Sheet')


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
    c.drawRightString(R, base(48.0, 13), 'SurfaceGuard')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.3  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Water-based PUD Floor Coating')
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
            'Coating performance depends on substrate, surface preparation, film thickness and site conditions; '
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
para('SurfaceGuard is a one-component, water-based floor coating for concrete and cement floors, built on '
     'premium self-crosslinking polyurethane dispersion (PUD) technology. The carrier is water rather than '
     'solvent, so odour during application is very low and rooms can remain occupied while work proceeds. The '
     'dried film is a true polyurethane: it resists water, the alkalinity of cementitious substrates and everyday '
     'scratching and scuffing, and it withstands sunlight for interior and exterior use. Supplied ready to use '
     '\u2014 stir and apply by roller, no mixing ratios, no pot life \u2014 tools clean up with plain water.')

section('KEY DATA')
kv([
    ('Type',              'One-component waterborne self-crosslinking polyurethane dispersion (PUD) floor coating'),
    ('Colours',           'White \u00b7 Light Grey \u00b7 Dark Grey \u00b7 Blue \u00b7 Sky Blue (select shade when ordering)'),
    ('Finish',            'Smooth, uniform film'),
    ('Odour',             'Very low \u2014 suitable for occupied interiors with normal ventilation'),
    ('Coverage',          'Approx. 5 m\u00b2 per kg for the complete 2-coat system on smooth, sound concrete; '
                          'rough or porous substrates consume more'),
    ('Recommended system','2 coats by short-pile roller, second coat applied crosswise to the first'),
    ('Pack sizes',        '1 kg and 5 kg'),
    ('Clean-up',          'Plain water, before the coating dries'),
    ('Storage',           'Keep tightly closed in a cool, shaded place. Protect from direct sun, heat build-up '
                          'and freezing'),
])

section('DRYING TIMES  (25 \u00b0C, 50 % RH \u2014 typical)')
kv([
    ('Touch dry',            '30\u201360 minutes'),
    ('Recoat',               '2\u20134 hours'),
    ('Light foot traffic',   'After 24 hours'),
    ('Normal service',       'After 3 days'),
    ('Full cure',            '7 days \u2014 avoid dragging furniture, parking vehicles, hard scrubbing and '
                             'standing water during this period'),
])

section('SURFACE PREPARATION')
para('New concrete must cure for at least 4 weeks before coating. The substrate must be clean, dry and sound: '
     'remove dust, oil, grease and algae completely \u2014 oil is the leading cause of adhesion failure. Dusting '
     'or friable surfaces must be repaired first; paint over a weak layer fails with that layer. Previously '
     'painted floors: abrade sound paint to a dull finish and remove flaking paint back to a firm substrate. '
     'Repair cracks and holes first and allow repairs to dry fully.')

section('APPLICATION')
para('Stir thoroughly to the bottom of the can before use. Apply 2 coats by short-pile roller in thin, even '
     'films; apply the second coat crosswise once the first has dried (2\u20134 h). Do not dilute with water to '
     'stretch coverage. Do not apply to damp floors, or outdoors if rain is expected within 6 hours.')

section('LIMITATIONS')
para('Designed for residential and light-to-medium commercial floors: homes, balconies, walkways, private '
     'garages, shops and offices. Not an industrial flooring system \u2014 forklift traffic, dragged machinery '
     'or routine aggressive chemical spillage requires a heavy-duty epoxy-PU system instead. The dried film is '
     'smooth; wet floors should be walked with care. In-house testing: the cured film passed 7 days of '
     'continuous immersion in highly alkaline cement water in the Lucerna laboratory.')

section('HEALTH & SAFETY')
para('Water-based, non-flammable, very low odour. Avoid contact with eyes and skin; rinse with plenty of water. '
     'Do not ingest. Keep out of reach of children. Ensure normal ventilation during application and drying. '
     'Dispose of residues in accordance with local regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written files/surfaceguard-tds.pdf')
