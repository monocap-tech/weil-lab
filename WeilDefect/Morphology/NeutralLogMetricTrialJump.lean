import WeilDefect.Morphology.NeutralLogMetricExteriorSplit
import WeilDefect.Morphology.NeutralLogMetricJumpCap
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- The trial, rather than its source candidate, extended by zero. -/
def neutralLogMetricTrialZeroExtension (B : ℝ) (v : ℝ → ℂ) : ℝ → ℂ :=
  (Icc (-B) B).indicator v

theorem neutralLogMetricTrialZeroExtension_measurable
    (B : ℝ) (v : ℝ → ℂ) (hv : Measurable v) :
    Measurable (neutralLogMetricTrialZeroExtension B v) :=
  hv.indicator measurableSet_Icc

theorem neutralLogMetricTrialZeroExtension_norm_le
    (B M : ℝ) (hM : 0 ≤ M) (v : ℝ → ℂ)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M) (y : ℝ) :
    ‖neutralLogMetricTrialZeroExtension B v y‖ ≤ M := by
  by_cases hy : y ∈ Icc (-B) B
  · simpa [neutralLogMetricTrialZeroExtension, hy] using hbound y hy
  · simpa [neutralLogMetricTrialZeroExtension, hy] using hM

/-- The actual full-line jump difference of a zero-extended trial. -/
def neutralLogMetricTrialJump (B : ℝ) (v : ℝ → ℂ) (x y : ℝ) : ℂ :=
  (v x - neutralLogMetricTrialZeroExtension B v y) *
    (neutralLogMetricJumpDensity |x - y| : ℂ)

/-- Exact pointwise partition, retaining both exterior half-lines. -/
theorem neutralLogMetricTrialJump_partition (B : ℝ) (hB : 0 ≤ B)
    (v : ℝ → ℂ) (x : ℝ) :
    neutralLogMetricTrialJump B v x =
      (fun y => (Icc (-B) B).indicator
        (fun z => (v x - v z) * (neutralLogMetricJumpDensity |x - z| : ℂ)) y +
        (Iio (-B)).indicator
          (fun z => v x * (neutralLogMetricJumpDensity |x - z| : ℂ)) y +
        (Ioi B).indicator
          (fun z => v x * (neutralLogMetricJumpDensity |x - z| : ℂ)) y) := by
  funext y
  by_cases hl : y < -B
  · have hc : y ∉ Icc (-B) B := fun h => (not_le_of_gt hl) h.1
    have hr : y ∉ Ioi B := by simp only [mem_Ioi]; linarith
    simp [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension, hl, hc, hr]
  · by_cases hr : B < y
    · have hc : y ∉ Icc (-B) B := fun h => (not_le_of_gt hr) h.2
      simp [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension,
        hl, hr, hc]
    · have hc : y ∈ Icc (-B) B := ⟨le_of_not_gt hl, le_of_not_gt hr⟩
      simp [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension,
        hl, hr, hc]

/-- Full-line spatial convergence follows from cancellation on the cap
and genuine convergence of both exterior tails. -/
theorem neutralLogMetricTrialJump_integrable
    (B x L : ℝ) (hB : 0 ≤ B) (hx : x ∈ Ioo (-B) B)
    (v : ℝ → ℂ) (hv : Measurable v) (hL : 0 ≤ L)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    Integrable (neutralLogMetricTrialJump B v x) := by
  have hi := (neutralLogMetricJumpDifference_integrableOn B x L v hv hL hmod).integrable_indicator measurableSet_Icc
  have hl0 : IntegrableOn (fun y : ℝ =>
      v x * (neutralLogMetricJumpDensity |x - y| : ℂ)) (Iio (-B)) :=
    (Complex.ofRealCLM.integrable_comp
      (neutralLogMetricJump_left_exterior_integrable B x hx.1)).const_mul (v x)
  have hl := hl0.integrable_indicator measurableSet_Iio
  have hr0 : IntegrableOn (fun y : ℝ =>
      v x * (neutralLogMetricJumpDensity |x - y| : ℂ)) (Ioi B) :=
    (Complex.ofRealCLM.integrable_comp
      (neutralLogMetricJump_right_exterior_integrable B x hx.2)).const_mul (v x)
  have hr := hr0.integrable_indicator measurableSet_Ioi
  rw [neutralLogMetricTrialJump_partition B hB v x]
  exact (hi.add hl).add hr

/-- The actual full-line complex jump integral equals the internal
cancelled integral plus the two endpoint tail terms. -/
theorem neutralLogMetricTrialJump_integral
    (B x L : ℝ) (hB : 0 ≤ B) (hx : x ∈ Ioo (-B) B)
    (v : ℝ → ℂ) (hv : Measurable v) (hL : 0 ≤ L)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    (∫ y, neutralLogMetricTrialJump B v x y) =
      (∫ y in Icc (-B) B,
        (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)) +
        v x * (neutralLogMetricExteriorSource B x : ℂ) := by
  have hi := (neutralLogMetricJumpDifference_integrableOn B x L v hv hL hmod).integrable_indicator measurableSet_Icc
  have hl0 : IntegrableOn (fun y : ℝ =>
      v x * (neutralLogMetricJumpDensity |x - y| : ℂ)) (Iio (-B)) :=
    (Complex.ofRealCLM.integrable_comp
      (neutralLogMetricJump_left_exterior_integrable B x hx.1)).const_mul (v x)
  have hl := hl0.integrable_indicator measurableSet_Iio
  have hr0 : IntegrableOn (fun y : ℝ =>
      v x * (neutralLogMetricJumpDensity |x - y| : ℂ)) (Ioi B) :=
    (Complex.ofRealCLM.integrable_comp
      (neutralLogMetricJump_right_exterior_integrable B x hx.2)).const_mul (v x)
  have hr := hr0.integrable_indicator measurableSet_Ioi
  rw [neutralLogMetricTrialJump_partition B hB v x]
  dsimp only
  have hsum := integral_add (hi.add hl) hr
  have hpair := integral_add hi hl
  simp only [Pi.add_apply] at hsum hpair
  rw [hsum, hpair, integral_indicator measurableSet_Icc, integral_indicator measurableSet_Iio,
    integral_indicator measurableSet_Ioi, integral_const_mul, integral_const_mul,
    integral_complex_ofReal, integral_complex_ofReal,
    neutralLogMetricJump_left_exterior_integral B x hx.1,
    neutralLogMetricJump_right_exterior_integral B x hx.2]
  simp only [neutralLogMetricExteriorSource, Complex.ofReal_add]
  ring

