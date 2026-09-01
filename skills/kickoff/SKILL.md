---
name: kickoff
description: >-
  New-project scaffold, Josh's way. Manual trigger only: /kickoff plus the project
  name and one-line purpose. Creates the standard project files, git discipline,
  launch config, and memory hooks so every project starts with the same bones.
disable-model-invocation: true
---

# /kickoff — Project Scaffold

Every Josh project gets the same skeleton so agents (and future sessions) always know
where things live. Documents its own absolute path — relative paths have bitten twice.

## What gets created
1. **Project directory** with git initialized and an initial commit.
2. **CLAUDE.md** — project rules: stack, absolute path (C:\ form), LOCKED section
   (empty but present), pointers to CONTEXT.md and DECISIONS.md.
3. **CONTEXT.md** — living status doc: what this is, current state, next milestone.
4. **DECISIONS.md** — append-only log, seeded with the kickoff decision and date
   (absolute dates, never "today").
5. **launch.json entry** (~/.claude/launch.json) if the project has a dev server —
   append, never overwrite; other sessions edit this file too.
6. **Feature-branch discipline** — main stays deployable; work happens on branches.
7. **Verification skill stub** — if the project has a UI or API, run
   /create-verification-skill once the dev loop exists (note it in CONTEXT.md as an
   early milestone, not a someday).

## Build order reminder
Interface → Data → Architecture → Plumbing, and prove the plumbing end-to-end before
polishing the interface.

## Memory hooks
- Project-specific facts → the project's own files, from day one.
- Cross-project learnings → /mem. Never both.
- If the project relates to an existing memory (a prior vertical, a client), link it
  in CLAUDE.md so future sessions load the history.

## Rules
- ATOMIC COMPLETION: the scaffold ends with everything created and committed, plus a
  one-paragraph "how to resume this project in a fresh session" note in CONTEXT.md.
- Ask for the stack only if it isn't obvious from the purpose; default to the
  simplest thing that ships.
