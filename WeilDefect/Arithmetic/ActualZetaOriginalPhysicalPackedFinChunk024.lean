import Mathlib.Tactic

namespace WeilDefect

/-! NF725: independently compiled bounded original Fin 242 packing, block 24–31. This proves no numerical matrix identity. -/

/-- Finite packing interval [192, 242) with exact actual Fin 242 indices. -/
theorem neutralNF724Chunk024
    (P : Fin 242 → Prop)
    (h024 : ∀ k : Fin 8, P (⟨192 + k.val, by omega⟩ : Fin 242))
    (h025 : ∀ k : Fin 8, P (⟨200 + k.val, by omega⟩ : Fin 242))
    (h026 : ∀ k : Fin 8, P (⟨208 + k.val, by omega⟩ : Fin 242))
    (h027 : ∀ k : Fin 8, P (⟨216 + k.val, by omega⟩ : Fin 242))
    (h028 : ∀ k : Fin 8, P (⟨224 + k.val, by omega⟩ : Fin 242))
    (h029 : ∀ k : Fin 8, P (⟨232 + k.val, by omega⟩ : Fin 242))
    (h030 : ∀ k : Fin 2, P (⟨240 + k.val, by omega⟩ : Fin 242))
    (i : Fin 242) (hlo : 192 ≤ i.val) (hhi : i.val < 242) : P i := by
  by_cases hi024 : i.val < 200
  · let k : Fin 8 := ⟨i.val - 192, by omega⟩
    have hk : (⟨192 + k.val, by omega⟩ : Fin 242) = i := by
      apply Fin.ext
      dsimp [k] <;> omega
    simpa only [hk] using h024 k
  ·
    by_cases hi025 : i.val < 208
    · let k : Fin 8 := ⟨i.val - 200, by omega⟩
      have hk : (⟨200 + k.val, by omega⟩ : Fin 242) = i := by
        apply Fin.ext
        dsimp [k] <;> omega
      simpa only [hk] using h025 k
    ·
      by_cases hi026 : i.val < 216
      · let k : Fin 8 := ⟨i.val - 208, by omega⟩
        have hk : (⟨208 + k.val, by omega⟩ : Fin 242) = i := by
          apply Fin.ext
          dsimp [k] <;> omega
        simpa only [hk] using h026 k
      ·
        by_cases hi027 : i.val < 224
        · let k : Fin 8 := ⟨i.val - 216, by omega⟩
          have hk : (⟨216 + k.val, by omega⟩ : Fin 242) = i := by
            apply Fin.ext
            dsimp [k] <;> omega
          simpa only [hk] using h027 k
        ·
          by_cases hi028 : i.val < 232
          · let k : Fin 8 := ⟨i.val - 224, by omega⟩
            have hk : (⟨224 + k.val, by omega⟩ : Fin 242) = i := by
              apply Fin.ext
              dsimp [k] <;> omega
            simpa only [hk] using h028 k
          ·
            by_cases hi029 : i.val < 240
            · let k : Fin 8 := ⟨i.val - 232, by omega⟩
              have hk : (⟨232 + k.val, by omega⟩ : Fin 242) = i := by
                apply Fin.ext
                dsimp [k] <;> omega
              simpa only [hk] using h029 k
            ·
              let k : Fin 2 := ⟨i.val - 240, by omega⟩
              have hk : (⟨240 + k.val, by omega⟩ : Fin 242) = i := by
                apply Fin.ext
                dsimp [k] <;> omega
              simpa only [hk] using h030 k

#print axioms neutralNF724Chunk024

end WeilDefect
