# -*- coding: utf-8 -*-
"""FlexGrip TDS — house style (geometry per files/deepseal-tds.pdf lineage)."""
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/flexgrip-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro FlexGrip — Technical Data Sheet')


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


TOTAL = 2


def header(page):
    c.setFont('Helvetica-Bold', 15); c.setFillGray(0)
    c.drawString(L, base(48.5, 15), 'LUCERNAPRO')
    c.setFont('Helvetica-Bold', 13)
    c.drawRightString(R, base(48.0, 13), 'FlexGrip')
    c.setFont('Helvetica', 8.0)
    c.drawString(L, base(58.0, 8.0),
                 'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  July 2026  \u00b7  Page %d of %d' % (page, TOTAL))
    c.setFont('Helvetica', 8.5)
    c.drawRightString(R, base(58.1, 8.5), 'High-Strength Flexible Repair Adhesive')
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
            'Bond performance depends on substrate, surface condition, film thickness and clamping; values are '
            'typical guidance only and do not constitute a specification. Users must verify suitability for their '
            'intended application. Made in Thailand.')
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
para('FlexGrip is a one-component, clear, low-viscosity adhesive based on moisture-curing HydroCure Polymer '
     'technology powered by Covestro (Germany). The liquid cures by reacting with ambient humidity into a '
     'high-strength elastomer that combines rubber-like flexibility with rope-like resistance to tearing: the '
     'cured film stretches to 460 % of its original length while tensile strength climbs to 33 MPa at break. '
     'Because the bond flexes with the substrate instead of resisting it, FlexGrip survives the repeated flexing '
     'that cracks rigid adhesives \u2014 the property that allows it to replace stitching in shoe-sole repair, its '
     'original application. It bonds without abrasion or primer to rubber, leather, ceramic including glazed '
     'tile, wood, metal, brick and most plastics, withstands permanent water immersion after full cure, and is '
     'deliberately slow-setting so that parts can be repositioned without time pressure during assembly.')

section('KEY DATA')
kv([
    ('Chemistry', 'One-component moisture-curing HydroCure Polymer \u2014 powered by Covestro (Germany)'),
    ('Supplied form', 'Clear, water-thin liquid \u2014 ready to use; no mixing, no catalyst, no primer'),
    ('Cure mechanism', 'Reacts with humidity in the air and substrate; deliberately slow-setting to allow '
                       'repositioning during assembly'),
    ('Tensile strength', '33 MPa at break (cured free film, JIS K 6251) \u2014 approx. 330 kg per cm\u00b2 of '
                         'bond area'),
    ('Elongation at break', '460 % (cured free film, JIS K 6251)'),
    ('Tensile modulus', '8.7 MPa at 100 % elongation \u00b7 18 MPa at 300 % elongation'),
    ('Adhesion', 'Rubber, leather, ceramic incl. glazed tile, wood, metal, brick, most plastics \u2014 '
                 'no abrasion, no primer required'),
    ('Application', 'Thin, full-coverage film on one or both faces; parts held in firm, continuous contact '
                    'throughout the clamping period'),
    ('Surface set', 'Approx. 6 hours'),
    ('Clamping time', '12 hours minimum before releasing clamps, bands or tape'),
    ('Full cure', 'Approx. 40 hours before heavy service, hard use or water contact'),
    ('Water resistance', 'Permanent immersion after full cure; bonding to damp and underwater surfaces is '
                         'possible where unavoidable \u2014 a clean, dry surface gives the highest bond strength'),
    ('Chemical resistance', 'Cured film resists water, dilute acids and common solvents including thinner'),
    ('UV behaviour', 'Bond strength is unaffected by sunlight; exposed cured adhesive may yellow over time \u2014 '
                     'keep bond lines thin and closed with no squeeze-out (see notes)'),
    ('Colour', 'Clear'),
    ('Packaging', '200 g bottle \u00b7 20 ml trial sachet'),
    ('Storage', 'Sealed original container, dry and shaded, room temperature \u2014 do not refrigerate'),
    ('Shelf life', '12 months unopened \u2014 see storage notes; the opened bottle is moisture-sensitive'),
])

