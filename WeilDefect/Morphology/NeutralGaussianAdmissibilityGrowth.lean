import WeilDefect.Morphology.NeutralGaussianAdmissibility

namespace WeilDefect

noncomputable section

open MeasureTheory

/--
Source-facing growth premise for the explicit finite-dimensional pole/evaluation
component.  WD-T40 only needs that the pole has fixed exponential growth.

For the actual compact-window pole species this is supplied by the fixed span
of exp(±x/2); RPB-100 keeps that source input explicit.
-/
structure RightLimitWeilPoleExponentialGrowthPremise
    (pole : ℝ → ℂ) : Prop where
  growthConstant : ℝ
  growthRate : ℝ
  growthConstant_nonneg : 0 ≤ growthConstant
  growthRate_nonneg : 0 ≤ growthRate
  growth_bound :
    ∀ x : ℝ,
      ‖pole x‖
        ≤ growthConstant * Real.exp (growthRate * |x|)

/--
Pointwise completed-tail bound for the explicit pole paired with the actual
moving-Gaussian filtered mode.
-/
theorem poleFilteredMode_norm_le_completedTail
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (pole : ℝ → ℂ)
    (hPole : RightLimitWeilPoleExponentialGrowthPremise pole)
    (Ck : ℂ) {R x : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 ≤ R)
    (hlarge :
      8 * hPole.growthRate
        ≤ R * (residual.a - c))
    (hx : x ∉ Set.Ioo (-residual.a) residual.a) :
    ‖pole x
        * movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (hPole.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (hPole.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16))
      * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
  have hfiltered :=
    movingGaussianFilteredMode_norm_le_exteriorEnvelope
      carrier residual Ck R x hc hR hx
  have hcompletion :=
    gaussianTailCompletion_bound
      hPole.growthRate_nonneg hR hc residual.strict
      hlarge hx
  rw [norm_mul]
  calc
    ‖pole x‖
        * ‖movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (hPole.growthConstant
      * Real.exp (hPole.growthRate * |x|))
      *
    ((‖Ck‖ * Real.sqrt R
      * gaussianSupportEnvelope R c x)
      * neutralPhysicalCompactL1Mass carrier) := by
        exact mul_le_mul
          (hPole.growth_bound x)
          hfiltered
          (norm_nonneg _)
          (mul_nonneg
            hPole.growthConstant_nonneg
            (Real.exp_nonneg _))
    _ ≤
    (hPole.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (hPole.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16))
      * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
        have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
          mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
        have hnonneg :
            0 ≤ hPole.growthConstant
              * (‖Ck‖ * Real.sqrt R)
              * neutralPhysicalCompactL1Mass carrier :=
          mul_nonneg
            (mul_nonneg hPole.growthConstant_nonneg hkernel)
            (neutralPhysicalCompactL1Mass_nonneg carrier)
        nlinarith [hcompletion]

