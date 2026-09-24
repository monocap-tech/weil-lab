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

/-- WD-X03: an explicit jointly-over-budget witness, using (r=3/4). -/
theorem wd_x03_explicit_witness :
    let r : ℝ := 3 / 4
    0 < 1 - r ^ 2 ∧ 1 - 2 * r ^ 2 < 0 := by
  norm_num

/-- WD-X04: the 2×2 Schur complement is exactly (1-r^2). -/
theorem wd_x04_shorted_covariance_identity (r : ℝ) :
    (1 : ℝ) - r * (1 : ℝ)⁻¹ * r = 1 - r ^ 2 := by
  ring

/--
WD-X04: there is no uniform positive lower floor for the shorted covariance
over the family (K_r) as (r) approaches (1) from below.
-/
theorem wd_x04_no_uniform_shorted_floor
    (ε : ℝ)
    (hε : 0 < ε)
    (hε1 : ε < 1) :
    ∃ r : ℝ,
      0 < r ∧
      r < 1 ∧
      0 < 1 - r ^ 2 ∧
      1 - r ^ 2 < ε := by
  refine ⟨1 - ε / 2, ?_⟩
  constructor
  · nlinarith
  constructor
  · nlinarith
  constructor
  · nlinarith [sq_nonneg ε]
  · nlinarith [sq_nonneg ε]

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
