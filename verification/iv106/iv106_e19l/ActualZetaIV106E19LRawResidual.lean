import WeilDefect.Arithmetic.ActualZetaIV106E19KExactProjection

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct BigOperators

abbrev neutralIV106E19LH := NeutralLogHilbertCarrier (11/10:ℝ)

def neutralIV106E19LInclusion : neutralIV106E19LH →L[ℂ] RealComplexL2 :=
  (neutralLogHilbertSubmodule (11/10:ℝ)).toSubmodule.subtypeL

/-- Raw weighted-coordinate Riesz column. The actual row is its
orthogonal projection onto the supported carrier. -/
def neutralIV106E19LRawColumn (f : RealComplexL2) : RealComplexL2 :=
  (ContinuousLinearMap.adjoint neutralLogPhysical) f

theorem neutralIV106E19LColumn_project (f : RealComplexL2) :
    (ContinuousLinearMap.adjoint (neutralLogPhysicalInclusion (11/10:ℝ))) f =
      (ContinuousLinearMap.adjoint neutralIV106E19LInclusion)
        (neutralIV106E19LRawColumn f) := by
  unfold neutralLogPhysicalInclusion neutralIV106E19LRawColumn
    neutralIV106E19LInclusion
  rw [ContinuousLinearMap.adjoint_comp]
  rfl

/-- Physical representatives of every actual original C3 row, including
the signed moment difference, not two separate constraints. -/
def neutralIV106E19LColumn (k : ℕ) (hk : 0 < k) :
    neutralIV106E16Index k → RealComplexL2
  | .inl i => neutralIV106C3CellColumn (11/10:ℝ) 665 i
  | .inr (.inl _) => neutralMomentColumnL2 (11/10:ℝ) (1/2) -
      neutralMomentColumnL2 (11/10:ℝ) (-(1/2))
  | .inr (.inr (.inl i)) => (neutralIV100Carrier k hk i).toLp 2 volume
  | .inr (.inr (.inr i)) => neutralIV105CResponse k hk i

theorem neutralIV106E19LRow_project (k : ℕ) (hk : 0 < k)
    (j : neutralIV106E16Index k) :
    neutralIV106E14Row k hk j =
      (ContinuousLinearMap.adjoint neutralIV106E19LInclusion)
        (neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk j)) := by
  rw [← neutralIV106E19LColumn_project]
  let d := neutralIV106E14Row k hk j -
    (ContinuousLinearMap.adjoint (neutralLogPhysicalInclusion (11/10:ℝ)))
      (neutralIV106E19LColumn k hk j)
  have h (q : neutralIV106E19LH) :
      inner ℂ (neutralIV106E14Row k hk j) q =
        inner ℂ ((ContinuousLinearMap.adjoint (neutralLogPhysicalInclusion (11/10:ℝ)))
          (neutralIV106E19LColumn k hk j)) q := by
    rw [neutralIV106E14Row_pair,adjoint_inner_left]
    rcases j with i | j
    · rfl
    · rcases j with u | j
      · change neutralLogMoment (11/10:ℝ) (1/2) q -
          neutralLogMoment (11/10:ℝ) (-(1/2)) q =
        inner ℂ (neutralMomentColumnL2 (11/10:ℝ) (1/2) -
          neutralMomentColumnL2 (11/10:ℝ) (-(1/2))) (neutralLogPhysical q.val)
        rw [inner_sub_left,neutralMomentColumnL2_inner,neutralMomentColumnL2_inner,
          neutralLogMoment_eq,neutralLogMoment_eq]
      · rcases j with i | i <;> rfl
  have hz : inner ℂ d d = 0 := by
    dsimp only [d]
    rw [inner_sub_left,h,sub_self]
  exact sub_eq_zero.mp (inner_self_eq_zero.mp hz)

/-- A raw multiplier lift, plus the actual supported cross-pole operator.
Keeping the latter as a carrier term avoids any change of pole convention. -/
def neutralIV106E19LRawAction (x : neutralIV106E19LH) : RealComplexL2 :=
  neutralActualZetaLogSymbolMultiplication (11/10:ℝ) x.val +
    (neutralLogPoleOperator (11/10:ℝ) x).val

theorem neutralIV106E19LInclusion_adjoint_self (x : neutralIV106E19LH) :
    (ContinuousLinearMap.adjoint neutralIV106E19LInclusion) x.val = x := by
  let d := (ContinuousLinearMap.adjoint neutralIV106E19LInclusion) x.val-x
  have hz : inner ℂ d d = 0 := by
    change inner ℂ d ((ContinuousLinearMap.adjoint neutralIV106E19LInclusion) x.val-x) = 0
    rw [inner_sub_right,adjoint_inner_right]
    change inner ℂ d.val x.val-inner ℂ d.val x.val = 0
    exact sub_self _
  exact sub_eq_zero.mp (inner_self_eq_zero.mp hz)

theorem neutralIV106E19LAction_project (x : neutralIV106E19LH) :
    (ContinuousLinearMap.adjoint neutralIV106E19LInclusion)
      (neutralIV106E19LRawAction x) =
      neutralActualZetaLogWeilFormOperator (11/10:ℝ) x := by
  unfold neutralIV106E19LRawAction neutralActualZetaLogWeilFormOperator
  rw [map_add,neutralIV106E19LInclusion_adjoint_self]
  rfl

theorem neutralIV106E19LInclusion_norm :
    ‖ContinuousLinearMap.adjoint neutralIV106E19LInclusion‖ ≤ 1 := by
  rw [ContinuousLinearMap.norm_adjoint_eq]
  apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
  intro x
  simp [neutralIV106E19LInclusion]

/-- Two nested orthogonal compressions give a valid residual bound
directly in weighted Fourier L2. No exact projection inverse is needed. -/
theorem neutralIV106E19LRaw_reserve (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk)
    (d : neutralIV106E16Index k → ℂ) :
    ‖neutralIV106E15Residual k hk y t‖ ≤
      ‖neutralIV106E19LRawAction (y.val-t.val) -
        ∑ j, d j • neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk j)‖ := by
  let P := ContinuousLinearMap.adjoint neutralIV106E19LInclusion
  let v := neutralIV106E19LRawAction (y.val-t.val) -
        ∑ j, d j • neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk j)
  have he : P v =
      neutralActualZetaLogWeilFormOperator (11/10:ℝ) (y.val-t.val) -
        (∑ j, d j • neutralIV106E14LiftedRow k hk j).val := by
    dsimp only [v]
    rw [map_sub,map_sum,neutralIV106E19LAction_project]
    simp only [map_smul,← neutralIV106E19LRow_project]
    change _ = _ - (neutralIV106E13Finite k hk).subtypeL
      (∑ j, d j • neutralIV106E14LiftedRow k hk j)
    simp only [map_sum,map_smul]
    rfl
  calc
    _ ≤ ‖P v‖ := by rw [he]; exact neutralIV106E19KRow_reserve k hk y t d
    _ ≤ ‖v‖ := (P.le_opNorm _).trans (by
      simpa using mul_le_mul_of_nonneg_right neutralIV106E19LInclusion_norm (norm_nonneg v))

#print axioms neutralIV106E19LColumn_project
#print axioms neutralIV106E19LRow_project
#print axioms neutralIV106E19LInclusion_adjoint_self
#print axioms neutralIV106E19LAction_project
#print axioms neutralIV106E19LInclusion_norm
#print axioms neutralIV106E19LRaw_reserve
end
end WeilDefect
