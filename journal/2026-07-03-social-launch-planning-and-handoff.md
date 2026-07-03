---
kind: journals
uri: "klappy://romance/journal/2026-07-03-social-launch-planning-and-handoff"
title: "Session — Social Accounts, Web Home, Naming Cross-Check, Cowork Handoff"
audience: docs
exposure: nav
tier: 2
voice: neutral
stability: stable
tags: [romance, journal, session, social-media, instagram, tiktok, facebook, website, naming, handoff]
date: "2026-07-03"
derives_from: "journal/2026-06-10-governance-baseline.md"
complements: "canon/governance/brand-constraints.md"
status: active
---

# Session — Social Accounts, Web Home, Naming Cross-Check, Cowork Handoff (2026-07-03)

> Reviewed project status, planned the social account slate (FB/IG/TikTok), ruled the web home (`cafe.tataoro.com`, custom build on Cloudflare), sketched homepage structure. Captain cross-checked the naming slate — "Romance Café" was omitted untested. Blind naming test designed and handed off to a Cowork session with native subagents. Still awaiting Elkin's pricing/blending reply.

## Decisions

1. **[D] Web home: `cafe.tataoro.com`**, using the existing tataoro.com domain and email (`cafe@tataoro.com` preferred inbox). Custom page built on Cloudflare Pages now; commerce layer (Stripe link or Shopify) bolted on when Elkin's pricing lands.
2. **[D] Account creation order:** Facebook Page first (Meta foundation) → Instagram Business linked to it → TikTok claimed-but-dormant → Meta Business Suite. Handle consistency across platforms outranks any individual handle; if the primary is taken anywhere, all platforms drop to the fallback together.
3. **[D] TikTok deferred as an active channel** for launch #1 — buyers live in Tatiana's IG audience; TikTok is cold discovery, better for run #2. Handle claimed defensively regardless.
4. **[D] Naming decision deferred pending blind test.** Handle slate under test: `@romancebytataoro`, `@romancecafe` ("Romance Café"), `@romancecafetataoro`, `@romance.tataoro`, `@cafetataoro`.

## Observations

5. **[O] GitHub repos matching the project under klappy:** `romance-coffee-tata-oro-journal` (canonical) and `TataOroWhatsAppGPT` (adjacent Tata Oro brand project).
6. **[O] "Café" reads differently by audience:** physical-coffee-shop connotation in English, but simply "coffee" in Spanish — potentially strong for the Spanish-dominant primary audience. Untested; now part of the blind test design.
7. **[O] Managed-agents dispatch unavailable from this session** — no ANTHROPIC_API_KEY in environment. Cowork's native subagents chosen instead (also a cleaner context break per canon).

## Learnings

8. **[L] Untested assumption caught by captain cross-check:** first officer's original handle slate omitted "Romance Café" without evidence — a naming preference presented as if vetted. Debrief rule: candidate names get enumerated and tested (or explicitly ruled out with a stated reason) before a slate is presented.

## Constraints (existing, reaffirmed in planning)

9. **[C] All audience-facing copy (bios, homepage, story paragraph) carries Tatiana's authorial-voice review** before publishing. Homepage and bio drafts in this session are pre-review drafts only.
10. **[C] Bilingual EN/ES with Colombian Spanish defaults** applies to bios, homepage, and all social profiles.

## Handoffs

11. **[H] Blind naming test → Cowork session.** Full brief delivered in-conversation: two personas (Spanish-dominant Tata Oro follower; cold English coffee buyer), ≥5 blind evaluators per persona per name, scored on memorability / clarity / purchase intent / trust transfer / searchability. Output: ranked recommendation encoded as `klappy://romance/journal/2026-07-03-blind-naming-test`, committed to this repo. Naming ruling remains the captain's.
12. **[H] Homepage build gated** on four planning questions (photography, email-capture backend, EN/ES presentation, story-copy drafting flow) plus naming outcome.

## Opens

13. **[?] Elkin's pricing/blending reply** — still the launch-timeline gate.
14. **[?] Handle availability** — unverifiable until live signup; slate + fallback order defined.
15. **[?] Pre-launch email capture backend** — leaning Cloudflare Worker + D1, undecided.
