import WeilDefect.MasterRecon.V10B75b
import WeilDefect.MasterRecon.V10B15a
import WeilDefect.MasterRecon.V10B17a

/-! V10B76a: isolate the exact residual receiver at the historical
budget 24. Scalar central series and vertical Stirling remain explicit;
no external theorem or historical matrix provenance is adopted. -/
namespace WeilDefect.MasterRecon.V10B76a
open MeasureTheory

theorem residual_measurable : Measurable V10B8e.residual :=
  V10B8f.residual_continuous.measurable

theorem residual_tail_24 (hV : V10B8f.VerticalStirling) (u : ℝ)
    (hu : 1/2 ≤ |-Real.pi*u|) : |V10B8e.residual u| ≤ 24 := by
  exact (V10B8f.tail_residual hV u hu).trans V10B17a.globalBudget_le_24

theorem residual_central_24 (hS : V10B15a.CentralSeries) (u : ℝ)
    (hu : |-Real.pi*u| ≤ 1/2) : |V10B8e.residual u| ≤ 24 :=
  (V10B15a.central_residual hS u hu).trans V10B17a.globalBudget_le_24

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

#print axioms WeilDefect.MasterRecon.V10B76a.residual_measurable
#print axioms WeilDefect.MasterRecon.V10B76a.residual_tail_24
#print axioms WeilDefect.MasterRecon.V10B76a.residual_central_24
#print axioms WeilDefect.MasterRecon.V10B76a.residual_uniform_24
#print axioms WeilDefect.MasterRecon.V10B76a.residual_receiver
