import WeilDefect.Arithmetic.ActualZetaDivisorSummability
import WeilDefect.Morphology.NeutralNativeDirichletCoordinates

namespace WeilDefect
noncomputable section
open scoped ComplexConjugate
open MeasureTheory Set
set_option maxHeartbeats 800000

/-- The concrete endpoint-corrected Green column at an actual divisor copy. -/
def neutralActualZetaGreenColumn (a : ℝ) (q : NeutralActualZetaDivisorCoordinate) :
    RealComplexL2 :=
  neutralDirichletGreenColumnL2 a (neutralActualZetaDivisorOrdinate q)

/-- Inverse-square Green coefficient decay away from the finite low-height set. -/
theorem neutralActualZetaGreenQ_sq_le (q : NeutralActualZetaDivisorCoordinate)
    (hq : 1 ≤ |q.1.val.im|) :
    ‖problemOneGreenQ (neutralActualZetaDivisorOrdinate q)‖ ^ 2 ≤
      16 * neutralActualZetaDivisorQuarticWeight q := by
  let h : ℝ := |q.1.val.im|
  have hh : 0 < h := lt_of_lt_of_le zero_lt_one hq
  have hd : h ^ 2 ≤ ‖problemOneGreenDenom (neutralActualZetaDivisorOrdinate q)‖ := by
    simpa [h, neutralActualZetaDivisorOrdinate, neutralActualZetaOrdinate_re,
      sq_abs] using problemOneGreenDenom_norm_lower
        (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaOrdinate_strictStrip q.1).le
  have hQ : ‖problemOneGreenQ (neutralActualZetaDivisorOrdinate q)‖ ≤ 1 / h ^ 2 := by
    rw [problemOneGreenQ, norm_inv, one_div]
    exact (inv_le_inv₀ (lt_of_lt_of_le (sq_pos_of_pos hh) hd)
      (sq_pos_of_pos hh)).2 hd
  have hs := pow_le_pow_left₀ (norm_nonneg _) hQ 2
  have hp : (1 + h) ^ 4 ≤ 16 * h ^ 4 := by
    have hp := pow_le_pow_left₀ (by positivity : 0 ≤ 1 + h)
      (by change 1 + h ≤ 2 * h; linarith only [hq]) 4
    nlinarith only [hp]
  have hb : (1 / h ^ 2) ^ 2 ≤ 16 / (1 + h) ^ 4 := by
    rw [div_pow, one_pow, ← pow_mul]
    exact (div_le_div_iff₀ (by positivity : 0 < h ^ (2 * 2))
      (by positivity : 0 < (1 + h) ^ 4)).2 (by simpa using hp)
  change _ ≤ 16 * (1 / (1 + h) ^ 4)
  simpa only [mul_one_div] using hs.trans hb

/-- Low-height exceptions are finite; full-divisor coefficient summability is unconditional. -/
theorem neutralActualZetaGreenQ_sq_summable :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖problemOneGreenQ (neutralActualZetaDivisorOrdinate q)‖ ^ 2) := by
  apply Summable.of_norm_bounded_eventually
    (neutralActualZetaDivisorQuarticWeight_summable.mul_left 16)
  filter_upwards [(neutralActualZetaDivisorHeightWindow_finite 1).eventually_cofinite_notMem]
    with q hq
  have hh : 1 ≤ |q.1.val.im| := by
    change ¬ |q.1.val.im| ≤ 1 at hq
    exact (lt_of_not_ge hq).le
  simpa only [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _)] using
    neutralActualZetaGreenQ_sq_le q hh

