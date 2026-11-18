import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard0
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard1
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard2
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard3
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard4
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard5
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard6
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard7
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointKernelShard8
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointReceiptCertifiedBase
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointStrictSignBridge
import WeilDefect.Arithmetic.ActualZetaOriginalCriticalSolveCustody

namespace WeilDefect
noncomputable section
open MeasureTheory
set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

/-! NF605: the complete original ENDPOINT checker, without a
native_decide assumption. All 275 individual checks were accepted
in NF603 CI twice. This source-level aggregation is a new proof
candidate, not yet a compiled theorem. -/

theorem neutralNF605AllSelected (j : Fin 242) :
    neutralNF602SelectedCheck j = true := by
  by_cases h0 : j.val < 32
  · exact neutralNF605SelectedShard0 j (by omega) h0
  ·
    by_cases h1 : j.val < 64
    · exact neutralNF605SelectedShard1 j (by omega) h1
    ·
      by_cases h2 : j.val < 96
      · exact neutralNF605SelectedShard2 j (by omega) h2
      ·
        by_cases h3 : j.val < 128
        · exact neutralNF605SelectedShard3 j (by omega) h3
        ·
          by_cases h4 : j.val < 160
          · exact neutralNF605SelectedShard4 j (by omega) h4
          ·
            by_cases h5 : j.val < 192
            · exact neutralNF605SelectedShard5 j (by omega) h5
            ·
              by_cases h6 : j.val < 224
              · exact neutralNF605SelectedShard6 j (by omega) h6
              ·
                exact neutralNF605SelectedShard7 j (by omega) j.isLt

theorem neutralNF605EndpointCheck : neutralNF597EndpointCheck = true :=
  neutralNF603EndpointCheck_of_modes neutralNF605AllSelected
    neutralNF605CriticalShard8 neutralNF605PoleCheck

theorem neutralNF605Endpoint_negative (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    neutralNF587Source a b (11/10) < -(1/10^11:ℝ) :=
  neutralNF597Endpoint_negative_of_check neutralNF605EndpointCheck a b hbox

theorem neutralNF605OriginalCarrier_nonzero
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b)
    (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume) :
    hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ≠ 0 :=
  neutralNF601Endpoint_L2_ne_zero (neutralNF587Source a b)
    (neutralNF587Source_contDiff a b).continuous
    (ne_of_lt ((neutralNF605Endpoint_negative a b hbox).trans (by norm_num))) hLp

/-- For the actual exact critical vector, the only source custody
premise left in Lean is containment of the 242 selected coordinates.
All local support positivity assumptions remain explicit. -/
theorem neutralNF605OriginalGraph_positive_of_selected
    (a : Fin 242 → ℝ)
    (ha : ∀ j, |a j-neutralNF587SelectedMid j| ≤ neutralNF587SelectedRadius j)
    (hlocal : neutralNF599SmoothCollarLower (2/5)) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint
        (neutralNF587Source a neutralNF604OriginalCritical)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint
          (neutralNF587Source a neutralNF604OriginalCritical)) ∧
      0 < neutralNF598GraphWeil (11/10) K :=
  neutralNF601NF407Graph_positive_of_endpointCheck a neutralNF604OriginalCritical
    (neutralNF604Box_of_selected a ha) neutralNF605EndpointCheck hlocal

#print axioms neutralNF605EndpointCheck
#print axioms neutralNF605Endpoint_negative
#print axioms neutralNF605OriginalGraph_positive_of_selected

end
end WeilDefect
