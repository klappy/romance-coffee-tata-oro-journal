---
uri: "klappy://romance/notebooklm/manifest"
title: "NotebookLM Package Manifest — Romance by Tata Oro Cinematic Video Pack"
kind: docs
audience: docs
exposure: nav
tier: 1
voice: neutral
stability: draft
tags: [romance, notebooklm, manifest, video, source-pack]
date: "2026-08-01"
derives_from: "charters/2026-08-01-notebooklm-cinematic-video-package.md"
status: "draft — pending Tatiana review"
---

# NotebookLM Package Manifest

> D1 deliverable of `charters/2026-08-01-notebooklm-cinematic-video-package.md`.
> This manifest lists every file in the pack, its source of record, its
> ratification status, and when it was verified. **Every claim in D2/D3/D4
> must trace back to a row in this table.**

## ⚠️ RETIREMENT NOTICE (read before using any pack file)

The line **"a special cup of coffee for everyday people"** is still
binding text in this repo's canon (`canon/governance/brand-guide.md`,
`canon/governance/brand-constraints.md`) as of 2026-08-01. **The charter
governing this pack (captain, ratified 2026-07-31) RETIRES this line.**
Canon amendment to strike it is pending, tracked separately — this flight
did NOT edit `canon/` files. The line therefore still appears, verbatim, inside the
export copies `notebooklm/sources/brand-guide.md`,
`notebooklm/sources/brand-constraints.md`, and
`notebooklm/sources/label-romance-by-tata-oro.md` (each under its own
retirement-notice banner), and is quoted for rule-statement purposes in
this manifest, `notebooklm/style-bible-motion.md` (Retired-line
exclusion), `notebooklm/prompt-suite.md` (cross-scene reminders), and
`notebooklm/assembly-instructions.md` (grounding check). Those framed
appearances are the ONLY permitted ones. **It MUST NOT appear in any
generated output** — not in on-screen text, not in any prompt output,
not in any caption hook, not in any NotebookLM-generated storyboard,
audio, or answer. `notebooklm/assembly-instructions.md`
includes a Q&A grounding check that specifically tests for this.

## Manifest table

| Pack file | Source of record | Ratification status | Verified-at |
|---|---|---|---|
| `notebooklm/sources/brand-guide.md` | `canon/governance/brand-guide.md` (repo canon) | Canon binding, but carries the retired positioning line — see retirement notice above | Read from repo 2026-08-01T03:25Z |
| `notebooklm/sources/brand-constraints.md` | `canon/governance/brand-constraints.md` (repo canon) | Canon binding, but carries the retired positioning line — see retirement notice above | Read from repo 2026-08-01T03:25Z |
| `notebooklm/sources/instagram-launch-caption.md` | `originals/instagram-launch-caption.md` | **Ratified** — Tatiana ("she loves it") + captain, 2026-07-31 | Read from repo 2026-08-01T03:25Z |
| `notebooklm/sources/label-romance-by-tata-oro.md` | `originals/label-romance-by-tata-oro.md` | Active reference (print-label description); open reconciliation flags carried through unresolved | Read from repo 2026-08-01T03:25Z |
| `notebooklm/sources/brewing-letter-romance-by-tata-oro.md` | `originals/brewing-letter-romance-by-tata-oro.md` | Active (Chris's authorial voice, EN+ES) | Read from repo 2026-08-01T03:25Z |
| `notebooklm/sources/back-of-bag-instructions.md` | `originals/back-of-bag-instructions.md` | Active (EN+ES) | Read from repo 2026-08-01T03:25Z |
| `notebooklm/sources/cafe-tataoro-com-copy.md` | `klappy/cafe-tataoro-com` `public/index.html` @ `8b92d3c` | **Ratified** — voiceover-derived site story; voiceover source Bee transcript 2026-07-31 7:48 PM EDT | **Seat-verified**, byte-identical to live site, live-fetched 2026-08-01T03:20Z (container has no egress to confirm independently) |
| `notebooklm/sources/shopify-product-facts.md` | Shopify Admin `gid://shopify/Product/9317298208920` | Active listing (ACTIVE status); EN description registered, **ES description NOT registered — named gap, see below** | **Seat-verified** live 2026-08-01T03:21Z (container has no egress to confirm independently) |
| `notebooklm/sources/blind-tasting-provenance.md` | Bee conv 8289557 (2026-05-26) + Bee conv 8123017 (2026-05-16) | Primary-source transcript quotes; conv 8289557 has a flagged ASR artifact ("Rosado" → "risotto") | **Seat-verified**, carried verbatim per charter (container has no egress to confirm independently) |

## Named gaps (do not invent — record and route to Tatiana/captain)

1. **No registered Spanish-language Shopify product description.**
   Confirmed absent on the live Shopify listing (seat-verified
   2026-08-01T03:21Z) and absent from this repo's `originals/` and
   `canon/` trees (searched 2026-08-01). The EN description is registered;
   ES is not. Any ES product-page copy needed for the video pack's
   specialty-before-price framing must be freshly drafted and routed
   through the Tatiana gate — it does not exist as a source today.
2. **Label reconciliation flags (inherited, not resolved by this pack).**
   `notebooklm/sources/label-romance-by-tata-oro.md` inherits open
   questions from its source: "Castillo Lavado" (label) vs. "Castillo
   Chocolate" (canon) naming, and origin-department wording for Bourbon
   Rosado (Huila vs. "Guayabal de Síquima, Huila"). Not resolved here;
   flagged so D3 prompts don't silently pick a side.
3. **Retail price drift.** `brand-constraints.md` (2026-06-10) records a
   ~$25/12oz target; the live Shopify price is $27.99. Not a pack
   blocker — the live price is treated as current — but noted so no
   downstream prompt cites the stale $25 figure.

## Gate reminder

Every file in `notebooklm/sources/`, plus D2/D3/D4, is a **draft** for
Tatiana's (customer-facing) and the captain's (authorial voice) review.
Nothing in this pack is cleared to publish. See charter constraint #2.
