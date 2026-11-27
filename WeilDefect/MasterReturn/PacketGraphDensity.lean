import WeilDefect.MasterReturn.GraphDensity

/-! RETURN108-O: a dense physical packet image and a graph-norm bound
on the closed packet submodule suffice to establish surjectivity and
full graph density simultaneously. No full-domain lift is assumed. -/
namespace WeilDefect.MasterReturn.GraphDensity

open Set
variable {G X : Type*}
    [NormedAddCommGroup G] [NormedSpace ℂ G] [CompleteSpace G]
    [NormedAddCommGroup X] [NormedSpace ℂ X]

/-- An injective physical projection with bounded inverse on a complete
packet subspace is onto if that subspace has dense physical image.
The subspace must then be the whole graph. -/
theorem graph_top_and_surjective_of_closed_packet_bound
    (P : G →L[ℂ] X) (hP : Function.Injective P)
    (S : Submodule ℂ G) (hS : IsClosed (S : Set G))
    (C : ℝ≥0) (hbound : ∀ g ∈ S, ‖g‖ ≤ (C:ℝ)*‖P g‖)
    (hd : Dense (P '' (S : Set G))) :
    S = ⊤ ∧ Function.Surjective P := by
  letI : CompleteSpace S := hS.completeSpace_coe
  let Q : S →L[ℂ] X := P.comp S.subtypeL
  have hQ : AntilipschitzWith C Q := by
    apply AntilipschitzWith.of_le_mul_dist
    intro u v
    rw [dist_eq_norm,dist_eq_norm,← map_sub]
    exact hbound ((u-v : S) : G) (u-v : S).property
  have hc : IsClosed (Set.range Q) := hQ.isClosed_range Q.uniformContinuous
  have hR : Set.range Q = P '' (S : Set G) := by
    ext x
    constructor
    · rintro ⟨v,rfl⟩
      exact ⟨v.val,v.property,rfl⟩
    · rintro ⟨v,hv,rfl⟩
      exact ⟨⟨v,hv⟩,rfl⟩
  have honto : Function.Surjective Q := by
    intro x
    have hx := hd x
    rw [← hR,hc.closure_eq] at hx
    exact hx
  constructor
  · apply top_unique
    intro g hg
    obtain ⟨v,hv⟩ := honto (P g)
    have he : (v:G) = g := hP hv
    rw [← he]
    exact v.property
  · intro x
    obtain ⟨v,hv⟩ := honto x
    exact ⟨v.val,hv⟩

/-- A bound on the algebraic Green packet span suffices; continuity
extends it to the graph-norm closure, without global sample estimates
for arbitrary graph elements. -/
theorem packet_bound_extends_to_closure
    (P : G →L[ℂ] X) (D : Submodule ℂ G) (C : ℝ≥0)
    (hbound : ∀ g ∈ D, ‖g‖ ≤ (C:ℝ)*‖P g‖) :
    ∀ g ∈ D.topologicalClosure, ‖g‖ ≤ (C:ℝ)*‖P g‖ := by
  have hc : IsClosed {g : G | ‖g‖ ≤ (C:ℝ)*‖P g‖} :=
    isClosed_le continuous_norm (continuous_const.mul P.continuous.norm)
  have hsub : (D : Set G) ⊆ {g : G | ‖g‖ ≤ (C:ℝ)*‖P g‖} :=
    fun g hg => hbound g hg
  intro g hg
  exact closure_minimal hsub hc hg

end WeilDefect.MasterReturn.GraphDensity

#print axioms WeilDefect.MasterReturn.GraphDensity.graph_top_and_surjective_of_closed_packet_bound
#print axioms WeilDefect.MasterReturn.GraphDensity.packet_bound_extends_to_closure
