# -*- coding: utf-8 -*-
"""
build_fiberglass_pool_post.py — เคส PoolArmour: สระไฟเบอร์กลาสที่เคยฉาบปูนปูกระเบื้องแล้วกระเบื้องหลุดซ้ำ
รื้อกระเบื้อง → ขัดผิวปูนเรียบ → CorePrimer → PoolArmour สีเทา (น้ำออกเขียวมรกต)
/post/fiberglass-pool-tiles-to-poolarmour (+ /en/…)
วิธี: chrome-transplant จากโพสต์ solar-panel-defender-feibo-lab (เหมือน build_feibo_stone_cases.py) — TH+EN
รูป: /img/post/fiberglass-pool-tiles-to-poolarmour-h1..h6.webp (ภาพจากทีมช่าง ก.ย. 2026, 640px จาก Facebook)
รัน: python3 tools/build_fiberglass_pool_post.py (จาก root ของ repo)
"""
import os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "solar-panel-defender-feibo-lab"
SLUG = "fiberglass-pool-tiles-to-poolarmour"


def dims(k):
    return Image.open(os.path.join(ROOT, "img", "post", f"{SLUG}-h{k}.webp")).size


def fig(k, alt, cap, hero=False):
    w, h = dims(k)
    cls = ' class="hero"' if hero else ''
    icls = ' class="tall"' if h > w else ''
    lazy = '' if hero else ' loading="lazy"'
    return (f'    <figure{cls}><img{icls} src="/img/post/{SLUG}-h{k}.webp" alt="{alt}"{lazy} '
            f'width="{w}" height="{h}"><figcaption>{cap}</figcaption></figure>\n')


def pair(k1, k2, alt1, alt2, cap):
    """สองภาพแนวตั้งวางคู่กัน (ภาพต้นฉบับ 480x640) — ใช้ grid inline เหมือนแกลเลอรีโพสต์อื่น"""
    return ('    <figure style="margin-top:18px"><div style="display:flex;gap:10px">'
            f'<img src="/img/post/{SLUG}-h{k1}.webp" alt="{alt1}" loading="lazy" width="480" height="640" style="width:calc(50% - 5px);min-width:0;border-radius:12px;border:1px solid var(--line)">'
            f'<img src="/img/post/{SLUG}-h{k2}.webp" alt="{alt2}" loading="lazy" width="480" height="640" style="width:calc(50% - 5px);min-width:0;border-radius:12px;border:1px solid var(--line)">'
            f'</div><figcaption>{cap}</figcaption></figure>\n')


def step(n, h2, parts):
    return (f'    <section class="step">\n      <h2><span class="n">{n}</span>{h2}</h2>\n'
            + "".join((f"      <p>{p}</p>\n" if not p.lstrip().startswith("<") else p) for p in parts)
            + "    </section>\n")


