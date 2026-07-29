# -*- coding: utf-8 -*-
"""IronLock TDS — house style (geometry measured from files/deepseal-tds.pdf)."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
import os

W, H = A4                      # 595.2756 x 841.8898
L, R = 45.4, 549.9
CW = R - L
ORANGE = (0.847059, 0.341176, 0.109804)
BAR    = (0.937255, 0.937255, 0.925490)
RULE   = (0.862745, 0.862745, 0.839216)
BODY, LEAD = 8.6, 12.2
LABEL_W = 156.7

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/ironlock-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro IronLock — Technical Data Sheet')


def base(bottom, size):           # pdfplumber 'bottom' -> reportlab baseline
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


# ---------- header ----------
c.setFont('Helvetica-Bold', 15); c.setFillGray(0)
c.drawString(L, base(48.5, 15), 'LUCERNAPRO')
c.setFont('Helvetica-Bold', 13)
c.drawRightString(R, base(48.0, 13), 'IronLock')
c.setFont('Helvetica', 8.0)
c.drawString(L, base(58.0, 8.0), 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  July 2026')
c.setFont('Helvetica', 8.5)
c.drawRightString(R, base(58.1, 8.5), 'Water-Based Anti-Corrosive Coating')
c.setStrokeColorRGB(*ORANGE); c.setLineWidth(1.6)
c.line(L, H - 66.2, R, H - 66.2)

y = 70.9                                    # running "top" cursor (from page top)


def section(title):
    global y
    c.setFillColorRGB(*BAR)
    c.rect(L, H - (y + 13), CW, 13, stroke=0, fill=1)
    c.setFillGray(0); c.setFont('Helvetica-Bold', 9.0)
    c.drawString(L + 4.0, base(y + 11.3, 9.0), title)
    y += 13


def para(text, gap=14.2, indent=2.0):
    global y
    y += gap
    c.setFillGray(0); c.setFont('Helvetica', BODY)
    for ln in wrap(text, 'Helvetica', BODY, CW - indent):
        c.drawString(L + indent, base(y + 8.6, BODY), ln)
        y += LEAD
    y -= LEAD
    y += 8.6


def bullets(items, gap=14.2):
    global y
    y += gap
    c.setFillGray(0)
    for it in items:
        c.setFont('Helvetica', BODY)
        c.drawString(L + 2.0, base(y + 8.6, BODY), '\u2022')
        for i, ln in enumerate(wrap(it, 'Helvetica', BODY, CW - 12.0)):
            c.drawString(L + 12.0, base(y + 8.6, BODY), ln)
            y += LEAD
        y -= LEAD
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
para('IronLock is a single-component, ready-to-use water-based anti-corrosive coating for steel and coated-steel '
     'substrates. It is built around an active anti-corrosive pigment sourced from a United States specialty-chemicals '
     'producer \u2014 chosen in place of the zinc-based inhibitive pigments in common use because it is not classified '
     'as toxic and not classified as hazardous to the aquatic environment \u2014 dispersed in a waterborne binder '
     'system. It is formulated to bond directly to substrates that conventional anti-corrosive paints handle poorly, '
     'including hot-dip galvanised steel, zinc sheet and metal roofing sheet, and needs no separate primer. The dried '
     'film is low in odour, tolerates standing water, and acts both as a corrosion barrier and as a renewable wear '
     'layer on surfaces under continuous water flow such as gutters. It is not intended for use over active rust.')

section('KEY DATA')
kv([
    ('Chemistry', 'Single-component waterborne coating with an active anti-corrosive pigment (US-sourced)'),
    ('Supplied form', 'Ready to use \u2014 stir thoroughly before use; do not thin with water'),
    ('Colours', 'White \u00b7 Grey \u00b7 Black'),
    ('Substrates', 'Steel, sheet steel, structural sections, galvanised steel, zinc sheet, roofing sheet'),
    ('Primer', 'None required \u2014 direct-to-metal'),
    ('Application', 'Brush, roller or spray \u2014 thin, even coats'),
    ('Coats', '2 coats standard; apply the second coat cross-wise to the first'),
    ('Overcoating interval', '30\u201360 minutes, ambient-dependent \u2014 overcoat once dry to the touch'),
    ('Coverage', '1 kg \u00bb approx. 5 m\u00b2 over 2 coats on smooth substrates (4.5 kg \u00bb approx. 22 m\u00b2). '
                 'Open sections \u2014 railings, fences, gratings, lattice \u2014 consume substantially more'),
    ('Service exposure', 'Interior and exterior; tolerates standing water once fully dry'),
    ('Tool cleaning', 'Water, immediately while the coating is still wet'),
    ('Packaging', '1 kg \u00b7 4.5 kg'),
    ('Storage', 'Sealed original container, dry, 10\u201330 \u00b0C \u2014 protect from frost, do not allow to freeze'),
    ('Shelf life', '12 months unopened'),
])

section('NOTE ON VALUES')
para('Coverage assumes smooth, non-absorbent substrates at normal film build. Profiled roofing sheet, previously '
     'corroded steel and open sections such as fences and gratings consume significantly more, because the true '
     'surface area is several times the area the eye estimates. Figures here are typical guidance only, not a '
     'specification.')

section('APPLICATION NOTES')
bullets([
    'Assess the substrate first. IronLock is a protective coating, not a rust treatment \u2014 it is not designed to '
    'be applied over active rust.',
    'Rust must be removed or converted first. Loose scale must always come off mechanically; where full mechanical '
    'cleaning is impractical \u2014 structural steel, large frameworks \u2014 convert the remaining rust with a rust '
    'converter and let it dry before coating.',
    'Degrease new material. New steel, galvanised steel and roofing sheet normally carry an invisible mill oil or '
    'anti-corrosion film from the factory \u2014 the most common single cause of coating failure. Clean with a '
    'degreaser or soapy water, rinse and dry fully.',
    'Stir thoroughly from the bottom of the pack until colour and consistency are uniform \u2014 inadequate stirring '
    'leaves the anti-corrosive pigment sitting in the bottom.',
    'Apply thin, even coats rather than one heavy coat, especially on round sections, corners, welds and fastener '
    'heads \u2014 the points where film thins and where corrosion starts first.',
    'Do not apply if rain is expected within a few hours, onto wet or dew-covered surfaces, or onto roofing sheet '
    'hot in direct sun \u2014 the film dries too fast to flow out evenly.',
    'On rainwater gutters, coat the full run inside and out \u2014 the inner face is where water, silt and leaf '
    'litter attack the substrate first. Avoid water, abrasion and heavy loads for the first 24 hours.',
])

section('HEALTH & SAFETY')
para('Water-based and low in odour, but this is an industrial coating. Wear gloves and eye protection, avoid '
     'prolonged skin contact, and ventilate when spraying. Keep out of reach of children. Do not empty into drains '
     'or waterways. Refer to the Safety Data Sheet for full information.')

# ---------- footer ----------
c.setFont('Helvetica', 7.5); c.setFillGray(0)
c.drawString(L, base(782.0, 7.5),
             'Lucerna Co., Ltd. \u00b7 23 Suriyat Rd. Soi 4, Nai Mueang, Mueang, Ubon Ratchathani 34000, Thailand')
c.drawString(L, base(791.0, 7.5),
             'Tel 062-005-7933 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com')
c.setFont('Helvetica-Oblique', 6.8); c.setFillGray(0.25)
foot = ('The information herein is given in good faith based on our current knowledge and practical experience. '
        'Coverage and drying behaviour depend on substrate and site conditions; values are typical guidance only and '
        'do not constitute a specification. Users must verify suitability for their intended application. '
        'Made in Thailand.')
for i, ln in enumerate(wrap(foot, 'Helvetica-Oblique', 6.8, CW)):
    c.drawString(L, base(800.3 + i * 8.4, 6.8), ln)

c.showPage(); c.save()
print('written')
