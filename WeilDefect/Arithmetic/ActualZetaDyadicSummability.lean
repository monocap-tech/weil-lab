import WeilDefect.Arithmetic.ActualZetaDivisorSummability
import Mathlib.Data.Nat.Log
import Mathlib.Analysis.SpecificLimits.Normed

namespace WeilDefect
noncomputable section
open scoped BigOperators
set_option maxHeartbeats 800000

/-- Dyadic bands partition the actual multiplicity divisor by log₂(floor(height)+1). -/
def neutralActualZetaDivisorDyadicBand (n : ℕ) : Set NeutralActualZetaDivisorCoordinate :=
  {q | Nat.log 2 (⌊|q.1.val.im|⌋₊ + 1) = n}

/-- The inverse-square height weight on every actual multiplicity copy. -/
def neutralActualZetaDivisorQuadraticWeight (q : NeutralActualZetaDivisorCoordinate) : ℝ :=
  1 / (1 + |q.1.val.im|) ^ 2

theorem neutralActualZetaDivisorDyadicBand_height (n : ℕ)
    (q : neutralActualZetaDivisorDyadicBand n) :
    (2 : ℝ) ^ n ≤ 1 + |q.val.1.val.im| ∧ |q.val.1.val.im| < (2 : ℝ) ^ (n + 1) := by
  have hq : Nat.log 2 (⌊|q.val.1.val.im|⌋₊ + 1) = n := q.property
  have hlo := Nat.pow_log_le_self 2 (Nat.succ_ne_zero ⌊|q.val.1.val.im|⌋₊)
  have hhi := Nat.lt_pow_succ_log_self (by norm_num : 1 < 2) (⌊|q.val.1.val.im|⌋₊ + 1)
  rw [hq] at hlo hhi
  have hlo' : (2 : ℝ) ^ n ≤ (⌊|q.val.1.val.im|⌋₊ : ℝ) + 1 := by exact_mod_cast hlo
  have hhi' : (⌊|q.val.1.val.im|⌋₊ : ℝ) + 1 < (2 : ℝ) ^ (n + 1) := by exact_mod_cast hhi
  constructor
  · have hf := Nat.floor_le (abs_nonneg q.val.1.val.im)
    linarith
  · exact (Nat.lt_floor_add_one |q.val.1.val.im|).trans hhi'

theorem neutralActualZetaDivisorDyadicBand_finite (n : ℕ) :
    (neutralActualZetaDivisorDyadicBand n).Finite := by
  apply (neutralActualZetaDivisorHeightWindow_finite ((2 : ℝ) ^ (n + 1))).subset
  intro q hq
  exact (neutralActualZetaDivisorDyadicBand_height n ⟨q, hq⟩).2.le

instance neutralActualZetaDivisorDyadicBand_fintype (n : ℕ) :
    Fintype (neutralActualZetaDivisorDyadicBand n) :=
  (neutralActualZetaDivisorDyadicBand_finite n).fintype

theorem neutralActualZetaDivisorDyadicBand_partition (q : NeutralActualZetaDivisorCoordinate) :
    ∃! n, q ∈ neutralActualZetaDivisorDyadicBand n := by
  refine ⟨Nat.log 2 (⌊|q.1.val.im|⌋₊ + 1), rfl, ?_⟩
  intro n hn
  exact hn.symm

/-- The actual cumulative logarithmic count yields an O((n+2)2ⁿ) dyadic count. -/
theorem neutralActualZetaDivisorDyadicBand_card_bound :
    ∃ A : ℝ, 0 < A ∧ ∀ n : ℕ,
      (Fintype.card (neutralActualZetaDivisorDyadicBand n) : ℝ) ≤
        A * ((n : ℝ) + 2) * (2 : ℝ) ^ n := by
  obtain ⟨K, hK, hcount⟩ := neutralActualZetaDivisorHeightWindow_card_le_log_growth
  refine ⟨6 * K, by positivity, fun n => ?_⟩
  let f : neutralActualZetaDivisorDyadicBand n →
      neutralActualZetaDivisorHeightWindow ((2 : ℝ) ^ (n + 1)) :=
    fun q => ⟨q.val, (neutralActualZetaDivisorDyadicBand_height n q).2.le⟩
  have hf : Function.Injective f := by
    intro q r h
    apply Subtype.ext
    exact congrArg (fun x : neutralActualZetaDivisorHeightWindow ((2 : ℝ) ^ (n + 1)) => x.val) h
  have hc : (Fintype.card (neutralActualZetaDivisorDyadicBand n) : ℝ) ≤
      K * ((2 : ℝ) ^ (n + 1) + 1) * Real.log ((2 : ℝ) ^ (n + 1) + 2) := by
    have hh := hcount ((2 : ℝ) ^ (n + 1))
    rw [abs_of_nonneg (by positivity)] at hh
    exact (by exact_mod_cast Fintype.card_le_of_injective f hf).trans hh
  have hd : 1 ≤ (2 : ℝ) ^ n := one_le_pow₀ (by norm_num)
  have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
  have hT : (2 : ℝ) ^ (n + 1) + 1 ≤ 3 * (2 : ℝ) ^ n := by
    rw [pow_succ]; linarith only [hd]
  have hl : Real.log ((2 : ℝ) ^ (n + 1) + 2) ≤ 2 * ((n : ℝ) + 2) := by
    have harg : (2 : ℝ) ^ (n + 1) + 2 ≤ (2 : ℝ) ^ (n + 2) := by
      rw [show n + 2 = (n + 1) + 1 by omega, pow_succ, pow_succ]
      linarith only [hd]
    have hm := Real.log_le_log (by positivity : 0 < (2 : ℝ) ^ (n + 1) + 2) harg
    rw [Real.log_pow, Nat.cast_add, Nat.cast_ofNat] at hm
    have hlog : Real.log 2 ≤ 2 := Real.log_le_self (by norm_num)
    have hh := mul_le_mul_of_nonneg_left hlog (by positivity : 0 ≤ (n : ℝ) + 2)
    nlinarith only [hm, hh]
  have hm := mul_le_mul hT hl (Real.log_nonneg (by
    have hp : 1 ≤ (2 : ℝ) ^ (n + 1) := one_le_pow₀ (by norm_num)
    linarith)) (by positivity : 0 ≤ 3 * (2 : ℝ) ^ n)
  have hk := mul_le_mul_of_nonneg_left hm hK.le
  calc
    _ ≤ _ := hc
    _ ≤ _ := by nlinarith only [hk]

