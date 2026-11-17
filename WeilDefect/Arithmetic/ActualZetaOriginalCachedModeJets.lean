import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointModeJets
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointComputationalCore

namespace WeilDefect
noncomputable section

/-! NF593: a shared array of exact rounded exponential jet balls.
The recurrence is evaluated once per order. The lookup theorem is
an equality of rational rectangles, not just an enclosure bound. -/

@[simp] theorem neutralNF593ExpTable_size (a : NF591Rect) (Q n : ℕ) :
    (neutralNF593ExpTable a Q n).size = n+1 := by
  induction n with
  | zero => rfl
  | succ n ih => simp [neutralNF593ExpTable,ih]

theorem neutralNF593ExpTable_get (a : NF591Rect) (Q n j : ℕ) (hj : j ≤ n) :
    (neutralNF593ExpTable a Q n)[j]? = some (neutralNF592ExpJetBall a Q j) := by
  induction n generalizing j with
  | zero =>
    have he : j = 0 := by omega
    subst j
    rfl
  | succ n ih =>
    rw [neutralNF593ExpTable,Array.getElem?_push,neutralNF593ExpTable_size]
    by_cases he : j=n+1
    · subst j
      simp only [ite_true,neutralNF593ReadRect,ih n (by omega : n ≤ n),
        Option.getD_some,neutralNF592ExpJetBall]
    · rw [if_neg he]
      exact ih j (by omega)

theorem neutralNF593ExpTable_read (a : NF591Rect) (Q n j : ℕ) (hj : j ≤ n) :
    neutralNF593ReadRect (neutralNF593ExpTable a Q n) j =
      neutralNF592ExpJetBall a Q j := by
  simp only [neutralNF593ReadRect,neutralNF593ExpTable_get a Q n j hj,Option.getD_some]

theorem neutralNF593RectSum_congr (a b : ℕ → NF591Rect) (N : ℕ)
    (h : ∀ n < N, a n=b n) :
    neutralNF592RectSum a N=neutralNF592RectSum b N := by
  induction N with
  | zero => rfl
  | succ N ih =>
    rw [neutralNF592RectSum,neutralNF592RectSum,ih (fun n hn => h n (by omega)),
      h N (by omega)]

theorem neutralNF593Partial_eq_sum (a : NF591Rect) (Q N : ℕ) :
    neutralNF592ExpPartial a Q N =
      neutralNF592RectSum (neutralNF592ExpJetBall a Q) N := by
  induction N with
  | zero => rfl
  | succ N ih => simp only [neutralNF592ExpPartial,neutralNF592RectSum,ih]

theorem neutralNF593SmallExp_eq (a : NF591Rect) (Q N : ℕ) :
    neutralNF593SmallExp a Q N = neutralNF592SmallExpBall a Q N := by
  unfold neutralNF593SmallExp neutralNF592SmallExpBall
  rw [neutralNF593Partial_eq_sum]
  dsimp only
  apply congrArg (fun r : NF591Rect => r.expand (1/(Q:ℚ)))
  apply neutralNF593RectSum_congr
  intro n hn
  exact neutralNF593ExpTable_read a Q N n (by omega)

theorem neutralNF593Phase_eq (p : NF591Ball) (f : ℚ) (Q N : ℕ) :
    neutralNF593Phase p f Q N = neutralNF592PhaseBall p f Q N := by
  simp only [neutralNF593Phase,neutralNF592PhaseBall,neutralNF593SmallExp_eq]

theorem neutralNF593ModeFromTable_eq (a : NF591Rect) (Q K k n : ℕ) (hn : n ≤ K) :
    neutralNF593ModeFromTable (neutralNF593ExpTable a Q K) Q k n =
      neutralNF592ModeBall a Q k n := by
  unfold neutralNF593ModeFromTable neutralNF592ModeBall
  apply neutralNF593RectSum_congr
  intro m hm
  rw [neutralNF593ExpTable_read a Q K (n-m) (by omega)]

theorem neutralNF593OscillatorTable_read (p : NF591Ball) (f : ℚ)
    (Q N k K n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593OscillatorTable p f Q N k K) n =
      neutralNF592OscillatorBall p f Q N k n := by
  unfold neutralNF593ReadBall neutralNF593OscillatorTable neutralNF592OscillatorBall
  simp only [Array.getElem?_ofFn,dif_pos hn,Option.getD_some,
    neutralNF593Phase_eq,neutralNF593ModeFromTable_eq _ _ _ _ _ (by omega : n ≤ K)]

theorem neutralNF593PoleTable_read (Q N K n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593PoleTable Q N K) n =
      neutralNF592PoleBall Q N n := by
  unfold neutralNF593ReadBall neutralNF593PoleTable neutralNF592PoleBall
  simp only [Array.getElem?_ofFn,dif_pos hn,Option.getD_some,
    neutralNF593SmallExp_eq,neutralNF593ExpTable_read _ _ _ _ (by omega : n ≤ K)]

end
end WeilDefect
