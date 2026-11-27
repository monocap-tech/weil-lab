import WeilDefect.MasterRecon.V08J
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-! V10B9a: compare F08's original logarithmic weight with RECON's
angular logarithmic weight in the SAME Mathlib Fourier coordinate.
The old carrier approximation is received as a physical-domain theorem,
so no source from a different branch is silently imported. -/
namespace WeilDefect.MasterRecon.V10B9a

open MeasureTheory Set
open scoped FourierTransform
open V08I (FullL2 logCarrier physicalInclusion logWeight)

noncomputable def oldWeight (u : ℝ) : ℝ := Real.log (Real.exp 1+|u|)

theorem oldWeight_one (u : ℝ) : 1 ≤ oldWeight u := by
  unfold oldWeight
  rw [Real.le_log_iff_exp_le (by positivity)]
  linarith [abs_nonneg u]

theorem oldWeight_continuous : Continuous oldWeight := by
  unfold oldWeight
  apply Continuous.log (by fun_prop)
  intro u
  positivity

noncomputable def forwardConstant : ℝ := 1+Real.log (2+2*Real.pi)

noncomputable def reverseConstant : ℝ := 1+1/Real.log 2

theorem forwardConstant_pos : 0 < forwardConstant := by
  unfold forwardConstant
  have h : 0 ≤ Real.log (2+2*Real.pi) := Real.log_nonneg (by linarith [Real.pi_pos])
  linarith

theorem reverseConstant_pos : 0 < reverseConstant := by
  unfold reverseConstant
  have h : 0 < Real.log 2 := Real.log_pos (by norm_num)
  positivity

theorem weight_forward (u : ℝ) : logWeight u ≤ forwardConstant*oldWeight u := by
  have he : 1 ≤ Real.exp 1 := by
    linarith [Real.add_one_le_exp (1:ℝ)]
  have hp : 0 < 2*Real.pi := by positivity
  have hprod : 2+|2*Real.pi*u| ≤ (2+2*Real.pi)*(Real.exp 1+|u|) := by
    rw [abs_mul,abs_of_pos hp]
    nlinarith [mul_nonneg (show 0 ≤ Real.exp 1-1 by linarith) (show 0 ≤ 2*Real.pi by positivity),
      abs_nonneg u]
  have h := Real.log_le_log (by positivity : 0 < 2+|2*Real.pi*u|) hprod
  rw [Real.log_mul (by positivity) (by positivity)] at h
  have hc : 0 ≤ Real.log (2+2*Real.pi) := Real.log_nonneg (by linarith [Real.pi_pos])
  unfold logWeight forwardConstant oldWeight at *
  nlinarith [mul_nonneg hc (show 0 ≤ Real.log (Real.exp 1+|u|)-1 by
    exact sub_nonneg.mpr (oldWeight_one u))]

theorem weight_reverse (u : ℝ) : oldWeight u ≤ reverseConstant*logWeight u := by
  have hp : 1 ≤ 2*Real.pi := by linarith [Real.pi_gt_three]
  have he : 1 ≤ Real.exp 1 := by linarith [Real.add_one_le_exp (1:ℝ)]
  have hprod : Real.exp 1+|u| ≤ Real.exp 1*(2+|2*Real.pi*u|) := by
    rw [abs_mul,abs_of_nonneg (by linarith : 0 ≤ 2*Real.pi)]
    have hx : |u| ≤ 2*Real.pi*|u| := by nlinarith [abs_nonneg u]
    have hy : 0 ≤ 2*Real.pi*|u| := by positivity
    nlinarith [mul_nonneg (show 0 ≤ Real.exp 1-1 by linarith) hy]
  have h := Real.log_le_log (by positivity : 0 < Real.exp 1+|u|) hprod
  rw [Real.log_mul (by positivity) (by positivity),Real.log_exp] at h
  have hl : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hq : 1 ≤ (1/Real.log 2)*logWeight u := by
    rw [div_mul_eq_mul_div,one_mul,le_div_iff₀ hl,one_mul]
    exact V08I.logWeight_lower u
  unfold oldWeight reverseConstant
  change Real.log (Real.exp 1+|u|) ≤ _
  change Real.log (Real.exp 1+|u|) ≤ 1+logWeight u at h
  nlinarith only [h,hq]

noncomputable def oldDensity (f : FullL2) (u : ℝ) : ℝ :=
  oldWeight u*‖(𝓕 f : FullL2) u‖^2

