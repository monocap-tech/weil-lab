import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialSourceNodes
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF564 — formal polynomial derivative side of the ACTUAL original
241-oscillator odd-jet Hermite bridge, without assuming that
the original source derivatives match its coefficients.

For the TRUE 242-index real left-kernel coefficient vector a, the
frozen NF557 dual is p_a(T)=Σ_n(-1)^n a_n T^n. Its associated odd
polynomial F_a(X)=X*p_a(X²) expands to the 242 exact monomials
Σ_n(-1)^n a_n X^(2n+1).

This module uses Polynomial.iterate_derivative_sum and the
Mathlib theorem iterate_derivative_X_pow_eq_C_mul to establish
the exact kth derivative coefficients of F_a at any real ω.
That is the algebraic half of the source derivative-to-dual
Hermite theorem for original k=0,...,m_f-1.

This does NOT assert original source independence, nor that
higher derivatives of sine/cosine are already Lean verified.
-/

/-- Exact 242-column original left-kernel odd generating polynomial,
with historical coefficients and odd orders 1,...,483 unchanged. -/
def neutralNF564OriginalDualOddPolynomial (a : Fin 242 → ℝ) :
    Polynomial ℝ :=
  ∑ n : Fin 242, C ((-1 : ℝ) ^ n.val * a n) * X ^ (2 * n.val + 1)

/-- Direct scalar evaluation of the original odd dual polynomial:
F_a(ω) = ω*p_a(ω²), with the actual signs (-1)^n. -/
theorem neutralNF564OriginalDualOddPolynomial_eval
    (a : Fin 242 → ℝ) (ω : ℝ) :
    (neutralNF564OriginalDualOddPolynomial a).eval ω =
      ω * (neutralNF557OriginalDualPolynomial a).eval (ω ^ 2) := by
  unfold neutralNF564OriginalDualOddPolynomial
    neutralNF557OriginalDualPolynomial
  simp only [Polynomial.eval_finsetSum, Polynomial.eval_mul,
    Polynomial.eval_C, Polynomial.eval_pow, Polynomial.eval_X]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n hn
  rw [Polynomial.eval_monomial]
  have hpow : ω ^ (2 * n.val + 1) = ω * (ω ^ 2) ^ n.val := by
    rw [pow_add, pow_mul]
    ring
  rw [hpow]
  ring

/-- Polynomial IDENTIFICATION: the original odd Hermite object
is literally X*p_a(X²), not an independently chosen polynomial
or a numerical approximation of the source oscillators. -/
theorem neutralNF564OriginalDualOddPolynomial_eq_quadratic
    (a : Fin 242 → ℝ) :
    neutralNF564OriginalDualOddPolynomial a =
      X * (neutralNF557OriginalDualPolynomial a).comp (X ^ 2) := by
  apply Polynomial.funext
  intro ω
  rw [Polynomial.eval_mul, Polynomial.eval_X, Polynomial.eval_comp,
    Polynomial.eval_pow, Polynomial.eval_X]
  exact neutralNF564OriginalDualOddPolynomial_eval a ω

/-- EXACT kth formal polynomial derivative of the true original
odd-jet dual, at any real ω and any k. The descending factorial
is the true polynomial derivative of ω^(2n+1), with NO
factorial approximation or assumption about source independence. -/
theorem neutralNF564OriginalDualOddPolynomial_iterateDerivative_eval
    (a : Fin 242 → ℝ) (k : ℕ) (ω : ℝ) :
    eval ω ((Polynomial.derivative^[k])
      (neutralNF564OriginalDualOddPolynomial a)) =
      ∑ n : Fin 242,
        ((-1 : ℝ) ^ n.val * a n) *
          (Nat.descFactorial (2 * n.val + 1) k : ℝ) *
          ω ^ (2 * n.val + 1 - k) := by
  unfold neutralNF564OriginalDualOddPolynomial
  rw [Polynomial.iterate_derivative_sum]
  simp only [Polynomial.iterate_derivative_C_mul,
    Polynomial.iterate_derivative_X_pow_eq_C_mul,
    Polynomial.eval_finsetSum, Polynomial.eval_mul,
    Polynomial.eval_C, Polynomial.eval_pow, Polynomial.eval_X]
  apply Finset.sum_congr rfl
  intro n hn
  ring

