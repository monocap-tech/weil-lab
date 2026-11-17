import WeilDefect.Arithmetic.ActualZetaOriginalJ242ComplexOddJetMatrixInvertible
import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramWeightedSquare
import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open scoped ContDiff

/-!
NF567 — from the genuine original real J242 odd-jet matrix to
GLOBAL ANALYTIC REAL AND COMPLEX GENERATOR INDEPENDENCE.

This file explicitly proves that every historical NF407 original
generator is smooth, the actual finite real combination
differentiates termwise at all 242 odd orders, and that a
combination vanishing identically is annihilated by the
authentic 242×242 real odd-jet matrix.

The real matrix IsUnit is the NF566 upstream candidate, and
its complexification is the NF567 candidate. The original
physical strict Gram requires a further *local* analytic
identity theorem (NF551), which is NOT supplied by this file.

All statements here are unverified Lean candidates until
focused Actions accepts the entire dependency chain.
-/

/-- Every exact original selected REAL source generator,
including all 241 x^k trig monomials and the last genuine
sinh(x/2), is C-infinity as a REAL function. -/
theorem neutralNF567OriginalRealGenerator_contDiff
    (j : Fin 242) :
    ContDiff ℝ ∞ (nf545OriginalSelectedRealGenerator j) := by
  classical
  unfold nf545OriginalSelectedRealGenerator
  split_ifs
  · dsimp
    split_ifs <;> fun_prop
  · fun_prop

/-- Exact real combination of the 242 authentic analytic
source functions, without physical-window truncation or
a freely chosen polynomial family. -/
def neutralNF567OriginalRealCombination
    (a : Fin 242 → ℝ) (x : ℝ) : ℝ :=
  ∑ j : Fin 242, a j * nf545OriginalSelectedRealGenerator j x

/-- Termwise real differentiation of the TRUE original
242-source analytic combination at ANY order n, in particular
the 242 original odd initial orders 1,3,...,483. -/
theorem neutralNF567OriginalRealCombination_iteratedDeriv
    (a : Fin 242 → ℝ) (n : ℕ) :
    (iteratedDeriv n (neutralNF567OriginalRealCombination a)) 0 =
      ∑ j : Fin 242,
        a j * (iteratedDeriv n
          (nf545OriginalSelectedRealGenerator j)) 0 := by
  unfold neutralNF567OriginalRealCombination
  rw [iteratedDeriv_fun_sum (I := Finset.univ)
    (f := fun j : Fin 242 => fun x : ℝ =>
      a j * nf545OriginalSelectedRealGenerator j x) (n := n) (x := 0) (by
    intro j hj
    exact (contDiff_const.mul
      (neutralNF567OriginalRealGenerator_contDiff j)).contDiffAt.of_le (by simp))]
  apply Finset.sum_congr rfl
  intro j hj
  exact iteratedDeriv_const_mul_field
    (n := n) (x := 0) (a j)
    (nf545OriginalSelectedRealGenerator j)

/-- Global vanishing of the authentic original 242 real
generator combination forces ALL 242 source derivatives'
matrix coordinates to vanish. -/
theorem neutralNF567OriginalRealCombination_zero_mulVec
    (a : Fin 242 → ℝ)
    (hzero : ∀ x : ℝ, neutralNF567OriginalRealCombination a x = 0) :
    neutralNF560ActualOriginalOddJetMatrix *ᵥ a = 0 := by
  funext n
  have hfun :
      neutralNF567OriginalRealCombination a = (fun _ : ℝ => 0) :=
    funext hzero
  have hderiv := congrArg
    (fun f : ℝ → ℝ => (iteratedDeriv (2 * n.val + 1) f) 0) hfun
  rw [neutralNF567OriginalRealCombination_iteratedDeriv,
    iteratedDeriv_fun_const_zero] at hderiv
  change (∑ j : Fin 242,
    neutralNF560ActualOriginalOddJetMatrix n j * a j) = 0
  calc
    (∑ j : Fin 242,
      neutralNF560ActualOriginalOddJetMatrix n j * a j) =
        ∑ j : Fin 242,
          a j * neutralNF560ActualOriginalOddJetMatrix n j := by
      apply Finset.sum_congr rfl
      intro j hj
      ring
    _ = 0 := by
      simpa only [neutralNF560ActualOriginalOddJetMatrix] using hderiv

/-- The actual REAL 242-function family is GLOBALLY independent,
as soon as the true original real odd-jet matrix is accepted
invertible. This uses pointwise real analytic source values
and exact differentiation, not numerical evaluation. -/
theorem neutralNF567OriginalRealGlobalIndependent
    (a : Fin 242 → ℝ)
    (hzero : ∀ x : ℝ, neutralNF567OriginalRealCombination a x = 0) :
    a = 0 := by
  have hmatrix :=
    neutralNF567OriginalRealCombination_zero_mulVec a hzero
  have hinj :
      Function.Injective neutralNF560ActualOriginalOddJetMatrix.mulVec :=
    Matrix.mulVec_injective_iff_isUnit.mpr
      neutralNF566OriginalOddJetMatrix_isUnit
  exact hinj (by simpa using hmatrix)

/-- The original COMPLEX physical combination uses precisely
the real functions and historical source order; its real part
is the corresponding real-coefficient source combination. -/
theorem neutralNF567OriginalComplexSource_re
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF550OriginalSourceCombination d x).re =
      neutralNF567OriginalRealCombination (fun j => (d j).re) x := by
  simp [neutralNF550OriginalSourceCombination,
    neutralNF546OriginalComplexGenerator,
    neutralNF567OriginalRealCombination,
    Complex.mul_re]

/-- The imaginary part of the unchanged original complex
source combination is equally an ORIGINAL real combination. -/
theorem neutralNF567OriginalComplexSource_im
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF550OriginalSourceCombination d x).im =
      neutralNF567OriginalRealCombination (fun j => (d j).im) x := by
  simp [neutralNF550OriginalSourceCombination,
    neutralNF546OriginalComplexGenerator,
    neutralNF567OriginalRealCombination,
    Complex.mul_im]

/-- The actual 242 genuine analytic source generators are
GLOBALLY COMPLEX independent: if their untruncated original
complex combination vanishes on all reals, every original
complex coefficient is zero. This is a global theorem, not
yet the local-collar theorem needed by the canonical Gram. -/
theorem neutralNF567OriginalComplexGlobalIndependent
    (d : Fin 242 → ℂ)
    (hzero : ∀ x : ℝ, neutralNF550OriginalSourceCombination d x = 0) :
    d = 0 := by
  have hre : (fun j : Fin 242 => (d j).re) = 0 :=
    neutralNF567OriginalRealGlobalIndependent _ (by
      intro x
      have hz := congrArg Complex.re (hzero x)
      simpa only [neutralNF567OriginalComplexSource_re,
        Complex.zero_re] using hz)
  have him : (fun j : Fin 242 => (d j).im) = 0 :=
    neutralNF567OriginalRealGlobalIndependent _ (by
      intro x
      have hz := congrArg Complex.im (hzero x)
      simpa only [neutralNF567OriginalComplexSource_im,
        Complex.zero_im] using hz)
  funext j
  apply Complex.ext
  · exact congrFun hre j
  · exact congrFun him j

end
end WeilDefect