TH = dict(
    title="สระไฟเบอร์กลาสที่ฉาบปูนปูกระเบื้องแล้วกระเบื้องหลุดซ้ำ — รื้อออก ขัดเรียบ แล้วเคลือบ PoolArmour สีเทา",
    desc="สระไฟเบอร์กลาสที่เคยถูกฉาบปูนและปูกระเบื้องทับ กระเบื้องหลุดเป็นรอบๆ เพราะเปลือกไฟเบอร์ขยับแต่ปูนกับกระเบื้องไม่ขยับตาม — ทีมช่างรื้อกระเบื้องออก ขัดผิวปูนให้เรียบ รองพื้น CorePrimer แล้วเคลือบ PoolArmour สีเทา เลือกเทาเพราะเติมน้ำแล้วออกเขียวมรกต",
    eyebrow="Case Study · สระว่ายน้ำ / PoolArmour + CorePrimer",
    meta="เผยแพร่ ก.ย. 2026 · ภาพหน้างานจากทีมช่างผู้รับเหมา",
    intro=[
        'สระนี้เป็นสระ<b>ไฟเบอร์กลาส</b>ที่ครั้งหนึ่งถูกฉาบปูนแล้วปูกระเบื้องโมเสกทับทั้งสระ หน้าตาเหมือนสระคอนกรีตทุกอย่าง — จนกระเบื้องเริ่มหลุด ซ่อมแล้วหลุดอีก เจ้าของสระเลยส่งช่างมาปรึกษาเราว่าจะเอายังไงกับมันดี',
        'คำตอบของเราไม่ใช่ปูกระเบื้องใหม่ให้ดีกว่าเดิม แต่คือเลิกสู้กับธรรมชาติของไฟเบอร์กลาส แล้วเปลี่ยนไปใช้ผิวที่ขยับตามมันได้',
    ],
    hero=("สระไฟเบอร์กลาสหลังเคลือบ PoolArmour สีเทาทั้งสระ ยังไม่เติมน้ำ มีบันไดมุมสระ",
          "หลังงานเสร็จ — PoolArmour สีเทาทั้งสระ ก่อนเติมน้ำ เฉดนี้พอน้ำลงจะออกเขียวมรกต"),
    steps=[
        ("01", "ทำไมกระเบื้องบนสระไฟเบอร์ถึงหลุดซ้ำ — ไม่ใช่ฝีมือช่าง", [
            'เปลือกไฟเบอร์กลาส<b>ขยับ</b> — ยืดหดตามอุณหภูมิ แอ่นตามระดับน้ำ ขยับตามดินรอบสระ เป็นข้อดีของมันเพราะไม่แตกร้าวเหมือนคอนกรีต แต่ปูนฉาบกับกระเบื้องเป็นวัสดุแข็งที่ไม่ขยับตาม พอสองอย่างนี้ประกบกัน แรงเฉือนที่รอยต่อระหว่างปูนกับไฟเบอร์จะสะสมทุกรอบที่สระร้อน-เย็น เติมน้ำ-ปล่อยน้ำ จนวันหนึ่งปูนแยกตัวออกจากเปลือกและกระเบื้องหลุดออกมาเป็นแผง ปูใหม่ก็กลับมาเป็นแบบเดิมเพราะสาเหตุยังอยู่',
            pair(2, 3, "กระเบื้องโมเสกบนผนังสระ มีคราบตะไคร่และแนวกาวที่กระเบื้องหลุดออก", "ช่างรื้อกระเบื้องโมเสกออกจากพื้นและผนังสระ เห็นเศษกระเบื้องกองอยู่",
                 "ซ้าย: กระเบื้องบนผนังสระก่อนรื้อ — หลุดเป็นหย่อม เห็นแนวปูนกาวใต้กระเบื้อง · ขวา: ระหว่างรื้อ กระเบื้องกับกาวออกมาเป็นแผ่นๆ"),
        ]),
        ("02", "แนวทางที่เราแนะนำ: รื้อออกให้หมด แล้วขัดปูนที่เหลือให้เรียบ", [
            'ทีมช่างรื้อกระเบื้องและกาวออกทั้งสระ ปูนฉาบชั้นที่ยังยึดแน่นกับเปลือกไฟเบอร์เก็บไว้ แล้ว<b>ขัดผิวให้เรียบทั้งผืน</b> — ขั้นนี้คือขั้นที่กำหนดหน้าตาของงานทั้งหมด เพราะ PoolArmour เป็นฟิล์มบางที่ตามผิว ผิวปูนเป็นคลื่น สีก็เป็นคลื่น ขัดจนเรียบ สีก็เรียบ',
            'จากนั้นรองพื้นด้วย <a href="/coreprimer">CorePrimer</a> ให้ซึมลงเนื้อปูนและล็อกผิวที่ร่วนให้แน่น แล้วจึงเคลือบ <a href="/poolarmour">PoolArmour</a> ทับ — ฟิล์ม PoolArmour ยืดหยุ่นพอที่จะขยับตามเปลือกไฟเบอร์ได้ ต่างจากกระเบื้องตรงนี้',
            pair(4, 5, "สระไฟเบอร์กลาสหลังรื้อกระเบื้อง เหลือผิวปูนที่ขัดเรียบทั้งสระ", "สระหลังขัดผิวปูนเรียบทั้งผืน พร้อมลงระบบ มองเห็นบันไดมุมสระ",
                 "ผิวปูนหลังรื้อกระเบื้องและขัดเรียบทั้งสระ — พื้น ผนัง และบันได พร้อมสำหรับรองพื้น CorePrimer แล้วเคลือบ PoolArmour"),
        ]),
        ("03", "ทำไมต้องสีเทา", [
            'เจ้าของสระเลือกสีเทาตามที่เราแนะนำ เพราะสีสระที่ยังไม่เติมน้ำกับที่เติมน้ำแล้วคนละเรื่อง — สีขาวเติมน้ำแล้วออกฟ้าอ่อนสว่าง ส่วน<b>สีเทาเติมน้ำแล้วออกเขียวมรกต</b> เป็นเฉดคลาสสิกที่เข้ากับสวนและไม้รอบสระแบบนี้ที่สุด ดูตัวอย่างน้ำลงแล้วของทั้งสองเฉดได้ที่หน้า <a href="/poolarmour#showcase">PoolArmour</a>',
            fig(6, "ผิว PoolArmour สีเทาหลังเคลือบเสร็จ มีน้ำฝนขังบนพื้นสระและใบไม้ร่วง",
                "หลังเคลือบเสร็จ ฝนตกลงมาก่อนเติมน้ำ — ผิวเทาเรียบทั้งพื้นและบันได แค่น้ำฝนบางๆ ก็เริ่มเห็นโทนเขียวแล้ว"),
        ]),
        ("04", "ถ้าสระไฟเบอร์ของคุณเป็นแบบนี้", [
            'สระไฟเบอร์กลาสที่ผิวเจลโค้ตเดิมด่าง ซีด หรือถูกฉาบปูนทับมาก่อน — อย่าปูกระเบื้อง และอย่าฉาบทับเพิ่ม ผิวที่ใช้ได้กับเปลือกที่ขยับคือฟิล์มที่ยืดหยุ่น รื้อของแข็งออก ขัดผิวให้เรียบ รองพื้นให้ถูกตัว แล้วค่อยเคลือบ ส่งรูปสระมาทางแชทเพจได้เลย ทีมงานดูให้ก่อนว่าต้องรื้อถึงชั้นไหน',
        ]),
    ],
    prods='<div class="prods"><span class="lbl">สินค้าที่ใช้ในงานนี้:</span><a href="/poolarmour">PoolArmour</a><a href="/coreprimer">CorePrimer</a></div>\n  <a class="back" href="/casestudy/">← กลับไปดูเคสอื่นๆ</a>\n',
)

