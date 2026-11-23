import WeilDefect.Generated.F08.OriginalSmoothedWindow

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped FourierTransform Convolution Topology

/-!
F08-021: The genuinely C-infinity, compact, L1 and L2 ORIGINAL signed-Weil
physical window convolution of F08-019 is now installed as an actual element
of the source RealComplexL2 class, not a pointwise impostor.

The canonical MemLp.toLp representative agrees a.e. with that same
physical convolution, and its native L2 Fourier coordinate is a.e. equal
to the precise ordinary negative-2π original-source Fourier product.

This does NOT show the mollified spectral element has finite logarithmic
energy for arbitrary original L2 window, nor inward dilation/core density,
nor unrestricted original signed Weil positivity.
-/

/-- The actual source native L² class of the true smooth compact physical
convolution. This is not an alternative formal function space. -/
def f08_021_originalSmoothedWindowL2
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    RealComplexL2 :=
  (f08_019_original_smoothed_window_memLp_two a f φ).toLp
    (f08_019_originalSmoothedWindow a f φ)

/-- The actual native L² class has precisely the physical C-infinity
source-window convolution as its representative, almost everywhere. -/
theorem f08_021_original_smoothed_window_native_ae
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    (f08_021_originalSmoothedWindowL2 a f φ : ℝ → ℂ) =ᵐ[volume]
      f08_019_originalSmoothedWindow a f φ := by
  exact (f08_019_original_smoothed_window_memLp_two a f φ).coeFn_toLp

/-- The native L² representative is also genuinely L¹, because its actual
source physical representative is the previously proven L¹ convolution. -/
theorem f08_021_original_smoothed_window_native_integrable
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    Integrable (f08_021_originalSmoothedWindowL2 a f φ : ℝ → ℂ) volume := by
  exact (f08_019_original_smoothed_window_integrable a f φ).congr
    (f08_021_original_smoothed_window_native_ae a f φ)

/-- The actual native complex L² representative has the original physical
support radius almost everywhere, without asserting the arbitrary canonical
Lp representative itself is pointwise smooth. -/
theorem f08_021_original_smoothed_window_native_ae_support
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    ∀ᵐ x : ℝ ∂volume,
      x ∉ Set.Icc (-(a + φ.rOut)) (a + φ.rOut) →
        f08_021_originalSmoothedWindowL2 a f φ x = 0 := by
  filter_upwards [f08_021_original_smoothed_window_native_ae a f φ] with x hx hnot
  rw [hx]
  have houtside :
      x ∉ Function.support (f08_019_originalSmoothedWindow a f φ) := by
    intro hs
    exact hnot (f08_019_original_smoothed_window_support_radius a f φ hs)
  exact Function.notMem_support.mp houtside

/-- This is the needed native-Plancherel coordinate bridge: the actual
original smooth physical convolution has the same L² Fourier coordinate
as its own ordinary L¹ Fourier transform, almost everywhere. -/
theorem f08_021_original_smoothed_window_native_fourier_ae
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    (𝓕 (f08_021_originalSmoothedWindowL2 a f φ) : RealComplexL2) =ᵐ[volume]
      (𝓕 (f08_019_originalSmoothedWindow a f φ : ℝ → ℂ)) := by
  have hnative :=
    neutralIntegrableL2_fourier_ae
      (f08_021_originalSmoothedWindowL2 a f φ)
      (f08_021_original_smoothed_window_native_integrable a f φ)
  have hraw (ξ : ℝ) :
      (𝓕 (f08_021_originalSmoothedWindowL2 a f φ : ℝ → ℂ)) ξ =
      (𝓕 (f08_019_originalSmoothedWindow a f φ : ℝ → ℂ)) ξ :=
    Real.fourier_congr_ae
      (f08_021_original_smoothed_window_native_ae a f φ) ξ
  filter_upwards [hnative] with ξ hξ
  exact hξ.trans (hraw ξ)

/-- The exact original signed-Weil ordinary -2π Fourier sample is now
attached to the native RealComplexL2 Fourier transform of the actual smooth
compact source physical window, not merely to a hypothetical multiplier. -/
theorem f08_021_original_smoothed_window_native_fourier_product_ae
    (a : ℝ) (f : RealComplexL2) (φ : ContDiffBump (0 : ℝ)) :
    (𝓕 (f08_021_originalSmoothedWindowL2 a f φ) : RealComplexL2) =ᵐ[volume]
      (fun ξ : ℝ =>
        neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) f *
        f08_015_originalMollifierMultiplier φ ξ) := by
  filter_upwards [f08_021_original_smoothed_window_native_fourier_ae a f φ]
    with ξ hξ
  exact hξ.trans (f08_019_original_smoothed_window_fourier a f φ ξ)

/-- This is an identity for the explicitly certified shrinking bump
sequence, with no arbitrary unconstructed sequence and no extra
assumption on f's L² norm. -/
theorem f08_021_explicit_original_smoothed_window_native_fourier_ae
    (a : ℝ) (f : RealComplexL2) (n : ℕ) :
    (𝓕 (f08_021_originalSmoothedWindowL2 a f
      (f08_017_shrinkingBump n)) : RealComplexL2) =ᵐ[volume]
      (fun ξ : ℝ =>
        neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) f *
        f08_015_originalMollifierMultiplier
          (f08_017_shrinkingBump n) ξ) :=
  f08_021_original_smoothed_window_native_fourier_product_ae
    a f (f08_017_shrinkingBump n)

#print axioms f08_021_original_smoothed_window_native_ae
#print axioms f08_021_original_smoothed_window_native_integrable
#print axioms f08_021_original_smoothed_window_native_ae_support
#print axioms f08_021_original_smoothed_window_native_fourier_ae
#print axioms f08_021_original_smoothed_window_native_fourier_product_ae
#print axioms f08_021_explicit_original_smoothed_window_native_fourier_ae

end
end WeilDefect