/-- The exact REAL translation of Mathlib's descending
factorial into the source-audited binomial times monomial
factorial, for arbitrary derivative and oscillator orders. -/
theorem neutralNF564DescendingFactorial_eq_chooseFactorial
    (m k : ℕ) :
    (Nat.descFactorial m k : ℝ) =
      (m.choose k : ℝ) * (k.factorial : ℝ) := by
  have hn : Nat.descFactorial m k = m.choose k * k.factorial := by
    simpa only [Nat.mul_comm] using
      (Nat.descFactorial_eq_factorial_mul_choose m k)
  exact_mod_cast hn

/-- The historical cosine/sine source parity sign identity.
For k=2r or 2r+1, the original source uses the sign
(-1)^(n-r), whereas polynomial differentiation of
F_a(X)=Σ(-1)^n a_n X^(2n+1) introduces (-1)^n.
Multiplication by (-1)^r reconciles them exactly. -/
theorem neutralNF564OriginalOddDualSignTransfer
    (n r : ℕ) (hr : r ≤ n) :
    (-1 : ℝ) ^ r * (-1 : ℝ) ^ n =
      (-1 : ℝ) ^ (n - r) := by
  have htwice : (-1 : ℝ) ^ r * (-1 : ℝ) ^ r = 1 := by
    rw [← pow_add, show r + r = 2 * r by omega, pow_mul]
    norm_num
  calc
    (-1 : ℝ) ^ r * (-1 : ℝ) ^ n =
        (-1 : ℝ) ^ r *
          ((-1 : ℝ) ^ (n - r) * (-1 : ℝ) ^ r) := by
      rw [← pow_add, Nat.sub_add_cancel hr]
    _ = (-1 : ℝ) ^ (n - r) *
          ((-1 : ℝ) ^ r * (-1 : ℝ) ^ r) := by ring
    _ = (-1 : ℝ) ^ (n - r) := by rw [htwice, mul_one]

/-- The signed kth coefficient of the original odd-dual Hermite
polynomial agrees with BOTH original trigonometric monomial
branches, k=2r or k=2r+1. The only analytic fact needed after
this is the authentic oscillator's initial derivative identity. -/
theorem neutralNF564OriginalOddDualSignedCoefficient
    (n r k : ℕ) (hr : r ≤ n) :
    (-1 : ℝ) ^ r *
        ((-1 : ℝ) ^ n *
          (Nat.descFactorial (2 * n + 1) k : ℝ)) =
      (-1 : ℝ) ^ (n - r) *
        ((2 * n + 1).choose k : ℝ) * (k.factorial : ℝ) := by
  rw [neutralNF564DescendingFactorial_eq_chooseFactorial]
  calc
    (-1 : ℝ) ^ r *
        ((-1 : ℝ) ^ n *
          ((2 * n + 1).choose k * (k.factorial : ℝ))) =
      ((-1 : ℝ) ^ r * (-1 : ℝ) ^ n) *
        ((2 * n + 1).choose k * (k.factorial : ℝ)) := by ring
    _ = (-1 : ℝ) ^ (n - r) *
        ((2 * n + 1).choose k * (k.factorial : ℝ)) := by
      rw [neutralNF564OriginalOddDualSignTransfer n r hr]
    _ = _ := by ring

/-- Base k=0 of the full original Hermite bridge is precisely
the quadratic dual evaluation, without any source derivative
assumption. All k>0 follow from the formally stated higher
polynomial derivative identity and actual oscillator jets. -/
theorem neutralNF564OriginalDualOddPolynomial_zeroDerivative
    (a : Fin 242 → ℝ) (ω : ℝ) :
    eval ω ((Polynomial.derivative^[0])
      (neutralNF564OriginalDualOddPolynomial a)) =
        ω * (neutralNF557OriginalDualPolynomial a).eval (ω ^ 2) := by
  simpa only [Function.iterate_zero_apply]
    using neutralNF564OriginalDualOddPolynomial_eval a ω

end
end WeilDefect
