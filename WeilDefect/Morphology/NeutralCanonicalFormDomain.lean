import WeilDefect.Morphology.NeutralWeilSourceDiagonal
import WeilDefect.Morphology.NeutralSourceOperatorDomain

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform

theorem logarithmicFourierWeight_continuous : Continuous logarithmicFourierWeight := by
  unfold logarithmicFourierWeight
  apply Continuous.log (by fun_prop)
  intro ξ
  exact ne_of_gt (add_pos_of_pos_of_nonneg (Real.exp_pos 1) (abs_nonneg ξ))

/-- Finite logarithmic Fourier energy is stable under actual L2 addition. -/
theorem finiteLogFourierEnergy_add {f g : RealComplexL2}
    (hf : Integrable (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume)
    (hg : Integrable (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 g : RealComplexL2) ξ‖ ^ 2) volume) :
    Integrable (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 (f + g) : RealComplexL2) ξ‖ ^ 2) volume := by
  apply ((hf.add hg).const_mul 2).mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 (f + g) : RealComplexL2)).norm.pow 2)
  · filter_upwards [Lp.coeFn_add (𝓕 f : RealComplexL2) (𝓕 g : RealComplexL2)] with ξ hξ
    have hadd : (𝓕 (f + g) : RealComplexL2) = 𝓕 f + 𝓕 g :=
      (Lp.fourierTransformₗᵢ ℝ ℂ).map_add f g
    rw [hadd, hξ]
    simp only [Pi.add_apply]
    have hw : 0 ≤ logarithmicFourierWeight ξ :=
      le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hw (sq_nonneg _))]
    have hb : ‖(𝓕 f : RealComplexL2) ξ + (𝓕 g : RealComplexL2) ξ‖ ^ 2 ≤
        2 * (‖(𝓕 f : RealComplexL2) ξ‖ ^ 2 + ‖(𝓕 g : RealComplexL2) ξ‖ ^ 2) := by
      have hn := norm_add_le ((𝓕 f : RealComplexL2) ξ) ((𝓕 g : RealComplexL2) ξ)
      nlinarith [norm_nonneg ((𝓕 f : RealComplexL2) ξ + (𝓕 g : RealComplexL2) ξ),
        norm_nonneg ((𝓕 f : RealComplexL2) ξ), norm_nonneg ((𝓕 g : RealComplexL2) ξ),
        sq_nonneg (‖(𝓕 f : RealComplexL2) ξ‖ - ‖(𝓕 g : RealComplexL2) ξ‖)]
    nlinarith [mul_le_mul_of_nonneg_left hb hw]

/-- Complex scaling preserves the genuine logarithmic energy integral. -/
theorem finiteLogFourierEnergy_smul (z : ℂ) {f : RealComplexL2}
    (hf : Integrable (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume) :
    Integrable (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 (z • f) : RealComplexL2) ξ‖ ^ 2) volume := by
  apply (hf.const_mul (‖z‖ ^ 2)).congr
  filter_upwards [Lp.coeFn_smul z (𝓕 f : RealComplexL2)] with ξ hξ
  rw [fourier_smul, hξ]
  simp only [Pi.smul_apply, norm_smul]
  ring

/-- The full concrete supported logarithmic form domain. No source quadratic
identity or carrier energy is included in its definition. -/
def neutralCanonicalLogFormDomain (a : ℝ) : Submodule ℂ RealComplexL2 where
  carrier := {f | (∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) ∧
    Integrable (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume}
  zero_mem' := by
    constructor
    · filter_upwards [Lp.coeFn_zero ℂ 2 volume] with x hx
      intro _
      exact hx
    · apply (integrable_zero ℝ ℝ volume).congr
      filter_upwards [Lp.coeFn_zero ℂ 2 volume] with ξ hξ
      have hzero : (𝓕 (0 : RealComplexL2) : RealComplexL2) = 0 :=
        (Lp.fourierTransformₗᵢ ℝ ℂ).map_zero
      rw [hzero]
      simp only [hξ, Pi.zero_apply, norm_zero, zero_pow (by decide : 2 ≠ 0), mul_zero]
  add_mem' := by
    intro f g hf hg
    constructor
    · filter_upwards [hf.1, hg.1, Lp.coeFn_add f g] with x hfx hgx hx
      intro houtside
      simp only [hx, Pi.add_apply, hfx houtside, hgx houtside, zero_add]
    · exact finiteLogFourierEnergy_add hf.2 hg.2
  smul_mem' := by
    intro z f hf
    constructor
    · filter_upwards [hf.1, Lp.coeFn_smul z f] with x hfx hx
      intro houtside
      simp only [hx, Pi.smul_apply, hfx houtside, smul_zero]
    · exact finiteLogFourierEnergy_smul z hf.2

theorem mem_neutralCanonicalLogFormDomain_iff (a : ℝ) (f : RealComplexL2) :
    f ∈ neutralCanonicalLogFormDomain a ↔
      (∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) ∧
      Integrable (fun ξ => logarithmicFourierWeight ξ * ‖(𝓕 f : RealComplexL2) ξ‖ ^ 2) volume :=
  Iff.rfl

/-- Every lawful source-domain attachment lies inside the concrete domain.
This is containment, not identification of the imported source form. -/
theorem sourceFormDomain_le_canonical
    {c : ℝ} {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    {carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs} {a : ℝ}
    (D : NeutralSourceFormDomainAttachment carrier a) :
    D.domain ≤ neutralCanonicalLogFormDomain a := by
  intro f hf
  exact ⟨D.supported ⟨f, hf⟩, D.logEnergy ⟨f, hf⟩⟩

/-- Attach the actual carrier to the full concrete domain from its single
finite-energy witness. Physical support is derived from the carrier itself. -/
def neutralCanonicalSourceFormDomainAttachment
    {c : ℝ} {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a : ℝ} (hca : c ≤ a)
    (henergy : Integrable (fun ξ => logarithmicFourierWeight ξ *
      ‖(𝓕 carrier.l2Mode : RealComplexL2) ξ‖ ^ 2) volume) :
    NeutralSourceFormDomainAttachment carrier a where
  domain := neutralCanonicalLogFormDomain a
  supported := fun f => f.property.1
  carrier_mem := by
    refine ⟨?_, henergy⟩
    filter_upwards [carrier.h_memLp.coeFn_toLp] with x hx
    intro houtside
    change carrier.h_memLp.toLp carrier.h x = 0
    rw [hx]
    apply carrier.representative_eq_zero_of_not_mem
    intro hmem
    apply houtside
    exact Set.Icc_subset_Icc (neg_le_neg hca) hca hmem
  logEnergy := fun f => f.property.2

end

end WeilDefect
