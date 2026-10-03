import WeilDefect.Morphology.NeutralSourceBoundaryRemoval
import Mathlib.Analysis.Calculus.BumpFunction.InnerProduct

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped SchwartzMap ContDiff

/-- Temperate growth at an auxiliary radius follows from the actual retained
symbol and the already certified finite prime growth. -/
theorem neutralWeilSymbolTemperate_at_radius
    {a : ℝ} (ha : RightLimitWeilSymbolTemperatePremise a) (b : ℝ) :
    RightLimitWeilSymbolTemperatePremise b := by
  refine ⟨?_⟩
  have heq :
      (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib b ξ : ℂ)) =
        (fun ξ : ℝ => (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ)) -
          (fun ξ : ℝ => (neutralFinitePrimeSymbol (rightLimitPrimePowerFinset b) ξ : ℂ)) := by
    rw [neutralArchimedeanSymbol_eq_core_add_prime b]
    exact (add_sub_cancel_right _ _).symm
  rw [heq]
  exact (neutralArchimedeanSymbol_temperate a ha).sub
    (neutralFinitePrimeSymbol_temperate _)

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The auxiliary gap changes only the archimedean continuation. The full
prime cutoff remains the target radius a. -/
def neutralInnerCollarResidual
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a b : ℝ) (x : ℝ) : ℂ :=
  neutralArchimedeanGapFunction carrier (b-c) x -
    neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x +
      neutralWeilSourcePole carrier x

theorem neutralInnerCollarResidual_locallyIntegrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) {b : ℝ} (hcb : c < b) :
    LocallyIntegrable (neutralInnerCollarResidual carrier a b) volume :=
  ((neutralArchimedeanGapFunction_continuous carrier
    (sub_pos.mpr hcb)).locallyIntegrable.sub
    (neutralFinitePrimePhysical_locallyIntegrable carrier _)).add
      (neutralWeilSourcePole_growthData carrier).pole_locallyIntegrable

/-- Actual fixed-cutoff source pairing outside the inner radius. No spectral
operator-domain membership or representation premise is supplied. -/
theorem neutralInnerCollarResidual_exterior_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b : ℝ} (hc : 0 ≤ c) (hcb : c < b)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u)
    (hext : ∀ x ∈ Set.Ioo (-b) b, u x = 0) :
    frozenWeilCompactAction carrier a ha u hu =
      ∫ x : ℝ, u x * neutralInnerCollarResidual carrier a b x := by
  unfold frozenWeilCompactAction
  rw [neutralWeilMultiplierCore_eq_archimedean_sub_prime carrier a ha u,
    neutralArchimedeanMultiplierCore_exterior_pairing carrier hc hcb
      (neutralWeilSymbolTemperate_at_radius ha b) u hext]
  have hg := neutralArchimedeanGapFunction_pairing_integrable carrier
    (sub_pos.mpr hcb) u
  have hp := neutralFinitePrime_pairing_integrable carrier
    (rightLimitPrimePowerFinset a) u
  have hq := frozenWeilCompactAction_pole_integrable carrier u hu
  rw [← integral_sub hg hp]
  calc
    _ = ∫ x : ℝ, (u x * neutralArchimedeanGapFunction carrier (b-c) x -
        u x * neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x) +
          u x * neutralWeilSourcePole carrier x := by
      simpa only [Pi.sub_apply, Pi.add_apply] using (integral_add (hg.sub hp) hq).symm
    _ = _ := by
      apply integral_congr_ae
      filter_upwards [] with x
      unfold neutralInnerCollarResidual
      ring

/-- Actual central cancellation proves compatibility of the constructed
collar function with zero on the open overlap. -/
theorem neutralInnerCollarResidual_overlap_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b : ℝ} (hc : 0 ≤ c) (hcb : c < b)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a →
        frozenWeilCompactAction carrier a ha u hu = 0) :
    ∀ᵐ x ∂volume, x ∈ Set.Ioo (-a) a ∩ (Set.Icc (-b) b)ᶜ →
      neutralInnerCollarResidual carrier a b x = 0 := by
  apply locallyIntegrable_ae_zero_of_compactSchwartz_on_open
    (neutralInnerCollarResidual_locallyIntegrable carrier a hcb)
    (isOpen_Ioo.inter isClosed_Icc.isOpen_compl)
  intro u hu hs
  rw [← neutralInnerCollarResidual_exterior_pairing carrier hc hcb ha u hu
    (by
      intro x hx
      apply image_eq_zero_of_notMem_tsupport
      intro hxs
      exact (hs hxs).2 ⟨hx.1.le, hx.2.le⟩)]
  exact hcentral u hu (hs.trans Set.inter_subset_left)

