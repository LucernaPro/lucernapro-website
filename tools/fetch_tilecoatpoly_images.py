#!/usr/bin/env python3
"""
Pipeline รูป gallery หน้า /tilecoatpoly — รันจาก root ของ repo:

    pip install pillow requests
    python tools/fetch_tilecoatpoly_images.py

ทำ 3 อย่างตาม SPEC ข้อ 4:
  1. ดาวน์โหลดรูป gallery จาก Wix static (ต้นฉบับเต็ม ไม่เอาเวอร์ชันย่อ)
  2. แปลงเป็น WebP quality 74 กว้างสูงสุด 480px → img/tilecoatpoly-gXX.webp
  3. สลับ src ใน tilecoatpoly/index.html จาก hotlink เป็นไฟล์ local ให้อัตโนมัติ

รันซ้ำได้ (idempotent) — ไฟล์ที่มีอยู่แล้วจะข้าม, src ที่สลับแล้วจะไม่แตะ
"""
import io
import re
import sys
from pathlib import Path

try:
    import requests
    from PIL import Image
except ImportError:
    sys.exit("ติดตั้งก่อน: pip install pillow requests")

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "img"
PAGE = ROOT / "tilecoatpoly" / "index.html"

MAX_W = 480      # SPEC: กว้างสูงสุด 480px
HERO_W = 900     # SPEC: รูปหลักหน้าสินค้า 900px
QUALITY = 74     # SPEC: WebP quality 74

# รูปหลักของหน้า (pack shot จาก hero ของ Wix เดิม) — ตรวจด้วยตาหลังแปลงว่าใช่รูปสินค้าตัวเต็ม
HERO = ("00cbb9_2969ba0a32d749ecbc2e0f749f33b447~mv2.png", "tilecoatpoly-hero.webp")

# media id บน Wix → ไฟล์ปลายทาง (ลำดับตรงกับหน้าเว็บ)
GALLERY = [
    ("00cbb9_fd04cc60cac1492c81b19999062f7cc4~mv2.jpg", "tilecoatpoly-g01.webp"),
    ("00cbb9_eaae2c12b8314abba9752c917b2aa6f4~mv2.jpg", "tilecoatpoly-g02.webp"),
    ("00cbb9_0ba53141016f492cbebe73be9ef06d50~mv2.jpg", "tilecoatpoly-g03.webp"),
    ("00cbb9_bfd9e9cfa51e46d68e29ab921de4b386~mv2.jpg", "tilecoatpoly-g04.webp"),
    ("00cbb9_9c06c3d9562a45b9b953b09e69d0a194~mv2.jpg", "tilecoatpoly-g05.webp"),
    ("00cbb9_29b6a326f51f4998b68e57a7ce62701f~mv2.jpg", "tilecoatpoly-g06.webp"),
    ("00cbb9_a6e35edba14f4de0998e9393ff8d80ae~mv2.jpg", "tilecoatpoly-g07.webp"),
    ("00cbb9_dd329e3ba8474125be6cb19aef5d8ab8~mv2.jpg", "tilecoatpoly-g08.webp"),
    ("00cbb9_c0762e8255a14247a135da5d35ce6237~mv2.jpg", "tilecoatpoly-g09.webp"),
    ("00cbb9_bd9e51d4f78645259adef9a7793aed29~mv2.jpg", "tilecoatpoly-g10.webp"),
    ("00cbb9_e0a7f0db70fc4841ae45020faf18e450~mv2.jpg", "tilecoatpoly-g11.webp"),
    ("00cbb9_097baf9aac494c38abb73cc49c15f180~mv2.jpg", "tilecoatpoly-g12.webp"),
    ("00cbb9_825bbd1bfb6846f797c772ac85b4bb8b~mv2.jpg", "tilecoatpoly-g13.webp"),
]


def fetch_and_convert(media_id: str, out_name: str, max_w: int = MAX_W) -> bool:
    out_path = IMG_DIR / out_name
    if out_path.exists():
        print(f"  skip (มีแล้ว)  {out_name}")
        return True
    url = f"https://static.wixstatic.com/media/{media_id}"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
    except Exception as e:
        print(f"  FAIL download  {out_name}: {e}")
        return False
    im = Image.open(io.BytesIO(r.content)).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    im.save(out_path, "WEBP", quality=QUALITY)
    print(f"  ok  {out_name}  ({im.width}x{im.height}, {out_path.stat().st_size // 1024} KB)")
    return True


def rewrite_page() -> int:
    html = PAGE.read_text(encoding="utf-8")
    swapped = 0

    # 1) gallery: สลับเฉพาะ <img> ที่มี data-local และไฟล์ local มีจริงแล้ว
    pattern = re.compile(r'src="https://static\.wixstatic\.com/[^"]+"(\s+data-local="([^"]+)")')

    def local_exists(rel: str) -> bool:
        # รองรับทั้ง root-relative (/img/x.webp → เทียบจาก root repo) และ relative ปกติ
        return (ROOT / rel.lstrip("/")).exists() if rel.startswith("/") else (PAGE.parent / rel).resolve().exists()

    def repl(m: re.Match) -> str:
        nonlocal swapped
        local_rel = m.group(2)
        if local_exists(local_rel):
            swapped += 1
            return f'src="{local_rel}"'
        return m.group(0)

    html = pattern.sub(repl, html)

    # 2) hero: สลับเป็นตัว 900px เมื่อไฟล์พร้อม
    hero_rel = f"/img/{HERO[1]}"
    if (ROOT / hero_rel.lstrip("/")).exists() and 'src="/img/tilecoatpoly.webp"' in html:
        html = html.replace('src="/img/tilecoatpoly.webp"', f'src="{hero_rel}"', 1)
        swapped += 1

    if swapped:
        PAGE.write_text(html, encoding="utf-8")
    return swapped


def main() -> None:
    if not PAGE.exists():
        sys.exit(f"ไม่พบ {PAGE} — รันจาก root ของ repo")
    IMG_DIR.mkdir(exist_ok=True)
    print("ดาวน์โหลด + แปลงรูป gallery:")
    ok = sum(fetch_and_convert(mid, name) for mid, name in GALLERY)
    print("\nรูปหลัก (hero 900px):")
    hero_ok = fetch_and_convert(HERO[0], HERO[1], max_w=HERO_W)
    print(f"\nรูปพร้อมใช้ {ok}/{len(GALLERY)} + hero {'OK' if hero_ok else 'FAIL'}")
    swapped = rewrite_page()
    print(f"สลับ src ในหน้าเว็บ {swapped} จุด")
    if ok == len(GALLERY) and swapped:
        print("\n✅ เสร็จ — ตรวจหน้าเว็บแล้ว commit ทั้ง img/ และ tilecoatpoly/index.html ได้เลย")
    else:
        print("\n⚠️ ยังไม่ครบ — รันซ้ำได้ หรือเช็ค media id ตัวที่ fail")


if __name__ == "__main__":
    main()
