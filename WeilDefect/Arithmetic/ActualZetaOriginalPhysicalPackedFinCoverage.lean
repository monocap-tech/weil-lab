import Mathlib.Tactic

namespace WeilDefect

/-! NF724: split exact Fin 242 packed coordinate coverage into four bounded
pure finite-arithmetic proofs. These do not use the original matrix cache.
Thirty Fin 8 blocks and one final Fin 2 block exactly partition 0..241.
Original NF722 remains the stable public assembly interface. -/

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

/-- Global coverage by four disjoint, bounded finite-arithmetic packets. -/
theorem neutralNF724Fin242OfPackedBlocks
    (P : Fin 242 → Prop)
    (h000 : ∀ k : Fin 8, P (⟨k.val, by omega⟩ : Fin 242))
    (h001 : ∀ k : Fin 8, P (⟨8 + k.val, by omega⟩ : Fin 242))
    (h002 : ∀ k : Fin 8, P (⟨16 + k.val, by omega⟩ : Fin 242))
    (h003 : ∀ k : Fin 8, P (⟨24 + k.val, by omega⟩ : Fin 242))
    (h004 : ∀ k : Fin 8, P (⟨32 + k.val, by omega⟩ : Fin 242))
    (h005 : ∀ k : Fin 8, P (⟨40 + k.val, by omega⟩ : Fin 242))
    (h006 : ∀ k : Fin 8, P (⟨48 + k.val, by omega⟩ : Fin 242))
    (h007 : ∀ k : Fin 8, P (⟨56 + k.val, by omega⟩ : Fin 242))
    (h008 : ∀ k : Fin 8, P (⟨64 + k.val, by omega⟩ : Fin 242))
    (h009 : ∀ k : Fin 8, P (⟨72 + k.val, by omega⟩ : Fin 242))
    (h010 : ∀ k : Fin 8, P (⟨80 + k.val, by omega⟩ : Fin 242))
    (h011 : ∀ k : Fin 8, P (⟨88 + k.val, by omega⟩ : Fin 242))
    (h012 : ∀ k : Fin 8, P (⟨96 + k.val, by omega⟩ : Fin 242))
    (h013 : ∀ k : Fin 8, P (⟨104 + k.val, by omega⟩ : Fin 242))
    (h014 : ∀ k : Fin 8, P (⟨112 + k.val, by omega⟩ : Fin 242))
    (h015 : ∀ k : Fin 8, P (⟨120 + k.val, by omega⟩ : Fin 242))
    (h016 : ∀ k : Fin 8, P (⟨128 + k.val, by omega⟩ : Fin 242))
    (h017 : ∀ k : Fin 8, P (⟨136 + k.val, by omega⟩ : Fin 242))
    (h018 : ∀ k : Fin 8, P (⟨144 + k.val, by omega⟩ : Fin 242))
    (h019 : ∀ k : Fin 8, P (⟨152 + k.val, by omega⟩ : Fin 242))
    (h020 : ∀ k : Fin 8, P (⟨160 + k.val, by omega⟩ : Fin 242))
    (h021 : ∀ k : Fin 8, P (⟨168 + k.val, by omega⟩ : Fin 242))
    (h022 : ∀ k : Fin 8, P (⟨176 + k.val, by omega⟩ : Fin 242))
    (h023 : ∀ k : Fin 8, P (⟨184 + k.val, by omega⟩ : Fin 242))
    (h024 : ∀ k : Fin 8, P (⟨192 + k.val, by omega⟩ : Fin 242))
    (h025 : ∀ k : Fin 8, P (⟨200 + k.val, by omega⟩ : Fin 242))
    (h026 : ∀ k : Fin 8, P (⟨208 + k.val, by omega⟩ : Fin 242))
    (h027 : ∀ k : Fin 8, P (⟨216 + k.val, by omega⟩ : Fin 242))
    (h028 : ∀ k : Fin 8, P (⟨224 + k.val, by omega⟩ : Fin 242))
    (h029 : ∀ k : Fin 8, P (⟨232 + k.val, by omega⟩ : Fin 242))
    (h030 : ∀ k : Fin 2, P (⟨240 + k.val, by omega⟩ : Fin 242))
    : ∀ i : Fin 242, P i := by
  intro i
  by_cases h0 : i.val < 64
  · exact neutralNF724Chunk000 P
      h000
      h001
      h002
      h003
      h004
      h005
      h006
      h007
      i (by omega) h0
  · by_cases h1 : i.val < 128
    · exact neutralNF724Chunk008 P
        h008
        h009
        h010
        h011
        h012
        h013
        h014
        h015
        i (by omega) h1
    · by_cases h2 : i.val < 192
      · exact neutralNF724Chunk016 P
          h016
          h017
          h018
          h019
          h020
          h021
          h022
          h023
          i (by omega) h2
      · exact neutralNF724Chunk024 P
          h024
          h025
          h026
          h027
          h028
          h029
          h030
          i (by omega) i.isLt

#print axioms WeilDefect.neutralNF724Chunk000
#print axioms WeilDefect.neutralNF724Chunk008
#print axioms WeilDefect.neutralNF724Chunk016
#print axioms WeilDefect.neutralNF724Chunk024
#print axioms WeilDefect.neutralNF724Fin242OfPackedBlocks

end WeilDefect
