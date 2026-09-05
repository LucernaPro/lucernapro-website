#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_site_search.py — ใส่ช่องค้นหาทั้งเว็บให้ทุกหน้า (ถอนได้: ทุกชิ้นมี marker "sitesearch")

ใส่ 3 ชิ้นต่อหน้า:
1. CSS  `<style id="sitesearch-css">` ก่อน </head>
2. ลิ้นชักมือถือ: ฟอร์มค้นหาใต้ .mnav-tag  (ส่งไป /search?q= หรือ /en/search?q=)
3. topbar เดสก์ท็อป: ลิงก์ 🔍 ก่อนปุ่มสลับธีม (ซ่อนบนมือถือ เพราะลิ้นชักมีช่องอยู่แล้ว)

รันซ้ำได้ — หน้าไหนมีแล้วจะข้าม  ·  แพตช์เทมเพลตใน tools/gen_posts.py ด้วย
วิธีใช้:  python3 tools/add_site_search.py
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

CSS = """<style id="sitesearch-css">
  .mnav-search{margin:12px 0 4px;position:relative}
  .mnav-search input{width:100%;font-family:inherit;font-size:15px;padding:11px 12px 11px 38px;border:1.5px solid var(--line);border-radius:10px;background:var(--panel);color:var(--ink);outline:none}
  .mnav-search input::placeholder{color:var(--muted)}
  .mnav-search input:focus{border-color:var(--orange);box-shadow:0 0 0 3px rgba(237,106,47,.22)}
  .mnav-search svg{position:absolute;left:12px;top:50%;transform:translateY(-50%);width:17px;height:17px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;opacity:.6}
  .topsearch{display:none;align-items:center;gap:6px;font-size:14px;color:var(--muted);white-space:nowrap;text-decoration:none}
  .topsearch svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round}
  .topsearch:hover{color:var(--orange)}
  @media(min-width:861px){.topsearch{display:inline-flex}}
</style>
"""
ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.8-3.8"/></svg>'

def drawer(lang):
    act, ph, lab = ("/en/search", "Search products / case studies…", "Search") if lang == "en" else ("/search", "ค้นหาสินค้า / เคสหน้างาน…", "ค้นหา")
    return (f'  <form class="mnav-search" id="siteSearch" action="{act}" method="get" role="search">'
            f'{ICON}<input type="search" name="q" placeholder="{ph}" aria-label="{lab}" autocomplete="off"></form>\n')

def toplink(lang):
    href, lab = ("/en/search", "Search") if lang == "en" else ("/search", "ค้นหา")
    return f'    <a class="topsearch" href="{href}">{ICON}<span>{lab}</span></a>\n'

def patch(text, lang):
    if 'id="siteSearch"' in text:
        return text, False
    ok = True
    # 1 CSS
    if "</head>" in text:
        text = text.replace("</head>", CSS + "</head>", 1)
    else:
        ok = False
    # 2 drawer — หลังบรรทัด .mnav-tag
    m = re.search(r'[ \t]*<div class="mnav-tag"[^\n]*\n', text)
    if m:
        text = text[:m.end()] + drawer(lang) + text[m.end():]
    else:
        ok = False
    # 3 topbar — หน้าที่มี topnav อยู่แล้ว (โพสต์/เคส/หน้าแรก): ชี้ลิงก์ "ค้นหาสินค้า" ไป /search แทน
    #            หน้าสินค้า (ไม่มี topnav): แทรกลิงก์ 🔍 ก่อนปุ่มธีมเดสก์ท็อป
    href, lab = ("/en/search", "Search") if lang == "en" else ("/search", "ค้นหา")
    nav = re.search(r'<a href="(?:/en)?/?#finder">(ค้นหาสินค้า|Find products|Search products|Search)</a>', text)
    navtag = re.search(r'<nav class="(?:topnav|nav)"', text[:nav.start()]) if nav else None
    if nav and navtag and "</nav>" not in text[navtag.start():nav.start()]:
        text = text[:nav.start()] + f'<a href="{href}">{lab}</a>' + text[nav.end():]
    else:
        m = re.search(r'[ \t]*<button class="theme-toggle" id="themeToggle"', text)
        if m:
            text = text[:m.start()] + toplink(lang) + text[m.start():]
        else:
            ok = False
    return text, ok

def main():
    done = skipped = failed = 0
    for f in sorted(glob.glob("**/index.html", recursive=True)):
        if f.startswith(("node_modules/", "review/", "tools/")):
            continue
        lang = "en" if f == "en/index.html" or f.startswith("en/") else "th"
        t = open(f, encoding="utf-8").read()
        new, ok = patch(t, lang)
        if new == t:
            skipped += 1; continue
        if not ok:
            failed += 1; print("  ⚠ ใส่ไม่ครบ:", f); continue
        open(f, "w", encoding="utf-8").write(new); done += 1
    # เทมเพลตโพสต์
    tp = "tools/gen_posts.py"
    if os.path.exists(tp):
        t = open(tp, encoding="utf-8").read()
        if 'id="siteSearch"' not in t:
            new, ok = patch(t, "th")
            if ok and new != t:
                open(tp, "w", encoding="utf-8").write(new); print("  แพตช์เทมเพลต", tp)
            else:
                print("  ⚠ เทมเพลต", tp, "แพตช์อัตโนมัติไม่ได้ — ต้องใส่มือ")
    print(f"ใส่แล้ว {done} หน้า · มีอยู่แล้ว {skipped} · ไม่ครบ {failed}")

if __name__ == "__main__":
    main()
