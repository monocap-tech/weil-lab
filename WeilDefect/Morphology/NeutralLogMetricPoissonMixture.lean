import WeilDefect.Morphology.NeutralLogMetricPoissonAction
import Mathlib.MeasureTheory.Integral.Prod

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- Genuine joint convergence on a time interval bounded away from zero.
The weight is bounded only on that interval, and the spatial line is whole. -/
theorem neutralLogMetricPoissonMixture_integrable
    (ε R x M W : ℝ) (hε : 0 < ε) (hM : 0 ≤ M) (hW : 0 ≤ W)
    (w : ℝ → ℝ) (hw : Measurable w)
    (hwbound : ∀ t ∈ Icc ε R, |w t| ≤ W)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    Integrable (fun p : ℝ × ℝ => (w p.1 : ℂ) * (v x - v p.2) *
      (neutralLogMetricPoissonDensity p.1 (x - p.2) : ℂ))
      ((volume.restrict (Icc ε R)).prod volume) := by
  let f : ℝ × ℝ → ℂ := fun p => (w p.1 : ℂ) * (v x - v p.2) *
    (neutralLogMetricPoissonDensity p.1 (x - p.2) : ℂ)
  have hm : Measurable f := by
    dsimp [f]
    unfold neutralLogMetricPoissonDensity
    fun_prop
  apply (integrable_prod_iff hm.aestronglyMeasurable).mpr
  constructor
  · filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    have hd := neutralLogMetricPoissonDifference_integrable t x M
      (lt_of_lt_of_le hε ht.1) v hv hbound
    simpa only [f, mul_assoc] using hd.const_mul (w t : ℂ)
  · have hc : IntegrableOn (fun _ : ℝ => W * (2 * M)) (Icc ε R) :=
      integrableOn_const (by simp : volume (Icc ε R) ≠ ⊤)
    apply hc.mono' hm.stronglyMeasurable.norm.integral_prod_right'.aestronglyMeasurable
    filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    rw [Real.norm_eq_abs, abs_of_nonneg (integral_nonneg (fun y => norm_nonneg (f (t, y))))]
    have htpos : 0 < t := lt_of_lt_of_le hε ht.1
    have hd := (neutralLogMetricPoissonDifference_integrable t x M htpos v hv hbound).
      const_mul (w t : ℂ)
    have hk := neutralLogMetricPoissonDensity_shift_integrable t x htpos
    have hb : ∀ y : ℝ, ‖f (t, y)‖ ≤
        (W * (2 * M)) * neutralLogMetricPoissonDensity t (x - y) := by
      intro y
      have hvd : ‖v x - v y‖ ≤ 2 * M :=
        (norm_sub_le _ _).trans (by linarith [hbound x, hbound y])
      dsimp [f]
      rw [norm_mul, norm_mul, Complex.norm_real, Complex.norm_real,
        Real.norm_eq_abs, Real.norm_eq_abs,
        abs_of_pos (neutralLogMetricPoissonDensity_positive t (x - y) htpos)]
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul (hwbound t ht) hvd (norm_nonneg _) hW)
        (neutralLogMetricPoissonDensity_positive t (x - y) htpos).le
    have hi : (∫ y : ℝ, ‖f (t, y)‖) ≤
        ∫ y : ℝ, (W * (2 * M)) * neutralLogMetricPoissonDensity t (x - y) := by
      apply integral_mono (by simpa only [f, mul_assoc] using hd.norm)
        (hk.const_mul (W * (2 * M))) hb
    simpa only [integral_const_mul,
      neutralLogMetricPoissonDensity_shift_integral t x htpos, mul_one] using hi

/-- Fubini exchange is derived from the joint convergence certificate. -/
theorem neutralLogMetricPoissonMixture_swap
    (ε R x M W : ℝ) (hε : 0 < ε) (hM : 0 ≤ M) (hW : 0 ≤ W)
    (w : ℝ → ℝ) (hw : Measurable w)
    (hwbound : ∀ t ∈ Icc ε R, |w t| ≤ W)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    (∫ t in Icc ε R, ∫ y : ℝ, (w t : ℂ) * (v x - v y) *
      (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
    ∫ y : ℝ, ∫ t in Icc ε R, (w t : ℂ) * (v x - v y) *
      (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
  exact integral_integral_swap
    (neutralLogMetricPoissonMixture_integrable ε R x M W hε hM hW w hw hwbound v hv hbound)

/-- The actual logarithmic Laplace weight satisfies the truncated bound. -/
theorem neutralLogMetricLaplaceWeight_truncated_bound
    (ε R t : ℝ) (hε : 0 < ε) (ht : t ∈ Icc ε R) :
    |Real.exp (-(Real.exp 1) * t) / t| ≤ 1 / ε := by
  have htpos : 0 < t := lt_of_lt_of_le hε ht.1
  have he : Real.exp (-(Real.exp 1) * t) ≤ 1 := by
    calc
      Real.exp (-(Real.exp 1) * t) ≤ Real.exp 0 :=
        Real.exp_le_exp.mpr (by nlinarith [Real.exp_pos (1 : ℝ)])
      _ = 1 := Real.exp_zero
  rw [abs_of_pos (div_pos (Real.exp_pos _) htpos)]
  apply (div_le_iff₀ htpos).mpr
  have hlarge : 1 ≤ (1 / ε) * t := by
    rw [one_div, inv_mul_eq_div]
    exact (le_div_iff₀ hε).mpr (by simpa using ht.1)
  exact he.trans hlarge

/-- Exchange for the actual damped logarithmic mixture, without an
integrability premise or any passage through time zero. -/
theorem neutralLogMetricPoissonLaplaceMixture_swap
    (ε R x M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    (∫ t in Icc ε R, ∫ y : ℝ,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) * (v x - v y) *
        (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
    ∫ y : ℝ, ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) * (v x - v y) *
        (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
  exact neutralLogMetricPoissonMixture_swap ε R x M (1 / ε) hε hM (by positivity)
    (fun t => Real.exp (-(Real.exp 1) * t) / t) (by fun_prop)
    (fun t ht => neutralLogMetricLaplaceWeight_truncated_bound ε R t hε ht) v hv hbound

end
end WeilDefect
