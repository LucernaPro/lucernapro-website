# lucerna-docs Worker (source copy)
Cloudflare Worker `lucerna-docs` (lucerna-docs.lekvtwin.workers.dev) — ออกเลขเอกสารและเก็บไฟล์ใน GitHub repo `GH_REPO` (LucernaPro/lucerna-accounting).
Vars: `GH_REPO` (text), `GH_TOKEN` (secret, fine-grained PAT Contents r/w), `PIN` (secret).
Deploy: Cloudflare dashboard → Workers & Pages → lucerna-docs → Edit code → paste worker.js → Deploy.
Types: QT / BL / INV (เลขตามเดือนที่คีย์), CA ใบกำกับอย่างย่อ (เลขตามเดือนของวันที่ในใบ).
