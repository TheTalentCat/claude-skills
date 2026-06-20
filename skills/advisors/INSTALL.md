# advisors — Claude Code skill (two advisory boards in one)

- **PRISM** — reviews & scores an idea / pitch / plan / strategy: a 9-expert board,
  Step 0→8, a /100 score, and a verdict.
- **The Billion-Dollar Board** — coaches a *specific* business challenge using the
  frameworks of 8 operators (Hormozi, Cardone, Godin, Gary Vee, Belfort, Brunson,
  Kennedy, Robbins): clarify → route to the right expert → apply their frameworks.

## Install
1. Copy the `advisors/` folder into your Claude Code skills directory:
   - macOS / Linux:  `~/.claude/skills/advisors/`
   - (so you end up with `~/.claude/skills/advisors/SKILL.md`)
2. Start a new Claude Code session (skills load at startup).
3. Invoke it: "advisors", "review my idea", "score this pitch", "board review",
   or "what would Hormozi / Cardone / Godin say about ___".

## Files
- `SKILL.md` — the skill (routes between the two boards).
- `billion-dollar-board.md` — the 8-operator framework library SKILL.md reads.
