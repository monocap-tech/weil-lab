import WeilDefect.Arithmetic.ActualZetaDyadicSummability
import WeilDefect.Arithmetic.ActualZetaGreenSampling

namespace WeilDefect
noncomputable section
open InnerProductSpace ContinuousLinearMap
open scoped ENNReal
set_option maxHeartbeats 800000

/-- The compact derivative of the endpoint-corrected actual Green column. -/
def neutralActualZetaGradientColumn (a : ℝ) (q : NeutralActualZetaDivisorCoordinate) :
    RealComplexL2 :=
  neutralDirichletGradientColumnL2 a (neutralActualZetaDivisorOrdinate q)

theorem neutralActualZetaGreenQ_le_quadratic (q : NeutralActualZetaDivisorCoordinate)
    (hq : 1 ≤ |q.1.val.im|) :
    ‖problemOneGreenQ (neutralActualZetaDivisorOrdinate q)‖ ≤
      4 * neutralActualZetaDivisorQuadraticWeight q := by
  let h : ℝ := |q.1.val.im|
  have hh : 0 < h := lt_of_lt_of_le zero_lt_one hq
  have hd : h ^ 2 ≤ ‖problemOneGreenDenom (neutralActualZetaDivisorOrdinate q)‖ := by
    simpa [h, neutralActualZetaDivisorOrdinate, neutralActualZetaOrdinate_re, sq_abs] using
      problemOneGreenDenom_norm_lower (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaOrdinate_strictStrip q.1).le
  have hQ : ‖problemOneGreenQ (neutralActualZetaDivisorOrdinate q)‖ ≤ 1 / h ^ 2 := by
    rw [problemOneGreenQ, norm_inv, one_div]
    exact (inv_le_inv₀ (lt_of_lt_of_le (sq_pos_of_pos hh) hd) (sq_pos_of_pos hh)).2 hd
  have hp : (1 + h) ^ 2 ≤ 4 * h ^ 2 := by
    have hp := pow_le_pow_left₀ (by positivity : 0 ≤ 1 + h)
      (by change 1 + h ≤ 2 * h; linarith only [hq]) 2
    nlinarith only [hp]
  have hb : 1 / h ^ 2 ≤ 4 / (1 + h) ^ 2 :=
    (div_le_div_iff₀ (by positivity) (by positivity)).2 (by simpa using hp)
  change _ ≤ 4 * (1 / (1 + h) ^ 2)
  simpa only [mul_one_div] using hQ.trans hb

/-- Full actual-divisor absolute summability of reciprocal Green coefficients. -/
theorem neutralActualZetaGreenQ_norm_summable :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖problemOneGreenQ (neutralActualZetaDivisorOrdinate q)‖) := by
  apply Summable.of_norm_bounded_eventually
    (neutralActualZetaDivisorQuadraticWeight_summable.mul_left 4)
  filter_upwards [(neutralActualZetaDivisorHeightWindow_finite 1).eventually_cofinite_notMem]
    with q hq
  have hh : 1 ≤ |q.1.val.im| := by
    change ¬ |q.1.val.im| ≤ 1 at hq
    exact (lt_of_not_ge hq).le
  simpa only [norm_norm] using neutralActualZetaGreenQ_le_quadratic q hh

/-- Exact physical value-plus-gradient energy, using actual open-strip nonresonance. -/
theorem neutralActualZetaGreenEnergy_coordinates (a : ℝ) (ha : 0 < a)
    (q : NeutralActualZetaDivisorCoordinate) :
    problemOneColumnEnergySq a (neutralActualZetaDivisorOrdinate q) =
      ‖neutralActualZetaGradientColumn a q‖ ^ 2 +
        (1 / 4 : ℝ) * ‖neutralActualZetaGreenColumn a q‖ ^ 2 :=
  neutralDirichletGreen_nativeL2_energy a (neutralActualZetaDivisorOrdinate q) ha
    (neutralActualZetaOrdinate_greenDenom_ne_zero q.1)

/-- Actual Dirichlet Green energies sum over all analytic multiplicity copies. -/
theorem neutralActualZetaGreenEnergy_summable (a : ℝ) (ha : 0 < a) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      problemOneColumnEnergySq a (neutralActualZetaDivisorOrdinate q)) := by
  apply Summable.of_nonneg_of_le (fun q => norm_nonneg _)
    (fun q => problemOneColumnEnergySq_le a (neutralActualZetaDivisorOrdinate q) ha
      (neutralActualZetaOrdinate_strictStrip q.1).le)
    (neutralActualZetaGreenQ_norm_summable.mul_left (6 * a * (Real.exp (a / 2)) ^ 2))

/-- Concrete compact derivative columns are square summable on the actual divisor. -/
theorem neutralActualZetaGradientColumn_sq_summable (a : ℝ) (ha : 0 < a) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralActualZetaGradientColumn a q‖ ^ 2) := by
  apply Summable.of_nonneg_of_le (fun q => sq_nonneg _) (fun q => ?_)
    (neutralActualZetaGreenEnergy_summable a ha)
  rw [neutralActualZetaGreenEnergy_coordinates a ha q]
  have hg := sq_nonneg ‖neutralActualZetaGreenColumn a q‖
  linarith

/-- Every actual lp² coefficient family has a convergent derivative-column synthesis. -/
theorem neutralActualZetaGradientSeries_summable (a : ℝ) (ha : 0 < a)
    (u : NeutralActualZetaGreenCoefficients) :
    Summable (fun q => u q • neutralActualZetaGradientColumn a q) := by
  have hu : Summable (fun q => ‖u q‖ ^ 2) := by
    simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
      (lp.hasSum_norm (p := (2 : ℝ≥0∞)) (by norm_num) u).summable
  have hn : Summable (fun q => ‖u q • neutralActualZetaGradientColumn a q‖) := by
    apply Summable.of_nonneg_of_le (fun q => norm_nonneg _) (fun q => ?_)
      (hu.add (neutralActualZetaGradientColumn_sq_summable a ha))
    rw [norm_smul]
    nlinarith only [sq_nonneg (‖u q‖ - ‖neutralActualZetaGradientColumn a q‖)]
  exact hn.of_norm

/-- The actual derivative-column synthesis as a physical L² vector. -/
def neutralActualZetaGradientSynthesis (a : ℝ) (u : NeutralActualZetaGreenCoefficients) :
    RealComplexL2 :=
  ∑' q, u q • neutralActualZetaGradientColumn a q

theorem neutralActualZetaGradientSynthesis_hasSum (a : ℝ) (ha : 0 < a)
    (u : NeutralActualZetaGreenCoefficients) :
    HasSum (fun q => u q • neutralActualZetaGradientColumn a q)
      (neutralActualZetaGradientSynthesis a u) :=
  (neutralActualZetaGradientSeries_summable a ha u).hasSum

theorem neutralActualZetaGradientSynthesis_inner (a : ℝ) (ha : 0 < a)
    (u : NeutralActualZetaGreenCoefficients) (f : RealComplexL2) :
    inner ℂ f (neutralActualZetaGradientSynthesis a u) =
      ∑' q, u q * inner ℂ f (neutralActualZetaGradientColumn a q) := by
  have h := (neutralActualZetaGradientSynthesis_hasSum a ha u).mapL (innerSL ℂ f)
  simpa only [innerSL_apply_apply, inner_smul_right] using h.tsum_eq.symm

end
end WeilDefect
