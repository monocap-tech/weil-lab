import Mathlib

namespace WeilDefect
noncomputable section

/-! NF589: elementary complex-disc majorants. The exponential
growth depends on the imaginary part, not the absolute frequency
times the full real collar center. -/

theorem neutralNF589Exp_le_pow_three (x : ℝ) (N : ℕ) (hx : x ≤ N) :
    Real.exp x ≤ (3:ℝ)^N := by
  calc
    _ ≤ Real.exp (N:ℝ) := Real.exp_le_exp.mpr hx
    _ = (Real.exp 1)^N := by
      simpa only [mul_one] using Real.exp_nat_mul 1 N
    _ ≤ _ := pow_le_pow_left₀ (Real.exp_pos _).le Real.exp_one_lt_three.le _

theorem neutralNF589Sin_norm (z : ℂ) :
    ‖Complex.sin z‖ ≤ Real.exp |z.im| := by
  have hp : ‖Complex.exp (z*Complex.I)‖ ≤ Real.exp |z.im| := by
    rw [Complex.norm_exp]
    apply Real.exp_le_exp.mpr
    simpa [Complex.mul_re] using neg_le_abs z.im
  have hn : ‖Complex.exp (-z*Complex.I)‖ ≤ Real.exp |z.im| := by
    rw [Complex.norm_exp]
    apply Real.exp_le_exp.mpr
    simpa [Complex.mul_re,Complex.neg_im] using le_abs_self z.im
  have h : 2*‖Complex.sin z‖ ≤ 2*Real.exp |z.im| := by
    calc
      _ = ‖(2:ℂ)*Complex.sin z‖ := by rw [norm_mul]; norm_num
      _ = ‖(Complex.exp (-z*Complex.I)-Complex.exp (z*Complex.I))*Complex.I‖ := by rw [Complex.two_sin]
      _ ≤ _ := by
        rw [norm_mul,Complex.norm_I,mul_one]
        linarith [norm_sub_le (Complex.exp (-z*Complex.I)) (Complex.exp (z*Complex.I))]
  linarith

theorem neutralNF589Cos_norm (z : ℂ) :
    ‖Complex.cos z‖ ≤ Real.exp |z.im| := by
  have hp : ‖Complex.exp (z*Complex.I)‖ ≤ Real.exp |z.im| := by
    rw [Complex.norm_exp]
    apply Real.exp_le_exp.mpr
    simpa [Complex.mul_re] using neg_le_abs z.im
  have hn : ‖Complex.exp (-z*Complex.I)‖ ≤ Real.exp |z.im| := by
    rw [Complex.norm_exp]
    apply Real.exp_le_exp.mpr
    simpa [Complex.mul_re,Complex.neg_im] using le_abs_self z.im
  have h : 2*‖Complex.cos z‖ ≤ 2*Real.exp |z.im| := by
    calc
      _ = ‖(2:ℂ)*Complex.cos z‖ := by rw [norm_mul]; norm_num
      _ = ‖Complex.exp (z*Complex.I)+Complex.exp (-z*Complex.I)‖ := by rw [Complex.two_cos]
      _ ≤ _ := by linarith [norm_add_le (Complex.exp (z*Complex.I)) (Complex.exp (-z*Complex.I))]
  linarith

theorem neutralNF589Sinh_norm (z : ℂ) :
    ‖Complex.sinh z‖ ≤ Real.exp ‖z‖ := by
  have hp : ‖Complex.exp z‖ ≤ Real.exp ‖z‖ := by
    rw [Complex.norm_exp]
    exact Real.exp_le_exp.mpr ((le_abs_self _).trans (Complex.abs_re_le_norm _))
  have hn : ‖Complex.exp (-z)‖ ≤ Real.exp ‖z‖ := by
    rw [Complex.norm_exp,Complex.neg_re]
    exact Real.exp_le_exp.mpr ((neg_le_abs _).trans (Complex.abs_re_le_norm _))
  have h : 2*‖Complex.sinh z‖ ≤ 2*Real.exp ‖z‖ := by
    calc
      _ = ‖(2:ℂ)*Complex.sinh z‖ := by rw [norm_mul]; norm_num
      _ = ‖Complex.exp z-Complex.exp (-z)‖ := by rw [Complex.two_sinh]
      _ ≤ _ := by linarith [norm_sub_le (Complex.exp z) (Complex.exp (-z))]
  linarith

