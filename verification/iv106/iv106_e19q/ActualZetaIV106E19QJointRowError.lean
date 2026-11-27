import WeilDefect.Arithmetic.ActualZetaIV106E19MOutsideCorrection
import WeilDefect.Arithmetic.ActualZetaIV106E19PStepAdmission

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped BigOperators InnerProduct

/-- A joint raw defect is an enclosure of the actual synthesized row
error. The estimate is on arbitrary complex coefficients, not just on
individual columns. -/
theorem neutralIV106E19QJoint_error {I : Type*} [Fintype I]
    (k : ℕ) (hk : 0 < k)
    (j : I → neutralIV106E16Index k)
    (x : I → neutralIV106E19LH) (g : I → RealComplexL2)
    (hg : ∀ i, ∀ᵐ t ∂volume, t ∈ Set.Icc (-(11/10:ℝ)) (11/10) → g i t = 0)
    (c : I → ℂ) :
    ‖∑ i,c i • (neutralIV106E14Row k hk (j i)-x i)‖ ≤
      ‖∑ i,c i • (neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk (j i)) -
        (x i).val-neutralIV106E19LRawColumn (g i))‖ := by
  classical
  let P := ContinuousLinearMap.adjoint neutralIV106E19LInclusion
  let v (i : I) := neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk (j i)) -
    (x i).val-neutralIV106E19LRawColumn (g i)
  have he (i : I) : P (v i) = neutralIV106E14Row k hk (j i)-x i := by
    dsimp only [P,v]
    rw [map_sub,map_sub,← neutralIV106E19LRow_project,
      neutralIV106E19LInclusion_adjoint_self,
      neutralIV106E19MOutside_zero (g i) (hg i),sub_zero]
  change ‖∑ i,c i • (neutralIV106E14Row k hk (j i)-x i)‖ ≤ ‖∑ i,c i • v i‖
  have hmap : P (∑ i,c i • v i) =
      ∑ i,c i • (neutralIV106E14Row k hk (j i)-x i) := by
    rw [map_sum]
    simp only [map_smul,he]
  rw [← hmap]
  exact (P.le_opNorm _).trans (by
    simpa using mul_le_mul_of_nonneg_right neutralIV106E19LInclusion_norm
      (norm_nonneg (∑ i,c i • v i)))

/-- A raw joint squared-norm matrix bound passes to the true supported
row error Gram in Loewner order. No independence of the rows is needed. -/
theorem neutralIV106E19QJoint_receiver {I : Type*} [Fintype I]
    (k : ℕ) (hk : 0 < k) (j : I → neutralIV106E16Index k)
    (x : I → neutralIV106E19LH) (g : I → RealComplexL2)
    (hg : ∀ i, ∀ᵐ t ∂volume, t ∈ Set.Icc (-(11/10:ℝ)) (11/10) → g i t = 0)
    (U : ℝ)
    (h : ∀ c : I → ℂ,
      ‖∑ i,c i • (neutralIV106E19LRawColumn (neutralIV106E19LColumn k hk (j i)) -
        (x i).val-neutralIV106E19LRawColumn (g i))‖^2 ≤
      U * (∑ i, ‖c i‖^2)) :
    ∀ c : I → ℂ,
      ‖∑ i,c i • (neutralIV106E14Row k hk (j i)-x i)‖^2 ≤
        U * (∑ i, ‖c i‖^2) := by
  intro c
  exact (pow_le_pow_left₀ (norm_nonneg _)
    (neutralIV106E19QJoint_error k hk j x g hg c) 2).trans (h c)

#print axioms neutralIV106E19QJoint_error
#print axioms neutralIV106E19QJoint_receiver
end
end WeilDefect
