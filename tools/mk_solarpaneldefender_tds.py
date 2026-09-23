# -*- coding: utf-8 -*-
"""Solar Panel Defender TDS — house style, EN page + TH page in one PDF. Issue 1.0
(Sep 2026): translated from the raw-material manufacturer's Chinese TDS for the
PV-glass grade; values are the manufacturer's typical values. Site doctrine: no raw
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

c = canvas.Canvas(os.environ.get('LP_OUT', 'files/solarpaneldefender-tds.pdf'), pagesize=A4)
c.setTitle('LucernaPro Solar Panel Defender — Technical Data Sheet')


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
    c.drawString(L, base(815.0, 7.2), 'Tel 097-079-9547, 097-079-6583 \u00b7 Office 062-005-7933 \u00b7 Lucernapro@yahoo.com \u00b7 www.lucernapro.com/solarpaneldefender')


EN_FOOT = ('Given in good faith on the basis of our current knowledge and applying to the product as supplied. '
           'Site conditions, substrate condition and workmanship are outside our control and no warranty of result '
           'is given or implied; users should satisfy themselves that the product suits the intended use, by trial '
           'on site if necessary.')
TH_FOOT = ('\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e19\u0e35\u0e49\u0e43\u0e2b\u0e49\u0e44\u0e27\u0e49\u0e42\u0e14\u0e22\u0e2a\u0e38\u0e08\u0e23\u0e34\u0e15\u0e15\u0e32\u0e21\u0e04\u0e27\u0e32\u0e21\u0e23\u0e39\u0e49\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e41\u0e25\u0e30\u0e43\u0e0a\u0e49\u0e01\u0e31\u0e1a\u0e1c\u0e25\u0e34\u0e15\u0e20\u0e31\u0e13\u0e11\u0e4c\u0e15\u0e32\u0e21\u0e2a\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e08\u0e31\u0e14\u0e2a\u0e48\u0e07 \u0e2a\u0e20\u0e32\u0e1e\u0e2b\u0e19\u0e49\u0e32\u0e07\u0e32\u0e19 \u0e2a\u0e20\u0e32\u0e1e\u0e1e\u0e37\u0e49\u0e19\u0e1c\u0e34\u0e27 \u0e41\u0e25\u0e30\u0e1d\u0e35\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19\u0e2d\u0e22\u0e39\u0e48\u0e19\u0e2d\u0e01\u0e40\u0e2b\u0e19\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e04\u0e27\u0e1a\u0e04\u0e38\u0e21\u0e02\u0e2d\u0e07\u0e40\u0e23\u0e32 \u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e25\u0e31\u0e1e\u0e18\u0e4c\u0e44\u0e21\u0e48\u0e27\u0e48\u0e32\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e42\u0e14\u0e22\u0e19\u0e31\u0e22 \u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e04\u0e27\u0e23\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e08\u0e23\u0e34\u0e07 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e27\u0e48\u0e32\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e02\u0e2d\u0e07\u0e15\u0e19')

header('Solar Panel Defender',
       'TECHNICAL DATA SHEET  \u00b7  Issue 1.0  \u00b7  September 2026  \u00b7  Page 1 of 2',
       'Self-cleaning anti-reflective nano coating for solar-panel glass')
y = 67.0


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


# ---------- content ----------
section('PRODUCT DESCRIPTION', gap=4.0)
para('LucernaPro Solar Panel Defender is a single-component, alcohol- and water-borne nano coating for the glass '
     'face of photovoltaic panels and for other glass and inorganic surfaces. It leaves a transparent, inorganic, '
     'super-hydrophilic film only nanometres thick: water spreads into a sheet instead of beading, so wind and '
     'rain carry dust and grime off the panel and cleaning intervals fall sharply. The film also acts as an '
     'anti-reflective layer that raises visible-light transmittance, and it dissipates static charge so that '
     'airborne dust is not attracted to the glass. It is applied thin, in a single coat, with a sponge or cloth '
     '\u2014 no special equipment is needed \u2014 and cures at room temperature or by gentle heating. Being '
     'inorganic, the cured film in principle does not yellow or age.')

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
    ('Cured film',        'Water contact angle \u2264 7\u00b0 (super-hydrophilic) \u00b7 visible-light '
                          'transmittance of coated glass 92.7 % \u00b7 surface resistance 10^9 ohm '
                          '(anti-static) \u00b7 pencil hardness 6H \u00b7 cross-cut adhesion grade 0 '
                          '(GB/T 9286-1998, GB/T 31815-2015) \u00b7 acid resistance: no visible cracking or '
                          'blistering'),
    ('Substrates',        'Glass, photovoltaic glass and other inorganic surfaces. Surfaces that repel alcohol '
                          'cannot be coated unless first plasma- or corona-treated.'),
    ('Application',       'By hand with a fine-pored sponge (melamine type) or a non-woven / microfibre cloth. '
                          'Pour onto the applicator, never onto the panel; spread thin and even in one pass.'),
    ('Consumption',       'Approx. 100 g per 16 m\u00b2 (\u2248 6\u20137 ml/m\u00b2) applied thin in one pass with a squeegee or '
                          'applicator pad, as found in our own field application. The raw-material manufacturer quotes '
                          '10\u201315 ml/m\u00b2 for sponge application.'),
    ('Coats',             'One \u2014 a single thin coat; do not go back over the same area repeatedly'),
    ('Tack-free',         'About 5 minutes at room temperature'),
    ('Hardening',         'The surface hardens immediately on application; hardened through in about 1 hour at '
                          'room temperature \u2014 or by heat, 50\u00b0C \u2248 2 min / 70\u00b0C \u2248 1 min'),
    ('Full cure',         'About 6 hours in warm weather, up to 20 hours in cool conditions. Keep the film dry '
                          'until then.'),
    ('Storage',           '\u221210 to 45\u00b0C, container tightly closed, in a cool shaded place out of direct '
                          'sunlight and away from sparks and flame. Keep out of reach of children.'),
    ('Shelf life',        '12 months from the date of manufacture unopened. Use up soon after opening; beyond '
                          '12 months, test performance before use.'),
    ('Packaging',         '100 g \u00b7 500 g \u00b7 1 kg'),
])

section('NOTE ON VALUES')
para('Typical values from the manufacturer\u2019s testing of the coating material, given as guidance and not as '
     'a specification. Drying and cure times depend on temperature, humidity and airflow, and consumption on '
     'the applicator and substrate. Where the product label differs from this sheet, the label governs. '
     'Independent test reports (RoHS, VOC) are available on the product page.')

section('APPLICATION NOTES')
bullet('Clean and degrease first. Remove dust, oil film and old deposits; the glass must be completely dry. '
       'The coating cannot bond over oil or moisture.', gap=5.0)
bullet('Thin is everything. One thin, even coat gives the best result. Going back over the same area '
       'repeatedly builds an uneven film, wastes material and can leave streaks.')
bullet('Iridescence is normal. Depending on the application method, a faint rainbow sheen (thin-film '
       'interference) may appear on glass and other transparent substrates. It is the anti-reflective film, not '
       'residue, and does not reduce transmittance.')
bullet('Keep water off until cured. Water landing on the film before it has fully cured leaves permanent water '
       'marks. Do not apply when rain or heavy dew is expected within the cure period.')
bullet('The coating reduces the adhesion of new dust and dirt; it does not remove what is already bonded. '
       'Stains that have been forced onto the film \u2014 baked or pressed on \u2014 are difficult to remove.')
bullet('Aftercare. Wipe only with a soft cloth dampened with water. Hard towels, brushes or scouring pads '
       'scratch the film and reduce its performance. If a cleaner is needed, use a neutral or mildly acidic '
       'one; alkaline cleaners of pH 11 and above destroy the coating and must not be used.')
bullet('Recoat when dust is seen to cling more readily than before: clean, dry, and apply one thin coat as '
       'at first application.')

section('HEALTH AND SAFETY')
para('Flammable liquid and vapour (flash point 26.5\u00b0C) with an ethanol-type odour. Keep away from heat, '
     'sparks, open flames and hot surfaces; no smoking; use only with good ventilation. Causes serious eye '
     'damage \u2014 wear safety glasses and gloves; if in eyes, rinse cautiously with water for several minutes '
     'and seek medical attention. Vapour may cause drowsiness or dizziness. Keep the container tightly closed '
     'and store cool, shaded and out of direct sunlight. Refer to the Safety Data Sheet before use.')

print('EN page final y =', y)
assert y < 778, 'EN content overflows into footer: y=%s' % y
footer(EN_FOOT)
c.showPage()

# ================= PAGE 2 — THAI =================
FR, FB, FI = 'Sarabun', 'Sarabun-Bold', 'Sarabun-Italic'
BODY, LEAD = 7.9, 10.3
LABEL_W = 100.0
JUSTIFY = False

header('Solar Panel Defender',
       'TECHNICAL DATA SHEET \u00b7 Issue 1.0 \u00b7 กันยายน 2026 \u00b7 หน้า 2 จาก 2',
       'น้ำยาเคลือบนาโน Self-Cleaning ลดแสงสะท้อน สำหรับกระจกแผงโซลาร์เซลล์')
y = 67.0

section('ข้อมูลผลิตภัณฑ์', gap=4.0)
para('Solar Panel Defender ของ LucernaPro เป็นน้ำยาเคลือบนาโนชนิดส่วนผสมเดียว สูตรแอลกอฮอล์ผสมน้ำ สำหรับผิวกระจกแผงโซลาร์เซลล์ '
     'และผิวกระจกหรือวัสดุอนินทรีย์อื่นๆ / เคลือบแล้วได้ฟิล์มใสระดับนาโนเมตร เป็นสารอนินทรีย์ และดูดซับน้ำสูงมาก (super-hydrophilic) '
     'น้ำที่ตกลงบนผิวจะแผ่เป็นแผ่นบางแทนที่จะเกาะเป็นหยด ลมและฝนจึงพาฝุ่นและคราบสกปรกหลุดออกจากแผงไปเอง ลดรอบขึ้นล้างแผงลงชัดเจน / '
     'ฟิล์มยังทำหน้าที่ลดแสงสะท้อน (anti-reflective) ทำให้แสงส่องผ่านกระจกได้มากขึ้น และช่วยสลายไฟฟ้าสถิตบนผิว ฝุ่นในอากาศจึงไม่ถูกดูดมาเกาะ / '
     'ทาบางๆ รอบเดียวด้วยฟองน้ำหรือผ้า ไม่ต้องใช้เครื่องมือพิเศษ เซ็ตตัวได้ที่อุณหภูมิห้องหรือเร่งด้วยความร้อนอ่อนๆ '
     'และเพราะเป็นฟิล์มอนินทรีย์ โดยหลักการจึงไม่เหลืองและไม่เสื่อมตามอายุ')

section('ข้อมูลสำคัญ')
kv([
    ('ชนิด',              'น้ำยาเคลือบนาโน Self-Cleaning ส่วนผสมเดียว (1K) สูตรแอลกอฮอล์ผสมน้ำ พร้อมใช้ — ห้ามเจือจาง'),
    ('ลักษณะ',            'ของเหลวกึ่งใส สีฟ้าอ่อนถึงขาวอ่อน มีกลิ่นเอทานอลเล็กน้อย'),
    ('เนื้อสาร (solids)',  '10 ± 2 % โดยน้ำหนัก (DIN EN ISO 3251, 1 ชม. / 120°C)'),
    ('ความหนาแน่น (20°C)', '0.88–0.92 g/cm³ (DIN EN ISO 2811-2)'),
    ('pH',                '4.0–6.0 (DIN ISO 976)'),
    ('จุดวาบไฟ',           '26.5°C closed cup (ISO 13736) — ของเหลวไวไฟ'),
    ('องค์ประกอบ',         'ซิลิกาอสัณฐาน ซิลิเกต และออกไซด์อนินทรีย์ ยึดด้วยเรซินพิเศษและพอลิเมอร์อินทรีย์ '
                          'ร่วมกับทินออกไซด์ / ตัวพา: แอลกอฮอล์และน้ำ'),
    ('ฟิล์มหลังเซ็ตตัว',    'มุมสัมผัสน้ำ ≤ 7° (super-hydrophilic) · อัตราส่งผ่านแสงของกระจกที่เคลือบ 92.7 % · '
                          'ความต้านทานผิว 10⁹ Ω (กันไฟฟ้าสถิต) · ความแข็งดินสอ 6H · การยึดเกาะ cross-cut เกรด 0 '
                          '(GB/T 9286-1998, GB/T 31815-2015) · ทนกรด: ไม่พบรอยแตกหรือฟองพอง'),
    ('พื้นผิวที่ใช้ได้',      'กระจก กระจกแผงโซลาร์ และผิววัสดุอนินทรีย์อื่นๆ / ผิวที่ไม่รับแอลกอฮอล์ (น้ำยาเกาะไม่ติด) เคลือบไม่ได้ '
                          'เว้นแต่ผ่านการปรับผิวด้วย plasma หรือ corona ก่อน'),
    ('วิธีทา',             'ทาด้วยมือ ใช้ฟองน้ำรูละเอียด (ฟองน้ำเมลามีน) หรือผ้าไม่ถักทอ / ผ้าไมโครไฟเบอร์ '
                          'เทน้ำยาลงบนผ้าหรือฟองน้ำ ห้ามเทหรือฉีดลงแผงตรงๆ แล้วปาดเกลี่ยบางและสม่ำเสมอในรอบเดียว'),
    ('อัตราการใช้',         'ประมาณ 100 g ต่อ 16 ตร.ม. (≈ 6–7 มล./ตร.ม.) เมื่อทาบางรอบเดียวด้วยไม้ปาดยางหรือ applicator pad '
                          'จากการใช้งานจริงของเรา / ผู้ผลิตวัตถุดิบระบุ 10–15 มล./ตร.ม. สำหรับการทาด้วยฟองน้ำ'),
    ('จำนวนรอบ',          '1 รอบ — ทาบางรอบเดียว ห้ามทาซ้ำวนไปวนมาที่เดิม'),
    ('แห้งสัมผัส',         'ประมาณ 5 นาที ที่อุณหภูมิห้อง'),
    ('การแข็งตัว',         'ผิวหน้าแข็งตัวทันทีหลังทา และแข็งตัวทั่วทั้งฟิล์มในราว 1 ชั่วโมงที่อุณหภูมิห้อง — '
                          'หรือเร่งด้วยความร้อน 50°C ≈ 2 นาที / 70°C ≈ 1 นาที'),
    ('เซ็ตตัวเต็มที่',       'ประมาณ 6 ชั่วโมงในอากาศร้อน และนานถึง 20 ชั่วโมงในอากาศเย็น — ห้ามให้ฟิล์มโดนน้ำจนกว่าจะครบ'),
    ('การเก็บรักษา',        '−10 ถึง 45°C ปิดฝาให้สนิท เก็บในที่เย็น ร่ม ไม่โดนแดดโดยตรง ห่างประกายไฟและเปลวไฟ เก็บพ้นมือเด็ก'),
    ('อายุผลิตภัณฑ์',       '12 เดือนนับจากวันผลิตเมื่อยังไม่เปิด เปิดแล้วควรใช้ให้หมดโดยเร็ว หากเกิน 12 เดือน '
                          'ให้ทดสอบประสิทธิภาพก่อนใช้'),
    ('ขนาดบรรจุ',          '100 g · 500 g · 1 kg'),
])

section('หมายเหตุเรื่องค่าตัวเลข')
para('ค่าทั่วไปจากการทดสอบของผู้ผลิตวัตถุดิบเคลือบ ให้ไว้เป็นแนวทาง ไม่ใช่ข้อกำหนดผูกพัน — เวลาแห้งและเซ็ตตัวขึ้นกับอุณหภูมิ ความชื้น '
     'และการถ่ายเทอากาศ ส่วนอัตราการใช้ขึ้นกับอุปกรณ์ทาและพื้นผิว หากฉลากผลิตภัณฑ์ระบุต่างจากเอกสารนี้ ให้ยึดฉลากเป็นหลัก / '
     'รายงานทดสอบจากแล็บอิสระ (RoHS, VOC) ดาวน์โหลดได้ที่หน้าสินค้า')

section('ข้อควรรู้ในการใช้งาน')
bullet('ทำความสะอาดและล้างคราบน้ำมันก่อนเสมอ — เช็ดฝุ่น ฟิล์มน้ำมัน และคราบเก่าออกให้หมด ผิวกระจกต้องแห้งสนิท '
       'น้ำยาไม่สามารถยึดเกาะบนคราบน้ำมันหรือความชื้นได้', gap=5.0)
bullet('บางคือหัวใจ — ทาบางและสม่ำเสมอรอบเดียวให้ผลดีที่สุด การทาซ้ำวนไปวนมาที่เดิมทำให้ฟิล์มหนาไม่สม่ำเสมอ เปลืองน้ำยา '
       'และเสี่ยงเป็นคราบเป็นทาง')
bullet('คราบสีรุ้งเป็นเรื่องปกติ — ขึ้นกับวิธีทา อาจเห็นสีรุ้งจางๆ (thin-film interference) บนกระจกและวัสดุใสอื่นๆ '
       'นั่นคือฟิล์มลดแสงสะท้อน ไม่ใช่คราบตกค้าง และไม่ลดการส่องผ่านของแสง')
bullet('ห้ามให้โดนน้ำจนกว่าจะเซ็ตตัวเต็มที่ — น้ำที่ตกลงบนฟิล์มก่อนเซ็ตตัวครบจะทิ้งรอยคราบน้ำถาวร '
       'อย่าทาเมื่อคาดว่าจะมีฝนหรือน้ำค้างหนักภายในช่วงเวลาเซ็ตตัว')
bullet('น้ำยาช่วยให้ฝุ่นและคราบใหม่เกาะติดยากขึ้น แต่ไม่ได้ลบคราบที่ฝังแน่นอยู่แล้ว — คราบที่ถูกอัดหรืออบติดลงบนฟิล์มจะเช็ดออกยาก')
bullet('การดูแลหลังเคลือบ — เช็ดด้วยผ้านุ่มชุบน้ำหมาดเท่านั้น ผ้าหยาบ แปรง หรือใยขัดจะทำให้ฟิล์มเป็นรอยและประสิทธิภาพลดลง '
       'ถ้าจำเป็นต้องใช้น้ำยาทำความสะอาด เลือกสูตรกลางหรือกรดอ่อน / น้ำยาที่เป็นด่าง pH 11 ขึ้นไปทำลายชั้นเคลือบ ห้ามใช้เด็ดขาด')
bullet('เคลือบซ้ำเมื่อสังเกตว่าฝุ่นเริ่มเกาะติดง่ายกว่าเดิม — ทำความสะอาด รอให้แห้ง แล้วทาบางรอบเดียวเหมือนครั้งแรก')

section('ความปลอดภัย')
para('ของเหลวและไอระเหยไวไฟ (จุดวาบไฟ 26.5°C) มีกลิ่นแบบเอทานอล — เก็บห่างความร้อน ประกายไฟ เปลวไฟ และผิวร้อน ห้ามสูบบุหรี่ '
     'ทำงานในที่อากาศถ่ายเทดีเท่านั้น / เป็นอันตรายร้ายแรงต่อดวงตา — สวมแว่นตานิรภัยและถุงมือ เข้าตาให้ล้างด้วยน้ำสะอาดต่อเนื่องหลายนาที '
     'แล้วไปพบแพทย์ / ไอระเหยอาจทำให้ง่วงซึมหรือเวียนศีรษะ / ปิดฝาให้สนิท เก็บในที่เย็น ร่ม ไม่โดนแดด / '
     'อ่านเอกสารข้อมูลความปลอดภัย (SDS) ก่อนใช้งาน')

print('TH page final y =', y)
assert y < 778, 'TH content overflows into footer: y=%s' % y
footer(TH_FOOT, disc_size=6.8, disc_lead=8.4)
c.save()
print('written', os.environ.get('LP_OUT', 'files/solarpaneldefender-tds.pdf'))
