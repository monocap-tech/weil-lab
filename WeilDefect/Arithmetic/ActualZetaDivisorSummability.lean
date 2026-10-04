import WeilDefect.Arithmetic.ActualZetaLogGrowth
import Mathlib.Analysis.PSeries
import Mathlib.Topology.Algebra.InfiniteSum.Real

namespace WeilDefect
noncomputable section
open scoped BigOperators
set_option maxHeartbeats 800000

/-- Half-open absolute-height unit band, including every multiplicity copy.
Using the floor assigns each actual divisor coordinate to exactly one band. -/
def neutralActualZetaDivisorUnitBand (n : ℕ) : Set NeutralActualZetaDivisorCoordinate :=
  {q | ⌊|q.1.val.im|⌋₊ = n}

/-- A fixed polynomial tail weight on the actual multiplicity divisor. -/
def neutralActualZetaDivisorQuarticWeight (q : NeutralActualZetaDivisorCoordinate) : ℝ :=
  1 / (1 + |q.1.val.im|) ^ 4

theorem neutralActualZetaDivisorUnitBand_subset (n : ℕ) :
    neutralActualZetaDivisorUnitBand n ⊆
      neutralActualZetaDivisorHeightWindow ((n : ℝ) + 1) := by
  intro q hq
  have h := Nat.lt_floor_add_one |q.1.val.im|
  change ⌊|q.1.val.im|⌋₊ = n at hq
  rw [hq] at h
  exact h.le

theorem neutralActualZetaDivisorUnitBand_finite (n : ℕ) :
    (neutralActualZetaDivisorUnitBand n).Finite :=
  (neutralActualZetaDivisorHeightWindow_finite _).subset
    (neutralActualZetaDivisorUnitBand_subset n)

instance neutralActualZetaDivisorUnitBand_fintype (n : ℕ) :
    Fintype (neutralActualZetaDivisorUnitBand n) :=
  (neutralActualZetaDivisorUnitBand_finite n).fintype

theorem neutralActualZetaDivisorUnitBand_partition (q : NeutralActualZetaDivisorCoordinate) :
    ∃! n, q ∈ neutralActualZetaDivisorUnitBand n := by
  refine ⟨⌊|q.1.val.im|⌋₊, rfl, ?_⟩
  intro n hn
  exact hn.symm

/-- Coarse band control obtained from the certified cumulative count.
This does not assert the sharp local logarithmic density estimate. -/
theorem neutralActualZetaDivisorUnitBand_card_bound :
    ∃ A : ℝ, 0 < A ∧ ∀ n : ℕ,
      (Fintype.card (neutralActualZetaDivisorUnitBand n) : ℝ) ≤
        A * ((n : ℝ) + 1) ^ 2 := by
  obtain ⟨K, hK, hcount⟩ := neutralActualZetaDivisorHeightWindow_card_le_log_growth
  refine ⟨6 * K, by positivity, fun n => ?_⟩
  let f : neutralActualZetaDivisorUnitBand n →
      neutralActualZetaDivisorHeightWindow ((n : ℝ) + 1) :=
    fun q => ⟨q.val, neutralActualZetaDivisorUnitBand_subset n q.property⟩
  have hf : Function.Injective f := by
    intro q r h
    apply Subtype.ext
    exact congrArg
      (fun x : neutralActualZetaDivisorHeightWindow ((n : ℝ) + 1) => x.val) h
  have hcard : (Fintype.card (neutralActualZetaDivisorUnitBand n) : ℝ) ≤
      (Fintype.card (neutralActualZetaDivisorHeightWindow ((n : ℝ) + 1)) : ℝ) := by
    exact_mod_cast Fintype.card_le_of_injective f hf
  have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
  have hc := hcount ((n : ℝ) + 1)
  rw [abs_of_nonneg (by linarith : 0 ≤ (n : ℝ) + 1)] at hc
  simp only [show (n : ℝ) + 1 + 1 = (n : ℝ) + 2 by ring,
    show (n : ℝ) + 1 + 2 = (n : ℝ) + 3 by ring] at hc
  have hl : Real.log ((n : ℝ) + 3) ≤ (n : ℝ) + 3 :=
    Real.log_le_self (by positivity)
  have hm := mul_le_mul_of_nonneg_left hl
    (by positivity : 0 ≤ K * ((n : ℝ) + 2))
  have hp : ((n : ℝ) + 2) * ((n : ℝ) + 3) ≤ 6 * ((n : ℝ) + 1) ^ 2 := by
    nlinarith only [hn, sq_nonneg (n : ℝ)]
  have hpK := mul_le_mul_of_nonneg_left hp hK.le
  calc
    _ ≤ _ := hcard.trans hc
    _ ≤ K * ((n : ℝ) + 2) * ((n : ℝ) + 3) := hm
    _ ≤ (6 * K) * ((n : ℝ) + 1) ^ 2 := by
      nlinarith only [hpK]

