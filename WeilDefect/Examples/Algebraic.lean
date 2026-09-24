import Mathlib

namespace WeilDefect

/--
WD-X03: separate channel budgets can each be positive while the joint budget is negative.
The hypotheses isolate exactly the scalar inequalities used by the example.
-/
theorem wd_x03_individual_not_compositional
    (r : ℝ)
    (hIndividual : r ^ 2 < 1)
    (hJoint : 1 < 2 * r ^ 2) :
    0 < 1 - r ^ 2 ∧ 1 - 2 * r ^ 2 < 0 := by
  constructor <;> linarith

/-- WD-X04: the 2×2 Schur complement is exactly (1-r^2). -/
theorem wd_x04_shorted_covariance_identity (r : ℝ) :
    (1 : ℝ) - r * (1 : ℝ)⁻¹ * r = 1 - r ^ 2 := by
  ring

/--
WD-X07: the antisymmetric two-point rational response has the exact
inverse-square numerator.
-/
theorem wd_x07_response_identity
    (z ρ₁ ρ₂ : ℂ)
    (h₁ : z ≠ ρ₁)
    (h₂ : z ≠ ρ₂) :
    1 / (z - ρ₁) - 1 / (z - ρ₂)
      = (ρ₁ - ρ₂) / ((z - ρ₁) * (z - ρ₂)) := by
  field_simp [sub_ne_zero.mpr h₁, sub_ne_zero.mpr h₂]
  ring

end WeilDefect
