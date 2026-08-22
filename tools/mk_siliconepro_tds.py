# -*- coding: utf-8 -*-
"""SiliconePro TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page).
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/siliconepro-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro SiliconePro — Technical Data Sheet')


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
    c.drawRightString(R, base(48.0, 13), 'SiliconePro')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Water-based Silicone Waterproofing \u2014 Ready to Use')
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
para('SiliconePro is a one-component, water-based silicone waterproofing coating for rooftop decks, roofs and '
     'joints, supplied ready to use: no Part B, no measuring, no working-time pressure \u2014 stir and brush. '
     'The thick, dense body holds its line well over joints and seams, and the cured film is flexible, '
     'UV-resistant outdoors and tolerant of ponding water \u2014 the standing-water condition on flat decks '
     'where most waterproofing membranes blister and peel first. Film thickness is the one variable in the '
     'user\u2019s hands, and the rule is simple: the thicker the film, the longer it lasts. Applied bare, the '
     'system serves around 5 years; reinforced with woven fiberglass cloth it extends to 8\u201310 years. It '
     'also serves as a sacrificial top layer over LucernaPro PolyPro, taking the sun and wear so that only this '
     'layer needs renewing at maintenance time.')

section('KEY DATA')
kv([
    ('Type',            'One-component water-based silicone waterproofing coating \u2014 ready to use'),
    ('Colour',          'Grey. Overpaintable with ordinary paint once the film has fully set.'),
    ('Coverage',        'Standard mode: 1 kg \u2248 5 m\u00b2 for the complete 2-coat system. Fiberglass mode: '
                        'approx. 1 kg per 1 m\u00b2 \u2014 far higher consumption, traded for service life.'),
    ('Service life',    'Approx. 5 years applied bare \u00b7 8\u201310 years with woven fiberglass '
                        'reinforcement \u00b7 thicker films last longer in both modes'),
    ('Coats',           'Minimum 2, brush or roller, an even continuous film over every corner and joint'),
    ('Recoat',          'Approx. 2 hours between coats'),
    ('Return to service', 'At least 6 hours after the final coat'),
    ('Priming',         'Glazed tile: prime with LucernaPro MarineGuard first \u2014 mandatory. Ordinary '
                        'concrete: no primer; it adds nothing. Fiberglass mode: no primer in any case.'),
    ('Pack sizes',      '1 kg (\u2248 5 m\u00b2) \u00b7 2.5 kg (\u2248 12.5 m\u00b2) \u00b7 5 kg (\u2248 25 m\u00b2), '
                        'standard 2-coat basis'),
    ('Lid discipline',  'Decant only what is needed and reseal the tub immediately \u2014 material left in an '
                        'open tub begins to set and is lost. Never work from an open tub.'),
    ('Storage',         'Keep tightly closed in a cool, shaded place. Protect from direct sun, heat build-up '
                        'and freezing. Keep out of reach of children.'),
])

section('SURFACE PREPARATION')
para('The surface must be completely dry, clean and free of dust and grease \u2014 wash down and allow to dry '
     'fully before starting; the film bonds only as well as the surface is clean. Fill all cracks and joint '
     'gaps flush first \u2014 on deck work use LucernaPro PatchPro \u2014 then coat over; skipping the repair '
     'stage defeats the waterproofing system. On glazed tile, prime with MarineGuard before coating; unprimed '
     'film does not hold on a glazed surface.')

section('APPLICATION')
para('Stir the tub thoroughly to a single uniform body, decant a working quantity and reseal the lid at once. '
     'Apply the first coat by brush or roller, covering corners and joint lines completely \u2014 an even, '
     'continuous film matters more than local thickness. Recoat after about 2 hours; two coats minimum, and a '
     'third only adds life. Allow at least 6 hours after the final coat before returning the area to service. '
     'FIBERGLASS MODE (8\u201310 years): apply a thin wet coat along the run, lay woven fiberglass cloth into '
     'the wet film and press it flat \u2014 no air pockets, no wrinkles \u2014 then topcoat repeatedly until no '
     'white point of cloth shows anywhere. A visible white point is a pinhole that lets water sit beneath the '
     'cloth and fail worse than bare concrete; coat until every one is gone.')

section('HEALTH & SAFETY')
para('Water-based, non-flammable, low odour. Avoid contact with eyes and prolonged contact with skin; rinse '
     'with plenty of water. Do not ingest. Ensure normal ventilation during application and drying. Keep out '
     'of reach of children. Dispose of residues in accordance with local regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written files/siliconepro-tds.pdf')
