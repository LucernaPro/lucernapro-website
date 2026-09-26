# -*- coding: utf-8 -*-
"""PureBreeze TDS — house style, EN page + TH page in one PDF. Issue 1.0
(Sep 2026): translated from the raw-material manufacturer's Chinese TDS for the
air-conditioner coil-fin grade (KT01/FBq301); values are the manufacturer's typical values. Site doctrine: no raw
material codes or supplier grade names published."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

_F = os.path.join(os.path.dirname(__file__), 'fonts')
pdfmetrics.registerFont(TTFont('Sarabun', os.path.join(_F, 'Sarabun-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Sarabun-Bold', os.path.join(_F, 'Sarabun-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Sarabun-Italic', os.path.join(_F, 'Sarabun-Italic.ttf')))

W, H = A4
L, R = 45.4, 549.9
CW = R - L
ORANGE = (0.847059, 0.341176, 0.109804)
BAR    = (0.937255, 0.937255, 0.925490)
RULE   = (0.862745, 0.862745, 0.839216)
BODY, LEAD = 7.2, 9.4
LABEL_W = 118.0
FR, FB, FI = 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique'
JUSTIFY = True

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/purebreeze-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro PureBreeze — Technical Data Sheet')


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


def header(title, issue_line, tagline):
    c.setFont('Helvetica-Bold', 15); c.setFillGray(0)
    c.drawString(L, base(46.5, 15), 'LUCERNAPRO')
    c.setFont(FB, 12)
    c.drawRightString(R, base(46.0, 12), title)
    c.setFont(FR, 7.6)
    c.drawString(L, base(56.0, 7.6), issue_line)
    c.drawRightString(R, base(56.0, 7.6), tagline)
    c.setStrokeColorRGB(*ORANGE); c.setLineWidth(1.6)
    c.line(L, H - 63.0, R, H - 63.0)


def footer(foot, disc_size=6.4, disc_lead=7.8):
    c.setFont(FI, disc_size); c.setFillGray(0.25)
    for i, ln in enumerate(wrap(foot, FI, disc_size, CW)):
        c.drawString(L, base(786.0 + i * disc_lead, disc_size), ln)
    c.setFont('Helvetica', 7.2); c.setFillGray(0)
    c.drawString(L, base(806.0, 7.2), 'Lucerna Co., Ltd. \u00b7 23 Suriyat Road Soi 4, Nai Mueang, Mueang, Ubon Ratchathani 34000, Thailand')
    c.drawString(L, base(815.0, 7.2), 'Tel 097-079-9547, 097-079-6583 \u00b7 Office 062-005-7933 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com/purebreeze')


EN_FOOT = ('Given in good faith on the basis of our current knowledge and applying to the product as supplied. '
           'Site conditions, substrate condition and workmanship are outside our control and no warranty of result '
           'is given or implied; users should satisfy themselves that the product suits the intended use, by trial '
           'on site if necessary.')
TH_FOOT = ('\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e19\u0e35\u0e49\u0e43\u0e2b\u0e49\u0e44\u0e27\u0e49\u0e42\u0e14\u0e22\u0e2a\u0e38\u0e08\u0e23\u0e34\u0e15\u0e15\u0e32\u0e21\u0e04\u0e27\u0e32\u0e21\u0e23\u0e39\u0e49\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e41\u0e25\u0e30\u0e43\u0e0a\u0e49\u0e01\u0e31\u0e1a\u0e1c\u0e25\u0e34\u0e15\u0e20\u0e31\u0e13\u0e11\u0e4c\u0e15\u0e32\u0e21\u0e2a\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e08\u0e31\u0e14\u0e2a\u0e48\u0e07 \u0e2a\u0e20\u0e32\u0e1e\u0e2b\u0e19\u0e49\u0e32\u0e07\u0e32\u0e19 \u0e2a\u0e20\u0e32\u0e1e\u0e1e\u0e37\u0e49\u0e19\u0e1c\u0e34\u0e27 \u0e41\u0e25\u0e30\u0e1d\u0e35\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19\u0e2d\u0e22\u0e39\u0e48\u0e19\u0e2d\u0e01\u0e40\u0e2b\u0e19\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e04\u0e27\u0e1a\u0e04\u0e38\u0e21\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e25\u0e31\u0e1e\u0e18\u0e4c\u0e44\u0e21\u0e48\u0e27\u0e48\u0e32\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e42\u0e14\u0e22\u0e19\u0e31\u0e22 \u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e04\u0e27\u0e23\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e08\u0e23\u0e34\u0e07 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e27\u0e48\u0e32\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e02\u0e2d\u0e07\u0e15\u0e19')



def section(title, gap=3.0):
    global y
    y += gap
    c.setFillColorRGB(*BAR)
    c.rect(L, H - (y + 11.5), CW, 11.5, stroke=0, fill=1)
    c.setFillGray(0); c.setFont(FB, 8.2)
    c.drawString(L + 4.0, base(y + 10.0, 8.2), title)
    y += 11.5


def para(text, gap=6.4, indent=2.0, width=None):
    global y
    y += gap
    c.setFillGray(0)
    w = (width or CW) - indent
    lines = wrap(text, FR, BODY, w)
    for i, ln in enumerate(lines):
        nsp = ln.count(' ')
        if JUSTIFY and i < len(lines) - 1 and nsp > 0:
            extra = (w - stringWidth(ln, FR, BODY)) / nsp
            t = c.beginText(L + indent, base(y + BODY, BODY))
            t.setFont(FR, BODY)
            t.setWordSpace(extra)
            t.textOut(ln)
            c.drawText(t)
        else:
            c.setFont(FR, BODY)
            c.drawString(L + indent, base(y + BODY, BODY), ln)
        y += LEAD
    y -= LEAD
    y += BODY + 0.6


def kv(rows, gap=5.0):
    global y
    y += gap
    for label, value in rows:
        lines = wrap(value, FR, BODY, CW - LABEL_W - 2.0)
        c.setFillGray(0); c.setFont(FR, BODY)
        for j, lln in enumerate(wrap(label, FR, BODY, LABEL_W - 6)):
            c.drawString(L + 2.0, base(y + BODY + j * LEAD, BODY), lln)
        for i, ln in enumerate(lines):
            c.drawString(L + LABEL_W, base(y + BODY + i * LEAD, BODY), ln)
        y += LEAD * len(lines) + 2.6
        c.setStrokeColorRGB(*RULE); c.setLineWidth(0.35)
        c.line(L, H - y, R, H - y)
        y += 1.4
    y += 1.0


def bullet(text, gap=3.4):
    global y
    y += gap
    c.setFillGray(0); c.setFont(FR, BODY)
    c.drawString(L + 3.0, base(y + BODY, BODY), '\u2022')
    lines = wrap(text, FR, BODY, CW - 14.0)
    for i, ln in enumerate(lines):
        c.drawString(L + 12.0, base(y + BODY + i * LEAD, BODY), ln)
    y += LEAD * (len(lines) - 1) + BODY



header('PureBreeze',
       'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  September 2026  \u00b7  Page 1 of 2',
       'Self-cleaning anti-static antibacterial nano coating for A/C coil fins')
y = 67.0

section('PRODUCT DESCRIPTION', gap=4.0)
para('LucernaPro PureBreeze is a single-component, alcohol- and water-borne nano coating for the aluminium fins '
     'of air-conditioner evaporator and condenser coils and for other metal and plastic parts of air-handling '
     'equipment. It leaves a transparent, inorganic film only nanometres thick that makes the fin surface '
     'super-hydrophilic: the condensate that forms on a running evaporator spreads into a sheet instead of beading, '
     'slides in under settled dust and carries it down to the drain pan, so the coil rinses its own fins in '
     'operation and dust builds up far more slowly. The film dissipates static charge so airborne dust is not '
     'attracted to the fins, carries a nano antibacterial layer that inhibits bacteria and mould on the '
     'permanently damp fin surface, and is thin enough to have no effect on heat exchange. It is sprayed thin, in '
     'a single coat, at low pressure and cures at room temperature. Being inorganic, the cured film in principle '
     'does not yellow or age.')

section('KEY DATA')
kv([
    ('Type',              'Single-component (1K) nano self-cleaning coating, alcohol- and water-borne, supplied '
                          'ready to use \u2014 do not dilute'),
    ('Appearance',        'Pale blue to pale white translucent liquid with a slight ethanol odour'),
    ('Solids',            '10 \u00b1 2 % by weight (DIN EN ISO 3251, 1 h / 120\u00b0C)'),
    ('Density (20\u00b0C)', '0.88\u20130.92 g/cm\u00b3 (DIN EN ISO 2811-2)'),
    ('pH',                '4.0\u20136.0 (DIN ISO 976)'),
    ('Flash point',       '26.5\u00b0C closed cup (ISO 13736) \u2014 flammable liquid'),
    ('Composition',       'Amorphous silica, silicates and inorganic oxides bound with a special resin and organic '
                          'polymer, plus tin oxide; carrier: alcohols and water'),
    ('Cured film',        'Water contact angle \u2264 7\u00b0 (super-hydrophilic) \u00b7 surface resistance 10^9 ohm '
                          '(anti-static) \u00b7 pencil hardness 6H \u00b7 cross-cut adhesion grade 0 '
                          '(GB/T 9286-1998, GB/T 31815-2015) \u00b7 acid resistance: no visible cracking or '
                          'blistering \u00b7 visible-light transmittance on glass 92.7 %'),
    ('Antibacterial',     'E. coli and S. aureus inhibited > 99 % after 24 h contact (GB 21551.2-2010 App. A); '
                          'mould-proof grade 0 against 5 standard strains (App. C) \u2014 Guangdong Detection Center '
                          'of Microbiology, report 2020SPS942R01D'),
    ('Substrates',        'Aluminium coil fins, metal and plastic parts of air-conditioning and heat-exchange '
                          'equipment. Surfaces that repel alcohol cannot be coated unless first plasma- or '
                          'corona-treated. Degrease oily surfaces before application.'),
    ('Application',       'Spray. HVLP gun, 1.0\u20131.2 mm nozzle, about 0.2 MPa air pressure; or any sprayer that '
                          'gives a fine mist at low pressure. High pressure flattens fins and bounces the liquid off.'),
    ('Consumption',       'About 30\u201350 ml/m\u00b2 depending on spray method and substrate (manufacturer figure). '
                          'The indoor coil of a 12,000 BTU wall split takes about 20 ml as a thin low-pressure '
                          'mist in our own measured application (indoor unit only).'),
    ('Coats',             'One \u2014 a single thin, even coat; do not spray to the point of running'),
    ('Tack-free',         'About 5 minutes at room temperature'),
    ('Hardening',         'The surface hardens immediately on application; hardened through in about 1 hour at '
                          'room temperature \u2014 or by heat, 50\u00b0C \u2248 2 min / 70\u00b0C \u2248 1 min. Keep water '
                          'off the film until then or it will show water marks.'),
    ('Full cure',         'About 6 hours in warm weather, up to 20 hours in cool conditions'),
    ('Storage',           '\u221210 to 45\u00b0C, container tightly closed, in a cool shaded place out of direct '
                          'sunlight and away from sparks and flame. Keep out of reach of children.'),
    ('Shelf life',        '12 months from the date of manufacture unopened. Use up soon after opening; beyond '
                          '12 months, test performance before use.'),
    ('Packaging',         '100 g \u00b7 500 g \u00b7 1 kg'),
])

section('NOTE ON VALUES')
para('Typical values from the manufacturer\u2019s testing of the coating material, given as guidance and not as '
     'a specification. Drying and cure times depend on temperature, humidity and airflow, and consumption on '
     'the sprayer, pressure and fin geometry. Where the product label differs from this sheet, the label governs. '
     'The microbial test report and the Safety Data Sheet are available on the product page.')

section('APPLICATION NOTES')
bullet('Switch off and isolate the unit. Wash the coil as usual with coil cleaner and low-pressure water, rinse '
       'every trace of cleaner off, and blow or air-dry until the fins are completely dry. The coating cannot bond '
       'over dust, cleaner residue or moisture.', gap=5.0)
bullet('Thin is everything. One fine, even mist over the whole fin pack. Liquid that runs and pools at the bottom '
       'of the coil is wasted and does nothing.')
bullet('Keep water off until hardened. Do not switch the unit on or let condensate form until the film has '
       'hardened through (about 1 hour); water on an unhardened film leaves permanent marks.')
bullet('The coating reduces the adhesion of new dust and dirt; it does not remove what is already bonded, and it '
       'does not replace filter washing. Mould or slime in the drain pan and blower must be cleaned out separately.')
bullet('Aftercare. At the next cleaning try low-pressure plain water first. Do not scrub the fins with hard '
       'brushes. If a cleaner is needed, use a neutral or mildly acidic one; alkaline coil cleaners of pH 11 and '
       'above destroy the coating and must not be used on a coated coil.')
bullet('Recoat after every full wash with coil cleaner and pressure water, once the fins are dry \u2014 such a wash '
       'removes part of the film with the dirt.')

section('HEALTH AND SAFETY')
para('Flammable liquid and vapour (flash point 26.5\u00b0C) with an ethanol-type odour; the mixture also contains '
     'n-propanol and methanol. Keep away from heat, sparks, open flames and hot surfaces; no smoking; switch the '
     'unit off and isolate the power before spraying. Use only with good ventilation and wear an organic-vapour '
     'respirator when spraying, safety glasses and gloves \u2014 causes serious eye damage; if in eyes, rinse '
     'cautiously with water for several minutes and seek medical attention. Vapour may cause drowsiness or '
     'dizziness. Keep the container tightly closed and store cool, shaded and out of direct sunlight. Refer to '
     'the Safety Data Sheet before use.')

print('EN page final y =', y)
assert y < 778, 'EN content overflows into footer: y=%s' % y
footer(EN_FOOT)
c.showPage()

# ================= PAGE 2 — THAI =================
FR, FB, FI = 'Sarabun', 'Sarabun-Bold', 'Sarabun-Italic'
BODY, LEAD = 7.9, 10.3
LABEL_W = 100.0
JUSTIFY = False

header('PureBreeze',
       'TECHNICAL DATA SHEET \u00b7 Issue 1.0 \u00b7 กันยายน 2026 \u00b7 หน้า 2 จาก 2',
       'น้ำยาเคลือบนาโน Self-Cleaning กันฝุ่น ยับยั้งเชื้อ สำหรับฟินคอยล์แอร์')
y = 67.0

section('ข้อมูลผลิตภัณฑ์', gap=4.0)
para('PureBreeze ของ LucernaPro เป็นน้ำยาเคลือบนาโนชนิดส่วนผสมเดียว สูตรแอลกอฮอล์ผสมน้ำ สำหรับฟินอะลูมิเนียมของคอยล์เย็นและคอยล์ร้อน '
     'ของเครื่องปรับอากาศ และชิ้นส่วนโลหะหรือพลาสติกอื่นในระบบปรับอากาศ / เคลือบแล้วได้ฟิล์มใสระดับนาโนเมตร เป็นสารอนินทรีย์ '
     'ทำให้ผิวฟินเป็น super-hydrophilic น้ำที่กลั่นตัวบนคอยล์เย็นขณะทำงานจะแผ่เป็นแผ่นบางแทนที่จะเกาะเป็นหยด แทรกใต้ฝุ่นแล้วพาไหลลงถาดน้ำทิ้ง '
     'คอยล์จึงล้างฟินให้ตัวเองระหว่างทำงาน ฝุ่นสะสมช้าลงมาก / ฟิล์มสลายไฟฟ้าสถิตบนผิว ฝุ่นในอากาศไม่ถูกดูดมาเกาะ มีชั้นนาโนยับยั้งแบคทีเรียและรา '
     'บนผิวฟินที่เปียกชื้นตลอดเวลา และบางจนไม่มีผลต่อการแลกเปลี่ยนความร้อน / พ่นบางๆ รอบเดียวด้วยแรงดันต่ำ เซ็ตตัวที่อุณหภูมิห้อง '
     'และเพราะเป็นฟิล์มอนินทรีย์ โดยหลักการจึงไม่เหลืองและไม่เสื่อมตามอายุ')

section('ข้อมูลสำคัญ')
kv([
    ('ชนิด',              'น้ำยาเคลือบนาโน Self-Cleaning ส่วนผสมเดียว (1K) สูตรแอลกอฮอล์ผสมน้ำ พร้อมใช้ — ห้ามเจือจาง'),
    ('ลักษณะ',            'ของเหลวกึ่งใส สีฟ้าอ่อนถึงขาวอ่อน มีกลิ่นเอทานอลเล็กน้อย'),
    ('เนื้อสาร (solids)',  '10 ± 2 % โดยน้ำหนัก (DIN EN ISO 3251, 1 ชม. / 120°C)'),
    ('ความหนาแน่น (20°C)', '0.88–0.92 g/cm³ (DIN EN ISO 2811-2)'),
    ('pH',                '4.0–6.0 (DIN ISO 976)'),
    ('จุดวาบไฟ',           '26.5°C closed cup (ISO 13736) — ของเหลวไวไฟ'),
    ('องค์ประกอบ',         'ซิลิกาอสัณฐาน ซิลิเกต และออกไซด์อนินทรีย์ ยึดด้วยเรซินพิเศษและพอลิเมอร์อินทรีย์ ร่วมกับทินออกไซด์ / ตัวพา: แอลกอฮอล์และน้ำ'),
    ('ฟิล์มหลังเซ็ตตัว',    'มุมสัมผัสน้ำ ≤ 7° (super-hydrophilic) · ความต้านทานผิว 10⁹ Ω (กันไฟฟ้าสถิต) · ความแข็งดินสอ 6H · '
                          'การยึดเกาะ cross-cut เกรด 0 (GB/T 9286-1998, GB/T 31815-2015) · ทนกรด: ไม่พบรอยแตกหรือฟองพอง'),
    ('ยับยั้งเชื้อ',         'E. coli และ S. aureus ยับยั้งได้ > 99 % หลังสัมผัส 24 ชม. (GB 21551.2-2010 ภาคผนวก A) · ต้านเชื้อรา '
                          'ระดับ 0 กับเชื้อรามาตรฐาน 5 สายพันธุ์ (ภาคผนวก C) — Guangdong Detection Center of Microbiology '
                          'รายงานเลขที่ 2020SPS942R01D'),
    ('พื้นผิวที่ใช้ได้',      'ฟินอะลูมิเนียมของคอยล์ ชิ้นส่วนโลหะและพลาสติกของเครื่องปรับอากาศและอุปกรณ์แลกเปลี่ยนความร้อน / '
                          'ผิวที่ไม่รับแอลกอฮอล์เคลือบไม่ได้ เว้นแต่ปรับผิวด้วย plasma หรือ corona ก่อน / ผิวที่มีคราบน้ำมันต้องล้างไขมันออกก่อน'),
    ('วิธีทา',             'พ่น — กาพ่นสี HVLP หัว 1.0–1.2 มม. แรงดันลมราว 0.2 MPa หรือเครื่องพ่นใดก็ได้ที่ให้ละอองละเอียดที่แรงดันต่ำ '
                          'แรงดันสูงทำให้ฟินล้มและน้ำยาเด้งออก'),
    ('อัตราการใช้',         'ประมาณ 30–50 มล./ตร.ม. ขึ้นกับวิธีพ่นและพื้นผิว (ค่าของผู้ผลิตวัตถุดิบ) / คอยล์เย็นแอร์ผนัง 12,000 BTU หนึ่งตัว (เฉพาะตัวในห้อง) '
                          'จากการพ่นและชั่งจริงของเราใช้ราว 20 มล. เมื่อพ่นละอองบางแรงดันต่ำ'),
    ('จำนวนรอบ',          '1 รอบ — พ่นบางสม่ำเสมอรอบเดียว ไม่พ่นจนไหลย้อย'),
    ('แห้งสัมผัส',         'ประมาณ 5 นาที ที่อุณหภูมิห้อง'),
    ('การแข็งตัว',         'ผิวหน้าแข็งตัวทันทีหลังพ่น และแข็งตัวทั่วทั้งฟิล์มในราว 1 ชั่วโมงที่อุณหภูมิห้อง — หรือเร่งด้วยความร้อน 50°C ≈ 2 นาที / '
                          '70°C ≈ 1 นาที / ห้ามให้ฟิล์มโดนน้ำจนกว่าจะแข็งตัว ไม่เช่นนั้นจะเป็นรอยคราบน้ำ'),
    ('เซ็ตตัวเต็มที่',       'ประมาณ 6 ชั่วโมงในอากาศร้อน และนานถึง 20 ชั่วโมงในอากาศเย็น'),
    ('การเก็บรักษา',        '−10 ถึง 45°C ปิดฝาให้สนิท เก็บในที่เย็น ร่ม ไม่โดนแดดโดยตรง ห่างประกายไฟและเปลวไฟ เก็บพ้นมือเด็ก'),
    ('อายุผลิตภัณฑ์',       '12 เดือนนับจากวันผลิตเมื่อยังไม่เปิด เปิดแล้วควรใช้ให้หมดโดยเร็ว หากเกิน 12 เดือน ให้ทดสอบประสิทธิภาพก่อนใช้'),
    ('ขนาดบรรจุ',          '100 g · 500 g · 1 kg'),
])

section('หมายเหตุเรื่องค่าตัวเลข')
para('ค่าทั่วไปจากการทดสอบของผู้ผลิตวัตถุดิบเคลือบ ให้ไว้เป็นแนวทาง ไม่ใช่ข้อกำหนดผูกพัน — เวลาแห้งและเซ็ตตัวขึ้นกับอุณหภูมิ ความชื้น '
     'และการถ่ายเทอากาศ ส่วนอัตราการใช้ขึ้นกับเครื่องพ่น แรงดัน และรูปทรงฟิน หากฉลากผลิตภัณฑ์ระบุต่างจากเอกสารนี้ ให้ยึดฉลากเป็นหลัก / '
     'รายงานทดสอบจุลชีพและเอกสารข้อมูลความปลอดภัย ดาวน์โหลดได้ที่หน้าสินค้า')

section('ข้อควรรู้ในการใช้งาน')
bullet('ปิดเครื่องและตัดไฟก่อน ล้างคอยล์ตามปกติด้วยน้ำยาล้างคอยล์และน้ำแรงดันเบา ล้างคราบน้ำยาออกให้หมด แล้วเป่าหรือปล่อยให้ฟินแห้งสนิท '
       'น้ำยาไม่สามารถยึดเกาะบนฝุ่น คราบน้ำยาล้าง หรือความชื้นได้', gap=5.0)
bullet('บางคือหัวใจ — พ่นละอองละเอียดสม่ำเสมอรอบเดียวให้ทั่วแผงฟิน น้ำยาที่ไหลไปรวมกันด้านล่างคอยล์คือของที่เสียเปล่า')
bullet('ห้ามให้โดนน้ำจนกว่าจะแข็งตัว — อย่าเปิดเครื่องหรือปล่อยให้เกิดน้ำกลั่นตัวจนกว่าฟิล์มจะแข็งตัวทั่ว (ราว 1 ชั่วโมง) '
       'น้ำบนฟิล์มที่ยังไม่แข็งจะทิ้งรอยถาวร')
bullet('น้ำยาช่วยให้ฝุ่นและคราบใหม่เกาะติดยากขึ้น แต่ไม่ได้ลบคราบที่ฝังแน่นอยู่แล้ว และไม่ได้แทนการล้างแผ่นกรอง / '
       'ราหรือเมือกในถาดน้ำทิ้งและโบลเวอร์ต้องล้างออกต่างหาก')
bullet('การดูแลหลังเคลือบ — รอบล้างถัดไปลองน้ำเปล่าแรงดันเบาก่อน ไม่ขัดฟินด้วยแปรงแข็ง ถ้าจำเป็นต้องใช้น้ำยา เลือกสูตรกลางหรือกรดอ่อน / '
       'น้ำยาล้างคอยล์ที่เป็นด่าง pH 11 ขึ้นไปทำลายชั้นเคลือบ ห้ามใช้กับคอยล์ที่เคลือบแล้ว')
bullet('เคลือบซ้ำหลังการล้างใหญ่ด้วยน้ำยาล้างคอยล์และน้ำแรงดันทุกครั้ง เมื่อฟินแห้งแล้ว — การล้างแบบนั้นเอาฟิล์มออกไปพร้อมคราบส่วนหนึ่ง')

section('ความปลอดภัย')
para('ของเหลวและไอระเหยไวไฟ (จุดวาบไฟ 26.5°C) มีกลิ่นแบบเอทานอล ส่วนผสมมีโพรพานอลและเมทานอลด้วย — เก็บห่างความร้อน ประกายไฟ เปลวไฟ '
     'และผิวร้อน ห้ามสูบบุหรี่ ปิดเครื่องและตัดไฟก่อนพ่นทุกครั้ง / ทำงานในที่อากาศถ่ายเทดีเท่านั้น สวมหน้ากากกรองไอสารอินทรีย์ขณะพ่น '
     'แว่นตานิรภัย และถุงมือ — เป็นอันตรายร้ายแรงต่อดวงตา เข้าตาให้ล้างด้วยน้ำสะอาดต่อเนื่องหลายนาทีแล้วไปพบแพทย์ / '
     'ไอระเหยอาจทำให้ง่วงซึมหรือเวียนศีรษะ / ปิดฝาให้สนิท เก็บในที่เย็น ร่ม ไม่โดนแดด / อ่านเอกสารข้อมูลความปลอดภัย (SDS) ก่อนใช้งาน')

print('TH page final y =', y)
assert y < 778, 'TH content overflows into footer: y=%s' % y
footer(TH_FOOT, disc_size=6.8, disc_lead=8.4)
c.save()
print('written', os.environ.get('LP_OUT', 'files/purebreeze-tds.pdf'))
