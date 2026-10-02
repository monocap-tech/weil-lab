import WeilDefect.Morphology.NeutralDigammaLimit
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped FourierTransform SchwartzMap Topology RealInnerProductSpace

theorem neutralCenteredDigammaCubicMass_nonneg : 0 ≤ neutralCenteredDigammaCubicMass := by
  unfold neutralCenteredDigammaCubicMass
  exact tsum_nonneg (fun _ => by positivity)

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Explicit integrable majorant built from two actual Schwartz multipliers
and the actual carrier's global L1 norm mass. -/
def neutralCenteredDigammaPairingMajorant
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) (ξ : ℝ) : ℝ :=
  (∫ x : ℝ, ‖carrier.h x‖) *
    (‖SchwartzMap.smulLeftCLM ℂ (neutralCenteredDigammaSymbol 0) (𝓕⁻ u) ξ‖ +
      (64*Real.pi^2*neutralCenteredDigammaCubicMass) *
        ‖SchwartzMap.smulLeftCLM ℂ (fun t : ℝ => (t : ℂ)^2) (𝓕⁻ u) ξ‖)

theorem neutralCenteredDigammaPairingMajorant_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) :
    Integrable (neutralCenteredDigammaPairingMajorant carrier u) volume := by
  exact ((SchwartzMap.smulLeftCLM ℂ (neutralCenteredDigammaSymbol 0)
    (𝓕⁻ u)).integrable.norm.add
      ((SchwartzMap.smulLeftCLM ℂ (fun t : ℝ => (t : ℂ)^2)
        (𝓕⁻ u)).integrable.norm.const_mul
          (64*Real.pi^2*neutralCenteredDigammaCubicMass))).const_mul
            (∫ x : ℝ, ‖carrier.h x‖)

theorem neutralCenteredDigammaPairing_norm_bound
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (N : ℕ) (ξ : ℝ) :
    ‖(𝓕⁻ u ξ * neutralCenteredDigammaSymbol N ξ) * 𝓕 carrier.h ξ‖ ≤
      neutralCenteredDigammaPairingMajorant carrier u ξ := by
  have h0 := neutralCenteredDigammaSymbol_temperate 0 a hSymbol
  have h2 : Function.HasTemperateGrowth (fun t : ℝ => (t : ℂ)^2) := by fun_prop
  have hC := neutralCenteredDigammaSymbol_uniform_norm_bound N ξ
  have hF : ‖𝓕 carrier.h ξ‖ ≤ ∫ x : ℝ, ‖carrier.h x‖ := by
    rw [Real.fourier_real_eq]
    exact (norm_integral_le_integral_norm _).trans_eq (by simp)
  simp only [norm_mul]
  calc
    ‖𝓕⁻ u ξ‖ * ‖neutralCenteredDigammaSymbol N ξ‖ * ‖𝓕 carrier.h ξ‖ ≤
        (‖𝓕⁻ u ξ‖ * (‖neutralCenteredDigammaSymbol 0 ξ‖ +
          64*(Real.pi*ξ)^2*neutralCenteredDigammaCubicMass)) * ‖𝓕 carrier.h ξ‖ :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hC (norm_nonneg _)) (norm_nonneg _)
    _ ≤ (‖𝓕⁻ u ξ‖ * (‖neutralCenteredDigammaSymbol 0 ξ‖ +
          64*(Real.pi*ξ)^2*neutralCenteredDigammaCubicMass)) *
            (∫ x : ℝ, ‖carrier.h x‖) :=
      mul_le_mul_of_nonneg_left hF
        (mul_nonneg (norm_nonneg _) ((norm_nonneg _).trans hC))
    _ = neutralCenteredDigammaPairingMajorant carrier u ξ := by
      simp only [neutralCenteredDigammaPairingMajorant,
        SchwartzMap.smulLeftCLM_apply_apply h0, SchwartzMap.smulLeftCLM_apply_apply h2,
        norm_smul, norm_pow, Complex.norm_real, Real.norm_eq_abs, sq_abs]
      ring

/-- Actual Fourier integral of the represented pointwise residual; no
smoothness or multiplier CLM for the limiting symbol is postulated. -/
def neutralCenteredDigammaResidualPairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) : ℂ :=
  ∫ ξ : ℝ, (𝓕⁻ u ξ * neutralCenteredDigammaLimit ξ) * 𝓕 carrier.h ξ

