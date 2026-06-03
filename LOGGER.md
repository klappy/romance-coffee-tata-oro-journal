# Romance Journal — Conversation Logger

Paste this at the end of any Romance by Tata Oro conversation to log it.

---

## Prompt (copy everything below the line)

---

Log this conversation to the Romance journal repo.

**Repo:** https://github.com/klappy/romance-coffee-tata-oro-journal
**PAT:** (stored in project instructions)
**Conversation start date:** [REPLACE WITH DATE, e.g. 2026-06-02]

**Instructions:**

1. Clone the repo using the PAT from project instructions.
2. Read the existing artifacts to understand what's already recorded.
3. Extract DOLCHEO artifacts from THIS conversation — Decisions, Observations, Learnings, Constraints, Handoffs, Explores, Opens. Only encode what's new (not already in the repo).
4. Create markdown files with oddkit-compatible YAML frontmatter under the appropriate `artifacts/` subfolder. Use the conversation start date in filenames and frontmatter `date` field. URIs follow `klappy://romance/{type}/{slug}` pattern.
5. If the conversation produced deliverables (emails, documents, copy), save the final versions to `originals/` with frontmatter.
6. Update `README.md` current status section if project state changed.
7. Commit with a descriptive message and push.
8. Run `oddkit:oddkit_catalog` with `knowledge_base_url: https://github.com/klappy/romance-coffee-tata-oro-journal` to verify indexing.

**Frontmatter template:**
```yaml
---
uri: "klappy://romance/{type}/{slug}"
title: "{Type} — {Descriptive Title}"
audience: docs
exposure: nav
tier: 2
voice: neutral
stability: stable
tags: [romance, {type}, {relevant-tags}]
date: "{YYYY-MM-DD}"
derives_from: "{path-or-uri-if-applicable}"
complements: "{path-or-uri-if-applicable}"
status: active
---
```

**Do not re-encode** anything already in the repo. Check first.
