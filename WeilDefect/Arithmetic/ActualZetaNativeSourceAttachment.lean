import WeilDefect.Arithmetic.ActualZetaNativeWeilForm
import WeilDefect.Arithmetic.ActualZetaSourceDecomposition

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped FourierTransform ComplexConjugate
set_option maxHeartbeats 800000

/-- Exact source quadratic on the constructed Green vector, with both
canonical-image pole moments expanded on that same physical vector. -/
theorem neutralActualZetaGreenZeroForm_source_quadratic
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenZeroForm a v v =
      (((∫ ξ : ℝ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) +
      2 * (conj (sourceWindowMoment a (-(1/2))
        (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a v)).re : ℝ) : ℂ) := by
  rw [neutralActualZetaGreenZeroForm_native_diagonal a ha v,
    neutralLogPoleOperator_diagonal, neutralActualZetaGreenCanonical_physical,
    Complex.ofReal_add]
  rfl

/-- Real quadratic attachment follows from the complex identity, without
a positivity or retained-mode membership premise. -/
theorem neutralActualZetaGreenZeroForm_source_quadratic_re
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    (neutralActualZetaGreenZeroForm a v v).re =
      (∫ ξ : ℝ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) +
      2 * (conj (sourceWindowMoment a (-(1/2))
        (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a v)).re := by
  rw [neutralActualZetaGreenZeroForm_source_quadratic a ha v]
  rfl

/-- The concrete convergent P/N source forms attach to the exact native mixed
Weil form on both unchanged constructed Green coefficient slots. -/
theorem neutralActualZetaGreenSourceForms_native_mixed
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenPositiveForm a ha v w -
      neutralActualZetaGreenNegativeForm a ha v w =
    2 * ((∫ ξ : ℝ,
      conj ((𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
          (𝓕 (neutralActualZetaGreenSynthesis a w) : RealComplexL2) ξ) +
      (conj (sourceWindowMoment a (-(1/2)) (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a w) +
       conj (sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (-(1/2)) (neutralActualZetaGreenSynthesis a w))) := by
  rw [← neutralActualZetaGreenZeroForm_source_decomposition a ha v w,
    neutralActualZetaGreenZeroForm_native_mixed a ha v w,
    neutralLogPoleOperator_mixed, neutralActualZetaGreenCanonical_physical,
    neutralActualZetaGreenCanonical_physical]

/-- Both full-divisor source energies converge and their real difference is
twice the existing signed source quadratic on the same physical Green vector. -/
theorem neutralActualZetaGreenSourceEnergy_native_quadratic
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2) -
    (∑' q : NeutralActualZetaDivisorCoordinate,
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2) =
    2 * ((∫ ξ : ℝ, rightLimitCompactWeilSymbolMathlib a ξ *
      ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) +
      2 * (conj (sourceWindowMoment a (-(1/2))
        (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a v)).re) := by
  rw [← neutralActualZetaGreenZeroForm_source_energy a ha v,
    neutralActualZetaGreenZeroForm_source_quadratic_re a ha v]

end
end WeilDefect
