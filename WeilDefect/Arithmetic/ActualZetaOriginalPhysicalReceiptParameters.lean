import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointPhase

namespace WeilDefect

/-! NF616: a provisional high-precision reference configuration.
2600 decimal digits exceeds the nominal 8192-bit Arb precision.
These three fees concern ONLY transcendental truncation; they do
not certify the final physical residual payments. -/

def neutralNF616Q : ℕ := 10^2600
def neutralNF616ExpN : ℕ := 1200
def neutralNF616AtanN : ℕ := 2000

set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

theorem neutralNF616Q_pos : 0 < neutralNF616Q := by
  unfold neutralNF616Q
  positivity

theorem neutralNF616ExpFee_nat : 2*neutralNF616Q ≤ Nat.factorial neutralNF616ExpN := by
  decide +kernel

theorem neutralNF616Atan5Fee_nat : neutralNF616Q ≤ 5^4001*4001 := by
  decide +kernel

theorem neutralNF616Atan239Fee_nat : neutralNF616Q ≤ 239^4001*4001 := by
  decide +kernel

theorem neutralNF616ExpFee :
    2/(Nat.factorial neutralNF616ExpN:ℝ) ≤ 1/(neutralNF616Q:ℝ) := by
  apply (div_le_div_iff₀ (by positivity : (0:ℝ)<Nat.factorial neutralNF616ExpN)
    (by exact_mod_cast neutralNF616Q_pos : (0:ℝ)<neutralNF616Q)).mpr
  have h : (2:ℝ)*(neutralNF616Q:ℝ) ≤ (Nat.factorial neutralNF616ExpN:ℝ) := by
    exact_mod_cast neutralNF616ExpFee_nat
  simpa only [one_mul] using h

theorem neutralNF616AtanFee (p : ℕ) (hp : 0<p)
    (h : neutralNF616Q ≤ p^4001*4001) :
    (1/(p:ℝ))^4001/4001 ≤ 1/(neutralNF616Q:ℝ) := by
  have hp' : (0:ℝ)<p := by exact_mod_cast hp
  have hq : (0:ℝ)<neutralNF616Q := by exact_mod_cast neutralNF616Q_pos
  rw [div_pow,one_pow,div_div]
  apply one_div_le_one_div_of_le hq
  exact_mod_cast h

theorem neutralNF616Pi_sound :
    (neutralNF592PiBall neutralNF616Q neutralNF616AtanN).Contains Real.pi := by
  apply neutralNF592PiBall_sound _ _ neutralNF616Q_pos
  · change (1/5:ℝ)^(2*2000+1)/(2*(2000:ℝ)+1) ≤ _
    norm_num only [show (2*2000+1:ℕ)=4001 by decide,show (2*(2000:ℝ)+1)=4001 by norm_num]
    exact neutralNF616AtanFee 5 (by decide) neutralNF616Atan5Fee_nat
  · change (1/239:ℝ)^(2*2000+1)/(2*(2000:ℝ)+1) ≤ _
    norm_num only [show (2*2000+1:ℕ)=4001 by decide,show (2*(2000:ℝ)+1)=4001 by norm_num]
    exact neutralNF616AtanFee 239 (by decide) neutralNF616Atan239Fee_nat

end WeilDefect
