import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointPhase
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentEnclosure

namespace WeilDefect
noncomputable section

/-! NF615: the actual exponential moment frequencies have rational
real part and rational multiples of 2π in the imaginary part.
Reuse the accepted periodic reduction instead of expanding a
large imaginary argument. Keep precision generic. -/

def neutralNF615Lambda (h f : ℚ) : ℂ :=
  (h:ℂ) + Complex.I*((2*Real.pi*(f:ℝ):ℝ):ℂ)

def neutralNF615LambdaRect (p : NF591Ball) (h f : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨NF591Ball.exactQ h Q,
    (p.mul (NF591Ball.exactQ (2*f) Q)).round Q⟩

theorem neutralNF615LambdaRect_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (h f : ℚ) (Q : ℕ) (hQ : 0<Q) :
    (neutralNF615LambdaRect p h f Q).Contains (neutralNF615Lambda h f) := by
  constructor
  · simpa [neutralNF615LambdaRect,neutralNF615Lambda,Complex.add_re,
      Complex.mul_re,← Complex.ofReal_ratCast] using NF591Ball.contains_exactQ h Q hQ
  · have hh := NF591Ball.contains_rounded_mul hp
      (NF591Ball.contains_exactQ (2*f) Q hQ) Q hQ
    have he : (neutralNF615Lambda h f).im = Real.pi*((2*f:ℚ):ℝ) := by
      simp [neutralNF615Lambda,← Complex.ofReal_ratCast]
      ring
    rw [he]
    exact hh

def neutralNF615RealEndpoint (h : ℚ) (Q N : ℕ) : NF591Rect :=
  let a := neutralNF592SmallExpBall (NF591Rect.realQ (h*11/20) Q) Q N
  a.mulQ a Q

theorem neutralNF615RealEndpoint_sound (h : ℚ) (hh : |h| ≤ 1)
    (Q N : ℕ) (hQ : 0<Q) (hN : 1≤N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF615RealEndpoint h Q N).Contains (Complex.exp ((h:ℂ)*(11/10))) := by
  let z : ℂ := ((h*11/20:ℚ):ℂ)
  have hz : ‖z‖ ≤ 1 := by
    have hr : |(h:ℝ)| ≤ 1 := by exact_mod_cast hh
    dsimp [z]
    rw [← Complex.ofReal_ratCast,Complex.norm_real]
    push_cast
    rw [abs_div,abs_mul,abs_of_pos (by norm_num : (0:ℝ)<11),
      abs_of_pos (by norm_num : (0:ℝ)<20)]
    linarith
  have ha := neutralNF592SmallExpBall_sound _ z Q N hQ hN
    (NF591Rect.contains_realQ (h*11/20) Q hQ) hz hfee
  have hs := NF591Rect.contains_mulQ ha ha Q hQ
  have he : z+z=(h:ℂ)*(11/10) := by dsimp [z]; push_cast; ring
  rw [← he,Complex.exp_add]
  exact hs

def neutralNF615Endpoint (p : NF591Ball) (h f : ℚ) (Q N : ℕ) : NF591Rect :=
  (neutralNF615RealEndpoint h Q N).mulQ (neutralNF592PhaseBall p f Q N) Q

theorem neutralNF615Endpoint_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (h f : ℚ) (hh : |h|≤1) (Q N : ℕ) (hQ : 0<Q) (hN : 1≤N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF615Endpoint p h f Q N).Contains
      (Complex.exp (neutralNF615Lambda h f*(11/10))) := by
  have ha := neutralNF615RealEndpoint_sound h hh Q N hQ hN hfee
  have hb := neutralNF592PhaseBall_sound p hp f Q N hQ hN hfee
  unfold neutralNF615Endpoint neutralNF615Lambda
  rw [add_mul,Complex.exp_add,mul_assoc]
  exact NF591Rect.contains_mulQ ha hb Q hQ

theorem neutralNF615Lambda_neg (h f : ℚ) :
    neutralNF615Lambda (-h) (-f) = -neutralNF615Lambda h f := by
  unfold neutralNF615Lambda
  push_cast
  ring

def neutralNF615BoundaryRect (p : NF591Ball) (h f : ℚ) (Q N n : ℕ) : NF591Rect :=
  ((NF591Rect.realQ ((11/10:ℚ)^n) Q).mulQ
    (neutralNF615Endpoint p h f Q N) Q).add
    (((NF591Rect.realQ ((-11/10:ℚ)^n) Q).mulQ
      (neutralNF615Endpoint p (-h) (-f) Q N) Q).neg)

theorem neutralNF615BoundaryRect_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (h f : ℚ) (hh : |h|≤1) (Q N n : ℕ) (hQ : 0<Q) (hN : 1≤N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF615BoundaryRect p h f Q N n).Contains
      (neutralNF614Boundary (-(11/10:ℝ)) (11/10:ℝ) (neutralNF615Lambda h f) n) := by
  have hpos := neutralNF615Endpoint_sound p hp h f hh Q N hQ hN hfee
  have hneg := neutralNF615Endpoint_sound p hp (-h) (-f) (by simpa using hh)
    Q N hQ hN hfee
  rw [neutralNF615Lambda_neg,neg_mul] at hneg
  have hb := NF591Rect.contains_mulQ
    (NF591Rect.contains_realQ ((11/10:ℚ)^n) Q hQ) hpos Q hQ
  have ha := NF591Rect.contains_mulQ
    (NF591Rect.contains_realQ ((-11/10:ℚ)^n) Q hQ) hneg Q hQ
  unfold neutralNF615BoundaryRect neutralNF614Boundary
  convert NF591Rect.contains_add hb (NF591Rect.contains_neg ha) using 1 <;>
    push_cast <;> ring

end
end WeilDefect
