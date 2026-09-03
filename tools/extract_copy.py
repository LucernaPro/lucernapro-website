#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_copy.py — ดึง "ข้อความที่คนอ่านเห็น" ของทุกหน้าออกมาเป็นไฟล์ .md เพื่อให้ AI กวาดอ่านตรวจความสมเหตุสมผล
(หัวข้อ h1–h4, ย่อหน้า, แคปชันรูป, alt รูป, ข้อความในตาราง) — ตัด nav/footer/script/style/CSS ทิ้ง

ทำไมต้องมี: เว็บโตจน "อ่านทั้งเว็บ" ในแชทเดียวไม่ไหว ไฟล์นี้ทำให้ตรวจเป็นชุดได้ (ทีละ 5–10 หน้า)
และเปรียบเทียบ TH/EN คู่กันได้ในไฟล์เดียว

วิธีใช้:
  python3 tools/extract_copy.py                 # ทุกหน้า → review/copy/<path>.md
  python3 tools/extract_copy.py paintcoating stonesurface post/feibo-rail-transit   # เฉพาะบางหน้า
  python3 tools/extract_copy.py --since 2026-09-01   # เฉพาะหน้าที่ commit หลังวันนั้น (ใช้ git log)
ผลลัพธ์: review/copy/*.md (ไม่ต้อง commit — โฟลเดอร์ review/ อยู่ใน .gitignore)
"""
import os, re, sys, html, glob, subprocess
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT = "review/copy"

SKIP_TAGS = {"script", "style", "noscript", "svg", "header", "footer", "nav", "aside"}
BLOCK_TAGS = {"h1", "h2", "h3", "h4", "p", "figcaption", "li", "td", "th", "dt", "dd", "blockquote", "summary"}

class Copy(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0; self.buf = None; self.tag = None; self.out = []; self.in_main = False
    def handle_starttag(self, t, attrs):
        d = dict(attrs)
        if t in SKIP_TAGS: self.skip += 1; return
        if self.skip: return
        if t == "img" and d.get("alt"):
            self.out.append(("img", d["alt"].strip()))
        if t in BLOCK_TAGS:
            self.buf = []; self.tag = t
        elif t == "br" and self.buf is not None:
            self.buf.append(" ")
    def handle_endtag(self, t):
        if t in SKIP_TAGS: self.skip = max(0, self.skip - 1); return
        if self.skip: return
        if t in BLOCK_TAGS and self.buf is not None:
            txt = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            if txt: self.out.append((self.tag, txt))
            self.buf = None; self.tag = None
    def handle_data(self, data):
        if self.skip or self.buf is None: return
        self.buf.append(data)

def extract(path):
    h = open(path, encoding="utf-8").read()
    # drop the mobile drawer / topbar / contact / why / explore blocks (shared chrome)
    h = re.sub(r"<!-- ═══ MOBILE DRAWER MENU.*?จบลิ้นชัก MOBILE DRAWER MENU ═══ -->", "", h, flags=re.S)
    h = re.sub(r'<section class="(?:why|explore|contact)">.*?</section>', "", h, flags=re.S)
    p = Copy(); p.feed(h)
    title = re.search(r"<title>(.*?)</title>", h, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)">', h, re.S)
    lines = [f"# {html.unescape(title.group(1).strip()) if title else path}", f"_{path}_", ""]
    if desc: lines += ["> META: " + html.unescape(desc.group(1)), ""]
    seen = set()
    for tag, txt in p.out:
        key = (tag, txt)
        if key in seen: continue
        seen.add(key)
        mark = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "figcaption": "🖼 ", "img": "[alt] ", "li": "- ", "td": "| ", "th": "| "}.get(tag, "")
        lines.append(mark + txt)
    return "\n".join(lines) + "\n"

def pages_since(date):
    out = subprocess.run(["git", "log", f"--since={date}", "--name-only", "--pretty=format:"], capture_output=True, text=True).stdout
    return sorted({l.strip() for l in out.splitlines() if l.strip().endswith("index.html")})

def main(argv):
    if argv and argv[0] == "--since":
        targets = pages_since(argv[1])
    elif argv:
        targets = []
        for a in argv:
            a = a.strip("/")
            for cand in (f"{a}/index.html", f"en/{a}/index.html"):
                if os.path.exists(cand): targets.append(cand)
    else:
        targets = sorted(glob.glob("**/index.html", recursive=True))
    os.makedirs(OUT, exist_ok=True)
    n = 0; total = 0
    for t in targets:
        if not os.path.exists(t): continue
        md = extract(t)
        name = t.replace("/index.html", "").replace("/", "__") or "home"
        with open(os.path.join(OUT, name + ".md"), "w", encoding="utf-8") as f:
            f.write(md)
        n += 1; total += len(md)
    print(f"เขียน {n} ไฟล์ → {OUT}/ ({total//1024} KB รวม) — อ่านตรวจทีละ 5–10 ไฟล์ หรือเทียบ TH/EN คู่กัน")

if __name__ == "__main__":
    main(sys.argv[1:])
