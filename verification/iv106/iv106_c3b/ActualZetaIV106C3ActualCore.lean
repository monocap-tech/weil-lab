import WeilDefect.Arithmetic.ActualZetaIV106C3ConstraintDensity
import WeilDefect.Generated.F08.OriginalDenseCoreTransfer
import WeilDefect.Arithmetic.ActualZetaIV106C2OriginalFormMargin

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap InnerProduct

/-- The closed-window supported Schwartz core, as a linear subspace.
It contains the strict-interior dense core of F08-076. -/
def neutralIV106C3Core (a : ℝ) : Submodule ℂ (NeutralLogHilbertCarrier a) where
  carrier := {q | ∃ s : 𝓢(ℝ, ℂ),
    (∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) ∧
    neutralLogPhysical q.val = s.toLp 2 volume}
  zero_mem' := by
    refine ⟨0, ?_, ?_⟩
    · intro x hx
      rfl
    · change neutralLogPhysical (0 : RealComplexL2) =
        SchwartzMap.toLpCLM ℂ ℂ 2 volume 0
      rw [map_zero, map_zero]
  add_mem' := by
    rintro p q ⟨u, hu, hpu⟩ ⟨v, hv, hpv⟩
    refine ⟨u+v, ?_, ?_⟩
    · intro x hx
      change u x + v x = 0
      rw [hu x hx, hv x hx, add_zero]
    · change neutralLogPhysical (p.val + q.val) =
        SchwartzMap.toLpCLM ℂ ℂ 2 volume (u+v)
      simp only [map_add, SchwartzMap.toLpCLM_apply, hpu, hpv]
  smul_mem' := by
    rintro c q ⟨s, hs, hp⟩
    refine ⟨c • s, ?_, ?_⟩
    · intro x hx
      change c • s x = 0
      rw [hs x hx, smul_zero]
    · change neutralLogPhysical (c • q.val) =
        SchwartzMap.toLpCLM ℂ ℂ 2 volume (c • s)
      simp only [map_smul, SchwartzMap.toLpCLM_apply, hp]

theorem neutralIV106C3Core_dense (a : ℝ) (ha : 0 < a) :
    Dense (neutralIV106C3Core a : Set (NeutralLogHilbertCarrier a)) := by
  apply (f08_076_core_dense a ha).mono
  rintro q ⟨s, hs, hw, hp⟩
  exact ⟨s, hw, hp⟩

theorem neutralIV106C3Core_kernel_closure (a : ℝ) (ha : 0 < a) (m : ℕ)
    (T : NeutralLogHilbertCarrier a →L[ℂ] (Fin m → ℂ)) :
    closure ((neutralIV106C3Core a : Set (NeutralLogHilbertCarrier a)) ∩
      {q | T q = 0}) = {q | T q = 0} :=
  neutralIV106C3Closure _ (neutralIV106C3Core_dense a ha) T

/-- Conditional mass margin extends to the entire closed constrained carrier.
The concrete constraint map and the core inequality remain separate gates. -/
theorem neutralIV106C3Core_mass_transfer (a : ℝ) (ha : 0 < a) (m : ℕ)
    (T : NeutralLogHilbertCarrier a →L[ℂ] (Fin m → ℂ))
    (hcore : ∀ q ∈ neutralIV106C3Core a, T q = 0 →
      ‖neutralLogPhysical q.val‖^2 ≤
        (inner ℂ q (neutralActualZetaLogWeilFormOperator a q)).re)
    (q : NeutralLogHilbertCarrier a) (hq : T q = 0) :
    ‖q‖^2 / (1+neutralIV106C2Loss a) ≤
      (inner ℂ q (neutralActualZetaLogWeilFormOperator a q)).re := by
  apply neutralIV106C2Native_form_margin a q
  let S : Set (NeutralLogHilbertCarrier a) :=
    {x | ‖neutralLogPhysical x.val‖^2 ≤
      (inner ℂ x (neutralActualZetaLogWeilFormOperator a x)).re}
  have hleft : Continuous (fun x : NeutralLogHilbertCarrier a =>
      ‖neutralLogPhysical x.val‖^2) :=
    ((neutralLogPhysical.continuous.comp continuous_subtype_val).norm).pow 2
  have hright : Continuous (fun x : NeutralLogHilbertCarrier a =>
      (inner ℂ x (neutralActualZetaLogWeilFormOperator a x)).re) :=
    Complex.continuous_re.comp
      (continuous_id.inner (neutralActualZetaLogWeilFormOperator a).continuous)
  have hc : IsClosed S := isClosed_le hleft hright
  have hs : (neutralIV106C3Core a : Set (NeutralLogHilbertCarrier a)) ∩
      {x | T x = 0} ⊆ S := by
    intro x hx
    exact hcore x hx.1 hx.2
  have h := closure_minimal hs hc
  rw [neutralIV106C3Core_kernel_closure a ha m T] at h
  exact h hq

#print axioms neutralIV106C3Core_dense
#print axioms neutralIV106C3Core_kernel_closure
#print axioms neutralIV106C3Core_mass_transfer
end
end WeilDefect
