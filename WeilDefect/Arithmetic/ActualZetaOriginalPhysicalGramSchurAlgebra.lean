import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramCoercivityClosure

namespace WeilDefect

/-!
NF669: exact finite Schur-completion identity, independent of the
particular original source matrix. The original A block is certified
coercive by NF665. The remaining genuinely source-dependent gates
are the cross-block Riesz response and nonnegative 227-source Schur
remainder; neither is silently assumed to hold for the physical H.
-/

noncomputable section
open Finset

def neutralNF669Bilinear {n : ℕ}
    (A : Fin n → Fin n → ℝ)
    (x u : Fin n → ℝ) : ℝ :=
  ∑ i : Fin n, ∑ j : Fin n, A i j * x i * u j

def neutralNF669Mixed {n m : ℕ}
    (B : Fin n → Fin m → ℝ)
    (x : Fin n → ℝ) (y : Fin m → ℝ) : ℝ :=
  ∑ i : Fin n, ∑ j : Fin m, B i j * x i * y j

def neutralNF669BlockEnergy {n m : ℕ}
    (A : Fin n → Fin n → ℝ)
    (B : Fin n → Fin m → ℝ)
    (C : Fin m → Fin m → ℝ)
    (x : Fin n → ℝ) (y : Fin m → ℝ) : ℝ :=
  neutralNF661Quadratic A x +
    2 * neutralNF669Mixed B x y +
    neutralNF661Quadratic C y

theorem neutralNF669Bilinear_add_left {n : ℕ}
    (A : Fin n → Fin n → ℝ)
    (x u v : Fin n → ℝ) :
    neutralNF669Bilinear A (fun i => x i + u i) v =
      neutralNF669Bilinear A x v +
        neutralNF669Bilinear A u v := by
  unfold neutralNF669Bilinear
  calc
    (∑ i : Fin n, ∑ j : Fin n,
      A i j * (x i + u i) * v j) =
      ∑ i : Fin n, ∑ j : Fin n,
        (A i j * x i * v j + A i j * u i * v j) := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      ring
    _ = (∑ i : Fin n, ∑ j : Fin n, A i j * x i * v j) +
        (∑ i : Fin n, ∑ j : Fin n, A i j * u i * v j) := by
      simp only [Finset.sum_add_distrib]

theorem neutralNF669Bilinear_add_right {n : ℕ}
    (A : Fin n → Fin n → ℝ)
    (x u v : Fin n → ℝ) :
    neutralNF669Bilinear A x (fun j => u j + v j) =
      neutralNF669Bilinear A x u +
        neutralNF669Bilinear A x v := by
  unfold neutralNF669Bilinear
  calc
    (∑ i : Fin n, ∑ j : Fin n,
      A i j * x i * (u j + v j)) =
      ∑ i : Fin n, ∑ j : Fin n,
        (A i j * x i * u j + A i j * x i * v j) := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      ring
    _ = (∑ i : Fin n, ∑ j : Fin n, A i j * x i * u j) +
        (∑ i : Fin n, ∑ j : Fin n, A i j * x i * v j) := by
      simp only [Finset.sum_add_distrib]

theorem neutralNF669Bilinear_symm {n : ℕ}
    (A : Fin n → Fin n → ℝ)
    (hSym : ∀ i j, A i j = A j i)
    (x u : Fin n → ℝ) :
    neutralNF669Bilinear A x u =
      neutralNF669Bilinear A u x := by
  unfold neutralNF669Bilinear
  calc
    (∑ i : Fin n, ∑ j : Fin n, A i j * x i * u j) =
      ∑ j : Fin n, ∑ i : Fin n, A i j * x i * u j :=
      Finset.sum_comm
    _ = ∑ j : Fin n, ∑ i : Fin n, A j i * u j * x i := by
      apply Finset.sum_congr rfl
      intro j _
      apply Finset.sum_congr rfl
      intro i _
      rw [hSym i j]
      ring
    _ = ∑ i : Fin n, ∑ j : Fin n, A i j * u i * x j := rfl

