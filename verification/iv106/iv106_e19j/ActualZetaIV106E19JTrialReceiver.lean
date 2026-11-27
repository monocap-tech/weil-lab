import WeilDefect.Arithmetic.ActualZetaIV106E19JTriangular
import WeilDefect.Arithmetic.ActualZetaIV106E16ResidualGram

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped BigOperators InnerProduct

/-- Every matrix of coefficients synthesizes admissible E16 trial rows.
No row-independence hypothesis on the original constraints is needed. -/
def neutralIV106E19JTrials {J : Type*} [Fintype J]
    (k : ℕ) (hk : 0 < k) (z : J → neutralIV106E12Kernel k hk)
    (C : neutralIV106E16Index k → J → ℂ) :
    neutralIV106E16Index k → neutralIV106E12Kernel k hk :=
  fun i => ∑ j, C i j • z j

/-- The receiver uses the full compressed operator, not its projection
onto the finite trial bank. In-bank residual cancellation is insufficient. -/
theorem neutralIV106E19JResidual {J : Type*} [Fintype J]
    (k : ℕ) (hk : 0 < k) (z : J → neutralIV106E12Kernel k hk)
    (C : neutralIV106E16Index k → J → ℂ) (i : neutralIV106E16Index k) :
    neutralIV106E15Residual k hk (neutralIV106E14LiftedRow k hk i)
      (neutralIV106E19JTrials k hk z C i) =
    neutralIV106E15RHS k hk (neutralIV106E14LiftedRow k hk i) -
      ∑ j, C i j • neutralIV106E12Compressed k hk (z j) := by
  unfold neutralIV106E15Residual neutralIV106E19JTrials
  simp only [map_sum,map_smul]

/-- Expansion of the actual ambient trial vector for the energy Gram. -/
theorem neutralIV106E19JTrialVector {J : Type*} [Fintype J]
    (k : ℕ) (hk : 0 < k) (z : J → neutralIV106E12Kernel k hk)
    (C : neutralIV106E16Index k → J → ℂ) (i : neutralIV106E16Index k) :
    neutralIV106E16TrialVector k hk (neutralIV106E19JTrials k hk z C) i =
      neutralIV106E14Row k hk i - ∑ j, C i j • (z j).val := by
  unfold neutralIV106E16TrialVector neutralIV106E19JTrials
  change _ - (neutralIV106E12Kernel k hk).subtypeL (∑ j, C i j • z j) = _
  simp only [map_sum,map_smul]
  rfl

/-- The true residual Gram uses the original full kernel operator.
This equality is independent of how the coefficients were selected. -/
theorem neutralIV106E19JResidualGram {J : Type*} [Fintype J]
    (k : ℕ) (hk : 0 < k) (z : J → neutralIV106E12Kernel k hk)
    (C : neutralIV106E16Index k → J → ℂ)
    (i l : neutralIV106E16Index k) :
    neutralIV106E16ResidualGram k hk (neutralIV106E19JTrials k hk z C) i l =
      inner ℂ
        (neutralIV106E15RHS k hk (neutralIV106E14LiftedRow k hk i) -
          ∑ j, C i j • neutralIV106E12Compressed k hk (z j))
        (neutralIV106E15RHS k hk (neutralIV106E14LiftedRow k hk l) -
          ∑ j, C l j • neutralIV106E12Compressed k hk (z j)) := by
  unfold neutralIV106E16ResidualGram
  rw [neutralIV106E19JResidual,neutralIV106E19JResidual]

/-- For a candidate least-squares solution, exact full-kernel residual
orthogonality to the compressed bank proves optimality in that bank.
It does not prove that the residual itself is zero. -/
theorem neutralIV106E19JLeastSquares {H J : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [Fintype J]
    (b : H) (v : J → H) (c d : J → ℂ)
    (ho : ∀ j, inner ℂ (v j) (b-∑ l, c l • v l) = 0) :
    ‖b-∑ j, c j • v j‖^2 ≤ ‖b-∑ j, d j • v j‖^2 := by
  let r := b-∑ j, c j • v j
  let w := ∑ j, (c j-d j) • v j
  have hw : inner ℂ w r = 0 := by
    dsimp [w]
    rw [sum_inner]
    simp only [inner_smul_left, r, ho, mul_zero, Finset.sum_const_zero]
  have he : b-∑ j, d j • v j = r+w := by
    dsimp [r,w]
    simp only [sub_smul,Finset.sum_sub_distrib]
    abel
  rw [he, norm_add_sq_eq_norm_sq_add_norm_sq_of_inner_eq_zero (by
    rw [← inner_conj_symm,hw]
    simp)]
  linarith [sq_nonneg ‖w‖]

#print axioms neutralIV106E19JResidual
#print axioms neutralIV106E19JTrialVector
#print axioms neutralIV106E19JResidualGram
#print axioms neutralIV106E19JLeastSquares
end
end WeilDefect
