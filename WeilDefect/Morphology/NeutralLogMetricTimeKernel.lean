import WeilDefect.Morphology.NeutralLogMetricPoissonConvolution
import WeilDefect.Morphology.NeutralLogMetricPoissonMixture

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped FourierTransform

/-- The finite Laplace mixture kernel is jointly integrable in time
 and the whole physical line, before taking its Fourier transform. -/
theorem neutralLogMetricTimeKernel_joint_integrable
    (ε R : ℝ) (hε : 0 < ε) :
    Integrable (fun p : ℝ × ℝ =>
      ((Real.exp (-(Real.exp 1) * p.1) / p.1 : ℝ) : ℂ) *
        (neutralLogMetricPoissonDensity p.1 p.2 : ℂ))
      ((volume.restrict (Icc ε R)).prod volume) := by
  let F : ℝ × ℝ → ℂ := fun p =>
    ((Real.exp (-(Real.exp 1) * p.1) / p.1 : ℝ) : ℂ) *
      (neutralLogMetricPoissonDensity p.1 p.2 : ℂ)
  have hm : Measurable F := by
    dsimp [F]
    unfold neutralLogMetricPoissonDensity
    fun_prop
  apply (integrable_prod_iff hm.aestronglyMeasurable).mpr
  constructor
  · filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    exact (neutralLogMetricPoissonDensity_integrable t
      (lt_of_lt_of_le hε ht.1)).ofReal.const_mul _
  · have hc : IntegrableOn (fun _ : ℝ => 1 / ε) (Icc ε R) :=
      integrableOn_const (by simp : volume (Icc ε R) ≠ ⊤)
    apply hc.mono' hm.stronglyMeasurable.norm.integral_prod_right'.aestronglyMeasurable
    filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    have htpos : 0 < t := lt_of_lt_of_le hε ht.1
    have he : (fun x : ℝ => ‖F (t, x)‖) =
        (fun x : ℝ => |Real.exp (-(Real.exp 1) * t) / t| *
          neutralLogMetricPoissonDensity t x) := by
      funext x
      simp only [F, norm_mul, Complex.norm_real, Real.norm_eq_abs,
        abs_of_pos (neutralLogMetricPoissonDensity_positive t x htpos)]
    rw [Real.norm_eq_abs, abs_of_nonneg (integral_nonneg (fun x => norm_nonneg (F (t, x)))),
      he, integral_const_mul, neutralLogMetricPoissonDensity_integral t htpos, mul_one]
    exact neutralLogMetricLaplaceWeight_truncated_bound ε R t hε ht

/-- The actual finite time mixture kernel is integrable on the whole line. -/
theorem neutralLogMetricTimeKernel_integrable (ε R : ℝ) (hε : 0 < ε) :
    Integrable (fun x : ℝ => ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (neutralLogMetricPoissonDensity t x : ℂ)) :=
  (neutralLogMetricTimeKernel_joint_integrable ε R hε).integral_prod_left

/-- Fourier transformation commutes with the finite time kernel mixture,
 by the proved joint integrability and unit modulus of the Fourier character. -/
theorem neutralLogMetricTimeKernel_fourier
    (ε R ξ : ℝ) (hε : 0 < ε) :
    (𝓕 (fun x : ℝ => ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (neutralLogMetricPoissonDensity t x : ℂ))) ξ =
      ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (Real.exp (-t * |ξ|) : ℂ) := by
  let F : ℝ × ℝ → ℂ := fun p =>
    ((Real.exp (-(Real.exp 1) * p.1) / p.1 : ℝ) : ℂ) *
      (neutralLogMetricPoissonDensity p.1 p.2 : ℂ)
  have hF : Integrable F ((volume.restrict (Icc ε R)).prod volume) :=
    neutralLogMetricTimeKernel_joint_integrable ε R hε
  have hs : Integrable (fun p : ℝ × ℝ =>
      Real.fourierChar (-inner ℝ p.2 ξ) • F p)
      ((volume.restrict (Icc ε R)).prod volume) := by
    apply hF.mono
    · exact (Real.continuous_fourierChar.comp (by fun_prop)).aestronglyMeasurable.smul
        hF.aestronglyMeasurable
    · filter_upwards [] with p
      simp
  rw [Real.fourier_eq]
  change (∫ x : ℝ, Real.fourierChar (-inner ℝ x ξ) • ∫ t in Icc ε R, F (t, x)) = _
  calc
    _ = ∫ x : ℝ, ∫ t in Icc ε R,
        Real.fourierChar (-inner ℝ x ξ) • F (t, x) := by
      congr 1
      funext x
      simp only [Circle.smul_def, integral_smul]
    _ = ∫ t in Icc ε R, ∫ x : ℝ,
        Real.fourierChar (-inner ℝ x ξ) • F (t, x) :=
      (integral_integral_swap hs).symm
    _ = _ := by
      apply setIntegral_congr_fun measurableSet_Icc
      intro t ht
      have htpos : 0 < t := lt_of_lt_of_le hε ht.1
      have he : (∫ x : ℝ, Real.fourierChar (-inner ℝ x ξ) • F (t, x)) =
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (𝓕 (fun x : ℝ => (neutralLogMetricPoissonDensity t x : ℂ))) ξ := by
        rw [Real.fourier_eq]
        simp only [F, Circle.smul_def, smul_eq_mul]
        rw [← integral_const_mul]
        apply integral_congr_ae
        filter_upwards [] with x
        ring
      rw [he, neutralLogMetricPoissonDensity_fourier t ξ htpos]


