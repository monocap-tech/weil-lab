import WeilDefect.Arithmetic.ActualZetaOriginalSignedGraphLimit

namespace WeilDefect
noncomputable section
open InnerProductSpace

/-! NF598: physical custody determines the entire graph vector.
This does not assert that arbitrary physical L² vectors have a graph
lift, or that physical L² convergence alone implies graph convergence. -/

theorem neutralNF598LogPhysical_injective (a : ℝ) :
    Function.Injective (fun k : NeutralLogHilbertCarrier a => neutralLogPhysical k.val) := by
  intro k l h
  have he : neutralLogHilbertToCanonical k = neutralLogHilbertToCanonical l := Subtype.ext h
  calc
    k = neutralCanonicalToLogHilbert (neutralLogHilbertToCanonical k) :=
      (neutralLogHilbertToCanonical_rightInverse k).symm
    _ = neutralCanonicalToLogHilbert (neutralLogHilbertToCanonical l) :=
      congrArg (fun v => neutralCanonicalToLogHilbert v) he
    _ = l := neutralLogHilbertToCanonical_rightInverse l

theorem neutralNF598GraphPhysical_injective (a : ℝ) :
    Function.Injective (neutralNF598GraphPhysical a) := by
  intro u v h
  have hk : neutralActualZetaSourcePhysical a u = neutralActualZetaSourcePhysical a v :=
    neutralNF598LogPhysical_injective a h
  apply Subtype.ext
  apply Prod.ext
  · exact hk
  · apply Prod.ext
    · change neutralActualZetaPositiveAnalysis a u = neutralActualZetaPositiveAnalysis a v
      apply lp.ext
      funext q
      change neutralActualZetaPositiveAnalysis a u q = neutralActualZetaPositiveAnalysis a v q
      rw [(neutralActualZetaSourceAnalysis_sampling a u q).1,
        (neutralActualZetaSourceAnalysis_sampling a v q).1,hk]
    · change neutralActualZetaNegativeAnalysis a u = neutralActualZetaNegativeAnalysis a v
      apply lp.ext
      funext q
      change neutralActualZetaNegativeAnalysis a u q = neutralActualZetaNegativeAnalysis a v q
      rw [(neutralActualZetaSourceAnalysis_sampling a u q).2,
        (neutralActualZetaSourceAnalysis_sampling a v q).2,hk]

theorem neutralNF598GraphWeil_eq_of_physical (a : ℝ)
    (u v : NeutralActualZetaSourceDomain a)
    (h : neutralNF598GraphPhysical a u = neutralNF598GraphPhysical a v) :
    neutralNF598GraphWeil a u = neutralNF598GraphWeil a v :=
  congrArg (neutralNF598GraphWeil a) (neutralNF598GraphPhysical_injective a h)

end
end WeilDefect
