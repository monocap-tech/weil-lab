import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV014 — Original PRIME-ACTIVE mixed Weil support geometry.

IV013 imposed translated disjointness at EVERY integer 0≤n<N.
The literal zeta prime series contains the authentic factor
ArithmeticFunction.vonMangoldt n, and only terms where this
coefficient is NONZERO can contribute. IV014 therefore restricts
the geometrical separation condition to the genuine arithmetic
active indices. No primality test or fabricated prime oracle is
introduced: the full original Λ(n)/√n remains in every source sum.

Theorems below are source-specific Lean CANDIDATES requiring direct
kernel/standard-axiom verification. No nonzero new-support test,
new-support diagonal sign, new mixed Schur estimate or RH is proved.
-/

/-- A strictly WEAKER finite prime-translation separation condition
than IV013: only the original nonzero von-Mangoldt coefficients matter.
In particular, n with Λ(n)=0 imposes NO physical disjointness test. -/
def neutralIV014ActivePrimeSeparated
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ) : Prop :=
  ∀ n : ℕ, n ∈ Finset.range N →
    ArithmeticFunction.vonMangoldt n ≠ 0 →
    ∀ x : ℝ, t x = 0 ∨
      (s (x - Real.log n) = 0 ∧ s (x + Real.log n) = 0)

/-- The earlier all-integer IV013 criterion implies the new genuine
von-Mangoldt-active condition, without any extra source assumption. -/
theorem neutralIV014ActiveSeparated_of_strong
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ)
    (hstrong : neutralIV013OriginalPrimeSeparated s t N) :
    neutralIV014ActivePrimeSeparated s t N := by
  intro n hn _ x
  exact hstrong n hn x

/-- The genuine complex mixed physical correlation vanishes at both
original ±log n frequencies whenever Λ(n)≠0 and the two Schwartz
tests avoid that *active* translated source overlap. -/
theorem neutralIV014ActiveCorrelation_vanish
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hsep : neutralIV014ActivePrimeSeparated s t N)
    (n : ℕ) (hn : n ∈ Finset.range N)
    (hactive : ArithmeticFunction.vonMangoldt n ≠ 0) :
    neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
        (Real.log n) = 0 ∧
      neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
        (-Real.log n) = 0 := by
  constructor
  · rw [neutralIV011MixedCorrelation_eq_schwartzIntegral a b hab s t hs ht]
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    rcases hsep n hn hactive x with htx | ⟨hsx, _⟩
    · simp [htx]
    · simp [hsx]
  · rw [neutralIV011MixedCorrelation_eq_schwartzIntegral a b hab s t hs ht]
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    rcases hsep n hn hactive x with htx | ⟨_, hsx⟩
    · simp [htx]
    · simp [sub_neg_eq_add, hsx]

/-- The actual nonnegative translated-overlap cost is zero at both
active original prime frequencies under IV014 source separation.
This is stronger than merely observing cancellation in an integral. -/
theorem neutralIV014ActivePhysicalOverlap_zero
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ)
    (hsep : neutralIV014ActivePrimeSeparated s t N)
    (n : ℕ) (hn : n ∈ Finset.range N)
    (hactive : ArithmeticFunction.vonMangoldt n ≠ 0) :
    neutralIV012PhysicalOverlapCost s t (Real.log n) = 0 ∧
      neutralIV012PhysicalOverlapCost s t (-Real.log n) = 0 := by
  constructor
  · unfold neutralIV012PhysicalOverlapCost
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    rcases hsep n hn hactive x with htx | ⟨hsx, _⟩
    · simp [htx]
    · simp [hsx]
  · unfold neutralIV012PhysicalOverlapCost
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    rcases hsep n hn hactive x with htx | ⟨_, hsx⟩
    · simp [htx]
    · simp [sub_neg_eq_add, hsx]

/-- Unlike IV013's all-integer condition, the ACTUAL finite
nonnegative prime-envelope budget vanishes under the strictly
arithmetic-active condition. Inactive terms contribute zero by
their authentic Λ(n) factor, irrespective of physical overlap. -/
theorem neutralIV014ActiveFinitePrimeBudget_zero
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ)
    (hsep : neutralIV014ActivePrimeSeparated s t N) :
    neutralIV012OriginalFinitePrimeOverlapBudget s t N = 0 := by
  unfold neutralIV012OriginalFinitePrimeOverlapBudget
  apply Finset.sum_eq_zero
  intro n hn
  by_cases hz : ArithmeticFunction.vonMangoldt n = 0
  · simp [hz]
  · obtain ⟨hp, hm⟩ :=
      neutralIV014ActivePhysicalOverlap_zero s t N hsep n hn hz
    simp [hp, hm]