noncomputable def newDensity (f : FullL2) (u : ℝ) : ℝ :=
  logWeight u*‖(𝓕 f : FullL2) u‖^2

theorem oldDensity_measurable (f : FullL2) :
    AEStronglyMeasurable (oldDensity f) volume :=
  oldWeight_continuous.aestronglyMeasurable.mul
    ((Lp.aestronglyMeasurable (𝓕 f : FullL2)).norm.pow 2)

theorem newDensity_measurable (f : FullL2) :
    AEStronglyMeasurable (newDensity f) volume :=
  V08I.logWeight_continuous.aestronglyMeasurable.mul
    ((Lp.aestronglyMeasurable (𝓕 f : FullL2)).norm.pow 2)

theorem oldDensity_nonneg (f : FullL2) (u : ℝ) : 0 ≤ oldDensity f u :=
  mul_nonneg (by linarith [oldWeight_one u]) (sq_nonneg _)

theorem newDensity_nonneg (f : FullL2) (u : ℝ) : 0 ≤ newDensity f u :=
  mul_nonneg (V08I.logWeight_pos u).le (sq_nonneg _)

theorem newDensity_le (f : FullL2) (u : ℝ) :
    newDensity f u ≤ forwardConstant*oldDensity f u := by
  unfold newDensity oldDensity
  rw [← mul_assoc]
  exact mul_le_mul_of_nonneg_right (weight_forward u) (sq_nonneg _)

theorem oldDensity_le (f : FullL2) (u : ℝ) :
    oldDensity f u ≤ reverseConstant*newDensity f u := by
  unfold newDensity oldDensity
  rw [← mul_assoc]
  exact mul_le_mul_of_nonneg_right (weight_reverse u) (sq_nonneg _)

theorem integrable_old_iff_new (f : FullL2) :
    Integrable (oldDensity f) ↔ Integrable (newDensity f) := by
  constructor
  · intro h
    apply (h.const_mul forwardConstant).mono' (newDensity_measurable f)
    filter_upwards with u
    rw [Real.norm_eq_abs,abs_of_nonneg (newDensity_nonneg f u)]
    exact newDensity_le f u
  · intro h
    apply (h.const_mul reverseConstant).mono' (oldDensity_measurable f)
    filter_upwards with u
    rw [Real.norm_eq_abs,abs_of_nonneg (oldDensity_nonneg f u)]
    exact oldDensity_le f u

theorem energy_forward (f : FullL2) (hf : Integrable (oldDensity f)) :
    (∫ u, newDensity f u) ≤ forwardConstant*(∫ u, oldDensity f u) := by
  rw [← integral_const_mul]
  exact integral_mono ((integrable_old_iff_new f).mp hf) (hf.const_mul _) (newDensity_le f)

theorem energy_reverse (f : FullL2) (hf : Integrable (newDensity f)) :
    (∫ u, oldDensity f u) ≤ reverseConstant*(∫ u, newDensity f u) := by
  rw [← integral_const_mul]
  exact integral_mono ((integrable_old_iff_new f).mpr hf) (hf.const_mul _) (oldDensity_le f)

end WeilDefect.MasterRecon.V10B9a

#print axioms WeilDefect.MasterRecon.V10B9a.oldWeight_one
#print axioms WeilDefect.MasterRecon.V10B9a.oldWeight_continuous
#print axioms WeilDefect.MasterRecon.V10B9a.forwardConstant_pos
#print axioms WeilDefect.MasterRecon.V10B9a.reverseConstant_pos
#print axioms WeilDefect.MasterRecon.V10B9a.weight_forward
#print axioms WeilDefect.MasterRecon.V10B9a.weight_reverse
#print axioms WeilDefect.MasterRecon.V10B9a.oldDensity_measurable
#print axioms WeilDefect.MasterRecon.V10B9a.newDensity_measurable
#print axioms WeilDefect.MasterRecon.V10B9a.oldDensity_nonneg
#print axioms WeilDefect.MasterRecon.V10B9a.newDensity_nonneg
#print axioms WeilDefect.MasterRecon.V10B9a.newDensity_le
#print axioms WeilDefect.MasterRecon.V10B9a.oldDensity_le
#print axioms WeilDefect.MasterRecon.V10B9a.integrable_old_iff_new
#print axioms WeilDefect.MasterRecon.V10B9a.energy_forward
#print axioms WeilDefect.MasterRecon.V10B9a.energy_reverse
