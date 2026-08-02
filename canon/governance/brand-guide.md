---
uri: "klappy://romance/canon/governance/brand-guide"
title: "Brand Guide — Café Tata Oro / Romance by Tata Oro (Design & Web Source of Truth)"
kind: canon
audience: docs
exposure: nav
tier: 1
voice: neutral
stability: semi_stable
tags: [romance, canon, governance, brand-guide, visual-identity, voice, palette, typography, web, landing-page, bakeoff]
date: "2026-07-03"
status: active
governs: "Design and marketing execution — website, landing page, insert card, social, and all visual/verbal brand application"
derives_from: "canon/governance/brand-constraints.md, canon/governance/project-charter.md, journal/2026-07-03-naming-ruling-cafe-tata-oro.md, originals/label-romance-by-tata-oro.md"
complements: "canon/governance/communication-standards.md"
---

# Brand Guide — Café Tata Oro / Romance by Tata Oro

> The design and web source of truth. This guide **operationalizes** `brand-constraints.md` for designers and builders; where the two ever differ, **`brand-constraints.md` is binding** and this guide yields. Anything in Tatiana's authorial voice or brand feel is subject to her review before publishing.

---

## 1. Brand at a glance

- **House / storefront brand:** **Café Tata Oro** — the shop and audience-facing account. Handle `@cafe.tataoro`; home `cafe.tataoro.com`; inbox `cafe@tataoro.com`.
- **Product (first blend / SKU):** **Romance by Tata Oro** — the coffee itself; the canon-locked name and visual identity live here.
- **Positioning (binding, external):** the ratified tagline pair — *"A Colombian soul. An American spirit. One beautiful blend."* and *"Two stories. One cup."* ⚠️ The former line *"a special cup of coffee for everyday people"* is **RETIRED** — see `brand-constraints.md` § Positioning Line and § Banned Phrases.
- **Essence:** an approachable, romantic, documentary-true Colombian coffee — Tatiana's real daily ritual made into a cup, extended from her established Tata Oro brand.
- **Taglines (on-pack, ratified):** *"Two stories. One cup."* · *"A Colombian soul. An American spirit. One beautiful blend."*
- **One-line boilerplate (EN):** *Romance by Tata Oro is a small-lot Colombian blend — a Colombian soul and an American spirit in one beautiful blend, from Tata Oro.*
- **One-line boilerplate (ES):** *Romance by Tata Oro es una mezcla colombiana de lote pequeño — un alma colombiana y un espíritu americano en una mezcla hermosa, de Tata Oro.*

---

## 2. The story (documentary — never embellished)

Tell it as fact, not marketing. During their dating years, Chris and Tatiana traded "algún día" ("someday") daydreams. After marriage, that someday became a **daily ritual**: chocolate-note coffee with **fresh-ground cinnamon bark** and panela, sustained for **18+ months**. The blend recreates that exact cup, with beans grown near Tatiana's Colombian hometown. Three independent, uncoordinated convergences named the feeling — Chris ("we are sending romance"), Tatiana mid-tasting, and Chris's mother unprompted. **Do not embellish beyond these facts.**

---

## 3. Messaging pillars

1. **The ritual, made pourable** — a real 18-month morning ritual, not a concept.
2. **Two stories, one cup** — a Colombian soul and an American spirit; two people, one blend.
3. **Small-lot, hand-picked, honest** — medium roast, named origins, no inflated claims.
4. **From someone you already trust** — Tata Oro's warmth and taste, extended to coffee.
5. **Everyday luxury** — special but unpretentious; *"A Colombian soul. An American spirit. One beautiful blend."*

> Internal shorthand "approachable luxury" **must not** appear in external copy. The full binding banned-phrase list (including the retired positioning line and "coming soon"/"muy pronto") lives in `brand-constraints.md` § Banned Phrases — copy work checks it before drafting AND greps output against it before presenting.

---

## 4. Voice & tone

- **Bilingual EN/ES**, Colombian-Spanish defaults. Warm, intimate, documentary. Faith- and family-adjacent warmth without preaching.
- **Sounds like:** a heartfelt letter from Tatiana. **Not like:** ad copy, hype, or superlatives.
- **Do:** short, sensory, true sentences; Spanish that feels native, not translated. **Don't:** clichés ("bold & smooth"), fake scarcity, or claims we can't back.
- Anything **signed by or spoken as Tatiana** requires her review of the exact text.