section('NOTE ON VALUES')
para('Mechanical values are measured on a fully cured free film to JIS K 6251 and describe the adhesive '
     'material itself. The strength of a finished joint additionally depends on surface cleanliness, film '
     'thickness, contact pressure during cure and the bonded area \u2014 a thin, fully wetted film held in firm '
     'contact for the full clamping period reaches the highest joint strength. Figures are typical guidance '
     'only and are not a specification.')

footer(); c.showPage(); header(2); y = 70.9

section('DESIGN PRINCIPLE \u2014 FLEXIBLE, NOT HARD')
para('A shoe sole flexes thousands of times a day. A rigid, glass-hard adhesive resists that movement, '
     'concentrates stress at the bond edge and fails by cracking within weeks \u2014 the standard failure mode '
     'of hot-melt and contact adhesives in sole repair. FlexGrip takes the opposite route: the cured film is a '
     'high-grade elastomer whose tensile strength rises as it stretches, from 8.7 MPa at 100 % strain to '
     '33 MPa at the 460 % break point. The bond therefore follows every flex of the substrate while the '
     'reserve of strength grows under load \u2014 which is why a glued repair can genuinely replace stitching, '
     'and why the same behaviour carries over to loose tiles, cracked fan blades, brick, battery casings and '
     'the many other repairs users have taken it to.')

section('APPLICATION NOTES')
bullets([
    'Clean the surfaces and let them dry: remove dust, soil and grease completely. No abrasion and no primer '
    'are required, but do not apply to a wet surface unless unavoidable \u2014 moisture on the bond face '
    'reduces performance for no benefit.',
    'Apply a THIN film over the full contact area, on one or both faces. Never apply a thick, oozing bead. If '
    'excess squeezes out of the joint, wipe it off immediately while still wet \u2014 once cured it cannot be '
    'removed by any solvent.',
    'Wide gaps and large voids (e.g. a debonded tile): lay a piece of tissue paper soaked in adhesive into the '
    'gap. This increases the bonded area, saves adhesive and produces a tighter repair.',
    'Clamp the parts in firm, continuous contact \u2014 rubber bands, tape, clamps or a dead weight, whatever '
    'is at hand. Parts can still be repositioned without hurry during the open time.',
    'Shoe repairs: always pack the shoe to shape with cloth or paper BEFORE binding or taping. Binding an '
    'empty shoe distorts it permanently \u2014 no adhesive can correct a shoe cured out of shape.',
    'Respect the clock: surface set approx. 6 hours; keep the joint clamped for a full 12 hours before '
    'releasing \u2014 releasing early is the leading cause of failed repairs; allow approx. 40 hours before '
    'heavy service or water contact.',
    'Adhesive on skin: scrub the hands with DRY detergent powder, without water, until the tack is gone, then '
    'rinse; repeated washing-up liquid is the fallback. Never clean skin with thinner or strong acid \u2014 '
    'hazardous to the skin, and the cured adhesive resists thinner in any case.',
    'Bottle care \u2014 humidity is the enemy: after use, wipe the bottle neck and cap clean (otherwise the cap '
    'seizes), tape over the neck as an extra air seal, then close the cap tightly. Store dry, shaded, at '
    'normal room temperature. Do not refrigerate.',
])

section('HEALTH & SAFETY')
para('Uncured adhesive contains an aromatic isocyanate prepolymer and may cause skin and respiratory '
     'sensitisation. Work in a ventilated area; wear protective gloves and eye protection; avoid skin and eye '
     'contact with uncured material. In case of eye contact, rinse immediately with plenty of clean water and '
     'seek medical attention. Fully cured material is inert. Keep out of reach of children. Refer to the '
     'Safety Data Sheet for full information.')

section('STORAGE')
para('Store in the original tightly sealed container in a dry, shaded place at normal room temperature. The '
     'product cures on contact with humid air \u2014 air entering an opened bottle is what spoils the adhesive '
     'before its time. Reseal immediately after use as described in the application notes. Do not refrigerate. '
     'Shelf life 12 months unopened.')

# ---------- close ----------
footer()
c.showPage(); c.save()
print('written')
