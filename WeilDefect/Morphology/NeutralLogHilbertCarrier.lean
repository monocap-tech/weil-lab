import WeilDefect.Morphology.NeutralLogFormEnergy
import Mathlib.Topology.Algebra.Module.ClosedSubmodule

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform

/-- Pointwise multiplication by an actual measurable contraction. -/
private def contractiveMultiplyMemLp
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (hb : ∀ x, ‖m x‖ ≤ 1) (f : RealComplexL2) :
    MemLp (fun x => m x * f x) 2 volume := by
  apply (Lp.memLp f).of_le (hm.mul (Lp.aestronglyMeasurable f))
  filter_upwards [] with x
  simpa only [Pi.mul_apply, norm_mul, one_mul] using
    mul_le_mul_of_nonneg_right (hb x) (norm_nonneg (f x))

private def contractiveMultiplyLinear
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (hb : ∀ x, ‖m x‖ ≤ 1) : RealComplexL2 →ₗ[ℂ] RealComplexL2 where
  toFun f := (contractiveMultiplyMemLp m hm hb f).toLp (fun x => m x * f x)
  map_add' f g := by
    apply Lp.ext
    filter_upwards [(contractiveMultiplyMemLp m hm hb (f+g)).coeFn_toLp,
      (contractiveMultiplyMemLp m hm hb f).coeFn_toLp,
      (contractiveMultiplyMemLp m hm hb g).coeFn_toLp,
      Lp.coeFn_add f g,
      Lp.coeFn_add ((contractiveMultiplyMemLp m hm hb f).toLp _)
        ((contractiveMultiplyMemLp m hm hb g).toLp _)] with x hfg hf hg hadd hout
    simp only [hfg, hout, Pi.add_apply, hf, hg, hadd, mul_add]
  map_smul' z f := by
    apply Lp.ext
    filter_upwards [(contractiveMultiplyMemLp m hm hb (z • f)).coeFn_toLp,
      (contractiveMultiplyMemLp m hm hb f).coeFn_toLp,
      Lp.coeFn_smul z f,
      Lp.coeFn_smul z ((contractiveMultiplyMemLp m hm hb f).toLp _)]
      with x hzf hf hz hout
    change (contractiveMultiplyMemLp m hm hb (z • f)).toLp _ x =
      (z • (contractiveMultiplyMemLp m hm hb f).toLp _) x
    rw [hzf, hout, hz, hf]
    simp only [Pi.smul_apply, smul_eq_mul]
    ring

private theorem contractiveMultiplyLinear_norm_le
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (hb : ∀ x, ‖m x‖ ≤ 1) (f : RealComplexL2) :
    ‖contractiveMultiplyLinear m hm hb f‖ ≤ ‖f‖ := by
  apply Lp.norm_le_norm_of_ae_le
  filter_upwards [(contractiveMultiplyMemLp m hm hb f).coeFn_toLp] with x hx
  change ‖(contractiveMultiplyMemLp m hm hb f).toLp _ x‖ ≤ ‖f x‖
  rw [hx, norm_mul]
  simpa only [one_mul] using
    mul_le_mul_of_nonneg_right (hb x) (norm_nonneg (f x))

private def contractiveMultiply
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (hb : ∀ x, ‖m x‖ ≤ 1) : RealComplexL2 →L[ℂ] RealComplexL2 :=
  (contractiveMultiplyLinear m hm hb).mkContinuous 1
    (fun f => by simpa only [one_mul] using contractiveMultiplyLinear_norm_le m hm hb f)

private theorem contractiveMultiply_coe
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (hb : ∀ x, ‖m x‖ ≤ 1) (f : RealComplexL2) :
    (contractiveMultiply m hm hb f : ℝ → ℂ) =ᵐ[volume] fun x => m x * f x :=
  (contractiveMultiplyMemLp m hm hb f).coeFn_toLp

def neutralLogInverseWeight (ξ : ℝ) : ℂ :=
  (Real.sqrt (logarithmicFourierWeight ξ) : ℂ)⁻¹

theorem neutralLogInverseWeight_norm_le (ξ : ℝ) :
    ‖neutralLogInverseWeight ξ‖ ≤ 1 := by
  have hs : 1 ≤ Real.sqrt (logarithmicFourierWeight ξ) := by
    simpa using Real.sqrt_le_sqrt (one_le_logarithmicFourierWeight ξ)
  unfold neutralLogInverseWeight
  rw [norm_inv, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _)]
  exact (inv_le_one₀ (by linarith : 0 < Real.sqrt (logarithmicFourierWeight ξ))).mpr hs

theorem neutralLogInverseWeight_measurable :
    AEStronglyMeasurable neutralLogInverseWeight volume := by
  unfold neutralLogInverseWeight
  exact (Complex.continuous_ofReal.comp
    (Real.continuous_sqrt.comp logarithmicFourierWeight_continuous)).measurable.inv.aestronglyMeasurable

/-- Actual bounded inverse of the square-root logarithmic weight. -/
def neutralLogUnweight : RealComplexL2 →L[ℂ] RealComplexL2 :=
  contractiveMultiply neutralLogInverseWeight neutralLogInverseWeight_measurable
    neutralLogInverseWeight_norm_le

