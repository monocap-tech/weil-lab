# Weil-Lab — CP029 controlled reopening
## First isolated genuine original-Zeta-v4.35 compilation: pointwise Borwein only

**Track:** independent CP### original signed-Weil ↔ analytic/spectral compatibility program. CP029 stacks on draft CP028 #850 → CP027 #849 → CP026 #848. All original IV###/NF### acceptance records, proofs, identities and PI### prime/Gamma comparisons remain untouched.

### 1. Concrete highest-value task

Obtain genuine **Lean4 v4.35.0 kernel feedback** on the **upstream-only** source module `cp011_zeta_v435/CP027PointwiseBorwein.lean`. This module contains 11 candidate theorems, ending with **two unconditional original M=6, N=256 pointwise Borwein caps** at exact rational heights 150.05352 and 150.05353:

[
\operatorname{zetaRemainderBound}(\tfrac12+150.05352i,6,256)
\le3\times10^{-13},
]
[
\operatorname{zetaRemainderBound}(\tfrac12+150.05353i,6,256)
\le3\times10^{-13}.
]

It imports **only four immutable upstream modules**: `Zeta.EulerMaclaurin.ErrorBound`, `Mathlib.RingTheory.Polynomial.Pochhammer`, `Mathlib.NumberTheory.Bernoulli`, and `Mathlib.Analysis.SpecialFunctions.Pow.Real`. It does **not** import CP021, CP026, CP027TwoFiniteSigns or CP028. Its present Lean source Git blob is frozen for this diagnostic at `7a4dd8f0994e13c2653cdc3e499409b6072ed8a7`. If the actual compiler finds an error, repair the source in a separate bounded revision and update that pin only after independent source review.

The source calculation is independently exact:

[
\frac{328}{27}\,
\frac7{6\cdot14!}\,
\frac{\prod_{j=0}^{12}(151+j)}{256^{13}}
=\frac{1069402300239520471}{3802951800684688204490109616128}
\approx2.812032222041268\times10^{-13}<3\times10^{-13}.
]

This arithmetic is not the actual Lean proof. A genuine compiler run must check the underlying original `bernoulli 14 = 7/6`, exact complex `ascPochhammer` induction, real exponent bounding `Complex.norm_cpow_eq_rpow_re_of_pos`, and the concrete original `zetaRemainderBound` definitional equality.

### 2. Input dependencies and frozen provenance

- **Lean compiler:** `cp011_zeta_v435/lean-toolchain` exactly `leanprover/lean4:v4.35.0`.
- **True original Zeta:** `smmercuri/zeta` tag `v1-1e6` resolved through Lake, checkout commit **`c06b4e13d9c847e50a32c3d738271cbad62ae9f3`** checked after `lake update`.
- **Mathlib:** pulled through the original Lake dependency; five true original Zeta/Mathlib Git blob+theorem API contracts checked with the existing `scripts/cp027_original_center_borwein_328_over_27_source_gate.py` against **the actual Lake package contents**.
- **Local proof source:** only `CP027PointwiseBorwein.lean` and its pre-existing `[[lean_lib]]` target. No `lakefile.toml`, original IV/NF source file, or historical proof is modified in CP029.
- **Sufficient runner:** one Ubuntu runner, original upstream Mathlib cache, and one `lake build CP027PointwiseBorwein`. No dependency on the uncompiled CP026 bridge or numerical A6,256 signs.

### 3. Actually checked CI fan-out, before submitting changes

The CP028 branch contains **36** workflow YAML files. We inspected the event/paths sections of **all 36** in the CP029 preparation. Ordinary PR-triggered workflows are path-scoped (the root Lean workflow also restricts paths and main-branch pushes); the others are manual/explicit-label opt-ins. The two inherited CP013 and CP014 *source-lineage* workflows have repaired `pull_request.paths` filters but both include the **shared `cp011_zeta_v435/lakefile.toml`**. This explains why changes to that registry on older CP PRs triggered them, even when the actual new research topic was different. Their completed successes on CP028 #850 are source-lineage gates, NOT CP027/29 pointwise kernel receipts.

**CP029 avoids that shared file entirely.** It introduces only:
1. `scripts/cp029_original_one_leaf_kernel_receipt_gate.py`,
2. `.github/workflows/cp029-original-pointwise-Zeta435-single-leaf-opt-in.yml`,
3. this `docs/CP029_CONTROLLED_REOPENING_SINGLE_LEAF_COMPILER_CUSTODY.md`.

