import WeilDefect.Arithmetic.ActualZetaOriginalCachedModeJets
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointComputationalCore

namespace WeilDefect
noncomputable section
open Finset

/-! NF593: hoist each mode, phase, pole and primitive coefficient
ball outside the 400-order source loop. No numerical approximation
is introduced by caching. -/

theorem neutralNF593SelectedTable_read (p : NF591Ball) (Q N K : ℕ)
    (j : Fin 242) (n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593SelectedTable p Q N K j) n =
      neutralNF592SelectedJetBall p Q N j n := by
  unfold neutralNF593SelectedTable neutralNF592SelectedJetBall
  by_cases hj : j.val < 241
  · simp only [dif_pos hj,neutralNF593OscillatorTable_read _ _ _ _ _ _ _ hn]
  · simp only [dif_neg hj,neutralNF593PoleTable_read _ _ _ _ hn]

theorem neutralNF593CriticalFromTables_eq (p : NF591Ball) (Q N K : ℕ)
    (b : NF591Ball) (j : Fin 4) (n : ℕ) (hn : n<K) :
    neutralNF593CriticalFromTables Q b j n
      (Array.ofFn (fun k : Fin 32 =>
        neutralNF593OscillatorTable p neutralNF587CriticalFrequencies[k.val]! Q N 0 K))
      (neutralNF593PoleTable Q N K) =
      neutralNF592CriticalContribution p Q N b j n := by
  unfold neutralNF593CriticalFromTables neutralNF592CriticalContribution
  simp only [neutralNF593PoleTable_read _ _ _ _ hn]
  congr 1
  congr 1
  funext k
  simp only [neutralNF593ReadTable,Array.getElem?_ofFn,dif_pos k.isLt,Option.getD_some,
    neutralNF593OscillatorTable_read _ _ _ _ _ _ _ hn]

theorem neutralNF593SourceTable_read (p : NF591Ball) (Q N K n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593SourceTable p Q N K) n =
      neutralNF592SourceBall p Q N n := by
  unfold neutralNF593ReadBall neutralNF593SourceTable
  simp only [Array.getElem?_ofFn,dif_pos hn,Option.getD_some]
  unfold neutralNF592SourceBall
  congr 1
  · congr 1
    funext j
    simp only [neutralNF593ReadBall,neutralNF593ReadTable,Array.getElem?_ofFn,dif_pos j.isLt,Option.getD_some]
    exact congrArg (fun z => ((neutralNF592PrimitiveBox neutralNF587SelectedDyads[j.val]! Q).mul z).round Q)
      (neutralNF593SelectedTable_read p Q N K j n hn)
  · congr 1
    funext j
    simpa only [neutralNF593ReadBall,Array.getElem?_ofFn,dif_pos j.isLt,Option.getD_some] using
      neutralNF593CriticalFromTables_eq p Q N K
        (neutralNF592PrimitiveBox neutralNF587CriticalDyads[j.val]! Q) j n hn

theorem neutralNF593OriginalTable_read (n : Fin 400) :
    neutralNF593ReadBall neutralNF593OriginalTable n.val = neutralNF592OriginalJetBall n.val :=
  neutralNF593SourceTable_read _ _ _ _ _ n.isLt

/-- Executable comparison on the cached table. The proof of truth
must be separate from the definition of this Boolean. -/
theorem neutralNF593CheckTable_sound (t : Array NF591Ball) (K : ℕ)
    (h : neutralNF593CheckTable t K = true) :
    ∀ n < K, |(neutralNF593ReadBall t n).mid|+(neutralNF593ReadBall t n).rad ≤
      (neutralNF588U400Ceil n:ℚ)/10^40 := by
  intro n hn
  unfold neutralNF593CheckTable at h
  have hh := List.all_eq_true.mp h n (List.mem_range.mpr hn)
  exact of_decide_eq_true hh


end
end WeilDefect
