import WeilDefect.Generated.F08.OriginalSchwartzCarrierApprox
import WeilDefect.Arithmetic.ActualZetaNativeFormOperator

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap InnerProduct

/-- Physical reconstruction is faithful on the original supported weighted carrier. -/
theorem f08_076_physical_injective (a : ℝ) :
    Function.Injective (fun k : NeutralLogHilbertCarrier a => neutralLogPhysical k.val) := by
  intro p q h
  have hc : neutralLogHilbertToCanonical p = neutralLogHilbertToCanonical q :=
    Subtype.ext h
  have hk := congrArg (neutralCanonicalToLogHilbert (a := a)) hc
  rw [neutralLogHilbertToCanonical_rightInverse p,
    neutralLogHilbertToCanonical_rightInverse q] at hk
  exact hk

/-- Actual strict-interior Schwartz core, specified in physical L² rather than
by an abstract density witness. -/
def f08_076_core (a : ℝ) : Set (NeutralLogHilbertCarrier a) :=
  {q | ∃ s : 𝓢(ℝ, ℂ),
    tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a ∧
    (∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) ∧
    neutralLogPhysical q.val = s.toLp 2 volume}

theorem f08_076_core_dense (a : ℝ) (ha : 0 < a) :
    Dense (f08_076_core a) := by
  rw [Metric.dense_iff]
  intro k ε hε
  obtain ⟨q, s, hs, hw, hp, he⟩ :=
    f08_075_original_schwartzCarrier_approx ha k ε hε
  refine ⟨q, ⟨s, hs, hw, hp⟩, ?_⟩
  simpa only [dist_eq_norm, norm_sub_rev] using he

/-- Exact lift identification for any physically faithful lift, in particular
the independently certified IV102 lift. No IV103 source identity is assumed. -/
theorem f08_076_lift_identification (a : ℝ) (q l : NeutralLogHilbertCarrier a)
    (s : 𝓢(ℝ, ℂ))
    (hq : neutralLogPhysical q.val = s.toLp 2 volume)
    (hl : neutralLogPhysical l.val = s.toLp 2 volume) :
    q = l :=
  f08_076_physical_injective a (hq.trans hl.symm)

/-- Native positivity is equivalent to positivity on the actual strict interior
Schwartz core; the arithmetic source identity is a separate obligation. -/
theorem f08_076_native_nonneg_iff_core (a : ℝ) (ha : 0 < a) :
    (∀ k : NeutralLogHilbertCarrier a,
      0 ≤ (inner ℂ k (neutralActualZetaLogWeilFormOperator a k)).re) ↔
    (∀ k ∈ f08_076_core a,
      0 ≤ (inner ℂ k (neutralActualZetaLogWeilFormOperator a k)).re) := by
  constructor
  · intro h k _
    exact h k
  · intro h k
    let S : Set (NeutralLogHilbertCarrier a) :=
      {x | 0 ≤ (inner ℂ x (neutralActualZetaLogWeilFormOperator a x)).re}
    have hc : Continuous (fun x : NeutralLogHilbertCarrier a =>
      (inner ℂ x (neutralActualZetaLogWeilFormOperator a x)).re) :=
      Complex.continuous_re.comp
        (continuous_id.inner (neutralActualZetaLogWeilFormOperator a).continuous)
    have hclosed : IsClosed S := isClosed_le continuous_const hc
    have hsub : f08_076_core a ⊆ S := fun x hx => h x hx
    have hcl := closure_minimal hsub hclosed
    rw [(f08_076_core_dense a ha).closure_eq] at hcl
    exact hcl (Set.mem_univ k)

#print axioms f08_076_physical_injective
#print axioms f08_076_core_dense
#print axioms f08_076_lift_identification
#print axioms f08_076_native_nonneg_iff_core

end
end WeilDefect
