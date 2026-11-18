import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedExp

namespace WeilDefect

/-! NF636: use integer coordinates instead of normalizing enormous
rational products for each Taylor step. The floor/ceil witness gate
checks two exact brackets, independently of the proposed quotient.
The additional +1 radius unit is the incumbent NF591 convention. -/

structure NF636Ball where
  mid : ℤ
  rad : ℤ
  deriving DecidableEq

def NF636Ball.denote (b : NF636Ball) (Q : ℕ) : NF591Ball :=
  ⟨(b.mid:ℚ)/Q,(b.rad:ℚ)/Q⟩

def NF636Ball.add (a b : NF636Ball) : NF636Ball :=
  ⟨a.mid+b.mid,a.rad+b.rad⟩

def NF636Ball.neg (a : NF636Ball) : NF636Ball := ⟨-a.mid,a.rad⟩

def NF636Ball.roundProposal (m r d : ℤ) : NF636Ball :=
  ⟨m/d,-((-r)/d)+1⟩

def NF636Ball.roundGate (m r d : ℤ) (b : NF636Ball) : Bool :=
  decide (0<d ∧ b.mid*d≤m ∧ m<(b.mid+1)*d ∧
    (b.rad-2)*d<r ∧ r≤(b.rad-1)*d)

theorem NF636Ball.roundGate_sound (m r d : ℤ) (b : NF636Ball)
    (Q : ℕ) (hQ : 0<Q) (hc : NF636Ball.roundGate m r d b=true) :
    (NF591Ball.mk ((m:ℚ)/d/Q) ((r:ℚ)/d/Q)).round Q=b.denote Q := by
  have h : 0<d ∧ b.mid*d≤m ∧ m<(b.mid+1)*d ∧
      (b.rad-2)*d<r ∧ r≤(b.rad-1)*d := of_decide_eq_true hc
  have hd : (0:ℚ)<d := by exact_mod_cast h.1
  have hq : (0:ℚ)<Q := by exact_mod_cast hQ
  have hm : ⌊(m:ℚ)/d⌋=b.mid := by
    apply Int.floor_eq_iff.mpr
    constructor
    · apply (le_div_iff₀ hd).mpr
      exact_mod_cast h.2.1
    · apply (div_lt_iff₀ hd).mpr
      exact_mod_cast h.2.2.1
  have hr : ⌈(r:ℚ)/d⌉=b.rad-1 := by
    apply Int.ceil_eq_iff.mpr
    constructor
    · have hh : (((b.rad-1:ℤ):ℚ)-1)*(d:ℚ)<(r:ℚ) := by
        push_cast
        exact_mod_cast h.2.2.2.1
      exact (lt_div_iff₀ hd).mpr hh
    · apply (div_le_iff₀ hd).mpr
      exact_mod_cast h.2.2.2.2
  unfold NF591Ball.round NF636Ball.denote
  dsimp only
  rw [div_mul_cancel₀ _ hq.ne',div_mul_cancel₀ _ hq.ne',hm,hr]
  have he : ((b.rad-1:ℤ):ℚ)+1=(b.rad:ℚ) := by push_cast; ring
  rw [he]

def NF636Ball.productRad (a b : NF636Ball) : ℤ :=
  |a.mid|*b.rad+|b.mid|*a.rad+a.rad*b.rad

def NF636Ball.mul (a b : NF636Ball) (Q : ℕ) : NF636Ball :=
  NF636Ball.roundProposal (a.mid*b.mid) (a.productRad b) Q

def NF636Ball.mulGate (a b : NF636Ball) (Q : ℕ) : Bool :=
  NF636Ball.roundGate (a.mid*b.mid) (a.productRad b) Q (a.mul b Q)

def NF636Ball.div (a : NF636Ball) (d : ℕ) : NF636Ball :=
  NF636Ball.roundProposal a.mid a.rad d

def NF636Ball.divGate (a : NF636Ball) (d : ℕ) : Bool :=
  NF636Ball.roundGate a.mid a.rad d (a.div d)

theorem NF636Ball.add_denote (a b : NF636Ball) (Q : ℕ) :
    (a.add b).denote Q=(a.denote Q).add (b.denote Q) := by
  simp [NF636Ball.add,NF636Ball.denote,NF591Ball.add,add_div]

theorem NF636Ball.neg_denote (a : NF636Ball) (Q : ℕ) :
    a.neg.denote Q=(a.denote Q).neg := by
  simp [NF636Ball.neg,NF636Ball.denote,NF591Ball.neg,neg_div]

theorem NF636Ball.mul_denote (a b : NF636Ball) (Q : ℕ)
    (hQ : 0<Q) (hc : a.mulGate b Q=true) :
    (a.mul b Q).denote Q=((a.denote Q).mul (b.denote Q)).round Q := by
  have hq : (0:ℚ)<Q := by exact_mod_cast hQ
  have he : (a.denote Q).mul (b.denote Q)=
      NF591Ball.mk (((a.mid*b.mid:ℤ):ℚ)/Q/Q)
        (((a.productRad b:ℤ):ℚ)/Q/Q) := by
    simp only [NF636Ball.denote,NF591Ball.mul,NF636Ball.productRad,
      Int.cast_mul,Int.cast_add,Int.cast_abs,abs_div,abs_of_pos hq]
    congr 1 <;> ring
  rw [he]
  symm
  exact NF636Ball.roundGate_sound _ _ _ _ Q hQ hc

theorem NF636Ball.div_denote (a : NF636Ball) (Q d : ℕ)
    (hQ : 0<Q) (hc : a.divGate d=true) :
    (a.div d).denote Q=((a.denote Q).divPos (d:ℚ)).round Q := by
  have he : (a.denote Q).divPos (d:ℚ)=
      NF591Ball.mk ((a.mid:ℚ)/d/Q) ((a.rad:ℚ)/d/Q) := by
    simp only [NF636Ball.denote,NF591Ball.divPos]
    congr 1 <;> ring
  rw [he]
  symm
  exact NF636Ball.roundGate_sound _ _ _ _ Q hQ hc

end WeilDefect
