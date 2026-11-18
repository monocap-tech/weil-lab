import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedPi

namespace WeilDefect

/-! NF644: preserve the exact alternating rounded Machin tail.
Once the denominator exceeds Q, the positive term rounds to (0,1/Q),
the negative term to (-1/Q,1/Q). A pair contributes (-1/Q,2/Q).
This is not an analytic truncation or a tighter replacement pi ball. -/

def neutralNF644Denom (p n : ℕ) : ℕ := p^(2*n+1)*(2*n+1)

theorem neutralNF644Denom_mono (p : ℕ) (hp : 1 ≤ p) :
    Monotone (neutralNF644Denom p) := by
  intro i j hij
  unfold neutralNF644Denom
  have he : 2*i+1 ≤ 2*j+1 := by omega
  exact Nat.mul_le_mul (Nat.pow_le_pow_right hp he) he

theorem neutralNF644Term (p n : ℕ) :
    neutralNF592AtanTerm (1/(p:ℚ)) n =
      (-1:ℚ)^n/(neutralNF644Denom p n:ℚ) := by
  unfold neutralNF592AtanTerm neutralNF644Denom
  push_cast
  rw [div_pow,one_pow,← mul_div_assoc,mul_one,div_div]

theorem neutralNF644PosRound (x : ℚ) (Q : ℕ)
    (h0 : 0 < x*Q) (h1 : x*Q < 1) :
    NF591Ball.exactQ x Q=⟨0,1/(Q:ℚ)⟩ := by
  have hf : ⌊x*Q⌋=(0:ℤ) := by
    apply Int.floor_eq_iff.mpr
    simpa using And.intro h0.le h1
  have hn : (⌊x*(Q:ℚ)⌋:ℚ)≠x*Q := by rw [hf]; exact ne_of_lt h0
  simp [NF591Ball.exactQ,hn,NF591Ball.round,hf]

theorem neutralNF644NegRound (x : ℚ) (Q : ℕ)
    (h0 : -1 < x*Q) (h1 : x*Q < 0) :
    NF591Ball.exactQ x Q=⟨-1/(Q:ℚ),1/(Q:ℚ)⟩ := by
  have hf : ⌊x*Q⌋=(-1:ℤ) := by
    apply Int.floor_eq_iff.mpr
    simpa using And.intro h0.le h1
  have hn : (⌊x*(Q:ℚ)⌋:ℚ)≠x*Q := by
    rw [hf]
    exact ne_of_lt (by simpa using h0)
  simp [NF591Ball.exactQ,hn,NF591Ball.round,hf]

theorem neutralNF644Pair (p Q k : ℕ) (hQ : 0 < Q)
    (hD : Q < neutralNF644Denom p (2*k))
    (hE : Q < neutralNF644Denom p (2*k+1)) :
    (NF591Ball.exactQ (neutralNF592AtanTerm (1/(p:ℚ)) (2*k)) Q).add
      (NF591Ball.exactQ (neutralNF592AtanTerm (1/(p:ℚ)) (2*k+1)) Q)=
        ⟨-1/(Q:ℚ),2/(Q:ℚ)⟩ := by
  have hq : (0:ℚ)<Q := by exact_mod_cast hQ
  have hd : (Q:ℚ)<(neutralNF644Denom p (2*k):ℚ) := by exact_mod_cast hD
  have he : (Q:ℚ)<(neutralNF644Denom p (2*k+1):ℚ) := by exact_mod_cast hE
  have hd0 := hq.trans hd
  have he0 := hq.trans he
  have hs : (-1:ℚ)^(2*k)=1 := by rw [pow_mul]; norm_num
  have ht : (-1:ℚ)^(2*k+1)=-1 := by rw [pow_succ,hs]; norm_num
  rw [neutralNF644Term,neutralNF644Term,hs,ht]
  have hu : (1/(neutralNF644Denom p (2*k):ℚ))*Q<1 := by
    rw [div_mul_eq_mul_div]
    apply (div_lt_iff₀ hd0).mpr
    simpa using hd
  have hv : -1 < (-1/(neutralNF644Denom p (2*k+1):ℚ))*Q := by
    rw [div_mul_eq_mul_div]
    apply (lt_div_iff₀ he0).mpr
    linarith
  rw [neutralNF644PosRound _ Q (mul_pos (div_pos (by norm_num) hd0) hq) hu,
      neutralNF644NegRound _ Q hv (mul_neg_of_neg_of_pos (div_neg_of_neg_of_pos (by norm_num) he0) hq)]
  simp only [NF591Ball.add,zero_add]
  congr 1 <;> ring

def neutralNF644Tail (Q pairs : ℕ) : NF591Ball :=
  ⟨-(pairs:ℚ)/Q,2*(pairs:ℚ)/Q⟩

theorem neutralNF644AtanTail (p Q start pairs : ℕ)
    (hp : 1 ≤ p) (hQ : 0 < Q) (hg : Q < neutralNF644Denom p (2*start)) :
    neutralNF592AtanPartial (1/(p:ℚ)) Q (2*start+2*pairs) =
      (neutralNF592AtanPartial (1/(p:ℚ)) Q (2*start)).add
        (neutralNF644Tail Q pairs) := by
  induction pairs with
  | zero =>
    simp [neutralNF644Tail,neutralNF632Ball_add_zero]
  | succ k ih =>
    have hidx : 2*start+2*(k+1)=2*(start+k)+1+1 := by omega
    have hd : Q < neutralNF644Denom p (2*(start+k)) :=
      hg.trans_le (neutralNF644Denom_mono p hp (by omega))
    have he : Q < neutralNF644Denom p (2*(start+k)+1) :=
      hg.trans_le (neutralNF644Denom_mono p hp (by omega))
    have hbase : 2*(start+k)=2*start+2*k := by omega
    rw [hidx,neutralNF592AtanPartial,neutralNF592AtanPartial,
      neutralNF632Ball_add_assoc,neutralNF644Pair p Q (start+k) hQ hd he,
      hbase,ih,neutralNF632Ball_add_assoc]
    congr 1
    simp only [neutralNF644Tail,NF591Ball.add,Nat.cast_succ]
    congr 1 <;> ring

theorem neutralNF644AtanTail_of_prefix (p Q start pairs : ℕ) (a b : NF591Ball)
    (hp : 1 ≤ p) (hQ : 0 < Q)
    (hg : decide (Q < neutralNF644Denom p (2*start))=true)
    (ha : neutralNF592AtanPartial (1/(p:ℚ)) Q (2*start)=a)
    (hb : neutralNF632BallEq (a.add (neutralNF644Tail Q pairs)) b=true) :
    neutralNF592AtanPartial (1/(p:ℚ)) Q (2*start+2*pairs)=b := by
  rw [neutralNF644AtanTail p Q start pairs hp hQ (of_decide_eq_true hg),ha]
  exact neutralNF632BallEq_sound _ _ hb

end WeilDefect
