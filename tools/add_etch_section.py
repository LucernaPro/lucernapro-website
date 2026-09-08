#!/usr/bin/env python3
"""Add the "อยากให้ทนขั้นสุด" acid-etch surface-prep section (id="etch") to
/poolarmour and /coreprimer (TH + EN), right after the how-to section, and
repoint the existing water-drop notes from "message us first" to the section.
Idempotent: skips a page that already has id="etch".
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

CSS = """
  /* ---------- เปิดผิวปูนด้วยกรดเกลือ (#etch) ---------- */
  .etch{margin:44px 0 0;border-top:1px solid var(--line);background:linear-gradient(180deg, rgba(216,87,28,.07), transparent 45%), var(--panel);padding:50px 0 54px}
  .egate{margin-top:22px;display:grid;grid-template-columns:1fr;gap:12px;max-width:920px}
  @media(min-width:760px){.egate{grid-template-columns:1fr 1fr}}
  .egate>div{border:1px solid var(--line);border-left:3px solid var(--orange);border-radius:12px;background:var(--bg);padding:16px 18px}
  .egate .k{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;color:var(--orange);text-transform:uppercase}
  .egate h4{font-family:var(--disp);font-size:16px;margin-top:5px}
  .egate p{font-size:14px;color:var(--muted);margin-top:5px}
  .egate p b{color:var(--ink)}
  .esteps{margin-top:26px;display:grid;grid-template-columns:1fr;gap:12px;max-width:920px}
  @media(min-width:760px){.esteps{grid-template-columns:repeat(2,1fr)}}
  @media(min-width:1000px){.esteps{grid-template-columns:repeat(4,1fr)}}
  .estep{border:1px solid var(--line);border-radius:12px;background:var(--bg);padding:16px}
  .estep .no{font-family:var(--mono);font-size:12px;color:var(--orange);display:inline-grid;place-items:center;width:30px;height:30px;border:1.5px solid var(--orange);border-radius:50%;background:var(--panel)}
  .estep h4{font-family:var(--disp);font-size:15.5px;margin-top:10px}
  .estep p{font-size:13.5px;color:var(--muted);margin-top:4px}
  .estep p b{color:var(--ink)}
  .echeck{margin-top:22px;max-width:720px;border:1px solid var(--line);border-radius:12px;background:var(--bg);padding:16px 18px}
  .echeck h4{font-family:var(--disp);font-size:16px}
  .echeck ul{margin:8px 0 0 18px;font-size:14px;color:var(--muted)}
  .echeck li{margin-top:4px}
  .echeck li b{color:var(--ink)}
