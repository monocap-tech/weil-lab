import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointExpRecurrence

namespace WeilDefect
noncomputable section
open Finset

/-! NF592: the actual transcendental inputs of the fixedpoint
replay, including periodic reduction of the historical oscillator
phase. Only the constant phase is reduced. The jet frequency is
always the full original frequency. -/

def neutralNF592AtanTerm (x : ℚ) (n : ℕ) : ℚ :=
  (-1:ℚ)^n*x^(2*n+1)/(2*n+1:ℚ)

def neutralNF592AtanPartial (x : ℚ) (Q : ℕ) : ℕ → NF591Ball
  | 0 => ⟨0,0⟩
  | n+1 => (neutralNF592AtanPartial x Q n).add
    (NF591Ball.exactQ (neutralNF592AtanTerm x n) Q)

theorem neutralNF592AtanPartial_sound (x : ℚ) (Q : ℕ) (hQ : 0 < Q) (N : ℕ) :
    (neutralNF592AtanPartial x Q N).Contains (neutralNF591AtanPoly N (x:ℝ)) := by
  induction N with
  | zero => simp [neutralNF592AtanPartial,neutralNF591AtanPoly,NF591Ball.Contains]
  | succ N ih =>
    rw [neutralNF592AtanPartial,neutralNF591AtanPoly,sum_range_succ]
    apply NF591Ball.contains_add ih
    simpa only [neutralNF592AtanTerm,Rat.cast_div,Rat.cast_mul,Rat.cast_pow,
      Rat.cast_add,Rat.cast_neg,Rat.cast_one,Rat.cast_ofNat,Rat.cast_natCast] using
      NF591Ball.contains_exactQ (neutralNF592AtanTerm x N) Q hQ

def neutralNF592AtanBall (x : ℚ) (Q N : ℕ) : NF591Ball :=
  (neutralNF592AtanPartial x Q N).expand (1/(Q:ℚ))

