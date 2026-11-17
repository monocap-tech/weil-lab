import WeilDefect.Arithmetic.ActualZetaOriginalCachedSourceEquality
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointBudgetBridge

namespace WeilDefect
noncomputable section

theorem neutralNF593Budget_of_check
    (h : neutralNF593CheckTable neutralNF593OriginalTable 400 = true) :
    neutralNF592OriginalFixedpointBudget := by
  intro n
  have hb := neutralNF593CheckTable_sound neutralNF593OriginalTable 400 h n.val n.isLt
  rw [neutralNF593OriginalTable_read n] at hb
  exact hb

/-- A checked Boolean now suffices for the full original collar
bounds throughout the same uncertainty box, with no opaque
numerical or transcendental hypothesis. -/
theorem neutralNF593OriginalCollar_of_check
    (h : neutralNF593CheckTable neutralNF593OriginalTable 400 = true)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) :
    (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |neutralNF587Source a b x| ≤ 2/10^7) ∧
      (∀ x ∈ Set.Icc (549/500:ℝ) (11/10),
        |deriv (neutralNF587Source a b) x| ≤ 7/10^4) :=
  neutralNF592OriginalCollar_of_fixedpointBudget (neutralNF593Budget_of_check h) a b hbox

end
end WeilDefect
