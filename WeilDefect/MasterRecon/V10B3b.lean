import WeilDefect.MasterRecon.V10B3a
import Mathlib.MeasureTheory.Integral.MeanInequalities
import Mathlib.MeasureTheory.Measure.Prod

/-! V10B3b: nonnegative squared-energy Young receiver.
Use Hölder in half-power form and Tonelli, keeping translation
invariance and pointwise weighted Fourier domination explicit.
No Bochner convolution identity is asserted here. -/
namespace WeilDefect.MasterRecon.V10B3b

open MeasureTheory
open scoped ENNReal

theorem half_power_product (a b : ℝ≥0∞) :
    a ^ (1/2 : ℝ) * (a * b ^ (2 : ℝ)) ^ (1/2 : ℝ) = a * b := by
  rw [ENNReal.mul_rpow_of_nonneg _ _ (by norm_num : (0 : ℝ) ≤ 1/2),
    ← ENNReal.rpow_mul]
  have h : (2 : ℝ) * (1/2 : ℝ) = 1 := by norm_num
  rw [h, ENNReal.rpow_one, ← mul_assoc,
    ← ENNReal.rpow_add_of_nonneg (by norm_num : (0 : ℝ) ≤ 1/2)
      (by norm_num : (0 : ℝ) ≤ 1/2)]
  norm_num

theorem half_power_square (a b : ℝ≥0∞) :
    (a ^ (1/2 : ℝ) * b ^ (1/2 : ℝ)) ^ (2 : ℝ) = a * b := by
  rw [ENNReal.mul_rpow_of_nonneg _ _ (by norm_num : (0 : ℝ) ≤ 2),
    ← ENNReal.rpow_mul, ← ENNReal.rpow_mul]
  norm_num

theorem weighted_cs {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (k f : α → ℝ≥0∞) (hk : Measurable k) (hf : Measurable f) :
    (∫⁻ x, k x * f x ∂μ) ^ (2 : ℝ) ≤
      (∫⁻ x, k x ∂μ) * (∫⁻ x, k x * f x ^ (2 : ℝ) ∂μ) := by
  have h := ENNReal.lintegral_mul_norm_pow_le (μ := μ)
    hk.aemeasurable (show AEMeasurable (fun x => k x * f x ^ (2 : ℝ)) μ by
      fun_prop) (p := (1/2 : ℝ)) (q := (1/2 : ℝ))
    (by norm_num) (by norm_num) (by norm_num)
  simp only [half_power_product] at h
  have h' := ENNReal.rpow_le_rpow h (by norm_num : (0 : ℝ) ≤ 2)
  rwa [half_power_square] at h'

/-- The energy of a nonnegative convolution is bounded by the product
of the L¹ kernel mass and the translated L² energy. Translation
invariance is passed explicitly in this version of the receiver. -/
theorem convolution_square (k f : ℝ → ℝ≥0∞)
    (hk : Measurable k) (hf : Measurable f)
    (htranslate : ∀ u : ℝ, (∫⁻ y, f (y-u) ^ (2 : ℝ)) =
      ∫⁻ y, f y ^ (2 : ℝ)) :
    (∫⁻ y, (∫⁻ u, k u * f (y-u)) ^ (2 : ℝ)) ≤
      (∫⁻ u, k u) ^ (2 : ℝ) * (∫⁻ y, f y ^ (2 : ℝ)) := by
  let M : ℝ≥0∞ := ∫⁻ u, k u
  let N : ℝ≥0∞ := ∫⁻ y, f y ^ (2 : ℝ)
  have hmeas : Measurable (fun p : ℝ × ℝ => k p.2 * f (p.1-p.2) ^ (2 : ℝ)) := by
    fun_prop
  have hslice : Measurable (fun y : ℝ => ∫⁻ u, k u * f (y-u) ^ (2 : ℝ)) :=
    hmeas.lintegral_prod_right'
  calc
    (∫⁻ y, (∫⁻ u, k u * f (y-u)) ^ (2 : ℝ)) ≤
        ∫⁻ y, M * ∫⁻ u, k u * f (y-u) ^ (2 : ℝ) := by
      apply lintegral_mono
      intro y
      exact weighted_cs volume k (fun u => f (y-u)) hk (by fun_prop)
    _ = M * ∫⁻ y, ∫⁻ u, k u * f (y-u) ^ (2 : ℝ) :=
      lintegral_const_mul M hslice
    _ = M * ∫⁻ u, ∫⁻ y, k u * f (y-u) ^ (2 : ℝ) := by
      rw [lintegral_lintegral_swap hmeas.aemeasurable]
    _ = M * ∫⁻ u, k u * N := by
      congr 1
      apply lintegral_congr
      intro u
      rw [lintegral_const_mul _ (by fun_prop), htranslate u]
    _ = M * (M * N) := by rw [lintegral_mul_const _ hk]
    _ = M ^ (2 : ℝ) * N := by
      rw [show (2 : ℝ) = ((2 : ℕ) : ℝ) by norm_num, ENNReal.rpow_natCast, pow_two, mul_assoc]

/-- Receive pointwise domination by the nonnegative convolution,
without imposing Bochner integrability or a Fourier convention. -/
theorem dominated_convolution_square (g k f : ℝ → ℝ≥0∞)
    (hk : Measurable k) (hf : Measurable f)
    (htranslate : ∀ u : ℝ, (∫⁻ y, f (y-u) ^ (2 : ℝ)) =
      ∫⁻ y, f y ^ (2 : ℝ))
    (hdom : ∀ y, g y ≤ ∫⁻ u, k u * f (y-u)) :
    (∫⁻ y, g y ^ (2 : ℝ)) ≤
      (∫⁻ u, k u) ^ (2 : ℝ) * (∫⁻ y, f y ^ (2 : ℝ)) := by
  exact (lintegral_mono (fun y => ENNReal.rpow_le_rpow (hdom y) (by norm_num))).trans
    (convolution_square k f hk hf htranslate)

end WeilDefect.MasterRecon.V10B3b

#print axioms WeilDefect.MasterRecon.V10B3b.half_power_product
#print axioms WeilDefect.MasterRecon.V10B3b.half_power_square
#print axioms WeilDefect.MasterRecon.V10B3b.weighted_cs
#print axioms WeilDefect.MasterRecon.V10B3b.convolution_square
#print axioms WeilDefect.MasterRecon.V10B3b.dominated_convolution_square
