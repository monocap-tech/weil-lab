import WeilDefect.Arithmetic.ActualZetaOriginalJ242FrequencyHermitePolynomial
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF568 — completely independent ORIGINAL dual nonzero transfer:
p_a≠0 implies F_a(X)=X*p_a(X²)≠0. No NF566 oscillator
differentiation, NF567 original source blocks or NF550 Gram needed.
Uses Mathlib's nonconstant-polynomial composition criterion.
-/

/-- Exact algebraic nonzero transfer for an arbitrary true real
dual p: X*p(X²) cannot vanish unless p=0. It uses the fact that
X² is not a constant polynomial, not an assumed injective source
matrix. -/
theorem neutralNF568OddQuadraticPolynomial_ne_zero
    (p : Polynomial ℝ) (hp : p ≠ 0) :
    ((Polynomial.X : Polynomial ℝ) *
      p.comp (Polynomial.X ^ 2)) ≠ 0 := by
  have hnonconstant :
      ((Polynomial.X : Polynomial ℝ) ^ 2) ≠
        Polynomial.C (((Polynomial.X : Polynomial ℝ) ^ 2).coeff 0) := by
    intro heq
    have hdeg := congrArg Polynomial.natDegree heq
    simp only [Polynomial.natDegree_X_pow, Polynomial.natDegree_C] at hdeg
    omega
  have hcomp : p.comp ((Polynomial.X : Polynomial ℝ) ^ 2) ≠ 0 := by
    intro heq
    rcases (Polynomial.comp_eq_zero_iff).mp heq with hp0 | ⟨_, hconstant⟩
    · exact hp hp0
    · exact hnonconstant hconstant
  exact mul_ne_zero Polynomial.X_ne_zero hcomp

/-- In the actual original 242-row coefficient family the exact
NF565 source frequency polynomial is nonzero whenever the
original signed dual p_a is nonzero. No extra polynomial premise. -/
theorem neutralNF568OriginalFrequencyHermite_ne_zero
    (a : Fin 242 → ℝ)
    (hp : neutralNF557OriginalDualPolynomial a ≠ 0) :
    neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0 := by
  rw [neutralNF565OriginalFrequencyHermitePolynomial_eq_comp]
  exact neutralNF568OddQuadraticPolynomial_ne_zero
    (neutralNF557OriginalDualPolynomial a) hp

end
end WeilDefect
