import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramCoercivityClosure
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramCongruenceInterval

namespace WeilDefect

/-!
NF662: source-independent real interval attachment through a full
finite congruence, with explicit recovery of the upper triangle.
No numerical center/radius or positivity claim is assumed by definition.
-/

noncomputable section
open Finset

/-- A lower-triangular set of real interval proofs suffices for a
symmetric actual matrix and symmetric numerical center and radius. -/
theorem neutralNF662SymmetricLower_to_full
    {n : ℕ} (H C E : Fin n → Fin n → ℝ)
    (hH : ∀ i j, H i j = H j i)
    (hC : ∀ i j, C i j = C j i)
    (hE : ∀ i j, E i j = E j i)
    (hLower : ∀ i j, j.val ≤ i.val →
      |H i j - C i j| ≤ E i j) :
    ∀ i j, |H i j - C i j| ≤ E i j := by
  intro i j
  by_cases hij : j.val ≤ i.val
  · exact hLower i j hij
  · have hji : i.val ≤ j.val := by omega
    have hb := hLower j i hji
    rw [← hH i j, ← hC i j, ← hE i j] at hb
    exact hb

/-- For the original physical integral-defined block, the symmetry
hypothesis is already a certified theorem of NF606/NF661. -/
theorem neutralNF662OriginalPhysicalLower_to_full
    (C E : Fin 15 → Fin 15 → ℝ)
    (hC : ∀ i j, C i j = C j i)
    (hE : ∀ i j, E i j = E j i)
    (hLower : ∀ i j, j.val ≤ i.val →
      |neutralNF661PhysicalH i j - C i j| ≤ E i j) :
    ∀ i j, |neutralNF661PhysicalH i j - C i j| ≤ E i j := by
  exact neutralNF662SymmetricLower_to_full
    neutralNF661PhysicalH C E neutralNF661PhysicalH_symm hC hE hLower

/-- The actual real transformed entry. In particular, H can be the
original integral matrix, not a numerically substituted matrix. -/
def neutralNF662Congruence {n : ℕ}
    (K H : Fin n → Fin n → ℝ) (i j : Fin n) : ℝ :=
  ∑ p : Fin n, ∑ q : Fin n, K i p * K j q * H p q

/-- The unrounded center induced by congruence. -/
def neutralNF662Center {n : ℕ}
    (K C : Fin n → Fin n → ℝ) (i j : Fin n) : ℝ :=
  ∑ p : Fin n, ∑ q : Fin n, K i p * K j q * C p q

/-- Absolute-value propagation of entrywise radii. -/
def neutralNF662Radius {n : ℕ}
    (K E : Fin n → Fin n → ℝ) (i j : Fin n) : ℝ :=
  ∑ p : Fin n, ∑ q : Fin n, |K i p * K j q| * E p q

theorem neutralNF662ActualCongruence_enclosed
    {n : ℕ} (H C E K : Fin n → Fin n → ℝ)
    (h : ∀ i j, |H i j - C i j| ≤ E i j)
    (i j : Fin n) :
    |neutralNF662Congruence K H i j -
      neutralNF662Center K C i j| ≤
        neutralNF662Radius K E i j := by
  exact neutralNF659CongruenceEntry_bound H C E K h i j

/-- Directly compose the original real physical lower-triangle intervals
with the previously certified generic congruence inequality. -/
theorem neutralNF662OriginalPhysicalCongruence_enclosed
    (C E K : Fin 15 → Fin 15 → ℝ)
    (hC : ∀ i j, C i j = C j i)
    (hE : ∀ i j, E i j = E j i)
    (hLower : ∀ i j, j.val ≤ i.val →
      |neutralNF661PhysicalH i j - C i j| ≤ E i j)
    (i j : Fin 15) :
    |neutralNF662Congruence K neutralNF661PhysicalH i j -
      neutralNF662Center K C i j| ≤
        neutralNF662Radius K E i j := by
  exact neutralNF662ActualCongruence_enclosed
    neutralNF661PhysicalH C E K
    (neutralNF662OriginalPhysicalLower_to_full C E hC hE hLower) i j

#print axioms neutralNF662OriginalPhysicalLower_to_full
#print axioms neutralNF662OriginalPhysicalCongruence_enclosed

end
end WeilDefect
