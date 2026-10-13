import WeilDefect.Arithmetic.ActualZetaCorrelationTransform
import WeilDefect.Morphology.NeutralLogPoleSourceAttachment

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped InnerProduct ComplexConjugate

/-- Imaginary-axis raw sampling is exactly the retained real exponential moment. -/
theorem neutralWindowEvaluation_imaginary (a s : ℝ) (f : RealComplexL2) :
    neutralWindowEvaluation a (Complex.I * (s : ℂ)) f =
      sourceWindowMoment a (-s) f := by
  unfold neutralWindowEvaluation sourceWindowMoment
  apply integral_congr_ae
  filter_upwards [] with x
  have he : Complex.I * (Complex.I * (s : ℂ)) * (x : ℂ) =
      ((-s * x : ℝ) : ℂ) := by
    calc
      _ = (Complex.I * Complex.I) * (s : ℂ) * (x : ℂ) := by ring
      _ = _ := by rw [Complex.I_mul_I]; push_cast; ring
  rw [he, ← Complex.ofReal_exp]

/-- The imaginary-axis correlation transform has opposite moments in its two slots. -/
theorem neutralWindowCorrelation_imaginary (a s : ℝ) (f g : RealComplexL2) :
    neutralRawTransform (neutralWindowCorrelation a f g) (Complex.I * (s : ℂ)) =
      conj (sourceWindowMoment a s f) * sourceWindowMoment a (-s) g := by
  rw [neutralWindowCorrelation_rawTransform]
  have hc : conj (Complex.I * (s : ℂ)) = Complex.I * ((-s : ℝ) : ℂ) := by
    simp <;> ring
  rw [hc, neutralWindowEvaluation_imaginary, neutralWindowEvaluation_imaginary]
  simp only [neg_neg]

/-- The two explicit-formula poles give the Hermitian cross moments, with no square replacement. -/
theorem neutralWindowCorrelation_poleCrossTerms (a : ℝ) (f g : RealComplexL2) :
    neutralRawTransform (neutralWindowCorrelation a f g) (Complex.I * ((1/2 : ℝ) : ℂ)) +
      neutralRawTransform (neutralWindowCorrelation a f g) (Complex.I * ((-(1/2) : ℝ) : ℂ)) =
      conj (sourceWindowMoment a (-(1/2)) f) * sourceWindowMoment a (1/2) g +
      conj (sourceWindowMoment a (1/2) f) * sourceWindowMoment a (-(1/2)) g := by
  rw [neutralWindowCorrelation_imaginary, neutralWindowCorrelation_imaginary]
  simp only [neg_neg]
  exact add_comm _ _

/-- Exact pole operator attachment on the existing complete logarithmic carrier. -/
theorem neutralLogHilbertCorrelation_poleOperator (a : ℝ)
    (f g : NeutralLogHilbertCarrier a) :
    neutralRawTransform (neutralWindowCorrelation a
      (neutralLogPhysical f.val) (neutralLogPhysical g.val))
      (Complex.I * ((1/2 : ℝ) : ℂ)) +
      neutralRawTransform (neutralWindowCorrelation a
        (neutralLogPhysical f.val) (neutralLogPhysical g.val))
        (Complex.I * ((-(1/2) : ℝ) : ℂ)) =
      inner ℂ f (neutralLogPoleOperator a g) := by
  rw [neutralWindowCorrelation_poleCrossTerms, neutralLogPoleOperator_mixed]

/-- The diagonal pole sum is real, through the exact established cross-pole operator. -/
theorem neutralLogHilbertCorrelation_poleDiagonal (a : ℝ)
    (f : NeutralLogHilbertCarrier a) :
    neutralRawTransform (neutralWindowCorrelation a
      (neutralLogPhysical f.val) (neutralLogPhysical f.val))
      (Complex.I * ((1/2 : ℝ) : ℂ)) +
      neutralRawTransform (neutralWindowCorrelation a
        (neutralLogPhysical f.val) (neutralLogPhysical f.val))
        (Complex.I * ((-(1/2) : ℝ) : ℂ)) =
      ((2 * (conj (sourceWindowMoment a (-(1/2)) (neutralLogPhysical f.val)) *
        sourceWindowMoment a (1/2) (neutralLogPhysical f.val)).re : ℝ) : ℂ) := by
  rw [neutralLogHilbertCorrelation_poleOperator, neutralLogPoleOperator_diagonal]

/-- The constructed actual-divisor Green correlation attaches to the pole operator
on its exact canonical image. This does not identify a retained WD-T38 vector. -/
theorem neutralActualZetaGreenCorrelation_poleOperator
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralRawTransform (neutralWindowCorrelation a
      (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w))
      (Complex.I * ((1/2 : ℝ) : ℂ)) +
      neutralRawTransform (neutralWindowCorrelation a
        (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w))
        (Complex.I * ((-(1/2) : ℝ) : ℂ)) =
      inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
        (neutralLogPoleOperator a
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) := by
  simpa only [neutralActualZetaGreenCanonical_physical] using
    neutralLogHilbertCorrelation_poleOperator a
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))

end
end WeilDefect
