import WeilDefect.Arithmetic.ActualZetaDyadicSummability
import Mathlib.Analysis.SpecificLimits.Normed

namespace WeilDefect
noncomputable section

/-!
NF574. The NF524/NF528 ORIGINAL endpoint-log transform has
logarithmic-over-linear decay, not the quartic decay of a smooth
test. This is the actual requisite slower squared envelope, on
the genuine multiplicity divisor. No new zero count assumption.
-/

def neutralNF574LogDyadicIndex (q : NeutralActualZetaDivisorCoordinate) : ℕ :=
  Nat.log 2 (⌊|q.1.val.im|⌋₊ + 1)

def neutralNF574LogDyadicWeight (q : NeutralActualZetaDivisorCoordinate) : ℝ :=
  ((neutralNF574LogDyadicIndex q : ℝ) + 2)^2 *
    (1 / 4 : ℝ) ^ neutralNF574LogDyadicIndex q

theorem neutralNF574LogDyadicWeight_nonneg (q : NeutralActualZetaDivisorCoordinate) :
    0 ≤ neutralNF574LogDyadicWeight q := by
  unfold neutralNF574LogDyadicWeight
  positivity

theorem neutralNF574LogDyadicWeight_onBand (n : ℕ)
    (q : neutralActualZetaDivisorDyadicBand n) :
    neutralNF574LogDyadicWeight q.val = ((n : ℝ) + 2)^2 * (1 / 4 : ℝ)^n := by
  have hn : neutralNF574LogDyadicIndex q.val = n := q.property
  simp only [neutralNF574LogDyadicWeight, hn]

/-- Exact real geometric-cubic majorant for the original log decay. -/
theorem neutralNF574CubicGeometric_summable :
    Summable (fun n : ℕ => ((n : ℝ) + 2)^3 * (1 / 2 : ℝ)^n) := by
  have hr : ‖(1 / 2 : ℝ)‖ < 1 := by norm_num
  have h0 := summable_geometric_of_norm_lt_one hr
  have h1 : Summable (fun n : ℕ => (n : ℝ) * (1 / 2 : ℝ)^n) := by
    simpa only [pow_one] using summable_pow_mul_geometric_of_norm_lt_one 1 hr
  have h2 : Summable (fun n : ℕ => (n : ℝ)^2 * (1 / 2 : ℝ)^n) :=
    summable_pow_mul_geometric_of_norm_lt_one 2 hr
  have h3 : Summable (fun n : ℕ => (n : ℝ)^3 * (1 / 2 : ℝ)^n) :=
    summable_pow_mul_geometric_of_norm_lt_one 3 hr
  apply (((h3.add (h2.mul_left 6)).add (h1.mul_left 12)).add
    (h0.mul_left 8)).congr
  intro n
  ring

/-- Both multiplicity and the logarithmic loss are paid, with no
finite-height cutoff: the original squared dyadic majorant is ℓ¹. -/
theorem neutralNF574LogDyadicWeight_summable :
    Summable neutralNF574LogDyadicWeight := by
  obtain ⟨A, hA, hcount⟩ := neutralActualZetaDivisorDyadicBand_card_bound
  have hband (n : ℕ) :
      (∑' q : neutralActualZetaDivisorDyadicBand n,
        neutralNF574LogDyadicWeight q.val) ≤
      A * (((n : ℝ) + 2)^3 * (1 / 2 : ℝ)^n) := by
    rw [tsum_fintype]
    simp only [neutralNF574LogDyadicWeight_onBand, Finset.sum_const,
      Finset.card_univ, nsmul_eq_mul]
    calc
      _ ≤ (A * ((n : ℝ) + 2) * (2 : ℝ)^n) *
          (((n : ℝ) + 2)^2 * (1 / 4 : ℝ)^n) :=
        mul_le_mul_of_nonneg_right (hcount n) (by positivity)
      _ = _ := by
        have hpow : (2 : ℝ)^n * (1 / 4 : ℝ)^n = (1 / 2 : ℝ)^n := by
          rw [← mul_pow]
          norm_num
        calc
          _ = A * ((n : ℝ) + 2)^3 * ((2 : ℝ)^n * (1 / 4 : ℝ)^n) := by ring
          _ = _ := by rw [hpow]; ring
  have hs : Summable (fun n : ℕ => ∑' q : neutralActualZetaDivisorDyadicBand n,
      neutralNF574LogDyadicWeight q.val) :=
    Summable.of_nonneg_of_le
      (fun n => tsum_nonneg (fun q => neutralNF574LogDyadicWeight_nonneg q.val))
      hband (neutralNF574CubicGeometric_summable.mul_left A)
  apply (summable_partition (f := neutralNF574LogDyadicWeight)
    neutralNF574LogDyadicWeight_nonneg neutralActualZetaDivisorDyadicBand_partition).2
  exact ⟨fun _ => Summable.of_finite, hs⟩

