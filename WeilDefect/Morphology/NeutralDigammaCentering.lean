import WeilDefect.Morphology.NeutralDigammaRealBounds

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped FourierTransform SchwartzMap Topology

/-- Actual shifted symbol with precisely its zero-frequency scalar removed. -/
def neutralCenteredDigammaSymbol (N : ℕ) (ξ : ℝ) : ℂ :=
  neutralShiftedDigammaSymbol N ξ - neutralShiftedDigammaSymbol N 0

theorem neutralCenteredDigammaSymbol_temperate (N : ℕ) (a : ℝ)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) :
    Function.HasTemperateGrowth (neutralCenteredDigammaSymbol N) := by
  have heq : neutralCenteredDigammaSymbol N =
      neutralShiftedDigammaSymbol N + (fun _ : ℝ => -neutralShiftedDigammaSymbol N 0) := by
    ext ξ
    simp [neutralCenteredDigammaSymbol, sub_eq_add_neg]
  rw [heq]
  exact (neutralShiftedDigammaSymbol_temperate N a hSymbol).add (by fun_prop)

/-- General scalar subtraction law in the existing tempered action. -/
theorem neutralFourierMultiplier_sub_const_pairing
    {m : ℝ → ℂ} (hm : Function.HasTemperateGrowth m)
    (k : ℂ) (f : RealComplexTempered) (u : SchwartzMap ℝ ℂ) :
    TemperedDistribution.fourierMultiplierCLM ℂ (fun ξ => m ξ - k) f u =
      TemperedDistribution.fourierMultiplierCLM ℂ m f u - k * f u := by
  have hc : Function.HasTemperateGrowth (fun _ : ℝ => -k) := by fun_prop
  have heq : (fun ξ : ℝ => m ξ - k) = m + (fun _ : ℝ => -k) := by
    ext ξ
    simp [sub_eq_add_neg]
  have hadd : TemperedDistribution.fourierMultiplierCLM ℂ
      (m + (fun _ : ℝ => -k)) f u =
      TemperedDistribution.fourierMultiplierCLM ℂ m f u +
        TemperedDistribution.fourierMultiplierCLM ℂ (fun _ : ℝ => -k) f u := by
    simp only [TemperedDistribution.fourierMultiplierCLM_apply_apply,
      SchwartzMap.smulLeftCLM_add hm hc, ContinuousLinearMap.add_apply,
      FourierTransform.fourier_add, map_add]
  rw [heq, hadd, TemperedDistribution.fourierMultiplierCLM_const]
  simp [smul_eq_mul, sub_eq_add_neg]

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Support separation annihilates the actual carrier distribution itself,
not the unidentified archimedean residual. -/
theorem neutralPhysical_temperedMode_exterior_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c < a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) : carrier.temperedMode u = 0 := by
  rw [neutralPhysical_temperedMode_apply]
  apply integral_eq_zero_of_ae
  filter_upwards with x
  by_cases hx : x ∈ Set.Icc (-c) c
  · have hxa : x ∈ Set.Ioo (-a) a := by
      rcases hx with ⟨hl, hr⟩
      constructor <;> linarith
    rw [hu x hxa, zero_mul]
  · rw [carrier.representative_eq_zero_of_not_mem hx, mul_zero]

/-- Centering removes the actual scalar contact action exactly on separated
tests. No estimate of the frequency-dependent remainder is assumed. -/
theorem neutralCenteredDigammaAction_eq_shifted_exterior
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (N : ℕ) {a : ℝ} (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    TemperedDistribution.fourierMultiplierCLM ℂ (neutralCenteredDigammaSymbol N)
        carrier.temperedMode u = neutralShiftedDigammaAction N carrier.temperedMode u := by
  unfold neutralCenteredDigammaSymbol neutralShiftedDigammaAction
  rw [neutralFourierMultiplier_sub_const_pairing
    (neutralShiftedDigammaSymbol_temperate N a hSymbol),
    neutralPhysical_temperedMode_exterior_zero carrier hca u hu, mul_zero, sub_zero]

/-- Centered and uncentered actual tails have the same source-defect limit
on separated tests. Existence is proved; the zero value remains open. -/
theorem neutralCenteredDigammaAction_exterior_defect_tendsto
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    Tendsto (fun N : ℕ => TemperedDistribution.fourierMultiplierCLM ℂ
      (neutralCenteredDigammaSymbol N) carrier.temperedMode u) atTop
      (𝓝 (neutralArchimedeanMultiplierCore carrier.temperedMode u -
        ∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x)) := by
  simp_rw [neutralCenteredDigammaAction_eq_shifted_exterior carrier _ hca hSymbol u hu]
  exact neutralShiftedDigammaAction_exterior_defect_tendsto carrier hc hca hSymbol u hu

/-- The exact remaining analytic target can now be stated entirely for the
centered actual frequency remainder, with no scalar-growth contamination. -/
theorem neutralCenteredDigammaAction_exterior_zero_iff
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    Tendsto (fun N : ℕ => TemperedDistribution.fourierMultiplierCLM ℂ
        (neutralCenteredDigammaSymbol N) carrier.temperedMode u) atTop (𝓝 0) ↔
      neutralArchimedeanMultiplierCore carrier.temperedMode u =
        ∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x := by
  simp_rw [neutralCenteredDigammaAction_eq_shifted_exterior carrier _ hca hSymbol u hu]
  exact neutralShiftedDigammaAction_exterior_zero_iff carrier hc hca hSymbol u hu

end

end WeilDefect
