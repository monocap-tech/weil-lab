import WeilDefect.Arithmetic.ActualZetaIV080GammaLinearEnvelopeGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory

/-!
IV085 — literal original von Mangoldt term and its finite physical
truncation on a bounded-support test, independently of IV081–IV084.
The subtraction in literatureRHS and both evaluation signs are retained.
-/

/-- Exact summand of the original Zeta23 literature RHS. -/
def neutralIV085PrimeSummand (k : ℝ → ℂ) (n : ℕ) : ℂ :=
  ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
    (k (Real.log n) + k (-Real.log n))

/-- No non-prime-power contributes to the literal source sum. -/
theorem neutralIV085PrimeSummand_nonPrimePower
    (k : ℝ → ℂ) (n : ℕ) (hn : ¬ IsPrimePow n) :
    neutralIV085PrimeSummand k n = 0 := by
  have hz := ArithmeticFunction.vonMangoldt_eq_zero_iff.mpr hn
  simp [neutralIV085PrimeSummand, hz]

/-- Both physical source evaluations vanish beyond the support radius. -/
theorem neutralIV085PrimeSummand_logFar
    (k : ℝ → ℂ) {L : ℝ}
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L)
    (n : ℕ) (hn : L < Real.log n) :
    neutralIV085PrimeSummand k n = 0 := by
  have hp : k (Real.log n) = 0 := by
    by_contra h
    exact (not_lt_of_ge ((le_abs_self _).trans (hsupp _ h))) hn
  have hm : k (-Real.log n) = 0 := by
    by_contra h
    have hb := hsupp _ h
    rw [abs_neg] at hb
    exact (not_lt_of_ge ((le_abs_self _).trans hb)) hn
  simp [neutralIV085PrimeSummand, hp, hm]

/-- Explicit finite cutoff: any natural N strictly above exp L. -/
theorem neutralIV085PrimeCutoff_log
    (L : ℝ) (N n : ℕ) (hN : Real.exp L < (N : ℝ))
    (hn : N ≤ n) : L < Real.log n := by
  have hc : (N : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  calc
    L = Real.log (Real.exp L) := (Real.log_exp _).symm
    _ < Real.log (n : ℝ) :=
      Real.log_lt_log (Real.exp_pos _) (hN.trans_le hc)

/-- The original prime sum equals a finite range, with no tail error. -/
theorem neutralIV085PrimeSum_eq_finite
    (k : ℝ → ℂ) {L : ℝ}
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L)
    (N : ℕ) (hN : Real.exp L < (N : ℝ)) :
    (∑' n : ℕ, neutralIV085PrimeSummand k n) =
      ∑ n ∈ Finset.range N, neutralIV085PrimeSummand k n := by
  apply tsum_eq_sum
  intro n hn
  have hnN : N ≤ n := Nat.le_of_not_gt (by
    intro hlt
    exact hn (Finset.mem_range.mpr hlt))
  exact neutralIV085PrimeSummand_logFar k hsupp n
    (neutralIV085PrimeCutoff_log L N n hN hnN)

/-- The literal source prime term is subtracted, not added.
This only expands the finite arithmetic component; the untouched
pole and original infinite Gamma components remain in source form. -/
theorem neutralIV085LiteratureRHS_finitePrime
    (k : ℝ → ℂ) {L : ℝ}
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L)
    (N : ℕ) (hN : Real.exp L < (N : ℝ)) :
    Zeta23.EF.literatureRHS k =
      Zeta23.paperFT k (Complex.I / 2) +
      Zeta23.paperFT k (-Complex.I / 2) -
      (∑ n ∈ Finset.range N, neutralIV085PrimeSummand k n) +
      (1 / (2 * Real.pi) : ℂ) *
        (∫ r : ℝ, Zeta23.paperFT k (r : ℂ) *
          (Zeta23.EF.gammaBracket r : ℂ)) := by
  unfold Zeta23.EF.literatureRHS
  change _ + _ - (∑' n : ℕ, neutralIV085PrimeSummand k n) + _ = _
  rw [neutralIV085PrimeSum_eq_finite k hsupp N hN]

#print axioms neutralIV085PrimeSummand_nonPrimePower
#print axioms neutralIV085PrimeSummand_logFar
#print axioms neutralIV085PrimeCutoff_log
#print axioms neutralIV085PrimeSum_eq_finite
#print axioms neutralIV085LiteratureRHS_finitePrime

end
end WeilDefect
