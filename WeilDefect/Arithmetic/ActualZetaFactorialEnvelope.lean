import WeilDefect.Arithmetic.ActualZetaMellinRepresentation
import WeilDefect.Arithmetic.ActualZetaJensenGrowth

namespace WeilDefect
noncomputable section
open Set Metric
open scoped Topology

/-- Kernel-derived factorial majorant for pole-cleared completed zeta
on a natural-radius disk; the added one retains both endpoint values. -/
def neutralActualZetaFactorialMajorant (p C : ℝ) (n : ℕ) : ℝ :=
  (n : ℝ) * ((n : ℝ) + 1) *
    (C * ((n.factorial : ℝ) / (p / 2) ^ n) *
      (Real.exp (-(p / 2)) / (p / 2))) + 1

theorem neutralActualZetaFactorialMajorant_one_le
    {p C : ℝ} (hp : 0 < p) (hC : 0 < C) (n : ℕ) :
    1 ≤ neutralActualZetaFactorialMajorant p C n := by
  unfold neutralActualZetaFactorialMajorant
  have : 0 ≤ (n : ℝ) * ((n : ℝ) + 1) *
      (C * ((n.factorial : ℝ) / (p / 2) ^ n) *
        (Real.exp (-(p / 2)) / (p / 2))) := by positivity
  linarith

/-- An explicit actual entire-function disk bound from the actual
completed-zeta Mellin construction, with no supplied divisor estimate. -/
theorem neutralActualZetaEntire_factorial_bound :
    ∃ p C : ℝ, 0 < p ∧ 0 < C ∧ ∀ (n : ℕ) (z : ℂ),
      ‖z‖ ≤ (n : ℝ) →
      ‖neutralActualZetaEntire z‖ ≤ neutralActualZetaFactorialMajorant p C n := by
  obtain ⟨p, C, hp, hC, hb⟩ := neutralActualZetaCompleted_factorial_bound
  refine ⟨p, C, hp, hC, fun n z hz => ?_⟩
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hsub : ‖z - 1‖ ≤ (n : ℝ) + 1 := by
    have h := norm_sub_le z 1
    rw [norm_one] at h
    linarith
  have hprod : ‖z‖ * ‖z - 1‖ ≤ (n : ℝ) * ((n : ℝ) + 1) :=
    mul_le_mul hz hsub (norm_nonneg _) hn
  have hB : 0 ≤ C * ((n.factorial : ℝ) / (p / 2) ^ n) *
      (Real.exp (-(p / 2)) / (p / 2)) := by positivity
  unfold neutralActualZetaEntire neutralActualZetaFactorialMajorant
  calc
    _ ≤ ‖z * (z - 1) * completedRiemannZeta₀ z‖ + ‖(1 : ℂ)‖ := norm_add_le _ _
    _ = (‖z‖ * ‖z - 1‖) * ‖completedRiemannZeta₀ z‖ + 1 := by
      rw [norm_mul, norm_mul, norm_one]
    _ ≤ _ := by
      have h := mul_le_mul hprod (hb n z hz)
        (norm_nonneg _) (mul_nonneg hn (by positivity))
      linarith

/-- The actual enclosing-circle envelope has an explicit factorial
majorant as soon as the enclosing radius is bounded by the moment order. -/
theorem neutralActualZetaCircleEnvelope_factorial_bound :
    ∃ p C : ℝ, 0 < p ∧ 0 < C ∧ ∀ (T : ℝ) (n : ℕ),
      2 * (|T| + 2) ≤ (n : ℝ) →
      neutralActualZetaCircleEnvelope T ≤ neutralActualZetaFactorialMajorant p C n := by
  obtain ⟨p, C, hp, hC, hb⟩ := neutralActualZetaEntire_factorial_bound
  refine ⟨p, C, hp, hC, fun T n hn => ?_⟩
  have hr : 0 ≤ 2 * (|T| + 2) := by positivity
  have hne : ((fun z => ‖neutralActualZetaEntire z‖) ''
      sphere (0 : ℂ) (2 * (|T| + 2))).Nonempty := by
    refine ⟨‖neutralActualZetaEntire (2 * (|T| + 2) : ℝ)‖,
      ⟨(2 * (|T| + 2) : ℝ), ?_, rfl⟩⟩
    simpa only [mem_sphere, dist_zero_right, Complex.norm_real,
      Real.norm_eq_abs, abs_of_nonneg hr]
  unfold neutralActualZetaCircleEnvelope
  apply max_le (neutralActualZetaFactorialMajorant_one_le hp hC n)
  apply csSup_le hne
  rintro y ⟨z, hz, rfl⟩
  have hzR : ‖z‖ = 2 * (|T| + 2) := by
    simpa only [mem_sphere, dist_zero_right] using hz
  exact hb n z (hzR.le.trans hn)

/-- Actual multiplicity counts inherit the explicit factorial majorant
through the previously certified Jensen bound. The O(T log T)
simplification and local unit-height estimates are separate. -/
theorem neutralActualZetaDivisorHeightWindow_card_le_factorial :
    ∃ p C : ℝ, 0 < p ∧ 0 < C ∧ ∀ (T : ℝ) (n : ℕ),
      2 * (|T| + 2) ≤ (n : ℝ) →
      (Fintype.card (neutralActualZetaDivisorHeightWindow T) : ℝ) ≤
        Real.log (neutralActualZetaFactorialMajorant p C n) / Real.log 2 := by
  obtain ⟨p, C, hp, hC, hb⟩ := neutralActualZetaCircleEnvelope_factorial_bound
  refine ⟨p, C, hp, hC, fun T n hn => ?_⟩
  apply (neutralActualZetaDivisorHeightWindow_card_le_envelope T).trans
  apply div_le_div_of_nonneg_right _ (Real.log_pos (by norm_num : (1 : ℝ) < 2)).le
  exact Real.log_le_log
    (lt_of_lt_of_le zero_lt_one (neutralActualZetaCircleEnvelope_one_le T))
    (hb T n hn)

end
end WeilDefect