EN = dict(
    title="A Fibreglass Pool That Had Been Rendered and Tiled — Tiles Kept Falling Off, So We Stripped It Back and Coated It in Grey PoolArmour",
    desc="A fibreglass pool that had once been rendered and tiled over. The tiles kept coming off in patches because the fibreglass shell moves and render and tile do not — the crew stripped the tiles, ground the render smooth, primed with CorePrimer and coated in grey PoolArmour. Grey, because filled with water it turns emerald green",
    eyebrow="Case Study · Swimming Pools / PoolArmour + CorePrimer",
    meta="Published Sept 2026 · Site photos from the contractor's crew",
    intro=[
        'This is a <b>fibreglass</b> pool that at some point had been rendered and covered in mosaic tile from top to bottom — it looked exactly like a concrete pool. Until the tiles started coming off. Repaired, came off again. The owner sent the contractor to ask us what to do with it.',
        'Our answer was not "tile it better this time". It was to stop fighting the nature of fibreglass and switch to a surface that can move with it.',
    ],
    hero=("Fibreglass pool coated entirely in grey PoolArmour, not yet filled, with corner steps",
          "After the job — grey PoolArmour over the whole pool, before filling. Under water this shade turns emerald green"),
    steps=[
        ("01", "Why tiles keep falling off a fibreglass pool — it isn't the tiler", [
            'A fibreglass shell <b>moves</b> — it expands and contracts with temperature, flexes with the water level, shifts with the ground around it. That is its strength: it does not crack the way concrete does. But render and tile are rigid materials that do not move with it. Put the two together and shear builds up at the render-to-fibreglass interface every time the pool heats and cools, fills and drains, until one day the render lets go of the shell and the tiles come off in sheets. Re-tiling brings it straight back, because the cause is still there.',
            pair(2, 3, "Mosaic tile on a pool wall with algae staining and exposed adhesive where tiles have come off", "Crew stripping mosaic tile off the pool floor and walls, with tile debris piled up",
                 "Left: the tiled wall before stripping — coming off in patches, adhesive lines showing underneath · Right: stripping in progress, tile and adhesive coming away in sheets"),
        ]),
        ("02", "What we recommended: strip it all, then grind what's left smooth", [
            'The crew removed all the tile and adhesive. The render layer that was still firmly bonded to the fibreglass shell stayed, and they <b>ground the whole surface smooth</b> — this is the step that decides how the finished job looks, because PoolArmour is a thin film that follows the surface: wavy render gives a wavy finish, smooth render gives a smooth one.',
            'Then a primer coat of <a href="/en/coreprimer">CorePrimer</a>, soaking into the render and locking down any loose surface, followed by <a href="/en/poolarmour">PoolArmour</a> over the top — a film flexible enough to move with the fibreglass shell, which is exactly where tile fails.',
            pair(4, 5, "Fibreglass pool after stripping, with the render ground smooth over the whole pool", "Pool with the render ground smooth throughout, ready for the system, corner steps visible",
                 "The render after stripping and grinding — floor, walls and steps, ready for CorePrimer and then PoolArmour"),
        ]),
        ("03", "Why grey", [
            'The owner went with grey on our recommendation, because a pool colour empty and a pool colour full of water are two different things — white fills to a bright pale blue, while <b>grey fills to emerald green</b>, the classic shade that suits a garden and the planting around a pool like this best. Both shades under water are shown on the <a href="/en/poolarmour#showcase">PoolArmour</a> page.',
            fig(6, "Finished grey PoolArmour surface with rainwater lying on the pool floor and fallen leaves",
                "Finished, and rain came before the fill — a smooth grey surface over floor and steps; even a thin layer of rainwater starts to show the green"),
        ]),
        ("04", "If your fibreglass pool looks like this", [
            'A fibreglass pool whose original gelcoat is blotchy or faded, or that has been rendered over before — do not tile it, and do not add another render coat. The only surface that works on a shell that moves is a flexible film. Strip the rigid layers, grind the surface smooth, prime with the right primer, then coat. Send us photos of the pool on the page chat and we will tell you how far back it needs to come.',
        ]),
    ],
    prods='<div class="prods"><span class="lbl">Products used in this job:</span><a href="/en/poolarmour">PoolArmour</a><a href="/en/coreprimer">CorePrimer</a></div>\n  <a class="back" href="/en/casestudy/">← Back to all case studies</a>\n',
)


