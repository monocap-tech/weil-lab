import WeilDefect.Morphology.NeutralLogMetricPoissonFourier
import WeilDefect.Morphology.NeutralLogMetricPoissonAction
import Mathlib.Analysis.Fourier.Convolution

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped Convolution FourierTransform

/-- Cap-bounded measurable trials have integrable zero extensions;
 no global integrability of the original trial is needed. -/
theorem neutralLogMetricTrialZeroExtension_integrable
    (B M : ℝ) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M) :
    Integrable (neutralLogMetricTrialZeroExtension B v) := by
  have hi : IntegrableOn v (Icc (-B) B) := by
    apply Measure.integrableOn_of_bounded
      (by simp : volume (Icc (-B) B) ≠ ⊤) hv.aestronglyMeasurable
    filter_upwards [ae_restrict_mem measurableSet_Icc] with x hx
    exact hbound x hx
  exact hi.integrable_indicator measurableSet_Icc

/-- The whole-line Poisson convolution of an integrable trial is
 integrable, retaining the exterior part of its action. -/
theorem neutralLogMetricPoissonConvolution_integrable
    (t : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Integrable v) :
    Integrable (fun x : ℝ => ∫ y : ℝ,
      v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) := by
  change Integrable (v ⋆[ContinuousLinearMap.mul ℂ ℂ]
    (fun x : ℝ => (neutralLogMetricPoissonDensity t x : ℂ)))
  exact hv.integrable_convolution (ContinuousLinearMap.mul ℂ ℂ)
    (neutralLogMetricPoissonDensity_integrable t ht).ofReal

/-- Exact Fourier transport of the actual whole-line convolution. -/
theorem neutralLogMetricPoissonConvolution_fourier
    (t ξ : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Integrable v) :
    (𝓕 (fun x : ℝ => ∫ y : ℝ,
      v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) ξ =
      (𝓕 v) ξ * (Real.exp (-t * |ξ|) : ℂ) := by
  change (𝓕 (v ⋆[ContinuousLinearMap.mul ℂ ℂ]
    (fun x : ℝ => (neutralLogMetricPoissonDensity t x : ℂ)))) ξ = _
  rw [Real.fourier_mul_convolution_eq hv
    (neutralLogMetricPoissonDensity_integrable t ht).ofReal,
    neutralLogMetricPoissonDensity_fourier t ξ ht]

/-- The Fourier convolution identity applies to the actual zero
 extension using only measurability and boundedness on the finite cap. -/
theorem neutralLogMetricPoissonConvolution_zeroExtension_fourier
    (B M t ξ : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M) :
    (𝓕 (fun x : ℝ => ∫ y : ℝ,
      neutralLogMetricTrialZeroExtension B v y *
        (neutralLogMetricPoissonDensity t (x - y) : ℂ))) ξ =
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        (Real.exp (-t * |ξ|) : ℂ) := by
  exact neutralLogMetricPoissonConvolution_fourier t ξ ht _
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)

end
end WeilDefect
