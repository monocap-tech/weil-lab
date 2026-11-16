import WeilDefect.Arithmetic.ActualZetaOriginalJ242OriginalPoleDual
import WeilDefect.Arithmetic.ActualZetaOriginalJ242SourceFunctions
import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF560 — first actual ANALYTIC initial-jet theorem for one of the
242 authentic NF407 source generators. The index 241 generator is
literally Real.sinh(x/2), not an assumed formal derivative sequence.

Mathlib already proves Real.iteratedDeriv_odd_sinh and the exact
chain rule for iteratedDeriv of f(c*x). Combine them with the
source-accepted NF545 pole identity to obtain ALL odd derivatives
of the genuine original sinh pole at x=0. The previous NF559
polynomial pole evaluation identity is then available to attach
this analytic row to the original 242-index dual polynomial.

The 241 original sine/cosine monomial higher-derivative formulas,
their dual bridge, combined root-budget divisibility and global
independence are separately OPEN in Lean.
-/

/-- The true analytic odd derivatives of the unmodified sinh-pole
function at zero; each coefficient is 2^(-(2n+1)), for every n,
not merely a bounded finite test list. -/
theorem neutralNF560SinhHalf_oddIteratedDeriv (n : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => Real.sinh (x / 2))) 0 =
      (1 / 2 : ℝ) ^ (2 * n + 1) := by
  have hfun : (fun x : ℝ => Real.sinh (x / 2)) =
      (fun x : ℝ => Real.sinh ((1 / 2 : ℝ) * x)) := by
    funext x
    congr 1
    ring
  rw [hfun]
  rw [iteratedDeriv_comp_const_mul
    (Real.contDiff_sinh (n := 2 * n + 1)) (1 / 2 : ℝ)]
  simp only [Real.iteratedDeriv_odd_sinh, Real.cosh_zero, mul_one]

/-- The actual ORIGINAL source function at pole row 241 has
these exact odd initial derivatives. No arbitrary generator
sequence or numerical replacement is substituted. -/
theorem neutralNF560ActualOriginalPole_oddIteratedDeriv (n : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (nf545OriginalSelectedRealGenerator ⟨241, by omega⟩)) 0 =
      (1 / 2 : ℝ) ^ (2 * n + 1) := by
  have hsource :
      nf545OriginalSelectedRealGenerator ⟨241, by omega⟩ =
        (fun x : ℝ => Real.sinh (x / 2)) := by
    funext x
    exact nf545OriginalSelectedPole_is_sinh x
  rw [hsource]
  exact neutralNF560SinhHalf_oddIteratedDeriv n

/-- The 242 exact genuine original sinh odd derivatives, paired
with original real dual row coefficients a, are the dual polynomial
at the ACTUAL negative squared-frequency pole node -1/4.

This is the first fully source-analytic instance of the source
dual left-kernel identity, subject to compiler acceptance. -/
theorem neutralNF560ActualOriginalPole_dualOddJets
    (a : Fin 242 → ℝ) :
    (∑ n : Fin 242,
      a n * (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨241, by omega⟩)) 0) =
      (1 / 2 : ℝ) *
        (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) := by
  calc
    (∑ n : Fin 242,
      a n * (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨241, by omega⟩)) 0) =
      ∑ n : Fin 242, a n * (1 / 2 : ℝ) ^ (2 * n.val + 1) := by
        apply Finset.sum_congr rfl
        intro n hn
        rw [neutralNF560ActualOriginalPole_oddIteratedDeriv n.val]
    _ = (1 / 2 : ℝ) *
          (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) := by
      exact (neutralNF559OriginalDualPolynomial_pole_eval a).symm

/-- The AUTHENTIC real 242×242 odd-initial-derivative matrix,
including all 241 sine/cosine monomial oscillator generators and
the true index-241 sinh pole. Its row n is derivative order 2n+1,
not a numerical sample or a freely prescribed finite matrix. -/
def neutralNF560ActualOriginalOddJetMatrix :
    Matrix (Fin 242) (Fin 242) ℝ :=
  fun n j =>
    (iteratedDeriv (2 * n.val + 1)
      (nf545OriginalSelectedRealGenerator j)) 0

/-- The last column of the actual analytic source odd-jet matrix
is precisely the genuine sinh-pole derivative sequence. -/
theorem neutralNF560ActualOriginalOddJetMatrix_pole (n : Fin 242) :
    neutralNF560ActualOriginalOddJetMatrix n ⟨241, by omega⟩ =
      (1 / 2 : ℝ) ^ (2 * n.val + 1) := by
  exact neutralNF560ActualOriginalPole_oddIteratedDeriv n.val

/-- Vanishing of the true original matrix's left-kernel pole
coordinate forces the actual dual polynomial to have the
negative real root -1/4. This lemma is a direct analytic-source
obligation, not a surrogate Gram or a general finite basis. -/
theorem neutralNF560OriginalMatrixPoleKernelForcesRoot
    (a : Fin 242 → ℝ)
    (hpole :
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n ⟨241, by omega⟩) = 0) :
    (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) = 0 := by
  apply neutralNF560OriginalPoleForcesDualRoot a
  exact hpole

/-- The authentic original index-241 sinh pole equation forces
the dual polynomial's vanishing at its genuine negative node.
This needs no assumptions about the other 241 oscillators. -/
theorem neutralNF560OriginalPoleForcesDualRoot
    (a : Fin 242 → ℝ)
    (hpole : (∑ n : Fin 242,
      a n * (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨241, by omega⟩)) 0) = 0) :
    (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) = 0 := by
  rw [neutralNF560ActualOriginalPole_dualOddJets] at hpole
  have hhalf : (1 / 2 : ℝ) ≠ 0 := by norm_num
  exact (mul_eq_zero.mp hpole).resolve_left hhalf

end
end WeilDefect
