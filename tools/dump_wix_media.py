#!/usr/bin/env python3
"""
ดูดคลังรูป + เอกสารทั้งหมดจาก Wix เดิม (ก่อน cutover) — รันจาก root ของ repo:

    pip install requests
    python tools/dump_wix_media.py            # ทุกหน้า (55 slug)
    python tools/dump_wix_media.py tilecoatpoly polyurea   # เฉพาะบาง slug

ผลลัพธ์ (โฟลเดอร์ wix_dump/ — อยู่ใน .gitignore ไม่เข้า repo):
    wix_dump/{slug}/{nn}-{media_id}      รูป/ไฟล์ต้นฉบับเต็มความละเอียดของหน้านั้น
    wix_dump/_shared/                    รูปที่โผล่หลายหน้า (โลโก้, icon, footer ฯลฯ)
    wix_dump/manifest.json               แผนที่ slug → ไฟล์ (ให้ Claude เซสชันถัดไปอ่าน)

รันซ้ำได้ (idempotent) — ไฟล์ที่โหลดแล้วข้าม, หน้า fail ค่อยรันใหม่เฉพาะ slug นั้น
"""
import json
import re
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("ติดตั้งก่อน: pip install requests")

ROOT = Path(__file__).resolve().parent.parent
DUMP = ROOT / "wix_dump"
BASE = "https://www.lucernapro.com"
UA = {"User-Agent": "Mozilla/5.0 (LucernaPro migration archiver)"}
SHARED_THRESHOLD = 5   # media id โผล่ตั้งแต่กี่หน้าขึ้นไป = asset ส่วนกลาง

# ทุก slug จาก nav ของ Wix (รวมตัวเลิกขาย 3 ตัวไว้เป็น archive: drypro, goldmine, sightsaver)
SLUGS = [
    # Flooring
    "boundgravel", "epdm", "epoxycoating", "solidfloor", "thermaglaze",
    "creterevive", "patchpro", "levelpro",
    # Wall
    "deepstick", "fillerace",
    # Waterproof
    "tilecoatpoly", "polypro", "polyurea", "exotic", "siliconepro", "deepseal",
    "polyaspartic", "poolarmour", "crystalseal", "compositecore", "aquashell",
    "pmma", "heatshield", "drygard", "spackleflex", "pondmax", "masterseal",
    "epoxycatridge", "epoxygrout", "carbontilegrout",
    # Painting
    "goldmine",
    # Protection Coating
    "schutzfirearm", "splatter", "marineguard", "ghostshield", "offshore",
    "solarpaneldefender", "drypro",
    # เคมีทั่วไป
    "modernfiberglass", "submarine", "flexgrip", "polyasparticadhesive",
    "swiftset", "prolatex", "revival", "ironlock", "denimblack", "blast",
    "anchoringepoxy",
    # Automotive
    "schutznano", "schutznano9h", "americaniron", "nanoceramic", "sightsaver",
    "plastibright",
    # หน้าปริศนาที่ tilecoatpoly เดิมลิงก์ไป — เก็บไว้ด้วยเผื่อมีของ
    "tilegrout-expire",
]

MEDIA_RE = re.compile(r"static\.wixstatic\.com/media/([A-Za-z0-9_]+~mv2[A-Za-z0-9_.]*\.(?:jpe?g|png|webp|gif))")
FILES_RE = re.compile(r"(?:https?://www\.lucernapro\.com)?(/_files/ugd/[A-Za-z0-9_./-]+\.(?:pdf|png|jpe?g))")


def get(url: str, tries: int = 3) -> requests.Response | None:
    for i in range(tries):
        try:
            r = requests.get(url, headers=UA, timeout=40)
            if r.status_code == 200:
                return r
            print(f"    HTTP {r.status_code}  {url}")
        except Exception as e:
            print(f"    retry {i + 1}: {e}")
        time.sleep(1.5 * (i + 1))
    return None


def scan_pages(slugs: list[str]) -> tuple[dict, dict]:
    """คืน (page_media: slug → [ids ตามลำดับในหน้า], counts: id → จำนวนหน้าที่พบ)"""
    page_media: dict[str, list[str]] = {}
    counts: dict[str, int] = {}
    for slug in slugs:
        r = get(f"{BASE}/{slug}")
        if r is None:
            print(f"  FAIL page  /{slug}")
            continue
        ids: list[str] = []
        for m in MEDIA_RE.findall(r.text):
            if m not in ids:
                ids.append(m)
        for f in FILES_RE.findall(r.text):
            if f not in ids:
                ids.append(f)
        page_media[slug] = ids
        for i in set(ids):
            counts[i] = counts.get(i, 0) + 1
        print(f"  scan /{slug}: พบ {len(ids)} ไฟล์")
        time.sleep(0.4)  # สุภาพกับ Wix หน่อย
    return page_media, counts


def download(item: str, dest_dir: Path, order: int) -> Path | None:
    if item.startswith("/_files/"):
        url = BASE + item
        name = f"{order:02d}-doc-{Path(item).name}"
    else:
        url = f"https://static.wixstatic.com/media/{item}"  # ไม่มี transform = original เต็มความละเอียด
        name = f"{order:02d}-{item}"
    dest = dest_dir / name
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    r = get(url)
    if r is None:
        print(f"    FAIL dl  {item}")
        return None
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(r.content)
    print(f"    ok  {name}  ({len(r.content) // 1024} KB)")
    time.sleep(0.3)
    return dest


def main() -> None:
    targets = sys.argv[1:] or SLUGS
    unknown = [s for s in targets if s not in SLUGS]
    if unknown:
        print(f"เตือน: slug นอกสารบบ (จะลองดึงอยู่ดี): {unknown}")
    DUMP.mkdir(exist_ok=True)

    print(f"สแกน {len(targets)} หน้า:")
    page_media, counts = scan_pages(targets)

    shared_ids = {i for i, c in counts.items() if c >= SHARED_THRESHOLD}
    print(f"\nasset ส่วนกลาง (โผล่ ≥{SHARED_THRESHOLD} หน้า): {len(shared_ids)} ไฟล์")

    manifest: dict[str, list[str]] = {}
    for slug, ids in page_media.items():
        own = [i for i in ids if i not in shared_ids]
        print(f"\nโหลด /{slug} ({len(own)} ไฟล์เฉพาะหน้า):")
        saved = []
        for n, item in enumerate(own, 1):
            p = download(item, DUMP / slug, n)
            if p:
                saved.append(p.name)
        manifest[slug] = saved

    print(f"\nโหลด _shared ({len(shared_ids)} ไฟล์):")
    shared_saved = []
    for n, item in enumerate(sorted(shared_ids), 1):
        p = download(item, DUMP / "_shared", n)
        if p:
            shared_saved.append(p.name)
    manifest["_shared"] = shared_saved

    (DUMP / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    total = sum(len(v) for v in manifest.values())
    print(f"\n✅ เสร็จ — {total} ไฟล์ ใน {DUMP}/ พร้อม manifest.json")
    print("หน้าไหนไฟล์ไม่ครบ รันซ้ำเฉพาะ slug นั้นได้เลย เช่น: python tools/dump_wix_media.py polyurea")


if __name__ == "__main__":
    main()
