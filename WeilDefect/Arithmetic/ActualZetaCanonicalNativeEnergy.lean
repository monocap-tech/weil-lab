import WeilDefect.Arithmetic.ActualZetaNativeLogBounds
import WeilDefect.Arithmetic.ActualZetaNativeWeilForm
import WeilDefect.Morphology.NeutralLogBackgroundEnergy

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped FourierTransform ComplexConjugate
set_option maxHeartbeats 800000

/-- A constant selected from the certified actual symbol envelope.
Its defining theorem has no analytic or representation premise. -/
def neutralActualZetaNativeLogError (a : ℝ) : ℝ :=
  (neutralActualZetaNativeSymbol_log_bound a).choose

theorem neutralActualZetaNativeLogError_spec (a : ℝ) :
    0 ≤ neutralActualZetaNativeLogError a ∧ ∀ ξ : ℝ,
      |rightLimitCompactWeilSymbolMathlib a ξ - logarithmicFourierWeight ξ| ≤
        neutralActualZetaNativeLogError a :=
  (neutralActualZetaNativeSymbol_log_bound a).choose_spec

/-- Actual zeroth-order continuity, independent of all-derivative temperate growth. -/
theorem neutralActualZetaNativeSymbol_continuous (a : ℝ) :
    Continuous (rightLimitCompactWeilSymbolMathlib a) := by
  have hc : Continuous (fun ξ : ℝ =>
      compactWindowArchimedeanSymbol (2 * Real.pi * ξ)) := by
    have h := neutralActualZetaGammaBracket_continuous.comp
      (continuous_const.mul continuous_id : Continuous (fun ξ : ℝ => 2 * Real.pi * ξ))
    simpa only [Function.comp_def, Pi.mul_apply,
      neutralActualZetaGammaBracket_native] using h
  unfold rightLimitCompactWeilSymbolMathlib rightLimitCompactWeilSymbol
  apply hc.sub
  unfold rightLimitPrimeSymbol
  fun_prop

theorem neutralActualZetaNativeSymbol_abs_log_le (a ξ : ℝ) :
    |rightLimitCompactWeilSymbolMathlib a ξ| ≤
      (1 + neutralActualZetaNativeLogError a) * logarithmicFourierWeight ξ := by
  have hb := abs_le.mp ((neutralActualZetaNativeLogError_spec a).2 ξ)
  have hC := (neutralActualZetaNativeLogError_spec a).1
  have hw := one_le_logarithmicFourierWeight ξ
  have hm := mul_le_mul_of_nonneg_left hw hC
  apply abs_le.mpr
  constructor <;> nlinarith

/-- Absolute native energy genuinely converges on the entire canonical domain. -/
theorem neutralActualZetaCanonical_absoluteEnergy_integrable
    (a : ℝ) (f : neutralCanonicalLogFormDomain a) :
    Integrable (fun ξ => |rightLimitCompactWeilSymbolMathlib a ξ| *
      ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) := by
  apply (f.property.2.const_mul (1 + neutralActualZetaNativeLogError a)).mono'
  · exact (neutralActualZetaNativeSymbol_continuous a).abs.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f.val : RealComplexL2)).norm.pow 2)
  · filter_upwards [] with ξ
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (abs_nonneg _) (sq_nonneg _))]
    simpa only [mul_assoc] using mul_le_mul_of_nonneg_right
      (neutralActualZetaNativeSymbol_abs_log_le a ξ) (sq_nonneg _)

theorem neutralActualZetaCanonical_signedEnergy_integrable
    (a : ℝ) (f : neutralCanonicalLogFormDomain a) :
    Integrable (fun ξ => rightLimitCompactWeilSymbolMathlib a ξ *
      ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) := by
  apply (neutralActualZetaCanonical_absoluteEnergy_integrable a f).mono'
  · exact (neutralActualZetaNativeSymbol_continuous a).aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f.val : RealComplexL2)).norm.pow 2)
  · filter_upwards [] with ξ
    simp only [Real.norm_eq_abs, abs_mul,
      abs_of_nonneg (sq_nonneg ‖(𝓕 f.val : RealComplexL2) ξ‖)]

