import WeilDefect.MasterRecon.V10B75b

/-! V10B76b: exact Archimedean-plus-pole load and row correction on
the actual retained orthogonal complement. Prime-zero is not invoked.
This is not yet the numerical A/R certificate or a literal convolution. -/
namespace WeilDefect.MasterRecon.V10B76b
open MeasureTheory Set
open scoped InnerProduct BigOperators ComplexConjugate
open V08I (logCarrier)
open V08K (supportMeasure)
open V10B69a (J dividedTrial poleLoad)
open V10B75b (archLoad)
open V10B8e (archOperator)

noncomputable def fullLoad (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (j : Fin 16) :
    V08F.PhysicalL2 (supportMeasure (1/4)) :=
  archLoad hd C hC j + poleLoad (dividedTrial j)

theorem full_physical_pair (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (j : Fin 16)
    (w : logCarrier (1/4)) :
    inner ℂ ((archOperator (1/4) hd C hC + V10B8c.poleOperator (1/4) (by norm_num))
      (dividedTrial j)) w = inner ℂ (fullLoad hd C hC j) (J w) := by
  rw [ContinuousLinearMap.add_apply,inner_add_left,V10B75b.arch_restricted_pair,
    V10B69a.pole_physical_pair,fullLoad,inner_add_left]

theorem corrected_physical_pair (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (j : Fin 16) (a : Fin 16 → ℂ)
    (w : logCarrier (1/4)) (hw : w ∈ V10B17b.retainedᗮ) :
    inner ℂ ((archOperator (1/4) hd C hC + V10B8c.poleOperator (1/4) (by norm_num))
      (dividedTrial j)) w =
      inner ℂ (fullLoad hd C hC j-∑ i, a i • V10B68a.rowVector i) (J w) := by
  rw [V10B69a.row_subtraction_invariant _ _ w hw]
  exact full_physical_pair hd C hC j w

end WeilDefect.MasterRecon.V10B76b

#print axioms WeilDefect.MasterRecon.V10B76b.full_physical_pair
#print axioms WeilDefect.MasterRecon.V10B76b.corrected_physical_pair
