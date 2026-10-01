import WeilDefect.Morphology.NeutralIntegralGrowthGaussian

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-- Radius-only pole tail estimate; no residual growth fields are consumed. -/
theorem poleFilteredMode_norm_le_radiusTail
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hca : c < a)
    (pole : ℝ → ℂ)
    (hpole : NeutralPoleExponentialGrowthData pole)
    (Ck : ℂ) {R x : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 ≤ R)
    (hlarge :
      8 * hpole.growthRate
        ≤ R * (a - c))
    (hx : x ∉ Set.Ioo (-a) a) :
    ‖pole x * movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (hpole.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (hpole.growthRate * c)
      * Real.exp (-R * (a - c) ^ 2 / 16))
      * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
  have hfiltered :=
    movingGaussianFilteredMode_norm_le_radiusEnvelope
      carrier a hca Ck R x hc hR hx
  have hcompletion :=
    gaussianTailCompletion_bound
      hpole.growthRate_nonneg hR hc hca
      hlarge hx
  rw [norm_mul]
  calc
    ‖pole x‖ * ‖movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (hpole.growthConstant
      * Real.exp (hpole.growthRate * |x|))
      *
    ((‖Ck‖ * Real.sqrt R
      * gaussianSupportEnvelope R c x)
      * neutralPhysicalCompactL1Mass carrier) := by
        exact mul_le_mul
          (hpole.growth_bound x)
          hfiltered
          (norm_nonneg _)
          (mul_nonneg
            hpole.growthConstant_nonneg
            (Real.exp_nonneg _))
    _ ≤
    (hpole.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (hpole.growthRate * c)
      * Real.exp (-R * (a - c) ^ 2 / 16))
      * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
        have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
          mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
        have hnonneg :
            0 ≤ hpole.growthConstant
              * (‖Ck‖ * Real.sqrt R)
              * neutralPhysicalCompactL1Mass carrier :=
          mul_nonneg
            (mul_nonneg hpole.growthConstant_nonneg hkernel)
            (neutralPhysicalCompactL1Mass_nonneg carrier)
        nlinarith [hcompletion]

/--
The explicit exponential-growth pole term pairs integrably with the actual
moving-Gaussian filtered mode.
-/
theorem poleFilteredMode_integrable_of_radius
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hca : c < a)
    (pole : ℝ → ℂ)
    (hpole : NeutralPoleExponentialGrowthData pole)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge :
      8 * hpole.growthRate
        ≤ R * (a - c)) :
    Integrable
      (fun x : ℝ =>
        pole x * movingGaussianFilteredMode Ck R carrier x) volume := by
  let A : ℝ :=
    hpole.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (hpole.growthRate * c)
      * Real.exp (-R * (a - c) ^ 2 / 16)
  have hA : 0 ≤ A := by
    dsimp [A]
    have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
      mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
    have h₁ :
        0 ≤ hpole.growthConstant
          * (‖Ck‖ * Real.sqrt R)
          * neutralPhysicalCompactL1Mass carrier :=
      mul_nonneg
        (mul_nonneg hpole.growthConstant_nonneg hkernel)
        (neutralPhysicalCompactL1Mass_nonneg carrier)
    exact mul_nonneg
      (mul_nonneg h₁ (Real.exp_nonneg _))
      (Real.exp_nonneg _)
  have hext :
      IntegrableOn
        (fun x : ℝ =>
          pole x * movingGaussianFilteredMode Ck R carrier x)
        (gaussianExteriorSet a) volume := by
    have htail :
        IntegrableOn
          (fun x : ℝ =>
            A * Real.exp (-R * (|x| - c) ^ 2 / 16))
          (gaussianExteriorSet a) volume :=
      (gaussianExteriorTail_integrableOn hR hc hca).const_mul A
    have hfilteredMeas :
        AEStronglyMeasurable
          (movingGaussianFilteredMode Ck R carrier) volume :=
      (movingGaussianFilteredMode_continuous
        carrier Ck hR.le).aestronglyMeasurable
    have hpairMeas :
        AEStronglyMeasurable
          (fun x : ℝ =>
            pole x * movingGaussianFilteredMode Ck R carrier x) volume :=
      hpole.pole_locallyIntegrable.aestronglyMeasurable.mul hfilteredMeas
    apply Integrable.mono htail hpairMeas.restrict
    have hextMeas : MeasurableSet (gaussianExteriorSet a) := by
      unfold gaussianExteriorSet
      exact measurableSet_Iic.union measurableSet_Ici
    filter_upwards [self_mem_ae_restrict hextMeas] with x hx
    have hxout :
        x ∉ Set.Ioo (-a) a := by
      rw [gaussianExteriorSet] at hx
      rcases hx with hxleft | hxright
      · exact fun hin => (not_lt_of_ge hxleft) hin.1
      · exact fun hin => (not_lt_of_ge hxright) hin.2
    have hbound :=
      poleFilteredMode_norm_le_radiusTail
        carrier a hca pole hpole Ck hc hR.le hlarge hxout
    have htailNonneg :
        0 ≤ A * Real.exp (-R * (|x| - c) ^ 2 / 16) :=
      mul_nonneg hA (Real.exp_nonneg _)
    rw [Real.norm_eq_abs, abs_of_nonneg htailNonneg]
    simpa [A] using hbound
  have hint :
      IntegrableOn
        (fun x : ℝ =>
          pole x * movingGaussianFilteredMode Ck R carrier x)
        (Set.Icc (-a) a) volume := by
    have hpoleInt :
        IntegrableOn pole (Set.Icc (-a) a) volume :=
      hpole.pole_locallyIntegrable.integrableOn_isCompact isCompact_Icc
    exact hpoleInt.mul_continuousOn
      (movingGaussianFilteredMode_continuous
        carrier Ck hR.le).continuousOn
      isCompact_Icc
  have hall :
      IntegrableOn
        (fun x : ℝ =>
          pole x * movingGaussianFilteredMode Ck R carrier x)
        (Set.Icc (-a) a
          ∪ gaussianExteriorSet a) volume :=
    hint.union hext
  have hunion :
      Set.Icc (-a) a
          ∪ gaussianExteriorSet a
        = Set.univ := by
    ext x
    simp [gaussianExteriorSet]
    by_cases hx : x < -a
    · right
      left
      exact le_of_lt hx
    · by_cases hx' : a < x
      · right
        right
        exact le_of_lt hx'
      · left
        exact ⟨le_of_not_gt hx, le_of_not_gt hx'⟩
  rw [hunion] at hall
  exact integrableOn_univ.mp hall


variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The actual source pole pairs with the Hermitian Gaussian using its fixed
half-rate growth and radius geometry, independently of residual growth. -/
theorem neutralWeilSourcePole_dualGaussian_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hca : c < a) (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c) (hR : 0 < R) (hlarge : 4 ≤ R*(a-c)) :
    Integrable (fun x =>
      movingGaussianFilteredModeDualTest Ck R hR carrier x *
        neutralWeilSourcePole carrier x) volume := by
  let f := movingGaussianFilteredModeSchwartz Ck R hR carrier
  have hp : Integrable (fun x => f x * neutralWeilSourcePole carrier x) volume := by
    have hrate : 8 * (neutralWeilSourcePole_growthData carrier).growthRate ≤ R*(a-c) := by
      change 8 * (1/2 : ℝ) ≤ R*(a-c)
      norm_num
      exact hlarge
    simpa only [f, movingGaussianFilteredModeSchwartz_apply, mul_comm] using
      poleFilteredMode_integrable_of_radius carrier a hca _
        (neutralWeilSourcePole_growthData carrier) Ck hc hR hrate
  exact integrable_conjugateSchwartz_mul f _
    (neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable.aestronglyMeasurable hp

/-- Exact fixed-cutoff source action, represented by an integral-growth
residual on compact tests. The Gaussian identity is not assumed as a field. -/
structure IntegralGrowthWeilWeakRealization
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (d : NeutralIntegralGrowthResidual c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise d.a) : Prop where
  compactIdentity : ∀ (u : SchwartzMap ℝ ℂ), HasCompactSupport u →
    (∫ x, u x * d.q x) =
      rightLimitWeilMultiplierCore d.a hSymbol carrier.temperedMode u +
        ∫ x, u x * neutralWeilSourcePole carrier x

/-- Derive the actual Hermitian Gaussian multiplier-plus-pole identity from
compact realization. Both product integrability obligations are proved. -/
theorem integralGrowthWeilGaussianHermitian
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (d : NeutralIntegralGrowthResidual c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise d.a)
    (hweak : IntegralGrowthWeilWeakRealization carrier d hSymbol)
    (Ck : ℂ) {R : ℝ} (hc : 0 ≤ c) (hR : 0 < R)
    (hqLarge : 8*d.rate ≤ R*(d.a-c)) (hpLarge : 4 ≤ R*(d.a-c)) :
    Integrable (fun x =>
      movingGaussianFilteredModeDualTest Ck R hR carrier x * d.q x) volume ∧
    Integrable (fun x =>
      movingGaussianFilteredModeDualTest Ck R hR carrier x *
        neutralWeilSourcePole carrier x) volume ∧
    (∫ x, movingGaussianFilteredModeDualTest Ck R hR carrier x * d.q x) =
      rightLimitWeilMultiplierCore d.a hSymbol carrier.temperedMode
        (movingGaussianFilteredModeDualTest Ck R hR carrier) +
      ∫ x, movingGaussianFilteredModeDualTest Ck R hR carrier x *
        neutralWeilSourcePole carrier x := by
  have hq : Integrable (fun x =>
      movingGaussianFilteredModeDualTest Ck R hR carrier x * d.q x) volume := by
    simpa only [movingGaussianFilteredModeDualTest_apply] using
      (integralGrowthGaussian_pairing_bound carrier d Ck R hc hR.le hqLarge).1
  have hp := neutralWeilSourcePole_dualGaussian_integrable carrier d.a d.strict Ck hc hR hpLarge
  refine ⟨hq, hp, ?_⟩
  exact integralGrowth_weakIdentity_of_integrableSchwartz
    (rightLimitWeilMultiplierCore d.a hSymbol carrier.temperedMode) d.q _
    hweak.compactIdentity (movingGaussianFilteredModeDualTest Ck R hR carrier) hq hp

end

end WeilDefect
