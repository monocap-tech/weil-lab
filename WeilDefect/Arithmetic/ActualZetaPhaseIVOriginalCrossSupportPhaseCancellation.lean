import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV013: SOURCE-EXACT phase-sensitive cross-support arithmetic gate.

IV012's absolute prime/pole/Gamma envelope discards the complex phase
between the finite genuine mixed prime series and the unchanged
analytic remainder. This source keeps the sign and phase of the EXACT
original arithmetic explicit formula, separating the prime sum from
the combined actual two poles and original Gamma integral.

The cross-term interference identity is an exact equality in ℝ, not
a new zeta positivity hypothesis. The new geometric prime-free test
class is certified only under an explicit translated-overlap
separation condition, and does not assert general extended support
Weil positivity.

All statement/proof texts are Lean CANDIDATES pending actual kernel
verification and strict upstream source axiom audits.
-/

/-- Actual original arithmetic nonprime remainder, retaining BOTH
original pole residues and the unmodified complex Gamma/digamma term. -/
def neutralIV013OriginalMixedAnalyticRemainder
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) : ℂ :=
  neutralIV011OriginalMixedPole b s t +
    neutralIV011OriginalMixedArch b s t

/-- The genuine original mixed arithmetic Weil entry is analytic
remainder MINUS the full exact prime contribution. -/
theorem neutralIV013OriginalMixed_eq_analytic_sub_prime
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    neutralIV010Mixed b s t =
      neutralIV013OriginalMixedAnalyticRemainder b s t -
        neutralIV011OriginalMixedPrime b s t := by
  rw [neutralIV011OriginalMixed_arithmeticSplit]
  unfold neutralIV013OriginalMixedAnalyticRemainder
  ring

/-- Exact original finite-prime arithmetic interference identity:
the squared complex modulus of the true mixed Weil value differs from
the sum of the two separate squared budgets by a real phase-coupling
term. This identity retains the crucial subtraction of the original
prime side of Zeta23.EF.literatureRHS. -/
theorem neutralIV013OriginalMixed_phaseInterference
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    (neutralIV010Mixed b s t).re^2 +
      (neutralIV010Mixed b s t).im^2 =
      (neutralIV013OriginalMixedAnalyticRemainder b s t).re^2 +
      (neutralIV013OriginalMixedAnalyticRemainder b s t).im^2 +
      (neutralIV011OriginalMixedPrime b s t).re^2 +
      (neutralIV011OriginalMixedPrime b s t).im^2 -
      2 * ((neutralIV013OriginalMixedAnalyticRemainder b s t).re *
        (neutralIV011OriginalMixedPrime b s t).re +
        (neutralIV013OriginalMixedAnalyticRemainder b s t).im *
        (neutralIV011OriginalMixedPrime b s t).im) := by
  rw [neutralIV013OriginalMixed_eq_analytic_sub_prime]
  simp only [Complex.sub_re, Complex.sub_im]
  ring

/-- The EXACT original phase-sensitive criterion is equivalent to the
sharp source mixed Schur determinant bound. Unlike IV012's absolute
envelope, this criterion preserves cross-component cancellation. -/
theorem neutralIV013OriginalMixed_crossBound_iff_alignment
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) (A D : ℝ) :
    ((neutralIV010Mixed b s t).re^2 +
        (neutralIV010Mixed b s t).im^2 ≤ A * D) ↔
      ((neutralIV013OriginalMixedAnalyticRemainder b s t).re^2 +
        (neutralIV013OriginalMixedAnalyticRemainder b s t).im^2 +
        (neutralIV011OriginalMixedPrime b s t).re^2 +
        (neutralIV011OriginalMixedPrime b s t).im^2 ≤
          A * D +
          2 * ((neutralIV013OriginalMixedAnalyticRemainder b s t).re *
            (neutralIV011OriginalMixedPrime b s t).re +
            (neutralIV013OriginalMixedAnalyticRemainder b s t).im *
            (neutralIV011OriginalMixedPrime b s t).im)) := by
  rw [neutralIV013OriginalMixed_phaseInterference]
  constructor <;> intro h <;> linarith

/-- Strong geometric version of "new test is prime separated" for
the finite original arithmetic frequencies. The condition refers
only to actual two physical Schwartz function values, and does not
assume positivity of any Weil pairing. -/
def neutralIV013OriginalPrimeSeparated
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ) : Prop :=
  ∀ n : ℕ, n ∈ Finset.range N →
    ∀ x : ℝ, t x = 0 ∨
      (s (x - Real.log n) = 0 ∧ s (x + Real.log n) = 0)

