import WeilDefect.Arithmetic.ActualZetaIV106E19LRawResidual

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap FourierTransform
open scoped InnerProduct FourierTransform ComplexConjugate

/-- The inverse square-root weight is a real multiplier, hence
self-adjoint on weighted-coordinate L2. -/
theorem neutralIV106E19MUnweight_pair (f g : RealComplexL2) :
    inner ℂ (neutralLogUnweight f) g =
      inner ℂ f (neutralLogUnweight g) := by
  rw [L2.inner_def,L2.inner_def]
  apply integral_congr_ae
  filter_upwards [neutralLogUnweight_coe f,neutralLogUnweight_coe g] with ξ hf hg
  rw [hf,hg]
  simp only [RCLike.inner_apply',neutralLogInverseWeight,map_mul,map_inv₀,
    Complex.conj_ofReal]
  ring

/-- The original physical reconstruction adjoint is unweighting
after the unitary physical Fourier transform. -/
theorem neutralIV106E19MRaw_eq (f : RealComplexL2) :
    neutralIV106E19LRawColumn f = neutralLogUnweight (𝓕 f) := by
  let d := neutralIV106E19LRawColumn f-neutralLogUnweight (𝓕 f)
  have hp (q : RealComplexL2) :
      inner ℂ (neutralIV106E19LRawColumn f) q =
      inner ℂ (neutralLogUnweight (𝓕 f)) q := by
    unfold neutralIV106E19LRawColumn
    rw [adjoint_inner_left,neutralIV106E19MUnweight_pair]
    have h := (Lp.fourierTransformₗᵢ ℝ ℂ).inner_map_map f
      (neutralLogPhysical q)
    change inner ℂ (𝓕 f : RealComplexL2)
      (𝓕 (neutralLogPhysical q) : RealComplexL2) = _ at h
    rw [neutralLogPhysical_fourier] at h
    exact h.symm
  have hz : inner ℂ d d = 0 := by
    dsimp only [d]
    rw [inner_sub_left,hp,sub_self]
  exact sub_eq_zero.mp (inner_self_eq_zero.mp hz)

theorem neutralIV106E19MRaw_coe (f : RealComplexL2) :
    (neutralIV106E19LRawColumn f : ℝ → ℂ) =ᵐ[volume]
      fun ξ => neutralLogInverseWeight ξ*(𝓕 f : RealComplexL2) ξ := by
  rw [neutralIV106E19MRaw_eq]
  exact neutralLogUnweight_coe _

theorem neutralIV106E19MRaw_pair (f g : RealComplexL2) :
    inner ℂ (neutralIV106E19LRawColumn f) (neutralIV106E19LRawColumn g) =
      ∫ ξ, conj ((𝓕 f : RealComplexL2) ξ) *
        (logarithmicFourierWeight ξ : ℂ)⁻¹*(𝓕 g : RealComplexL2) ξ := by
  rw [L2.inner_def]
  apply integral_congr_ae
  filter_upwards [neutralIV106E19MRaw_coe f,neutralIV106E19MRaw_coe g] with ξ hf hg
  rw [hf,hg]
  simp only [RCLike.inner_apply',neutralLogInverseWeight,map_mul,map_inv₀,
    Complex.conj_ofReal]
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    zero_le_one.trans (one_le_logarithmicFourierWeight ξ)
  have hs : (Real.sqrt (logarithmicFourierWeight ξ):ℂ)^2 =
      (logarithmicFourierWeight ξ:ℂ) := by
    exact_mod_cast Real.sq_sqrt hw
  rw [← hs,inv_pow]
  ring

/-- The raw column norm is bounded by its physical L2 norm.
The additional carrier projection is not included here. -/
theorem neutralIV106E19MRaw_norm (f : RealComplexL2) :
    ‖neutralIV106E19LRawColumn f‖ ≤ ‖f‖ := by
  calc
    _ ≤ ‖(𝓕 f : RealComplexL2)‖ := by
      apply Lp.norm_le_norm_of_ae_le
      filter_upwards [neutralIV106E19MRaw_coe f] with ξ hξ
      rw [hξ,norm_mul]
      simpa using mul_le_mul_of_nonneg_right
        (neutralLogInverseWeight_norm_le ξ) (norm_nonneg ((𝓕 f : RealComplexL2) ξ))
    _ = _ := (Lp.fourierTransformₗᵢ ℝ ℂ).norm_map f

#print axioms neutralIV106E19MUnweight_pair
#print axioms neutralIV106E19MRaw_eq
#print axioms neutralIV106E19MRaw_coe
#print axioms neutralIV106E19MRaw_pair
#print axioms neutralIV106E19MRaw_norm
end
end WeilDefect
