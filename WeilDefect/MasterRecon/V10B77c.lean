import WeilDefect.MasterRecon.V10B77a
import WeilDefect.MasterRecon.V10B77b
import WeilDefect.MasterRecon.V10B76a

/-! V10B77c: close the original residual receiver only after both
independently audited scalar suppliers pass. -/
namespace WeilDefect.MasterRecon.V10B77c

theorem residual_uniform_24 : ∀ u, |V10B8e.residual u| ≤ 24 :=
  V10B76a.residual_uniform_24 V10B77a.central_series V10B77b.vertical_stirling

theorem residual_estimate : V10B8e.ResidualEstimate :=
  V10B76a.residual_receiver V10B77a.central_series V10B77b.vertical_stirling

end WeilDefect.MasterRecon.V10B77c

#print axioms WeilDefect.MasterRecon.V10B77c.residual_uniform_24
#print axioms WeilDefect.MasterRecon.V10B77c.residual_estimate
