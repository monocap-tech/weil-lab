import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalEvenCollarCutoff

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
NF548 final interface: no arbitrary moment map, no arbitrary
Schwartz columns, and no arbitrary cutoff χ. The only remaining
source-specific mathematical gate is STRICT positive definiteness
of the one canonical ORIGINAL J242 Gram.
-/

/-- ALL original 242 source correction directions with the SAME
explicit even nonnegative C∞ cutoff and true sinh pole. -/
def neutralNF548CanonicalOriginalColumns : Fin 242 → 𝓢(ℝ, ℂ) :=
  neutralNF547OriginalWeightedColumns
    neutralNF548ComplexEvenCollarCutoff
    neutralNF548ComplexEvenCollarCutoff_smooth
    neutralNF548ComplexEvenCollarCutoff_hasCompactSupport

/-- Canonical source χj columns vanish outside the original
terminal collars, by construction—not a separate geometry hypothesis. -/
theorem neutralNF548CanonicalOriginalColumns_supported
    (j : Fin 242) (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    neutralNF548CanonicalOriginalColumns j x = 0 := by
  exact neutralNF547OriginalWeightedColumn_supported
    neutralNF548ComplexEvenCollarCutoff
    neutralNF548ComplexEvenCollarCutoff_smooth
    neutralNF548ComplexEvenCollarCutoff_hasCompactSupport
    neutralNF548ComplexEvenCollarCutoff_supported j x hx

/-- Original full-window physical source moments of the exact
canonical χj corrections; no free Gram matrix or coefficient family. -/
theorem neutralNF548CanonicalGram_eq_physical :
    neutralNF548CanonicalOriginalWeightedGram =
      neutralNF544PhysicalGram
        neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns := by
  rfl

/-- POSITIVITY OF THE CONCRETE CANONICAL SOURCE GRAM is the final
undischarged finite-rank arithmetic/analytic premise. The source
independence proof from NF545 establishes it on paper, but its
actual weighted integral positivity is NOT YET compiled in Lean. -/
def neutralNF548CanonicalRightInverse
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) *
          (neutralNF548CanonicalOriginalWeightedGram d) i).re) :
    NeutralNF543RightInverse :=
  neutralNF544GramRightInverse
    neutralNF546OriginalSelectedMoments
    neutralNF548CanonicalOriginalColumns
    (neutralNF544PhysicalGram_injective_of_pos
      neutralNF546OriginalSelectedMoments
      neutralNF548CanonicalOriginalColumns hpos)

/-- The constructed fixed original J242 source correction has all
242 exact same-source moments, with NO right-inverse assumption. -/
theorem neutralNF548CanonicalRightInverse_correct
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) *
          (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (d : Fin 242 → ℂ) :
    neutralNF546OriginalSelectedMoments
      ((neutralNF548CanonicalRightInverse hpos d).toLp 2 volume) = d := by
  exact neutralNF544GramRightInverse_correct
    neutralNF546OriginalSelectedMoments neutralNF548CanonicalOriginalColumns
    (neutralNF544PhysicalGram_injective_of_pos
      neutralNF546OriginalSelectedMoments neutralNF548CanonicalOriginalColumns hpos)
    d

/-- Every canonical original source correction remains STRICTLY
inside the authentic E, with no additional support premise. -/
theorem neutralNF548CanonicalRightInverse_supported
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) *
          (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (d : Fin 242 → ℂ) (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    (neutralNF548CanonicalRightInverse hpos d) x = 0 := by
  exact neutralNF544GramRightInverse_supported
    neutralNF546OriginalSelectedMoments neutralNF548CanonicalOriginalColumns
    (neutralNF544PhysicalGram_injective_of_pos
      neutralNF546OriginalSelectedMoments neutralNF548CanonicalOriginalColumns hpos)
    neutralNF548CanonicalOriginalColumns_supported d x hx

/-- The EXACT original endpoint source moment correction with
ALL choices M,b,χ fixed to authentic functions and geometry:
one positive-definiteness premise; NO other finite Gram premisses.

The original noncompact/singular ell_U is not asserted smooth or H¹:
only its corrected C∞ strict-collar Schwartz representatives are
admitted to the true logarithmic Hilbert carrier. -/
theorem neutralNF548OriginalMomentMatchedLogCarrier
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) *
          (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0) :
    ∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val =
        (neutralNF543Correct
          neutralNF546OriginalSelectedMoments
          (neutralNF548CanonicalRightInverse hpos) ell g).toLp 2 volume ∧
      neutralNF546OriginalSelectedMoments
        ((neutralNF543Correct
          neutralNF546OriginalSelectedMoments
          (neutralNF548CanonicalRightInverse hpos) ell g).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments ell := by
  exact neutralNF543Correct_hasOriginalLogCarrierAnd242Moments
    neutralNF546OriginalSelectedMoments
    (neutralNF548CanonicalRightInverse hpos)
    (neutralNF548CanonicalRightInverse_correct hpos)
    ell g hg
    (neutralNF548CanonicalRightInverse_supported hpos)

end
end WeilDefect
