module

public import CP028CoarseFiniteBoxes

/-!
CP030: original source six-scalar finite Euler-Maclaurin proof interface.

Four real/imag source A6,256 component caps and two source rotated-real
signed caps imply both CP028 original finite boxes, and hence the
CP028 original narrow zero theorem CONDITIONAL on all six caps and all
inherited sources genuinely compiling.

The six numerical scalar hypotheses are NOT yet Lean-proved; Python
10^-9 outward cells are external evidence and may NEVER be asserted
as new axioms. This new file itself has NO compiler receipt.

This file is deliberately not added to the shared Lake registry yet:
it must be built after the CP028 source stack is actually compiled.
No change to IV/NF/PI workflows or acceptance records.
-/

@[expose] public section

namespace CP030FiniteComponentCells

open CP026OriginalPointBridge CP028CoarseFiniteBoxes

private abbrev componentCap : ℝ := (1 : ℝ) / 10000

/-- Six deliberately loose original REAL scalar proof obligations. -/
def FiniteScalarCells : Prop :=
  |(sourceA tLeft).re| ≤ componentCap ∧
  |(sourceA tLeft).im| ≤ componentCap ∧
  sourceFiniteZ tLeft ≤ -((2 : ℝ) / (10 : ℝ) ^ 7) ∧
  |(sourceA tRight).re| ≤ componentCap ∧
  |(sourceA tRight).im| ≤ componentCap ∧
  ((1 : ℝ) / (10 : ℝ) ^ 6) ≤ sourceFiniteZ tRight

/-- Two component caps of 10^-4 give the genuine complex norm cap
2e-4 < 1e-3. No transcendental/numerical facts are used here. -/
theorem norm_of_coordinate_caps (z : ℂ)
    (hr : |z.re| ≤ componentCap)
    (hi : |z.im| ≤ componentCap) :
    ‖z‖ ≤ (1 : ℝ) / 1000 := by
  have hz : (z.re : ℂ) + (z.im : ℂ) * Complex.I = z := by
    apply Complex.ext <;> simp
  calc
    ‖z‖ = ‖(z.re : ℂ) + (z.im : ℂ) * Complex.I‖ := by rw [hz]
    _ ≤ ‖(z.re : ℂ)‖ + ‖(z.im : ℂ) * Complex.I‖ := norm_add_le _ _
    _ = |z.re| + |z.im| := by simp [norm_mul]
    _ ≤ componentCap + componentCap := add_le_add hr hi
    _ ≤ (1 : ℝ) / 1000 := by norm_num [componentCap]

/-- A genuine CP028 left finite box from the three left scalars. -/
theorem left_coarse_of_scalar (h : FiniteScalarCells) : FiniteLeftBox := by
  rcases h with ⟨hr,hi,hf,_,_,_⟩
  constructor
  · exact norm_of_coordinate_caps (sourceA tLeft) hr hi
  · exact lt_of_le_of_lt hf (by norm_num)

/-- A genuine CP028 right finite box from the three right scalars. -/
theorem right_coarse_of_scalar (h : FiniteScalarCells) : FiniteRightBox := by
  rcases h with ⟨_,_,_,hr,hi,hf⟩
  constructor
  · exact norm_of_coordinate_caps (sourceA tRight) hr hi
  · exact lt_of_lt_of_le (by norm_num) hf

/-- Still CONDITIONAL on SIX original source scalar numerical claims,
and on genuine acceptance of every imported CP026/27/28 proof. -/
theorem original_narrow_zero_of_scalar_cells (h : FiniteScalarCells) :
    ∃ t : ℝ, tLeft < t ∧ t < tRight ∧
      riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0 := by
  exact original_narrow_zero_of_two_coarse_boxes
    (left_coarse_of_scalar h) (right_coarse_of_scalar h)

end CP030FiniteComponentCells

#print axioms CP030FiniteComponentCells.norm_of_coordinate_caps
#print axioms CP030FiniteComponentCells.left_coarse_of_scalar
#print axioms CP030FiniteComponentCells.right_coarse_of_scalar
#print axioms CP030FiniteComponentCells.original_narrow_zero_of_scalar_cells
