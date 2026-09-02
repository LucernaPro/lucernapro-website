# -*- coding: utf-8 -*-
"""Polyurea Standard TDS — same form as the original PolyPro TDS (Canva, 2-column,
orange tables), rebuilt in reportlab. Bilingual: EN pages 1-2 + TH pages 3-4 in the
same document (house rule Aug 2026).
Site doctrine: no raw material codes/percentages published (solvent % and filler
info are internal — never printed here).
VALUES marked None render as "— TBC —" + a DRAFT banner until the owner confirms
them. Fill VALUES below, rerun, banner disappears automatically.
Usage: python3 tools/mk_polyurea_tds.py   (env LP_OUT overrides output path)"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

_T = os.path.dirname(os.path.abspath(__file__))
_F = os.path.join(_T, 'fonts')
pdfmetrics.registerFont(TTFont('Sarabun', os.path.join(_F, 'Sarabun-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Sarabun-Bold', os.path.join(_F, 'Sarabun-Bold.ttf')))
LOGO = os.path.join(_T, 'assets', 'lucerna-hex.png')

# ---------------------------------------------------------------- owner values
# None => "— TBC —" (draft). Fill with real numbers from the owner, then rerun.
VALUES = {
    # Owner 1 Sep 2026: "ทุกอย่างเหมือน PolyPro แค่เติม solvent + ไม่มี filler — ลอกได้เลย"
    # Copied from PolyPro TDS: film indicators, gloss, storage, conditions.
    # NOT copied (solvent changes them / would leak solids %): weight solids,
    # viscosity, specific gravity, film thickness, flash points — rows removed.
    'elongation':   ('≥100%', '≥100%'),
    'tensile':      ('≥15 MPa', '≥15 MPa'),
    'tear':         ('≥60', '≥60'),
    'adhesion':     ('≥4 MPa', '≥4 MPa'),
    'wear':         ('≤40', '≤40'),
    'gloss':        ('semi gloss', 'กึ่งเงา (semi gloss)'),
    'storage_time': ('Part A: 1 year / Part B: 1 year', 'Part A: 1 ปี / Part B: 1 ปี'),
    'storage_temp': ('0°C - 30°C', '0°C - 30°C'),
    'pack':         ('Sets of 1 kg / 5 kg / 9 kg — total weight of Part A + Part B combined (1:1 mix = equal parts)',
                     'ชุด 1 กก. / 5 กก. / 9 กก. — น้ำหนักรวม Part A + Part B (ผสม 1:1 = อย่างละครึ่ง)'),
    'amb':          ('Ambient temperature: 5°C - 30°C, ambient humidity: ≤85%',
                     'อุณหภูมิแวดล้อม 5°C - 30°C ความชื้นสัมพัทธ์ ≤85%'),
}
DRAFT = any(v is None for v in VALUES.values())  # all filled => FINAL
TBC_EN, TBC_TH = '— TBC —', '— รอยืนยัน —'

def V(key, lang):
    v = VALUES.get(key)
    if not v:
        return TBC_TH if lang == 'th' else TBC_EN
    return v[1] if lang == 'th' else v[0]

W, H = A4
L, R = 50.0, 545.0
COL2 = 308.0          # right column x
C1R  = 290.0          # left column right edge
ORANGE = (0.949, 0.420, 0.161)
GREY   = (0.922, 0.922, 0.925)
DARK   = (0.35, 0.35, 0.35)
c = canvas.Canvas(os.environ.get('LP_OUT', os.path.join(_T, '..', 'files', 'polyurea-tds.pdf')), pagesize=A4)
c.setTitle('LucernaPro Polyurea Standard — Technical Data Sheet')

def fonts(lang):
    return ('Sarabun', 'Sarabun-Bold')

def wrap(text, font, size, width):
    out, line = [], ''
    for w_ in text.split(' '):
        t = (line + ' ' + w_).strip()
        if stringWidth(t, font, size) <= width:
            line = t
        else:
            if line: out.append(line)
            line = w_
    if line: out.append(line)
    return out

def rich(y, x, width, parts, lang, size=10, lead=13.6):
    """parts: list of (text, bold). TBC text renders orange."""
    FR, FB = fonts(lang)
    cx = x
    for text, bold in parts:
        f = FB if bold else FR
        for w_ in text.split(' '):
            if not w_: continue
            token = w_ + ' '
            tw = stringWidth(token, f, size)
            if cx + tw > x + width + 2:
                y -= lead; cx = x
            c.setFont(f, size)
            c.setFillColorRGB(*ORANGE) if DRAFT and ('TBC' in w_ or 'รอยืนยัน' in w_) else c.setFillGray(0.08)
            c.drawString(cx, y, w_)
            cx += tw
    return y - lead

def para(y, x, width, label, text, lang, size=10, lead=13.6):
    return rich(y, x, width, ([(label + ':', True)] if label else []) + [(text, False)], lang, size, lead) - 3

def bullets(y, x, width, items, lang, size=10, lead=13.2):
    FR, _ = fonts(lang)
    for it in items:
        c.setFillGray(0.08); c.setFont(FR, size)
        c.drawString(x + 4, y, '•')
        y = rich(y, x + 16, width - 16, [(it, False)], lang, size, lead)
        y -= 1.5
    return y - 2

def head_bold(y, x, text, lang, size=11):
    _, FB = fonts(lang)
    c.setFillGray(0); c.setFont(FB, size)
    c.drawString(x, y, text)
    return y - 16

def kv_table(y, x, width, rows, lang, size=9.6, valx_ratio=0.56, min_h=34):
    """PolyPro-style boxed rows: label left, value right, grid + alt grey fill."""
    FR, _ = fonts(lang)
    vx = x + width * valx_ratio
    for i, (k, v) in enumerate(rows):
        kl = wrap(k, FR, size, width * valx_ratio - 14)
        vl = wrap(v, FR, size, width * (1 - valx_ratio) - 14)
        h = max(min_h, 14 + 12 * max(len(kl), len(vl)))
        if i % 2 == 0:
            c.setFillColorRGB(*GREY); c.rect(x, y - h, width, h, stroke=0, fill=1)
        c.setStrokeGray(0); c.setLineWidth(0.8)
        c.rect(x, y - h, width, h, stroke=1, fill=0)
        c.line(vx, y, vx, y - h)
        ty = y - 15
        c.setFont(FR, size)
        for ln in kl:
            c.setFillGray(0.08); c.drawString(x + 7, ty, ln); ty -= 12
        ty = y - 15
        tbc = DRAFT and (TBC_EN in v or TBC_TH in v)
        for ln in vl:
            c.setFillColorRGB(*ORANGE) if tbc else c.setFillGray(0.08)
            c.drawString(vx + 7, ty, ln); ty -= 12
        y -= h
    return y

def bar_title(y, x, width, text, lang, h=22):
    _, FB = fonts(lang)
    c.setFillColorRGB(*ORANGE); c.setStrokeGray(0); c.setLineWidth(0.8)
    c.rect(x, y - h, width, h, stroke=1, fill=1)
    c.setFillGray(1); c.setFont(FB, 10.5)
    c.drawString(x + 7, y - h + 7, text)
    return y - h

def temp_table(y, x, width, head, row_label, cells, lang):
    """1 header row (orange first cell) + 1 data row, PolyPro pot-life style."""
    FR, FB = fonts(lang)
    n = len(cells)
    lab_w = width * 0.42
    cw = (width - lab_w) / n
    for r, (lab, vals, hdr) in enumerate(((head[0], head[1:], True), (row_label, cells, False))):
        yy = y - 30 * r
        if hdr:
            c.setFillColorRGB(*ORANGE); c.rect(x, yy - 30, lab_w, 30, stroke=0, fill=1)
        c.setStrokeGray(0); c.setLineWidth(0.8)
        c.rect(x, yy - 30, lab_w, 30, stroke=1, fill=0)
        c.setFont(FB if hdr else FR, 9.6)
        c.setFillGray(1) if hdr else c.setFillGray(0.08)
        c.drawString(x + 7, yy - 19, lab)
        for i, v in enumerate(vals):
            cx = x + lab_w + cw * i
            c.rect(cx, yy - 30, cw, 30, stroke=1, fill=0)
            c.setFont(FR, 9.6)
            c.setFillColorRGB(*ORANGE) if DRAFT and (TBC_EN in v or TBC_TH in v) else c.setFillGray(0.08)
            c.drawCentredString(cx + cw / 2, yy - 19, v[:22])
    return y - 60

def header(lang, subtitle):
    if os.path.exists(LOGO):
        c.drawImage(LOGO, W / 2 - 21, H - 66, width=42, height=42, mask='auto')
    c.setFillGray(0); c.setFont('Helvetica-Bold', 17)
    c.drawCentredString(W / 2, H - 84, 'LUCERNAPRO')
    FR, _ = fonts(lang)
    c.setFont(FR, 10.5)
    c.drawCentredString(W / 2, H - 99, subtitle)
    c.setStrokeGray(0.1); c.setLineWidth(1)
    c.line(L, H - 112, R, H - 112)
    c.setFillColorRGB(*DARK)
    c.rect(R - 150, H - 115, 150, 6, stroke=0, fill=1)
    if DRAFT:
        c.setFillColorRGB(0.8, 0.1, 0.1); c.setFont('Sarabun-Bold', 10)
        c.drawString(L, H - 34, 'DRAFT — ค่าที่เป็นสีส้ม (TBC) รอเจ้าของยืนยัน ห้ามเผยแพร่')
    return H - 134

def footer(with_logo=False):
    c.setFillColorRGB(*DARK); c.rect(L - 10, 28, R - L + 20, 12, stroke=0, fill=1)
    c.setFillColorRGB(*ORANGE); c.rect(W / 2 - 120, 26, 240, 16, stroke=0, fill=1)
    c.setFillGray(1); c.setFont('Helvetica', 9)
    c.drawCentredString(W / 2, 30.5, 'www.lucernapro.com')
    if with_logo and os.path.exists(LOGO):
        c.drawImage(LOGO, W / 2 - 76, 52, width=26, height=26, mask='auto')
        c.setFillGray(0); c.setFont('Helvetica-Bold', 15)
        c.drawString(W / 2 - 44, 59, 'LUCERNAPRO')

# ------------------------------------------------------------------- content
EN = dict(
    subtitle='Technical Data Sheet of POLYUREA STANDARD',
    pno=('Product No.', 'POLYUREA STANDARD (A/B)'),
    pname=('Product Name', 'Polyaspartic Polyurea Elastomeric Waterproof Coating (roller grade, solvent-based)'),
    intro=('Product Introduction', 'The main agent is polyaspartic resin with pigments and auxiliary agents in a solvent carrier. The curing agent is a modified isocyanate.'),
    feat_h='Product Features:',
    feats=['True polyurea chemistry in a roller-applied formula — no spray equipment needed',
           'Withstands long-term ponding water; UV-stable for outdoor exposure',
           'Low-viscosity film penetrates deep into bare concrete for strong adhesion',
           'Higher film flexibility than our thick-film grades',
           'Simple two-coat application with a 4-inch short-nap roller'],
    use=('Design Use', 'Waterproofing of bare concrete rooftops (roof decks), balconies and concrete floors. Not suitable over glazed tiles — use PolyPro or TileCoat Polyurea for tiled surfaces.'),
    agents_h=('Main Agent', 'Curing Agent'),
    rate_rows=[('Theoretical coating rate:', ''),
               ('Theoretical value:', '1 kg per 5 square meters at 2 coats'),
               ('Actual value:', 'related to surface treatment, external environment, construction method and other factors')],
    ind_h='Main Technical Indicators of Coating Film:',
    cons_h='Construction Parameters:',
    ratio=[('Use ratio:', True), ('A:B = 1 : 1 by weight — weigh on a digital scale only, never estimate by eye. Stir a full 1 minute, all the way to the bottom of the bucket.', False)],
    pot=[('Application time:', True), ('Pot life ≈ 10 minutes after mixing — mix small batches you can finish in time.', False)],
    cond_h='Construction conditions:',
    method='Construction method: Brush or Roller (4-inch short-nap)',
    clean='Cleaning agent: thinner',
    dry_h='Drying time and painting interval (approx. 30°C):',
    dry_note='The above data are for guidance only; actual drying time / recoat interval may be longer or shorter depending on film thickness, ventilation, humidity and substrate condition.',
    pkg_h='Coating Package:',
    pkg='Self-priming: apply the first coat as thin as possible to seal substrate absorption — no separate primer required on sound bare concrete. Topcoat: not required.',
    surf_h='Surface Treatment:',
    surf=['Surface must be clean, dry and free of dust, grease and stains',
          'Remove all old paint, wax or primer completely — do not coat over them',
          'Repair cracks and holes flush before coating; the membrane must be continuous',
          'Mask the edges of the work area with tape'],
    sto_h='Storage:',
    pack_h='Packaging Specifications:',
    sec_h='Security Measures:',
    sec=['Solvent-based: always work in a well-ventilated area',
         'Contains combustible substances — keep away from sparks; do not smoke in the work area',
         'Avoid contact with skin and eyes; if in eyes, flush with plenty of water and seek medical attention',
         'Not suitable for persons sensitive to thinner or chemicals — have a contractor apply instead',
         'Comply with all health and safety regulations on site'],
    stmt_h='Statement:',
    stmt='The information provided in this product specification is based solely on our knowledge gained in the laboratory and in practice. However, since use of the product is usually beyond our control, we only give a guarantee of the quality of the product itself. We reserve the right to amend the specification by prior notice.',
)
TH = dict(
    subtitle='เอกสารข้อมูลทางเทคนิค POLYUREA STANDARD',
    pno=('รหัสสินค้า', 'POLYUREA STANDARD (A/B)'),
    pname=('ชื่อสินค้า', 'กันซึม Polyaspartic Polyurea ชนิดยืดหยุ่น (เกรดทาด้วยลูกกลิ้ง สูตร solvent-base)'),
    intro=('ข้อมูลผลิตภัณฑ์', 'ส่วนเนื้อหลักคือเรซิน polyaspartic ผสมเม็ดสีและสารช่วยในตัวทำละลาย ส่วนน้ำยาบ่มคือ isocyanate ชนิดดัดแปลง'),
    feat_h='จุดเด่นของผลิตภัณฑ์:',
    feats=['เคมี Polyurea แท้ในสูตรทาด้วยลูกกลิ้ง — ไม่ต้องใช้เครื่องพ่น',
           'แช่น้ำขังได้ยาวนาน ทนแดดกลางแจ้ง',
           'เนื้อเหลวซึมลึกลงผิวปูนเปลือย ยึดเกาะแน่น',
           'ฟิล์มยืดหยุ่นสูงกว่ารุ่นฟิล์มหนาของเรา',
           'ทาง่ายเพียง 2 รอบ ด้วยลูกกลิ้งขนสั้น 4 นิ้ว'],
    use=('การใช้งานที่ออกแบบไว้', 'งานกันซึมดาดฟ้าปูน ระเบียงปูน และพื้นคอนกรีตเปลือย ไม่เหมาะกับผิวกระเบื้องเคลือบ — งานกระเบื้องให้ใช้ PolyPro หรือ TileCoat Polyurea'),
    agents_h=('ส่วนเนื้อ (Part A)', 'น้ำยาบ่ม (Part B)'),
    rate_rows=[('อัตราการปกคลุมทางทฤษฎี:', ''),
               ('ค่าทางทฤษฎี:', '1 กก. ต่อ 5 ตร.ม. ที่การทา 2 รอบ'),
               ('ค่าจริง:', 'ขึ้นกับการเตรียมพื้นผิว สภาพแวดล้อม และวิธีการทำงานหน้างาน')],
    ind_h='ค่าดัชนีทางเทคนิคหลักของฟิล์ม:',
    cons_h='พารามิเตอร์การทำงาน:',
    ratio=[('อัตราส่วนผสม:', True), ('A:B = 1 : 1 โดยน้ำหนัก — ชั่งด้วยเครื่องชั่งดิจิทัลเท่านั้น ห้ามกะด้วยสายตา แล้วกวนให้ทั่วถึงก้นถัง 1 นาทีเต็ม', False)],
    pot=[('เวลาทำงานหลังผสม:', True), ('Pot life ประมาณ 10 นาที — แบ่งผสมทีละน้อยเท่าที่ทาทัน', False)],
    cond_h='สภาวะการทำงาน:',
    method='วิธีการทา: แปรง หรือลูกกลิ้งขนสั้น 4 นิ้ว',
    clean='น้ำยาล้างอุปกรณ์: ทินเนอร์',
    dry_h='เวลาแห้งและระยะเว้นระหว่างรอบ (ประมาณที่ 30°C):',
    dry_note='ตัวเลขข้างต้นเป็นค่าแนะนำ เวลาแห้งจริงอาจสั้นหรือยาวกว่านี้ ขึ้นกับความหนาฟิล์ม การระบายอากาศ ความชื้น และสภาพพื้นผิว',
    pkg_h='ระบบเคลือบ:',
    pkg='รองพื้นในตัว: ทารอบแรกให้บางที่สุดเพื่อกันพื้นผิวดูดสี — ปูนเปลือยสภาพดีไม่ต้องใช้รองพื้นแยก และไม่ต้องเคลือบทับหน้า',
    surf_h='การเตรียมพื้นผิว:',
    surf=['พื้นผิวต้องสะอาด แห้งสนิท ไม่มีฝุ่น คราบมัน คราบสกปรก',
          'ผิวที่เคยทาสี ลงแวกซ์ หรือรองพื้นไว้ ต้องขูดออกทั้งหมด ห้ามทาทับ',
          'โป๊วรอยแตก หลุม ร่อง ให้เต็มเรียบก่อนเสมอ — ระบบกันซึมต้องเป็นผืนเดียวต่อเนื่อง',
          'ติดกระดาษกาวรอบขอบพื้นที่กันเลอะ'],
    sto_h='การจัดเก็บ:',
    pack_h='ขนาดบรรจุ:',
    sec_h='ความปลอดภัย:',
    sec=['สูตร solvent-base: ทำงานในที่อากาศถ่ายเทเสมอ',
         'มีส่วนผสมติดไฟได้ — ห้ามทำงานใกล้ประกายไฟ และห้ามสูบบุหรี่ในบริเวณงาน',
         'หลีกเลี่ยงการสัมผัสผิวหนังและดวงตา หากเข้าตาให้ล้างด้วยน้ำสะอาดปริมาณมากและพบแพทย์ทันที',
         'ไม่เหมาะกับผู้ที่แพ้ทินเนอร์หรือสารเคมี — แนะนำให้ช่างเป็นผู้ดำเนินการแทน',
         'ปฏิบัติตามข้อกำหนดความปลอดภัยของหน้างานทุกข้อ'],
    stmt_h='คำชี้แจง:',
    stmt='ข้อมูลในเอกสารฉบับนี้อ้างอิงจากความรู้ที่ได้จากห้องปฏิบัติการและการใช้งานจริงของบริษัทเท่านั้น เนื่องจากการใช้งานผลิตภัณฑ์อยู่นอกเหนือการควบคุมของบริษัท บริษัทจึงรับประกันเฉพาะคุณภาพของตัวผลิตภัณฑ์ และขอสงวนสิทธิ์ในการแก้ไขข้อมูลโดยแจ้งให้ทราบล่วงหน้า',
)

def page1(lang, d):
    y = header(lang, d['subtitle'])
    FR, FB = fonts(lang)
    # left column
    yl = y
    yl = para(yl, L, C1R - L, d['pno'][0], d['pno'][1], lang)
    yl = para(yl, L, C1R - L, d['pname'][0], d['pname'][1], lang)
    yl = para(yl, L, C1R - L, d['intro'][0], d['intro'][1], lang)
    yl -= 6
    yl = head_bold(yl, L, d['feat_h'], lang)
    yl = bullets(yl, L, C1R - L, d['feats'], lang)
    yl = para(yl, L, C1R - L, d['use'][0], d['use'][1], lang)
    yl -= 8
    # Main/Curing agent split table
    half = (C1R - L) / 2
    c.setFillColorRGB(*ORANGE); c.setStrokeGray(0); c.setLineWidth(0.8)
    c.rect(L, yl - 22, C1R - L, 22, stroke=1, fill=1)
    c.line(L + half, yl, L + half, yl - 22)
    c.setFillGray(1); c.setFont(FB, 10)
    c.drawString(L + 7, yl - 15, d['agents_h'][0])
    c.drawString(L + half + 7, yl - 15, d['agents_h'][1])
    yl -= 22
    app = 'Appearance: colored liquid' if lang == 'en' else 'ลักษณะ: ของเหลวมีสี'
    for row in ((app, app),):
        hh = 30
        c.setStrokeGray(0); c.rect(L, yl - hh, C1R - L, hh, stroke=1, fill=0)
        c.line(L + half, yl, L + half, yl - hh)
        for i, txt in enumerate(row):
            tbc = DRAFT and (TBC_EN in txt or TBC_TH in txt)
            c.setFont(FR, 9.2)
            xx = L + 7 + half * i
            for j, ln in enumerate(wrap(txt, FR, 9.2, half - 14)[:2]):
                c.setFillColorRGB(*ORANGE) if tbc else c.setFillGray(0.08)
                c.drawString(xx, yl - 14 - 11 * j, ln)
        yl -= hh
    single = [
        (('Gloss: ' if lang == 'en' else 'ความเงา: ') + V('gloss', lang)),
    ]
    for i, txt in enumerate(single):
        hh = 30
        if i % 2 == 0:
            c.setFillColorRGB(*GREY); c.rect(L, yl - hh, C1R - L, hh, stroke=0, fill=1)
        c.setStrokeGray(0); c.rect(L, yl - hh, C1R - L, hh, stroke=1, fill=0)
        tbc = DRAFT and (TBC_EN in txt or TBC_TH in txt)
        c.setFont(FR, 9.2)
        for j, ln in enumerate(wrap(txt, FR, 9.2, C1R - L - 14)[:2]):
            c.setFillColorRGB(*ORANGE) if tbc else c.setFillGray(0.08)
            c.drawString(L + 7, yl - 14 - 11 * j, ln)
        yl -= hh
    # right column
    yr = y
    c.setFillColorRGB(*GREY); c.setStrokeGray(0); c.setLineWidth(0.8)
    c.rect(COL2, yr - 24, R - COL2, 24, stroke=1, fill=1)
    c.setFillGray(0.08); c.setFont(fonts(lang)[0], 9.8)
    c.drawString(COL2 + 7, yr - 16, d['rate_rows'][0][0])
    yr -= 24
    yr = kv_table(yr, COL2, R - COL2, [(d['rate_rows'][1][0], d['rate_rows'][1][1]),
                                       (d['rate_rows'][2][0], d['rate_rows'][2][1])], lang, valx_ratio=0.34, min_h=40)
    yr -= 16
    yr = bar_title(yr, COL2, R - COL2, d['ind_h'], lang)
    ind = [(('Elongation' if lang == 'en' else 'การยืดตัว (Elongation)'), V('elongation', lang)),
           (('Tensile strength' if lang == 'en' else 'แรงดึง (Tensile strength)'), V('tensile', lang)),
           (('Tear strength N/mm' if lang == 'en' else 'แรงฉีกขาด N/mm'), V('tear', lang)),
           (('Adhesion (concrete):' if lang == 'en' else 'การยึดเกาะ (คอนกรีต):'), V('adhesion', lang)),
           (('Wear resistance (1000g/500r):' if lang == 'en' else 'ความทนการขัดสี (1000g/500r):'), V('wear', lang))]
    yr = kv_table(yr, COL2, R - COL2, ind, lang, valx_ratio=0.6, min_h=36)
    yr -= 14
    yr = head_bold(yr, COL2, d['cons_h'], lang)
    yr = rich(yr, COL2, R - COL2, d['ratio'], lang, size=9.8, lead=13)
    yr -= 3
    yr = rich(yr, COL2, R - COL2, d['pot'], lang, size=9.8, lead=13)
    yr -= 8
    yr = head_bold(yr, COL2, d['cond_h'], lang, size=10)
    yr = rich(yr, COL2, R - COL2, [(V('amb', lang), False)], lang, size=9.8, lead=13)
    dew = ('Substrate temperature: at least 3°C above the air dew point.' if lang == 'en'
           else 'อุณหภูมิพื้นผิว: สูงกว่าจุดน้ำค้างของอากาศอย่างน้อย 3°C')
    yr = rich(yr, COL2, R - COL2, [(dew, False)], lang, size=9.8, lead=13)
    yr = rich(yr, COL2, R - COL2, [(d['method'], False)], lang, size=9.8, lead=13)
    yr = rich(yr, COL2, R - COL2, [(d['clean'], False)], lang, size=9.8, lead=13)
    footer()
    c.showPage()

def page2(lang, d):
    FR, FB = fonts(lang)
    y = H - 60
    if DRAFT:
        c.setFillColorRGB(0.8, 0.1, 0.1); c.setFont('Sarabun-Bold', 10)
        c.drawString(L, H - 34, 'DRAFT — ค่าที่เป็นสีส้ม (TBC) รอเจ้าของยืนยัน ห้ามเผยแพร่')
    # left
    yl = head_bold(y, L, d['dry_h'], lang, size=10.5)
    dry = [(('Dry to recoat' if lang == 'en' else 'เว้นก่อนทารอบถัดไป'), '2 ' + ('hours' if lang == 'en' else 'ชั่วโมง')),
           (('Ready for foot traffic (after final coat)' if lang == 'en' else 'เดินใช้งานได้ (หลังทารอบสุดท้าย)'), '6 ' + ('hours' if lang == 'en' else 'ชั่วโมง'))]
    yl = kv_table(yl, L, C1R - L, dry, lang, valx_ratio=0.62, min_h=32)
    yl -= 18
    yl = rich(yl, L, C1R - L, [(d['dry_note'], False)], lang, size=9.6, lead=12.8)
    yl -= 10
    yl = head_bold(yl, L, d['pkg_h'], lang)
    yl = rich(yl, L, C1R - L, [(d['pkg'], False)], lang, size=9.8, lead=13)
    yl -= 10
    yl = head_bold(yl, L, d['surf_h'], lang)
    yl = bullets(yl, L, C1R - L, d['surf'], lang, size=9.8)
    # right
    yr = head_bold(y, COL2, d['sto_h'], lang)
    st = ('Storage time: ' if lang == 'en' else 'อายุการเก็บ: ') + V('storage_time', lang)
    st2 = ('Storage temperature: ' if lang == 'en' else 'อุณหภูมิจัดเก็บ: ') + V('storage_temp', lang)
    yr = rich(yr, COL2, R - COL2, [(st, False)], lang, size=9.8, lead=13)
    yr = rich(yr, COL2, R - COL2, [(st2, False)], lang, size=9.8, lead=13)
    yr -= 10
    yr = head_bold(yr, COL2, d['pack_h'], lang)
    yr = rich(yr, COL2, R - COL2, [(V('pack', lang), False)], lang, size=9.8, lead=13)
    yr -= 10
    yr = head_bold(yr, COL2, d['sec_h'], lang)
    yr = bullets(yr, COL2, R - COL2, d['sec'], lang, size=9.8)
    yr -= 6
    yr = head_bold(yr, COL2, d['stmt_h'], lang)
    yr = rich(yr, COL2, R - COL2, [(d['stmt'], False)], lang, size=9.4, lead=12.6)
    footer(with_logo=True)
    c.showPage()

for lang, d in (('en', EN), ('th', TH)):
    page1(lang, d)
    page2(lang, d)
c.save()
print('OK', 'DRAFT' if DRAFT else 'FINAL', '->', os.environ.get('LP_OUT', 'files/polyurea-tds.pdf'))
