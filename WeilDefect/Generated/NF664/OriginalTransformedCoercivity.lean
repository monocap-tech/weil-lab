import WeilDefect.Generated.NF663.Complete
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramTransformedDominance

namespace WeilDefect

/-!
NF664: final source-bound 15-dimensional transformed coercivity
certificate. Every real transformed interval is from the original NF606
physical integral via the NF662/NF663 chain. The integer margin is
NF659's previously kernel-verified exact row calculation, not a new
matrix-valued assumption. The return to original coordinates requires
a separate explicit inverse/norm argument.
-/

noncomputable section

theorem nf664OriginalIntegerMargin (i : Fin 15) :
    nf658MinMargin ≤
      nf659CenterAt i i - nf659RadiusAt i i -
        ∑ j : Fin 15, if i = j then (0 : ℤ)
          else |nf659CenterAt i j| + nf659RadiusAt i j := by
  change nf658MinMargin ≤ nf659MarginAt i
  exact nf659MarginUniform i

theorem nf664AuthenticatedOriginalTransformedCoercivity
    (y : Fin 15 → ℝ) :
    ((nf658MinMargin : ℝ) / (10 ^ 64 : ℝ) ^ 3) *
      neutralNF661SqNorm y ≤
      neutralNF661Quadratic
        (neutralNF664ActualPhysicalB nf662OriginalPreconditionerReal) y := by
  exact neutralNF664PhysicalTransformed_coercivity
    nf662OriginalPreconditionerReal
    nf659CenterAt nf659RadiusAt
    ((10 ^ 64 : ℝ) ^ 3) (by positivity) nf658MinMargin
    nf663ActualPhysical_transformedEnclosed
    nf664OriginalIntegerMargin y

#print axioms nf664OriginalIntegerMargin
#print axioms nf664AuthenticatedOriginalTransformedCoercivity

end
end WeilDefect
