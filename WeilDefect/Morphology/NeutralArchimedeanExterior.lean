import WeilDefect.Morphology.NeutralIntegralGrowthWeilIdentity
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap
open scoped ComplexConjugate

/-- Positive off-diagonal Gauss factor with its singularity cut off at a
specified positive gap. Its negative is the candidate archimedean kernel. -/
def archimedeanGapKernel (δ z : ℝ) : ℝ :=
  Real.exp (-(max δ |z|) / 2) / (1 - Real.exp (-2 * max δ |z|))

theorem archimedeanGapKernel_denominator_pos {δ : ℝ} (hδ : 0 < δ) (z : ℝ) :
    0 < 1 - Real.exp (-2 * max δ |z|) := by
  have he : Real.exp (-2 * max δ |z|) < Real.exp 0 :=
    Real.exp_lt_exp.mpr (by nlinarith [le_max_left δ |z|])
  simpa only [Real.exp_zero, sub_pos] using he

theorem archimedeanGapKernel_continuous {δ : ℝ} (hδ : 0 < δ) :
    Continuous (archimedeanGapKernel δ) := by
  unfold archimedeanGapKernel
  apply Continuous.div
  · fun_prop
  · fun_prop
  · intro z
    exact ne_of_gt (archimedeanGapKernel_denominator_pos hδ z)

/-- An explicit uniform bound independent of the displacement. -/
theorem archimedeanGapKernel_bound {δ : ℝ} (hδ : 0 < δ) (z : ℝ) :
    0 ≤ archimedeanGapKernel δ z ∧
    archimedeanGapKernel δ z ≤ 1 / (1 - Real.exp (-2*δ)) := by
  have hd : 0 < 1 - Real.exp (-2*δ) := by
    have he : Real.exp (-2*δ) < Real.exp 0 := Real.exp_lt_exp.mpr (by linarith)
    simpa only [Real.exp_zero, sub_pos] using he
  have hn : Real.exp (-(max δ |z|)/2) ≤ 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_le_exp.mpr
    nlinarith [le_max_left δ |z|]
  have hden : 1 - Real.exp (-2*δ) ≤ 1 - Real.exp (-2*max δ |z|) := by
    have he := Real.exp_le_exp.mpr
      (show -2*max δ |z| ≤ -2*δ by nlinarith [le_max_left δ |z|])
    linarith
  unfold archimedeanGapKernel
  refine ⟨div_nonneg (Real.exp_nonneg _) (archimedeanGapKernel_denominator_pos hδ z).le, ?_⟩
  calc
    _ ≤ Real.exp (-(max δ |z|)/2) / (1 - Real.exp (-2*δ)) :=
      div_le_div_of_nonneg_left (Real.exp_nonneg _) hd hden
    _ ≤ _ := (div_le_div_iff_of_pos_right hd).mpr hn

/-- Signed complex kernel, retaining the negative half of the pinned cosine
density. Fourier/distribution identification is not asserted by this definition. -/
def archimedeanGapKernelComplex (δ z : ℝ) : ℂ :=
  (-archimedeanGapKernel δ z : ℝ)

theorem archimedeanGapKernelComplex_continuous {δ : ℝ} (hδ : 0 < δ) :
    Continuous (archimedeanGapKernelComplex δ) :=
  Complex.continuous_ofReal.comp (archimedeanGapKernel_continuous hδ).neg

theorem archimedeanGapKernelComplex_norm_bound {δ : ℝ} (hδ : 0 < δ) (z : ℝ) :
    ‖archimedeanGapKernelComplex δ z‖ ≤ 1 / (1 - Real.exp (-2*δ)) := by
  have h := archimedeanGapKernel_bound hδ z
  simpa only [archimedeanGapKernelComplex, Complex.norm_real, Real.norm_eq_abs,
    abs_neg, abs_of_nonneg h.1] using h.2

