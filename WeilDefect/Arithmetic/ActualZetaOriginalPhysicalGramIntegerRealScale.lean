import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramRealIntervalTransport

namespace WeilDefect

/-!
NF663: exact integer-to-real scaling for the original compact Gram witness.

The original 64-digit entry enclosure has scale S; the integral-defined
matrix itself is never rounded or replaced. A rational preconditioner
K_int/S transforms centers and radii with denominator S^3.
The arithmetic statements below are source-independent and do not
assume positivity, invertibility, or any numerical matrix witness.
-/

noncomputable section
open Finset

def neutralNF663CenterInteger {n : ℕ}
    (K C : Fin n → Fin n → ℤ) (i j : Fin n) : ℤ :=
  ∑ p : Fin n, ∑ q : Fin n, K i p * K j q * C p q

def neutralNF663RadiusInteger {n : ℕ}
    (K E : Fin n → Fin n → ℤ) (i j : Fin n) : ℤ :=
  ∑ p : Fin n, ∑ q : Fin n, |K i p * K j q| * E p q

theorem neutralNF663CenterInteger_cast {n : ℕ}
    (K C : Fin n → Fin n → ℤ) (i j : Fin n) :
    (neutralNF663CenterInteger K C i j : ℝ) =
      ∑ p : Fin n, ∑ q : Fin n,
        (K i p : ℝ) * (K j q : ℝ) * (C p q : ℝ) := by
  simp only [neutralNF663CenterInteger, Int.cast_sum, Int.cast_mul]

theorem neutralNF663RadiusInteger_cast {n : ℕ}
    (K E : Fin n → Fin n → ℤ) (i j : Fin n) :
    (neutralNF663RadiusInteger K E i j : ℝ) =
      ∑ p : Fin n, ∑ q : Fin n,
        |(K i p : ℝ) * (K j q : ℝ)| * (E p q : ℝ) := by
  simp only [neutralNF663RadiusInteger, Int.cast_sum,
    Int.cast_mul, Int.cast_abs]

theorem neutralNF663Center_scale {n : ℕ}
    (K C : Fin n → Fin n → ℤ) (S : ℝ) (hS : S ≠ 0)
    (i j : Fin n) :
    neutralNF662Center
      (fun a b => (K a b : ℝ) / S)
      (fun a b => (C a b : ℝ) / S) i j =
      (neutralNF663CenterInteger K C i j : ℝ) / S ^ 3 := by
  unfold neutralNF662Center
  calc
    (∑ p : Fin n, ∑ q : Fin n,
      (K i p : ℝ) / S * ((K j q : ℝ) / S) * ((C p q : ℝ) / S)) =
        ∑ p : Fin n, ∑ q : Fin n,
          ((K i p : ℝ) * (K j q : ℝ) * (C p q : ℝ)) / S ^ 3 := by
      apply Finset.sum_congr rfl
      intro p _
      apply Finset.sum_congr rfl
      intro q _
      field_simp [hS]
      ring
    _ = (∑ p : Fin n, ∑ q : Fin n,
          (K i p : ℝ) * (K j q : ℝ) * (C p q : ℝ)) / S ^ 3 := by
      simp only [Finset.sum_div]
    _ = (neutralNF663CenterInteger K C i j : ℝ) / S ^ 3 := by
      rw [neutralNF663CenterInteger_cast]

theorem neutralNF663Radius_scale {n : ℕ}
    (K E : Fin n → Fin n → ℤ) (S : ℝ) (hS : 0 < S)
    (i j : Fin n) :
    neutralNF662Radius
      (fun a b => (K a b : ℝ) / S)
      (fun a b => (E a b : ℝ) / S) i j =
      (neutralNF663RadiusInteger K E i j : ℝ) / S ^ 3 := by
  unfold neutralNF662Radius
  calc
    (∑ p : Fin n, ∑ q : Fin n,
      |((K i p : ℝ) / S) * ((K j q : ℝ) / S)| *
        ((E p q : ℝ) / S)) =
        ∑ p : Fin n, ∑ q : Fin n,
          (|(K i p : ℝ) * (K j q : ℝ)| * (E p q : ℝ)) / S ^ 3 := by
      apply Finset.sum_congr rfl
      intro p _
      apply Finset.sum_congr rfl
      intro q _
      rw [abs_mul, abs_div, abs_div, abs_of_pos hS]
      rw [abs_mul]
      field_simp [ne_of_gt hS]
      ring
    _ = (∑ p : Fin n, ∑ q : Fin n,
          |(K i p : ℝ) * (K j q : ℝ)| * (E p q : ℝ)) / S ^ 3 := by
      simp only [Finset.sum_div]
    _ = (neutralNF663RadiusInteger K E i j : ℝ) / S ^ 3 := by
      rw [neutralNF663RadiusInteger_cast]

/-- The bridge from *actual real source entries* to the exact integer
transformed witness, with the correct cubic scale. -/
theorem neutralNF663ActualIntegerCongruence_enclosed {n : ℕ}
    (H : Fin n → Fin n → ℝ)
    (K C E : Fin n → Fin n → ℤ)
    (S : ℝ) (hS : 0 < S)
    (hSource : ∀ p q : Fin n,
      |H p q - (C p q : ℝ) / S| ≤ (E p q : ℝ) / S)
    (i j : Fin n) :
    |neutralNF662Congruence (fun a b => (K a b : ℝ) / S)
        H i j -
      (neutralNF663CenterInteger K C i j : ℝ) / S ^ 3| ≤
      (neutralNF663RadiusInteger K E i j : ℝ) / S ^ 3 := by
  have hb := neutralNF662ActualCongruence_enclosed
    H (fun a b => (C a b : ℝ) / S)
      (fun a b => (E a b : ℝ) / S)
      (fun a b => (K a b : ℝ) / S)
    hSource i j
  rw [neutralNF663Center_scale K C S (ne_of_gt hS) i j,
      neutralNF663Radius_scale K E S hS i j] at hb
  exact hb

#print axioms neutralNF663Center_scale
#print axioms neutralNF663Radius_scale
#print axioms neutralNF663ActualIntegerCongruence_enclosed

end
end WeilDefect
