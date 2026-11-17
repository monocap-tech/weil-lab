import WeilDefect.Arithmetic.ActualZetaOriginalCachedModeJets
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointBudgetBridge

namespace WeilDefect
noncomputable section
open Finset

/-! NF593: hoist each mode, phase, pole and primitive coefficient
ball outside the 400-order source loop. No numerical approximation
is introduced by caching. -/

def neutralNF593ReadTable (a : Array (Array NF591Ball)) (j : ℕ) :
    Array NF591Ball := a[j]?.getD #[]

def neutralNF593SelectedTable (p : NF591Ball) (Q N K : ℕ) (j : Fin 242) :
    Array NF591Ball :=
  if hj : j.val < 241 then
    let node := nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩
    neutralNF593OscillatorTable p node.1 Q N node.2 K
  else neutralNF593PoleTable Q N K

theorem neutralNF593SelectedTable_read (p : NF591Ball) (Q N K : ℕ)
    (j : Fin 242) (n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593SelectedTable p Q N K j) n =
      neutralNF592SelectedJetBall p Q N j n := by
  unfold neutralNF593SelectedTable neutralNF592SelectedJetBall
  by_cases hj : j.val < 241
  · simp only [dif_pos hj,neutralNF593OscillatorTable_read _ _ _ _ _ _ _ hn]
  · simp only [dif_neg hj,neutralNF593PoleTable_read _ _ _ _ hn]

def neutralNF593CriticalFromTables (Q : ℕ) (b : NF591Ball)
    (j : Fin 4) (n : ℕ) (sines : Array (Array NF591Ball)) (pole : Array NF591Ball) : NF591Ball :=
  (neutralNF592BallSum univ (fun k : Fin 32 =>
    ((((b.mul (NF591Ball.exactQ ((neutralNF587CriticalSines[j.val]!)[k.val]!) Q)).round Q).mul
      (neutralNF593ReadBall (neutralNF593ReadTable sines k.val) n)).round Q))).add
    ((((b.mul (NF591Ball.exactQ neutralNF587CriticalPoles[j.val]! Q)).round Q).mul
      (neutralNF593ReadBall pole n)).round Q)

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

def neutralNF593SourceTable (p : NF591Ball) (Q N K : ℕ) : Array NF591Ball :=
  let selected := Array.ofFn (fun j : Fin 242 => neutralNF593SelectedTable p Q N K j)
  let sines := Array.ofFn (fun k : Fin 32 =>
    neutralNF593OscillatorTable p neutralNF587CriticalFrequencies[k.val]! Q N 0 K)
  let pole := neutralNF593PoleTable Q N K
  let a := Array.ofFn (fun j : Fin 242 => neutralNF592PrimitiveBox neutralNF587SelectedDyads[j.val]! Q)
  let b := Array.ofFn (fun j : Fin 4 => neutralNF592PrimitiveBox neutralNF587CriticalDyads[j.val]! Q)
  Array.ofFn (fun n : Fin K =>
    (neutralNF592BallSum univ (fun j : Fin 242 =>
      (( (neutralNF593ReadBall a j.val).mul
        (neutralNF593ReadBall (neutralNF593ReadTable selected j.val) n.val)).round Q))).add
      (neutralNF592BallSum univ (fun j : Fin 4 =>
        neutralNF593CriticalFromTables Q (neutralNF593ReadBall b j.val) j n.val sines pole)))

theorem neutralNF593SourceTable_read (p : NF591Ball) (Q N K n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593SourceTable p Q N K) n =
      neutralNF592SourceBall p Q N n := by
  unfold neutralNF593ReadBall neutralNF593SourceTable
  simp only [Array.getElem?_ofFn,dif_pos hn,Option.getD_some]
  unfold neutralNF592SourceBall
  congr 1
  · congr 1
    funext j
    simp only [neutralNF593ReadTable,Array.getElem?_ofFn,dif_pos j.isLt,Option.getD_some]
    exact congrArg (fun z => ((neutralNF592PrimitiveBox neutralNF587SelectedDyads[j.val]! Q).mul z).round Q)
      (neutralNF593SelectedTable_read p Q N K j n hn)
  · congr 1
    funext j
    simpa only [Array.getElem?_ofFn,dif_pos j.isLt,Option.getD_some] using
      neutralNF593CriticalFromTables_eq p Q N K
        (neutralNF592PrimitiveBox neutralNF587CriticalDyads[j.val]! Q) j n hn

def neutralNF593OriginalTable : Array NF591Ball :=
  neutralNF593SourceTable (neutralNF592PiBall neutralNF592Q 200) neutralNF592Q 220 400

theorem neutralNF593OriginalTable_read (n : Fin 400) :
    neutralNF593ReadBall neutralNF593OriginalTable n.val = neutralNF592OriginalJetBall n.val :=
  neutralNF593SourceTable_read _ _ _ _ _ n.isLt

/-- Executable comparison on the cached table. The proof of truth
must be separate from the definition of this Boolean. -/
def neutralNF593CheckTable (t : Array NF591Ball) (K : ℕ) : Bool :=
  (List.range K).all (fun n =>
    let b := neutralNF593ReadBall t n
    decide (|b.mid|+b.rad ≤ (neutralNF588U400Ceil n:ℚ)/10^40))

theorem neutralNF593CheckTable_sound (t : Array NF591Ball) (K : ℕ)
    (h : neutralNF593CheckTable t K = true) :
    ∀ n < K, |(neutralNF593ReadBall t n).mid|+(neutralNF593ReadBall t n).rad ≤
      (neutralNF588U400Ceil n:ℚ)/10^40 := by
  intro n hn
  unfold neutralNF593CheckTable at h
  have hh := List.all_eq_true.mp h n (List.mem_range.mpr hn)
  exact of_decide_eq_true hh

theorem neutralNF593Budget_of_check
    (h : neutralNF593CheckTable neutralNF593OriginalTable 400 = true) :
    neutralNF592OriginalFixedpointBudget := by
  intro n
  have hb := neutralNF593CheckTable_sound neutralNF593OriginalTable 400 h n.val n.isLt
  rw [neutralNF593OriginalTable_read n] at hb
  exact hb

end
end WeilDefect