/-- The ORIGINAL full von-Mangoldt mixed prime contribution vanishes
exactly, with all prime powers and both signs retained, under the
weaker arithmetic-active translated-support separation criterion. -/
theorem neutralIV014ActiveMixedPrime_zero
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (hsep : neutralIV014ActivePrimeSeparated s t N) :
    neutralIV011OriginalMixedPrime b s t = 0 := by
  rw [neutralIV011OriginalMixedPrime_eq_finite a b hab s t hs ht N hN]
  apply Finset.sum_eq_zero
  intro n hn
  by_cases hz : ArithmeticFunction.vonMangoldt n = 0
  · simp [hz]
  · obtain ⟨hp, hm⟩ :=
      neutralIV014ActiveCorrelation_vanish a b hab s t hs ht N hsep n hn hz
    simp [hp, hm]

/-- Arithmetic-active separation reduces the literal mixed zeta
explicit formula to its UNCHANGED genuine two poles plus Gamma
integral, without assuming that this remainder is positive. -/
theorem neutralIV014ActiveMixed_eq_analytic
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (hsep : neutralIV014ActivePrimeSeparated s t N) :
    neutralIV010Mixed b s t =
      neutralIV013OriginalMixedAnalyticRemainder b s t := by
  rw [neutralIV013OriginalMixed_eq_analytic_sub_prime,
    neutralIV014ActiveMixedPrime_zero a b hab s t hs ht N hN hsep]
  ring

/-- CHECKABLE FINITE INTERVAL GEOMETRY: if the two physical test
intervals have center difference avoiding both signed original
log-prime shifts by more than the sum of their radii, all nonzero
von-Mangoldt interactions vanish pointwise. The test uses literal
support inclusions and all genuine n<N with Λ(n)≠0. -/
theorem neutralIV014ActiveSeparated_of_intervalGap
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ)
    (cs ct rs rt : ℝ)
    (hs : ∀ x : ℝ, x ∉ Set.Icc (cs - rs) (cs + rs) → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (ct - rt) (ct + rt) → t x = 0)
    (hgap : ∀ n : ℕ, n ∈ Finset.range N →
      ArithmeticFunction.vonMangoldt n ≠ 0 →
      rs + rt < |ct - cs - Real.log n| ∧
      rs + rt < |ct - cs + Real.log n|) :
    neutralIV014ActivePrimeSeparated s t N := by
  intro n hn hactive x
  by_cases hx : x ∈ Set.Icc (ct - rt) (ct + rt)
  · right
    constructor
    · apply hs
      intro hy
      have hbound : |ct - cs - Real.log n| ≤ rs + rt := by
        apply abs_le.mpr
        rcases hx with ⟨hxl, hxr⟩
        rcases hy with ⟨hyl, hyr⟩
        constructor <;> linarith
      exact (not_lt_of_ge hbound) (hgap n hn hactive).1
    · apply hs
      intro hy
      have hbound : |ct - cs + Real.log n| ≤ rs + rt := by
        apply abs_le.mpr
        rcases hx with ⟨hxl, hxr⟩
        rcases hy with ⟨hyl, hyr⟩
        constructor <;> linarith
      exact (not_lt_of_ge hbound) (hgap n hn hactive).2
  · left
    exact ht x hx

/-- The earlier IV012 triangle envelope loses its WHOLE finite
prime portion under the new active criterion, not just the signed
prime sum. This is an exact positive-budget identity. -/
theorem neutralIV014ActiveArithmeticBudget_eq_residual
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) (N : ℕ)
    (hsep : neutralIV014ActivePrimeSeparated s t N) :
    neutralIV012OriginalMixedArithmeticBudget b s t N =
      neutralIV012OriginalPoleMomentBudget b s t +
        neutralIV012OriginalGammaAbsoluteBudget b s t := by
  unfold neutralIV012OriginalMixedArithmeticBudget
  rw [neutralIV014ActiveFinitePrimeBudget_zero s t N hsep]
  ring

/-- A truly source-bound, PRIME-FREE mixed zeta Weil norm estimate:
the two genuine pole-moment products and unmodified Gamma integral
alone dominate the original signed arithmetic mixed value. -/
theorem neutralIV014ActiveMixed_norm_le_residualBudget
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (hsep : neutralIV014ActivePrimeSeparated s t N) :
    ‖neutralIV010Mixed b s t‖ ≤
      neutralIV012OriginalPoleMomentBudget b s t +
        neutralIV012OriginalGammaAbsoluteBudget b s t := by
  rw [neutralIV014ActiveMixed_eq_analytic a b hab s t hs ht N hN hsep]
  unfold neutralIV013OriginalMixedAnalyticRemainder
  calc
    ‖neutralIV011OriginalMixedPole b s t +
        neutralIV011OriginalMixedArch b s t‖ ≤
      ‖neutralIV011OriginalMixedPole b s t‖ +
        ‖neutralIV011OriginalMixedArch b s t‖ := norm_add_le _ _
    _ ≤ neutralIV012OriginalPoleMomentBudget b s t +
        neutralIV012OriginalGammaAbsoluteBudget b s t :=
      add_le_add
        (neutralIV012OriginalMixedPole_norm_le_momentBudget b s t)
        (neutralIV012OriginalMixedArch_norm_le_gammaBudget b s t)

