import WeilDefect.Arithmetic.CP_C1B_OriginalNineProbeSource
import WeilDefect.Arithmetic.CP_C1C_OriginalCompleteDivisorFinite3
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP-C1(D) — NINE-SCALAR COMPLETE ORIGINAL WEIL COMPATIBILITY GATE.

This is an executable Lean CANDIDATE, not an accepted new kernel theorem.
The original source is Zeta23.EF.literatureRHS of the genuine physical
two-input correlation. CP-C1(B) supplies the actual first-antilinear
physical phase polarizations. CP-C1(C) supplies full original zeta-divisor
matrix equality. An INDEPENDENT candidate Hermitian target T is arbitrary:
its nine scalar probe comparisons are EXPLICIT HYPOTHESES, not conclusions.

No support-independent positivity, zero roster, RH, or outside spectral
model equivalence is assumed. Exact CP001 flat bump instances are unpaid.
-/

/-- Actual physical diagonal real Weil evaluation of a Schwartz test. -/
def neutralCPC1DPhysicalEnergy (a : ℝ) (f : 𝓢(ℝ, ℂ)) : ℝ :=
  (neutralCPC1BOriginalDiagonal a f).re

/-- Every ORIGINAL arithmetic 3x3 mixed real component is recovered
from physical diagonal probes of s_i, s_j and s_i+s_j. -/
theorem neutralCPC1D_original_re_from_physicalProbes
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin 3) :
    (neutralIV007OriginalMixedEntry a s i j).re =
      (neutralCPC1DPhysicalEnergy a (s i + s j) -
        neutralCPC1DPhysicalEnergy a (s i) -
        neutralCPC1DPhysicalEnergy a (s j)) / 2 := by
  change (neutralCPC1BOriginalMixed a (s i) (s j)).re =
    ((neutralCPC1BOriginalDiagonal a (s i + s j)).re -
      (neutralCPC1BOriginalDiagonal a (s i)).re -
      (neutralCPC1BOriginalDiagonal a (s j)).re) / 2
  exact neutralCPC1BOriginal_re_from_three_probes
    a (s i) (s j) (hs i) (hs j)

/-- Every ORIGINAL arithmetic 3x3 mixed imaginary component needs the
physical i-relative-phase probe. The sign is NEGATIVE (first antilinear). -/
theorem neutralCPC1D_original_im_from_physicalProbes
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin 3) :
    (neutralIV007OriginalMixedEntry a s i j).im =
      -(neutralCPC1DPhysicalEnergy a (s i + Complex.I • s j) -
        neutralCPC1DPhysicalEnergy a (s i) -
        neutralCPC1DPhysicalEnergy a (s j)) / 2 := by
  change (neutralCPC1BOriginalMixed a (s i) (s j)).im =
    -((neutralCPC1BOriginalDiagonal a (s i + Complex.I • s j)).re -
      (neutralCPC1BOriginalDiagonal a (s i)).re -
      (neutralCPC1BOriginalDiagonal a (s j)).re) / 2
  exact neutralCPC1BOriginal_im_from_three_probes
    a (s i) (s j) (hs i) (hs j)

/-- The COMPLETE original zeta-divisor entries have the same real
physical probe dictionary, via the source-specific IV008 equality. -/
theorem neutralCPC1D_divisor_re_from_physicalProbes
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin 3) :
    (neutralIV007OriginalDivisorEntry a s i j).re =
      (neutralCPC1DPhysicalEnergy a (s i + s j) -
        neutralCPC1DPhysicalEnergy a (s i) -
        neutralCPC1DPhysicalEnergy a (s j)) / 2 := by
  rw [neutralIV008OriginalMixedEntry_eq_divisor a s hs i j]
  exact neutralCPC1D_original_re_from_physicalProbes a s hs i j

