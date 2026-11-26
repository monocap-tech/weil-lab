import WeilDefect.Arithmetic.ActualZetaIV103OriginalSchwartzSpectralAttachment
import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-- Supported Schwartz representative of the literal window correlation.
Translation preserves the almost-everywhere equality of the representatives. -/
theorem neutralIV106E8Representative (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0) (t : ℝ) :
    neutralIV103Correlation a v v t =
      ∫ x : ℝ, v x * conj (v (x-t)) := by
  unfold neutralIV103Correlation neutralWindowCorrelation
  have h := neutralIV006Schwartz_window_ae a v hv
  have ht := (measurePreserving_add_right (volume : Measure ℝ) (-t)).quasiMeasurePreserving.ae h
  apply integral_congr_ae
  filter_upwards [h,ht] with x hx hxt
  rw [hx, sub_eq_add_neg, hxt]

/-- Shift to the positive-lag physical autocorrelation coordinates. -/
theorem neutralIV106E8Positive (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0) (t : ℝ) :
    neutralIV103Correlation a v v t =
      ∫ x : ℝ, conj (v x)*v (x+t) := by
  rw [neutralIV106E8Representative a v hv]
  let f : ℝ → ℂ := fun x => v x * conj (v (x-t))
  calc
    (∫ x : ℝ, f x) = ∫ x : ℝ, f (x+t) :=
      (integral_add_right_eq_self (μ := volume) f t).symm
    _ = _ := by
      apply integral_congr_ae
      filter_upwards [] with x
      dsimp [f]
      rw [add_sub_cancel_right, mul_comm]

/-- Exact conjugacy of the negative lag, without any numerical normalization. -/
theorem neutralIV106E8Negative (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0) (t : ℝ) :
    neutralIV103Correlation a v v (-t) =
      conj (neutralIV103Correlation a v v t) := by
  rw [neutralIV106E8Representative a v hv, neutralIV106E8Positive a v hv,
    ← integral_conj]
  apply integral_congr_ae
  filter_upwards [] with x
  simp [sub_neg_eq_add, map_mul, mul_comm]

/-- Compact support supplies true integrability of the physical product. -/
theorem neutralIV106E8Integrable (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0) (t : ℝ) :
    Integrable (fun x : ℝ => conj (v x)*v (x+t)) := by
  have hc : Continuous (fun x : ℝ => conj (v x)*v (x+t)) :=
    (Complex.continuous_conj.comp v.continuous).mul
      (v.continuous.comp (continuous_id.add continuous_const))
  have hs : HasCompactSupport (fun x : ℝ => conj (v x)*v (x+t)) := by
    apply HasCompactSupport.intro (K := Set.Icc (-a) a) isCompact_Icc
    intro x hx
    simp [hv x hx]
  exact hc.integrable_of_hasCompactSupport hs

/-- Real-part transport from the original complex correlation to the fiber integrand. -/
theorem neutralIV106E8Real (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0) (t : ℝ) :
    (neutralIV103Correlation a v v t).re =
      ∫ x : ℝ, (star (v x)*v (x+t)).re := by
  rw [neutralIV106E8Positive a v hv]
  simpa only [Complex.star_def] using
    (integral_re (neutralIV106E8Integrable a v hv t)).symm

/-- The literal IV085 summand carries precisely twice the positive-lag energy. -/
theorem neutralIV106E8Summand (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-a) a, v x = 0) (n : ℕ) :
    (neutralIV085PrimeSummand (neutralIV103Correlation a v v) n).re =
      2*(ArithmeticFunction.vonMangoldt n / Real.sqrt n)*
        (∫ x : ℝ, (star (v x)*v (x+Real.log n)).re) := by
  unfold neutralIV085PrimeSummand
  rw [neutralIV106E8Negative a v hv]
  simp only [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    Complex.add_re, Complex.conj_re, zero_mul, sub_zero]
  rw [neutralIV106E8Real a v hv]
  ring

#print axioms neutralIV106E8Representative
#print axioms neutralIV106E8Positive
#print axioms neutralIV106E8Negative
#print axioms neutralIV106E8Integrable
#print axioms neutralIV106E8Real
#print axioms neutralIV106E8Summand
end
end WeilDefect
