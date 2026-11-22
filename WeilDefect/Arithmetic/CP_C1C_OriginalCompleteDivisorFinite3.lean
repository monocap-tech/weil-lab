import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP-C1(C) source-contract candidate. No new positivity or RH statement.

This does NOT use CP-C1(B), IV010 or the unproved spectral-trace model.
It directly specializes the already kernel-accepted original IV008/IV009
mixed-entry and physical diagonal dictionaries to Fin 3.

The complete original divisor retains every zero with multiplicity,
and the matching original mixed arithmetic entry remains the full
Zeta23.EF.literatureRHS (pole - prime + Gamma) expression.

The specific CP001 frozen bump shape and its numeric enclosures are
NOT represented by the arbitrary supported Schwartz family below.
No independent zero roster/normalization dictionary is inferred.

SOURCE CANDIDATE ONLY: no compiler/axiom receipt for these new names.
-/

/-- Exact full-multiplicity arithmetic-to-divisor equality for all
nine entries of an arbitrary authentic supported Fin 3 family. -/
theorem neutralCPC1C_originalFiniteThree_matrix_eq_divisor
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) :
    (fun i j : Fin 3 => neutralIV007OriginalMixedEntry a s i j) =
      (fun i j : Fin 3 => neutralIV007OriginalDivisorEntry a s i j) := by
  funext i j
  exact (neutralIV008OriginalMixedEntry_eq_divisor a s hs i j).symm

/-- The full original physical signed Weil diagonal equals the
complete untruncated zeta-divisor mixed 3x3 energy. It is NOT a
positive semidefinite Gram representation off the critical line. -/
theorem neutralCPC1C_originalFiniteThree_diagonal_eq_divisorEnergy
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ))
    (u : Fin 3 → ℂ)
    (hs : ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) :
    Zeta23.EF.literatureRHS
        (neutralWindowCorrelation a
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)) =
      ∑ i : Fin 3, ∑ j : Fin 3,
        conj (u i) * neutralIV007OriginalDivisorEntry a s i j * u j := by
  calc
    Zeta23.EF.literatureRHS
        (neutralWindowCorrelation a
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)) =
        neutralIV007OriginalMixedEnergy a s u :=
          (neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
            a s u hs).symm
    _ = ∑ i : Fin 3, ∑ j : Fin 3,
          conj (u i) * neutralIV007OriginalDivisorEntry a s i j * u j := by
      unfold neutralIV007OriginalMixedEnergy
      apply Finset.sum_congr rfl
      intro i hi
      apply Finset.sum_congr rfl
      intro j hj
      rw [← neutralIV008OriginalMixedEntry_eq_divisor a s hs i j]

/-- The exact complete original divisor matrix is Hermitian; it is
not thereby positive semidefinite. -/
theorem neutralCPC1C_originalFiniteThree_divisorHermitian
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ)) (i j : Fin 3) :
    conj (neutralIV007OriginalDivisorEntry a s i j) =
      neutralIV007OriginalDivisorEntry a s j i := by
  exact neutralIV008OriginalDivisorEntry_hermitian a s i j

#print axioms neutralIV008OriginalMixedEntry_eq_divisor
#print axioms neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
#print axioms neutralCPC1C_originalFiniteThree_matrix_eq_divisor
#print axioms neutralCPC1C_originalFiniteThree_diagonal_eq_divisorEnergy
#print axioms neutralCPC1C_originalFiniteThree_divisorHermitian

end
end WeilDefect
