import Mathlib.Tactic

namespace WeilDefect

/-! NF730: source-independent exact Fin242 left-half binary-shard assembly.
Pure finite-index routing only; assumes four separately certified range predicates,
not any numerical HD/A product gate truth. -/

/-- Assemble four 32-coordinate original-position ranges into the left half. -/
theorem neutralNF730LeftOfFourQuads
    (P : Fin 242 → Prop)
    (h000 : ∀ i : Fin 242, 0 ≤ i.val → i.val < 32 → P i)
    (h004 : ∀ i : Fin 242, 32 ≤ i.val → i.val < 64 → P i)
    (h008 : ∀ i : Fin 242, 64 ≤ i.val → i.val < 96 → P i)
    (h012 : ∀ i : Fin 242, 96 ≤ i.val → i.val < 128 → P i)
    (i : Fin 242) (hi : i.val < 128) : P i := by
  by_cases h32 : i.val < 32
  · exact h000 i (by omega) h32
  ·
    by_cases h64 : i.val < 64
    · exact h004 i (by omega) h64
    ·
      by_cases h96 : i.val < 96
      · exact h008 i (by omega) h96
      ·
        exact h012 i (by omega) hi

#print axioms neutralNF730LeftOfFourQuads

end WeilDefect
