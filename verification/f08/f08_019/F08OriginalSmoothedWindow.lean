import WeilDefect.Generated.F08.ExplicitShrinkingPhysicalMollifier
import WeilDefect.Generated.F08.OriginalWindowMollifierFourier
import WeilDefect.Generated.F08.OriginalWindowConvolutionSupport
import Mathlib.Analysis.Calculus.ContDiff.Convolution
import Mathlib.MeasureTheory.Function.LpSpace.Indicator

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped FourierTransform Convolution Topology

/-!
F08-019. Genuine regularization of the L2 physical compact-window
representative from the original signed zeta source by the constructed
positive normalized complex smooth physical mollifier.

The original source operator uses the complex bilinear
ContinuousLinearMap.mul ℂ ℂ. The real differentiability theorem for
convolution requires the REAL bilinear realization of the identical
complex multiplication. We prove the two convolutions pointwise equal.

The physical output is smooth, L1, compactly supported, L2 and has
the original -2π Fourier product. This is not yet the fixed-radius
inner-window form-core density and does not imply Weil positivity.
-/

/-- The same original physical complex convolution integrand is obtained
when multiplication is viewed as a real rather than complex bilinear map.
This is an identity of actual physical functions, not an abstract bridge. -/
theorem f08_019_original_window_complex_real_convolution
    (a : ℝ) (f : RealComplexL2) (rho : ℝ → ℂ) :
    (neutralWindowRepresentative a f
      ⋆[ContinuousLinearMap.mul ℂ ℂ] rho) =
    (neutralWindowRepresentative a f
      ⋆[ContinuousLinearMap.mul ℝ ℂ] rho) := by
  funext x
  simp only [MeasureTheory.convolution_def]
  rfl

/-- The smoothed version of the *literal original* physical window,
using the genuine actual F08-011 complex-valued normalized smooth bump. -/
def f08_019_originalSmoothedWindow
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) : ℝ → ℂ :=
  neutralWindowRepresentative a f
    ⋆[ContinuousLinearMap.mul ℂ ℂ] f08_011_complexMollifier φ

/-- This is genuinely L1, by source-window L1 and normalized bump L1. -/
theorem f08_019_original_smoothed_window_integrable
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    Integrable (f08_019_originalSmoothedWindow a f φ) volume := by
  change Integrable
    (neutralWindowRepresentative a f
      ⋆[ContinuousLinearMap.mul ℂ ℂ] f08_011_complexMollifier φ) volume
  exact (f08_007_original_window_representative_integrable a f).integrable_convolution
    (ContinuousLinearMap.mul ℂ ℂ)
    (f08_011_complexMollifier_integrable φ)

/-- True C-infinity regularity of convolution of the non-smooth original
L2 sharp-window representative with the genuine smooth compact physical
bump. The input window is NOT assumed smooth. -/
theorem f08_019_original_smoothed_window_smooth
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    ContDiff ℝ (↑(⊤ : ℕ∞))
      (f08_019_originalSmoothedWindow a f φ) := by
  have hs :
      ContDiff ℝ (↑(⊤ : ℕ∞))
        (neutralWindowRepresentative a f
          ⋆[ContinuousLinearMap.mul ℝ ℂ]
            f08_011_complexMollifier φ) :=
    (f08_011_complexMollifier_hasCompactSupport φ).contDiff_convolution_right
      (ContinuousLinearMap.mul ℝ ℂ)
      (f08_007_original_window_representative_integrable a f).locallyIntegrable
      (f08_011_complexMollifier_smooth φ)
  simpa only [f08_019_originalSmoothedWindow,
    f08_019_original_window_complex_real_convolution] using hs

/-- The source-physical window grows only by the actual support radius,
not an assumed abstract epsilon multiplier width. -/
theorem f08_019_original_smoothed_window_support_radius
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    Function.support (f08_019_originalSmoothedWindow a f φ) ⊆
      Set.Icc (-(a + φ.rOut)) (a + φ.rOut) := by
  exact f08_009_original_window_convolution_support_radius
    a φ.rOut f (f08_011_complexMollifier φ)
    (f08_011_complexMollifier_support φ)

/-- Compact support of the actually smoothed original physical window. -/
theorem f08_019_original_smoothed_window_hasCompactSupport
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    HasCompactSupport (f08_019_originalSmoothedWindow a f φ) := by
  apply HasCompactSupport.intro
    (K := Set.Icc (-(a + φ.rOut)) (a + φ.rOut)) isCompact_Icc
  intro x hx
  have hn : x ∉ Function.support
      (f08_019_originalSmoothedWindow a f φ) := by
    intro h
    exact hx (f08_019_original_smoothed_window_support_radius a f φ h)
  exact Function.notMem_support.mp hn

/-- This genuinely smooth compact physical function also represents a
square-integrable complex source-window function. -/
theorem f08_019_original_smoothed_window_memLp_two
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    MemLp (f08_019_originalSmoothedWindow a f φ) 2 volume := by
  exact (f08_019_original_smoothed_window_smooth a f φ).continuous
    |>.memLp_of_hasCompactSupport
      (f08_019_original_smoothed_window_hasCompactSupport a f φ)

/-- Exact -2π ordinary Fourier factorization in the ORIGINAL source:
the compact-window complex Fourier sample times the actual physical
normalized smooth mollifier's Fourier multiplier. -/
theorem f08_019_original_smoothed_window_fourier
    (a : ℝ) (f : RealComplexL2)
    (φ : ContDiffBump (0 : ℝ)) (ξ : ℝ) :
    (𝓕 (f08_019_originalSmoothedWindow a f φ)) ξ =
      neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) f *
      f08_015_originalMollifierMultiplier φ ξ := by
  exact f08_007_original_window_convolution_fourier a f
    (f08_011_complexMollifier φ)
    (f08_011_complexMollifier_integrable φ) ξ

/-- Actual selected shrinking bump family gives eventual support control
in any *expanded* physical window [-a-epsilon, a+epsilon].
An inward dilation is still necessary for strict fixed support. -/
theorem f08_019_original_smoothed_window_eventual_support
    (a : ℝ) (f : RealComplexL2) (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop,
      Function.support
        (f08_019_originalSmoothedWindow a f (f08_017_shrinkingBump n)) ⊆
      Set.Icc (-(a + ε)) (a + ε) := by
  have hevent :
      ∀ᶠ n : ℕ in atTop,
        (f08_017_shrinkingBump n).rOut < ε :=
    f08_017_shrinkingBump_radius_tendsto_zero.eventually
      (eventually_lt_nhds hε)
  filter_upwards [hevent] with n hn
  intro x hx
  obtain ⟨hl, hu⟩ :=
    f08_019_original_smoothed_window_support_radius a f
      (f08_017_shrinkingBump n) hx
  exact ⟨by linarith, by linarith⟩

#print axioms f08_019_original_window_complex_real_convolution
#print axioms f08_019_original_smoothed_window_integrable
#print axioms f08_019_original_smoothed_window_smooth
#print axioms f08_019_original_smoothed_window_support_radius
#print axioms f08_019_original_smoothed_window_hasCompactSupport
#print axioms f08_019_original_smoothed_window_memLp_two
#print axioms f08_019_original_smoothed_window_fourier
#print axioms f08_019_original_smoothed_window_eventual_support

end
end WeilDefect
