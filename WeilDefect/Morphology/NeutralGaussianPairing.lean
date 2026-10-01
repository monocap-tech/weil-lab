import WeilDefect.Morphology.NeutralGaussianTail
import Mathlib.Analysis.Convolution
import Mathlib.Tactic

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap
open Set

/-- The certified compactly supported F-1 representative is globally integrable. -/
theorem neutralPhysicalRepresentative_integrable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    Integrable carrier.h volume := by
  exact
    (neutralPhysicalRepresentative_integrableOn carrier).integrable_of_forall_notMem_eq_zero
      (fun x hx =>
        carrier.representative_eq_zero_of_not_mem hx)

/-- The convention-parametric moving Gaussian physical kernel is continuous. -/
theorem movingGaussianPhysicalKernel_continuous
    (Ck : ℂ) (R : ℝ) :
    Continuous (movingGaussianPhysicalKernel Ck R) := by
  unfold movingGaussianPhysicalKernel
  fun_prop

/--
For nonnegative R, the moving Gaussian kernel is uniformly bounded by
||Ck|| * sqrt R.
-/
theorem movingGaussianPhysicalKernel_norm_le
    {Ck : ℂ} {R z : ℝ}
    (hR : 0 ≤ R) :
    ‖movingGaussianPhysicalKernel Ck R z‖
      ≤ ‖Ck‖ * Real.sqrt R := by
  rw [norm_movingGaussianPhysicalKernel Ck R z hR]
  have hexp :
      Real.exp (-R * |z| ^ 2 / 4) ≤ 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_le_exp.mpr
    have hnonneg : 0 ≤ R * |z| ^ 2 / 4 := by positivity
    linarith
  exact mul_le_of_le_one_right
    (mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R))
    hexp

/-- The moving Gaussian kernel has bounded norm range. -/
theorem movingGaussianPhysicalKernel_bddAbove_norm
    {Ck : ℂ} {R : ℝ}
    (hR : 0 ≤ R) :
    BddAbove
      (Set.range
        (fun z : ℝ =>
          ‖movingGaussianPhysicalKernel Ck R z‖)) := by
  refine ⟨‖Ck‖ * Real.sqrt R, ?_⟩
  rintro _ ⟨z, rfl⟩
  exact movingGaussianPhysicalKernel_norm_le hR

/--
The compact-support definition of the filtered mode agrees with ordinary
whole-line convolution because the certified representative vanishes outside
[-c,c].
-/
theorem movingGaussianFilteredMode_eq_convolution
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (Ck : ℂ) (R : ℝ) :
    movingGaussianFilteredMode Ck R carrier
      =
    MeasureTheory.convolution
      carrier.h
      (movingGaussianPhysicalKernel Ck R)
      (lsmul ℂ ℂ)
      volume := by
  funext x
  unfold movingGaussianFilteredMode
  rw [MeasureTheory.convolution_def]
  simp only [lsmul_apply, smul_eq_mul]
  apply setIntegral_eq_integral_of_forall_compl_eq_zero
  intro y hy
  rw [carrier.representative_eq_zero_of_not_mem hy]
  simp

/-- The actual filtered F-1 mode is continuous in the physical variable. -/
theorem movingGaussianFilteredMode_continuous
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (Ck : ℂ) {R : ℝ}
    (hR : 0 ≤ R) :
    Continuous (movingGaussianFilteredMode Ck R carrier) := by
  rw [movingGaussianFilteredMode_eq_convolution carrier Ck R]
  exact
    (movingGaussianPhysicalKernel_bddAbove_norm hR).continuous_convolution_right_of_integrable
      (lsmul ℂ ℂ)
      (neutralPhysicalRepresentative_integrable carrier)
      (movingGaussianPhysicalKernel_continuous Ck R)

/--
Pointwise completed-tail bound for the actual residual-filtered-mode product.
-/
theorem residualFilteredMode_norm_le_completedTail
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) {R x : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 ≤ R)
    (hlarge :
      8 * residual.growthRate
        ≤ R * (residual.a - c))
    (hx : x ∉ Set.Ioo (-residual.a) residual.a) :
    ‖residual.q x
        * movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (residual.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (residual.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16))
      * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
  have hfiltered :=
    movingGaussianFilteredMode_norm_le_exteriorEnvelope
      carrier residual Ck R x hc hR hx
  have hcompletion :=
    gaussianTailCompletion_bound
      residual.growthRate_nonneg hR hc residual.strict
      hlarge hx
  rw [norm_mul]
  calc
    ‖residual.q x‖
        * ‖movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (residual.growthConstant
      * Real.exp (residual.growthRate * |x|))
      *
    ((‖Ck‖ * Real.sqrt R
      * gaussianSupportEnvelope R c x)
      * neutralPhysicalCompactL1Mass carrier) := by
        exact mul_le_mul
          (residual.growth_bound x)
          hfiltered
          (norm_nonneg _)
          (mul_nonneg
            residual.growthConstant_nonneg
            (Real.exp_nonneg _))
    _ ≤
    (residual.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (residual.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16))
      * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
        have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
          mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
        have hnonneg :
            0 ≤ residual.growthConstant
              * (‖Ck‖ * Real.sqrt R)
              * neutralPhysicalCompactL1Mass carrier :=
          mul_nonneg
            (mul_nonneg residual.growthConstant_nonneg hkernel)
            (neutralPhysicalCompactL1Mass_nonneg carrier)
        nlinarith [hcompletion]

