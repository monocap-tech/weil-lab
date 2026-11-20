import WeilDefect.Arithmetic.ActualZetaOriginalCollarCoercivity

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap

/-!
NF735: retype existing NF600 *genuine signed explicit-formula*
coercivity as stability under pairwise complex superposition
INSIDE the same literal, frozen two-collar support E.

This is not the cross-support bridge: when one source falls outside
the fixed E, NF600's support hypothesis is unavailable.
-/

def neutralNF735InOriginalCollars (s : 𝓢(ℝ,ℂ)) : Prop :=
  ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → s x = 0

theorem neutralNF735OriginalCollars_add
    (s t : 𝓢(ℝ,ℂ))
    (hs : neutralNF735InOriginalCollars s)
    (ht : neutralNF735InOriginalCollars t) :
    neutralNF735InOriginalCollars (s + t) := by
  intro x hx
  simp [hs x hx, ht x hx]

theorem neutralNF735OriginalCollars_smul
    (z : ℂ) (s : 𝓢(ℝ,ℂ))
    (hs : neutralNF735InOriginalCollars s) :
    neutralNF735InOriginalCollars (z • s) := by
  intro x hx
  simp [hs x hx]

/-- Arbitrary *complex* linear combinations of two actual original
collar tests satisfy the literal EF 2/5 lower bound; this is a
consequence of the existing NF600 infinite-dimensional inequality. -/
theorem neutralNF735OriginalLocalSpanTwo_coercive
    (s t : 𝓢(ℝ,ℂ)) (z w : ℂ)
    (hs : neutralNF735InOriginalCollars s)
    (ht : neutralNF735InOriginalCollars t) :
    (2/5:ℝ) * ‖(z • s + w • t).toLp 2 volume‖^2 ≤
      neutralNF598SmoothWeil (z • s + w • t) := by
  exact neutralNF600SmoothCollarLower (z • s + w • t)
    (neutralNF735OriginalCollars_add _ _
      (neutralNF735OriginalCollars_smul z s hs)
      (neutralNF735OriginalCollars_smul w t ht))

/-- An actual source-specific Weil nonnegativity theorem for a
two-generator span, but ONLY for functions both supported in E. -/
theorem neutralNF735OriginalLocalSpanTwo_nonnegative
    (s t : 𝓢(ℝ,ℂ)) (z w : ℂ)
    (hs : neutralNF735InOriginalCollars s)
    (ht : neutralNF735InOriginalCollars t) :
    0 ≤ neutralNF598SmoothWeil (z • s + w • t) := by
  have h := neutralNF735OriginalLocalSpanTwo_coercive s t z w hs ht
  have h0 : (0:ℝ) ≤ (2/5:ℝ) * ‖(z • s + w • t).toLp 2 volume‖^2 := by
    positivity
  exact h0.trans h

#print axioms neutralNF735OriginalCollars_add
#print axioms neutralNF735OriginalCollars_smul
#print axioms neutralNF735OriginalLocalSpanTwo_coercive
#print axioms neutralNF735OriginalLocalSpanTwo_nonnegative

end
end WeilDefect
