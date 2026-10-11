import WeilDefect.Morphology.NeutralLogMetricTimeKernel
import WeilDefect.Morphology.NeutralLogMetricLaplaceCutoff

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology
open scoped FourierTransform

/-- The damped coefficient term is integrable on every finite
 positive-time interval, so its subtraction from the scalar term is legitimate. -/
theorem neutralLogMetricDampedCoefficient_integrableOn
    (ε R ξ : ℝ) (hε : 0 < ε) :
    IntegrableOn (fun t : ℝ =>
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (Real.exp (-t * |ξ|) : ℂ)) (Icc ε R) := by
  apply Measure.integrableOn_of_bounded
    (by simp : volume (Icc ε R) ≠ ⊤)
    (by fun_prop : Measurable (fun t : ℝ =>
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (Real.exp (-t * |ξ|) : ℂ))).aestronglyMeasurable
  filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
  have htpos : 0 < t := lt_of_lt_of_le hε ht.1
  have he : Real.exp (-t * |ξ|) ≤ 1 := by
    rw [← Real.exp_zero]
    apply Real.exp_le_exp.mpr
    nlinarith [mul_nonneg htpos.le (abs_nonneg ξ)]
  rw [norm_mul, Complex.norm_real, Complex.norm_real, Real.norm_eq_abs,
    Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
  calc
    _ ≤ (1 / ε) * 1 := mul_le_mul
      (neutralLogMetricLaplaceWeight_truncated_bound ε R t hε ht) he
      (Real.exp_pos _).le (by positivity)
    _ = _ := mul_one _

/-- Exact finite coefficient cancellation, using integrability of both
 terms rather than subtracting totalized improper integrals. -/
theorem neutralLogMetricTimeCoefficient_eq_cancelled
    (ε R ξ : ℝ) (hε : 0 < ε) :
    ((1 + ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)) -
      ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (Real.exp (-t * |ξ|) : ℂ)) =
    1 + ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (1 - (Real.exp (-t * |ξ|) : ℂ)) := by
  have he : (∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (1 - (Real.exp (-t * |ξ|) : ℂ))) =
      (∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)) -
        ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (Real.exp (-t * |ξ|) : ℂ) := by
    simp_rw [mul_sub, mul_one]
    exact integral_sub (neutralLogMetricLaplaceWeight_integrableOn ε R hε)
      (neutralLogMetricDampedCoefficient_integrableOn ε R ξ hε)
  rw [he]
  ring

/-- Fourier transforms of the actual full-line finite cutoff actions
 converge pointwise to the trial transform times the canonical logarithmic weight. -/
