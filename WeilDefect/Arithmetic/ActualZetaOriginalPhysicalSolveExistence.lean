import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSolveResidual
import Mathlib.LinearAlgebra.FiniteDimensional.Basic

namespace WeilDefect
noncomputable section
open Finset

/-! NF611: the same near-identity row certificate used for the
residual also supplies existence and uniqueness of the actual
real transformed solution. No numerical LU existence premise. -/

def neutralNF611LinearApply {n : ℕ} (A : Fin n → Fin n → ℝ) :
    (Fin n → ℝ) →ₗ[ℝ] (Fin n → ℝ) where
  toFun := neutralNF606Apply A
  map_add' x y := by
    funext i
    simp [neutralNF606Apply, mul_add, Finset.sum_add_distrib]
  map_smul' c x := by
    funext i
    change (∑ j, A i j * (c * x j)) = c * ∑ j, A i j * x j
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring

theorem neutralNF611LinearApply_injective {n : ℕ} (A : Fin n → Fin n → ℝ)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect A i j|) ≤ 1/100) :
    Function.Injective (neutralNF611LinearApply A) := by
  intro x z h
  funext i
  have hres (j : Fin n) :
      |neutralNF606Apply A x j-neutralNF606Apply A z j| ≤ (0:ℝ) := by
    have hj : neutralNF606Apply A x j = neutralNF606Apply A z j :=
      congrFun h j
    rw [hj,sub_self,abs_zero]
  have hb := neutralNF606Residual_bound A x z (neutralNF606Apply A x)
    0 (by norm_num) hrow (fun _ => rfl) hres i
  have hz : |x i-z i| = 0 := le_antisymm (by simpa using hb) (abs_nonneg _)
  exact sub_eq_zero.mp (abs_eq_zero.mp hz)

theorem neutralNF611Solve_existsUnique {n : ℕ} (A : Fin n → Fin n → ℝ)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect A i j|) ≤ 1/100)
    (rhs : Fin n → ℝ) :
    ∃! y : Fin n → ℝ, ∀ i, neutralNF606Apply A y i = rhs i := by
  have hi := neutralNF611LinearApply_injective A hrow
  have hs : Function.Surjective (neutralNF611LinearApply A) := by
    first
    | exact (LinearMap.injective_iff_surjective).mp hi
    | exact (LinearMap.injective_iff_surjective (neutralNF611LinearApply A)).mp hi
    | exact (FiniteDimensional.injective_iff_surjective).mp hi
    | exact (FiniteDimensional.injective_iff_surjective (neutralNF611LinearApply A)).mp hi
  obtain ⟨y,hy⟩ := hs rhs
  have hy' (i : Fin n) : neutralNF606Apply A y i = rhs i := congrFun hy i
  refine ⟨y,hy',?_⟩
  intro z hz
  apply hi
  funext i
  exact (hz i).trans (hy' i).symm

/-- The accepted physical residual attachment needs no separate
exact solution hypothesis once the same row test is supplied. -/
theorem neutralNF611PhysicalSolve_box
    (D : Fin 242 → Fin 242 → ℝ) (y0 : Fin 242 → ℝ)
    (r : ℝ) (hr : 0≤r)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100)
    (hres : ∀ i, |neutralNF606TransformedRHS D i -
      neutralNF606Apply (neutralNF606TransformedH D) y0 i| ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i|+
      (∑ j, |D i j|)*(2*r) ≤ neutralNF587SelectedRadius i) :
    ∃! y : Fin 242 → ℝ,
      (∀ i, neutralNF606Apply (neutralNF606TransformedH D) y i =
        neutralNF606TransformedRHS D i) ∧
      neutralNF587SourceInFrozenBox (neutralNF606Apply D y) neutralNF604OriginalCritical := by
  obtain ⟨y,hy,huniq⟩ := neutralNF611Solve_existsUnique
    (neutralNF606TransformedH D) hrow (neutralNF606TransformedRHS D)
  refine ⟨y,⟨hy,neutralNF606OriginalBox_of_physical_residual D y y0 r hr
    hrow hy hres hpay⟩,?_⟩
  intro z hz
  exact huniq z hz.1

end
end WeilDefect
