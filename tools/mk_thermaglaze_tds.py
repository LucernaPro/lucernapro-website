# -*- coding: utf-8 -*-
"""ThermaGlaze TDS — house style (geometry measured from files/deepseal-tds.pdf)."""
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/thermaglaze-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro ThermaGlaze — Technical Data Sheet')


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


# ---------- header / footer ----------
TOTAL = 2


def header(page):
    c.setFont('Helvetica-Bold', 15); c.setFillGray(0)
    c.drawString(L, base(48.5, 15), 'LUCERNAPRO')
    c.setFont('Helvetica-Bold', 13)
    c.drawRightString(R, base(48.0, 13), 'ThermaGlaze')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  July 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Single-Component Thermoplastic Floor Coating')
    c.setStrokeColorRGB(*ORANGE); c.setLineWidth(1.6)
    c.line(L, H - 66.2, R, H - 66.2)


def footer():
    c.setFont('Helvetica', 7.5); c.setFillGray(0)
    c.drawString(L, base(782.0, 7.5),
                 'Lucerna Co., Ltd. \u00b7 23 Suriyat Rd. Soi 4, Nai Mueang, Mueang, Ubon Ratchathani 34000, Thailand')
    c.drawString(L, base(791.0, 7.5),
                 'Tel 062-005-7933 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com')
    c.setFont('Helvetica-Oblique', 6.8); c.setFillGray(0.25)
    foot = ('The information herein is given in good faith based on our current knowledge and practical experience. '
            'Coverage and drying behaviour depend on substrate and site conditions; values are typical guidance only '
            'and do not constitute a specification. Users must verify suitability for their intended application. '
            'Made in Thailand.')
    for i, ln in enumerate(wrap(foot, 'Helvetica-Oblique', 6.8, CW)):
        c.drawString(L, base(800.3 + i * 8.4, 6.8), ln)


def newpage():
    global y
    footer(); c.showPage(); header(2); y = 70.9


header(1)
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
para('ThermaGlaze is a single-component, ready-to-use thermoplastic floor coating supplied in a solvent carrier. '
     'It requires no mixing, no catalyst and no separate primer, and has no pot life \u2014 an opened pack may be '
     'resealed and used again later. The film dries by solvent evaporation and bonds strongly to sound concrete, '
     'and is also used on fibre-cement board, timber and metal. It is suitable for interior and exterior service '
     'and does not yellow on exterior exposure. Supplied pigmented (light grey, dark grey, black) and as a clear '
     'grade. It is a decorative and protective surface film: it seals a porous floor against dusting and staining '
     'and improves cleanability, but it does not add structural strength to the substrate and does not bridge '
     'cracks. It is not intended for glazed ceramic tile or power-trowelled polished concrete.')

section('KEY DATA')
kv([
    ('Chemistry', 'Single-component thermoplastic resin system in organic solvent'),
    ('Supplied form', 'Ready to use \u2014 stir thoroughly from the bottom of the pack; do not thin'),
    ('Grades', 'Pigmented \u00b7 Clear'),
    ('Colours', 'Light grey \u00b7 Dark grey \u00b7 Black \u00b7 Clear'),
    ('Substrates', 'Concrete and cement screed, fibre-cement board, timber, metal'),
    ('Not suitable for', 'Glazed ceramic tile, power-trowelled polished concrete, friable or dusting surfaces '
                         'that have not been prepared, damp substrates and substrates with rising moisture'),
    ('Primer', 'None required on sound concrete. On dusting or highly absorbent concrete, prime with '
               'LucernaPro Marine Guard and allow to dry before coating'),
    ('Substrate age', 'New concrete \u2014 minimum 28 days cure before coating'),
    ('Application', 'Short-nap roller, brush or spray \u2014 thin, even coats'),
    ('Coats', '2 coats standard; apply the second coat cross-wise to the first. Highly absorbent floors may '
              'require a third'),
    ('Coverage', '1 kg \u00bb approx. 5 m\u00b2 over 2 coats on smooth, sound concrete. Rough, porous or highly '
                 'absorbent floors consume significantly more, particularly on the first coat'),
    ('Touch dry', 'Approx. 30\u201360 minutes'),
    ('Overcoating interval', '2\u20134 hours \u2014 longer in cool or humid conditions; overcoat once dry to the touch'),
    ('Light foot traffic', 'After 24 hours'),
    ('Full service', '7 days \u2014 avoid heavy loads, dragging, abrasion, standing water and vehicle traffic '
                     'until then'),
    ('Service exposure', 'Interior and exterior; non-yellowing on exterior exposure'),
    ('Recoating in service', 'Clean, dry and recoat directly \u2014 no abrading of the existing film required'),
    ('Tool cleaning', 'Solvent thinner, immediately while the coating is still wet'),
    ('Packaging', '1 kg \u00b7 2.5 kg \u00b7 5 kg \u00b7 15 kg'),
    ('Storage', 'Sealed original container, dry and shaded, 10\u201330 \u00b0C, away from heat and ignition sources'),
    ('Shelf life', '12 months unopened'),
])

