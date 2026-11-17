import Mathlib

namespace WeilDefect

/-! NF594: two source-independent exact integer inequalities pay
the stronger circle majorant and the high-degree cutoff.
These are small kernel decisions, not external arithmetic axioms. -/

set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

theorem neutralNF594Disc285_nat :
    (400:ℕ)*10^143*2^13*3^283 ≤ 10^285 := by
  decide +kernel

theorem neutralNF594HighDegree_nat : (10:ℕ)^325 ≤ 20^250 := by
  decide +kernel

theorem neutralNF594Disc285_real :
    (400:ℝ)*10^143*2^13*3^283 ≤ 10^285 := by
  exact_mod_cast neutralNF594Disc285_nat

theorem neutralNF594HighDegree_base :
    (10:ℝ)^285*(1/20:ℝ)^250 ≤ 1/(10:ℝ)^40 := by
  have h : (10:ℝ)^325 ≤ (20:ℝ)^250 := by
    exact_mod_cast neutralNF594HighDegree_nat
  rw [div_pow,one_pow,← div_eq_mul_inv, mul_one]
  apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
  rw [one_mul,← pow_add]
  exact h

theorem neutralNF594HighDegree (n : ℕ) (hn : 250 ≤ n) :
    (10:ℝ)^285*(1/20:ℝ)^n ≤ 1/(10:ℝ)^40 := by
  have he : n = 250+(n-250) := by omega
  have hp : (1/20:ℝ)^(n-250) ≤ 1 :=
    pow_le_one₀ (by norm_num) (by norm_num)
  calc
    (10:ℝ)^285*(1/20:ℝ)^n =
        ((10:ℝ)^285*(1/20:ℝ)^250)*(1/20:ℝ)^(n-250) := by
      conv_lhs => rw [he,pow_add]
      ring
    _ ≤ ((10:ℝ)^285*(1/20:ℝ)^250)*1 :=
      mul_le_mul_of_nonneg_left hp (by positivity)
    _ ≤ _ := by rw [mul_one]; exact neutralNF594HighDegree_base

end WeilDefect
