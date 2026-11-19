import WeilDefect.Generated.NF669.OriginalPhysicalComplementDictionary
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramPositiveDefinite
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramSchurAlgebra

namespace WeilDefect

/-!
NF670: original physical 15×227 Riesz response exists by the
certified 10^-60 coercivity of the literal integral-defined A block.

The genuine original 15×15 A operator is injective; Mathlib's
finite-field matrix nonsingular theorem promotes it to a matrix
unit, so its row map is surjective. The genuine original cross block
B then has a unique source-defined A-Riesz response for every
227-vector. No numerical solve, extra Gram axiom, or cofinite Schur
positivity claim enters the construction.
-/

noncomputable section
open Finset

/-- The already certified original physical 15-source Gram as a
square real matrix. Its entries remain original NF606 integrals. -/
def nf670ActualA : Matrix (Fin 15) (Fin 15) ℝ :=
  nf669OriginalA

/-- The genuine physical 15×227 mixed block applied to all remaining
original oscillator coefficients. -/
def nf670ActualCrossRHS (y : Fin 227 → ℝ) (i : Fin 15) : ℝ :=
  ∑ j : Fin 227, nf669OriginalB i j * y j

theorem nf670ActualA_rowAction (x : Fin 15 → ℝ) :
    nf670ActualA.mulVec x =
      neutralNF668GramApply nf669OriginalA x := by
  funext i
  simp only [nf670ActualA, neutralNF668GramApply,
    Matrix.mulVec_apply_eq_sum]

/-- Source-specific kernel triviality, obtained from the accepted
original NF665 coercivity, not presumed from a numerical determinant. -/
theorem nf670ActualA_injective :
    Function.Injective nf670ActualA.mulVec := by
  have hGramInj :
      Function.Injective (neutralNF668GramApply nf669OriginalA) :=
    neutralNF668GramApply_injective nf669OriginalA
      ((1 : ℝ) / (10 ^ 60 : ℝ)) (by positivity)
      nf669OriginalA_coercivity
  intro x y hxy
  apply hGramInj
  rw [← nf670ActualA_rowAction, ← nf670ActualA_rowAction]
  exact hxy

/-- A genuine Matrix unit follows from positive-definite original
physical H, via finite-dimensional field linear algebra. -/
theorem nf670ActualA_isUnit : IsUnit nf670ActualA := by
  exact (Matrix.mulVec_injective_iff_isUnit).mp
    nf670ActualA_injective

theorem nf670ActualA_surjective :
    Function.Surjective nf670ActualA.mulVec := by
  exact (Matrix.mulVec_surjective_iff_isUnit).mpr
    nf670ActualA_isUnit

/-- Every original mixed Gram right-hand side has an exact physical
A-block Riesz solution. This is an existence theorem, with no added
assumption, for every y in the 227 complementary source directions. -/
theorem nf670ActualRiesz_exists
    (y : Fin 227 → ℝ) :
    ∃ u : Fin 15 → ℝ,
      ∀ i : Fin 15,
        (∑ j : Fin 15, nf669OriginalA i j * u j) =
          nf670ActualCrossRHS y i := by
  obtain ⟨u, hu⟩ := nf670ActualA_surjective
    (nf670ActualCrossRHS y)
  refine ⟨u, ?_⟩
  intro i
  have hi := congrFun hu i
  simpa only [nf670ActualA, Matrix.mulVec_apply_eq_sum] using hi

/-- The exact Riesz response U(y)=A⁻¹By is defined using the
mathematically established solution, not a rounded inverse. -/
noncomputable def nf670ActualRieszResponse
    (y : Fin 227 → ℝ) : Fin 15 → ℝ :=
  Classical.choose (nf670ActualRiesz_exists y)

theorem nf670ActualRiesz_solves
    (y : Fin 227 → ℝ) (i : Fin 15) :
    (∑ j : Fin 15,
      nf669OriginalA i j * nf670ActualRieszResponse y j) =
        nf670ActualCrossRHS y i := by
  exact Classical.choose_spec (nf670ActualRiesz_exists y) i

