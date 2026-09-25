import WeilDefect.Arithmetic.LogarithmicForm
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

namespace WeilDefect

open Filter Asymptotics
open scoped Topology

/-- Positive-Sobolev squared frequency weight N^(2 eps). -/
noncomputable def positiveSobolevFrequencyWeight
    (eps x : ℝ) : ℝ :=
  x ^ (2 * eps)

/--
The canonical logarithmic Fourier weight is at most a constant multiple of
log x at high positive frequency.
-/
theorem logarithmicFourierWeight_isBigO_log :
    logarithmicFourierWeight =O[atTop] Real.log := by
  apply IsBigO.of_bound 2
  filter_upwards
    [eventually_ge_atTop (max (Real.exp 1) 2 : ℝ)] with x hx
  have hexp_le : Real.exp 1 ≤ x :=
    (le_max_left _ _).trans hx
  have htwo_le : (2 : ℝ) ≤ x :=
    (le_max_right _ _).trans hx
  have hxpos : 0 < x := lt_of_lt_of_le (by norm_num) htwo_le
  have hx0 : 0 ≤ x := hxpos.le
  have hargpos : 0 < Real.exp 1 + x := by positivity
  have hsum : Real.exp 1 + x ≤ x ^ 2 := by
    calc
      Real.exp 1 + x ≤ x + x := add_le_add_right hexp_le x
      _ = 2 * x := by ring
      _ ≤ x ^ 2 := by nlinarith
  have hlog :
      Real.log (Real.exp 1 + x) ≤ 2 * Real.log x := by
    calc
      Real.log (Real.exp 1 + x)
          ≤ Real.log (x ^ 2) :=
        Real.log_le_log hargpos hsum
      _ = 2 * Real.log x := by
        rw [Real.log_pow]
        norm_num
  have hlogx : 0 ≤ Real.log x := Real.log_nonneg (by linarith)
  have hlogarg : 0 ≤ Real.log (Real.exp 1 + x) := by
    apply Real.log_nonneg
    have : (1 : ℝ) ≤ Real.exp 1 := by
      simpa using Real.one_le_exp 1
    linarith
  rw [Real.norm_eq_abs, Real.norm_eq_abs,
    abs_of_nonneg hlogarg, abs_of_nonneg hlogx]
  simpa [logarithmicFourierWeight, abs_of_nonneg hx0] using hlog

/--
For every positive Sobolev exponent, logarithmic Fourier weight is little-o of
the squared Sobolev frequency weight.
-/
theorem logarithmicFourierWeight_isLittleO_positiveSobolev
    {eps : ℝ} (heps : 0 < eps) :
    logarithmicFourierWeight
      =o[atTop]
    fun x : ℝ => positiveSobolevFrequencyWeight eps x := by
  unfold positiveSobolevFrequencyWeight
  exact logarithmicFourierWeight_isBigO_log.trans_isLittleO
    (isLittleO_log_rpow_atTop (mul_pos (by norm_num) heps))

/--
The positive-Sobolev frequency weight cannot be uniformly O of the logarithmic
Fourier weight.
-/
theorem positiveSobolevFrequencyWeight_not_isBigO_logarithmic
    {eps : ℝ} (heps : 0 < eps) :
    ¬ (fun x : ℝ => positiveSobolevFrequencyWeight eps x)
        =O[atTop] logarithmicFourierWeight := by
  have hfreq :
      ∃ᶠ x : ℝ in atTop,
        positiveSobolevFrequencyWeight eps x ≠ 0 := by
    have hev :
        ∀ᶠ x : ℝ in atTop,
          positiveSobolevFrequencyWeight eps x ≠ 0 := by
      filter_upwards [eventually_gt_atTop (0 : ℝ)] with x hx
      unfold positiveSobolevFrequencyWeight
      exact (Real.rpow_pos_of_pos hx _).ne'
    exact hev.frequently
  exact
    (logarithmicFourierWeight_isLittleO_positiveSobolev heps).not_isBigO
      hfreq

/--
WD-T36 transfer theorem.

Any fixed-support oscillatory witness family whose shifted Weil-form energy is
O(logarithmic weight), while its positive-Sobolev squared norm dominates
N^(2 eps), rules out a uniform coercive Sobolev estimate.
-/
theorem wd_t36_no_uniform_positive_sobolev_coercivity_of_witness
    {eps : ℝ} (heps : 0 < eps)
    (formSq sobolevSq : ℝ → ℝ)
    (hform :
      formSq =O[atTop] logarithmicFourierWeight)
    (hsob :
      (fun x : ℝ => positiveSobolevFrequencyWeight eps x)
        =O[atTop] sobolevSq) :
    ¬ sobolevSq =O[atTop] formSq := by
  intro hcoercive
  have hbad :
      (fun x : ℝ => positiveSobolevFrequencyWeight eps x)
        =O[atTop] logarithmicFourierWeight :=
    hsob.trans (hcoercive.trans hform)
  exact
    positiveSobolevFrequencyWeight_not_isBigO_logarithmic heps hbad

/--
WD-T36 / ZW2-T8 in its pure logarithmic-form sharpness model: no positive
Sobolev frequency weight can be uniformly controlled by the logarithmic form
weight at high frequency.
-/
theorem wd_t36_no_positive_sobolev_bootstrap
    {eps : ℝ} (heps : 0 < eps) :
    ¬ (fun x : ℝ => positiveSobolevFrequencyWeight eps x)
        =O[atTop] logarithmicFourierWeight :=
  positiveSobolevFrequencyWeight_not_isBigO_logarithmic heps

end WeilDefect
