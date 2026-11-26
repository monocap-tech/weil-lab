import WeilDefect.MasterRecon.V10B4b
import Mathlib.Analysis.SpecialFunctions.JapaneseBracket

/-! V10B4c: a universal weighted L¹ majorant for quadratic Fourier
decay. Parameter a reconciles angular and cycles-frequency weights. -/
namespace WeilDefect.MasterRecon.V10B4c

open MeasureTheory
open scoped FourierTransform

noncomputable def majorant (a u : ℝ) : ℝ :=
  Real.sqrt (Real.log (2 + a * |u|)) / (1 + u^2)

theorem majorant_nonnegative (a u : ℝ) : 0 ≤ majorant a u := by
  unfold majorant
  positivity

theorem majorant_continuous (a : ℝ) (ha : 0 ≤ a) :
    Continuous (majorant a) := by
  unfold majorant
  apply Continuous.div
  · apply Real.continuous_sqrt.comp
    apply Continuous.log (by fun_prop)
    intro u
    have h := mul_nonneg ha (abs_nonneg u)
    linarith
  · fun_prop
  · intro u
    positivity

theorem majorant_bound (a u : ℝ) (ha : 0 ≤ a) :
    majorant a u ≤ (2 * Real.sqrt (2+a)) *
      (1 + |u|) ^ (-(3/2) : ℝ) := by
  let v : ℝ := 1 + |u|
  have hv : 0 < v := by dsimp [v]; positivity
  have h0 : 0 ≤ 2 + a * |u| := by positivity
  have h1 : Real.log (2+a*|u|) ≤ (2+a)*v := by
    apply (Real.log_le_self h0).trans
    dsimp [v]
    nlinarith [abs_nonneg u, ha]
  have h2 := Real.sqrt_le_sqrt h1
  rw [Real.sqrt_mul (by positivity : 0 ≤ 2+a)] at h2
  have hden : v^2 ≤ 2 * (1+u^2) := by
    dsimp [v]
    nlinarith [sq_abs u, sq_nonneg (|u|-1)]
  have hrec : (1+u^2)⁻¹ ≤ 2 / v^2 := by
    apply (le_div_iff₀ (by positivity : 0 < v^2)).2
    rw [inv_mul_eq_div]
    exact (div_le_iff₀ (by positivity : 0 < 1+u^2)).2 hden
  have hpow : Real.sqrt v / v^2 = v ^ (-(3/2) : ℝ) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast]
    rw [div_eq_mul_inv, ← Real.rpow_neg hv.le, ← Real.rpow_add hv]
    norm_num
  unfold majorant
  rw [div_eq_mul_inv]
  calc
    Real.sqrt (Real.log (2+a*|u|)) * (1+u^2)⁻¹ ≤
        (Real.sqrt (2+a) * Real.sqrt v) * (2 / v^2) :=
      mul_le_mul h2 hrec (by positivity) (by positivity)
    _ = (2 * Real.sqrt (2+a)) * (Real.sqrt v / v^2) := by ring
    _ = _ := by rw [hpow]

theorem majorant_integrable (a : ℝ) (ha : 0 ≤ a) :
    Integrable (majorant a) := by
  have h : Integrable (fun u : ℝ => (1 + ‖u‖) ^ (-(3/2) : ℝ)) :=
    integrable_one_add_norm (μ := volume) (by norm_num)
  apply (h.const_mul (2 * Real.sqrt (2+a))).mono'
    (majorant_continuous a ha).aestronglyMeasurable
  filter_upwards with u
  rw [Real.norm_eq_abs, abs_of_nonneg (majorant_nonnegative a u)]
  simpa only [Real.norm_eq_abs] using majorant_bound a u ha

theorem weighted_kernel_integrable (K : ℝ → ℂ) (hK : Measurable K)
    (a C : ℝ) (ha : 0 ≤ a) (hC : 0 ≤ C)
    (hbound : ∀ u, ‖K u‖ ≤ C / (1+u^2)) :
    Integrable (fun u => Real.sqrt (Real.log (2+a*|u|)) * ‖K u‖) := by
  apply ((majorant_integrable a ha).const_mul C).mono'
  · apply Measurable.aestronglyMeasurable
    fun_prop
  · filter_upwards with u
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    unfold majorant
    calc
      Real.sqrt (Real.log (2+a*|u|)) * ‖K u‖ ≤
          Real.sqrt (Real.log (2+a*|u|)) * (C / (1+u^2)) :=
        mul_le_mul_of_nonneg_left (hbound u) (Real.sqrt_nonneg _)
      _ = _ := by ring

theorem weighted_kernel_mass_bound (K : ℝ → ℂ) (hK : Measurable K)
    (a C : ℝ) (ha : 0 ≤ a) (hC : 0 ≤ C)
    (hbound : ∀ u, ‖K u‖ ≤ C / (1+u^2)) :
    (∫ u, Real.sqrt (Real.log (2+a*|u|)) * ‖K u‖) ≤
      C * ∫ u, majorant a u := by
  rw [← integral_const_mul]
  apply integral_mono
    (weighted_kernel_integrable K hK a C ha hC hbound)
    ((majorant_integrable a ha).const_mul C)
  intro u
  unfold majorant
  calc
    Real.sqrt (Real.log (2+a*|u|)) * ‖K u‖ ≤
        Real.sqrt (Real.log (2+a*|u|)) * (C / (1+u^2)) :=
      mul_le_mul_of_nonneg_left (hbound u) (Real.sqrt_nonneg _)
    _ = _ := by ring

end WeilDefect.MasterRecon.V10B4c

#print axioms WeilDefect.MasterRecon.V10B4c.majorant_nonnegative
#print axioms WeilDefect.MasterRecon.V10B4c.majorant_continuous
#print axioms WeilDefect.MasterRecon.V10B4c.majorant_bound
#print axioms WeilDefect.MasterRecon.V10B4c.majorant_integrable
#print axioms WeilDefect.MasterRecon.V10B4c.weighted_kernel_integrable
#print axioms WeilDefect.MasterRecon.V10B4c.weighted_kernel_mass_bound