/--
The residual-filtered-mode product is integrable on the exterior once the
large-parameter condition for Gaussian completion holds.
-/
theorem residualFilteredMode_integrableOn_exterior
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge :
      8 * residual.growthRate
        ≤ R * (residual.a - c)) :
    IntegrableOn
      (fun x : ℝ =>
        residual.q x
          * movingGaussianFilteredMode Ck R carrier x)
      (gaussianExteriorSet residual.a) volume := by
  let A : ℝ :=
    residual.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (residual.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16)
  have hA : 0 ≤ A := by
    dsimp [A]
    have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
      mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
    have h₁ :
        0 ≤ residual.growthConstant
          * (‖Ck‖ * Real.sqrt R)
          * neutralPhysicalCompactL1Mass carrier :=
      mul_nonneg
        (mul_nonneg residual.growthConstant_nonneg hkernel)
        (neutralPhysicalCompactL1Mass_nonneg carrier)
    exact mul_nonneg
      (mul_nonneg h₁ (Real.exp_nonneg _))
      (Real.exp_nonneg _)
  have htail :
      IntegrableOn
        (fun x : ℝ =>
          A * Real.exp (-R * (|x| - c) ^ 2 / 16))
        (gaussianExteriorSet residual.a) volume :=
    (gaussianExteriorTail_integrableOn hR hc residual.strict).const_mul A
  have hfilteredMeas :
      AEStronglyMeasurable
        (movingGaussianFilteredMode Ck R carrier) volume :=
    (movingGaussianFilteredMode_continuous
      carrier Ck hR.le).aestronglyMeasurable
  have hpairMeas :
      AEStronglyMeasurable
        (fun x : ℝ =>
          residual.q x
            * movingGaussianFilteredMode Ck R carrier x) volume :=
    residual.q_locallyIntegrable.aestronglyMeasurable.mul
      hfilteredMeas
  apply Integrable.mono htail hpairMeas.restrict
  have hextMeas : MeasurableSet (gaussianExteriorSet residual.a) := by
    unfold gaussianExteriorSet
    exact measurableSet_Iic.union measurableSet_Ici
  filter_upwards [self_mem_ae_restrict hextMeas] with x hx
  have hxout :
      x ∉ Set.Ioo (-residual.a) residual.a := by
    rw [gaussianExteriorSet] at hx
    rcases hx with hxleft | hxright
    · exact fun hin => (not_lt_of_ge hxleft) hin.1
    · exact fun hin => (not_lt_of_ge hxright) hin.2
  have hbound :=
    residualFilteredMode_norm_le_completedTail
      carrier residual Ck hc hR.le hlarge hxout
  have htailNonneg :
      0 ≤ A * Real.exp (-R * (|x| - c) ^ 2 / 16) :=
    mul_nonneg hA (Real.exp_nonneg _)
  rw [Real.norm_eq_abs, abs_of_nonneg htailNonneg]
  simpa [A] using hbound

