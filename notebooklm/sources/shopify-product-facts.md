---
uri: "klappy://romance/notebooklm/sources/shopify-product-facts"
title: "[SEAT-VERIFIED] Shopify Product Facts — Café Romance by Tata Oro"
kind: docs
audience: docs
exposure: nav
tier: 2
voice: neutral
stability: draft
tags: [romance, notebooklm, source-pack, shopify, product, sku, price, seat-verified]
date: "2026-08-01"
derives_from: "off-repo: Shopify Admin — gid://shopify/Product/9317298208920"
status: active
---

# [SEAT-VERIFIED] Shopify Product Facts

> **Source of record:** Shopify Admin, product
> `gid://shopify/Product/9317298208920`. **Verified live by the dispatch
> seat 2026-08-01T03:21Z.** This container cannot reach `api.github.com`
> or Shopify directly (egress restrictions), so these facts are carried
> verbatim from the seat's verified read — not re-derived.

## Product

- **GID:** `gid://shopify/Product/9317298208920`
- **Status:** ACTIVE
- **Title:** "Café Romance by Tata Oro — Specialty Colombian Coffee ☕"
- **Vendor:** "Romance by Tata Oro"
- **Type:** Coffee
- **Price:** $27.99 USD

## Variants

| Variant | SKU | GID | Qty |
|---|---|---|---|
| Ground | `ROM-COL-12OZ-GRD` | `gid://shopify/ProductVariant/49618530697368` | 99 |
| Whole Bean | `ROM-COL-12OZ-WB` | `gid://shopify/ProductVariant/49618614714520` | 0 (next batch) |

## Photos

- Front (matte black bag): `https://cdn.shopify.com/s/files/1/0705/3744/5528/files/final-front.jpg?v=1785538195`
- Back (label): `https://cdn.shopify.com/s/files/1/0705/3744/5528/files/final-back.jpg?v=1785538195`

> Use these two stills as direct visual reference for the D3 bag-reveal
> prompt — not as a source to re-derive label text from; label text is
> `notebooklm/sources/label-romance-by-tata-oro.md`.

## Product description

- **EN description:** registered on Shopify — Tatiana's EN quote, plus
  Ritual / Blend / First Roast / Insert-card sections, taglines rendered
  as sentence-unit lines (matches `notebooklm/sources/cafe-tataoro-com-copy.md`).
- **ES description:** **NOT REGISTERED on Shopify.** ⚠️ **NAMED GAP** —
  no Spanish-language product description exists on the live product
  listing. Confirmed absent both on Shopify (seat-verified 2026-08-01T03:21Z)
  and in this repo (`originals/`, `canon/` searched, none found). Recorded
  in `notebooklm/MANIFEST.md` as an open gap — nothing invented to fill it;
  D3/D4 prompts must not assume an ES product description exists.

## Cross-check

Price ($27.99) matches `notebooklm/sources/cafe-tataoro-com-copy.md`
(site copy). Retail target in `notebooklm/sources/brand-constraints.md`
recorded ~$25/12oz as of 2026-06-10 — the live $27.99 is the current
ratified price, superseding that earlier target figure (not a conflict,
just a later pricing decision; not in scope for this pack to reconcile
further).
