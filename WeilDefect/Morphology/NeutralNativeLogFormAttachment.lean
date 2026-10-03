import WeilDefect.Morphology.NeutralNativeFourierRepresentative

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform

/-- The canonical logarithmic weight is dominated by a genuine first
derivative energy weight, with no retained symbol comparison. -/
theorem logarithmicFourierWeight_le_derivativeWeight (ξ : ℝ) :
    logarithmicFourierWeight ξ ≤ Real.exp 1 + ξ ^ 2 := by
  have hlog := Real.log_le_sub_one_of_pos
    (show 0 < Real.exp 1 + |ξ| by positivity)
  have habs : |ξ| ≤ ξ ^ 2 + 1 := by
    nlinarith [sq_nonneg (|ξ| - 1), sq_abs ξ]
  unfold logarithmicFourierWeight
  linarith

/-- Remove only the nonzero Fourier derivative constant from the proved
native product. This is derived regularity, not an operator-domain premise. -/
theorem neutralNativeGreenSynthesis_frequency_memLp
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    MemLp (fun ξ : ℝ => (ξ : ℂ) *
      (𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2) ξ) 2 volume := by
  have hk : (2 * Real.pi * Complex.I : ℂ) ≠ 0 := by
    exact mul_ne_zero (mul_ne_zero (by norm_num)
      (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero)) Complex.I_ne_zero
  have h := (neutralNativeFourierDerivativeProduct_memLp a ha data C hCount v).const_mul
    (2 * Real.pi * Complex.I : ℂ)⁻¹
  have heq : (fun ξ => (2 * Real.pi * Complex.I : ℂ)⁻¹ *
      neutralNativeFourierDerivativeProduct a data v ξ) =
      (fun ξ : ℝ => (ξ : ℂ) *
        (𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2) ξ) := by
    funext ξ
    unfold neutralNativeFourierDerivativeProduct
    rw [← mul_assoc, ← mul_assoc, inv_mul_cancel₀ hk, one_mul]
  rw [heq] at h
  exact h

/-- Actual logarithmic energy of the physical native Green synthesis,
derived from its actual derivative and base L2 mass. -/
theorem neutralNativeGreenSynthesis_logEnergy
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    Integrable (fun ξ => logarithmicFourierWeight ξ *
      ‖(𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2) ξ‖ ^ 2) volume := by
  have hF := Lp.memLp (𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2)
  have hp := neutralNativeGreenSynthesis_frequency_memLp a ha data C hCount v
  have hmass := (memLp_two_iff_integrable_sq_norm hF.aestronglyMeasurable).mp hF
  have hprod := (memLp_two_iff_integrable_sq_norm hp.aestronglyMeasurable).mp hp
  apply ((hmass.const_mul (Real.exp 1)).add hprod).mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      (hF.aestronglyMeasurable.norm.pow 2)
  · filter_upwards with ξ
    have hw : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hw (sq_nonneg _))]
    calc
      logarithmicFourierWeight ξ *
          ‖(𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2) ξ‖ ^ 2 ≤
        (Real.exp 1 + ξ ^ 2) *
          ‖(𝓕 (neutralNativeGreenSynthesis a data v) : RealComplexL2) ξ‖ ^ 2 :=
        mul_le_mul_of_nonneg_right
          (logarithmicFourierWeight_le_derivativeWeight ξ) (sq_nonneg _)
      _ = _ := by
        simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs, mul_pow, sq_abs]
        ring

/-- The actual native physical vector now inhabits the canonical supported
logarithmic form domain. No source/null identity is asserted by this definition. -/
def neutralNativeGreenCanonical
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) : neutralCanonicalLogFormDomain a :=
  ⟨neutralNativeGreenSynthesis a data v,
    neutralNativeGreenSynthesis_supported a ha data C hCount v,
    neutralNativeGreenSynthesis_logEnergy a ha data C hCount v⟩

/-- Canonical attachment preserves the actual physical synthesis exactly. -/
theorem neutralNativeGreenCanonical_val
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    (neutralNativeGreenCanonical a ha data C hCount v).val =
      neutralNativeGreenSynthesis a data v := rfl

/-- The existing complete logarithmic carrier realizes the same physical
vector; no new completion or conditional representation is introduced. -/
theorem neutralNativeGreenCanonical_physical
    {count : ℕ → ℕ} (a : ℝ) (ha : 0 < a)
    (data : ActualProblemOneShellData count) (C : ℝ)
    (hCount : ZetaZeroShellCountData count C)
    (v : NeutralNativeShellCoefficients count) :
    neutralLogPhysical
      (neutralCanonicalToLogHilbert
        (neutralNativeGreenCanonical a ha data C hCount v)).val =
      neutralNativeGreenSynthesis a data v := by
  exact neutralLogPhysical_weighted
    (neutralNativeGreenCanonical a ha data C hCount v)

end

end WeilDefect
