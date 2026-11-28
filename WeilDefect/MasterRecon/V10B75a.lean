import WeilDefect.MasterRecon.V10B74b

/-! V10B75a: exact principal and Archimedean pairing on the original
weighted carrier. The residual estimate remains explicit. -/
namespace WeilDefect.MasterRecon.V10B75a
open MeasureTheory Set
open scoped InnerProduct FourierTransform ComplexConjugate
open V08I (FullL2 logCarrier physicalInclusion logWeight inverseWeight)
open V10B69a (dividedTrial)
open V10B74a (F principalSpectrum)
open V10B8e (spectralPhysical archOperator realMultiplier)
open V10B74b (gammaSpectrum physicalAction)

theorem principal_pair (j : Fin 16) (w : logCarrier (1/4)) :
    inner ℂ (dividedTrial j) w =
      inner ℂ (principalSpectrum j) (spectralPhysical (1/4) w) := by
  change inner ℂ (dividedTrial j : FullL2) (w : FullL2) = _
  rw [L2.inner_def,L2.inner_def]
  apply integral_congr_ae
  have hj := V08I.physicalInclusion_fourier_ae (1/4) (dividedTrial j)
  change (F j : ℝ → ℂ) =ᵐ[volume]
    fun u => inverseWeight u * (dividedTrial j : FullL2) u at hj
  have hw := V08I.physicalInclusion_fourier_ae (1/4) w
  change (spectralPhysical (1/4) w : ℝ → ℂ) =ᵐ[volume]
    fun u => inverseWeight u * (w : FullL2) u at hw
  filter_upwards [V10B74a.principalSpectrum_ae j,hj,hw] with u hp hj' hw'
  rw [hp,hj',hw']
  simp only [RCLike.inner_apply', inverseWeight, map_mul, Complex.conj_ofReal]
  have hreal : logWeight u * (Real.sqrt (logWeight u))⁻¹ *
      (Real.sqrt (logWeight u))⁻¹ = 1 := by
    rw [mul_assoc, ← pow_two, inv_pow, Real.sq_sqrt (V08I.logWeight_pos u).le,
      mul_inv_cancel₀ (V08I.logWeight_pos u).ne']
  have hc : (logWeight u : ℂ) * ((Real.sqrt (logWeight u))⁻¹ : ℝ) *
      ((Real.sqrt (logWeight u))⁻¹ : ℝ) = 1 := by exact_mod_cast hreal
  calc
    _ = 1 * (conj ((dividedTrial j : FullL2) u) * (w : FullL2) u) := by ring
    _ = _ := by rw [← hc]; ring

theorem arch_spectral_pair (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (j : Fin 16)
    (w : logCarrier (1/4)) :
    inner ℂ (archOperator (1/4) hd C hC (dividedTrial j)) w =
      inner ℂ (gammaSpectrum hd C hC j) (spectralPhysical (1/4) w) := by
  unfold archOperator V10B8e.correction gammaSpectrum
  rw [ContinuousLinearMap.add_apply,ContinuousLinearMap.one_apply,inner_add_left]
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]
  rw [principal_pair, ← V10B74b.actual_spectrum j, inner_add_left]

theorem arch_physical_pair (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (j : Fin 16)
    (w : logCarrier (1/4)) :
    inner ℂ (archOperator (1/4) hd C hC (dividedTrial j)) w =
      inner ℂ (physicalAction hd C hC j) (physicalInclusion (1/4) w) := by
  rw [arch_spectral_pair, ← V10B74b.physicalAction_fourier]
  change inner ℂ ((Lp.fourierTransformₗᵢ ℝ ℂ) (physicalAction hd C hC j))
    ((Lp.fourierTransformₗᵢ ℝ ℂ) (physicalInclusion (1/4) w)) = _
  first
  | exact (Lp.fourierTransformₗᵢ ℝ ℂ).inner_map_map _ _
  | exact (Lp.fourierTransformₗᵢ ℝ ℂ).toLinearIsometry.inner_map_map _ _

end WeilDefect.MasterRecon.V10B75a

#print axioms WeilDefect.MasterRecon.V10B75a.principal_pair
#print axioms WeilDefect.MasterRecon.V10B75a.arch_spectral_pair
#print axioms WeilDefect.MasterRecon.V10B75a.arch_physical_pair
