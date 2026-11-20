import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff
import WeilDefect.Arithmetic.ActualZetaCorrelationPoles
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV012: genuine original cross-support quantitative arithmetic ledger.

The old/new physical Schwartz correlation is the actual IV011
translated-product integral. We bound its finite prime contribution
by a completely explicit *nonnegative physical overlap* cost, retain
the genuine opposite source-window pole moments, and dominate the
unchanged original Gamma bracket by its absolute Fourier integral.

This is a rigorous proposed source-specific SUFFICIENT envelope for the
IV010 cross-support determinant inequality, NOT a proof that the
envelope is small enough or that the new diagonal is positive.

There are no new axioms, oracle estimates, RH assumptions or artificial
EF replacements. All upstream modules require independent kernel PASS.
-/

/-- Explicit nonnegative physical translated-overlap cost for genuine
arbitrary complex Schwartz tests; cancellation is discarded only for
this estimate, not in the definition of the original zeta pairing. -/
def neutralIV012PhysicalOverlapCost
    (s t : 𝓢(ℝ, ℂ)) (τ : ℝ) : ℝ :=
  ∫ x : ℝ, ‖t x‖ * ‖s (x - τ)‖

theorem neutralIV012PhysicalOverlapCost_nonnegative
    (s t : 𝓢(ℝ, ℂ)) (τ : ℝ) :
    0 ≤ neutralIV012PhysicalOverlapCost s t τ := by
  unfold neutralIV012PhysicalOverlapCost
  exact integral_nonneg (fun x => mul_nonneg (norm_nonneg _) (norm_nonneg _))

/-- Actual source-bound mixed correlation estimate from the
original translated product; no abstract PSD inequality is invoked.
It uses the unchanged complex conjugation and real physical shift. -/
theorem neutralIV012MixedCorrelation_norm_le_overlap
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (τ : ℝ) :
    ‖neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume) τ‖ ≤
      neutralIV012PhysicalOverlapCost s t τ := by
  rw [neutralIV011MixedCorrelation_eq_schwartzIntegral a b hab s t hs ht τ]
  unfold neutralIV012PhysicalOverlapCost
  calc
    ‖∫ x : ℝ, t x * conj (s (x-τ))‖ ≤
        ∫ x : ℝ, ‖t x * conj (s (x-τ))‖ :=
      norm_integral_le_integral_norm _
    _ = ∫ x : ℝ, ‖t x‖ * ‖s (x-τ)‖ := by
      simp only [norm_mul, Complex.norm_conj]

/-- The actual original finite mixed von-Mangoldt prime envelope.
The only discarded information is cancellation in the two physical
translated overlap integrals, which are positive by construction. -/
def neutralIV012OriginalFinitePrimeOverlapBudget
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.range N,
    (ArithmeticFunction.vonMangoldt n / Real.sqrt n) *
      (neutralIV012PhysicalOverlapCost s t (Real.log n) +
        neutralIV012PhysicalOverlapCost s t (-Real.log n))

theorem neutralIV012OriginalPrimeOverlapBudget_nonnegative
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ) :
    0 ≤ neutralIV012OriginalFinitePrimeOverlapBudget s t N := by
  unfold neutralIV012OriginalFinitePrimeOverlapBudget
  apply Finset.sum_nonneg
  intro n hn
  exact mul_nonneg
    (div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _))
    (add_nonneg (neutralIV012PhysicalOverlapCost_nonnegative s t _)
      (neutralIV012PhysicalOverlapCost_nonnegative s t _))

