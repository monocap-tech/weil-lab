import WeilDefect.Arithmetic.ActualZetaOriginalJ242OscillatorHermiteDualBridge
import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualOscillatorOddDerivatives
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF564 — source-indexed, ALL original oscillator source columns:
the true analytic odd-initial-jet left-kernel equations become
Hermite derivative equations for the exact signed odd polynomial
F_a(X)=X*p_a(X²).

Each i : Fin 241 points to its historical NF407 frozen rational
frequency and order through nf545OriginalOscillatorNodeAt.
There is NO new oscillator, numerical Gram, arbitrary independence
assumption, or replacement of the true separate sinh(x/2) pole.

The generic sine/cosine parity bridge lives in
ActualZetaOriginalJ242OscillatorHermiteDualBridge; this module
attaches it to the exact original source indices and true omega.
-/

/-- The 242-row analytic dual bridge for either original
parity-selected monomial function at ANY order k. The polynomial
derivative is formal and exact (not finite differences). -/
theorem neutralNF564ParitySelectedSource_oddJetDual
    (a : Fin 242 → ℝ) (ω : ℝ) (k : ℕ) :
    (∑ n : Fin 242,
      a n * (iteratedDeriv (2 * n.val + 1)
        (fun x : ℝ => x ^ k *
          (if Even k then Real.sin (ω * x)
           else Real.cos (ω * x)))) 0) =
      (-1 : ℝ) ^ (k / 2) *
        eval ω ((Polynomial.derivative^[k])
          (neutralNF564OriginalDualOddPolynomial a)) := by
  rcases even_or_odd k with he | ho
  · obtain ⟨r, hkr⟩ := even_iff_exists_two_mul.mp he
    subst k
    have hev : Even (2 * r) := by
      exact even_two_mul r
    have hdiv : (2 * r) / 2 = r := by omega
    simpa only [if_pos hev, hdiv] using
      (neutralNF564EvenSine_actualOddJetSum_eqHermiteDerivative a ω r)
  · obtain ⟨r, hkr⟩ := ho
    subst k
    have hodd : ¬ Even (2 * r + 1) := by
      simp
    have hdiv : (2 * r + 1) / 2 = r := by omega
    simpa only [if_neg hodd, hdiv] using
      (neutralNF564OddCosine_actualOddJetSum_eqHermiteDerivative a ω r)

/-- The actual, ORIGINAL NF407 241 oscillator columns are
precisely frequency derivatives of the same source dual
polynomial. This is the key missing analytic→Hermite translation
at arbitrary historical order k_i. -/
theorem neutralNF564ActualOriginalOscillator_oddJetDual
    (a : Fin 242 → ℝ) (i : Fin 241) :
    (∑ n : Fin 242,
      a n * (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) =
      (-1 : ℝ) ^ (neutralNF562OriginalOscillatorOrder i / 2) *
        eval (neutralNF562OriginalOscillatorOmega i)
          ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
            (neutralNF564OriginalDualOddPolynomial a)) := by
  rw [neutralNF562OriginalOscillator_exactSource i]
  exact neutralNF564ParitySelectedSource_oddJetDual a
    (neutralNF562OriginalOscillatorOmega i)
    (neutralNF562OriginalOscillatorOrder i)

/-- Every original oscillator left-kernel equation, indexed by
its EXACT source table index i, forces the corresponding
polynomial Hermite derivative to vanish at its true frequency
omega_i>0. The sign (-1)^(k_i/2) never vanishes. -/
theorem neutralNF564ActualOriginalOscillator_kernelForcesHermiteRoot
    (a : Fin 242 → ℝ) (i : Fin 241)
    (hcolumn :
      (∑ n : Fin 242,
        a n * (iteratedDeriv (2 * n.val + 1)
          (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) = 0) :
    eval (neutralNF562OriginalOscillatorOmega i)
      ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
        (neutralNF564OriginalDualOddPolynomial a)) = 0 := by
  rw [neutralNF564ActualOriginalOscillator_oddJetDual] at hcolumn
  have hsgn :
      ((-1 : ℝ) ^ (neutralNF562OriginalOscillatorOrder i / 2)) ≠ 0 :=
    pow_ne_zero _ (by norm_num)
  exact (mul_eq_zero.mp hcolumn).resolve_left hsgn

end
end WeilDefect
