---
name: audit
description: >-
  The ball-back pass. Use when Josh returns work for a second look — "revisit this",
  "reflect on what we did", "audit", "take another pass", "double-check our work",
  "is this still right", or when he questions whether earlier claims still hold.
  A structured reverification of standing claims against current reality, drift hunt,
  and leverage-ranked findings. Mutually beneficial: Josh gets verified truth,
  Claude banks durable learnings.
---

# /audit — The Ball-Back Pass

Josh's highest-leverage habit: he hands finished-looking work back and asks for honest
re-examination. This skill makes that pass rigorous instead of vibes-based.

## Phase 1 — Reconstruct the claims
List what was claimed or delivered in the scope under audit. Sources: this session's
statements, CONTEXT.md, DECISIONS.md, recent commits, deployed artifacts. Each claim
gets written down explicitly — "X works", "Y is synced", "Z was removed everywhere".

## Phase 2 — Reverify against reality
**VALIDATE, DON'T THEORIZE.** Every claim is retested by direct observation — run it,
fetch it, diff it, open it. `tsc` passing is not proof. A green result last week is
not a green result now. Label anything unverifiable as UNVERIFIED, never assume it.

## Phase 3 — Hunt drift
Specifically look for what changed underneath the work:
- **Shared-checkout drift** — other agents/sessions modified shared files (launch.json,
  configs, main branch). This happens on Josh's machine; check, don't assume.
- **External drift** — upstream repos moved, Bolt deploys stomped git work, services changed.
- **Loose threads** — anything promised but not delivered end-to-end (atomic completion check).
- **Redundancy & staleness** — duplicated effort, stale docs, assumptions that expired.

## Phase 4 — Leverage-ranked findings
Report findings ordered by impact on Josh's actual goals, each with:
**evidence → implication → recommended action**, tagged:
- `[fixed]` — reversible, in scope, already done this pass
- `[your call]` — consequential or scope-changing; Josh decides
- `[note]` — worth knowing, no action needed

A clean audit is a valid result. Never manufacture findings to look thorough.
Cap at the findings that matter; no exhaustive noise.

## Phase 5 — Close the loop
- Apply the `[fixed]` items and show proof.
- Bank durable learnings in the right scope: cross-project → `/mem save`;
  project-specific → DECISIONS.md. One scope, never both.
- End with one line: what is now stronger because of this pass.

## Rules
- Never re-litigate decisions Josh already made — audit execution, not his calls.
- Findings need evidence from THIS pass, not memory of the last one.
- If the audit scope is unclear, ask one question: "audit what — the session, the
  project, or a specific deliverable?"
