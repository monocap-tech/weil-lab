import WeilDefect.Arithmetic.ActualZetaOriginalCachedModeJets
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointComputationalCore

namespace WeilDefect
noncomputable section
open Finset
set_option maxHeartbeats 2000000
set_option maxRecDepth 10000

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

private theorem neutralNF598ReadBall_ofFn {K : ℕ}
    (f : Fin K → NF591Ball) (n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (Array.ofFn f) n = f ⟨n,hn⟩ := by
  simp only [neutralNF593ReadBall,Array.getElem?_ofFn,dif_pos hn,Option.getD_some]

private theorem neutralNF598ReadTable_ofFn {K : ℕ}
    (f : Fin K → Array NF591Ball) (n : ℕ) (hn : n<K) :
    neutralNF593ReadTable (Array.ofFn f) n = f ⟨n,hn⟩ := by
  simp only [neutralNF593ReadTable,Array.getElem?_ofFn,dif_pos hn,Option.getD_some]

theorem neutralNF593CriticalFromTables_eq (p : NF591Ball) (Q N K : ℕ)
    (b : NF591Ball) (j : Fin 4) (n : ℕ) (hn : n<K) :
    neutralNF593CriticalFromTables Q b j n
      (Array.ofFn (fun k : Fin 32 =>
        neutralNF593OscillatorTable p neutralNF587CriticalFrequencies[k.val]! Q N 0 K))
      (neutralNF593PoleTable Q N K) =
      neutralNF592CriticalContribution p Q N b j n := by
  have hs (k : Fin 32) :
      neutralNF593ReadBall (neutralNF593ReadTable
        (Array.ofFn (fun k : Fin 32 =>
          neutralNF593OscillatorTable p neutralNF587CriticalFrequencies[k.val]! Q N 0 K)) k.val) n =
        neutralNF592OscillatorBall p neutralNF587CriticalFrequencies[k.val]! Q N 0 n := by
    rw [neutralNF598ReadTable_ofFn _ _ k.isLt]
    exact neutralNF593OscillatorTable_read _ _ _ _ _ _ _ hn
  have hp := neutralNF593PoleTable_read Q N K n hn
  unfold neutralNF593CriticalFromTables neutralNF592CriticalContribution
  simp only [hs,hp]

theorem neutralNF593SourceTable_read (p : NF591Ball) (Q N K n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593SourceTable p Q N K) n =
      neutralNF592SourceBall p Q N n := by
  have hs (j : Fin 242) :
      neutralNF593ReadBall (neutralNF593ReadTable
        (Array.ofFn (fun j : Fin 242 => neutralNF593SelectedTable p Q N K j)) j.val) n =
        neutralNF592SelectedJetBall p Q N j n := by
    rw [neutralNF598ReadTable_ofFn _ _ j.isLt]
    exact neutralNF593SelectedTable_read p Q N K j n hn
  unfold neutralNF593SourceTable
  rw [neutralNF598ReadBall_ofFn _ _ hn]
  dsimp only
  unfold neutralNF592SourceBall
  simp only [neutralNF598ReadBall_ofFn _ _ (Fin.isLt _),hs,
    neutralNF593CriticalFromTables_eq p Q N K _ _ n hn]

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
