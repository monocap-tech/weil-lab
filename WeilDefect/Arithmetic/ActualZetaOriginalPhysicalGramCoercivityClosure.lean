import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSolveResidual

namespace WeilDefect

/-!
NF661: original physical 15-source target and a generic coercivity transport
through a preconditioner. These statements do not silently assume full matrix
positivity. The numerical/analytic attachment to NF658 and NF659 remains a
separate proof obligation.
-/

noncomputable section
open Finset

/-- The exact selected original physical basis: oscillators 0,...,13
and the original genuine sinh pole generator 241. -/
def neutralNF661Source (i : Fin 15) : Fin 242 :=
  ⟨if i.val = 14 then 241 else i.val, by
    have hi := i.isLt
    split_ifs <;> omega⟩

def neutralNF661PhysicalH (i j : Fin 15) : ℝ :=
  neutralNF606PhysicalH (neutralNF661Source i) (neutralNF661Source j)

theorem neutralNF661PhysicalH_symm (i j : Fin 15) :
    neutralNF661PhysicalH i j = neutralNF661PhysicalH j i := by
  exact neutralNF606PhysicalH_symm _ _

/-- Real quadratic energy, with the source dimension deliberately generic. -/
def neutralNF661Quadratic {n : ℕ}
    (a : Fin n → Fin n → ℝ) (x : Fin n → ℝ) : ℝ :=
  ∑ i : Fin n, ∑ j : Fin n, a i j * x i * x j

def neutralNF661SqNorm {n : ℕ} (x : Fin n → ℝ) : ℝ :=
  ∑ i : Fin n, x i ^ 2

theorem neutralNF661SqNorm_nonneg {n : ℕ} (x : Fin n → ℝ) :
    0 ≤ neutralNF661SqNorm x := by
  unfold neutralNF661SqNorm
  exact Finset.sum_nonneg (fun i _ => sq_nonneg _)

/-- The final basis-transfer inequality only needs:
1. positive-form coercivity in transformed coordinates;
2. the exact quadratic-form identity for the change of basis;
3. a norm bound for that basis map; and
4. surjectivity of the map.
None of these analytic/geometric premises is conjured by this theorem. -/
theorem neutralNF661Coercivity_of_preconditioned
    {n : ℕ}
    (H B : Fin n → Fin n → ℝ)
    (T : (Fin n → ℝ) → (Fin n → ℝ))
    (m normBound target : ℝ)
    (htarget : 0 ≤ target)
    (hmargin : ∀ y, m * neutralNF661SqNorm y ≤
      neutralNF661Quadratic B y)
    (hcongruence : ∀ y,
      neutralNF661Quadratic B y =
        neutralNF661Quadratic H (T y))
    (hnorm : ∀ y,
      neutralNF661SqNorm (T y) ≤ normBound * neutralNF661SqNorm y)
    (honto : ∀ x, ∃ y, T y = x)
    (hgate : target * normBound ≤ m) :
    ∀ x, target * neutralNF661SqNorm x ≤
      neutralNF661Quadratic H x := by
  intro x
  obtain ⟨y, hy⟩ := honto x
  subst x
  have hnorm' := hnorm y
  have hpos := neutralNF661SqNorm_nonneg y
  calc
    target * neutralNF661SqNorm (T y) ≤
        target * (normBound * neutralNF661SqNorm y) :=
      mul_le_mul_of_nonneg_left hnorm' htarget
    _ = (target * normBound) * neutralNF661SqNorm y := by ring
    _ ≤ m * neutralNF661SqNorm y :=
      mul_le_mul_of_nonneg_right hgate hpos
    _ ≤ neutralNF661Quadratic B y := hmargin y
    _ = neutralNF661Quadratic H (T y) := hcongruence y

#print axioms neutralNF661PhysicalH_symm
#print axioms neutralNF661Coercivity_of_preconditioned

end
end WeilDefect
