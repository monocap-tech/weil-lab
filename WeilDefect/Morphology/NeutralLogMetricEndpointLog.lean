import WeilDefect.Morphology.NeutralLogMetricEndpointBounds
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

namespace WeilDefect
noncomputable section
open MeasureTheory Set Real

/-- The positive-distance tail is obtained by splitting at distance one. -/
theorem neutralLogMetricEndpointTail_split (d : ℝ) (hd : 0 < d) :
    neutralLogMetricEndpointTail d =
      (∫ r in d..1, neutralLogMetricJumpDensity r) +
        neutralLogMetricEndpointTail 1 := by
  exact (intervalIntegral.integral_interval_add_Ioi
    (neutralLogMetricEndpointTail_integrable d hd)
    (neutralLogMetricEndpointTail_integrable 1 zero_lt_one)).symm

/-- Integrating the near-diagonal 1/r majorant gives logarithmic growth. -/
theorem neutralLogMetricEndpointTail_le_log (d : ℝ) (hd : 0 < d) (hd1 : d ≤ 1) :
    neutralLogMetricEndpointTail d ≤
      Real.log (1 / d) + 1 / (2 * Real.pi ^ 2 * Real.exp 1) := by
  have hc : ContinuousOn (fun r : ℝ => r⁻¹) (Icc d 1) :=
    continuousOn_inv₀.mono (fun r hr => ne_of_gt (hd.trans_le hr.1))
  have hi : (∫ r in d..1, neutralLogMetricJumpDensity r) ≤ Real.log (1 / d) := by
    rw [intervalIntegral.integral_of_le hd1,
      ← intervalIntegral.integral_inv_of_pos hd zero_lt_one,
      intervalIntegral.integral_of_le hd1]
    apply integral_mono_ae
      ((neutralLogMetricEndpointTail_integrable d hd).mono_set Ioc_subset_Ioi_self)
      (hc.integrableOn_Icc.mono_set Ioc_subset_Icc_self)
    filter_upwards [ae_restrict_mem measurableSet_Ioc] with r hr
    simpa only [one_div] using neutralLogMetricJumpDensity_le_inv r (hd.trans hr.1)
  rw [neutralLogMetricEndpointTail_split d hd]
  have ht := neutralLogMetricEndpointTail_le 1 zero_lt_one
  simp only [div_one] at ht
  linarith

/-- One logarithmic majorant valid at every strictly positive distance. -/
theorem neutralLogMetricEndpointTail_le_abs_log (d : ℝ) (hd : 0 < d) :
    neutralLogMetricEndpointTail d ≤
      1 / (2 * Real.pi ^ 2 * Real.exp 1) + |Real.log d| := by
  by_cases hd1 : d ≤ 1
  · have h := neutralLogMetricEndpointTail_le_log d hd hd1
    rw [Real.log_div one_ne_zero (ne_of_gt hd), Real.log_one, zero_sub] at h
    linarith [neg_abs_le (Real.log d)]
  · have h := neutralLogMetricEndpointTail_le d hd
    have hC : 0 ≤ 1 / (2 * Real.pi ^ 2 * Real.exp 1) := by positivity
    have hdiv : (1 / (2 * Real.pi ^ 2 * Real.exp 1)) / d ≤
        1 / (2 * Real.pi ^ 2 * Real.exp 1) := by
      apply (div_le_iff₀ hd).mpr
      simpa only [mul_one] using
        mul_le_mul_of_nonneg_left (le_of_lt (lt_of_not_ge hd1)) hC
    linarith [abs_nonneg (Real.log d)]

/-- Both endpoint contributions admit a logarithmic interior majorant. -/
theorem neutralLogMetricExteriorSource_le_abs_log (B x : ℝ) (hx : |x| < B) :
    neutralLogMetricExteriorSource B x ≤
      2 * (1 / (2 * Real.pi ^ 2 * Real.exp 1)) +
        |Real.log (B - x)| + |Real.log (B + x)| := by
  have hl : 0 < B - x := by linarith [le_abs_self x]
  have hr : 0 < B + x := by linarith [neg_abs_le x]
  have h := add_le_add (neutralLogMetricEndpointTail_le_abs_log _ hl)
    (neutralLogMetricEndpointTail_le_abs_log _ hr)
  unfold neutralLogMetricExteriorSource
  linarith

end
end WeilDefect