theorem neutralCenteredDigamma_frequency_pairing_tendsto
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) :
    Tendsto (fun N : ℕ => ∫ ξ : ℝ,
      (𝓕⁻ u ξ * neutralCenteredDigammaSymbol N ξ) * 𝓕 carrier.h ξ) atTop
        (𝓝 (neutralCenteredDigammaResidualPairing carrier u)) := by
  have hF : Continuous (𝓕 carrier.h) :=
    VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar
      continuous_inner (neutralPhysicalRepresentative_integrable carrier)
  apply tendsto_integral_of_dominated_convergence
    (neutralCenteredDigammaPairingMajorant carrier u)
  · intro N
    exact ((𝓕⁻ u).continuous.aestronglyMeasurable.mul
      (neutralCenteredDigammaSymbol_temperate N a hSymbol).1.continuous.aestronglyMeasurable).mul
        hF.aestronglyMeasurable
  · exact neutralCenteredDigammaPairingMajorant_integrable carrier u
  · intro N
    filter_upwards with ξ
    exact neutralCenteredDigammaPairing_norm_bound carrier a hSymbol u N ξ
  · filter_upwards with ξ
    exact (tendsto_const_nhds.mul (neutralCenteredDigammaSymbol_tendsto ξ)).mul
      tendsto_const_nhds

/-- Exact Fourier-side pairing of the existing actual centered action. -/
theorem neutralCenteredDigammaAction_frequency_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (N : ℕ) (u : SchwartzMap ℝ ℂ) :
    TemperedDistribution.fourierMultiplierCLM ℂ (neutralCenteredDigammaSymbol N)
      carrier.temperedMode u = ∫ ξ : ℝ,
        (𝓕⁻ u ξ * neutralCenteredDigammaSymbol N ξ) * 𝓕 carrier.h ξ := by
  let v : SchwartzMap ℝ ℂ :=
    SchwartzMap.smulLeftCLM ℂ (neutralCenteredDigammaSymbol N) (𝓕⁻ u)
  rw [TemperedDistribution.fourierMultiplierCLM_apply_apply,
    neutralPhysical_temperedMode_apply]
  have ht : (∫ x, 𝓕 v x * carrier.h x) = ∫ ξ, v ξ * 𝓕 carrier.h ξ := by
    change (∫ x, VectorFourier.fourierIntegral Real.fourierChar volume
      (innerₗ ℝ) (v : ℝ → ℂ) x * carrier.h x) =
      ∫ ξ, v ξ * VectorFourier.fourierIntegral Real.fourierChar volume (innerₗ ℝ) carrier.h ξ
    simpa [ContinuousLinearMap.mul_apply'] using!
      VectorFourier.integral_bilin_fourierIntegral_eq_flip (ContinuousLinearMap.mul ℂ ℂ)
        (L := innerₗ ℝ) (μ := volume) (ν := volume)
        Real.continuous_fourierChar continuous_inner v.integrable
        (neutralPhysicalRepresentative_integrable carrier)
  change (∫ x, 𝓕 v x * carrier.h x) = _
  rw [ht]
  apply integral_congr_ae
  filter_upwards with ξ
  dsimp [v]
  rw [SchwartzMap.smulLeftCLM_apply_apply
    (neutralCenteredDigammaSymbol_temperate N a hSymbol)]
  simp only [smul_eq_mul]
  ring

/-- Dominated convergence for the actual existing action on every Schwartz
test. The limiting residual is represented, but is not proved zero. -/
theorem neutralCenteredDigammaAction_residual_tendsto
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) :
    Tendsto (fun N : ℕ => TemperedDistribution.fourierMultiplierCLM ℂ
      (neutralCenteredDigammaSymbol N) carrier.temperedMode u) atTop
        (𝓝 (neutralCenteredDigammaResidualPairing carrier u)) := by
  simp_rw [neutralCenteredDigammaAction_frequency_pairing carrier a hSymbol]
  exact neutralCenteredDigamma_frequency_pairing_tendsto carrier a hSymbol u

/-- The actual frequency residual equals the previously isolated physical
source-attachment defect on separated tests. Neither side is asserted zero. -/
theorem neutralCenteredDigammaResidualPairing_eq_exterior_defect
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a) (u : SchwartzMap ℝ ℂ)
    (hu : ∀ x ∈ Set.Ioo (-a) a, u x = 0) :
    neutralCenteredDigammaResidualPairing carrier u =
      neutralArchimedeanMultiplierCore carrier.temperedMode u -
        ∫ x, u x * neutralArchimedeanGapFunction carrier (a-c) x := by
  exact tendsto_nhds_unique (neutralCenteredDigammaAction_residual_tendsto carrier a hSymbol u)
    (neutralCenteredDigammaAction_exterior_defect_tendsto carrier hc hca hSymbol u hu)

end

end WeilDefect