/-- The constructed endpoint candidate is the trial plus its genuine
full-line jump integral on the cap interior. This is not yet a Fourier identity. -/
theorem neutralLogMetricEndpointCandidate_eq_trial_jump
    (B x L : ℝ) (hB : 0 ≤ B) (hx : x ∈ Ioo (-B) B)
    (v : ℝ → ℂ) (hv : Measurable v) (hL : 0 ≤ L)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    neutralLogMetricEndpointCandidate B v x =
      v x + ∫ y, neutralLogMetricTrialJump B v x y := by
  rw [neutralLogMetricTrialJump_integral B x L hB hx v hv hL hmod]
  simp only [neutralLogMetricEndpointCandidate]
  ring

/-- Absolute spatial budget retaining both endpoint tails. This controls
 the integral of the norm, rather than only the norm of the integral. -/
theorem neutralLogMetricTrialJump_integral_norm_le
    (B x L M : ℝ) (hB : 0 ≤ B) (hx : x ∈ Ioo (-B) B)
    (hL : 0 ≤ L) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ‖v x‖ ≤ M)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    (∫ y : ℝ, ‖neutralLogMetricTrialJump B v x y‖) ≤
      2 * B * L + M * neutralLogMetricExteriorSource B x := by
  have hc0 : IntegrableOn (fun _ : ℝ => L) (Icc (-B) B) :=
    integrableOn_const (by simp : volume (Icc (-B) B) ≠ ⊤)
  have hc := hc0.integrable_indicator measurableSet_Icc
  have hl0 := (neutralLogMetricJump_left_exterior_integrable B x hx.1).const_mul M
  have hr0 := (neutralLogMetricJump_right_exterior_integrable B x hx.2).const_mul M
  have hl := hl0.integrable_indicator measurableSet_Iio
  have hr := hr0.integrable_indicator measurableSet_Ioi
  have hext (y : ℝ) :
      ‖v x * (neutralLogMetricJumpDensity |x - y| : ℂ)‖ ≤
        M * neutralLogMetricJumpDensity |x - y| := by
    rw [norm_mul, Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (neutralLogMetricJumpDensity_nonnegative _)]
    exact mul_le_mul_of_nonneg_right hbound
      (neutralLogMetricJumpDensity_nonnegative _)
  have hb : (∫ y : ℝ, ‖neutralLogMetricTrialJump B v x y‖) ≤
      ∫ y : ℝ, (Icc (-B) B).indicator (fun _ => L) y +
        (Iio (-B)).indicator
          (fun z => M * neutralLogMetricJumpDensity |x - z|) y +
        (Ioi B).indicator
          (fun z => M * neutralLogMetricJumpDensity |x - z|) y := by
    apply integral_mono_ae
      (neutralLogMetricTrialJump_integrable B x L hB hx v hv hL hmod).norm
      ((hc.add hl).add hr)
    apply Filter.Eventually.of_forall
    intro y
    by_cases hleft : y < -B
    · have hcap : y ∉ Icc (-B) B := fun h => (not_le_of_gt hleft) h.1
      have hright : y ∉ Ioi B := by simp only [mem_Ioi]; linarith
      simpa [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension,
        hleft, hcap, hright] using hext y
    · by_cases hright : B < y
      · have hcap : y ∉ Icc (-B) B := fun h => (not_le_of_gt hright) h.2
        simpa [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension,
          hleft, hright, hcap] using hext y
      · have hcap : y ∈ Icc (-B) B := ⟨le_of_not_gt hleft, le_of_not_gt hright⟩
        simpa [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension,
          hleft, hright, hcap] using
          neutralLogMetricJumpDifference_norm_le v L x y hL (hmod y hcap)
  have hsum := integral_add (hc.add hl) hr
  have hpair := integral_add hc hl
  simp only [Pi.add_apply] at hsum hpair
  calc
    _ ≤ _ := hb
    _ = 2 * B * L + M * neutralLogMetricExteriorSource B x := by
      rw [hsum, hpair, integral_indicator measurableSet_Icc,
        integral_indicator measurableSet_Iio, integral_indicator measurableSet_Ioi,
        integral_const_mul, integral_const_mul,
        neutralLogMetricJump_left_exterior_integral B x hx.1,
        neutralLogMetricJump_right_exterior_integral B x hx.2,
        setIntegral_const, Real.volume_real_Icc_of_le (by linarith : -B ≤ B)]
      simp only [smul_eq_mul, neutralLogMetricExteriorSource]
      ring

end
end WeilDefect
