import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTriangularCacheAssembly

namespace WeilDefect

/-!
NF722: exact finite gluing of the 31 signed-digit original row-one blocks.

The theorem is independent of the numerical center cache.  Its 31 local
hypotheses correspond exactly to NF700 packed blocks 000..030.  The final
block has *two* entries (240,241). Each block is a full original-coordinate
hypothesis, not an oracle or an assumption that the full global matrix passed.

NF722 supplies the missing all-coordinate *logical assembly mechanism*.
Applying it to the actual original NF715–NF720 kernel certificates remains
separate, and requires NF717's missing audited 32-coordinate source batch.
-/

/-- Cover all 242 physical coordinates with the disjoint blocks
0..7, 8..15, ..., 232..239, 240..241. Every coordinate is transported
from a finite-window hypothesis using a proof of exact Fin equality. -/
theorem neutralNF722Fin242OfPackedBlocks
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
  by_cases hi000 : i.val < 8
    · let k : Fin 8 := ⟨i.val, by omega⟩
      have hk : (⟨k.val, by omega⟩ : Fin 242) = i := by
        apply Fin.ext
        dsimp [k] <;> omega
      simpa only [hk] using h000 k
    · by_cases hi001 : i.val < 16
      · let k : Fin 8 := ⟨i.val - 8, by omega⟩
        have hk : (⟨8 + k.val, by omega⟩ : Fin 242) = i := by
          apply Fin.ext
          dsimp [k] <;> omega
        simpa only [hk] using h001 k
      · by_cases hi002 : i.val < 24
        · let k : Fin 8 := ⟨i.val - 16, by omega⟩
          have hk : (⟨16 + k.val, by omega⟩ : Fin 242) = i := by
            apply Fin.ext
            dsimp [k] <;> omega
          simpa only [hk] using h002 k
        · by_cases hi003 : i.val < 32
          · let k : Fin 8 := ⟨i.val - 24, by omega⟩
            have hk : (⟨24 + k.val, by omega⟩ : Fin 242) = i := by
              apply Fin.ext
              dsimp [k] <;> omega
            simpa only [hk] using h003 k
          · by_cases hi004 : i.val < 40
            · let k : Fin 8 := ⟨i.val - 32, by omega⟩
              have hk : (⟨32 + k.val, by omega⟩ : Fin 242) = i := by
                apply Fin.ext
                dsimp [k] <;> omega
              simpa only [hk] using h004 k
            · by_cases hi005 : i.val < 48
              · let k : Fin 8 := ⟨i.val - 40, by omega⟩
                have hk : (⟨40 + k.val, by omega⟩ : Fin 242) = i := by
                  apply Fin.ext
                  dsimp [k] <;> omega
                simpa only [hk] using h005 k
              · by_cases hi006 : i.val < 56
                · let k : Fin 8 := ⟨i.val - 48, by omega⟩
                  have hk : (⟨48 + k.val, by omega⟩ : Fin 242) = i := by
                    apply Fin.ext
                    dsimp [k] <;> omega
                  simpa only [hk] using h006 k
                · by_cases hi007 : i.val < 64
                  · let k : Fin 8 := ⟨i.val - 56, by omega⟩
                    have hk : (⟨56 + k.val, by omega⟩ : Fin 242) = i := by
                      apply Fin.ext
                      dsimp [k] <;> omega
                    simpa only [hk] using h007 k
                  · by_cases hi008 : i.val < 72
                    · let k : Fin 8 := ⟨i.val - 64, by omega⟩
                      have hk : (⟨64 + k.val, by omega⟩ : Fin 242) = i := by
                        apply Fin.ext
                        dsimp [k] <;> omega
                      simpa only [hk] using h008 k
                    · by_cases hi009 : i.val < 80
                      · let k : Fin 8 := ⟨i.val - 72, by omega⟩
                        have hk : (⟨72 + k.val, by omega⟩ : Fin 242) = i := by
                          apply Fin.ext
                          dsimp [k] <;> omega
                        simpa only [hk] using h009 k
                      · by_cases hi010 : i.val < 88
                        · let k : Fin 8 := ⟨i.val - 80, by omega⟩
                          have hk : (⟨80 + k.val, by omega⟩ : Fin 242) = i := by
                            apply Fin.ext
                            dsimp [k] <;> omega
                          simpa only [hk] using h010 k
                        · by_cases hi011 : i.val < 96
                          · let k : Fin 8 := ⟨i.val - 88, by omega⟩
                            have hk : (⟨88 + k.val, by omega⟩ : Fin 242) = i := by
                              apply Fin.ext
                              dsimp [k] <;> omega
                            simpa only [hk] using h011 k
                          · by_cases hi012 : i.val < 104
                            · let k : Fin 8 := ⟨i.val - 96, by omega⟩
                              have hk : (⟨96 + k.val, by omega⟩ : Fin 242) = i := by
                                apply Fin.ext
                                dsimp [k] <;> omega
                              simpa only [hk] using h012 k
                            · by_cases hi013 : i.val < 112
                              · let k : Fin 8 := ⟨i.val - 104, by omega⟩
                                have hk : (⟨104 + k.val, by omega⟩ : Fin 242) = i := by
                                  apply Fin.ext
                                  dsimp [k] <;> omega
                                simpa only [hk] using h013 k
                              · by_cases hi014 : i.val < 120
                                · let k : Fin 8 := ⟨i.val - 112, by omega⟩
                                  have hk : (⟨112 + k.val, by omega⟩ : Fin 242) = i := by
                                    apply Fin.ext
                                    dsimp [k] <;> omega
                                  simpa only [hk] using h014 k
                                · by_cases hi015 : i.val < 128
                                  · let k : Fin 8 := ⟨i.val - 120, by omega⟩
                                    have hk : (⟨120 + k.val, by omega⟩ : Fin 242) = i := by
                                      apply Fin.ext
                                      dsimp [k] <;> omega
                                    simpa only [hk] using h015 k
                                  · by_cases hi016 : i.val < 136
                                    · let k : Fin 8 := ⟨i.val - 128, by omega⟩
                                      have hk : (⟨128 + k.val, by omega⟩ : Fin 242) = i := by
                                        apply Fin.ext
                                        dsimp [k] <;> omega
                                      simpa only [hk] using h016 k
                                    · by_cases hi017 : i.val < 144
                                      · let k : Fin 8 := ⟨i.val - 136, by omega⟩
                                        have hk : (⟨136 + k.val, by omega⟩ : Fin 242) = i := by
                                          apply Fin.ext
                                          dsimp [k] <;> omega
                                        simpa only [hk] using h017 k
                                      · by_cases hi018 : i.val < 152
                                        · let k : Fin 8 := ⟨i.val - 144, by omega⟩
                                          have hk : (⟨144 + k.val, by omega⟩ : Fin 242) = i := by
                                            apply Fin.ext
                                            dsimp [k] <;> omega
                                          simpa only [hk] using h018 k
                                        · by_cases hi019 : i.val < 160
                                          · let k : Fin 8 := ⟨i.val - 152, by omega⟩
                                            have hk : (⟨152 + k.val, by omega⟩ : Fin 242) = i := by
                                              apply Fin.ext
                                              dsimp [k] <;> omega
                                            simpa only [hk] using h019 k
                                          · by_cases hi020 : i.val < 168
                                            · let k : Fin 8 := ⟨i.val - 160, by omega⟩
                                              have hk : (⟨160 + k.val, by omega⟩ : Fin 242) = i := by
                                                apply Fin.ext
                                                dsimp [k] <;> omega
                                              simpa only [hk] using h020 k
                                            · by_cases hi021 : i.val < 176
                                              · let k : Fin 8 := ⟨i.val - 168, by omega⟩
                                                have hk : (⟨168 + k.val, by omega⟩ : Fin 242) = i := by
                                                  apply Fin.ext
                                                  dsimp [k] <;> omega
                                                simpa only [hk] using h021 k
                                              · by_cases hi022 : i.val < 184
                                                · let k : Fin 8 := ⟨i.val - 176, by omega⟩
                                                  have hk : (⟨176 + k.val, by omega⟩ : Fin 242) = i := by
                                                    apply Fin.ext
                                                    dsimp [k] <;> omega
                                                  simpa only [hk] using h022 k
                                                · by_cases hi023 : i.val < 192
                                                  · let k : Fin 8 := ⟨i.val - 184, by omega⟩
                                                    have hk : (⟨184 + k.val, by omega⟩ : Fin 242) = i := by
                                                      apply Fin.ext
                                                      dsimp [k] <;> omega
                                                    simpa only [hk] using h023 k
                                                  · by_cases hi024 : i.val < 200
                                                    · let k : Fin 8 := ⟨i.val - 192, by omega⟩
                                                      have hk : (⟨192 + k.val, by omega⟩ : Fin 242) = i := by
                                                        apply Fin.ext
                                                        dsimp [k] <;> omega
                                                      simpa only [hk] using h024 k
                                                    · by_cases hi025 : i.val < 208
                                                      · let k : Fin 8 := ⟨i.val - 200, by omega⟩
                                                        have hk : (⟨200 + k.val, by omega⟩ : Fin 242) = i := by
                                                          apply Fin.ext
                                                          dsimp [k] <;> omega
                                                        simpa only [hk] using h025 k
                                                      · by_cases hi026 : i.val < 216
                                                        · let k : Fin 8 := ⟨i.val - 208, by omega⟩
                                                          have hk : (⟨208 + k.val, by omega⟩ : Fin 242) = i := by
                                                            apply Fin.ext
                                                            dsimp [k] <;> omega
                                                          simpa only [hk] using h026 k
                                                        · by_cases hi027 : i.val < 224
                                                          · let k : Fin 8 := ⟨i.val - 216, by omega⟩
                                                            have hk : (⟨216 + k.val, by omega⟩ : Fin 242) = i := by
                                                              apply Fin.ext
                                                              dsimp [k] <;> omega
                                                            simpa only [hk] using h027 k
                                                          · by_cases hi028 : i.val < 232
                                                            · let k : Fin 8 := ⟨i.val - 224, by omega⟩
                                                              have hk : (⟨224 + k.val, by omega⟩ : Fin 242) = i := by
                                                                apply Fin.ext
                                                                dsimp [k] <;> omega
                                                              simpa only [hk] using h028 k
                                                            · by_cases hi029 : i.val < 240
                                                              · let k : Fin 8 := ⟨i.val - 232, by omega⟩
                                                                have hk : (⟨232 + k.val, by omega⟩ : Fin 242) = i := by
                                                                  apply Fin.ext
                                                                  dsimp [k] <;> omega
                                                                simpa only [hk] using h029 k
                                                              · let k : Fin 2 := ⟨i.val - 240, by omega⟩
                                                                have hk : (⟨240 + k.val, by omega⟩ : Fin 242) = i := by
                                                                  apply Fin.ext
                                                                  dsimp [k] <;> omega
                                                                simpa only [hk] using h030 k

