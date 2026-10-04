import WeilDefect.Arithmetic.ActualZetaCorrelationRegularity

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate SchwartzMap
set_option maxHeartbeats 800000

private theorem ordinary_fourier_continuous (f : RealComplexL2) (hf : Integrable f) :
    Continuous (𝓕 (f : ℝ → ℂ)) := by
  exact VectorFourier.fourierIntegral_continuous
    (L := innerₗ ℝ) Real.continuous_fourierChar continuous_inner hf

private theorem integrableL2_fourier_pairing (f : RealComplexL2) (hf : Integrable f)
    (u : SchwartzMap ℝ ℂ) :
    (∫ ξ, u ξ * (𝓕 f : RealComplexL2) ξ) =
      ∫ ξ, u ξ * (𝓕 (f : ℝ → ℂ)) ξ := by
  have h := congrArg (fun T : TemperedDistribution ℝ ℂ => T u)
    (Lp.fourier_toTemperedDistribution_eq f)
  rw [TemperedDistribution.fourier_apply, Lp.toTemperedDistribution_apply,
    Lp.toTemperedDistribution_apply] at h
  simp only [smul_eq_mul] at h
  rw [← h]
  simpa only [ContinuousLinearMap.mul_apply'] using
    VectorFourier.integral_bilin_fourierIntegral_eq_flip
      (ContinuousLinearMap.mul ℂ ℂ) (L := innerₗ ℝ)
      Real.continuous_fourierChar continuous_inner u.integrable hf

/-- The ordinary L¹ Fourier integral and the existing L² Fourier coordinate
agree almost everywhere, proved by compact smooth test uniqueness. -/
theorem neutralIntegrableL2_fourier_ae (f : RealComplexL2) (hf : Integrable f) :
    (𝓕 f : RealComplexL2) =ᵐ[volume] (𝓕 (f : ℝ → ℂ)) := by
  apply ae_eq_of_integral_contDiff_smul_eq
    ((Lp.memLp (𝓕 f : RealComplexL2)).locallyIntegrable (by norm_num))
    (ordinary_fourier_continuous f hf).locallyIntegrable
  intro g hg hgc
  let gc : ℝ → ℂ := Complex.ofRealCLM ∘ g
  have hc : HasCompactSupport gc := hgc.comp_left rfl
  have hd : ContDiff ℝ ∞ gc := Complex.ofRealCLM.contDiff.comp hg
  let u : SchwartzMap ℝ ℂ := hc.toSchwartzMap hd
  have h := integrableL2_fourier_pairing f hf u
  change (∫ ξ, (g ξ : ℂ) * (𝓕 f : RealComplexL2) ξ) =
    ∫ ξ, (g ξ : ℂ) * (𝓕 (f : ℝ → ℂ)) ξ at h
  simpa only [Complex.real_smul] using h

/-- Actual compact support makes the constructed Green synthesis globally L¹. -/
theorem neutralActualZetaGreenSynthesis_integrable
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    Integrable (neutralActualZetaGreenSynthesis a v : ℝ → ℂ) := by
  have hi : Integrable (neutralWindowRepresentative a
      (neutralActualZetaGreenSynthesis a v)) := by
    simpa using neutralWindowRepresentative_twist_integrable a
      (neutralActualZetaGreenSynthesis a v) 0
  exact hi.congr (neutralActualZetaGreenSynthesis_windowRepresentative_ae a ha v)

/-- Derived L¹/L² agreement for the exact constructed actual-divisor Green vector. -/
theorem neutralActualZetaGreenSynthesis_fourier_ae
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) =ᵐ[volume]
      (𝓕 (neutralActualZetaGreenSynthesis a v : ℝ → ℂ)) :=
  neutralIntegrableL2_fourier_ae _
    (neutralActualZetaGreenSynthesis_integrable a ha v)

/-- Exact conversion from Mathlib's negative-exponent 2π transform to the
project's positive-exponent raw transform. No integrability premise is needed. -/
theorem neutralRawTransform_fourier (k : ℝ → ℂ) (ξ : ℝ) :
    (𝓕 k) ξ = neutralRawTransform k ((-2 * Real.pi * ξ : ℝ) : ℂ) := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  unfold neutralRawTransform
  apply integral_congr_ae
  filter_upwards [] with x
  simp only [smul_eq_mul]
  have he : ((-2 * Real.pi * x * ξ : ℝ) : ℂ) * Complex.I =
      Complex.I * ((-2 * Real.pi * ξ : ℝ) : ℂ) * (x : ℂ) := by
    push_cast
    ring
  rw [he]
  exact mul_comm _ _

/-- Exact window Fourier dictionary, retaining the same indicator representative. -/
theorem neutralWindowRepresentative_fourier (a : ℝ) (f : RealComplexL2) (ξ : ℝ) :
    (𝓕 (neutralWindowRepresentative a f)) ξ =
      neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) f := by
  rw [neutralRawTransform_fourier]
  unfold neutralRawTransform neutralWindowEvaluation
  rw [← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;> simp [neutralWindowRepresentative, hx]

/-- The supported actual Green vector has the same pointwise ordinary Fourier
integral as its compact-window raw samples, with exact normalization. -/
theorem neutralActualZetaGreenSynthesis_fourier_window
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) (ξ : ℝ) :
    (𝓕 (neutralActualZetaGreenSynthesis a v : ℝ → ℂ)) ξ =
      neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ)
        (neutralActualZetaGreenSynthesis a v) := by
  calc
    _ = (𝓕 (neutralWindowRepresentative a (neutralActualZetaGreenSynthesis a v))) ξ :=
      Real.fourier_congr_ae
        (neutralActualZetaGreenSynthesis_windowRepresentative_ae a ha v).symm ξ
    _ = _ := neutralWindowRepresentative_fourier a _ ξ

/-- The exact compact mixed correlation's ordinary Fourier transform agrees
almost everywhere with the concrete spectrum used by the C² inverse integral. -/
theorem neutralActualZetaGreenCorrelation_fourier_spectrum_ae
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    (𝓕 (neutralWindowCorrelation a
      (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w))) =ᵐ[volume]
      neutralActualZetaGreenCorrelationSpectrum a v w := by
  filter_upwards [neutralActualZetaGreenSynthesis_fourier_ae a ha v,
    neutralActualZetaGreenSynthesis_fourier_ae a ha w] with ξ hv hw
  rw [neutralRawTransform_fourier, neutralWindowCorrelation_rawTransform]
  simp only [Complex.conj_ofReal]
  unfold neutralActualZetaGreenCorrelationSpectrum
  rw [hv, hw, neutralActualZetaGreenSynthesis_fourier_window a ha v,
    neutralActualZetaGreenSynthesis_fourier_window a ha w]

/-- The ordinary Fourier transform of the same compact correlation is L¹,
derived from the spectrum attachment rather than assumed for inversion. -/
theorem neutralActualZetaGreenCorrelation_fourier_integrable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Integrable (𝓕 (neutralWindowCorrelation a
      (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w))) :=
  (neutralActualZetaGreenCorrelationSpectrum_integrable a v w).congr
    (neutralActualZetaGreenCorrelation_fourier_spectrum_ae a ha v w).symm

end
end WeilDefect