/-- Concrete unconditional norm bound for the EXACT finite original
mixed prime sum, with all genuine source Λ(n)/√n weights retained.
No new arithmetic sign hypothesis is introduced. -/
theorem neutralIV012OriginalMixedPrime_norm_le_overlapBudget
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n) :
    ‖neutralIV011OriginalMixedPrime b s t‖ ≤
      neutralIV012OriginalFinitePrimeOverlapBudget s t N := by
  rw [neutralIV011OriginalMixedPrime_eq_finite a b hab s t hs ht N hN]
  unfold neutralIV012OriginalFinitePrimeOverlapBudget
  calc
    ‖∑ n ∈ Finset.range N,
      ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
        (neutralWindowCorrelation b (s.toLp 2 volume)
            (t.toLp 2 volume) (Real.log n) +
          neutralWindowCorrelation b (s.toLp 2 volume)
            (t.toLp 2 volume) (-Real.log n))‖ ≤
      ∑ n ∈ Finset.range N,
        ‖((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
          (neutralWindowCorrelation b (s.toLp 2 volume)
            (t.toLp 2 volume) (Real.log n) +
            neutralWindowCorrelation b (s.toLp 2 volume)
              (t.toLp 2 volume) (-Real.log n))‖ :=
        norm_sum_le _ _
    _ ≤ ∑ n ∈ Finset.range N,
      (ArithmeticFunction.vonMangoldt n / Real.sqrt n) *
        (neutralIV012PhysicalOverlapCost s t (Real.log n) +
          neutralIV012PhysicalOverlapCost s t (-Real.log n)) := by
        apply Finset.sum_le_sum
        intro n hn
        have hw : 0 ≤ ArithmeticFunction.vonMangoldt n / Real.sqrt n :=
          div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _)
        rw [norm_mul, Complex.norm_real, Real.norm_eq_abs,
          abs_of_nonneg hw]
        apply mul_le_mul_of_nonneg_left _ hw
        calc
          ‖neutralWindowCorrelation b (s.toLp 2 volume)
              (t.toLp 2 volume) (Real.log n) +
            neutralWindowCorrelation b (s.toLp 2 volume)
              (t.toLp 2 volume) (-Real.log n)‖ ≤
            ‖neutralWindowCorrelation b (s.toLp 2 volume)
              (t.toLp 2 volume) (Real.log n)‖ +
            ‖neutralWindowCorrelation b (s.toLp 2 volume)
              (t.toLp 2 volume) (-Real.log n)‖ := norm_add_le _ _
          _ ≤ neutralIV012PhysicalOverlapCost s t (Real.log n) +
            neutralIV012PhysicalOverlapCost s t (-Real.log n) :=
              add_le_add
                (neutralIV012MixedCorrelation_norm_le_overlap
                  a b hab s t hs ht (Real.log n))
                (neutralIV012MixedCorrelation_norm_le_overlap
                  a b hab s t hs ht (-Real.log n))

/-- Genuine original two-pole cross moment budget; the first slot
and second slot retain their opposite ±1/2 window moments. -/
def neutralIV012OriginalPoleMomentBudget
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) : ℝ :=
  ‖sourceWindowMoment b (-(1/2)) (s.toLp 2 volume)‖ *
      ‖sourceWindowMoment b (1/2) (t.toLp 2 volume)‖ +
    ‖sourceWindowMoment b (1/2) (s.toLp 2 volume)‖ *
      ‖sourceWindowMoment b (-(1/2)) (t.toLp 2 volume)‖

theorem neutralIV012OriginalPoleMomentBudget_nonnegative
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    0 ≤ neutralIV012OriginalPoleMomentBudget b s t := by
  unfold neutralIV012OriginalPoleMomentBudget
  positivity

/-- Exact original arithmetic mixed pole dictionary, retaining both
distinct original exponential physical source moments. -/
theorem neutralIV012OriginalMixedPole_eq_sourceMoments
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    neutralIV011OriginalMixedPole b s t =
      conj (sourceWindowMoment b (-(1/2)) (s.toLp 2 volume)) *
        sourceWindowMoment b (1/2) (t.toLp 2 volume) +
      conj (sourceWindowMoment b (1/2) (s.toLp 2 volume)) *
        sourceWindowMoment b (-(1/2)) (t.toLp 2 volume) := by
  unfold neutralIV011OriginalMixedPole
  simp only [← neutralRawTransform_eq_paperFT]
  rw [show Complex.I / 2 = Complex.I * ((1/2:ℝ):ℂ) by push_cast; ring,
    show -Complex.I / 2 = Complex.I * ((-(1/2):ℝ):ℂ) by push_cast; ring]
  exact neutralWindowCorrelation_poleCrossTerms b _ _

/-- Actual original pole contribution is bounded by the sum of the
two correct physical source-moment products. -/
theorem neutralIV012OriginalMixedPole_norm_le_momentBudget
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    ‖neutralIV011OriginalMixedPole b s t‖ ≤
      neutralIV012OriginalPoleMomentBudget b s t := by
  rw [neutralIV012OriginalMixedPole_eq_sourceMoments]
  calc
    ‖conj (sourceWindowMoment b (-(1/2)) (s.toLp 2 volume)) *
        sourceWindowMoment b (1/2) (t.toLp 2 volume) +
      conj (sourceWindowMoment b (1/2) (s.toLp 2 volume)) *
        sourceWindowMoment b (-(1/2)) (t.toLp 2 volume)‖ ≤
      ‖conj (sourceWindowMoment b (-(1/2)) (s.toLp 2 volume)) *
        sourceWindowMoment b (1/2) (t.toLp 2 volume)‖ +
      ‖conj (sourceWindowMoment b (1/2) (s.toLp 2 volume)) *
        sourceWindowMoment b (-(1/2)) (t.toLp 2 volume)‖ :=
        norm_add_le _ _
    _ = neutralIV012OriginalPoleMomentBudget b s t := by
      simp only [neutralIV012OriginalPoleMomentBudget, norm_mul,
        Complex.norm_conj]

