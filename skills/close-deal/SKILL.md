---
name: close-deal
description: >-
  Negotiation support with Josh's backstop built in. Manual trigger only: /close-deal
  plus the deal context. Payoff analysis from the counterparty's own numbers,
  credibility assessment of their threats and promises, drafted counters —
  and every consequential counter goes to Josh for review before send. Always.
disable-model-invocation: true
---

# /close-deal — Negotiation Support

Josh named negotiation as a self-identified weak spot and set a standing backstop:
consequential counters get reviewed before send, and leverage gets built from the
counterparty's own numbers. This skill runs that playbook.

## Phase 1 — Frame the game
/game-classifier + /payoff-matrix-builder: what game is this actually? One-shot or
repeated? Who walks away with what if no deal happens (both BATNAs, honestly)?

## Phase 2 — Mine their numbers
Leverage comes from the counterparty's own statements: their quoted prices, volumes,
timelines, constraints. Extract every number they've given and compute what those
numbers imply about their economics. Their numbers, not our guesses, anchor the counter.
(The GreenBridge anchor exists because of this: their ask priced the data.)

## Phase 3 — Assess credibility
/credibility-assessor on their threats, deadlines, and "final offers" — backed by
interest and capability, or cheap talk? /negotiation-strategist and /sales-negotiator
for the tactical read. /bluff-and-deception-analyst if something smells off.

## Phase 4 — Design the counter
Draft 2-3 counter options with expected outcomes: anchor, concession path, and the
walk-away line. Include what we concede cheaply that they value dearly (and vice versa).
For pricing: never per-record, per-package anchoring from prior deals.

## Phase 5 — 🛑 THE BACKSTOP
**Nothing consequential is sent without Josh's review.** Present the recommended
counter, the fallback, and the walk-away line side by side with the reasoning. Josh
edits, approves, and sends. This gate exists at his request; do not soften it even
when he seems rushed — a 2-minute review beats a regretted send.

## Rules
- Model their side as competent and self-interested, not villainous or dumb.
- Track every commitment made across the thread; surface them before each counter.
- Log deal learnings to /mem when they generalize (patterns, not one deal's details).
