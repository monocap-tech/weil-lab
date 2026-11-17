import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF565 — the exact no-degree-room theorem for simultaneous
DISTINCT REAL ROOTS WITH PRESCRIBED MULTIPLICITIES.

Unlike the one-root obstruction and the generic degree divisor
theorem from NF553, this theorem assembles ALL simultaneous
distinct root multiplicity demands into one finite budget, using
Mathlib's genuine polynomial root multiset (not a numerical
determinant or simulated node list).

Later source-specific instantiation uses the original 67 positive
squared oscillators (sum multiplicity 241) plus the true distinct
negative sinh-pole node -1/4 (multiplicity 1), total 242.
-/

/-- Any finite collection of distinct real nodes with formal
root multiplicity demands exceeding the polynomial's degree
forces the polynomial to vanish identically.

The Finset enforces distinctness of nodes by construction.
The proof uses the actual multiset of all roots counted with
multiplicity and Mathlib's card_roots' theorem. This is the
generic LAST algebraic gate, and is not an assumption about
the original source's 68 nodes. -/
theorem neutralNF565FiniteDistinctRootMultiplicityDegreeStop
    (p : Polynomial ℝ) (s : Finset ℝ) (m : ℝ → ℕ)
    (hroot : ∀ x ∈ s, m x ≤ rootMultiplicity x p)
    (hbudget : p.natDegree < ∑ x ∈ s, m x) :
    p = 0 := by
  classical
  by_contra hp
  let u : Finset ℝ := s ∪ p.roots.toFinset
  have hcount :
      (∑ x ∈ s, p.roots.count x) ≤ p.roots.card := by
    calc
      (∑ x ∈ s, p.roots.count x) ≤
          ∑ x ∈ u, p.roots.count x := by
            apply Finset.sum_le_sum_of_subset_of_nonneg
            · exact Finset.subset_union_left
            · intro x hx hxnot
              exact Nat.zero_le _
      _ = p.roots.card := by
        apply Multiset.sum_count_eq_card
        intro x hx
        exact Finset.mem_union_right s
          (Multiset.mem_toFinset.mpr hx)
  have hdemand :
      (∑ x ∈ s, m x) ≤
        (∑ x ∈ s, p.roots.count x) := by
    apply Finset.sum_le_sum
    intro x hx
    simpa only [Polynomial.count_roots] using hroot x hx
  have hdegree := Polynomial.card_roots' p
  omega

end
end WeilDefect
