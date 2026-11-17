import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualPoleOddDerivatives
import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open scoped ContDiff

/-!
NF569 — independent analytic reduction from a vanishing global
combination of the literal original NF407 generators to the
RIGHT kernel of its actual NF560 odd-jet matrix.

This requires only ordinary finite-sum differentiation and the
smoothness of the original sine/cosine/sinh functions, not the
pending NF566 oscillator closed jet formulas, NF568 left-kernel
proof, or NF550 Gram.
-/

/-- Each literal original real source function is smooth to
every finite order, before any physical-window truncation. -/
theorem neutralNF569OriginalRealGenerator_contDiffAt
    (j : Fin 242) (m : ℕ) (x : ℝ) :
    ContDiffAt ℝ m (nf545OriginalSelectedRealGenerator j) x := by
  by_cases hj : j.val < 241
  · simp only [nf545OriginalSelectedRealGenerator, dif_pos hj]
    split_ifs <;> fun_prop
  · simp only [nf545OriginalSelectedRealGenerator, dif_neg hj]
    fun_prop

/-- Original real combination, with precisely the authentic
242 source indices and no altered frequency or source window. -/
def neutralNF569OriginalRealCombination
    (b : Fin 242 → ℝ) (x : ℝ) : ℝ :=
  ∑ j : Fin 242, b j * nf545OriginalSelectedRealGenerator j x

/-- Differentiating the actual real source combination to odd
order 2n+1 at zero produces its true odd-jet matrix row action.
No closed formula for any individual jet is required here. -/
theorem neutralNF569OriginalRealCombination_oddJet
    (b : Fin 242 → ℝ) (n : Fin 242) :
    (iteratedDeriv (2 * n.val + 1)
      (neutralNF569OriginalRealCombination b)) 0 =
      ∑ j : Fin 242, neutralNF560ActualOriginalOddJetMatrix n j * b j := by
  unfold neutralNF569OriginalRealCombination
  rw [iteratedDeriv_fun_sum
    (f := fun j : Fin 242 => fun x : ℝ =>
      b j * nf545OriginalSelectedRealGenerator j x)
    (I := Finset.univ)
    (fun j _ => (contDiffAt_const).mul
      (neutralNF569OriginalRealGenerator_contDiffAt j (2 * n.val + 1) 0))]
  apply Finset.sum_congr rfl
  intro j hj
  rw [iteratedDeriv_const_mul_field]
  change b j * neutralNF560ActualOriginalOddJetMatrix n j =
    neutralNF560ActualOriginalOddJetMatrix n j * b j
  exact mul_comm _ _

/-- Any globally zero combination of the ORIGINAL real source
functions is in the actual analytic odd-jet matrix RIGHT kernel.
The coefficients b themselves need not be real-source kernel
coefficients of any assumed abstract basis. -/
theorem neutralNF569OriginalRealCombination_zero_forcesRightKernel
    (b : Fin 242 → ℝ)
    (hzero : ∀ x : ℝ, neutralNF569OriginalRealCombination b x = 0) :
    ∀ n : Fin 242,
      (∑ j : Fin 242, neutralNF560ActualOriginalOddJetMatrix n j * b j) = 0 := by
  have hfun : neutralNF569OriginalRealCombination b =
      (fun _ : ℝ => (0 : ℝ)) := funext hzero
  intro n
  rw [← neutralNF569OriginalRealCombination_oddJet b n, hfun]
  simp

/-- The true complex-coefficient source combination, defined
using the SAME real generator functions under Complex.ofReal. -/
def neutralNF569OriginalComplexCombination
    (d : Fin 242 → ℂ) (x : ℝ) : ℂ :=
  ∑ j : Fin 242, d j * (nf545OriginalSelectedRealGenerator j x : ℂ)

/-- Real part of the genuine complex combination is exactly
the original real combination of coefficient real parts. -/
theorem neutralNF569OriginalComplexCombination_re
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF569OriginalComplexCombination d x).re =
      neutralNF569OriginalRealCombination (fun j => (d j).re) x := by
  classical
  unfold neutralNF569OriginalComplexCombination
    neutralNF569OriginalRealCombination
  let f : Fin 242 → ℂ :=
    fun j => d j * (nf545OriginalSelectedRealGenerator j x : ℂ)
  have hsum (s : Finset (Fin 242)) :
      (∑ j ∈ s, f j).re = ∑ j ∈ s, (f j).re := by
    induction s using Finset.induction_on with
    | empty => simp
    | insert i s hi ih =>
        simp only [Finset.sum_insert hi, Complex.add_re, ih]
  change (∑ j : Fin 242, f j).re = _
  rw [hsum Finset.univ]
  apply Finset.sum_congr rfl
  intro j hj
  simp [f, Complex.mul_re]

/-- Imaginary part uses the SAME original real generator space,
with imaginary coefficients as the real vector. -/
theorem neutralNF569OriginalComplexCombination_im
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF569OriginalComplexCombination d x).im =
      neutralNF569OriginalRealCombination (fun j => (d j).im) x := by
  classical
  unfold neutralNF569OriginalComplexCombination
    neutralNF569OriginalRealCombination
  let f : Fin 242 → ℂ :=
    fun j => d j * (nf545OriginalSelectedRealGenerator j x : ℂ)
  have hsum (s : Finset (Fin 242)) :
      (∑ j ∈ s, f j).im = ∑ j ∈ s, (f j).im := by
    induction s using Finset.induction_on with
    | empty => simp
    | insert i s hi ih =>
        simp only [Finset.sum_insert hi, Complex.add_im, ih]
  change (∑ j : Fin 242, f j).im = _
  rw [hsum Finset.univ]
  apply Finset.sum_congr rfl
  intro j hj
  simp [f, Complex.mul_im]

end
end WeilDefect
