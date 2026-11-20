import WeilDefect.Arithmetic.ActualZetaPhaseIVFiniteMixedWindowSystem
import WeilDefect.Arithmetic.ActualZetaWeilZeroForm
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
IV008 — Original signed mixed Weil Hermitian attachment for arbitrary
compactly supported COMPLEX Schwartz families.

Unlike an abstract PSD matrix, the entries below are literally the
two-argument Zeta23.EF.literatureRHS on the ORIGINAL
neutralWindowCorrelation; the actual complete-multiplicity zero-side
is attached using NF533/NF534 and the IV006 window representative.

The genuine zeta divisor involution conjugates the frequencies,
and therefore yields Hermitian symmetry, without any positivity claim
and without RH or real/odd test assumptions.

The resulting original finite complex quadratic energy is REAL.
It need NOT be nonnegative. Its equality with the diagonal Weil
functional applied to a physical Schwartz linear combination is the
SEPARATE, still-unproved sesquilinear/polarization attachment.
-/

/-- Any complex Schwartz function supported pointwise in the actual
closed physical window has compact support, supplying the required
explicit-formula regularity input. -/
theorem neutralIV008SchwartzWindow_hasCompactSupport
    (a : ℝ) (s : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    HasCompactSupport (fun x : ℝ => s x) := by
  apply HasCompactSupport.intro (K := Set.Icc (-a) a) isCompact_Icc
  intro x hx
  exact hs x hx

/-- This is the EXACT ORIGINAL full-divisor mixed zeta EF, for every
pair from an arbitrary finite family of complex Schwartz tests
supported within the same actual physical window. The first argument
is the conjugate-frequency partner. No synthetic arithmetic oracle. -/
theorem neutralIV008OriginalMixedEntry_eq_divisor
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin n) :
    neutralIV007OriginalDivisorEntry a s i j =
      neutralIV007OriginalMixedEntry a s i j := by
  unfold neutralIV007OriginalDivisorEntry neutralIV007OriginalMixedEntry
  exact neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond
    a ((s i).toLp 2 volume) ((s j).toLp 2 volume)
    (fun x : ℝ => (s j) x)
    ((s j).smooth 2)
    (neutralIV008SchwartzWindow_hasCompactSupport a (s j) (hs j))
    (neutralIV006Schwartz_window_ae a (s j) (hs j))

/-- Original full-divisor mixed series are Hermitian by the genuine
analytic divisor partner involution, for all complex Schwartz families.
No real/odd or positivity hypothesis is needed; the source's full
multiplicity-copy indexing is unchanged. -/
theorem neutralIV008OriginalDivisorEntry_hermitian
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (i j : Fin n) :
    conj (neutralIV007OriginalDivisorEntry a s i j) =
      neutralIV007OriginalDivisorEntry a s j i := by
  unfold neutralIV007OriginalDivisorEntry
  rw [Complex.conj_tsum]
  rw [← neutralActualZetaDivisorPairEquiv.tsum_eq
    (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q))
        ((s j).toLp 2 volume)) *
      neutralWindowEvaluation a
        (neutralActualZetaDivisorOrdinate q)
        ((s i).toLp 2 volume))]
  apply tsum_congr
  intro q
  change conj (conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate q))
      ((s i).toLp 2 volume)) *
    neutralWindowEvaluation a
      (neutralActualZetaDivisorOrdinate q)
      ((s j).toLp 2 volume)) =
    conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate
        (neutralActualZetaDivisorPair q)))
      ((s j).toLp 2 volume)) *
    neutralWindowEvaluation a
      (neutralActualZetaDivisorOrdinate
        (neutralActualZetaDivisorPair q))
      ((s i).toLp 2 volume)
  rw [neutralActualZetaDivisorOrdinate_pair]
  simp only [map_mul, starRingEnd_apply, star_star]
  exact mul_comm _ _

/-- The ACTUAL arithmetic two-input Weil mixed entries are Hermitian
on any compactly supported complex Schwartz family, by literal NF533
explicit-formula attachment and exact full-divisor conjugation. -/
theorem neutralIV008OriginalMixedEntry_hermitian
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin n) :
    conj (neutralIV007OriginalMixedEntry a s i j) =
      neutralIV007OriginalMixedEntry a s j i := by
  have hij := neutralIV008OriginalMixedEntry_eq_divisor a s hs i j
  have hji := neutralIV008OriginalMixedEntry_eq_divisor a s hs j i
  calc
    conj (neutralIV007OriginalMixedEntry a s i j) =
        conj (neutralIV007OriginalDivisorEntry a s i j) :=
      congrArg conj hij.symm
    _ = neutralIV007OriginalDivisorEntry a s j i :=
      neutralIV008OriginalDivisorEntry_hermitian a s i j
    _ = neutralIV007OriginalMixedEntry a s j i := hji

/-- Original signed Weil diagonal entries are real, not necessarily
nonnegative. This is a theorem about the authentic literature RHS. -/
theorem neutralIV008OriginalMixedDiagonal_im_zero
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i : Fin n) :
    (neutralIV007OriginalMixedEntry a s i i).im = 0 := by
  have h := congrArg Complex.im
    (neutralIV008OriginalMixedEntry_hermitian a s hs i i)
  simp only [Complex.conj_im] at h
  linarith

/-- A full finite complex coefficient energy built from the authentic
Hermitian arithmetic Weil EF has real value, despite its arbitrary
complex test functions and coefficient vector. This theorem does NOT
assert that the real number is positive. -/
theorem neutralIV008OriginalMixedEnergy_im_zero
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (u : Fin n → ℂ) :
    (neutralIV007OriginalMixedEnergy a s u).im = 0 := by
  have hc : conj (neutralIV007OriginalMixedEnergy a s u) =
      neutralIV007OriginalMixedEnergy a s u := by
    unfold neutralIV007OriginalMixedEnergy
    simp only [map_sum, map_mul, starRingEnd_apply, star_star]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    have hji := neutralIV008OriginalMixedEntry_hermitian a s hs j i
    change u j * conj (neutralIV007OriginalMixedEntry a s j i) * conj (u i) =
      conj (u i) * neutralIV007OriginalMixedEntry a s i j * u j
    rw [hji]
    ring
  have h := congrArg Complex.im hc
  simp only [Complex.conj_im] at h
  linarith

/-- Canonical real-axis identification of the genuine signed mixed
quadratic energy; no claim that this real number is nonnegative. -/
theorem neutralIV008OriginalMixedEnergy_eq_re
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (u : Fin n → ℂ) :
    neutralIV007OriginalMixedEnergy a s u =
      ((neutralIV007OriginalMixedEnergy a s u).re : ℂ) := by
  apply Complex.ext
  · simp
  · simp [neutralIV008OriginalMixedEnergy_im_zero a s hs u]

#print axioms neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond
#print axioms neutralActualZetaDivisorPairEquiv
#print axioms neutralIV007OriginalMixedEntry_natural
#print axioms neutralIV008SchwartzWindow_hasCompactSupport
#print axioms neutralIV008OriginalMixedEntry_eq_divisor
#print axioms neutralIV008OriginalDivisorEntry_hermitian
#print axioms neutralIV008OriginalMixedEntry_hermitian
#print axioms neutralIV008OriginalMixedDiagonal_im_zero
#print axioms neutralIV008OriginalMixedEnergy_im_zero
#print axioms neutralIV008OriginalMixedEnergy_eq_re

end
end WeilDefect
