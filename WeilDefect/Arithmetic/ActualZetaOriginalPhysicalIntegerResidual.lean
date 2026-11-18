import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerTaylor
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentTable

namespace WeilDefect

/-! NF637: residual checker on fixed-scale integer coordinates.
The cache and boundary rectangles must independently equal the
reference inputs. The local residual inequality uses cross products
rather than normalized rational arithmetic. -/

def NF636Rect.neg (a : NF636Rect) : NF636Rect :=
  ⟨a.re.neg,a.im.neg⟩

theorem NF636Rect.neg_denote (a : NF636Rect) (Q : ℕ) :
    a.neg.denote Q=(a.denote Q).neg := by
  simp only [NF636Rect.neg,NF636Rect.denote,NF591Rect.neg,NF636Ball.neg_denote]

def NF636Rect.upper (a : NF636Rect) : ℤ :=
  |a.re.mid|+a.re.rad+(|a.im.mid|+a.im.rad)

theorem NF636Rect.upper_denote (a : NF636Rect) (Q : ℕ) (hQ : 0<Q) :
    neutralNF615RectNormUpper (a.denote Q)=(a.upper:ℚ)/Q := by
  have hq : (0:ℚ)<Q := by exact_mod_cast hQ
  simp only [neutralNF615RectNormUpper,NF636Rect.denote,NF636Ball.denote,
    NF636Rect.upper,Int.cast_add,Int.cast_abs,abs_div,abs_of_pos hq]
  ring

structure NF637Row where
  re : ℤ
  im : ℤ
  rad : ℤ

def NF637Row.denote (q : NF637Row) (Q : ℕ) : NF617MomentRow :=
  ⟨(q.re:ℚ)/Q,(q.im:ℚ)/Q,(q.rad:ℚ)/Q⟩

def NF637Row.point (q : NF637Row) : NF636Rect :=
  ⟨⟨q.re,0⟩,⟨q.im,0⟩⟩

def neutralNF637NatRect (Q n : ℕ) : NF636Rect :=
  ⟨⟨(n:ℤ)*Q,0⟩,⟨0,0⟩⟩

def neutralNF637Base (B Z : NF636Rect) (q : NF637Row) (Q : ℕ) : NF636Rect :=
  B.add (Z.mul q.point Q).neg

def neutralNF637Succ (B Z : NF636Rect) (q prev : NF637Row) (Q n : ℕ) : NF636Rect :=
  (B.add (((neutralNF637NatRect Q (n+1)).mul prev.point Q).neg)).add
    (Z.mul q.point Q).neg

def neutralNF637Fee (a : NF636Rect) (q : NF637Row) (prior : ℤ)
    (d e : ℤ) : Bool :=
  decide (0<d ∧ 0<e ∧ 0≤q.rad ∧ e*(a.upper+prior)≤d*q.rad)

theorem neutralNF637Fee_sound (a : NF636Rect) (q : NF637Row) (prior d e : ℤ)
    (Q : ℕ) (hQ : 0<Q)
    (hc : neutralNF637Fee a q prior d e=true) :
    0≤(q.denote Q).rad ∧
    neutralNF615RectBelow (a.denote Q)
      (((d:ℚ)/e)*(q.denote Q).rad-(prior:ℚ)/Q)=true := by
  have h : 0<d ∧ 0<e ∧ 0≤q.rad ∧ e*(a.upper+prior)≤d*q.rad :=
    of_decide_eq_true hc
  have he : (0:ℚ)<e := by exact_mod_cast h.2.1
  have hq : (0:ℚ)<Q := by exact_mod_cast hQ
  constructor
  · exact div_nonneg (by exact_mod_cast h.2.2.1) hq.le
  · unfold neutralNF615RectBelow
    apply decide_eq_true
    rw [NF636Rect.upper_denote a Q hQ]
    change (a.upper:ℚ)/Q ≤ ((d:ℚ)/e)*((q.rad:ℚ)/Q)-(prior:ℚ)/Q
    have hp : (e:ℚ)*((a.upper:ℚ)+prior)≤(d:ℚ)*q.rad := by
      exact_mod_cast h.2.2.2
    have hp' : (a.upper:ℚ)+prior≤(d:ℚ)*q.rad/e := by
      apply (le_div_iff₀ he).mpr
      simpa only [mul_comm] using hp
    have hh := div_le_div_of_nonneg_right hp' hq.le
    calc
      (a.upper:ℚ)/Q = ((a.upper:ℚ)+prior)/Q-(prior:ℚ)/Q := by ring
      _ ≤ ((d:ℚ)*q.rad/e)/Q-(prior:ℚ)/Q := sub_le_sub_right hh _
      _ = ((d:ℚ)/e)*((q.rad:ℚ)/Q)-(prior:ℚ)/Q := by ring

