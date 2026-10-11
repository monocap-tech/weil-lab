import WeilDefect.Morphology.NeutralLogMetricPoissonConvolution
import WeilDefect.Morphology.NeutralLogMetricPoissonMixture

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped FourierTransform Convolution

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
      (lt_of_lt_of_le hε ht.1)).ofReal.const_mul
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)
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
  (neutralLogMetricTimeKernel_joint_integrable ε R hε).integral_prod_right

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
      dsimp only
      exact he.trans (congrArg
        (fun z : ℂ => ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) * z)
        (neutralLogMetricPoissonDensity_fourier t ξ htpos))


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
      dsimp only
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


/-- The actual finite time-integrated convolution is integrable over
 the whole line when the bounded trial is itself integrable. -/
theorem neutralLogMetricTimeConvolution_integrable
    (ε R M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    Integrable (fun x : ℝ => ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) := by
  let K : ℝ → ℂ := fun x => ∫ t in Icc ε R,
    ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (neutralLogMetricPoissonDensity t x : ℂ)
  have he : (fun x : ℝ => ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
      v ⋆[ContinuousLinearMap.mul ℂ ℂ] K := by
    funext x
    exact neutralLogMetricTimeConvolution_eq_kernel ε R x M hε hM v hv hbound
  rw [he]
  exact hvi.integrable_convolution (ContinuousLinearMap.mul ℂ ℂ)
    (neutralLogMetricTimeKernel_integrable ε R hε)

/-- Fourier transport of the actual finite integrated convolution,
 obtained from its proved kernel attachment and the kernel Fourier identity. -/
theorem neutralLogMetricTimeConvolution_fourier
    (ε R M ξ : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    (𝓕 (fun x : ℝ => ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) ξ =
      (𝓕 v) ξ * ∫ t in Icc ε R,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (Real.exp (-t * |ξ|) : ℂ) := by
  let K : ℝ → ℂ := fun x => ∫ t in Icc ε R,
    ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
      (neutralLogMetricPoissonDensity t x : ℂ)
  have he : (fun x : ℝ => ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
      v ⋆[ContinuousLinearMap.mul ℂ ℂ] K := by
    funext x
    exact neutralLogMetricTimeConvolution_eq_kernel ε R x M hε hM v hv hbound
  have hconv := Real.fourier_mul_convolution_eq hvi
    (neutralLogMetricTimeKernel_integrable ε R hε) ξ
  have hkernel := neutralLogMetricTimeKernel_fourier ε R ξ hε
  exact (congrArg (fun f : ℝ → ℂ => (𝓕 f) ξ) he).trans
    (hconv.trans (congrArg (fun z : ℂ => (𝓕 v) ξ * z) hkernel))

/-- Actual cap-bounded zero extensions satisfy the integrated Fourier
 identity without global integrability of the unextended trial. -/
theorem neutralLogMetricTimeConvolution_zeroExtension_fourier
    (B M ε R ξ : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M) :
    (𝓕 (fun x : ℝ => ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
          (neutralLogMetricPoissonDensity t (x - y) : ℂ))) ξ =
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ * ∫ t in Icc ε R,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (Real.exp (-t * |ξ|) : ℂ) := by
  exact neutralLogMetricTimeConvolution_fourier ε R M ξ hε hM _
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)


/-- The complex Laplace weight is integrable on every finite interval
 whose lower endpoint is positive. -/
theorem neutralLogMetricLaplaceWeight_integrableOn
    (ε R : ℝ) (hε : 0 < ε) :
    IntegrableOn (fun t : ℝ =>
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)) (Icc ε R) := by
  apply Measure.integrableOn_of_bounded
    (by simp : volume (Icc ε R) ≠ ⊤)
    (by fun_prop : Measurable (fun t : ℝ =>
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ))).aestronglyMeasurable
  filter_upwards [ae_restrict_mem measurableSet_Icc] with t ht
  simpa only [Complex.norm_real, Real.norm_eq_abs] using
    neutralLogMetricLaplaceWeight_truncated_bound ε R t hε ht

/-- The actual finite cancelled action splits into its scalar identity
 term and integrated convolution; subtraction is justified by time integrability. -/
theorem neutralLogMetricTimeAction_decomposition
    (ε R x M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hbound : ∀ y, ‖v y‖ ≤ M) :
    v x + (∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) =
    (1 + ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)) * v x -
      ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
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
  change v x + (∫ t in Icc ε R, w t * (v x - C t)) =
    (1 + ∫ t in Icc ε R, w t) * v x - ∫ t in Icc ε R, w t * C t
  simp_rw [mul_sub]
  rw [integral_sub (hw.mul_const (v x)) hc, integral_mul_const]
  ring

/-- The finite cancelled action is integrable over the full physical
 line, retaining the exterior convolution of the trial. -/
theorem neutralLogMetricTimeAction_integrable
    (ε R M : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    Integrable (fun x : ℝ => v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) := by
  have he : (fun x : ℝ => v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) =
      (fun x : ℝ =>
        (1 + ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)) * v x -
          ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) := by
    funext x
    exact neutralLogMetricTimeAction_decomposition ε R x M hε hM v hv hbound
  rw [he]
  exact (hvi.const_mul _).sub
    (neutralLogMetricTimeConvolution_integrable ε R M hε hM v hv hvi hbound)

/-- Cap-bounded measurable trials give genuinely integrable full-line
 finite cancelled actions through their actual zero extensions. -/
theorem neutralLogMetricTimeAction_zeroExtension_integrable
    (B M ε R : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M) :
    Integrable (fun x : ℝ => neutralLogMetricTrialZeroExtension B v x +
      ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (neutralLogMetricTrialZeroExtension B v x - ∫ y : ℝ,
          neutralLogMetricTrialZeroExtension B v y *
            (neutralLogMetricPoissonDensity t (x - y) : ℂ))) := by
  exact neutralLogMetricTimeAction_integrable ε R M hε hM _
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)


