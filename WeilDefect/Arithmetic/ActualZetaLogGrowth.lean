import WeilDefect.Arithmetic.ActualZetaFactorialEnvelope
import Mathlib.Data.Nat.Factorial.Basic

namespace WeilDefect
noncomputable section

/-- Scalar logarithmic conversion of the certified factorial majorant.
The constants depend only on the positive theta-kernel constants. -/
theorem neutralActualZetaFactorialMajorant_log_bound
    {p C : ℝ} (hp : 0 < p) (hC : 0 < C) :
    ∃ K : ℝ, 0 < K ∧ ∀ n : ℕ,
      Real.log (neutralActualZetaFactorialMajorant p C n) ≤
        K * ((n : ℝ) + 1) * Real.log ((n : ℝ) + 2) := by
  let q : ℝ := p / 2
  let B : ℝ := max 1 (C * (Real.exp (-q) / q))
  let b : ℝ := max 1 (1 / q)
  have hq : 0 < q := by dsimp [q]; positivity
  have hB : 1 ≤ B := le_max_left _ _
  have hb : 1 ≤ b := le_max_left _ _
  have hBpos : 0 < B := lt_of_lt_of_le zero_lt_one hB
  have hbpos : 0 < b := lt_of_lt_of_le zero_lt_one hb
  have hL : 0 < Real.log 2 := Real.log_pos (by norm_num)
  let D : ℝ := Real.log (B + 1) / Real.log 2 + 2 + Real.log b / Real.log 2
  have hLB : 0 ≤ Real.log (B + 1) := Real.log_nonneg (by linarith)
  have hLb : 0 ≤ Real.log b := Real.log_nonneg hb
  have hD : 0 < D := by dsimp [D]; positivity
  refine ⟨D, hD, fun n => ?_⟩
  let x : ℝ := (n : ℝ) + 1
  have hx : 1 ≤ x := by dsimp [x]; positivity
  have hxpos : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
  have hf : (n.factorial : ℝ) ≤ x ^ n := by
    have h := Nat.factorial_le_pow n
    have hc : (n.factorial : ℝ) ≤ (n : ℝ) ^ n := by exact_mod_cast h
    exact hc.trans (pow_le_pow_left₀ hn (by dsimp [x]; linarith) n)
  have hqpow : (1 / q) ^ n ≤ b ^ n :=
    pow_le_pow_left₀ (by positivity) (le_max_right _ _) n
  have hfac : (n.factorial : ℝ) / q ^ n ≤ x ^ n * b ^ n := by
    rw [div_eq_mul_inv, ← inv_pow]
    calc
      _ = (n.factorial : ℝ) * (1 / q) ^ n := by simp
      _ ≤ x ^ n * b ^ n := mul_le_mul hf hqpow (by positivity) (by positivity)
  have hpoly : (n : ℝ) * ((n : ℝ) + 1) ≤ x ^ 2 := by
    dsimp [x]; nlinarith
  have hmain : (n : ℝ) * ((n : ℝ) + 1) *
      (C * ((n.factorial : ℝ) / q ^ n) * (Real.exp (-q) / q)) ≤
      B * x ^ (n + 2) * b ^ n := by
    have hconst : C * (Real.exp (-q) / q) ≤ B := le_max_right _ _
    have hprod := mul_le_mul hpoly
      (mul_le_mul hconst hfac (by positivity) hBpos.le)
      (by positivity) (by positivity : 0 ≤ x ^ 2)
    calc
      _ = ((n : ℝ) * ((n : ℝ) + 1)) *
          ((C * (Real.exp (-q) / q)) * ((n.factorial : ℝ) / q ^ n)) := by ring
      _ ≤ x ^ 2 * (B * (x ^ n * b ^ n)) := hprod
      _ = B * x ^ (n + 2) * b ^ n := by rw [pow_add]; ring
  have hunit : 1 ≤ x ^ (n + 2) * b ^ n :=
    one_le_mul_of_one_le_of_one_le (one_le_pow₀ hx) (one_le_pow₀ hb)
  have hmajor : neutralActualZetaFactorialMajorant p C n ≤
      (B + 1) * x ^ (n + 2) * b ^ n := by
    change (n : ℝ) * ((n : ℝ) + 1) *
      (C * ((n.factorial : ℝ) / q ^ n) * (Real.exp (-q) / q)) + 1 ≤ _
    nlinarith
  have hlog := Real.log_le_log
    (lt_of_lt_of_le zero_lt_one (neutralActualZetaFactorialMajorant_one_le hp hC n))
    hmajor
  have hlogeq : Real.log ((B + 1) * x ^ (n + 2) * b ^ n) =
      Real.log (B + 1) + ((n : ℝ) + 2) * Real.log x + (n : ℝ) * Real.log b := by
    rw [Real.log_mul (by positivity) (by positivity),
      Real.log_mul (by positivity) (by positivity), Real.log_pow, Real.log_pow]
    push_cast
    ring
  rw [hlogeq] at hlog
  have hy : 0 < (n : ℝ) + 2 := by positivity
  have hly : Real.log 2 ≤ Real.log ((n : ℝ) + 2) :=
    Real.log_le_log (by norm_num) (by linarith)
  have hly0 : 0 ≤ Real.log ((n : ℝ) + 2) := hL.le.trans hly
  have hlx : Real.log x ≤ Real.log ((n : ℝ) + 2) :=
    Real.log_le_log hxpos (by dsimp [x]; linarith)
  have hxly : Real.log 2 ≤ x * Real.log ((n : ℝ) + 2) := by nlinarith
  have h1 : Real.log (B + 1) ≤
      (Real.log (B + 1) / Real.log 2) * x * Real.log ((n : ℝ) + 2) := by
    have h := mul_le_mul_of_nonneg_left hxly (div_nonneg hLB hL.le)
    have he : (Real.log (B + 1) / Real.log 2) * Real.log 2 =
        Real.log (B + 1) := div_mul_cancel₀ _ hL.ne'
    rw [he] at h
    nlinarith
  have h2 : ((n : ℝ) + 2) * Real.log x ≤
      2 * x * Real.log ((n : ℝ) + 2) := by
    have h := mul_le_mul_of_nonneg_left hlx (by positivity : 0 ≤ (n : ℝ) + 2)
    dsimp [x] at *
    nlinarith
  have h3 : (n : ℝ) * Real.log b ≤
      (Real.log b / Real.log 2) * x * Real.log ((n : ℝ) + 2) := by
    have h := mul_le_mul_of_nonneg_left hly (div_nonneg hLb hL.le)
    rw [div_mul_cancel₀ _ hL.ne'] at h
    have h' := mul_le_mul_of_nonneg_left h hxpos.le
    have hn' : (n : ℝ) * Real.log b ≤ x * Real.log b :=
      mul_le_mul_of_nonneg_right (by dsimp [x]; linarith) hLb
    nlinarith
  change _ ≤ D * x * Real.log ((n : ℝ) + 2)
  dsimp [D]
  nlinarith

/-- Multiplicity-weighted actual height counts have logarithmic moment-order
growth, directly from the actual theta/Jensen estimates. -/
theorem neutralActualZetaDivisorHeightWindow_card_le_log_moment :
    ∃ K : ℝ, 0 < K ∧ ∀ (T : ℝ) (n : ℕ),
      2 * (|T| + 2) ≤ (n : ℝ) →
      (Fintype.card (neutralActualZetaDivisorHeightWindow T) : ℝ) ≤
        K * ((n : ℝ) + 1) * Real.log ((n : ℝ) + 2) := by
  obtain ⟨p, C, hp, hC, hf⟩ := neutralActualZetaDivisorHeightWindow_card_le_factorial
  obtain ⟨K, hK, hlog⟩ := neutralActualZetaFactorialMajorant_log_bound hp hC
  have hL : 0 < Real.log 2 := Real.log_pos (by norm_num)
  refine ⟨K / Real.log 2, by positivity, fun T n hn => ?_⟩
  calc
    _ ≤ Real.log (neutralActualZetaFactorialMajorant p C n) / Real.log 2 := hf T n hn
    _ ≤ (K * ((n : ℝ) + 1) * Real.log ((n : ℝ) + 2)) / Real.log 2 :=
      div_le_div_of_nonneg_right (hlog n) hL.le
    _ = _ := by ring

end
end WeilDefect
