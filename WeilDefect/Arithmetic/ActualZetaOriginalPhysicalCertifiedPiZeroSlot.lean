import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIndexedEndpoints
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedPi

namespace WeilDefect

/-! NF645: independent zero real slot and certified pi attachment.
This module deliberately does not depend on NF633/NF643, whose
new generic Taylor machinery is still awaiting compiler recovery.
For the zero argument, every rounded product is exactly constant,
irrespective of the incoming jet. No high-degree Taylor checks. -/

def neutralNF645RectEq (a b : NF591Rect) : Bool :=
  neutralNF632BallEq a.re b.re && neutralNF632BallEq a.im b.im

theorem neutralNF645RectEq_sound (a b : NF591Rect)
    (h : neutralNF645RectEq a b = true) : a=b := by
  simp only [neutralNF645RectEq,Bool.and_eq_true] at h
  have hr := neutralNF632BallEq_sound _ _ h.1
  have hi := neutralNF632BallEq_sound _ _ h.2
  cases a
  cases b
  simp_all

theorem neutralNF645Pi_attach (p certified : NF591Ball)
    (h : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=certified)
    (hc : neutralNF632BallEq certified p=true) :
    neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p :=
  h.trans (neutralNF632BallEq_sound _ _ hc)

theorem neutralNF645Mul_zero (b : NF591Ball) (Q : ℕ) :
    (b.mul ⟨0,0⟩).round Q=⟨0,1/(Q:ℚ)⟩ := by
  simp [NF591Ball.mul,NF591Ball.round]

def neutralNF645Fixed (Q : ℕ) : NF591Rect :=
  ⟨⟨0,2/(Q:ℚ)⟩,⟨0,2/(Q:ℚ)⟩⟩

theorem neutralNF645MulQ_zero (b : NF591Rect) (Q : ℕ) :
    b.mulQ NF591Rect.zero Q=neutralNF645Fixed Q := by
  unfold NF591Rect.mulQ
  dsimp only [NF591Rect.zero]
  simp only [neutralNF645Mul_zero,NF591Ball.add,NF591Ball.neg,
    neutralNF645Fixed,neg_zero,add_zero]
  congr 1 <;> congr 1 <;> ring

theorem neutralNF645DivBall (Q n : ℕ) (hQ : 0<Q) (hn : 1≤n) :
    (NF591Ball.divPos ⟨0,2/(Q:ℚ)⟩ ((n:ℚ)+1)).round Q=
      ⟨0,2/(Q:ℚ)⟩ := by
  have hq : (0:ℚ)<Q := by exact_mod_cast hQ
  have hd : (0:ℚ)<(n:ℚ)+1 := by positivity
  have hn' : (1:ℚ)≤n := by exact_mod_cast hn
  have he : (2/(Q:ℚ))/((n:ℚ)+1)*(Q:ℚ)=2/((n:ℚ)+1) := by
    field_simp [hq.ne',hd.ne']
  have hp : (0:ℚ)<2/((n:ℚ)+1) := by positivity
  have hu : (2:ℚ)/((n:ℚ)+1)≤1 := by
    apply (div_le_iff₀ hd).mpr
    linarith
  have hc : ⌈(2:ℚ)/((n:ℚ)+1)⌉=(1:ℤ) := by
    apply Int.ceil_eq_iff.mpr
    simpa using And.intro hp hu
  simp [NF591Ball.divPos,NF591Ball.round,he,hc] <;> norm_num

theorem neutralNF645ZeroJet (Q n : ℕ) (hQ : 0<Q) :
    neutralNF592ExpJetBall NF591Rect.zero Q (n+2)=neutralNF645Fixed Q := by
  rw [show n+2=(n+1)+1 by omega,neutralNF592ExpJetBall,
      neutralNF645MulQ_zero]
  change (NF591Rect.mk ⟨0,2/(Q:ℚ)⟩ ⟨0,2/(Q:ℚ)⟩).divQ
    (((n+1:ℕ):ℚ)+1) Q=neutralNF645Fixed Q
  simp only [NF591Rect.divQ,neutralNF645Fixed,neutralNF645DivBall Q (n+1) hQ (by omega)]
  
