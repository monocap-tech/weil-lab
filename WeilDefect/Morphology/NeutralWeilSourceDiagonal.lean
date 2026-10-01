import WeilDefect.Morphology.NeutralWeilSourceMixedForm

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped ComplexConjugate FourierTransform

/-- The absolute-symbol estimate is a consequence of the retained shifted
comparison. No new absolute-symbol analytic premise is introduced. -/
theorem absoluteSymbolBound_of_shiftedComparison
    (m : ℝ → ℝ) (upperC shift : ℝ)
    (hlower : ∀ ξ, 0 ≤ m ξ + shift)
    (hupper : ∀ ξ, m ξ + shift ≤ upperC * logarithmicFourierWeight ξ)
    (ξ : ℝ) :
    |m ξ| ≤ (|upperC| + |shift|) * logarithmicFourierWeight ξ := by
  have hw := one_le_logarithmicFourierWeight ξ
  have hw0 : 0 ≤ logarithmicFourierWeight ξ := le_trans (by norm_num) hw
  have hu := mul_le_mul_of_nonneg_right (le_abs_self upperC) hw0
  have hs := mul_le_mul_of_nonneg_left hw (abs_nonneg shift)
  have hb := mul_nonneg (abs_nonneg upperC) hw0
  apply abs_le.mpr
  constructor <;> nlinarith [hlower ξ, hupper ξ, le_abs_self shift, neg_le_abs shift]

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
  {carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs} {a : ℝ}

/-- Transfer WD-T35/38's retained two-sided comparison in normalized Fourier
coordinates to the mixed form's absolute bound. -/
theorem rightLimitWeil_absoluteSymbolBound
    (lowerC upperC shift : ℝ) (hlowerC : 0 ≤ lowerC)
    (hlower : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
      rightLimitCompactWeilSymbolMathlib a ξ + shift)
    (hupper : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
      upperC * logarithmicFourierWeight ξ) (ξ : ℝ) :
    |rightLimitCompactWeilSymbolMathlib a ξ| ≤
      (|upperC| + |shift|) * logarithmicFourierWeight ξ := by
  apply absoluteSymbolBound_of_shiftedComparison _ upperC shift _ hupper ξ
  intro η
  exact (mul_nonneg hlowerC
    (le_trans (by norm_num) (one_le_logarithmicFourierWeight η))).trans (hlower η)

variable (D : NeutralSourceFormDomainAttachment carrier a)
  (hSymbol : RightLimitWeilSymbolTemperatePremise a) (C : ℝ)
  (hbound : ∀ ξ, |rightLimitCompactWeilSymbolMathlib a ξ| ≤
    C * logarithmicFourierWeight ξ)

include hSymbol C hbound in
/-- The signed real diagonal energy also genuinely converges. -/
theorem sourceDomain_signedEnergy_integrable (f : D.domain) :
    Integrable (fun ξ => rightLimitCompactWeilSymbolMathlib a ξ *
      ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) volume := by
  apply (D.absoluteSymbolEnergy hSymbol C hbound f).mono'
  · exact (Complex.continuous_re.comp
      hSymbol.hasTemperateGrowth.1.continuous).aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f.val : RealComplexL2)).norm.pow 2)
  · filter_upwards [] with ξ
    simp only [Real.norm_eq_abs, abs_mul,
      abs_of_nonneg (sq_nonneg ‖(𝓕 f.val : RealComplexL2) ξ‖)]
    exact le_rfl