/-- Outside the target window both gap truncations agree with the same
certified off-diagonal kernel. The prime and pole terms are unchanged. -/
theorem neutralInnerCollarResidual_eq_candidate_exterior
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b x : ℝ} (hc : 0 ≤ c) (hcb : c < b) (hba : b < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    neutralInnerCollarResidual carrier a b x =
      neutralExteriorResidualCandidate carrier a x := by
  have hxb : x ∉ Set.Ioo (-b) b := by
    intro h
    exact hx ⟨by linarith [h.1], by linarith [h.2]⟩
  rw [neutralExteriorResidualCandidate_eq_exterior carrier hx]
  unfold neutralInnerCollarResidual neutralExteriorResidualIngredients
  rw [neutralArchimedeanGapFunction_eq_exteriorFormula carrier hc hcb hxb,
    neutralArchimedeanGapFunction_eq_exteriorFormula carrier hc (hcb.trans hba) hx]

/-- Central cancellation makes the actual collar and the existing concrete
candidate agree almost everywhere outside the inner closed interval. -/
theorem neutralInnerCollarResidual_ae_eq_candidate
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b : ℝ} (hc : 0 ≤ c) (hcb : c < b) (hba : b < a)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a →
        frozenWeilCompactAction carrier a ha u hu = 0) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-b) b →
      neutralInnerCollarResidual carrier a b x =
        neutralExteriorResidualCandidate carrier a x := by
  filter_upwards [neutralInnerCollarResidual_overlap_zero carrier hc hcb ha hcentral]
    with x hzero hx
  by_cases hxa : x ∈ Set.Ioo (-a) a
  · rw [hzero ⟨hxa, hx⟩, neutralExteriorResidualCandidate_zero carrier hxa]
  · exact neutralInnerCollarResidual_eq_candidate_exterior carrier hc hcb hba hxa

