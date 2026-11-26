import Mathlib

namespace WeilDefect
noncomputable section

/-- Five positive odd-power terms suffice for the needed logarithm lower bound. -/
theorem neutralIV106E1Log118 : (477067/100000:ℝ) ≤ Real.log 118 := by
  have h2 := Real.sum_range_le_log_div (x := (1/3:ℝ)) (by norm_num) (by norm_num) 5
  have hq := Real.sum_range_le_log_div (x := (27/91:ℝ)) (by norm_num) (by norm_num) 5
  norm_num [Finset.sum_range_succ] at h2 hq
  have he : Real.log (118:ℝ) = 6 * Real.log 2 + Real.log (59/32) := by
    rw [show (118:ℝ) = 2^6 * (59/32) by norm_num,
      Real.log_mul (by norm_num) (by norm_num), Real.log_pow]
    norm_num
  rw [he]
  linarith only [h2, hq]

/-- The actual constants leave a strict rational reserve above one. -/
theorem neutralIV106E1Budget :
    (5003/5000:ℝ) ≤ Real.log 118 + 1/2 -
      (118^2 * Real.pi^2/3 + 25/12)*(11/3325)^2 - 471031/125000 := by
  have hp : Real.pi ≤ (22/7:ℝ) := Real.pi_lt_d4.le.trans (by norm_num)
  have hp2 := pow_le_pow_left₀ Real.pi_pos.le hp 2
  have hl := neutralIV106E1Log118
  nlinarith only [hp2, hl]

/-- Arithmetic energy receiver. The Gamma, grouped prime and pole estimates
are hypotheses, not established by the scalar budget. -/
theorem neutralIV106E1Budget_receiver (M G P H Q : ℝ)
    (hM : 0 ≤ M)
    (hG : (Real.log 118 + 1/2 -
      (118^2 * Real.pi^2/3 + 25/12)*(11/3325)^2)*M ≤ G)
    (hP : P ≤ (471031/125000:ℝ)*M) (hH : 0 ≤ H)
    (hQ : Q = G-P+H) : (5003/5000:ℝ)*M ≤ Q := by
  have hb := mul_le_mul_of_nonneg_right neutralIV106E1Budget hM
  linarith only [hb,hG,hP,hH,hQ]

#print axioms neutralIV106E1Log118
#print axioms neutralIV106E1Budget
#print axioms neutralIV106E1Budget_receiver
end
end WeilDefect
