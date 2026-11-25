import WeilDefect.Generated.F08.NativeLogDilationFactor
import WeilDefect.Generated.F08.LogDilationFixedVectorCorrection
import WeilDefect.Generated.F08.NativeFrequencyDilation
import WeilDefect.Morphology.NeutralLogHilbertCarrier

namespace WeilDefect
noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform ENNReal

/-- Cancellation of the exact logarithmic correction against the original
square-root energy weight. -/
theorem f08_063_logCorrection_mul_sqrt (lam xi : ℝ) :
    f08_025_logDilationFactor lam xi *
      Real.sqrt (logarithmicFourierWeight (lam * xi)) =
      Real.sqrt (logarithmicFourierWeight xi) := by
  have hp : 0 < logarithmicFourierWeight (lam * xi) :=
    lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight (lam * xi))
  have hn : 0 ≤ logarithmicFourierWeight xi :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight xi)
  unfold f08_025_logDilationFactor
  rw [Real.sqrt_div hn]
  exact div_mul_cancel₀ _ (ne_of_gt (Real.sqrt_pos.mpr hp))

/-- Actual weighted Fourier representative identity, conditional only on
the explicit native Fourier covariance of the proposed physical vector.
No finite-energy assumption on that vector is used. -/
theorem f08_063_weightedCoordinate_ae
    {a : ℝ} (f : neutralCanonicalLogFormDomain a)
    (lam : ℝ) (hlam : 0 < lam) (g : RealComplexL2)
    (hfour : (𝓕 g : RealComplexL2) =
      f08_030_nativeFrequencyDilation lam (ne_of_gt hlam) (𝓕 f.val : RealComplexL2)) :
    (fun xi : ℝ => (Real.sqrt (logarithmicFourierWeight xi) : ℂ) *
      (𝓕 g : RealComplexL2) xi) =ᵐ[volume]
    (fun xi : ℝ => f08_025_logDilationFactor lam xi •
      f08_030_nativeFrequencyDilation lam (ne_of_gt hlam) (neutralLogWeightedL2 f) xi) := by
  have hac : f08_027_scaledFrequencyMeasure lam ≪ (volume : Measure ℝ) := by
    rw [f08_027_scaledFrequencyMeasure_jacobian lam (ne_of_gt hlam)]
    exact Measure.smul_absolutelyContinuous
  have hk := (f08_027_scale_measurePreserving lam).quasiMeasurePreserving.ae_eq_comp
    (hac.ae_eq (neutralLogWeightedL2_coe f))
  rw [hfour]
  filter_upwards [hk,
    f08_030_nativeFrequencyDilation_ae lam (ne_of_gt hlam) (𝓕 f.val : RealComplexL2),
    f08_030_nativeFrequencyDilation_ae lam (ne_of_gt hlam) (neutralLogWeightedL2 f)]
    with xi hki h1 h2
  change neutralLogWeightedL2 f (lam * xi) = neutralLogWeightedFourier f (lam * xi) at hki
  rw [h1, h2, hki]
  unfold neutralLogWeightedFourier
  simp only [smul_eq_mul]
  change (Real.sqrt (logarithmicFourierWeight xi) : ℂ) *
      ((Real.sqrt (abs lam) : ℂ) * (𝓕 f.val : RealComplexL2) (lam * xi)) =
    (f08_025_logDilationFactor lam xi : ℂ) *
      ((Real.sqrt (abs lam) : ℂ) *
        ((Real.sqrt (logarithmicFourierWeight (lam * xi)) : ℂ) *
          (𝓕 f.val : RealComplexL2) (lam * xi)))
  have hc : (f08_025_logDilationFactor lam xi : ℂ) *
      (Real.sqrt (logarithmicFourierWeight (lam * xi)) : ℂ) =
      (Real.sqrt (logarithmicFourierWeight xi) : ℂ) := by
    exact_mod_cast f08_063_logCorrection_mul_sqrt lam xi
  calc
    _ = (Real.sqrt (logarithmicFourierWeight xi) : ℂ) *
        (Real.sqrt (abs lam) : ℂ) * (𝓕 f.val : RealComplexL2) (lam * xi) := by ring
    _ = _ := by rw [← hc]; ring

/-- The exact correction times any native L² vector has integrable squared
norm on inward scales. This is the independent finite-energy receiver. -/
theorem f08_063_correctedNative_memLp
    (lam : ℝ) (hlo : (1 / 2 : ℝ) ≤ lam) (hhi : lam ≤ 1)
    (k : RealComplexL2) :
    MemLp (fun xi : ℝ => f08_025_logDilationFactor lam xi • k xi) 2 volume := by
  have hm := (f08_057_logDilationFactor_continuous lam).aestronglyMeasurable.smul
    (Lp.aestronglyMeasurable k)
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hk := (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable k)).mp (Lp.memLp k)
  apply (hk.const_mul (1 + Real.log 2)).mono'
  · exact hm.norm.pow 2
  · filter_upwards [] with xi
    rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _), norm_smul, mul_pow,
      Real.norm_eq_abs, sq_abs]
    exact mul_le_mul_of_nonneg_right (f08_025_logDilationFactor_sq_le lam xi hlo hhi)
      (sq_nonneg _)

#print axioms f08_063_logCorrection_mul_sqrt
#print axioms f08_063_weightedCoordinate_ae
#print axioms f08_063_correctedNative_memLp

end
end WeilDefect
