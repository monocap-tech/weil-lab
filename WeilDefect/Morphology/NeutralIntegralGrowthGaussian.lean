import WeilDefect.Morphology.NeutralWeilPrimeRegularity

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped ComplexConjugate SchwartzMap Topology

/-- Integral-growth residual: genuine weighted L1 mass replaces the stronger
pointwise exponential field. Source realization is a separate obligation. -/
structure NeutralIntegralGrowthResidual (c : ℝ) where
  a : ℝ
  strict : c < a
  q : ℝ → ℂ
  locallyIntegrable : LocallyIntegrable q volume
  rate : ℝ
  rate_nonneg : 0 ≤ rate
  weightedIntegrable : Integrable (fun x => ‖q x‖ * Real.exp (-rate * |x|)) volume
  vanishes_ae : ∀ᵐ x ∂volume, x ∈ Set.Ioo (-a) a → q x = 0

/-- Weighted mass controls a conjugated pairing whenever the test absorbs the
inverse weight outside the null interval. All integrability is genuine. -/
theorem integralGrowth_pairing_bound
    (q g : ℝ → ℂ) (a κ A : ℝ)
    (hq : AEStronglyMeasurable q volume)
    (hg : AEStronglyMeasurable g volume)
    (hw : Integrable (fun x => ‖q x‖ * Real.exp (-κ * |x|)) volume)
    (hzero : ∀ᵐ x ∂volume, x ∈ Set.Ioo (-a) a → q x = 0)
    (hbound : ∀ x, x ∉ Set.Ioo (-a) a →
      ‖g x‖ * Real.exp (κ * |x|) ≤ A) :
    Integrable (fun x => conj (g x) * q x) volume ∧
    ‖∫ x, conj (g x) * q x‖ ≤ A * ∫ x, ‖q x‖ * Real.exp (-κ * |x|) := by
  have hdom : ∀ᵐ x ∂volume,
      ‖conj (g x) * q x‖ ≤ A * (‖q x‖ * Real.exp (-κ * |x|)) := by
    filter_upwards [hzero] with x hx
    by_cases hin : x ∈ Set.Ioo (-a) a
    · simp only [hx hin, mul_zero, norm_zero, zero_mul, le_refl]
    · have he : Real.exp (κ * |x|) * Real.exp (-κ * |x|) = 1 := by
      rw [← Real.exp_add]
        rw [show κ * |x| + -κ * |x| = 0 by ring, Real.exp_zero]
      have hid :
          (‖q x‖ * Real.exp (-κ * |x|)) * (‖g x‖ * Real.exp (κ * |x|)) =
            ‖g x‖ * ‖q x‖ := by
        calc
          _ = (‖g x‖ * ‖q x‖) *
            (Real.exp (κ * |x|) * Real.exp (-κ * |x|)) := by ring
          _ = _ := by rw [he, mul_one]
      rw [norm_mul, Complex.norm_conj, ← hid]
      calc
        _ ≤ (‖q x‖ * Real.exp (-κ * |x|)) * A :=
          mul_le_mul_of_nonneg_left (hbound x hin) (by positivity)
        _ = _ := by ring
  have hi : Integrable (fun x => conj (g x) * q x) volume :=
    (hw.const_mul A).mono'
      ((Complex.continuous_conj.comp_aestronglyMeasurable hg).mul hq) hdom
  refine ⟨hi, ?_⟩
  calc
    ‖∫ x, conj (g x) * q x‖ ≤ ∫ x, ‖conj (g x) * q x‖ :=
      norm_integral_le_integral_norm _
    _ ≤ ∫ x, A * (‖q x‖ * Real.exp (-κ * |x|)) :=
      integral_mono_ae hi.norm (hw.const_mul A) hdom
    _ = _ := integral_const_mul _ _

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Radius-only exterior envelope for the actual Gaussian mode; no residual
growth or representation fields are used in this geometric estimate. -/
theorem movingGaussianFilteredMode_norm_le_radiusEnvelope
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hca : c < a) (Ck : ℂ) (R x : ℝ)
    (hc : 0 ≤ c) (hR : 0 ≤ R) (hx : x ∉ Set.Ioo (-a) a) :
    ‖movingGaussianFilteredMode Ck R carrier x‖ ≤
      (‖Ck‖ * Real.sqrt R * gaussianSupportEnvelope R c x) *
        neutralPhysicalCompactL1Mass carrier := by
  let K := ‖Ck‖ * Real.sqrt R * gaussianSupportEnvelope R c x
  have hInt := neutralPhysicalRepresentative_integrableOn carrier
  have hCont : Continuous (fun y : ℝ => movingGaussianPhysicalKernel Ck R (x-y)) := by
    unfold movingGaussianPhysicalKernel
    fun_prop
  have hProd := hInt.mul_continuousOn hCont.continuousOn isCompact_Icc
  calc
    ‖movingGaussianFilteredMode Ck R carrier x‖ ≤
      ∫ y in Set.Icc (-c) c, ‖carrier.h y * movingGaussianPhysicalKernel Ck R (x-y)‖ :=
        norm_integral_le_integral_norm _
    _ ≤ ∫ y in Set.Icc (-c) c, K * ‖carrier.h y‖ := by
      refine setIntegral_mono_ae_restrict hProd.norm (hInt.norm.const_mul K) ?_
      filter_upwards [self_mem_ae_restrict measurableSet_Icc] with y hy
      rw [norm_mul]
      calc
        _ ≤ ‖carrier.h y‖ * K := mul_le_mul_of_nonneg_left
          (movingGaussianPhysicalKernel_norm_le_exteriorEnvelope hR hc hca hx hy)
          (norm_nonneg _)
        _ = _ := by ring
    _ = _ := by rw [integral_const_mul]; rfl

