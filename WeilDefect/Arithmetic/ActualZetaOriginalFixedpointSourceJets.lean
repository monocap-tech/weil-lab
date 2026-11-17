import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointModeJets
import WeilDefect.Arithmetic.ActualZetaOriginalNF407CanonicalJetRecurrence
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointComputationalCore
import WeilDefect.Arithmetic.ActualZetaOriginalU400NormalizedBudget

namespace WeilDefect
noncomputable section
open Finset

/-! NF592: full primitive coefficient-box assembly, no regrouping.
This is a reference evaluator and soundness candidate. Efficient
caching and a kernel-checked evaluation receipt remain separate. -/

theorem neutralNF592BallSum_sound {ι : Type*} (s : Finset ι)
    (a : ι → NF591Ball) (x : ι → ℝ)
    (h : ∀ j ∈ s, (a j).Contains (x j)) :
    (neutralNF592BallSum s a).Contains (∑ j ∈ s, x j) := by
  unfold NF591Ball.Contains neutralNF592BallSum
  simp only [Rat.cast_sum]
  rw [← sum_sub_distrib,← Real.norm_eq_abs]
  apply (norm_sum_le _ _).trans
  apply sum_le_sum
  intro j hj
  rw [Real.norm_eq_abs]
  exact h j hj

theorem neutralNF592DyadicQ_spec (p : ℤ × ℤ) :
    (neutralNF592DyadicQ p:ℝ) = neutralNF587Dyadic p := by
  unfold neutralNF592DyadicQ neutralNF587Dyadic
  push_cast
  rfl

theorem neutralNF592PrimitiveBox_sound (row : (ℤ × ℤ) × (ℤ × ℤ))
    (Q : ℕ) (hQ : 0 < Q) (x : ℝ)
    (hx : |x-neutralNF587Dyadic row.1| ≤ |neutralNF587Dyadic row.2|) :
    (neutralNF592PrimitiveBox row Q).Contains x := by
  have hm := NF591Ball.contains_exactQ (neutralNF592DyadicQ row.1) Q hQ
  have hr := NF591Ball.contains_abs_bound
    (NF591Ball.contains_exactQ (neutralNF592DyadicQ row.2) Q hQ)
  rw [neutralNF592DyadicQ_spec] at hm hr
  exact NF591Ball.contains_expand _ hm (hx.trans hr)

theorem neutralNF592SelectedJetBall_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (Q N : ℕ) (hQ : 0 < Q) (hN : 1 ≤ N) (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ))
    (j : Fin 242) (n : ℕ) :
    (neutralNF592SelectedJetBall p Q N j n).Contains (neutralNF590SelectedJet j n) := by
  unfold neutralNF592SelectedJetBall neutralNF590SelectedJet
  by_cases hj : j.val < 241
  · simp only [dif_pos hj]
    exact neutralNF592OscillatorBall_sound p hp _ Q N _ n hQ hN hfee
  · simp only [dif_neg hj]
    exact neutralNF592PoleBall_sound Q N n hQ hN hfee

/-- Multiply the primitive critical coefficient into each probe
component BEFORE summing, just as the integer-only replay did. -/
theorem neutralNF592CriticalContribution_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (Q N : ℕ) (hQ : 0 < Q) (hN : 1 ≤ N) (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ))
    (b : NF591Ball) (β : ℝ) (hb : b.Contains β) (j : Fin 4) (n : ℕ) :
    (neutralNF592CriticalContribution p Q N b j n).Contains (β*neutralNF590CriticalJet j n) := by
  unfold neutralNF592CriticalContribution neutralNF590CriticalJet
  rw [mul_add,mul_sum]
  apply NF591Ball.contains_add
  · apply neutralNF592BallSum_sound
    intro k _
    rw [← mul_assoc]
    exact NF591Ball.contains_rounded_mul
      (NF591Ball.contains_rounded_mul hb
        (NF591Ball.contains_exactQ _ Q hQ) Q hQ)
      (neutralNF592OscillatorBall_sound p hp _ Q N 0 n hQ hN hfee) Q hQ
  · rw [← mul_assoc]
    exact NF591Ball.contains_rounded_mul
      (NF591Ball.contains_rounded_mul hb
        (NF591Ball.contains_exactQ _ Q hQ) Q hQ)
      (neutralNF592PoleBall_sound Q N n hQ hN hfee) Q hQ

theorem neutralNF592SourceBall_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (Q N : ℕ) (hQ : 0 < Q) (hN : 1 ≤ N) (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ))
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) (n : ℕ) :
    (neutralNF592SourceBall p Q N n).Contains (neutralNF590SourceJet a b n) := by
  unfold neutralNF592SourceBall neutralNF590SourceJet
  apply NF591Ball.contains_add
  · apply neutralNF592BallSum_sound
    intro j _
    exact NF591Ball.contains_rounded_mul
      (neutralNF592PrimitiveBox_sound _ Q hQ (a j) (hbox.1 j))
      (neutralNF592SelectedJetBall_sound p hp Q N hQ hN hfee j n) Q hQ
  · apply neutralNF592BallSum_sound
    intro j _
    exact neutralNF592CriticalContribution_sound p hp Q N hQ hN hfee _
      (b j) (neutralNF592PrimitiveBox_sound _ Q hQ (b j) (hbox.2 j)) j n

/-- A finite rational comparison against each stored ceiling is
enough for analytic enclosure of EVERY coefficient choice. This
is not yet a proof of the comparisons themselves. -/
theorem neutralNF592SourceJet_of_ballBudget
    (p : NF591Ball) (hp : p.Contains Real.pi)
    (Q N : ℕ) (hQ : 0 < Q) (hN : 1 ≤ N) (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ))
    (hbudget : ∀ n < 400, |(neutralNF592SourceBall p Q N n).mid|+
      (neutralNF592SourceBall p Q N n).rad ≤ (neutralNF588U400Ceil n:ℚ)/10^40)
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (hbox : neutralNF587SourceInFrozenBox a b) :
    ∀ n < 400, ‖neutralNF590SourceJet a b n‖ ≤ neutralNF588U400Bound n := by
  intro n hn
  rw [Real.norm_eq_abs]
  apply (NF591Ball.contains_abs_bound
    (neutralNF592SourceBall_sound p hp Q N hQ hN hfee a b hbox n)).trans
  unfold neutralNF588U400Bound
  have hr := Rat.cast_le (K := ℝ).mpr (hbudget n hn)
  simpa only [Rat.cast_div,Rat.cast_natCast,Rat.cast_pow,Rat.cast_ofNat] using hr

end
end WeilDefect