/--
The pole-filtered-mode product is integrable on the exterior once the fixed
pole growth is absorbed by the Gaussian completion.
-/
theorem poleFilteredMode_integrableOn_exterior
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (pole : ℝ → ℂ)
    (hpoleLocal : LocallyIntegrable pole volume)
    (hPole : RightLimitWeilPoleExponentialGrowthPremise pole)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge :
      8 * hPole.growthRate
        ≤ R * (residual.a - c)) :
    IntegrableOn
      (fun x : ℝ =>
        pole x
          * movingGaussianFilteredMode Ck R carrier x)
      (gaussianExteriorSet residual.a) volume := by
  let A : ℝ :=
    hPole.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (hPole.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16)
  have hA : 0 ≤ A := by
    dsimp [A]
    have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
      mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
    have h₁ :
        0 ≤ hPole.growthConstant
          * (‖Ck‖ * Real.sqrt R)
          * neutralPhysicalCompactL1Mass carrier :=
      mul_nonneg
        (mul_nonneg hPole.growthConstant_nonneg hkernel)
        (neutralPhysicalCompactL1Mass_nonneg carrier)
    exact mul_nonneg
      (mul_nonneg h₁ (Real.exp_nonneg _))
      (Real.exp_nonneg _)
  have htail :
      IntegrableOn
        (fun x : ℝ =>
          A * Real.exp (-R * (|x| - c) ^ 2 / 16))
        (gaussianExteriorSet residual.a) volume :=
    (gaussianExteriorTail_integrableOn hR hc residual.strict).const_mul A
  have hfilteredMeas :
      AEStronglyMeasurable
        (movingGaussianFilteredMode Ck R carrier) volume :=
    (movingGaussianFilteredMode_continuous
      carrier Ck hR.le).aestronglyMeasurable
  have hpairMeas :
      AEStronglyMeasurable
        (fun x : ℝ =>
          pole x
            * movingGaussianFilteredMode Ck R carrier x) volume :=
    hpoleLocal.aestronglyMeasurable.mul hfilteredMeas
  apply Integrable.mono htail hpairMeas.restrict
  have hextMeas : MeasurableSet (gaussianExteriorSet residual.a) := by
    unfold gaussianExteriorSet
    exact measurableSet_Iic.union measurableSet_Ici
  filter_upwards [self_mem_ae_restrict hextMeas] with x hx
  have hxout :
      x ∉ Set.Ioo (-residual.a) residual.a := by
    rw [gaussianExteriorSet] at hx
    rcases hx with hxleft | hxright
    · exact fun hin => (not_lt_of_ge hxleft) hin.1
    · exact fun hin => (not_lt_of_ge hxright) hin.2
  have hbound :=
    poleFilteredMode_norm_le_completedTail
      carrier residual pole hPole Ck hc hR.le hlarge hxout
  have htailNonneg :
      0 ≤ A * Real.exp (-R * (|x| - c) ^ 2 / 16) :=
    mul_nonneg hA (Real.exp_nonneg _)
  rw [Real.norm_eq_abs, abs_of_nonneg htailNonneg]
  simpa [A] using hbound

/--
The actual pole-filtered-mode product is globally integrable: local
integrability handles the compact middle interval and exponential-growth
completion handles both tails.
-/
theorem poleFilteredMode_integrable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (pole : ℝ → ℂ)
    (hpoleLocal : LocallyIntegrable pole volume)
    (hPole : RightLimitWeilPoleExponentialGrowthPremise pole)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge :
      8 * hPole.growthRate
        ≤ R * (residual.a - c)) :
    Integrable
      (fun x : ℝ =>
        pole x
          * movingGaussianFilteredMode Ck R carrier x) volume := by
  have hmiddle :
      IntegrableOn
        (fun x : ℝ =>
          pole x
            * movingGaussianFilteredMode Ck R carrier x)
        (Set.Icc (-residual.a) residual.a) volume := by
    exact
      (hpoleLocal.integrableOn_isCompact isCompact_Icc).mul_continuousOn
        (movingGaussianFilteredMode_continuous
          carrier Ck hR.le).continuousOn
        isCompact_Icc
  have hext :
      IntegrableOn
        (fun x : ℝ =>
          pole x
            * movingGaussianFilteredMode Ck R carrier x)
        (gaussianExteriorSet residual.a) volume :=
    poleFilteredMode_integrableOn_exterior
      carrier residual pole hpoleLocal hPole Ck hc hR hlarge
  have htotal :=
    hmiddle.union hext
  have hunion :
      Set.Icc (-residual.a) residual.a
          ∪ gaussianExteriorSet residual.a
        = Set.univ := by
    ext x
    simp only [Set.mem_union, Set.mem_Icc, Set.mem_univ, iff_true]
    rw [gaussianExteriorSet]
    simp only [Set.mem_union, Set.mem_Iic, Set.mem_Ici]
    by_cases hleft : x ≤ -residual.a
    · exact Or.inr (Or.inl hleft)
    · have hneg : -residual.a ≤ x :=
        le_of_lt (lt_of_not_ge hleft)
      by_cases hright : residual.a ≤ x
      · exact Or.inr (Or.inr hright)
      · have hxa : x ≤ residual.a :=
          le_of_lt (lt_of_not_ge hright)
        exact Or.inl ⟨hneg, hxa⟩
  rw [hunion] at htotal
  simpa using htotal

