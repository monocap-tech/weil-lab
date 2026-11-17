import WeilDefect.Arithmetic.ActualZetaOriginalAnalyticTailCutoff
import WeilDefect.Arithmetic.ActualZetaOriginalCachedSourceJets

namespace WeilDefect
noncomputable section

/-! NF594: pay degrees 250..399 analytically, without invoking
the interval evaluator on those degrees. Retain the original
400-entry ceiling table and both accepted budgets unchanged. -/

theorem neutralNF594Disc285_of_box (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) (w : ℂ) (hw : ‖w‖ ≤ 20) :
    ‖neutralNF588NormalizedSource a b w‖ ≤ (10:ℝ)^285 := by
  apply (neutralNF594SourceDisc_raw_of_scalarBounds a b
    (neutralNF589ScalarBounds_of_box a b hbox) w hw).trans
  unfold neutralNF589ModeMajorant
  calc
    _ = (400:ℝ)*10^143*2^13*3^283 := by ring
    _ ≤ _ := neutralNF594Disc285_real

set_option maxRecDepth 10000 in
set_option maxHeartbeats 2000000 in
theorem neutralNF594LateCeil :
    ∀ n : Fin 400, 250 ≤ n.val → neutralNF588U400Ceil n.val = 1 := by
  decide +kernel

theorem neutralNF594LateJet (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) (n : ℕ)
    (hl : 250 ≤ n) (hu : n<400) :
    ‖neutralNF590SourceJet a b n‖ ≤ neutralNF588U400Bound n := by
  rw [neutralNF590SourceJet_eq_canonical]
  have h := neutralNF588NormalizedCoefficient_bound
    (neutralNF588NormalizedSource a b) (neutralNF588NormalizedSource_differentiable a b)
    ((10:ℝ)^285) (fun w hw => neutralNF594Disc285_of_box a b hbox w hw.le) n
  apply h.trans
  unfold neutralNF588U400Bound
  rw [neutralNF594LateCeil ⟨n,hu⟩ hl]
  push_cast
  exact neutralNF594HighDegree n hl

def neutralNF594HeadBudget : Prop :=
  ∀ n < 250, |(neutralNF592OriginalJetBall n).mid|+
    (neutralNF592OriginalJetBall n).rad ≤ (neutralNF588U400Ceil n:ℚ)/10^40

theorem neutralNF594HeadJet (hhead : neutralNF594HeadBudget)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b)
    (n : ℕ) (hn : n<250) :
    ‖neutralNF590SourceJet a b n‖ ≤ neutralNF588U400Bound n := by
  have h := neutralNF592SourceBall_sound
    (neutralNF592PiBall neutralNF592Q 200)
    (neutralNF592PiBall_sound neutralNF592Q 200 neutralNF592Q_pos
      neutralNF592Atan5Fee neutralNF592Atan239Fee)
    neutralNF592Q 220 neutralNF592Q_pos (by decide) neutralNF592ExpFee a b hbox n
  rw [Real.norm_eq_abs]
  apply (NF591Ball.contains_abs_bound h).trans
  unfold neutralNF588U400Bound
  have hr :
      ((|(neutralNF592OriginalJetBall n).mid|+
        (neutralNF592OriginalJetBall n).rad:ℚ):ℝ) ≤
      (((neutralNF588U400Ceil n:ℚ)/10^40:ℚ):ℝ) :=
    Rat.cast_le.mpr (hhead n hn)
  simpa only [neutralNF592OriginalJetBall,Rat.cast_div,Rat.cast_natCast,
    Rat.cast_pow,Rat.cast_ofNat] using hr

theorem neutralNF594AllJets_of_headBudget (hhead : neutralNF594HeadBudget)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) :
    ∀ n < 400, ‖neutralNF590SourceJet a b n‖ ≤ neutralNF588U400Bound n := by
  intro n hn
  by_cases hl : n<250
  · exact neutralNF594HeadJet hhead a b hbox n hl
  · exact neutralNF594LateJet a b hbox n (Nat.le_of_not_gt hl) hn

theorem neutralNF594OriginalCollar_of_headBudget
    (hhead : neutralNF594HeadBudget)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) :
    (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |neutralNF587Source a b x| ≤ 2/10^7) ∧
      (∀ x ∈ Set.Icc (549/500:ℝ) (11/10),
        |deriv (neutralNF587Source a b) x| ≤ 7/10^4) :=
  neutralNF590SourceBounds_of_recurrence a b hbox
    (neutralNF594AllJets_of_headBudget hhead a b hbox)

end
end WeilDefect
