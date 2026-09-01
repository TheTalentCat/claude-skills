---
name: new-vertical
description: >-
  The Roster playbook — stand up a new data vertical (source → scrape → clean →
  package → price → pitch). Manual trigger only: /new-vertical plus the vertical.
  Enforces Josh's spend doctrine as a hard gate: paying customer before paid scrape.
disable-model-invocation: true
---

# /new-vertical — The Roster Playbook

The pattern behind ContractorRoster, HealthcareRoster, RetailRoster: public/licensed
data → cleaned and packaged → sold to a buyer who values coverage. This skill runs it
in order with the gates that past mistakes earned.

## Phase 1 — Source identification
Find the authoritative sources (gov registries, license boards, tax portals). Assess:
coverage, freshness, access method, legality/ToS. Known patterns: Akamai-blocked gov
sites yield to python curl_cffi impersonate="chrome"; FAST/GenTax portals need the
window.open hook flow. Check /mem and past DECISIONS.md before solving a solved problem.

## Phase 2 — 🛑 THE SPEND GATE
**No paid scrape, no paid data, no paid API beyond trivial cost until a paying customer
(or signed commitment) exists for this vertical.** This is Josh's $2k Outscraper lesson
and it is not negotiable. Free samples and small test pulls are fine — they are how the
pitch gets built. If tempted, stop and put the decision to Josh with the numbers.

## Phase 3 — Scrape & ingest
Use /scrapling for protected targets. Never discard data that cost money or effort —
raw pulls are archived before any transformation. Idempotent, resumable jobs.

## Phase 4 — Clean & package
Dedupe, normalize, geocode as needed. **Delivery shape mirrors ContractorRoster** —
same file structure, column conventions, and summary sheet, so buyers and tooling
transfer across verticals.

## Phase 5 — Price & pitch
Anchor from the GreenBridge deal (~$4,900 / 800K rows). **Never quote per-record** —
quote per-vertical or per-package. Build the pitch with a real data sample, coverage
stats, and a concrete use case in the buyer's language (/offers and /proposal-writer help).

## Rules
- Raw data is never deleted. Transformations are reproducible from raw.
- Each vertical gets its own project dir with CLAUDE.md + CONTEXT.md + DECISIONS.md.
- Consequential pricing or outreach goes to Josh before send.
