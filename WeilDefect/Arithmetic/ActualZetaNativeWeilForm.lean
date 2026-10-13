import WeilDefect.Arithmetic.ActualZetaArchimedeanTransport

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped FourierTransform ComplexConjugate
set_option maxHeartbeats 800000

private theorem prime_term_integrable
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (n : ℕ) :
    Integrable (fun ξ : ℝ =>
      ((compactWindowPrimeCoefficient n *
        Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ) *
          neutralActualZetaGreenCorrelationSpectrum a v w ξ) := by
  have h := (neutralActualZetaGreenCorrelationSpectrum_integrable a v w).mul_bdd
    (c := |compactWindowPrimeCoefficient n|)
    (show Continuous (fun ξ : ℝ =>
      ((compactWindowPrimeCoefficient n *
        Real.cos ((2 * Real.pi * ξ) * Real.log n) : ℝ) : ℂ)) from by
          fun_prop).aestronglyMeasurable
    (by
      filter_upwards [] with ξ
      simp only [Complex.norm_real, Real.norm_eq_abs, abs_mul]
      simpa using mul_le_mul_of_nonneg_left
        (Real.abs_cos_le_one ((2 * Real.pi * ξ) * Real.log n))
        (abs_nonneg (compactWindowPrimeCoefficient n)))
  apply h.congr
  filter_upwards [] with ξ
  exact mul_comm _ _

/-- The finite right-limit prime spectral pairing is absolutely integrable. -/
theorem neutralActualZetaGreenPrime_spectral_integrable
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (fun ξ : ℝ => (rightLimitPrimeSymbol a (2 * Real.pi * ξ) : ℂ) *
      neutralActualZetaGreenCorrelationSpectrum a v w ξ) := by
  have h := integrable_finset_sum (rightLimitPrimePowerFinset a)
    (fun n _ => prime_term_integrable a v w n)
  apply h.congr
  filter_upwards [] with ξ
  simp only [rightLimitPrimeSymbol, Complex.ofReal_sum, Finset.sum_mul]

/-- The signed native Weil multiplier is integrable on these actual Green carriers. -/
theorem neutralActualZetaGreenWeil_spectral_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
      neutralActualZetaGreenCorrelationSpectrum a v w ξ) := by
  have h := (neutralActualZetaGreenArchimedean_spectral_integrable a ha v w).sub
    (neutralActualZetaGreenPrime_spectral_integrable a v w)
  apply h.congr
  filter_upwards [] with ξ
  simp only [Pi.sub_apply, rightLimitCompactWeilSymbolMathlib,
    rightLimitCompactWeilSymbol, Complex.ofReal_sub, sub_mul]

/-- The actual full-divisor zero form equals the exact native Weil multiplier
plus the existing pole operator on the same canonical Green images. -/
theorem neutralActualZetaGreenZeroForm_native
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenZeroForm a v w =
      (∫ ξ : ℝ, (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        neutralActualZetaGreenCorrelationSpectrum a v w ξ) +
      inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
        (neutralLogPoleOperator a
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) := by
  have hm : (∫ ξ : ℝ, (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
      neutralActualZetaGreenCorrelationSpectrum a v w ξ) =
    (∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
      neutralActualZetaGreenCorrelationSpectrum a v w ξ) -
    (∫ ξ : ℝ, (rightLimitPrimeSymbol a (2 * Real.pi * ξ) : ℂ) *
      neutralActualZetaGreenCorrelationSpectrum a v w ξ) := by
    rw [← integral_sub
      (neutralActualZetaGreenArchimedean_spectral_integrable a ha v w)
      (neutralActualZetaGreenPrime_spectral_integrable a v w)]
    apply integral_congr_ae
    filter_upwards [] with ξ
    simp only [rightLimitCompactWeilSymbolMathlib, rightLimitCompactWeilSymbol,
      Complex.ofReal_sub, sub_mul]
  rw [neutralActualZetaGreenZeroForm_arithmetic a ha v w,
    neutralActualZetaGreenPrimeForm_spectral a ha v w,
    neutralActualZetaGreenArchimedeanForm_spectral a ha v w, hm]
  ring

/-- The native identity in the existing physical mixed Fourier convention.
No retained spectral operator-domain premise is introduced. -/
theorem neutralActualZetaGreenZeroForm_native_mixed
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenZeroForm a v w =
      (∫ ξ : ℝ, conj ((𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
          (𝓕 (neutralActualZetaGreenSynthesis a w) : RealComplexL2) ξ) +
      inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
        (neutralLogPoleOperator a
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) := by
  rw [neutralActualZetaGreenZeroForm_native a ha v w]
  congr 1
  apply integral_congr_ae
  filter_upwards [] with ξ
  unfold neutralActualZetaGreenCorrelationSpectrum
  ring

/-- The actual zero-form diagonal has the native real signed Fourier energy
and the same canonical-image pole pairing; no positivity is asserted. -/
theorem neutralActualZetaGreenZeroForm_native_diagonal
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenZeroForm a v v =
      ((∫ ξ : ℝ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2 : ℝ) : ℂ) +
      inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
        (neutralLogPoleOperator a
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) := by
  rw [neutralActualZetaGreenZeroForm_native a ha v v]
  congr 1
  calc
    _ = ∫ ξ : ℝ, ((rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2 : ℝ) : ℂ) := by
      apply integral_congr_ae
      filter_upwards [] with ξ
      simp only [neutralActualZetaGreenCorrelationSpectrum, Complex.conj_mul',
        Complex.ofReal_mul, Complex.ofReal_pow]
    _ = _ := integral_complex_ofReal

end
end WeilDefect
