import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF555 — exact algebraic squared-frequency root bridge, in characteristic zero.

For a real polynomial p and positive oscillator omega, set
F(X) = X * p.comp (X^2).  The NF554 original-source odd-jet
identities force high-order derivative vanishing of F at omega.

To transfer the corresponding root multiplicity back to p at
t=omega^2, we do NOT need a general Faà di Bruno theorem.
If p(Y)=(Y-t)^m q(Y), then
  F(X)=(X-omega)^m * [X*(X+omega)^m*q(X^2)].
The bracket is NONZERO at X=omega whenever omega>0 and q(t) != 0.
Thus the local root multiplicities agree.

The proved candidates here establish the exact factorization
and the nonzero-cofactor step generically over the real polynomials.
Source-specific odd-jet-to-formal-derivative Lean transfer and
the final rootMultiplicity equality are separately OPEN.
-/

/-- The squared-frequency polynomial factors into the two authentic
opposite real roots. For the true NF407 oscillators omega=2πf>0. -/
theorem neutralNF555SquareNodeFactorization (ω : ℝ) :
    (X : Polynomial ℝ) ^ 2 - C (ω ^ 2) =
      ((X : Polynomial ℝ) - C ω) * ((X : Polynomial ℝ) + C ω) := by
  have hc : (C (ω ^ 2) : Polynomial ℝ) = (C ω) ^ 2 := by
    simp
  rw [hc]
  ring

/-- Pulling one prescribed root factor through the quadratic
substitution gives the corresponding factor at each ±omega root.
The external X factor is the exact odd dual F(X)=X*p(X²). -/
theorem neutralNF555OriginalDualQuadraticFactorization
    (ω : ℝ) (q : Polynomial ℝ) (m : ℕ) :
    (X : Polynomial ℝ) *
        (((X - C (ω ^ 2)) ^ m * q).comp (X ^ 2)) =
      (X - C ω) ^ m *
        (X * (X + C ω) ^ m * q.comp (X ^ 2)) := by
  simp only [Polynomial.mul_comp, Polynomial.pow_comp,
    Polynomial.sub_comp, Polynomial.X_comp, Polynomial.C_comp,
    Polynomial.X_pow_comp]
  rw [neutralNF555SquareNodeFactorization]
  rw [mul_pow]
  ring

/-- The factor outside (X-omega)^m is nonzero at omega for
the genuine original strictly positive oscillator frequency.
This is the local multiplicity-preservation ingredient. -/
theorem neutralNF555OriginalDualQuadraticCofactor_nonzero
    (ω : ℝ) (hω : 0 < ω) (q : Polynomial ℝ) (m : ℕ)
    (hq : eval (ω ^ 2) q ≠ 0) :
    eval ω (X * (X + C ω) ^ m * q.comp (X ^ 2)) ≠ 0 := by
  have hdouble : ω + ω ≠ 0 := ne_of_gt (by linarith)
  have hnonzero :
      ω * (ω + ω) ^ m * eval (ω ^ 2) q ≠ 0 :=
    mul_ne_zero
      (mul_ne_zero (ne_of_gt hω) (pow_ne_zero m hdouble)) hq
  simpa only [Polynomial.eval_mul, Polynomial.eval_X,
    Polynomial.eval_pow, Polynomial.eval_add, Polynomial.eval_C,
    Polynomial.eval_comp] using hnonzero

end
end WeilDefect
