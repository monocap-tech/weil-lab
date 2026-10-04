import WeilDefect.Arithmetic.ActualZetaLiteralFormula
import WeilDefect.Morphology.NeutralWeilMultiplier

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped FourierTransform BigOperators

/-- The literal prime summand on the fixed inverse correlation. -/
def neutralActualZetaGreenPrimeSummand
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (n : ℕ) : ℂ :=
  ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
    (neutralActualZetaGreenCorrelationInverse a v w (Real.log n) +
      neutralActualZetaGreenCorrelationInverse a v w (-Real.log n))

theorem neutralActualZetaGreenPrimeSummand_zero
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) (n : ℕ)
    (hn : n ∉ rightLimitPrimePowerFinset a) :
    neutralActualZetaGreenPrimeSummand a v w n = 0 := by
  by_cases hpp : IsPrimePow n
  · have hlog : 2 * a < Real.log (n : ℝ) := by
      apply lt_of_not_ge
      intro h
      exact hn ((mem_rightLimitPrimePowerFinset a n).2 ⟨hpp, h⟩)
    have hp : Real.log (n : ℝ) ∉ Set.Icc (-(2 * a)) (2 * a) := by
      intro h
      linarith [h.2]
    have hm : -Real.log (n : ℝ) ∉ Set.Icc (-(2 * a)) (2 * a) := by
      intro h
      linarith [h.1]
    simp only [neutralActualZetaGreenPrimeSummand,
      neutralActualZetaGreenCorrelationInverse_supported a ha v w _ hp,
      neutralActualZetaGreenCorrelationInverse_supported a ha v w _ hm, add_zero, mul_zero]
  · have hz := ArithmeticFunction.vonMangoldt_eq_zero_iff.mpr hpp
    simp [neutralActualZetaGreenPrimeSummand, hz]

theorem neutralActualZetaGreenPrimeSummand_summable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Summable (neutralActualZetaGreenPrimeSummand a v w) := by
  apply summable_of_hasFiniteSupport
  apply (rightLimitPrimePowerFinset a).finite_toSet.subset
  intro n hn
  by_contra h
  exact hn (neutralActualZetaGreenPrimeSummand_zero a ha v w n h)

theorem neutralActualZetaGreenPrimeForm_finite
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenPrimeForm a v w =
      ∑ n ∈ rightLimitPrimePowerFinset a, neutralActualZetaGreenPrimeSummand a v w n := by
  exact tsum_eq_sum (fun n hn => neutralActualZetaGreenPrimeSummand_zero a ha v w n hn)

/-- Evaluation of this same correlation in the dual Fourier integral. -/
theorem neutralActualZetaGreenCorrelationInverse_spectral
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (t : ℝ) :
    neutralActualZetaGreenCorrelationInverse a v w t =
      neutralRawTransform (neutralActualZetaGreenCorrelationSpectrum a v w)
        ((2 * Real.pi * t : ℝ) : ℂ) := by
  unfold neutralActualZetaGreenCorrelationInverse
  rw [Real.fourierInv_eq_fourier_neg, neutralRawTransform_fourier]
  congr 1
  push_cast
  ring

private theorem real_phase_integrable (f : ℝ → ℂ) (hf : Integrable f) (t : ℝ) :
    Integrable (fun ξ : ℝ => f ξ *
      Complex.exp (Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ))) := by
  apply hf.mul_bdd (c := 1)
    (show Continuous (fun ξ : ℝ =>
      Complex.exp (Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ))) from by
        fun_prop).aestronglyMeasurable
  filter_upwards [] with ξ
  simp [Complex.norm_exp, Complex.mul_re, Complex.mul_im]

private theorem real_phase_pair (x : ℝ) :
    Complex.exp (Complex.I * (x : ℂ)) + Complex.exp (Complex.I * ((-x : ℝ) : ℂ)) =
      (2 : ℂ) * (Real.cos x : ℂ) := by
  simp only [Complex.ofReal_neg, mul_neg, mul_comm Complex.I (x : ℂ)]
  rw [Complex.ofReal_cos, Complex.cos]
  ring

