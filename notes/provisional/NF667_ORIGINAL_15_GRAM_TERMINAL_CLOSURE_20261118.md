# NF667 — original 15-source physical Gram terminal compiler closure

## Current verified compiler state

NF666 workflow run **44452465896**:
- Generic preconditioner mechanics job **135319468579**: SUCCESS, including real Frobenius bound, finite four-sum quadratic congruence, triangular preconditioner surjectivity and standard axiom audit.
- Source-dependent original preconditioner job **135319468992**: FAIL at a single matrix elaboration declaration `(nf665OriginalRealK : Matrix ...).IsLowerTriangular`. The actual `nf665OriginalRealK` is a function, and Lean resolved the projection from `Function`, not `Matrix`.
- Complete terminal source job **135319468900**: all preliminary source verification and stages succeeded, including the regenerated NF662 225 real original physical interval proofs, NF663 450 exact integer double-sum identifications and source-real transformed enclosures, and NF664 **actual** physical transformed coercivity. In the build log the critical `nf663ActualPhysical_transformedEnclosed` and `nf664AuthenticatedOriginalTransformedCoercivity` theorems both list only `[propext, Classical.choice, Quot.sound]`. The job stopped while compiling the exact original K preconditioner because of the same lower-triangular elaboration issue; the terminal theorem was not yet reached, and remains OPEN.

## Exact NF667 compiler repair

`Generated/NF665/OriginalPreconditionerFrame.lean`: replace the ambiguous field projection `(nf665OriginalRealK : Matrix (Fin 15) (Fin 15) ℝ).IsLowerTriangular` with the explicit fully qualified proposition `Matrix.IsLowerTriangular (nf665OriginalRealK : Matrix (Fin 15) (Fin 15) ℝ)`. No matrix entry, source index, numeric witness, coercivity target or proof assumption is changed.

The source original K has already supplied exact 15×15 integer upper-zero and diagonal-equals-`10^64` gates. Once the repaired type elaborates, it should permit direct use of the Lean-passed generic triangular-surjectivity theorem. Success of that source-dependent proof and the terminal coercivity theorem **requires a fresh standard-axiom compiler audit**; no premature PASS is assigned.

## Terminal mathematical target

`nf665OriginalPhysical_coercivity`:

`∀ x : Fin 15 → ℝ, ((1:ℝ)/(10^60:ℝ)) * neutralNF661SqNorm x ≤ neutralNF661Quadratic neutralNF661PhysicalH x.`

This is a statement about the genuinely integral-defined NF606 physical Gram matrix restricted to original generators 0–13 and 241. It does **not** establish the positivity of all 242 original source directions, the full signed Weil transport, global Weil positivity or the Riemann hypothesis.

## Certification gate

The original `nf665-original-preconditioner-frame.yml` workflow is inherited and checks (1) generic matrix mechanics with axiom audit, (2) the frozen 15×15 original K with axiom audit, and (3) the whole reconstructed source-attached physical inequality with its `#print axioms` audit. A complete successful terminal job and no `sorryAx` are mandatory for claiming the local theorem CLOSED. Draft branch only; no main merge.