theorem neutralNF669Quadratic_add {n : ℕ}
    (A : Fin n → Fin n → ℝ)
    (hSym : ∀ i j, A i j = A j i)
    (x u : Fin n → ℝ) :
    neutralNF661Quadratic A (fun i => x i + u i) =
      neutralNF661Quadratic A x +
        2 * neutralNF669Bilinear A x u +
        neutralNF661Quadratic A u := by
  change
    neutralNF669Bilinear A (fun i => x i + u i)
      (fun i => x i + u i) =
    neutralNF669Bilinear A x x +
      2 * neutralNF669Bilinear A x u +
      neutralNF669Bilinear A u u
  calc
    neutralNF669Bilinear A (fun i => x i + u i)
      (fun i => x i + u i) =
      neutralNF669Bilinear A x (fun i => x i + u i) +
        neutralNF669Bilinear A u (fun i => x i + u i) :=
      neutralNF669Bilinear_add_left A x u _
    _ = (neutralNF669Bilinear A x x +
          neutralNF669Bilinear A x u) +
        (neutralNF669Bilinear A u x +
          neutralNF669Bilinear A u u) := by
      rw [neutralNF669Bilinear_add_right A x x u,
        neutralNF669Bilinear_add_right A u x u]
    _ = neutralNF669Bilinear A x x +
          2 * neutralNF669Bilinear A x u +
          neutralNF669Bilinear A u u := by
      rw [neutralNF669Bilinear_symm A hSym u x]
      ring

/-- Exact Schur square completion given an authentic Riesz response U
for the B cross block. Establishing the response is a separate gate. -/
theorem neutralNF669Schur_completion {n m : ℕ}
    (A : Fin n → Fin n → ℝ)
    (B : Fin n → Fin m → ℝ)
    (C : Fin m → Fin m → ℝ)
    (hSym : ∀ i j, A i j = A j i)
    (U : (Fin m → ℝ) → (Fin n → ℝ))
    (hResponse : ∀ x y,
      neutralNF669Mixed B x y = neutralNF669Bilinear A x (U y))
    (x : Fin n → ℝ) (y : Fin m → ℝ) :
    neutralNF669BlockEnergy A B C x y =
      neutralNF661Quadratic A (fun i => x i + U y i) +
        (neutralNF661Quadratic C y -
          neutralNF661Quadratic A (U y)) := by
  have hs := neutralNF669Quadratic_add A hSym x (U y)
  unfold neutralNF669BlockEnergy
  rw [hResponse x y]
  linarith

/-- The exact sufficient Schur gate: once A is already certified
nonnegative, the *remaining* gate is only the cofinite Schur energy.
No numeric/complement positivity claim is introduced here. -/
theorem neutralNF669Schur_sufficient {n m : ℕ}
    (A : Fin n → Fin n → ℝ)
    (B : Fin n → Fin m → ℝ)
    (C : Fin m → Fin m → ℝ)
    (hSym : ∀ i j, A i j = A j i)
    (U : (Fin m → ℝ) → (Fin n → ℝ))
    (hResponse : ∀ x y,
      neutralNF669Mixed B x y = neutralNF669Bilinear A x (U y))
    (hA : ∀ x, 0 ≤ neutralNF661Quadratic A x)
    (hSchur : ∀ y, 0 ≤
      neutralNF661Quadratic C y -
        neutralNF661Quadratic A (U y))
    (x : Fin n → ℝ) (y : Fin m → ℝ) :
    0 ≤ neutralNF669BlockEnergy A B C x y := by
  rw [neutralNF669Schur_completion A B C hSym U hResponse x y]
  exact add_nonneg (hA _) (hSchur y)

/-- Conversely, full block positivity forces the cofinite Schur
energy to be nonnegative. This is the precise mathematical gate
remaining after the original selected 15-source certification. -/
theorem neutralNF669Schur_necessary {n m : ℕ}
    (A : Fin n → Fin n → ℝ)
    (B : Fin n → Fin m → ℝ)
    (C : Fin m → Fin m → ℝ)
    (hSym : ∀ i j, A i j = A j i)
    (U : (Fin m → ℝ) → (Fin n → ℝ))
    (hResponse : ∀ x y,
      neutralNF669Mixed B x y = neutralNF669Bilinear A x (U y))
    (hFull : ∀ x y, 0 ≤ neutralNF669BlockEnergy A B C x y)
    (y : Fin m → ℝ) :
    0 ≤ neutralNF661Quadratic C y -
      neutralNF661Quadratic A (U y) := by
  have h := hFull (fun i => -(U y i)) y
  rw [neutralNF669Schur_completion A B C hSym U hResponse] at h
  have hzero :
      (fun i : Fin n => -(U y i) + U y i) =
        (fun _ => (0 : ℝ)) := by
    funext i
    ring
  rw [hzero] at h
  have hz :
      neutralNF661Quadratic A (fun _ => (0 : ℝ)) = 0 := by
    simp [neutralNF661Quadratic]
  rw [hz, zero_add] at h
  exact h

#print axioms neutralNF669Bilinear_add_left
#print axioms neutralNF669Bilinear_add_right
#print axioms neutralNF669Bilinear_symm
#print axioms neutralNF669Quadratic_add
#print axioms neutralNF669Schur_completion
#print axioms neutralNF669Schur_sufficient
#print axioms neutralNF669Schur_necessary

end
end WeilDefect
