import WeilDefect.Morphology.NeutralWeilSourceThreshold

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate FourierTransform

/-- Complex polarization on the retained domain itself. The first slot is
antilinear. This does not enlarge a source form domain to the ambient L2 space. -/
theorem sourceFormDomain_polarization
    {V : Type*} [AddCommGroup V] [Module ℂ V]
    (B : V →ₗ⋆[ℂ] V →ₗ[ℂ] ℂ) (x y : V) :
    B x y =
      (B (x + y) (x + y) - B (x - y) (x - y) -
        Complex.I * B (x + Complex.I • y) (x + Complex.I • y) +
        Complex.I * B (x - Complex.I • y) (x - Complex.I • y)) / 4 := by
  simp only [map_add, map_sub, LinearMap.add_apply, LinearMap.sub_apply,
    map_smulₛₗ, LinearMap.smul_apply, smul_eq_mul, RingHom.id_apply,
    starRingEnd_apply, Complex.star_def, Complex.conj_I,
    ← pow_two, Complex.I_sq, mul_add, ← mul_assoc, mul_neg, neg_neg,
    one_mul, neg_one_mul, mul_sub, sub_sub]
  ring

/-- Equality of complex quadratic forms determines mixed terms on a specified
submodule. Membership of both vectors remains explicit and load-bearing. -/
theorem sourceFormDomain_eq_of_diagonal
    {V : Type*} [AddCommGroup V] [Module ℂ V]
    (D : Submodule ℂ V)
    (B C : D →ₗ⋆[ℂ] D →ₗ[ℂ] ℂ)
    (hdiag : ∀ z : D, B z z = C z z) (x y : D) :
    B x y = C x y := by
  rw [sourceFormDomain_polarization B x y,
    sourceFormDomain_polarization C x y]
  simp only [hdiag]

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Source-domain custody for the actual rough carrier. The domain and its
logarithmic energy are supplied explicitly, rather than inferred from L2 or
from smoothness of the ordinary Fourier transform. Source diagonal attachment
is a separate obligation. -/
structure NeutralSourceFormDomainAttachment
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) where
  domain : Submodule ℂ RealComplexL2
  supported : ∀ f : domain, ∀ᵐ x ∂volume,
    x ∉ Set.Icc (-a) a → (f.val : ℝ → ℂ) x = 0
  carrier_mem : carrier.l2Mode ∈ domain
  logEnergy :
    ∀ f : domain,
      Integrable
        (fun ξ : ℝ => logarithmicFourierWeight ξ *
          ‖(𝓕 (f.val) : RealComplexL2) ξ‖ ^ 2) volume

/-- A function representing the fixed-cutoff multiplier core. Every analytic
and source identification obligation is visible. In particular, a tempered
distribution alone is not used to construct these regularity fields. -/
structure NeutralWeilCoreFunctionRepresentation
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a) where
  r : ℝ → ℂ
  locallyIntegrable : LocallyIntegrable r volume
  growthConstant : ℝ
  growthRate : ℝ
  growthConstant_nonneg : 0 ≤ growthConstant
  growthRate_nonneg : 0 ≤ growthRate
  growth_bound : ∀ x : ℝ,
    ‖r x‖ ≤ growthConstant * Real.exp (growthRate * |x|)
  represents : ∀ (u : SchwartzMap ℝ ℂ) (_hu : HasCompactSupport u),
    (∫ x : ℝ, u x * r x ∂volume) =
      rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode u

/-- Construct the full residual as core plus the already certified source
pole. The central cancellation is required of this specific sum. -/
def neutralWeilResidualFromCore
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a)
    {hSymbol : RightLimitWeilSymbolTemperatePremise a}
    (core : NeutralWeilCoreFunctionRepresentation carrier a hSymbol)
    (hzero : ∀ᵐ x ∂volume,
      x ∈ Set.Ioo (-a) a → core.r x + neutralWeilSourcePole carrier x = 0) :
    NeutralExponentialResidualCarrier c where
  a := a
  strict := hca
  q := fun x => core.r x + neutralWeilSourcePole carrier x
  q_locallyIntegrable := core.locallyIntegrable.add
    (neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable
  growthConstant := core.growthConstant +
    (neutralWeilSourcePole_growthData carrier).growthConstant
  growthRate := max core.growthRate
    (neutralWeilSourcePole_growthData carrier).growthRate
  growthConstant_nonneg := add_nonneg core.growthConstant_nonneg
    (neutralWeilSourcePole_growthData carrier).growthConstant_nonneg
  growthRate_nonneg := core.growthRate_nonneg.trans (le_max_left _ _)
  growth_bound := by
    intro x
    let p := neutralWeilSourcePole_growthData carrier
    have hr := Real.exp_le_exp.mpr
      (mul_le_mul_of_nonneg_right (le_max_left core.growthRate p.growthRate)
        (abs_nonneg x))
    have hp := Real.exp_le_exp.mpr
      (mul_le_mul_of_nonneg_right (le_max_right core.growthRate p.growthRate)
        (abs_nonneg x))
    calc
      ‖core.r x + neutralWeilSourcePole carrier x‖ ≤
        ‖core.r x‖ + ‖neutralWeilSourcePole carrier x‖ := norm_add_le _ _
      _ ≤ core.growthConstant * Real.exp (core.growthRate * |x|) +
        p.growthConstant * Real.exp (p.growthRate * |x|) :=
          add_le_add (core.growth_bound x) (p.growth_bound x)
      _ ≤ core.growthConstant * Real.exp (max core.growthRate p.growthRate * |x|) +
        p.growthConstant * Real.exp (max core.growthRate p.growthRate * |x|) :=
          add_le_add (mul_le_mul_of_nonneg_left hr core.growthConstant_nonneg)
            (mul_le_mul_of_nonneg_left hp p.growthConstant_nonneg)
      _ = _ := by ring
  vanishes_ae := hzero

/-- Exact compact-test realization for the residual just constructed. Its weak
identity follows from genuine integrability and the core representation; it is
not a new assumption about an already packaged full residual. -/
theorem neutralWeilResidualFromCore_weakRealization
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a)
    {hSymbol : RightLimitWeilSymbolTemperatePremise a}
    (core : NeutralWeilCoreFunctionRepresentation carrier a hSymbol)
    (hzero : ∀ᵐ x ∂volume,
      x ∈ Set.Ioo (-a) a → core.r x + neutralWeilSourcePole carrier x = 0) :
    RightLimitWeilWeakRealizationPremise c carrier
      (neutralWeilResidualFromCore carrier hca core hzero)
      hSymbol (neutralWeilSourcePole carrier) := by
  refine ⟨(neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable, ?_⟩
  intro u hu
  change (∫ x : ℝ, u x * (core.r x + neutralWeilSourcePole carrier x) ∂volume) = _
  simp only [mul_add]
  rw [integral_add
    (compactSchwartz_mul_locallyIntegrable u hu core.r core.locallyIntegrable)
    (frozenWeilCompactAction_pole_integrable carrier u hu), core.represents u hu]

end

end WeilDefect
