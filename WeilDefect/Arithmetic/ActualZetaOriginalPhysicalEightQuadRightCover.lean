import Mathlib.Tactic

namespace WeilDefect

/-! NF730: source-independent exact Fin242 right-half binary-shard assembly.
Pure finite-index routing only; assumes four separately certified range predicates,
not any numerical HD/A product gate truth. -/

/-- Assemble four 32-coordinate original-position ranges into the right half. -/
theorem neutralNF730RightOfFourQuads
    (P : Fin 242 → Prop)
    (h016 : ∀ i : Fin 242, 128 ≤ i.val → i.val < 160 → P i)
    (h020 : ∀ i : Fin 242, 160 ≤ i.val → i.val < 192 → P i)
    (h024 : ∀ i : Fin 242, 192 ≤ i.val → i.val < 224 → P i)
    (h028 : ∀ i : Fin 242, 224 ≤ i.val → i.val < 242 → P i)
    (i : Fin 242) (hlo : 128 ≤ i.val) : P i := by
  by_cases h160 : i.val < 160
  · exact h016 i (by omega) h160
  ·
    by_cases h192 : i.val < 192
    · exact h020 i (by omega) h192
    ·
      by_cases h224 : i.val < 224
      · exact h024 i (by omega) h224
      ·
        exact h028 i (by omega) i.isLt

#print axioms neutralNF730RightOfFourQuads

end WeilDefect