theorem neutralLogMetricTimeAction_fourier_natural_tendsto
    (M ξ : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ)
    (hv : Measurable v) (hvi : Integrable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    Tendsto (fun n : ℕ => (𝓕 (fun x : ℝ => v x +
      ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ)
      atTop (𝓝 ((𝓕 v) ξ * (logarithmicFourierWeight ξ : ℂ))) := by
  have he (n : ℕ) : (𝓕 (fun x : ℝ => v x +
      ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ =
      (𝓕 v) ξ * (1 +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (1 - (Real.exp (-t * |ξ|) : ℂ))) := by
    exact (neutralLogMetricTimeAction_fourier
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) M ξ (by positivity) hM v hv hvi hbound).trans
      (congrArg (fun z : ℂ => (𝓕 v) ξ * z)
        (neutralLogMetricTimeCoefficient_eq_cancelled
          (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) ξ (by positivity)))
  simp_rw [he]
  exact (tendsto_const_nhds : Tendsto (fun _ : ℕ => (𝓕 v) ξ) atTop (𝓝 ((𝓕 v) ξ))).mul
    (neutralLogMetricPoissonLaplaceCoefficient_tendsto ξ)

/-- The pointwise spectral limit applies to actual cap-bounded trial
 zero extensions, with no global conditions on the original trial. -/
theorem neutralLogMetricTimeAction_zeroExtension_fourier_natural_tendsto
    (B M ξ : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M) :
    Tendsto (fun n : ℕ => (𝓕 (fun x : ℝ => neutralLogMetricTrialZeroExtension B v x +
      ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (neutralLogMetricTrialZeroExtension B v x - ∫ y : ℝ,
            neutralLogMetricTrialZeroExtension B v y *
              (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ)
      atTop (𝓝 ((𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        (logarithmicFourierWeight ξ : ℂ))) := by
  exact neutralLogMetricTimeAction_fourier_natural_tendsto M ξ hM _
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)


/-- Every finite positive-time coefficient lies between one and the
 canonical logarithmic weight, independently of the cutoff. -/
theorem neutralLogMetricLaplaceCutoff_bounds
    (ε R ξ : ℝ) (hε : 0 < ε) :
    1 ≤ 1 + (∫ t in Icc ε R,
      neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t) ∧
    1 + (∫ t in Icc ε R,
      neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t) ≤ logarithmicFourierWeight ξ := by
  have hs : Icc ε R ⊆ Ioi (0 : ℝ) := fun t ht => lt_of_lt_of_le hε ht.1
  have hn : 0 ≤ ∫ t in Icc ε R,
      neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t := by
    apply integral_nonneg_of_ae
    filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    exact (neutralLogMetricLaplaceIntegrand_bounds _ _ _ (abs_nonneg ξ) (hs ht)).1
  have hi := neutralLogMetricLaplaceIntegrand_integrable
    (Real.exp 1) |ξ| (Real.exp_pos _) (abs_nonneg ξ)
  have hm : (∫ t in Icc ε R,
      neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t) ≤
      ∫ t in Ioi (0 : ℝ), neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t := by
    apply setIntegral_mono_set hi
    · filter_upwards [ae_restrict_mem measurableSet_Ioi] with t ht
      exact (neutralLogMetricLaplaceIntegrand_bounds _ _ _ (abs_nonneg ξ) ht).1
    · exact Filter.Eventually.of_forall hs
  have he := neutralLogMetricLaplace_weight |ξ| (abs_nonneg ξ)
  change logarithmicFourierWeight ξ = _ at he
  constructor <;> linarith

/-- The norm of the actual complex cancelled coefficient is bounded
 by the full logarithmic weight for every finite positive-time cutoff. -/
theorem neutralLogMetricCancelledCoefficient_norm_le
    (ε R ξ : ℝ) (hε : 0 < ε) :
    ‖(1 : ℂ) + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (1 - (Real.exp (-t * |ξ|) : ℂ))‖ ≤ logarithmicFourierWeight ξ := by
  have he (t : ℝ) :
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (1 - (Real.exp (-t * |ξ|) : ℂ)) =
      (neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t : ℂ) := by
    have ht : -t * |ξ| = -|ξ| * t := by ring
    rw [ht]
    unfold neutralLogMetricLaplaceIntegrand
    push_cast
    ring
  simp_rw [he, integral_complex_ofReal]
  have hb := neutralLogMetricLaplaceCutoff_bounds ε R ξ hε
  have hc : (1 : ℂ) +
      (∫ t in Icc ε R, neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t : ℝ) =
      ((1 + ∫ t in Icc ε R,
        neutralLogMetricLaplaceIntegrand (Real.exp 1) |ξ| t : ℝ) : ℂ) := by
    simp only [Complex.ofReal_add, Complex.ofReal_one]
  rw [hc, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (by linarith [hb.1])]
  exact hb.2

/-- The actual finite full-line action Fourier transform has a common
 pointwise spectral majorant, retaining the exact logarithmic weight. -/
theorem neutralLogMetricTimeAction_fourier_norm_le
    (ε R M ξ : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    ‖(𝓕 (fun x : ℝ => v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ‖ ≤
      ‖(𝓕 v) ξ‖ * logarithmicFourierWeight ξ := by
  have he := (neutralLogMetricTimeAction_fourier ε R M ξ hε hM v hv hvi hbound).trans
    (congrArg (fun z : ℂ => (𝓕 v) ξ * z)
      (neutralLogMetricTimeCoefficient_eq_cancelled ε R ξ hε))
  rw [he, norm_mul]
  exact mul_le_mul_of_nonneg_left
    (neutralLogMetricCancelledCoefficient_norm_le ε R ξ hε) (norm_nonneg _)

end
end WeilDefect