/-- Completion absorbs the inverse integral-growth weight into the actual
Gaussian, leaving a uniform collar exponential. -/
theorem movingGaussianFilteredMode_weighted_exterior_bound
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a κ : ℝ) (hca : c < a) (hκ : 0 ≤ κ) (Ck : ℂ) (R x : ℝ)
    (hc : 0 ≤ c) (hR : 0 ≤ R) (hlarge : 8 * κ ≤ R * (a-c))
    (hx : x ∉ Set.Ioo (-a) a) :
    ‖movingGaussianFilteredMode Ck R carrier x‖ * Real.exp (κ * |x|) ≤
      (‖Ck‖ * Real.sqrt R * neutralPhysicalCompactL1Mass carrier) *
        Real.exp (κ*c) * Real.exp (-R * (a-c)^2 / 16) := by
  have hf := movingGaussianFilteredMode_norm_le_radiusEnvelope carrier a hca Ck R x hc hR hx
  have ht := gaussianTailCompletion_bound hκ hR hc hca hlarge hx
  have he : Real.exp (-R * (|x|-c)^2 / 16) ≤ 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_le_exp.mpr
    nlinarith [mul_nonneg hR (sq_nonneg (|x|-c))]
  have ht' : Real.exp (κ * |x|) * gaussianSupportEnvelope R c x ≤
      Real.exp (κ*c) * Real.exp (-R * (a-c)^2 / 16) := by
    calc
      _ ≤ _ := ht
      _ ≤ _ := mul_le_of_le_one_right (by positivity) he
  have hcoef : 0 ≤ ‖Ck‖ * Real.sqrt R * neutralPhysicalCompactL1Mass carrier :=
    mul_nonneg (mul_nonneg (norm_nonneg _) (Real.sqrt_nonneg _))
      (neutralPhysicalCompactL1Mass_nonneg carrier)
  calc
    _ ≤ ((‖Ck‖ * Real.sqrt R * gaussianSupportEnvelope R c x) *
      neutralPhysicalCompactL1Mass carrier) * Real.exp (κ * |x|) :=
        mul_le_mul_of_nonneg_right hf (Real.exp_nonneg _)
    _ = (‖Ck‖ * Real.sqrt R * neutralPhysicalCompactL1Mass carrier) *
      (Real.exp (κ * |x|) * gaussianSupportEnvelope R c x) := by ring
    _ ≤ _ := by
      simpa only [mul_assoc] using mul_le_mul_of_nonneg_left ht' hcoef