/-- The source-defined A-Riesz response is unique. -/
theorem nf670ActualRiesz_unique
    (y : Fin 227 → ℝ) (u : Fin 15 → ℝ)
    (hu : ∀ i : Fin 15,
      (∑ j : Fin 15, nf669OriginalA i j * u j) =
        nf670ActualCrossRHS y i) :
    u = nf670ActualRieszResponse y := by
  apply nf670ActualA_injective
  funext i
  have hi := hu i
  have hj := nf670ActualRiesz_solves y i
  simpa only [nf670ActualA, Matrix.mulVec_apply_eq_sum] using
    hi.trans hj.symm

/-- Source-integral mixed Gram energy has exactly the A-Riesz
bilinear representation demanded by Schur completion. -/
theorem nf670ActualRiesz_crossIdentity
    (x : Fin 15 → ℝ) (y : Fin 227 → ℝ) :
    neutralNF669Mixed nf669OriginalB x y =
      neutralNF669Bilinear nf669OriginalA
        x (nf670ActualRieszResponse y) := by
  unfold neutralNF669Mixed neutralNF669Bilinear
  apply Finset.sum_congr rfl
  intro i _
  calc
    (∑ j : Fin 227,
      nf669OriginalB i j * x i * y j) =
      x i * nf670ActualCrossRHS y i := by
        unfold nf670ActualCrossRHS
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        ring
    _ = x i * (∑ j : Fin 15,
          nf669OriginalA i j * nf670ActualRieszResponse y j) := by
        rw [nf670ActualRiesz_solves y i]
    _ = ∑ j : Fin 15,
        nf669OriginalA i j * x i *
          nf670ActualRieszResponse y j := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        ring

/-- The certified local A block supplies an unconditional
nonnegative part in the exact source Schur energy. -/
theorem nf670ActualA_nonnegative (x : Fin 15 → ℝ) :
    0 ≤ neutralNF661Quadratic nf669OriginalA x := by
  exact le_trans
    (mul_nonneg (by positivity)
      (neutralNF661SqNorm_nonneg x))
    (nf669OriginalA_coercivity x)

/-- Quantitative remaining obligation:
strict positivity of the 227-source complementary Schur energy is
not proved by the present 15-source certificate. -/
def nf670ActualSchurEnergy (y : Fin 227 → ℝ) : ℝ :=
  neutralNF661Quadratic nf669OriginalC y -
    neutralNF661Quadratic nf669OriginalA
      (nf670ActualRieszResponse y)

/-- A source-specific sufficient implication now has no unspecified
Riesz-response assumption. The only remaining hypothesis is the
authentic 227-source Schur energy nonnegativity. -/
theorem nf670ActualPhysical_block_nonnegative_of_schur
    (hSchur : ∀ y : Fin 227 → ℝ,
      0 ≤ nf670ActualSchurEnergy y)
    (x : Fin 15 → ℝ) (y : Fin 227 → ℝ) :
    0 ≤ neutralNF669BlockEnergy
      nf669OriginalA nf669OriginalB nf669OriginalC x y := by
  apply neutralNF669Schur_sufficient
    nf669OriginalA nf669OriginalB nf669OriginalC
    nf669OriginalA_symm nf670ActualRieszResponse
    nf670ActualRiesz_crossIdentity nf670ActualA_nonnegative
  exact hSchur

/-- Conversely full physical block positivity forces exactly the
same authentic Schur energy condition. -/
theorem nf670ActualPhysical_schur_necessary
    (hFull : ∀ x : Fin 15 → ℝ, ∀ y : Fin 227 → ℝ,
      0 ≤ neutralNF669BlockEnergy
        nf669OriginalA nf669OriginalB nf669OriginalC x y)
    (y : Fin 227 → ℝ) :
    0 ≤ nf670ActualSchurEnergy y := by
  exact neutralNF669Schur_necessary
    nf669OriginalA nf669OriginalB nf669OriginalC
    nf669OriginalA_symm nf670ActualRieszResponse
    nf670ActualRiesz_crossIdentity hFull y

#print axioms nf670ActualA_injective
#print axioms nf670ActualA_isUnit
#print axioms nf670ActualA_surjective
#print axioms nf670ActualRiesz_exists
#print axioms nf670ActualRiesz_solves
#print axioms nf670ActualRiesz_unique
#print axioms nf670ActualRiesz_crossIdentity
#print axioms nf670ActualPhysical_block_nonnegative_of_schur
#print axioms nf670ActualPhysical_schur_necessary

end
end WeilDefect
