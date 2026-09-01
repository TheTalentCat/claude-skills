---
name: ship-feature
description: >-
  Josh's build loop for features on existing products. Manual trigger only:
  /ship-feature plus the feature. Brainstorm gate → plan → isolated workspace →
  execute with verification → review → commit per verified feature →
  end-to-end proof before "done".
disable-model-invocation: true
---

# /ship-feature — The Build Loop

Shipping speed over architectural purity, but never over proof. This is the standard
path from "build X" to a verified, committed feature.

## Phase 1 — Brainstorm gate
/brainstorming (superpowers): intent, requirements, 2-3 approaches with trade-offs
in plain terms. Simplest thing that works wins — no premature abstraction. Design
approved before any code.

## Phase 2 — Plan
/writing-plans: bite-sized steps with exact commands and expected output. For
multi-workstream features, plan the parallel split now (see Phase 3).

## Phase 3 — Workspace discipline
On the default branch? Create a feature branch first. Parallel agents on one checkout
is Josh's normal mode — use /using-git-worktrees for isolation, each worktree with its
own node_modules. Commit early so Bolt exports and other agents can't stomp the work.

## Phase 4 — Execute with verification
/executing-plans or /subagent-driven-development for the work. If the project has a
verification skill (from /create-verification-skill), use it every step. If it's a
project we'll touch again, creating one IS part of this feature's scope.
Isolate volatile external-facing code behind adapters.

## Phase 5 — Review & commit
/requesting-code-review on major chunks. TRUST BUT VERIFY: read subagent diffs before
reporting their work done. Commit after each verified feature, not in one blob at the end.

## Phase 6 — End-to-end proof
Before the word "done": real evidence — rendered UI, HTTP response, DB row, delivered
email. Screenshot or paste it. "Should work" is not a completion state. Document any
gotcha discovered to DECISIONS.md unprompted.

## Rules
- ATOMIC COMPLETION: no manual setup steps left for Josh, or an explicit list of
  exactly what's blocked and why.
- Run /sculpt before shipping anything user-facing that grew during the build.
