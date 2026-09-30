import WeilDefect.Morphology.NeutralGaussianPairing

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped SchwartzMap Topology

/--
F-4 domain bridge for the one noncompact test family used by WD-T40.

This structure strengthens the existing compact-test EXT-4 realization only
enough to admit the actual moving-Gaussian filtered mode.  It deliberately
contains no logarithmic coercivity or downstream Fourier-decay statement.
-/
structure RightLimitWeilGaussianAdmissibilityBridge
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
  compactWeak :
    RightLimitWeilWeakRealizationPremise
      c carrier residual hSymbol pole
  gaussianTest : SchwartzMap ℝ ℂ
  gaussianTest_apply :
    ∀ x : ℝ,
      gaussianTest x =
        movingGaussianFilteredMode Ck R carrier x
  residual_pairing_integrable :
    Integrable
      (fun x : ℝ =>
        gaussianTest x * residual.q x) volume
  pole_pairing_integrable :
    Integrable
      (fun x : ℝ =>
        gaussianTest x * pole x) volume
  gaussianWeakIdentity :
    (∫ x : ℝ,
      gaussianTest x * residual.q x ∂volume)
      =
    rightLimitWeilMultiplierCore
        residual.a hSymbol carrier.temperedMode gaussianTest
      +
    ∫ x : ℝ,
      gaussianTest x * pole x ∂volume

namespace RightLimitWeilGaussianAdmissibilityBridge

variable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    {carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs}
    {residual : NeutralExponentialResidualCarrier c}
    {hSymbol : RightLimitWeilSymbolTemperatePremise residual.a}
    {pole : ℝ → ℂ}
    {Ck : ℂ}
    {R : ℝ}

/--
The physical F-3 pairing is exactly the left-hand side of the admissible
Gaussian weak identity.
-/
theorem movingGaussianResidualPairing_eq_weakLeft
    (d :
      RightLimitWeilGaussianAdmissibilityBridge
        c carrier residual hSymbol pole Ck R) :
    movingGaussianResidualPairing carrier residual Ck R
      =
    ∫ x : ℝ,
      d.gaussianTest x * residual.q x ∂volume := by
  unfold movingGaussianResidualPairing
  apply integral_congr_ae
  filter_upwards with x
  rw [d.gaussianTest_apply x]
  exact mul_comm _ _

/--
Typed F-4 domain bridge.

It exposes the two required integrability statements and transfers the
compact-test EXT-4 realization to the actual moving-Gaussian test without
asserting any coercive estimate.
-/
theorem gaussianWeakRealization
    (d :
      RightLimitWeilGaussianAdmissibilityBridge
        c carrier residual hSymbol pole Ck R) :
    Integrable
        (fun x : ℝ =>
          d.gaussianTest x * residual.q x) volume
      ∧
    Integrable
        (fun x : ℝ =>
          d.gaussianTest x * pole x) volume
      ∧
    movingGaussianResidualPairing carrier residual Ck R
      =
    rightLimitWeilMultiplierCore
        residual.a hSymbol carrier.temperedMode d.gaussianTest
      +
    ∫ x : ℝ,
      d.gaussianTest x * pole x ∂volume := by
  refine ⟨d.residual_pairing_integrable, d.pole_pairing_integrable, ?_⟩
  rw [d.movingGaussianResidualPairing_eq_weakLeft]
  exact d.gaussianWeakIdentity

/--
Forget Gaussian admissibility and recover the already-certified compact-test
EXT-4 realization premise.
-/
def toCompactWeak
    (d :
      RightLimitWeilGaussianAdmissibilityBridge
        c carrier residual hSymbol pole Ck R) :
    RightLimitWeilWeakRealizationPremise
      c carrier residual hSymbol pole :=
  d.compactWeak

end RightLimitWeilGaussianAdmissibilityBridge


/--
Cutoff package sufficient to derive Gaussian admissibility from the existing
compact-test EXT-4 realization.