/--
The completed Gaussian tail mass on the two exterior half-lines is bounded by
two full translated Gaussian masses.
-/
theorem gaussianExteriorTail_integral_le
    {R c a : ℝ}
    (hR : 0 < R)
    (hc : 0 ≤ c)
    (hca : c < a) :
    ∫ x in gaussianExteriorSet a,
        Real.exp (-R * (|x| - c) ^ 2 / 16)
      ≤
    2 * Real.sqrt (Real.pi / (R / 16)) := by
  have ha : 0 < a := lt_of_le_of_lt hc hca
  have hb : 0 < R / 16 := by positivity
  have hbase :
      Integrable
        (fun t : ℝ =>
          Real.exp (-(R / 16) * t ^ 2)) :=
    integrable_exp_neg_mul_sq hb
  have hrightShift :
      Integrable
        (fun x : ℝ =>
          Real.exp (-(R / 16) * (x - c) ^ 2)) :=
    hbase.comp_sub_right c
  have hleftShift :
      Integrable
        (fun x : ℝ =>
          Real.exp (-(R / 16) * (x + c) ^ 2)) := by
    simpa only [sub_neg_eq_add] using
      hbase.comp_sub_right (-c)
  have hright :
      (∫ x in Set.Ici a,
        Real.exp (-R * (|x| - c) ^ 2 / 16))
        ≤ Real.sqrt (Real.pi / (R / 16)) := by
    calc
      (∫ x in Set.Ici a,
        Real.exp (-R * (|x| - c) ^ 2 / 16))
          =
      ∫ x in Set.Ici a,
        Real.exp (-(R / 16) * (x - c) ^ 2) := by
          apply setIntegral_congr_fun measurableSet_Ici
          intro x hx
          have hx0 : 0 ≤ x := ha.le.trans hx
          change
            Real.exp (-R * (|x| - c) ^ 2 / 16)
              =
            Real.exp (-(R / 16) * (x - c) ^ 2)
          rw [abs_of_nonneg hx0]
          congr 1
          ring
      _ ≤ ∫ x in Set.univ,
          Real.exp (-(R / 16) * (x - c) ^ 2) := by
            exact setIntegral_mono_set
              hrightShift.integrableOn
              (ae_of_all _ fun _ => Real.exp_nonneg _)
              (Set.subset_univ _).eventuallySubset
      _ = ∫ x : ℝ,
          Real.exp (-(R / 16) * (x - c) ^ 2) := by
            simp
      _ = ∫ t : ℝ,
          Real.exp (-(R / 16) * t ^ 2) := by
            exact
              integral_sub_right_eq_self
                (μ := volume)
                (fun t : ℝ => Real.exp (-(R / 16) * t ^ 2)) c
      _ = Real.sqrt (Real.pi / (R / 16)) :=
        integral_gaussian (R / 16)
  have hleft :
      (∫ x in Set.Iic (-a),
        Real.exp (-R * (|x| - c) ^ 2 / 16))
        ≤ Real.sqrt (Real.pi / (R / 16)) := by
    calc
      (∫ x in Set.Iic (-a),
        Real.exp (-R * (|x| - c) ^ 2 / 16))
          =
      ∫ x in Set.Iic (-a),
        Real.exp (-(R / 16) * (x + c) ^ 2) := by
          apply setIntegral_congr_fun measurableSet_Iic
          intro x hx
          have hx0 : x ≤ 0 :=
            hx.trans (neg_nonpos.mpr ha.le)
          change
            Real.exp (-R * (|x| - c) ^ 2 / 16)
              =
            Real.exp (-(R / 16) * (x + c) ^ 2)
          rw [abs_of_nonpos hx0]
          congr 1
          ring
      _ ≤ ∫ x in Set.univ,
          Real.exp (-(R / 16) * (x + c) ^ 2) := by
            exact setIntegral_mono_set
              hleftShift.integrableOn
              (ae_of_all _ fun _ => Real.exp_nonneg _)
              (Set.subset_univ _).eventuallySubset
      _ = ∫ x : ℝ,
          Real.exp (-(R / 16) * (x + c) ^ 2) := by
            simp
      _ = ∫ t : ℝ,
          Real.exp (-(R / 16) * t ^ 2) := by
            simpa only [sub_neg_eq_add] using
              integral_sub_right_eq_self
                (μ := volume)
                (fun t : ℝ =>
                  Real.exp (-(R / 16) * t ^ 2)) (-c)
      _ = Real.sqrt (Real.pi / (R / 16)) :=
        integral_gaussian (R / 16)
  have htail :=
    gaussianExteriorTail_integrableOn hR hc hca
  have hdisj :
      Disjoint (Set.Iic (-a)) (Set.Ici a) := by
    exact Set.Iic_disjoint_Ici.2 (by linarith)
  rw [gaussianExteriorSet,
    setIntegral_union hdisj measurableSet_Ici
      (htail.mono_set Set.subset_union_left)
      (htail.mono_set Set.subset_union_right)]
  linarith

/-- Whole-line physical pairing of the residual with the moving Gaussian filtered mode. -/
def movingGaussianResidualPairing
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) (R : ℝ) : ℂ :=
  ∫ x : ℝ,
    residual.q x
      * movingGaussianFilteredMode Ck R carrier x

/--
Final F-3 physical pairing estimate.

