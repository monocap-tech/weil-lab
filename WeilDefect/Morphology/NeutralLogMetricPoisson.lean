import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.Fourier.FourierTransform

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped FourierTransform

/-- Damped inverse-transform integrand at angular frequency w. -/
def neutralLogMetricPoissonIntegrand (t w ξ : ℝ) : ℂ :=
  Complex.exp (-(t : ℂ) * ((|ξ| : ℝ) : ℂ) + (w : ℂ) * Complex.I * (ξ : ℂ))

private theorem poisson_left (t w : ℝ) :
    EqOn (neutralLogMetricPoissonIntegrand t w)
      (fun ξ : ℝ => Complex.exp (((t : ℂ) + (w : ℂ) * Complex.I) * ξ)) (Iic 0) := by
  intro ξ hξ
  unfold neutralLogMetricPoissonIntegrand
  rw [abs_of_nonpos hξ, Complex.ofReal_neg]
  congr 1
  ring

private theorem poisson_right (t w : ℝ) :
    EqOn (neutralLogMetricPoissonIntegrand t w)
      (fun ξ : ℝ => Complex.exp ((-(t : ℂ) + (w : ℂ) * Complex.I) * ξ)) (Ioi 0) := by
  intro ξ hξ
  unfold neutralLogMetricPoissonIntegrand
  rw [abs_of_pos hξ]
  congr 1
  ring

/-- Absolute convergence on both half-lines. -/
theorem neutralLogMetricPoissonIntegrand_integrable (t w : ℝ) (ht : 0 < t) :
    Integrable (neutralLogMetricPoissonIntegrand t w) := by
  have hl := integrableOn_exp_mul_complex_Iic
    (a := (t : ℂ) + (w : ℂ) * Complex.I) (by simpa using ht) 0
  have hr := integrableOn_exp_mul_complex_Ioi
    (a := -(t : ℂ) + (w : ℂ) * Complex.I) (by simpa using neg_neg_of_pos ht) 0
  have hl' := hl.congr_fun (poisson_left t w).symm measurableSet_Iic
  have hr' := hr.congr_fun (poisson_right t w).symm measurableSet_Ioi
  simpa only [Iic_union_Ioi, integrableOn_univ] using hl'.union hr'

/-- Evaluating the two damped half-lines gives the exact rational kernel. -/
theorem neutralLogMetricPoisson_integral (t w : ℝ) (ht : 0 < t) :
    (∫ ξ : ℝ, neutralLogMetricPoissonIntegrand t w ξ) =
      ((2 * t / (t ^ 2 + w ^ 2) : ℝ) : ℂ) := by
  have hp : 0 < ((t : ℂ) + (w : ℂ) * Complex.I).re := by simpa using ht
  have hn : (-(t : ℂ) + (w : ℂ) * Complex.I).re < 0 := by
    simpa using neg_neg_of_pos ht
  have hl := setIntegral_congr_fun (μ := volume) measurableSet_Iic (poisson_left t w)
  have hr := setIntegral_congr_fun (μ := volume) measurableSet_Ioi (poisson_right t w)
  have hsplit := integral_add_compl measurableSet_Iic
    (neutralLogMetricPoissonIntegrand_integrable t w ht)
  rw [compl_Iic] at hsplit
  rw [← hsplit, hl, hr, integral_exp_mul_complex_Iic hp,
    integral_exp_mul_complex_Ioi hn]
  simp only [Complex.ofReal_zero, mul_zero, Complex.exp_zero]
  have hpn : (t : ℂ) + (w : ℂ) * Complex.I ≠ 0 := by
    intro h
    have := congrArg Complex.re h
    simp only [Complex.add_re, Complex.mul_re, Complex.ofReal_re,
      Complex.ofReal_im, Complex.I_re, Complex.I_im, mul_zero, zero_mul,
      sub_zero, add_zero, Complex.zero_re] at this
    linarith
  have hnn : -(t : ℂ) + (w : ℂ) * Complex.I ≠ 0 := by
    intro h
    have := congrArg Complex.re h
    simp only [Complex.add_re, Complex.neg_re, Complex.mul_re, Complex.ofReal_re,
      Complex.ofReal_im, Complex.I_re, Complex.I_im, mul_zero, zero_mul,
      sub_zero, add_zero, Complex.zero_re] at this
    linarith
  have hd : (t : ℂ) ^ 2 + (w : ℂ) ^ 2 ≠ 0 := by
    have hdreal : t ^ 2 + w ^ 2 ≠ 0 := by nlinarith [sq_pos_of_pos ht, sq_nonneg w]
    exact_mod_cast hdreal
  push_cast
  field_simp [hpn, hnn, hd] <;> ring_nf <;> simp [Complex.I_sq] <;> ring

/-- Project normalization: angular frequency is 2*pi*x. -/
def neutralLogMetricPoissonDensity (t x : ℝ) : ℝ :=
  2 * t / (t ^ 2 + 4 * Real.pi ^ 2 * x ^ 2)

theorem neutralLogMetricPoisson_integral_normalized (t x : ℝ) (ht : 0 < t) :
    (∫ ξ : ℝ, neutralLogMetricPoissonIntegrand t (2 * Real.pi * x) ξ) =
      (neutralLogMetricPoissonDensity t x : ℂ) := by
  rw [neutralLogMetricPoisson_integral t _ ht]
  unfold neutralLogMetricPoissonDensity
  have hden : t ^ 2 + (2 * Real.pi * x) ^ 2 =
      t ^ 2 + 4 * Real.pi ^ 2 * x ^ 2 := by ring
  rw [hden]

/-- The actual inverse Fourier pair, in Mathlib's 2*pi convention. -/
theorem neutralLogMetricPoisson_fourierInv (t x : ℝ) (ht : 0 < t) :
    (𝓕⁻ (fun ξ : ℝ => (Real.exp (-t * |ξ|) : ℂ))) x =
      (neutralLogMetricPoissonDensity t x : ℂ) := by
  rw [Real.fourierInv_eq']
  calc
    _ = ∫ ξ : ℝ, neutralLogMetricPoissonIntegrand t (2 * Real.pi * x) ξ := by
      apply integral_congr_ae
      filter_upwards [] with ξ
      simp only [smul_eq_mul, RCLike.inner_apply', starRingEnd_apply, star_trivial,
        Complex.ofReal_exp]
      rw [← Complex.exp_add]
      unfold neutralLogMetricPoissonIntegrand
      congr 1
      push_cast
      ring
    _ = _ := neutralLogMetricPoisson_integral_normalized t x ht

end
end WeilDefect
