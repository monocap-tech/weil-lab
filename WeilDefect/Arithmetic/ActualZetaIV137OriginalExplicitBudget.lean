import WeilDefect.Arithmetic.ActualZetaIV136OriginalHeadCoverage
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap FourierTransform ComplexConjugate BigOperators

/-- Replace the classically selected logarithmic error by any proved
one-sided numerical envelope for the unchanged signed symbol. -/
theorem neutralIV137Canonical_garding (a C : ℝ)
    (f : neutralCanonicalLogFormDomain a)
    (hC : ∀ ξ : ℝ, logarithmicFourierWeight ξ ≤ rightLimitCompactWeilSymbolMathlib a ξ + C) :
    ‖neutralLogWeightedL2 f‖^2 ≤ neutralActualZetaCanonicalNativeQuadratic a f +
      (C+neutralPhysicalPoleEnergyConstant a)*‖f.val‖^2 := by
  have hm : Integrable (fun ξ : ℝ => ‖(𝓕 f.val : RealComplexL2) ξ‖^2) :=
    (memLp_two_iff_integrable_sq_norm
      (Lp.aestronglyMeasurable (𝓕 f.val : RealComplexL2))).mp (Lp.memLp _)
  have hs : Integrable (fun ξ => (rightLimitCompactWeilSymbolMathlib a ξ + C) *
      ‖(𝓕 f.val : RealComplexL2) ξ‖^2) := by
    convert (neutralActualZetaCanonical_signedEnergy_integrable a f).add
      (hm.const_mul C) using 1 <;> funext ξ <;> simp only [Pi.add_apply] <;> ring
  have hl : ‖neutralLogWeightedL2 f‖^2 ≤
      ∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ+C)*‖(𝓕 f.val : RealComplexL2) ξ‖^2 := by
    rw [neutralLogWeightedL2_norm_sq]
    apply integral_mono f.property.2 hs
    intro ξ
    exact mul_le_mul_of_nonneg_right (hC ξ) (sq_nonneg _)
  have he : (∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ+C)*
      ‖(𝓕 f.val : RealComplexL2) ξ‖^2) =
      (∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ*‖(𝓕 f.val : RealComplexL2) ξ‖^2)
        + C*‖f.val‖^2 := by
    calc
      _ = ∫ ξ, (rightLimitCompactWeilSymbolMathlib a ξ*‖(𝓕 f.val : RealComplexL2) ξ‖^2 +
        C*‖(𝓕 f.val : RealComplexL2) ξ‖^2) := by
        apply integral_congr_ae
        filter_upwards [] with ξ
        ring
      _ = _ := by
        rw [integral_add (neutralActualZetaCanonical_signedEnergy_integrable a f)
          (hm.const_mul C), integral_const_mul, ← neutralPhysicalL2_norm_sq, Lp.norm_fourier_eq]
  rw [he] at hl
  have hp := (abs_le.mp (neutralPhysicalPoleEnergy_abs_le a f.val)).1
  unfold neutralActualZetaCanonicalNativeQuadratic
  nlinarith only [hl,hp]

/-- Use the actual physical row norms, not the earlier sum-of-norms budget. -/
def neutralIV137PackedBudget (k : ℕ) (hk : 0 < k) : ℝ :=
  ∑ i : Fin k, (5/2:ℝ) *
    ‖neutralIV133PhysicalRow (11/10:ℝ) (neutralIV100Carrier k hk i)‖^2 /
    neutralIV104Mass k hk i

theorem neutralIV137Response_bound (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV108RowBudget k hk v ≤ neutralIV137PackedBudget k hk * ‖v.toLp 2 volume‖^2 := by
  unfold neutralIV108RowBudget neutralIV137PackedBudget
  rw [Finset.sum_mul]
  apply Finset.sum_le_sum
  intro i hi
  have hu := neutralIV009OriginalCollars_supported_window _
    (neutralIV100Carrier_collars k hk i)
  have hb := norm_inner_le_norm (𝕜 := ℂ)
    (neutralIV133PhysicalRow (11/10:ℝ) (neutralIV100Carrier k hk i)) (v.toLp 2 volume)
  rw [neutralIV133PhysicalRow_pair _ (by norm_num) _ _ hu hv] at hb
  change ‖neutralIV106CrossRHS k hk v i‖ ≤ _ at hb
  have hs := pow_le_pow_left₀ (norm_nonneg _) hb 2
  calc
    _ ≤ (5/2:ℝ) * (‖neutralIV133PhysicalRow (11/10:ℝ)
        (neutralIV100Carrier k hk i)‖*‖v.toLp 2 volume‖)^2 /
        neutralIV104Mass k hk i :=
      div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left hs (by norm_num))
        (neutralIV100Carrier_mass_pos k hk i).le
    _ = _ := by ring

