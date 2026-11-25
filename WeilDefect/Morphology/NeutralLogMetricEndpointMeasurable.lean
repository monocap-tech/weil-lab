import WeilDefect.Morphology.NeutralLogMetricJumpCap

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- Measurability of the moving endpoint tail, including totalized values.
Convergence at positive distances is a separate theorem. -/
theorem neutralLogMetricEndpointTail_measurable :
    Measurable neutralLogMetricEndpointTail := by
  have hm : Measurable
      (({p : ℝ × ℝ | p.1 < p.2}).indicator
        (fun p => neutralLogMetricJumpDensity p.2)) :=
    (neutralLogMetricJumpDensity_measurable.comp measurable_snd).indicator
      (measurableSet_lt measurable_fst measurable_snd)
  have hi := hm.stronglyMeasurable.integral_prod_right'
    (ν := (volume : Measure ℝ))
  have he : (fun d : ℝ => ∫ r : ℝ,
      ({p : ℝ × ℝ | p.1 < p.2}).indicator
        (fun p => neutralLogMetricJumpDensity p.2) (d, r)) =
      neutralLogMetricEndpointTail := by
    funext d
    change (∫ r : ℝ, (Ioi d).indicator neutralLogMetricJumpDensity r) =
      ∫ r in Ioi d, neutralLogMetricJumpDensity r
    exact integral_indicator measurableSet_Ioi
  rw [← he]
  exact hi.measurable

/-- Both moving exterior contributions are measurable. -/
theorem neutralLogMetricExteriorSource_measurable (B : ℝ) :
    Measurable (neutralLogMetricExteriorSource B) := by
  exact (neutralLogMetricEndpointTail_measurable.comp (by fun_prop)).add
    (neutralLogMetricEndpointTail_measurable.comp (by fun_prop))

/-- Measurability in the observation variable of the internal jump integral. -/
theorem neutralLogMetricJumpIntegral_measurable
    (B : ℝ) (v : ℝ → ℂ) (hv : Measurable v) :
    Measurable (fun x : ℝ => ∫ y in Icc (-B) B,
      (v x - v y) * (neutralLogMetricJumpDensity |x - y| : ℂ)) := by
  have hd : Measurable (fun p : ℝ × ℝ =>
      neutralLogMetricJumpDensity |p.1 - p.2|) :=
    neutralLogMetricJumpDensity_measurable.comp (by fun_prop)
  have hm : Measurable (fun p : ℝ × ℝ =>
      (v p.1 - v p.2) * (neutralLogMetricJumpDensity |p.1 - p.2| : ℂ)) :=
    ((hv.comp measurable_fst).sub (hv.comp measurable_snd)).mul
      (Complex.continuous_ofReal.measurable.comp hd)
  exact hm.stronglyMeasurable.integral_prod_right'.measurable

/-- The full endpoint candidate is measurable for every measurable trial.
This does not assert square integrability or spectral source identity. -/
theorem neutralLogMetricEndpointCandidate_measurable
    (B : ℝ) (v : ℝ → ℂ) (hv : Measurable v) :
    Measurable (neutralLogMetricEndpointCandidate B v) := by
  exact (hv.add (neutralLogMetricJumpIntegral_measurable B v hv)).add
    (hv.mul (Complex.continuous_ofReal.measurable.comp
      (neutralLogMetricExteriorSource_measurable B)))

end
end WeilDefect
