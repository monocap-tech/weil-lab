import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF568 — GENERIC exact simultaneous finite root-count bound for
67 distinct real nodes with strictly positive multiplicities and
one distinct pole. Entirely independent of the historical NF407
source, odd-jet differentiation, and physical Gram. The source-
specific instantiation is separate.
-/

/-- Fundamental FINITE root budget: at 67 distinct real nodes and one
separate pole, the sum of lower bounds on root multiplicities cannot
exceed the degree of any nonzero real polynomial.

The positive m_g hypothesis forces each specified node into p.roots,
so the multiset root counts can be summed without double counting.
The pole is also a genuine root, and contributes one more count. -/
theorem neutralNF568Distinct67PlusPole_rootCountBound
    (p : Polynomial ℝ) (hp : p ≠ 0)
    (nodes : Fin 67 → ℝ) (hinj : Function.Injective nodes)
    (pole : ℝ) (hsep : ∀ g : Fin 67, nodes g ≠ pole)
    (m : Fin 67 → ℕ) (hmpos : ∀ g, 0 < m g)
    (hroots : ∀ g, m g ≤ Polynomial.rootMultiplicity (nodes g) p)
    (hpole : p.eval pole = 0) :
    (∑ g : Fin 67, m g) + 1 ≤ p.natDegree := by
  classical
  let s : Finset ℝ := Finset.univ.image nodes
  have hpole_not_mem : pole ∉ s := by
    intro hmem
    obtain ⟨g, _, heq⟩ := Finset.mem_image.mp hmem
    exact hsep g heq
  have hpole_mem_roots : pole ∈ p.roots :=
    (Polynomial.mem_roots hp).mpr hpole
  have hpole_count : 1 ≤ p.roots.count pole :=
    Multiset.count_pos.mpr hpole_mem_roots
  have hnodes_count (g : Fin 67) :
      m g ≤ p.roots.count (nodes g) := by
    simpa only [Polynomial.count_roots] using hroots g
  have hnodes_mem_roots (g : Fin 67) : nodes g ∈ p.roots := by
    apply Multiset.count_pos.mp
    exact lt_of_lt_of_le (hmpos g) (hnodes_count g)
  have hsubset : insert pole s ⊆ p.roots.toFinset := by
    intro x hx
    rcases Finset.mem_insert.mp hx with rfl | hx
    · exact Multiset.mem_toFinset.mpr hpole_mem_roots
    · obtain ⟨g, _, rfl⟩ := Finset.mem_image.mp hx
      exact Multiset.mem_toFinset.mpr (hnodes_mem_roots g)
  have hsum : (∑ g : Fin 67, m g) ≤
      ∑ g : Fin 67, p.roots.count (nodes g) :=
    Finset.sum_le_sum (fun g _ => hnodes_count g)
  calc
    (∑ g : Fin 67, m g) + 1 ≤
        (∑ g : Fin 67, p.roots.count (nodes g)) +
          p.roots.count pole :=
      Nat.add_le_add hsum hpole_count
    _ = ∑ x ∈ insert pole s, p.roots.count x := by
      rw [Finset.sum_insert hpole_not_mem]
      rw [Finset.sum_image hinj.injOn]
      omega
    _ ≤ ∑ x ∈ p.roots.toFinset, p.roots.count x := by
      apply Finset.sum_le_sum_of_subset_of_nonneg hsubset
      intro x hx hxnot
      exact Nat.zero_le _
    _ = p.roots.card :=
      Multiset.toFinset_sum_count_eq _
    _ ≤ p.natDegree :=
      Polynomial.card_roots' p

end
end WeilDefect
