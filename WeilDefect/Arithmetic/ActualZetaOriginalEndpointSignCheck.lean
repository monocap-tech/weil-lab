import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointSourceJets

namespace WeilDefect
noncomputable section

/-! NF597: endpoint sign is an independent single-coefficient
obligation. The absolute-value ceiling alone cannot prove it. -/

theorem neutralNF597SourceJet_zero (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    neutralNF590SourceJet a b 0 = neutralNF587Source a b (11/10) := by
  have h := neutralNF590SourceJet_hasSum a b 0
  have ht : (∑' n : ℕ, neutralNF590SourceJet a b n*(0:ℝ)^n) =
      neutralNF590SourceJet a b 0 := by
    rw [tsum_eq_single 0]
    · simp
    · intro n hn
      simp [zero_pow hn]
  rw [h.tsum_eq] at ht
  simpa using ht.symm

def neutralNF597EndpointCheck : Bool :=
  let v := neutralNF592OriginalJetBall 0
  decide (v.mid+v.rad < -(1/10^11:ℚ))

/-- The endpoint sign is uniform on the genuine primitive box.
No Cauchy disc majorant, tail certificate, or other 399
coefficient comparisons enter the implication. -/
theorem neutralNF597Endpoint_negative_of_check
    (hcheck : neutralNF597EndpointCheck = true)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    neutralNF587Source a b (11/10) < -(1/10^11:ℝ) := by
  have h := neutralNF592SourceBall_sound
    (neutralNF592PiBall neutralNF592Q 200)
    (neutralNF592PiBall_sound neutralNF592Q 200 neutralNF592Q_pos
      neutralNF592Atan5Fee neutralNF592Atan239Fee)
    neutralNF592Q 220 neutralNF592Q_pos (by decide) neutralNF592ExpFee a b hbox 0
  change (neutralNF592OriginalJetBall 0).Contains (neutralNF590SourceJet a b 0) at h
  rw [neutralNF597SourceJet_zero] at h
  have hc : (neutralNF592OriginalJetBall 0).mid+
      (neutralNF592OriginalJetBall 0).rad < -(1/10^11:ℚ) := by
    exact of_decide_eq_true hcheck
  have hc' : ((neutralNF592OriginalJetBall 0).mid:ℝ)+
      ((neutralNF592OriginalJetBall 0).rad:ℝ) < -(1/10^11:ℝ) := by exact_mod_cast hc
  unfold NF591Ball.Contains at h
  have hu := le_trans (le_abs_self _) h
  linarith only [hu,hc']

end
end WeilDefect
