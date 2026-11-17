import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialCoefficient
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF565 — an *algebraic*, original-242-coefficient frequency-side
Hermite polynomial, independent of pending analytic oscillator
differentiation and pending NF550 physical Gram compilation.

The genuine original odd-jet dual (NF557) has the exact real
coefficients p_a(T) = Σ_(n:Fin 242) (-1)^n a_n T^n.
The correct frequency polynomial is F_a(Z)=Z*p_a(Z²)
= Σ_(n:Fin 242) (-1)^n a_n Z^(2n+1).

Unlike a generic free Hermite matrix, the a_n are the *actual*
242 original odd-initial-jet left-kernel row coefficients. There
is no new frequency, no source matrix surrogate and no axiom.

The formal k-th frequency derivative of F_a(Z) is a finite
explicit descending-factorial sum; this is the common right-hand
side for every original k-th monomial sine/cosine column.
Connecting it to the *analytic* NF545 generators remains separate.
-/

/-- Exact ORIGINAL odd-jet frequency polynomial as a finite
signed sum of odd monomials, using precisely 242 coefficient rows. -/
def neutralNF565OriginalFrequencyHermitePolynomial
    (a : Fin 242 → ℝ) : Polynomial ℝ :=
  ∑ n : Fin 242,
    Polynomial.C ((-1 : ℝ) ^ n.val * a n) *
      Polynomial.X ^ (2 * n.val + 1)

/-- Evaluation of the genuine frequency polynomial is exactly
frequency times the true NF557 original signed dual evaluated
at the positive squared-frequency node, for *every* real frequency.
This is a polynomial identity, not the (still pending) source
sin/cos analytic derivative bridge. -/
theorem neutralNF565OriginalFrequencyHermitePolynomial_eval
    (a : Fin 242 → ℝ) (freq : ℝ) :
    (neutralNF565OriginalFrequencyHermitePolynomial a).eval freq =
      freq * (neutralNF557OriginalDualPolynomial a).eval (freq ^ 2) := by
  unfold neutralNF565OriginalFrequencyHermitePolynomial
    neutralNF557OriginalDualPolynomial
  rw [Polynomial.eval_finsetSum, Polynomial.eval_finsetSum,
    Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n hn
  simp only [Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_pow,
    Polynomial.eval_X, Polynomial.eval_monomial]
  have hpow : freq ^ (2 * n.val + 1) =
      freq * (freq ^ 2) ^ n.val := by
    rw [pow_add, ← pow_mul]
    ring
  rw [hpow]
  ring

/-- The finite signed odd-monomial frequency polynomial is
LITERALLY X times the unchanged original signed dual with X²
substituted, as a Polynomial ℝ identity (not only at a
particular selected source frequency). -/
theorem neutralNF565OriginalFrequencyHermitePolynomial_eq_comp
    (a : Fin 242 → ℝ) :
    neutralNF565OriginalFrequencyHermitePolynomial a =
      Polynomial.X *
        (neutralNF557OriginalDualPolynomial a).comp (Polynomial.X ^ 2) := by
  apply Polynomial.funext
  intro freq
  simpa only [Polynomial.eval_mul, Polynomial.eval_X,
    Polynomial.eval_comp, Polynomial.eval_pow] using
      neutralNF565OriginalFrequencyHermitePolynomial_eval a freq

/-- The frequency Hermite polynomial is genuinely ODD.
This is the finite algebraic symmetry corresponding to the
unchanged odd sine/cosine-monomial and sinh source generators.
It is derived, not taken as an extra source assumption. -/
theorem neutralNF565OriginalFrequencyHermitePolynomial_odd
    (a : Fin 242 → ℝ) (freq : ℝ) :
    (neutralNF565OriginalFrequencyHermitePolynomial a).eval (-freq) =
      -((neutralNF565OriginalFrequencyHermitePolynomial a).eval freq) := by
  rw [neutralNF565OriginalFrequencyHermitePolynomial_eval,
    neutralNF565OriginalFrequencyHermitePolynomial_eval]
  rw [even_two, neg_pow]
  ring

/-- The EXACT formal derivative of order k of the original
frequency-side dual is the finite Hermite falling-factorial sum
for all k, without a nonzero-frequency assumption.

Mathlib's derivative of X^(2n+1) is the exact Nat.descFactorial
(2n+1) k times X^(2n+1-k). This is the algebraic half of the
original 241-column analytic-to-dual bridge. -/
theorem neutralNF565OriginalFrequencyHermitePolynomial_derivative_eval
    (a : Fin 242 → ℝ) (freq : ℝ) (k : ℕ) :
    ((Polynomial.derivative^[k])
      (neutralNF565OriginalFrequencyHermitePolynomial a)).eval freq =
      ∑ n : Fin 242,
        ((-1 : ℝ) ^ n.val * a n) *
          (Nat.descFactorial (2 * n.val + 1) k : ℝ) *
          freq ^ (2 * n.val + 1 - k) := by
  unfold neutralNF565OriginalFrequencyHermitePolynomial
  rw [Polynomial.iterate_derivative_sum]
  simp only [Polynomial.iterate_derivative_C_mul,
    Polynomial.iterate_derivative_X_pow_eq_C_mul,
    Polynomial.eval_finsetSum, Polynomial.eval_mul,
    Polynomial.eval_C, Polynomial.eval_pow, Polynomial.eval_X]
  apply Finset.sum_congr rfl
  intro n hn
  ring

/-- The frequency-side Hermite polynomial cannot have
an identically vanishing formal k=0 derivative unless the
original 242-coefficient signed dual is zero. This is a clean
algebraic gate for the eventual left-kernel injectivity argument. -/
theorem neutralNF565OriginalFrequencyHermitePolynomial_eval_zero_of_dual_root
    (a : Fin 242 → ℝ) (freq : ℝ)
    (hroot : (neutralNF557OriginalDualPolynomial a).eval (freq ^ 2) = 0) :
    (neutralNF565OriginalFrequencyHermitePolynomial a).eval freq = 0 := by
  rw [neutralNF565OriginalFrequencyHermitePolynomial_eval, hroot, mul_zero]

end
end WeilDefect