---

## 5. Naming & architecture

| Layer | Name | Where it appears |
|---|---|---|
| House / storefront | **Café Tata Oro** | site, social `@cafe.tataoro`, `cafe.tataoro.com`, packaging house line |
| Product / blend | **Romance by Tata Oro** | bag front, product pages, the SKU |

Rule: the **product** is always "Romance by Tata Oro" with the locked cursive script. The **storefront** is "Café Tata Oro." Never render the product as "Tata Oro Cafe." (Canon note: `brand-constraints.md` still needs a ratified update to encode this house/product split — gated on Tatiana's brand-feel review.)

---

## 6. Logo & brand marks

- **Primary wordmark:** **"Romance"** in the locked gold cursive script + "BY: TATA ORO" beneath. Non-negotiable lettering. On web, use the official artwork asset for the wordmark — **do not substitute a system cursive font** for the logo itself.
- **Brand icon:** the circular mark — coffee **steam forming two faces/silhouettes leaning together**, the heart implied in negative space. **A literal heart graphic must never be used.**
- **Supporting motif:** fine gold **botanical line-art** (coffee branches, leaves, elongated cacao-pod) — used sparingly in corners/margins, never crowding.
- **Clear space & don'ts:** keep generous negative space; never recolor the script off-palette, never place the mark on busy/light backgrounds without the black field, never stretch or add drop shadows.

---

## 7. Color palette (sampled from the production label)

Gold-on-black is the DNA. Hex values below are sampled from the label artwork; treat as web tokens (get final print values from the designer's source file).

| Token | Hex | Role |
|---|---|---|
| **Ink Black** | `#0A0A0A` (pure `#000000` for pack) | primary background |
| **Champagne Gold** | `#EAD1AE` | the "Romance" script, headlines, primary accent |
| **Deep Gold** | `#C8A26A` | gold hover/pressed, dividers, secondary accent |
| **Butterscotch** | `#C39B6E` | warm mid-tone, iconography |
| **Cocoa Cream** | `#D8C6B0` | muted labels, captions |
| **Irish Coffee** | `#4A3728` | deep brown panels, depth on black |
| **Espresso** | `#6B4A3B` | brown text on cream surfaces |
| **Cream (body text)** | `#EDE3D6` | body copy on black (use gold for accents, cream for reading) |

Accessibility: Champagne Gold and Cream both clear AA on Ink Black at body sizes; reserve Deep Gold/Butterscotch for large text or accents (lower contrast).

CSS tokens:
```css
:root{
  --ink:#0A0A0A; --gold:#EAD1AE; --gold-deep:#C8A26A;
  --butterscotch:#C39B6E; --cocoa:#D8C6B0; --irish:#4A3728;
  --espresso:#6B4A3B; --cream:#EDE3D6;
}
```

---

## 8. Typography

- **Logo script:** locked artwork (see §6) — not a font.
- **Headlines (editorial/romantic):** a high-contrast elegant serif — **Cormorant Garamond** (web) — for story headers and pull quotes.
- **UI / labels / taglines:** a clean geometric sans in **ALL CAPS with wide letter-spacing**, matching the label's "TWO STORIES. ONE CUP." treatment — **Montserrat** (or Jost).
- **Body:** Montserrat / system sans, generous line-height, `--cream` on `--ink`.
- **Hierarchy:** oversized serif headline → tracked-caps sans kicker → readable sans body. Let black negative space do the luxury work.

---

## 9. Imagery & art direction

- **Photography:** moody, low-key, warm — matte-black bag on dark wood, scattered roasted beans, burlap, espresso cups, soft directional light (the existing mockup is the reference frame).
- **Graphics:** gold line-art botanicals; the steam-to-couple motif; lots of black negative space.
- **Mood:** intimate, premium, handcrafted — a love letter, not a supermarket shelf.
- **Don't:** bright/clinical product shots, literal hearts, stock "coffee cup on white," heavy filters, clutter.

---

## 10. Packaging system

- **Bag (minimal, ratified):** matte black 12 oz / 340 g stand-up pouch, degassing valve, front wordmark + "Two stories. One cup.", back = blend/origin/roast/grind. **Deliberately spare — the designer kept it minimal.**
- **Insert card (NEW — recovers what the bag couldn't hold):** color-laser-printed in-house, slipped into every bag. Carries **(1) the story, (2) the tasting notes and how they work together, (3) a QR code to `cafe.tataoro.com`.** Because it's printed on demand, copy can iterate without reprinting bags. Card copy is Tatiana-reviewed.
- **The web is the long version:** everything cut from the bag lives fully on the site; the card's QR is the bridge from hand to screen.

---

## 11. Product facts & tasting notes (DRAFT — pending confirmation)

- **Blend:** 70/30 Castillo (washed, "Castillo Chocolate") + Bourbon Rosado Canela. **Origins per label:** Castillo — Cundinamarca; Bourbon Rosado — Huila, Colombia. Roast **Medium**. **12 oz / 340 g.** Whole bean **and** ground (50/50 production).
- **Tasting-note draft:** *Chocolate and panela-caramel from the Castillo base, lifted by a delicate cinnamon-rosado warmth from the Bourbon Rosado — a smooth, medium-bodied cup that finishes like the ritual it came from.* 
- ⚠️ **Reconciliation open:** the label says "Castillo Lavado" / "Bourbon Rosado" while canon says "Castillo Chocolate" / "Bourbon Rosado Canela"; origin wording ("Guayabal de Síquima, Huila") needs a department check. **Finalize tasting notes with the roaster + Tatiana before card/site go live.**

---

## 12. Website / landing-page blueprint (`cafe.tataoro.com`)

**Prime directive:** the site does the **final conversion** — traffic → story → **single-click purchase**. Mobile-first (the funnel is Instagram). Everything routes here (bag QR, card QR, social bio).

**Section flow (long-scroll landing page):**
1. **Hero** — black canvas, gold "Romance" wordmark, *"Two stories. One cup.,"* positioning line, **primary CTA `Buy — $XX` (single click)**, bag hero image, subtle steam motion.
2. **Promise strip** — the positioning line + 3 trust cues (small-lot · hand-picked · medium roast).
3. **The Story** — documentary scroll (someday → daily ritual → the cup).
4. **The Blend & tasting notes** — Castillo + Bourbon Rosado, chocolate + cinnamon, *how they work together* (the recovered content).
5. **Provenance** — Colombia origins, roaster, hand-picked small-lot.
6. **Inside every bag** — the card + QR moment; whole-bean/ground choice.
7. **Trust / creator** — the Tata Oro connection, tasteful; testimonials when available.
8. **Buy block** — single SKU, price, grind toggle (whole/ground), qty, **single-click checkout**; sticky Buy button persists on scroll.
9. **Footer** — EN/ES toggle, `cafe@tataoro.com`, `@cafe.tataoro`, brief story, policies.

**Conversion principles:** one primary CTA (Buy), price visible above the fold, sticky buy bar, minimal checkout friction (single-click via Stripe Payment Link or Shopify), trust signals near CTA, fast load, EN/ES, analytics + QR **UTM** tags.

**Open build decisions:** checkout mechanism (Stripe Payment Link vs. Shopify) and final price — gated on Elkin's pricing.

---

## 13. Bakeoff brief (landing-page concepts)

**Goal:** the best coffee landing page that flows with our story/branding **and** drives traffic + single-click sales. Build competing concepts, then judge against one rubric.

**Proposed concept directions (each honors the locks; differs in art direction):**
- **A · "Editorial Romance"** — story-first, cinematic full-bleed photography, serif headlines, slow emotional scroll; conversion via a persistent sticky buy bar.
- **B · "Luxe Minimal / Product Hero"** — Apple-style focus on the bag, tight copy, maximal black negative space, fastest path to buy; the most conversion-optimized.
- **C · "Warm Ritual / Bilingual Cultural"** — Colombian warmth and texture (burlap, wood, panela), EN/ES front-and-center, creator trust and the ritual foregrounded.

**Evaluation rubric (score each 1–5):** Brand & story fit (locks respected) · Conversion potential (path to single-click) · Premium "wow" · Mobile-first (IG funnel) · Differentiation · Build feasibility.

---

## 14. Governance & review gates

- `brand-constraints.md` is **binding**; this guide operationalizes it.
- **Tatiana** reviews anything in her voice or brand feel (card copy, site copy, taglines-in-context) before publishing; captain ratifies strategy/canon.
- **Open follow-ups:** update `brand-constraints.md` for the house/product split (pending Tatiana); finalize tasting notes; choose checkout + price; define QR UTM.
