import WeilDefect.Morphology.NeutralLogMetricTimeActionLimit

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- Positive-time Poisson convolution preserves the trial's uniform bound. -/
theorem neutralLogMetricPoissonConvolution_norm_le
    (t x M : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    ‖∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)‖ ≤ M := by
  have hi := neutralLogMetricPoissonProduct_integrable t x M ht v hv hbound
  have hk := neutralLogMetricPoissonDensity_shift_integrable t x ht
  have hb (y : ℝ) : ‖v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)‖ ≤
      M * neutralLogMetricPoissonDensity t (x - y) := by
    rw [norm_mul, Complex.norm_real, Real.norm_eq_abs,
      abs_of_pos (neutralLogMetricPoissonDensity_positive t (x - y) ht)]
    exact mul_le_mul_of_nonneg_right (hbound y)
      (neutralLogMetricPoissonDensity_positive t (x - y) ht).le
  have hle := integral_mono hi.norm (hk.const_mul M) hb
  have he : (∫ y : ℝ, M * neutralLogMetricPoissonDensity t (x - y)) = M := by
    rw [integral_const_mul, neutralLogMetricPoissonDensity_shift_integral t x ht, mul_one]
  exact (norm_integral_le_integral_norm _).trans (hle.trans_eq he)

/-- Every finite full-line cancelled action has a uniform physical
 bound. Unlike the spectral majorant, this needs no weighted-product domain premise. -/
theorem neutralLogMetricTimeAction_norm_le
    (ε R x M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    ‖v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))‖ ≤
      M + (∫ t in Icc ε R, |Real.exp (-(Real.exp 1) * t) / t|) * (2 * M) := by
  let w : ℝ → ℂ := fun t => ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)
  let C : ℝ → ℂ := fun t => ∫ y : ℝ,
    v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)
  have hw : IntegrableOn w (Icc ε R) := neutralLogMetricLaplaceWeight_integrableOn ε R hε
  have hc : IntegrableOn (fun t => w t * C t) (Icc ε R) := by
    apply (neutralLogMetricTimeConvolution_joint_integrable ε R x M hε hM
      v hv hbound).integral_prod_left.congr
    filter_upwards [] with t
    change (∫ y : ℝ, w t * v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
      w t * ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)
    simp_rw [mul_assoc]
    exact integral_const_mul _ _
  have hi : IntegrableOn (fun t => w t * (v x - C t)) (Icc ε R) := by
    simpa only [mul_sub, Pi.sub_apply] using (hw.mul_const (v x)).sub hc
  have hb : ∀ᵐ t ∂(volume.restrict (Icc ε R)),
      ‖w t * (v x - C t)‖ ≤ ‖w t‖ * (2 * M) := by
    filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    have hp : ‖C t‖ ≤ M := neutralLogMetricPoissonConvolution_norm_le
      t x M (lt_of_lt_of_le hε ht.1) v hv hbound
    have hd : ‖v x - C t‖ ≤ 2 * M :=
      (norm_sub_le _ _).trans (by linarith [hbound x])
    rw [norm_mul]
    exact mul_le_mul_of_nonneg_left hd (norm_nonneg _)
  have hle := integral_mono_ae hi.norm (hw.norm.mul_const (2 * M)) hb
  rw [integral_mul_const] at hle
  have hn : ‖∫ t in Icc ε R, w t * (v x - C t)‖ ≤
      (∫ t in Icc ε R, ‖w t‖) * (2 * M) :=
    (norm_integral_le_integral_norm _).trans hle
  have hsum := (norm_add_le (v x) (∫ t in Icc ε R, w t * (v x - C t))).trans
    (add_le_add (hbound x) hn)
  simpa only [w, Complex.norm_real, Real.norm_eq_abs] using hsum


/-- Every actual full-line finite action is in physical L2. Squared
 norms are dominated by the uniform bound times the proved integrable norm. -/
theorem neutralLogMetricTimeAction_memLp_two
    (ε R M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    MemLp (fun x : ℝ => v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) 2 volume := by
  let A : ℝ → ℂ := fun x => v x + ∫ t in Icc ε R,
    ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))
  let C : ℝ := M + (∫ t in Icc ε R, |Real.exp (-(Real.exp 1) * t) / t|) * (2 * M)
  have hA : Integrable A := neutralLogMetricTimeAction_integrable ε R M hε hM v hv hvi hbound
  have hb (x : ℝ) : ‖A x‖ ≤ C := neutralLogMetricTimeAction_norm_le ε R x M hε hM v hv hbound
  apply (memLp_two_iff_integrable_sq_norm hA.aestronglyMeasurable).mpr
  simp_rw [pow_two]
  apply (hA.norm.const_mul C).mono'
    (hA.aestronglyMeasurable.norm.mul hA.aestronglyMeasurable.norm)
  filter_upwards [] with x
  change ‖‖A x‖ * ‖A x‖‖ ≤ C * ‖A x‖
  rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (norm_nonneg _) (norm_nonneg _))]
  exact mul_le_mul_of_nonneg_right (hb x) (norm_nonneg _)

/-- Cap-bounded measurable trials give full-line finite actions in L2,
 including their exterior component, without any spectral-domain premise. -/
theorem neutralLogMetricTimeAction_zeroExtension_memLp_two
    (B M ε R : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M) :
    MemLp (fun x : ℝ => neutralLogMetricTrialZeroExtension B v x +
      ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (neutralLogMetricTrialZeroExtension B v x - ∫ y : ℝ,
          neutralLogMetricTrialZeroExtension B v y *
            (neutralLogMetricPoissonDensity t (x - y) : ℂ))) 2 volume := by
  exact neutralLogMetricTimeAction_memLp_two ε R M hε hM _
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)

/-- The actual full-line finite action has integrable pairings against
 every physical L2 test, with no spectral-domain assumption. -/
theorem neutralLogMetricTimeAction_integrable_inner
    (ε R M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) (φ : RealComplexL2) :
    Integrable (fun x : ℝ => inner ℂ
      (v x + ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) (φ x)) := by
  let A : ℝ → ℂ := fun x => v x + ∫ t in Icc ε R,
    ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))
  have hA : MemLp A 2 volume := neutralLogMetricTimeAction_memLp_two ε R M hε hM
    v hv hvi hbound
  apply (L2.integrable_inner (𝕜 := ℂ) (hA.toLp A) φ).congr
  filter_upwards [hA.coeFn_toLp] with x hx
  rw [hx]

end
end WeilDefect
