import WeilDefect.Morphology.NeutralLogMetricPoissonMass
import WeilDefect.Morphology.NeutralLogMetricTrialJump
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- Reflection and translation preserve the genuine Poisson kernel's L1 mass. -/
theorem neutralLogMetricPoissonDensity_shift_integrable
    (t x : ℝ) (ht : 0 < t) :
    Integrable (fun y : ℝ => neutralLogMetricPoissonDensity t (x - y)) := by
  have hp : MeasurePreserving (fun y : ℝ => x - y) volume volume := by
    simpa [Function.comp_def, sub_eq_add_neg] using
      (measurePreserving_add_left (volume : Measure ℝ) x).comp
        (Measure.measurePreserving_neg (volume : Measure ℝ))
  exact hp.integrable_comp_of_integrable (neutralLogMetricPoissonDensity_integrable t ht)

/-- The translated reflected physical kernel still has exact unit mass. -/
theorem neutralLogMetricPoissonDensity_shift_integral
    (t x : ℝ) (ht : 0 < t) :
    (∫ y : ℝ, neutralLogMetricPoissonDensity t (x - y)) = 1 := by
  have hp : MeasurePreserving (fun y : ℝ => x - y) volume volume := by
    simpa [Function.comp_def, sub_eq_add_neg] using
      (measurePreserving_add_left (volume : Measure ℝ) x).comp
        (Measure.measurePreserving_neg (volume : Measure ℝ))
  have hm : MeasurableEmbedding (fun y : ℝ => x - y) := by
    simpa [Function.comp_def, sub_eq_add_neg] using
      (MeasurableEquiv.addLeft x).measurableEmbedding.comp
        (MeasurableEquiv.neg ℝ).measurableEmbedding
  have he := hp.setIntegral_preimage_emb hm
    (neutralLogMetricPoissonDensity t) univ
  have he' : (∫ y : ℝ, neutralLogMetricPoissonDensity t (x - y)) =
      ∫ y : ℝ, neutralLogMetricPoissonDensity t y := by simpa using he
  rw [he', neutralLogMetricPoissonDensity_integral t ht]

/-- Bounded measurable trials have a genuinely convergent physical
Poisson convolution at every positive time and every spatial point. -/
theorem neutralLogMetricPoissonProduct_integrable
    (t x M : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    Integrable (fun y : ℝ => v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) := by
  exact (neutralLogMetricPoissonDensity_shift_integrable t x ht).ofReal.bdd_mul
    hv.aestronglyMeasurable (Filter.Eventually.of_forall hbound)

/-- The cancelled positive-time Poisson difference is integrable before
any Laplace-time integration or limit is taken. -/
theorem neutralLogMetricPoissonDifference_integrable
    (t x M : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    Integrable (fun y : ℝ =>
      (v x - v y) * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) := by
  have hc := (neutralLogMetricPoissonDensity_shift_integrable t x ht).ofReal.const_mul (v x)
  have hvp := neutralLogMetricPoissonProduct_integrable t x M ht v hv hbound
  simpa only [sub_mul] using hc.sub hvp

/-- Exact positive-time action: the cancelled integral is identity minus
Poisson convolution, with genuine convergence proved above. -/
theorem neutralLogMetricPoissonDifference_integral
    (t x M : ℝ) (ht : 0 < t) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y, ‖v y‖ ≤ M) :
    (∫ y : ℝ, (v x - v y) * (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
      v x - ∫ y : ℝ, v y * (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
  have hc := (neutralLogMetricPoissonDensity_shift_integrable t x ht).ofReal.const_mul (v x)
  have hvp := neutralLogMetricPoissonProduct_integrable t x M ht v hv hbound
  simp_rw [sub_mul]
  rw [integral_sub hc hvp, integral_const_mul, integral_complex_ofReal,
    neutralLogMetricPoissonDensity_shift_integral t x ht]
  simp

/-- The positive-time action applies to cap-bounded trials through their
actual zero extension; no global bound on the original trial is required. -/
theorem neutralLogMetricPoissonDifference_zeroExtension_integral
    (B t x M : ℝ) (ht : 0 < t) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M) :
    (∫ y : ℝ,
      (neutralLogMetricTrialZeroExtension B v x - neutralLogMetricTrialZeroExtension B v y) *
        (neutralLogMetricPoissonDensity t (x - y) : ℂ)) =
      neutralLogMetricTrialZeroExtension B v x - ∫ y : ℝ,
        neutralLogMetricTrialZeroExtension B v y *
          (neutralLogMetricPoissonDensity t (x - y) : ℂ) := by
  exact neutralLogMetricPoissonDifference_integral t x M ht _
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)

end
end WeilDefect
