import WeilDefect.Morphology.NeutralLogBackgroundSourceAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap
open scoped InnerProduct ComplexConjugate FourierTransform

/-- Genuine physical L2 mass, independently of logarithmic form energy. -/
theorem neutralPhysicalL2_norm_sq (k : RealComplexL2) :
    ‖k‖ ^ 2 = ∫ ξ, ‖k ξ‖ ^ 2 := by
  have hi : inner ℂ k k = ((∫ ξ, ‖k ξ‖ ^ 2 : ℝ) : ℂ) := by
    rw [L2.inner_def]
    simp only [RCLike.inner_apply', Complex.conj_mul', ← Complex.ofReal_pow]
    exact integral_complex_ofReal
  rw [norm_sq_eq_re_inner (𝕜 := ℂ), hi]
  rfl

theorem neutralSourceWindowMoment_sq_bound (a s : ℝ) (k : RealComplexL2) :
    ‖sourceWindowMoment a s k‖ ^ 2 ≤
      ‖neutralMomentColumnL2 a s‖ ^ 2 * ‖k‖ ^ 2 := by
  have h : ‖sourceWindowMoment a s k‖ ≤ ‖neutralMomentColumnL2 a s‖ * ‖k‖ := by
    rw [← neutralMomentColumnL2_inner]
    exact norm_inner_le_norm _ _
  have hp : 0 ≤
      (‖neutralMomentColumnL2 a s‖ * ‖k‖ - ‖sourceWindowMoment a s k‖) *
      (‖neutralMomentColumnL2 a s‖ * ‖k‖ + ‖sourceWindowMoment a s k‖) :=
    mul_nonneg (sub_nonneg.mpr h)
      (add_nonneg (mul_nonneg (norm_nonneg _) (norm_nonneg _)) (norm_nonneg _))
  nlinarith only [hp]

/-- Actual physical-L2 error constant from the two compact exponential columns.
It is not WD-T38's independently parameterized scalar poleC. -/
def neutralPhysicalPoleEnergyConstant (a : ℝ) : ℝ :=
  ‖neutralMomentColumnL2 a (-(1/2))‖ ^ 2 +
    ‖neutralMomentColumnL2 a (1/2)‖ ^ 2

theorem neutralPhysicalPoleEnergyConstant_nonnegative (a : ℝ) :
    0 ≤ neutralPhysicalPoleEnergyConstant a :=
  add_nonneg (sq_nonneg _) (sq_nonneg _)

/-- Control of the actual Hermitian pole, including its possible negative sign. -/
theorem neutralPhysicalPoleEnergy_abs_le (a : ℝ) (k : RealComplexL2) :
    |2 * (conj (sourceWindowMoment a (-(1/2)) k) *
      sourceWindowMoment a (1/2) k).re| ≤
        neutralPhysicalPoleEnergyConstant a * ‖k‖ ^ 2 := by
  have hr := Complex.abs_re_le_norm
    (conj (sourceWindowMoment a (-(1/2)) k) * sourceWindowMoment a (1/2) k)
  rw [norm_mul, Complex.norm_conj] at hr
  have hm := neutralSourceWindowMoment_sq_bound a (-(1/2)) k
  have hp := neutralSourceWindowMoment_sq_bound a (1/2) k
  have hab := sq_nonneg
    (‖sourceWindowMoment a (-(1/2)) k‖ - ‖sourceWindowMoment a (1/2) k‖)
  rw [abs_mul, abs_of_pos (by norm_num : (0 : ℝ) < 2)]
  unfold neutralPhysicalPoleEnergyConstant
  nlinarith only [hr, hm, hp, hab]

variable (a : ℝ) (ha : RightLimitWeilSymbolTemperatePremise a)
  (lowerC upperC shift : ℝ) (h0 : 0 ≤ lowerC)
  (hl : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
    rightLimitCompactWeilSymbolMathlib a ξ + shift)
  (hu : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
    upperC * logarithmicFourierWeight ξ)

include ha lowerC upperC shift h0 hl hu

/-- The retained constant shift contributes physical L2 energy exactly.
This uses ordinary L2 Plancherel, not spectral product membership. -/
theorem neutralLogPhysical_shiftedSymbolEnergy_eq (f : NeutralLogHilbertCarrier a) :
    (∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ + shift) *
      ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2) =
    (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
      ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2) +
      shift * ‖neutralLogPhysical f.val‖ ^ 2 := by
  have hs := neutralLogPhysical_signedSymbolEnergy a ha lowerC upperC shift h0 hl hu f.val
  have hn := (memLp_two_iff_integrable_sq_norm
    (Lp.aestronglyMeasurable (𝓕 (neutralLogPhysical f.val) : RealComplexL2))).mp (Lp.memLp _)
  calc
    _ = ∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2 +
      shift * ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2) := by
      apply integral_congr_ae
      filter_upwards [] with ξ
      ring
    _ = _ := by
      rw [integral_add hs (hn.const_mul shift), integral_const_mul,
        ← neutralPhysicalL2_norm_sq, Lp.norm_fourier_eq]

/-- Actual logarithmic lower estimate with a physical L2 error.
No strict positivity of the full Weil form is asserted. -/
theorem neutralLogWeilFormOperator_garding (f : NeutralLogHilbertCarrier a) :
    lowerC * ‖f‖ ^ 2 ≤
      (inner ℂ f (neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu f)).re +
      (shift + neutralPhysicalPoleEnergyConstant a) * ‖neutralLogPhysical f.val‖ ^ 2 := by
  have hs := (neutralLogPhysical_shiftedComparison a ha lowerC upperC shift h0 hl hu f).1
  rw [neutralLogPhysical_shiftedSymbolEnergy_eq a ha lowerC upperC shift h0 hl hu f] at hs
  have hp := (abs_le.mp (neutralPhysicalPoleEnergy_abs_le a (neutralLogPhysical f.val))).1
  have hd :
      (inner ℂ f (neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu f)).re =
      (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2) +
        2 * (conj (sourceWindowMoment a (-(1/2)) (neutralLogPhysical f.val)) *
          sourceWindowMoment a (1/2) (neutralLogPhysical f.val)).re := by
    rw [neutralLogWeilFormOperator_diagonal, Complex.ofReal_re]
  nlinarith only [hs, hp, hd]

/-- The concrete selected addition is nonnegative, so the same actual
logarithmic lower estimate holds for the background expression. -/
theorem neutralLogBackgroundOperator_garding {ι : Type*} [Fintype ι]
    (z : ι → ℂ) (f : NeutralLogHilbertCarrier a) :
    lowerC * ‖f‖ ^ 2 ≤
      (inner ℂ f (neutralLogBackgroundOperator a ha lowerC upperC shift h0 hl hu z f)).re +
      (shift + neutralPhysicalPoleEnergyConstant a) * ‖neutralLogPhysical f.val‖ ^ 2 := by
  have hs := neutralLogWeilFormOperator_garding a ha lowerC upperC shift h0 hl hu f
  have hp := neutralLogFiniteSelectedOperator_nonnegative a z f
  have hd :
      (inner ℂ f (neutralLogBackgroundOperator a ha lowerC upperC shift h0 hl hu z f)).re =
      (inner ℂ f (neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu f)).re +
      (inner ℂ f (neutralLogFiniteSelectedOperator a z f)).re := by
    simp only [neutralLogBackgroundOperator, ContinuousLinearMap.add_apply,
      _root_.inner_add_right, Complex.add_re]
  nlinarith only [hs, hp, hd]

end

end WeilDefect
