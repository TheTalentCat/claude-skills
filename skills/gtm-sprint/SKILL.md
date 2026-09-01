---
name: gtm-sprint
description: >-
  Go-to-market sprint for a product — ICP → positioning & copy in Josh's voice →
  landing page → SEO → outreach. Manual trigger only: /gtm-sprint plus the product.
disable-model-invocation: true
---

# /gtm-sprint — Product Go-To-Market

Runs the marketing motion end-to-end for one product, with Josh's voice and site
standards baked in rather than remembered.

## Phase 1 — ICP & positioning
/icp-modeller for the ideal customer profile. /product-marketing + /senior-product-marketer
for positioning. One-sentence positioning before any copy gets written.

## Phase 2 — Copy, in Josh's voice
Hard rules, not suggestions:
- Headlines and subheadlines are **centered** on every page we design.
- First-person Josh copy: **no dashes, no colons**. Short sentences. Periods.
  Staccato fragments are fine.
- Never diminish the reader. No meta-commentary. Unpack jargon. Short, kind, concrete.
- Run /unslop on everything before it ships.
Use /copywriting frameworks + /content-copy for structure; /copy-editing for the pass.

## Phase 3 — Landing page
Design with /design-consultation or /frontend-design as fits. Run /sculpt before
shipping — the tired-eyed reader test applies to every page. Build Bolt-compatible
when the site lives in Bolt (static assets in public/; never hand-deploy over a
Bolt-managed site — the next Bolt publish stomps it).

## Phase 4 — SEO
Keyword research with the Keywords Everywhere API (key in memory: topics/api-keys.md).
/seo-audit for technical health, /ai-seo for LLM-search visibility, /schema for
structured data. Prioritize by volume × intent, not vanity keywords.

## Phase 5 — Outreach
/cold-email + /outbound-copywriter sequences for the ICP. /directory-submissions for
the cheap wins. Everything outbound is drafted, never sent — **Josh reviews and sends**.

## Rules
- Adan is the marketing expert. When work overlaps his lane (SEO strategy, positioning),
  flag outputs as "ready for Adan's review" rather than final.
- End-to-end proof for anything technical (page live, form delivers, pixel fires).
