import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointPhase

namespace WeilDefect

/-! NF616: a provisional high-precision reference configuration.
2604 decimal digits exceeds the nominal 8192-bit Arb precision.
These three fees concern ONLY transcendental truncation; they do
not certify the final physical residual payments. -/

def nf618GuardQ : ℕ := 10^2604
def nf618GuardExpN : ℕ := 1200
def nf618GuardAtanN : ℕ := 2000

set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

theorem nf618GuardQ_pos : 0 < nf618GuardQ := by
  unfold nf618GuardQ
  positivity

theorem nf618GuardExpFee_nat : 2*nf618GuardQ ≤ Nat.factorial nf618GuardExpN := by
  decide +kernel

theorem nf618GuardAtan5Fee_nat : nf618GuardQ ≤ 5^4001*4001 := by
  decide +kernel

theorem nf618GuardAtan239Fee_nat : nf618GuardQ ≤ 239^4001*4001 := by
  decide +kernel

theorem nf618GuardExpFee :
    2/(Nat.factorial nf618GuardExpN:ℝ) ≤ 1/(nf618GuardQ:ℝ) := by
  apply (div_le_div_iff₀ (by positivity : (0:ℝ)<Nat.factorial nf618GuardExpN)
    (by exact_mod_cast nf618GuardQ_pos : (0:ℝ)<nf618GuardQ)).mpr
  have h : (2:ℝ)*(nf618GuardQ:ℝ) ≤ (Nat.factorial nf618GuardExpN:ℝ) := by
    exact_mod_cast nf618GuardExpFee_nat
  simpa only [one_mul] using h

theorem nf618GuardAtanFee (p : ℕ) (hp : 0<p)
    (h : nf618GuardQ ≤ p^4001*4001) :
    (1/(p:ℝ))^4001/4001 ≤ 1/(nf618GuardQ:ℝ) := by
  have hp' : (0:ℝ)<p := by exact_mod_cast hp
  have hq : (0:ℝ)<nf618GuardQ := by exact_mod_cast nf618GuardQ_pos
  rw [div_pow,one_pow,div_div]
  apply one_div_le_one_div_of_le hq
  exact_mod_cast h

theorem nf618GuardPi_sound :
    (neutralNF592PiBall nf618GuardQ nf618GuardAtanN).Contains Real.pi := by
  apply neutralNF592PiBall_sound _ _ nf618GuardQ_pos
  · change (1/5:ℝ)^(2*2000+1)/(2*(2000:ℝ)+1) ≤ _
    norm_num only [show (2*2000+1:ℕ)=4001 by decide,show (2*(2000:ℝ)+1)=4001 by norm_num]
    exact nf618GuardAtanFee 5 (by decide) nf618GuardAtan5Fee_nat
  · change (1/239:ℝ)^(2*2000+1)/(2*(2000:ℝ)+1) ≤ _
    norm_num only [show (2*2000+1:ℕ)=4001 by decide,show (2*(2000:ℝ)+1)=4001 by norm_num]
    exact nf618GuardAtanFee 239 (by decide) nf618GuardAtan239Fee_nat

end WeilDefect