/-- If all finitely many relevant genuine prime translates of the
old physical support avoid the new test, the two ORIGINAL complex
correlation samples at ±log n vanish identically. -/
theorem neutralIV013PrimeSeparated_correlationVanish
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hsep : neutralIV013OriginalPrimeSeparated s t N)
    (n : ℕ) (hn : n ∈ Finset.range N) :
    neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
        (Real.log n) = 0 ∧
      neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
        (-Real.log n) = 0 := by
  constructor
  · rw [neutralIV011MixedCorrelation_eq_schwartzIntegral a b hab s t hs ht]
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    rcases hsep n hn x with htx | ⟨hsx, _⟩
    · simp [htx]
    · simp [hsx]
  · rw [neutralIV011MixedCorrelation_eq_schwartzIntegral a b hab s t hs ht]
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    rcases hsep n hn x with htx | ⟨_, hsx⟩
    · simp [htx]
    · simpa only [sub_neg_eq_add, hsx, map_zero, mul_zero]

/-- Exact SOURCE-specific prime cancellation by geometric
nonoverlap at every actually relevant n<N. All genuine Λ(n)/√n
weights stay inside the finite formula before they vanish. -/
theorem neutralIV013PrimeSeparated_originalPrime_zero
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (hsep : neutralIV013OriginalPrimeSeparated s t N) :
    neutralIV011OriginalMixedPrime b s t = 0 := by
  rw [neutralIV011OriginalMixedPrime_eq_finite a b hab s t hs ht N hN]
  apply Finset.sum_eq_zero
  intro n hn
  obtain ⟨hp, hm⟩ :=
    neutralIV013PrimeSeparated_correlationVanish
      a b hab s t hs ht N hsep n hn
  simp [hp, hm]

/-- A genuinely new-support test meeting the prime-separation
criterion leaves EXACTLY the true original two-pole-plus-Gamma
remainder in the mixed arithmetic EF. No sign is asserted. -/
theorem neutralIV013PrimeSeparated_originalMixed_eq_analytic
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (hsep : neutralIV013OriginalPrimeSeparated s t N) :
    neutralIV010Mixed b s t =
      neutralIV013OriginalMixedAnalyticRemainder b s t := by
  rw [neutralIV013OriginalMixed_eq_analytic_sub_prime,
    neutralIV013PrimeSeparated_originalPrime_zero a b hab s t hs ht N hN hsep]
  ring

