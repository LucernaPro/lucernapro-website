# -*- coding: utf-8 -*-
"""SchutzFirearm TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page).
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/schutzfirearm-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro SchutzFirearm — Technical Data Sheet')


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
    c.drawRightString(R, base(48.0, 13), 'SchutzFirearm')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Micron-thin Ceramic Protective Coating')
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
para('SchutzFirearm is a one-component polysilazane ceramic coating for the exterior protection of firearms, '
     'applied by the wipe-on, wipe-off method. On curing, the liquid converts to a dense ceramic network of '
     'Si\u2013N\u2013Si and Si\u2013O\u2013Si bonds anchored to the metal \u2014 a permanent micron-thin '
     'barrier, not an oil film that evaporates or wipes away. The cured surface is dry to the touch and matte: '
     'it sheds water, resists cleaning chemicals and heat, reduces glare, and gives a firmer grip than an '
     'oiled surface \u2014 the exterior no longer needs rust-preventive oil at all. Consumption is remarkably '
     'low: 2\u20133 drops coat an entire handgun. The chemistry comes from industrial thin-film ceramic '
     'coating work; protecting a firearm is a small task for it.')

section('KEY DATA')
kv([
    ('Type',            'One-component polysilazane ceramic coating \u2014 wipe on, wipe off'),
    ('Substrates',      'Steel, plastic and polymer frames \u2014 exterior surfaces'),
    ('Finish',          'Matte, glare-reducing, dry to the touch; micron-thin \u2014 does not alter part '
                        'dimensions when applied thin and wiped off'),
    ('Consumption',     '2\u20133 small drops per handgun, applied from a coating foam \u2014 never dropped '
                        'onto the firearm directly'),
    ('Flash time',      'Wipe off excess after at least 2 minutes and no later than 5 \u2014 time it, do not '
                        'guess. Past 5 minutes the film hardens and is very difficult to remove.'),
    ('Cure',            'Initial 24 hours dry, no water contact \u00b7 full cure 7 days \u2014 full hardness, '
                        'chemical and heat resistance develop only after this'),
    ('Pack size',       '10 ml bottle'),
    ('Bottle care',     'Reseal immediately after use \u2014 the coating cures with moisture in the air, and '
                        'a bottle left open hardens in the bottle'),
    ('Storage',         'Tightly closed, cool, dry and shaded, away from heat and ignition sources. Keep out '
                        'of reach of children.'),
])

section('MEASURED PROPERTIES \u2014 AFTER 7-DAY FULL CURE')
kv([
    ('Pencil hardness', '4H'),
    ('Water contact angle', '> 100\u00b0 \u2014 hydrophobic; water beads and rolls off'),
    ('Heat resistance', 'Up to 400 \u00b0C after full cure'),
    ('Chemical resistance', 'Acids, alkalis, solvents and common cleaning agents; UV-stable outdoors'),
    ('Abrasion',        'Withstands normal handling and holster wear'),
])

section('APPLICATION')
para('Degrease completely first \u2014 the ceramic film cannot bond over oil; wash off all rust-preventive '
     'oil and leave the surface clean and dry. Place 2\u20133 drops on the coating foam and spread thinly; '
     'coverage is all that is needed \u2014 a thicker film protects no better, it only streaks and hardens '
     'into residue. Work one section at a time (slide, frame, small parts) to keep the wipe timing easy. After '
     '2\u20135 minutes, buff the excess off with a microfiber cloth in circular strokes until uniform, leaving '
     'no residue. Cure 24 hours dry; full protection arrives at 7 days.')

section('LIMITATIONS')
para('The coating prevents \u2014 it does not reverse. Existing rust is not removed and existing wear marks '
     'are not filled; the worn front slide edges of any well-used firearm are only partially masked, though '
     'protected well against further wear. Do not coat the bore or internal slide parts unless certain \u2014 '
     'toleranced components are not worth the risk; when in doubt, skip them. The internal mechanism still '
     'requires its normal lubrication; only the exterior is freed from oil.')

section('HEALTH & SAFETY')
para('Solvent-borne and flammable. Use only with good ventilation, away from flames, sparks and smoking; the '
     'coating releases vapour while drying and curing. Wear gloves and avoid contact with skin and eyes; wash '
     'skin with soap and water. Do not ingest. Keep away from moisture until applied. Keep out of reach of '
     'children. Dispose of residues in accordance with local regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written files/schutzfirearm-tds.pdf')
