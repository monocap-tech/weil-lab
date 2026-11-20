import Mathlib.Tactic

namespace WeilDefect

/-! NF739: three-support Gram obstruction. Even if the energy is
nonnegative on EVERY two-coordinate support subspace, it need not be
nonnegative on the complete three-coordinate span. This is purely a
finite-dimensional countermodel and is NOT a negative Weil zeta example. -/

/-- A real symmetric 3×3 quadratic Gram model with unit diagonal and
off-diagonal -1. Every principal 2×2 restriction is positive
semidefinite, while the full 3×3 quadratic form has a negative vector. -/
def neutralNF739ThreeSupportCrossModel (v : Fin 3 → ℝ) : ℝ :=
  (v 0)^2 + (v 1)^2 + (v 2)^2 -
    2*((v 0)*(v 1) + (v 0)*(v 2) + (v 1)*(v 2))

/-- Pair 0/1 has exactly a nonnegative square, despite a full-form
negative direction in the three-component model. -/
theorem neutralNF739ThreeSupport_pair01_nonnegative (x y : ℝ) :
    0 ≤ neutralNF739ThreeSupportCrossModel
      (fun i => if i = 0 then x else if i = 1 then y else 0) := by
  simp only [neutralNF739ThreeSupportCrossModel]
  norm_num
  nlinarith [sq_nonneg (x - y)]

/-- Pair 0/2 is nonnegative on every two-component coefficient choice. -/
theorem neutralNF739ThreeSupport_pair02_nonnegative (x z : ℝ) :
    0 ≤ neutralNF739ThreeSupportCrossModel
      (fun i => if i = 0 then x else if i = 2 then z else 0) := by
  simp only [neutralNF739ThreeSupportCrossModel]
  norm_num
  nlinarith [sq_nonneg (x - z)]

/-- Pair 1/2 is nonnegative on every two-component coefficient choice. -/
theorem neutralNF739ThreeSupport_pair12_nonnegative (y z : ℝ) :
    0 ≤ neutralNF739ThreeSupportCrossModel
      (fun i => if i = 1 then y else if i = 2 then z else 0) := by
  simp only [neutralNF739ThreeSupportCrossModel]
  norm_num
  nlinarith [sq_nonneg (y - z)]

/-- Explicit failure of full positivity even though the three complete
pairwise coordinate planes are all PSD: Q(1,1,1) = -3. -/
theorem neutralNF739ThreeSupport_all_ones_negative :
    neutralNF739ThreeSupportCrossModel
      (fun _ : Fin 3 => (1 : ℝ)) = -3 := by
  norm_num [neutralNF739ThreeSupportCrossModel]

/-- Existence of a negative full three-support mixture under a
pairwise-PSD model. This rebuts the inference that proving the
two-support mixed EF problem automatically yields global many-support
Weil positivity. -/
theorem neutralNF739PairwisePSD_not_fullPSD :
    ∃ v : Fin 3 → ℝ, neutralNF739ThreeSupportCrossModel v < 0 := by
  refine ⟨(fun _ : Fin 3 => (1 : ℝ)), ?_⟩
  rw [neutralNF739ThreeSupport_all_ones_negative]
  norm_num

#print axioms neutralNF739ThreeSupport_pair01_nonnegative
#print axioms neutralNF739ThreeSupport_pair02_nonnegative
#print axioms neutralNF739ThreeSupport_pair12_nonnegative
#print axioms neutralNF739ThreeSupport_all_ones_negative
#print axioms neutralNF739PairwisePSD_not_fullPSD

end WeilDefect