/--
The residual-filtered-mode product is globally integrable using the certified
a.e. vanishing on the central interval.
-/
theorem residualFilteredMode_integrable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge :
      8 * residual.growthRate
        ≤ R * (residual.a - c)) :
    Integrable
      (fun x : ℝ =>
        residual.q x
          * movingGaussianFilteredMode Ck R carrier x) volume := by
  have hext :=
    residualFilteredMode_integrableOn_exterior
      carrier residual Ck hc hR hlarge
  apply hext.integrable_of_ae_notMem_eq_zero
  filter_upwards [residual.vanishes_ae] with x hq hx
  have hin :
      x ∈ Set.Ioo (-residual.a) residual.a := by
    simp [gaussianExteriorSet] at hx
    exact ⟨hx.1, hx.2⟩
  rw [hq hin, zero_mul]

/--
The remaining genuinely nontrivial cutoff step after RPB-100.

It packages only a Schwartz realization of the actual filtered mode together
with extension of the compact-test weak identity to that realization.
Integrability is intentionally absent: RPB-100 derives it from the certified
residual growth and the explicit pole-growth premise.
-/
structure RightLimitWeilGaussianCutoffExtension
    (c : ℝ)
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (pole : ℝ → ℂ)
    (Ck : ℂ)
    (R : ℝ) where
  gaussianTest : SchwartzMap ℝ ℂ
  gaussianTest_apply :
    ∀ x : ℝ,
      gaussianTest x =
        movingGaussianFilteredMode Ck R carrier x
  gaussianWeakIdentity :
    (∫ x : ℝ,
      gaussianTest x * residual.q x ∂volume)
      =
    rightLimitWeilMultiplierCore
        residual.a hSymbol carrier.temperedMode gaussianTest
      +
    ∫ x : ℝ,
      gaussianTest x * pole x ∂volume

/--
Growth-discharge constructor for the build-certified RPB-98 admissibility
interface.

After RPB-100, the residual and pole integrability fields are no longer
independent assumptions: they are derived from the certified F-3 estimates
and the explicit pole-growth premise.  The only remaining input is the cutoff
extension itself.
-/
noncomputable def gaussianAdmissibilityOfCutoffExtension
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (pole : ℝ → ℂ)
    (compactWeak :
      RightLimitWeilWeakRealizationPremise
        c carrier residual hSymbol pole)
    (hPole : RightLimitWeilPoleExponentialGrowthPremise pole)
    (Ck : ℂ) {R : ℝ}
    (cutoff :
      RightLimitWeilGaussianCutoffExtension
        c carrier residual hSymbol pole Ck R)
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlargeResidual :
      8 * residual.growthRate
        ≤ R * (residual.a - c))
    (hlargePole :
      8 * hPole.growthRate
        ≤ R * (residual.a - c)) :
    RightLimitWeilGaussianAdmissibilityBridge
      c carrier residual hSymbol pole Ck R := by
  have hResidualRaw :
      Integrable
        (fun x : ℝ =>
          residual.q x
            * movingGaussianFilteredMode Ck R carrier x) volume :=
    residualFilteredMode_integrable
      carrier residual Ck hc hR hlargeResidual
  have hResidual :
      Integrable
        (fun x : ℝ =>
          cutoff.gaussianTest x * residual.q x) volume := by
    apply hResidualRaw.congr
    filter_upwards with x
    rw [cutoff.gaussianTest_apply x, mul_comm]
  have hPoleRaw :
      Integrable
        (fun x : ℝ =>
          pole x
            * movingGaussianFilteredMode Ck R carrier x) volume :=
    poleFilteredMode_integrable
      carrier residual pole compactWeak.pole_locallyIntegrable
      hPole Ck hc hR hlargePole
  have hPolePair :
      Integrable
        (fun x : ℝ =>
          cutoff.gaussianTest x * pole x) volume := by
    apply hPoleRaw.congr
    filter_upwards with x
    rw [cutoff.gaussianTest_apply x, mul_comm]
  exact {
    compactWeak := compactWeak
    gaussianTest := cutoff.gaussianTest
    gaussianTest_apply := cutoff.gaussianTest_apply
    residual_pairing_integrable := hResidual
    pole_pairing_integrable := hPolePair
    gaussianWeakIdentity := cutoff.gaussianWeakIdentity
  }

end

end WeilDefect
