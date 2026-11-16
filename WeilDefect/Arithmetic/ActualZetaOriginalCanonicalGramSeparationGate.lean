import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramWeightedSquare

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
NF550 — CONSEQUENCE of the actual canonical J242 source
collar-separation criterion. No extra Gram positivity, no free M,
no free Schwartz b_j, no free χ, and no assumed right inverse.

Only one exact SOURCE uniqueness condition remains in these
statements: every nonzero linear combination of the ACTUAL
NF407 242 selected functions is nonzero somewhere on the fixed
interval (c-r,c+r) inside the unchanged original positive collar.

The exponential-polynomial 136-root argument supplies an
analytic proof of this; its Lean formalization remains pending.
-/

/-- The one outstanding original-source arithmetic/analytic
nonvanishing condition, stated with the ACTUAL source generators
and the ONE exact fixed NF548 collar interval. -/
def NeutralNF550OriginalCollarSeparatesJ242 : Prop :=
  ∀ d : Fin 242 → ℂ, d ≠ 0 →
    ∃ x : ℝ,
      x ∈ Set.Ioo
        (neutralNF548CollarCenter - 1 / 2000)
        (neutralNF548CollarCenter + 1 / 2000) ∧
      neutralNF550OriginalSourceCombination d x ≠ 0

/-- Under just the SOURCE nonvanishing criterion, the fixed
canonical original weighted Gram is strictly Hermitian positive
and hence injective. Neither property is separately assumed. -/
theorem neutralNF550OriginalCanonicalGram_injective_of_source_separation
    (hsource : NeutralNF550OriginalCollarSeparatesJ242) :
    Function.Injective neutralNF548CanonicalOriginalWeightedGram := by
  exact neutralNF544PhysicalGram_injective_of_pos
    neutralNF546OriginalSelectedMoments
    neutralNF548CanonicalOriginalColumns
    (neutralNF550CanonicalOriginalGram_pos_of_collar_separation hsource)

/-- The ORIGINAL true 242-dimensional physical moment map has a
constructible strict-E-supported Schwartz right inverse, conditional
only on the actual original J242 local separation. This removes the
previous free Gram-positive-matrix hypothesis. -/
theorem neutralNF550Original242RightInverse_of_source_separation
    (hsource : NeutralNF550OriginalCollarSeparatesJ242) :
    ∃ R : NeutralNF543RightInverse,
      (∀ d : Fin 242 → ℂ,
        neutralNF546OriginalSelectedMoments
          ((R d).toLp 2 volume) = d) ∧
      (∀ (d : Fin 242 → ℂ) (x : ℝ),
        x ∉ neutralNF543OriginalCollars → (R d) x = 0) := by
  let hpos := neutralNF550CanonicalOriginalGram_pos_of_collar_separation hsource
  refine ⟨neutralNF548CanonicalRightInverse hpos, ?_, ?_⟩
  · exact neutralNF548CanonicalRightInverse_correct hpos
  · exact neutralNF548CanonicalRightInverse_supported hpos

/-- The corrected authentic smooth test is admitted to the
unmodified genuine log Hilbert carrier and matches all 242
original selected moments EXACTLY. The only source-specific
hypothesis is original J242 collar separation; the old Gram
positive-definite premise has been eliminated algebraically. -/
theorem neutralNF550Original242MomentMatchedLogCarrier_of_source_separation
    (hsource : NeutralNF550OriginalCollarSeparatesJ242)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ,
      x ∉ neutralNF543OriginalCollars → g x = 0) :
    ∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val =
        (neutralNF543Correct neutralNF546OriginalSelectedMoments
          (neutralNF548CanonicalRightInverse
            (neutralNF550CanonicalOriginalGram_pos_of_collar_separation hsource))
          ell g).toLp 2 volume ∧
      neutralNF546OriginalSelectedMoments
        ((neutralNF543Correct neutralNF546OriginalSelectedMoments
          (neutralNF548CanonicalRightInverse
            (neutralNF550CanonicalOriginalGram_pos_of_collar_separation hsource))
          ell g).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments ell := by
  exact neutralNF548OriginalMomentMatchedLogCarrier
    (neutralNF550CanonicalOriginalGram_pos_of_collar_separation hsource)
    ell g hg

end
end WeilDefect