theorem neutralActualZetaDivisorQuarticWeight_band_le (n : ℕ)
    (q : neutralActualZetaDivisorUnitBand n) :
    neutralActualZetaDivisorQuarticWeight q.val ≤ 1 / ((n : ℝ) + 1) ^ 4 := by
  have hfloor := Nat.floor_le (abs_nonneg q.val.1.val.im)
  have hq := q.property
  change ⌊|q.val.1.val.im|⌋₊ = n at hq
  rw [hq] at hfloor
  have hpow : ((n : ℝ) + 1) ^ 4 ≤ (1 + |q.val.1.val.im|) ^ 4 :=
    pow_le_pow_left₀ (by positivity) (by linarith only [hfloor]) _
  exact one_div_le_one_div_of_le (by positivity) hpow

/-- The actual divisor has an unconditional summable quartic height weight.
No arbitrary enumeration, sharp local count, RH, or operator domain is used. -/
theorem neutralActualZetaDivisorQuarticWeight_summable :
    Summable neutralActualZetaDivisorQuarticWeight := by
  obtain ⟨A, hA, hcard⟩ := neutralActualZetaDivisorUnitBand_card_bound
  have hbase : Summable (fun n : ℕ => 1 / ((n : ℝ) + 1) ^ 2) := by
    have h := (Real.summable_one_div_nat_pow (p := 2)).2 (by norm_num)
    have hi : Function.Injective (fun n : ℕ => n + 1) := by
      intro n m hnm
      change n + 1 = m + 1 at hnm
      exact Nat.add_right_cancel hnm
    simpa only [Function.comp_apply, Nat.cast_add, Nat.cast_one] using h.comp_injective hi
  have hband : ∀ n : ℕ,
      (∑' q : neutralActualZetaDivisorUnitBand n,
        neutralActualZetaDivisorQuarticWeight q.val) ≤ A * (1 / ((n : ℝ) + 1) ^ 2) := by
    intro n
    rw [tsum_fintype]
    calc
      _ ≤ ∑ _q : neutralActualZetaDivisorUnitBand n, 1 / ((n : ℝ) + 1) ^ 4 :=
        Finset.sum_le_sum (fun q _ => neutralActualZetaDivisorQuarticWeight_band_le n q)
      _ = (Fintype.card (neutralActualZetaDivisorUnitBand n) : ℝ) *
          (1 / ((n : ℝ) + 1) ^ 4) := by simp
      _ ≤ (A * ((n : ℝ) + 1) ^ 2) * (1 / ((n : ℝ) + 1) ^ 4) :=
        mul_le_mul_of_nonneg_right (hcard n) (by positivity)
      _ = _ := by
        have hn : (n : ℝ) + 1 ≠ 0 := by positivity
        field_simp
        <;> ring
  have hsum : Summable (fun n : ℕ =>
      ∑' q : neutralActualZetaDivisorUnitBand n,
        neutralActualZetaDivisorQuarticWeight q.val) :=
    Summable.of_nonneg_of_le (fun n => tsum_nonneg (fun q => by
      unfold neutralActualZetaDivisorQuarticWeight
      positivity)) hband (hbase.mul_left A)
  apply (summable_partition
    (f := neutralActualZetaDivisorQuarticWeight)
    (fun q => by unfold neutralActualZetaDivisorQuarticWeight; positivity)
    neutralActualZetaDivisorUnitBand_partition).2
  exact ⟨fun n => Summable.of_finite, hsum⟩

/-- Absolute convergence of complex actual-divisor samples with quartic
decay. The analytic sample-decay hypothesis is explicit and separate. -/
theorem neutralActualZetaDivisor_summable_of_quartic_bound
    (f : NeutralActualZetaDivisorCoordinate → ℂ) (M : ℝ)
    (hf : ∀ q, ‖f q‖ ≤ M * neutralActualZetaDivisorQuarticWeight q) :
    Summable f :=
  Summable.of_norm_bounded
    (neutralActualZetaDivisorQuarticWeight_summable.mul_left M) hf

end
end WeilDefect
