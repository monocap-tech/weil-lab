import WeilDefect.Morphology.NeutralOperatorFormEnergy

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped ComplexConjugate FourierTransform ComplexInnerProductSpace

/-- The physical Hermitian L2 pairing genuinely converges. -/
theorem l2HermitianPairing_integrable (f g : RealComplexL2) :
    Integrable (fun x : ℝ => conj (f x) * g x) volume := by
  simpa only [RCLike.inner_apply'] using (L2.integrable_inner (𝕜 := ℂ) f g)

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Plancherel identifies the physical operator core pairing with the exact
normalized spectral pairing, without a source quadratic identity premise. -/
theorem neutralWeilOperatorDomainCore_hermitian_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (a : ℝ)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (f : RealComplexL2) :
    (∫ x : ℝ, conj (f x) * neutralWeilOperatorDomainCore carrier a hp x) =
      ∫ ξ : ℝ, conj ((𝓕 f : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 carrier.l2Mode : RealComplexL2) ξ := by
  calc
    _ = ⟪f, neutralWeilOperatorDomainCore carrier a hp⟫ := by
      simp only [L2.inner_def, RCLike.inner_apply']
    _ = ⟪𝓕 f, 𝓕 (neutralWeilOperatorDomainCore carrier a hp)⟫ :=
      (Lp.inner_fourier_eq f _).symm
    _ = ⟪𝓕 f, hp.toLp (neutralWeilSpectralProduct carrier a)⟫ := by
      rw [neutralWeilOperatorDomainCore, fourier_fourierInv_eq]
    _ = _ := by
      rw [L2.inner_def]
      apply integral_congr_ae
      filter_upwards [hp.coeFn_toLp] with ξ hξ
      rw [RCLike.inner_apply', hξ]
      unfold neutralWeilSpectralProduct
      ring

/-- The multiplier part of the form, tested against any vector in its domain,
is the actual physical operator-core pairing on the carrier column. -/
theorem sourceDomainMultiplierPairing_operatorCore
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (a : ℝ)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (D : NeutralSourceFormDomainAttachment carrier a) (f : D.domain) :
    sourceDomainMultiplierPairing D f ⟨carrier.l2Mode, D.carrier_mem⟩ =
      ∫ x : ℝ, conj (f.val x) * neutralWeilOperatorDomainCore carrier a hp x :=
  (neutralWeilOperatorDomainCore_hermitian_pairing carrier a hp f.val).symm

/-- Genuine convergence for the chosen physical carrier representative. -/
theorem neutralWeilOperatorDomainCore_carrier_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (a : ℝ)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume) :
    Integrable (fun x : ℝ => conj (carrier.h x) *
      neutralWeilOperatorDomainCore carrier a hp x) volume := by
  apply (l2HermitianPairing_integrable carrier.l2Mode
    (neutralWeilOperatorDomainCore carrier a hp)).congr
  filter_upwards [carrier.h_memLp.coeFn_toLp] with x hx
  change conj (carrier.h_memLp.toLp carrier.h x) * _ = _
  rw [hx]

/-- The concrete quadratic diagonal is the physical core-plus-pole energy.
This identifies the constructed objects, not an imported abstract source form. -/
theorem sourceDomainQuadratic_operatorCore
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c ≤ a)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (D : NeutralSourceFormDomainAttachment carrier a) :
    sourceDomainQuadratic D ⟨carrier.l2Mode, D.carrier_mem⟩ =
      (∫ x : ℝ, conj (carrier.h x) *
        neutralWeilOperatorDomainCore carrier a hp x).re +
      (∫ x : ℝ, conj (carrier.h x) * neutralWeilSourcePole carrier x).re := by
  have hdiag := congrArg Complex.re
    (sourceDomainMultiplierPairing_diagonal D ⟨carrier.l2Mode, D.carrier_mem⟩)
  rw [sourceDomainMultiplierPairing_operatorCore carrier a hp D] at hdiag
  simp only [Complex.ofReal_re] at hdiag
  rw [sourceDomainQuadratic_carrier D hca, ← hdiag]
  congr 1
  apply congrArg Complex.re
  apply integral_congr_ae
  filter_upwards [carrier.h_memLp.coeFn_toLp] with x hx
  change conj (carrier.h_memLp.toLp carrier.h x) * _ = _
  rw [hx]

end

end WeilDefect
