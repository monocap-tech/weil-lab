import WeilDefect.Arithmetic.ActualZetaOriginalReducedJetBudget
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointComputationalCore

namespace WeilDefect
noncomputable section

/-! NF594: an independently checkable block uses only the cached
prefix needed for that block. Five 50-order blocks suffice after
the analytic high-degree cutoff. Boolean checking and its soundness
are separate; no native_decide proposition is assumed. -/

theorem neutralNF594BlockCheck_sound (lo count n : ℕ)
    (hl : lo ≤ n) (hu : n < lo+count)
    (h : neutralNF594BlockCheck lo count = true) :
    |(neutralNF592OriginalJetBall n).mid|+
      (neutralNF592OriginalJetBall n).rad ≤ (neutralNF588U400Ceil n:ℚ)/10^40 := by
  unfold neutralNF594BlockCheck at h
  have hi : n-lo < count := by omega
  have hb := List.all_eq_true.mp h (n-lo) (List.mem_range.mpr hi)
  have he : lo+(n-lo)=n := by omega
  simp only [he,neutralNF593SourceTable_read _ _ _ _ _ hu] at hb
  exact of_decide_eq_true hb

theorem neutralNF594HeadBudget_of_blocks
    (h : ∀ j : Fin 5, neutralNF594BlockCheck (50*j.val) 50 = true) :
    neutralNF594HeadBudget := by
  intro n hn
  have hj : n/50<5 := by omega
  let j : Fin 5 := ⟨n/50,hj⟩
  have hl : 50*j.val ≤ n := by dsimp [j]; omega
  have hu : n < 50*j.val+50 := by dsimp [j]; omega
  exact neutralNF594BlockCheck_sound (50*j.val) 50 n hl hu (h j)

theorem neutralNF594Blocks_join
    (h0 : neutralNF594BlockCheck 0 50 = true)
    (h1 : neutralNF594BlockCheck 50 50 = true)
    (h2 : neutralNF594BlockCheck 100 50 = true)
    (h3 : neutralNF594BlockCheck 150 50 = true)
    (h4 : neutralNF594BlockCheck 200 50 = true) :
    neutralNF594HeadBudget := by
  apply neutralNF594HeadBudget_of_blocks
  intro j
  fin_cases j
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4

theorem neutralNF594OriginalCollar_of_blocks
    (h0 : neutralNF594BlockCheck 0 50 = true)
    (h1 : neutralNF594BlockCheck 50 50 = true)
    (h2 : neutralNF594BlockCheck 100 50 = true)
    (h3 : neutralNF594BlockCheck 150 50 = true)
    (h4 : neutralNF594BlockCheck 200 50 = true)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) :
    (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |neutralNF587Source a b x| ≤ 2/10^7) ∧
      (∀ x ∈ Set.Icc (549/500:ℝ) (11/10),
        |deriv (neutralNF587Source a b) x| ≤ 7/10^4) :=
  neutralNF594OriginalCollar_of_headBudget (neutralNF594Blocks_join h0 h1 h2 h3 h4) a b hbox

end
end WeilDefect
