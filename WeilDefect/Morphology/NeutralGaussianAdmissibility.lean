import WeilDefect.Morphology.NeutralGaussianPairing

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap

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

end

end WeilDefect
