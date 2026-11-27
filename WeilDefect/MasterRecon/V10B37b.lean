import WeilDefect.MasterRecon.V10B33a
import Mathlib.Data.Nat.Choose.Sum

/-! V10B37b: an economical uniform envelope for the shifted Legendre
basis. The sharp bound 1 is not needed for the frozen geometric reserve. -/
namespace WeilDefect.MasterRecon.V10B37b
open Polynomial
open scoped BigOperators
open WeilDefect.MasterRecon.V10B33a

theorem choose_bound (n k : ℕ) : (n.choose k:ℝ) ≤ (2:ℝ)^n := by
  by_cases hk : k ≤ n
  · have h : n.choose k ≤ ∑ i ∈ Finset.range (n+1), n.choose i :=
      Finset.single_le_sum (f := fun i => n.choose i)
        (fun i _ => Nat.zero_le _) (Finset.mem_range.mpr (by omega))
    rw [Nat.sum_range_choose] at h
    exact_mod_cast h
  · rw [Nat.choose_eq_zero_of_lt (by omega)]
    norm_num

theorem legendre_half_bound (j : ℕ) (z : ℝ) (hz : 0 ≤ z) (hz' : z ≤ 1/2) :
    |legendre j z| ≤ (4:ℝ)^j := by
  unfold legendre shiftedLegendre
  simp only [map_sum,map_mul,map_pow,aeval_C,aeval_X,algebraMap_int_eq,Int.cast_mul,Int.cast_pow,
    Int.cast_neg,Int.cast_one,Int.cast_natCast,abs_mul,abs_pow,abs_neg,abs_one,one_pow,one_mul]
  change |∑ k ∈ Finset.range (j+1), (-1:ℝ)^k*(j.choose k:ℝ)*((j+k).choose j:ℝ)*z^k| ≤ (4:ℝ)^j
  calc
    _ ≤ ∑ k ∈ Finset.range (j+1),
        |(-1:ℝ)^k*(j.choose k:ℝ)*((j+k).choose j:ℝ)*z^k| := by
      simpa only [Real.norm_eq_abs] using
        (norm_sum_le (Finset.range (j+1))
          (fun k => (-1:ℝ)^k*(j.choose k:ℝ)*((j+k).choose j:ℝ)*z^k))
    _ ≤ ∑ k ∈ Finset.range (j+1), (2:ℝ)^j*(j.choose k:ℝ) := by
      apply Finset.sum_le_sum
      intro k _
      simp only [abs_mul,abs_pow,abs_neg,abs_one,one_pow,one_mul,
        abs_of_nonneg (show (0:ℝ) ≤ (j.choose k:ℝ) by positivity),
        abs_of_nonneg (show (0:ℝ) ≤ ((j+k).choose j:ℝ) by positivity),abs_of_nonneg hz]
      have h₁ := choose_bound (j+k) j
      have h₂ : (2*z)^k ≤ 1 := by
        simpa using pow_le_pow_left₀ (show 0 ≤ 2*z by positivity)
          (show 2*z ≤ 1 by linarith) k
      calc
        _ ≤ (j.choose k:ℝ)*(2:ℝ)^(j+k)*z^k :=
          mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left h₁ (by positivity))
            (by positivity)
        _ = ((2:ℝ)^j*(j.choose k:ℝ))*(2*z)^k := by rw [pow_add,mul_pow]; ring
        _ ≤ _ := mul_le_of_le_one_right (by positivity) h₂
    _ = _ := by
      rw [← Finset.mul_sum]
      have h : (∑ k ∈ Finset.range (j+1), (j.choose k:ℝ)) = (2:ℝ)^j := by
        exact_mod_cast Nat.sum_range_choose j
      rw [h,← mul_pow]
      norm_num

theorem legendre_uniform_envelope (j : ℕ) (z : ℝ) (hz : z ∈ Set.Icc (0:ℝ) 1) :
    |legendre j z| ≤ (4:ℝ)^j := by
  by_cases h : z ≤ 1/2
  · exact legendre_half_bound j z hz.1 h
  · have he : |legendre j (1-z)| = |legendre j z| := by
      rw [legendre_reflect,abs_mul,abs_pow,abs_neg,abs_one,one_pow,one_mul]
    rw [← he]
    exact legendre_half_bound j (1-z) (by linarith [hz.2]) (by linarith)

theorem weighted_outer_reserve :
    (4:ℝ)^35*(1/65000:ℝ)^10/(1-16/65000) < 1/(10:ℝ)^27 := by norm_num

end WeilDefect.MasterRecon.V10B37b

#print axioms WeilDefect.MasterRecon.V10B37b.choose_bound
#print axioms WeilDefect.MasterRecon.V10B37b.legendre_half_bound
#print axioms WeilDefect.MasterRecon.V10B37b.legendre_uniform_envelope
#print axioms WeilDefect.MasterRecon.V10B37b.weighted_outer_reserve
