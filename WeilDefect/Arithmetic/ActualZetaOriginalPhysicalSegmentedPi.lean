import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalReceiptParameters

namespace WeilDefect

/-! NF632: segment the original Machin computation, keeping exact
reference semantics. A segment can be evaluated without evaluating
any earlier segment. The join proof rewrites by local certificates,
rather than reducing the whole 4000-term rational expression again. -/

def neutralNF632AtanSegment (x : ℚ) (Q start : ℕ) : ℕ → NF591Ball
  | 0 => ⟨0,0⟩
  | n+1 => (neutralNF632AtanSegment x Q start n).add
      (NF591Ball.exactQ (neutralNF592AtanTerm x (start+n)) Q)

theorem neutralNF632Ball_add_assoc (a b c : NF591Ball) :
    (a.add b).add c = a.add (b.add c) := by
  cases a; cases b; cases c
  simp [NF591Ball.add,add_assoc]

theorem neutralNF632Ball_add_zero (a : NF591Ball) :
    a.add ⟨0,0⟩ = a := by
  cases a
  simp [NF591Ball.add]

theorem neutralNF632AtanPartial_extend (x : ℚ) (Q start len : ℕ) :
    neutralNF592AtanPartial x Q (start+len) =
      (neutralNF592AtanPartial x Q start).add
        (neutralNF632AtanSegment x Q start len) := by
  induction len with
  | zero => simp [neutralNF632AtanSegment,neutralNF632Ball_add_zero]
  | succ n ih =>
    rw [Nat.add_succ,neutralNF592AtanPartial,neutralNF632AtanSegment,ih]
    exact neutralNF632Ball_add_assoc _ _ _

def neutralNF632BallEq (a b : NF591Ball) : Bool :=
  decide (a.mid=b.mid ∧ a.rad=b.rad)

theorem neutralNF632BallEq_sound (a b : NF591Ball)
    (h : neutralNF632BallEq a b=true) : a=b := by
  have he : a.mid=b.mid ∧ a.rad=b.rad := of_decide_eq_true h
  cases a
  cases b
  simp_all

theorem neutralNF632AtanPrefix_extend (x : ℚ) (Q start len : ℕ)
    (a b c : NF591Ball)
    (ha : neutralNF592AtanPartial x Q start = a)
    (hb : neutralNF632BallEq (neutralNF632AtanSegment x Q start len) b=true)
    (hc : neutralNF632BallEq (a.add b) c=true) :
    neutralNF592AtanPartial x Q (start+len) = c := by
  rw [neutralNF632AtanPartial_extend,ha,neutralNF632BallEq_sound _ _ hb]
  exact neutralNF632BallEq_sound _ _ hc

def neutralNF632PiFromPartials (a b : NF591Ball) (Q : ℕ) : NF591Ball :=
  (((NF591Ball.exactQ 16 Q).mul (a.expand (1/(Q:ℚ)))).round Q).add
    ((((NF591Ball.exactQ 4 Q).mul (b.expand (1/(Q:ℚ)))).round Q).neg)

theorem neutralNF632Pi_of_partials (Q N : ℕ) (a b p : NF591Ball)
    (ha : neutralNF592AtanPartial (1/5) Q N=a)
    (hb : neutralNF592AtanPartial (1/239) Q N=b)
    (hc : neutralNF632BallEq (neutralNF632PiFromPartials a b Q) p=true) :
    neutralNF592PiBall Q N=p := by
  unfold neutralNF592PiBall neutralNF592AtanBall
  rw [ha,hb]
  exact neutralNF632BallEq_sound _ _ hc

theorem neutralNF632HighPrecisionPi_sound (p : NF591Ball)
    (h : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p) :
    p.Contains Real.pi := by
  rw [← h]
  exact neutralNF616Pi_sound

end WeilDefect
