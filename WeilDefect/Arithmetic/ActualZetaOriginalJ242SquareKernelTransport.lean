import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
NF569 — square real matrix left-to-right kernel transport.
Independent of the original oscillator, Hermite root-budget and
physical Gram proof chains. Uses finite-dimensional surjectivity
of a linear endomorphism, not a numeric matrix inversion.
-/

/-- The finite left action a ↦ aᵀA as a linear endomorphism.
The source row/column orientation is explicit. -/
def neutralNF569RealSquareLeftAction {N : ℕ}
    (A : Matrix (Fin N) (Fin N) ℝ) :
    (Fin N → ℝ) →ₗ[ℝ] (Fin N → ℝ) where
  toFun a j := ∑ n : Fin N, a n * A n j
  map_add' a b := by
    funext j
    simp only [Pi.add_apply, add_mul, Finset.sum_add_distrib]
  map_smul' c a := by
    funext j
    simp only [Pi.smul_apply, smul_eq_mul, Finset.mul_sum, mul_assoc]

/-- Exact finite bilinear pairing identity, without any
symmetry assumption on A. -/
theorem neutralNF569RealSquare_pairing {N : ℕ}
    (A : Matrix (Fin N) (Fin N) ℝ)
    (a b : Fin N → ℝ) :
    (∑ j : Fin N, (neutralNF569RealSquareLeftAction A a) j * b j) =
      ∑ n : Fin N, a n * (∑ j : Fin N, A n j * b j) := by
  change (∑ j : Fin N, (∑ n : Fin N, a n * A n j) * b j) = _
  simp only [Finset.sum_mul, Finset.mul_sum, mul_assoc]
  exact Finset.sum_comm

/-- If the left action of a REAL SQUARE matrix has trivial kernel,
the right action also has trivial kernel. Surjectivity lets us
choose an actual row vector whose left action is an arbitrary
coordinate functional, so no determinant bound or numerical
conditioning is needed. -/
theorem neutralNF569RealSquare_rightKernel_zero_of_leftKernel_zero
    {N : ℕ} (A : Matrix (Fin N) (Fin N) ℝ)
    (hleft : ∀ a : Fin N → ℝ,
      (∀ j : Fin N, (∑ n : Fin N, a n * A n j) = 0) → a = 0)
    (b : Fin N → ℝ)
    (hright : ∀ n : Fin N, (∑ j : Fin N, A n j * b j) = 0) :
    b = 0 := by
  classical
  let L := neutralNF569RealSquareLeftAction A
  have hinj : Function.Injective L := by
    intro a c hac
    have hz : L (a - c) = 0 := by
      rw [map_sub, hac, sub_self]
    have hd : a - c = 0 := by
      apply hleft
      intro j
      exact congrFun hz j
    exact sub_eq_zero.mp hd
  have hsurj : Function.Surjective L :=
    LinearMap.injective_iff_surjective.mp hinj
  funext i
  let e : Fin N → ℝ := fun j => if j = i then 1 else 0
  obtain ⟨a, ha⟩ := hsurj e
  have hp := neutralNF569RealSquare_pairing A a b
  change (∑ j : Fin N, L a j * b j) =
    ∑ n : Fin N, a n * (∑ j : Fin N, A n j * b j) at hp
  rw [ha] at hp
  have hz : (∑ j : Fin N, e j * b j) = 0 := by
    simpa only [hright, mul_zero, Finset.sum_const_zero] using hp
  have he : (∑ j : Fin N, e j * b j) = b i := by
    simp [e, ite_mul, Finset.sum_ite_eq']
  rw [he] at hz
  exact hz

end
end WeilDefect