The whole-line pairing reduces a.e. to the exterior because the certified
residual vanishes on the strict enlarged interval.  The remaining exterior
integral is exponentially small in R up to the exact Gaussian mass factor.
-/
theorem movingGaussianResidualPairing_norm_le
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) {R : ℝ}
    (hc : 0 ≤ c)
    (hR : 0 < R)
    (hlarge :
      8 * residual.growthRate
        ≤ R * (residual.a - c)) :
    ‖movingGaussianResidualPairing carrier residual Ck R‖
      ≤
    (residual.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (residual.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16))
      *
    (2 * Real.sqrt (Real.pi / (R / 16))) := by
  let A : ℝ :=
    residual.growthConstant
      * (‖Ck‖ * Real.sqrt R)
      * neutralPhysicalCompactL1Mass carrier
      * Real.exp (residual.growthRate * c)
      * Real.exp (-R * (residual.a - c) ^ 2 / 16)
  let f : ℝ → ℂ :=
    fun x =>
      residual.q x
        * movingGaussianFilteredMode Ck R carrier x
  have hfext :
      IntegrableOn f (gaussianExteriorSet residual.a) volume :=
    residualFilteredMode_integrableOn_exterior
      carrier residual Ck hc hR hlarge
  have hfull_to_ext :
      (∫ x : ℝ, f x)
        =
      ∫ x in gaussianExteriorSet residual.a, f x := by
    symm
    apply setIntegral_eq_integral_of_ae_compl_eq_zero
    filter_upwards [residual.vanishes_ae] with x hx hnot
    have hin :
        x ∈ Set.Ioo (-residual.a) residual.a := by
      simp [gaussianExteriorSet] at hnot
      exact ⟨hnot.1, hnot.2⟩
    change
      residual.q x * movingGaussianFilteredMode Ck R carrier x = 0
    rw [hx hin, zero_mul]
  rw [movingGaussianResidualPairing, show
    (fun x : ℝ =>
      residual.q x
        * movingGaussianFilteredMode Ck R carrier x) = f by rfl,
    hfull_to_ext]
  calc
    ‖∫ x in gaussianExteriorSet residual.a, f x‖
      ≤ ∫ x in gaussianExteriorSet residual.a, ‖f x‖ := by
        exact norm_integral_le_integral_norm _
    _ ≤ ∫ x in gaussianExteriorSet residual.a,
          A * Real.exp (-R * (|x| - c) ^ 2 / 16) := by
        have hA : 0 ≤ A := by
          dsimp [A]
          have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
            mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
          have h₁ :
              0 ≤ residual.growthConstant
                * (‖Ck‖ * Real.sqrt R)
                * neutralPhysicalCompactL1Mass carrier :=
            mul_nonneg
              (mul_nonneg residual.growthConstant_nonneg hkernel)
              (neutralPhysicalCompactL1Mass_nonneg carrier)
          exact mul_nonneg
            (mul_nonneg h₁ (Real.exp_nonneg _))
            (Real.exp_nonneg _)
        refine setIntegral_mono_ae_restrict
          hfext.norm
          ((gaussianExteriorTail_integrableOn hR hc residual.strict).const_mul A) ?_
        have hextMeas : MeasurableSet (gaussianExteriorSet residual.a) := by
          unfold gaussianExteriorSet
          exact measurableSet_Iic.union measurableSet_Ici
        filter_upwards [self_mem_ae_restrict hextMeas] with x hx
        have hxout :
            x ∉ Set.Ioo (-residual.a) residual.a := by
          rw [gaussianExteriorSet] at hx
          rcases hx with hxleft | hxright
          · exact fun hin => (not_lt_of_ge hxleft) hin.1
          · exact fun hin => (not_lt_of_ge hxright) hin.2
        have hbound :=
          residualFilteredMode_norm_le_completedTail
            carrier residual Ck hc hR.le hlarge hxout
        simpa [f, A] using hbound
    _ =
      A * (∫ x in gaussianExteriorSet residual.a,
        Real.exp (-R * (|x| - c) ^ 2 / 16)) := by
          rw [← integral_const_mul]
    _ ≤
      A * (2 * Real.sqrt (Real.pi / (R / 16))) := by
        have hA : 0 ≤ A := by
          dsimp [A]
          have hkernel : 0 ≤ ‖Ck‖ * Real.sqrt R :=
            mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R)
          have h₁ :
              0 ≤ residual.growthConstant
                * (‖Ck‖ * Real.sqrt R)
                * neutralPhysicalCompactL1Mass carrier :=
            mul_nonneg
              (mul_nonneg residual.growthConstant_nonneg hkernel)
              (neutralPhysicalCompactL1Mass_nonneg carrier)
          exact mul_nonneg
            (mul_nonneg h₁ (Real.exp_nonneg _))
            (Real.exp_nonneg _)
        exact mul_le_mul_of_nonneg_left
          (gaussianExteriorTail_integral_le hR hc residual.strict) hA
    _ =
      (residual.growthConstant
        * (‖Ck‖ * Real.sqrt R)
        * neutralPhysicalCompactL1Mass carrier
        * Real.exp (residual.growthRate * c)
        * Real.exp (-R * (residual.a - c) ^ 2 / 16))
        *
      (2 * Real.sqrt (Real.pi / (R / 16))) := by
        rfl

end

end WeilDefect