None of those new paths appears in any preexisting ordinary-PR workflow path filter inspected. **Expected ordinary draft PR-creation fan-out attributable to these changes: zero runnable CI jobs.** This is a static trigger audit, not a promise about unrelated repository activity, manual labels or GitHub platform scheduling. No heavy CI launch is performed by this PR.

The new CP029 workflow has **ONLY** `workflow_dispatch` and `pull_request: types: [labeled]`, with the job additionally gated to the exact label **`cp029-pointwise-lean`** or manual dispatch. No ordinary PR opened/synchronize or push trigger. One workflow, **one job**, concurrency keyed per PR/branch, 150-minute job ceiling; the actual Lean compile step has its own smaller ceiling. Other existing label-only workflows may register **skipped** runs for a label event, but their job-level label conditions prevent them consuming heavy runner slots for the CP029 label.

**Launch policy:** coordinate with the IV/NF owner before applying the label; do not launch simultaneously with another heavy original NF/IV compiler. Since this workflow is new on a draft branch, the **explicit PR label is the viable premerge trigger**; manual dispatch is available when the workflow exists on the default branch. The source/log submission itself does not apply a label or dispatch anything.

### 4. Verification criteria and strict failure handling

**Before actual Lean:** `python -m py_compile` for both CP027/29 source gates; existing CP027 exact `Fraction` self-test and original 12 source declarations; CP029 frozen true module identity, exactly four genuine upstream imports and exactly 11 expected `#print axioms` directives; original `lean-toolchain` identity and five real frozen upstream Git blob/API gates.

**Genuine Lean compiler:** successful `lake build CP027PointwiseBorwein` with shell `pipefail`, producing its actual nonempty `.lake/build/lib/lean/CP027PointwiseBorwein.olean`. A build command failure **stops the acceptance step**, preserves full build logs and extracts the first actual compiler failure. A build that was never reached is NOT called a compilation failure of the source.

**Strict axiom audit:** successful `lake env lean CP027PointwiseBorwein.lean`, and unique actual `#print axioms` outputs for ALL ELEVEN declarations. Reject any **nonstandard axioms** (allowed only `propext`, `Classical.choice`, `Quot.sound`, or no axioms), errors, `sorryAx`, absent .olean or absent/transplanted logs. The CP029 fail-closed audit writes the actual kernel receipt **only when** all genuine compiler checks pass.

**Artifact custody:** original source preflights, exact pinned Git checks, Mathlib cache log, the full genuine build log, the first-error extraction, genuine axiom log, `.olean`, and a signed-off-by-tests JSON containing SHA-256 content digests; the JSON itself is not a theorem. The workflow uploads diagnostics even when compilation fails.

**If Lean compilation fails:** publish first concrete elaboration error and the *smallest source repair* under a new controlled CP update; rerun only this one target. Do **not** count the original pointwise caps as kernel accepted.

**If Lean compilation passes and axiom outputs are standard:** only the **two real original center-point Borwein remainder lemmas** (and their nine supporting lemmas) advance from source-only to actual genuine Lean kernel acceptance. The conditional CP026–CP028 IVT bridge, both original *finite numerical complex boxes* ((\|A\|\le10^{-3}) plus (\widetilde Z_A(t_L)<-10^{-7}), (\widetilde Z_A(t_R)>10^{-7})), original zero ordinal #53 attachment, whole-interval curvature and complete normalized signed Weil↔spectral (3\times3) equality **remain OPEN**. A standard-only axiom audit of a theorem with numerical hypotheses would not pay those hypotheses.

### 5. Parallel mathematical research, no CI needed

CP028's two coarse finite approximant boxes should be prepared as **small outward-rational Taylor interval manifests** using the source-verified 255-term Euler–Maclaurin representation, with exact phase and Bernoulli corrections. Use a coarser provable precision (e.g. (10^{-9}) absolute interval cells) and negative controls; do not introduce the external CP025 JSON values as Lean axioms. This is a *separate numerical task*, not a precondition for the one-leaf CP029 compiler feedback.

For cross-projection compatibility, preserve IV030's **equal-support/equal-mass/equal-interaction-graph but opposite original prime contributions** as an immediate falsifier for a graph-only Weil-to-spectral equivalence dictionary. Any future proposed preservation law must carry phase information; it cannot identify the original signed form with a numeric zero roster merely because both have source-verified local certificates. No global signed Weil positivity or RH claim.

**Custody:** Original NF accepted numerical frontier remains **692/968**, not affected by CP029. IV certified source lemmas and protected NF750–NF753 jobs are unchanged. The CP029 branch adds no source-level accepted theorems until the genuine compiler returns a receipt.