/-- The native mixed multiplier also genuinely converges on this same domain. -/
theorem neutralActualZetaCanonical_mixed_integrable
    (a : ℝ) (f g : neutralCanonicalLogFormDomain a) :
    Integrable (fun ξ => conj ((𝓕 f.val : RealComplexL2) ξ) *
      (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
      (𝓕 g.val : RealComplexL2) ξ) := by
  apply integrable_mixedMultiplier
  · exact (neutralActualZetaNativeSymbol_continuous a).aestronglyMeasurable
  · exact Lp.aestronglyMeasurable _
  · exact Lp.aestronglyMeasurable _
  · exact neutralActualZetaCanonical_absoluteEnergy_integrable a f
  · exact neutralActualZetaCanonical_absoluteEnergy_integrable a g

/-- Concrete signed multiplier-plus-cross-pole quadratic on the canonical
supported logarithmic domain. This definition carries no source identity. -/
def neutralActualZetaCanonicalNativeQuadratic
    (a : ℝ) (f : neutralCanonicalLogFormDomain a) : ℝ :=
  (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
    ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) +
  2 * (conj (sourceWindowMoment a (-(1/2)) f.val) *
    sourceWindowMoment a (1/2) f.val).re

private theorem canonical_fourier_mass (a : ℝ)
    (f : neutralCanonicalLogFormDomain a) :
    Integrable (fun ξ => ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) :=
  (memLp_two_iff_integrable_sq_norm
    (Lp.aestronglyMeasurable (𝓕 f.val : RealComplexL2))).mp (Lp.memLp _)

/-- The actual constant shift contributes physical L2 mass, by Plancherel. -/
theorem neutralActualZetaCanonical_shift_energy
    (a : ℝ) (f : neutralCanonicalLogFormDomain a) :
    (∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ +
      neutralActualZetaNativeLogError a) * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) =
    (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
      ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) +
      neutralActualZetaNativeLogError a * ‖f.val‖ ^ 2 := by
  calc
    _ = ∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 +
      neutralActualZetaNativeLogError a * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) := by
      apply integral_congr_ae
      filter_upwards [] with ξ
      ring
    _ = _ := by
      rw [integral_add (neutralActualZetaCanonical_signedEnergy_integrable a f)
        ((canonical_fourier_mass a f).const_mul _), integral_const_mul,
        ← neutralPhysicalL2_norm_sq, Lp.norm_fourier_eq]

/-- Canonical logarithmic norm controls ordinary physical mass. -/
theorem neutralActualZetaCanonical_mass_le_log
    (a : ℝ) (f : neutralCanonicalLogFormDomain a) :
    ‖f.val‖ ^ 2 ≤ ‖neutralLogWeightedL2 f‖ ^ 2 := by
  rw [neutralLogWeightedL2_norm_sq]
  have hm : ‖f.val‖ ^ 2 =
      ∫ ξ, ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 := by
    rw [← neutralPhysicalL2_norm_sq, Lp.norm_fourier_eq]
  rw [hm]
  apply integral_mono (canonical_fourier_mass a f) f.property.2
  intro ξ
  simpa only [one_mul] using mul_le_mul_of_nonneg_right
    (one_le_logarithmicFourierWeight ξ) (sq_nonneg _)

/-- Unconditional native Gårding estimate on the full canonical form domain.
The error is physical L2 mass, not a positivity claim. -/
theorem neutralActualZetaCanonicalNativeQuadratic_garding
    (a : ℝ) (f : neutralCanonicalLogFormDomain a) :
    ‖neutralLogWeightedL2 f‖ ^ 2 ≤
      neutralActualZetaCanonicalNativeQuadratic a f +
      (neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
        ‖f.val‖ ^ 2 := by
  have hs : Integrable (fun ξ => (rightLimitCompactWeilSymbolMathlib a ξ +
      neutralActualZetaNativeLogError a) * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) := by
    convert (neutralActualZetaCanonical_signedEnergy_integrable a f).add
      ((canonical_fourier_mass a f).const_mul (neutralActualZetaNativeLogError a))
      using 1 <;> funext ξ <;> simp only [Pi.add_apply] <;> ring
  have hl : ‖neutralLogWeightedL2 f‖ ^ 2 ≤
      ∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ +
        neutralActualZetaNativeLogError a) * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 := by
    rw [neutralLogWeightedL2_norm_sq]
    apply integral_mono f.property.2 hs
    intro ξ
    have hb := (abs_le.mp ((neutralActualZetaNativeLogError_spec a).2 ξ)).1
    exact mul_le_mul_of_nonneg_right (by linarith) (sq_nonneg _)
  rw [neutralActualZetaCanonical_shift_energy a f] at hl
  have hp := (abs_le.mp (neutralPhysicalPoleEnergy_abs_le a f.val)).1
  unfold neutralActualZetaCanonicalNativeQuadratic
  nlinarith only [hl, hp]

