import WeilDefect.Morphology.NeutralNativeDirichletSynthesis
import Mathlib.Analysis.Distribution.SchwartzSpace.Deriv

namespace WeilDefect

noncomputable section

attribute [local instance 1100] NormedSpace.complexToReal

open MeasureTheory InnerProductSpace
open scoped BigOperators Interval ComplexConjugate SchwartzMap

private theorem nativeTest_compactColumn_inner
    (a : ℝ) (f : ℝ → ℂ)
    (hf : MemLp ((Set.Icc (-a) a).indicator f) 2 volume)
    (u : SchwartzMap ℝ ℂ) :
    inner ℂ (u.toLp 2 volume) (hf.toLp ((Set.Icc (-a) a).indicator f)) =
      ∫ x in Set.Icc (-a) a, conj (u x) * f x := by
  rw [L2.inner_def, ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [u.coeFn_toLp 2 volume, hf.coeFn_toLp] with x hu hx
  rw [hu, hx]
  by_cases hmem : x ∈ Set.Icc (-a) a <;> simp [hmem, mul_comm]

theorem neutralNativeTest_green_inner (a : ℝ) (z : ℂ) (u : SchwartzMap ℝ ℂ) :
    inner ℂ (u.toLp 2 volume) (neutralDirichletGreenColumnL2 a z) =
      ∫ x in Set.Icc (-a) a, conj (u x) * dirichletProblemOneColumn a z x :=
  nativeTest_compactColumn_inner a _ (neutralDirichletGreenColumn_memLp a z) u

theorem neutralNativeTest_gradient_inner (a : ℝ) (z : ℂ) (u : SchwartzMap ℝ ℂ) :
    inner ℂ (u.toLp 2 volume) (neutralDirichletGradientColumnL2 a z) =
      ∫ x in Set.Icc (-a) a,
        conj (u x) * deriv (dirichletProblemOneColumn a z) x :=
  nativeTest_compactColumn_inner a _ (neutralDirichletGradientColumn_memLp a z) u

private theorem nativeWeak_interval_eq_window
    (a : ℝ) (ha : 0 ≤ a) (f : ℝ → ℂ) :
    (∫ x in -a..a, f x) = ∫ x in Set.Icc (-a) a, f x := by
  rw [intervalIntegral.integral_of_le (by linarith), integral_Icc_eq_integral_Ioc]

/-- Global weak derivative identity for the zero-extended actual Green column.
The Dirichlet endpoints cancel for every Schwartz test, without a support
restriction on the test and without a spectral-domain premise. -/
theorem neutralNativeGreenColumn_weakDerivative
    (a : ℝ) (ha : 0 < a) (z : ℂ) (u : SchwartzMap ℝ ℂ) :
    inner ℂ ((SchwartzMap.derivCLM ℂ ℂ u).toLp 2 volume)
        (neutralDirichletGreenColumnL2 a z) =
      -inner ℂ (u.toLp 2 volume) (neutralDirichletGradientColumnL2 a z) := by
  let g := dirichletProblemOneColumn a z
  have hg : ContDiff ℝ 2 g := contDiff_dirichletProblemOneColumn a z
  have hdu : Continuous (deriv u) := (u.smooth 2).continuous_deriv (by norm_num)
  have hdg : Continuous (deriv g) := hg.continuous_deriv (by norm_num)
  have h1 : IntervalIntegrable (fun x => conj (deriv u x) * g x)
      volume (-a) a := (hdu.star.mul hg.continuous).intervalIntegrable _ _
  have h2 : IntervalIntegrable (fun x => conj (u x) * deriv g x)
      volume (-a) a := (u.continuous.star.mul hdg).intervalIntegrable _ _
  have hib := intervalIntegral.integral_deriv_mul_eq_sub
    (fun x _ => (u.hasDerivAt x).star)
    (fun x _ => (hg.differentiable (by norm_num) x).hasDerivAt)
    (hdu.star.intervalIntegrable (-a) a)
    (hdg.intervalIntegrable (-a) a)
  have hsum : (∫ x in -a..a, conj (deriv u x) * g x) +
      (∫ x in -a..a, conj (u x) * deriv g x) = 0 := by
    rw [← intervalIntegral.integral_add h1 h2]
    simpa only [starRingEnd_apply, g, dirichletProblemOneColumn_pos a z ha.ne',
      dirichletProblemOneColumn_neg a z ha.ne', mul_zero, sub_zero] using hib
  rw [neutralNativeTest_green_inner, neutralNativeTest_gradient_inner]
  simp only [SchwartzMap.derivCLM_apply]
  simp only [nativeWeak_interval_eq_window a ha.le] at hsum
  change (∫ x in Set.Icc (-a) a, conj (deriv u x) * g x) =
    -(∫ x in Set.Icc (-a) a, conj (u x) * deriv g x)
  linear_combination hsum

/-- The actual derivative synthesis is the global weak derivative of the
actual Green synthesis. Both vectors were already constructed in L2.
This identifies native regularity, not the independently supplied WD-T38 mode. -/
theorem neutralNativeGreenSynthesis_weakDerivative
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) (u : SchwartzMap ℝ ℂ) :
    inner ℂ ((SchwartzMap.derivCLM ℂ ℂ u).toLp 2 volume)
        (neutralNativeGreenSynthesis a data v) =
      -inner ℂ (u.toLp 2 volume) (neutralNativeGradientSynthesis a data v) := by
  rw [neutralNativeGreenSynthesis_inner a ha data C hCount,
    neutralNativeGradientSynthesis_inner a ha data C hCount, ← tsum_neg]
  apply tsum_congr
  intro g
  rw [neutralNativeGreenColumn_weakDerivative a ha (data.gamma g) u, mul_neg]

end

end WeilDefect
