import WeilDefect.Arithmetic.ActualZetaOriginalJ242OddDualHermitePolynomialDerivatives
import WeilDefect.Arithmetic.ActualZetaOriginalJ242MonomialTrigOddJets
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF564 — complete analytic-to-polynomial Hermite bridge for both
parity forms of the TRUE original oscillator columns.

The authentic NF407 selected oscillator source has precisely
  x^(2r) * sin(ωx),   k=2r,
  x^(2r+1) * cos(ωx), k=2r+1,
for the original positive frequencies ω=2πf.

This file proves the generic ALL 242 odd-derivative source rows
sum to (-1)^r times the kth formal derivative of the TRUE
original dual polynomial F_a(X)=X*p_a(X²).

The separate source-indexed attachment, 68-node root-budget
divisibility and finite rank transfer remain separate gates.
No arbitrary generator independence assumption is introduced.
-/

/-- Exact original parity-adjusted polynomial derivative coefficient
as the scalar Leibniz term for either of the two source forms. -/
private theorem neutralNF564HermiteScalarParity
    (a ω : ℝ) (n r k t : ℕ) (hr : r ≤ n) :
    a * (( (2 * n + 1).choose k : ℝ) *
      (k.factorial : ℝ) * ((-1 : ℝ) ^ (n - r) * ω ^ t)) =
      (-1 : ℝ) ^ r *
        (((-1 : ℝ) ^ n * a) *
          (Nat.descFactorial (2 * n + 1) k : ℝ) * ω ^ t) := by
  rw [neutralNF564DescendingFactorial_eq_chooseFactorial]
  have hs := neutralNF564OriginalOddDualSignTransfer n r hr
  calc
    a * (((2 * n + 1).choose k : ℝ) *
        (k.factorial : ℝ) * ((-1 : ℝ) ^ (n - r) * ω ^ t)) =
      a * (((2 * n + 1).choose k : ℝ) *
        (k.factorial : ℝ) *
          (((-1 : ℝ) ^ r * (-1 : ℝ) ^ n) * ω ^ t)) := by
        rw [hs]
    _ = _ := by ring

/-- Every genuine even-order monomial-sine source jet is the
corresponding signed odd-dual Hermite derivative coefficient.
The below-order case is proved by the actual monomial
zero-jet theorem and zero descending factorial. -/
theorem neutralNF564EvenSineOddJet_isHermiteTerm
    (a ω : ℝ) (n r : ℕ) :
    a * (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r) * Real.sin (ω * x))) 0 =
      (-1 : ℝ) ^ r *
        (((-1 : ℝ) ^ n * a) *
          (Nat.descFactorial (2 * n + 1) (2 * r) : ℝ) *
          ω ^ (2 * n + 1 - 2 * r)) := by
  by_cases hr : r ≤ n
  · have hsub : 2 * n + 1 - 2 * r = 2 * (n - r) + 1 := by omega
    rw [neutralNF562EvenMonomialSine_originalOddJet ω n r hr, hsub]
    exact neutralNF564HermiteScalarParity
      a ω n r (2 * r) (2 * (n - r) + 1) hr
  · have hlt : n < r := Nat.lt_of_not_ge hr
    have hbelow : 2 * n + 1 < 2 * r := by omega
    rw [neutralNF562EvenMonomialSine_originalOddJet_below ω n r hlt]
    have hzero :
        Nat.descFactorial (2 * n + 1) (2 * r) = 0 :=
      Nat.descFactorial_eq_zero_iff_lt.mpr hbelow
    simp [hzero]

/-- Every genuine odd-order monomial-cosine source jet is the
corresponding signed odd-dual Hermite derivative coefficient. -/
theorem neutralNF564OddCosineOddJet_isHermiteTerm
    (a ω : ℝ) (n r : ℕ) :
    a * (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r + 1) * Real.cos (ω * x))) 0 =
      (-1 : ℝ) ^ r *
        (((-1 : ℝ) ^ n * a) *
          (Nat.descFactorial (2 * n + 1) (2 * r + 1) : ℝ) *
          ω ^ (2 * n + 1 - (2 * r + 1))) := by
  by_cases hr : r ≤ n
  · have hsub : 2 * n + 1 - (2 * r + 1) = 2 * (n - r) := by omega
    rw [neutralNF562OddMonomialCosine_originalOddJet ω n r hr, hsub]
    exact neutralNF564HermiteScalarParity
      a ω n r (2 * r + 1) (2 * (n - r)) hr
  · have hlt : n < r := Nat.lt_of_not_ge hr
    have hbelow : 2 * n + 1 < 2 * r + 1 := by omega
    rw [neutralNF562OddMonomialCosine_originalOddJet_below ω n r hlt]
    have hzero :
        Nat.descFactorial (2 * n + 1) (2 * r + 1) = 0 :=
      Nat.descFactorial_eq_zero_iff_lt.mpr hbelow
    simp [hzero]

/-- Full 242-odd-row original EVEN monomial sine source relation:
the left-kernel sum equals the r-parity corrected 2r-th
derivative of F_a(X)=X*p_a(X²) at exactly the same frequency ω. -/
theorem neutralNF564EvenSine_actualOddJetSum_eqHermiteDerivative
    (a : Fin 242 → ℝ) (ω : ℝ) (r : ℕ) :
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (fun x : ℝ => x ^ (2 * r) * Real.sin (ω * x))) 0) =
      (-1 : ℝ) ^ r *
        eval ω ((Polynomial.derivative^[2 * r])
          (neutralNF564OriginalDualOddPolynomial a)) := by
  rw [neutralNF564OriginalDualOddPolynomial_iterateDerivative_eval]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n hn
  exact neutralNF564EvenSineOddJet_isHermiteTerm
    (a n) ω n.val r

/-- Full 242-odd-row original ODD monomial cosine source relation:
the left-kernel sum equals the r-parity corrected (2r+1)-st
formal derivative of the genuine odd dual F_a at ω. -/
theorem neutralNF564OddCosine_actualOddJetSum_eqHermiteDerivative
    (a : Fin 242 → ℝ) (ω : ℝ) (r : ℕ) :
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (fun x : ℝ => x ^ (2 * r + 1) * Real.cos (ω * x))) 0) =
      (-1 : ℝ) ^ r *
        eval ω ((Polynomial.derivative^[2 * r + 1])
          (neutralNF564OriginalDualOddPolynomial a)) := by
  rw [neutralNF564OriginalDualOddPolynomial_iterateDerivative_eval]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro n hn
  exact neutralNF564OddCosineOddJet_isHermiteTerm
    (a n) ω n.val r

end
end WeilDefect
