import WeilDefect.Morphology.NeutralGaussianSupportGap
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Tactic

namespace WeilDefect

noncomputable section

open MeasureTheory
open Set

/-- The two exterior half-lines complementary to the strict null interval. -/
def gaussianExteriorSet (a : ℝ) : Set ℝ :=
  Set.Iic (-a) ∪ Set.Ici a

/--
The actual moving-Gaussian kernel retains the full exterior distance envelope,
not merely the collar constant.
-/
theorem movingGaussianPhysicalKernel_norm_le_exteriorEnvelope
    {Ck : ℂ} {R c a x y : ℝ}
    (hR : 0 ≤ R)
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a)
    (hy : y ∈ Set.Icc (-c) c) :
    ‖movingGaussianPhysicalKernel Ck R (x - y)‖
      ≤
    ‖Ck‖ * Real.sqrt R
      * gaussianSupportEnvelope R c x := by
  rw [norm_movingGaussianPhysicalKernel Ck R (x - y) hR]
  unfold gaussianSupportEnvelope
  have hgap :
      |x| - c ≤ |x - y| := by
    have hyabs : |y| ≤ c := (abs_le).2 hy
    exact (sub_le_sub_left hyabs |x|).trans
      (abs_sub_abs_le_abs_sub x y)
  have ha : 0 ≤ a := hc.trans (le_of_lt hca)
  have hxabs : a ≤ |x| :=
    radius_le_abs_of_not_mem_Ioo ha hx
  have hxgap0 : 0 ≤ |x| - c := by
    linarith
  have hsq :
      (|x| - c) ^ 2 ≤ |x - y| ^ 2 := by
    nlinarith [sq_nonneg (|x - y| - (|x| - c))]
  have hexp :
      Real.exp (-R * |x - y| ^ 2 / 4)
        ≤ Real.exp (-R * (|x| - c) ^ 2 / 4) := by
    apply Real.exp_le_exp.mpr
    have hmul :
        R * (|x| - c) ^ 2 ≤ R * |x - y| ^ 2 :=
      mul_le_mul_of_nonneg_left hsq hR
    nlinarith
  exact mul_le_mul_of_nonneg_left hexp
    (mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R))

/--
Exterior envelope for the actual filtered F-1 mode with the full physical
Gaussian tail retained.
-/
theorem movingGaussianFilteredMode_norm_le_exteriorEnvelope
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) (R x : ℝ)
    (hc : 0 ≤ c)
    (hR : 0 ≤ R)
    (hx : x ∉ Set.Ioo (-residual.a) residual.a) :
    ‖movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (‖Ck‖ * Real.sqrt R
      * gaussianSupportEnvelope R c x)
      * neutralPhysicalCompactL1Mass carrier := by
  let Kx : ℝ :=
    ‖Ck‖ * Real.sqrt R * gaussianSupportEnvelope R c x
  have hInt :
      IntegrableOn carrier.h (Set.Icc (-c) c) volume :=
    neutralPhysicalRepresentative_integrableOn carrier
  have hKernelCont :
      Continuous
        (fun y : ℝ =>
          movingGaussianPhysicalKernel Ck R (x - y)) := by
    unfold movingGaussianPhysicalKernel
    fun_prop
  have hProd :
      IntegrableOn
        (fun y : ℝ =>
          carrier.h y * movingGaussianPhysicalKernel Ck R (x - y))
        (Set.Icc (-c) c) volume := by
    exact hInt.mul_continuousOn
      hKernelCont.continuousOn isCompact_Icc
  calc
    ‖movingGaussianFilteredMode Ck R carrier x‖
        ≤ ∫ y in Set.Icc (-c) c,
            ‖carrier.h y
              * movingGaussianPhysicalKernel Ck R (x - y)‖ := by
      unfold movingGaussianFilteredMode
      exact norm_integral_le_integral_norm _
    _ ≤ ∫ y in Set.Icc (-c) c,
          Kx * ‖carrier.h y‖ := by
      refine setIntegral_mono_ae_restrict
        hProd.norm
        (hInt.norm.const_mul Kx) ?_
      filter_upwards [self_mem_ae_restrict measurableSet_Icc] with y hy
      rw [norm_mul]
      calc
        ‖carrier.h y‖
            * ‖movingGaussianPhysicalKernel Ck R (x - y)‖
            ≤ ‖carrier.h y‖ * Kx := by
              apply mul_le_mul_of_nonneg_left
              · exact movingGaussianPhysicalKernel_norm_le_exteriorEnvelope
                  hR hc residual.strict hx hy
              · exact norm_nonneg _
        _ = Kx * ‖carrier.h y‖ := by ring
    _ = Kx * neutralPhysicalCompactL1Mass carrier := by
      rw [integral_const_mul]
      rfl
    _ = (‖Ck‖ * Real.sqrt R
          * gaussianSupportEnvelope R c x)
          * neutralPhysicalCompactL1Mass carrier := by
      rfl

