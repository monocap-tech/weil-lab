import WeilDefect.Morphology.NeutralGaussianCutoffPairing
import WeilDefect.Morphology.NeutralWeilPoleGrowth

namespace WeilDefect

noncomputable section

open MeasureTheory

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Assemble the explicit Schwartz test, compact cutoff sequence, and ordinary
pairing limits. The pole growth data remain an explicit input. -/
def rightLimitWeilGaussianCutoff_of_growth
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (pole : ℝ → ℂ) (hpole : NeutralPoleExponentialGrowthData pole)
    (Ck : ℂ) {R : ℝ} (hc : 0 ≤ c) (hR : 0 < R)
    (hqLarge : 8 * residual.growthRate ≤ R * (residual.a - c))
    (hpLarge : 8 * hpole.growthRate ≤ R * (residual.a - c)) :
    RightLimitWeilGaussianCutoffPremise c carrier residual pole Ck R where
  gaussianTest := movingGaussianFilteredModeSchwartz Ck R hR carrier
  gaussianTest_apply := movingGaussianFilteredModeSchwartz_apply Ck R hR carrier
  cutoff := movingGaussianFilteredModeCompactCutoff Ck R hR carrier
  cutoff_compact := movingGaussianFilteredModeCompactCutoff_compact Ck R hR carrier
  cutoff_tendsto := movingGaussianFilteredModeCompactCutoff_tendsto Ck R hR carrier
  residual_pairing_integrable := by
    simpa only [movingGaussianFilteredModeSchwartz_apply, mul_comm] using
      residualFilteredMode_integrable carrier residual Ck hc hR hqLarge
  pole_pairing_integrable := by
    simpa only [movingGaussianFilteredModeSchwartz_apply, mul_comm] using
      poleFilteredMode_integrable carrier residual pole hpole Ck hc hR hpLarge
  residual_pairing_tendsto :=
    movingGaussianFilteredModeCompactCutoff_residual_pairing_tendsto
      carrier residual Ck hc hR hqLarge
  pole_pairing_tendsto :=
    movingGaussianFilteredModeCompactCutoff_pole_pairing_tendsto
      carrier residual pole hpole Ck hc hR hpLarge

/-- The Gaussian weak identity is derived by the cutoff limit;
it is not an additional premise of this constructor. -/
def rightLimitWeilGaussianAdmissibility_of_growth
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (pole : ℝ → ℂ) (hpole : NeutralPoleExponentialGrowthData pole)
    (hEXT4 : RightLimitWeilWeakRealizationPremise c carrier residual hSymbol pole)
    (Ck : ℂ) {R : ℝ} (hc : 0 ≤ c) (hR : 0 < R)
    (hqLarge : 8 * residual.growthRate ≤ R * (residual.a - c))
    (hpLarge : 8 * hpole.growthRate ≤ R * (residual.a - c)) :
    RightLimitWeilGaussianAdmissibilityBridge c carrier residual hSymbol pole Ck R :=
  (rightLimitWeilGaussianCutoff_of_growth carrier residual pole hpole Ck
    hc hR hqLarge hpLarge).toGaussianAdmissibilityBridge hEXT4

/-- Concrete source-pole specialization. The imported compact weak identity
must identify this very pole; an arbitrary locally integrable pole is not
silently substituted. Coercivity is not asserted. -/
def rightLimitWeilGaussianAdmissibility_sourcePole
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSymbol : RightLimitWeilSymbolTemperatePremise residual.a)
    (hEXT4 : RightLimitWeilWeakRealizationPremise c carrier residual hSymbol
      (neutralWeilSourcePole carrier))
    (Ck : ℂ) {R : ℝ} (hc : 0 ≤ c) (hR : 0 < R)
    (hqLarge : 8 * residual.growthRate ≤ R * (residual.a - c))
    (hpLarge : 4 ≤ R * (residual.a - c)) :
    RightLimitWeilGaussianAdmissibilityBridge c carrier residual hSymbol
      (neutralWeilSourcePole carrier) Ck R := by
  apply rightLimitWeilGaussianAdmissibility_of_growth carrier residual hSymbol
    (neutralWeilSourcePole carrier) (neutralWeilSourcePole_growthData carrier)
    hEXT4 Ck hc hR hqLarge
  simpa [neutralWeilSourcePole_growthData, neutralWeilExponentialPole_growthData] using hpLarge

end

end WeilDefect