"""

TH = """
<section class="etch" id="etch">
  <div class="wrap">
    <div class="rdtag">SURFACE PREP — เปิดผิวปูนก่อนทา</div>
    <h2 class="sec-h" style="font-size:clamp(24px,3.6vw,32px)">อยากให้ทนขั้นสุด <em>อ่านตรงนี้ก่อนทา</em></h2>
    <p class="sec-sub">ปูนสระที่ฉาบขัดมันจะผิวเรียบปิดสนิท สีซึมลงไม่ได้ ทาแล้วหลุดแน่นอน — ต้องเปิดผิวด้วย<b>กรดเกลือ</b>ก่อน แต่จะต้องทำหรือไม่ต้องทำ ให้หยดน้ำเป็นคนตัดสิน</p>
    <div class="egate">
      <div><div class="k">หยดน้ำ — ซึมหายภายใน 1 นาที</div><h4>ผ่าน — ไม่ต้องล้างกรด</h4><p>ข้ามขั้นตอนข้างล่างได้เลย ไปที่<b>รองพื้น CorePrimer แล้วทา PoolArmour</b>ตามขั้นตอนปกติ</p></div>
      <div><div class="k">หยดน้ำ — เป็นเม็ดหรือค้างอยู่บนผิว</div><h4>ไม่ผ่าน — ต้องล้างกรดตาม 7 ขั้นนี้</h4><p>ทำครบแล้ว<b>หยดน้ำซ้ำอีกครั้ง</b>ต้องซึมถึงจะทาได้ — ถ้าอ่านแล้วไม่เข้าใจ ค่อยทักมาคุย</p></div>
    </div>

    <div class="note" style="margin-top:22px;border-left-color:var(--orange)"><b>ต้องเตรียม:</b> กรดเกลือ (ซื้อได้ทั่วไป) · น้ำสะอาด สายยาง แปรงขัดพื้นด้ามยาว · <b>เบกกิ้งโซดา 1 กก. ต่อสระ 1 สระ</b> · ถุงมือยาง แว่นกันสารเคมี รองเท้าบูท</div>

    <div class="esteps">
      <div class="estep"><span class="no">1</span><h4>ราดน้ำให้ปูนเปียกทั่ว</h4><p>ทำ<b>ก่อนราดกรดเสมอ</b> — ปูนแห้งจะดูดกรดเป็นหย่อม ผิวจะออกมาไม่เท่ากัน</p></div>
      <div class="estep"><span class="no">2</span><h4>ผสมกรด</h4><p>กรดเกลือ <b>1 ส่วน : น้ำ 5 ส่วน</b> — <b>เทกรดลงน้ำ ห้ามเทน้ำลงกรด</b></p></div>
      <div class="estep"><span class="no">3</span><h4>ราดกรดทีละส่วน แล้วขัด</h4><p>จะเห็นฟองฟู่ขึ้นมา <b>ขัดด้วยแปรงตอนกำลังฟู่</b> ประมาณ 5–10 นาที · <b>ถ้าไม่ฟู่</b> = มีคราบน้ำมันหรือสีเก่าปิดหน้าอยู่ กรดไม่ช่วย ต้องขัดหรือล้างคราบออกก่อนแล้วเริ่มใหม่</p></div>
      <div class="estep"><span class="no">4</span><h4>ล้างน้ำแรงๆ ให้ทั่ว</h4><p>ล้างจน<b>ไม่มีฟอง</b>เหลืออยู่</p></div>
      <div class="estep"><span class="no">5</span><h4>ล้างด้วยน้ำเบกกิ้งโซดา</h4><p>เบกกิ้งโซดา <b>1 กก. ต่อน้ำ 20 ลิตร</b> ราดให้ทั่วเพื่อล้างกรดที่เหลือ — <b>ขั้นนี้สำคัญที่สุด</b> ถ้าข้าม สีจะพองภายหลัง</p></div>
      <div class="estep"><span class="no">6</span><h4>ล้างน้ำเปล่าอีกรอบ</h4><p>ล้างให้สะอาด ไม่มีคราบขาวเหลือ</p></div>
      <div class="estep"><span class="no">7</span><h4>ปล่อยแห้งสนิท 2–3 วัน</h4><p><b>ห้ามมีน้ำขัง</b> แล้วค่อยเช็คตามกล่องข้างล่างก่อนรองพื้น</p></div>
    </div>

    <div class="echeck">
      <h4>เช็คก่อนรองพื้น — ต้องผ่านทั้ง 2 ข้อ</h4>
      <ul>
        <li>เอามือลูบผิวปูน ต้อง<b>สากเหมือนกระดาษทรายละเอียด</b> และ<b>ไม่มีผงติดมือ</b></li>
        <li>หยดน้ำต้อง<b>ซึมหายภายใน 1 นาที</b></li>
      </ul>
    </div>

    <div class="warn"><b>⚠ ระวัง:</b> สระเป็นแอ่ง ไอกรดจะกองอยู่ข้างล่าง <b>ทำตอนมีลม</b> อย่าก้มหน้าลงไปดมใกล้ๆ · <b>ห้ามมีคลอรีน</b>หรือน้ำยาฆ่าเชื้ออยู่ในสระตอนราดกรด · กรดกระเด็นโดนตัว ล้างน้ำสะอาดทันที</div>
    <div class="note"><b>ไม่ว่าจะทางไหน</b> — ผ่านหยดน้ำตั้งแต่แรก หรือล้างกรดแล้วผ่าน — <b>ต้องรองพื้นด้วย <a href="/coreprimer" style="color:var(--orange)">CorePrimer</a> ก่อนทา <a href="/poolarmour" style="color:var(--orange)">PoolArmour</a> เสมอ</b> ขั้นนี้ไม่มีข้าม</div>
  </div>
