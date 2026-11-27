import WeilDefect.Arithmetic.ActualZetaIV106E19MRawFourier

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct BigOperators

/-- Exterior physical columns project to zero on the supported carrier.
They may therefore be used as arbitrary corrections to raw Fourier
residuals, with no need to solve the exact support projection. -/
theorem neutralIV106E19MOutside_zero (g : RealComplexL2)
    (hg : ∀ᵐ x ∂volume, x ∈ Set.Icc (-(11/10:ℝ)) (11/10) → g x = 0) :
    (ContinuousLinearMap.adjoint neutralIV106E19LInclusion)
      (neutralIV106E19LRawColumn g) = 0 := by
  rw [← neutralIV106E19LColumn_project]
  let p := (ContinuousLinearMap.adjoint (neutralLogPhysicalInclusion (11/10:ℝ))) g
  have hz : inner ℂ p p = 0 := by
    change inner ℂ ((ContinuousLinearMap.adjoint
      (neutralLogPhysicalInclusion (11/10:ℝ))) g) p = 0
    rw [adjoint_inner_left,L2.inner_def]
    have hzero : (fun x : ℝ => inner ℂ (g x)
        (neutralLogPhysical p.val x)) =ᵐ[volume] (fun _ => 0) := by
      filter_upwards [hg,neutralLogHilbertCarrier_supported p] with x hx hp
      by_cases hm : x ∈ Set.Icc (-(11/10:ℝ)) (11/10)
      · rw [hx hm,zero_inner]
      · rw [hp hm,inner_zero]
    rw [integral_congr_ae hzero]
    simp
  exact inner_self_eq_zero.mp hz

/-- A candidate supported Riesz vector receives a quantitative error
bound from its raw-coordinate defect after any exterior correction. -/
theorem neutralIV106E19MRow_error (k : ℕ) (hk : 0 < k)
    (j : neutralIV106E16Index k) (x : neutralIV106E19LH)
    (g : RealComplexL2)
    (hg : ∀ᵐ t ∂volume, t ∈ Set.Icc (-(11/10:ℝ)) (11/10) → g t = 0) :
    ‖neutralIV106E14Row k hk j-x‖ ≤
      ‖neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk j) -
        x.val-neutralIV106E19LRawColumn g‖ := by
  let P := ContinuousLinearMap.adjoint neutralIV106E19LInclusion
  let v := neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk j) -
    x.val-neutralIV106E19LRawColumn g
  have he : P v = neutralIV106E14Row k hk j-x := by
    dsimp only [P,v]
    rw [map_sub,map_sub,← neutralIV106E19LRow_project,
      neutralIV106E19LInclusion_adjoint_self,neutralIV106E19MOutside_zero g hg,sub_zero]
  rw [← he]
  exact (P.le_opNorm v).trans (by
    simpa using mul_le_mul_of_nonneg_right neutralIV106E19LInclusion_norm (norm_nonneg v))

/-- The raw residual enclosure also admits arbitrary exterior corrections.
Unlike replacing the supported projection by an identity, this
preserves the direction of the full-kernel residual inequality. -/
theorem neutralIV106E19MResidual_outside (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk)
    (d : neutralIV106E16Index k → ℂ) (g : RealComplexL2)
    (hg : ∀ᵐ x ∂volume, x ∈ Set.Icc (-(11/10:ℝ)) (11/10) → g x = 0) :
    ‖neutralIV106E15Residual k hk y t‖ ≤
      ‖neutralIV106E19LRawAction (y.val-t.val) -
        (∑ j, d j • neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk j)) -
        neutralIV106E19LRawColumn g‖ := by
  let P := ContinuousLinearMap.adjoint neutralIV106E19LInclusion
  let v := neutralIV106E19LRawAction (y.val-t.val) -
    (∑ j, d j • neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk j)) -
    neutralIV106E19LRawColumn g
  have he : P v =
      neutralActualZetaLogWeilFormOperator (11/10:ℝ) (y.val-t.val) -
      (∑ j, d j • neutralIV106E14LiftedRow k hk j).val := by
    dsimp only [P,v]
    rw [map_sub,map_sub,map_sum,neutralIV106E19LAction_project,
      neutralIV106E19MOutside_zero g hg,sub_zero]
    simp only [map_smul,← neutralIV106E19LRow_project]
    change _ = _ - (neutralIV106E13Finite k hk).subtypeL
      (∑ j, d j • neutralIV106E14LiftedRow k hk j)
    simp only [map_sum,map_smul]
    rfl
  calc
    _ ≤ ‖P v‖ := by rw [he]; exact neutralIV106E19KRow_reserve k hk y t d
    _ ≤ ‖v‖ := (P.le_opNorm v).trans (by
      simpa using mul_le_mul_of_nonneg_right neutralIV106E19LInclusion_norm (norm_nonneg v))

#print axioms neutralIV106E19MOutside_zero
#print axioms neutralIV106E19MRow_error
#print axioms neutralIV106E19MResidual_outside
end
end WeilDefect