/-- The actual complex multiplier pairing diagonal is exactly the real
normalized symbol energy, with no hidden Fourier scaling constant. -/
theorem sourceDomainMultiplierPairing_diagonal (f : D.domain) :
    sourceDomainMultiplierPairing D f f =
      (((∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) : ℝ) : ℂ) := by
  unfold sourceDomainMultiplierPairing
  calc
    _ = ∫ ξ, ((rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 : ℝ) : ℂ) := by
      apply integral_congr_ae
      filter_upwards [] with ξ
      calc
        _ = (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
            (conj ((𝓕 f.val : RealComplexL2) ξ) * (𝓕 f.val : RealComplexL2) ξ) := by ring
        _ = _ := by simp only [Complex.conj_mul', Complex.ofReal_mul, Complex.ofReal_pow]
    _ = _ := integral_complex_ofReal

/-- Hermitian pole cross terms have the real quadratic diagonal. The real
part is essential for complex carriers. -/
theorem sourcePoleCrossTerms_diagonal (z w : ℂ) :
    conj z * w + conj w * z = ((2 * (conj z * w).re : ℝ) : ℂ) := by
  apply Complex.ext <;>
    simp only [Complex.add_re, Complex.add_im, Complex.mul_re, Complex.mul_im,
      Complex.conj_re, Complex.conj_im, Complex.ofReal_re, Complex.ofReal_im] <;> ring

/-- The explicit real source diagonal on the retained domain. Integrability
is proved above; this definition is not used as a totalization shortcut. -/
def sourceDomainQuadratic (f : D.domain) : ℝ :=
  (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
    ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) +
  2 * (conj (sourceWindowMoment a (-(1 / 2)) f.val) *
    sourceWindowMoment a (1 / 2) f.val).re

theorem sourceDomainWeilForm_diagonal (f : D.domain) :
    sourceDomainWeilForm D hSymbol C hbound f f = (sourceDomainQuadratic D f : ℂ) := by
  rw [sourceDomainWeilForm_apply,
    sourceDomainMultiplierPairing_diagonal D f,
    sourcePoleCrossTerms_diagonal]
  simp only [sourceDomainQuadratic, Complex.ofReal_add]

/-- The actual carrier's quadratic pole term is the real Hermitian pairing
with the previously represented source pole function. -/
theorem sourceDomainQuadratic_carrier (hca : c ≤ a) :
    sourceDomainQuadratic D ⟨carrier.l2Mode, D.carrier_mem⟩ =
      (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 carrier.l2Mode : RealComplexL2) ξ‖ ^ 2) +
      (∫ x, conj (carrier.h x) * neutralWeilSourcePole carrier x).re := by
  simp only [sourceDomainQuadratic, sourceWindowMoment_carrier hca]
  rw [neutralWeilSourcePole_hermitian_pairing_eq]
  congr 1
  rw [show
      neutralWeilPoleMoment carrier (-(1 / 2)) * conj (neutralWeilPoleMoment carrier (1 / 2)) +
      neutralWeilPoleMoment carrier (1 / 2) * conj (neutralWeilPoleMoment carrier (-(1 / 2))) =
      conj (neutralWeilPoleMoment carrier (-(1 / 2))) * neutralWeilPoleMoment carrier (1 / 2) +
      conj (neutralWeilPoleMoment carrier (1 / 2)) * neutralWeilPoleMoment carrier (-(1 / 2)) by ring,
    sourcePoleCrossTerms_diagonal]
  rfl

/-- Consume the retained source formula in its explicit real quadratic form,
rather than assuming equality with an abstract candidate diagonal. -/
theorem sourceDomainWeilForm_eq_of_sourceQuadratic
    (B : D.domain →ₗ⋆[ℂ] D.domain →ₗ[ℂ] ℂ)
    (hsource : ∀ z : D.domain, B z z = (sourceDomainQuadratic D z : ℂ))
    (f g : D.domain) : B f g = sourceDomainWeilForm D hSymbol C hbound f g := by
  apply sourceDomainWeilForm_eq_of_diagonal D hSymbol C hbound B _ f g
  intro z
  rw [sourceDomainWeilForm_diagonal]
  exact hsource z

/-- Construct the same concrete form directly from the retained shifted
lower/upper estimates, deriving the absolute bound internally. -/
def sourceDomainWeilFormFromShiftedComparison
    (lowerC upperC shift : ℝ) (hlowerC : 0 ≤ lowerC)
    (hlower : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
      rightLimitCompactWeilSymbolMathlib a ξ + shift)
    (hupper : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
      upperC * logarithmicFourierWeight ξ) :
    D.domain →ₗ⋆[ℂ] D.domain →ₗ[ℂ] ℂ :=
  sourceDomainWeilForm D hSymbol (|upperC| + |shift|)
    (rightLimitWeil_absoluteSymbolBound lowerC upperC shift hlowerC hlower hupper)

/-- The source's explicit quadratic identity now suffices for mixed equality
without a separate absolute-symbol premise. All vectors remain in the domain. -/
theorem sourceDomainWeilFormFromShiftedComparison_eq_of_sourceQuadratic
    (lowerC upperC shift : ℝ) (hlowerC : 0 ≤ lowerC)
    (hlower : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
      rightLimitCompactWeilSymbolMathlib a ξ + shift)
    (hupper : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
      upperC * logarithmicFourierWeight ξ)
    (B : D.domain →ₗ⋆[ℂ] D.domain →ₗ[ℂ] ℂ)
    (hsource : ∀ z : D.domain, B z z = (sourceDomainQuadratic D z : ℂ))
    (f g : D.domain) :
    B f g = sourceDomainWeilFormFromShiftedComparison D hSymbol
      lowerC upperC shift hlowerC hlower hupper f g := by
  exact sourceDomainWeilForm_eq_of_sourceQuadratic D hSymbol _ _ B hsource f g

end

end WeilDefect
