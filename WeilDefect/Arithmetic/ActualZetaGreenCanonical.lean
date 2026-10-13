import WeilDefect.Arithmetic.ActualZetaGreenEnergy
import WeilDefect.Morphology.NeutralNativeLogFormAttachment

namespace WeilDefect
noncomputable section
attribute [local instance 1100] NormedSpace.complexToReal
open MeasureTheory FourierTransform InnerProductSpace
open scoped BigOperators SchwartzMap ComplexConjugate FourierTransform LineDeriv Real ContDiff
set_option maxHeartbeats 800000

/-- The actual derivative synthesis is the global weak derivative of the
actual Green synthesis. Both vectors were already constructed in L2.
This identifies native regularity, not the independently supplied WD-T38 mode. -/
theorem neutralActualZetaGreenSynthesis_weakDerivative
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) (u : SchwartzMap ℝ ℂ) :
    inner ℂ ((SchwartzMap.derivCLM ℂ ℂ u).toLp 2 volume)
        (neutralActualZetaGreenSynthesis a v) =
      -inner ℂ (u.toLp 2 volume) (neutralActualZetaGradientSynthesis a v) := by
  rw [neutralActualZetaGreenSynthesis_inner a ha,
    neutralActualZetaGradientSynthesis_inner a ha, ← tsum_neg]
  apply tsum_congr
  intro g
  change v g * inner ℂ ((SchwartzMap.derivCLM ℂ ℂ u).toLp 2 volume)
      (neutralDirichletGreenColumnL2 a (neutralActualZetaDivisorOrdinate g)) = _
  rw [neutralNativeGreenColumn_weakDerivative a ha (neutralActualZetaDivisorOrdinate g) u, mul_neg]
  rfl

/-- Compact support survives the actual L2 Green synthesis, by continuity
of the existing physical outside-restriction map. -/
theorem neutralActualZetaGreenSynthesis_supported
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a →
      neutralActualZetaGreenSynthesis a v x = 0 := by
  apply (neutralOutsideRestriction_zero_iff a _).mp
  have h := (neutralActualZetaGreenSynthesis_hasSum a ha v).mapL
    (neutralOutsideRestriction a)
  have hz (g : NeutralActualZetaDivisorCoordinate) :
      neutralOutsideRestriction a
        (v g • neutralDirichletGreenColumnL2 a (neutralActualZetaDivisorOrdinate g)) = 0 := by
    rw [map_smul]
    have hc := (neutralOutsideRestriction_zero_iff a _).mpr
      (neutralNativeGreenColumn_supported a (neutralActualZetaDivisorOrdinate g))
    rw [hc, smul_zero]
  have ht := h.tsum_eq.symm
  simpa only [neutralActualZetaGreenColumn, hz, tsum_zero] using ht

/-- Compact support survives the actual L2 derivative synthesis. Combined
with its global weak derivative identity, both spatial witnesses are attached. -/
theorem neutralActualZetaGradientSynthesis_supported
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a →
      neutralActualZetaGradientSynthesis a v x = 0 := by
  apply (neutralOutsideRestriction_zero_iff a _).mp
  have h := (neutralActualZetaGradientSynthesis_hasSum a ha v).mapL
    (neutralOutsideRestriction a)
  have hz (g : NeutralActualZetaDivisorCoordinate) :
      neutralOutsideRestriction a
        (v g • neutralDirichletGradientColumnL2 a (neutralActualZetaDivisorOrdinate g)) = 0 := by
    rw [map_smul]
    have hc := (neutralOutsideRestriction_zero_iff a _).mpr
      (neutralNativeGradientColumn_supported a (neutralActualZetaDivisorOrdinate g))
    rw [hc, smul_zero]
  have ht := h.tsum_eq.symm
  simpa only [neutralActualZetaGradientColumn, hz, tsum_zero] using ht

/-- The constructed native L2 weak derivative is the derivative of its
actual tempered distribution. No derivative representative is assumed. -/
theorem neutralActualZetaGreenSynthesis_temperedDerivative
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    TemperedDistribution.derivCLM ℂ
        (Lp.toTemperedDistribution (neutralActualZetaGreenSynthesis a v)) =
      Lp.toTemperedDistribution (neutralActualZetaGradientSynthesis a v) := by
  ext u
  rw [TemperedDistribution.derivCLM_apply_apply,
    Lp.toTemperedDistribution_apply, Lp.toTemperedDistribution_apply]
  simp only [SchwartzMap.neg_apply, smul_eq_mul, neg_mul, integral_neg]
  have h := neutralActualZetaGreenSynthesis_weakDerivative a ha v
    (conjugateSchwartz u)
  rw [neutralNative_derivative_conjugateTest,
    neutralNative_conjugateTest_inner, neutralNative_conjugateTest_inner] at h
  simp only [SchwartzMap.derivCLM_apply] at h ⊢
  linear_combination -h