The only noncompact identity is obtained as a limit of compactly supported
Schwartz tests; it is not stored as an assumption here.
-/
structure RightLimitWeilGaussianCutoffPremise
    (c : ℝ)
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (pole : ℝ → ℂ)
    (Ck : ℂ)
    (R : ℝ) where
  gaussianTest : SchwartzMap ℝ ℂ
  gaussianTest_apply :
    ∀ x : ℝ,
      gaussianTest x =
        movingGaussianFilteredMode Ck R carrier x
  cutoff : ℕ → SchwartzMap ℝ ℂ
  cutoff_compact :
    ∀ n : ℕ, HasCompactSupport (cutoff n)
  cutoff_tendsto :
    Tendsto cutoff atTop (𝓝 gaussianTest)
  residual_pairing_integrable :
    Integrable
      (fun x : ℝ =>
        gaussianTest x * residual.q x) volume
  pole_pairing_integrable :
    Integrable
      (fun x : ℝ =>
        gaussianTest x * pole x) volume
  residual_pairing_tendsto :
    Tendsto
      (fun n : ℕ =>
        ∫ x : ℝ, cutoff n x * residual.q x ∂volume)
      atTop
      (𝓝
        (∫ x : ℝ,
          gaussianTest x * residual.q x ∂volume))
  pole_pairing_tendsto :
    Tendsto
      (fun n : ℕ =>
        ∫ x : ℝ, cutoff n x * pole x ∂volume)
      atTop
      (𝓝
        (∫ x : ℝ,
          gaussianTest x * pole x ∂volume))

namespace RightLimitWeilGaussianCutoffPremise

variable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    {carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs}
    {residual : NeutralExponentialResidualCarrier c}
    {hSymbol : RightLimitWeilSymbolTemperatePremise residual.a}
    {pole : ℝ → ℂ}
    {Ck : ℂ}
    {R : ℝ}

/--
Termwise compact-test EXT-4 plus cutoff convergence imply the weak identity
for the actual moving-Gaussian test.

The multiplier-core limit is internal: tempered distributions are continuous
linear functionals on Schwartz space.
-/
theorem gaussianWeakIdentity_of_cutoff
    (hcompact :
      RightLimitWeilWeakRealizationPremise
        c carrier residual hSymbol pole)
    (d :
      RightLimitWeilGaussianCutoffPremise
        c carrier residual pole Ck R) :
    (∫ x : ℝ,
      d.gaussianTest x * residual.q x ∂volume)
      =
    rightLimitWeilMultiplierCore
        residual.a hSymbol carrier.temperedMode d.gaussianTest
      +
    ∫ x : ℝ,
      d.gaussianTest x * pole x ∂volume := by
  let core :=
    rightLimitWeilMultiplierCore
      residual.a hSymbol carrier.temperedMode
  have hcore :
      Tendsto
        (fun n : ℕ => core (d.cutoff n))
        atTop
        (𝓝 (core d.gaussianTest)) :=
    core.continuous.continuousAt.tendsto.comp d.cutoff_tendsto
  have hright :
      Tendsto
        (fun n : ℕ =>
          core (d.cutoff n)
            + ∫ x : ℝ, d.cutoff n x * pole x ∂volume)
        atTop
        (𝓝
          (core d.gaussianTest
            + ∫ x : ℝ,
                d.gaussianTest x * pole x ∂volume)) :=
    hcore.add d.pole_pairing_tendsto
  have hleft :
      Tendsto
        (fun n : ℕ =>
          ∫ x : ℝ, d.cutoff n x * residual.q x ∂volume)
        atTop
        (𝓝
          (core d.gaussianTest
            + ∫ x : ℝ,
                d.gaussianTest x * pole x ∂volume)) := by
    refine hright.congr' ?_
    exact Eventually.of_forall fun n =>
      (hcompact.weakIdentity
        (d.cutoff n) (d.cutoff_compact n)).symm
  exact tendsto_nhds_unique
    d.residual_pairing_tendsto hleft

/--
Construct the build-certified Gaussian-admissibility bridge from compact EXT-4
and a cutoff package.

No coercive estimate is introduced here.
-/
noncomputable def toGaussianAdmissibilityBridge
    (hcompact :
      RightLimitWeilWeakRealizationPremise
        c carrier residual hSymbol pole)
    (d :
      RightLimitWeilGaussianCutoffPremise
        c carrier residual pole Ck R) :
    RightLimitWeilGaussianAdmissibilityBridge
      c carrier residual hSymbol pole Ck R := {
  compactWeak := hcompact
  gaussianTest := d.gaussianTest
  gaussianTest_apply := d.gaussianTest_apply
  residual_pairing_integrable := d.residual_pairing_integrable
  pole_pairing_integrable := d.pole_pairing_integrable
  gaussianWeakIdentity :=
    gaussianWeakIdentity_of_cutoff hcompact d
}

end RightLimitWeilGaussianCutoffPremise

end

end WeilDefect
