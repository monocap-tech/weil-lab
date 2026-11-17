import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointModeJets

namespace WeilDefect
noncomputable section

/-! NF593: a shared array of exact rounded exponential jet balls.
The recurrence is evaluated once per order. The lookup theorem is
an equality of rational rectangles, not just an enclosure bound. -/

def neutralNF593ReadRect (v : Array NF591Rect) (n : ℕ) : NF591Rect :=
  v[n]?.getD NF591Rect.zero

def neutralNF593ExpTable (a : NF591Rect) (Q : ℕ) : ℕ → Array NF591Rect
  | 0 => #[NF591Rect.one]
  | n+1 =>
    let v := neutralNF593ExpTable a Q n
    v.push (((neutralNF593ReadRect v n).mulQ a Q).divQ (n+1:ℚ) Q)

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
      simp only [if_pos rfl,neutralNF593ReadRect,ih n (by omega : n ≤ n),
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

def neutralNF593SmallExp (a : NF591Rect) (Q N : ℕ) : NF591Rect :=
  let table := neutralNF593ExpTable a Q N
  (neutralNF592RectSum (neutralNF593ReadRect table) N).expand (1/(Q:ℚ))

theorem neutralNF593SmallExp_eq (a : NF591Rect) (Q N : ℕ) :
    neutralNF593SmallExp a Q N = neutralNF592SmallExpBall a Q N := by
  unfold neutralNF593SmallExp neutralNF592SmallExpBall
  rw [neutralNF593Partial_eq_sum]
  congr 1
  apply neutralNF593RectSum_congr
  intro n hn
  exact neutralNF593ExpTable_read a Q N n (by omega)

def neutralNF593Phase (p : NF591Ball) (f : ℚ) (Q N : ℕ) : NF591Rect :=
  let a := neutralNF593SmallExp (neutralNF592PhaseArg p f Q) Q N
  let b := a.mulQ a Q
  b.mulQ b Q

theorem neutralNF593Phase_eq (p : NF591Ball) (f : ℚ) (Q N : ℕ) :
    neutralNF593Phase p f Q N = neutralNF592PhaseBall p f Q N := by
  simp only [neutralNF593Phase,neutralNF592PhaseBall,neutralNF593SmallExp_eq]

def neutralNF593ModeFromTable (table : Array NF591Rect) (Q k n : ℕ) : NF591Rect :=
  neutralNF592RectSum (fun m =>
    (neutralNF593ReadRect table (n-m)).scaleQ
      (NF591Ball.exactQ (neutralNF592PolyQ k m) Q) Q) (min k n+1)

theorem neutralNF593ModeFromTable_eq (a : NF591Rect) (Q K k n : ℕ) (hn : n ≤ K) :
    neutralNF593ModeFromTable (neutralNF593ExpTable a Q K) Q k n =
      neutralNF592ModeBall a Q k n := by
  unfold neutralNF593ModeFromTable neutralNF592ModeBall
  apply neutralNF593RectSum_congr
  intro m hm
  rw [neutralNF593ExpTable_read a Q K (n-m) (by omega)]

def neutralNF593OscillatorTable (p : NF591Ball) (f : ℚ) (Q N k K : ℕ) :
    Array NF591Ball :=
  let phase := neutralNF593Phase p f Q N
  let phase' := if Even k then phase.rotateMinusI else phase
  let table := neutralNF593ExpTable (neutralNF592FrequencyBall p f Q) Q K
  Array.ofFn (fun n : Fin K =>
    (phase'.mulQ (neutralNF593ModeFromTable table Q k n.val) Q).re)

def neutralNF593ReadBall (table : Array NF591Ball) (n : ℕ) : NF591Ball :=
  table[n]?.getD ⟨0,0⟩

theorem neutralNF593OscillatorTable_read (p : NF591Ball) (f : ℚ)
    (Q N k K n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593OscillatorTable p f Q N k K) n =
      neutralNF592OscillatorBall p f Q N k n := by
  unfold neutralNF593ReadBall neutralNF593OscillatorTable neutralNF592OscillatorBall
  simp only [Array.getElem?_ofFn,dif_pos hn,Option.getD_some,
    neutralNF593Phase_eq,neutralNF593ModeFromTable_eq _ _ _ _ _ (by omega : n ≤ K)]

def neutralNF593PoleTable (Q N K : ℕ) : Array NF591Ball :=
  let p := neutralNF593SmallExp (NF591Rect.realQ (11/20) Q) Q N
  let q := neutralNF593SmallExp (NF591Rect.realQ (-11/20) Q) Q N
  let ep := neutralNF593ExpTable (NF591Rect.realQ (-1/1000) Q) Q K
  let en := neutralNF593ExpTable (NF591Rect.realQ (1/1000) Q) Q K
  Array.ofFn (fun n : Fin K =>
    (((p.mulQ (neutralNF593ReadRect ep n.val) Q).re.add
      (q.mulQ (neutralNF593ReadRect en n.val) Q).re.neg).divPos 2).round Q)

theorem neutralNF593PoleTable_read (Q N K n : ℕ) (hn : n<K) :
    neutralNF593ReadBall (neutralNF593PoleTable Q N K) n =
      neutralNF592PoleBall Q N n := by
  unfold neutralNF593ReadBall neutralNF593PoleTable neutralNF592PoleBall
  simp only [Array.getElem?_ofFn,dif_pos hn,Option.getD_some,
    neutralNF593SmallExp_eq,neutralNF593ExpTable_read _ _ _ _ (by omega : n ≤ K)]

end
end WeilDefect
