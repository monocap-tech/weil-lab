import WeilDefect.Morphology.NeutralShiftedDigammaAction

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped Topology

/-- A geometric error bound uniform over all displacements beyond the gap. -/
theorem neutralFiniteGaussKernel_gap_error (N : ℕ) {δ z : ℝ}
    (hδ : 0 < δ) (hz : δ ≤ |z|) :
    ‖neutralFiniteGaussKernelComplex N z + archimedeanGapKernelComplex δ z‖ ≤
      (1 / (1 - Real.exp (-2*δ))) * (Real.exp (-2*δ))^N := by
  have hzne : z ≠ 0 := by
    intro h
    simp [h] at hz
    linarith
  have heq : archimedeanGapKernel |z| z = archimedeanGapKernel δ z := by
    simp only [archimedeanGapKernel, max_self, max_eq_right hz]
  have hg := archimedeanGapKernel_bound hδ z
  have hp : (Real.exp (-2*|z|))^N ≤ (Real.exp (-2*δ))^N :=
    pow_le_pow_left₀ (Real.exp_nonneg _) (Real.exp_le_exp.mpr (by linarith)) N
  have hr : neutralFiniteGaussKernel N z + -archimedeanGapKernel δ z =
      -(archimedeanGapKernel δ z * (Real.exp (-2*|z|))^N) := by
    rw [neutralFiniteGaussKernel_eq N hzne, heq]
    ring
  rw [neutralFiniteGaussKernelComplex, archimedeanGapKernelComplex,
    ← Complex.ofReal_add, hr, Complex.norm_real, Real.norm_eq_abs, abs_neg,
    abs_of_nonneg (mul_nonneg hg.1 (pow_nonneg (Real.exp_nonneg _) N))]
  exact mul_le_mul hg.2 hp (pow_nonneg (Real.exp_nonneg _) N)
    (le_trans hg.1 hg.2)

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

theorem neutralFiniteGaussConvolution_eq_compactIntegral
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ) (x : ℝ) :
    neutralFiniteGaussConvolution carrier N x =
      ∫ y in Set.Icc (-c) c, carrier.h y * neutralFiniteGaussKernelComplex N (x-y) := by
  unfold neutralFiniteGaussConvolution
  rw [MeasureTheory.convolution_def]
  simp only [ContinuousLinearMap.mul_apply']
  symm
  apply setIntegral_eq_integral_of_forall_compl_eq_zero
  intro y hy
  rw [carrier.representative_eq_zero_of_not_mem hy, zero_mul]

theorem neutralFiniteGaussConvolution_integrand_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ) (x : ℝ) :
    IntegrableOn (fun y => carrier.h y * neutralFiniteGaussKernelComplex N (x-y))
      (Set.Icc (-c) c) volume := by
  have hk : Continuous (neutralFiniteGaussKernelComplex N) := by
    unfold neutralFiniteGaussKernelComplex neutralFiniteGaussKernel
    fun_prop
  exact (neutralPhysicalRepresentative_integrableOn carrier).mul_continuousOn
    (hk.comp (continuous_const.sub continuous_id)).continuousOn isCompact_Icc

/-- Quantitative convergence on the entire exterior from the actual rough
carrier's L1 mass, without a pointwise bound on the carrier. -/
theorem neutralFiniteGaussConvolution_exterior_error
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (N : ℕ) {a x : ℝ} (hc : 0 ≤ c) (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    ‖neutralFiniteGaussConvolution carrier N x +
      neutralArchimedeanGapFunction carrier (a-c) x‖ ≤
      ((1 / (1 - Real.exp (-2*(a-c)))) * (Real.exp (-2*(a-c)))^N) *
        neutralPhysicalCompactL1Mass carrier := by
  let B : ℝ := (1 / (1 - Real.exp (-2*(a-c)))) * (Real.exp (-2*(a-c)))^N
  have hδ : 0 < a-c := sub_pos.mpr hca
  have hf := neutralFiniteGaussConvolution_integrand_integrable carrier N x
  have hg := neutralArchimedeanGapFunction_integrand_integrable carrier hδ x
  rw [neutralFiniteGaussConvolution_eq_compactIntegral,
    neutralArchimedeanGapFunction_eq_compactIntegral, ← integral_add hf hg]
  calc
    _ ≤ ∫ y in Set.Icc (-c) c,
      ‖carrier.h y * neutralFiniteGaussKernelComplex N (x-y) +
        carrier.h y * archimedeanGapKernelComplex (a-c) (x-y)‖ :=
          norm_integral_le_integral_norm _
    _ ≤ ∫ y in Set.Icc (-c) c, B * ‖carrier.h y‖ := by
      refine setIntegral_mono_ae_restrict (hf.add hg).norm
        ((neutralPhysicalRepresentative_integrableOn carrier).norm.const_mul B) ?_
      filter_upwards [] with y hy
      rw [← mul_add, norm_mul]
      calc
        _ ≤ ‖carrier.h y‖ * B := mul_le_mul_of_nonneg_left
          (neutralFiniteGaussKernel_gap_error N hδ
            (supportGap_le_abs_sub_point hc hca hx hy)) (norm_nonneg _)
        _ = _ := by ring
    _ = _ := by rw [integral_const_mul]; rfl

/-- The positive finite convolution converges to the negative of the signed
gap function at every exterior point. This is not the shifted-tail limit. -/
theorem neutralFiniteGaussConvolution_exterior_tendsto
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a x : ℝ} (hc : 0 ≤ c) (hca : c < a) (hx : x ∉ Set.Ioo (-a) a) :
    Tendsto (fun N : ℕ => neutralFiniteGaussConvolution carrier N x) atTop
      (𝓝 (-neutralArchimedeanGapFunction carrier (a-c) x)) := by
  have hr : Real.exp (-2*(a-c)) < 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_lt_exp.mpr
    linarith
  have hp := tendsto_pow_atTop_nhds_zero_of_lt_one (Real.exp_nonneg (-2*(a-c))) hr
  have hb := (tendsto_const_nhds.mul hp).mul_const (neutralPhysicalCompactL1Mass carrier)
  have hn : Tendsto (fun N : ℕ => ‖neutralFiniteGaussConvolution carrier N x +
      neutralArchimedeanGapFunction carrier (a-c) x‖) atTop (𝓝 0) := by
    apply squeeze_zero (fun N => norm_nonneg _) (fun N =>
      neutralFiniteGaussConvolution_exterior_error carrier N hc hca hx)
    simpa using hb
  apply tendsto_iff_norm_sub_tendsto_zero.mpr
  simpa only [sub_neg_eq_add] using hn

end

end WeilDefect
