---
uri: "klappy://romance/canon/governance/journal-standards"
title: "Journal Standards — DOLCHEO Encoding, URIs, Frontmatter & Logging Procedure"
kind: canon
audience: docs
exposure: nav
tier: 1
voice: neutral
stability: stable
tags: [romance, canon, governance, journal, dolcheo, oddkit, frontmatter, uri, logger]
date: "2026-06-10"
status: active
governs: "How sessions are journaled, encoded, and indexed in this repository"
complements: "LOGGER.md, canon/governance/project-charter.md"
---

# Journal Standards

> How working sessions become durable, indexed canon in this repository.

## Encoding Framework (binding)

- All project decisions, observations, learnings, constraints, handoffs, explores, and opens are encoded via **oddkit encode** using the DOLCHEO framework.
- Encode does NOT persist. Every encode output MUST be saved into a journal entry (or canon file) and committed — `persist_required` is always on the caller.
- Consequential decisions SHOULD pass through oddkit challenge before encoding.

## Repository Structure (binding)

- `canon/governance/` — binding project standards (this tree). Tier 1.
- `journal/` — one dated file per working session, all DOLCHEO types together. Tier 2. Splitting by encoding type (the old `artifacts/{type}/` layout) is deprecated — it did not scale.
- `originals/` — source documents preserved as searchable markdown with frontmatter.
- `creed/` — foundational axioms.
- `LOGGER.md` — reusable prompt for logging future conversations with proper backdating.

## URI Conventions (binding)

- Sessions: `klappy://romance/journal/{YYYY-MM-DD-slug}`
- Governance: `klappy://romance/canon/governance/{slug}`
- Originals: `klappy://romance/originals/{slug}`

## Frontmatter Rule (binding)

- Every markdown file MUST carry a `---`-delimited YAML frontmatter block with at minimum: `uri`, `title`, `kind`, `audience`, `tier`, `tags`, `date`, `status`. Files without it are invisible to the oddkit catalog regardless of content — inline metadata is insufficient.
- **`kind:` is mandatory** (learned 2026-06-10): oddkit resolves kind from frontmatter `kind:` first, then from path prefix — but this repo's prefixes (`journal/` singular, `originals/`, `creed/`) do not match the recognized kind prefixes, so files without explicit `kind:` resolve to no kind and silently drop from the catalog. Use `kind: journals` for sessions, `kind: docs` for originals/README/LOGGER, `kind: canon` for canon and creed.
- Canon files add `kind: canon` and `governs:`. Journal entries add `derives_from:` linking the prior session where applicable.
- References in `derives_from:` / `complements:` MUST point at live paths; stale references to deleted structures are audit failures.

## Logging Procedure (binding)

1. At the end of a working session (or via `LOGGER.md` pasted into any conversation), encode the session's artifacts with oddkit encode.
2. Write one dated journal entry under `journal/` with the session's Decisions, Observations, Learnings, Constraints, Handoffs, and Opens. Backdate to the session date, not the logging date.
3. Set git identity per session (`git config user.email` / `user.name`) before committing — commits fail without it.
4. Commit and push, then verify indexing: `oddkit_catalog` with `knowledge_base_url: https://github.com/klappy/romance-coffee-tata-oro-journal`, `sort_by: date`, `limit: 50`. (`oddkit_version` reports baseline counts only — it cannot verify the overlay.)

## Governance Fetch Rule (binding)

- Sessions operating on this project MUST fetch governance live from this repo at the moment of use via `knowledge_base_url` — never act from a memory or summary of it. Memory may point; canon decides.
