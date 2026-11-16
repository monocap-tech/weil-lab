import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramRightInverse
import Mathlib.MeasureTheory.Function.L2Space

namespace WeilDefect
noncomputable section
open MeasureTheory Module
open scoped SchwartzMap ComplexConjugate

/-!
NF549: FIRST EXACT INTEGRAL IDENTIFICATION OF THE TRUE ORIGINAL
242-MOMENT PHYSICAL GRAM IN LEAN SOURCE.

The original selected full-window J_i is a genuine complex L²
class, not a pointwise substitute. The canonical cutoff χ and
the 242 original χ*j_i Schwartz columns are the exact NF548 objects.

This module carefully uses L²-a.e. compatibility, not an illegal
identification of arbitrary L² equivalence classes pointwise.

The final strict-positive analytic weighted Gram proof is still
open; here we eliminate the first source-GRAM integral-identity gap.
-/

/-- Every concrete original selected physical J_i moment of a
Schwartz test is the ORIGINAL full-window integral, with no
unidentified linear functional. This theorem uses the actual
L² pairing and both honest a.e. representatives. -/
theorem neutralNF549OriginalPhysicalMoment_eq_integral
    (i : Fin 242) (s : 𝓢(ℝ, ℂ)) :
    neutralNF546OriginalSelectedMoments (s.toLp 2 volume) i =
      ∫ x : ℝ, conj (neutralNF546OriginalWindowGenerator i x) * s x ∂volume := by
  change inner ℂ (neutralNF546OriginalSelectedPhysicalL2 i)
      (s.toLp 2 volume) = _
  rw [MeasureTheory.L2.inner_def]
  apply integral_congr_ae
  filter_upwards
    [neutralNF546OriginalSelectedPhysicalL2_ae i,
     s.coeFn_toLp 2 volume] with x hi hs
  simp only [hi, hs, RCLike.inner_apply, mul_comm]

/-- The fixed canonical ORIGINAL weighted Gram's i-th coordinate
is the actual physical L² inner-product integral of source J_i
against the real-even-cutoff Schwartz synthesis B_χ(d). -/
theorem neutralNF549CanonicalGram_entry_integral
    (d : Fin 242 → ℂ) (i : Fin 242) :
    neutralNF548CanonicalOriginalWeightedGram d i =
      ∫ x : ℝ,
        conj (neutralNF546OriginalWindowGenerator i x) *
          (neutralNF544BumpSynthesis
            neutralNF548CanonicalOriginalColumns d) x ∂volume := by
  change neutralNF546OriginalSelectedMoments
      ((neutralNF544BumpSynthesis
        neutralNF548CanonicalOriginalColumns d).toLp 2 volume) i = _
  exact neutralNF549OriginalPhysicalMoment_eq_integral i
    (neutralNF544BumpSynthesis neutralNF548CanonicalOriginalColumns d)

/-- The canonical J242 Schwartz synthesis is exactly the ORIGINAL
finite source combination times the one ACTUAL smooth χ, pointwise.
No second cutoff, polynomial family, or substitute moments. -/
theorem neutralNF549CanonicalSynthesis_pointwise
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF544BumpSynthesis
      neutralNF548CanonicalOriginalColumns d) x =
        neutralNF548ComplexEvenCollarCutoff x *
          (∑ j : Fin 242,
            d j * neutralNF546OriginalComplexGenerator j x) := by
  simp only [neutralNF544BumpSynthesis,
    Module.Basis.constr_apply_fintype, Pi.basisFun_repr]
  simp only [map_sum, SchwartzMap.sum_apply, SchwartzMap.smul_apply]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [neutralNF547OriginalWeightedColumn_apply]
  ring

/-- True canonical original Gram entry is therefore the ORIGINAL
weighted source integral with zero extension of J_i on [-B,B].
This is the exact infinite-continuum physical integral, not
quadrature or selected samples. -/
theorem neutralNF549CanonicalGram_eq_weighted_source_integral
    (d : Fin 242 → ℂ) (i : Fin 242) :
    neutralNF548CanonicalOriginalWeightedGram d i =
      ∫ x : ℝ,
        conj (neutralNF546OriginalWindowGenerator i x) *
          neutralNF548ComplexEvenCollarCutoff x *
          (∑ j : Fin 242,
            d j * neutralNF546OriginalComplexGenerator j x) ∂volume := by
  rw [neutralNF549CanonicalGram_entry_integral]
  apply integral_congr_ae
  filter_upwards [] with x
  rw [neutralNF549CanonicalSynthesis_pointwise d x]
  ring

/-- The genuine original selected J242 physical source span
inside actual L², synthesized from the 242 SOURCE GENERATORS.
No arbitrary Hilbert basis is substituted. -/
def neutralNF549OriginalPhysicalSynthesis :
    (Fin 242 → ℂ) →ₗ[ℂ] RealComplexL2 :=
  (Pi.basisFun ℂ (Fin 242)).constr ℂ
    neutralNF546OriginalSelectedPhysicalL2

/-- The ORIGINAL Hermitian finite Gram quadratic form is exactly
the true physical L² pairing of (i) the original 242-generator
source combination and (ii) the smooth χ-weighted original source
combination. This is stronger than a purely abstract 242×242
algebraic identity, and needs no source-specific positivity axiom.
-/
theorem neutralNF549CanonicalGram_quadratic_eq_physical_pairing
    (d : Fin 242 → ℂ) :
    (∑ i : Fin 242,
      conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i) =
        inner ℂ (neutralNF549OriginalPhysicalSynthesis d)
          ((neutralNF544BumpSynthesis
            neutralNF548CanonicalOriginalColumns d).toLp 2 volume) := by
  simp only [neutralNF549OriginalPhysicalSynthesis,
    Module.Basis.constr_apply_fintype, Pi.basisFun_repr]
  rw [sum_inner]
  apply Finset.sum_congr rfl
  intro i hi
  rw [inner_smul_left]
  simp only [starRingEnd_apply]
  rfl

end
end WeilDefect
