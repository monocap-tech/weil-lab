import WeilDefect.Morphology.NeutralLogMetricJumpCap
import Mathlib.MeasureTheory.Integral.ExpDecay

namespace WeilDefect
noncomputable section
open MeasureTheory Set Real

/-- Exponential damping gives an integrable spatial far-tail majorant. -/
theorem neutralLogMetricJumpDensity_le_inverse_square (r : ℝ) (hr : 0 < r) :
    neutralLogMetricJumpDensity r ≤
      (1 / (2 * Real.pi ^ 2 * Real.exp 1)) / r ^ 2 := by
  have hd : 0 < 4 * Real.pi ^ 2 * r ^ 2 := by positivity
  have hdom := (exp_neg_integrableOn_Ioi 0 (Real.exp_pos (1 : ℝ))).div_const
    (4 * Real.pi ^ 2 * r ^ 2)
  have hi : (∫ t in Ioi (0 : ℝ),
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)) ≤
      ∫ t in Ioi (0 : ℝ),
        Real.exp (-(Real.exp 1) * t) / (4 * Real.pi ^ 2 * r ^ 2) := by
    apply integral_mono_ae (neutralLogMetricJumpDensity_integrable r hr) hdom
    filter_upwards [] with t
    exact div_le_div_of_nonneg_left (Real.exp_pos _).le hd
      (by nlinarith [sq_nonneg t])
  have he : (∫ t in Ioi (0 : ℝ), Real.exp (-(Real.exp 1) * t)) =
      1 / Real.exp 1 := by
    rw [integral_exp_mul_Ioi (neg_neg_of_pos (Real.exp_pos (1 : ℝ))) 0]
    simp
  unfold neutralLogMetricJumpDensity
  calc
    2 * (∫ t in Ioi (0 : ℝ),
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2))
        ≤ 2 * ((1 / Real.exp 1) / (4 * Real.pi ^ 2 * r ^ 2)) := by
      rw [integral_div, he] at hi
      linarith
    _ = (1 / (2 * Real.pi ^ 2 * Real.exp 1)) / r ^ 2 := by
      field_simp [ne_of_gt hr, ne_of_gt Real.pi_pos, Real.exp_ne_zero (1 : ℝ)] <;> ring

private theorem metricEndpoint_inverse_square_integrable (d : ℝ) (hd : 0 < d) :
    IntegrableOn (fun r : ℝ => 1 / r ^ 2) (Ioi d) := by
  have h := integrableOn_Ioi_rpow_of_lt (a := (-2 : ℝ)) (by norm_num) hd
  apply h.congr_fun _ measurableSet_Ioi
  intro r hr
  change r ^ (-(2 : ℝ)) = 1 / r ^ 2
  rw [Real.rpow_neg (le_of_lt (hd.trans hr)), Real.rpow_two, one_div]

private theorem metricEndpoint_inverse_square_integral (d : ℝ) (hd : 0 < d) :
    (∫ r in Ioi d, 1 / r ^ 2) = 1 / d := by
  have heq : EqOn (fun r : ℝ => 1 / r ^ 2) (fun r : ℝ => r ^ (-2 : ℝ)) (Ioi d) := by
    intro r hr
    change 1 / r ^ 2 = r ^ (-(2 : ℝ))
    rw [Real.rpow_neg (le_of_lt (hd.trans hr)), Real.rpow_two, one_div]
  rw [setIntegral_congr_fun measurableSet_Ioi heq,
    integral_Ioi_rpow_of_lt (by norm_num : (-2 : ℝ) < -1) hd]
  norm_num [Real.rpow_neg_one, one_div]

/-- Every endpoint tail at positive distance genuinely converges. -/
theorem neutralLogMetricEndpointTail_integrable (d : ℝ) (hd : 0 < d) :
    IntegrableOn neutralLogMetricJumpDensity (Ioi d) := by
  have hdom := (metricEndpoint_inverse_square_integrable d hd).const_mul
    (1 / (2 * Real.pi ^ 2 * Real.exp 1))
  apply hdom.mono' neutralLogMetricJumpDensity_measurable.aestronglyMeasurable
  filter_upwards [ae_restrict_mem measurableSet_Ioi] with r hr
  rw [Real.norm_eq_abs, abs_of_nonneg (neutralLogMetricJumpDensity_nonnegative r)]
  have h := neutralLogMetricJumpDensity_le_inverse_square r (hd.trans hr)
  simpa only [div_eq_mul_inv, one_mul] using h

/-- Quantitative endpoint-tail bound at strictly positive distance. -/
theorem neutralLogMetricEndpointTail_le (d : ℝ) (hd : 0 < d) :
    neutralLogMetricEndpointTail d ≤
      (1 / (2 * Real.pi ^ 2 * Real.exp 1)) / d := by
  have hdom := (metricEndpoint_inverse_square_integrable d hd).const_mul
    (1 / (2 * Real.pi ^ 2 * Real.exp 1))
  unfold neutralLogMetricEndpointTail
  calc
    (∫ r in Ioi d, neutralLogMetricJumpDensity r) ≤
        ∫ r in Ioi d, (1 / (2 * Real.pi ^ 2 * Real.exp 1)) * (1 / r ^ 2) := by
      apply integral_mono_ae (neutralLogMetricEndpointTail_integrable d hd) hdom
      filter_upwards [ae_restrict_mem measurableSet_Ioi] with r hr
      have h := neutralLogMetricJumpDensity_le_inverse_square r (hd.trans hr)
      simpa only [div_eq_mul_inv, one_mul] using h
    _ = (1 / (2 * Real.pi ^ 2 * Real.exp 1)) / d := by
      rw [integral_const_mul, metricEndpoint_inverse_square_integral d hd]
      ring

/-- Both exterior contributions are controlled at interior points. This
coarse reciprocal-distance estimate is not an endpoint L2 bound. -/
theorem neutralLogMetricExteriorSource_le (B x : ℝ) (hx : |x| < B) :
    neutralLogMetricExteriorSource B x ≤
      (1 / (2 * Real.pi ^ 2 * Real.exp 1)) / (B - x) +
      (1 / (2 * Real.pi ^ 2 * Real.exp 1)) / (B + x) := by
  have hleft : 0 < B - x := by linarith [le_abs_self x]
  have hright : 0 < B + x := by linarith [neg_abs_le x]
  exact add_le_add (neutralLogMetricEndpointTail_le _ hleft)
    (neutralLogMetricEndpointTail_le _ hright)

end
end WeilDefect
