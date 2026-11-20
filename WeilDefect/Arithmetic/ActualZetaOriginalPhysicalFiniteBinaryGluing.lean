import Mathlib.Tactic

namespace WeilDefect

/-!
NF727: source-independent binary finite-index gluing at physical size 242.

The first source family handles positions 0..127 and the second 128..241.
This theorem has only TWO proof premises rather than the 31 original packed
source-bound numeric certificate families. It is intentionally general:
neither the original matrix nor any numerical gate truth is asserted here.

The completed original numeric theorem will require actual kernel-accepted
left/right gate families, not merely a successful abstract implication.
-/

/-- Exactly combine independently checked original 128- and 114-coordinate
    half-range hypotheses. No new numerical or analytic assumption. -/
theorem neutralNF727Fin242OfTwoHalves
    (P : Fin 242 → Prop)
    (left : ∀ i : Fin 242, i.val < 128 → P i)
    (right : ∀ i : Fin 242, 128 ≤ i.val → P i)
    : ∀ i : Fin 242, P i := by
  intro i
  by_cases h : i.val < 128
  · exact left i h
  · exact right i (Nat.le_of_not_gt h)

/-- Combine a pair of separate proposition families, corresponding to the
    original HD row-one and A column-one global product-gate predicates,
    once each has its two *actual* source-specific half certificates. -/
theorem neutralNF727PairFin242OfTwoHalves
    (HD A : Fin 242 → Prop)
    (hdLeft : ∀ i : Fin 242, i.val < 128 → HD i)
    (hdRight : ∀ i : Fin 242, 128 ≤ i.val → HD i)
    (aLeft : ∀ i : Fin 242, i.val < 128 → A i)
    (aRight : ∀ i : Fin 242, 128 ≤ i.val → A i)
    : (∀ i : Fin 242, HD i) ∧ (∀ i : Fin 242, A i) := by
  exact ⟨neutralNF727Fin242OfTwoHalves HD hdLeft hdRight,
    neutralNF727Fin242OfTwoHalves A aLeft aRight⟩

#print axioms neutralNF727Fin242OfTwoHalves
#print axioms neutralNF727PairFin242OfTwoHalves

end WeilDefect