/-- The remaining original Gamma/digamma arithmetic contribution,
reexpressed as its nonnegative absolute real-frequency integral.
Unlike the prime cutoff it is still an INFINITE analytic integral. -/
def neutralIV012OriginalGammaAbsoluteBudget
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) : ℝ :=
  let k := neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
  (1/(2*Real.pi)) *
    ∫ r : ℝ, ‖Zeta23.paperFT k (r : ℂ)‖ *
      |Zeta23.EF.gammaBracket r|

theorem neutralIV012OriginalGammaAbsoluteBudget_nonnegative
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    0 ≤ neutralIV012OriginalGammaAbsoluteBudget b s t := by
  unfold neutralIV012OriginalGammaAbsoluteBudget
  apply mul_nonneg (by positivity)
  apply integral_nonneg
  intro r
  exact mul_nonneg (norm_nonneg _) (abs_nonneg _)

/-- The original mixed archimedean term is bounded by the actual
absolute Fourier/gamma integral, preserving the exact 2π factor. -/
theorem neutralIV012OriginalMixedArch_norm_le_gammaBudget
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    ‖neutralIV011OriginalMixedArch b s t‖ ≤
      neutralIV012OriginalGammaAbsoluteBudget b s t := by
  unfold neutralIV011OriginalMixedArch neutralIV012OriginalGammaAbsoluteBudget
  have hc : 0 ≤ (1/(2*Real.pi) : ℝ) := by positivity
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hc]
  have h := norm_integral_le_integral_norm (fun r : ℝ =>
    Zeta23.paperFT
      (neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume))
      (r : ℂ) * (Zeta23.EF.gammaBracket r : ℂ))
  simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs] at h
  exact mul_le_mul_of_nonneg_left h hc

/-- Exact nonnegative arithmetic envelope for the actual original
old/new complex mixed Weil EF, with distinct true prime, pole, Gamma
components, not an abstract matrix norm. -/
def neutralIV012OriginalMixedArithmeticBudget
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) (N : ℕ) : ℝ :=
  neutralIV012OriginalPoleMomentBudget b s t +
    neutralIV012OriginalFinitePrimeOverlapBudget s t N +
    neutralIV012OriginalGammaAbsoluteBudget b s t

theorem neutralIV012OriginalMixedArithmeticBudget_nonnegative
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) (N : ℕ) :
    0 ≤ neutralIV012OriginalMixedArithmeticBudget b s t N := by
  unfold neutralIV012OriginalMixedArithmeticBudget
  exact add_nonneg
    (add_nonneg
      (neutralIV012OriginalPoleMomentBudget_nonnegative b s t)
      (neutralIV012OriginalPrimeOverlapBudget_nonnegative s t N))
    (neutralIV012OriginalGammaAbsoluteBudget_nonnegative b s t)

/-- Source-specific unconditional modulus bound on the ORIGINAL
arithmetic zeta mixed Weil entry under nested physical supports.
The only extra input is a valid finite log-prime cutoff N. -/
theorem neutralIV012OriginalMixed_norm_le_arithmeticBudget
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n) :
    ‖neutralIV010Mixed b s t‖ ≤
      neutralIV012OriginalMixedArithmeticBudget b s t N := by
  rw [neutralIV011OriginalMixed_arithmeticSplit]
  unfold neutralIV012OriginalMixedArithmeticBudget
  calc
    ‖neutralIV011OriginalMixedPole b s t -
        neutralIV011OriginalMixedPrime b s t +
        neutralIV011OriginalMixedArch b s t‖ ≤
      ‖neutralIV011OriginalMixedPole b s t‖ +
        ‖neutralIV011OriginalMixedPrime b s t‖ +
        ‖neutralIV011OriginalMixedArch b s t‖ := by
      calc
        _ ≤ ‖neutralIV011OriginalMixedPole b s t -
              neutralIV011OriginalMixedPrime b s t‖ +
            ‖neutralIV011OriginalMixedArch b s t‖ := norm_add_le _ _
        _ ≤ (‖neutralIV011OriginalMixedPole b s t‖ +
              ‖neutralIV011OriginalMixedPrime b s t‖) +
            ‖neutralIV011OriginalMixedArch b s t‖ := by
              exact add_le_add_right (norm_sub_le _ _) _
    _ ≤ neutralIV012OriginalPoleMomentBudget b s t +
        neutralIV012OriginalFinitePrimeOverlapBudget s t N +
        neutralIV012OriginalGammaAbsoluteBudget b s t := by
      exact add_le_add
        (add_le_add
          (neutralIV012OriginalMixedPole_norm_le_momentBudget b s t)
          (neutralIV012OriginalMixedPrime_norm_le_overlapBudget
            a b hab s t hs ht N hN))
        (neutralIV012OriginalMixedArch_norm_le_gammaBudget b s t)

