# -*- coding: utf-8 -*-
"""IronLock SDS — house style (geometry measured from files/deepstick-sds.pdf)."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth

# ฟอนต์ไทย Sarabun (เหมือน deepstick-sds) — ดึงจาก Google Fonts บน GitHub ถ้ายังไม่มีในเครื่อง
import os, urllib.request
FONTDIR = os.environ.get('LP_FONTDIR', '/tmp/lp-fonts')
os.makedirs(FONTDIR, exist_ok=True)
for _v in ('Regular', 'Bold'):
    _p = os.path.join(FONTDIR, f'Sarabun-{_v}.ttf')
    if not os.path.exists(_p):
        urllib.request.urlretrieve(
            f'https://raw.githubusercontent.com/google/fonts/main/ofl/sarabun/Sarabun-{_v}.ttf', _p)
pdfmetrics.registerFont(TTFont('Sarabun', os.path.join(FONTDIR, 'Sarabun-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Sarabun-Bold', os.path.join(FONTDIR, 'Sarabun-Bold.ttf')))

W, H = A4
COLS = [(57.0, 281.7), (313.6, 538.3)]
RULE = (0.862745, 0.862745, 0.839216)
FILL = (0.956863, 0.956863, 0.945098)
BODY, LEAD = 8.6, 11.4
HEAD = 10.5
PAD = 7.0
GAP = 14.1
TOP0 = 85.4
BOTTOM = 786.0

TITLE = 'Safety Data Sheet of IRONLOCK  \u00b7  Issue 1.0  \u00b7  July 2026'
DISC = ('\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e02\u0e49\u0e32\u0e07\u0e15\u0e49\u0e19\u0e08\u0e31\u0e14\u0e17\u0e33\u0e02\u0e36\u0e49\u0e19'
        '\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e41\u0e25\u0e30\u0e1b\u0e23\u0e30\u0e2a\u0e1a\u0e01\u0e32\u0e23\u0e13\u0e4c'
        '\u0e20\u0e32\u0e22\u0e43\u0e15\u0e49\u0e2a\u0e20\u0e32\u0e27\u0e30\u0e17\u0e35\u0e48\u0e04\u0e27\u0e1a\u0e04\u0e38\u0e21\u0e44\u0e14\u0e49 '
        '\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e08\u0e23\u0e34\u0e07\u0e2d\u0e32\u0e08\u0e41\u0e15\u0e01\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19'
        '\u0e15\u0e32\u0e21\u0e1e\u0e37\u0e49\u0e19\u0e1c\u0e34\u0e27\u0e41\u0e25\u0e30\u0e2a\u0e20\u0e32\u0e1e\u0e41\u0e27\u0e14\u0e25\u0e49\u0e2d\u0e21 '
        '\u0e0b\u0e36\u0e48\u0e07\u0e2d\u0e22\u0e39\u0e48\u0e19\u0e2d\u0e01\u0e40\u0e2b\u0e19\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e04\u0e27\u0e1a\u0e04\u0e38\u0e21'
        '\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17 '
        '\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e2f \u0e02\u0e2d\u0e2a\u0e07\u0e27\u0e19\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e4c'
        '\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25'
        '\u0e42\u0e14\u0e22\u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e41\u0e08\u0e49\u0e07\u0e43\u0e2b\u0e49\u0e17\u0e23\u0e32\u0e1a'
        '\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32')


def wrap(text, font, size, width):
    lines, line = [], ''
    for tok in text.split(' '):
        while stringWidth(tok, font, size) > width:      # ภาษาไทยไม่มีช่องว่าง ต้องตัดทีละตัวอักษร
            cut = len(tok)
            while cut > 1 and stringWidth(tok[:cut], font, size) > width:
                cut -= 1
            if line:
                lines.append(line); line = ''
            lines.append(tok[:cut]); tok = tok[cut:]
        cand = (line + ' ' + tok).strip()
        if stringWidth(cand, font, size) <= width:
            line = cand
        else:
            if line:
                lines.append(line)
            line = tok
    if line:
        lines.append(line)
    return lines


SECTIONS = [
 ('1. Identification (\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1c\u0e25\u0e34\u0e15\u0e20\u0e31\u0e13\u0e11\u0e4c)', [
   'Product Name: IronLock \u2014 single-component water-based anti-corrosive coating',
   'Product Use: Protective anti-corrosive coating for steel and galvanised steel (\u0e2a\u0e35\u0e01\u0e31\u0e19\u0e2a\u0e19\u0e34\u0e21\u0e2a\u0e39\u0e15\u0e23\u0e19\u0e49\u0e33\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e40\u0e2b\u0e25\u0e47\u0e01\u0e41\u0e25\u0e30\u0e40\u0e2b\u0e25\u0e47\u0e01\u0e0a\u0e38\u0e1a\u0e2a\u0e31\u0e07\u0e01\u0e30\u0e2a\u0e35)',
   'Manufacturer: \u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17 \u0e25\u0e39\u0e40\u0e0b\u0e2d\u0e19\u0e48\u0e32 \u0e08\u0e33\u0e01\u0e31\u0e14 (Lucerna Co., Ltd.)',
   'Address: 23 \u0e16.\u0e2a\u0e38\u0e23\u0e34\u0e22\u0e32\u0e15\u0e23\u0e4c \u0e0b\u0e2d\u0e22 4 \u0e15.\u0e43\u0e19\u0e40\u0e21\u0e37\u0e2d\u0e07 \u0e2d.\u0e40\u0e21\u0e37\u0e2d\u0e07 \u0e08.\u0e2d\u0e38\u0e1a\u0e25\u0e23\u0e32\u0e0a\u0e18\u0e32\u0e19\u0e35 34000',
   'Contact: 097-079-9547, 097-079-6583 | LINE: @lucerna | www.lucernapro.com',
 ]),
 ('2. Hazards Identification (\u0e04\u0e27\u0e32\u0e21\u0e40\u0e1b\u0e47\u0e19\u0e2d\u0e31\u0e19\u0e15\u0e23\u0e32\u0e22)', [
   'Flammability: Not classified as flammable \u2014 water-based, no flash point. (\u0e2a\u0e39\u0e15\u0e23\u0e19\u0e49\u0e33 \u0e44\u0e21\u0e48\u0e15\u0e34\u0e14\u0e44\u0e1f \u0e44\u0e21\u0e48\u0e21\u0e35\u0e08\u0e38\u0e14\u0e27\u0e32\u0e1a\u0e44\u0e1f)',
   'Skin / Eyes: May cause mild irritation on prolonged or repeated contact. (\u0e2a\u0e31\u0e21\u0e1c\u0e31\u0e2a\u0e19\u0e32\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e0b\u0e49\u0e33\u0e46 \u0e2d\u0e32\u0e08\u0e23\u0e30\u0e04\u0e32\u0e22\u0e40\u0e04\u0e37\u0e2d\u0e07\u0e1c\u0e34\u0e27\u0e2b\u0e19\u0e31\u0e07\u0e41\u0e25\u0e30\u0e14\u0e27\u0e07\u0e15\u0e32)',
   'Sensitisation: Contains in-can preservatives as is normal for waterborne coatings; may produce an allergic skin reaction in sensitised individuals. (\u0e21\u0e35\u0e2a\u0e32\u0e23\u0e01\u0e31\u0e19\u0e40\u0e2a\u0e35\u0e22\u0e43\u0e19\u0e01\u0e23\u0e30\u0e1b\u0e38\u0e01\u0e15\u0e32\u0e21\u0e1b\u0e01\u0e15\u0e34\u0e02\u0e2d\u0e07\u0e2a\u0e35\u0e2a\u0e39\u0e15\u0e23\u0e19\u0e49\u0e33 \u0e1c\u0e39\u0e49\u0e17\u0e35\u0e48\u0e41\u0e1e\u0e49\u0e07\u0e48\u0e32\u0e22\u0e2d\u0e32\u0e08\u0e40\u0e01\u0e34\u0e14\u0e2d\u0e32\u0e01\u0e32\u0e23\u0e41\u0e1e\u0e49\u0e17\u0e32\u0e07\u0e1c\u0e34\u0e27\u0e2b\u0e19\u0e31\u0e07)',
   'Spray mist: Do not breathe spray mist when applying by spray gun. (\u0e2b\u0e49\u0e32\u0e21\u0e2a\u0e39\u0e14\u0e14\u0e21\u0e25\u0e30\u0e2d\u0e2d\u0e07\u0e02\u0e13\u0e30\u0e1e\u0e48\u0e19)',
   'Cured film: Inert and safe to handle. (\u0e1f\u0e34\u0e25\u0e4c\u0e21\u0e17\u0e35\u0e48\u0e41\u0e2b\u0e49\u0e07\u0e2a\u0e19\u0e34\u0e17\u0e41\u0e25\u0e49\u0e27\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22)',
 ]),
 ('3. Composition (\u0e2a\u0e48\u0e27\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e2d\u0e1a)', [
   'Waterborne binder system, active anti-corrosive pigment, extenders and colour pigments dispersed in water.',
   'The anti-corrosive pigment used is not classified as toxic and is not classified as hazardous to the aquatic environment.',
   'Note: Specific chemical identities are withheld as a trade secret. (\u0e02\u0e2d\u0e2a\u0e07\u0e27\u0e19\u0e0a\u0e37\u0e48\u0e2d\u0e2a\u0e32\u0e23\u0e40\u0e04\u0e21\u0e35\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e40\u0e1b\u0e47\u0e19\u0e04\u0e27\u0e32\u0e21\u0e25\u0e31\u0e1a\u0e17\u0e32\u0e07\u0e01\u0e32\u0e23\u0e04\u0e49\u0e32)',
 ]),
 ('4. First Aid (\u0e01\u0e32\u0e23\u0e1b\u0e10\u0e21\u0e1e\u0e22\u0e32\u0e1a\u0e32\u0e25)', [
   'Eyes: Rinse with clean water for at least 15 minutes; seek medical advice if irritation persists. (\u0e25\u0e49\u0e32\u0e07\u0e19\u0e49\u0e33\u0e2a\u0e30\u0e2d\u0e32\u0e14\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22 15 \u0e19\u0e32\u0e17\u0e35)',
   'Skin: Wash with soap and water; remove contaminated clothing. (\u0e25\u0e49\u0e32\u0e07\u0e14\u0e49\u0e27\u0e22\u0e2a\u0e1a\u0e39\u0e48\u0e41\u0e25\u0e30\u0e19\u0e49\u0e33)',
   'Inhalation: Move to fresh air. (\u0e19\u0e33\u0e2d\u0e2d\u0e01\u0e2a\u0e39\u0e48\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e01\u0e32\u0e28\u0e16\u0e48\u0e32\u0e22\u0e40\u0e17)',
   'Ingestion: Rinse mouth, do not induce vomiting, seek medical advice. (\u0e1a\u0e49\u0e27\u0e19\u0e1b\u0e32\u0e01 \u0e2b\u0e49\u0e32\u0e21\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e2d\u0e32\u0e40\u0e08\u0e35\u0e22\u0e19 \u0e1e\u0e1a\u0e41\u0e1e\u0e17\u0e22\u0e4c)',
 ]),
 ('5. Fire-Fighting (\u0e01\u0e32\u0e23\u0e14\u0e31\u0e1a\u0e40\u0e1e\u0e25\u0e34\u0e07)', [
   'The wet product does not support combustion. In a surrounding fire use water spray, foam, CO2 or dry chemical.',
   'Dried film will burn and produces dense smoke \u2014 use self-contained breathing apparatus. (\u0e1f\u0e34\u0e25\u0e4c\u0e21\u0e17\u0e35\u0e48\u0e41\u0e2b\u0e49\u0e07\u0e41\u0e25\u0e49\u0e27\u0e15\u0e34\u0e14\u0e44\u0e1f\u0e44\u0e14\u0e49\u0e41\u0e25\u0e30\u0e40\u0e01\u0e34\u0e14\u0e04\u0e27\u0e31\u0e19\u0e2b\u0e19\u0e32)',
 ]),
 ('6. Accidental Release (\u0e01\u0e23\u0e13\u0e35\u0e2b\u0e01\u0e23\u0e31\u0e48\u0e27\u0e44\u0e2b\u0e25)', [
   'Contain the spill; absorb with sand, earth or absorbent material and collect for disposal. Wet residues on hard surfaces may be wiped up with water.',
   'Do not wash into drains or waterways. (\u0e2b\u0e49\u0e32\u0e21\u0e17\u0e34\u0e49\u0e07\u0e25\u0e07\u0e17\u0e48\u0e2d\u0e23\u0e30\u0e1a\u0e32\u0e22\u0e19\u0e49\u0e33\u0e2b\u0e23\u0e37\u0e2d\u0e41\u0e2b\u0e25\u0e48\u0e07\u0e19\u0e49\u0e33)',
 ]),
 ('7. Handling & Storage (\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e41\u0e25\u0e30\u0e40\u0e01\u0e47\u0e1a\u0e23\u0e31\u0e01\u0e29\u0e32)', [
   'Handling: Ventilate the working area, particularly when spraying. Avoid prolonged skin contact. Close the lid immediately after use. (\u0e23\u0e30\u0e1a\u0e32\u0e22\u0e2d\u0e32\u0e01\u0e32\u0e28\u0e43\u0e2b\u0e49\u0e14\u0e35 \u0e43\u0e0a\u0e49\u0e40\u0e2a\u0e23\u0e47\u0e08\u0e1b\u0e34\u0e14\u0e1d\u0e32\u0e17\u0e31\u0e19\u0e17\u0e35)',
   'Storage: Store sealed in the original container, dry, 10\u201330 \u00b0C, out of direct sunlight. Protect from frost \u2014 do not allow to freeze. (\u0e40\u0e01\u0e47\u0e1a\u0e43\u0e19\u0e20\u0e32\u0e0a\u0e19\u0e30\u0e1b\u0e34\u0e14\u0e2a\u0e19\u0e34\u0e17 \u0e17\u0e35\u0e48\u0e41\u0e2b\u0e49\u0e07 10\u201330 \u00b0C \u0e2b\u0e49\u0e32\u0e21\u0e43\u0e2b\u0e49\u0e41\u0e02\u0e47\u0e07\u0e15\u0e31\u0e27)',
   'Shelf life: 12 months unopened. (\u0e2d\u0e32\u0e22\u0e38\u0e01\u0e32\u0e23\u0e40\u0e01\u0e47\u0e1a 12 \u0e40\u0e14\u0e37\u0e2d\u0e19)',
 ]),
 ('8. Exposure Control / PPE (\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c\u0e1b\u0e49\u0e2d\u0e07\u0e01\u0e31\u0e19)', [
   'Eyes: Safety glasses or goggles. (\u0e41\u0e27\u0e48\u0e19\u0e15\u0e32\u0e19\u0e34\u0e23\u0e20\u0e31\u0e22)',
   'Skin: Protective gloves. (\u0e16\u0e38\u0e07\u0e21\u0e37\u0e2d)',
   'Respiratory: Not normally required for brush or roller application in a ventilated area. Wear a particulate mask when spraying. (\u0e07\u0e32\u0e19\u0e41\u0e1b\u0e23\u0e07-\u0e25\u0e39\u0e01\u0e01\u0e25\u0e34\u0e49\u0e07\u0e44\u0e21\u0e48\u0e08\u0e33\u0e40\u0e1b\u0e47\u0e19 \u0e07\u0e32\u0e19\u0e1e\u0e48\u0e19\u0e43\u0e2b\u0e49\u0e2a\u0e27\u0e21\u0e2b\u0e19\u0e49\u0e32\u0e01\u0e32\u0e01\u0e01\u0e31\u0e19\u0e25\u0e30\u0e2d\u0e2d\u0e07)',
 ]),
 ('9. Physical & Chemical Properties (\u0e04\u0e38\u0e13\u0e2a\u0e21\u0e1a\u0e31\u0e15\u0e34)', [
   'Appearance: Liquid coating \u2014 White, Grey or Black.',
   'Odour: Low, characteristic. (\u0e01\u0e25\u0e34\u0e48\u0e19\u0e2d\u0e48\u0e2d\u0e19)',
   'Solubility: Miscible with water while wet; water-resistant once cured.',
   'Flash point: None \u2014 water-based.',
   'Density, pH, VOC content, viscosity: No data available for this issue.',
 ]),
 ('10. Stability & Reactivity (\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e16\u0e35\u0e22\u0e23)', [
   'Stable under the recommended storage and handling conditions.',
   'Avoid freezing, strong acids and strong oxidising agents. (\u0e2b\u0e25\u0e35\u0e01\u0e40\u0e25\u0e35\u0e48\u0e22\u0e07\u0e01\u0e32\u0e23\u0e41\u0e0a\u0e48\u0e41\u0e02\u0e47\u0e07 \u0e01\u0e23\u0e14\u0e41\u0e01\u0e48 \u0e41\u0e25\u0e30\u0e2a\u0e32\u0e23\u0e2d\u0e2d\u0e01\u0e0b\u0e34\u0e44\u0e14\u0e2a\u0e4c\u0e41\u0e23\u0e07)',
 ]),
 ('11. Toxicology (\u0e1e\u0e34\u0e29\u0e27\u0e34\u0e17\u0e22\u0e32)', [
   'Mild skin and eye irritant on prolonged contact. Preservatives present in the wet product may cause an allergic skin reaction in sensitised individuals.',
   'No data available on chronic effects of the mixture. Cured film is inert. (\u0e1f\u0e34\u0e25\u0e4c\u0e21\u0e17\u0e35\u0e48\u0e41\u0e2b\u0e49\u0e07\u0e2a\u0e19\u0e34\u0e17\u0e41\u0e25\u0e49\u0e27\u0e44\u0e21\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e2d\u0e31\u0e19\u0e15\u0e23\u0e32\u0e22)',
 ]),
 ('12. Environmental (\u0e2a\u0e34\u0e48\u0e07\u0e41\u0e27\u0e14\u0e25\u0e49\u0e2d\u0e21)', [
   'The anti-corrosive pigment used is not classified as hazardous to the aquatic environment.',
   'Wet product must nevertheless never be released into waterways or drains. (\u0e2b\u0e49\u0e32\u0e21\u0e1b\u0e25\u0e48\u0e2d\u0e22\u0e2a\u0e35\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e41\u0e2b\u0e49\u0e07\u0e25\u0e07\u0e41\u0e2b\u0e25\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e23\u0e37\u0e2d\u0e17\u0e48\u0e2d\u0e23\u0e30\u0e1a\u0e32\u0e22\u0e19\u0e49\u0e33)',
 ]),
 ('13. Disposal (\u0e01\u0e32\u0e23\u0e01\u0e33\u0e08\u0e31\u0e14)', [
   'Allow residues to dry fully before disposal. Dispose of in accordance with local regulations; do not pour into drains. (\u0e1b\u0e25\u0e48\u0e2d\u0e22\u0e40\u0e28\u0e29\u0e2a\u0e35\u0e43\u0e2b\u0e49\u0e41\u0e2b\u0e49\u0e07\u0e2a\u0e19\u0e34\u0e17\u0e01\u0e48\u0e2d\u0e19\u0e17\u0e34\u0e49\u0e07\u0e15\u0e32\u0e21\u0e02\u0e49\u0e2d\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e17\u0e49\u0e2d\u0e07\u0e16\u0e34\u0e48\u0e19)',
 ]),
 ('14. Transport (\u0e01\u0e32\u0e23\u0e02\u0e19\u0e2a\u0e48\u0e07)', [
   'Not classified as dangerous goods. (\u0e44\u0e21\u0e48\u0e08\u0e31\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e2d\u0e31\u0e19\u0e15\u0e23\u0e32\u0e22\u0e43\u0e19\u0e01\u0e32\u0e23\u0e02\u0e19\u0e2a\u0e48\u0e07)',
 ]),
 ('15. Regulations (\u0e02\u0e49\u0e2d\u0e01\u0e33\u0e2b\u0e19\u0e14)', [
   'Complies with Thai safety & labeling laws. (\u0e40\u0e1b\u0e47\u0e19\u0e44\u0e1b\u0e15\u0e32\u0e21\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22\u0e41\u0e25\u0e30\u0e09\u0e25\u0e32\u0e01\u0e02\u0e2d\u0e07\u0e44\u0e17\u0e22)',
 ]),
 ('16. Other (\u0e2d\u0e37\u0e48\u0e19\u0e46)', [
   'Prepared by Lucerna Co., Ltd. \u00b7 Issue 1.0 \u2014 July 2026 (first issue).',
   'Physical property values shown as "no data available" will be added in a later issue.',
   'For guidance only, not a legal guarantee.',
 ]),
]


def measure(sec):
    title, items = sec
    w = COLS[0][1] - COLS[0][0] - 2 * PAD
    h = PAD + HEAD + 4
    for it in items:
        h += LEAD * len(wrap(it, 'Sarabun', BODY, w)) + 2.5
    return h + PAD - 2.5


c = canvas.Canvas(os.environ.get('LP_OUT', 'files/ironlock-sds.pdf'), pagesize=A4)
c.setTitle('LucernaPro IronLock \u2014 Safety Data Sheet')


def page_header():
    c.setFont('Helvetica-Bold', 14); c.setFillGray(0)
    c.drawCentredString(W / 2, H - (34.3 + 11.0), 'LUCERNAPRO')
    c.setFont('Sarabun-Bold', HEAD)
    c.drawCentredString(W / 2, H - (53.3 + 8.4), TITLE)
    c.setStrokeColorRGB(*RULE); c.setLineWidth(0.8)
    c.line(51.0, H - 68.0, 544.3, H - 68.0)


def page_footer():
    c.setFont('Sarabun', 6.4); c.setFillGray(0.25)
    for i, ln in enumerate(wrap(DISC, 'Sarabun', 6.4, 493.3)):
        c.drawCentredString(W / 2, H - (800.1 + i * 8.0), ln)
    c.setFont('Sarabun', 6.4); c.setFillGray(0.35)
    c.drawCentredString(W / 2, H - 818.0, 'www.lucernapro.com')


def draw(sec, x0, x1, top, h):
    title, items = sec
    c.setFillColorRGB(*FILL); c.setStrokeColorRGB(*RULE); c.setLineWidth(0.6)
    c.rect(x0, H - (top + h), x1 - x0, h, stroke=1, fill=1)
    y = top + PAD + HEAD - 2.0
    c.setFillGray(0); c.setFont('Sarabun-Bold', HEAD)
    c.drawString(x0 + PAD, H - y, title)
    y += 6.0
    c.setFont('Sarabun', BODY)
    for it in items:
        for ln in wrap(it, 'Sarabun', BODY, x1 - x0 - 2 * PAD):
            y += LEAD
            c.drawString(x0 + PAD, H - y, ln)
        y += 2.5


# แบ่งคอลัมน์แบบกำหนดเอง เพื่อให้ทั้ง 4 คอลัมน์ (2 หน้า) สูงใกล้เคียงกัน ไม่มีคอลัมน์โหรงเหรง
COLUMN_SPLIT = [range(0, 3), range(3, 7), range(7, 11), range(11, 16)]
page_header()
for ci, rng in enumerate(COLUMN_SPLIT):
    if ci == 2:
        page_footer(); c.showPage(); page_header()
    x0, x1 = COLS[ci % 2]
    top = TOP0
    for i in rng:
        h = measure(SECTIONS[i])
        assert top + h <= BOTTOM, (i, top + h)
        draw(SECTIONS[i], x0, x1, top, h)
        top += h + GAP
page_footer()
c.showPage(); c.save()
print('written')
