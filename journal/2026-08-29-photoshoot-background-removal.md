# 2026-08-29 — Photoshoot background removal (front + back bag)

## What landed
Captain shot new product photos of the production matte bag (front:
IMG_6068, back with barcode: IMG_6072) for the Amazon listing work.
Backgrounds removed; ten files land in `originals/`:

- `photoshoot-2026-08-29-front-original.jpg` / `-back-original.jpg` — as shot
- `photoshoot-{front,back}-cutout-transparent.png` — alpha cutouts, tight crop, 5% margin
- `photoshoot-{front,back}-cutout-white.jpg` — same crop on pure white (255)
- `photoshoot-{front,back}-square-2000-{white,transparent}.png/jpg` —
  2000×2000 masters, bag at exactly 85% of frame height, centered.
  These are the Amazon-conformant frames (square, ≥85% fill, pure white).

## Method
Deterministic local pixel work (skins-are-disposable applies): rembg with
isnet-general-use; alpha verified on checkerboard; margins verified by
measurement, not eyeball.

## Debrief — one caught defect
First crop used raw-alpha `getbbox()`, which honored a few invisible
alpha≤2 specks and skewed margins 127px vs 886px — bag looked off-center.
Captain caught it. Fix: threshold alpha>8 before bbox, then equal margins.
Lesson: **verify geometry with numbers; previews hide asymmetry.**
Second captain challenge ("is the whitespace sufficient?") surfaced that
margin choice was taste, not spec — resolved by cutting square 85%-fill
masters per Amazon guidance.

## Relation to the slot plan
Slot 1 (MAIN render) and Slot 3 (back render) remain the committed renders.
These photoshoot cutouts are real-product photography — candidate material
for remaining slots or replacement of renders, captain's call, not decided
here.
