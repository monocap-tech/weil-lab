import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP004 SOURCE-BRIDGE CANDIDATE ON AN **IV022-DERIVED COMPANION BRANCH**.
This is deliberately NOT part of the CP003/CP004 independent documentation
branch, whose base main does not yet include the unmerged Phase IV source modules.

This file attaches three elementary, CONDITIONAL algebraic bridge lemmas to
the LITERAL original mixed signed Weil correlation and von Mangoldt sum.
It neither constructs the exact CP001 compact bump family nor proves any
of its specific finite real log-gap hypotheses; those are OPEN subsequent
source obligations. No RH, positive prime oracle, or sorry is introduced.

Kernel acceptance requires successful lake build + strict source-bounded
#print axioms; merely committing these candidates is NOT a Lean PASS.
-/

/-- The actual original physical two-input correlation has precisely
the t(x)*conj(s(x-tau)) orientation used in CP002–CP004. -/
theorem neutralCP004OriginalCorrelationIntegral
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0)
    (τ : ℝ) :
    neutralWindowCorrelation (11/10:ℝ)
      (s.toLp 2 volume) (t.toLp 2 volume) τ =
      ∫ x : ℝ, t x * conj (s (x - τ)) := by
  exact neutralIV011MixedCorrelation_eq_schwartzIntegral
    (11/10:ℝ) (11/10:ℝ) (le_refl _)
    s t hs ht τ

/-- One unchanged literal source summand; NO new arithmetic oracle. -/
def neutralCP004OriginalPrimeSummand
    (s t : 𝓢(ℝ, ℂ)) (n : ℕ) : ℂ :=
    ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
      (neutralWindowCorrelation (11/10:ℝ)
        (s.toLp 2 volume) (t.toLp 2 volume) (Real.log n) +
       neutralWindowCorrelation (11/10:ℝ)
        (s.toLp 2 volume) (t.toLp 2 volume) (-Real.log n))

/-- Actual ORIGINAL mixed von Mangoldt prime expression reduces
to its authentic finite first ten summands under the explicitly shown
log10 cutoff hypothesis. This is a generic source bridge, not proof
that the CP001 frozen bumps satisfy all their separate log gaps. -/
theorem neutralCP004OriginalPrimeFiniteTen
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0)
    (hcut : ∀ n : ℕ, 10 ≤ n → (11/5:ℝ) < Real.log n) :
    neutralIV011OriginalMixedPrime (11/10:ℝ) s t =
      ∑ n ∈ Finset.range 10,
        neutralCP004OriginalPrimeSummand s t n := by
  have hcut' (n : ℕ) (hn : 10 ≤ n) :
      (11/10:ℝ) + (11/10:ℝ) < Real.log n := by
    have h := hcut n hn
    convert h using 1 <;> norm_num
  simpa [neutralCP004OriginalPrimeSummand] using
    (neutralIV011OriginalMixedPrime_eq_finite
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      s t hs ht 10 hcut')

/-- When all OTHER actual finite ORIGINAL summands vanish,
the real surviving n=9 contribution is retained exactly,
including both signs and the genuine Λ(9)/sqrt(9) coefficient.
The assumptions are explicit; no frozen-bump overlap table is
silently introduced. -/
theorem neutralCP004OriginalPrimeSingleN9_of_otherTermsZero
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0)
    (hcut : ∀ n : ℕ, 10 ≤ n → (11/5:ℝ) < Real.log n)
    (hother : ∀ n ∈ Finset.range 10, n ≠ 9 →
      neutralCP004OriginalPrimeSummand s t n = 0) :
    neutralIV011OriginalMixedPrime (11/10:ℝ) s t =
      neutralCP004OriginalPrimeSummand s t 9 := by
  rw [neutralCP004OriginalPrimeFiniteTen s t hs ht hcut]
  apply Finset.sum_eq_single 9
  · intro n hn hne
    exact hother n hn hne
  · intro hnot
    exact False.elim (hnot (by norm_num))

/-- True original prime-zero conclusion for a mixed pair
whose finite SOURCE summands all vanish, rather than
assuming a false universal positivity or prime-free property. -/
theorem neutralCP004OriginalPrimeZero_of_allTermsZero
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0)
    (hcut : ∀ n : ℕ, 10 ≤ n → (11/5:ℝ) < Real.log n)
    (hall : ∀ n ∈ Finset.range 10,
      neutralCP004OriginalPrimeSummand s t n = 0) :
    neutralIV011OriginalMixedPrime (11/10:ℝ) s t = 0 := by
  rw [neutralCP004OriginalPrimeFiniteTen s t hs ht hcut]
  apply Finset.sum_eq_zero
  intro n hn
  exact hall n hn

#print axioms neutralIV011MixedCorrelation_eq_schwartzIntegral
#print axioms neutralIV011OriginalMixedPrime_eq_finite
#print axioms neutralCP004OriginalCorrelationIntegral
#print axioms neutralCP004OriginalPrimeFiniteTen
#print axioms neutralCP004OriginalPrimeSingleN9_of_otherTermsZero
#print axioms neutralCP004OriginalPrimeZero_of_allTermsZero

end
end WeilDefect