/-- The genuine endpoint logarithmic-over-linear envelope is dominated
on each actual divisor band by the summable dyadic envelope. -/
theorem neutralNF574LogStripEnvelope_sq_le (q : NeutralActualZetaDivisorCoordinate) :
    ((1 + Real.log (2 + |q.1.val.im|)) / (1 + |q.1.val.im|))^2 ≤
      4 * neutralNF574LogDyadicWeight q := by
  let n := neutralNF574LogDyadicIndex q
  have hq : q ∈ neutralActualZetaDivisorDyadicBand n := rfl
  obtain ⟨hlo, hhi⟩ := neutralActualZetaDivisorDyadicBand_height n ⟨q, hq⟩
  have h2n : 1 ≤ (2 : ℝ)^(n+1) := one_le_pow₀ (by norm_num)
  have harg : 2 + |q.1.val.im| ≤ (2 : ℝ)^(n+3) := by
    rw [show n+3 = (n+1)+2 by omega, pow_add]
    norm_num
    linarith
  have hlog := Real.log_le_log (by positivity : 0 < 2 + |q.1.val.im|) harg
  rw [Real.log_pow, Nat.cast_add, Nat.cast_ofNat] at hlog
  have hlog2 : Real.log 2 ≤ 1 := by
    have he : (2 : ℝ) ≤ Real.exp 1 := by
      linarith [Real.add_one_le_exp (1 : ℝ)]
    simpa only [Real.log_exp] using Real.log_le_log (by norm_num : (0:ℝ)<2) he
  have hmul := mul_le_mul_of_nonneg_left hlog2 (by positivity : 0 ≤ (n:ℝ)+3)
  have hnum : 1 + Real.log (2 + |q.1.val.im|) ≤ 2 * ((n:ℝ)+2) := by
    nlinarith only [hlog, hmul, Nat.cast_nonneg (α := ℝ) n]
  have hnum0 : 0 ≤ 1 + Real.log (2 + |q.1.val.im|) := by
    have : 0 ≤ Real.log (2 + |q.1.val.im|) := Real.log_nonneg (by positivity)
    linarith
  have hratio :
      (1 + Real.log (2 + |q.1.val.im|)) / (1 + |q.1.val.im|) ≤
      2 * ((n:ℝ)+2) / (2:ℝ)^n := by
    exact (div_le_div_of_nonneg_right hnum (by positivity)).trans
      (div_le_div_of_nonneg_left (by positivity) (by positivity) hlo)
  have hs := pow_le_pow_left₀ (div_nonneg hnum0 (by positivity)) hratio 2
  calc
    _ ≤ (2 * ((n:ℝ)+2) / (2:ℝ)^n)^2 := hs
    _ = 4 * neutralNF574LogDyadicWeight q := by
      rw [neutralNF574LogDyadicWeight_onBand n ⟨q,hq⟩]
      have hden : ((2 : ℝ)^n)^2 = (4 : ℝ)^n := by
        rw [← pow_mul, Nat.mul_comm n 2, pow_mul]
        norm_num
      have hinv : (1 / 4 : ℝ)^n = 1 / (4 : ℝ)^n := by
        rw [div_pow, one_pow]
      rw [div_pow, hden, hinv]
      ring

end
end WeilDefect