theorem neutralNF645ZeroPartial (Q len : ℕ) (hQ : 0<Q) :
    neutralNF592ExpPartial NF591Rect.zero Q (len+2)=
      (neutralNF592ExpPartial NF591Rect.zero Q 2).expand (2*(len:ℚ)/Q) := by
  induction len with
  | zero =>
    rcases h : neutralNF592ExpPartial NF591Rect.zero Q 2 with ⟨⟨x,r⟩,⟨y,s⟩⟩
    simp [NF591Rect.expand,NF591Ball.expand]
  | succ n ih =>
    rw [show n+1+2=(n+2)+1 by omega,neutralNF592ExpPartial,
        neutralNF645ZeroJet Q n hQ,ih]
    rcases h : neutralNF592ExpPartial NF591Rect.zero Q 2 with ⟨⟨x,r⟩,⟨y,s⟩⟩
    simp only [NF591Rect.expand,NF591Ball.expand,NF591Rect.add,NF591Ball.add,
      neutralNF645Fixed,add_zero,Nat.cast_add,Nat.cast_one]
    congr 1 <;> congr 1 <;> ring

theorem neutralNF645RealQ_zero (Q : ℕ) :
    NF591Rect.realQ ((0:ℚ)*11/20) Q = NF591Rect.zero := by
  simp [NF591Rect.realQ,NF591Rect.zero,NF591Ball.exactQ]

theorem neutralNF645ZeroSlot (a e : NF591Rect)
    (ha : neutralNF645RectEq
      (neutralNF592ExpPartial NF591Rect.zero neutralNF616Q 2) a=true)
    (he : neutralNF645RectEq
      ((a.expand (2*(1198:ℚ)/neutralNF616Q+1/(neutralNF616Q:ℚ))).mulQ
       (a.expand (2*(1198:ℚ)/neutralNF616Q+1/(neutralNF616Q:ℚ))) neutralNF616Q) e=true) :
    neutralNF635RealRef 0=e := by
  have hz := neutralNF645RealQ_zero neutralNF616Q
  have hsum := neutralNF645ZeroPartial neutralNF616Q 1198 neutralNF616Q_pos
  have ha' := neutralNF645RectEq_sound _ _ ha
  rw [ha'] at hsum
  unfold neutralNF635RealRef neutralNF621RealEndpoint
  rw [hz,neutralNF593SmallExp_eq]
  unfold neutralNF592SmallExpBall
  change ((neutralNF592ExpPartial NF591Rect.zero neutralNF616Q (1198+2)).expand
      (1/(neutralNF616Q:ℚ))).mulQ
      ((neutralNF592ExpPartial NF591Rect.zero neutralNF616Q (1198+2)).expand
      (1/(neutralNF616Q:ℚ))) neutralNF616Q=e
  rw [hsum]
  have hx (b : NF591Rect) (x y : ℚ) : (b.expand x).expand y=b.expand (x+y) := by
    rcases b with ⟨⟨u,r⟩,⟨v,s⟩⟩
    simp [NF591Rect.expand,NF591Ball.expand,add_assoc]
  rw [hx]
  exact neutralNF645RectEq_sound _ _ he

theorem neutralNF645Zero_attach (b : NF635EndpointBank) (i : ℕ) (v : NF591Rect)
    (hk : decide (neutralNF635ParamRead b.keys i=0)=true)
    (hv : neutralNF645RectEq (b.read i) v=true)
    (he : neutralNF635RealRef 0=v) :
    b.read i=neutralNF635RealRef (neutralNF635ParamRead b.keys i) := by
  rw [of_decide_eq_true hk,he]
  exact neutralNF645RectEq_sound _ _ hv

end WeilDefect
