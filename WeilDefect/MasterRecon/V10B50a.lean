import WeilDefect.MasterRecon.V10B13a
import WeilDefect.MasterRecon.V10B8c
import Mathlib.Analysis.InnerProductSpace.Orthogonal

/-! V10B50a: literal carrier moments and pole evaluations, with a generic
adjoint-span kernel characterization. Independent of the uncompiled
V10B17b tail estimate and of the optimized matrix. -/
namespace WeilDefect.MasterRecon.V10B50a

open MeasureTheory Set
open scoped InnerProduct ComplexConjugate
open V08I (logCarrier physicalInclusion)
open V08K (supportMeasure restrictPhysical)

theorem moment_literal (t : ℝ) (ht : 0 ≤ t) (j : ℕ) (g : logCarrier t) :
    V10B13a.moment t ht j g =
      ∫ x, (x:ℂ)^j * physicalInclusion t g x ∂supportMeasure t := by
  rw [V10B13a.moment,ContinuousLinearMap.comp_apply,V08E.moment_apply]
  apply integral_congr_ae
  have h₁ := V08F.physicalL1Inclusion_ae (supportMeasure t)
    (restrictPhysical t (physicalInclusion t g))
  have h₂ := V08K.restrictPhysical_ae t (physicalInclusion t g)
  filter_upwards [h₁,h₂] with x hx hy
  change (x:ℂ)^j * (V08F.physicalL1Inclusion (supportMeasure t)
    (restrictPhysical t (physicalInclusion t g))) x = _
  rw [hx,hy]

theorem eval_literal (t a : ℝ) (ht : 0 ≤ t) (g : logCarrier t) :
    V10B8c.eval t a ht g =
      ∫ x, (Real.exp (a*x):ℂ)*physicalInclusion t g x ∂supportMeasure t := by
  unfold V10B8c.eval V10B8c.evalRestricted
  rw [ContinuousLinearMap.comp_apply,ContinuousLinearMap.comp_apply,
    innerSL_apply_apply,L2.inner_def]
  apply integral_congr_ae
  filter_upwards [MemLp.coeFn_toLp (V10B8c.expVector_mem t a ht),
    V08K.restrictPhysical_ae t (physicalInclusion t g)] with x hx hy
  change inner ℂ (V10B8c.vector t a ht x)
    (restrictPhysical t (physicalInclusion t g) x) = _
  rw [show V10B8c.vector t a ht x = V10B8c.expVector a x from hx,hy,
    RCLike.inner_apply']
  simp [V10B8c.expVector]

theorem pole_literal (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t) :
    (V10B8c.eval t (1/2) ht-V10B8c.eval t (-1/2) ht) g =
      (∫ x, (Real.exp ((1/2:ℝ)*x):ℂ)*physicalInclusion t g x ∂supportMeasure t) -
      (∫ x, (Real.exp ((-1/2:ℝ)*x):ℂ)*physicalInclusion t g x ∂supportMeasure t) := by
  rw [ContinuousLinearMap.sub_apply,eval_literal,eval_literal]

theorem adjoint_span_iff {H : Type*} [NormedAddCommGroup H]
    [InnerProductSpace ℂ H] [CompleteSpace H] {ι : Type*}
    (L : ι → H →L[ℂ] ℂ) (g : H) :
    g ∈ (Submodule.span ℂ (Set.range (fun i => (L i).adjoint 1)))ᗮ ↔
      ∀ i, L i g = 0 := by
  constructor
  · intro h i
    have hi := h _ (Submodule.subset_span ⟨i,rfl⟩)
    rw [ContinuousLinearMap.adjoint_inner_left,RCLike.inner_apply'] at hi
    simpa using hi
  · intro h
    have hs : Submodule.span ℂ (Set.range (fun i => (L i).adjoint 1)) ≤
        (innerSL ℂ g).ker := by
      apply Submodule.span_le.mpr
      rintro _ ⟨i,rfl⟩
      change inner ℂ g ((L i).adjoint 1) = 0
      rw [inner_eq_zero_symm,ContinuousLinearMap.adjoint_inner_left,h i,inner_zero_right]
    intro u hu
    have hh := hs hu
    change inner ℂ g u = 0 at hh
    exact inner_eq_zero_symm.mp hh

end WeilDefect.MasterRecon.V10B50a

#print axioms WeilDefect.MasterRecon.V10B50a.moment_literal
#print axioms WeilDefect.MasterRecon.V10B50a.eval_literal
#print axioms WeilDefect.MasterRecon.V10B50a.pole_literal
#print axioms WeilDefect.MasterRecon.V10B50a.adjoint_span_iff