private theorem actualZetaLineDerivative_one (f : TemperedDistribution ℝ ℂ) :
    ∂_{(1 : ℝ)} f = TemperedDistribution.derivCLM ℂ f := by
  ext u
  rw [TemperedDistribution.lineDerivOp_apply_apply,
    TemperedDistribution.derivCLM_apply_apply]
  congr 1

/-- Actual native Fourier derivative bridge. The frequency multiplier of
the Green synthesis is represented, as a distribution, by the actual L2
Fourier transform of the already constructed derivative synthesis.
Pointwise frequency-product L2 membership remains a separate conclusion. -/
theorem neutralActualZetaGreenSynthesis_fourierDerivative
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    Lp.toTemperedDistribution
        (𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2) =
      (2 * Real.pi * Complex.I) •
        TemperedDistribution.smulLeftCLM ℂ (fun ξ : ℝ => (ξ : ℂ))
          (Lp.toTemperedDistribution
            (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2)) := by
  have h := TemperedDistribution.fourier_lineDerivOp_eq
    (Lp.toTemperedDistribution (neutralActualZetaGreenSynthesis a v)) (1 : ℝ)
  rw [actualZetaLineDerivative_one, neutralActualZetaGreenSynthesis_temperedDerivative a ha,
    Lp.fourier_toTemperedDistribution_eq, Lp.fourier_toTemperedDistribution_eq] at h
  have hi : (fun ξ : ℝ => ((inner ℝ ξ (1 : ℝ) : ℝ) : ℂ)) =
      (fun ξ : ℝ => (ξ : ℂ)) := by
    ext ξ
    simp [RCLike.inner_apply]
  simpa only [hi] using h

/-- The actual first-derivative frequency product of the native physical
Green vector. This is not the full Weil spectral product. -/
def neutralActualZetaFourierDerivativeProduct
    (a : ℝ)
    (v : NeutralActualZetaGreenCoefficients) (ξ : ℝ) : ℂ :=
  (2 * Real.pi * Complex.I) * (ξ : ℂ) *
    (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ

/-- The product has a lawful locally integrable representative before its
global L2 membership is proved. -/
theorem neutralActualZetaFourierDerivativeProduct_locallyIntegrable
    (a : ℝ)
    (v : NeutralActualZetaGreenCoefficients) :
    LocallyIntegrable (neutralActualZetaFourierDerivativeProduct a v) volume := by
  have hc : Continuous (fun ξ : ℝ => (2 * Real.pi * Complex.I) * (ξ : ℂ)) := by
    fun_prop
  exact ((Lp.memLp (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2)).locallyIntegrable (by norm_num)).continuous_mul hc

/-- The certified actual distribution identity gives the concrete Schwartz
pairing of the derivative frequency product. -/
theorem neutralActualZetaFourierDerivativeProduct_pairing
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) (u : SchwartzMap ℝ ℂ) :
    (∫ ξ, u ξ * (𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2) ξ) =
      ∫ ξ, u ξ * neutralActualZetaFourierDerivativeProduct a v ξ := by
  have ht : (fun ξ : ℝ => (ξ : ℂ)).HasTemperateGrowth := by fun_prop
  have h := congrArg (fun T : TemperedDistribution ℝ ℂ => T u)
    (neutralActualZetaGreenSynthesis_fourierDerivative a ha v)
  change Lp.toTemperedDistribution
      (𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2) u =
    (2 * Real.pi * Complex.I) *
      (TemperedDistribution.smulLeftCLM ℂ (fun ξ : ℝ => (ξ : ℂ))
        (Lp.toTemperedDistribution
          (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2)) u) at h
  rw [Lp.toTemperedDistribution_apply,
    TemperedDistribution.smulLeftCLM_apply_apply, Lp.toTemperedDistribution_apply] at h
  simp only [SchwartzMap.smulLeftCLM_apply_apply ht, smul_eq_mul] at h
  rw [h, ← integral_const_mul]
  apply integral_congr_ae
  filter_upwards [] with ξ
  unfold neutralActualZetaFourierDerivativeProduct
  ring

