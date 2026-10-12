import WeilDefect.Morphology.NeutralLogMetricTimeActionBounds
import WeilDefect.Morphology.NeutralLogMetricSpectralL2
import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology FourierTransform
open scoped FourierTransform

/-- Ordinary Fourier integrals and L2 Fourier vectors agree for an
 integrable L2 function, using the existing repo's L1/L2 agreement theorem. -/
theorem neutralLogMetricIntegrableL2_fourier_toLp_eq
    (f : ℝ → ℂ) (hfi : Integrable f) (hf : MemLp f 2 volume)
    (hF : MemLp (𝓕 f) 2 volume) :
    (𝓕 (hf.toLp f) : RealComplexL2) = hF.toLp (𝓕 f) := by
  have hi : Integrable (hf.toLp f : ℝ → ℂ) := hfi.congr hf.coeFn_toLp.symm
  have ha := neutralIntegrableL2_fourier_ae (hf.toLp f) hi
  apply Lp.ext
  filter_upwards [ha, hF.coeFn_toLp] with ξ hξ hFξ
  exact (hξ.trans (Real.fourier_congr_ae hf.coeFn_toLp ξ)).trans hFξ.symm

/-- The inverse transform of the ordinary-Fourier L2 representative
 is the actual physical L2 representative, not a separately postulated source. -/
theorem neutralLogMetricIntegrableL2_fourierInv_toLp_eq
    (f : ℝ → ℂ) (hfi : Integrable f) (hf : MemLp f 2 volume)
    (hF : MemLp (𝓕 f) 2 volume) :
    (𝓕⁻ (hF.toLp (𝓕 f)) : RealComplexL2) = hf.toLp f := by
  have h := congrArg (fun u : RealComplexL2 => (𝓕⁻ u : RealComplexL2))
    (neutralLogMetricIntegrableL2_fourier_toLp_eq f hfi hf hF)
  simpa only [fourierInv_fourier_eq] using h.symm

set_option maxHeartbeats 1000000 in
/-- The constructed inverse-transformed finite-action spectral vector
 equals the actual full-line physical action vector, retaining exterior action. -/
theorem neutralLogMetricTimeAction_fourierInv_eq_physical
    (ε R M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    (𝓕⁻ ((neutralLogMetricTimeAction_fourier_memLp_two ε R M hε hM
      v hv hvi hbound hp).toLp
      (𝓕 (fun x : ℝ => v x + ∫ t in Icc ε R,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))))) :
            RealComplexL2) =
      (neutralLogMetricTimeAction_memLp_two ε R M hε hM v hv hvi hbound).toLp
        (fun x : ℝ => v x + ∫ t in Icc ε R,
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) := by
  exact neutralLogMetricIntegrableL2_fourierInv_toLp_eq _
    (neutralLogMetricTimeAction_integrable ε R M hε hM v hv hvi hbound)
    (neutralLogMetricTimeAction_memLp_two ε R M hε hM v hv hvi hbound)
    (neutralLogMetricTimeAction_fourier_memLp_two ε R M hε hM v hv hvi hbound hp)


set_option maxHeartbeats 1000000 in
/-- The actual full-line physical action vectors converge to the inverse
 Fourier transform of the weighted product, under its explicit L2 domain premise. -/
theorem neutralLogMetricTimeAction_physical_toLp_tendsto
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume) :
    Tendsto (fun n : ℕ =>
      (neutralLogMetricTimeAction_memLp_two
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound).toLp
        (fun x : ℝ => v x +
          ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
            ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
              (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))))
      atTop (𝓝 (𝓕⁻ (hp.toLp
        (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ))) : RealComplexL2)) := by
  have h := neutralLogMetricTimeAction_fourierInv_toLp_tendsto M hM v hv hvi hbound hp
  simp_rw [neutralLogMetricTimeAction_fourierInv_eq_physical] at h
  exact h

set_option maxHeartbeats 1000000 in
/-- Actual physical-vector pairings converge against every physical L2 test. -/
theorem neutralLogMetricTimeAction_physical_inner_tendsto
    (M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M)
    (hp : MemLp (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)) 2 volume)
    (φ : RealComplexL2) :
    Tendsto (fun n : ℕ => inner ℂ
      ((neutralLogMetricTimeAction_memLp_two
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M (by positivity) hM v hv hvi hbound).toLp
        (fun x : ℝ => v x +
          ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
            ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
              (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) φ)
      atTop (𝓝 (inner ℂ (𝓕⁻ (hp.toLp
        (fun ξ : ℝ => (𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ)))) φ)) := by
  have hc : Continuous (fun u : RealComplexL2 => inner ℂ u φ) :=
    continuous_id.inner (𝕜 := ℂ) continuous_const
  exact (hc.tendsto _).comp
    (neutralLogMetricTimeAction_physical_toLp_tendsto M hM v hv hvi hbound hp)

end
end WeilDefect