theorem neutralActualZetaDivisorQuadraticWeight_band_le (n : ℕ)
    (q : neutralActualZetaDivisorDyadicBand n) :
    neutralActualZetaDivisorQuadraticWeight q.val ≤ 1 / ((2 : ℝ) ^ n) ^ 2 := by
  have hp := pow_le_pow_left₀ (by positivity : 0 ≤ (2 : ℝ) ^ n)
    (neutralActualZetaDivisorDyadicBand_height n q).1 2
  exact one_div_le_one_div_of_le (by positivity) hp

/-- Unconditional inverse-square summability from actual logarithmic growth,
without a sharp local unit-height count or an enumeration. -/
theorem neutralActualZetaDivisorQuadraticWeight_summable :
    Summable neutralActualZetaDivisorQuadraticWeight := by
  obtain ⟨A, hA, hcard⟩ := neutralActualZetaDivisorDyadicBand_card_bound
  have hr : ‖(1 / 2 : ℝ)‖ < 1 := by norm_num
  have hgeom := summable_geometric_of_norm_lt_one hr
  have hlin : Summable (fun n : ℕ => (n : ℝ) * (1 / 2 : ℝ) ^ n) := by
    simpa only [pow_one] using summable_pow_mul_geometric_of_norm_lt_one 1 hr
  have hbase : Summable (fun n : ℕ => ((n : ℝ) + 2) * (1 / 2 : ℝ) ^ n) := by
    simpa only [add_mul] using hlin.add (hgeom.mul_left 2)
  have hband : ∀ n : ℕ, (∑' q : neutralActualZetaDivisorDyadicBand n,
      neutralActualZetaDivisorQuadraticWeight q.val) ≤
        A * (((n : ℝ) + 2) * (1 / 2 : ℝ) ^ n) := by
    intro n
    rw [tsum_fintype]
    calc
      _ ≤ ∑ _q : neutralActualZetaDivisorDyadicBand n, 1 / ((2 : ℝ) ^ n) ^ 2 :=
        Finset.sum_le_sum (fun q _ => neutralActualZetaDivisorQuadraticWeight_band_le n q)
      _ = (Fintype.card (neutralActualZetaDivisorDyadicBand n) : ℝ) *
          (1 / ((2 : ℝ) ^ n) ^ 2) := by simp
      _ ≤ (A * ((n : ℝ) + 2) * (2 : ℝ) ^ n) * (1 / ((2 : ℝ) ^ n) ^ 2) :=
        mul_le_mul_of_nonneg_right (hcard n) (by positivity)
      _ = _ := by
        rw [← one_div_pow]
        have hp : (2 : ℝ) ^ n ≠ 0 := by positivity
        field_simp
        <;> ring
  have hs : Summable (fun n : ℕ => ∑' q : neutralActualZetaDivisorDyadicBand n,
      neutralActualZetaDivisorQuadraticWeight q.val) :=
    Summable.of_nonneg_of_le (fun n => tsum_nonneg (fun q => by
      unfold neutralActualZetaDivisorQuadraticWeight; positivity)) hband (hbase.mul_left A)
  apply (summable_partition (f := neutralActualZetaDivisorQuadraticWeight)
    (fun q => by unfold neutralActualZetaDivisorQuadraticWeight; positivity)
    neutralActualZetaDivisorDyadicBand_partition).2
  exact ⟨fun n => Summable.of_finite, hs⟩

end
end WeilDefect
