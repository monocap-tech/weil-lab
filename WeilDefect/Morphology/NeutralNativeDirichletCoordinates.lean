import WeilDefect.DirichletGreenMixed
import WeilDefect.Morphology.NeutralLogDirichletSourceAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped ComplexConjugate Interval

/-- Actual compact derivative coordinate of the full native Green column. -/
def neutralDirichletGradientColumn (a : ℝ) (z : ℂ) (x : ℝ) : ℂ :=
  (Set.Icc (-a) a).indicator (deriv (dirichletProblemOneColumn a z)) x

theorem neutralDirichletGradientColumn_memLp (a : ℝ) (z : ℂ) :
    MemLp (neutralDirichletGradientColumn a z) 2 volume := by
  have hc : Continuous (deriv (dirichletProblemOneColumn a z)) :=
    (contDiff_dirichletProblemOneColumn a z).continuous_deriv (by norm_num)
  have hm : AEStronglyMeasurable (neutralDirichletGradientColumn a z) volume :=
    hc.aestronglyMeasurable.indicator measurableSet_Icc
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hi : IntegrableOn (fun x : ℝ =>
      ‖deriv (dirichletProblemOneColumn a z) x‖ ^ 2) (Set.Icc (-a) a) volume :=
    (hc.norm.pow 2).integrableOn_Icc
  apply (hi.integrable_indicator measurableSet_Icc).congr
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;> simp [neutralDirichletGradientColumn, hx]

def neutralDirichletGradientColumnL2 (a : ℝ) (z : ℂ) : RealComplexL2 :=
  (neutralDirichletGradientColumn_memLp a z).toLp (neutralDirichletGradientColumn a z)

theorem neutralDirichletGradientColumnL2_mixed (a : ℝ) (z w : ℂ) :
    inner ℂ (neutralDirichletGradientColumnL2 a z)
      (neutralDirichletGradientColumnL2 a w) =
      ∫ x in Set.Icc (-a) a,
        conj (deriv (dirichletProblemOneColumn a z) x) *
          deriv (dirichletProblemOneColumn a w) x := by
  rw [L2.inner_def, ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [(neutralDirichletGradientColumn_memLp a z).coeFn_toLp,
    (neutralDirichletGradientColumn_memLp a w).coeFn_toLp] with x hz hw
  change inner ℂ ((neutralDirichletGradientColumn_memLp a z).toLp
    (neutralDirichletGradientColumn a z) x)
    ((neutralDirichletGradientColumn_memLp a w).toLp
      (neutralDirichletGradientColumn a w) x) = _
  rw [hz, hw]
  by_cases hx : x ∈ Set.Icc (-a) a <;>
    simp [neutralDirichletGradientColumn, hx, mul_comm]

theorem neutralDirichletGreenColumnL2_mixed (a : ℝ) (z w : ℂ) :
    inner ℂ (neutralDirichletGreenColumnL2 a z)
      (neutralDirichletGreenColumnL2 a w) =
      ∫ x in Set.Icc (-a) a,
        conj (dirichletProblemOneColumn a z x) *
          dirichletProblemOneColumn a w x := by
  rw [L2.inner_def, ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [(neutralDirichletGreenColumn_memLp a z).coeFn_toLp,
    (neutralDirichletGreenColumn_memLp a w).coeFn_toLp] with x hz hw
  change inner ℂ ((neutralDirichletGreenColumn_memLp a z).toLp
    (neutralDirichletGreenColumn a z) x)
    ((neutralDirichletGreenColumn_memLp a w).toLp
      (neutralDirichletGreenColumn a w) x) = _
  rw [hz, hw]
  by_cases hx : x ∈ Set.Icc (-a) a <;>
    simp [neutralDirichletGreenColumn, hx, mul_comm]

private theorem nativeInterval_eq_window (a : ℝ) (ha : 0 ≤ a) (f : ℝ → ℂ) :
    (∫ x in -a..a, f x) = ∫ x in Set.Icc (-a) a, f x := by
  rw [intervalIntegral.integral_of_le (by linarith), integral_Icc_eq_integral_Ioc]

/-- Exact native source pairing in concrete physical L2 coordinates. -/
theorem neutralDirichletGreen_nativeL2_pairing (a : ℝ) (z w : ℂ)
    (ha : 0 < a) (hz : problemOneGreenDenom z ≠ 0) :
    (∫ x in -a..a, conj (realExpMode (problemOneFreq z) x) *
      dirichletProblemOneColumn a w x) =
      inner ℂ (neutralDirichletGradientColumnL2 a z)
        (neutralDirichletGradientColumnL2 a w) +
      ((1 / 4 : ℝ) : ℂ) * inner ℂ (neutralDirichletGreenColumnL2 a z)
        (neutralDirichletGreenColumnL2 a w) := by
  rw [dirichletProblemOneColumn_green_mixed a z w ha.ne' hz,
    neutralDirichletGradientColumnL2_mixed, neutralDirichletGreenColumnL2_mixed,
    nativeInterval_eq_window a ha.le, nativeInterval_eq_window a ha.le]
  norm_num

/-- The previously certified native energy is the actual sum of the two
physical L2 energies. No stronger domain premise for a WD-T38 mode is used. -/
theorem neutralDirichletGreen_nativeL2_energy (a : ℝ) (z : ℂ)
    (ha : 0 < a) (hz : problemOneGreenDenom z ≠ 0) :
    problemOneColumnEnergySq a z =
      ‖neutralDirichletGradientColumnL2 a z‖ ^ 2 +
        (1 / 4 : ℝ) * ‖neutralDirichletGreenColumnL2 a z‖ ^ 2 := by
  have hp : problemOneGreenPairing a z =
      inner ℂ (neutralDirichletGradientColumnL2 a z)
        (neutralDirichletGradientColumnL2 a z) +
      ((1 / 4 : ℝ) : ℂ) * inner ℂ (neutralDirichletGreenColumnL2 a z)
        (neutralDirichletGreenColumnL2 a z) := by
    unfold problemOneGreenPairing
    simpa only [starRingEnd_apply] using neutralDirichletGreen_nativeL2_pairing a z z ha hz
  have hr := congrArg Complex.re hp
  rw [problemOneGreenPairing_eq_dirichletEnergy a z ha hz, Complex.ofReal_re] at hr
  have hd : (inner ℂ (neutralDirichletGradientColumnL2 a z)
      (neutralDirichletGradientColumnL2 a z)).re =
        ‖neutralDirichletGradientColumnL2 a z‖ ^ 2 :=
    (norm_sq_eq_re_inner (𝕜 := ℂ) (neutralDirichletGradientColumnL2 a z)).symm
  have hg : (inner ℂ (neutralDirichletGreenColumnL2 a z)
      (neutralDirichletGreenColumnL2 a z)).re =
        ‖neutralDirichletGreenColumnL2 a z‖ ^ 2 :=
    (norm_sq_eq_re_inner (𝕜 := ℂ) (neutralDirichletGreenColumnL2 a z)).symm
  simp only [Complex.add_re, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    zero_mul, sub_zero, hd, hg] at hr
  rw [problemOneColumnEnergySq_eq_dirichletEnergy a z ha hz]
  exact hr

end

end WeilDefect
