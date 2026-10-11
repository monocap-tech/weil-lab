import WeilDefect.Morphology.NeutralLogMetricTimeActionBounds
import WeilDefect.Morphology.NeutralLogMetricSpectralL2
import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
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

/-- The constructed inverse-transformed finite-action spectral vector
 equals the actual full-line physical action vector, retaining exterior action. -/
set_option maxHeartbeats 1000000 in
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

end
end WeilDefect
