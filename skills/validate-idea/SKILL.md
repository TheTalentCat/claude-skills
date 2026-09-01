---
name: validate-idea
description: >-
  Josh's prototype-first idea validation pipeline. Manual trigger only — /validate-idea
  plus the idea. Interrogate demand, score with the advisory board, scan competitors,
  then build a real end-to-end prototype and benchmark it against best-in-class.
  Ends with an explicit tech-readiness and pursue/park/kill verdict.
disable-model-invocation: true
---

# /validate-idea — Prototype-First Validation

Josh validates by building, not by talking. Ideas earn a verdict through a working
prototype benchmarked against the best alternative, then get an explicit
pursue / park / kill call — parked ideas get a written tech-readiness note
("revisit when X becomes possible").

## Phase 1 — Interrogate (cheap kill first)
Run /office-hours forcing questions: demand reality, status quo, desperate specificity,
narrowest wedge, real observations, future-fit. If it dies here, it dies cheap.

## Phase 2 — Board score
Run /advisors (PRISM). Capture the /100 score, verdict, and the three things that
matter most. Below-threshold ideas stop here unless Josh overrides.

## Phase 3 — Competitive scan
Who solves this today, how well, at what price? Identify best-in-class — that is the
benchmark bar for Phase 4. Use /competitor-profiling for real competitors.

## Phase 4 — Build the prototype
Real, end-to-end, ugly is fine. Build order: Interface → Data → Architecture → Plumbing,
and **prove the plumbing end-to-end before polishing anything**. Timebox it. Use real
data, real APIs, real output — no mocked cores.

## Phase 5 — Benchmark & verdict
Put the prototype next to best-in-class on the dimensions that matter (quality, speed,
cost). Then deliver:
- **PURSUE** — beats or credibly reaches the bar; name the wedge.
- **PARK** — right idea, tech or market not ready; write the explicit
  tech-readiness condition that reopens it.
- **KILL** — the demand or the math isn't there; say which and show the evidence.

## Rules
- END-TO-END PROOF before any claim the prototype "works".
- Spend doctrine: no paid data or paid scrape for a prototype — free tiers and samples
  until a paying customer or a PURSUE verdict justifies spend.
- The verdict is a recommendation. Josh makes the call.
