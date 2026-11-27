import WeilDefect.MasterRecon.V10B17b
import WeilDefect.MasterRecon.V10B14a

/-! Numerical transport budget for the small-support pilot.
Uses the exact L1 inclusion and zero-band embedding, not a fitted norm. -/
namespace WeilDefect.MasterRecon.V10B17c

open MeasureTheory Set
open scoped FourierTransform ENNReal
open V08I (FullL2 logCarrier physicalInclusion)
open V10B13a (input out)

theorem physical_norm (t : ℝ) (g : logCarrier t) :
    ‖physicalInclusion t g‖ ≤ (Real.sqrt (Real.log 2))⁻¹*‖g‖ := by
  change ‖(Lp.fourierTransformₗᵢ ℝ ℂ).symm (V08I.unweight (g:FullL2))‖ ≤ _
  rw [(Lp.fourierTransformₗᵢ ℝ ℂ).symm.norm_map]
  exact V08I.mulValue_bound _ _ _ _ (g:FullL2)

theorem pilot_input_norm : ‖input (1/4)‖ ≤ 1 := by
  apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
  intro g
  let μ := V08K.supportMeasure (1/4)
  let f := V08K.restrictPhysical (1/4) (physicalInclusion (1/4) g)
  have h := V08F.physicalL1Value_bound μ f
  have hμ : μ univ = ENNReal.ofReal (1/2) := by
    simp [μ,V08K.supportMeasure,Measure.restrict_apply_univ,Real.volume_Icc]
    norm_num
  rw [hμ,ENNReal.toReal_rpow,ENNReal.toReal_ofReal (by norm_num),← Real.sqrt_eq_rpow] at h
  have hf := V10B14a.restrict_norm (1/4) (physicalInclusion (1/4) g)
  have hj := physical_norm (1/4) g
  have hlog : (1/2:ℝ) ≤ Real.log 2 := by linarith [Real.log_two_gt_d9]
  have hrat : Real.sqrt (1/2) * (Real.sqrt (Real.log 2))⁻¹ ≤ 1 := by
    rw [← div_eq_mul_inv]
    exact (div_le_one (Real.sqrt_pos.2 (by positivity))).mpr (Real.sqrt_le_sqrt hlog)
  change ‖V08F.physicalL1Value μ f‖ ≤ 1*‖g‖
  calc
    _ ≤ Real.sqrt (1/2)*‖f‖ := h
    _ ≤ Real.sqrt (1/2)*‖physicalInclusion (1/4) g‖ :=
      mul_le_mul_of_nonneg_left hf (Real.sqrt_nonneg _)
    _ ≤ Real.sqrt (1/2)*((Real.sqrt (Real.log 2))⁻¹*‖g‖) :=
      mul_le_mul_of_nonneg_left hj (Real.sqrt_nonneg _)
    _ ≤ _ := by rw [← mul_assoc]; exact mul_le_mul_of_nonneg_right hrat (norm_nonneg _)

local instance bandCompact (R : ℝ) : CompactSpace (V08E.Band R) :=
  compactSpace_Icc (-R) R

theorem pilot_output_norm : ‖out 3 (by norm_num)‖ ≤ Real.sqrt 6 := by
  apply ContinuousLinearMap.opNorm_le_bound _ (Real.sqrt_nonneg _)
  intro g
  let f := g.comp (V08K.scaleBand 3)
  have h := V08G.zeroBandValue_bound volume 3 (by norm_num)
    isCompact_Icc.measure_lt_top.ne f
  have hμ : (volume : Measure ℝ).real (Icc (-3:ℝ) 3) = 6 := by
    simp [Measure.real,Real.volume_Icc]
    norm_num
  rw [hμ,show (1/(2:ℝ≥0∞).toReal:ℝ)=1/2 by norm_num,← Real.sqrt_eq_rpow] at h
  have hf : ‖f‖ ≤ ‖g‖ := by
    apply (ContinuousMap.norm_le _ (norm_nonneg g)).mpr
    intro u
    exact g.norm_coe_le_norm _
  change ‖(Lp.fourierTransformₗᵢ ℝ ℂ).symm
    (V08G.zeroBandValue volume 3 (by norm_num) isCompact_Icc.measure_lt_top.ne f)‖ ≤ _
  rw [(Lp.fourierTransformₗᵢ ℝ ℂ).symm.norm_map]
  exact h.trans (mul_le_mul_of_nonneg_left hf (Real.sqrt_nonneg _))

theorem pilot_transport :
    (‖out 3 (by norm_num)‖*‖input (1/4)‖)^2 ≤ 6 := by
  have h := mul_le_mul pilot_output_norm pilot_input_norm (norm_nonneg _) (Real.sqrt_nonneg _)
  rw [mul_one] at h
  have hs := (sq_le_sq₀ (by positivity) (Real.sqrt_nonneg _)).mpr h
  rwa [Real.sq_sqrt (by norm_num)] at hs

end WeilDefect.MasterRecon.V10B17c

#print axioms WeilDefect.MasterRecon.V10B17c.physical_norm
#print axioms WeilDefect.MasterRecon.V10B17c.pilot_input_norm
#print axioms WeilDefect.MasterRecon.V10B17c.pilot_output_norm
#print axioms WeilDefect.MasterRecon.V10B17c.pilot_transport
