import WeilDefect.Arithmetic.ActualZetaOriginalJ242GlobalComplexSourceIndependence
import WeilDefect.Arithmetic.ActualZetaOriginalJ242AnalyticIdentity
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
NF567 — unconditional strict positivity of the ONE ORIGINAL
canonical J242 weighted Gram, once the exact original
NF566 real odd-jet invertibility and the NF551 local-to-global
analytic identity have both passed Lean.

This is NOT an axiom or a modified Gram. Every 241 original
sine/cosine oscillator, real sinh pole, fixed original
χ and exact NF549 physical L² pairing are preserved.

Logical chain:
  authentic 242×242 real odd jets IsUnit (NF566)
  → exact REAL global source independence
  → exact COMPLEX global source independence (NF567)
  → analytic unique continuation from original collar (NF551)
  → genuine NF550 weighted-square strict Gram
  → true strict-E-supported Schwartz right inverse.

NF550/NF551 and NF566/NF567 still have pending compiler
obligations. Therefore these are CANDIDATE Lean theorems;
do not report unconditional certified original positivity
until the entire dependent compile passes.
-/

/-- The one exact source-global-independence Prop of NF551
has a candidate proof from the authentic original analytic
odd-jet matrix rank, without additional source hypotheses. -/
theorem neutralNF567OriginalGlobalIndependence :
    NeutralNF551OriginalJ242GlobalIndependence := by
  intro d hzero
  exact neutralNF567OriginalComplexGlobalIndependent d hzero

/-- No nonzero 242-coefficient ORIGINAL source combination
can vanish across the TRUE fixed positive endpoint collar.
This is a consequence of actual source global independence
and NF551's analytic identity, not an assumption. -/
theorem neutralNF567OriginalCanonicalCollarSeparation :
    NeutralNF550OriginalCollarSeparatesJ242 := by
  exact neutralNF551OriginalJ242GlobalIndependence_implies_collar
    neutralNF567OriginalGlobalIndependence

/-- THE ACTUAL ORIGINAL 242-SOURCE WEIGHTED CANONICAL GRAM IS
STRICTLY HERMITIAN POSITIVE for every complex d ≠ 0.

The Gram is exactly the fixed NF548 original χ-weighted
physical moment Gram, not a surrogate or sampled matrix. -/
theorem neutralNF567OriginalCanonicalGram_strictPos :
    ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) *
          (neutralNF548CanonicalOriginalWeightedGram d) i).re := by
  exact neutralNF550CanonicalOriginalGram_pos_of_collar_separation
    neutralNF567OriginalCanonicalCollarSeparation

/-- The canonical original J242 Gram linear map is injective,
without assuming a free positive matrix or source separation. -/
theorem neutralNF567OriginalCanonicalGram_injective :
    Function.Injective neutralNF548CanonicalOriginalWeightedGram := by
  exact neutralNF550OriginalCanonicalGram_injective_of_source_separation
    neutralNF567OriginalCanonicalCollarSeparation

/-- An authentic Schwartz source-correction right inverse with
support strictly inside the original fixed terminal E collars
and the complete unchanged 242 physical L² moments. -/
theorem neutralNF567Original242SchwartzRightInverse :
    ∃ R : NeutralNF543RightInverse,
      (∀ d : Fin 242 → ℂ,
        neutralNF546OriginalSelectedMoments
          ((R d).toLp 2 volume) = d) ∧
      (∀ (d : Fin 242 → ℂ) (x : ℝ),
        x ∉ neutralNF543OriginalCollars → (R d) x = 0) := by
  exact neutralNF550Original242RightInverse_of_source_separation
    neutralNF567OriginalCanonicalCollarSeparation

end
end WeilDefect
