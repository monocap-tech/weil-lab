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
  rw [integral_add (hi.add hl) hr, integral_add hi hl,
    integral_indicator measurableSet_Icc, integral_indicator measurableSet_Iio,
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

end
end WeilDefect
