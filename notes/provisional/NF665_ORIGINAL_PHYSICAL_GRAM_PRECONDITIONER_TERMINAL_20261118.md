# NF665 — explicit original physical frame and 10^-60 terminal theorem candidate

## Compiler truth recovered

- NF658 corrected workflow **44434056814**: Lean SUCCESS, source-derived 120 original compact physical-entry intervals and standard axiom audit.
- NF659 workflow **44430374282**: Lean SUCCESS for 450 exact integer transformed centers/radii, 15 margins and the coercivity integer gate.
- NF660 workflow **44437954229**: Lean SUCCESS, symmetric quadratic diagonal-dominance and real-interval coercivity, standard-axiom audit.
- NF661 workflow **44437952335**: Lean SUCCESS, literal original 15-source physical block and generic quantitative coercivity transfer, standard-axiom audit.
- NF662 generic real interval transfer stage: Lean PASS in previous runs, but NF662 physical pilots **44441238249** failed because the two-field rational-ball symmetry proof over-simplified away the rationals and produced an integer-equality type mismatch. NF665 replaces simplification with explicit rational cast equalities; new acceptance pending.
- NF663 generic integer-real scaling run **44439396898** failed at exactly two redundant `ring` tactics after `field_simp` had already closed the goals. NF665 repairs both; new acceptance pending.
- NF664 generic run **44441238965**, job **135282299796**, Lean SUCCESS for transformed-real quadratic coercivity from integer margins. Its original full physical attachment job was in progress at last verification. NF665 additionally explicitly reconciles `if i=j` and `if j=i` in the old NF664 margin source specialization, avoiding unjustified definitional equality.

## New source-independent mathematical proof candidates

`ActualZetaOriginalPhysicalGramPreconditionerFrame.lean`:

1. `neutralNF665TransposeAction`: exact (x_p=\sum_i y_i K_{ip}) with no numerical approximation.
2. `neutralNF665FrobeniusNorm_bound`: squared Euclidean norm of (K^T y) is bounded by the Frobenius sum of squares of (K) times squared norm of (y), by Mathlib's finite Cauchy–Schwarz theorem.
3. `neutralNF665Quadratic_congruence`: the complete four-index finite sum identity
   `yᵀ (K H Kᵀ) y = (Kᵀy)ᵀ H (Kᵀy)`.
4. `neutralNF665Transpose_surjective_of_lower`: a lower-triangular real square matrix with nonzero diagonal has nonzero determinant, is a matrix unit, and gives a surjective transposed coordinate map, using Mathlib determinant and `Matrix.vecMul_surjective_iff_isUnit`.

These are proof candidates until the NF665 generic CI job reports Lean success and clean axioms.

## The authentic frozen integer preconditioner

`Generated/NF665/OriginalPreconditionerFrame.lean` refers directly to `nf658Kints` from the original accepted NF658 witness and:
- proves all entries strictly above the diagonal vanish by a finite `decide +kernel` proposition;
- proves its fifteen diagonal entries equal (S=10^{64}) by a separate exact gate;
- defines (K_{\rm real}=K_{\rm int}/S);
- derives real lower-triangularity, nonzero diagonal, surjective (K^T);
- derives (|K^T y|^2\le (kn/S^2)|y|^2), where `kn=nf659KNormSq` exactly;
- derives actual original H integral quadratic congruence.

These concrete statements are **Lean pending**, but their numeric inputs are the original NF658/NF659 arrays, not a second solver output. This proof bank is built independently from the pending 225-entry NF662/NF663 source-real attachment.

## The proposed complete original 15-source physical theorem

`Generated/NF665/OriginalPhysicalCoercivity.lean` takes the genuine physical H integral on indices 0,...,13,241 and proposes:

`∀ x : Fin 15 → ℝ, (1/(10^60:ℝ)) * neutralNF661SqNorm x ≤ neutralNF661Quadratic neutralNF661PhysicalH x`.

Its proof is a direct application of already accepted NF661 general quantitative basis transfer, using:
- the NF664 specific transformed-real dominance theorem (requires NF662/NF663 physical-real attachments);
- the NF665 exact congruence, norm bound, surjective map;
- a new arithmetic lemma converting the accepted NF659 **strict integer inequality** `nf658MinMargin*10^60>10^64*nf659KNormSq` into the exact real (10^{-60}) gate.

The exact terminal theorem remains **OPEN** until a complete regenerated original source build, the theorem, and its axiom audit all pass. It would close only **the original 15-generator physical Gram coercivity**, NOT all 242 source directions, the entire signed Weil form, global Weil positivity, or RH.

## Focused CI

The new `.github/workflows/nf665-original-preconditioner-frame.yml` has three independent jobs:
1. generic Frobenius/quadruple-sum/surjectivity proofs and axiom audit;
2. original frozen integer K, lower triangularity, invertibility, exact norm and quadratic identity (generates NF658 and NF659 artifacts, not dependent on NF662 membership);
3. complete original frozen source proof bank, all real physical intervals, NF664 transformed coercivity, then the terminal 10^-60 physical 15-generator theorem with axiom audit.

All new NF665 theorem claims are **compiler pending**. Source branch is stacked against NF664, not main.