/-- Source-accurate finite-family one-new-support Schur extension
with a PHASE-AWARE arithmetic alignment hypothesis, not an absolute
prime/pole/Gamma triangle budget. The needed new-support analytic
inequality is explicit and does NOT follow automatically from the
original zeta explicit formula. -/
theorem neutralIV013OriginalOneNew_nonnegative_of_alignment
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (hOld : 0 ≤ (neutralIV007OriginalMixedEnergy a s u).re)
    (hNew : 0 ≤ (neutralIV010Diagonal b t).re)
    (hAlign :
      (neutralIV013OriginalMixedAnalyticRemainder b
        (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV013OriginalMixedAnalyticRemainder b
        (neutralIV009PhysicalSchwartzSum s u) t).im^2 +
      (neutralIV011OriginalMixedPrime b
        (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV011OriginalMixedPrime b
        (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
        (neutralIV007OriginalMixedEnergy a s u).re *
          (neutralIV010Diagonal b t).re +
        2 * ((neutralIV013OriginalMixedAnalyticRemainder b
          (neutralIV009PhysicalSchwartzSum s u) t).re *
          (neutralIV011OriginalMixedPrime b
            (neutralIV009PhysicalSchwartzSum s u) t).re +
          (neutralIV013OriginalMixedAnalyticRemainder b
            (neutralIV009PhysicalSchwartzSum s u) t).im *
          (neutralIV011OriginalMixedPrime b
            (neutralIV009PhysicalSchwartzSum s u) t).im))
    (v : ℂ) :
    0 ≤ (neutralIV010Diagonal b
      (neutralIV009PhysicalSchwartzSum s u + v • t)).re := by
  have hCross :=
    (neutralIV013OriginalMixed_crossBound_iff_alignment b
      (neutralIV009PhysicalSchwartzSum s u) t
      (neutralIV007OriginalMixedEnergy a s u).re
      (neutralIV010Diagonal b t).re).mpr hAlign
  exact neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
    a b hab s u hs t ht hOld hNew hCross v

/-- Exact converse: whenever the original finite-prime/analytic
interference is too weak to satisfy the sharp mixed determinant, a
strictly positive new diagonal produces the explicit REAL NEGATIVE
original Schwartz test of IV011. This is conditional evidence of what
a genuine expanded-support counterexample WOULD require, not an
assertion that one exists for the zeta pairing. -/
theorem neutralIV013OriginalOneNew_negative_of_alignmentFailure
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (hNew : 0 < (neutralIV010Diagonal b t).re)
    (hFail :
      (neutralIV007OriginalMixedEnergy a s u).re *
        (neutralIV010Diagonal b t).re +
        2 * ((neutralIV013OriginalMixedAnalyticRemainder b
          (neutralIV009PhysicalSchwartzSum s u) t).re *
          (neutralIV011OriginalMixedPrime b
            (neutralIV009PhysicalSchwartzSum s u) t).re +
          (neutralIV013OriginalMixedAnalyticRemainder b
            (neutralIV009PhysicalSchwartzSum s u) t).im *
          (neutralIV011OriginalMixedPrime b
            (neutralIV009PhysicalSchwartzSum s u) t).im) <
      (neutralIV013OriginalMixedAnalyticRemainder b
        (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV013OriginalMixedAnalyticRemainder b
        (neutralIV009PhysicalSchwartzSum s u) t).im^2 +
      (neutralIV011OriginalMixedPrime b
        (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV011OriginalMixedPrime b
        (neutralIV009PhysicalSchwartzSum s u) t).im^2) :
    (neutralIV010Diagonal b
      (neutralIV009PhysicalSchwartzSum s u +
        (neutralIV011SchurMinimizer
          (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t)
          (neutralIV010Diagonal b t).re) • t)).re < 0 := by
  have h := neutralIV013OriginalMixed_phaseInterference b
    (neutralIV009PhysicalSchwartzSum s u) t
  have hSchur :
      (neutralIV007OriginalMixedEnergy a s u).re *
          (neutralIV010Diagonal b t).re <
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
        (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).im^2 := by
    linarith
  exact neutralIV011OriginalCrossFailure_negativeWitness
    a b hab s u hs t ht hNew hSchur

/-- In the original PRIME-FREE geometric class, the genuine
cross-support mixed Schur criterion reduces to the exact analytic
pole-plus-Gamma remainder, rather than the coarse absolute envelope.
The new diagonal and the remainder-vs-old-energy bound remain real
analytic premises, so this does not prove enlarged-support positivity.
-/
theorem neutralIV013PrimeSeparated_oneNew_nonnegative_of_analyticBound
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (hsep : neutralIV013OriginalPrimeSeparated
      (neutralIV009PhysicalSchwartzSum s u) t N)
    (hOld : 0 ≤ (neutralIV007OriginalMixedEnergy a s u).re)
    (hNew : 0 ≤ (neutralIV010Diagonal b t).re)
    (hResidual :
      (neutralIV013OriginalMixedAnalyticRemainder b
        (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV013OriginalMixedAnalyticRemainder b
        (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
        (neutralIV007OriginalMixedEnergy a s u).re *
          (neutralIV010Diagonal b t).re)
    (v : ℂ) :
    0 ≤ (neutralIV010Diagonal b
      (neutralIV009PhysicalSchwartzSum s u + v • t)).re := by
  have hS : ∀ x : ℝ, x ∉ Set.Icc (-a) a →
      neutralIV009PhysicalSchwartzSum s u x = 0 :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs
  have hfree := neutralIV013PrimeSeparated_originalMixed_eq_analytic
    a b hab (neutralIV009PhysicalSchwartzSum s u) t hS ht N hN hsep
  have hcross :
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
        (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
          (neutralIV007OriginalMixedEnergy a s u).re *
            (neutralIV010Diagonal b t).re := by
    rw [hfree]
    exact hResidual
  exact neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
    a b hab s u hs t ht hOld hNew hcross v

#print axioms neutralIV011OriginalMixed_finitePrimeArithmetic
#print axioms neutralIV011OriginalCrossFailure_negativeWitness
#print axioms neutralIV012OriginalMixed_norm_le_arithmeticBudget
#print axioms neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
#print axioms neutralIV013OriginalMixed_eq_analytic_sub_prime
#print axioms neutralIV013OriginalMixed_phaseInterference
#print axioms neutralIV013OriginalMixed_crossBound_iff_alignment
#print axioms neutralIV013PrimeSeparated_correlationVanish
#print axioms neutralIV013PrimeSeparated_originalPrime_zero
#print axioms neutralIV013PrimeSeparated_originalMixed_eq_analytic
#print axioms neutralIV013OriginalOneNew_nonnegative_of_alignment
#print axioms neutralIV013OriginalOneNew_negative_of_alignmentFailure
#print axioms neutralIV013PrimeSeparated_oneNew_nonnegative_of_analyticBound

end
end WeilDefect
