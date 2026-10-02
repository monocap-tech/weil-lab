import WeilDefect.Morphology.NeutralSourceDefectLocalization
import WeilDefect.Morphology.NeutralIntegralGrowthWeilIdentity
import Mathlib.Analysis.Distribution.AEEqOfIntegralContDiff

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap ContDiff

/-- Compact complex Schwartz tests detect a locally integrable function on
an open set, by the smooth compact-test fundamental lemma. -/
theorem locallyIntegrable_ae_zero_of_compactSchwartz_on_open
    {q : ℝ → ℂ} (hq : LocallyIntegrable q volume)
    {U : Set ℝ} (hU : IsOpen U)
    (hzero : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ U → (∫ x : ℝ, u x * q x) = 0) :
    ∀ᵐ x ∂volume, x ∈ U → q x = 0 := by
  apply hU.ae_eq_zero_of_integral_contDiff_smul_eq_zero (hq.locallyIntegrableOn U)
  intro g hg hgc hgs
  let gc : ℝ → ℂ := Complex.ofRealCLM ∘ g
  have hc : HasCompactSupport gc := hgc.comp_left rfl
  have hd : ContDiff ℝ ∞ gc := Complex.ofRealCLM.contDiff.comp hg
  let u : SchwartzMap ℝ ℂ := hc.toSchwartzMap hd
  have hu : HasCompactSupport u := hc
  have hs : tsupport u ⊆ U := (tsupport_comp_subset rfl g).trans hgs
  have hz := hzero u hu hs
  change (∫ x : ℝ, (g x : ℂ) * q x) = 0 at hz
  simpa only [Complex.real_smul] using hz

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Exterior attachment forces every locally integrable representative of
the actual defect to vanish almost everywhere outside the closed window. -/
theorem neutralCompactSourceDefect_regular_exterior_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    {q : ℝ → ℂ} (hq : LocallyIntegrable q volume)
    (hrep : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      (∫ x : ℝ, u x * q x) = neutralCompactSourceDefect carrier a hSymbol u hu) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → q x = 0 := by
  apply locallyIntegrable_ae_zero_of_compactSchwartz_on_open hq isClosed_Icc.isOpen_compl
  intro u hu hs
  rw [hrep u hu]
  apply neutralCompactSourceDefect_exterior_zero carrier hc hca hSymbol u hu
  intro x hx
  apply image_eq_zero_of_notMem_tsupport
  intro hxs
  exact hs hxs ⟨hx.1.le, hx.2.le⟩

/-- Actual central source cancellation transfers to an almost-everywhere
statement only after a genuine regular defect representative is supplied. -/
theorem neutralCompactSourceDefect_regular_central_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    {q : ℝ → ℂ} (hq : LocallyIntegrable q volume)
    (hrep : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      (∫ x : ℝ, u x * q x) = neutralCompactSourceDefect carrier a hSymbol u hu)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a → frozenWeilCompactAction carrier a hSymbol u hu = 0) :
    ∀ᵐ x ∂volume, x ∈ Set.Ioo (-a) a → q x = 0 := by
  apply locallyIntegrable_ae_zero_of_compactSchwartz_on_open hq isOpen_Ioo
  intro u hu hs
  rw [hrep u hu, neutralCompactSourceDefect_central_eq_action carrier a hSymbol u hu
    (subset_tsupport u |>.trans hs)]
  exact hcentral u hu hs

/-- A regular actual defect has no surviving boundary contribution once
central cancellation is supplied: the two endpoints are volume-null. -/
theorem neutralCompactSourceDefect_zero_of_regular_central_cancellation
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    {q : ℝ → ℂ} (hq : LocallyIntegrable q volume)
    (hrep : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      (∫ x : ℝ, u x * q x) = neutralCompactSourceDefect carrier a hSymbol u hu)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a → frozenWeilCompactAction carrier a hSymbol u hu = 0)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    neutralCompactSourceDefect carrier a hSymbol u hu = 0 := by
  have he := neutralCompactSourceDefect_regular_exterior_zero carrier hc hca hSymbol hq hrep
  have hi := neutralCompactSourceDefect_regular_central_zero carrier a hSymbol hq hrep hcentral
  have hz : ∀ᵐ x ∂volume, q x = 0 := by
    filter_upwards [he, hi, volume.ae_ne (-a), volume.ae_ne a] with x hxe hxi hxl hxr
    by_cases hx : x ∈ Set.Icc (-a) a
    · exact hxi ⟨lt_of_le_of_ne hx.1 (Ne.symm hxl), lt_of_le_of_ne hx.2 hxr⟩
    · exact hxe hx
  rw [← hrep u hu]
  calc
    (∫ x : ℝ, u x * q x) = ∫ _x : ℝ, (0 : ℂ) := by
      apply integral_congr_ae
      filter_upwards [hz] with x hx
      rw [hx, mul_zero]
    _ = 0 := by simp

/-- Whole compact weak realization follows from central cancellation plus
regularity of the actual defect. Neither missing witness is manufactured. -/
theorem neutralExteriorIntegralGrowthResidual_realizes_of_regular_cancellation
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    {q : ℝ → ℂ} (hq : LocallyIntegrable q volume)
    (hrep : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      (∫ x : ℝ, u x * q x) = neutralCompactSourceDefect carrier a hSymbol u hu)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a → frozenWeilCompactAction carrier a hSymbol u hu = 0) :
    IntegralGrowthWeilWeakRealization carrier
      (neutralExteriorIntegralGrowthResidual carrier hca) hSymbol := by
  constructor
  intro u hu
  have hz := neutralCompactSourceDefect_zero_of_regular_central_cancellation
    carrier hc hca hSymbol hq hrep hcentral u hu
  exact (sub_eq_zero.mp hz).symm

end

end WeilDefect