def neutralNF637BaseGate (B Z : NF636Rect) (q : NF637Row)
    (Q : ℕ) (d e : ℤ) : Bool :=
  Z.mulGate q.point Q &&
    neutralNF637Fee (neutralNF637Base B Z q Q) q 0 d e

def neutralNF637SuccGate (B Z : NF636Rect) (q prev : NF637Row)
    (Q n : ℕ) (d e : ℤ) : Bool :=
  (neutralNF637NatRect Q (n+1)).mulGate prev.point Q &&
  (Z.mulGate q.point Q &&
    neutralNF637Fee (neutralNF637Succ B Z q prev Q n) q (((n+1:ℕ):ℤ)*prev.rad) d e)

theorem neutralNF637Base_to_ref (B Z : NF636Rect) (q : NF637Row)
    (Q : ℕ) (d e : ℤ) (hQ : 0<Q)
    (hq : q.point.denote Q=(q.denote Q).rect Q)
    (hc : neutralNF637BaseGate B Z q Q d e=true) :
    0≤(q.denote Q).rad ∧
    neutralNF615RectBelow
      (neutralNF615BaseResidualRect (B.denote Q) (Z.denote Q) ((q.denote Q).rect Q) Q)
      (((d:ℚ)/e)*(q.denote Q).rad)=true := by
  simp only [neutralNF637BaseGate,Bool.and_eq_true] at hc
  have h := neutralNF637Fee_sound _ q 0 d e Q hQ hc.2
  have he : (neutralNF637Base B Z q Q).denote Q =
      neutralNF615BaseResidualRect (B.denote Q) (Z.denote Q) ((q.denote Q).rect Q) Q := by
    simp only [neutralNF637Base,neutralNF615BaseResidualRect,NF636Rect.add_denote,
      NF636Rect.neg_denote,NF636Rect.mul_denote _ _ Q hQ hc.1,hq]
  rw [he] at h
  simpa using h

theorem neutralNF637Succ_to_ref (B Z : NF636Rect) (q prev : NF637Row)
    (Q n : ℕ) (d e : ℤ) (hQ : 0<Q)
    (hq : q.point.denote Q=(q.denote Q).rect Q)
    (hp : prev.point.denote Q=(prev.denote Q).rect Q)
    (hn : (neutralNF637NatRect Q (n+1)).denote Q=NF591Rect.realQ (n+1:ℚ) Q)
    (hc : neutralNF637SuccGate B Z q prev Q n d e=true) :
    0≤(q.denote Q).rad ∧
    neutralNF615RectBelow
      (neutralNF615ResidualRect (B.denote Q) (Z.denote Q)
        ((prev.denote Q).rect Q) ((q.denote Q).rect Q) Q n)
      (((d:ℚ)/e)*(q.denote Q).rad-(n+1:ℚ)*(prev.denote Q).rad)=true := by
  simp only [neutralNF637SuccGate,Bool.and_eq_true] at hc
  have h := neutralNF637Fee_sound _ q (((n+1:ℕ):ℤ)*prev.rad) d e Q hQ hc.2.2
  have he : (neutralNF637Succ B Z q prev Q n).denote Q =
      neutralNF615ResidualRect (B.denote Q) (Z.denote Q)
        ((prev.denote Q).rect Q) ((q.denote Q).rect Q) Q n := by
    simp only [neutralNF637Succ,neutralNF615ResidualRect,NF636Rect.add_denote,
      NF636Rect.neg_denote,NF636Rect.mul_denote _ _ Q hQ hc.1,
      NF636Rect.mul_denote _ _ Q hQ hc.2.1,hq,hp,hn]
  rw [he] at h
  have hcast : ((((n+1:ℕ):ℤ)*prev.rad:ℤ):ℚ)/Q=(n+1:ℚ)*(prev.denote Q).rad := by
    simp only [NF637Row.denote,Int.cast_mul,Int.cast_natCast,Nat.cast_add,Nat.cast_one]
    ring
  rwa [hcast] at h

end WeilDefect
