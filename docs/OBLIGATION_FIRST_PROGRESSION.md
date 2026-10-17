# Obligation-first progression doctrine

**Approved 2026-10-16.** This governs ongoing post-Horizon Weil-Lab research. The canonical machine-readable authority for the *current research obligation* is [`research/obligations.json`](../research/obligations.json). The Git SHA remains the authority for *what code and certificates actually exist*. Neither authority supersedes mathematical proofs or independent verification.

## Governing principle

Research progression means **discharging, refining or rigorously identifying a theorem obligation** on the path to RH. It does not mean incrementing RC, SI, SM or LF checkpoint numbers. Methods do not own obligations; obligations govern methods.

Four distinct identities must not be collapsed:

1. **Objective** — the final theorem or research goal (RH).
2. **Obligation** — a stable, theorem-shaped missing statement with exact domain, scope and acceptance condition.
3. **Method** — SI, SM, RC, LF or integration; several can attack the same obligation.
4. **Checkpoint** — immutable source/certificate/validator record with its own proof standing and provenance.

## Canonical progression

- **Recover:** Inspect current Git head, the obligation manifest, explicit dependencies, last accepted evidence, active checks and CI results. A chat thread's title or last topic has no priority authority.
- **Select:** Work on the manifest's active obligation, provided it is open and its immediate dependencies are discharged. A reassignment requires an explicit justified manifest change, not a numerical heuristic.
- **Advance:** Pursue the best justified method. Switch SM/SI/RC/LF within the same conversation if the mathematical dependency changes. Record the reason; preserve earlier results.
- **Verify:** Record analytic standing, exact-rational checks, Lean compilation, independent audit and original-object applicability **separately**. CI validates declared checks; it does not establish the unproved final statement.
- **Reconcile:** Each newly accepted result must say whether the active obligation is *closed, narrowed, still open, obstructed,* or *reassigned*. Update evidence and dependencies; never silently promote a conditional theorem.
- **Stop:** An obligation closes only when its exact acceptance condition has been met and the proof is attached to the original object. Passing a proxy threshold, proving an equivalence, producing a smaller residual for a different problem, or obtaining a green workflow does not suffice.

### NF and conversation continuity

An unqualified `NF` instructs a live recovery and one justified advance on the canonical open obligation. A user who explicitly scopes RC/LF/SM or another mathematical task retains that local scope. A method transfer does **not** require a fresh conversation; the next turn should state the active obligation, the chosen method, the basis for the change and whether the missing theorem was actually discharged.

An unqualified `recover` checks repository custody and manifest consistency first. No tool call may be represented as a successful commit, merge, or passing test until it is confirmed. If the manifest or repository is unavailable, report that limitation and do not invent a head or closure.

### Prioritization and pivots

The priority order in the manifest is a **reviewable judgment** and cannot override dependencies or known obstructions. Prefer the highest-value actionable obligation, not the easiest next checkpoint. An immediate method switch is warranted when the current strategy reaches a proved method-class ceiling, a missing dependency, or an independent theorem eliminates the bottleneck.

Promising new structures are valuable only if they produce a verifiable inequality or nontrivial reduction; a reformulation of the acceptance condition is not closure. Avoid both checkpoint-number chasing and conceptual novelty chasing.

### Custody and historical interfaces

Existing RC/SI/SM/LF names, notes, commit SHAs, and certificate hashes are **immutable historical provenance**; do not renumber or rewrite them. The RC `--checkpoint latest` selector means *highest RC validator for an RC replay*, never *current research obligation*. The dedicated obligation workflow reads the manifest's named active checks without inspecting the largest checkpoint number.

The [RC204 completion dashboard](RESEARCH_COMPLETION_DASHBOARD.md) and [Horizon research map](RESEARCH_MAP.md) remain historical snapshots until regenerated; they do not select the active frontier. Separate Git branches and PRs remain legitimate implementation isolation, not separate conversational jurisdictions.

## Approval and changes

Changes to `active_obligation`, dependencies, a closure status, or acceptance conditions must carry a reviewed explanation of the evidence and tradeoff. This is a governance change, not a way to relabel a gap as proved. The canonical frontier must be inspected in the same PR; CI rejects incoherent references, missing prerequisites and unsafe active command declarations.

The source of truth is the manifest plus cited, checked proof artifacts. This doctrine deliberately does **not** claim RH, Stage I, whole-original-form positivity or even-sector closure.