theorem neutralLogUnweight_coe (k : RealComplexL2) :
    (neutralLogUnweight k : ℝ → ℂ) =ᵐ[volume]
      fun ξ => neutralLogInverseWeight ξ * k ξ :=
  contractiveMultiply_coe _ _ _ k

/-- Physical reconstruction from the genuine weighted Fourier coordinate. -/
def neutralLogPhysical : RealComplexL2 →L[ℂ] RealComplexL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).symm.toContinuousLinearEquiv.toContinuousLinearMap ∘L
    neutralLogUnweight

theorem neutralLogPhysical_fourier (k : RealComplexL2) :
    (𝓕 (neutralLogPhysical k) : RealComplexL2) = neutralLogUnweight k :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).apply_symm_apply _

private theorem neutralLogSqrt_ne_zero (ξ : ℝ) :
    (Real.sqrt (logarithmicFourierWeight ξ) : ℂ) ≠ 0 := by
  have hs : 0 < Real.sqrt (logarithmicFourierWeight ξ) :=
    Real.sqrt_pos.mpr (lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight ξ))
  exact_mod_cast ne_of_gt hs

theorem neutralLogPhysical_weighted {a : ℝ}
    (f : neutralCanonicalLogFormDomain a) :
    neutralLogPhysical (neutralLogWeightedL2 f) = f.val := by
  apply (Lp.fourierTransformₗᵢ ℝ ℂ).injective
  change (𝓕 (neutralLogPhysical (neutralLogWeightedL2 f)) : RealComplexL2) = 𝓕 f.val
  rw [neutralLogPhysical_fourier]
  apply Lp.ext
  filter_upwards [neutralLogUnweight_coe (neutralLogWeightedL2 f),
    neutralLogWeightedL2_coe f] with ξ hk hf
  rw [hk, hf]
  unfold neutralLogInverseWeight neutralLogWeightedFourier
  rw [← mul_assoc, inv_mul_cancel₀ (neutralLogSqrt_ne_zero ξ), one_mul]

private def neutralOutsideWeight (a x : ℝ) : ℂ :=
  (Set.Icc (-a) a)ᶜ.indicator (fun _ => (1 : ℂ)) x

private theorem neutralOutsideWeight_measurable (a : ℝ) :
    AEStronglyMeasurable (neutralOutsideWeight a) volume :=
  (aestronglyMeasurable_const.indicator measurableSet_Icc.compl)

private theorem neutralOutsideWeight_bound (a x : ℝ) :
    ‖neutralOutsideWeight a x‖ ≤ 1 := by
  unfold neutralOutsideWeight
  by_cases hx : x ∈ (Set.Icc (-a) a)ᶜ <;> simp [hx]

private def neutralOutsideRestriction (a : ℝ) : RealComplexL2 →L[ℂ] RealComplexL2 :=
  contractiveMultiply (neutralOutsideWeight a) (neutralOutsideWeight_measurable a)
    (neutralOutsideWeight_bound a)

private theorem neutralOutsideRestriction_zero_iff (a : ℝ) (f : RealComplexL2) :
    neutralOutsideRestriction a f = 0 ↔
      ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0 := by
  constructor
  · intro hz
    filter_upwards [contractiveMultiply_coe (neutralOutsideWeight a)
      (neutralOutsideWeight_measurable a) (neutralOutsideWeight_bound a) f,
      Lp.coeFn_zero ℂ 2 volume] with x hx hzero
    intro hout
    have hh : neutralOutsideRestriction a f x = 0 := by rw [hz]; exact hzero
    change contractiveMultiply (neutralOutsideWeight a)
      (neutralOutsideWeight_measurable a) (neutralOutsideWeight_bound a) f x = 0 at hh
    rw [hx] at hh
    simpa [neutralOutsideWeight, hout] using hh
  · intro hf
    apply Lp.ext
    filter_upwards [hf, contractiveMultiply_coe (neutralOutsideWeight a)
      (neutralOutsideWeight_measurable a) (neutralOutsideWeight_bound a) f,
      Lp.coeFn_zero ℂ 2 volume] with x hfx hx hzero
    change contractiveMultiply (neutralOutsideWeight a)
      (neutralOutsideWeight_measurable a) (neutralOutsideWeight_bound a) f x = (0 : RealComplexL2) x
    rw [hx, hzero]
    by_cases hout : x ∉ Set.Icc (-a) a
    · simp [neutralOutsideWeight, hout, hfx hout]
    · simp [neutralOutsideWeight, hout]

/-- Closed weighted-coordinate realization of the supported logarithmic
form carrier. Closure is proved by the kernel of a concrete bounded map. -/
def neutralLogHilbertSubmodule (a : ℝ) : ClosedSubmodule ℂ RealComplexL2 where
  toSubmodule := (neutralOutsideRestriction a ∘L neutralLogPhysical).ker
  isClosed' := (neutralOutsideRestriction a ∘L neutralLogPhysical).isClosed_ker

