import WeilDefect.Morphology.NeutralExteriorAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Actual exterior source ingredients, including the physical pole, pair
integrably with every compact Schwartz test. -/
theorem neutralExteriorResidualIngredients_compact_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    Integrable (fun x : ℝ => u x * neutralExteriorResidualIngredients carrier a x)
      volume :=
  compactSchwartz_mul_locallyIntegrable u hu _
    (neutralExteriorResidualIngredients_locallyIntegrable carrier hca)

/-- The zero continuation has exactly the same pairing on exterior tests;
the test itself annihilates every central modification. -/
theorem neutralExteriorResidualCandidate_pairing_eq_ingredients
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    (∫ x : ℝ, u x * neutralExteriorResidualCandidate carrier a x) =
      ∫ x : ℝ, u x * neutralExteriorResidualIngredients carrier a x := by
  apply integral_congr_ae
  filter_upwards with x
  by_cases hx : x ∈ Set.Ioo (-a) a
  · rw [hu x hx, zero_mul, zero_mul]
  · rw [neutralExteriorResidualCandidate_eq_exterior carrier hx]

/-- Add the actual integrable pole to the certified exterior multiplier
attachment, obtaining the frozen corrected source action. -/
theorem frozenWeilCompactAction_exterior_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (huCompact : HasCompactSupport u)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    frozenWeilCompactAction carrier a hSymbol u huCompact =
      ∫ x : ℝ, u x * neutralExteriorResidualIngredients carrier a x := by
  unfold frozenWeilCompactAction
  rw [neutralWeilMultiplierCore_exterior_pairing carrier hc hca hSymbol u hu]
  rw [← integral_add (neutralExteriorMultiplierCore_pairing_integrable carrier hca u)
    (frozenWeilCompactAction_pole_integrable carrier u huCompact)]
  apply integral_congr_ae
  filter_upwards with x
  unfold neutralExteriorResidualIngredients
  ring

/-- Actual compact exterior realization by the existing zero-continued
residual candidate. Whole compact weak realization remains separate. -/
theorem neutralExteriorResidualCandidate_exterior_represents
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (huCompact : HasCompactSupport u)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    (∫ x : ℝ, u x * neutralExteriorResidualCandidate carrier a x) =
      frozenWeilCompactAction carrier a hSymbol u huCompact := by
  rw [neutralExteriorResidualCandidate_pairing_eq_ingredients carrier a u hu]
  exact (frozenWeilCompactAction_exterior_pairing carrier hc hca hSymbol u huCompact hu).symm

end

end WeilDefect
