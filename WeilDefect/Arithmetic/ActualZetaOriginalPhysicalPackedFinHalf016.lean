import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedFinChunk016
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedFinChunk024

namespace WeilDefect

/-! NF726: independently compiled two-chunk lemma for exact physical coordinates [128,242).
This is a pure finite-index statement, with no numerical matrix hypothesis. -/

theorem neutralNF726Half016
    (P : Fin 242 → Prop)
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
    (i : Fin 242) (hlo : 128 ≤ i.val) : P i := by
  by_cases hmid : i.val < 192
  · exact neutralNF724Chunk016 P
      h016
      h017
      h018
      h019
      h020
      h021
      h022
      h023
      i (by omega) hmid
  · exact neutralNF724Chunk024 P
      h024
      h025
      h026
      h027
      h028
      h029
      h030
      i (by omega) i.isLt

#print axioms neutralNF726Half016

end WeilDefect
