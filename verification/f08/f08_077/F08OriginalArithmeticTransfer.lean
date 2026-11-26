import WeilDefect.Generated.F08.OriginalDenseCoreTransfer
import WeilDefect.Arithmetic.ActualZetaIV103OriginalSchwartzSpectralAttachment

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap InnerProduct

/-- The literal arithmetic attachment, now discharged by the dual-certified IV103 identity. -/
def f08_077_originalAttachment (a : ℝ) : Prop :=
  ∀ (u v : 𝓢(ℝ, ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0),
    neutralIV101Mixed a u v =
      inner ℂ (neutralIV102Lift a u hu)
        (neutralActualZetaLogWeilFormOperator a (neutralIV102Lift a v hv))

/-- Direct discharge of the arithmetic attachment from the exact IV103 source. -/
theorem f08_077_originalAttachment_of_IV103 (a : ℝ) (ha : 0 ≤ a) :
    f08_077_originalAttachment a := by
  intro u v hu hv
  exact neutralIV103Mixed_native a ha u v hu hv

/-- Full native nonnegativity iff original arithmetic nonnegativity on
all supported Schwartz tests. This is an equivalence, not positivity. -/
theorem f08_077_original_nonneg_iff_native (a : ℝ) (ha : 0 < a) :
    (∀ k : NeutralLogHilbertCarrier a,
      0 ≤ (inner ℂ k (neutralActualZetaLogWeilFormOperator a k)).re) ↔
    (∀ (s : 𝓢(ℝ, ℂ))
      (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0),
      0 ≤ (neutralIV101Mixed a s s).re) := by
  have hattach := f08_077_originalAttachment_of_IV103 a ha.le
  constructor
  · intro h s hs
    rw [hattach s s hs hs]
    exact h (neutralIV102Lift a s hs)
  · intro h
    apply (f08_076_native_nonneg_iff_core a ha).2
    intro q hq
    obtain ⟨s, _, hs, hp⟩ := hq
    have he : q = neutralIV102Lift a s hs :=
      f08_076_lift_identification a q _ s hp
        (neutralIV102Lift_physical a s hs)
    rw [he, ← hattach s s hs hs]
    exact h s hs

/-- Any separately continuous extension agreeing on the literal supported
Schwartz pairings must equal the native bounded form everywhere.
No claim about any independently defined nonsmooth source is made. -/
theorem f08_077_original_extension_unique (a : ℝ) (ha : 0 < a)
    (E : NeutralLogHilbertCarrier a → NeutralLogHilbertCarrier a → ℂ)
    (hleft : ∀ y, Continuous (fun x => E x y))
    (hright : ∀ x, Continuous (E x))
    (hsource : ∀ (u v : 𝓢(ℝ, ℂ))
      (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
      (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0),
      E (neutralIV102Lift a u hu) (neutralIV102Lift a v hv) =
        neutralIV101Mixed a u v) :
    ∀ x y, E x y = inner ℂ x (neutralActualZetaLogWeilFormOperator a y) := by
  have hattach := f08_077_originalAttachment_of_IV103 a ha.le
  let A := neutralActualZetaLogWeilFormOperator a
  have hd := f08_076_core_dense a ha
  have hcore : ∀ x ∈ f08_076_core a, ∀ y ∈ f08_076_core a,
      E x y = inner ℂ x (A y) := by
    intro x hx y hy
    obtain ⟨u, _, hu, hpu⟩ := hx
    obtain ⟨v, _, hv, hpv⟩ := hy
    have he₁ := f08_076_lift_identification a x (neutralIV102Lift a u hu) u hpu
      (neutralIV102Lift_physical a u hu)
    have he₂ := f08_076_lift_identification a y (neutralIV102Lift a v hv) v hpv
      (neutralIV102Lift_physical a v hv)
    rw [he₁, he₂]
    exact (hsource u v hu hv).trans (hattach u v hu hv)
  have hfirst : ∀ x, ∀ y ∈ f08_076_core a, E x y = inner ℂ x (A y) := by
    intro x y hy
    let S : Set (NeutralLogHilbertCarrier a) := {z | E z y = inner ℂ z (A y)}
    have hc : IsClosed S := isClosed_eq (hleft y) (continuous_id.inner continuous_const)
    have hs : f08_076_core a ⊆ S := fun z hz => hcore z hz y hy
    have hh := closure_minimal hs hc
    rw [hd.closure_eq] at hh
    exact hh (Set.mem_univ x)
  intro x y
  let S : Set (NeutralLogHilbertCarrier a) := {z | E x z = inner ℂ x (A z)}
  have hc : IsClosed S := isClosed_eq (hright x) (continuous_const.inner A.continuous)
  have hs : f08_076_core a ⊆ S := fun z hz => hfirst x z hz
  have hh := closure_minimal hs hc
  rw [hd.closure_eq] at hh
  exact hh (Set.mem_univ y)

#print axioms f08_077_originalAttachment_of_IV103
#print axioms f08_077_original_nonneg_iff_native
#print axioms f08_077_original_extension_unique
end
end WeilDefect