</section>
"""

EN = """
<section class="etch" id="etch">
  <div class="wrap">
    <div class="rdtag">SURFACE PREP — open the concrete before you paint</div>
    <h2 class="sec-h" style="font-size:clamp(24px,3.6vw,32px)">Want it to last as long as possible? <em>Read this before you paint</em></h2>
    <p class="sec-sub">A steel-trowelled pool render is sealed smooth: the paint can't soak in, so it will peel. The surface has to be opened with <b>muriatic acid</b> first — but let a drop of water decide whether you need to.</p>
    <div class="egate">
      <div><div class="k">Water drop — soaks in within 1 minute</div><h4>Pass — no acid wash needed</h4><p>Skip the steps below and go straight to <b>CorePrimer, then PoolArmour</b> as usual</p></div>
      <div><div class="k">Water drop — beads up or sits on the surface</div><h4>Fail — do the 7-step acid wash</h4><p>When you're done, <b>drop water on it again</b>: it has to soak in before you paint — if anything here isn't clear, message us</p></div>
    </div>

    <div class="note" style="margin-top:22px;border-left-color:var(--orange)"><b>You need:</b> muriatic acid (hydrochloric acid, sold at any hardware shop) · clean water, a hose and a long-handled stiff scrubbing brush · <b>1 kg baking soda per pool</b> · rubber gloves, chemical goggles, rubber boots</div>

    <div class="esteps">
      <div class="estep"><span class="no">1</span><h4>Wet the whole surface</h4><p><b>Always before the acid</b> — dry concrete drinks the acid in patches and the surface comes out uneven</p></div>
      <div class="estep"><span class="no">2</span><h4>Dilute the acid</h4><p><b>1 part acid : 5 parts water</b> — <b>pour the acid into the water, never water into acid</b></p></div>
      <div class="estep"><span class="no">3</span><h4>Pour one area at a time and scrub</h4><p>It will fizz — <b>scrub with the brush while it fizzes</b>, about 5–10 minutes · <b>no fizz</b> = oil, grease or old paint is sealing the surface; acid won't help, remove that first and start again</p></div>
      <div class="estep"><span class="no">4</span><h4>Rinse hard with water</h4><p>Rinse until <b>no foam</b> remains</p></div>
      <div class="estep"><span class="no">5</span><h4>Wash with baking-soda water</h4><p><b>1 kg baking soda in 20 litres of water</b>, over the whole surface, to neutralise the leftover acid — <b>the most important step</b>: skip it and the paint will blister later</p></div>
      <div class="estep"><span class="no">6</span><h4>Rinse with clean water again</h4><p>Until it's clean, with no white residue left</p></div>
      <div class="estep"><span class="no">7</span><h4>Let it dry completely, 2–3 days</h4><p><b>No standing water</b> — then run the check below before priming</p></div>
    </div>

    <div class="echeck">
      <h4>Check before priming — both must pass</h4>
      <ul>
        <li>Run your hand over it: it should feel <b>like fine sandpaper</b> and leave <b>no dust on your palm</b></li>
        <li>A drop of water must <b>soak in within 1 minute</b></li>
      </ul>
    </div>

    <div class="warn"><b>⚠ Safety:</b> a pool is a basin — acid fumes collect at the bottom. <b>Work when there's a breeze</b> and don't lean in close · <b>no chlorine</b> or sanitiser anywhere in the pool while you're using acid · acid on skin: rinse with clean water immediately</div>
    <div class="note"><b>Either way</b> — whether the drop passed straight away or passed after the acid wash — <b>prime with <a href="/en/coreprimer" style="color:var(--orange)">CorePrimer</a> before <a href="/en/poolarmour" style="color:var(--orange)">PoolArmour</a>, every time.</b> There is no skipping this step.</div>
  </div>
