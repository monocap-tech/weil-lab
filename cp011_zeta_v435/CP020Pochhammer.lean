module

public import Zeta.EulerMaclaurin.ErrorBound
public import Mathlib.RingTheory.Polynomial.Pochhammer
public import Mathlib.NumberTheory.Bernoulli

/-!
CP020: a reusable, FULLY QUANTIFIED norm inequality for the genuine
original 13-factor ascending Pochhammer polynomial, and a source
candidate for the ORIGINAL exact Bernoulli number B_14 = 7/6.

This is not a numerical sampling of its complex roots or coefficients.
Both statements are source-level candidates until the original Zeta
Lean v4.35 kernel and actual standard axiom audit accept them.
-/

@[expose] public section

open Finset

namespace CP020Pochhammer

/-- Original ascending Pochhammer polynomial is a finite product,
bounded on a COMPLEX disk by exactly the 13 scalar factors. The
bound works at arbitrary order and will be specialized to n=13. -/
theorem norm_ascPochhammer_eval_le_product
    (z : ℂ) (h : ‖z‖ ≤ (151 : ℝ)) (n : ℕ) :
    ‖(ascPochhammer ℂ n).eval z‖ ≤
      ∏ j ∈ Finset.range n, ((151 : ℝ) + j) := by
  induction n with
  | zero =>
      simp [ascPochhammer_zero]
  | succ n ih =>
      rw [ascPochhammer_succ_eval, norm_mul, Finset.prod_range_succ]
      have hfactor : ‖z + (n : ℂ)‖ ≤ (151 : ℝ) + n := by
        calc
          ‖z + (n : ℂ)‖ ≤ ‖z‖ + ‖(n : ℂ)‖ :=
            norm_add_le _ _
          _ = ‖z‖ + (n : ℝ) := by simp
          _ ≤ 151 + n := by linarith
      exact mul_le_mul ih hfactor (norm_nonneg _) (by positivity)

/-- The genuine source `Mathlib.NumberTheory.Bernoulli.bernoulli`
is rational, with B_14 = 7/6. This theorem is deliberately a
concrete original Lean kernel obligation, not an external numeric
hypothesis or a new axiom. -/
theorem original_bernoulli_fourteen :
    bernoulli 14 = (7 : ℚ) / 6 := by
  norm_num [bernoulli, bernoulli', Fin.sum_univ_eq_sum_range,
    Finset.sum_range_succ]

/-- For the source original M=6 Euler–Maclaurin error, its complex
coefficient is the EXACT real rational 7/(6*14!). -/
theorem source_B14_coefficient_norm :
    ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ)‖
      = (7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ)) := by
  rw [original_bernoulli_fourteen]
  norm_num [Complex.norm_real, Real.norm_eq_abs, Nat.factorial]

/-- All thirteen scalar Pochhammer majorants stay strictly positive. -/
theorem majorant_product_nonneg :
    (0 : ℝ) ≤ ∏ j ∈ Finset.range 13, ((151 : ℝ) + j) := by
  positivity

end CP020Pochhammer

#print axioms CP020Pochhammer.norm_ascPochhammer_eval_le_product
#print axioms CP020Pochhammer.original_bernoulli_fourteen
#print axioms CP020Pochhammer.source_B14_coefficient_norm
#print axioms CP020Pochhammer.majorant_product_nonneg
