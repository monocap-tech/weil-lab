import WeilDefect.Morphology.NeutralDigammaCentering
import Mathlib.Analysis.PSeries

namespace WeilDefect

noncomputable section

open scoped BigOperators

/-- Exact real deficit of a reciprocal term after zero-frequency centering. -/
theorem neutralGaussReciprocal_centered_deficit (n : ℕ) (t : ℝ) :
    neutralGaussReciprocal n 0 - neutralGaussReciprocal n t =
      (t/2)^2 / (((n : ℝ)+1/4) * (((n : ℝ)+1/4)^2 + (t/2)^2)) := by
  have hr : 0 < (n : ℝ)+1/4 := by positivity
  have hd : 0 < ((n : ℝ)+1/4)^2 + (t/2)^2 := by positivity
  unfold neutralGaussReciprocal
  field_simp [ne_of_gt hr, ne_of_gt hd] <;> ring

/-- A concrete cubic bound uniform in the natural shift index. -/
theorem neutralGaussReciprocal_centered_bound (n : ℕ) (t : ℝ) :
    0 ≤ neutralGaussReciprocal n 0 - neutralGaussReciprocal n t ∧
    neutralGaussReciprocal n 0 - neutralGaussReciprocal n t ≤
      64 * (t/2)^2 / ((n : ℝ)+1)^3 := by
  rw [neutralGaussReciprocal_centered_deficit]
  let r : ℝ := (n : ℝ)+1/4
  let s : ℝ := (n : ℝ)+1
  have hr : 0 < r := by dsimp [r]; positivity
  have hs : 0 < s := by dsimp [s]; positivity
  have hd : 0 < r * (r^2+(t/2)^2) := by positivity
  have hsr : s ≤ 4*r := by dsimp [s,r]; nlinarith [Nat.cast_nonneg n (R := ℝ)]
  have hc : s^3 ≤ (4*r)^3 := pow_le_pow_left₀ hs.le hsr 3
  constructor
  · exact div_nonneg (sq_nonneg _) hd.le
  · change (t/2)^2 / (r*(r^2+(t/2)^2)) ≤ 64*(t/2)^2/s^3
    apply (div_le_div_iff₀ hd (pow_pos hs 3)).mpr
    have h := mul_le_mul_of_nonneg_left hc (sq_nonneg (t/2))
    nlinarith [mul_nonneg hr.le (sq_nonneg ((t/2)^2))]

/-- Exact actual centered digamma increment, derived from the recurrence. -/
theorem neutralCenteredDigammaSymbol_step (N : ℕ) (ξ : ℝ) :
    neutralCenteredDigammaSymbol (N+1) ξ - neutralCenteredDigammaSymbol N ξ =
      ((neutralGaussReciprocal N (2*Real.pi*ξ) - neutralGaussReciprocal N 0 : ℝ) : ℂ) := by
  unfold neutralCenteredDigammaSymbol
  simp only [neutralShiftedDigammaSymbol_eq_add, Pi.add_apply, Finset.sum_range_succ,
    Complex.ofReal_add, mul_zero, Complex.ofReal_sub]
  ring

/-- Independent quantitative decay of successive actual centered tails.
This bounds increments, not the centered tail's limiting value. -/
theorem neutralCenteredDigammaSymbol_step_norm_bound (N : ℕ) (ξ : ℝ) :
    ‖neutralCenteredDigammaSymbol (N+1) ξ - neutralCenteredDigammaSymbol N ξ‖ ≤
      64 * (Real.pi*ξ)^2 / ((N : ℝ)+1)^3 := by
  rw [neutralCenteredDigammaSymbol_step, Complex.norm_real, Real.norm_eq_abs,
    ← abs_neg]
  have h := neutralGaussReciprocal_centered_bound N (2*Real.pi*ξ)
  have he : -(neutralGaussReciprocal N (2*Real.pi*ξ) - neutralGaussReciprocal N 0) =
      neutralGaussReciprocal N 0 - neutralGaussReciprocal N (2*Real.pi*ξ) := by ring
  rw [he, abs_of_nonneg h.1]
  convert h.2 using 1 <;> ring

/-- Every fixed-frequency actual centered-tail increment series is absolutely
summable. No identification of the resulting limit with zero is asserted. -/
theorem neutralCenteredDigammaSymbol_step_norm_summable (ξ : ℝ) :
    Summable (fun N : ℕ =>
      ‖neutralCenteredDigammaSymbol (N+1) ξ - neutralCenteredDigammaSymbol N ξ‖) := by
  have hs : Summable (fun N : ℕ => 1 / ((N : ℝ)+1)^3) := by
    simpa only [Nat.cast_add, Nat.cast_one] using
      (summable_nat_add_iff (f := fun N : ℕ => 1 / (N : ℝ)^3) 1).mpr
        (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < (3 : ℕ)))
  have hb : Summable (fun N : ℕ => 64*(Real.pi*ξ)^2 / ((N : ℝ)+1)^3) := by
    simpa only [mul_one_div] using hs.mul_left (64*(Real.pi*ξ)^2)
  exact hb.of_nonneg_of_le (fun _ => norm_nonneg _)
    (fun N => neutralCenteredDigammaSymbol_step_norm_bound N ξ)

end

end WeilDefect