/-- Away from zero the truncated kernel is literally the pinned off-diagonal
formula. The condition keeps the denominator away from its singularity. -/
theorem archimedeanGapKernelComplex_eq_offDiagonal
    {δ z : ℝ} (hz : δ ≤ |z|) :
    archimedeanGapKernelComplex δ z =
      (- (Real.exp (-|z|/2) / (1 - Real.exp (-2*|z|))) : ℝ) := by
  simp only [archimedeanGapKernelComplex, archimedeanGapKernel, max_eq_right hz]

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- An actual continuous function obtained by convolving the rough compact
carrier with the gap-truncated archimedean kernel. Only its exterior agrees
with the singular off-diagonal formula; this is not the whole core. -/
def neutralArchimedeanGapFunction
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (δ : ℝ) : ℝ → ℂ :=
  MeasureTheory.convolution carrier.h (archimedeanGapKernelComplex δ) (lsmul ℂ ℂ) volume

theorem neutralArchimedeanGapFunction_continuous
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {δ : ℝ} (hδ : 0 < δ) :
    Continuous (neutralArchimedeanGapFunction carrier δ) := by
  have hb : BddAbove (Set.range (fun z => ‖archimedeanGapKernelComplex δ z‖)) := by
    refine ⟨1 / (1 - Real.exp (-2*δ)), ?_⟩
    rintro _ ⟨z, rfl⟩
    exact archimedeanGapKernelComplex_norm_bound hδ z
  exact hb.continuous_convolution_right_of_integrable (lsmul ℂ ℂ)
    (neutralPhysicalRepresentative_integrable carrier)
    (archimedeanGapKernelComplex_continuous hδ)

theorem neutralArchimedeanGapFunction_eq_compactIntegral
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (δ x : ℝ) :
    neutralArchimedeanGapFunction carrier δ x =
      ∫ y in Set.Icc (-c) c, carrier.h y * archimedeanGapKernelComplex δ (x-y) := by
  unfold neutralArchimedeanGapFunction
  rw [MeasureTheory.convolution_def]
  simp only [lsmul_apply, smul_eq_mul]
  symm
  apply setIntegral_eq_integral_of_forall_compl_eq_zero
  intro y hy
  rw [carrier.representative_eq_zero_of_not_mem hy, zero_mul]

theorem neutralArchimedeanGapFunction_integrand_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {δ : ℝ} (hδ : 0 < δ) (x : ℝ) :
    IntegrableOn (fun y => carrier.h y * archimedeanGapKernelComplex δ (x-y))
      (Set.Icc (-c) c) volume :=
  (neutralPhysicalRepresentative_integrableOn carrier).mul_continuousOn
    ((archimedeanGapKernelComplex_continuous hδ).comp
      (continuous_const.sub continuous_id)).continuousOn isCompact_Icc

/-- Uniform function bound from actual compact L1 mass; no boundedness of h
or positive Sobolev regularity is assumed. -/
theorem neutralArchimedeanGapFunction_norm_bound
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {δ : ℝ} (hδ : 0 < δ) (x : ℝ) :
    ‖neutralArchimedeanGapFunction carrier δ x‖ ≤
      (1 / (1 - Real.exp (-2*δ))) * neutralPhysicalCompactL1Mass carrier := by
  rw [neutralArchimedeanGapFunction_eq_compactIntegral]
  calc
    _ ≤ ∫ y in Set.Icc (-c) c,
      ‖carrier.h y * archimedeanGapKernelComplex δ (x-y)‖ :=
        norm_integral_le_integral_norm _
    _ ≤ ∫ y in Set.Icc (-c) c, (1 / (1 - Real.exp (-2*δ))) * ‖carrier.h y‖ := by
      refine setIntegral_mono_ae_restrict
        (neutralArchimedeanGapFunction_integrand_integrable carrier hδ x).norm
        ((neutralPhysicalRepresentative_integrableOn carrier).norm.const_mul _) ?_
      filter_upwards [] with y
      rw [norm_mul]
      calc
        _ ≤ ‖carrier.h y‖ * (1 / (1 - Real.exp (-2*δ))) :=
          mul_le_mul_of_nonneg_left (archimedeanGapKernelComplex_norm_bound hδ _) (norm_nonneg _)
        _ = _ := by ring
    _ = _ := by rw [integral_const_mul]; rfl

