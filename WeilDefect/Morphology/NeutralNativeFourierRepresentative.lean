import WeilDefect.Morphology.NeutralNativeFourierDerivative
import Mathlib.Analysis.Distribution.AEEqOfIntegralContDiff

namespace WeilDefect

noncomputable section

attribute [local instance 1100] NormedSpace.complexToReal

open MeasureTheory FourierTransform
open scoped SchwartzMap FourierTransform Real

/-- The actual first-derivative frequency product of the native physical
Green vector. This is not the full Weil spectral product. -/
def neutralNativeFourierDerivativeProduct
    {count : ℕ → ℕ} (a : ℝ) (data : ActualProblemOneShellData count)
    (v : NeutralNativeShellCoefficients count) (ξ : ℝ) : ℂ :=
  (2 * Real.pi * Complex.I) * (ξ : ℂ) *
    (𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2) ξ

/-- The product has a lawful locally integrable representative before its
global L2 membership is proved. -/
theorem neutralNativeFourierDerivativeProduct_locallyIntegrable
    {count : ℕ → ℕ} (a : ℝ) (data : ActualProblemOneShellData count)
    (v : NeutralNativeShellCoefficients count) :
    LocallyIntegrable (neutralNativeFourierDerivativeProduct a data v) volume := by
  have hc : Continuous (fun ξ : ℝ => (2 * Real.pi * Complex.I) * (ξ : ℂ)) := by
    fun_prop
  exact ((Lp.memLp (𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2)).
    locallyIntegrable (by norm_num)).continuous_mul hc

/-- The certified actual distribution identity gives the concrete Schwartz
pairing of the derivative frequency product. -/
theorem neutralNativeFourierDerivativeProduct_pairing
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) (u : SchwartzMap ℝ ℂ) :
    (∫ ξ, u ξ * (𝓕 (neutralNativeGradientSynthesis a data v) : RealComplexL2) ξ) =
      ∫ ξ, u ξ * neutralNativeFourierDerivativeProduct a data v ξ := by
  have ht : (fun ξ : ℝ => (ξ : ℂ)).HasTemperateGrowth := by fun_prop
  have h := congrArg (fun T : TemperedDistribution ℝ ℂ => T u)
    (neutralNativeGreenSynthesis_fourierDerivative a ha data C hCount v)
  change Lp.toTemperedDistribution
      (𝓕 (neutralNativeGradientSynthesis a data v) : RealComplexL2) u =
    (2 * Real.pi * Complex.I) *
      (TemperedDistribution.smulLeftCLM ℂ (fun ξ : ℝ => (ξ : ℂ))
        (Lp.toTemperedDistribution
          (𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2)) u) at h
  rw [Lp.toTemperedDistribution_apply,
    TemperedDistribution.smulLeftCLM_apply_apply, Lp.toTemperedDistribution_apply] at h
  simp only [SchwartzMap.smulLeftCLM_apply_apply ht, smul_eq_mul] at h
  rw [h, ← integral_const_mul]
  apply integral_congr_ae
  filter_upwards [] with ξ
  unfold neutralNativeFourierDerivativeProduct
  ring

/-- Uniqueness of locally integrable compact-smooth test pairings identifies
the actual frequency product almost everywhere with the constructed L2
Fourier derivative. No spectral membership premise is imported. -/
theorem neutralNativeFourierDerivativeProduct_ae
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    (𝓕 (neutralNativeGradientSynthesis a data v) : RealComplexL2) =ᵐ[volume]
      neutralNativeFourierDerivativeProduct a data v := by
  apply ae_eq_of_integral_contDiff_smul_eq
    ((Lp.memLp (𝓕 (neutralNativeGradientSynthesis a data v) : RealComplexL2)).
      locallyIntegrable (by norm_num))
    (neutralNativeFourierDerivativeProduct_locallyIntegrable a data v)
  intro g hg hgc
  let gc : ℝ → ℂ := Complex.ofRealCLM ∘ g
  have hc : HasCompactSupport gc := hgc.comp_left rfl
  have hd : ContDiff ℝ ∞ gc := Complex.ofRealCLM.contDiff.comp hg
  let u : SchwartzMap ℝ ℂ := hc.toSchwartzMap hd
  have h := neutralNativeFourierDerivativeProduct_pairing a ha data C hCount v u
  change (∫ ξ, (g ξ : ℂ) *
      (𝓕 (neutralNativeGradientSynthesis a data v) : RealComplexL2) ξ) =
    ∫ ξ, (g ξ : ℂ) * neutralNativeFourierDerivativeProduct a data v ξ at h
  simpa only [Complex.real_smul] using h

/-- Genuine L2 membership of the native first-derivative frequency product,
derived from the retained shell inputs and the constructed derivative.
It does not assert Weil spectral membership for the current WD-T38 carrier. -/
theorem neutralNativeFourierDerivativeProduct_memLp
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    MemLp (neutralNativeFourierDerivativeProduct a data v) 2 volume :=
  (Lp.memLp (𝓕 (neutralNativeGradientSynthesis a data v) : RealComplexL2)).congr
    (neutralNativeFourierDerivativeProduct_ae a ha data C hCount v)

end

end WeilDefect
