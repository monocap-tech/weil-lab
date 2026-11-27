import WeilDefect.Arithmetic.ActualZetaIV106E19MRawFourier
import Mathlib.Analysis.SpecialFunctions.JapaneseBracket

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped FourierTransform BigOperators

/-- A bounded-jump step function has enough decay for logarithmic
energy, although its weak derivative need not belong to L2. -/
theorem neutralIV106E19PWeight_sqrt (ξ : ℝ) :
    logarithmicFourierWeight ξ ≤
      2*Real.sqrt (Real.exp 1+1)*Real.sqrt (1+|ξ|) := by
  let t := Real.exp 1+|ξ|
  have ht : 0 < t := add_pos_of_pos_of_nonneg (Real.exp_pos 1) (abs_nonneg ξ)
  have hs : 0 < Real.sqrt t := Real.sqrt_pos.mpr ht
  have he : Real.log t = 2*Real.log (Real.sqrt t) := by
    calc
      _ = Real.log (Real.sqrt t*Real.sqrt t) := by
        rw [← sq,Real.sq_sqrt ht.le]
      _ = _ := by rw [Real.log_mul hs.ne' hs.ne']; ring
  have hlog := Real.log_le_sub_one_of_pos hs
  have hb : t ≤ (Real.exp 1+1)*(1+|ξ|) := by
    dsimp [t]
    nlinarith [mul_nonneg (Real.exp_pos 1).le (abs_nonneg ξ)]
  have hm := Real.sqrt_le_sqrt hb
  rw [Real.sqrt_mul (by positivity)] at hm
  change Real.log t ≤ _
  rw [he]
  linarith

/-- The actual weighted form domain admits every supported physical L2
vector with reciprocal Fourier decay. The remaining step-column Fourier
transform identity is deliberately kept as an explicit premise. -/
theorem neutralIV106E19PDecay_admission (a : ℝ) (f : RealComplexL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0)
    (C : ℝ) (hC : 0 ≤ C)
    (hf : ∀ᵐ ξ ∂volume,
      ‖(𝓕 f : RealComplexL2) ξ‖ ≤ C/(1+|ξ|)) :
    ∃ x : NeutralLogHilbertCarrier a, neutralLogPhysical x.val = f := by
  have hI : Integrable (fun ξ : ℝ => (1+‖ξ‖)^(-(3/2:ℝ))) volume :=
    integrable_one_add_norm (by norm_num : (Module.finrank ℝ ℝ:ℝ) < 3/2)
  let K := 2*Real.sqrt (Real.exp 1+1)*C^2
  have hE : Integrable (fun ξ =>
      logarithmicFourierWeight ξ*‖(𝓕 f : RealComplexL2) ξ‖^2) volume := by
    apply (hI.const_mul K).mono'
    · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
        ((Lp.aestronglyMeasurable (𝓕 f : RealComplexL2)).norm.pow 2)
    · filter_upwards [hf] with ξ hξ
      have hw : 0 ≤ logarithmicFourierWeight ξ :=
        zero_le_one.trans (one_le_logarithmicFourierWeight ξ)
      have hp : 0 < 1+|ξ| := by positivity
      rw [Real.norm_eq_abs,abs_of_nonneg (mul_nonneg hw (sq_nonneg _))]
      calc
        _ ≤ logarithmicFourierWeight ξ*(C/(1+|ξ|))^2 :=
          mul_le_mul_of_nonneg_left
            (pow_le_pow_left₀ (norm_nonneg _) hξ 2) hw
        _ ≤ (2*Real.sqrt (Real.exp 1+1)*Real.sqrt (1+|ξ|))*
            (C/(1+|ξ|))^2 :=
          mul_le_mul_of_nonneg_right (neutralIV106E19PWeight_sqrt ξ) (sq_nonneg _)
        _ = _ := by
          rw [Real.norm_eq_abs,Real.sqrt_eq_rpow,div_pow]
          have he : (1+|ξ|)^(1/2:ℝ) / (1+|ξ|)^2 =
              (1+|ξ|)^(-(3/2:ℝ)) := by
            rw [← Real.rpow_natCast, ← Real.rpow_sub hp]
            norm_num
          unfold K
          rw [← he]
          ring
  let p : neutralCanonicalLogFormDomain a := ⟨f,hs,hE⟩
  exact ⟨neutralCanonicalToLogHilbert p,neutralLogPhysical_weighted p⟩

/-- Finite supported sums preserve the literal logarithmic carrier.
No derivative-witness assumption is imposed on the individual steps. -/
theorem neutralIV106E19PSum_admission {I : Type*} [Fintype I]
    (a : ℝ) (f : I → RealComplexL2) (c : I → ℂ)
    (h : ∀ i, ∃ p : NeutralLogHilbertCarrier a,
      neutralLogPhysical p.val = f i) :
    ∃ p : NeutralLogHilbertCarrier a,
      neutralLogPhysical p.val = ∑ i,c i • f i := by
  classical
  choose p hp using h
  refine ⟨∑ i,c i • p i,?_⟩
  change neutralLogPhysicalInclusion a (∑ i,c i • p i) = _
  simp only [map_sum,map_smul]
  change (∑ i,c i • neutralLogPhysical (p i).val) = _
  simp_rw [hp]

#print axioms neutralIV106E19PWeight_sqrt
#print axioms neutralIV106E19PDecay_admission
#print axioms neutralIV106E19PSum_admission
end
end WeilDefect
