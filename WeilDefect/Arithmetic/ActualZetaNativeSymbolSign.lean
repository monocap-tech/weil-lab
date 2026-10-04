import WeilDefect.Arithmetic.ActualZetaBackgroundGramTests
import Mathlib.NumberTheory.Harmonic.EulerMascheroni

namespace WeilDefect
noncomputable section
open scoped BigOperators
set_option maxHeartbeats 800000

/-- Actual digamma quarter value, obtained from the pinned duplication,
reflection and half-value identities. No numerical oracle is used. -/
theorem neutralActualZetaDigamma_quarter_re :
    (Complex.digamma (1 / 4)).re =
      -3 * Real.log 2 - Real.eulerMascheroniConstant - Real.pi / 2 := by
  have hs : ∀ n : ℤ, (1 / 4 : ℂ) ≠ n := by
    intro n hn
    have hr := congrArg Complex.re hn
    norm_num at hr
    have he : (1 : ℝ) = 4 * (n : ℝ) := by linarith
    have hi : (1 : ℤ) = 4 * n := by exact_mod_cast he
    omega
  have ht : ∀ m : ℕ, 2 * (1 / 4 : ℂ) ≠ -(m : ℂ) := by
    intro m hm
    have hr := congrArg Complex.re hm
    norm_num at hr
    have hn : (0 : ℝ) ≤ m := Nat.cast_nonneg m
    linarith
  have hcot : Complex.cot ((Real.pi : ℂ) * (1 / 4)) = 1 := by
    have he : (Real.pi : ℂ) * (1 / 4) = ((Real.pi / 4 : ℝ) : ℂ) := by
      push_cast
      ring
    rw [he, ← Complex.ofReal_cot, ← Real.tan_inv_eq_cot,
      Real.tan_pi_div_four]
    norm_num
  have hl : (Complex.log 2).re = Real.log 2 := by
    simpa using Complex.log_ofReal_re (2 : ℝ)
  have hr := congrArg Complex.re (Complex.digamma_one_sub hs)
  have hd := congrArg Complex.re (Complex.digamma_two_mul ht)
  have hh := congrArg Complex.re Complex.digamma_one_half
  norm_num [Complex.add_re, Complex.mul_re, hcot] at hr
  norm_num [Complex.add_re, Complex.mul_re, hl] at hd
  norm_num [Complex.sub_re, Complex.neg_re, Complex.mul_re, hl] at hh
  linarith

theorem neutralActualZetaPrimeCoefficient_nonnegative (n : ℕ) :
    0 ≤ compactWindowPrimeCoefficient n := by
  exact div_nonneg
    (mul_nonneg (by norm_num) ArithmeticFunction.vonMangoldt_nonneg)
    (Real.sqrt_nonneg _)

/-- Exact scalar multiplier value at zero frequency. This is a scalar sign
calculation, not a negative supported-vector certificate. -/
theorem neutralActualZetaNativeSymbol_zero (a : ℝ) :
    rightLimitCompactWeilSymbolMathlib a 0 =
      -3 * Real.log 2 - Real.eulerMascheroniConstant - Real.pi / 2 -
        Real.log Real.pi -
        ∑ n ∈ rightLimitPrimePowerFinset a, compactWindowPrimeCoefficient n := by
  simp only [rightLimitCompactWeilSymbolMathlib, rightLimitCompactWeilSymbol,
    rightLimitPrimeSymbol, compactWindowArchimedeanSymbol,
    mul_zero, zero_div, add_zero, Real.cos_zero, mul_one]
  rw [neutralActualZetaDigamma_quarter_re]

/-- The actual scalar symbol is strictly negative at zero for every window.
Hence unconditional pointwise positivity is not the missing WD-T10 proof. -/
theorem neutralActualZetaNativeSymbol_zero_negative (a : ℝ) :
    rightLimitCompactWeilSymbolMathlib a 0 < 0 := by
  rw [neutralActualZetaNativeSymbol_zero]
  have hp : 0 ≤ ∑ n ∈ rightLimitPrimePowerFinset a, compactWindowPrimeCoefficient n :=
    Finset.sum_nonneg fun n _ => neutralActualZetaPrimeCoefficient_nonnegative n
  have hl2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hlpi : 0 < Real.log Real.pi := Real.log_pos (by linarith [Real.pi_gt_three])
  have hg := Real.one_half_lt_eulerMascheroniConstant
  have hpi := Real.pi_pos
  linarith

theorem neutralActualZetaNativeSymbol_not_pointwise_positive (a : ℝ) :
    ¬ ∀ ξ : ℝ, 0 ≤ rightLimitCompactWeilSymbolMathlib a ξ := by
  intro h
  exact (not_le_of_gt (neutralActualZetaNativeSymbol_zero_negative a)) (h 0)

/-- Scalar negativity persists on an open frequency neighborhood.
Supported vectors and pole/selected corrections remain independent. -/
theorem neutralActualZetaNativeSymbol_negative_neighborhood (a : ℝ) :
    ∃ ε : ℝ, 0 < ε ∧ ∀ ξ : ℝ, |ξ| < ε →
      rightLimitCompactWeilSymbolMathlib a ξ < 0 := by
  have ho : IsOpen {ξ : ℝ | rightLimitCompactWeilSymbolMathlib a ξ < 0} :=
    isOpen_lt (neutralActualZetaNativeSymbol_continuous a) continuous_const
  obtain ⟨ε, he, hb⟩ := Metric.isOpen_iff.mp ho 0
    (neutralActualZetaNativeSymbol_zero_negative a)
  refine ⟨ε, he, ?_⟩
  intro ξ hξ
  apply hb
  simpa only [Metric.mem_ball, Real.dist_eq, sub_zero] using hξ

end
end WeilDefect
