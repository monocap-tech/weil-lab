import WeilDefect.Arithmetic.ActualZetaOriginalDirectedRounding
import WeilDefect.Arithmetic.ActualZetaOriginalJetRecurrence
import WeilDefect.Arithmetic.ActualZetaOriginalTranscendentalRemainders

namespace WeilDefect
noncomputable section
open Finset

/-! NF592: executable rational fixed-point arithmetic with the
NF591 outward-rounding convention. Q is generic, not a trust input.
The complex product rounds each of its four real products. -/

def NF591Ball.exactQ (q : ℚ) (Q : ℕ) : NF591Ball :=
  if (⌊q*(Q:ℚ)⌋:ℚ) = q*Q then ⟨q,0⟩ else (NF591Ball.mk q 0).round Q

theorem NF591Ball.contains_exactQ (q : ℚ) (Q : ℕ) (hQ : 0 < Q) :
    (NF591Ball.exactQ q Q).Contains (q:ℝ) := by
  have h : (NF591Ball.mk q 0).Contains (q:ℝ) := by simp [Contains]
  unfold exactQ
  split_ifs
  · exact h
  · exact contains_round h Q hQ

def NF591Ball.expand (a : NF591Ball) (r : ℚ) : NF591Ball :=
  ⟨a.mid,a.rad+r⟩

theorem NF591Ball.contains_expand {a : NF591Ball} {x y : ℝ} (r : ℚ)
    (hx : a.Contains x) (hy : |y-x| ≤ (r:ℝ)) :
    (a.expand r).Contains y := by
  unfold Contains at *
  simp only [expand,Rat.cast_add]
  calc
    |y-(a.mid:ℝ)| = |(y-x)+(x-(a.mid:ℝ))| := by congr 1 <;> ring
    _ ≤ |y-x|+|x-(a.mid:ℝ)| := abs_add_le _ _
    _ ≤ _ := by linarith

