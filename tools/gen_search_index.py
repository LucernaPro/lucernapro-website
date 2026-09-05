#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_search_index.py — สร้าง /search-index.json สำหรับช่องค้นหาทั้งเว็บ (/search, /en/search)

แหล่งความจริง (ไม่ต้องดูแลรายการแยก):
- สินค้า  = การ์ดใน index.html / en/index.html  (ชื่อ, คำอธิบาย, data-search, รูป, ลิงก์)
- เคส     = การ์ดใน casestudy/index.html / en/casestudy/index.html  (หัวข้อ, ย่อหน้า, หมวด, สินค้าที่ใช้, รูป, ลิงก์)

วิธีใช้:  python3 tools/gen_search_index.py   (รันจากรากรีโป — รันทุกครั้งที่เพิ่มสินค้า/เคสใหม่)
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def strip(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    return html.unescape(re.sub(r"\s+", " ", s)).strip()

def products(path, lang):
    out = []
    if not os.path.exists(path):
        return out
    t = open(path, encoding="utf-8").read()
    for m in re.finditer(r'<a class="card"[^>]*href="([^"]+)"[^>]*data-search="([^"]*)"[^>]*>(.*?)</a>', t, re.S):
        href, kw, body = m.group(1), m.group(2), m.group(3)
        img = re.search(r'<img[^>]*src="([^"]+)"', body)
        name = re.search(r'class="pname">(.*?)</div>', body, re.S)
        desc = re.search(r'class="pdesc">(.*?)</div>', body, re.S)
        if not name:
            continue
        src = img.group(1) if img else ""
        if src and not src.startswith("/"):
            src = "/" + src
        out.append({"t": "p", "l": lang, "n": strip(name.group(1)), "d": strip(desc.group(1) if desc else ""),
                    "k": strip(kw), "u": href, "i": src})
    return out

def cases(path, lang):
    out = []
    if not os.path.exists(path):
        return out
    t = open(path, encoding="utf-8").read()
    for m in re.finditer(r'<article class="case"[^>]*>(.*?)</article>', t, re.S):
        body = m.group(1)
        href = re.search(r'href="([^"]+)"', body)
        img = re.search(r'<img[^>]*src="([^"]+)"', body)
        cat = re.search(r'<span class="cat[^"]*">(.*?)</span>', body, re.S)
        h2 = re.search(r"<h2>(.*?)</h2>", body, re.S)
        p = re.search(r"<p>(.*?)</p>", body, re.S)
        prods = re.findall(r'class="prods">.*?</div>', body, re.S)
        used = " ".join(strip(x) for x in re.findall(r"<a[^>]*>(.*?)</a>", prods[0], re.S)) if prods else ""
        if not (href and h2):
            continue
        out.append({"t": "c", "l": lang, "n": strip(h2.group(1)), "d": strip(p.group(1) if p else ""),
                    "k": (strip(cat.group(1)) + " " + used).strip() if cat else used,
                    "u": href.group(1), "i": img.group(1) if img else ""})
    return out

def main():
    items = (products("index.html", "th") + products("en/index.html", "en")
             + cases("casestudy/index.html", "th") + cases("en/casestudy/index.html", "en"))
    # กันซ้ำ (การ์ดสินค้าบางใบอาจปรากฏ 2 หมวดบนหน้าแรก)
    seen, uniq = set(), []
    for it in items:
        key = (it["l"], it["u"])
        if key in seen:
            continue
        seen.add(key); uniq.append(it)
    with open("search-index.json", "w", encoding="utf-8") as f:
        json.dump(uniq, f, ensure_ascii=False, separators=(",", ":"))
    n = lambda t, l: sum(1 for x in uniq if x["t"] == t and x["l"] == l)
    print(f"search-index.json: สินค้า TH {n('p','th')} / EN {n('p','en')} · เคส TH {n('c','th')} / EN {n('c','en')}")

if __name__ == "__main__":
    main()
