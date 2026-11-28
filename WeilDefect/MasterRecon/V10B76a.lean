import WeilDefect.MasterRecon.V10B15a
import Mathlib.Analysis.Complex.ExponentialBounds

/-! V10B76a: isolate the exact residual receiver at the historical
budget 24. Scalar central series and vertical Stirling remain explicit;
no external theorem or historical matrix provenance is adopted. -/
namespace WeilDefect.MasterRecon.V10B76a
open MeasureTheory

/- Exact proof extracted from V10B17a; no signed-symbol dependency. -/
theorem globalBudget_le_24 : V10B15a.globalBudget ≤ 24 := by
  have hp : 0 ≤ Real.log Real.pi := Real.log_nonneg (by linarith [Real.pi_gt_three])
  have h4 : Real.log Real.pi ≤ 2*Real.log 2 := by
    have h := Real.log_le_log Real.pi_pos (by linarith [Real.pi_lt_d2] : Real.pi ≤ 4)
    have he : Real.log (4:ℝ) = 2*Real.log 2 := by
      rw [show (4:ℝ) = 2*2 by norm_num,Real.log_mul (by norm_num) (by norm_num)]
      ring
    rwa [he] at h
  have h6 : Real.log (6:ℝ) = Real.log 2+Real.log 3 := by
    rw [show (6:ℝ) = 2*3 by norm_num,Real.log_mul (by norm_num) (by norm_num)]
  unfold V10B15a.globalBudget
  rw [abs_of_nonneg hp,h6]
  linarith [Real.log_two_lt_d9,Real.log_three_lt_d9]

theorem residual_measurable : Measurable V10B8e.residual :=
  V10B8f.residual_continuous.measurable

theorem residual_tail_24 (hV : V10B8f.VerticalStirling) (u : ℝ)
    (hu : 1/2 ≤ |-Real.pi*u|) : |V10B8e.residual u| ≤ 24 := by
  exact (V10B8f.tail_residual hV u hu).trans globalBudget_le_24

theorem residual_central_24 (hS : V10B15a.CentralSeries) (u : ℝ)
    (hu : |-Real.pi*u| ≤ 1/2) : |V10B8e.residual u| ≤ 24 :=
  (V10B15a.central_residual hS u hu).trans globalBudget_le_24

theorem residual_uniform_24 (hS : V10B15a.CentralSeries)
    (hV : V10B8f.VerticalStirling) : ∀ u, |V10B8e.residual u| ≤ 24 := by
  intro u
  by_cases hu : |-Real.pi*u| ≤ 1/2
  · exact residual_central_24 hS u hu
  · exact residual_tail_24 hV u (le_of_lt (lt_of_not_ge hu))

theorem residual_receiver (hS : V10B15a.CentralSeries)
    (hV : V10B8f.VerticalStirling) : V10B8e.ResidualEstimate :=
  ⟨residual_measurable,24,by norm_num,residual_uniform_24 hS hV⟩

end WeilDefect.MasterRecon.V10B76a

#print axioms WeilDefect.MasterRecon.V10B76a.globalBudget_le_24
#print axioms WeilDefect.MasterRecon.V10B76a.residual_measurable
#print axioms WeilDefect.MasterRecon.V10B76a.residual_tail_24
#print axioms WeilDefect.MasterRecon.V10B76a.residual_central_24
#print axioms WeilDefect.MasterRecon.V10B76a.residual_uniform_24
#print axioms WeilDefect.MasterRecon.V10B76a.residual_receiver