/-- Actual Hermitian Gaussian pairing with integral growth, including its
strict support-gap exponential estimate. No pointwise residual bound occurs. -/
theorem integralGrowthGaussian_pairing_bound
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (d : NeutralIntegralGrowthResidual c) (Ck : ℂ) (R : ℝ)
    (hc : 0 ≤ c) (hR : 0 ≤ R) (hlarge : 8*d.rate ≤ R*(d.a-c)) :
    Integrable (fun x => conj (movingGaussianFilteredMode Ck R carrier x) * d.q x) volume ∧
    ‖∫ x, conj (movingGaussianFilteredMode Ck R carrier x) * d.q x‖ ≤
      ((‖Ck‖ * Real.sqrt R * neutralPhysicalCompactL1Mass carrier) *
        Real.exp (d.rate*c) * Real.exp (-R*(d.a-c)^2/16)) *
        ∫ x, ‖d.q x‖ * Real.exp (-d.rate * |x|) := by
  exact integralGrowth_pairing_bound d.q _ d.a d.rate _
    d.locallyIntegrable.aestronglyMeasurable
    (movingGaussianFilteredMode_continuous carrier Ck hR).aestronglyMeasurable
    d.weightedIntegrable d.vanishes_ae
    (fun x hx => movingGaussianFilteredMode_weighted_exterior_bound
      carrier d.a d.rate d.strict d.rate_nonneg Ck R x hc hR hlarge hx)

/-- The actual shell inhabits the integral-growth residual interface directly,
with zero rate; no bounded representative is requested. -/
def primeShellIntegralGrowthResidual
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a b : ℝ) (hca : c < a) : NeutralIntegralGrowthResidual c where
  a := a
  strict := hca
  q := frozenWeilPrimeShellPhysical carrier a b
  locallyIntegrable := (frozenWeilPrimeShellPhysical_integrable carrier a b).locallyIntegrable
  rate := 0
  rate_nonneg := le_rfl
  weightedIntegrable := by
    simpa using (frozenWeilPrimeShellPhysical_integrable carrier a b).norm
  vanishes_ae := Filter.Eventually.of_forall fun x hx =>
    frozenWeilPrimeShellPhysical_zero_on_window carrier hca.le hx

/-- The all-compact-test weak identity extends to an integrably paired Schwartz
test independently of any pointwise-growth residual package. -/
theorem integralGrowth_weakIdentity_of_integrableSchwartz
    (core : RealComplexTempered) (q pole : ℝ → ℂ)
    (hweak : ∀ (u : SchwartzMap ℝ ℂ), HasCompactSupport u →
      (∫ x, u x * q x) = core u + ∫ x, u x * pole x)
    (f : SchwartzMap ℝ ℂ)
    (hq : Integrable (fun x => f x * q x) volume)
    (hp : Integrable (fun x => f x * pole x) volume) :
    (∫ x, f x * q x) = core f + ∫ x, f x * pole x := by
  let cut : ℕ → SchwartzMap ℝ ℂ := fun N =>
    neutralGaussianSchwartzCutoff ((N : ℝ)+1) f
  have hcut : Tendsto cut atTop (𝓝 f) := neutralGaussianSchwartzCutoff_tendsto f
  have hcore : Tendsto (fun N => core (cut N)) atTop (𝓝 (core f)) :=
    core.continuous.continuousAt.tendsto.comp hcut
  have hqLimit := neutralGaussianSchwartzCutoff_pairing_tendsto f q hq
  have hpLimit := neutralGaussianSchwartzCutoff_pairing_tendsto f pole hp
  have hleft : Tendsto (fun N => ∫ x, cut N x * q x) atTop
      (𝓝 (core f + ∫ x, f x * pole x)) := by
    refine (hcore.add hpLimit).congr' ?_
    exact Filter.Eventually.of_forall fun N =>
      (hweak (cut N) (neutralGaussianSchwartzCutoff_compact
        (by positivity : (N : ℝ)+1 ≠ 0) f)).symm
  exact tendsto_nhds_unique hqLimit hleft

end

end WeilDefect
