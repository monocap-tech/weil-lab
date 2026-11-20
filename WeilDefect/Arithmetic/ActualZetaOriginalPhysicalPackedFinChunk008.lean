import Mathlib.Tactic

namespace WeilDefect

/-! NF725: independently compiled bounded original Fin 242 packing, block 8–16. This proves no numerical matrix identity. -/

/-- Finite packing interval [64, 128) with exact actual Fin 242 indices. -/
theorem neutralNF724Chunk008
    (P : Fin 242 → Prop)
    (h008 : ∀ k : Fin 8, P (⟨64 + k.val, by omega⟩ : Fin 242))
    (h009 : ∀ k : Fin 8, P (⟨72 + k.val, by omega⟩ : Fin 242))
    (h010 : ∀ k : Fin 8, P (⟨80 + k.val, by omega⟩ : Fin 242))
    (h011 : ∀ k : Fin 8, P (⟨88 + k.val, by omega⟩ : Fin 242))
    (h012 : ∀ k : Fin 8, P (⟨96 + k.val, by omega⟩ : Fin 242))
    (h013 : ∀ k : Fin 8, P (⟨104 + k.val, by omega⟩ : Fin 242))
    (h014 : ∀ k : Fin 8, P (⟨112 + k.val, by omega⟩ : Fin 242))
    (h015 : ∀ k : Fin 8, P (⟨120 + k.val, by omega⟩ : Fin 242))
    (i : Fin 242) (hlo : 64 ≤ i.val) (hhi : i.val < 128) : P i := by
  by_cases hi008 : i.val < 72
  · let k : Fin 8 := ⟨i.val - 64, by omega⟩
    have hk : (⟨64 + k.val, by omega⟩ : Fin 242) = i := by
      apply Fin.ext
      dsimp [k] <;> omega
    simpa only [hk] using h008 k
  ·
    by_cases hi009 : i.val < 80
    · let k : Fin 8 := ⟨i.val - 72, by omega⟩
      have hk : (⟨72 + k.val, by omega⟩ : Fin 242) = i := by
        apply Fin.ext
        dsimp [k] <;> omega
      simpa only [hk] using h009 k
    ·
      by_cases hi010 : i.val < 88
      · let k : Fin 8 := ⟨i.val - 80, by omega⟩
        have hk : (⟨80 + k.val, by omega⟩ : Fin 242) = i := by
          apply Fin.ext
          dsimp [k] <;> omega
        simpa only [hk] using h010 k
      ·
        by_cases hi011 : i.val < 96
        · let k : Fin 8 := ⟨i.val - 88, by omega⟩
          have hk : (⟨88 + k.val, by omega⟩ : Fin 242) = i := by
            apply Fin.ext
            dsimp [k] <;> omega
          simpa only [hk] using h011 k
        ·
          by_cases hi012 : i.val < 104
          · let k : Fin 8 := ⟨i.val - 96, by omega⟩
            have hk : (⟨96 + k.val, by omega⟩ : Fin 242) = i := by
              apply Fin.ext
              dsimp [k] <;> omega
            simpa only [hk] using h012 k
          ·
            by_cases hi013 : i.val < 112
            · let k : Fin 8 := ⟨i.val - 104, by omega⟩
              have hk : (⟨104 + k.val, by omega⟩ : Fin 242) = i := by
                apply Fin.ext
                dsimp [k] <;> omega
              simpa only [hk] using h013 k
            ·
              by_cases hi014 : i.val < 120
              · let k : Fin 8 := ⟨i.val - 112, by omega⟩
                have hk : (⟨112 + k.val, by omega⟩ : Fin 242) = i := by
                  apply Fin.ext
                  dsimp [k] <;> omega
                simpa only [hk] using h014 k
              ·
                let k : Fin 8 := ⟨i.val - 120, by omega⟩
                have hk : (⟨120 + k.val, by omega⟩ : Fin 242) = i := by
                  apply Fin.ext
                  dsimp [k] <;> omega
                simpa only [hk] using h015 k

#print axioms neutralNF724Chunk008

end WeilDefect
