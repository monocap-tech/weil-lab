import Mathlib.Tactic

namespace WeilDefect

/-! NF725: independently compiled bounded original Fin 242 packing, block 16–24. This proves no numerical matrix identity. -/

/-- Finite packing interval [128, 192) with exact actual Fin 242 indices. -/
theorem neutralNF724Chunk016
    (P : Fin 242 → Prop)
    (h016 : ∀ k : Fin 8, P (⟨128 + k.val, by omega⟩ : Fin 242))
    (h017 : ∀ k : Fin 8, P (⟨136 + k.val, by omega⟩ : Fin 242))
    (h018 : ∀ k : Fin 8, P (⟨144 + k.val, by omega⟩ : Fin 242))
    (h019 : ∀ k : Fin 8, P (⟨152 + k.val, by omega⟩ : Fin 242))
    (h020 : ∀ k : Fin 8, P (⟨160 + k.val, by omega⟩ : Fin 242))
    (h021 : ∀ k : Fin 8, P (⟨168 + k.val, by omega⟩ : Fin 242))
    (h022 : ∀ k : Fin 8, P (⟨176 + k.val, by omega⟩ : Fin 242))
    (h023 : ∀ k : Fin 8, P (⟨184 + k.val, by omega⟩ : Fin 242))
    (i : Fin 242) (hlo : 128 ≤ i.val) (hhi : i.val < 192) : P i := by
  by_cases hi016 : i.val < 136
  · let k : Fin 8 := ⟨i.val - 128, by omega⟩
    have hk : (⟨128 + k.val, by omega⟩ : Fin 242) = i := by
      apply Fin.ext
      dsimp [k] <;> omega
    simpa only [hk] using h016 k
  ·
    by_cases hi017 : i.val < 144
    · let k : Fin 8 := ⟨i.val - 136, by omega⟩
      have hk : (⟨136 + k.val, by omega⟩ : Fin 242) = i := by
        apply Fin.ext
        dsimp [k] <;> omega
      simpa only [hk] using h017 k
    ·
      by_cases hi018 : i.val < 152
      · let k : Fin 8 := ⟨i.val - 144, by omega⟩
        have hk : (⟨144 + k.val, by omega⟩ : Fin 242) = i := by
          apply Fin.ext
          dsimp [k] <;> omega
        simpa only [hk] using h018 k
      ·
        by_cases hi019 : i.val < 160
        · let k : Fin 8 := ⟨i.val - 152, by omega⟩
          have hk : (⟨152 + k.val, by omega⟩ : Fin 242) = i := by
            apply Fin.ext
            dsimp [k] <;> omega
          simpa only [hk] using h019 k
        ·
          by_cases hi020 : i.val < 168
          · let k : Fin 8 := ⟨i.val - 160, by omega⟩
            have hk : (⟨160 + k.val, by omega⟩ : Fin 242) = i := by
              apply Fin.ext
              dsimp [k] <;> omega
            simpa only [hk] using h020 k
          ·
            by_cases hi021 : i.val < 176
            · let k : Fin 8 := ⟨i.val - 168, by omega⟩
              have hk : (⟨168 + k.val, by omega⟩ : Fin 242) = i := by
                apply Fin.ext
                dsimp [k] <;> omega
              simpa only [hk] using h021 k
            ·
              by_cases hi022 : i.val < 184
              · let k : Fin 8 := ⟨i.val - 176, by omega⟩
                have hk : (⟨176 + k.val, by omega⟩ : Fin 242) = i := by
                  apply Fin.ext
                  dsimp [k] <;> omega
                simpa only [hk] using h022 k
              ·
                let k : Fin 8 := ⟨i.val - 184, by omega⟩
                have hk : (⟨184 + k.val, by omega⟩ : Fin 242) = i := by
                  apply Fin.ext
                  dsimp [k] <;> omega
                simpa only [hk] using h023 k

#print axioms neutralNF724Chunk016

end WeilDefect