/-- The function's actual exterior value is the untruncated pinned Gauss
integral, since every displacement from the carrier has at least the gap. -/
theorem neutralArchimedeanGapFunction_eq_exteriorFormula
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a x : ℝ} (hc : 0 ≤ c) (hca : c < a) (hx : x ∉ Set.Ioo (-a) a) :
    neutralArchimedeanGapFunction carrier (a-c) x =
      ∫ y in Set.Icc (-c) c, carrier.h y *
        ((- (Real.exp (-|x-y|/2) / (1 - Real.exp (-2*|x-y|))) : ℝ) : ℂ) := by
  rw [neutralArchimedeanGapFunction_eq_compactIntegral]
  apply setIntegral_congr_fun measurableSet_Icc
  intro y hy
  rw [archimedeanGapKernelComplex_eq_offDiagonal
    (supportGap_le_abs_sub_point hc hca hx hy)]

/-- Genuine convergence of the untruncated exterior formula. -/
theorem neutralArchimedeanExterior_integrand_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a x : ℝ} (hc : 0 ≤ c) (hca : c < a) (hx : x ∉ Set.Ioo (-a) a) :
    IntegrableOn (fun y => carrier.h y *
      ((- (Real.exp (-|x-y|/2) / (1 - Real.exp (-2*|x-y|))) : ℝ) : ℂ))
      (Set.Icc (-c) c) volume := by
  apply (integrableOn_congr_fun ?_ measurableSet_Icc).mp
    (neutralArchimedeanGapFunction_integrand_integrable carrier (sub_pos.mpr hca) x)
  intro y hy
  rw [archimedeanGapKernelComplex_eq_offDiagonal
    (supportGap_le_abs_sub_point hc hca hx hy)]

/-- The fixed inverse exponential weight is globally integrable. -/
theorem integrable_exp_neg_rate_abs {κ : ℝ} (hκ : 0 < κ) :
    Integrable (fun x : ℝ => Real.exp (-κ * |x|)) volume := by
  have hl : IntegrableOn (fun x : ℝ => Real.exp (-κ * |x|)) (Set.Iic 0) volume := by
    apply (integrableOn_congr_fun ?_ measurableSet_Iic).mp (integrableOn_exp_mul_Iic hκ 0)
    intro x hx
    rw [abs_of_nonpos hx]
    congr 1
    ring
  have hr : IntegrableOn (fun x : ℝ => Real.exp (-κ * |x|)) (Set.Ioi 0) volume := by
    apply (integrableOn_congr_fun ?_ measurableSet_Ioi).mp
      (integrableOn_exp_mul_Ioi (neg_lt_zero.mpr hκ) 0)
    intro x hx
    rw [abs_of_pos hx]
  have hall := hl.union hr
  rw [Set.Iic_union_Ioi] at hall
  exact integrableOn_univ.mp hall

/-- Actual finite weighted mass for every positive rate, derived from the
constructed function's uniform bound, not imported as a representation field. -/
theorem neutralArchimedeanGapFunction_weightedNorm_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {δ κ : ℝ} (hδ : 0 < δ) (hκ : 0 < κ) :
    Integrable (fun x => ‖neutralArchimedeanGapFunction carrier δ x‖ *
      Real.exp (-κ * |x|)) volume := by
  apply ((integrable_exp_neg_rate_abs hκ).const_mul
    ((1 / (1 - Real.exp (-2*δ))) * neutralPhysicalCompactL1Mass carrier)).mono'
  · exact (neutralArchimedeanGapFunction_continuous carrier hδ).norm.aestronglyMeasurable.mul
      (by fun_prop : Continuous (fun x : ℝ => Real.exp (-κ * |x|))).aestronglyMeasurable
  · filter_upwards [] with x
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    exact mul_le_mul_of_nonneg_right (neutralArchimedeanGapFunction_norm_bound carrier hδ x)
      (Real.exp_nonneg _)

end

end WeilDefect
