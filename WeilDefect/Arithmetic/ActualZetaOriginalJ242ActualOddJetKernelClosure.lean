import WeilDefect.Arithmetic.ActualZetaOriginalJ242Original68RootBudget
import WeilDefect.Arithmetic.ActualZetaOriginalJ242Actual67BlockHermiteCompleteness
import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialCoefficient
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF568 — remove the remaining dual-nonzero condition and prove the
terminal REAL left-kernel triviality of the literal original 242×242
odd analytic derivative matrix A_nj = D_x^(2n+1) j_j(0).

The correct implication is
  p_a ≠ 0 ⇒ F_a = X * p_a.comp(X²) ≠ 0.
This requires checking that composing with the NONCONSTANT X²
cannot annihilate a nonzero real polynomial. It follows from
Mathlib's comp_eq_zero_iff; no interpolation or Gram assumption.

The generic 68-node simultaneous root-count bound is formalized
independently in ActualZetaOriginalJ242Original68RootBudget, and
the original source-specific 67 squared-node multiplicity constraints
come from NF567, in turn from NF566's literal source-analytic jets.

This is the full original odd-jet matrix LEFT kernel theorem provided
all its imported source analytic proofs compile. It is NOT a direct
claim about RH or complete gamma/prime cofinite coercivity.
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

/-- The FINAL real original J242 source odd-jet LEFT KERNEL
is trivial. Here A is the exact unchanged NF560 ANALYTIC matrix,
not the exact-audit coefficient CSV, a numerical approximation,
or an abstract Hermite system.

Every original oscillator monomial and the true sinh pole enters
through the NF566/NF567 source-indexed analytic bridge.
The 67+1 simultaneous multiplicity budget contradicts
natDegree(p_a)<242 if p_a≠0; therefore p_a=0 and NF558 implies
a=0.

This proof relies on NF566/NF567 Lean acceptance, which must be
checked before this theorem is considered compiler certified. -/
theorem neutralNF568OriginalActual242OddJetMatrix_leftKernel_zero
    (a : Fin 242 → ℝ)
    (hkernel : ∀ j : Fin 242,
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n j) = 0) :
    a = 0 := by
  have hpzero : neutralNF557OriginalDualPolynomial a = 0 := by
    by_contra hp
    have hF : neutralNF565OriginalFrequencyHermitePolynomial a ≠ 0 :=
      neutralNF568OriginalFrequencyHermite_ne_zero a hp
    obtain ⟨hgroups, hpole⟩ :=
      neutralNF567OriginalFull242Kernel_squaredDualRootMultiplicities
        a hkernel hp hF
    have hzero := neutralNF568OriginalDual68Roots_forcesZero
      a hgroups hpole
    exact hp hzero
  exact neutralNF558OriginalDualPolynomial_eq_zero a hpzero

/-- The authentic REAL square 242-by-242 source odd-jet matrix
has trivial LEFT kernel, hence no nonzero real row vector can
annihilate ALL 242 actual original analytic source columns. -/
theorem neutralNF568OriginalActual242OddJetMatrix_leftKernel_injective :
    Function.Injective
      (fun a : Fin 242 → ℝ =>
        fun j : Fin 242 =>
          ∑ n : Fin 242,
            a n * neutralNF560ActualOriginalOddJetMatrix n j) := by
  intro a b hab
  have hzero : (a - b : Fin 242 → ℝ) = 0 := by
    apply neutralNF568OriginalActual242OddJetMatrix_leftKernel_zero
    intro j
    have hj := congrFun hab j
    simpa only [Pi.sub_apply, sub_mul, Finset.sum_sub_distrib,
      sub_eq_zero] using hj
  exact sub_eq_zero.mp hzero

end
end WeilDefect