/-- A concrete compact L² norm bound, obtained from the existing pointwise Green bound. -/
theorem neutralActualZetaGreenColumn_sq_bound (a : ℝ) (ha : 0 < a)
    (q : NeutralActualZetaDivisorCoordinate) :
    ‖neutralActualZetaGreenColumn a q‖ ^ 2 ≤
      (18 * a * (Real.exp (a / 2)) ^ 2) *
        ‖problemOneGreenQ (neutralActualZetaDivisorOrdinate q)‖ ^ 2 := by
  let z := neutralActualZetaDivisorOrdinate q
  have hstrip : |z.im| ≤ 1 / 2 := (neutralActualZetaOrdinate_strictStrip q.1).le
  have hpoint : ∀ x ∈ Ι (-a) a,
      ‖conj (dirichletProblemOneColumn a z x) * dirichletProblemOneColumn a z x‖ ≤
        9 * (Real.exp (a / 2)) ^ 2 * ‖problemOneGreenQ z‖ ^ 2 := by
    intro x hx
    have hx' : x ∈ Ioc (-a) a := by simpa [uIoc_of_le (by linarith : -a ≤ a)] using hx
    have hb := norm_dirichletProblemOneColumn_le a x z ha hstrip ⟨hx'.1.le, hx'.2⟩
    rw [norm_mul, norm_conj]
    have hs := pow_le_pow_left₀ (norm_nonneg _) hb 2
    nlinarith only [hs]
  have hi := intervalIntegral.norm_integral_le_of_norm_le_const hpoint
  rw [abs_of_nonneg (by linarith : 0 ≤ a - (-a))] at hi
  have he : ‖neutralActualZetaGreenColumn a q‖ ^ 2 =
      ‖∫ x in -a..a, conj (dirichletProblemOneColumn a z x) *
        dirichletProblemOneColumn a z x‖ := by
    rw [intervalIntegral.integral_of_le (by linarith : -a ≤ a),
      ← integral_Icc_eq_integral_Ioc, ← neutralDirichletGreenColumnL2_mixed]
    rw [inner_self_eq_norm_sq_to_K, norm_pow, Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (norm_nonneg _)]
    rfl
  rw [he]
  convert hi using 1 <;> ring

/-- All actual multiplicity copies have square-summable concrete Green columns. -/
theorem neutralActualZetaGreenColumn_sq_summable (a : ℝ) (ha : 0 < a) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralActualZetaGreenColumn a q‖ ^ 2) :=
  Summable.of_nonneg_of_le (fun _ => sq_nonneg _)
    (neutralActualZetaGreenColumn_sq_bound a ha)
    (neutralActualZetaGreenQ_sq_summable.mul_left (18 * a * (Real.exp (a / 2)) ^ 2))

/-- Physical Green-smoothed samples converge for every L² input. -/
theorem neutralActualZetaGreenSample_sq_summable (a : ℝ) (ha : 0 < a)
    (f : RealComplexL2) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralActualZetaGreenColumn a q) f‖ ^ 2) := by
  apply Summable.of_nonneg_of_le (fun _ => sq_nonneg _)
    (fun q => ?_) ((neutralActualZetaGreenColumn_sq_summable a ha).mul_right (‖f‖ ^ 2))
  have hs := pow_le_pow_left₀ (norm_nonneg _)
    (norm_inner_le_norm (neutralActualZetaGreenColumn a q) f) 2
  simpa only [mul_pow] using hs

/-- Mixed Green-smoothed samples are absolutely summable on the actual divisor. -/
theorem neutralActualZetaGreenSample_mixed_summable (a : ℝ) (ha : 0 < a)
    (f g : RealComplexL2) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (inner ℂ (neutralActualZetaGreenColumn a q) f) *
        inner ℂ (neutralActualZetaGreenColumn a q) g) := by
  apply Summable.of_norm_bounded
    ((neutralActualZetaGreenColumn_sq_summable a ha).mul_right (‖f‖ * ‖g‖))
  intro q
  rw [norm_mul, norm_conj]
  have hb := mul_le_mul
    (norm_inner_le_norm (neutralActualZetaGreenColumn a q) f)
    (norm_inner_le_norm (neutralActualZetaGreenColumn a q) g)
    (norm_nonneg _) (mul_nonneg (norm_nonneg _) (norm_nonneg _))
  convert hb using 1 <;> ring

end
end WeilDefect