/-- The COMPLETE original zeta-divisor entries retain the same
orientation-sensitive negative-imaginary phase formula. -/
theorem neutralCPC1D_divisor_im_from_physicalProbes
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin 3) :
    (neutralIV007OriginalDivisorEntry a s i j).im =
      -(neutralCPC1DPhysicalEnergy a (s i + Complex.I • s j) -
        neutralCPC1DPhysicalEnergy a (s i) -
        neutralCPC1DPhysicalEnergy a (s j)) / 2 := by
  rw [neutralIV008OriginalMixedEntry_eq_divisor a s hs i j]
  exact neutralCPC1D_original_im_from_physicalProbes a s hs i j

/-- FALSIFIABLE compatibility gate: an INDEPENDENT Hermitian target T
is exactly the original signed Weil arithmetic 3x3 matrix if it
correctly reproduces the following NINE REAL scalar measurements:
3 diagonal readings, 3 off-diagonal +1 phase readings, and
3 off-diagonal i phase readings.

The target Hermitian law is a SEPARATE hypothesis. The source matrix
itself comes from genuine original IV008/IV009 mixed Weil identities.
This is NOT an independent spectral realization or unconditional equality.
-/
theorem neutralCPC1D_original_eq_target_of_nine_phase_readings
    (a : ℝ) (s : Fin 3 → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (T : Fin 3 → Fin 3 → ℂ)
    (hHerm : ∀ i j : Fin 3, conj (T i j) = T j i)
    (hDiag : ∀ i : Fin 3,
      (T i i).re = neutralCPC1DPhysicalEnergy a (s i))
    (hPlus : ∀ i j : Fin 3, i < j →
      (T i j).re =
        (neutralCPC1DPhysicalEnergy a (s i + s j) -
          neutralCPC1DPhysicalEnergy a (s i) -
          neutralCPC1DPhysicalEnergy a (s j)) / 2)
    (hPhase : ∀ i j : Fin 3, i < j →
      (T i j).im =
        -(neutralCPC1DPhysicalEnergy a (s i + Complex.I • s j) -
          neutralCPC1DPhysicalEnergy a (s i) -
          neutralCPC1DPhysicalEnergy a (s j)) / 2) :
    (fun i j : Fin 3 => neutralIV007OriginalMixedEntry a s i j) = T := by
  have hOriginalHerm :
      ∀ i j : Fin 3,
        conj (neutralIV007OriginalMixedEntry a s i j) =
          neutralIV007OriginalMixedEntry a s j i := by
    intro i j
    exact neutralIV008OriginalMixedEntry_hermitian a s hs i j
  have hTargetDiagIm : ∀ i : Fin 3, (T i i).im = 0 := by
    intro i
    have hh := congrArg Complex.im (hHerm i i)
    simp only [Complex.conj_im] at hh
    linarith
  have hUpper : ∀ i j : Fin 3, i < j →
      neutralIV007OriginalMixedEntry a s i j = T i j := by
    intro i j hij
    apply Complex.ext
    · rw [neutralCPC1D_original_re_from_physicalProbes a s hs i j]
      exact (hPlus i j hij).symm
    · rw [neutralCPC1D_original_im_from_physicalProbes a s hs i j]
      exact (hPhase i j hij).symm
  funext i j
  rcases lt_trichotomy i j with hij | heq | hji
  · exact hUpper i j hij
  · subst j
    apply Complex.ext
    · change neutralCPC1DPhysicalEnergy a (s i) = (T i i).re
      exact (hDiag i).symm
    · rw [neutralIV008OriginalMixedDiagonal_im_zero a s hs i,
          hTargetDiagIm i]
  · calc
      neutralIV007OriginalMixedEntry a s i j =
          conj (neutralIV007OriginalMixedEntry a s j i) :=
            (hOriginalHerm j i).symm
      _ = conj (T j i) := congrArg conj (hUpper j i hji)
      _ = T i j := hHerm j i

#print axioms neutralIV008OriginalMixedEntry_eq_divisor
#print axioms neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
#print axioms neutralCPC1D_original_re_from_physicalProbes
#print axioms neutralCPC1D_original_im_from_physicalProbes
#print axioms neutralCPC1D_divisor_re_from_physicalProbes
#print axioms neutralCPC1D_divisor_im_from_physicalProbes
#print axioms neutralCPC1D_original_eq_target_of_nine_phase_readings

end
end WeilDefect
