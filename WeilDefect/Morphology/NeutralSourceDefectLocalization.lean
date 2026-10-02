import WeilDefect.Morphology.NeutralExteriorSourceAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The actual remaining compact-test defect, with the corrected source action
and the concrete locally integrable exterior candidate kept distinct. -/
def neutralCompactSourceDefect
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) : ℂ :=
  frozenWeilCompactAction carrier a hSymbol u hu -
    ∫ x : ℝ, u x * neutralExteriorResidualCandidate carrier a x

/-- Genuine compact-test integrability of the candidate. -/
theorem neutralExteriorResidualCandidate_compact_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    Integrable (fun x : ℝ => u x * neutralExteriorResidualCandidate carrier a x)
      volume :=
  compactSchwartz_mul_locallyIntegrable u hu _
    (neutralExteriorResidualCandidate_locallyIntegrable carrier hca)

theorem neutralCompactSourceDefect_add
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u v : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) (hv : HasCompactSupport v) :
    neutralCompactSourceDefect carrier a hSymbol (u + v) (hu.add hv) =
      neutralCompactSourceDefect carrier a hSymbol u hu +
      neutralCompactSourceDefect carrier a hSymbol v hv := by
  unfold neutralCompactSourceDefect
  rw [frozenWeilCompactAction_add carrier a hSymbol u v hu hv]
  simp only [SchwartzMap.add_apply, add_mul]
  rw [integral_add
    (neutralExteriorResidualCandidate_compact_pairing_integrable carrier hca u hu)
    (neutralExteriorResidualCandidate_compact_pairing_integrable carrier hca v hv)]
  ring

/-- The actual defect vanishes on every compact exterior test. -/
theorem neutralCompactSourceDefect_exterior_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u)
    (hext : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    neutralCompactSourceDefect carrier a hSymbol u hu = 0 := by
  unfold neutralCompactSourceDefect
  rw [neutralExteriorResidualCandidate_exterior_represents carrier hc hca hSymbol u hu hext]
  exact sub_self _

/-- The defect depends only on the restriction of a compact test to the
central open window. This does not exclude distributions at its boundary. -/
theorem neutralCompactSourceDefect_eq_of_central_eq
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u v : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) (hv : HasCompactSupport v)
    (heq : ∀ x ∈ Set.Ioo (-a) a, u x = v x) :
    neutralCompactSourceDefect carrier a hSymbol u hu =
      neutralCompactSourceDefect carrier a hSymbol v hv := by
  have hw : HasCompactSupport (u - v) := hu.sub hv
  have hz := neutralCompactSourceDefect_exterior_zero carrier hc hca hSymbol
    (u - v) hw (by intro x hx; simp only [SchwartzMap.sub_apply, heq x hx, sub_self])
  have hadd := neutralCompactSourceDefect_add carrier hca hSymbol (u - v) v hw hv
  simpa only [sub_add_cancel, hz, zero_add] using hadd

/-- On a central test, the exterior candidate contributes zero. Central
cancellation is therefore exactly cancellation of the actual source action. -/
theorem neutralCompactSourceDefect_central_eq_action
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u)
    (hcentral : Function.support u ⊆ Set.Ioo (-a) a) :
    neutralCompactSourceDefect carrier a hSymbol u hu =
      frozenWeilCompactAction carrier a hSymbol u hu := by
  have hz : (∫ x : ℝ, u x * neutralExteriorResidualCandidate carrier a x) = 0 := by
    have hfun : (fun x : ℝ => u x * neutralExteriorResidualCandidate carrier a x) =
        fun _ => 0 := by
      funext x
      by_cases hx : u x = 0
      · rw [hx, zero_mul]
      · rw [neutralExteriorResidualCandidate_zero carrier (hcentral hx), mul_zero]
    rw [hfun]
    simp
  simp only [neutralCompactSourceDefect, hz, sub_zero]

end

end WeilDefect
