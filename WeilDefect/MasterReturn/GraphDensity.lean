import Mathlib.Analysis.Normed.Operator.Banach
import Mathlib.Tactic

/-! RETURN108-N: final graph-density transport, isolated from arithmetic.
The physical projection is assumed bijective, not just injective.
Both spaces are complete, so the bounded inverse theorem applies.
The dense stronger carrier and its dense packet set are independent
suppliers. This does not prove any of these premises for zeta. -/
namespace WeilDefect.MasterReturn.GraphDensity

open Set

variable {V X G : Type*}
    [NormedAddCommGroup V] [NormedSpace ℂ V]
    [NormedAddCommGroup X] [NormedSpace ℂ X] [CompleteSpace X]
    [NormedAddCommGroup G] [NormedSpace ℂ G] [CompleteSpace G]

/-- A dense stronger-carrier packet set has dense physical image if the
inclusion is continuous with dense range. No inverse norm bound needed. -/
theorem dense_image_of_dense_packets
    (J : V →L[ℂ] X) (hJ : DenseRange J)
    (D : Set V) (hD : Dense D) : Dense (J '' D) := by
  let C : Set X := closure (J '' D)
  have hc : IsClosed C := isClosed_closure
  have hd : D ⊆ J ⁻¹' C := by
    intro v hv
    exact subset_closure ⟨v,hv,rfl⟩
  have hpre := closure_minimal hd (hc.preimage J.continuous)
  have hr : Set.range J ⊆ C := by
    rintro x ⟨v,rfl⟩
    exact hpre (hD v)
  intro x
  exact closure_minimal hr hc (hJ x)

/-- Density in the physical coordinate implies density in a complete
source graph once its physical projection is bounded and bijective.
In particular a closed graph subspace with dense physical image is
the entire graph. -/
theorem closed_graph_eq_univ_of_dense_physical
    (P : G →L[ℂ] X) (hP : Function.Bijective P)
    (S : Set G) (hS : IsClosed S) (hD : Dense (P '' S)) :
    S = Set.univ := by
  let E : G ≃L[ℂ] X := ContinuousLinearEquiv.ofBijective P
    (LinearMap.ker_eq_bot.mpr hP.1) (LinearMap.range_eq_top.mpr hP.2)
  have hEP (g : G) : E g = P g := rfl
  have hsub : P '' S ⊆ E.symm ⁻¹' S := by
    rintro x ⟨g,hg,rfl⟩
    change E.symm (P g) ∈ S
    rw [← hEP g,E.symm_apply_apply]
    exact hg
  have hcl := closure_minimal hsub (hS.preimage E.symm.continuous)
  apply Set.eq_univ_of_forall
  intro g
  have hg := hcl (hD (P g))
  change E.symm (P g) ∈ S at hg
  rwa [← hEP g,E.symm_apply_apply] at hg

/-- The complete density transport from a stronger carrier, through
physical space, into a closed graph subspace. -/
theorem closed_graph_eq_univ_of_packet_transport
    (J : V →L[ℂ] X) (hJ : DenseRange J)
    (D : Set V) (hD : Dense D)
    (P : G →L[ℂ] X) (hP : Function.Bijective P)
    (S : Set G) (hS : IsClosed S)
    (hattach : J '' D ⊆ P '' S) : S = Set.univ :=
  closed_graph_eq_univ_of_dense_physical P hP S hS
    ((dense_image_of_dense_packets J hJ D hD).mono hattach)

end WeilDefect.MasterReturn.GraphDensity

#print axioms WeilDefect.MasterReturn.GraphDensity.dense_image_of_dense_packets
#print axioms WeilDefect.MasterReturn.GraphDensity.closed_graph_eq_univ_of_dense_physical
#print axioms WeilDefect.MasterReturn.GraphDensity.closed_graph_eq_univ_of_packet_transport
