import WeilDefect.Morphology.NeutralNativeSupport
import WeilDefect.Morphology.NeutralGaussianDualityAudit
import Mathlib.Analysis.Fourier.LpSpace

namespace WeilDefect

noncomputable section

attribute [local instance 1100] NormedSpace.complexToReal

open MeasureTheory FourierTransform
open scoped BigOperators SchwartzMap ComplexConjugate FourierTransform LineDeriv Real

/-- Convert the actual Hermitian L2 pairing to the bilinear distribution
test pairing, by the already constructed Schwartz conjugation. -/
theorem neutralNative_conjugateTest_inner (u : SchwartzMap ℝ ℂ) (f : RealComplexL2) :
    inner ℂ ((conjugateSchwartz u).toLp 2 volume) f = ∫ x, u x * f x := by
  rw [L2.inner_def]
  apply integral_congr_ae
  filter_upwards [(conjugateSchwartz u).coeFn_toLp 2 volume] with x hx
  rw [hx]
  simp [conjugateSchwartz_apply, RCLike.inner_apply', mul_comm]

/-- Conjugation commutes with the actual Schwartz derivative. -/
theorem neutralNative_derivative_conjugateTest (u : SchwartzMap ℝ ℂ) :
    SchwartzMap.derivCLM ℂ ℂ (conjugateSchwartz u) =
      conjugateSchwartz (SchwartzMap.derivCLM ℂ ℂ u) := by
  ext x
  simp only [SchwartzMap.derivCLM_apply, conjugateSchwartz_apply]
  have hc : (conjugateSchwartz u : ℝ → ℂ) = (fun y => star (u y)) := by
    funext y
    simp [conjugateSchwartz_apply, starRingEnd_apply]
  rw [hc]
  simpa only [starRingEnd_apply] using (u.hasDerivAt x).star.deriv

/-- The constructed native L2 weak derivative is the derivative of its
actual tempered distribution. No derivative representative is assumed. -/
theorem neutralNativeGreenSynthesis_temperedDerivative
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    TemperedDistribution.derivCLM ℂ
        (Lp.toTemperedDistribution (neutralNativeGreenSynthesis a data v)) =
      Lp.toTemperedDistribution (neutralNativeGradientSynthesis a data v) := by
  ext u
  rw [TemperedDistribution.derivCLM_apply_apply,
    Lp.toTemperedDistribution_apply, Lp.toTemperedDistribution_apply]
  simp only [SchwartzMap.neg_apply, smul_eq_mul, neg_mul, integral_neg]
  have h := neutralNativeGreenSynthesis_weakDerivative a ha data C hCount v
    (conjugateSchwartz u)
  rw [neutralNative_derivative_conjugateTest,
    neutralNative_conjugateTest_inner, neutralNative_conjugateTest_inner] at h
  simp only [SchwartzMap.derivCLM_apply] at h ⊢
  linear_combination -h

private theorem nativeLineDerivative_one (f : TemperedDistribution ℝ ℂ) :
    ∂_{(1 : ℝ)} f = TemperedDistribution.derivCLM ℂ f := by
  ext u
  rw [TemperedDistribution.lineDerivOp_apply_apply,
    TemperedDistribution.derivCLM_apply_apply]
  congr 1

/-- Actual native Fourier derivative bridge. The frequency multiplier of
the Green synthesis is represented, as a distribution, by the actual L2
Fourier transform of the already constructed derivative synthesis.
Pointwise frequency-product L2 membership remains a separate conclusion. -/
theorem neutralNativeGreenSynthesis_fourierDerivative
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    Lp.toTemperedDistribution
        (𝓕 (neutralNativeGradientSynthesis a data v) : RealComplexL2) =
      (2 * Real.pi * Complex.I) •
        TemperedDistribution.smulLeftCLM ℂ (fun ξ : ℝ => (ξ : ℂ))
          (Lp.toTemperedDistribution
            (𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2)) := by
  have h := TemperedDistribution.fourier_lineDerivOp_eq
    (Lp.toTemperedDistribution (neutralNativeGreenSynthesis a data v)) (1 : ℝ)
  rw [nativeLineDerivative_one, neutralNativeGreenSynthesis_temperedDerivative a ha data C hCount,
    Lp.fourier_toTemperedDistribution_eq, Lp.fourier_toTemperedDistribution_eq] at h
  have hi : (fun ξ : ℝ => ((inner ℝ ξ (1 : ℝ) : ℝ) : ℂ)) =
      (fun ξ : ℝ => (ξ : ℂ)) := by
    ext ξ
    simp [RCLike.inner_apply]
  simpa only [hi] using h

end

end WeilDefect