def render(d):
    hero_fig = fig(1, d["hero"][0], d["hero"][1], hero=True)
    steps = "".join(step(n, h2, parts) for n, h2, parts in d["steps"])
    return ("  <article>\n" + f'    <p>{d["intro"][0]}</p>\n' + hero_fig
            + "".join(f"    <p>{p}</p>\n" for p in d["intro"][1:]) + steps
            + "  </article>\n  " + d["prods"])


def transplant(src_path, out_path, title, desc, eyebrow, meta, body_html, og_img):
    h = open(src_path, encoding="utf-8").read()
    h = h.replace(SRC, SLUG)
    h = re.sub(r"<title>.*?</title>", f"<title>{title} | Case Study LucernaPro</title>", h, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title} | Case Study LucernaPro">', h, flags=re.S)
    h = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{og_img}">', h, flags=re.S)
    i = h.find('<main class="wrap">'); j = h.find("</main>")
    crumb = re.search(r'<p class="crumb">.*?</p>', h[i:j], flags=re.S).group(0)
    new_main = ('<main class="wrap">\n  ' + crumb + "\n"
                f'  <span class="eyebrow">{eyebrow}</span>\n'
                f"  <h1>{title}</h1>\n"
                f'  <p class="meta">{meta}</p>\n' + body_html)
    h = h[:i] + new_main + h[j:]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(h)
    print("built:", out_path)


if __name__ == "__main__":
    og = f"https://www.lucernapro.com/img/post/{SLUG}-h1.webp"
    transplant(os.path.join(ROOT, "post", SRC, "index.html"), os.path.join(ROOT, "post", SLUG, "index.html"),
               TH["title"], TH["desc"], TH["eyebrow"], TH["meta"], render(TH), og)
    transplant(os.path.join(ROOT, "en", "post", SRC, "index.html"), os.path.join(ROOT, "en", "post", SLUG, "index.html"),
               EN["title"], EN["desc"], EN["eyebrow"], EN["meta"], render(EN), og)
