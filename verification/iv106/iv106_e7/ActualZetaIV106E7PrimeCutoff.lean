import WeilDefect.Arithmetic.ActualZetaIV106E4PrimeCoefficients
import WeilDefect.Morphology.NeutralWeilMultiplier
import WeilDefect.Arithmetic.ActualZetaIV103OriginalSchwartzSpectralAttachment
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open scoped BigOperators SchwartzMap

/-- The exact threshold lies strictly between the ninth and tenth integers. -/
theorem neutralIV106E7Cutoff_log :
    Real.log 9 < (11/5:ℝ) ∧ (11/5:ℝ) < Real.log 10 := by
  obtain ⟨h2,h3,h5,h7⟩ := neutralIV106E4Log_upper
  have h9 : Real.log 9 = 2*Real.log 3 := by
    rw [show (9:ℝ) = 3^2 by norm_num, Real.log_pow]
    norm_num
  have hl2 := Real.sum_range_le_log_div (x := (1/3:ℝ)) (by norm_num) (by norm_num) 1
  have hlq := Real.sum_range_le_log_div (x := (1/9:ℝ)) (by norm_num) (by norm_num) 1
  norm_num [Finset.sum_range_succ] at hl2 hlq
  have h10 : Real.log 10 = 3*Real.log 2 + Real.log (5/4) := by
    calc
      Real.log 10 = Real.log ((2:ℝ)^3*(5/4)) := by norm_num
      _ = Real.log ((2:ℝ)^3) + Real.log (5/4) := Real.log_mul (by norm_num) (by norm_num)
      _ = _ := by rw [Real.log_pow]; norm_num
  constructor
  · linarith only [h3,h9]
  · linarith only [hl2,hlq,h10]

/-- No threshold prime power is omitted. This is the literal source finset. -/
theorem neutralIV106E7Inventory :
    rightLimitPrimePowerFinset (11/10:ℝ) = ({2,3,4,5,7,8,9}:Finset ℕ) := by
  classical
  obtain ⟨h9,h10⟩ := neutralIV106E7Cutoff_log
  ext n
  rw [mem_rightLimitPrimePowerFinset]
  constructor
  · rintro ⟨hp,hl⟩
    have hn : n < 10 := by
      by_contra h
      have he : Real.log 10 ≤ Real.log (n:ℝ) :=
        Real.log_le_log (by norm_num) (by exact_mod_cast (Nat.le_of_not_lt h))
      linarith
    have hn2 := hp.two_le
    interval_cases n <;> first | decide | exact False.elim ((by decide : ¬ IsPrimePow (6:ℕ)) hp)
  · intro hn
    have hmem : n = 2 ∨ n = 3 ∨ n = 4 ∨ n = 5 ∨ n = 7 ∨ n = 8 ∨ n = 9 := by
      simpa only [Finset.mem_insert, Finset.mem_singleton] using hn
    have hp : IsPrimePow n := by
      rcases hmem with h|h|h|h|h|h|h <;> subst n
      · exact (by decide : Nat.Prime 2).isPrimePow
      · exact (by decide : Nat.Prime 3).isPrimePow
      · exact (isPrimePow_nat_iff 4).2 ⟨2,2,by decide,by decide,by decide⟩
      · exact (by decide : Nat.Prime 5).isPrimePow
      · exact (by decide : Nat.Prime 7).isPrimePow
      · exact (isPrimePow_nat_iff 8).2 ⟨2,3,by decide,by decide,by decide⟩
      · exact (isPrimePow_nat_iff 9).2 ⟨3,2,by decide,by decide,by decide⟩
    have hn9 : n ≤ 9 := by
      rcases hmem with h|h|h|h|h|h|h <;> omega
    have hle := Real.log_le_log (show (0:ℝ) < n by exact_mod_cast hp.pos)
      (show (n:ℝ) ≤ 9 by exact_mod_cast hn9)
    exact ⟨hp, by linarith⟩

