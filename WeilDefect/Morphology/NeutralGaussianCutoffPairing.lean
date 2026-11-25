import WeilDefect.Morphology.NeutralGaussianCutoff
import WeilDefect.Morphology.NeutralGaussianAdmissibility
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace WeilDefect

noncomputable section

open MeasureTheory Filter Set
open scoped SchwartzMap Topology

theorem residualFilteredMode_integrable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge : 8 * residual.growthRate ≤ R * (residual.a - c)) :
    Integrable
      (fun x : ℝ =>
        residual.q x * movingGaussianFilteredMode Ck R carrier x) volume := by
  let f : ℝ → ℂ :=
    fun x => residual.q x * movingGaussianFilteredMode Ck R carrier x
  have hext : IntegrableOn f (gaussianExteriorSet residual.a) volume :=
    residualFilteredMode_integrableOn_exterior
      carrier residual Ck hc hR hlarge
  have hind :
      Integrable ((gaussianExteriorSet residual.a).indicator f) volume :=
    hext.integrable_indicator
      (by
        unfold gaussianExteriorSet
        exact measurableSet_Iic.union measurableSet_Ici)
  refine hind.congr ?_
  filter_upwards [residual.vanishes_ae] with x hx
  by_cases hxe : x ∈ gaussianExteriorSet residual.a
  · simp [Set.indicator_of_mem hxe, f]
  · have hxin : x ∈ Set.Ioo (-residual.a) residual.a := by
      simp [gaussianExteriorSet] at hxe
      exact ⟨hxe.1, hxe.2⟩
    have hq : residual.q x = 0 := hx hxin
    simp [Set.indicator_of_not_mem hxe, f, hq]

theorem neutralGaussianSchwartzCutoff_pairing_tendsto
    (f : SchwartzMap ℝ ℂ)
    (g : ℝ → ℂ)
    (hpair : Integrable (fun x : ℝ => f x * g x) volume) :
    Tendsto
      (fun N : ℕ =>
        ∫ x : ℝ,
          neutralGaussianSchwartzCutoff ((N : ℝ) + 1) f x * g x
          ∂volume)
      atTop
      (𝓝 (∫ x : ℝ, f x * g x ∂volume)) := by
  apply tendsto_integral_of_dominated_convergence
    (fun x : ℝ => ‖f x * g x‖)
  · intro N
    have hcut :
        AEStronglyMeasurable
          (fun x : ℝ =>
            (neutralGaussianCutoffScalar ((N : ℝ) + 1) x : ℂ)) volume := by
      exact
        (Complex.ofRealCLM.continuous.comp
          (neutralGaussianCutoffScalar_contDiff ((N : ℝ) + 1)).continuous).aestronglyMeasurable
    have hm := hcut.mul hpair.aestronglyMeasurable
    refine hm.congr ?_
    filter_upwards with x
    rw [neutralGaussianSchwartzCutoff_apply
      (by positivity : (N : ℝ) + 1 ≠ 0)]
    simp only [Complex.ofReal_mul]
    ring
  · exact hpair.norm
  · intro N
    exact Eventually.of_forall fun x => by
      rw [neutralGaussianSchwartzCutoff_apply
        (by positivity : (N : ℝ) + 1 ≠ 0),
        norm_mul, Complex.norm_real]
      have h0 : 0 ≤ neutralGaussianCutoffScalar ((N : ℝ) + 1) x := by
        exact neutralGaussianCutoffBump.nonneg
      have h1 : neutralGaussianCutoffScalar ((N : ℝ) + 1) x ≤ 1 := by
        exact neutralGaussianCutoffBump.le_one
      rw [abs_of_nonneg h0]
      calc
        neutralGaussianCutoffScalar ((N : ℝ) + 1) x * ‖f x‖ * ‖g x‖
            = neutralGaussianCutoffScalar ((N : ℝ) + 1) x * ‖f x * g x‖ := by
                rw [norm_mul]
        _ ≤ 1 * ‖f x * g x‖ := by
              exact mul_le_mul_of_nonneg_right h1 (norm_nonneg _)
        _ = ‖f x * g x‖ := one_mul _
  · exact Eventually.of_forall fun x => by
      have hr : Tendsto (fun N : ℕ => (N : ℝ) + 1) atTop atTop :=
        (tendsto_natCast_atTop_atTop :
          Tendsto (fun N : ℕ => (N : ℝ)) atTop atTop).atTop_add
            (tendsto_const_nhds (x := (1 : ℝ)))
      have hev : ∀ᶠ N : ℕ in atTop, |x| ≤ (N : ℝ) + 1 :=
        hr.eventually_ge_atTop |x|
      apply tendsto_of_eventually_eq tendsto_const_nhds
      filter_upwards [hev] with N hN
      rw [neutralGaussianSchwartzCutoff_apply
        (by positivity : (N : ℝ) + 1 ≠ 0),
        neutralGaussianCutoffScalar_one
          (by positivity : 0 < (N : ℝ) + 1) hN]
      simp

theorem movingGaussianFilteredModeCompactCutoff_residual_pairing_tendsto
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge : 8 * residual.growthRate ≤ R * (residual.a - c)) :
    Tendsto
      (fun N : ℕ =>
        ∫ x : ℝ,
          movingGaussianFilteredModeCompactCutoff Ck R hR carrier N x
            * residual.q x ∂volume)
      atTop
      (𝓝
        (∫ x : ℝ,
          movingGaussianFilteredModeSchwartz Ck R hR carrier x
            * residual.q x ∂volume)) := by
  have hres :
      Integrable
        (fun x : ℝ =>
          movingGaussianFilteredModeSchwartz Ck R hR carrier x
            * residual.q x) volume := by
    have h := residualFilteredMode_integrable carrier residual Ck hc hR hlarge
    simpa [movingGaussianFilteredModeSchwartz_apply, mul_comm] using h
  simpa [movingGaussianFilteredModeCompactCutoff] using
    neutralGaussianSchwartzCutoff_pairing_tendsto
      (movingGaussianFilteredModeSchwartz Ck R hR carrier)
      residual.q hres

theorem movingGaussianFilteredModeCompactCutoff_pole_pairing_tendsto
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (pole : ℝ → ℂ)
    (hpole : NeutralPoleExponentialGrowthData pole)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge : 8 * hpole.growthRate ≤ R * (residual.a - c)) :
    Tendsto
      (fun N : ℕ =>
        ∫ x : ℝ,
          movingGaussianFilteredModeCompactCutoff Ck R hR carrier N x
            * pole x ∂volume)
      atTop
      (𝓝
        (∫ x : ℝ,
          movingGaussianFilteredModeSchwartz Ck R hR carrier x
            * pole x ∂volume)) := by
  have hp :
      Integrable
        (fun x : ℝ =>
          movingGaussianFilteredModeSchwartz Ck R hR carrier x
            * pole x) volume := by
    have h :=
      poleFilteredMode_integrable
        carrier residual pole hpole Ck hc hR hlarge
    simpa [movingGaussianFilteredModeSchwartz_apply, mul_comm] using h
  simpa [movingGaussianFilteredModeCompactCutoff] using
    neutralGaussianSchwartzCutoff_pairing_tendsto
      (movingGaussianFilteredModeSchwartz Ck R hR carrier)
      pole hp

end

end WeilDefect