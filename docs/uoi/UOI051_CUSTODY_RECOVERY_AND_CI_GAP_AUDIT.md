# UOI051 — Recovery audit: UOI049/UOI050 repository custody and unresolved gates

**Date:** 2026-11-21 PT. **Type:** corrective custody record; NOT a new accepted theorem.

## Repository action and scope

The UOI049 and UOI050 analytic notes, elementary checkers, and exact-arithmetic receipts were initially emitted only as conversation artifacts, contrary to the project's GitHub-first research custody practice. This branch records those six files without promoting their mathematical claims. Both checkers replayed locally with `python`, reporting PASS on their explicitly narrow checks. The two checkers were subsequently adapted to write their receipts under the repository-relative `research/unified/receipts/` path instead of the nonportable conversation-only `/mnt/data/` path; locally tested copies reproduced the original JSON byte-for-byte. The source history preserves the initial received code as separate commits. The original analytic obligations remain open.

The accepted numerical frontier remains the independently reconciled **708/968** in issue #761 / #898; this branch does not change any accepted certificate or Lean theorem.

## Operational correction

The blanket CI research hold was explicitly **expired on 2026-11-21** by issue #834. The incident still documents lineage-specific uncontrolled PR fan-out, workflow validity, and generated Lake manifest ordering risks. Controlled research commits are authorized; full old NF/IV workflow trees must not be imported into `main`.

The four actual `main` workflows were fetched before this PR:
- `lean.yml`: source paths `lean-toolchain`, `lakefile.toml`, `lake-manifest.json`, `WeilDefect.lean`, `WeilDefect/**`, and itself.
- `formalization-metadata.yml`: `formalization.yaml` and itself.
- `uoi030-source-pinned-single-lane.yml`: only a dedicated `verification/uoi030/UOI030_ONE_SHOT_COMPILE_20261121.txt` push path or explicit manual dispatch.
- `rpb108-manual.yml`: manual dispatch only.

None of this branch's `docs/uoi/intake/`, `scripts/uoi/`, and `research/unified/receipts/` paths matches those automatic triggers. Expected heavy automatic PR fan-out: zero on this particular `main` lineage. This is an exact path-filter assessment, NOT a live Actions receipt or proof that historical branches are repaired.

The separate `governance/uoi000-unified-operative-investigation` branch diverged from `main` (36 ahead / 2 behind as observed). It contains an older `research/unified/obligations.json` execution policy of `consolidation_hold`; the later issue #834 controls the *blanket* hold, while per-lineage verification remains necessary. Do not silently overwrite the existing manifest or treat stale control-plane fields as current prohibitions.

## Mathematical defects / unpaid checks

1. **Geometry/source:** UOI049's exact `8`-adic collar centers and widths are a stated **assumption**, not independently matched to the original source/test family. All prime-power resonance results depending on that geometry are conditional.
2. **Source-to-native:** Exact Hermitian mixed-prime coefficient, first-slot conjugation, both `± log n` shifts, Gamma normalization, both crossed poles, and common-domain bridge remain unpaid.
3. **Gamma space:** The UOI045/UOI048 Gamma coercivity and completed infinite-tail Gamma carrier were not independently re-certified by these two scripts. The UOI049 local compactness and `beta_M` resonance lower bound rely on exact equivalence/regularity hypotheses.
4. **Compactness:** Neither a uniform `Gamma`-normalized prime operator bound nor the tail norm limit is proved; the UOI050 prime-number-theorem estimate is only fixed-smooth-head (or finite-dimensional head) and loses a derivative.
5. **Tail positivity:** No positive infinite-tail `tau_M`, sufficiently small upper bound on `beta_M`, nor Schur closure `(beta_M + kappa_M)^2 < alpha_M tau_M` is certified.
6. **Checker coverage:** UOI049 checks only rational prime-contact spacing; UOI050 checks symbolic derivative, three moment cancellations and collar scaling. Neither checks PNT, infinite operator norms, source identity, Lean, or RH. UOI050's polynomial precursor is only finitely differentiable after zero extension; do not describe it as a Schwartz test.
7. **Preceding UOI048 custody only partly recovered:** The issue/PR search for UOI048, UOI049, and UOI050 found no matching repository issue/PR before this recovery. This branch now includes the independently recovered UOI048 exact-rational checker and its original receipt, plus a clearly labelled summary from the user's report. The **complete mathematical derivation and source-defined collar geometry were not recovered**, and require independent source-bound intake. Do not fabricate their full proof from an executive summary.

## Acceptance / next actions

- Review the exact six source files and their statuses; treat this as **research custody only**.
- Reconcile with the separate UOI governance controller through a reviewed append-only intake; do not assume cherry-pick compatibility between diverged branches.
- Independently recover the full UOI048 analytic derivation and verify the earlier UOI045–047 source ancestry. UOI048's exact checker and receipt are now present, but certify only arithmetic. Record unpaid theorem nodes without displacing F40 → F41 → F42 priorities.
- Independently validate original collar geometry and mixed form, then seek a `Gamma`-uniform arithmetic square-function or operator estimate.
- Before *any* heavy Lean submission on a particular old research branch, audit that branch's effective workflow fan-out and Lake setup ordering. Nothing in this custody PR triggers heavy Lean.

**Evidence status:** repository custody corrected; analytic hypotheses unpromoted; original numerical 708/968 unchanged; unrestricted Weil positivity/RH open.