section('NOTE ON VALUES')
para('Coverage and drying figures are typical guidance only, not a specification. Coverage assumes a smooth, '
     'sound concrete substrate at normal film build; rough, porous and previously untreated floors consume '
     'substantially more on the first coat. Drying and overcoating intervals shorten in warm, dry, well-ventilated '
     'conditions and lengthen markedly in cool or humid conditions and in enclosed areas with poor air movement. '
     'Verify by touch before overcoating rather than by the clock.')

newpage()
section('THERMOPLASTIC FILM \u2014 WHAT THIS MEANS IN SERVICE')
para('A thermoplastic film is formed by solvent evaporation rather than by chemical cross-linking. Two practical '
     'consequences follow from this. First, the film remains soluble in its own solvent: a worn or damaged area '
     'can be re-coated directly without abrading, and the new material fuses into the existing film rather than '
     'sitting on top of it as a separate layer, so repairs and maintenance coats leave no visible lap. Second, '
     'the film is not resistant to spilled solvents, fuels or strong solvent-borne chemicals left in prolonged '
     'contact. Where such exposure is expected, a two-component cross-linked floor system should be specified '
     'instead.')

section('APPLICATION NOTES')
bullets([
    'Assess the substrate first. Rub the floor firmly by hand \u2014 if fine powder comes away, the surface layer '
    'is friable and must be mechanically abraded back to sound concrete and primed before coating. A coating '
    'applied over a dusting surface bonds to the dust, not to the concrete.',
    'Repair cracks and holes before coating. A floor coating does not bridge or conceal cracks; fill and level '
    'them first and allow the repair to cure fully.',
    'Remove all oil, grease, curing compounds, laitance and loose old coating. Vacuum thoroughly. The substrate '
    'must be fully dry \u2014 residual moisture beneath a solvent-borne film causes blistering.',
    'Ventilate throughout application and drying. This product contains organic solvents and has a strong odour. '
    'Do not use in enclosed spaces that cannot be ventilated.',
    'Stir thoroughly from the bottom of the pack until colour and consistency are uniform. Do not add thinner to '
    'extend coverage \u2014 a thinner film discards the durability the product was bought for.',
    'Apply the first coat thin and even. On absorbent concrete the first coat will appear to disappear into the '
    'floor; this is normal and expected, and the finished appearance is developed by the second coat.',
    'Plan the working direction and divide the area into bays before starting, so that the applicator is never '
    'required to walk back across wet coating.',
    'Do not apply to damp substrates, to floors subject to rising moisture, or in the open where rain is expected '
    'before the film has dried.',
])

section('HEALTH & SAFETY')
para('Contains organic solvents. Flammable \u2014 keep away from heat, sparks, open flame and hot-work operations, '
     'and do not smoke in the working area. Vapour is heavier than air and may accumulate at floor level in pits '
     'and enclosed spaces. Provide continuous mechanical or natural ventilation during application and drying, '
     'and wear an organic-vapour respirator, chemical-resistant gloves and eye protection \u2014 a dust mask is '
     'not adequate protection against solvent vapour. Do not work alone in a confined space. Keep out of reach of '
     'children. Do not empty into drains or waterways. Dispose of solvent-contaminated rags in a closed metal '
     'container. Refer to the Safety Data Sheet for full information.')

# ---------- close ----------
footer()
c.showPage(); c.save()
print('written')
