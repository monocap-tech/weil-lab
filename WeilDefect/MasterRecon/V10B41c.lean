import WeilDefect.MasterRecon.V10B41b
import Mathlib.Algebra.Polynomial.AlgebraMap

/-! V10B41c: literal centered Taylor polynomial attachment by coefficient
comparison. This proof is finite and independent of the beta recurrence. -/
namespace WeilDefect.MasterRecon.V10B41c
open Polynomial
open scoped BigOperators
open WeilDefect.MasterRecon.V10B41a
open WeilDefect.MasterRecon.V10B41b

def fullCoeff (k : ℕ) : ℚ :=
  ∑ r ∈ Finset.range 64,
    ((2:ℚ)^r/((8:ℚ)^r*(r.factorial:ℚ)))*
      ((-1/2:ℚ)^(r-k)*(r.choose k:ℚ))

noncomputable def TQ : ℚ[X] :=
  ∑ r ∈ Finset.range 64,
    C ((2:ℚ)^r/((8:ℚ)^r*(r.factorial:ℚ)))*(X+C (-1/2:ℚ))^r

theorem TQ_coeff (k : ℕ) : TQ.coeff k = fullCoeff k := by
  unfold TQ fullCoeff
  rw [Polynomial.finsetSum_coeff]
  apply Finset.sum_congr rfl
  intro r _
  rw [Polynomial.coeff_C_mul,Polynomial.coeff_X_add_C_pow]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem fullCoeff_check (k : Fin 64) :
    (t k:ℚ) = (scale:ℚ)*fullCoeff k := by
  fin_cases k <;> norm_num [t, tBank, scale, fullCoeff, Finset.sum_range_succ, Nat.factorial, Nat.choose]

theorem fullCoeff_high_zero (k : ℕ) (hk : 64 ≤ k) :
    fullCoeff k = 0 := by
  unfold fullCoeff
  apply Finset.sum_eq_zero
  intro r hr
  have hrk : r < k := (Finset.mem_range.mp hr).trans_le hk
  simp [Nat.choose_eq_zero_of_lt hrk]

theorem scaled_Taylor_identity :
    TP.map (Int.castRingHom ℚ) = C (scale:ℚ)*TQ := by
  ext k
  rw [Polynomial.coeff_map,Polynomial.coeff_C_mul,TQ_coeff,TP_coeff]
  by_cases hk : k<64
  · rw [if_pos hk]
    exact fullCoeff_check ⟨k,hk⟩
  · rw [if_neg hk,fullCoeff_high_zero k (by omega)]
    simp

theorem TQ_eval (x : ℝ) :
    aeval x TQ =
      ∑ r ∈ Finset.range 64, ((2*x-1)/8)^r/(r.factorial:ℝ) := by
  unfold TQ
  simp only [map_sum,map_mul,map_pow,map_add,aeval_C,aeval_X]
  apply Finset.sum_congr rfl
  intro r _
  simp only [map_div₀, map_pow, map_mul, map_natCast, map_ofNat, map_neg]
  change ((2:ℝ)^r/((8:ℝ)^r*(r.factorial:ℝ)))*(x+(-1/2:ℝ))^r = _
  rw [show (2*x-1)/8=(2/8:ℝ)*(x+(-1/2)) by ring,mul_pow,div_pow]
  ring

end WeilDefect.MasterRecon.V10B41c

#print axioms WeilDefect.MasterRecon.V10B41c.TQ_coeff
#print axioms WeilDefect.MasterRecon.V10B41c.fullCoeff_check
#print axioms WeilDefect.MasterRecon.V10B41c.fullCoeff_high_zero
#print axioms WeilDefect.MasterRecon.V10B41c.scaled_Taylor_identity
#print axioms WeilDefect.MasterRecon.V10B41c.TQ_eval
