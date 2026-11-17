import Mathlib

namespace WeilDefect

/-! NF592: the historical fixedpoint parameters and their three
finite analytic remainder fees. No source-dependent input. -/

def neutralNF592Q : ℕ := 10^250

theorem neutralNF592Q_pos : 0 < neutralNF592Q := by
  unfold neutralNF592Q
  positivity

set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

theorem neutralNF592ExpFee_nat : 2*neutralNF592Q ≤ Nat.factorial 220 := by
  decide +kernel

theorem neutralNF592Atan5Fee_nat : neutralNF592Q ≤ 5^401*401 := by
  decide +kernel

theorem neutralNF592Atan239Fee_nat : neutralNF592Q ≤ 239^401*401 := by
  decide +kernel

theorem neutralNF592ExpFee :
    2/(Nat.factorial 220:ℝ) ≤ 1/(neutralNF592Q:ℝ) := by
  apply (div_le_div_iff₀ (by positivity : (0:ℝ)<Nat.factorial 220)
    (by exact_mod_cast neutralNF592Q_pos : (0:ℝ)<neutralNF592Q)).mpr
  have h : (2:ℝ)*(neutralNF592Q:ℝ) ≤ (Nat.factorial 220:ℝ) := by
    exact_mod_cast neutralNF592ExpFee_nat
  simpa only [one_mul] using h

theorem neutralNF592AtanFee (p : ℕ) (hp : 0 < p)
    (h : neutralNF592Q ≤ p^401*401) :
    (1/(p:ℝ))^401/401 ≤ 1/(neutralNF592Q:ℝ) := by
  have hp' : (0:ℝ)<p := by exact_mod_cast hp
  have hq : (0:ℝ)<neutralNF592Q := by exact_mod_cast neutralNF592Q_pos
  have hd : (0:ℝ)<(p:ℝ)^401*401 := by positivity
  rw [div_pow,one_pow,div_div]
  apply (one_div_le_one_div_of_le hq)
  exact_mod_cast h

theorem neutralNF592Atan5Fee :
    (1/5:ℝ)^(2*200+1)/(2*(200:ℝ)+1) ≤ 1/(neutralNF592Q:ℝ) := by
  norm_num only [show (2*200+1:ℕ)=401 by decide,show (2*(200:ℝ)+1)=401 by norm_num]
  exact neutralNF592AtanFee 5 (by decide) neutralNF592Atan5Fee_nat

theorem neutralNF592Atan239Fee :
    (1/239:ℝ)^(2*200+1)/(2*(200:ℝ)+1) ≤ 1/(neutralNF592Q:ℝ) := by
  norm_num only [show (2*200+1:ℕ)=401 by decide,show (2*(200:ℝ)+1)=401 by norm_num]
  exact neutralNF592AtanFee 239 (by decide) neutralNF592Atan239Fee_nat

end WeilDefect