/--
Completion-of-the-square inequality that absorbs the residual's fixed
exponential growth into half of the Gaussian decay while extracting a uniform
collar exponential in the moving parameter.
-/
theorem gaussianTailCompletion_bound
    {κ R c a x : ℝ}
    (hκ : 0 ≤ κ)
    (hR : 0 ≤ R)
    (hc : 0 ≤ c)
    (hca : c < a)
    (hlarge : 8 * κ ≤ R * (a - c))
    (hx : x ∉ Set.Ioo (-a) a) :
    Real.exp (κ * |x|)
        * gaussianSupportEnvelope R c x
      ≤
    Real.exp (κ * c)
      * Real.exp (-R * (a - c) ^ 2 / 16)
      * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
  have hgap :
      a - c ≤ |x| - c :=
    supportGap_le_abs_sub hc hca hx
  have hδ0 : 0 ≤ a - c := sub_nonneg.mpr (le_of_lt hca)
  have hd0 : 0 ≤ |x| - c := hδ0.trans hgap
  have hRδd :
      R * (a - c) ≤ R * (|x| - c) :=
    mul_le_mul_of_nonneg_left hgap hR
  have hklinear :
      8 * κ ≤ R * (|x| - c) :=
    hlarge.trans hRδd
  have hkquad :
      8 * κ * (|x| - c)
        ≤ R * (|x| - c) ^ 2 := by
    nlinarith
  have hsq :
      (a - c) ^ 2 ≤ (|x| - c) ^ 2 := by
    nlinarith
  unfold gaussianSupportEnvelope
  calc
    Real.exp (κ * |x|)
        * Real.exp (-R * (|x| - c) ^ 2 / 4)
        =
      Real.exp
        (κ * |x| - R * (|x| - c) ^ 2 / 4) := by
          rw [← Real.exp_add]
          congr 1
          ring
    _ ≤ Real.exp
        (κ * c
          - R * (a - c) ^ 2 / 16
          - R * (|x| - c) ^ 2 / 16) := by
          apply Real.exp_le_exp.mpr
          nlinarith
    _ =
      Real.exp (κ * c)
        * Real.exp (-R * (a - c) ^ 2 / 16)
        * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
          rw [← Real.exp_add, ← Real.exp_add]
          congr 1
          ring

/--
The remaining physical Gaussian tail after completion is integrable on the
two exterior half-lines.
-/
theorem gaussianExteriorTail_integrableOn
    {R c a : ℝ}
    (hR : 0 < R)
    (hc : 0 ≤ c)
    (hca : c < a) :
    IntegrableOn
      (fun x : ℝ =>
        Real.exp (-R * (|x| - c) ^ 2 / 16))
      (gaussianExteriorSet a) volume := by
  have ha : 0 < a := lt_of_le_of_lt hc hca
  have hb : 0 < R / 16 := by positivity
  have hbase :
      Integrable
        (fun t : ℝ =>
          Real.exp (-(R / 16) * t ^ 2)) :=
    integrable_exp_neg_mul_sq hb
  have hright :
      IntegrableOn
        (fun x : ℝ =>
          Real.exp (-R * (|x| - c) ^ 2 / 16))
        (Set.Ici a) volume := by
    have hshift :
        Integrable
          (fun x : ℝ =>
            Real.exp (-(R / 16) * (x - c) ^ 2)) := by
      convert hbase.comp_sub_right c using 1 <;> ring
    refine (integrableOn_congr_fun ?_ measurableSet_Ici).2
      hshift.integrableOn
    intro x hx
    have hx0 : 0 ≤ x := ha.le.trans hx
    rw [abs_of_nonneg hx0]
    congr 1
    ring
  have hleft :
      IntegrableOn
        (fun x : ℝ =>
          Real.exp (-R * (|x| - c) ^ 2 / 16))
        (Set.Iic (-a)) volume := by
    have hshift :
        Integrable
          (fun x : ℝ =>
            Real.exp (-(R / 16) * (x + c) ^ 2)) := by
      convert hbase.comp_sub_right (-c) using 1 <;> ring
    refine (integrableOn_congr_fun ?_ measurableSet_Iic).2
      hshift.integrableOn
    intro x hx
    have hx0 : x ≤ 0 := hx.trans (neg_nonpos.mpr ha.le)
    rw [abs_of_nonpos hx0]
    congr 1
    ring
  exact hleft.union hright

end

end WeilDefect