/-- Exact source von Mangoldt values, not approximations to the log. -/
theorem neutralIV106E7Mangoldt :
    ArithmeticFunction.vonMangoldt 2 = Real.log 2 ∧
    ArithmeticFunction.vonMangoldt 3 = Real.log 3 ∧
    ArithmeticFunction.vonMangoldt 4 = Real.log 2 ∧
    ArithmeticFunction.vonMangoldt 5 = Real.log 5 ∧
    ArithmeticFunction.vonMangoldt 7 = Real.log 7 ∧
    ArithmeticFunction.vonMangoldt 8 = Real.log 2 ∧
    ArithmeticFunction.vonMangoldt 9 = Real.log 3 := by
  refine ⟨?_,?_,?_,?_,?_,?_,?_⟩
  · exact ArithmeticFunction.vonMangoldt_apply_prime (by decide : Nat.Prime 2)
  · exact ArithmeticFunction.vonMangoldt_apply_prime (by decide : Nat.Prime 3)
  · rw [show (4:ℕ)=2^2 by decide, ArithmeticFunction.vonMangoldt_apply_pow (by decide),
      ArithmeticFunction.vonMangoldt_apply_prime (by decide : Nat.Prime 2)]
    norm_num
  · exact ArithmeticFunction.vonMangoldt_apply_prime (by decide : Nat.Prime 5)
  · exact ArithmeticFunction.vonMangoldt_apply_prime (by decide : Nat.Prime 7)
  · rw [show (8:ℕ)=2^3 by decide, ArithmeticFunction.vonMangoldt_apply_pow (by decide),
      ArithmeticFunction.vonMangoldt_apply_prime (by decide : Nat.Prime 2)]
    norm_num
  · rw [show (9:ℕ)=3^2 by decide, ArithmeticFunction.vonMangoldt_apply_pow (by decide),
      ArithmeticFunction.vonMangoldt_apply_prime (by decide : Nat.Prime 3)]
    norm_num

/-- Literal lag identities for the repeated primes. -/
theorem neutralIV106E7Lags :
    Real.log 4 = 2*Real.log 2 ∧
    Real.log 8 = 3*Real.log 2 ∧
    Real.log 9 = 2*Real.log 3 := by
  refine ⟨?_,?_,?_⟩
  · rw [show (4:ℝ)=2^2 by norm_num, Real.log_pow]; norm_num
  · rw [show (8:ℝ)=2^3 by norm_num, Real.log_pow]; norm_num
  · rw [show (9:ℝ)=3^2 by norm_num, Real.log_pow]; norm_num

/-- The fixed physical window fits the four padded chain lengths. -/
theorem neutralIV106E7Cover :
    (11/5:ℝ) ≤ 4*Real.log 2 ∧
    (11/5:ℝ) ≤ 3*Real.log 3 ∧
    (11/5:ℝ) ≤ 2*Real.log 5 ∧
    (11/5:ℝ) ≤ 2*Real.log 7 := by
  have h2 := Real.sum_range_le_log_div (x := (1/3:ℝ)) (by norm_num) (by norm_num) 1
  have h3 := Real.sum_range_le_log_div (x := (1/2:ℝ)) (by norm_num) (by norm_num) 1
  have h5 := Real.log_le_log (by norm_num : (0:ℝ) < 4) (by norm_num : (4:ℝ) ≤ 5)
  have h7 := Real.log_le_log (by norm_num : (0:ℝ) < 4) (by norm_num : (4:ℝ) ≤ 7)
  have h4 := neutralIV106E7Lags.1
  norm_num [Finset.sum_range_succ] at h2 h3
  exact ⟨by linarith only [h2],by linarith only [h3],
    by linarith only [h2,h4,h5],by linarith only [h2,h4,h7]⟩

/-- Expand the original IV103 prime sum, with precisely its source inventory. -/
theorem neutralIV106E7Original_sum (v : 𝓢(ℝ,ℂ)) :
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) n) =
    neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) 2 +
    neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) 3 +
    neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) 4 +
    neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) 5 +
    neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) 7 +
    neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) 8 +
    neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) 9 := by
  rw [neutralIV103Prime_finite, neutralIV106E7Inventory]
  simp [Finset.sum_insert]
  <;> ring

#print axioms neutralIV106E7Cutoff_log
#print axioms neutralIV106E7Inventory
#print axioms neutralIV106E7Mangoldt
#print axioms neutralIV106E7Lags
#print axioms neutralIV106E7Cover
#print axioms neutralIV106E7Original_sum
end
end WeilDefect