</section>
"""

# text repoints (old -> new); applied wherever they occur on each page
TH_REPOINT = [
    ("ถ้าน้ำเป็นเม็ดกลิ้งหรือค้างอยู่บนผิวเป็นนาที = ปูนไม่ดูดซึม <b>อย่าเพิ่งซื้อ อย่าเพิ่งทา ทักมาคุยก่อน</b> ถ่ายรูปหยดน้ำนั้นส่งเข้าแชทเพจได้เลย",
     "ถ้าน้ำเป็นเม็ดกลิ้งหรือค้างอยู่บนผิวเป็นนาที = ปูนไม่ดูดซึม (ปูนขัดมันปิดหน้า หรือปูนผสมน้ำยากันซึมเยอะ) <b>อย่าเพิ่งทา — ต้องเปิดผิวด้วยกรดเกลือก่อน <a href=\"#etch\" style=\"color:var(--orange)\">อ่านวิธีทำเองด้านล่าง</a></b> ถ้าอ่านแล้วไม่เข้าใจ ค่อยถ่ายรูปหยดน้ำนั้นส่งเข้าแชทเพจมาคุย"),
    ("ถ้าหยดแล้วน้ำยังเป็นเม็ดกลิ้งอยู่บนผิว = ไม่ผ่าน ทักมาคุยก่อน ·",
     "ถ้าหยดแล้วน้ำยังเป็นเม็ดกลิ้งอยู่บนผิว = ไม่ผ่าน ต้องเปิดผิวก่อน (<a href=\"#etch\" style=\"color:var(--orange)\">วิธีอยู่ด้านล่าง</a>) ·"),
    ("<div class=\"pickrow\"><b>หยดน้ำลงผิวสระแล้วไม่ซึม</b> เป็นเม็ดกลิ้งหรือค้างอยู่บนผิว (ปูนผสมน้ำยากันซึมเยอะ)<span class=\"ans\">→ ทักมาคุยก่อน อย่าเพิ่งซื้อ</span></div>",
     "<div class=\"pickrow\"><b>หยดน้ำลงผิวสระแล้วไม่ซึม</b> เป็นเม็ดกลิ้งหรือค้างอยู่บนผิว (ปูนขัดมันปิดหน้า หรือปูนผสมน้ำยากันซึมเยอะ)<span class=\"ans\">→ เปิดผิวด้วยกรดเกลือก่อน แล้วค่อยรองพื้น — <a href=\"#etch\" style=\"color:var(--orange)\">วิธีทำเองด้านล่าง</a></span></div>"),
]
EN_REPOINT = [
    ("If the drop beads up or sits on the surface for a minute or more, the concrete isn't absorbent: <b>don't buy yet, don't paint yet, message us first</b> and send a photo of that drop.",
     "If the drop beads up or sits on the surface for a minute or more, the concrete isn't absorbent (a sealed trowelled render, or heavy waterproofing admixture): <b>don't paint yet — open the surface with an acid wash first, <a href=\"#etch\" style=\"color:var(--orange)\">the do-it-yourself steps are below</a></b>. If anything there isn't clear, send us a photo of that drop and we'll talk it through."),
    ("if the drop beads up and sits there instead, it fails — message us first ·",
     "if the drop beads up and sits there instead, it fails — open the surface first (<a href=\"#etch\" style=\"color:var(--orange)\">steps below</a>) ·"),
    ("<div class=\"pickrow\"><b>A drop of water doesn't soak in</b> — it beads up or sits on the surface (heavy waterproofing admixture in the pour)<span class=\"ans\">→ Message us first — don't buy yet</span></div>",
     "<div class=\"pickrow\"><b>A drop of water doesn't soak in</b> — it beads up or sits on the surface (a sealed trowelled render, or heavy waterproofing admixture)<span class=\"ans\">→ Acid-wash the surface first, then prime — <a href=\"#etch\" style=\"color:var(--orange)\">do-it-yourself steps below</a></span></div>"),
]

PAGES = [
    ("poolarmour/index.html", TH, TH_REPOINT),
    ("en/poolarmour/index.html", EN, EN_REPOINT),
    ("coreprimer/index.html", TH, TH_REPOINT),
    ("en/coreprimer/index.html", EN, EN_REPOINT),
]

def main():
    for rel, section, repoints in PAGES:
        p = ROOT / rel
        s = p.read_text(encoding="utf-8")
        if 'id="etch"' in s:
            print(f"skip {rel}: already has #etch"); continue
        # css: before the FIRST </style> (page stylesheet)
        s = s.replace("</style>", CSS + "</style>", 1)
        # section: right after the how-to section closes
        m = re.search(r'<section class="howto">.*?\n</section>\n', s, re.S)
        assert m, f"{rel}: howto section not found"
        s = s[:m.end()] + section + s[m.end():]
        n = 0
        for old, new in repoints:
            if old in s:
                s = s.replace(old, new); n += 1
        p.write_text(s, encoding="utf-8")
        print(f"ok {rel}: section added, {n} repoint(s)")

if __name__ == "__main__":
    main()
