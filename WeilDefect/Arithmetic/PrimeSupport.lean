import Mathlib.Algebra.IsPrimePow
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Order.Filter.AtTopBot.Archimedean

namespace WeilDefect

/-- Prime powers active under the compact-window support inequality log n < 2c. -/
def activePrimePowers (c : ℝ) : Set ℕ :=
  {n | IsPrimePow n ∧ Real.log (n : ℝ) < 2 * c}

/--
WD-T34 arithmetic core: for every fixed real support radius, only finitely many
natural prime powers satisfy the strict compact-window inequality log n < 2c.
-/
theorem wd_t34_active_prime_powers_finite (c : ℝ) :
    (activePrimePowers c).Finite := by
  obtain ⟨N : ℕ, hN⟩ := exists_nat_gt (Real.exp (2 * c))
  refine (Set.finite_Iio N).subset ?_
  intro n hn
  rcases hn with ⟨hnpp, hnlog⟩
  have hnNat : 0 < n := lt_of_lt_of_le Nat.zero_lt_two hnpp.two_le
  have hnpos : 0 < (n : ℝ) := by exact_mod_cast hnNat
  have hnexp : (n : ℝ) < Real.exp (2 * c) :=
    (Real.log_lt_iff_lt_exp hnpos).mp hnlog
  have hnNreal : (n : ℝ) < (N : ℝ) := lt_trans hnexp hN
  exact_mod_cast hnNreal

end WeilDefect