/-- The original finite mixed family admits one extra physical
Schwartz source under a quantitatively stronger but genuinely
prime-free POLE+GAMMA residual-square bound. Both old/new diagonal
signs and the true residual estimate remain EXPLICIT hypotheses.
No new-support zeta positivity is asserted or fabricated. -/
theorem neutralIV014ActiveOneNew_nonnegative_of_residual
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ m : ℕ, N ≤ m → a + b < Real.log m)
    (hsep : neutralIV014ActivePrimeSeparated
      (neutralIV009PhysicalSchwartzSum s u) t N)
    (hOld : 0 ≤ (neutralIV007OriginalMixedEnergy a s u).re)
    (hNew : 0 ≤ (neutralIV010Diagonal b t).re)
    (hResidual :
      (neutralIV012OriginalPoleMomentBudget b
        (neutralIV009PhysicalSchwartzSum s u) t +
        neutralIV012OriginalGammaAbsoluteBudget b
          (neutralIV009PhysicalSchwartzSum s u) t)^2 ≤
          (neutralIV007OriginalMixedEnergy a s u).re *
            (neutralIV010Diagonal b t).re)
    (v : ℂ) :
    0 ≤ (neutralIV010Diagonal b
      (neutralIV009PhysicalSchwartzSum s u + v • t)).re := by
  have hS : ∀ x : ℝ, x ∉ Set.Icc (-a) a →
      neutralIV009PhysicalSchwartzSum s u x = 0 :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs
  let S := neutralIV009PhysicalSchwartzSum s u
  have hbound : ‖neutralIV010Mixed b S t‖ ≤
    neutralIV012OriginalPoleMomentBudget b S t +
      neutralIV012OriginalGammaAbsoluteBudget b S t :=
    neutralIV014ActiveMixed_norm_le_residualBudget
      a b hab S t hS ht N hN hsep
  have hn : 0 ≤ ‖neutralIV010Mixed b S t‖ := norm_nonneg _
  have hsq : ‖neutralIV010Mixed b S t‖^2 ≤
      (neutralIV012OriginalPoleMomentBudget b S t +
        neutralIV012OriginalGammaAbsoluteBudget b S t)^2 :=
    (sq_le_sq₀ hn
      (add_nonneg
        (neutralIV012OriginalPoleMomentBudget_nonnegative b S t)
        (neutralIV012OriginalGammaAbsoluteBudget_nonnegative b S t))).mpr hbound
  have he : (neutralIV010Mixed b S t).re^2 +
      (neutralIV010Mixed b S t).im^2 =
      ‖neutralIV010Mixed b S t‖^2 := by
    rw [Complex.sq_norm, Complex.normSq_apply]
    ring
  have hcross :
      (neutralIV010Mixed b S t).re^2 +
        (neutralIV010Mixed b S t).im^2 ≤
          (neutralIV007OriginalMixedEnergy a s u).re *
            (neutralIV010Diagonal b t).re := by
    calc
      _ = ‖neutralIV010Mixed b S t‖^2 := he
      _ ≤ (neutralIV012OriginalPoleMomentBudget b S t +
          neutralIV012OriginalGammaAbsoluteBudget b S t)^2 := hsq
      _ ≤ _ := hResidual
  exact neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
    a b hab s u hs t ht hOld hNew hcross v

#print axioms neutralIV011OriginalMixedPrime_eq_finite
#print axioms neutralIV013OriginalMixed_eq_analytic_sub_prime
#print axioms neutralIV012OriginalMixedArch_norm_le_gammaBudget
#print axioms neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
#print axioms neutralIV014ActiveSeparated_of_strong
#print axioms neutralIV014ActiveCorrelation_vanish
#print axioms neutralIV014ActivePhysicalOverlap_zero
#print axioms neutralIV014ActiveFinitePrimeBudget_zero
#print axioms neutralIV014ActiveMixedPrime_zero
#print axioms neutralIV014ActiveMixed_eq_analytic
#print axioms neutralIV014ActiveSeparated_of_intervalGap
#print axioms neutralIV014ActiveArithmeticBudget_eq_residual
#print axioms neutralIV014ActiveMixed_norm_le_residualBudget
#print axioms neutralIV014ActiveOneNew_nonnegative_of_residual

end
end WeilDefect
