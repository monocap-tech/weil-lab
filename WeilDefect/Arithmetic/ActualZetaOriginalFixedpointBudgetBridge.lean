import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointSourceJets
import WeilDefect.Arithmetic.ActualZetaOriginalNF407RecurrenceBounds
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointParameters
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointComputationalCore

namespace WeilDefect
noncomputable section

/-! NF592: the final numerical obligation is a finite inequality
on a fully specified rational evaluator. The statement does not
assume any transcendental enclosure or arbitrary interval choice. -/

theorem neutralNF592OriginalJets_of_fixedpointBudget
    (hbudget : neutralNF592OriginalFixedpointBudget)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) :
    ∀ n < 400, ‖neutralNF590SourceJet a b n‖ ≤ neutralNF588U400Bound n := by
  apply neutralNF592SourceJet_of_ballBudget
    (neutralNF592PiBall neutralNF592Q 200)
    (neutralNF592PiBall_sound neutralNF592Q 200 neutralNF592Q_pos
      neutralNF592Atan5Fee neutralNF592Atan239Fee)
    neutralNF592Q 220 neutralNF592Q_pos (by decide) neutralNF592ExpFee
  · intro n hn
    exact hbudget ⟨n,hn⟩
  · exact hbox

theorem neutralNF592OriginalCollar_of_fixedpointBudget
    (hbudget : neutralNF592OriginalFixedpointBudget)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) :
    (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |neutralNF587Source a b x| ≤ 2/10^7) ∧
      (∀ x ∈ Set.Icc (549/500:ℝ) (11/10),
        |deriv (neutralNF587Source a b) x| ≤ 7/10^4) :=
  neutralNF590SourceBounds_of_recurrence a b hbox
    (neutralNF592OriginalJets_of_fixedpointBudget hbudget a b hbox)

end
end WeilDefect