def NF591Rect.realQ (q : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨NF591Ball.exactQ q Q,⟨0,0⟩⟩

def NF591Rect.one : NF591Rect := ⟨⟨1,0⟩,⟨0,0⟩⟩
def NF591Rect.zero : NF591Rect := ⟨⟨0,0⟩,⟨0,0⟩⟩

theorem NF591Rect.contains_one : NF591Rect.one.Contains 1 := by
  simp [one,Contains,NF591Ball.Contains]

theorem NF591Rect.contains_zero : NF591Rect.zero.Contains 0 := by
  simp [zero,Contains,NF591Ball.Contains]

theorem NF591Rect.contains_realQ (q : ℚ) (Q : ℕ) (hQ : 0 < Q) :
    (NF591Rect.realQ q Q).Contains (q:ℂ) := by
  constructor
  · simpa [realQ,← Complex.ofReal_ratCast] using NF591Ball.contains_exactQ q Q hQ
  · simp [realQ,NF591Ball.Contains,← Complex.ofReal_ratCast]

def NF591Rect.mulQ (a b : NF591Rect) (Q : ℕ) : NF591Rect :=
  let p := fun x y : NF591Ball => (x.mul y).round Q
  ⟨(p a.re b.re).add (p a.im b.im).neg,
    (p a.re b.im).add (p a.im b.re)⟩

theorem NF591Rect.contains_mulQ {a b : NF591Rect} {z w : ℂ}
    (hz : a.Contains z) (hw : b.Contains w) (Q : ℕ) (hQ : 0 < Q) :
    (a.mulQ b Q).Contains (z*w) := by
  constructor
  · simpa only [mulQ,Complex.mul_re,sub_eq_add_neg] using
      NF591Ball.contains_add (NF591Ball.contains_rounded_mul hz.1 hw.1 Q hQ)
        (NF591Ball.contains_neg (NF591Ball.contains_rounded_mul hz.2 hw.2 Q hQ))
  · simpa only [mulQ,Complex.mul_im,add_comm] using
      NF591Ball.contains_add (NF591Ball.contains_rounded_mul hz.1 hw.2 Q hQ)
        (NF591Ball.contains_rounded_mul hz.2 hw.1 Q hQ)

def NF591Rect.divQ (a : NF591Rect) (d : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨(a.re.divPos d).round Q,(a.im.divPos d).round Q⟩

theorem NF591Rect.contains_divQ {a : NF591Rect} {z : ℂ}
    (hz : a.Contains z) (d : ℚ) (hd : 0 < d) (Q : ℕ) (hQ : 0 < Q) :
    (a.divQ d Q).Contains (z/(d:ℂ)) := by
  have he : z/(d:ℂ) = ((d:ℝ)⁻¹:ℝ) • z := by
    rw [Complex.real_smul,div_eq_mul_inv,Complex.ofReal_inv,Complex.ofReal_ratCast,mul_comm]
  rw [he]
  constructor
  · simpa only [divQ,Complex.smul_re,smul_eq_mul,div_eq_mul_inv,mul_comm] using
      NF591Ball.contains_rounded_div hz.1 d hd Q hQ
  · simpa only [divQ,Complex.smul_im,smul_eq_mul,div_eq_mul_inv,mul_comm] using
      NF591Ball.contains_rounded_div hz.2 d hd Q hQ

def NF591Rect.expand (a : NF591Rect) (r : ℚ) : NF591Rect :=
  ⟨a.re.expand r,a.im.expand r⟩

theorem NF591Rect.contains_expand {a : NF591Rect} {z w : ℂ}
    (hz : a.Contains z) (r : ℚ) (hw : ‖w-z‖ ≤ (r:ℝ)) :
    (a.expand r).Contains w := by
  have h1 := (Complex.abs_re_le_norm (w-z)).trans hw
  have h2 := (Complex.abs_im_le_norm (w-z)).trans hw
  exact ⟨NF591Ball.contains_expand r hz.1 (by simpa only [Complex.sub_re] using h1),
    NF591Ball.contains_expand r hz.2 (by simpa only [Complex.sub_im] using h2)⟩

/-- Same recurrence as the exact integer replay; no factorial or
large power is evaluated by floating-point arithmetic. -/
def neutralNF592ExpJetBall (a : NF591Rect) (Q : ℕ) : ℕ → NF591Rect
  | 0 => NF591Rect.one
  | n+1 => ((neutralNF592ExpJetBall a Q n).mulQ a Q).divQ (n+1:ℚ) Q

theorem neutralNF592ExpJetBall_sound (a : NF591Rect) (z : ℂ) (Q : ℕ)
    (hQ : 0 < Q) (ha : a.Contains z) (n : ℕ) :
    (neutralNF592ExpJetBall a Q n).Contains (neutralNF590ExpJet z n) := by
  induction n with
  | zero => exact NF591Rect.contains_one
  | succ n ih =>
    rw [neutralNF592ExpJetBall,neutralNF590ExpJet]
    simpa only [Rat.cast_add,Rat.cast_natCast,Rat.cast_one] using
      NF591Rect.contains_divQ (NF591Rect.contains_mulQ ih ha Q hQ)
        (n+1:ℚ) (by positivity) Q hQ

def neutralNF592ExpPartial (a : NF591Rect) (Q : ℕ) : ℕ → NF591Rect
  | 0 => NF591Rect.zero
  | n+1 => (neutralNF592ExpPartial a Q n).add (neutralNF592ExpJetBall a Q n)

theorem neutralNF592ExpPartial_sound (a : NF591Rect) (z : ℂ) (Q : ℕ)
    (hQ : 0 < Q) (ha : a.Contains z) (N : ℕ) :
    (neutralNF592ExpPartial a Q N).Contains
      (∑ n ∈ range N, z^n/(n.factorial:ℂ)) := by
  induction N with
  | zero => simpa [neutralNF592ExpPartial] using NF591Rect.contains_zero
  | succ N ih =>
    rw [neutralNF592ExpPartial,sum_range_succ]
    exact NF591Rect.contains_add ih
      (by simpa only [neutralNF590ExpJet_eq] using neutralNF592ExpJetBall_sound a z Q hQ ha N)

def neutralNF592SmallExpBall (a : NF591Rect) (Q N : ℕ) : NF591Rect :=
  (neutralNF592ExpPartial a Q N).expand (1/(Q:ℚ))

/-- The exact small-disc error must be paid by a rational
comparison, not asserted from the replay. -/
theorem neutralNF592SmallExpBall_sound (a : NF591Rect) (z : ℂ) (Q N : ℕ)
    (hQ : 0 < Q) (hN : 1 ≤ N) (ha : a.Contains z) (hz : ‖z‖ ≤ 1)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF592SmallExpBall a Q N).Contains (Complex.exp z) := by
  apply NF591Rect.contains_expand (neutralNF592ExpPartial_sound a z Q hQ ha N)
  simpa only [Rat.cast_div,Rat.cast_one,Rat.cast_natCast] using
    (neutralNF591SmallExp_tail z hz N hN).trans hfee

end
end WeilDefect
