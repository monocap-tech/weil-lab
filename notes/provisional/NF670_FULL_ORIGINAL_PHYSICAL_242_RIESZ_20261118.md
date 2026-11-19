# NF670 — exact full 242-original-source quadratic form and Riesz response to the remaining 227 oscillators

## Authenticated predecessor status

- **NF667** original source 15-generator physical Gram coercivity at exact `10^-60`: Lean SUCCESS, full pinned physical-source rebuild and standard-axiom audit (workflow **44455028120**, all three jobs). This is the genuine NF606 interval-integral H on original indices `0..13` and pole `241`.
- **NF668** original physical 15-source nondegeneracy and unique-solve machinery: Lean SUCCESS, workflow **44457538220**, job **135336129115**, including exact source-derived interval attachments, strict positive energy, trivial Gram kernel, injective row action, and at-most-one solution for prescribed RHS, with standard-axiom audit.
- **NF669** source-independent symmetric bilinear expansion, exact Schur square completion, and necessary/sufficient cofinite energy criteria: Lean SUCCESS, workflow **44459126587**, generic job **135341343151**, with standard-axiom audit. Source-specific NF669 15+227 index dictionary still under full-source compilation at NF670 authorship time; do NOT assign Lean PASS prematurely.

## NF670 original complete physical quadratic

`WeilDefect/Generated/NF670/OriginalPhysicalFullQuadratic.lean` (new, Lean pending):

1. `nf670FullSource_sum`: exact reindexing identity for a finite sum over all original 242 generators, using NF669's explicitly proved genuine index equivalence and Mathlib `Fintype.sum_equiv`.
2. `nf670FullSource_quadratic_reindex`: apply exact equivalence to both indices of the original NF606 physical double sum `neutralNF661Quadratic neutralNF606PhysicalH z`.
3. `nf670AssembleOriginal`: reconstruct a 242-coefficient vector from exact original selected indices `0..13,241` and complement `14..240`, and prove source recovery and round trip.
4. `nf670Mixed_physicalTransposed`: certify literal physical B and its transpose as the same mixed quadratic term using original NF606 H symmetry.
5. `nf670FullPhysicalGram_blockEnergy`: *full* exact 242-dimensional original physical quadratic energy equals `Q_A(x)+2Cross_B(x,y)+Q_C(y)` at assembled coordinates.
6. `nf670FullPhysicalGram_allCoefficients`: the preceding identity specialized to **every original 242-source coefficient vector**, not only an unspecified block matrix or transformed surrogate.

No new numerical entries are introduced. The proof of the index reordering is genuinely source-bound, not a numerical Gram comparison. The six theorems await fresh Lean compiler/axiom acceptance.

## NF670 original cross-block Riesz response — no inversion hypothesis

`WeilDefect/Generated/NF670/OriginalPhysicalRieszResponse.lean` (new, Lean pending) imports NF669 actual A/B/C source definitions and NF668 now Lean-accepted generic Gram injectivity. The route is:

- `nf670ActualA` is exactly original 15×15 `nf669OriginalA`, not the transformed NF659 integer centers.
- Quantitative original NF665 coercivity implies `Function.Injective nf670ActualA.mulVec`; Mathlib's exact `Matrix.mulVec_injective_iff_isUnit` gives `IsUnit nf670ActualA`.
- Mathlib `Matrix.mulVec_surjective_iff_isUnit` gives existence of an original 15-source Riesz solution to **each** RHS `(By)_i=Σ_{j:Fin227} B_ij*y_j`, for arbitrary 227-source coefficients y.
- Choose the unique such solution to define the exact mathematical map `nf670ActualRieszResponse y = A^-1(By)` without a rounded inverse and without an explicit nonzero-determinant assumption.
- Prove its unique solution equation and exact mixed source-Gram bilinear identity `Cross_B(x,y)=Bilinear_A(x,U y)`.
- Define the actual 227-source Schur remainder `Q_C(y)-Q_A(U y)`, and specialize the now Lean-accepted NF669 Schur-completion sufficient and necessary conditions. The **only remaining hypothesis in the sufficient implication** is nonnegative actual complementary Schur energy; the authentic Riesz response is no longer a hypothesis.

There is still **NO certified quantitative lower bound on the genuine 227-source Schur remainder**. This source-dependent gap is explicitly preserved.

## Verification design

`.github/workflows/nf670-original-riesz-quadratic.yml` rebuilds the original pinned NF631/NF632/NF621/NF648 certificates, NF655 physical integrals, NF658/659 exact enclosures, NF662/663 real interval transfers, NF664 transformed coercivity and NF665 original physical coercivity. It then builds both new NF670 modules, invoking strict standard-axiom audits over 16 NF670 endpoints and all critical upstream source custody theorems. The axiom checker treats *axiom-free* declarations as valid while refusing `sorryAx` or any axiom outside `[propext, Classical.choice, Quot.sound]`.

All new NF670 declarations remain **compiler pending** until this new workflow completes and passes. They are substantive proposed Lean theorems, not currently accepted facts.

## Next NF671 mathematical direction

There are two different complementary claims:

1. Nonnegativity `Q_C(y)-Q_A(U y)≥0` follows from full 242-source physical Gram nonnegativity if the analytic L2 integral-square proof is attached; the physical Gram is an L2 product form, so this is a natural target.
2. **Strict quantitative** `Q_C(y)-Q_A(U y)≥c‖y‖²` requires nondegeneracy/coercivity on the 227-source quotient; neither follows from the certified A block alone. Source independence and quantitative bounds (or exact interval certificates) remain separate.
3. Neither physical Gram PSD nor this local/cofinite completion is equivalent to global signed Weil positivity or RH without additional signed Weil transport.

Draft stacked PR; no merge to main.