/-- The actual full-line finite cancelled action has the exact Fourier
 coefficient given by the scalar identity term minus the time-kernel multiplier. -/
theorem neutralLogMetricTimeAction_fourier
    (ε R M ξ : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v) (hvi : Integrable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    (𝓕 (fun x : ℝ => v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ =
      (𝓕 v) ξ * ((1 + ∫ t in Icc ε R,
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)) -
        ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (Real.exp (-t * |ξ|) : ℂ)) := by
  let w : ℝ → ℂ := fun t => ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)
  let c : ℂ := 1 + ∫ t in Icc ε R, w t
  let C : ℝ → ℂ := fun x => ∫ t in Icc ε R, w t *
    ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)
  have hC : Integrable C := neutralLogMetricTimeConvolution_integrable ε R M hε hM
    v hv hvi hbound
  have he : (fun x : ℝ => v x + ∫ t in Icc ε R, w t *
      (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ))) =
      (fun x : ℝ => c * v x - C x) := by
    funext x
    exact neutralLogMetricTimeAction_decomposition ε R x M hε hM v hv hbound
  have hs : (𝓕 (fun x : ℝ => c * v x - C x)) ξ =
      (𝓕 (fun x : ℝ => c * v x)) ξ - (𝓕 C) ξ := by
    rw [Real.fourier_eq, Real.fourier_eq, Real.fourier_eq]
    simp_rw [smul_sub]
    exact integral_sub ((Real.fourierIntegral_convergent_iff ξ).2 (hvi.const_mul c))
      ((Real.fourierIntegral_convergent_iff ξ).2 hC)
  have hscalar : (𝓕 (fun x : ℝ => c * v x)) ξ = c * (𝓕 v) ξ := by
    rw [Real.fourier_eq, Real.fourier_eq]
    simp only [Circle.smul_def, smul_eq_mul]
    rw [← integral_const_mul]
    apply integral_congr_ae
    filter_upwards [] with x
    ring
  have hconv : (𝓕 C) ξ = (𝓕 v) ξ *
      ∫ t in Icc ε R, w t * (Real.exp (-t * |ξ|) : ℂ) :=
    neutralLogMetricTimeConvolution_fourier ε R M ξ hε hM v hv hvi hbound
  change (𝓕 (fun x : ℝ => v x + ∫ t in Icc ε R, w t *
    (v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ =
    (𝓕 v) ξ * (c - ∫ t in Icc ε R, w t * (Real.exp (-t * |ξ|) : ℂ))
  calc
    _ = (𝓕 (fun x : ℝ => c * v x - C x)) ξ :=
      congrArg (fun f : ℝ → ℂ => (𝓕 f) ξ) he
    _ = (𝓕 (fun x : ℝ => c * v x)) ξ - (𝓕 C) ξ := hs
    _ = c * (𝓕 v) ξ - (𝓕 v) ξ *
        ∫ t in Icc ε R, w t * (Real.exp (-t * |ξ|) : ℂ) :=
      congrArg₂ (fun a b : ℂ => a - b) hscalar hconv
    _ = _ := by ring

/-- The finite-action Fourier identity applies to actual cap-bounded
 zero extensions without assumptions on the trial outside the cap. -/
theorem neutralLogMetricTimeAction_zeroExtension_fourier
    (B M ε R ξ : ℝ) (hε : 0 < ε) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M) :
    (𝓕 (fun x : ℝ => neutralLogMetricTrialZeroExtension B v x +
      ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (neutralLogMetricTrialZeroExtension B v x - ∫ y : ℝ,
          neutralLogMetricTrialZeroExtension B v y *
            (neutralLogMetricPoissonDensity t (x - y) : ℂ)))) ξ =
      (𝓕 (neutralLogMetricTrialZeroExtension B v)) ξ *
        ((1 + ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ)) -
          ∫ t in Icc ε R, ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (Real.exp (-t * |ξ|) : ℂ)) := by
  exact neutralLogMetricTimeAction_fourier ε R M ξ hε hM _
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_integrable B M v hv hbound)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)

end
end WeilDefect
