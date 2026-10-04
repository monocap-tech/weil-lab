import WeilDefect.Arithmetic.ActualZetaGreenGraphMixed
import WeilDefect.Morphology.NeutralLogSourceDomainRealization

namespace WeilDefect
noncomputable section
open ContinuousLinearMap
open scoped InnerProduct
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false

/-- Source graph equations determine both full coefficient vectors from the
logarithmic physical coordinate. This is uniqueness, not surjectivity. -/
theorem neutralActualZetaSourcePhysical_injective (a : ℝ) :
    Function.Injective (neutralActualZetaSourcePhysical a) := by
  intro f g h
  apply Subtype.ext
  apply Prod.ext
  · exact h
  · apply Prod.ext
    · apply lp.ext
      intro q
      exact (f.property q).1.trans ((congrArg
        (fun x => inner ℂ (neutralLogPositivePairSource a
          (neutralActualZetaDivisorOrdinate q)) x) h).trans (g.property q).1.symm)
    · apply lp.ext
      intro q
      exact (f.property q).2.trans ((congrArg
        (fun x => inner ℂ (neutralLogNegativePairSource a
          (neutralActualZetaDivisorOrdinate q)) x) h).trans (g.property q).2.symm)

/-- Hilbert graph re-coordination preserves that uniqueness. -/
theorem neutralActualZetaHilbertSourcePhysical_injective (a : ℝ) :
    Function.Injective (neutralActualZetaHilbertSourcePhysical a) := by
  intro f g h
  have he := neutralActualZetaSourcePhysical_injective a h
  calc
    f = neutralActualZetaSourceToHilbert a (neutralActualZetaHilbertToSource a f) :=
      (neutralActualZetaSourceToHilbert_hilbertToSource a f).symm
    _ = neutralActualZetaSourceToHilbert a (neutralActualZetaHilbertToSource a g) :=
      congrArg (neutralActualZetaSourceToHilbert a) he
    _ = g := neutralActualZetaSourceToHilbert_hilbertToSource a g