/-- Every compact test is realized by the actual concrete residual once
actual central cancellation is attached. The regularity witness is derived
from the strict support margin, with no spectral L2 premise. -/
theorem neutralExteriorResidualCandidate_represents_of_central
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a →
        frozenWeilCompactAction carrier a ha u hu = 0)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    (∫ x : ℝ, u x * neutralExteriorResidualCandidate carrier a x) =
      frozenWeilCompactAction carrier a ha u hu := by
  let b : ℝ := (c+a)/2
  let d : ℝ := (b+a)/2
  have hcb : c < b := by dsimp [b]; linarith
  have hba : b < a := by dsimp [b]; linarith
  have hb : 0 < b := lt_of_le_of_lt hc hcb
  have hbd : b < d := by dsimp [d]; linarith
  have hda : d < a := by dsimp [d]; linarith
  let χ : ContDiffBump (0 : ℝ) :=
    { rIn := b, rOut := d, rIn_pos := hb, rIn_lt_rOut := hbd }
  have hwc : HasCompactSupport (fun x : ℝ => (χ x : ℂ) * u x) :=
    hu.mul_left
  have hwd : ContDiff ℝ ∞ (fun x : ℝ => (χ x : ℂ) * u x) :=
    (Complex.ofRealCLM.contDiff.comp χ.contDiff).mul (u.smooth ⊤)
  let w : SchwartzMap ℝ ℂ := hwc.toSchwartzMap hwd
  have hw : HasCompactSupport w := hwc
  have hws : tsupport w ⊆ Set.Ioo (-a) a := by
    have hs : tsupport w ⊆ tsupport (χ : ℝ → ℝ) := by
      have hsc : tsupport (Complex.ofRealCLM ∘ (χ : ℝ → ℝ)) ⊆
          tsupport (χ : ℝ → ℝ) := tsupport_comp_subset rfl _
      exact tsupport_mul_subset_left.trans hsc
    intro x hx
    have hdist : |x| ≤ d := by
      have hm := hs hx
      rw [χ.tsupport_eq] at hm
      simpa only [Metric.mem_closedBall, dist_zero_right, Real.norm_eq_abs] using hm
    have hx' := abs_le.mp hdist
    exact ⟨by linarith [hx'.1], by linarith [hx'.2]⟩
  let v : SchwartzMap ℝ ℂ := u-w
  have hv : HasCompactSupport v := hu.sub hw
  have hvzero : ∀ x ∈ Set.Icc (-b) b, v x = 0 := by
    intro x hx
    have hone : χ x = 1 := by
      apply χ.one_of_mem_closedBall
      simpa only [Metric.mem_closedBall, dist_zero_right, Real.norm_eq_abs] using
        abs_le.mpr hx
    change u x - (χ x : ℂ) * u x = 0
    rw [hone]
    simp
  have hve : ∀ x ∈ Set.Ioo (-b) b, v x = 0 :=
    fun x hx => hvzero x ⟨hx.1.le, hx.2.le⟩
  have hav := neutralInnerCollarResidual_exterior_pairing carrier hc hcb ha v hv hve
  have hiv :
      (∫ x : ℝ, v x * neutralInnerCollarResidual carrier a b x) =
        ∫ x : ℝ, v x * neutralExteriorResidualCandidate carrier a x := by
    apply integral_congr_ae
    filter_upwards [neutralInnerCollarResidual_ae_eq_candidate carrier hc hcb hba
      ha hcentral] with x heq
    by_cases hx : x ∈ Set.Icc (-b) b
    · rw [hvzero x hx, zero_mul, zero_mul]
    · rw [heq hx]
  have hiw : (∫ x : ℝ, w x * neutralExteriorResidualCandidate carrier a x) = 0 := by
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    change w x * neutralExteriorResidualCandidate carrier a x = (0 : ℂ)
    by_cases hx : w x = 0
    · rw [hx, zero_mul]
    · rw [neutralExteriorResidualCandidate_zero carrier
        (hws (subset_tsupport w hx)), mul_zero]
  have huw : w + v = u := by dsimp [v]; abel
  have hadd : frozenWeilCompactAction carrier a ha u hu =
      frozenWeilCompactAction carrier a ha w hw + frozenWeilCompactAction carrier a ha v hv := by
    simpa only [huw] using frozenWeilCompactAction_add carrier a ha w v hw hv
  rw [hcentral w hw hws, zero_add, hav, hiv] at hadd
  conv_lhs => rw [← huw]
  calc
    _ = (∫ x : ℝ, w x * neutralExteriorResidualCandidate carrier a x) +
        ∫ x : ℝ, v x * neutralExteriorResidualCandidate carrier a x := by
      simp only [SchwartzMap.add_apply, add_mul]
      exact integral_add
        (neutralExteriorResidualCandidate_compact_pairing_integrable carrier hca w hw)
        (neutralExteriorResidualCandidate_compact_pairing_integrable carrier hca v hv)
    _ = _ := by rw [hiw, zero_add]; exact hadd.symm

/-- The zero function represents the actual source defect, proved from
central cancellation rather than supplied as an independent regularity input. -/
theorem neutralCompactSourceDefect_zero_of_central
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a →
        frozenWeilCompactAction carrier a ha u hu = 0)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    neutralCompactSourceDefect carrier a ha u hu = 0 := by
  unfold neutralCompactSourceDefect
  rw [neutralExteriorResidualCandidate_represents_of_central carrier hc hca ha hcentral u hu]
  exact sub_self _

/-- Consume the already certified boundary-removal theorem immediately with
the constructed zero actual defect. Central cancellation remains explicit. -/
theorem neutralExteriorIntegralGrowthResidual_realizes_of_central
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hcentral : ∀ (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      tsupport u ⊆ Set.Ioo (-a) a →
        frozenWeilCompactAction carrier a ha u hu = 0) :
    IntegralGrowthWeilWeakRealization carrier
      (neutralExteriorIntegralGrowthResidual carrier hca) ha := by
  apply neutralExteriorIntegralGrowthResidual_realizes_of_regular_cancellation
    carrier hc hca ha (q := fun _ => 0) (continuous_const.locallyIntegrable : LocallyIntegrable (fun _ : ℝ => (0 : ℂ)) volume)
  · intro u hu
    rw [neutralCompactSourceDefect_zero_of_central carrier hc hca ha hcentral u hu]
    simp
  · exact hcentral

end

end WeilDefect