abbrev NeutralLogHilbertCarrier (a : ℝ) :=
  (neutralLogHilbertSubmodule a).toSubmodule

theorem neutralLogHilbertCarrier_supported {a : ℝ}
    (k : NeutralLogHilbertCarrier a) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → neutralLogPhysical k.val x = 0 :=
  (neutralOutsideRestriction_zero_iff a _).mp k.property

/-- Every carrier coordinate has actual logarithmic energy. No spectral
operator-domain or source-identity premise is supplied. -/
theorem neutralLogPhysical_energy (k : RealComplexL2) :
    Integrable (fun ξ => logarithmicFourierWeight ξ *
      ‖(𝓕 (neutralLogPhysical k) : RealComplexL2) ξ‖ ^ 2) volume := by
  have hk := (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable k)).mp (Lp.memLp k)
  apply hk.congr
  filter_upwards [neutralLogUnweight_coe k] with ξ hξ
  rw [neutralLogPhysical_fourier, hξ]
  unfold neutralLogInverseWeight
  have hs := neutralLogSqrt_ne_zero ξ
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have hpos : 0 < Real.sqrt (logarithmicFourierWeight ξ) :=
    Real.sqrt_pos.mpr (lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight ξ))
  simp only [norm_mul, norm_inv, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _), mul_pow]
  rw [inv_pow, Real.sq_sqrt hw]
  rw [← mul_assoc, mul_inv_cancel₀ (ne_of_gt
    (lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight ξ))), one_mul]

/-- Concrete supported finite-energy vector, reconstructed without any
stronger regularity assumption. -/
def neutralLogHilbertToCanonical {a : ℝ} (k : NeutralLogHilbertCarrier a) :
    neutralCanonicalLogFormDomain a :=
  ⟨neutralLogPhysical k.val, neutralLogHilbertCarrier_supported k,
    neutralLogPhysical_energy k.val⟩

def neutralCanonicalToLogHilbert {a : ℝ} (f : neutralCanonicalLogFormDomain a) :
    NeutralLogHilbertCarrier a := by
  refine ⟨neutralLogWeightedL2 f, ?_⟩
  change neutralOutsideRestriction a (neutralLogPhysical (neutralLogWeightedL2 f)) = 0
  rw [neutralLogPhysical_weighted]
  exact (neutralOutsideRestriction_zero_iff a f.val).mpr f.property.1

theorem neutralLogHilbertToCanonical_leftInverse {a : ℝ} :
    Function.LeftInverse neutralLogHilbertToCanonical
      (neutralCanonicalToLogHilbert (a := a)) := by
  intro f
  apply Subtype.ext
  exact neutralLogPhysical_weighted f

theorem neutralLogHilbertToCanonical_rightInverse {a : ℝ} :
    Function.RightInverse neutralLogHilbertToCanonical
      (neutralCanonicalToLogHilbert (a := a)) := by
  intro k
  apply Subtype.ext
  apply Lp.ext
  filter_upwards [neutralLogWeightedL2_coe (neutralLogHilbertToCanonical k),
    neutralLogUnweight_coe k.val] with ξ hw hk
  change neutralLogWeightedL2 (neutralLogHilbertToCanonical k) ξ = k.val ξ
  rw [hw]
  unfold neutralLogWeightedFourier neutralLogHilbertToCanonical
  rw [neutralLogPhysical_fourier, hk]
  unfold neutralLogInverseWeight
  rw [← mul_assoc, mul_inv_cancel₀ (neutralLogSqrt_ne_zero ξ), one_mul]

/-- Completeness comes from the concrete closed kernel in weighted L2. -/
instance neutralLogHilbertCarrier_complete (a : ℝ) :
    CompleteSpace (NeutralLogHilbertCarrier a) :=
  (neutralLogHilbertSubmodule a).isClosed.completeSpace_coe

/-- The new Hilbert norm is exactly logarithmic Fourier energy, rather than
the ordinary L2 norm inherited by the canonical-domain subtype. -/
theorem neutralLogHilbertCarrier_norm_sq {a : ℝ}
    (k : NeutralLogHilbertCarrier a) :
    ‖k‖ ^ 2 = ∫ ξ, logarithmicFourierWeight ξ *
      ‖(𝓕 (neutralLogPhysical k.val) : RealComplexL2) ξ‖ ^ 2 := by
  have h := neutralLogWeightedL2_norm_sq (neutralLogHilbertToCanonical k)
  have heq : neutralLogWeightedL2 (neutralLogHilbertToCanonical k) = k.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse k)
  rw [heq] at h
  exact h

/-- Exact domain identification, with no source diagonal or spectral L2
hypothesis added to either side. -/
def neutralLogHilbertCanonicalEquiv (a : ℝ) :
    neutralCanonicalLogFormDomain a ≃ NeutralLogHilbertCarrier a where
  toFun := neutralCanonicalToLogHilbert
  invFun := neutralLogHilbertToCanonical
  left_inv := neutralLogHilbertToCanonical_leftInverse
  right_inv := neutralLogHilbertToCanonical_rightInverse

end

end WeilDefect