private theorem pair_integrand (a : ℝ) (v w : NeutralActualZetaGreenCoefficients)
    (t ξ : ℝ) :
    neutralActualZetaGreenCorrelationSpectrum a v w ξ *
        Complex.exp (Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ)) +
      neutralActualZetaGreenCorrelationSpectrum a v w ξ *
        Complex.exp (Complex.I * ((2 * Real.pi * (-t) : ℝ) : ℂ) * (ξ : ℂ)) =
      neutralActualZetaGreenCorrelationSpectrum a v w ξ *
        ((2 : ℂ) * (Real.cos ((2 * Real.pi * ξ) * t) : ℂ)) := by
  have hp : Complex.I * ((2 * Real.pi * t : ℝ) : ℂ) * (ξ : ℂ) =
      Complex.I * (((2 * Real.pi * ξ) * t : ℝ) : ℂ) := by push_cast; ring
  have hm : Complex.I * ((2 * Real.pi * (-t) : ℝ) : ℂ) * (ξ : ℂ) =
      Complex.I * ((-((2 * Real.pi * ξ) * t) : ℝ) : ℂ) := by push_cast; ring
  rw [hp, hm, ← mul_add, real_phase_pair]

theorem neutralActualZetaGreenCorrelationInverse_pair_spectral
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (t : ℝ) :
    neutralActualZetaGreenCorrelationInverse a v w t +
      neutralActualZetaGreenCorrelationInverse a v w (-t) =
      ∫ ξ : ℝ, neutralActualZetaGreenCorrelationSpectrum a v w ξ *
        ((2 : ℂ) * (Real.cos ((2 * Real.pi * ξ) * t) : ℂ)) := by
  rw [neutralActualZetaGreenCorrelationInverse_spectral,
    neutralActualZetaGreenCorrelationInverse_spectral]
  unfold neutralRawTransform
  rw [← integral_add
    (real_phase_integrable _ (neutralActualZetaGreenCorrelationSpectrum_integrable a v w) t)
    (real_phase_integrable _ (neutralActualZetaGreenCorrelationSpectrum_integrable a v w) (-t))]
  apply integral_congr_ae
  filter_upwards [] with ξ
  exact pair_integrand a v w t ξ

private theorem prime_integrand_eq
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (n : ℕ) (ξ : ℝ) :
    ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
      (neutralActualZetaGreenCorrelationSpectrum a v w ξ *
        ((2 : ℂ) * (Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℂ))) =
    ((compactWindowPrimeCoefficient n *
      Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ) *
      neutralActualZetaGreenCorrelationSpectrum a v w ξ := by
  unfold compactWindowPrimeCoefficient
  push_cast
  ring

private theorem prime_integrand_integrable
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (n : ℕ) :
    Integrable (fun ξ : ℝ =>
      ((compactWindowPrimeCoefficient n *
        Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ) *
        neutralActualZetaGreenCorrelationSpectrum a v w ξ) := by
  have h := ((real_phase_integrable _
    (neutralActualZetaGreenCorrelationSpectrum_integrable a v w) (Real.log n)).add
    (real_phase_integrable _
      (neutralActualZetaGreenCorrelationSpectrum_integrable a v w) (-Real.log n))).const_mul
        ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)
  apply h.congr
  filter_upwards [] with ξ
  simp only [Pi.add_apply]
  rw [pair_integrand, prime_integrand_eq]

theorem neutralActualZetaGreenPrimeSummand_spectral
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (n : ℕ) :
    neutralActualZetaGreenPrimeSummand a v w n =
      ∫ ξ : ℝ, ((compactWindowPrimeCoefficient n *
        Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ) *
        neutralActualZetaGreenCorrelationSpectrum a v w ξ := by
  unfold neutralActualZetaGreenPrimeSummand
  rw [neutralActualZetaGreenCorrelationInverse_pair_spectral, ← integral_const_mul]
  apply integral_congr_ae
  filter_upwards [] with ξ
  exact prime_integrand_eq a v w n ξ

/-- Exact right-limit prime multiplier on this same mixed Fourier carrier. -/
theorem neutralActualZetaGreenPrimeForm_spectral
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenPrimeForm a v w =
      ∫ ξ : ℝ, (rightLimitPrimeSymbol a (2 * Real.pi * ξ) : ℂ) *
        neutralActualZetaGreenCorrelationSpectrum a v w ξ := by
  rw [neutralActualZetaGreenPrimeForm_finite]
  simp_rw [neutralActualZetaGreenPrimeSummand_spectral]
  rw [← integral_finset_sum _ (fun n _ => prime_integrand_integrable a v w n)]
  apply integral_congr_ae
  filter_upwards [] with ξ
  simp only [rightLimitPrimeSymbol, Complex.ofReal_sum, Finset.sum_mul]

end
end WeilDefect
