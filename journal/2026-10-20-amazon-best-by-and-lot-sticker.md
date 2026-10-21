---
kind: docs
uri: "klappy://romance/journal/2026-10-20-amazon-best-by-and-lot-sticker"
title: "Session — Amazon Best-By Date and Lot Number Sticker"
audience: docs
exposure: nav
tier: 2
voice: neutral
stability: stable
tags: [romance, journal, session, amazon, compliance, sticker, best-by, lot, barcode]
date: "2026-10-20"
derives_from: "originals/stickers/compliance/sticker-B-barcode-importer.pdf, journal/2026-08-24-cost-ledger-and-amazon-distributor-pricing.md"
status: active
---

# Session — Amazon Best-By Date and Lot Number Sticker (2026-10-20)

Civil date 2026-10-20 (America/New_York). Amazon's listing review left two
requirements open: an expiration date and a lot number on the unit. Elkin
Gamba (WhatsApp, 2026-10-12) confirmed the batch was roasted, ground and
packaged on **2026-07-23**; 930 prints no expiration or lot, and its policy
is one year as the optimal consumption period, 1–2 years as shelf life
unopened.

## Decisions

- **D1 — Date printed: `BEST BY 01-23-2028`** (18 months from roast).
  Captain's ruling. Inside the roaster's stated 1–2 year shelf life;
  beyond its one-year optimal-period policy. The Amazon check-in math:
  units need more than 90 days of life on arrival, so stock must reach
  FBA by ~2027-10-25; units within 50 days (~2027-12-04) are disposed.
- **D2 — Lot number: `LOT 260723-01`** — roast date YYMMDD + run number.
  Assigned by us; the roaster printed none. Next runs become -02, -03.
  The lot encodes the date so it is self-auditing.
- **D3 — One consolidated sticker, not an add-on.** The compliance sticker
  (3.77 × 1.125 in: SKU, UPC, importer/distributor block, roaster, origin,
  net weight) grows by 0.25 in to 3.77 × 1.375 in and carries one new line:
  `BEST BY 01-23-2028` in 14 pt bold, with `LOT 260723-01 · ROASTED
  07-23-2026` small beside it. Nothing else on the sticker changes.
- **D4 — Build method: overlay, never redraw.** The new sticker is the
  original PDF with text overlaid (`build_overlay.py`), so the barcode,
  guard bars, OCR-B digits and layout are the original vectors untouched.

## Observations

- **O1** — The barcode/importer sticker and its 4×6 sheet from the prior
  session were never committed; they existed only as PDFs on the captain's
  device. Both are now in `originals/stickers/compliance/`. Filing is part
  of landing.
- **O2** — Regenerating the UPC with a barcode library produced a visibly
  different barcode (continuous digits, no split guard bars) and was
  rejected by the captain on sight. Reusing the original vector was the
  fix.
- **O3** — The sticker's SKU reads `TO-ROM-12OZ-GRD`; Shopify's variant SKU
  is `ROM-COL-12OZ-GRD`. Two SKU schemes exist for one product. Not blocking
  Amazon; flagged for reconciliation.
- **O4** — Amazon's published rule (secondary source, ScanPower summary of
  Seller Central) asks for MM-DD-YYYY or MM-YYYY, 36-point minimum, on unit
  and master carton; lot alone is insufficient. The ruled sticker uses
  14 pt. Accepted as a known risk: if check-in enforces the font size, the
  fix is a larger sticker on the same build, not a redesign.

## Learnings

- **L1** — When a print asset already exists and works, extend it; do not
  redesign it. Three redesigned options were rejected before the one
  that kept the original intact was accepted.
- **L2** — Search the repo and past sessions before saying an asset does
  not exist, and when it is missing from the repo, say "not committed"
  rather than "not made."

## Constraints

- **C1** — Compliance sticker content, fonts (Liberation Sans) and barcode
  are locked to `sticker-B-barcode-importer.pdf`; changes are overlays.
- **C2** — Master carton must carry the same best-by date and lot. Not yet
  built.

## Deliverables

- `originals/stickers/compliance/sticker-B-barcode-importer.pdf` — prior
  session's sticker (verbatim).
- `originals/stickers/compliance/sheet-4x6-B-barcode-importer-5up.pdf` —
  prior session's 4×6 sheet.
- `originals/stickers/compliance/sticker-C-bestby-2028-01-23.pdf` — ruled
  sticker, 3.77 × 1.375 in.
- `originals/stickers/compliance/sheet-4x6-C-bestby-2028-01-23.pdf` — 4-up
  on 4×6, stickers butted edge-to-edge with a short tick at each page
  edge marking every seam — no line across the stickers (captain,
  2026-10-21, after two misreads: crop marks, then full-width lines).
- `originals/stickers/compliance/sticker-side-bestby-01-23-2028.pdf` —
  date + lot only, 2 × 0.75 in, for the side of bags that already carry the
  barcode sticker (captain, 2026-10-21). Sheet:
  `sheet-4x6-side-bestby-01-23-2028.pdf`, 2 columns × 8 rows = 16 per 4×6,
  edge ticks per seam. Build: `build_side.py MM-DD-YYYY OUTDIR`.
- `originals/stickers/build/build_overlay.py`, `build_sheet.py` —
  re-rollable: `python3 build_overlay.py ORIGINAL.pdf MM-DD-YYYY OUTDIR`,
  then `python3 build_sheet.py STICKER.pdf OUT.pdf`.

## Opens

- **P1** — Master carton label with date + lot (C2).
- **P2** — SKU reconciliation (O3).
- **P3** — Whole-bean variant sticker (`…-WB`, "WHOLE BEAN") when that
  batch ships.
- **P4** — Confirm in Seller Central whether the listing is flagged
  expiration-dated; that decides whether the 36 pt rule applies (O4).