/-- A diagonal bound in the genuine logarithmic norm, derived from actual
symbol and pole estimates rather than an imported comparison premise. -/
theorem neutralActualZetaCanonicalNativeQuadratic_abs_le
    (a : ℝ) (f : neutralCanonicalLogFormDomain a) :
    |neutralActualZetaCanonicalNativeQuadratic a f| ≤
      (1 + neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
        ‖neutralLogWeightedL2 f‖ ^ 2 := by
  have hi : |∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2| ≤
      ∫ ξ, |rightLimitCompactWeilSymbolMathlib a ξ| *
        ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 := by
    have h := norm_integral_le_integral_norm (μ := volume)
      (fun ξ => rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2)
    simpa only [Real.norm_eq_abs, abs_mul, abs_of_nonneg
      (sq_nonneg ‖(𝓕 f.val : RealComplexL2) _‖)] using h
  have hb : (∫ ξ, |rightLimitCompactWeilSymbolMathlib a ξ| *
      ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) ≤
      (1 + neutralActualZetaNativeLogError a) * ‖neutralLogWeightedL2 f‖ ^ 2 := by
    rw [neutralLogWeightedL2_norm_sq, ← integral_const_mul]
    apply integral_mono (neutralActualZetaCanonical_absoluteEnergy_integrable a f)
      (f.property.2.const_mul _)
    intro ξ
    simpa only [mul_assoc] using mul_le_mul_of_nonneg_right
      (neutralActualZetaNativeSymbol_abs_log_le a ξ) (sq_nonneg _)
  have hp := neutralPhysicalPoleEnergy_abs_le a f.val
  have hm := mul_le_mul_of_nonneg_left (neutralActualZetaCanonical_mass_le_log a f)
    (neutralPhysicalPoleEnergyConstant_nonnegative a)
  have ht := abs_add_le
    (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2)
    (2 * (conj (sourceWindowMoment a (-(1/2)) f.val) *
      sourceWindowMoment a (1/2) f.val).re)
  unfold neutralActualZetaCanonicalNativeQuadratic
  nlinarith only [hi, hb, hp, hm, ht]

/-- The canonical quadratic preserves the certified actual Green zero-form diagonal. -/
theorem neutralActualZetaGreenZeroForm_canonical_quadratic
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    (neutralActualZetaGreenZeroForm a v v).re =
      neutralActualZetaCanonicalNativeQuadratic a (neutralActualZetaGreenCanonical a ha v) := by
  rw [neutralActualZetaGreenZeroForm_native_diagonal a ha v,
    neutralLogPoleOperator_diagonal, Complex.add_re, Complex.ofReal_re,
    Complex.ofReal_re]
  change _ = (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
    ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) + _
  have hp : neutralLogPhysical
      (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v)).val =
      (neutralActualZetaGreenCanonical a ha v).val :=
    neutralLogPhysical_weighted _
  rw [hp]

/-- The actual zero form inherits the native logarithmic Gårding inequality
on the unchanged Green vector. No retained k is silently replaced by this vector. -/
theorem neutralActualZetaGreenZeroForm_garding
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    ‖neutralLogWeightedL2 (neutralActualZetaGreenCanonical a ha v)‖ ^ 2 ≤
      (neutralActualZetaGreenZeroForm a v v).re +
      (neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
        ‖neutralActualZetaGreenSynthesis a v‖ ^ 2 := by
  rw [neutralActualZetaGreenZeroForm_canonical_quadratic a ha v]
  exact neutralActualZetaCanonicalNativeQuadratic_garding a _

end
end WeilDefect
