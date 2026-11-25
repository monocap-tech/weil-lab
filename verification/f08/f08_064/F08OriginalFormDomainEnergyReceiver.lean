import WeilDefect.Morphology.NeutralLogHilbertCarrier
import WeilDefect.Generated.F08.OriginalNativeL2SquareIntegral

namespace WeilDefect
noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform

/-- The actual original logarithmic density equals the square of the
weighted Fourier representative for every native physical L² vector. -/
theorem f08_064_weightedFourier_sq (g : RealComplexL2) (xi : ℝ) :
    ‖(Real.sqrt (logarithmicFourierWeight xi) : ℂ) *
        (𝓕 g : RealComplexL2) xi‖ ^ 2 =
      logarithmicFourierWeight xi * ‖(𝓕 g : RealComplexL2) xi‖ ^ 2 := by
  have hw : 0 ≤ logarithmicFourierWeight xi :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight xi)
  simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _), mul_pow, Real.sq_sqrt hw]

/-- Finite energy is received from a genuine square-integrable weighted
coordinate, rather than being assumed for the target physical vector. -/
theorem f08_064_originalDomain_mem_of_weighted_memLp (a : ℝ) (g : RealComplexL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → g x = 0)
    (hk : MemLp (fun xi : ℝ => (Real.sqrt (logarithmicFourierWeight xi) : ℂ) *
      (𝓕 g : RealComplexL2) xi) 2 volume) :
    g ∈ neutralCanonicalLogFormDomain a := by
  refine ⟨hs, ?_⟩
  have hi := (memLp_two_iff_integrable_sq_norm hk.aestronglyMeasurable).mp hk
  apply hi.congr
  filter_upwards [] with xi
  exact f08_064_weightedFourier_sq g xi

/-- Exact weighted-coordinate difference norm, allowing different
original physical support radii. No convergence assumption is needed. -/
theorem f08_064_originalWeightedDifference_norm_sq {a b : ℝ}
    (f : neutralCanonicalLogFormDomain a) (g : neutralCanonicalLogFormDomain b) :
    ‖neutralLogWeightedL2 g - neutralLogWeightedL2 f‖ ^ 2 =
      ∫ xi : ℝ, ‖neutralLogWeightedFourier g xi -
        neutralLogWeightedFourier f xi‖ ^ 2 ∂volume := by
  rw [f08_052_originalL2_norm_sq_eq_integral]
  apply integral_congr_ae
  filter_upwards [Lp.coeFn_sub (neutralLogWeightedL2 g) (neutralLogWeightedL2 f),
    neutralLogWeightedL2_coe g, neutralLogWeightedL2_coe f] with xi hd hg hf
  simp only [hd, Pi.sub_apply, hg, hf]

#print axioms f08_064_weightedFourier_sq
#print axioms f08_064_originalDomain_mem_of_weighted_memLp
#print axioms f08_064_originalWeightedDifference_norm_sq

end
end WeilDefect
