import WeilDefect.Morphology.NeutralGaussExteriorLimit

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped Topology SchwartzMap

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The constructed signed gap function genuinely pairs with every Schwartz test. -/
theorem neutralArchimedeanGapFunction_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {δ : ℝ} (hδ : 0 < δ) (u : SchwartzMap ℝ ℂ) :
    Integrable (fun x => u x * neutralArchimedeanGapFunction carrier δ x) volume := by
  let C := (1 / (1 - Real.exp (-2*δ))) * neutralPhysicalCompactL1Mass carrier
  apply (u.integrable.norm.mul_const C).mono'
    (u.continuous.aestronglyMeasurable.mul
      (neutralArchimedeanGapFunction_continuous carrier hδ).aestronglyMeasurable)
  filter_upwards with x
  rw [norm_mul]
  exact mul_le_mul_of_nonneg_left
    (neutralArchimedeanGapFunction_norm_bound carrier hδ x) (norm_nonneg _)

/-- The uniform exterior bound passes through the actual Schwartz pairing.
Support separation is retained explicitly as central vanishing of the test. -/
theorem neutralFiniteGaussConvolution_exterior_pairing_error
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (N : ℕ) {a : ℝ} (hc : 0 ≤ c) (hca : c < a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    ‖(∫ x, u x * neutralFiniteGaussConvolution carrier N x) +
      ∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x‖ ≤
      (((1 / (1 - Real.exp (-2*(a-c)))) * (Real.exp (-2*(a-c)))^N) *
        neutralPhysicalCompactL1Mass carrier) * (∫ x : ℝ, ‖u x‖) := by
  let B := ((1 / (1 - Real.exp (-2*(a-c)))) * (Real.exp (-2*(a-c)))^N) *
    neutralPhysicalCompactL1Mass carrier
  have hδ : 0 < a-c := sub_pos.mpr hca
  have hden : 0 < 1 - Real.exp (-2*(a-c)) := by
    have h := archimedeanGapKernel_denominator_pos hδ (0 : ℝ)
    simpa [max_eq_left hδ.le] using h
  have hM : 0 ≤ neutralPhysicalCompactL1Mass carrier :=
    integral_nonneg (fun _ => norm_nonneg _)
  have hB : 0 ≤ B := by dsimp [B]; positivity
  have hf := neutralFiniteGaussConvolution_pairing_integrable carrier N u
  have hg := neutralArchimedeanGapFunction_pairing_integrable carrier hδ u
  rw [← integral_add hf hg]
  calc
    _ ≤ ∫ x : ℝ, ‖u x * neutralFiniteGaussConvolution carrier N x +
      u x * neutralArchimedeanGapFunction carrier (a-c) x‖ :=
        norm_integral_le_integral_norm _
    _ ≤ ∫ x : ℝ, B * ‖u x‖ := by
      apply integral_mono_ae (hf.add hg).norm (u.integrable.norm.const_mul B)
      filter_upwards with x
      by_cases hx : x ∈ Set.Ioo (-a) a
      · simp only [hu x hx, zero_mul, zero_add, norm_zero]
        exact mul_nonneg hB (norm_nonneg _)
      · rw [← mul_add, norm_mul]
        calc
          _ ≤ ‖u x‖ * B := mul_le_mul_of_nonneg_left
            (neutralFiniteGaussConvolution_exterior_error carrier N hc hca hx) (norm_nonneg _)
          _ = _ := by ring
    _ = _ := by rw [integral_const_mul]

/-- A genuine support-separated weak limit, derived from quantitative L1
control rather than substitution of a singular whole-line kernel. -/
theorem neutralFiniteGaussConvolution_exterior_pairing_tendsto
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    Tendsto (fun N : ℕ => ∫ x, u x * neutralFiniteGaussConvolution carrier N x) atTop
      (𝓝 (-(∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x))) := by
  have hr : Real.exp (-2*(a-c)) < 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_lt_exp.mpr
    linarith
  have hp := tendsto_pow_atTop_nhds_zero_of_lt_one (Real.exp_nonneg (-2*(a-c))) hr
  have hb : Tendsto (fun N : ℕ =>
      (((1 / (1 - Real.exp (-2*(a-c)))) * (Real.exp (-2*(a-c)))^N) *
        neutralPhysicalCompactL1Mass carrier) * (∫ x : ℝ, ‖u x‖)) atTop (𝓝 0) := by
    simpa using ((tendsto_const_nhds.mul hp).mul_const
      (neutralPhysicalCompactL1Mass carrier)).mul_const (∫ x : ℝ, ‖u x‖)
  have hn : Tendsto (fun N : ℕ =>
      ‖(∫ x, u x * neutralFiniteGaussConvolution carrier N x) +
        ∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x‖) atTop (𝓝 0) := by
    exact squeeze_zero (fun _ => norm_nonneg _) (fun N =>
      neutralFiniteGaussConvolution_exterior_pairing_error carrier N hc hca u hu) hb
  apply tendsto_iff_norm_sub_tendsto_zero.mpr
  simpa only [sub_neg_eq_add] using hn

/-- The actual shifted-tail pairing has a limit equal to the remaining
source-attachment defect. Its vanishing is not asserted. -/
theorem neutralShiftedDigammaAction_exterior_defect_tendsto
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    Tendsto (fun N : ℕ => neutralShiftedDigammaAction N carrier.temperedMode u) atTop
      (𝓝 (neutralArchimedeanMultiplierCore carrier.temperedMode u -
        ∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x)) := by
  have heq (N : ℕ) : neutralShiftedDigammaAction N carrier.temperedMode u =
      neutralArchimedeanMultiplierCore carrier.temperedMode u +
        ∫ x, u x * neutralFiniteGaussConvolution carrier N x := by
    have h := neutralArchimedeanMultiplierCore_eq_shifted_sub_convolution
      carrier N a hSymbol u
    rw [h]
    ring
  simp_rw [heq]
  simpa only [sub_eq_add_neg] using tendsto_const_nhds.add
    (neutralFiniteGaussConvolution_exterior_pairing_tendsto carrier hc hca u hu)

/-- Exact remaining analytic target: tail vanishing is equivalent to actual
archimedean attachment on this test. Neither side is supplied as a witness. -/
theorem neutralShiftedDigammaAction_exterior_zero_iff
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    Tendsto (fun N : ℕ => neutralShiftedDigammaAction N carrier.temperedMode u) atTop
        (𝓝 0) ↔
      neutralArchimedeanMultiplierCore carrier.temperedMode u =
        ∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x := by
  have h := neutralShiftedDigammaAction_exterior_defect_tendsto carrier hc hca hSymbol u hu
  constructor
  · intro hz
    exact sub_eq_zero.mp (tendsto_nhds_unique h hz)
  · intro heq
    simpa only [heq, sub_self] using h

end

end WeilDefect
