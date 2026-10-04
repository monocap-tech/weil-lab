import WeilDefect.Arithmetic.ActualZetaNativeFormOperator

namespace WeilDefect
noncomputable section
open ContinuousLinearMap
open scoped InnerProduct
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false

/-- The unchanged logarithmic physical coordinate of the complete Hilbert
source graph. Its boundedness uses the graph norm, not a source bound on all L2. -/
def neutralActualZetaHilbertSourcePhysical (a : ℝ) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralLogHilbertCarrier a :=
  (neutralActualZetaSourcePhysical a).comp (neutralActualZetaHilbertToSource a)

theorem neutralActualZetaGreenHilbertSourcePhysical (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaHilbertSourcePhysical a (neutralActualZetaGreenHilbertSourceLift a ha v) =
      neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v) := by
  simp only [neutralActualZetaHilbertSourcePhysical, comp_apply,
    neutralActualZetaGreenHilbertSourceLift_custody,
    neutralActualZetaGreenSourceLift_physical]

/-- Actual closure of the certified Green lifts in the complete source graph
norm. No assertion of density in the entire graph or physical carrier is included. -/
def neutralActualZetaGreenGraphClosure (a : ℝ) (ha : 0 < a) :
    Set (NeutralActualZetaHilbertSourceDomain a) :=
  closure (Set.range (neutralActualZetaGreenHilbertSourceLift a ha))

theorem neutralActualZetaGreenGraphClosure_isClosed (a : ℝ) (ha : 0 < a) :
    IsClosed (neutralActualZetaGreenGraphClosure a ha) :=
  isClosed_closure

theorem neutralActualZetaGreenHilbertSourceLift_mem_closure (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenHilbertSourceLift a ha v ∈ neutralActualZetaGreenGraphClosure a ha :=
  subset_closure (Set.mem_range_self v)

/-- Source/native diagonal equality extends to actual graph-norm limits of
Green lifts. Both source coefficient coordinates survive this topology. -/
theorem neutralActualZetaGreenGraphClosure_diagonal (a : ℝ) (ha : 0 < a)
    (f : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha) :
    inner ℂ f (neutralActualZetaHilbertSourceOperator a f) =
      inner ℂ (neutralActualZetaHilbertSourcePhysical a f)
        (neutralActualZetaLogWeilFormOperator a (neutralActualZetaHilbertSourcePhysical a f)) := by
  have hs : Continuous (fun x : NeutralActualZetaHilbertSourceDomain a =>
      inner ℂ x (neutralActualZetaHilbertSourceOperator a x)) :=
    continuous_id.inner (𝕜 := ℂ) (neutralActualZetaHilbertSourceOperator a).continuous
  have hn : Continuous (fun x : NeutralActualZetaHilbertSourceDomain a =>
      inner ℂ (neutralActualZetaHilbertSourcePhysical a x)
        (neutralActualZetaLogWeilFormOperator a (neutralActualZetaHilbertSourcePhysical a x))) :=
    (neutralActualZetaHilbertSourcePhysical a).continuous.inner (𝕜 := ℂ)
      ((neutralActualZetaLogWeilFormOperator a).continuous.comp
        (neutralActualZetaHilbertSourcePhysical a).continuous)
  have hc := isClosed_eq hs hn
  have hsub : Set.range (neutralActualZetaGreenHilbertSourceLift a ha) ⊆
      {x : NeutralActualZetaHilbertSourceDomain a |
        inner ℂ x (neutralActualZetaHilbertSourceOperator a x) =
          inner ℂ (neutralActualZetaHilbertSourcePhysical a x)
            (neutralActualZetaLogWeilFormOperator a (neutralActualZetaHilbertSourcePhysical a x))} := by
    rintro x ⟨v, rfl⟩
    rw [neutralActualZetaGreenHilbertSourcePhysical a ha v]
    exact neutralActualZetaGreenHilbertSource_native_operator_diagonal a ha v
  exact closure_minimal hsub hc hf

/-- The actual source quadratic attaches to the canonical native quadratic
on this proved closure, without a source identity supplied as a hypothesis. -/
theorem neutralActualZetaGreenGraphClosure_source_quadratic (a : ℝ) (ha : 0 < a)
    (f : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha) :
    neutralActualZetaSourceQuadratic a (neutralActualZetaHilbertToSource a f) =
      neutralActualZetaCanonicalNativeQuadratic a
        (neutralLogHilbertToCanonical (neutralActualZetaHilbertSourcePhysical a f)) := by
  have h := neutralActualZetaGreenGraphClosure_diagonal a ha f hf
  rw [neutralActualZetaHilbertSourceOperator_diagonal,
    neutralActualZetaLogWeilFormOperator_diagonal] at h
  exact_mod_cast h

/-- The source quadratic on actual Green graph limits inherits the native
Gårding bound, with physical L2 mass explicitly retained. -/
theorem neutralActualZetaGreenGraphClosure_garding (a : ℝ) (ha : 0 < a)
    (f : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha) :
    ‖neutralActualZetaHilbertSourcePhysical a f‖ ^ 2 ≤
      neutralActualZetaSourceQuadratic a (neutralActualZetaHilbertToSource a f) +
      (neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
        ‖neutralLogPhysical (neutralActualZetaHilbertSourcePhysical a f).val‖ ^ 2 := by
  have h := neutralActualZetaLogWeilFormOperator_garding a
    (neutralActualZetaHilbertSourcePhysical a f)
  rw [← neutralActualZetaGreenGraphClosure_diagonal a ha f hf,
    neutralActualZetaHilbertSourceOperator_diagonal, Complex.ofReal_re] at h
  exact h

/-- The absolute source quadratic is controlled by the genuine physical
logarithmic norm on this proved closure, rather than by source graph energy. -/
theorem neutralActualZetaGreenGraphClosure_source_abs_le (a : ℝ) (ha : 0 < a)
    (f : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha) :
    |neutralActualZetaSourceQuadratic a (neutralActualZetaHilbertToSource a f)| ≤
      (1 + neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
        ‖neutralActualZetaHilbertSourcePhysical a f‖ ^ 2 := by
  rw [neutralActualZetaGreenGraphClosure_source_quadratic a ha f hf]
  have h := neutralActualZetaCanonicalNativeQuadratic_abs_le a
    (neutralLogHilbertToCanonical (neutralActualZetaHilbertSourcePhysical a f))
  have he : neutralLogWeightedL2
      (neutralLogHilbertToCanonical (neutralActualZetaHilbertSourcePhysical a f)) =
      (neutralActualZetaHilbertSourcePhysical a f).val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse _)
  rw [he] at h
  exact h

end
end WeilDefect
