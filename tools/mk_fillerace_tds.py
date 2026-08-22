# -*- coding: utf-8 -*-
"""FillerAce TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page).
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/fillerace-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro FillerAce — Technical Data Sheet')


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
    c.drawRightString(R, base(48.0, 13), 'FillerAce')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Flexible Sandable Crack Filler \u2014 Ready to Use')
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
            'Performance depends on substrate, surface preparation, repair geometry and site conditions; '
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
para('FillerAce is a one-component, water-based flexible polymer filler for repairing cracks and joints in walls, '
     'supplied ready to use straight from the tub \u2014 no measuring, no mixing. Conventional fillers force a '
     'choice: hard fillers sand well but crack again when the wall moves, while flexible sealants move with the '
     'wall but cannot be sanded or painted. FillerAce combines both properties: the cured body remains flexible '
     'enough to follow normal wall movement, yet sands to a smooth finish and takes paint normally. It is '
     'formulated for full exterior exposure \u2014 sun, rain and long-term ponding water \u2014 and repairs from '
     'hairline cracks up to voids around 10 cm across in a single product. The thick, non-sag body stays where '
     'it is placed and bonds strongly to render, mortar and concrete; it also serves as a wood filler.')

section('KEY DATA')
kv([
    ('Type',            'One-component water-based flexible polymer filler \u2014 ready to use'),
    ('Repair range',    'Hairline cracks (after routing open \u2014 see Surface Preparation) up to voids '
                        'approx. 10 cm across'),
    ('Substrates',      'Render, mortar, concrete walls; also usable as a wood filler'),
    ('Use',             'Interior and exterior. Walls only \u2014 not recommended for trafficked floors, where '
                        'the body collects dirt, unless overcoated with a flexible PU floor paint.'),
    ('Ready to sand',   'Approx. 2 hours (typical conditions); sand coarse grit first, then fine'),
    ('Overcoating',     'Interior: paint directly after sanding. Exterior: apply a waterproof coating over the '
                        'repair before painting for maximum service life.'),
    ('Consumption',     'Material (g) \u2248 groove width (mm) \u00d7 depth (mm) \u00d7 length (m) \u00d7 1.7. '
                        'Example: a routed 5 \u00d7 5 mm groove takes approx. 40\u201345 g per metre \u2014 '
                        'roughly 20 m per 1 kg tub including wastage.'),
    ('Pack sizes',      '1 kg tub and 20 kg pail'),
    ('Clean-up',        'Plain water, while the material is still fresh'),
    ('Storage',         'Keep tightly closed in a cool, shaded place. Protect from direct sun, heat build-up '
                        'and freezing. Keep out of reach of children.'),
])

section('SURFACE PREPARATION')
para('The surface must be clean, sound and free of dust and loose mortar \u2014 adhesion is only as good as the '
     'surface beneath. Hairline cracks must be routed open with a grinder before filling: a narrow crack is too '
     'tight for the filler to reach the bottom, so material smeared over the surface bonds only to a thin skin '
     'and peels away when the wall moves or gets wet. Routing the crack open to let the filler reach full depth '
     'is the step that separates a repair lasting years from one that fails in the first month. Do not skip it.')

section('APPLICATION')
para('Ready to use \u2014 open the tub and fill. Press the material into the groove with a putty knife until it '
     'is packed full to the bottom, then strike off the line. Do not skim it thin: the repair needs body to '
     'carry load, so keep at least normal filling thickness. While the surface is still damp, smooth it over '
     'with plain water \u2014 a well-smoothed surface greatly reduces sanding. For an especially fine finish, '
     'skim-coat over the repair. After approx. 2 hours the repair is ready to sand: a power sander working from '
     'coarse to fine grit gives the smoothest result fastest. Large voids can be filled directly \u2014 the '
     'non-sag body will not slump.')

section('LIMITATIONS')
para('FillerAce resists re-cracking very well on walls subject to normal movement. It cannot restrain a '
     'structure that is still settling or moving severely \u2014 no filler can \u2014 and such cases must be '
     'corrected at the structural cause first. For heavy-duty repairs beyond the scope of a wall filler, '
     'including underwater and waterproofing repair work, use LucernaPro DeepStick.')

section('HEALTH & SAFETY')
para('Water-based and non-flammable. Avoid contact with eyes and prolonged contact with skin; rinse with plenty '
     'of water. Do not ingest. Wear a dust mask when sanding the cured material. Ensure normal ventilation '
     'during application and drying. Keep out of reach of children. Dispose of residues in accordance with '
     'local regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written files/fillerace-tds.pdf')
