import WeilDefect.Morphology.NeutralLogMetricPoissonMass
import Mathlib.Analysis.Fourier.Inversion

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped FourierTransform

/-- The damped spectral exponential is integrable at positive time. -/
theorem neutralLogMetricPoissonExponential_integrable (t : ℝ) (ht : 0 < t) :
    Integrable (fun ξ : ℝ => (Real.exp (-t * |ξ|) : ℂ)) := by
  have h := neutralLogMetricPoissonIntegrand_integrable t 0 ht
  have he : neutralLogMetricPoissonIntegrand t 0 =
      (fun ξ : ℝ => (Real.exp (-t * |ξ|) : ℂ)) := by
    funext ξ
    simp [neutralLogMetricPoissonIntegrand, Complex.ofReal_exp,
      Complex.ofReal_mul, Complex.ofReal_neg]
  rw [he] at h
  exact h

/-- The Fourier transform of the even spectral exponential is the same
 rational Poisson density as its inverse transform. -/
theorem neutralLogMetricPoissonExponential_fourier
    (t x : ℝ) (ht : 0 < t) :
    (𝓕 (fun ξ : ℝ => (Real.exp (-t * |ξ|) : ℂ))) x =
      (neutralLogMetricPoissonDensity t x : ℂ) := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  calc
    _ = ∫ ξ : ℝ, neutralLogMetricPoissonIntegrand t (-2 * Real.pi * x) ξ := by
      apply integral_congr_ae
      filter_upwards [] with ξ
      simp only [smul_eq_mul, Complex.ofReal_exp]
      rw [← Complex.exp_add]
      unfold neutralLogMetricPoissonIntegrand
      congr 1
      push_cast
      ring
    _ = _ := by
      rw [neutralLogMetricPoisson_integral t _ ht]
      unfold neutralLogMetricPoissonDensity
      have hden : t ^ 2 + (-2 * Real.pi * x) ^ 2 =
          t ^ 2 + 4 * Real.pi ^ 2 * x ^ 2 := by ring
      rw [hden]

/-- The actual physical Poisson kernel has spectral multiplier
 exp(-t*|ξ|), in Mathlib's 2*pi Fourier convention. -/
theorem neutralLogMetricPoissonDensity_fourier
    (t ξ : ℝ) (ht : 0 < t) :
    (𝓕 (fun x : ℝ => (neutralLogMetricPoissonDensity t x : ℂ))) ξ =
      (Real.exp (-t * |ξ|) : ℂ) := by
  let f : ℝ → ℂ := fun x => (Real.exp (-t * |x|) : ℂ)
  have hf : Integrable f := neutralLogMetricPoissonExponential_integrable t ht
  have hF : 𝓕 f = (fun x : ℝ => (neutralLogMetricPoissonDensity t x : ℂ)) := by
    funext x
    exact neutralLogMetricPoissonExponential_fourier t x ht
  have hFi : Integrable (𝓕 f) := by
    rw [hF]
    exact (neutralLogMetricPoissonDensity_integrable t ht).ofReal
  have hInv : 𝓕⁻ f = (fun x : ℝ => (neutralLogMetricPoissonDensity t x : ℂ)) := by
    funext x
    exact neutralLogMetricPoisson_fourierInv t x ht
  have hc : Continuous f := by unfold f; fun_prop
  have h := hf.fourier_fourierInv_eq hFi (hc.continuousAt (x := ξ))
  rw [hInv] at h
  exact h

end
end WeilDefect
