---
kind: journals
uri: "klappy://romance/journal/2026-07-03-landing-page-bakeoff-handoff"
title: "Handoff — Landing-Page Bakeoff for Claude Design Mode (3 concepts, Shopify checkout)"
audience: docs
exposure: nav
tier: 2
voice: neutral
stability: stable
tags: [romance, journal, handoff, bakeoff, landing-page, website, design-mode, shopify, conversion]
date: "2026-07-03"
derives_from: "canon/governance/brand-guide.md, journal/2026-07-03-insert-card-website-and-brand-guide.md"
complements: "canon/governance/brand-constraints.md, originals/label-romance-by-tata-oro.md"
status: active
---

# Handoff — Landing-Page Bakeoff for Claude Design Mode

> **For a fresh Claude Design-mode session.** Build a **3-concept bakeoff** of landing pages for `cafe.tataoro.com`. All three honor the same brand and content; they differ in art direction. Checkout is a **Shopify buy button** with single-click purchase. Judge with the rubric at the end. This brief is self-contained, but fetch live canon before building.

## Fetch first (source of truth)

Pass `knowledge_base_url: https://github.com/klappy/romance-coffee-tata-oro-journal` to oddkit and read:
- `klappy://romance/canon/governance/brand-guide` — palette, type, voice, imagery, page blueprint (primary reference).
- `klappy://romance/canon/governance/brand-constraints` — **binding** locks (name, visual identity, positioning line).
- `klappy://romance/originals/label-romance-by-tata-oro` — packaging transcription + asset paths.
- `klappy://romance/journal/2026-07-03-naming-ruling-cafe-tata-oro` — house/product architecture.

## Mission

The site does the **final conversion**: **traffic → story → single-click purchase.** Everything (bag QR, insert-card QR, social bio) routes here. It must look like the best coffee website and flow with the story.

## Audience & priorities

- **US market, ~50/50 English/Spanish.** Bilingual EN/ES (Colombian-Spanish defaults), toggle or parallel copy.
- **Mobile-first** — the funnel is Instagram (Tata Oro's ~200k). Design mobile → up.
- Primary KPI: **single-click purchase conversion.** Secondary: story immersion, email capture.

## Brand snapshot (standalone summary — full detail in brand-guide)

- **House brand:** Café Tata Oro (`@cafe.tataoro`, `cafe.tataoro.com`). **Product/SKU:** Romance by Tata Oro (locked gold cursive script).
- **Positioning (binding):** "A special cup of coffee for everyday people." **Taglines:** "Two stories. One cup." · "A Colombian soul. An American spirit. One beautiful blend."
- **Palette (sampled):** Ink Black `#0A0A0A` · Champagne Gold `#EAD1AE` · Deep Gold `#C8A26A` · Cocoa Cream `#D8C6B0` · Irish Coffee `#4A3728` · Cream body `#EDE3D6`. Gold-on-black DNA.
- **Type:** locked script wordmark (use artwork, not a font) · serif headlines (Cormorant Garamond) · tracked-caps sans for labels/UI (Montserrat) · sans body.
- **Marks:** circular steam-forming-two-faces icon (heart in negative space — **never a literal heart**); gold botanical line-art, used sparingly.
- **Story (documentary, do not embellish):** "someday" daydreams → an 18-month daily ritual of chocolate-note coffee + fresh-ground cinnamon bark + panela → the blend recreates that cup, grown near Tatiana's hometown.

## Required page sections (all concepts)

1. Hero — gold wordmark, "Two stories. One cup.", positioning line, **primary Buy CTA (single click)**, bag hero image, subtle steam motion.
2. Promise strip — positioning line + trust cues (small-lot · hand-picked · medium roast).
3. Story — documentary scroll.
4. The blend & **tasting notes** (the content cut from the bag — chocolate + cinnamon/rosado, how they work).
5. Provenance — Colombian origins, roaster, small-lot.
6. Inside every bag — the insert card + QR; whole-bean/ground choice.
7. Trust / creator — the Tata Oro connection (tasteful), testimonials when available.
8. **Buy block** — single SKU, price, grind toggle (whole/ground), qty, **Shopify single-click checkout**; **sticky Buy bar** on scroll.
9. Footer — EN/ES toggle, `cafe@tataoro.com`, `@cafe.tataoro`, policies.

## Checkout (ratified: Shopify)

- Integrate the **Shopify Buy Button SDK** (buy-button-js) or product embed; enable **dynamic "Buy now"** for true single-click checkout.
- Single SKU with a **grind variant** (Whole bean / Ground). Use placeholder `storefrontAccessToken` / `productId` / `variantId` until the store is live.
- Keep checkout friction minimal; surface price + Buy above the fold and in the sticky bar.

## The three concepts to build

- **A · Editorial Romance** — story-first; cinematic full-bleed photography; serif headlines; slow, emotional scroll; conversion via persistent sticky buy bar. Most brand-romantic.
- **B · Luxe Minimal / Product Hero** — Apple-style focus on the bag; maximal black negative space; tight copy; fastest path to buy. Most conversion-optimized.
- **C · Warm Ritual / Bilingual Cultural** — Colombian warmth and texture (burlap, wood, panela); EN/ES front-and-center; the ritual and creator trust foregrounded. Most audience-native.

Each is a distinct, self-contained page; shared content, different art direction, layout, and motion.

## Assets (in repo `originals/`)

- `label-romance-by-tata-oro.pdf` + `-front.png` / `-back.png` — label artwork/renders (usable for hero/product imagery).
- Bag mockup (styled product render, front+back) — **pending re-upload** by the captain; leave a slot for it.
- Wordmark/logo vector — request from the designer (currently only within the label artwork).

## Locks & review gates (do not violate)

- Product name "Romance by Tata Oro" with locked cursive script; **never "Tata Oro Cafe."** Never a literal heart. Positioning line is mandatory. Keep gold-on-black.
- **All copy is DRAFT pending Tatiana's authorial-voice + brand-feel review** before publishing. Tasting notes are **draft/unconfirmed** (Castillo "Lavado" vs "Chocolate"; Bourbon Rosado "Canela"; origin wording) — label them provisional.

## Evaluation rubric (score each concept 1–5)

Brand & story fit · Conversion potential (path to single-click) · Premium "wow" · Mobile-first (IG funnel) · Differentiation · Build feasibility. Recommend a winner with reasons; the captain rules.

## Open decisions to resolve during/after the bakeoff

- Final **price** (gated on Elkin) and Shopify store/product setup (tokens/IDs).
- **Tasting-note copy** finalized with roaster + Tatiana.
- **QR target + UTM** for the insert card.
- Photography: use existing mockup renders + shoot/generate additional lifestyle imagery.

## DOLCHEO

- **[H]** Landing-page bakeoff handed to Claude Design mode: 3 concepts (Editorial Romance / Luxe Minimal / Warm Ritual-Bilingual), Shopify single-click checkout, mobile-first EN/ES, against the brand guide; winner chosen via the rubric; captain rules.
- **[D]** Checkout mechanism = **Shopify buy button** (single-click "Buy now").
- **[D]** All three art directions compete in the bakeoff.
