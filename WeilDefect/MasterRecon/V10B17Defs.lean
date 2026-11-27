import WeilDefect.MasterRecon.V10B13a
import WeilDefect.MasterRecon.V10B8c

/-! Original V10B17a/V10B17b declarations, factored to separate the
retained-bank data from the historical analytic tail proof. Bodies and
qualified names are preserved verbatim. -/
namespace WeilDefect.MasterRecon.V10B17a

open V08I (logCarrier)

noncomputable def poleDifference (t : ℝ) (ht : 0 ≤ t) : logCarrier t →L[ℂ] ℂ :=
  V10B8c.eval t (1/2) ht - V10B8c.eval t (-1/2) ht

end WeilDefect.MasterRecon.V10B17a

namespace WeilDefect.MasterRecon.V10B17b

open scoped InnerProduct
open V08I (logCarrier)
open V10B13a (moment)
open V10B17a (poleDifference)

noncomputable def bank : Fin 15 ⊕ Unit → logCarrier (1/4) :=
  Sum.elim (fun j => (moment (1/4) (by norm_num) j.val).adjoint 1)
    (fun _ => (poleDifference (1/4) (by norm_num)).adjoint 1)

noncomputable def retained : Submodule ℂ (logCarrier (1/4)) :=
  Submodule.span ℂ (Set.range bank)

end WeilDefect.MasterRecon.V10B17b
