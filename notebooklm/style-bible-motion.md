---
uri: "klappy://romance/notebooklm/style-bible-motion"
title: "Style Bible for Motion — Romance by Tata Oro Cinematic Video"
kind: docs
audience: docs
exposure: nav
tier: 1
voice: neutral
stability: draft
tags: [romance, notebooklm, style-bible, motion, video, palette, voice]
date: "2026-08-01"
derives_from: "notebooklm/MANIFEST.md, canon/governance/brand-guide.md §7"
status: "draft — pending Tatiana review"
---

# Style Bible for Motion

> D2 deliverable of `charters/2026-08-01-notebooklm-cinematic-video-package.md`.
> Every rule below traces to a manifest source (see
> `notebooklm/MANIFEST.md`). This governs every prompt in
> `notebooklm/prompt-suite.md`.

## Palette (exact hex, from `canon/governance/brand-guide.md` §7)

| Token | Hex | Motion use |
|---|---|---|
| Ink Black | `#0A0A0A` (pure `#000000` for pack) | base grade, negative space, background of every shot |
| Champagne Gold | `#EAD1AE` | key light on gold accents (script, steam, rim light) |
| Deep Gold | `#C8A26A` | secondary highlights, gold dividers/wipes |
| Butterscotch | `#C39B6E` | warm mid-tones on skin/wood in ritual scenes |
| Cocoa Cream | `#D8C6B0` | muted captions, lower-third text |
| Irish Coffee | `#4A3728` | deep brown shadow fill, wood surfaces |
| Espresso | `#6B4A3B` | brown text-on-cream cards (story-card beat) |
| Cream (body text) | `#EDE3D6` | on-screen caption body copy on black |

Grade every scene toward Ink Black with Champagne/Deep Gold as the only
saturated highlights — matte black / gold / cream / cocoa is the entire
palette. No other hues enter the frame (no blue-hour teal, no red).

## Light

Moody café morning light: low-angle, warm, directional — a single
practical or window source, soft falloff into black. Steam and pour
motion catch rim light in Champagne Gold. Never flat, never bright/
clinical (brand-guide §9 explicitly rules out clinical product-shot
lighting). Reference frame: matte-black bag on dark wood, scattered
roasted beans, burlap, espresso cups, soft directional light.

## Type & on-screen text

Serif elegance for story beats (headline/pull-quote moments): a
high-contrast elegant serif in the spirit of Cormorant Garamond, set in
Cream or Champagne Gold on Ink Black. Tracked-caps geometric sans (Montserrat/
Jost spirit) for taglines and kickers, matching the label's "TWO STORIES.
ONE CUP." treatment — always rendered as complete sentence-unit lines
(see Tagline rule below). No default video-generator fonts; if the model
can't hit the exact face, favor a plain elegant serif over anything
playful, rounded, or condensed.

## Pacing

Slow pour pacing throughout: unhurried, documentary — no fast cuts, no
hype-reel speed-ramping. Let pours, steam, and hands breathe in real
time or slightly slower. This is a love letter, not an ad (brand-guide
§4). Cuts land on emotional beats (a name, a date, a taste word), not on
a music grid.

## Specialty-before-price doctrine, applied to video

The viewer must know this is specialty — hand-picked, small-lot,
named-origin, a real 18+-month ritual — before any price, SKU, or "buy"
beat appears on screen. Every video edit (D4 assembly) sequences story →
sensory/blend beats → bag/product beat → close, with any commerce cue
(price, buy CTA, SKU) held to the very end or omitted entirely from
story-cut videos. This mirrors the ratified Instagram bio's own doctrine
(`notebooklm/sources/instagram-launch-caption.md`): specialty and the
rare varietal lead; price never leads.

## EN/ES bilingual rhythm

Spanish carries the emotional beats — Tatiana's own words, always
delivered in her voice first (per `notebooklm/sources/cafe-tataoro-com-copy.md`).
English carries information — facts, blend components, weights, roast
level. Do not swap these roles: an English line should not be doing
emotional first-telling, and a Spanish line should not be doing pure
spec recitation. On-screen bilingual captions follow the same split —
ES caption for feeling, EN caption for fact — never a literal word-for-
word subtitle of the other language's line.

## Tagline rule (charter constraint #4 — binding)

Taglines render as complete sentence-unit lines, on screen and in
voiceover timing, never broken mid-sentence across a cut or a caption
line-wrap:

There are TWO ratified taglines (per `sources/brand-guide.md` and the
label doc): "Two stories. One cup." and "A Colombian soul. An American
spirit. One beautiful blend." The second is one tagline of three
sentence units; it may render as one line OR split only at sentence
boundaries — as the live registered surfaces themselves do (site meta
description: full triplet on one line; Shopify product description:
split after "spirit.") — never mid-sentence. The permitted sentence-unit
beats are:

- "Two stories. One cup."
- "A Colombian soul. An American spirit."
- "One beautiful blend."

Each one is its own held beat. A line break must fall between these
units, never inside one.

## Cream-metaphor rule (charter constraint #3 — binding)

"Drinks like cream" / «como crema en el café, sin nada de crema» is
Tatiana's own unprompted tasting language (`notebooklm/sources/blind-tasting-provenance.md`,
utt 2653308471/2653308511/2653308513-515). It is rendered ONLY as visual
metaphor — motion, light, and texture that evoke smoothness and body
(slow swirl, warm steam, silky pour arc, gold light catching the
surface). **No literal cream, milk, dairy pour, white liquid, or
cream-in-coffee shot may appear in any generated frame, ever.** Every
pour-adjacent prompt in `notebooklm/prompt-suite.md` restates this rule
inline so it survives prompt reuse outside this document.

## Retired-line exclusion (binding — see MANIFEST retirement notice)

"A special cup of coffee for everyday people" MUST NOT appear in any
on-screen text, voiceover, or caption generated from this style bible or
`notebooklm/prompt-suite.md`. It is retired per the governing charter;
its only permitted appearances in this entire pack are the
retirement-notice banners and bannered verbatim canon text in
`notebooklm/MANIFEST.md`, `notebooklm/sources/brand-guide.md`,
`notebooklm/sources/brand-constraints.md`, and
`notebooklm/sources/label-romance-by-tata-oro.md`, plus the framed
rule-statement quotations in this section, `notebooklm/prompt-suite.md`
(cross-scene reminders), `notebooklm/assembly-instructions.md`
(grounding check), and `notebooklm/sources/cafe-tataoro-com-copy.md`
(live-site absence-verification note). It must never appear in generated output.

## Gate reminder

This style bible is a draft. Customer-facing rendering choices (on-
screen Spanish, taglines-in-context) route through Tatiana; overall
authorial/documentary tone routes through the captain. Nothing here is
cleared to publish.
