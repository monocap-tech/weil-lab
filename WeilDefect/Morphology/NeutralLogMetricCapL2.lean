import WeilDefect.Morphology.NeutralLogMetricEndpointL2
import Mathlib.MeasureTheory.Group.Measure

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- The left endpoint tail is L2 on the physical cap interior. -/
theorem neutralLogMetricEndpointTail_left_memLp_two (B : ℝ) (hB : 0 ≤ B) :
    MemLp (fun x : ℝ => neutralLogMetricEndpointTail (B - x)) 2
      (volume.restrict (Ioo (-B) B)) := by
  have hr : MeasurePreserving (fun x : ℝ => B - x) volume volume := by
    simpa [Function.comp_def, sub_eq_add_neg] using
      (measurePreserving_add_left (volume : Measure ℝ) B).comp
        (Measure.measurePreserving_neg (volume : Measure ℝ))
  have hp := hr.restrict_preimage
    (measurableSet_Ioc : MeasurableSet (Ioc (0 : ℝ) (2 * B)))
  have ht := (neutralLogMetricEndpointTail_memLp_two (2 * B) (by positivity)).comp_measurePreserving hp
  apply ht.mono_measure
  apply Measure.restrict_mono _ le_rfl
  intro x hx
  change 0 < B - x ∧ B - x ≤ 2 * B
  constructor <;> linarith [hx.1, hx.2]

/-- The right endpoint tail is L2 on the same physical cap interior. -/
theorem neutralLogMetricEndpointTail_right_memLp_two (B : ℝ) (hB : 0 ≤ B) :
    MemLp (fun x : ℝ => neutralLogMetricEndpointTail (B + x)) 2
      (volume.restrict (Ioo (-B) B)) := by
  have hp := (measurePreserving_add_left (volume : Measure ℝ) B).restrict_preimage
    (measurableSet_Ioc : MeasurableSet (Ioc (0 : ℝ) (2 * B)))
  have ht := (neutralLogMetricEndpointTail_memLp_two (2 * B) (by positivity)).comp_measurePreserving hp
  apply ht.mono_measure
  apply Measure.restrict_mono _ le_rfl
  intro x hx
  change 0 < B + x ∧ B + x ≤ 2 * B
  constructor <;> linarith [hx.1, hx.2]

/-- Both genuine exterior tails are retained in the physical L2 function. -/
theorem neutralLogMetricExteriorSource_memLp_two (B : ℝ) (hB : 0 ≤ B) :
    MemLp (neutralLogMetricExteriorSource B) 2 (volume.restrict (Ioo (-B) B)) := by
  exact (neutralLogMetricEndpointTail_left_memLp_two B hB).add
    (neutralLogMetricEndpointTail_right_memLp_two B hB)

/-- Bounded trials preserve L2 control of the actual exterior source term. -/
theorem neutralLogMetricExteriorProduct_memLp_two
    (B M : ℝ) (hB : 0 ≤ B) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M) :
    MemLp (fun x : ℝ => v x * (neutralLogMetricExteriorSource B x : ℂ)) 2
      (volume.restrict (Ioo (-B) B)) := by
  have hg := (neutralLogMetricExteriorSource_memLp_two B hB).const_mul M
  apply hg.mono' ((hv.mul (Complex.continuous_ofReal.measurable.comp
    (neutralLogMetricExteriorSource_measurable B))).aestronglyMeasurable)
  filter_upwards [ae_restrict_mem measurableSet_Ioo] with x hx
  change ‖v x * (neutralLogMetricExteriorSource B x : ℂ)‖ ≤
    M * neutralLogMetricExteriorSource B x
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (neutralLogMetricExteriorSource_nonnegative B x)]
  exact mul_le_mul_of_nonneg_right
    (hbound x ⟨hx.1.le, hx.2.le⟩) (neutralLogMetricExteriorSource_nonnegative B x)

/-- The complete endpoint candidate is L2 on the cap for bounded measurable
trials with an explicit Lipschitz modulus. Weak source identity remains separate. -/
theorem neutralLogMetricEndpointCandidate_memLp_two
    (B M L : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) :
    MemLp (neutralLogMetricEndpointCandidate B v) 2
      (volume.restrict (Ioo (-B) B)) := by
  have hv2 : MemLp v 2 (volume.restrict (Ioo (-B) B)) := by
    apply MemLp.of_bound hv.aestronglyMeasurable M
    filter_upwards [ae_restrict_mem measurableSet_Ioo] with x hx
    exact hbound x ⟨hx.1.le, hx.2.le⟩
  have hj2 : MemLp (fun x : ℝ => ∫ y in Icc (-B) B,
      (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)) 2
      (volume.restrict (Ioo (-B) B)) := by
    apply MemLp.of_bound
      (neutralLogMetricJumpIntegral_measurable B v hv).aestronglyMeasurable (2 * B * L)
    filter_upwards [ae_restrict_mem measurableSet_Ioo] with x hx
    exact neutralLogMetricJumpDifference_integral_norm_le B x L hB v hv hL
      (hmod x ⟨hx.1.le, hx.2.le⟩)
  exact (hv2.add hj2).add (neutralLogMetricExteriorProduct_memLp_two B M hB v hv hbound)

end
end WeilDefect
