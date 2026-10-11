import WeilDefect.Morphology.NeutralLogMetricPoissonMixture

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- The genuine metric jump kernel with a finite positive time cutoff. -/
def neutralLogMetricTruncatedJumpDensity (ε R r : ℝ) : ℝ :=
  2 * ∫ t in Icc ε R,
    Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)

/-- Exact cancellation of the Laplace 1/t factor with the Poisson numerator. -/
theorem neutralLogMetricPoissonLaplace_product (t r : ℝ) (ht : 0 < t) :
    (Real.exp (-(Real.exp 1) * t) / t) * neutralLogMetricPoissonDensity t r =
      2 * (Real.exp (-(Real.exp 1) * t) /
        (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)) := by
  unfold neutralLogMetricPoissonDensity
  have hd : t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2 ≠ 0 := by
    have hh : 0 ≤ 4 * Real.pi ^ 2 * r ^ 2 := by positivity
    nlinarith [sq_pos_of_pos ht]
  field_simp [ne_of_gt ht, hd] <;> ring

/-- The truncated spatial kernel is exactly the positive-time Poisson mixture. -/
theorem neutralLogMetricTruncatedJumpDensity_eq_mixture
    (ε R r : ℝ) (hε : 0 < ε) :
    (∫ t in Icc ε R, (Real.exp (-(Real.exp 1) * t) / t) *
      neutralLogMetricPoissonDensity t r) =
      neutralLogMetricTruncatedJumpDensity ε R r := by
  calc
    (∫ t in Icc ε R, (Real.exp (-(Real.exp 1) * t) / t) *
      neutralLogMetricPoissonDensity t r) =
        ∫ t in Icc ε R, 2 * (Real.exp (-(Real.exp 1) * t) /
          (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)) := by
      apply setIntegral_congr_fun measurableSet_Icc
      intro t ht
      exact neutralLogMetricPoissonLaplace_product t r (lt_of_lt_of_le hε ht.1)
    _ = neutralLogMetricTruncatedJumpDensity ε R r := by
      rw [integral_const_mul]
      rfl

/-- The inner complex mixture has the actual truncated jump density. -/
theorem neutralLogMetricTruncatedJump_inner
    (ε R x y : ℝ) (hε : 0 < ε) (v : ℝ → ℂ) :
    (∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (v x - v y) * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
      (v x - v y) * (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ) := by
  have he : (fun t : ℝ => ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (v x - v y) * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
      (fun t : ℝ => (v x - v y) *
        (((Real.exp (-(Real.exp 1) * t) / t) *
          neutralLogMetricPoissonDensity t (x - y) : ℝ) : ℂ)) := by
    funext t
    push_cast
    ring
  rw [he, integral_const_mul, integral_complex_ofReal,
    neutralLogMetricTruncatedJumpDensity_eq_mixture ε R (x - y) hε]

/-- The identified spatial jump integral genuinely converges, by joint
mixture convergence rather than the totalized integral convention. -/
theorem neutralLogMetricTruncatedJump_integrable
    (ε R x M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    Integrable (fun y : ℝ => (v x - v y) *
      (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)) := by
  have hj := neutralLogMetricPoissonMixture_integrable ε R x M (1 / ε)
    hε hM (by positivity) (fun t => Real.exp (-(Real.exp 1) * t) / t)
    (by fun_prop)
    (fun t ht => neutralLogMetricLaplaceWeight_truncated_bound ε R t hε ht) v hv hbound
  exact hj.integral_prod_right.congr (Filter.Eventually.of_forall
    (fun y => neutralLogMetricTruncatedJump_inner ε R x y hε v))

/-- Actual truncated physical attachment: identity-minus-Poisson mixture
equals the spatial cancelled jump integral. No Fourier identity is assumed. -/
theorem neutralLogMetricTruncatedJump_action
    (ε R x M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    (∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) =
      ∫ y : ℝ, (v x - v y) *
        (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ) := by
  calc
    _ = ∫ t in Icc ε R, ∫ y : ℝ,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) * (v x - v y) *
          (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
      apply setIntegral_congr_fun measurableSet_Icc
      intro t ht
      rw [← neutralLogMetricPoissonDifference_integral t x M
        (lt_of_lt_of_le hε ht.1) v hv hbound]
      rw [← integral_const_mul]
      apply integral_congr_ae
      exact Filter.Eventually.of_forall (fun y => (mul_assoc _ _ _).symm)
    _ = ∫ y : ℝ, ∫ t in Icc ε R,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) * (v x - v y) *
          (neutralLogMetricPoissonDensity t (x - y) : ℂ) :=
      neutralLogMetricPoissonLaplaceMixture_swap ε R x M hε hM v hv hbound
    _ = _ := integral_congr_ae (Filter.Eventually.of_forall
      (fun y => neutralLogMetricTruncatedJump_inner ε R x y hε v))

end
end WeilDefect
