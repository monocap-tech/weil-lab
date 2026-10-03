import WeilDefect.DirichletResolvent
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts

namespace WeilDefect

noncomputable section

attribute [local instance 1100] NormedSpace.complexToReal

open MeasureTheory
open scoped Interval ComplexConjugate

theorem contDiff_dirichletProblemOneColumn (n : ℕ) (a : ℝ) (z : ℂ) :
    ContDiff ℝ n (dirichletProblemOneColumn a z) := by
  unfold dirichletProblemOneColumn dirichletRightBasis dirichletLeftBasis
    dirichletRightReal dirichletLeftReal realExpMode
  fun_prop

/-- Integration by parts for the full actual Green columns. Only the source
column's existing nonresonance condition and the Dirichlet endpoints are used. -/
theorem dirichletProblemOneColumn_green_mixed (a : ℝ) (z w : ℂ)
    (ha : a ≠ 0) (hz : problemOneGreenDenom z ≠ 0) :
    (∫ x in -a..a, conj (realExpMode (problemOneFreq z) x) *
      dirichletProblemOneColumn a w x) =
    (∫ x in -a..a, conj (deriv (dirichletProblemOneColumn a z) x) *
      deriv (dirichletProblemOneColumn a w) x) +
    (1 / 4 : ℂ) * (∫ x in -a..a,
      conj (dirichletProblemOneColumn a z x) * dirichletProblemOneColumn a w x) := by
  let g := dirichletProblemOneColumn a z
  let h := dirichletProblemOneColumn a w
  have hg : ContDiff ℝ 2 g := contDiff_dirichletProblemOneColumn 2 a z
  have hh : ContDiff ℝ 2 h := contDiff_dirichletProblemOneColumn 2 a w
  have hdg : ContDiff ℝ 1 (deriv g) := hg.deriv'
  have hddg : Continuous (deriv (deriv g)) :=
    hdg.continuous_deriv (by norm_num)
  have hdh : Continuous (deriv h) := hh.continuous_deriv (by norm_num)
  have h1 : IntervalIntegrable (fun x => conj (deriv (deriv g) x) * h x)
      volume (-a) a := (hddg.star.mul hh.continuous).intervalIntegrable _ _
  have h2 : IntervalIntegrable (fun x => conj (deriv g x) * deriv h x)
      volume (-a) a := (hdg.continuous.star.mul hdh).intervalIntegrable _ _
  have h3 : IntervalIntegrable (fun x => conj (g x) * h x)
      volume (-a) a := (hg.continuous.star.mul hh.continuous).intervalIntegrable _ _
  have hib := intervalIntegral.integral_deriv_mul_eq_sub
    (fun x _ => ((hdg.differentiable (by norm_num) x).hasDerivAt).star)
    (fun x _ => (hh.differentiable (by norm_num) x).hasDerivAt)
    (hddg.star.intervalIntegrable (-a) a)
    (hdh.intervalIntegrable (-a) a)
  have hsum : (∫ x in -a..a, conj (deriv (deriv g) x) * h x) +
      (∫ x in -a..a, conj (deriv g x) * deriv h x) = 0 := by
    rw [← intervalIntegral.integral_add h1 h2]
    simpa only [starRingEnd_apply, h, dirichletProblemOneColumn_pos a w ha,
      dirichletProblemOneColumn_neg a w ha, mul_zero, sub_zero] using hib
  have hsource : ∀ x, conj (realExpMode (problemOneFreq z) x) * h x =
      -(conj (deriv (deriv g) x) * h x) +
        (1 / 4 : ℂ) * (conj (g x) * h x) := by
    intro x
    rw [← problemOneL_dirichletProblemOneColumn a x z hz]
    change conj (-(iteratedDeriv 2 g x) + (1 / 4 : ℂ) * g x) * h x = _
    simp only [iteratedDeriv_succ, iteratedDeriv_zero, map_add, map_neg, map_mul,
      map_div₀, map_one, map_ofNat]
    ring
  calc
    _ = ∫ x in -a..a, -(conj (deriv (deriv g) x) * h x) +
        (1 / 4 : ℂ) * (conj (g x) * h x) := by
      apply intervalIntegral.integral_congr
      intro x _
      exact hsource x
    _ = -(∫ x in -a..a, conj (deriv (deriv g) x) * h x) +
        (1 / 4 : ℂ) * (∫ x in -a..a, conj (g x) * h x) := by
      have hadd := intervalIntegral.integral_add h1.neg
        (h3.const_mul (1 / 4 : ℂ))
      simpa only [Pi.neg_apply, intervalIntegral.integral_neg,
        intervalIntegral.integral_const_mul] using hadd
    _ = _ := by
      change -(∫ x in -a..a, conj (deriv (deriv g) x) * h x) + _ =
        (∫ x in -a..a, conj (deriv g x) * deriv h x) + _
      have heq : -(∫ x in -a..a, conj (deriv (deriv g) x) * h x) =
          (∫ x in -a..a, conj (deriv g x) * deriv h x) := by
        linear_combination -hsum
      rw [heq]

/-- Genuine positive Dirichlet energy of the actual full Green column. -/
def problemOneDirichletEnergy (a : ℝ) (z : ℂ) : ℝ :=
  (∫ x in -a..a, ‖deriv (dirichletProblemOneColumn a z) x‖ ^ 2) +
    (1 / 4 : ℝ) * (∫ x in -a..a, ‖dirichletProblemOneColumn a z x‖ ^ 2)

theorem problemOneGreenPairing_eq_dirichletEnergy (a : ℝ) (z : ℂ)
    (ha : a ≠ 0) (hz : problemOneGreenDenom z ≠ 0) :
    problemOneGreenPairing a z = (problemOneDirichletEnergy a z : ℂ) := by
  unfold problemOneGreenPairing
  simp only [← starRingEnd_apply]
  rw [dirichletProblemOneColumn_green_mixed a z z ha hz]
  simp only [Complex.conj_mul', Complex.ofReal_pow, intervalIntegral.integral_ofReal,
    problemOneDirichletEnergy, Complex.ofReal_add, Complex.ofReal_mul,
    Complex.ofReal_div, Complex.ofReal_one, Complex.ofReal_ofNat]

theorem problemOneDirichletEnergy_nonnegative (a : ℝ) (z : ℂ) (ha : 0 ≤ a) :
    0 ≤ problemOneDirichletEnergy a z := by
  unfold problemOneDirichletEnergy
  apply add_nonneg
  · exact intervalIntegral.integral_nonneg_of_forall (by linarith) (fun x => sq_nonneg _)
  · apply mul_nonneg (by norm_num)
    exact intervalIntegral.integral_nonneg_of_forall (by linarith) (fun x => sq_nonneg _)

/-- The retained native column energy is now the genuine Dirichlet energy.
This is column regularity, not Weil spectral L2 membership of a WD-T38 mode. -/
theorem problemOneColumnEnergySq_eq_dirichletEnergy (a : ℝ) (z : ℂ)
    (ha : 0 < a) (hz : problemOneGreenDenom z ≠ 0) :
    problemOneColumnEnergySq a z = problemOneDirichletEnergy a z := by
  rw [problemOneColumnEnergySq,
    problemOneGreenPairing_eq_dirichletEnergy a z (ne_of_gt ha) hz,
    Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (problemOneDirichletEnergy_nonnegative a z ha.le)]

end

end WeilDefect
