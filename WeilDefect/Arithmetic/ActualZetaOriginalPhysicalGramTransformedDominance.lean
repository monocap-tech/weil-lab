import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramDominanceTransfer
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramRealIntervalTransport

namespace WeilDefect

/-!
NF664: turn exact integer row-dominance margins into coercivity for the
ACTUAL congruence-transformed original 15-generator physical Gram matrix.

There is no positivity axiom: the endpoint theorem consumes an explicit
real entry interval proof and explicit integer margin inequalities.
Those premises are to be discharged by NF663/NF659 source certificates.
-/

noncomputable section
open Finset

theorem neutralNF664Congruence_symm {n : ℕ}
    (K H : Fin n → Fin n → ℝ)
    (hH : ∀ p q, H p q = H q p)
    (i j : Fin n) :
    neutralNF662Congruence K H i j =
      neutralNF662Congruence K H j i := by
  unfold neutralNF662Congruence
  calc
    (∑ p : Fin n, ∑ q : Fin n, K i p * K j q * H p q) =
      ∑ q : Fin n, ∑ p : Fin n, K i p * K j q * H p q :=
        Finset.sum_comm
    _ = ∑ q : Fin n, ∑ p : Fin n, K j q * K i p * H q p := by
      apply Finset.sum_congr rfl
      intro q _
      apply Finset.sum_congr rfl
      intro p _
      rw [hH p q]
      ring
    _ = ∑ p : Fin n, ∑ q : Fin n, K j p * K i q * H p q := rfl

def neutralNF664ActualPhysicalB
    (K : Fin 15 → Fin 15 → ℝ) (i j : Fin 15) : ℝ :=
  neutralNF662Congruence K neutralNF661PhysicalH i j

theorem neutralNF664ActualPhysicalB_symm
    (K : Fin 15 → Fin 15 → ℝ) (i j : Fin 15) :
    neutralNF664ActualPhysicalB K i j =
      neutralNF664ActualPhysicalB K j i :=
  neutralNF664Congruence_symm K neutralNF661PhysicalH
    neutralNF661PhysicalH_symm i j

theorem neutralNF664ScaledRowMargin
    {n : ℕ} (T U : Fin n → Fin n → ℤ)
    (denom : ℝ) (hd : 0 < denom) (m : ℤ)
    (hm : ∀ i : Fin n,
      m ≤ T i i - U i i -
        ∑ j : Fin n, if i = j then (0 : ℤ)
          else |T i j| + U i j) :
    ∀ i : Fin n,
      (m : ℝ) / denom ≤
        (T i i : ℝ) / denom - (U i i : ℝ) / denom -
        ∑ j : Fin n, if i = j then (0 : ℝ)
          else |(T i j : ℝ) / denom| + (U i j : ℝ) / denom := by
  classical
  intro i
  have hs (j : Fin n) :
      (if i = j then (0 : ℝ) else
        |(T i j : ℝ) / denom| + (U i j : ℝ) / denom) =
      ((if i = j then (0 : ℤ) else |T i j| + U i j : ℤ) : ℝ) / denom := by
    by_cases hij : i = j
    · simp [hij]
    · simp only [if_neg hij, Int.cast_add, Int.cast_abs]
      rw [abs_div, abs_of_pos hd]
      ring
  have hcast :
      (m : ℝ) ≤ (T i i : ℝ) - (U i i : ℝ) -
        ∑ j : Fin n,
          ((if i = j then (0 : ℤ) else |T i j| + U i j : ℤ) : ℝ) := by
    exact_mod_cast hm i
  have hdiv := (div_le_div_of_nonneg_right hcast hd.le)
  have hrewrite :
      ((T i i : ℝ) - (U i i : ℝ) -
        ∑ j : Fin n,
          ((if i = j then (0 : ℤ) else |T i j| + U i j : ℤ) : ℝ)) / denom =
      (T i i : ℝ) / denom - (U i i : ℝ) / denom -
        ∑ j : Fin n,
          (if i = j then (0 : ℝ) else
            |(T i j : ℝ) / denom| + (U i j : ℝ) / denom) := by
    rw [sub_div, sub_div, Finset.sum_div]
    congr 1
    apply Finset.sum_congr rfl
    intro j _
    exact (hs j).symm
  rw [hrewrite] at hdiv
  exact hdiv

/-- Actual physical transformed coercivity from the exact integer
margin witness, *conditional solely on authentic real interval custody*. -/
theorem neutralNF664PhysicalTransformed_coercivity
    (K : Fin 15 → Fin 15 → ℝ)
    (T U : Fin 15 → Fin 15 → ℤ)
    (denom : ℝ) (hd : 0 < denom) (m : ℤ)
    (hReal : ∀ i j : Fin 15,
      |neutralNF664ActualPhysicalB K i j -
        (T i j : ℝ) / denom| ≤
          (U i j : ℝ) / denom)
    (hMargin : ∀ i : Fin 15,
      m ≤ T i i - U i i -
        ∑ j : Fin 15, if i = j then (0 : ℤ)
          else |T i j| + U i j)
    (y : Fin 15 → ℝ) :
    ((m : ℝ) / denom) * neutralNF661SqNorm y ≤
      neutralNF661Quadratic (neutralNF664ActualPhysicalB K) y := by
  have hRows := neutralNF664ScaledRowMargin T U denom hd m hMargin
  exact neutralNF660Interval_coercivity
    (neutralNF664ActualPhysicalB K)
    (fun i j => (T i j : ℝ) / denom)
    (fun i j => (U i j : ℝ) / denom)
    (neutralNF664ActualPhysicalB_symm K)
    hReal ((m : ℝ) / denom) hRows y

#print axioms neutralNF664Congruence_symm
#print axioms neutralNF664ScaledRowMargin
#print axioms neutralNF664PhysicalTransformed_coercivity

end
end WeilDefect
