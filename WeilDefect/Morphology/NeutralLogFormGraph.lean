import WeilDefect.Morphology.NeutralCanonicalFormDomain

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform

def neutralLogWeightedFourier {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) (ξ : ℝ) : ℂ :=
  (Real.sqrt (logarithmicFourierWeight ξ) : ℂ) *
    (𝓕 f.val : RealComplexL2) ξ

/-- Every canonical domain vector has an actual energy coordinate in L2.
This is one-logarithm form energy, not the squared-symbol operator criterion. -/
theorem neutralLogWeightedFourier_memLp {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    MemLp (neutralLogWeightedFourier f) 2 volume := by
  have hm : AEStronglyMeasurable (neutralLogWeightedFourier f) volume :=
    (Complex.continuous_ofReal.comp
      (Real.continuous_sqrt.comp logarithmicFourierWeight_continuous)).aestronglyMeasurable.mul
      (Lp.aestronglyMeasurable (𝓕 f.val : RealComplexL2))
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  apply f.property.2.congr
  filter_upwards with ξ
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  simp only [neutralLogWeightedFourier, norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _), mul_pow, Real.sq_sqrt hw]

def neutralLogWeightedL2 {a : ℝ} (f : neutralCanonicalLogFormDomain a) :
    RealComplexL2 :=
  (neutralLogWeightedFourier_memLp f).toLp (neutralLogWeightedFourier f)

theorem neutralLogWeightedL2_coe {a : ℝ} (f : neutralCanonicalLogFormDomain a) :
    (neutralLogWeightedL2 f : ℝ → ℂ) =ᵐ[volume] neutralLogWeightedFourier f :=
  (neutralLogWeightedFourier_memLp f).coeFn_toLp

/-- Concrete energy graph, with the physical L2 coordinate retained. -/
def neutralLogFormGraphEmbedding (a : ℝ) :
    neutralCanonicalLogFormDomain a →ₗ[ℂ] (RealComplexL2 × RealComplexL2) where
  toFun f := (f.val, neutralLogWeightedL2 f)
  map_add' f g := by
    apply Prod.ext
    · rfl
    · apply Lp.ext
      filter_upwards [neutralLogWeightedL2_coe (f + g),
        neutralLogWeightedL2_coe f, neutralLogWeightedL2_coe g,
        Lp.coeFn_add (neutralLogWeightedL2 f) (neutralLogWeightedL2 g),
        Lp.coeFn_add (𝓕 f.val : RealComplexL2) (𝓕 g.val : RealComplexL2)]
        with ξ hfg hf hg hadd hfour
      change neutralLogWeightedL2 (f + g) ξ =
        (neutralLogWeightedL2 f + neutralLogWeightedL2 g) ξ
      rw [hfg, hadd]
      simp only [Pi.add_apply]
      rw [hf, hg]
      unfold neutralLogWeightedFourier
      have hFT : (𝓕 (f + g).val : RealComplexL2) = 𝓕 f.val + 𝓕 g.val :=
        (Lp.fourierTransformₗᵢ ℝ ℂ).map_add f.val g.val
      rw [hFT, hfour]
      simp only [Pi.add_apply, mul_add]
  map_smul' z f := by
    apply Prod.ext
    · rfl
    · apply Lp.ext
      filter_upwards [neutralLogWeightedL2_coe (z • f), neutralLogWeightedL2_coe f,
        Lp.coeFn_smul z (neutralLogWeightedL2 f),
        Lp.coeFn_smul z (𝓕 f.val : RealComplexL2)] with ξ hzf hf hz hfour
      change neutralLogWeightedL2 (z • f) ξ = (z • neutralLogWeightedL2 f) ξ
      rw [hzf, hz]
      simp only [Pi.smul_apply]
      rw [hf]
      unfold neutralLogWeightedFourier
      have hFT : (𝓕 (z • f).val : RealComplexL2) = z • 𝓕 f.val :=
        (Lp.fourierTransformₗᵢ ℝ ℂ).map_smul z f.val
      rw [hFT, hfour]
      simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
      ring

theorem neutralLogFormGraphEmbedding_injective (a : ℝ) :
    Function.Injective (neutralLogFormGraphEmbedding a) := by
  intro f g h
  apply Subtype.ext
  exact congrArg Prod.fst h

/-- A genuine graph norm on the canonical domain. Its inherited L2 subtype
norm is not redefined; this explicit energy norm is the source-topology candidate. -/
def neutralLogFormGraphNorm {a : ℝ} (f : neutralCanonicalLogFormDomain a) : ℝ :=
  ‖neutralLogFormGraphEmbedding a f‖

theorem neutralLogFormGraphNorm_eq_max {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    neutralLogFormGraphNorm f = max ‖f.val‖ ‖neutralLogWeightedL2 f‖ := rfl

theorem neutralLogFormGraphNorm_add_le {a : ℝ}
    (f g : neutralCanonicalLogFormDomain a) :
    neutralLogFormGraphNorm (f + g) ≤
      neutralLogFormGraphNorm f + neutralLogFormGraphNorm g := by
  unfold neutralLogFormGraphNorm
  rw [map_add]
  exact norm_add_le _ _

theorem neutralLogFormGraphNorm_smul {a : ℝ} (z : ℂ)
    (f : neutralCanonicalLogFormDomain a) :
    neutralLogFormGraphNorm (z • f) = ‖z‖ * neutralLogFormGraphNorm f := by
  unfold neutralLogFormGraphNorm
  rw [map_smul, norm_smul]

theorem neutralLogFormGraphNorm_eq_zero_iff {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    neutralLogFormGraphNorm f = 0 ↔ f = 0 := by
  unfold neutralLogFormGraphNorm
  rw [norm_eq_zero, ← (neutralLogFormGraphEmbedding a).map_zero]
  exact (neutralLogFormGraphEmbedding_injective a).eq_iff

end

end WeilDefect
