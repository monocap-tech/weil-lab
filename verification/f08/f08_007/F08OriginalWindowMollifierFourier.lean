import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import Mathlib.Analysis.Fourier.Convolution

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform Convolution

/-!
F08-007: literal complex Fourier dictionary for convolution with the ACTUAL
physical compact-window representative used in the original zeta Weil source.

The first input is neutralWindowRepresentative a f, with no unproved
Schwartz smoothness or support-cutoff boundedness. The ordinary Fourier
transform follows Mathlib's negative 2π exponent, and the original
positive-exponent neutralWindowEvaluation is evaluated at -2π ξ.

The mollifier is only assumed integrable here. A separate F08 step must
construct a compact positive unit-mass smooth mollifier, establish its
transform's contraction/limit, the physical support gap, and relate this
ordinary Fourier equality to the weighted L² carrier and original form.
-/

/-- An arbitrary compact-window physical complex-L² representative is
genuinely L¹, without requiring extra smoothness of the representative. -/
theorem f08_007_original_window_representative_integrable
    (a : ℝ) (f : RealComplexL2) :
    Integrable (neutralWindowRepresentative a f) := by
  simpa using neutralWindowRepresentative_twist_integrable a f 0

/-- Actual physical window/mollifier convolution's ordinary Fourier
transform factors into original complex-frequency sample and the
mollifier's ordinary Fourier transform. Full original -2π normalization. -/
theorem f08_007_original_window_convolution_fourier
    (a : ℝ) (f : RealComplexL2) (rho : ℝ → ℂ)
    (hrho : Integrable rho) (xi : ℝ) :
    (𝓕 (neutralWindowRepresentative a f
      ⋆[ContinuousLinearMap.mul ℂ ℂ] rho)) xi =
      neutralWindowEvaluation a ((-2 * Real.pi * xi : ℝ) : ℂ) f *
        (𝓕 rho) xi := by
  have hf := f08_007_original_window_representative_integrable a f
  rw [Real.fourier_mul_convolution_eq hf hrho xi,
      neutralWindowRepresentative_fourier]

/-- The same genuine physical convolution uses the project's original
positive-exponent raw transform; this identity is not an invented
alternative Fourier convention. -/
theorem f08_007_original_window_convolution_raw_transform
    (a : ℝ) (f : RealComplexL2) (rho : ℝ → ℂ)
    (hrho : Integrable rho) (xi : ℝ) :
    neutralRawTransform
      (neutralWindowRepresentative a f
        ⋆[ContinuousLinearMap.mul ℂ ℂ] rho)
      ((-2 * Real.pi * xi : ℝ) : ℂ) =
      neutralWindowEvaluation a ((-2 * Real.pi * xi : ℝ) : ℂ) f *
        (𝓕 rho) xi := by
  calc
    _ = (𝓕 (neutralWindowRepresentative a f
        ⋆[ContinuousLinearMap.mul ℂ ℂ] rho)) xi :=
      (neutralRawTransform_fourier _ xi).symm
    _ = _ := f08_007_original_window_convolution_fourier a f rho hrho xi

#print axioms f08_007_original_window_representative_integrable
#print axioms f08_007_original_window_convolution_fourier
#print axioms f08_007_original_window_convolution_raw_transform

end
end WeilDefect
