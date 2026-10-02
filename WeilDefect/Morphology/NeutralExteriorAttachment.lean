import WeilDefect.Morphology.NeutralDigammaCancellation

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped SchwartzMap Topology

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Actual uncentered tail vanishes on support-separated Schwartz tests,
because scalar centering has exactly zero carrier action there. -/
theorem neutralShiftedDigammaAction_exterior_tendsto_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    Tendsto (fun N : ℕ => neutralShiftedDigammaAction N carrier.temperedMode u)
      atTop (𝓝 0) := by
  have h := neutralCenteredDigammaAction_tendsto_zero carrier a hSymbol u
  simpa only [neutralCenteredDigammaAction_eq_shifted_exterior carrier _ hca hSymbol u hu]
    using h

/-- Actual exterior archimedean multiplier attachment, obtained from the
certified residual cancellation and exterior-defect identity. -/
theorem neutralArchimedeanMultiplierCore_exterior_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    neutralArchimedeanMultiplierCore carrier.temperedMode u =
      ∫ x : ℝ, u x * neutralArchimedeanGapFunction carrier (a-c) x := by
  exact (neutralCenteredDigammaAction_exterior_zero_iff carrier hc hca hSymbol u hu).mp
    (neutralCenteredDigammaAction_tendsto_zero carrier a hSymbol u)

/-- The concrete exterior core pairing genuinely converges. -/
theorem neutralExteriorMultiplierCore_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) (u : SchwartzMap ℝ ℂ) :
    Integrable (fun x : ℝ => u x *
      (neutralArchimedeanGapFunction carrier (a-c) x -
        neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x)) volume := by
  simpa only [mul_sub, Pi.sub_apply] using
    (neutralArchimedeanGapFunction_pairing_integrable carrier (sub_pos.mpr hca) u).sub
      (neutralFinitePrime_pairing_integrable carrier _ u)

/-- Actual full fixed-cutoff multiplier core equals the concrete gap-minus-
prime function on exterior tests. The pole and whole-source reconstruction
are separate obligations. Existing full-symbol growth is retained. -/
theorem neutralWeilMultiplierCore_exterior_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    rightLimitWeilMultiplierCore a hSymbol carrier.temperedMode u =
      ∫ x : ℝ, u x *
        (neutralArchimedeanGapFunction carrier (a-c) x -
          neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x) := by
  rw [neutralWeilMultiplierCore_eq_archimedean_sub_prime carrier a hSymbol u,
    neutralArchimedeanMultiplierCore_exterior_pairing carrier hc hca hSymbol u hu]
  simp only [mul_sub]
  exact (integral_sub
    (neutralArchimedeanGapFunction_pairing_integrable carrier (sub_pos.mpr hca) u)
    (neutralFinitePrime_pairing_integrable carrier _ u)).symm

end

end WeilDefect
