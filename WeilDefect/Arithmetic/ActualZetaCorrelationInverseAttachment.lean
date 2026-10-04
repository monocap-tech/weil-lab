import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import Mathlib.MeasureTheory.Measure.OpenPos

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate SchwartzMap ContDiff
set_option maxHeartbeats 800000

private theorem inverse_correlation_pairing
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients)
    (u : SchwartzMap ℝ ℂ) :
    (∫ x, u x * neutralActualZetaGreenCorrelationInverse a v w x) =
      ∫ x, u x * neutralWindowCorrelation a
        (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w) x := by
  let K := neutralWindowCorrelation a
    (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w)
  let S := neutralActualZetaGreenCorrelationSpectrum a v w
  have hK : Integrable K := neutralWindowCorrelation_integrable a _ _
  have hS : Integrable S := neutralActualZetaGreenCorrelationSpectrum_integrable a v w
  have hi : (∫ x, u x * (𝓕⁻ S) x) = ∫ ξ, (𝓕⁻ u) ξ * S ξ := by
    simpa [mul_comm] using!
      VectorFourier.integral_bilin_fourierIntegral_eq_flip
        (ContinuousLinearMap.mul ℂ ℂ) (L := -innerₗ ℝ)
        Real.continuous_fourierChar (by simpa using continuous_inner.neg)
        hS (show Integrable (u : ℝ → ℂ) volume from u.integrable)
  have hd : (∫ x, u x * K x) = ∫ ξ, (𝓕⁻ u) ξ * (𝓕 K) ξ := by
    simpa using!
      VectorFourier.integral_bilin_fourierIntegral_eq_flip
        (ContinuousLinearMap.mul ℂ ℂ) (L := innerₗ ℝ)
        Real.continuous_fourierChar continuous_inner
        (show Integrable (𝓕⁻ u : ℝ → ℂ) volume from (𝓕⁻ u).integrable) hK
  change (∫ x, u x * (𝓕⁻ S) x) = ∫ x, u x * K x
  rw [hi, hd]
  apply integral_congr_ae
  filter_upwards [neutralActualZetaGreenCorrelation_fourier_spectrum_ae a ha v w] with ξ hξ
  exact congrArg (fun z : ℂ => (𝓕⁻ u) ξ * z) hξ.symm

/-- The C² inverse integral is the same compact correlation almost everywhere,
proved by inverse duality and compact smooth test uniqueness. -/
theorem neutralActualZetaGreenCorrelationInverse_ae
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenCorrelationInverse a v w =ᵐ[volume]
      neutralWindowCorrelation a
        (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w) := by
  apply ae_eq_of_integral_contDiff_smul_eq
    (neutralActualZetaGreenCorrelationInverse_contDiff a ha v w).continuous.locallyIntegrable
    (neutralWindowCorrelation_integrable a _ _).locallyIntegrable
  intro g hg hgc
  let gc : ℝ → ℂ := Complex.ofRealCLM ∘ g
  have hc : HasCompactSupport gc := hgc.comp_left rfl
  have hd : ContDiff ℝ ∞ gc := Complex.ofRealCLM.contDiff.comp hg
  let u : SchwartzMap ℝ ℂ := hc.toSchwartzMap hd
  have h := inverse_correlation_pairing a ha v w u
  change (∫ x, (g x : ℂ) * neutralActualZetaGreenCorrelationInverse a v w x) =
    ∫ x, (g x : ℂ) * neutralWindowCorrelation a
      (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w) x at h
  simpa only [Complex.real_smul] using h

/-- Continuity turns almost-everywhere exterior vanishing into pointwise support. -/
theorem neutralActualZetaGreenCorrelationInverse_supported
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) (t : ℝ)
    (ht : t ∉ Set.Icc (-(2 * a)) (2 * a)) :
    neutralActualZetaGreenCorrelationInverse a v w t = 0 := by
  have hz : neutralActualZetaGreenCorrelationInverse a v w =ᵐ[
      volume.restrict (Set.Icc (-(2 * a)) (2 * a))ᶜ] (fun _ => (0 : ℂ)) := by
    rw [ae_restrict_iff' measurableSet_Icc.compl]
    filter_upwards [neutralActualZetaGreenCorrelationInverse_ae a ha v w] with x hx
    intro hout
    rw [hx]
    exact neutralWindowCorrelation_supported a _ _ x hout
  exact eqOn_open_of_ae_eq hz isClosed_Icc.isOpen_compl
    (neutralActualZetaGreenCorrelationInverse_contDiff a ha v w).continuous.continuousOn
    continuous_const.continuousOn ht

/-- The proved C² inverse representative has the exact doubled compact window. -/
theorem neutralActualZetaGreenCorrelationInverse_hasCompactSupport
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    HasCompactSupport (neutralActualZetaGreenCorrelationInverse a v w) :=
  HasCompactSupport.intro isCompact_Icc
    (neutralActualZetaGreenCorrelationInverse_supported a ha v w)

/-- Same-kernel almost-everywhere equality also gives full-line integrability. -/
theorem neutralActualZetaGreenCorrelationInverse_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (neutralActualZetaGreenCorrelationInverse a v w) :=
  (neutralWindowCorrelation_integrable a _ _).congr
    (neutralActualZetaGreenCorrelationInverse_ae a ha v w).symm

/-- Every complex raw-transform sample transfers through the proved identity. -/
theorem neutralActualZetaGreenCorrelationInverse_rawTransform
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) (z : ℂ) :
    neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w) z =
      neutralRawTransform (neutralWindowCorrelation a
        (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w)) z := by
  unfold neutralRawTransform
  apply integral_congr_ae
  filter_upwards [neutralActualZetaGreenCorrelationInverse_ae a ha v w] with x hx
  rw [hx]

/-- Absolute convergence on the actual full divisor survives the C² representative. -/
theorem neutralActualZetaGreenCorrelationInverse_samples_summable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w)
        (neutralActualZetaDivisorOrdinate q)) := by
  simpa only [neutralActualZetaGreenCorrelationInverse_rawTransform a ha v w] using
    neutralActualZetaGreenCorrelation_samples_summable a ha v w

/-- The C² compact representative retains the exact partner zero-side form. -/
theorem neutralActualZetaGreenCorrelationInverse_zeroForm
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w)
        (neutralActualZetaDivisorOrdinate q)) = neutralActualZetaGreenZeroForm a v w := by
  simp_rw [neutralActualZetaGreenCorrelationInverse_rawTransform a ha v w]
  exact neutralActualZetaGreenCorrelation_zeroForm a v w

/-- Both pole terms retain the existing operator on the same canonical Green image. -/
theorem neutralActualZetaGreenCorrelationInverse_poleOperator
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w)
      (Complex.I * ((1/2 : ℝ) : ℂ)) +
      neutralRawTransform (neutralActualZetaGreenCorrelationInverse a v w)
        (Complex.I * ((-(1/2) : ℝ) : ℂ)) =
      inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
        (neutralLogPoleOperator a
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) := by
  simpa only [neutralActualZetaGreenCorrelationInverse_rawTransform a ha v w] using
    neutralActualZetaGreenCorrelation_poleOperator a ha v w

end
end WeilDefect
