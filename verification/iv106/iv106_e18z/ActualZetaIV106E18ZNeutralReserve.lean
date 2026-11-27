import WeilDefect.Arithmetic.ActualZetaIV106E18ZSymbolReserve

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate

abbrev neutralIV106E18ZH := NeutralLogHilbertCarrier (11/10:ℝ)

/-- The improved constant applies to the existing multiplier, not a
replacement constructed using the improved numerical envelope. -/
theorem neutralIV106E18ZMultiply (f : RealComplexL2) :
    ‖neutralActualZetaLogSymbolMultiplication (11/10:ℝ) f‖ ≤ 19*‖f‖ := by
  apply Lp.norm_le_mul_norm_of_ae_le_mul
  filter_upwards [neutralActualZetaLogSymbolMultiplication_coe (11/10:ℝ) f] with ξ hξ
  rw [hξ,norm_mul]
  exact mul_le_mul_of_nonneg_right (neutralIV106E18ZRatio ξ) (norm_nonneg _)

theorem neutralIV106E18ZMultiplier_mixed (p q : neutralIV106E18ZH) :
    ‖inner ℂ p (neutralActualZetaLogMultiplierOperator (11/10:ℝ) q)‖ ≤
      19*‖p‖*‖q‖ := by
  change ‖inner ℂ p ((ContinuousLinearMap.adjoint
    (neutralLogHilbertSubmodule (11/10:ℝ)).toSubmodule.subtypeL)
    (neutralActualZetaLogSymbolMultiplication (11/10:ℝ) q.val))‖ ≤ _
  rw [adjoint_inner_right]
  change ‖inner ℂ p.val (neutralActualZetaLogSymbolMultiplication (11/10:ℝ) q.val)‖ ≤ _
  calc
    _ ≤ ‖p.val‖*‖neutralActualZetaLogSymbolMultiplication (11/10:ℝ) q.val‖ :=
      norm_inner_le_norm _ _
    _ ≤ ‖p.val‖*(19*‖q.val‖) :=
      mul_le_mul_of_nonneg_left (neutralIV106E18ZMultiply q.val) (norm_nonneg _)
    _ = _ := by change ‖p‖*(19*‖q‖) = _; ring

def neutralIV106E18ZNeutral (q : neutralIV106E18ZH) : Prop :=
  neutralLogMoment (11/10:ℝ) (-(1/2)) q = 0 ∧
  neutralLogMoment (11/10:ℝ) (1/2) q = 0

theorem neutralIV106E18ZNeutral_sub (q v : neutralIV106E18ZH)
    (hq : neutralIV106E18ZNeutral q) (hv : neutralIV106E18ZNeutral v) :
    neutralIV106E18ZNeutral (v-q) := by
  unfold neutralIV106E18ZNeutral at *
  rw [map_sub,map_sub,hv.1,hq.1,hv.2,hq.2]
  simp

/-- Exact cancellation requires neutrality only in the second slot.
The first slot may be an arbitrary native carrier vector. -/
theorem neutralIV106E18ZNative_mixed (p q : neutralIV106E18ZH)
    (hq : neutralIV106E18ZNeutral q) :
    ‖inner ℂ p (neutralActualZetaLogWeilFormOperator (11/10:ℝ) q)‖ ≤
      19*‖p‖*‖q‖ := by
  have hm := hq.1
  have hp := hq.2
  rw [neutralLogMoment_eq] at hm hp
  unfold neutralActualZetaLogWeilFormOperator
  rw [ContinuousLinearMap.add_apply,inner_add_right,
    neutralLogPoleOperator_mixed,hm,hp]
  simp only [mul_zero,add_zero]
  exact neutralIV106E18ZMultiplier_mixed p q

/-- Two-term perturbation of the actual mixed form: the reference and
replacement second-slot vectors must be neutral, but not the first slot. -/
theorem neutralIV106E18ZNeutral_error (p q u v : neutralIV106E18ZH)
    (hq : neutralIV106E18ZNeutral q) (hv : neutralIV106E18ZNeutral v)
    (M δ : ℝ) (hM : 0 ≤ M) (hδ : 0 ≤ δ)
    (hp : ‖p‖ ≤ M) (hqnorm : ‖q‖ ≤ M)
    (hu : ‖u-p‖ ≤ δ) (hvnorm : ‖v-q‖ ≤ δ) :
    ‖inner ℂ u (neutralActualZetaLogWeilFormOperator (11/10:ℝ) v) -
      inner ℂ p (neutralActualZetaLogWeilFormOperator (11/10:ℝ) q)‖ ≤
      19*(2*M*δ+δ^2) := by
  let W := neutralActualZetaLogWeilFormOperator (11/10:ℝ)
  have he : inner ℂ u (W v)-inner ℂ p (W q) =
      inner ℂ (u-p) (W q)+inner ℂ u (W (v-q)) := by
    simp only [map_sub,inner_sub_left,inner_sub_right]
    ring
  have hun : ‖u‖ ≤ M+δ := by
    calc
      _ = ‖(u-p)+p‖ := by rw [sub_add_cancel]
      _ ≤ ‖u-p‖+‖p‖ := norm_add_le _ _
      _ ≤ M+δ := by linarith
  change ‖inner ℂ u (W v)-inner ℂ p (W q)‖ ≤ _
  rw [he]
  calc
    _ ≤ ‖inner ℂ (u-p) (W q)‖+‖inner ℂ u (W (v-q))‖ := norm_add_le _ _
    _ ≤ 19*‖u-p‖*‖q‖+19*‖u‖*‖v-q‖ :=
      add_le_add (neutralIV106E18ZNative_mixed (u-p) q hq)
        (neutralIV106E18ZNative_mixed u (v-q) (neutralIV106E18ZNeutral_sub q v hq hv))
    _ ≤ 19*(δ*M)+19*((M+δ)*δ) := by
      simp only [mul_assoc]
      exact add_le_add
        (mul_le_mul_of_nonneg_left
          (mul_le_mul hu hqnorm (norm_nonneg _) hδ) (by norm_num))
        (mul_le_mul_of_nonneg_left
          (mul_le_mul hun hvnorm (norm_nonneg _) (add_nonneg hM hδ)) (by norm_num))
    _ = _ := by ring

#print axioms neutralIV106E18ZMultiply
#print axioms neutralIV106E18ZMultiplier_mixed
#print axioms neutralIV106E18ZNeutral_sub
#print axioms neutralIV106E18ZNative_mixed
#print axioms neutralIV106E18ZNeutral_error
end
end WeilDefect