/-- Absolute convergence permits addition of the actual Green series. -/
theorem neutralActualZetaGreenSynthesis_add (a : ℝ) (ha : 0 < a)
    (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenSynthesis a (v + w) =
      neutralActualZetaGreenSynthesis a v + neutralActualZetaGreenSynthesis a w := by
  unfold neutralActualZetaGreenSynthesis
  simp only [lp.coeFn_add, Pi.add_apply, add_smul]
  exact (neutralActualZetaGreenSeries_summable a ha v).tsum_add
    (neutralActualZetaGreenSeries_summable a ha w)

/-- Scalar multiplication commutes with the same convergent series. -/
theorem neutralActualZetaGreenSynthesis_smul (a : ℝ) (ha : 0 < a)
    (c : ℂ) (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenSynthesis a (c • v) = c • neutralActualZetaGreenSynthesis a v := by
  unfold neutralActualZetaGreenSynthesis
  simp only [lp.coeFn_smul, Pi.smul_apply, smul_smul]
  exact tsum_smul c (fun q => v q • neutralActualZetaGreenColumn a q)

/-- Actual canonical Green attachment is linear on the full coefficient
space. No boundedness in the source graph norm is assumed. -/
def neutralActualZetaGreenCanonicalLinear (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenCoefficients →ₗ[ℂ] neutralCanonicalLogFormDomain a where
  toFun := neutralActualZetaGreenCanonical a ha
  map_add' v w := Subtype.ext (neutralActualZetaGreenSynthesis_add a ha v w)
  map_smul' c v := Subtype.ext (neutralActualZetaGreenSynthesis_smul a ha c v)

/-- The unchanged canonical logarithmic coordinate as a genuine linear map. -/
def neutralActualZetaGreenLogLinear (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenCoefficients →ₗ[ℂ] NeutralLogHilbertCarrier a :=
  (neutralLogHilbertCanonicalLinearEquiv a).symm.toLinearMap.comp
    (neutralActualZetaGreenCanonicalLinear a ha)

/-- Source uniqueness promotes the concrete Green lifts to a linear map,
retaining both source coordinates rather than choosing new coefficients. -/
def neutralActualZetaGreenSourceLinear (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenCoefficients →ₗ[ℂ] NeutralActualZetaSourceDomain a where
  toFun := neutralActualZetaGreenSourceLift a ha
  map_add' v w := by
    apply neutralActualZetaSourcePhysical_injective a
    rw [map_add, neutralActualZetaGreenSourceLift_physical,
      neutralActualZetaGreenSourceLift_physical, neutralActualZetaGreenSourceLift_physical]
    exact (neutralActualZetaGreenLogLinear a ha).map_add v w
  map_smul' c v := by
    apply neutralActualZetaSourcePhysical_injective a
    rw [map_smul, neutralActualZetaGreenSourceLift_physical,
      neutralActualZetaGreenSourceLift_physical]
    exact (neutralActualZetaGreenLogLinear a ha).map_smul c v

/-- The already certified Hilbert Green lift, now with its proved linearity. -/
def neutralActualZetaGreenHilbertSourceLinear (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenCoefficients →ₗ[ℂ] NeutralActualZetaHilbertSourceDomain a :=
  (neutralActualZetaSourceToHilbert a).toLinearMap.comp
    (neutralActualZetaGreenSourceLinear a ha)

/-- Closed submodule obtained from the actual linear range. The next theorem
identifies it with the prior set closure, so no larger span is substituted. -/
def neutralActualZetaGreenClosedSubmodule (a : ℝ) (ha : 0 < a) :
    ClosedSubmodule ℂ (NeutralActualZetaHilbertSourceDomain a) :=
  ⟨(neutralActualZetaGreenHilbertSourceLinear a ha).range.topologicalClosure,
    (neutralActualZetaGreenHilbertSourceLinear a ha).range.isClosed_topologicalClosure⟩

theorem neutralActualZetaGreenClosedSubmodule_coe (a : ℝ) (ha : 0 < a) :
    (neutralActualZetaGreenClosedSubmodule a ha :
      Set (NeutralActualZetaHilbertSourceDomain a)) =
      neutralActualZetaGreenGraphClosure a ha := rfl

theorem neutralActualZetaGreenGraphClosure_add_mem (a : ℝ) (ha : 0 < a)
    (f g : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha)
    (hg : g ∈ neutralActualZetaGreenGraphClosure a ha) :
    f + g ∈ neutralActualZetaGreenGraphClosure a ha :=
  (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule.add_mem hf hg

theorem neutralActualZetaGreenGraphClosure_smul_mem (a : ℝ) (ha : 0 < a)
    (c : ℂ) (f : NeutralActualZetaHilbertSourceDomain a)
    (hf : f ∈ neutralActualZetaGreenGraphClosure a ha) :
    c • f ∈ neutralActualZetaGreenGraphClosure a ha :=
  (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule.smul_mem c hf

/-- The genuine complete Hilbert domain of actual Green graph limits. -/
abbrev NeutralActualZetaGreenGraphDomain (a : ℝ) (ha : 0 < a) :=
  (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule

instance neutralActualZetaGreenGraphDomain_innerProduct (a : ℝ) (ha : 0 < a) :
    InnerProductSpace ℂ (NeutralActualZetaGreenGraphDomain a ha) :=
  Submodule.innerProductSpace (𝕜 := ℂ) (E := NeutralActualZetaHilbertSourceDomain a)
    (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule

instance neutralActualZetaGreenGraphDomain_complete (a : ℝ) (ha : 0 < a) :
    CompleteSpace (NeutralActualZetaGreenGraphDomain a ha) :=
  (neutralActualZetaGreenClosedSubmodule a ha).isClosed.completeSpace_coe

theorem neutralActualZetaGreenGraphDomain_completeSpace (a : ℝ) (ha : 0 < a) :
    CompleteSpace (NeutralActualZetaGreenGraphDomain a ha) := inferInstance

/-- Every pair in this proved Hilbert domain carries the certified native
mixed identity without a separately supplied closure-membership premise. -/
theorem neutralActualZetaGreenGraphDomain_mixed (a : ℝ) (ha : 0 < a)
    (f g : NeutralActualZetaGreenGraphDomain a ha) :
    inner ℂ f.val (neutralActualZetaHilbertSourceOperator a g.val) =
      inner ℂ (neutralActualZetaHilbertSourcePhysical a f.val)
        (neutralActualZetaLogWeilFormOperator a
          (neutralActualZetaHilbertSourcePhysical a g.val)) :=
  neutralActualZetaGreenGraphClosure_mixed a ha f.val g.val f.property g.property

end
end WeilDefect
