# -*- coding: utf-8 -*-
"""SpackleFlex TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page).
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/spackleflex-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro SpackleFlex — Technical Data Sheet')


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
    c.drawRightString(R, base(48.0, 13), 'SpackleFlex')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Flexible Roof Joint Repair Putty \u2014 Ready to Use')
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
para('SpackleFlex is a one-component, water-based flexible polymer repair putty for roof leaks, supplied ready '
     'to use from the factory. It seals the classic leak points of Thai roofs \u2014 fastener heads, sheet '
     'joints and roof-to-wall junctions \u2014 in a single product, on every roof type: metal sheet, corrugated '
     'tile, cement tile and zinc (concrete rooftop decks excluded \u2014 those are full-surface waterproofing '
     'work). Roofs expand and contract with temperature day and night, and rigid repair materials crack with '
     'them; the SpackleFlex body stays highly flexible and moves with the roof, and its white polymer is '
     'UV-stabilised for far longer outdoor life than ordinary silicone sealant. Repaired samples have passed '
     'months of continuous immersion in the Lucerna soak tank with the body intact, firmly bonded and free of '
     'swelling \u2014 ponding water in roof channels is within its design duty.')

section('KEY DATA')
kv([
    ('Type',            'One-component water-based flexible polymer roof repair putty \u2014 ready to use'),
    ('Colour',          'White \u2014 reflects heat on the roof'),
    ('Suitable roofs',  'Metal sheet, corrugated tile, cement tile, zinc \u2014 all pitched roof types. NOT '
                        'for concrete rooftop decks (use a full-surface waterproofing system there).'),
    ('Repairs',         'Fastener heads \u00b7 sheet joints and seams \u00b7 roof-to-wall junctions and '
                        'flashing lines'),
    ('Consistency',     'Thick white cream \u2014 applies by putty knife (tub) or caulking gun (cartridge). '
                        'Not brushable; not a full-surface coating product.'),
    ('Set time',        'At least 6 hours before rain, service, or overcoating'),
    ('Overcoating',     'Optional, for maximum service life: after 6 hours, coat over with LucernaPro '
                        'SiliconePro or Exotic'),
    ('Pack sizes',      '350 g cartridge (caulking gun) \u00b7 1 kg tub (putty knife) \u00b7 20 kg pail'),
    ('Dilution',        'NEVER dilute with water or thinner \u2014 dilution destroys the designed flexibility '
                        'and water resistance'),
    ('Clean-up',        'Plain water, while the material is still fresh. Reseal the container airtight; '
                        'material keeps for later use.'),
    ('Storage',         'Keep tightly closed in a cool, shaded place. Protect from direct sun, heat build-up '
                        'and freezing. Keep out of reach of children.'),
])

section('SURFACE PREPARATION')
para('The surface must be completely dry, clean and free of dust and grease before filling \u2014 applied over '
     'a wet or damp surface, adhesion is lost before the repair begins. Check the weather first: do not apply '
     'when the surface is wet or rain is expected within 6 hours.')

section('APPLICATION')
para('Ready to use \u2014 open and apply; never mix anything in. Press the material over the repair area with '
     'a putty knife, or run a continuous bead from the cartridge along joint lines, until the point is covered '
     'completely with no holes or breaks \u2014 water always finds a hole, so the film must be one continuous '
     'body. Work point by point along fastener lines and seams without skipping. Allow at least 6 hours to set '
     'before the repair meets rain or before overcoating. Roof safety always comes first: non-slip footwear, '
     'step on the purlin lines, never mid-sheet.')

section('LIMITATIONS')
para('Roof work only. The body is engineered for maximum flexibility, and the trade-off is stated plainly: the '
     'cured surface cannot be sanded or painted over \u2014 do not use it on walls, furniture or any repair '
     'that must be finished with paint. It is a spot-and-seam repair putty, not a coating: for full-surface '
     'work, use a brush-applied waterproofing system instead.')

section('HEALTH & SAFETY')
para('Water-based, non-flammable, low odour. Avoid contact with eyes and prolonged contact with skin; rinse '
     'with plenty of water. Do not ingest. Ensure normal ventilation during application and drying. Keep out '
     'of reach of children. Dispose of residues in accordance with local regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written files/spackleflex-tds.pdf')
