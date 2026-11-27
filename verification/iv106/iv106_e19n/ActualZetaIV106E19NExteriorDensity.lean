import WeilDefect.Arithmetic.ActualZetaIV106E19MOutsideCorrection

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct

/-- The supported carrier is exactly the kernel of the original exterior
restriction after physical reconstruction. Its entire orthogonal complement
is the closure of the range of that map's adjoint. -/
theorem neutralIV106E19NExterior_density :
    (neutralLogHilbertSubmodule (11/10:ℝ)).toSubmoduleᗮ =
      (ContinuousLinearMap.adjoint
        (neutralOutsideRestriction (11/10:ℝ) ∘L neutralLogPhysical)).range.topologicalClosure := by
  change (neutralOutsideRestriction (11/10:ℝ) ∘L neutralLogPhysical).kerᗮ = _
  exact ContinuousLinearMap.orthogonal_ker _

/-- Exact adjoint factorization. The exterior correction bank does not
introduce an additional constraint on the supported problem. -/
theorem neutralIV106E19NExterior_factor (g : RealComplexL2) :
    (ContinuousLinearMap.adjoint
      (neutralOutsideRestriction (11/10:ℝ) ∘L neutralLogPhysical)) g =
      neutralIV106E19LRawColumn
        ((ContinuousLinearMap.adjoint (neutralOutsideRestriction (11/10:ℝ))) g) := by
  rw [ContinuousLinearMap.adjoint_comp]
  rfl

#print axioms neutralIV106E19NExterior_density
#print axioms neutralIV106E19NExterior_factor
end
end WeilDefect