/-- The quantitative ORIGINAL source budget is sufficient for the
actual complex mixed Schur determinant bound when its SQUARE is
controlled by the unchanged old/new REAL diagonals. This is a
CONDITIONAL bound: the budget comparison is NOT silently assumed. -/
theorem neutralIV012OriginalMixedSchur_of_arithmeticBudget
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (A D : ℝ)
    (hBudget :
      (neutralIV012OriginalMixedArithmeticBudget b s t N)^2 ≤ A * D) :
    (neutralIV010Mixed b s t).re^2 +
      (neutralIV010Mixed b s t).im^2 ≤ A * D := by
  let B := neutralIV010Mixed b s t
  have hb : ‖B‖ ≤ neutralIV012OriginalMixedArithmeticBudget b s t N :=
    neutralIV012OriginalMixed_norm_le_arithmeticBudget
      a b hab s t hs ht N hN
  have hsq : ‖B‖ ^ 2 ≤
      (neutralIV012OriginalMixedArithmeticBudget b s t N)^2 :=
    pow_le_pow_left₀ (norm_nonneg _) hb 2
  have he : B.re^2 + B.im^2 = ‖B‖^2 := by
    rw [Complex.sq_norm, Complex.normSq_apply]
    ring
  calc
    B.re^2 + B.im^2 = ‖B‖^2 := he
    _ ≤ (neutralIV012OriginalMixedArithmeticBudget b s t N)^2 := hsq
    _ ≤ A * D := hBudget

/-- Genuine original arithmetic one-new-support positivity provided
the authentic pole/finite-prime/Gamma ENVELOPE, not merely the
actual cross term, satisfies a strong sufficient square estimate.
Old and new diagonal signs are explicit hypotheses and remain open
for a truly newly admitted Schwartz direction. -/
theorem neutralIV012OriginalOneNew_nonnegative_of_budget
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ) (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n)
    (hOld : 0 ≤ (neutralIV007OriginalMixedEnergy a s u).re)
    (hNew : 0 ≤ (neutralIV010Diagonal b t).re)
    (hBudget :
      (neutralIV012OriginalMixedArithmeticBudget b
        (neutralIV009PhysicalSchwartzSum s u) t N)^2 ≤
          (neutralIV007OriginalMixedEnergy a s u).re *
            (neutralIV010Diagonal b t).re)
    (v : ℂ) :
    0 ≤ (neutralIV010Diagonal b
      (neutralIV009PhysicalSchwartzSum s u + v • t)).re := by
  have hS : ∀ x : ℝ, x ∉ Set.Icc (-a) a →
      neutralIV009PhysicalSchwartzSum s u x = 0 :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs
  have hCross :=
    neutralIV012OriginalMixedSchur_of_arithmeticBudget a b hab
      (neutralIV009PhysicalSchwartzSum s u) t hS ht
      N hN _ _ hBudget
  exact neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
    a b hab s u hs t ht hOld hNew hCross v

#print axioms neutralIV011OriginalMixed_finitePrimeArithmetic
#print axioms neutralIV011OriginalMixed_arithmeticSplit
#print axioms neutralIV011OriginalOneNew_nonnegative_iff_crossBound
#print axioms neutralWindowCorrelation_poleCrossTerms
#print axioms neutralIV012PhysicalOverlapCost_nonnegative
#print axioms neutralIV012MixedCorrelation_norm_le_overlap
#print axioms neutralIV012OriginalPrimeOverlapBudget_nonnegative
#print axioms neutralIV012OriginalMixedPrime_norm_le_overlapBudget
#print axioms neutralIV012OriginalPoleMomentBudget_nonnegative
#print axioms neutralIV012OriginalMixedPole_eq_sourceMoments
#print axioms neutralIV012OriginalMixedPole_norm_le_momentBudget
#print axioms neutralIV012OriginalGammaAbsoluteBudget_nonnegative
#print axioms neutralIV012OriginalMixedArch_norm_le_gammaBudget
#print axioms neutralIV012OriginalMixedArithmeticBudget_nonnegative
#print axioms neutralIV012OriginalMixed_norm_le_arithmeticBudget
#print axioms neutralIV012OriginalMixedSchur_of_arithmeticBudget
#print axioms neutralIV012OriginalOneNew_nonnegative_of_budget

end
end WeilDefect
