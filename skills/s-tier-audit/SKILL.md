---
name: s-tier-audit
description: The S-tier audit framework — evidence-independent, cross-vendor adversarial review for money/data/auth/prod changes. Use PROACTIVELY when reviewing another agent's implementation packet, gating a merge on a revenue or customer-data path, or when Josh says "audit this like A09", "full audit", "pre-merge review", or "s-tier". Codified 2026-09-11 from the ContractorRoster A09 role-swap experiment (Claude auditor × GPT Astra handler).
---

# /s-tier-audit — the framework

Born from the A09 repair cycle: 6 review rounds, findings in both directions,
zero unverified claims accepted. Extends Josh's /audit (the ball-back pass)
from "reverify this session's claims" to "gate another agent's work stream."

## Roles (separation of duties — the foundation)

- **Handler** executes: writes code, runs live infrastructure, collects
  evidence, prepares review packets. Never approves its own work.
- **Auditor** verifies: re-derives all evidence independently, reviews
  diffs, sets gate criteria, records verdicts. Never executes production
  changes in the stream it audits.
- **Josh** decides: business calls (spend, retention, storage, cutover),
  tiebreaks on disagreement, grants all release/deploy authority. A role
  swap or an approval NEVER transfers deploy/spend authority.
- Cross-vendor pairing (different model families for handler and auditor)
  is a deliberate feature: it de-correlates blind spots. Preserve it.

## The five laws

1. **Evidence independence.** Never review the report — review the work.
   Regenerate diffs from the commits and byte-compare against the packet.
   Re-run every test suite yourself in the same checkout. Re-run the full
   CI gate and read its output. A claim about external reality (a schema,
   a provider limit, an order size) gets checked at the source, never
   accepted from prose.
2. **Everything is claims — including yours.** Both agents' assertions are
   claims-to-verify. When your own record is corrected (it will be), write
   the correction into the verdict log as prominently as any finding
   against the handler. The verdict file is a running log of both.
3. **Severity is arithmetic, not adjective.** Before calling a finding
   blocking, compute the real exposure (how far are actual orders from the
   limit? what does the failure cost?). Type every finding: [defect],
   [hazard], [note], [your-call]. A clean pass is a valid result; never
   manufacture findings.
4. **Fail-closed or explain why.** Shipped behavior on any uncertainty
   (provider failure, write error, changed inputs, unknown external
   outcome) must stop and preserve evidence, not guess. Approving code
   that trades availability for correctness requires saying so on the
   record so operators aren't surprised by the first hold.
5. **Approval ≠ release.** Record every approval against an exact SHA.
   Approval permits merge review to proceed; it never authorizes deploy,
   migration, spend, or customer contact. Name what each approval does NOT
   cover.

## Gate scope and depth

The pre-merge gate applies to: **money, data boundaries, auth, production
behavior**. Depth scales with blast radius — a customer-facing surface over
private data gets the closest read (token handling, CSP, grants, bindings,
logging). Review in risk-ordered slices; never accept four slices as one
diff.

## The verdict artifact

One running VERDICT file per work stream, appended per round:
- What was independently verified (named: commands re-run, sources read).
- Findings, typed and ranked, each: evidence → implication → action.
- Concessions and self-corrections, dated.
- What this approval does NOT authorize.
- Open gates, restated every round so nothing silently drops.

## S-tier program requirements (beyond per-diff review)

These make the difference between A and S. Check them per project; the
ones marked (Josh) need operator action, not agent action:
1. **Cross-vendor adversarial pair** on every money/data work stream.
2. **Periodic fully-external audit** — an agent/human party to NEITHER
   role re-audits the finished stack before major cutover (Josh).
3. **Threat-modeling pass** (STRIDE-style: who attacks, from where, with
   what) on each new externally-reachable surface — proactive, not
   defect-prompted.
4. **Verification tooling floor**: property/fuzz tests on parsers and
   identity encodings; dependency + secret scanning on a cadence; the CI
   gate includes drift guards (config↔SQL allowlist class).
5. **Production alerting** on the failure modes audits keep finding:
   dead schedulers, silent job failures, stuck/starved queues, poisoned
   rows (Josh approves the alert channel).
6. **Live-evidence discipline**: read-only first, screenshots/query
   results archived to the packet, UTC timestamps, correlation caveats
   stated. Root causes stay "unresolved" until evidence closes them —
   an honest unresolved beats an invented mechanism.

## Anti-patterns (each one burned us once)

- Trusting your own extraction/regex as ground truth for coverage claims
  (missed fanout tables; the handler's config-evaluated guard was right).
- Sizing from a benchmark you didn't control (the 40 rec/s cache mirage).
- Inventing a mechanism to close an incident narrative (the ingress-kill
  postmortem). Say "unresolved."
- Letting "both agents agree" substitute for verification — agreement is
  cheap; evidence is the product.
- Scrubbing your own wrong record instead of handing it to the next
  reviewer as claims-to-verify.
- Accepting "covered by tests" without checking the fixture matches the real
  producer's output. A stand-in fixture (a plain 1-line CSV header where the
  real generator emits a metadata preamble first) proves nothing about
  production — it can pass while the real path is broken. Verify the fixture
  shape, not just the assertion. (A09 split-header defect, 2026-09-14.)
