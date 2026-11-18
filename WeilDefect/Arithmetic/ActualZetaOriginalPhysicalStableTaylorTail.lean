import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEndpointSlotCertificates

namespace WeilDefect

/-! NF643: exact stable rounded jet. Once zero midpoint and two
radius units are attained, a single product bound certifies every
later division. The tail is NOT discarded: each skipped term adds
two radius units to BOTH coordinates, exactly as the reference. -/

def neutralNF643Fixed (Q : ℕ) : NF591Rect :=
  ⟨⟨0,2/(Q:ℚ)⟩,⟨0,2/(Q:ℚ)⟩⟩

def neutralNF643StableGate (a : NF591Rect) (Q start : ℕ) : Bool :=
  let b := (neutralNF643Fixed Q).mulQ a Q
  decide (b.re.mid=0 ∧ b.im.mid=0 ∧
    0<b.re.rad*Q ∧ b.re.rad*Q≤(start:ℚ)+1 ∧
    0<b.im.rad*Q ∧ b.im.rad*Q≤(start:ℚ)+1)

theorem neutralNF643Div_fixed (b : NF591Ball) (Q n : ℕ)
    (hm : b.mid=0) (hr : 0<b.rad*(Q:ℚ))
    (hu : b.rad*(Q:ℚ)≤(n:ℚ)+1) :
    (b.divPos (n+1:ℚ)).round Q=⟨0,2/(Q:ℚ)⟩ := by
  have hd : (0:ℚ)<(n:ℚ)+1 := by positivity
  have hp : 0<b.rad/((n:ℚ)+1)*(Q:ℚ) := by
    rw [div_mul_eq_mul_div]
    exact div_pos hr hd
  have hle : b.rad/((n:ℚ)+1)*(Q:ℚ)≤1 := by
    rw [div_mul_eq_mul_div]
    apply (div_le_iff₀ hd).mpr
    simpa only [one_mul] using hu
  have hc : ⌈b.rad/((n:ℚ)+1)*(Q:ℚ)⌉=(1:ℤ) := by
    apply Int.ceil_eq_iff.mpr
    simpa using And.intro hp hle
  simp [NF591Ball.divPos,NF591Ball.round,hm,hc] <;> norm_num

theorem neutralNF643Stable_of_gate (a : NF591Rect) (Q start n : ℕ)
    (hn : start≤n) (hg : neutralNF643StableGate a Q start=true) :
    ((neutralNF643Fixed Q).mulQ a Q).divQ (n+1:ℚ) Q=
      neutralNF643Fixed Q := by
  let b := (neutralNF643Fixed Q).mulQ a Q
  have h : b.re.mid=0 ∧ b.im.mid=0 ∧
      0<b.re.rad*Q ∧ b.re.rad*Q≤(start:ℚ)+1 ∧
      0<b.im.rad*Q ∧ b.im.rad*Q≤(start:ℚ)+1 :=
    of_decide_eq_true hg
  have hn' : (start:ℚ)+1≤(n:ℚ)+1 := by
    exact add_le_add_right (by exact_mod_cast hn) 1
  have hr := neutralNF643Div_fixed b.re Q n h.1 h.2.2.1
    (h.2.2.2.1.trans hn')
  have hi := neutralNF643Div_fixed b.im Q n h.2.1 h.2.2.2.2.1
    (h.2.2.2.2.2.trans hn')
  change b.divQ (n+1:ℚ) Q=neutralNF643Fixed Q
  simp only [NF591Rect.divQ,hr,hi,neutralNF643Fixed]

def neutralNF643Tail (s : NF633ExpState) (Q len : ℕ) : NF633ExpState :=
  ⟨neutralNF643Fixed Q,s.sumState.expand (2*(len:ℚ)/Q)⟩

theorem neutralNF643Expand_zero (b : NF591Rect) (Q : ℕ) :
    b.expand (2*(0:ℚ)/Q)=b := by
  rcases b with ⟨⟨x,r⟩,⟨y,s⟩⟩
  simp [NF591Rect.expand,NF591Ball.expand]

theorem neutralNF643Expand_step (b : NF591Rect) (Q len : ℕ) :
    (b.expand (2*(len:ℚ)/Q)).add (neutralNF643Fixed Q)=
      b.expand (2*((len+1:ℕ):ℚ)/Q) := by
  rcases b with ⟨⟨x,r⟩,⟨y,s⟩⟩
  simp only [NF591Rect.expand,NF591Ball.expand,NF591Rect.add,NF591Ball.add,
    neutralNF643Fixed,add_zero,Nat.cast_add,Nat.cast_one]
  congr 1 <;> congr 1 <;> ring

theorem neutralNF643Tail_of_prefix (a : NF591Rect) (Q start len : ℕ)
    (s : NF633ExpState)
    (hs : neutralNF633State a Q start=s)
    (hj : s.jet=neutralNF643Fixed Q)
    (hg : neutralNF643StableGate a Q start=true) :
    neutralNF633State a Q (start+len)=neutralNF643Tail s Q len := by
  induction len with
  | zero =>
    simp only [Nat.add_zero,hs,neutralNF643Tail,Nat.cast_zero,neutralNF643Expand_zero]
    cases s
    simp_all
  | succ n ih =>
    rw [Nat.add_succ,← neutralNF633State_step,ih]
    unfold neutralNF643Tail NF633ExpState.step
    dsimp only
    rw [neutralNF643Stable_of_gate a Q start (start+n) (by omega) hg,
      neutralNF643Expand_step]

theorem neutralNF643Tail_to_state (a : NF591Rect) (Q start len : ℕ)
    (s t : NF633ExpState)
    (hs : neutralNF633State a Q start=s)
    (hj : neutralNF633RectEq s.jet (neutralNF643Fixed Q)=true)
    (hg : neutralNF643StableGate a Q start=true)
    (ht : neutralNF633StateEq (neutralNF643Tail s Q len) t=true) :
    neutralNF633State a Q (start+len)=t :=
  (neutralNF643Tail_of_prefix a Q start len s hs
    (neutralNF633RectEq_sound _ _ hj) hg).trans
      (neutralNF633StateEq_sound _ _ ht)

end WeilDefect
