import WeilDefect.Arithmetic.ActualZetaCorrelationPoles
import Mathlib.Analysis.Fourier.FourierTransformDeriv

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate

/-- Mixed physical L² Fourier product, in Mathlib's 2π Fourier normalization.
The first slot is conjugated; this is not the nonreal divisor partner pairing. -/
def neutralActualZetaGreenCorrelationSpectrum
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) (ξ : ℝ) : ℂ :=
  conj ((𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ) *
    (𝓕 (neutralActualZetaGreenSynthesis a w) : RealComplexL2) ξ

/-- The inverse integral of the concrete mixed Fourier product.
Identification with the compact correlation is a separate transport step. -/
def neutralActualZetaGreenCorrelationInverse
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) : ℝ → ℂ :=
  𝓕⁻ (neutralActualZetaGreenCorrelationSpectrum a v w)

private theorem mixed_norm_integrable {f g : ℝ → ℂ}
    (hf : MemLp f 2 volume) (hg : MemLp g 2 volume) :
    Integrable (fun ξ => ‖f ξ‖ * ‖g ξ‖) := by
  have hi := ((memLp_two_iff_integrable_sq_norm hf.aestronglyMeasurable).mp hf).add
    ((memLp_two_iff_integrable_sq_norm hg.aestronglyMeasurable).mp hg)
  apply hi.mono' (hf.aestronglyMeasurable.norm.mul hg.aestronglyMeasurable.norm)
  filter_upwards [] with ξ
  rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (norm_nonneg _) (norm_nonneg _))]
  nlinarith only [sq_nonneg (‖f ξ‖ - ‖g ξ‖)]

private theorem spectrum_aestronglyMeasurable
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) :
    AEStronglyMeasurable (neutralActualZetaGreenCorrelationSpectrum a v w) volume :=
  (Lp.aestronglyMeasurable
    (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2)).conj.mul
    (Lp.aestronglyMeasurable
      (𝓕 (neutralActualZetaGreenSynthesis a w) : RealComplexL2))

/-- Absolute integrability of the physical mixed Fourier product is derived from L². -/
theorem neutralActualZetaGreenCorrelationSpectrum_integrable
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (neutralActualZetaGreenCorrelationSpectrum a v w) := by
  apply (integrable_norm_iff (spectrum_aestronglyMeasurable a v w)).mp
  simpa only [neutralActualZetaGreenCorrelationSpectrum, norm_mul, Complex.norm_conj] using
    mixed_norm_integrable
      (Lp.memLp (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2))
      (Lp.memLp (𝓕 (neutralActualZetaGreenSynthesis a w) : RealComplexL2))

/-- The second absolute Fourier moment follows by putting one derived H¹
frequency factor in each slot. No retained-mode spectral premise is used. -/
theorem neutralActualZetaGreenCorrelationSpectrum_secondMoment
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (fun ξ : ℝ =>
      ‖ξ‖ ^ 2 * ‖neutralActualZetaGreenCorrelationSpectrum a v w ξ‖) := by
  have hi := mixed_norm_integrable
    (neutralActualZetaGreenSynthesis_frequency_memLp a ha v)
    (neutralActualZetaGreenSynthesis_frequency_memLp a ha w)
  apply hi.congr
  filter_upwards [] with ξ
  simp only [neutralActualZetaGreenCorrelationSpectrum, norm_mul, Complex.norm_conj,
    Complex.norm_real]
  ring

/-- All absolute Fourier moments needed for C² inversion are integrable. -/
theorem neutralActualZetaGreenCorrelationSpectrum_moments
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients)
    (n : ℕ) (hn : n ≤ 2) :
    Integrable (fun ξ : ℝ =>
      ‖ξ‖ ^ n * ‖neutralActualZetaGreenCorrelationSpectrum a v w ξ‖) := by
  have h0 := (neutralActualZetaGreenCorrelationSpectrum_integrable a v w).norm
  have h2 := neutralActualZetaGreenCorrelationSpectrum_secondMoment a ha v w
  interval_cases n
  · simpa only [pow_zero, one_mul] using h0
  · apply (h0.add h2).mono'
      ((continuous_norm.pow 1).aestronglyMeasurable.mul
        (spectrum_aestronglyMeasurable a v w).norm)
    filter_upwards [] with ξ
    rw [pow_one, Real.norm_eq_abs,
      abs_of_nonneg (mul_nonneg (norm_nonneg _) (norm_nonneg _))]
    have hξ : ‖ξ‖ ≤ 1 + ‖ξ‖ ^ 2 := by nlinarith only [sq_nonneg (‖ξ‖ - 1)]
    simpa only [add_mul, one_mul] using
      mul_le_mul_of_nonneg_right hξ
        (norm_nonneg (neutralActualZetaGreenCorrelationSpectrum a v w ξ))
  · exact h2

/-- The concrete inverse spectral integral is C² on the full real line.
Compact support and equality with the earlier correlation are not inferred here. -/
theorem neutralActualZetaGreenCorrelationInverse_contDiff
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    ContDiff ℝ 2 (neutralActualZetaGreenCorrelationInverse a v w) := by
  have h : ContDiff ℝ (2 : ℕ∞)
      (𝓕 (neutralActualZetaGreenCorrelationSpectrum a v w)) := by
    apply Real.contDiff_fourier
    intro n hn
    apply neutralActualZetaGreenCorrelationSpectrum_moments a ha v w n
    exact_mod_cast hn
  have he : neutralActualZetaGreenCorrelationInverse a v w =
      (𝓕 (neutralActualZetaGreenCorrelationSpectrum a v w)) ∘
        (fun x : ℝ => -x) := by
    funext x
    exact fourierInv_eq_fourier_neg _ _
  rw [he]
  exact h.comp contDiff_neg

end
end WeilDefect
