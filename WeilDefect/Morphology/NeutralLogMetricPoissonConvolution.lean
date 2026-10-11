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
  have h := Real.fourier_mul_convolution_eq hv
    (neutralLogMetricPoissonDensity_integrable t ht).ofReal ξ
  exact h.trans (congrArg (fun z : ℂ => (𝓕 v) ξ * z)
    (neutralLogMetricPoissonDensity_fourier t ξ ht))

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


/-- Identity minus the whole-line Poisson convolution is integrable
 for every integrable trial at positive time. -/
theorem neutralLogMetricPoissonAction_integrable
    (t : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Integrable v) :
    Integrable (fun x : ℝ => v x - ∫ y : ℝ,
      v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) :=
  hv.sub (neutralLogMetricPoissonConvolution_integrable t ht v hv)

/-- The cancelled whole-line action has multiplier 1-exp(-t*|ξ|).
 Fourier subtraction is justified by genuine integrability of both terms. -/
theorem neutralLogMetricPoissonAction_fourier
    (t ξ : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Integrable v) :
    (𝓕 (fun x : ℝ => v x - ∫ y : ℝ,
      v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) ξ =
      (𝓕 v) ξ * (1 - (Real.exp (-t * |ξ|) : ℂ)) := by
  let C : ℝ → ℂ := fun x => ∫ y : ℝ,
    v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)
  have hC : Integrable C := neutralLogMetricPoissonConvolution_integrable t ht v hv
  have hs : (𝓕 (fun x => v x - C x)) ξ = (𝓕 v) ξ - (𝓕 C) ξ := by
    rw [Real.fourier_eq, Real.fourier_eq, Real.fourier_eq]
    simp_rw [smul_sub]
    exact integral_sub ((Real.fourierIntegral_convergent_iff ξ).2 hv)
      ((Real.fourierIntegral_convergent_iff ξ).2 hC)
  have he : (𝓕 C) ξ = (𝓕 v) ξ * (Real.exp (-t * |ξ|) : ℂ) :=
    neutralLogMetricPoissonConvolution_fourier t ξ ht v hv
  change (𝓕 (fun x => v x - C x)) ξ = _
  rw [hs, he]
  ring

/-- The actual cancelled action of a cap-bounded zero-extended trial
 is integrable over the entire physical line. -/
theorem neutralLogMetricPoissonAction_zeroExtension_integrable
    (B M t : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M) :
    Integrable (fun x : ℝ => neutralLogMetricTrialZeroExtension B v x -
      ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
        (neutralLogMetricPoissonDensity t (x - y) : ℂ)) := by
  exact neutralLogMetricPoissonAction_integrable t ht _
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)

/-- Whole-line Fourier cancellation for the actual zero extension,
 without assuming global integrability of the original trial. -/
theorem neutralLogMetricPoissonAction_zeroExtension_fourier
    (B M t ξ : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M) :
    (𝓕 (fun x : ℝ => neutralLogMetricTrialZeroExtension B v x -
      ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
        (neutralLogMetricPoissonDensity t (x - y) : ℂ))) ξ =
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        (1 - (Real.exp (-t * |ξ|) : ℂ)) := by
  exact neutralLogMetricPoissonAction_fourier t ξ ht _
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)

end
end WeilDefect