/-- Any 31 audited original global HD packed-block families glue into
the complete original index-one HD row truth. This lemma does not provide
any of its 31 source-specific numerical premises. -/
theorem neutralNF722HDIndexOneOfPackedBlocks
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (h000 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨k.val, by omega⟩ : Fin 242) = true)
    (h001 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨8 + k.val, by omega⟩ : Fin 242) = true)
    (h002 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨16 + k.val, by omega⟩ : Fin 242) = true)
    (h003 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨24 + k.val, by omega⟩ : Fin 242) = true)
    (h004 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨32 + k.val, by omega⟩ : Fin 242) = true)
    (h005 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨40 + k.val, by omega⟩ : Fin 242) = true)
    (h006 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨48 + k.val, by omega⟩ : Fin 242) = true)
    (h007 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨56 + k.val, by omega⟩ : Fin 242) = true)
    (h008 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨64 + k.val, by omega⟩ : Fin 242) = true)
    (h009 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨72 + k.val, by omega⟩ : Fin 242) = true)
    (h010 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨80 + k.val, by omega⟩ : Fin 242) = true)
    (h011 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨88 + k.val, by omega⟩ : Fin 242) = true)
    (h012 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨96 + k.val, by omega⟩ : Fin 242) = true)
    (h013 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨104 + k.val, by omega⟩ : Fin 242) = true)
    (h014 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨112 + k.val, by omega⟩ : Fin 242) = true)
    (h015 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨120 + k.val, by omega⟩ : Fin 242) = true)
    (h016 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨128 + k.val, by omega⟩ : Fin 242) = true)
    (h017 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨136 + k.val, by omega⟩ : Fin 242) = true)
    (h018 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨144 + k.val, by omega⟩ : Fin 242) = true)
    (h019 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨152 + k.val, by omega⟩ : Fin 242) = true)
    (h020 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨160 + k.val, by omega⟩ : Fin 242) = true)
    (h021 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨168 + k.val, by omega⟩ : Fin 242) = true)
    (h022 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨176 + k.val, by omega⟩ : Fin 242) = true)
    (h023 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨184 + k.val, by omega⟩ : Fin 242) = true)
    (h024 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨192 + k.val, by omega⟩ : Fin 242) = true)
    (h025 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨200 + k.val, by omega⟩ : Fin 242) = true)
    (h026 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨208 + k.val, by omega⟩ : Fin 242) = true)
    (h027 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨216 + k.val, by omega⟩ : Fin 242) = true)
    (h028 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨224 + k.val, by omega⟩ : Fin 242) = true)
    (h029 : ∀ k : Fin 8, c.HDGate s (1 : Fin 242) (⟨232 + k.val, by omega⟩ : Fin 242) = true)
    (h030 : ∀ k : Fin 2, c.HDGate s (1 : Fin 242) (⟨240 + k.val, by omega⟩ : Fin 242) = true)
    : ∀ j : Fin 242, c.HDGate s (1 : Fin 242) j = true := by
  exact neutralNF722Fin242OfPackedBlocks
    (fun j : Fin 242 => c.HDGate s (1 : Fin 242) j = true)
    h000
    h001
    h002
    h003
    h004
    h005
    h006
    h007
    h008
    h009
    h010
    h011
    h012
    h013
    h014
    h015
    h016
    h017
    h018
    h019
    h020
    h021
    h022
    h023
    h024
    h025
    h026
    h027
    h028
    h029
    h030