/-- Uniqueness of locally integrable compact-smooth test pairings identifies
the actual frequency product almost everywhere with the constructed L2
Fourier derivative. No spectral membership premise is imported. -/
theorem neutralActualZetaFourierDerivativeProduct_ae
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    (𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2) =ᵐ[volume]
      neutralActualZetaFourierDerivativeProduct a v := by
  apply ae_eq_of_integral_contDiff_smul_eq
    ((Lp.memLp (𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2)).locallyIntegrable (by norm_num))
    (neutralActualZetaFourierDerivativeProduct_locallyIntegrable a v)
  intro g hg hgc
  let gc : ℝ → ℂ := Complex.ofRealCLM ∘ g
  have hc : HasCompactSupport gc := hgc.comp_left rfl
  have hd : ContDiff ℝ ∞ gc := Complex.ofRealCLM.contDiff.comp hg
  let u : SchwartzMap ℝ ℂ := hc.toSchwartzMap hd
  have h := neutralActualZetaFourierDerivativeProduct_pairing a ha v u
  change (∫ ξ, (g ξ : ℂ) *
      (𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2) ξ) =
    ∫ ξ, (g ξ : ℂ) * neutralActualZetaFourierDerivativeProduct a v ξ at h
  simpa only [Complex.real_smul] using h

/-- Genuine L2 membership of the native first-derivative frequency product,
derived from actual divisor growth and the constructed derivative.
It does not assert Weil spectral membership for the current WD-T38 carrier. -/
theorem neutralActualZetaFourierDerivativeProduct_memLp
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    MemLp (neutralActualZetaFourierDerivativeProduct a v) 2 volume :=
  (memLp_congr_ae (neutralActualZetaFourierDerivativeProduct_ae a ha v)).mp
    (Lp.memLp (𝓕 (neutralActualZetaGradientSynthesis a v) : RealComplexL2))

/-- Remove only the nonzero Fourier derivative constant from the proved
native product. This is derived regularity, not an operator-domain premise. -/
theorem neutralActualZetaGreenSynthesis_frequency_memLp
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    MemLp (fun ξ : ℝ => (ξ : ℂ) *
      (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ) 2 volume := by
  have hk : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    exact mul_ne_zero (mul_ne_zero (by norm_num)
      (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero)) Complex.I_ne_zero
  have h := (neutralActualZetaFourierDerivativeProduct_memLp a ha v).const_mul
    (2 * Real.pi * Complex.I : ℂ)⁻¹
  have heq : (fun ξ => (2 * Real.pi * Complex.I : ℂ)⁻¹ *
      neutralActualZetaFourierDerivativeProduct a v ξ) =
      (fun ξ : ℝ => (ξ : ℂ) *
        (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ) := by
    funext ξ
    unfold neutralActualZetaFourierDerivativeProduct
    rw [← mul_assoc, ← mul_assoc, inv_mul_cancel₀ hk, one_mul]
  rw [heq] at h
  exact h

/-- Actual logarithmic energy of the physical native Green synthesis,
derived from its actual derivative and base L2 mass. -/
theorem neutralActualZetaGreenSynthesis_logEnergy
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    Integrable (fun ξ => logarithmicFourierWeight ξ *
      ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) volume := by
  have hF := Lp.memLp (𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2)
  have hp := neutralActualZetaGreenSynthesis_frequency_memLp a ha v
  have hmass := (memLp_two_iff_integrable_sq_norm hF.aestronglyMeasurable).mp hF
  have hprod := (memLp_two_iff_integrable_sq_norm hp.aestronglyMeasurable).mp hp
  apply ((hmass.const_mul (Real.exp 1)).add hprod).mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      (hF.aestronglyMeasurable.norm.pow 2)
  · filter_upwards with ξ
    have hw : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hw (sq_nonneg _))]
    calc
      logarithmicFourierWeight ξ *
          ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2 ≤
        (Real.exp 1 + ξ ^ 2) *
          ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2 :=
        mul_le_mul_of_nonneg_right
          (logarithmicFourierWeight_le_derivativeWeight ξ) (sq_nonneg _)
      _ = _ := by
        simp only [Pi.add_apply, norm_mul, Complex.norm_real, Real.norm_eq_abs, mul_pow, sq_abs]
        ring

/-- The actual native physical vector now inhabits the canonical supported
logarithmic form domain. No source/null identity is asserted by this definition. -/
def neutralActualZetaGreenCanonical
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) : neutralCanonicalLogFormDomain a :=
  ⟨neutralActualZetaGreenSynthesis a v,
    neutralActualZetaGreenSynthesis_supported a ha v,
    neutralActualZetaGreenSynthesis_logEnergy a ha v⟩

/-- Canonical attachment preserves the actual physical synthesis exactly. -/
theorem neutralActualZetaGreenCanonical_val
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    (neutralActualZetaGreenCanonical a ha v).val =
      neutralActualZetaGreenSynthesis a v := rfl

/-- The existing complete logarithmic carrier realizes the same physical
vector; no new completion or conditional representation is introduced. -/
theorem neutralActualZetaGreenCanonical_physical
    (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralLogPhysical
      (neutralCanonicalToLogHilbert
        (neutralActualZetaGreenCanonical a ha v)).val =
      neutralActualZetaGreenSynthesis a v := by
  exact neutralLogPhysical_weighted
    (neutralActualZetaGreenCanonical a ha v)

end
end WeilDefect
