import WeilDefect.DirichletEnergy

namespace WeilDefect

noncomputable section

attribute [local instance 1100] NormedSpace.complexToReal

open MeasureTheory
open scoped Interval ComplexConjugate

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
  have hg : ContDiff ℝ 2 g := contDiff_dirichletProblemOneColumn a z
  have hh : ContDiff ℝ 2 h := contDiff_dirichletProblemOneColumn a w
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

/-- Reciprocity of distinct actual native source/Green columns. -/
theorem dirichletProblemOneColumn_green_reciprocity (a : ℝ) (z w : ℂ)
    (ha : a ≠ 0) (hz : problemOneGreenDenom z ≠ 0)
    (hw : problemOneGreenDenom w ≠ 0) :
    (∫ x in -a..a, conj (realExpMode (problemOneFreq z) x) *
      dirichletProblemOneColumn a w x) =
    conj (∫ x in -a..a, conj (realExpMode (problemOneFreq w) x) *
      dirichletProblemOneColumn a z x) := by
  have hconj (f g : ℝ → ℂ) :
      (∫ x in -a..a, conj (f x) * g x) =
        conj (∫ x in -a..a, conj (g x) * f x) := by
    rw [← intervalIntegral.intervalIntegral_conj]
    apply intervalIntegral.integral_congr
    intro x _
    simp [mul_comm]
  rw [dirichletProblemOneColumn_green_mixed a z w ha hz,
    dirichletProblemOneColumn_green_mixed a w z ha hw, map_add, map_mul]
  have hq : conj (1 / 4 : ℂ) = 1 / 4 := by
    simp only [map_div₀, map_one, map_ofNat]
  rw [hq, hconj (deriv (dirichletProblemOneColumn a z))
    (deriv (dirichletProblemOneColumn a w)),
    hconj (dirichletProblemOneColumn a z) (dirichletProblemOneColumn a w)]

/-- The mixed law's diagonal agrees with the already certified native
Dirichlet energy; no second energy definition is introduced. -/
theorem dirichletProblemOneColumn_green_mixed_diagonal (a : ℝ) (z : ℂ)
    (ha : 0 < a) (hz : problemOneGreenDenom z ≠ 0) :
    (∫ x in -a..a, conj (deriv (dirichletProblemOneColumn a z) x) *
      deriv (dirichletProblemOneColumn a z) x) +
    (1 / 4 : ℂ) * (∫ x in -a..a,
      conj (dirichletProblemOneColumn a z x) * dirichletProblemOneColumn a z x) =
        (problemOneDirichletEnergy a z : ℂ) := by
  rw [← dirichletProblemOneColumn_green_mixed a z z ha.ne' hz]
  have he := problemOneGreenPairing_eq_dirichletEnergy a z ha hz
  unfold problemOneGreenPairing at he
  simpa only [starRingEnd_apply] using he

end

end WeilDefect