/-- Any 31 audited original global A packed-block families glue into
the complete original index-one A column truth. This lemma does not provide
any of its 31 source-specific numerical premises. -/
theorem neutralNF722AIndexOneOfPackedBlocks
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (h000 : ∀ k : Fin 8, c.AGate s (⟨k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h001 : ∀ k : Fin 8, c.AGate s (⟨8 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h002 : ∀ k : Fin 8, c.AGate s (⟨16 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h003 : ∀ k : Fin 8, c.AGate s (⟨24 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h004 : ∀ k : Fin 8, c.AGate s (⟨32 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h005 : ∀ k : Fin 8, c.AGate s (⟨40 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h006 : ∀ k : Fin 8, c.AGate s (⟨48 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h007 : ∀ k : Fin 8, c.AGate s (⟨56 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h008 : ∀ k : Fin 8, c.AGate s (⟨64 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h009 : ∀ k : Fin 8, c.AGate s (⟨72 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h010 : ∀ k : Fin 8, c.AGate s (⟨80 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h011 : ∀ k : Fin 8, c.AGate s (⟨88 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h012 : ∀ k : Fin 8, c.AGate s (⟨96 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h013 : ∀ k : Fin 8, c.AGate s (⟨104 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h014 : ∀ k : Fin 8, c.AGate s (⟨112 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h015 : ∀ k : Fin 8, c.AGate s (⟨120 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h016 : ∀ k : Fin 8, c.AGate s (⟨128 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h017 : ∀ k : Fin 8, c.AGate s (⟨136 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h018 : ∀ k : Fin 8, c.AGate s (⟨144 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h019 : ∀ k : Fin 8, c.AGate s (⟨152 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h020 : ∀ k : Fin 8, c.AGate s (⟨160 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h021 : ∀ k : Fin 8, c.AGate s (⟨168 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h022 : ∀ k : Fin 8, c.AGate s (⟨176 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h023 : ∀ k : Fin 8, c.AGate s (⟨184 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h024 : ∀ k : Fin 8, c.AGate s (⟨192 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h025 : ∀ k : Fin 8, c.AGate s (⟨200 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h026 : ∀ k : Fin 8, c.AGate s (⟨208 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h027 : ∀ k : Fin 8, c.AGate s (⟨216 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h028 : ∀ k : Fin 8, c.AGate s (⟨224 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h029 : ∀ k : Fin 8, c.AGate s (⟨232 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    (h030 : ∀ k : Fin 2, c.AGate s (⟨240 + k.val, by omega⟩ : Fin 242) (1 : Fin 242) = true)
    : ∀ j : Fin 242, c.AGate s j (1 : Fin 242) = true := by
  exact neutralNF722Fin242OfPackedBlocks
    (fun j : Fin 242 => c.AGate s j (1 : Fin 242) = true)
    h000
    h001
    h002
    h003
    h004
    h005
    h006
    h007
    h008
    h009
    h010
    h011
    h012
    h013
    h014
    h015
    h016
    h017
    h018
    h019
    h020
    h021
    h022
    h023
    h024
    h025
    h026
    h027
    h028
    h029
    h030

#print axioms neutralNF722Fin242OfPackedBlocks
#print axioms neutralNF722HDIndexOneOfPackedBlocks
#print axioms neutralNF722AIndexOneOfPackedBlocks

end WeilDefect
