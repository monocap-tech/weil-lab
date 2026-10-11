import WeilDefect.Morphology.NeutralLogMetricTruncatedJump

namespace WeilDefect
noncomputable section
open MeasureTheory Set

theorem neutralLogMetricTruncatedJumpDensity_nonnegative (ε R r : ℝ) :
    0 ≤ neutralLogMetricTruncatedJumpDensity ε R r := by
  unfold neutralLogMetricTruncatedJumpDensity
  apply mul_nonneg (by norm_num)
  apply integral_nonneg
  intro t
  exact div_nonneg (Real.exp_pos _).le (by positivity)

/-- Absolute distance preserves the actual truncated kernel. -/
theorem neutralLogMetricTruncatedJumpDensity_abs (ε R r : ℝ) :
    neutralLogMetricTruncatedJumpDensity ε R |r| =
      neutralLogMetricTruncatedJumpDensity ε R r := by
  simp only [neutralLogMetricTruncatedJumpDensity, sq_abs]

/-- Every positive time truncation is dominated by the full jump density
away from the spatial diagonal. The full integral's convergence is used. -/
theorem neutralLogMetricTruncatedJumpDensity_le
    (ε R r : ℝ) (hε : 0 < ε) (hr : 0 < r) :
    neutralLogMetricTruncatedJumpDensity ε R r ≤ neutralLogMetricJumpDensity r := by
  have hs : Icc ε R ⊆ Ioi (0 : ℝ) := fun t ht => lt_of_lt_of_le hε ht.1
  have hi := neutralLogMetricJumpDensity_integrable r hr
  have hm : (∫ t in Icc ε R,
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)) ≤
      ∫ t in Ioi (0 : ℝ),
        Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2) := by
    exact setIntegral_mono_set hi
      (Filter.Eventually.of_forall (fun t => div_nonneg (Real.exp_pos _).le (by positivity)))
      (Filter.Eventually.of_forall hs)
  exact mul_le_mul_of_nonneg_left hm (by norm_num)

/-- Lipschitz cancellation supplies the same cutoff-independent bound
for every actual truncated jump kernel, including the diagonal. -/
theorem neutralLogMetricTruncatedJumpDifference_norm_le
    (ε R L x y : ℝ) (hε : 0 < ε) (hL : 0 ≤ L) (v : ℝ → ℂ)
    (hmod : ‖v x - v y‖ ≤ L * |x - y|) :
    ‖(v x - v y) * (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)‖ ≤ L := by
  by_cases hxy : x = y
  · subst y
    simpa using hL
  have hr : 0 < |x - y| := abs_pos.mpr (sub_ne_zero.mpr hxy)
  have hb : neutralLogMetricTruncatedJumpDensity ε R (x - y) ≤
      neutralLogMetricJumpDensity |x - y| := by
    rw [← neutralLogMetricTruncatedJumpDensity_abs ε R (x - y)]
    exact neutralLogMetricTruncatedJumpDensity_le ε R _ hε hr
  calc
    _ ≤ ‖(v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)‖ := by
      rw [norm_mul, norm_mul, Complex.norm_real, Complex.norm_real,
        Real.norm_eq_abs, Real.norm_eq_abs,
        abs_of_nonneg (neutralLogMetricTruncatedJumpDensity_nonnegative ε R (x - y)),
        abs_of_nonneg (neutralLogMetricJumpDensity_nonnegative |x - y|)]
      exact mul_le_mul_of_nonneg_left hb (norm_nonneg _)
    _ ≤ L := neutralLogMetricJumpDifference_norm_le v L x y hL hmod

/-- The full, genuinely integrable trial jump is a cutoff-independent
spatial majorant at cap-interior points. -/
theorem neutralLogMetricTruncatedTrialJump_norm_le
    (ε R B x y : ℝ) (hε : 0 < ε) (hx : x ∈ Icc (-B) B) (v : ℝ → ℂ) :
    ‖(v x - neutralLogMetricTrialZeroExtension B v y) *
      (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)‖ ≤
      ‖neutralLogMetricTrialJump B v x y‖ := by
  by_cases hxy : x = y
  · subst y
    simp [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension, hx]
  have hr : 0 < |x - y| := abs_pos.mpr (sub_ne_zero.mpr hxy)
  have hb : neutralLogMetricTruncatedJumpDensity ε R (x - y) ≤
      neutralLogMetricJumpDensity |x - y| := by
    rw [← neutralLogMetricTruncatedJumpDensity_abs ε R (x - y)]
    exact neutralLogMetricTruncatedJumpDensity_le ε R _ hε hr
  unfold neutralLogMetricTrialJump
  rw [norm_mul, norm_mul, Complex.norm_real, Complex.norm_real,
    Real.norm_eq_abs, Real.norm_eq_abs,
    abs_of_nonneg (neutralLogMetricTruncatedJumpDensity_nonnegative ε R (x - y)),
    abs_of_nonneg (neutralLogMetricJumpDensity_nonnegative |x - y|)]
  exact mul_le_mul_of_nonneg_left hb (norm_nonneg _)

end
end WeilDefect
