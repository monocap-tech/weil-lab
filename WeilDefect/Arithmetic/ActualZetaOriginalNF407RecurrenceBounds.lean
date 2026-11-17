import WeilDefect.Arithmetic.ActualZetaOriginalNF407CanonicalJetRecurrence
import WeilDefect.Arithmetic.ActualZetaOriginalNF407DiscTableBounds

namespace WeilDefect
noncomputable section

/-! NF590: the finite interval proof obligation is now expressed
on the explicit recurrence, rather than on opaque Cauchy integrals.
It must be paid by a checked interval certificate, not by an axiom. -/

theorem neutralNF590SourceBounds_of_recurrence
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b)
    (hinterval : ∀ n < 400, ‖neutralNF590SourceJet a b n‖ ≤
      neutralNF588U400Bound n) :
    (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |neutralNF587Source a b x| ≤ 2/10^7) ∧
      (∀ x ∈ Set.Icc (549/500:ℝ) (11/10),
        |deriv (neutralNF587Source a b) x| ≤ 7/10^4) := by
  apply neutralNF589SourceBounds_of_canonicalJets a b hbox
  intro n hn
  rw [← neutralNF590SourceJet_eq_canonical]
  exact hinterval n hn

end
end WeilDefect