/-- Joint convergence of the finite weighted convolution at every
 spatial point, for a bounded measurable trial. -/
theorem neutralLogMetricTimeConvolution_joint_integrable
    (ε R x M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    Integrable (fun p : ℝ × ℝ =>
      ((Real.exp (-(Real.exp 1) * p.1) / p.1 : ℝ) : ℂ) * v p.2 *
        (neutralLogMetricPoissonDensity p.1 (x - p.2) : ℂ))
      ((volume.restrict (Icc ε R)).prod volume) := by
  let F : ℝ × ℝ → ℂ := fun p =>
    ((Real.exp (-(Real.exp 1) * p.1) / p.1 : ℝ) : ℂ) * v p.2 *
      (neutralLogMetricPoissonDensity p.1 (x - p.2) : ℂ)
  have hm : Measurable F := by
    dsimp [F]
    unfold neutralLogMetricPoissonDensity
    fun_prop
  apply (integrable_prod_iff hm.aestronglyMeasurable).mpr
  constructor
  · filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    have hi := (neutralLogMetricPoissonProduct_integrable t x M
      (lt_of_lt_of_le hε ht.1) v hv hbound).const_mul
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)
    simpa only [F, mul_assoc] using hi
  · have hc : IntegrableOn (fun _ : ℝ => (1 / ε) * M) (Icc ε R) :=
      integrableOn_const (by simp : volume (Icc ε R) ≠ ⊤)
    apply hc.mono' hm.stronglyMeasurable.norm.integral_prod_right'.aestronglyMeasurable
    filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
    have htpos : 0 < t := lt_of_lt_of_le hε ht.1
    have hi := (neutralLogMetricPoissonProduct_integrable t x M htpos v hv hbound).const_mul
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)
    have hk := neutralLogMetricPoissonDensity_shift_integrable t x htpos
    have hb (y : ℝ) : ‖F (t, y)‖ ≤
        ((1 / ε) * M) * neutralLogMetricPoissonDensity t (x - y) := by
      dsimp [F]
      rw [norm_mul, norm_mul, Complex.norm_real, Complex.norm_real,
        Real.norm_eq_abs, Real.norm_eq_abs,
        abs_of_pos (neutralLogMetricPoissonDensity_positive t (x - y) htpos)]
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul (neutralLogMetricLaplaceWeight_truncated_bound ε R t hε ht)
          (hbound y) (norm_nonneg _) (by positivity))
        (neutralLogMetricPoissonDensity_positive t (x - y) htpos).le
    rw [Real.norm_eq_abs, abs_of_nonneg (integral_nonneg (fun y => norm_nonneg (F (t, y))))]
    have hle := integral_mono (by simpa only [F, mul_assoc] using hi.norm)
      (hk.const_mul ((1 / ε) * M)) hb
    simpa only [integral_const_mul,
      neutralLogMetricPoissonDensity_shift_integral t x htpos, mul_one] using hle

/-- The actual time-integrated Poisson convolution is convolution by
 the finite mixture kernel, with the exchange derived from joint convergence. -/
theorem neutralLogMetricTimeConvolution_eq_kernel
    (ε R x M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    (∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
    ∫ y : ℝ, v y * ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
  calc
    _ = ∫ t in Icc ε R, ∫ y : ℝ,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) * v y *
          (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
      apply setIntegral_congr_fun measurableSet_Icc
      intro t ht
      rw [← integral_const_mul]
      apply integral_congr_ae
      filter_upwards [] with y
      ring
    _ = ∫ y : ℝ, ∫ t in Icc ε R,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) * v y *
          (neutralLogMetricPoissonDensity t (x - y) : ℂ) :=
      integral_integral_swap
        (neutralLogMetricTimeConvolution_joint_integrable ε R x M hε hM v hv hbound)
    _ = _ := by
      apply integral_congr_ae
      filter_upwards [] with y
      rw [← integral_const_mul]
      apply integral_congr_ae
      filter_upwards [] with t
      ring

end
end WeilDefect
