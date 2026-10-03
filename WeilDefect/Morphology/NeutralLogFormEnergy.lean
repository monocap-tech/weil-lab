import WeilDefect.Morphology.NeutralLogFormGraph

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate ComplexInnerProductSpace

/-- The constructed energy coordinate has exactly the canonical logarithmic
density. This is not the squared full-symbol operator energy. -/
theorem neutralLogWeightedL2_sq_norm_ae {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    (fun ξ => ‖neutralLogWeightedL2 f ξ‖ ^ 2) =ᵐ[volume]
      (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) := by
  filter_upwards [neutralLogWeightedL2_coe f] with ξ hf
  rw [hf]
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  simp only [neutralLogWeightedFourier, norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _), mul_pow, Real.sq_sqrt hw]

/-- Weighted L2 pairing realizes the actual mixed logarithmic integrand. -/
theorem neutralLogWeightedL2_mixed_ae {a : ℝ}
    (f g : neutralCanonicalLogFormDomain a) :
    (fun ξ => conj (neutralLogWeightedL2 f ξ) * neutralLogWeightedL2 g ξ) =ᵐ[volume]
      (fun ξ => conj ((𝓕 f.val : RealComplexL2) ξ) *
        (logarithmicFourierWeight ξ : ℂ) * (𝓕 g.val : RealComplexL2) ξ) := by
  filter_upwards [neutralLogWeightedL2_coe f, neutralLogWeightedL2_coe g]
    with ξ hf hg
  rw [hf, hg]
  unfold neutralLogWeightedFourier
  simp only [map_mul, Complex.conj_ofReal]
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have hs : (Real.sqrt (logarithmicFourierWeight ξ) : ℂ) ^ 2 =
      (logarithmicFourierWeight ξ : ℂ) := by
    exact_mod_cast Real.sq_sqrt hw
  calc
    _ = conj ((𝓕 f.val : RealComplexL2) ξ) *
        (Real.sqrt (logarithmicFourierWeight ξ) : ℂ) ^ 2 *
        (𝓕 g.val : RealComplexL2) ξ := by ring
    _ = _ := by rw [hs]

/-- Mixed log energy genuinely converges on the full canonical domain. -/
theorem neutralCanonicalLog_mixed_integrable {a : ℝ}
    (f g : neutralCanonicalLogFormDomain a) :
    Integrable (fun ξ => conj ((𝓕 f.val : RealComplexL2) ξ) *
      (logarithmicFourierWeight ξ : ℂ) * (𝓕 g.val : RealComplexL2) ξ) volume := by
  have h : Integrable (fun ξ => conj (neutralLogWeightedL2 f ξ) *
      neutralLogWeightedL2 g ξ) volume := by
    simpa only [RCLike.inner_apply'] using
      (L2.integrable_inner (𝕜 := ℂ) (neutralLogWeightedL2 f) (neutralLogWeightedL2 g))
  exact h.congr (neutralLogWeightedL2_mixed_ae f g)

/-- Same-domain mixed energy is the inner product of the concrete coordinates. -/
theorem neutralLogWeightedL2_inner {a : ℝ}
    (f g : neutralCanonicalLogFormDomain a) :
    ⟪neutralLogWeightedL2 f, neutralLogWeightedL2 g⟫ =
      ∫ ξ, conj ((𝓕 f.val : RealComplexL2) ξ) *
        (logarithmicFourierWeight ξ : ℂ) * (𝓕 g.val : RealComplexL2) ξ := by
  simp only [L2.inner_def, RCLike.inner_apply']
  exact integral_congr_ae (neutralLogWeightedL2_mixed_ae f g)

/-- Exact diagonal energy attachment for the constructed graph coordinate. -/
theorem neutralLogWeightedL2_norm_sq {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    ‖neutralLogWeightedL2 f‖ ^ 2 =
      ∫ ξ, logarithmicFourierWeight ξ * ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 := by
  have hi : ⟪neutralLogWeightedL2 f, neutralLogWeightedL2 f⟫ =
      (((∫ ξ, logarithmicFourierWeight ξ *
        ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) : ℝ) : ℂ) := by
    rw [neutralLogWeightedL2_inner]
    calc
      _ = ∫ ξ, ((logarithmicFourierWeight ξ *
          ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2 : ℝ) : ℂ) := by
        apply integral_congr_ae
        filter_upwards [] with ξ
        calc
          _ = (logarithmicFourierWeight ξ : ℂ) *
              (conj ((𝓕 f.val : RealComplexL2) ξ) *
                (𝓕 f.val : RealComplexL2) ξ) := by ring
          _ = _ := by
            simp only [Complex.conj_mul', Complex.ofReal_mul, Complex.ofReal_pow]
      _ = _ := integral_complex_ofReal
  rw [norm_sq_eq_re_inner (𝕜 := ℂ), hi]
  rfl

end

end WeilDefect
