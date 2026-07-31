#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_sitemap.py — สร้าง sitemap.xml จากรีโปอัตโนมัติ (LucernaPro)

หลักการ:
- เดินหาทุก index.html ในรีโป แล้วอ่าน <link rel="canonical"> จากหน้าจริง
  → URL ใน sitemap ตรงกับความจริงบนหน้าเสมอ ไม่มีโอกาส drift
- อ่าน hreflang alternates จากหน้าจริง → ใส่เป็น xhtml:link คู่ th/en/x-default
- lastmod = วันที่ commit ล่าสุดของไฟล์ (git log) — อัปเดตเองทุกครั้งที่ regen
- ตัดโพสต์ V1 เก่าที่ถูกถอดจาก /casestudy ออก (doctrine: การ์ดบน /casestudy
  คือแหล่งความจริงว่าโพสต์ไหนใช้ได้ ไม่ใช่รายการโฟลเดอร์ในรีโป)
- URL ภาษาไทยใน path ถูก percent-encode ตามสเปค sitemap

วิธีใช้:  python3 tools/gen_sitemap.py   (รันจากรากรีโป)
"""
import os, re, subprocess, sys
from urllib.parse import quote
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.lucernapro.com"

CANON_RE = re.compile(r'<link\s+rel="canonical"\s+href="([^"]+)"')
ALT_RE = re.compile(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"')


def casestudy_allowed_posts():
    """slug โพสต์ที่มีการ์ดบน /casestudy (แหล่งความจริง)"""
    allowed = set()
    for cs in ("casestudy/index.html", "en/casestudy/index.html"):
        p = os.path.join(ROOT, cs)
        if not os.path.exists(p):
            continue
        html = open(p, encoding="utf-8").read()
        for m in re.finditer(r'href="/(?:en/)?post/([^"]+)"', html):
            allowed.add(m.group(1).rstrip("/"))
    return allowed


def git_lastmod(relpath):
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", relpath],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        return out or None
    except Exception:
        return None


def encode_url(url):
    """percent-encode เฉพาะ path (กัน slug ไทย) คง scheme/host ไว้"""
    if not url.startswith(DOMAIN):
        return url
    path = url[len(DOMAIN):]
    return DOMAIN + quote(path, safe="/")


def main():
    allowed_posts = casestudy_allowed_posts()
    if not allowed_posts:
        print("WARN: อ่านการ์ดจาก /casestudy ไม่ได้ — โพสต์จะไม่ถูกใส่เลย", file=sys.stderr)

    entries = []
    skipped = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
        if "index.html" not in filenames:
            continue
        rel = os.path.relpath(os.path.join(dirpath, "index.html"), ROOT).replace(os.sep, "/")

        # โพสต์: เอาเฉพาะที่มีการ์ดบน /casestudy
        m = re.match(r"^(?:en/)?post/([^/]+)/index\.html$", rel)
        if m and m.group(1) not in allowed_posts:
            skipped.append(rel)
            continue

        html = open(os.path.join(dirpath, "index.html"), encoding="utf-8").read()
        cm = CANON_RE.search(html)
        if not cm:
            skipped.append(rel + "  (ไม่มี canonical)")
            continue
        canon = cm.group(1)
        if not canon.startswith(DOMAIN):
            skipped.append(rel + f"  (canonical ไม่ absolute: {canon})")
            continue

        alts = [(lang, href) for lang, href in ALT_RE.findall(html)
                if href.startswith(DOMAIN)]
        entries.append((canon, alts, git_lastmod(rel)))

    entries.sort(key=lambda e: e[0])

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
             '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for canon, alts, lastmod in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(encode_url(canon))}</loc>")
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        for lang, href in alts:
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{escape(lang)}" '
                f'href="{escape(encode_url(href))}"/>'
            )
        lines.append("  </url>")
    lines.append("</urlset>")

    out = os.path.join(ROOT, "sitemap.xml")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"เขียน sitemap.xml แล้ว: {len(entries)} URL")
    if skipped:
        print("ข้าม:")
        for s in sorted(skipped):
            print("  -", s)


if __name__ == "__main__":
    main()
