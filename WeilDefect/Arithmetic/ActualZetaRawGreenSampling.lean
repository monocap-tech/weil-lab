import WeilDefect.Arithmetic.ActualZetaGreenCanonical

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped ComplexConjugate Interval FourierTransform
set_option maxHeartbeats 800000

theorem neutralWindowEvaluation_eq_inner (a : ℝ) (z : ℂ) (f : RealComplexL2) :
    neutralWindowEvaluation a z f =
      inner ℂ (neutralExponentialColumnL2 a (conj z)) f := by
  rw [neutralExponentialColumnL2_inner]
  simp

private theorem actualWindow_compactColumn (a : ℝ) (z : ℂ) (g : ℝ → ℂ)
    (hg : MemLp ((Set.Icc (-a) a).indicator g) 2 volume) :
    neutralWindowEvaluation a z (hg.toLp ((Set.Icc (-a) a).indicator g)) =
      ∫ x in Set.Icc (-a) a, g x * Complex.exp (Complex.I * z * (x : ℂ)) := by
  unfold neutralWindowEvaluation
  rw [← integral_indicator measurableSet_Icc, ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [hg.coeFn_toLp] with x hx
  by_cases hmem : x ∈ Set.Icc (-a) a <;> simp [hmem, hx]

/-- Dirichlet endpoint cancellation gives the exact raw-evaluation derivative relation. -/
theorem neutralActualZetaGreenColumn_windowDerivative (a : ℝ) (ha : 0 < a)
    (w z : ℂ) :
    Complex.I * z * neutralWindowEvaluation a z (neutralDirichletGreenColumnL2 a w) =
      -neutralWindowEvaluation a z (neutralDirichletGradientColumnL2 a w) := by
  let e : ℝ → ℂ := fun x => Complex.exp (Complex.I * z * (x : ℂ))
  let g := dirichletProblemOneColumn a w
  have hg : ContDiff ℝ 2 g := contDiff_dirichletProblemOneColumn a w
  have he (x : ℝ) : HasDerivAt e (Complex.I * z * e x) x := by
    simpa [e, mul_comm] using
      (((Complex.ofRealCLM.hasDerivAt (x := x)).const_mul (Complex.I * z)).cexp)
  have hc : Continuous e := by unfold e; fun_prop
  have hd : Continuous (deriv g) := hg.continuous_deriv (by norm_num)
  have h1 : IntervalIntegrable (fun x => (Complex.I * z * e x) * g x)
      volume (-a) a := ((hc.const_mul _).mul hg.continuous).intervalIntegrable _ _
  have h2 : IntervalIntegrable (fun x => e x * deriv g x)
      volume (-a) a := (hc.mul hd).intervalIntegrable _ _
  have hib := intervalIntegral.integral_deriv_mul_eq_sub
    (fun x _ => he x)
    (fun x _ => (hg.differentiable (by norm_num) x).hasDerivAt)
    ((hc.const_mul (Complex.I * z)).intervalIntegrable (-a) a)
    (hd.intervalIntegrable (-a) a)
  have hs : (∫ x in -a..a, (Complex.I * z * e x) * g x) +
      (∫ x in -a..a, e x * deriv g x) = 0 := by
    rw [← intervalIntegral.integral_add h1 h2]
    simpa only [g, dirichletProblemOneColumn_pos a w ha.ne',
      dirichletProblemOneColumn_neg a w ha.ne', mul_zero, sub_zero] using hib
  have hwin (f : ℝ → ℂ) :
      (∫ x in -a..a, f x) = ∫ x in Set.Icc (-a) a, f x := by
    rw [intervalIntegral.integral_of_le (by linarith), integral_Icc_eq_integral_Ioc]
  simp only [hwin] at hs
  have heq : (fun x => (Complex.I * z * e x) * g x) =
      (fun x => (Complex.I * z) * (g x * e x)) := by funext x; ring
  rw [heq, integral_const_mul] at hs
  have heq' : (fun x => e x * deriv g x) = (fun x => deriv g x * e x) := by
    funext x; ring
  rw [heq'] at hs
  have hG : neutralWindowEvaluation a z (neutralDirichletGreenColumnL2 a w) =
      ∫ x in Set.Icc (-a) a, g x * e x :=
    actualWindow_compactColumn a z g (neutralDirichletGreenColumn_memLp a w)
  have hD : neutralWindowEvaluation a z (neutralDirichletGradientColumnL2 a w) =
      ∫ x in Set.Icc (-a) a, deriv g x * e x :=
    actualWindow_compactColumn a z (deriv g) (neutralDirichletGradientColumn_memLp a w)
  rw [hG, hD]
  linear_combination hs

/-- Raw evaluation of the convergent actual synthesis obeys the same derivative identity. -/
theorem neutralActualZetaGreenSynthesis_windowDerivative (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) (z : ℂ) :
    Complex.I * z * neutralWindowEvaluation a z (neutralActualZetaGreenSynthesis a v) =
      -neutralWindowEvaluation a z (neutralActualZetaGradientSynthesis a v) := by
  rw [neutralWindowEvaluation_eq_inner, neutralWindowEvaluation_eq_inner,
    neutralActualZetaGreenSynthesis_inner a ha,
    neutralActualZetaGradientSynthesis_inner a ha, ← tsum_mul_left, ← tsum_neg]
  apply tsum_congr
  intro q
  have h := neutralActualZetaGreenColumn_windowDerivative a ha
    (neutralActualZetaDivisorOrdinate q) z
  rw [neutralWindowEvaluation_eq_inner, neutralWindowEvaluation_eq_inner] at h
  change Complex.I * z * (v q * inner ℂ (neutralExponentialColumnL2 a (conj z))
      (neutralDirichletGreenColumnL2 a (neutralActualZetaDivisorOrdinate q))) =
    -(v q * inner ℂ (neutralExponentialColumnL2 a (conj z))
      (neutralDirichletGradientColumnL2 a (neutralActualZetaDivisorOrdinate q)))
  linear_combination v q * h

/-- Uniform raw-column norm bound on the closed zeta ordinate strip. -/
theorem neutralExponentialColumnL2_sq_bound (a : ℝ) (ha : 0 < a) (z : ℂ)
    (hz : |z.im| ≤ 1 / 2) :
    ‖neutralExponentialColumnL2 a z‖ ^ 2 ≤ 2 * a * (Real.exp (a / 2)) ^ 2 := by
  let g : ℝ → ℂ := fun x => Complex.exp (-Complex.I * z * (x : ℂ))
  have hg (x : ℝ) (hx : x ∈ Set.Icc (-a) a) : ‖g x‖ ≤ Real.exp (a / 2) := by
    simpa [g, realExpMode, problemOneFreq, mul_comm, mul_left_comm, mul_assoc] using
      norm_problemOne_source_le a x z ha.le hz hx
  have hpoint : ∀ x ∈ Ι (-a) a, ‖conj (g x) * g x‖ ≤ (Real.exp (a / 2)) ^ 2 := by
    intro x hx
    have hx' : x ∈ Set.Ioc (-a) a := by simpa [Set.uIoc_of_le (by linarith : -a ≤ a)] using hx
    rw [norm_mul, Complex.norm_conj]
    simpa only [pow_two] using pow_le_pow_left₀ (norm_nonneg _) (hg x ⟨hx'.1.le, hx'.2⟩) 2
  have hi := intervalIntegral.norm_integral_le_of_norm_le_const hpoint
  rw [abs_of_nonneg (by linarith : 0 ≤ a - (-a))] at hi
  have hm : inner ℂ (neutralExponentialColumnL2 a z) (neutralExponentialColumnL2 a z) =
      ∫ x in Set.Icc (-a) a, conj (g x) * g x := by
    rw [L2.inner_def, ← integral_indicator measurableSet_Icc]
    apply integral_congr_ae
    filter_upwards [(neutralExponentialColumn_memLp a z).coeFn_toLp] with x hx
    change inner ℂ
      ((neutralExponentialColumn_memLp a z).toLp (neutralExponentialColumn a z) x)
      ((neutralExponentialColumn_memLp a z).toLp (neutralExponentialColumn a z) x) = _
    rw [hx]
    by_cases hmem : x ∈ Set.Icc (-a) a <;>
      simp [neutralExponentialColumn, g, hmem, RCLike.inner_apply', mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq]
  have he : ‖neutralExponentialColumnL2 a z‖ ^ 2 =
      ‖∫ x in -a..a, conj (g x) * g x‖ := by
    rw [intervalIntegral.integral_of_le (by linarith : -a ≤ a),
      ← integral_Icc_eq_integral_Ioc, ← hm,
      inner_self_eq_norm_sq_to_K (𝕜 := ℂ), norm_pow, RCLike.norm_ofReal, abs_norm]
  rw [he]
  convert hi using 1 <;> ring

/-- Raw compact-window evaluation is bounded uniformly across the zeta strip. -/
theorem neutralWindowEvaluation_sq_bound (a : ℝ) (ha : 0 < a) (z : ℂ)
    (hz : |z.im| ≤ 1 / 2) (f : RealComplexL2) :
    ‖neutralWindowEvaluation a z f‖ ^ 2 ≤
      (2 * a * (Real.exp (a / 2)) ^ 2) * ‖f‖ ^ 2 := by
  rw [neutralWindowEvaluation_eq_inner]
  have hc := neutralExponentialColumnL2_sq_bound a ha (conj z) (by simpa using hz)
  have hi := pow_le_pow_left₀ (norm_nonneg _)
    (norm_inner_le_norm (𝕜 := ℂ) (neutralExponentialColumnL2 a (conj z)) f) 2
  rw [mul_pow] at hi
  exact hi.trans (mul_le_mul_of_nonneg_right hc (sq_nonneg _))

/-- Concrete raw sampling decay, derived from the constructed gradient. -/
theorem neutralActualZetaGreenSynthesis_window_sq_le (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) (q : NeutralActualZetaDivisorCoordinate)
    (hq : 1 ≤ |q.1.val.im|) :
    ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralActualZetaGreenSynthesis a v)‖ ^ 2 ≤
      (8 * a * (Real.exp (a / 2)) ^ 2 *
        ‖neutralActualZetaGradientSynthesis a v‖ ^ 2) *
          neutralActualZetaDivisorQuadraticWeight q := by
  let z := neutralActualZetaDivisorOrdinate q
  let h := |q.1.val.im|
  let b := ‖neutralWindowEvaluation a z (neutralActualZetaGreenSynthesis a v)‖
  let B := (2 * a * (Real.exp (a / 2)) ^ 2) *
    ‖neutralActualZetaGradientSynthesis a v‖ ^ 2
  have hh : 0 < h := lt_of_lt_of_le zero_lt_one hq
  have hid := congrArg norm (neutralActualZetaGreenSynthesis_windowDerivative a ha v z)
  simp only [norm_mul, Complex.norm_I, one_mul, norm_neg] at hid
  have hid2 := congrArg (fun x : ℝ => x ^ 2) hid
  rw [mul_pow] at hid2
  have hb := neutralWindowEvaluation_sq_bound a ha z
    (neutralActualZetaOrdinate_strictStrip q.1).le (neutralActualZetaGradientSynthesis a v)
  have hre : h ≤ ‖z‖ := by
    simpa [h, z, neutralActualZetaDivisorOrdinate, neutralActualZetaOrdinate_re] using
      Complex.abs_re_le_norm z
  have hmass : h ^ 2 * b ^ 2 ≤ B := by
    have hp := mul_le_mul_of_nonneg_right
      (pow_le_pow_left₀ (abs_nonneg q.1.val.im) hre 2) (sq_nonneg b)
    change h ^ 2 * b ^ 2 ≤ ‖z‖ ^ 2 * b ^ 2 at hp
    change ‖z‖ ^ 2 * b ^ 2 = _ at hid2
    exact hp.trans (hid2.le.trans hb)
  have hp : (1 + h) ^ 2 ≤ 4 * h ^ 2 := by
    have ht := pow_le_pow_left₀ (by positivity : 0 ≤ 1 + h)
      (by change 1 + h ≤ 2 * h; linarith only [hq]) 2
    nlinarith only [ht]
  have hm := mul_le_mul_of_nonneg_right hp (sq_nonneg b)
  have he : 8 * a * (Real.exp (a / 2)) ^ 2 *
      ‖neutralActualZetaGradientSynthesis a v‖ ^ 2 = 4 * B := by dsimp [B]; ring
  rw [he]
  change b ^ 2 ≤ (4 * B) * (1 / (1 + h) ^ 2)
  rw [mul_one_div]
  apply (le_div_iff₀ (by positivity : 0 < (1 + h) ^ 2)).2
  nlinarith only [hm, hmass]

/-- Unconditional full-divisor raw square sampling for the actual H¹ Green synthesis. -/
theorem neutralActualZetaGreenSynthesis_window_sq_summable (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a v)‖ ^ 2) := by
  apply Summable.of_norm_bounded_eventually
    (neutralActualZetaDivisorQuadraticWeight_summable.mul_left
      (8 * a * (Real.exp (a / 2)) ^ 2 * ‖neutralActualZetaGradientSynthesis a v‖ ^ 2))
  filter_upwards [(neutralActualZetaDivisorHeightWindow_finite 1).eventually_cofinite_notMem]
    with q hq
  have hh : 1 ≤ |q.1.val.im| := by
    change ¬ |q.1.val.im| ≤ 1 at hq
    exact (lt_of_not_ge hq).le
  rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg
    ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralActualZetaGreenSynthesis a v)‖)]
  exact neutralActualZetaGreenSynthesis_window_sq_le a ha v q hh

/-- Mixed raw evaluations of two actual Green syntheses converge absolutely. -/
theorem neutralActualZetaGreenSynthesis_window_mixed_summable (a : ℝ) (ha : 0 < a)
    (v w : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a v)) *
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a w)) := by
  apply Summable.of_norm_bounded
    ((neutralActualZetaGreenSynthesis_window_sq_summable a ha v).add
      (neutralActualZetaGreenSynthesis_window_sq_summable a ha w))
  intro q
  rw [norm_mul, Complex.norm_conj]
  nlinarith only [sq_nonneg
    (‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a v)‖ -
      ‖neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralActualZetaGreenSynthesis a w)‖)]

end
end WeilDefect
