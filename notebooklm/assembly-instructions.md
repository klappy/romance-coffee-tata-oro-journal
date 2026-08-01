---
uri: "klappy://romance/notebooklm/assembly-instructions"
title: "NotebookLM Assembly Instructions — Romance by Tata Oro Cinematic Video Pack"
kind: docs
audience: docs
exposure: nav
tier: 1
voice: neutral
stability: draft
tags: [romance, notebooklm, assembly, upload-order, meta-prompts, grounding]
date: "2026-08-01"
derives_from: "notebooklm/MANIFEST.md, notebooklm/style-bible-motion.md, notebooklm/prompt-suite.md"
status: "draft — pending Tatiana review"
---

# NotebookLM Assembly Instructions

> D4 deliverable of `charters/2026-08-01-notebooklm-cinematic-video-package.md`.
> Follow this to import the pack into a fresh NotebookLM notebook and
> generate a first storyboard. **Acceptance target: a cold session
> imports the package in under ten minutes and produces a first
> storyboard with zero context questions; every generated claim traces
> to a manifest source.**

## Upload order

Upload in this order so NotebookLM's source list mirrors the pack's own
dependency order (governance → ratified voice → provenance → style →
prompts):

1. `notebooklm/MANIFEST.md` — upload FIRST. It carries the retirement
   notice and the named-gap list; every later source should be read
   against it.
2. `notebooklm/sources/brand-guide.md`
3. `notebooklm/sources/brand-constraints.md`
4. `notebooklm/sources/cafe-tataoro-com-copy.md` — the ratified
   voiceover script; the spine of D3's voiceover timing.
5. `notebooklm/sources/instagram-launch-caption.md`
6. `notebooklm/sources/label-romance-by-tata-oro.md`
7. `notebooklm/sources/shopify-product-facts.md`
8. `notebooklm/sources/brewing-letter-romance-by-tata-oro.md`
9. `notebooklm/sources/back-of-bag-instructions.md`
10. `notebooklm/sources/blind-tasting-provenance.md`
11. `notebooklm/style-bible-motion.md`
12. `notebooklm/prompt-suite.md`

Do NOT upload `charters/2026-08-01-notebooklm-cinematic-video-package.md`
itself or the `streams/` flight log — those are build-process artifacts,
not pack content, and would pollute grounding with meta-commentary about
the pack rather than the pack's substance.

## Notebook structure

- **Notebook name:** "Romance by Tata Oro — Cinematic Video Pack"
- **Source groups (NotebookLM doesn't enforce folders, but tag/label by
  prefix in each source's title for filterability):** Governance (`[EXPORT
  COPY]` items 2–3), Ratified Voice (items 4–5), Provenance (items 6–10),
  Craft (items 11–12).
- After upload, confirm the source count is exactly 12. If NotebookLM
  reports fewer, a file failed to parse — re-upload before running any
  meta-prompt below; a partial source set breaks the grounding
  guarantee.

## Meta-prompts to run inside NotebookLM

Run in this order; each depends on the prior one's grounding being
clean.

### 1. Storyboard generation

> "Using only the uploaded sources, generate a shot-by-shot storyboard
> for a short cinematic video following the six scenes in
> `prompt-suite.md` in order (emigration/what-you-carry → morning ritual
> → roaster beat → the pour → bag reveal → story-card/QR close). For
> each shot, cite which source file supports each factual claim. Flag
> anything you cannot ground in the uploaded sources instead of
> inventing it."

### 2. Audio overview as trailer test

> "Generate an audio overview of this notebook as if it were a trailer
> pitch for the video. Afterward, list every claim made in the audio
> overview and the source file that supports it."

Listen for tone drift (hype-reel language, superlatives, "bold &
smooth"-style clichés) — brand-guide voice rules (§4) forbid these; if
the audio overview drifts into ad-copy tone, that's a grounding failure
even if facts are correct.

### 3. Q&A grounding checks (run all of these — do not skip)

> a. "Does the retired positioning line 'a special cup of coffee for
> everyday people' appear anywhere in the generated storyboard or audio
> overview, outside of a retirement-notice quote in MANIFEST.md or the
> two `[EXPORT COPY]` source files? Answer yes/no and quote the
> location if yes."
>
> **Expected answer: No** (aside from the three retirement-notice
> banners). Any other "yes" is a FAIL — regenerate that shot/beat.

> b. "Does any shot in the storyboard depict literal cream, milk, dairy,
> or a white liquid being poured into or already in the coffee? Answer
> yes/no and cite the shot."
>
> **Expected answer: No.** "Drinks like cream" must remain metaphor only
> (style-bible-motion.md, Cream-metaphor rule). Any "yes" is a FAIL —
> regenerate that shot.

> c. "List every tagline used in the storyboard. For each, confirm it
> renders in complete sentence-unit lines and was never split
> mid-sentence across a cut or caption wrap. The two ratified taglines
> are 'Two stories. One cup.' and 'A Colombian soul. An American
> spirit. One beautiful blend.' — the second may render as one line or
> split only at sentence boundaries, as the live registered surfaces do."
>
> **Expected answer: every sentence unit intact, no mid-sentence split.**

> d. "For each spoken or captioned claim in the storyboard, name the
> exact source file and section it traces to. List any claim that has
> no traceable source."
>
> **Expected answer: an empty 'no traceable source' list.** If anything
> appears there, either find its manifest source or cut the claim —
> never leave it in "because it sounds right."

> e. "Does the storyboard reference a Spanish-language Shopify product
> description, or otherwise assume one exists?"
>
> **Expected answer: No** — per the named gap in `notebooklm/MANIFEST.md`,
> no ES Shopify description exists yet. If the storyboard assumes one,
> that's a grounding failure — regenerate without that assumption.

## Acceptance checklist

- [ ] Exactly 12 sources uploaded, in the order above.
- [ ] Storyboard meta-prompt runs with zero "I need more context"
      responses from NotebookLM.
- [ ] Audio-overview trailer test produces no unsupported claim.
- [ ] All five Q&A grounding checks return their expected answer.
- [ ] Total time from first upload to a passing storyboard: under ten
      minutes.

If any checklist item fails, do not proceed to actual video generation
(Veo/Sora/Runway) — fix the grounding first (usually a missing source
upload or a stale-canon leak) and re-run the failing meta-prompt.

## Gate reminder

Everything this notebook produces is a draft. Route customer-facing
output to Tatiana and authorial-voice/documentary judgment calls to the
captain before anything leaves this pack's boundary.
