import WeilDefect.Morphology.NeutralSourceBoundaryRemoval

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped SchwartzMap FourierTransform

/-- A genuine L2 spectral product represents distributional multiplication.
The symbol need not itself lie in an Lp space. -/
theorem l2SpectralProduct_toTemperedDistribution
    (m : ℝ → ℂ) (hm : Function.HasTemperateGrowth m) (f : RealComplexL2)
    (hp : MemLp (fun ξ : ℝ => m ξ * f ξ) 2 volume) :
    ((hp.toLp (fun ξ : ℝ => m ξ * f ξ) : RealComplexL2) : RealComplexTempered) =
      TemperedDistribution.smulLeftCLM ℂ m (f : RealComplexTempered) := by
  ext u
  simp only [Lp.toTemperedDistribution_apply,
    TemperedDistribution.smulLeftCLM_apply_apply]
  apply integral_congr_ae
  filter_upwards [hp.coeFn_toLp] with ξ hξ
  rw [hξ, SchwartzMap.smulLeftCLM_apply hm]
  simp only [smul_eq_mul]
  ring

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Exact operator-domain criterion in the already fixed Fourier coordinate.
It is stronger than the source form's one-logarithm quadratic energy. -/
def neutralWeilSpectralProduct
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a ξ : ℝ) : ℂ :=
  (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
    (𝓕 carrier.l2Mode : RealComplexL2) ξ

/-- Canonical physical L2 core constructed from the exact spectral product. -/
def neutralWeilOperatorDomainCore
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume) :
    RealComplexL2 :=
  𝓕⁻ (hp.toLp (neutralWeilSpectralProduct carrier a))

theorem neutralWeilOperatorDomainCore_toTemperedDistribution
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume) :
    ((neutralWeilOperatorDomainCore carrier a hp : RealComplexL2) : RealComplexTempered) =
      rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode := by
  unfold neutralWeilOperatorDomainCore rightLimitWeilMultiplierCore
  rw [TemperedDistribution.fourierMultiplierCLM_apply,
    carrier.fourier_temperedMode_eq,
    ← l2SpectralProduct_toTemperedDistribution _ hSymbol.hasTemperateGrowth
      (𝓕 carrier.l2Mode : RealComplexL2) hp,
    Lp.fourierInv_toTemperedDistribution_eq]

/-- Actual whole-line core pairing, without pointwise exponential growth. -/
theorem neutralWeilOperatorDomainCore_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (u : SchwartzMap ℝ ℂ) :
    (∫ x : ℝ, u x * neutralWeilOperatorDomainCore carrier a hp x) =
      rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode u := by
  have h := congrArg (fun T : RealComplexTempered => T u)
    (neutralWeilOperatorDomainCore_toTemperedDistribution carrier a hSymbol hp)
  simpa only [Lp.toTemperedDistribution_apply, smul_eq_mul] using h

/-- The regular actual source defect constructed from the operator-domain
core, the actual pole, and the certified exterior candidate. -/
def neutralWeilOperatorDomainDefect
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume) : ℝ → ℂ :=
  fun x => neutralWeilOperatorDomainCore carrier a hp x +
    neutralWeilSourcePole carrier x - neutralExteriorResidualCandidate carrier a x

theorem neutralWeilOperatorDomainDefect_locallyIntegrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume) :
    LocallyIntegrable (neutralWeilOperatorDomainDefect carrier a hp) volume :=
  (((Lp.memLp (neutralWeilOperatorDomainCore carrier a hp)).locallyIntegrable
    (by norm_num)).add
      (neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable).sub
        (neutralExteriorResidualCandidate_locallyIntegrable carrier hca)

theorem neutralWeilOperatorDomainDefect_represents
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    (∫ x : ℝ, u x * neutralWeilOperatorDomainDefect carrier a hp x) =
      neutralCompactSourceDefect carrier a hSymbol u hu := by
  have hr := compactSchwartz_mul_locallyIntegrable u hu
    (neutralWeilOperatorDomainCore carrier a hp)
    ((Lp.memLp _).locallyIntegrable (by norm_num))
  have hpole := frozenWeilCompactAction_pole_integrable carrier u hu
  have he := neutralExteriorResidualCandidate_compact_pairing_integrable carrier hca u hu
  unfold neutralWeilOperatorDomainDefect neutralCompactSourceDefect frozenWeilCompactAction
  simp only [mul_sub, mul_add]
  rw [integral_sub (hr.add hpole) he, integral_add hr hpole,
    neutralWeilOperatorDomainCore_pairing carrier a hSymbol hp u]

/-- The spectral operator-domain criterion supplies the regularity witness
needed by boundary removal. Actual central source cancellation remains. -/
theorem neutralExteriorIntegralGrowthResidual_realizes_of_operatorDomain
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (hp : MemLp (neutralWeilSpectralProduct carrier a) 2 volume)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a → frozenWeilCompactAction carrier a hSymbol u hu = 0) :
    IntegralGrowthWeilWeakRealization carrier
      (neutralExteriorIntegralGrowthResidual carrier hca) hSymbol :=
  neutralExteriorIntegralGrowthResidual_realizes_of_regular_cancellation
    carrier hc hca hSymbol
    (neutralWeilOperatorDomainDefect_locallyIntegrable carrier hca hp)
    (neutralWeilOperatorDomainDefect_represents carrier hca hSymbol hp) hcentral

end

end WeilDefect
