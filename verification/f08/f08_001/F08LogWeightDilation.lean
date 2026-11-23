import WeilDefect.Arithmetic.LogarithmicForm

namespace WeilDefect
noncomputable section

/-- Original logarithmic Fourier weight under inward physical dilation.
This scalar bound is not a form-core density or Weil positivity theorem. -/
theorem f08_logarithmicFourierWeight_dilation_le
    (lam xi : ℝ) (hlo : (1 / 2 : ℝ) ≤ lam) (hhi : lam ≤ 1) :
    logarithmicFourierWeight (xi / lam) ≤
      logarithmicFourierWeight xi + Real.log 2 := by
  have hpos : 0 < lam := by linarith
  have hinv : (1 : ℝ) / lam ≤ 2 := by
    apply (div_le_iff₀ hpos).2
    linarith
  have hscale : |xi| / lam ≤ 2 * |xi| := by
    calc
      |xi| / lam = |xi| * ((1 : ℝ) / lam) := by simp [div_eq_mul_inv]
      _ ≤ |xi| * 2 := mul_le_mul_of_nonneg_left hinv (abs_nonneg xi)
      _ = 2 * |xi| := by ring
  have he : 0 < Real.exp (1 : ℝ) := Real.exp_pos _
  have hbase : 0 < Real.exp (1 : ℝ) + |xi| :=
    add_pos_of_pos_of_nonneg he (abs_nonneg xi)
  have hbound : Real.exp (1 : ℝ) + |xi / lam| ≤
      2 * (Real.exp (1 : ℝ) + |xi|) := by
    rw [abs_div, abs_of_pos hpos]
    linarith
  have hlog : Real.log (Real.exp (1 : ℝ) + |xi / lam|) ≤
      Real.log (2 * (Real.exp (1 : ℝ) + |xi|)) :=
    Real.log_le_log (by positivity) hbound
  unfold logarithmicFourierWeight
  rw [Real.log_mul (by norm_num : (2 : ℝ) ≠ 0) (ne_of_gt hbase)] at hlog
  linarith

/-- A uniform multiplier for λ in [1/2,1], in the exact source weight. -/
theorem f08_logarithmicFourierWeight_dilation_uniform
    (lam xi : ℝ) (hlo : (1 / 2 : ℝ) ≤ lam) (hhi : lam ≤ 1) :
    logarithmicFourierWeight (xi / lam) ≤
      (1 + Real.log 2) * logarithmicFourierWeight xi := by
  have h := f08_logarithmicFourierWeight_dilation_le lam xi hlo hhi
  have hw := one_le_logarithmicFourierWeight xi
  have hlog : 0 ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  have hmul : 0 ≤ Real.log 2 * (logarithmicFourierWeight xi - 1) :=
    mul_nonneg hlog (sub_nonneg.mpr hw)
  nlinarith

#print axioms f08_logarithmicFourierWeight_dilation_le
#print axioms f08_logarithmicFourierWeight_dilation_uniform

end
end WeilDefect
