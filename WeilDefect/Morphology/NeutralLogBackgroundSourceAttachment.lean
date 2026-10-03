import WeilDefect.Morphology.NeutralLogSelectedSourceAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap
open scoped InnerProduct ComplexConjugate FourierTransform BigOperators

/-- Actual finite selected negative energy. Repeated indices represent
duplicate coefficient channels; no multiplicity quotient is assumed. -/
def neutralLogFiniteSelectedOperator {ι : Type*} [Fintype ι]
    (a : ℝ) (z : ι → ℂ) :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  ∑ i, neutralLogSelectedPairOperator a (z i)

theorem neutralLogFiniteSelectedOperator_mixed {ι : Type*} [Fintype ι]
    (a : ℝ) (z : ι → ℂ) (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogFiniteSelectedOperator a z g) =
      ∑ i, conj (inner ℂ (neutralLogNegativePairSource a (z i)) f) *
        inner ℂ (neutralLogNegativePairSource a (z i)) g := by
  classical
  simp only [neutralLogFiniteSelectedOperator, _root_.sum_apply,
    _root_.inner_sum, neutralLogSelectedPairOperator_mixed]

theorem neutralLogFiniteSelectedOperator_diagonal {ι : Type*} [Fintype ι]
    (a : ℝ) (z : ι → ℂ) (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogFiniteSelectedOperator a z f) =
      ((∑ i, ‖inner ℂ (neutralLogNegativePairSource a (z i)) f‖ ^ 2 : ℝ) : ℂ) := by
  classical
  simp only [neutralLogFiniteSelectedOperator, _root_.sum_apply,
    _root_.inner_sum, neutralLogSelectedPairOperator_diagonal, Complex.ofReal_sum]

theorem neutralLogFiniteSelectedOperator_nonnegative {ι : Type*} [Fintype ι]
    (a : ℝ) (z : ι → ℂ) (f : NeutralLogHilbertCarrier a) :
    0 ≤ (inner ℂ f (neutralLogFiniteSelectedOperator a z f)).re := by
  rw [neutralLogFiniteSelectedOperator_diagonal, Complex.ofReal_re]
  exact Finset.sum_nonneg (fun i _ => sq_nonneg _)

theorem neutralLogFiniteSelectedOperator_conjugate {ι : Type*} [Fintype ι]
    (a : ℝ) (z : ι → ℂ) :
    neutralLogFiniteSelectedOperator a (fun i => conj (z i)) =
      neutralLogFiniteSelectedOperator a z := by
  simp only [neutralLogFiniteSelectedOperator, neutralLogSelectedPairOperator_conjugate]

variable {ι : Type*} [Fintype ι]
  (a : ℝ) (ha : RightLimitWeilSymbolTemperatePremise a)
  (lowerC upperC shift : ℝ) (h0 : 0 ≤ lowerC)
  (hl : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
    rightLimitCompactWeilSymbolMathlib a ξ + shift)
  (hu : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
    upperC * logarithmicFourierWeight ξ)
  (z : ι → ℂ)

/-- Concrete effective-background expression: actual full arithmetic form
plus actual finite selected negative energy on the same complete carrier.
Strict positivity and identification with WD-T38's P are not assumed here. -/
def neutralLogBackgroundOperator :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu +
    neutralLogFiniteSelectedOperator a z

theorem neutralLogBackgroundOperator_mixed (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogBackgroundOperator a ha lowerC upperC shift h0 hl hu z g) =
      inner ℂ f (neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu g) +
      ∑ i, conj (inner ℂ (neutralLogNegativePairSource a (z i)) f) *
        inner ℂ (neutralLogNegativePairSource a (z i)) g := by
  simp only [neutralLogBackgroundOperator, ContinuousLinearMap.add_apply,
    _root_.inner_add_right, neutralLogFiniteSelectedOperator_mixed]

theorem neutralLogBackgroundOperator_diagonal (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogBackgroundOperator a ha lowerC upperC shift h0 hl hu z f) =
      (((∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2) +
        2 * (conj (sourceWindowMoment a (-(1/2)) (neutralLogPhysical f.val)) *
          sourceWindowMoment a (1/2) (neutralLogPhysical f.val)).re +
        ∑ i, ‖inner ℂ (neutralLogNegativePairSource a (z i)) f‖ ^ 2 : ℝ) : ℂ) := by
  simp only [neutralLogBackgroundOperator, ContinuousLinearMap.add_apply,
    _root_.inner_add_right, neutralLogWeilFormOperator_diagonal,
    neutralLogFiniteSelectedOperator_diagonal, Complex.ofReal_add]

/-- Exact subtraction recovers the full actual form. This does not assert
that the background or the full form annihilates the current carrier. -/
theorem neutralLogBackgroundOperator_sub_selected :
    neutralLogBackgroundOperator a ha lowerC upperC shift h0 hl hu z -
      neutralLogFiniteSelectedOperator a z =
        neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu := by
  exact add_sub_cancel_right _ _

theorem neutralLogBackgroundOperator_conjugate :
    neutralLogBackgroundOperator a ha lowerC upperC shift h0 hl hu
      (fun i => conj (z i)) =
    neutralLogBackgroundOperator a ha lowerC upperC shift h0 hl hu z := by
  simp only [neutralLogBackgroundOperator, neutralLogFiniteSelectedOperator_conjugate]

end

end WeilDefect
