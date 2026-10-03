import WeilDefect.Morphology.NeutralLogMultiplierSourceAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap InnerProductSpace
open scoped ComplexConjugate FourierTransform

/-- The concrete domain correspondence is complex-linear. The codomain keeps
its existing physical L2 norm; this is not a claim of norm equivalence. -/
def neutralLogHilbertCanonicalLinearEquiv (a : ℝ) :
    NeutralLogHilbertCarrier a ≃ₗ[ℂ] neutralCanonicalLogFormDomain a where
  toFun := neutralLogHilbertToCanonical
  invFun := neutralCanonicalToLogHilbert
  left_inv := neutralLogHilbertToCanonical_rightInverse
  right_inv := neutralLogHilbertToCanonical_leftInverse
  map_add' f g := by
    apply Subtype.ext
    exact neutralLogPhysical.map_add f.val g.val
  map_smul' z f := by
    apply Subtype.ext
    exact neutralLogPhysical.map_smul z f.val

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
  {carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs} {a : ℝ}

/-- Actual inclusion of a lawful source domain in the canonical domain. -/
def neutralSourceDomainToCanonical
    (D : NeutralSourceFormDomainAttachment carrier a) :
    D.domain →ₗ[ℂ] neutralCanonicalLogFormDomain a where
  toFun f := ⟨f.val, D.supported f, D.logEnergy f⟩
  map_add' _ _ := Subtype.ext rfl
  map_smul' _ _ := Subtype.ext rfl

/-- Actual complex-linear lifting to the complete logarithmic carrier. -/
def neutralSourceDomainToLogHilbert
    (D : NeutralSourceFormDomainAttachment carrier a) :
    D.domain →ₗ[ℂ] NeutralLogHilbertCarrier a :=
  (neutralLogHilbertCanonicalLinearEquiv a).symm.toLinearMap.comp
    (neutralSourceDomainToCanonical D)

theorem neutralSourceDomainToLogHilbert_physical
    (D : NeutralSourceFormDomainAttachment carrier a) (f : D.domain) :
    neutralLogPhysical (neutralSourceDomainToLogHilbert D f).val = f.val := by
  exact congrArg Subtype.val
    (neutralLogHilbertToCanonical_leftInverse (neutralSourceDomainToCanonical D f))

theorem neutralSourceDomainToLogHilbert_injective
    (D : NeutralSourceFormDomainAttachment carrier a) :
    Function.Injective (neutralSourceDomainToLogHilbert D) := by
  intro f g h
  apply Subtype.ext
  have hp := congrArg (fun v : NeutralLogHilbertCarrier a =>
    neutralLogPhysical v.val) h
  simpa only [neutralSourceDomainToLogHilbert_physical] using hp

/-- The lifting uses the actual logarithmic energy norm, not operator L2. -/
theorem neutralSourceDomainToLogHilbert_norm_sq
    (D : NeutralSourceFormDomainAttachment carrier a) (f : D.domain) :
    ‖neutralSourceDomainToLogHilbert D f‖ ^ 2 =
      ∫ ξ, logarithmicFourierWeight ξ * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 := by
  rw [neutralLogHilbertCarrier_norm_sq, neutralSourceDomainToLogHilbert_physical]

/-- The distinguished source-domain carrier is the same physical vector
after the actual linear lift. This does not supply D for a WD-T38 instance. -/
theorem neutralSourceDomainToLogHilbert_carrier
    (D : NeutralSourceFormDomainAttachment carrier a) :
    neutralLogPhysical
      (neutralSourceDomainToLogHilbert D ⟨carrier.l2Mode, D.carrier_mem⟩).val =
        carrier.l2Mode :=
  neutralSourceDomainToLogHilbert_physical D _

variable (D : NeutralSourceFormDomainAttachment carrier a)
  (ha : RightLimitWeilSymbolTemperatePremise a)
  (lowerC upperC shift : ℝ) (h0 : 0 ≤ lowerC)
  (hl : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
    rightLimitCompactWeilSymbolMathlib a ξ + shift)
  (hu : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
    upperC * logarithmicFourierWeight ξ)

/-- Exact attachment to the already constructed sourceDomainWeilForm.
Both slots remain in the same lawful source domain; no hrep is assumed. -/
theorem neutralSourceDomainToLogHilbert_mixed (f g : D.domain) :
    inner ℂ (neutralSourceDomainToLogHilbert D f)
      (neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu
        (neutralSourceDomainToLogHilbert D g)) =
      sourceDomainWeilFormFromShiftedComparison D ha lowerC upperC shift h0 hl hu
        f g := by
  rw [neutralLogWeilFormOperator_mixed]
  simp only [neutralSourceDomainToLogHilbert_physical,
    sourceDomainWeilFormFromShiftedComparison, sourceDomainWeilForm_apply,
    sourceDomainMultiplierPairing]

/-- Exact attachment to the existing real source quadratic, including the
actual complex cross-pole term. -/
theorem neutralSourceDomainToLogHilbert_quadratic (f : D.domain) :
    inner ℂ (neutralSourceDomainToLogHilbert D f)
      (neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu
        (neutralSourceDomainToLogHilbert D f)) =
      (sourceDomainQuadratic D f : ℂ) := by
  rw [neutralLogWeilFormOperator_diagonal]
  simp only [neutralSourceDomainToLogHilbert_physical, sourceDomainQuadratic]

end

end WeilDefect
