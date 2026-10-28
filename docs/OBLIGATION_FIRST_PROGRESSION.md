# Obligation-first progression doctrine

**Approved 2026-10-16.** This governs ongoing post-Horizon Weil-Lab research. The canonical machine-readable authority for the *current research obligation* is [`research/obligations.json`](../research/obligations.json). The Git SHA remains the authority for *what code and certificates actually exist*. Neither authority supersedes mathematical proofs or independent verification.

## Current GitHub custody contract — 2026-10-28

The repository owner has explicitly directed that **every investigation is maintained on GitHub by default, with no per-pass authorization required**. `GOVERNANCE.md` is the authoritative Weil-Lab operational rule. For `NF` or ordinary continuation, make an additive research branch/commit/draft PR with source hashes, scripts and scope-typed evidence as part of the pass; do not leave research silently local. Earlier `NO_TRANSFER` language is superseded. Preserve historical data and do not automatically merge, rewrite source artifacts or promote conditional evidence to theorem closure. This repository-specific rule is not inherited from or overruled by another project's repository contract.

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

Existing RC/SI/SM/LF names, notes, commit SHAs, and certificate hashes are **immutable historical provenance**; do not renumber or rewrite them. The RC `--checkpoint latest` selector means *highest RC validator for an RC replay*, never *current research obligation*. The dedicated obligation workflow reads the manifest's named active checks without inspecting the largest checkpoint number. Checks marked `per-update` replay on governance PRs; expensive retained historical checks marked `on-demand` are explicitly selected by `python scripts/verify_obligation_manifest.py --run-active --deep`. This is not a waiver of original certificate replay, which remains available in its own dedicated workflow.

The [RC204 completion dashboard](RESEARCH_COMPLETION_DASHBOARD.md) and [Horizon research map](RESEARCH_MAP.md) remain historical snapshots until regenerated; they do not select the active frontier. Separate Git branches and PRs remain legitimate implementation isolation, not separate conversational jurisdictions.

## Approval and changes

Changes to `active_obligation`, dependencies, a closure status, or acceptance conditions must carry a reviewed explanation of the evidence and tradeoff. This is a governance change, not a way to relabel a gap as proved. The canonical frontier must be inspected in the same PR; CI rejects incoherent references, missing prerequisites and unsafe active command declarations.

The source of truth is the manifest plus cited, checked proof artifacts. This doctrine deliberately does **not** claim RH, Stage I, whole-original-form positivity or even-sector closure.

## October 23 critical-path acceptance refinement

The original odd-source SI29/SM19 pole-conditioned operator floor and MG21 finite-source analytic positivity make *qualitative* positivity of independently supported finite-source strong-action moments a discharged analytic consequence, conditional on the inherited original physical source domain. Do not advance the canonical obligation by increasing the count of independently verified positive source directions without a proved connection to the genuine original signed-operator 470-source inequality.

Any new computational front must **either** close a presently open original theorem, tighten an actual complete source/negative/residual Loewner term on the SAME source and trial family, prove a correctly scoped method-class ceiling, or provide original-operator domain/inverse/covariance information required by such a term. Checkpoint increments, local eigenvalue signs, trace changes and favorable diagonal source subspaces do not qualify by themselves.

Under [the October 23 critical-path audit](CRITICAL_PATH_RESET_20261023.md), W-ODD-NEG remains open. Its first matched computational preflight is the original full 470-source Galerkin/cap comparison `(51/56)G0-N0cap>0`, retaining all original negative-frequency cap columns, pole, real frequencies and source cross terms. If the fixed cap/trial fails this necessary **method-specific** test, further reduction of its nonnegative inverse-residual charge cannot make the fixed MG07 inequality true. Stop refining that residual, revise the cap or trial, and independently reassess. Even a successful cap-only preflight is NOT signed-operator closure: `DB` and a single uniform rational `t>0` must still satisfy the complete MG07 matrix test, or the exact SM34 original Schur must be separately proved.

Source-domain/physical Fourier identities, strong residuals, exact rational outward enclosures and independent replay remain mandatory; do not promote any branch result to a merged theorem or RH proof without the canonical complete-operator and global transfer conditions.
