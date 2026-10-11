import WeilDefect.Morphology.NeutralLogMetricEndpointSource
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

namespace WeilDefect
noncomputable section
open MeasureTheory Set Real

private theorem metricJump_cauchy_eq (a t : ℝ) (ha : 0 < a) :
    1 / (t ^ 2 + a ^ 2) =
      (1 / a ^ 2) * (1 + ((1 / a) * t) ^ 2)⁻¹ := by
  have hd : t ^ 2 + a ^ 2 ≠ 0 := by positivity
  have hc : 1 + ((1 / a) * t) ^ 2 ≠ 0 := by positivity
  field_simp [ne_of_gt ha, hd, hc] <;> ring

private theorem metricJump_cauchy_integrable (a : ℝ) (ha : 0 < a) :
    Integrable (fun t : ℝ => 1 / (t ^ 2 + a ^ 2)) := by
  have heq : (fun t : ℝ => 1 / (t ^ 2 + a ^ 2)) =
      (fun t : ℝ => (1 / a ^ 2) * (1 + ((1 / a) * t) ^ 2)⁻¹) := by
    funext t
    exact metricJump_cauchy_eq a t ha
  rw [heq]
  exact (integrable_inv_one_add_mul_sq (by positivity : (1 : ℝ) / a ≠ 0)).const_mul _

private theorem metricJump_cauchy_integral (a : ℝ) (ha : 0 < a) :
    (∫ t : ℝ, 1 / (t ^ 2 + a ^ 2)) = Real.pi / a := by
  have heq : (fun t : ℝ => 1 / (t ^ 2 + a ^ 2)) =
      (fun t : ℝ => (1 / a ^ 2) * (1 + ((1 / a) * t) ^ 2)⁻¹) := by
    funext t
    exact metricJump_cauchy_eq a t ha
  rw [heq, integral_const_mul, integral_univ_inv_one_add_mul_sq,
    abs_of_pos (by positivity : (0 : ℝ) < 1 / a)]
  field_simp [ne_of_gt ha] <;> ring

/-- Off the diagonal, the defining jump integral genuinely converges. -/
theorem neutralLogMetricJumpDensity_integrable (r : ℝ) (hr : 0 < r) :
    IntegrableOn (fun t : ℝ =>
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2))
      (Ioi 0) := by
  have hc := (metricJump_cauchy_integrable (2 * Real.pi * r)
    (by positivity)).integrableOn (s := Ioi 0)
  apply hc.mono'
  · exact (by fun_prop : Measurable (fun t : ℝ =>
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2))).aestronglyMeasurable
  · filter_upwards [ae_restrict_mem measurableSet_Ioi] with t ht
    have he : Real.exp (-(Real.exp 1) * t) ≤ 1 := by
      rw [← Real.exp_zero]
      apply Real.exp_le_exp.mpr
      nlinarith [Real.exp_pos (1 : ℝ)]
    have hn : 0 ≤ Real.exp (-(Real.exp 1) * t) /
        (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2) := by positivity
    rw [Real.norm_eq_abs, abs_of_nonneg hn]
    have hd : 0 ≤ t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2 := by positivity
    have h := div_le_div_of_nonneg_right he hd
    rw [show (2 * Real.pi * r) ^ 2 = 4 * Real.pi ^ 2 * r ^ 2 by ring]
    exact h

/-- A conservative Cauchy majorant sufficient for Lipschitz cancellation.
Using the full line rather than its positive half costs a factor of two. -/
theorem neutralLogMetricJumpDensity_le_inv (r : ℝ) (hr : 0 < r) :
    neutralLogMetricJumpDensity r ≤ 1 / r := by
  let q : ℝ → ℝ := fun t => 1 / (t ^ 2 + (2 * Real.pi * r) ^ 2)
  have hq : Integrable q := metricJump_cauchy_integrable _ (by positivity)
  have hcomp : (∫ t in Ioi (0 : ℝ),
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)) ≤
      ∫ t in Ioi (0 : ℝ), q t := by
    apply integral_mono_ae (neutralLogMetricJumpDensity_integrable r hr) hq.integrableOn
    filter_upwards [ae_restrict_mem measurableSet_Ioi] with t ht
    have he : Real.exp (-(Real.exp 1) * t) ≤ 1 := by
      rw [← Real.exp_zero]
      apply Real.exp_le_exp.mpr
      nlinarith [Real.exp_pos (1 : ℝ)]
    have h := div_le_div_of_nonneg_right he
      (by positivity : 0 ≤ t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)
    dsimp [q]
    rw [show (2 * Real.pi * r) ^ 2 = 4 * Real.pi ^ 2 * r ^ 2 by ring]
    exact h
  have hwhole : (∫ t in Ioi (0 : ℝ), q t) ≤ ∫ t : ℝ, q t :=
    integral_mono_measure Measure.restrict_le_self
      (ae_of_all _ (fun t => by dsimp [q]; positivity)) hq
  have hmass : (∫ t : ℝ, q t) = Real.pi / (2 * Real.pi * r) :=
    metricJump_cauchy_integral _ (by positivity)
  unfold neutralLogMetricJumpDensity
  calc
    2 * (∫ t in Ioi (0 : ℝ),
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2))
        ≤ 2 * (Real.pi / (2 * Real.pi * r)) := by linarith
    _ = 1 / r := by field_simp [ne_of_gt hr, ne_of_gt Real.pi_pos] <;> ring

/-- The trial difference cancels the jump singularity pointwise, including
the diagonal, under an explicit Lipschitz modulus. -/
theorem neutralLogMetricJumpDifference_norm_le
    (v : ℝ → ℂ) (L x y : ℝ) (hL : 0 ≤ L)
    (hv : ‖v x - v y‖ ≤ L * |x - y|) :
    ‖(v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)‖ ≤ L := by
  by_cases hxy : x = y
  · subst y
    simpa using hL
  have hr : 0 < |x - y| := abs_pos.mpr (sub_ne_zero.mpr hxy)
  have hn := neutralLogMetricJumpDensity_nonnegative |x - y|
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hn]
  calc
    ‖v x - v y‖ * neutralLogMetricJumpDensity |x - y|
        ≤ (L * |x - y|) * (1 / |x - y|) :=
      mul_le_mul hv (neutralLogMetricJumpDensity_le_inv _ hr) hn
        (mul_nonneg hL (abs_nonneg _))
    _ = L := by field_simp [ne_of_gt hr] <;> ring

end
end WeilDefect
