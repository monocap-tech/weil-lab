import WeilDefect.Morphology.NeutralCanonicalFormDomain

namespace WeilDefect
noncomputable section
open MeasureTheory

/-- F08-003: contraction of the *original* logarithmic Fourier energy
under a pointwise complex multiplier of modulus at most one.
This is a lemma for Fourier coordinates, not an assertion that a physical
sharp cutoff preserves the logarithmic form domain. -/
theorem f08_log_weight_multiplier_pointwise_le
    (m : ℝ → ℂ) (hm : ∀ ξ : ℝ, ‖m ξ‖ ≤ 1)
    (F : ℝ → ℂ) (ξ : ℝ) :
    logarithmicFourierWeight ξ * ‖m ξ * F ξ‖ ^ 2 ≤
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2 := by
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have hnorm : ‖m ξ * F ξ‖ ≤ ‖F ξ‖ := by
    calc
      ‖m ξ * F ξ‖ = ‖m ξ‖ * ‖F ξ‖ := norm_mul _ _
      _ ≤ 1 * ‖F ξ‖ :=
        mul_le_mul_of_nonneg_right (hm ξ) (norm_nonneg _)
      _ = ‖F ξ‖ := one_mul _
  have hsq : ‖m ξ * F ξ‖ ^ 2 ≤ ‖F ξ‖ ^ 2 := by
    nlinarith [norm_nonneg (m ξ * F ξ), norm_nonneg (F ξ)]
  exact mul_le_mul_of_nonneg_left hsq hw

/-- The original logarithmic energy remains integrable after a
complex contraction of its actual L² Fourier coordinate. In particular
this covers the spectral half of positive unit-mass mollification once
its exact physical convolution/Fourier multiplier dictionary is proved. -/
theorem f08_log_weight_multiplier_integrable
    (F : RealComplexL2)
    (hF : Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2) volume)
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (hbound : ∀ ξ : ℝ, ‖m ξ‖ ≤ 1) :
    Integrable (fun ξ : ℝ =>
      logarithmicFourierWeight ξ * ‖m ξ * F ξ‖ ^ 2) volume := by
  apply hF.mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      ((hm.mul (Lp.aestronglyMeasurable F)).norm.pow 2)
  · filter_upwards [] with ξ
    have hw : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    have hn1 : 0 ≤ logarithmicFourierWeight ξ * ‖m ξ * F ξ‖ ^ 2 :=
      mul_nonneg hw (sq_nonneg _)
    have hn2 : 0 ≤ logarithmicFourierWeight ξ * ‖F ξ‖ ^ 2 :=
      mul_nonneg hw (sq_nonneg _)
    simpa only [Real.norm_eq_abs, abs_of_nonneg hn1, abs_of_nonneg hn2] using
      f08_log_weight_multiplier_pointwise_le m hbound F ξ

#print axioms f08_log_weight_multiplier_pointwise_le
#print axioms f08_log_weight_multiplier_integrable

end
end WeilDefect