theorem neutralNF589NormalizedGeometry (w : ℂ) (hw : ‖w‖ ≤ 20) :
    ‖(11/10:ℂ)-w/500‖ ≤ 2 ∧ |((11/10:ℂ)-w/500).im| ≤ 1/25 := by
  have hdiv : ‖w/500‖ ≤ (1/25:ℝ) := by
    rw [norm_div,show ‖(500:ℂ)‖ = 500 by norm_num]
    linarith
  constructor
  · exact (norm_sub_le _ _).trans (by
      have h : ‖(11/10:ℂ)‖ = (11/10:ℝ) := by rw [norm_div]; norm_num
      rw [h]
      linarith)
  · have h : ((11/10:ℂ)-w/500).im = -(w/500).im := by
      simp [Complex.sub_im]
    rw [h,abs_neg]
    exact (Complex.abs_im_le_norm _).trans hdiv

theorem neutralNF589Oscillator_norm (x : ℂ) (f : ℝ) (k : ℕ)
    (hx : ‖x‖ ≤ 2) (hy : |x.im| ≤ 1/25)
    (hf : 0 ≤ f) (hf' : f ≤ 883) (hk : k ≤ 13) :
    ‖x^k*(if Even k then Complex.sin (2*(Real.pi:ℂ)*(f:ℂ)*x)
      else Complex.cos (2*(Real.pi:ℂ)*(f:ℂ)*x))‖ ≤ (2:ℝ)^13*3^283 := by
  let z := 2*(Real.pi:ℂ)*(f:ℂ)*x
  have hz : z.im = 2*Real.pi*f*x.im := by
    simp [z,Complex.mul_im,Complex.mul_re]
  have hzi : |z.im| ≤ 283 := by
    rw [hz,abs_mul,abs_of_nonneg (by positivity : 0 ≤ 2*Real.pi*f)]
    calc
      _ ≤ (2*Real.pi*f)*(1/25) := mul_le_mul_of_nonneg_left hy (by positivity)
      _ ≤ (2*4*883:ℝ)*(1/25) := by
        gcongr
        exact Real.pi_lt_four.le
      _ ≤ _ := by norm_num
  have hpow : ‖x^k‖ ≤ (2:ℝ)^13 := by
    rw [norm_pow]
    exact (pow_le_pow_left₀ (norm_nonneg _) hx _).trans (pow_le_pow_right₀ (by norm_num) hk)
  have htrig : ‖if Even k then Complex.sin z else Complex.cos z‖ ≤ (3:ℝ)^283 := by
    split_ifs
    · exact (neutralNF589Sin_norm z).trans (neutralNF589Exp_le_pow_three _ 283 hzi)
    · exact (neutralNF589Cos_norm z).trans (neutralNF589Exp_le_pow_three _ 283 hzi)
  rw [norm_mul]
  exact mul_le_mul hpow htrig (norm_nonneg _) (by positivity)

theorem neutralNF589Pole_norm (x : ℂ) (hx : ‖x‖ ≤ 2) :
    ‖Complex.sinh (x/2)‖ ≤ 3 := by
  apply (neutralNF589Sinh_norm _).trans
  apply (Real.exp_le_exp.mpr (show ‖x/2‖ ≤ 1 by
    rw [norm_div,show ‖(2:ℂ)‖ = 2 by norm_num]
    linarith)).trans
  exact Real.exp_one_lt_three.le

end
end WeilDefect
