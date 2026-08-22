# -*- coding: utf-8 -*-
"""Epoxy TileGrout TDS — house style (geometry per files/deepseal-tds.pdf lineage, 1 page)."""
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/epoxygrout-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro Epoxy TileGrout — Technical Data Sheet')


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
    c.drawRightString(R, base(48.0, 13), 'Epoxy TileGrout')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  August 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'Two-component Waterproof Epoxy Tile Grout')
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
            'Performance depends on substrate, surface preparation, joint condition and site conditions; '
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
para('Epoxy TileGrout is a two-component epoxy grout for regrouting tile joints without removing a single tile. '
     'Ordinary cement grout is porous: it absorbs water, feeds black mould and is the number-one path by which '
     'bathroom water finds its way under the tiles and into the room below. The cured epoxy joint is dense and '
     'non-absorbent \u2014 it seals the joint at the source, resists mould and staining, and wipes clean. Unlike '
     'most two-component grouts on the market, the mixing ratio is an equal 1 : 1 by weight \u2014 the simplest '
     'possible ratio to measure, so first-time users can portion the two parts accurately without special '
     'equipment. Designed for waterproofing service life of up to 5 years on a correctly prepared joint.')

section('KEY DATA')
kv([
    ('Type',            'Two-component (2K) epoxy tile grout \u2014 self-mix'),
    ('Mixing ratio',    'Part A : Part B = 1 : 1 \u2014 equal parts. Mix only as much as can be used before the '
                        'material begins to set; work zone by zone.'),
    ('Colours',         'White \u00b7 Light Grey \u00b7 Dark Grey'),
    ('Coverage',        '1 kg \u2248 10 m\u00b2 of grout line, based on 30 \u00d7 30 cm tiles and larger. Smaller '
                        'tiles or wider joints consume more.'),
    ('Return to service', '4\u20136 hours after grouting. Keep the joints away from water while curing.'),
    ('Application',     'Spread into the joint between masking-tape lines; compact fully, then tool the line '
                        'smooth with a flat stick'),
    ('Pack sizes',      '1 kg (\u2248 10 m\u00b2) and 2 kg (\u2248 20 m\u00b2)'),
    ('Clean-up',        'Wipe off any grout outside the line immediately, while still fresh \u2014 cured epoxy is '
                        'very difficult to remove from the tile face'),
    ('Storage',         'Keep both components tightly closed in a cool, shaded place, away from heat and direct '
                        'sunlight. Keep out of reach of children.'),
])

section('SURFACE PREPARATION')
para('Scrape the old cement grout out completely, down to the body of the joint \u2014 the new grout is only as '
     'strong as the joint beneath it. Brush out the dust and wipe the joint clean and dry. Then mask both sides '
     'of every joint with tape. Taping is a rule, not an option: epoxy that cures on the tile face is very '
     'difficult to remove, so if the tape is not on, do not start grouting.')

section('APPLICATION')
para('Measure Part A and Part B in equal amounts, 1 : 1, and stir until the mix is one single uniform colour with '
     'no streaks \u2014 incomplete mixing is the one failure that ruins the whole line, leaving the grout soft and '
     'uncured. Mix in portions; never mix the full pack at once and leave it standing. Spread the mixed grout '
     'into the joint between the tape lines and compact it fully \u2014 an air void today is a water path '
     'tomorrow. Tool the line smooth and level with a flat stick (an ice-cream stick works well). Remove the '
     'tape immediately after each line is finished, while the grout is still fresh; tape removed after cure '
     'tears a ragged edge. Allow 4\u20136 hours to set before returning the area to service, and keep water off '
     'the joints during this period.')

section('LIMITATIONS')
para('A self-mix grout trades convenience for economy: the user must measure, mix and work within the pot time '
     'of the material. Where the job cannot tolerate a mixing error \u2014 first-time users, or work handed to a '
     'contractor \u2014 LucernaPro Carbon is the same waterproof grout concept in a dual-cartridge gun format '
     'that mixes itself at the nozzle. Quoted coverage assumes 30 \u00d7 30 cm tiles; verify quantities for '
     'small-format tiles or wide joints before ordering.')

section('HEALTH & SAFETY')
para('Epoxy resin and hardener can irritate and sensitise the skin. Wear rubber gloves and avoid contact with '
     'skin and eyes; wash any contact immediately with soap and water \u2014 never with solvent. Do not ingest. '
     'Ensure normal ventilation during application and curing. Keep out of reach of children. Dispose of '
     'residues in accordance with local regulations.')

print('final y =', y)
assert y < 770, 'content overflows into footer: y=%s' % y
footer()
c.save()
print('written files/epoxygrout-tds.pdf')
