# -*- coding: utf-8 -*-
"""Lucerna Epoxy TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page).
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/lucerna-epoxy-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro Lucerna Epoxy — Technical Data Sheet')


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
    c.drawRightString(R, base(48.0, 13), 'Lucerna Epoxy')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Two-component High-build Epoxy Floor Coating')
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
    """Justified paragraph (มติ QA 18 ส.ค.: information paragraphs = justify)"""
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
para('Lucerna Epoxy is a two-component, high-build epoxy floor coating: a high molecular weight epoxy resin '
     'cured with a polyamide hardener, for properly prepared concrete and cement floors and walls. It is easy '
     'to apply and gives a hard, glossy film with excellent chemical and abrasion resistance, suitable as a '
     'top coat over an approved primer or as a single-coat system, in both atmospheric and immersed service. '
     'Interior use only \u2014 like all standard epoxies it is not suitable for outdoor areas or direct '
     'sunlight, where UV exposure causes chalking and colour change.')

section('KEY DATA')
kv([
    ('Type',           'Two-component solvent-based epoxy (polyamide-cured), high-build'),
    ('Colours',        'Per RAL K7 standard colour range'),
    ('Mixing ratio',   'Part A : Part B = 4 : 1 by weight \u2014 mix the full set where possible; '
                       'weigh accurately if splitting'),
    ('Coverage',       '\u2248 100 m\u00b2 per 16 kg set per coat; apply 2\u20133 coats for a fully '
                       'performing film'),
    ('Drying (25 \u00b0C)', 'Touch dry 2 h \u00b7 walk-on 5 h \u00b7 recoat from 5 h (typically 4\u20138 h '
                       'depending on temperature, humidity and airflow) \u00b7 light traffic 2 days \u00b7 '
                       'full cure 7 days'),
    ('Film properties', 'Gloss 60\u00b0 > 80 GU \u00b7 pencil hardness HB\u20132H \u00b7 cross-cut adhesion '
                       '100/100 \u00b7 solids 65 \u00b1 5 % \u00b7 specific gravity 1.35 \u00b1 0.15'),
    ('Application',    'Brush for stripes and small areas; roller for large areas'),
    ('Pack sizes',     '16 kg set (Part A 12.8 kg + Part B 3.2 kg) \u00b7 4 kg set (Part A 3.2 kg + '
                       'Part B 0.8 kg)'),
    ('Clean-up',       'Epoxy thinner. Clean mixing containers thoroughly before reuse \u2014 cured '
                       'particles from a previous batch cause film defects.'),
    ('Storage',        '12 months in unopened containers, tightly closed, in a dry, cool, well-ventilated '
                       'space below 37 \u00b0C, away from heat and ignition sources'),
])

section('SURFACE PREPARATION')
para('The substrate must be clean and dry \u2014 free of dust, oil and grease \u2014 with all laitance and '
     'contamination such as release or curing agents removed. New concrete must cure at least 4 weeks and '
     'read below 10 % moisture; sand or blast the surface, then fill pinholes and small cracks with a '
     'suitable repair material before priming, so the coating bonds to sound substrate. Old concrete must be '
     'prepared to the same standard. Prime within the LucernaPro system.')

section('APPLICATION & LIMITATIONS')
para('Mix Part A and Part B at 4 : 1 by weight until fully uniform, then apply by brush or roller. Allow each '
     'coat to cure through before recoating. Do not apply to wet or green concrete, or over polymer-modified '
     'patches, if moisture content exceeds 5 %; do not apply when air or substrate temperature is within '
     '3 \u00b0C of the dew point; protect the substrate from condensation from pipes or overhead leaks during '
     'application, and never coat surfaces where moisture vapour can condense and freeze \u2014 moisture '
     'trapped under an epoxy film is the classic cause of blistering and delamination.')

section('HEALTH & SAFETY')
para('Solvent-based: flammable \u2014 keep away from heat, sparks and open flame, and ensure good ventilation '
     'during mixing, application and cure. Avoid contact with skin and eyes; wear suitable gloves and eye '
     'protection, and rinse with plenty of water on contact. Do not ingest. Keep out of reach of children. '
     'Dispose of residues in accordance with local regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written', os.environ.get('LP_OUT', 'files/lucerna-epoxy-tds.pdf'))
