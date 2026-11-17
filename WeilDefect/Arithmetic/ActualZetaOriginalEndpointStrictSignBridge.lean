import WeilDefect.Arithmetic.ActualZetaOriginalEndpointNonzero
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointSignCheck

namespace WeilDefect
noncomputable section
open MeasureTheory

/-! NF601: no U400 or quantitative L2 lower bound is needed for
strict positivity of the original same-source endpoint graph.
Only the signed zeroth-order check, box custody and the universal
smooth support inequality are needed. Each remains explicit. -/

theorem neutralNF601NF407Graph_positive_of_endpointCheck
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b)
    (hcheck : neutralNF597EndpointCheck = true)
    (hlocal : neutralNF599SmoothCollarLower (2/5)) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      0 < neutralNF598GraphWeil (11/10) K := by
  have hneg := neutralNF597Endpoint_negative_of_check hcheck a b hbox
  have hB : neutralNF587Source a b (11/10) ≠ 0 := by
    exact ne_of_lt (hneg.trans (by norm_num))
  exact neutralNF601NF407Graph_positive a b (2/5) (by norm_num) hlocal hB

end
end WeilDefect