theorem neutralNF592AtanBall_sound (x : ℚ) (Q N : ℕ) (hQ : 0 < Q)
    (hx : 0 ≤ x) (hfee : (x:ℝ)^(2*N+1)/(2*N+1:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF592AtanBall x Q N).Contains (Real.arctan (x:ℝ)) := by
  apply NF591Ball.contains_expand _ (neutralNF592AtanPartial_sound x Q hQ N)
  simpa only [Rat.cast_div,Rat.cast_one,Rat.cast_natCast] using
    (neutralNF591Atan_tail (x:ℝ) (by exact_mod_cast hx) N).trans hfee

def neutralNF592PiBall (Q N : ℕ) : NF591Ball :=
  (((NF591Ball.exactQ 16 Q).mul (neutralNF592AtanBall (1/5) Q N)).round Q).add
    ((((NF591Ball.exactQ 4 Q).mul (neutralNF592AtanBall (1/239) Q N)).round Q).neg)

theorem neutralNF592PiBall_sound (Q N : ℕ) (hQ : 0 < Q)
    (h5 : (1/5:ℝ)^(2*N+1)/(2*N+1:ℝ) ≤ 1/(Q:ℝ))
    (h239 : (1/239:ℝ)^(2*N+1)/(2*N+1:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF592PiBall Q N).Contains Real.pi := by
  have h1 := neutralNF592AtanBall_sound (1/5) Q N hQ (by norm_num)
    (by simpa using h5)
  have h2 := neutralNF592AtanBall_sound (1/239) Q N hQ (by norm_num)
    (by simpa using h239)
  have hp := NF591Ball.contains_rounded_mul
    (NF591Ball.contains_exactQ 16 Q hQ) h1 Q hQ
  have hn := NF591Ball.contains_rounded_mul
    (NF591Ball.contains_exactQ 4 Q hQ) h2 Q hQ
  have h := NF591Ball.contains_add hp (NF591Ball.contains_neg hn)
  have hm := Real.four_mul_arctan_inv_5_sub_arctan_inv_239
  have he : (16:ℝ)*Real.arctan (1/5)-4*Real.arctan (1/239) = Real.pi := by
    simp only [one_div]
    linarith
  convert h using 1
  · simp [neutralNF592PiBall]
  · norm_num
    linarith [he]

def neutralNF592Turns (f : ℚ) : ℤ := ⌊f*(11/10:ℚ)+1/2⌋

def neutralNF592Reduced (f : ℚ) : ℚ :=
  f*(11/10:ℚ)-neutralNF592Turns f

theorem neutralNF592Reduced_abs (f : ℚ) : |neutralNF592Reduced f| ≤ 1/2 := by
  have h1 := Int.floor_le (f*(11/10:ℚ)+1/2)
  have h2 := Int.lt_floor_add_one (f*(11/10:ℚ)+1/2)
  unfold neutralNF592Reduced neutralNF592Turns
  exact abs_le.mpr ⟨by linarith,by linarith⟩

theorem neutralNF592Phase_identity (f : ℚ) :
    Complex.exp (Complex.I*((2*Real.pi*(f:ℝ):ℝ):ℂ)*(11/10)) =
      (Complex.exp (Complex.I*(Real.pi:ℂ)*(neutralNF592Reduced f:ℂ)/2))^4 := by
  let z := Complex.I*(Real.pi:ℂ)*(neutralNF592Reduced f:ℂ)/2
  have h : Complex.I*((2*Real.pi*(f:ℝ):ℝ):ℂ)*(11/10) =
      (4:ℂ)*z+(neutralNF592Turns f:ℂ)*(2*(Real.pi:ℂ)*Complex.I) := by
    dsimp [z,neutralNF592Reduced]
    push_cast
    ring
  rw [h,Complex.exp_add,Complex.exp_int_mul_two_pi_mul_I,mul_one]
  simpa using Complex.exp_nat_mul z 4

theorem neutralNF592Reduced_norm (f : ℚ) :
    ‖Complex.I*(Real.pi:ℂ)*(neutralNF592Reduced f:ℂ)/2‖ ≤ 1 := by
  have h := neutralNF592Reduced_abs f
  have hr : |(neutralNF592Reduced f:ℝ)| ≤ 1/2 := by exact_mod_cast h
  rw [norm_div,norm_mul,norm_mul,Complex.norm_I,one_mul,
    Complex.norm_real,Real.norm_eq_abs,abs_of_pos Real.pi_pos,
    ← Complex.ofReal_ratCast,Complex.norm_real,Real.norm_eq_abs,
    show ‖(2:ℂ)‖=2 by norm_num]
  have hp := mul_le_mul Real.pi_lt_four.le hr (abs_nonneg _) (by norm_num : (0:ℝ)≤4)
  linarith

def neutralNF592PhaseArg (p : NF591Ball) (f : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨⟨0,0⟩,(p.mul (NF591Ball.exactQ (neutralNF592Reduced f/2) Q)).round Q⟩

theorem neutralNF592PhaseArg_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (f : ℚ) (Q : ℕ) (hQ : 0 < Q) :
    (neutralNF592PhaseArg p f Q).Contains
      (Complex.I*(Real.pi:ℂ)*(neutralNF592Reduced f:ℂ)/2) := by
  have he : Complex.I*(Real.pi:ℂ)*(neutralNF592Reduced f:ℂ)/2 =
      ((Real.pi*(neutralNF592Reduced f:ℝ)/2:ℝ):ℂ)*Complex.I := by
    push_cast
    ring
  rw [he]
  constructor
  · simp [neutralNF592PhaseArg,NF591Ball.Contains,Complex.mul_re]
  · have h := NF591Ball.contains_rounded_mul hp
        (NF591Ball.contains_exactQ (neutralNF592Reduced f/2) Q hQ) Q hQ
    simpa [neutralNF592PhaseArg,Complex.mul_im,Rat.cast_div,mul_div_assoc] using h

def neutralNF592PhaseBall (p : NF591Ball) (f : ℚ) (Q N : ℕ) : NF591Rect :=
  let a := neutralNF592SmallExpBall (neutralNF592PhaseArg p f Q) Q N
  let b := a.mulQ a Q
  b.mulQ b Q

theorem neutralNF592PhaseBall_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (f : ℚ) (Q N : ℕ) (hQ : 0 < Q) (hN : 1 ≤ N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF592PhaseBall p f Q N).Contains
      (Complex.exp (Complex.I*((2*Real.pi*(f:ℝ):ℝ):ℂ)*(11/10))) := by
  let z := Complex.I*(Real.pi:ℂ)*(neutralNF592Reduced f:ℂ)/2
  have h := neutralNF592SmallExpBall_sound _ z Q N hQ hN
    (neutralNF592PhaseArg_sound p hp f Q hQ) (neutralNF592Reduced_norm f) hfee
  have h2 := NF591Rect.contains_mulQ h h Q hQ
  have h4 := NF591Rect.contains_mulQ h2 h2 Q hQ
  rw [neutralNF592Phase_identity]
  convert h4 using 1
  ring

end
end WeilDefect
