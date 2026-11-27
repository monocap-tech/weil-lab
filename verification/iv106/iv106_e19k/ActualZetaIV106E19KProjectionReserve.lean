import WeilDefect.Arithmetic.ActualZetaIV106E19JTrialReceiver

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped BigOperators InnerProduct

/-- The adjoint of the actual kernel inclusion is the full kernel
projection (with its codomain retained as the kernel subtype). -/
def neutralIV106E19KProject (k : ℕ) (hk : 0 < k) :
    neutralIV106E13H →L[ℂ] neutralIV106E12Kernel k hk :=
  ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL

theorem neutralIV106E19KProject_norm (k : ℕ) (hk : 0 < k) :
    ‖neutralIV106E19KProject k hk‖ ≤ 1 := by
  unfold neutralIV106E19KProject
  rw [ContinuousLinearMap.norm_adjoint_eq]
  apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
  intro x
  simp

/-- Every actual finite-sector vector disappears under full projection. -/
theorem neutralIV106E19KProject_finite (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) :
    neutralIV106E19KProject k hk y.val = 0 := by
  let p := neutralIV106E19KProject k hk y.val
  have h : inner ℂ p p = 0 := by
    change inner ℂ p ((ContinuousLinearMap.adjoint
      (neutralIV106E12Kernel k hk).subtypeL) y.val) = 0
    rw [adjoint_inner_right]
    exact (Submodule.mem_orthogonal _ _).mp y.property p.val p.property
  exact inner_self_eq_zero.mp h

/-- The true full projected residual can be bounded by an arbitrary
ambient action minus an arbitrary exact row-span correction. In contrast
to finite-bank Galerkin residuals this is an upper bound. -/
theorem neutralIV106E19KSubtract_bound (k : ℕ) (hk : 0 < k)
    (v : neutralIV106E13H) (y : neutralIV106E13Finite k hk) :
    ‖neutralIV106E19KProject k hk v‖ ≤ ‖v-y.val‖ := by
  let P := neutralIV106E19KProject k hk
  have he : P (v-y.val) = P v := by
    rw [map_sub,neutralIV106E19KProject_finite k hk y,sub_zero]
  rw [← he]
  exact (P.le_opNorm _).trans (by
    simpa using mul_le_mul_of_nonneg_right
      (neutralIV106E19KProject_norm k hk) (norm_nonneg (v-y.val)))

/-- The compressed trial residual is the projection of the actual
ambient action of the E16 trial vector. -/
theorem neutralIV106E19KResidual_project (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk) :
    neutralIV106E15Residual k hk y t =
      neutralIV106E19KProject k hk
        (neutralActualZetaLogWeilFormOperator (11/10) (y.val-t.val)) := by
  simp [neutralIV106E15Residual,neutralIV106E15RHS,
    neutralIV106E12Compressed,neutralIV106E19KProject,map_sub]

/-- All row coefficients are arbitrary. Their synthesis is in the
orthogonal finite sector by construction; no inverse of its Gram
and no row independence is required for this upper bound. -/
theorem neutralIV106E19KRow_reserve (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk)
    (d : neutralIV106E16Index k → ℂ) :
    ‖neutralIV106E15Residual k hk y t‖ ≤
      ‖neutralActualZetaLogWeilFormOperator (11/10) (y.val-t.val) -
        (∑ j, d j • neutralIV106E14LiftedRow k hk j).val‖ := by
  rw [neutralIV106E19KResidual_project]
  exact neutralIV106E19KSubtract_bound k hk _ _

/-- A finite-bank optimizer can use any ambient row correction; a
successful reserve is sufficient for the original E15 Schur receiver. -/
theorem neutralIV106E19KAmbient_receiver (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (t : neutralIV106E13Finite k hk → neutralIV106E12Kernel k hk)
    (d : neutralIV106E13Finite k hk → neutralIV106E16Index k → ℂ)
    (h : ∀ y, neutralIV106E11Alpha⁻¹ *
      ‖neutralActualZetaLogWeilFormOperator (11/10) (y.val-(t y).val) -
        (∑ j, d y j • neutralIV106E14LiftedRow k hk j).val‖^2 ≤
      neutralIV106E13Energy (y.val-(t y).val)) :
    ∀ q : neutralIV106E13H, 0 ≤ neutralIV106E13Energy q := by
  apply neutralIV106E15Trial_receiver k hk e he t
  intro y
  have hb := neutralIV106E19KRow_reserve k hk y (t y) (d y)
  exact (mul_le_mul_of_nonneg_left
    (pow_le_pow_left₀ (norm_nonneg _) hb 2)
    (inv_nonneg.mpr neutralIV106E11Alpha_pos.le)).trans (h y)

#print axioms neutralIV106E19KProject_norm
#print axioms neutralIV106E19KProject_finite
#print axioms neutralIV106E19KSubtract_bound
#print axioms neutralIV106E19KResidual_project
#print axioms neutralIV106E19KRow_reserve
#print axioms neutralIV106E19KAmbient_receiver
end
end WeilDefect
