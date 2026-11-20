import WeilDefect.Arithmetic.ActualZetaPhaseIVWindowNaturality

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
IV007 / Phase IV: exact FINITE-FAMILY transport of the original signed
two-argument Weil EF under physical-window enlargement.

A finite family of arbitrary complex Schwartz tests is held FIXED while
the containing observation window expands. We prove equality of every
literal arithmetic mixed entry, every original divisor-series mixed
entry, and the entire finite complex quadratic energy.

This is a genuine-source naturality / obligation-transfer result,
NOT an estimate on newly admitted supports. In particular the
universal real-quadratic nonnegativity gate is proved only
ANTITONE in the support radius: positivity on a larger class implies
positivity on each smaller class; the converse is NOT established.

This source imports IV006, whose independent kernel verification must
succeed before IV007's source theorems can be accepted.
-/

/-- An actual mixed signed Weil EF entry for a finite family of complex
Schwartz tests, with the authentic two-argument window correlation. -/
def neutralIV007OriginalMixedEntry {n : ℕ}
    (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ)) (i j : Fin n) : ℂ :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a
      ((s i).toLp 2 volume) ((s j).toLp 2 volume))

/-- The original all-multiplicity divisor zero-side entry in the
exact conjugation/frequency orientation used by the source. -/
def neutralIV007OriginalDivisorEntry {n : ℕ}
    (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ)) (i j : Fin n) : ℂ :=
  ∑' q : NeutralActualZetaDivisorCoordinate,
    conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate q))
      ((s i).toLp 2 volume)) *
      neutralWindowEvaluation a
        (neutralActualZetaDivisorOrdinate q)
        ((s j).toLp 2 volume)

/-- The full finite mixed Weil quadratic energy, retaining the
complex value rather than discarding the imaginary part prematurely.
No Hermitian symmetry or positive sign is assumed. -/
def neutralIV007OriginalMixedEnergy {n : ℕ}
    (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ) : ℂ :=
  ∑ i : Fin n, ∑ j : Fin n,
    conj (u i) * neutralIV007OriginalMixedEntry a s i j * u j

/-- Every genuine mixed EF entry is unchanged under enlargement of a
window already containing the entire fixed finite family. -/
theorem neutralIV007OriginalMixedEntry_natural
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin n) :
    neutralIV007OriginalMixedEntry a s i j =
      neutralIV007OriginalMixedEntry b s i j := by
  exact neutralIV006LiteralMixedEF_natural a b hab
    (s i) (s j) (hs i) (hs j)

/-- Every all-multiplicity original divisor entry is unchanged as well.
The actual zeta divisor copies and their conjugate samples are retained. -/
theorem neutralIV007OriginalDivisorEntry_natural
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin n) :
    neutralIV007OriginalDivisorEntry a s i j =
      neutralIV007OriginalDivisorEntry b s i j := by
  exact neutralIV006MixedDivisorSum_eq_of_support a b (s i) (s j)
    (hs i)
    (neutralIV006Schwartz_support_expand a b hab (s i) (hs i))
    (hs j)
    (neutralIV006Schwartz_support_expand a b hab (s j) (hs j))

/-- The entire indexed mixed entry matrix is literally the same
function on two index coordinates in both containing windows. -/
theorem neutralIV007OriginalMixedMatrix_natural
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) :
    (fun i j : Fin n => neutralIV007OriginalMixedEntry a s i j) =
      (fun i j : Fin n => neutralIV007OriginalMixedEntry b s i j) := by
  funext i
  funext j
  exact neutralIV007OriginalMixedEntry_natural a b hab s hs i j

/-- Simultaneous finite-family transport, with ARBITRARY complex
coefficients and all cross terms included. No estimates or RH. -/
theorem neutralIV007OriginalMixedEnergy_natural
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (u : Fin n → ℂ) :
    neutralIV007OriginalMixedEnergy a s u =
      neutralIV007OriginalMixedEnergy b s u := by
  unfold neutralIV007OriginalMixedEnergy
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  rw [neutralIV007OriginalMixedEntry_natural a b hab s hs i j]

/-- The real part of the exact finite complex energy is
window-independent for a fixed supported family. -/
theorem neutralIV007OriginalMixedEnergy_re_natural
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (u : Fin n → ℂ) :
    (neutralIV007OriginalMixedEnergy a s u).re =
      (neutralIV007OriginalMixedEnergy b s u).re := by
  exact congrArg Complex.re
    (neutralIV007OriginalMixedEnergy_natural a b hab s hs u)

/-- For one fixed finite support family, real-quadratic nonnegativity
for EVERY complex coefficient vector is equivalent in both windows.
This does not extend the allowed test-family support. -/
theorem neutralIV007FixedFamilyRealNonnegative_iff
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) :
    (∀ u : Fin n → ℂ,
        0 ≤ (neutralIV007OriginalMixedEnergy a s u).re) ↔
      (∀ u : Fin n → ℂ,
        0 ≤ (neutralIV007OriginalMixedEnergy b s u).re) := by
  constructor
  · intro h u
    rw [← neutralIV007OriginalMixedEnergy_re_natural a b hab s hs u]
    exact h u
  · intro h u
    rw [neutralIV007OriginalMixedEnergy_re_natural a b hab s hs u]
    exact h u

/-- The actual source-specific all-finite-family real-quadratic
nonnegativity OBLIGATION at a window radius. This is a proposition
to be investigated, not an axiom and not a theorem of positivity. -/
def neutralIV007UniversalRealNonnegative (a : ℝ) : Prop :=
  ∀ (n : ℕ) (s : Fin n → 𝓢(ℝ, ℂ)),
    (∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) →
    ∀ u : Fin n → ℂ,
      0 ≤ (neutralIV007OriginalMixedEnergy a s u).re

/-- Exact one-way support-class inclusion:
if EVERY family supported in the larger window is nonnegative,
then EVERY family supported in the smaller one is nonnegative.
The reverse implication cannot be obtained by IV006 naturality alone. -/
theorem neutralIV007UniversalRealNonnegative_antitone
    (a b : ℝ) (hab : a ≤ b)
    (hb : neutralIV007UniversalRealNonnegative b) :
    neutralIV007UniversalRealNonnegative a := by
  intro n s hs u
  have hsb : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-b) b → s i x = 0 := by
    intro i
    exact neutralIV006Schwartz_support_expand a b hab (s i) (hs i)
  have h : 0 ≤ (neutralIV007OriginalMixedEnergy b s u).re :=
    hb n s hsb u
  rw [← neutralIV007OriginalMixedEnergy_re_natural a b hab s hs u] at h
  exact h

#print axioms neutralIV006LiteralMixedEF_natural
#print axioms neutralIV006MixedDivisorSum_eq_of_support
#print axioms neutralIV006Schwartz_support_expand
#print axioms neutralIV007OriginalMixedEntry_natural
#print axioms neutralIV007OriginalDivisorEntry_natural
#print axioms neutralIV007OriginalMixedMatrix_natural
#print axioms neutralIV007OriginalMixedEnergy_natural
#print axioms neutralIV007OriginalMixedEnergy_re_natural
#print axioms neutralIV007FixedFamilyRealNonnegative_iff
#print axioms neutralIV007UniversalRealNonnegative_antitone

end
end WeilDefect
