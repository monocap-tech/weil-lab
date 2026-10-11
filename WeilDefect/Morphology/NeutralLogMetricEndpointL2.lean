import WeilDefect.Morphology.NeutralLogMetricEndpointLog
import WeilDefect.Morphology.NeutralLogMetricEndpointMeasurable
import Mathlib.Analysis.SpecialFunctions.Integrability.Basic
import Mathlib.MeasureTheory.Function.L2Space

namespace WeilDefect
noncomputable section
open MeasureTheory Set Real

/-- A globally positive-distance integrable majorant for the squared log. -/
theorem neutralLogMetric_log_sq_le (d : ℝ) (hd : 0 < d) :
    Real.log d ^ 2 ≤ 16 * (d ^ (-(1 / 2 : ℝ)) + d ^ (1 / 2 : ℝ)) := by
  have hpow (a : ℝ) : (d ^ a) ^ 2 = d ^ (a * 2) := by
    rw [← Real.rpow_natCast (d ^ a) 2, ← Real.rpow_mul hd.le]
    norm_num
  by_cases hd1 : d ≤ 1
  · have hl : Real.log d ≤ 0 := Real.log_nonpos hd.le hd1
    have hb := Real.log_le_sub_one_of_pos (Real.rpow_pos_of_pos hd (-(1 / 4 : ℝ)))
    rw [Real.log_rpow hd] at hb
    have ha : |Real.log d| ≤ 4 * d ^ (-(1 / 4 : ℝ)) := by
      rw [abs_of_nonpos hl]
      linarith
    have hs := (sq_le_sq₀ (abs_nonneg (Real.log d))
      (by positivity : 0 ≤ 4 * d ^ (-(1 / 4 : ℝ)))).mpr ha
    rw [sq_abs, mul_pow, hpow] at hs
    norm_num at hs
    have hp := Real.rpow_nonneg hd.le (1 / 2 : ℝ)
    nlinarith
  · have hl : 0 ≤ Real.log d := Real.log_nonneg (le_of_lt (lt_of_not_ge hd1))
    have hb := Real.log_le_sub_one_of_pos (Real.rpow_pos_of_pos hd (1 / 4 : ℝ))
    rw [Real.log_rpow hd] at hb
    have ha : |Real.log d| ≤ 4 * d ^ (1 / 4 : ℝ) := by
      rw [abs_of_nonneg hl]
      linarith
    have hs := (sq_le_sq₀ (abs_nonneg (Real.log d))
      (by positivity : 0 ≤ 4 * d ^ (1 / 4 : ℝ))).mpr ha
    rw [sq_abs, mul_pow, hpow] at hs
    norm_num at hs
    have hp := Real.rpow_nonneg hd.le (-(1 / 2 : ℝ))
    nlinarith

/-- Squared logarithms genuinely converge down to an endpoint. -/
theorem neutralLogMetric_log_sq_integrableOn (D : ℝ) (hD : 0 ≤ D) :
    IntegrableOn (fun d : ℝ => Real.log d ^ 2) (Ioc 0 D) := by
  have hm : IntegrableOn (fun d : ℝ => d ^ (-(1 / 2 : ℝ))) (Ioc 0 D) :=
    (intervalIntegrable_iff_integrableOn_Ioc_of_le hD).mp
      (intervalIntegral.intervalIntegrable_rpow' (by norm_num))
  have hp : IntegrableOn (fun d : ℝ => d ^ (1 / 2 : ℝ)) (Ioc 0 D) :=
    (intervalIntegrable_iff_integrableOn_Ioc_of_le hD).mp
      (intervalIntegral.intervalIntegrable_rpow' (by norm_num))
  apply ((hm.add hp).const_mul 16).mono' (by fun_prop)
  filter_upwards [ae_restrict_mem measurableSet_Ioc] with d hd
  change ‖Real.log d ^ 2‖ ≤ 16 * (d ^ (-(1 / 2 : ℝ)) + d ^ (1 / 2 : ℝ))
  rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg (Real.log d))]
  exact neutralLogMetric_log_sq_le d hd.1

/-- Logarithmic endpoint singularities belong to L2 on finite distance caps. -/
theorem neutralLogMetric_log_memLp_two (D : ℝ) (hD : 0 ≤ D) :
    MemLp Real.log 2 (volume.restrict (Ioc 0 D)) := by
  apply (memLp_two_iff_integrable_sq (by fun_prop)).mpr
  exact neutralLogMetric_log_sq_integrableOn D hD

/-- The actual moving endpoint tail is L2 all the way down to distance zero.
No spectral source identification is asserted by this membership theorem. -/
theorem neutralLogMetricEndpointTail_memLp_two (D : ℝ) (hD : 0 ≤ D) :
    MemLp neutralLogMetricEndpointTail 2 (volume.restrict (Ioc 0 D)) := by
  have hc : MemLp (fun _ : ℝ => 1 / (2 * Real.pi ^ 2 * Real.exp 1)) 2
      (volume.restrict (Ioc 0 D)) := memLp_const _
  have hg := hc.add (neutralLogMetric_log_memLp_two D hD).norm
  apply hg.mono' neutralLogMetricEndpointTail_measurable.aestronglyMeasurable
  filter_upwards [ae_restrict_mem measurableSet_Ioc] with d hd
  change ‖neutralLogMetricEndpointTail d‖ ≤
    1 / (2 * Real.pi ^ 2 * Real.exp 1) + ‖Real.log d‖
  rw [Real.norm_eq_abs, abs_of_nonneg (neutralLogMetricEndpointTail_nonnegative d)]
  simpa only [Pi.add_apply, Real.norm_eq_abs] using
    neutralLogMetricEndpointTail_le_abs_log d hd.1

end
end WeilDefect
