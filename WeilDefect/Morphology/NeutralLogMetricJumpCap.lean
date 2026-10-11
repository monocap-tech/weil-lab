import WeilDefect.Morphology.NeutralLogMetricJumpBounds
import Mathlib.MeasureTheory.Integral.Prod

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- Parameter measurability of the actual jump integral. This statement
includes totalized diagonal values; convergence off the diagonal is LF09. -/
theorem neutralLogMetricJumpDensity_measurable :
    Measurable neutralLogMetricJumpDensity := by
  have hm : Measurable (fun p : ℝ × ℝ =>
      Real.exp (-(Real.exp 1) * p.2) /
        (p.2 ^ 2 + 4 * Real.pi ^ 2 * p.1 ^ 2)) := by fun_prop
  have hi : StronglyMeasurable (fun r : ℝ => ∫ t in Ioi (0 : ℝ),
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)) :=
    hm.stronglyMeasurable.integral_prod_right'
  exact measurable_const.mul hi.measurable

/-- The actual spatial difference integrand is measurable for measurable
trials. No regularity assumption is hidden in the integral convention. -/
theorem neutralLogMetricJumpDifference_measurable
    (v : ℝ → ℂ) (hv : Measurable v) (x : ℝ) :
    Measurable (fun y : ℝ =>
      (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)) := by
  have hd : Measurable (fun y : ℝ => neutralLogMetricJumpDensity |x - y|) :=
    neutralLogMetricJumpDensity_measurable.comp (by fun_prop)
  exact (measurable_const.sub hv).mul (Complex.continuous_ofReal.measurable.comp hd)

/-- The bounded cancelled difference is genuinely integrable on any
finite cap, with an explicit pointwise modulus on that cap. -/
theorem neutralLogMetricJumpDifference_integrableOn
    (B x L : ℝ) (v : ℝ → ℂ) (hv : Measurable v) (hL : 0 ≤ L)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    IntegrableOn (fun y : ℝ =>
      (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)) (Icc (-B) B) := by
  apply Measure.integrableOn_of_bounded (by simp : volume (Icc (-B) B) ≠ ⊤)
    (neutralLogMetricJumpDifference_measurable v hv x).aestronglyMeasurable
  filter_upwards [ae_restrict_mem measurableSet_Icc] with y hy
  exact neutralLogMetricJumpDifference_norm_le v L x y hL (hmod y hy)

/-- Quantitative finite-cap budget for the internal jump source. -/
theorem neutralLogMetricJumpDifference_integral_norm_le
    (B x L : ℝ) (hB : 0 ≤ B) (v : ℝ → ℂ) (hv : Measurable v) (hL : 0 ≤ L)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    ‖∫ y in Icc (-B) B,
      (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)‖ ≤ 2 * B * L := by
  have hint := neutralLogMetricJumpDifference_integrableOn B x L v hv hL hmod
  have hc : IntegrableOn (fun _ : ℝ => L) (Icc (-B) B) := integrableOn_const
  have hbound : (∫ y in Icc (-B) B,
      ‖(v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)‖) ≤
      ∫ _ in Icc (-B) B, L := by
    apply integral_mono_ae hint.norm hc
    filter_upwards [ae_restrict_mem measurableSet_Icc] with y hy
    exact neutralLogMetricJumpDifference_norm_le v L x y hL (hmod y hy)
  calc
    ‖∫ y in Icc (-B) B,
      (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)‖
        ≤ ∫ y in Icc (-B) B,
          ‖(v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)‖ :=
      norm_integral_le_integral_norm _
    _ ≤ ∫ _ in Icc (-B) B, L := hbound
    _ = 2 * B * L := by
      rw [setIntegral_const, Real.volume_real_Icc_of_le (by linarith : -B ≤ B)]
      simp only [smul_eq_mul]
      ring

end
end WeilDefect
