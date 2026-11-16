import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialCoefficient
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF559 — the exact genuine sinh-pole row of the ORIGINAL NF407
242-by-242 odd-initial-derivative matrix, in polynomial dual form.

The 242nd original source is sinh(x/2), not a fabricated 68th
oscillator or a generic interpolation functional. At order 2n+1,
its initial derivative coefficient is exactly (1/2)^(2n+1).
This file proves the *finite dual polynomial algebra* which will
attach that genuine analytic derivative to the negative node -1/4.
Formal differentiation of sinh and the 241 oscillator functions
remains a SEPARATE genuine-source Lean obligation; this is not a
global independence proof.
-/

/-- Exact finite algebraic relation between the original odd-jet
dual polynomial coefficient at n, its real negative-pole evaluation,
and the true sinh pole coefficient (1/2)^(2n+1). -/
theorem neutralNF559OriginalPoleCoefficientIdentity (n : ℕ) (a : ℝ) :
    (1 / 2 : ℝ) * ((-1 : ℝ) ^ n * a * (-(1 / 4 : ℝ)) ^ n) =
      a * (1 / 2 : ℝ) ^ (2 * n + 1) := by
  have hbase : (-1 : ℝ) * (-(1 / 4 : ℝ)) = (1 / 2 : ℝ) ^ 2 := by
    norm_num
  calc
    (1 / 2 : ℝ) * ((-1 : ℝ) ^ n * a * (-(1 / 4 : ℝ)) ^ n) =
      a * ((1 / 2 : ℝ) * (((-1 : ℝ) * (-(1 / 4 : ℝ))) ^ n)) := by
        rw [mul_pow]
        ring
    _ = a * ((1 / 2 : ℝ) * (((1 / 2 : ℝ) ^ 2) ^ n)) := by
      rw [hbase]
    _ = a * (1 / 2 : ℝ) ^ (2 * n + 1) := by
      rw [pow_mul, pow_add]
      ring

/-- Evaluating the actual 242-indexed dual polynomial at the
genuine negative pole t=-1/4 reproduces the ORIGINAL 242 initial
sinh coefficients, without any oscillator substitution. -/
theorem neutralNF559OriginalDualPolynomial_pole_eval
    (a : Fin 242 → ℝ) :
    (1 / 2 : ℝ) *
        (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) =
      ∑ n : Fin 242, a n * (1 / 2 : ℝ) ^ (2 * n.val + 1) := by
  unfold neutralNF557OriginalDualPolynomial
  rw [Polynomial.eval_finset_sum]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n hn
  rw [Polynomial.eval_monomial]
  exact neutralNF559OriginalPoleCoefficientIdentity n.val (a n)

end
end WeilDefect
