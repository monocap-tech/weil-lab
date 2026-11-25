import WeilDefect.Generated.F08.OriginalWindowNativeWeightedSmoothing
import WeilDefect.Generated.F08.OriginalFormDomainEnergyReceiver

namespace WeilDefect
noncomputable section

open MeasureTheory Filter FourierTransform
open scoped FourierTransform Topology

/-- Sharp restriction does not change a vector already supported in the
original physical window. No general cutoff regularity is asserted. -/
theorem f08_068_supportedWindow_eq (a : ℝ) (f : RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) :
    f08_023_originalWindowL2 a f = f := by
  apply Lp.ext
  filter_upwards [f08_023_original_window_native_ae a f, hf] with x hx hfx
  rw [hx]
  by_cases hin : x ∈ Set.Icc (-a) a
  · simp [neutralWindowRepresentative, hin]
  · simp [neutralWindowRepresentative, hin, hfx hin]

/-- The genuine smooth physical convolution retains finite original
logarithmic energy and belongs to the actual collar domain. -/
theorem f08_068_smoothedDomain_mem {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) (φ : ContDiffBump (0 : ℝ)) :
    f08_021_originalSmoothedWindowL2 a f.val φ ∈
      neutralCanonicalLogFormDomain (a + φ.rOut) := by
  let g := f08_021_originalSmoothedWindowL2 a f.val φ
  have hw := f08_068_supportedWindow_eq a f.val f.property.1
  have hp : (𝓕 g : RealComplexL2) =ᵐ[volume]
      (fun xi : ℝ => (𝓕 f.val : RealComplexL2) xi *
        f08_015_originalMollifierMultiplier φ xi) := by
    filter_upwards [f08_021_original_smoothed_window_native_fourier_product_ae a f.val φ,
      f08_023_original_window_native_fourier_ae a f.val] with xi hg hf
    rw [hw] at hf
    change (𝓕 g : RealComplexL2) xi = _
    rw [hg, hf]
  refine ⟨f08_021_original_smoothed_window_native_ae_support a f.val φ, ?_⟩
  change Integrable (fun xi : ℝ => logarithmicFourierWeight xi *
    ‖(𝓕 g : RealComplexL2) xi‖ ^ 2) volume
  apply f.property.2.mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 g : RealComplexL2)).norm.pow 2)
  · filter_upwards [hp] with xi hx
    have hweight : 0 ≤ logarithmicFourierWeight xi :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight xi)
    change ‖logarithmicFourierWeight xi * ‖(𝓕 g : RealComplexL2) xi‖ ^ 2‖ ≤
      logarithmicFourierWeight xi * ‖(𝓕 f.val : RealComplexL2) xi‖ ^ 2
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hweight (sq_nonneg _)), hx,
      norm_mul, mul_pow]
    have hM := f08_015_original_mollifier_multiplier_contraction φ xi
    have hM2 : ‖f08_015_originalMollifierMultiplier φ xi‖ ^ 2 ≤ 1 := by
      have h := mul_nonneg (sub_nonneg.mpr hM)
        (add_nonneg (norm_nonneg (f08_015_originalMollifierMultiplier φ xi)) zero_le_one)
      nlinarith
    apply mul_le_mul_of_nonneg_left _ hweight
    simpa only [mul_one] using
      mul_le_mul_of_nonneg_left hM2 (sq_nonneg ‖(𝓕 f.val : RealComplexL2) xi‖)

def f08_068_smoothedDomain {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) (φ : ContDiffBump (0 : ℝ)) :
    neutralCanonicalLogFormDomain (a + φ.rOut) :=
  ⟨_, f08_068_smoothedDomain_mem f φ⟩

/-- Strong approximation in the original weighted coordinate, on the
actual smooth convolution classes in their collar domains. -/
theorem f08_068_weightedSmoothing_tendsto {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    Tendsto (fun n : ℕ =>
      neutralLogWeightedL2 (f08_068_smoothedDomain f (f08_017_shrinkingBump n)))
      atTop (𝓝 (neutralLogWeightedL2 f)) := by
  have hw := f08_068_supportedWindow_eq a f.val f.property.1
  have henergy : Integrable (fun xi : ℝ => logarithmicFourierWeight xi *
      ‖(𝓕 (f08_023_originalWindowL2 a f.val) : RealComplexL2) xi‖ ^ 2) volume := by
    rw [hw]
    exact f.property.2
  have hlim := f08_023_original_window_native_weighted_smoothing_tendsto_zero a f.val henergy
  rw [hw] at hlim
  have heq (n : ℕ) :
      ‖neutralLogWeightedL2 (f08_068_smoothedDomain f (f08_017_shrinkingBump n)) -
        neutralLogWeightedL2 f‖ ^ 2 =
      ∫ xi : ℝ, logarithmicFourierWeight xi *
        ‖(𝓕 (f08_021_originalSmoothedWindowL2 a f.val
          (f08_017_shrinkingBump n)) : RealComplexL2) xi -
            (𝓕 f.val : RealComplexL2) xi‖ ^ 2 ∂volume := by
    rw [f08_064_originalWeightedDifference_norm_sq]
    apply integral_congr_ae
    filter_upwards [] with xi
    let g := f08_068_smoothedDomain f (f08_017_shrinkingBump n)
    change ‖neutralLogWeightedFourier g xi - neutralLogWeightedFourier f xi‖ ^ 2 = _
    unfold neutralLogWeightedFourier
    rw [← mul_sub, norm_mul, mul_pow, Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (Real.sqrt_nonneg _),
      Real.sq_sqrt (le_trans (by norm_num) (one_le_logarithmicFourierWeight xi))]
    rfl
  rw [Metric.tendsto_nhds]
  intro ε hε
  filter_upwards [(Metric.tendsto_nhds.mp hlim) (ε ^ 2) (sq_pos_of_pos hε)] with n hn
  rw [Real.dist_eq, sub_zero] at hn
  rw [dist_eq_norm]
  have hsq := (heq n).trans_lt (lt_of_le_of_lt (le_abs_self _) hn)
  nlinarith [norm_nonneg (neutralLogWeightedL2 (f08_068_smoothedDomain f
    (f08_017_shrinkingBump n)) - neutralLogWeightedL2 f)]

#print axioms f08_068_supportedWindow_eq
#print axioms f08_068_smoothedDomain_mem
#print axioms f08_068_weightedSmoothing_tendsto

end
end WeilDefect
