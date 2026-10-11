import Mathlib.Analysis.SpecialFunctions.FrullaniIntegral
import Mathlib.MeasureTheory.Integral.ExpDecay

namespace WeilDefect

noncomputable section
open MeasureTheory Filter Set Real
open scoped Topology

/-- RC24's nonnegative Laplace integrand, with arbitrary positive damping. -/
def neutralLogMetricLaplaceIntegrand (b s t : ℝ) : ℝ :=
  Real.exp (-b * t) * (1 - Real.exp (-s * t)) / t

/-- Cancellation at zero is bounded by an integrable exponential. -/
theorem neutralLogMetricLaplaceIntegrand_bounds
    (b s t : ℝ) (hs : 0 ≤ s) (ht : 0 < t) :
    0 ≤ neutralLogMetricLaplaceIntegrand b s t ∧
      neutralLogMetricLaplaceIntegrand b s t ≤ s * Real.exp (-b * t) := by
  have hst : 0 ≤ s * t := mul_nonneg hs ht.le
  have hsmall : Real.exp (-s * t) ≤ 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_le_exp.mpr
    nlinarith
  have hlarge : 1 - Real.exp (-s * t) ≤ s * t := by
    have h := Real.add_one_le_exp (-s * t)
    linarith
  unfold neutralLogMetricLaplaceIntegrand
  constructor
  · exact div_nonneg (mul_nonneg (Real.exp_pos _).le (sub_nonneg.mpr hsmall)) ht.le
  · apply (div_le_iff₀ ht).mpr
    have h := mul_le_mul_of_nonneg_left hlarge (Real.exp_pos (-b * t)).le
    nlinarith

/-- Genuine improper convergence; no totalized-integral shortcut. -/
theorem neutralLogMetricLaplaceIntegrand_integrable
    (b s : ℝ) (hb : 0 < b) (hs : 0 ≤ s) :
    IntegrableOn (neutralLogMetricLaplaceIntegrand b s) (Ioi 0) := by
  have hdom := (exp_neg_integrableOn_Ioi 0 hb).const_mul s
  apply hdom.mono'
  · exact (by unfold neutralLogMetricLaplaceIntegrand; fun_prop : Measurable (neutralLogMetricLaplaceIntegrand b s)).aestronglyMeasurable
  · filter_upwards [ae_restrict_mem measurableSet_Ioi] with t ht
    have h := neutralLogMetricLaplaceIntegrand_bounds b s t hs ht
    simpa only [Real.norm_eq_abs, abs_of_nonneg h.1] using h.2

/-- Positive damping and nonnegative frequency give the exact logarithm. -/
theorem neutralLogMetricLaplace_integral
    (b s : ℝ) (hb : 0 < b) (hs : 0 ≤ s) :
    (∫ t in Ioi (0 : ℝ), neutralLogMetricLaplaceIntegrand b s t) =
      Real.log ((b + s) / b) := by
  have heq : (fun t : ℝ => t⁻¹ •
      (Real.exp (-(b * t)) - Real.exp (-((b + s) * t)))) =
      neutralLogMetricLaplaceIntegrand b s := by
    funext t
    unfold neutralLogMetricLaplaceIntegrand
    rw [show -(b * t) = -b * t by ring, show -((b + s) * t) = -b * t + -s * t by ring, Real.exp_add]
    simp only [smul_eq_mul, div_eq_mul_inv]
    ring
  have hc : Continuous (fun t : ℝ => Real.exp (-t)) := by fun_prop
  have hlocal : LocallyIntegrableOn (fun t : ℝ => Real.exp (-t)) (Ioi 0) :=
    hc.locallyIntegrable.locallyIntegrableOn (Ioi 0)
  have hzero : Tendsto (fun t : ℝ => Real.exp (-t)) (𝓝[>] 0) (𝓝 (1 : ℝ)) := by
    simpa using (hc.continuousAt.tendsto.mono_left nhdsWithin_le_nhds :
      Tendsto (fun t : ℝ => Real.exp (-t)) (𝓝[>] (0 : ℝ)) (𝓝 (Real.exp (-0))))
  have hinfty : Tendsto (fun t : ℝ => Real.exp (-t)) atTop (𝓝 (0 : ℝ)) :=
    Real.tendsto_exp_atBot.comp tendsto_neg_atTop_atBot
  have hint : IntegrableOn (fun t : ℝ => t⁻¹ •
      (Real.exp (-(b * t)) - Real.exp (-((b + s) * t)))) (Ioi 0) := by
    rw [heq]
    exact neutralLogMetricLaplaceIntegrand_integrable b s hb hs
  have h := Frullani.integral_Ioi_eq hlocal hb (by linarith : 0 < b + s)
    hzero hinfty hint
  rw [heq] at h
  simpa using h

/-- Exact RC24 logarithmic weight representation at damping e. -/
theorem neutralLogMetricLaplace_weight (s : ℝ) (hs : 0 ≤ s) :
    Real.log (Real.exp 1 + s) = 1 +
      ∫ t in Ioi (0 : ℝ), neutralLogMetricLaplaceIntegrand (Real.exp 1) s t := by
  rw [neutralLogMetricLaplace_integral _ _ (Real.exp_pos _) hs,
    Real.log_div (by positivity : Real.exp 1 + s ≠ 0) (Real.exp_ne_zero _),
    Real.log_exp]
  ring

end
end WeilDefect
