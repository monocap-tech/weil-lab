import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerResidual
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFullTableSound

namespace WeilDefect

/-! NF638: exact point and boundary representation. Build every
boundary from the two shared integer endpoints; do not store a new
2600-digit boundary rectangle for each moment row. -/

theorem neutralNF638ExactQ_scaled (m : ℤ) (Q : ℕ) (hQ : 0<Q) :
    NF591Ball.exactQ ((m:ℚ)/Q) Q=⟨(m:ℚ)/Q,0⟩ := by
  have hq : (Q:ℚ)≠0 := by exact_mod_cast hQ.ne'
  have he : ((m:ℚ)/Q)*(Q:ℚ)=(m:ℚ) := div_mul_cancel₀ _ hq
  simp [NF591Ball.exactQ,he]

theorem NF637Row.point_denote (q : NF637Row) (Q : ℕ) (hQ : 0<Q) :
    q.point.denote Q=(q.denote Q).rect Q := by
  simp [NF637Row.point,NF637Row.denote,NF617MomentRow.rect,
    NF636Rect.denote,NF636Ball.denote,neutralNF638ExactQ_scaled _ Q hQ]

theorem neutralNF638NatRect_denote (Q n : ℕ) (hQ : 0<Q) :
    (neutralNF637NatRect Q n).denote Q=NF591Rect.realQ (n:ℚ) Q := by
  have hq : (Q:ℚ)≠0 := by exact_mod_cast hQ.ne'
  have he : (((n:ℤ)*(Q:ℤ):ℤ):ℚ)/Q=(n:ℚ) := by
    push_cast
    field_simp [hq]
  have hx := neutralNF638ExactQ_scaled ((n:ℤ)*(Q:ℤ)) Q hQ
  rw [he] at hx
  simp [neutralNF637NatRect,NF636Rect.denote,NF636Ball.denote,
    NF591Rect.realQ,he,hx]

def neutralNF638PowerMid (Q : ℕ) (b : ℤ) (n : ℕ) : ℤ :=
  (Q:ℤ)*b^n/10^n

def neutralNF638PowerGate (Q : ℕ) (b : ℤ) (n : ℕ) : Bool :=
  decide (neutralNF638PowerMid Q b n*10^n=(Q:ℤ)*b^n)

def neutralNF638PowerRect (Q : ℕ) (b : ℤ) (n : ℕ) : NF636Rect :=
  ⟨⟨neutralNF638PowerMid Q b n,0⟩,⟨0,0⟩⟩

theorem neutralNF638PowerRect_denote (Q : ℕ) (b : ℤ) (n : ℕ)
    (hQ : 0<Q) (hc : neutralNF638PowerGate Q b n=true) :
    (neutralNF638PowerRect Q b n).denote Q=NF591Rect.realQ (((b:ℚ)/10)^n) Q := by
  have hi : neutralNF638PowerMid Q b n*10^n=(Q:ℤ)*b^n := of_decide_eq_true hc
  have h : (neutralNF638PowerMid Q b n:ℚ)*(10:ℚ)^n=(Q:ℚ)*(b:ℚ)^n := by
    exact_mod_cast hi
  have hq : (Q:ℚ)≠0 := by exact_mod_cast hQ.ne'
  have ht : (10:ℚ)^n≠0 := by positivity
  have he : (neutralNF638PowerMid Q b n:ℚ)/Q=((b:ℚ)/10)^n := by
    rw [div_pow]
    apply (div_eq_div_iff hq ht).mpr
    simpa only [mul_comm] using h
  have hx := neutralNF638ExactQ_scaled (neutralNF638PowerMid Q b n) Q hQ
  rw [he] at hx
  simp [neutralNF638PowerRect,NF636Rect.denote,NF636Ball.denote,
    NF591Rect.realQ,he,hx]

structure NF638Cache where
  z : NF636Rect
  pos : NF636Rect
  neg : NF636Rect

def NF638Cache.denote (c : NF638Cache) (Q : ℕ) : NF617MomentCache :=
  ⟨c.z.denote Q,c.pos.denote Q,c.neg.denote Q⟩

def NF638Cache.boundary (c : NF638Cache) (Q n : ℕ) : NF636Rect :=
  ((neutralNF638PowerRect Q 11 n).mul c.pos Q).add
    (((neutralNF638PowerRect Q (-11) n).mul c.neg Q).neg)

def NF638Cache.boundaryGate (c : NF638Cache) (Q n : ℕ) : Bool :=
  neutralNF638PowerGate Q 11 n &&
    (neutralNF638PowerGate Q (-11) n &&
    ((neutralNF638PowerRect Q 11 n).mulGate c.pos Q &&
     (neutralNF638PowerRect Q (-11) n).mulGate c.neg Q))

theorem NF638Cache.boundary_denote (c : NF638Cache) (Q n : ℕ)
    (hQ : 0<Q) (hc : c.boundaryGate Q n=true) :
    (c.boundary Q n).denote Q=(c.denote Q).boundary Q n := by
  simp only [NF638Cache.boundaryGate,Bool.and_eq_true] at hc
  simp only [NF638Cache.boundary,NF638Cache.denote,NF617MomentCache.boundary,
    NF636Rect.add_denote,NF636Rect.neg_denote,
    NF636Rect.mul_denote _ _ Q hQ hc.2.2.1,
    NF636Rect.mul_denote _ _ Q hQ hc.2.2.2,
    neutralNF638PowerRect_denote Q 11 n hQ hc.1,
    neutralNF638PowerRect_denote Q (-11) n hQ hc.2.1] <;> norm_num

end WeilDefect
