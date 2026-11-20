import Mathlib.Tactic

namespace WeilDefect

/-! NF725: independently compiled bounded original Fin 242 packing, block 0–8. This proves no numerical matrix identity. -/

/-- Finite packing interval [0, 64) with exact actual Fin 242 indices. -/
theorem neutralNF724Chunk000
    (P : Fin 242 → Prop)
    (h000 : ∀ k : Fin 8, P (⟨k.val, by omega⟩ : Fin 242))
    (h001 : ∀ k : Fin 8, P (⟨8 + k.val, by omega⟩ : Fin 242))
    (h002 : ∀ k : Fin 8, P (⟨16 + k.val, by omega⟩ : Fin 242))
    (h003 : ∀ k : Fin 8, P (⟨24 + k.val, by omega⟩ : Fin 242))
    (h004 : ∀ k : Fin 8, P (⟨32 + k.val, by omega⟩ : Fin 242))
    (h005 : ∀ k : Fin 8, P (⟨40 + k.val, by omega⟩ : Fin 242))
    (h006 : ∀ k : Fin 8, P (⟨48 + k.val, by omega⟩ : Fin 242))
    (h007 : ∀ k : Fin 8, P (⟨56 + k.val, by omega⟩ : Fin 242))
    (i : Fin 242) (hlo : 0 ≤ i.val) (hhi : i.val < 64) : P i := by
  by_cases hi000 : i.val < 8
  · let k : Fin 8 := ⟨i.val, by omega⟩
    have hk : (⟨k.val, by omega⟩ : Fin 242) = i := by
      apply Fin.ext
      dsimp [k] <;> omega
    simpa only [hk] using h000 k
  ·
    by_cases hi001 : i.val < 16
    · let k : Fin 8 := ⟨i.val - 8, by omega⟩
      have hk : (⟨8 + k.val, by omega⟩ : Fin 242) = i := by
        apply Fin.ext
        dsimp [k] <;> omega
      simpa only [hk] using h001 k
    ·
      by_cases hi002 : i.val < 24
      · let k : Fin 8 := ⟨i.val - 16, by omega⟩
        have hk : (⟨16 + k.val, by omega⟩ : Fin 242) = i := by
          apply Fin.ext
          dsimp [k] <;> omega
        simpa only [hk] using h002 k
      ·
        by_cases hi003 : i.val < 32
        · let k : Fin 8 := ⟨i.val - 24, by omega⟩
          have hk : (⟨24 + k.val, by omega⟩ : Fin 242) = i := by
            apply Fin.ext
            dsimp [k] <;> omega
          simpa only [hk] using h003 k
        ·
          by_cases hi004 : i.val < 40
          · let k : Fin 8 := ⟨i.val - 32, by omega⟩
            have hk : (⟨32 + k.val, by omega⟩ : Fin 242) = i := by
              apply Fin.ext
              dsimp [k] <;> omega
            simpa only [hk] using h004 k
          ·
            by_cases hi005 : i.val < 48
            · let k : Fin 8 := ⟨i.val - 40, by omega⟩
              have hk : (⟨40 + k.val, by omega⟩ : Fin 242) = i := by
                apply Fin.ext
                dsimp [k] <;> omega
              simpa only [hk] using h005 k
            ·
              by_cases hi006 : i.val < 56
              · let k : Fin 8 := ⟨i.val - 48, by omega⟩
                have hk : (⟨48 + k.val, by omega⟩ : Fin 242) = i := by
                  apply Fin.ext
                  dsimp [k] <;> omega
                simpa only [hk] using h006 k
              ·
                let k : Fin 8 := ⟨i.val - 56, by omega⟩
                have hk : (⟨56 + k.val, by omega⟩ : Fin 242) = i := by
                  apply Fin.ext
                  dsimp [k] <;> omega
                simpa only [hk] using h007 k

#print axioms neutralNF724Chunk000

end WeilDefect
