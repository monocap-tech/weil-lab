import Mathlib

namespace WeilDefect
noncomputable section

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    [NormedAddCommGroup F] [NormedSpace ℂ F] [FiniteDimensional ℂ F]

/-- Every constraint value is realized by a vector of the dense core. -/
theorem neutralIV106C3Range (D : Submodule ℂ E) (hd : Dense (D : Set E))
    (T : E →L[ℂ] F) (x : E) : T x ∈ (T.domRestrict D).range := by
  let S := (T.domRestrict D).range
  have hc : IsClosed (T ⁻¹' (S : Set F)) :=
    (Submodule.closed_of_finiteDimensional S).preimage T.continuous
  have hs : (D : Set E) ⊆ T ⁻¹' (S : Set F) := by
    intro d h
    exact ⟨⟨d,h⟩, rfl⟩
  have h := closure_minimal hs hc
  rw [hd.closure_eq] at h
  exact h (Set.mem_univ x)

/-- A continuous correction taking values in the original core. -/
theorem neutralIV106C3Correction (D : Submodule ℂ E) (hd : Dense (D : Set E))
    (T : E →L[ℂ] F) :
    ∃ R : E →L[ℂ] E, (∀ x, T (R x) = 0) ∧
      (∀ x, T x = 0 → R x = x) ∧ (∀ x ∈ D, R x ∈ D) := by
  let S := (T.domRestrict D).range
  let U : D →L[ℂ] S := (T.domRestrict D).rangeRestrict
  let V : E →L[ℂ] S := T.codRestrict S (neutralIV106C3Range D hd T)
  have hu : U.range = ⊤ := by
    apply top_unique
    intro y _
    obtain ⟨d, h⟩ := y.property
    exact ⟨d, Subtype.ext h⟩
  obtain ⟨J,hJ⟩ := U.exists_rightInverse_of_surjective hu
  let R : E →L[ℂ] E := ContinuousLinearMap.id ℂ E - D.subtypeL.comp (J.comp V)
  refine ⟨R, ?_, ?_, ?_⟩
  · intro x
    have h := congrArg (fun f : S →L[ℂ] S => f (V x)) hJ
    have he : T (J (V x) : E) = T x :=
      congrArg (fun y : S => (y : F)) h
    change T (x - (J (V x) : E)) = 0
    rw [map_sub, he, sub_self]
  · intro x hx
    have hv : V x = 0 := Subtype.ext hx
    change x - (J (V x) : E) = x
    rw [hv, map_zero]
    exact sub_zero x
  · intro x hx
    change x - (J (V x) : E) ∈ D
    exact D.sub_mem hx (J (V x)).property

/-- Density survives finitely many exact continuous linear constraints. -/
theorem neutralIV106C3Closure (D : Submodule ℂ E) (hd : Dense (D : Set E))
    (T : E →L[ℂ] F) :
    closure ((D : Set E) ∩ {x | T x = 0}) = {x | T x = 0} := by
  obtain ⟨R,hR,hfix,hD⟩ := neutralIV106C3Correction D hd T
  let K : Set E := {x | T x = 0}
  let A : Set E := (D : Set E) ∩ K
  change closure A = K
  have hc : IsClosed K := isClosed_eq T.continuous continuous_const
  apply Set.Subset.antisymm
  · exact closure_minimal (fun _ h => h.2) hc
  · have hs : (D : Set E) ⊆ R ⁻¹' closure A := by
      intro x hx
      exact subset_closure ⟨hD x hx, hR x⟩
    have hall := closure_minimal hs (isClosed_closure.preimage R.continuous)
    rw [hd.closure_eq] at hall
    intro x hx
    have h : R x ∈ closure A := hall (Set.mem_univ x)
    rwa [hfix x hx] at h

#print axioms neutralIV106C3Range
#print axioms neutralIV106C3Correction
#print axioms neutralIV106C3Closure
end
end WeilDefect