theorem neutralIV137Schur_garding (k : ℕ) (hk : 0 < k) (C D : ℝ)
    (hC : ∀ ξ : ℝ, logarithmicFourierWeight ξ ≤ rightLimitCompactWeilSymbolMathlib (11/10:ℝ) ξ+C)
    (hD : neutralIV137PackedBudget k hk ≤ D)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    ‖neutralIV102Lift (11/10:ℝ) v hv‖^2 ≤ neutralIV107SchurEnergy k hk v +
      (C+neutralPhysicalPoleEnergyConstant (11/10:ℝ)+D)*‖v.toLp 2 volume‖^2 := by
  let f := neutralIV102Lift (11/10:ℝ) v hv
  have he : neutralLogWeightedL2 (neutralLogHilbertToCanonical f) = f.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse f)
  have hq : neutralIV101Q (11/10:ℝ) v =
      (inner ℂ f (neutralActualZetaLogWeilFormOperator (11/10:ℝ) f)).re := by
    unfold neutralIV101Q
    rw [neutralIV103Mixed_native _ (by norm_num) v v hv hv]
  -- The complex diagonal is attached through its real part.
  have hcanon : neutralActualZetaCanonicalNativeQuadratic (11/10:ℝ)
      (neutralLogHilbertToCanonical f) = neutralIV101Q (11/10:ℝ) v := by
    rw [hq, neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re]
  have h2 := neutralIV137Canonical_garding (11/10:ℝ) C (neutralLogHilbertToCanonical f) hC
  rw [he,hcanon] at h2
  change ‖f‖^2 ≤ neutralIV101Q (11/10:ℝ) v +
    (C+neutralPhysicalPoleEnergyConstant (11/10:ℝ)) *
      ‖neutralLogPhysical f.val‖^2 at h2
  change ‖f‖^2 ≤ _ at h2
  have hf : neutralLogPhysical f.val = v.toLp 2 volume := neutralIV102Lift_physical _ v hv
  rw [hf] at h2
  have hr := (neutralIV108Response_le_rowBudget k hk v).trans
    ((neutralIV137Response_bound k hk v hv).trans
      (mul_le_mul_of_nonneg_right hD (sq_nonneg _)))
  unfold neutralIV107SchurEnergy
  change ‖f‖^2 ≤ _
  linarith only [h2,hr]

theorem neutralIV137Tail_of_budget (k : ℕ) (hk : 0 < k) (C D eta T : ℝ) (N : ℕ)
    (hN : 0 < N) (hT : 0 ≤ T)
    (hC : ∀ ξ : ℝ, logarithmicFourierWeight ξ ≤ rightLimitCompactWeilSymbolMathlib (11/10:ℝ) ξ+C)
    (hD : neutralIV137PackedBudget k hk ≤ D)
    (hm : eta ≤ (1-neutralIV127Leakage (11/10:ℝ) N T)*Real.log (Real.exp 1+T) -
      (C+neutralPhysicalPoleEnergyConstant (11/10:ℝ)+D))
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hz : neutralIV127CellNull (11/10:ℝ) N v) :
    eta*‖v.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk v := by
  have hlog := neutralIV125LogLower_of_leakage (11/10:ℝ) v hv T _ hT
    (neutralIV127LowBand _ (by norm_num) N hN v hv hz T hT)
  have hg := neutralIV137Schur_garding k hk C D hC hD v hv
  have hp := mul_le_mul_of_nonneg_right hm (sq_nonneg ‖v.toLp 2 volume‖)
  linarith only [hlog,hg,hp]

#print axioms neutralIV137Canonical_garding
#print axioms neutralIV137Response_bound
#print axioms neutralIV137Schur_garding
#print axioms neutralIV137Tail_of_budget

end
end WeilDefect
