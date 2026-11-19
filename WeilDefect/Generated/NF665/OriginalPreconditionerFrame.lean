import WeilDefect.Generated.NF659.Complete
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramPreconditionerFrame

namespace WeilDefect

/-!
NF665: original frozen 15×15 preconditioner; explicit lower triangular,
nonzero diagonal, isomorphism, finite Frobenius estimate, and actual
physical congruence identity. All arithmetic properties are proof
targets against existing NF658/NF659 integer arrays. Nothing here
postulates invertibility.
-/

noncomputable section
open Finset

/-- Independent direct view of the original certified integer preconditioner. -/
def nf665OriginalRealK (i j : Fin 15) : ℝ :=
  (nf658Get nf658Kints i j : ℝ) / (10 ^ 64 : ℝ)

theorem nf665OriginalK_upperZero :
    ∀ i j : Fin 15, i < j →
      nf658Get nf658Kints i j = 0 := by
  decide +kernel

theorem nf665OriginalK_diagonal :
    ∀ i : Fin 15,
      nf658Get nf658Kints i i = (10 ^ 64 : ℤ) := by
  decide +kernel

theorem nf665OriginalK_isLowerTriangular :
    Matrix.IsLowerTriangular
      (nf665OriginalRealK : Matrix (Fin 15) (Fin 15) ℝ) := by
  change ∀ ⦃i j : Fin 15⦄, i < j →
      nf665OriginalRealK i j = 0
  intro i j hij
  change (nf658Get nf658Kints i j : ℝ) / (10 ^ 64 : ℝ) = 0
  rw [nf665OriginalK_upperZero i j hij]
  norm_num

theorem nf665OriginalK_diagonal_ne_zero :
    ∀ i : Fin 15,
      nf665OriginalRealK i i ≠ 0 := by
  intro i
  change (nf658Get nf658Kints i i : ℝ) / (10 ^ 64 : ℝ) ≠ 0
  rw [nf665OriginalK_diagonal i]
  norm_num

theorem nf665OriginalK_surjective :
    ∀ x : Fin 15 → ℝ, ∃ y : Fin 15 → ℝ,
      neutralNF665TransposeAction nf665OriginalRealK y = x :=
  neutralNF665Transpose_surjective_of_lower
    nf665OriginalRealK
    nf665OriginalK_isLowerTriangular
    nf665OriginalK_diagonal_ne_zero

theorem nf665OriginalK_frobeniusScale :
    (∑ i : Fin 15, ∑ j : Fin 15,
        (nf665OriginalRealK i j)^2) =
      (nf659KNormSq : ℝ) / (10 ^ 64 : ℝ)^2 := by
  have hcast : (nf659KNormSq : ℝ) =
      ∑ i : Fin 15, ∑ j : Fin 15,
        (nf658Get nf658Kints i j : ℝ)^2 := by
    simp only [nf659KNormSq, Int.cast_sum, Int.cast_pow]
  calc
    (∑ i : Fin 15, ∑ j : Fin 15,
        (nf665OriginalRealK i j)^2) =
      ∑ i : Fin 15, ∑ j : Fin 15,
        ((nf658Get nf658Kints i j : ℝ)^2 /
          (10 ^ 64 : ℝ)^2) := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      simp only [nf665OriginalRealK, div_pow]
    _ = (∑ i : Fin 15, ∑ j : Fin 15,
          (nf658Get nf658Kints i j : ℝ)^2) /
            (10 ^ 64 : ℝ)^2 := by
      simp only [Finset.sum_div]
    _ = (nf659KNormSq : ℝ) / (10 ^ 64 : ℝ)^2 := by
      rw [hcast]

theorem nf665OriginalK_normBound (y : Fin 15 → ℝ) :
    neutralNF661SqNorm
      (neutralNF665TransposeAction nf665OriginalRealK y) ≤
      ((nf659KNormSq : ℝ) / (10 ^ 64 : ℝ)^2) *
        neutralNF661SqNorm y := by
  have h := neutralNF665FrobeniusNorm_bound
    nf665OriginalRealK y
  rw [nf665OriginalK_frobeniusScale] at h
  exact h

theorem nf665OriginalPhysical_congruence (y : Fin 15 → ℝ) :
    neutralNF661Quadratic
      (neutralNF664ActualPhysicalB nf665OriginalRealK) y =
      neutralNF661Quadratic neutralNF661PhysicalH
        (neutralNF665TransposeAction nf665OriginalRealK y) := by
  change
    neutralNF661Quadratic
      (neutralNF662Congruence nf665OriginalRealK
        neutralNF661PhysicalH) y =
      neutralNF661Quadratic neutralNF661PhysicalH
        (neutralNF665TransposeAction nf665OriginalRealK y)
  exact neutralNF665Quadratic_congruence
    neutralNF661PhysicalH nf665OriginalRealK y

#print axioms nf665OriginalK_upperZero
#print axioms nf665OriginalK_diagonal
#print axioms nf665OriginalK_surjective
#print axioms nf665OriginalK_normBound
#print axioms nf665OriginalPhysical_congruence

end
end WeilDefect
