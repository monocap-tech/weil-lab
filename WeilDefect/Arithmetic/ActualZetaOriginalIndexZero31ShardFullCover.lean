import Mathlib.Tactic

namespace WeilDefect

/-!
NF744: exact full original Fin 242 index-zero cover from 31 independent
eight-coordinate ranges (30 full octets and a last two-coordinate slice).
Pure logical transfer ONLY: each original NF702/NF703 numerical range
still requires a separately accepted source-bound Lean kernel theorem.
-/

/-- Source-neutral full Fin242 implication from all 31 eight-coordinate
blocks, including the terminal [240,242) two-position range. -/
theorem neutralNF744AllFin242Of31OriginalIndexZeroShards
    (P : Fin 242 → Prop)
    (s000 : ∀ k : Fin 242, 0 ≤ k.val → k.val < 8 → P k)
    (s008 : ∀ k : Fin 242, 8 ≤ k.val → k.val < 16 → P k)
    (s016 : ∀ k : Fin 242, 16 ≤ k.val → k.val < 24 → P k)
    (s024 : ∀ k : Fin 242, 24 ≤ k.val → k.val < 32 → P k)
    (s032 : ∀ k : Fin 242, 32 ≤ k.val → k.val < 40 → P k)
    (s040 : ∀ k : Fin 242, 40 ≤ k.val → k.val < 48 → P k)
    (s048 : ∀ k : Fin 242, 48 ≤ k.val → k.val < 56 → P k)
    (s056 : ∀ k : Fin 242, 56 ≤ k.val → k.val < 64 → P k)
    (s064 : ∀ k : Fin 242, 64 ≤ k.val → k.val < 72 → P k)
    (s072 : ∀ k : Fin 242, 72 ≤ k.val → k.val < 80 → P k)
    (s080 : ∀ k : Fin 242, 80 ≤ k.val → k.val < 88 → P k)
    (s088 : ∀ k : Fin 242, 88 ≤ k.val → k.val < 96 → P k)
    (s096 : ∀ k : Fin 242, 96 ≤ k.val → k.val < 104 → P k)
    (s104 : ∀ k : Fin 242, 104 ≤ k.val → k.val < 112 → P k)
    (s112 : ∀ k : Fin 242, 112 ≤ k.val → k.val < 120 → P k)
    (s120 : ∀ k : Fin 242, 120 ≤ k.val → k.val < 128 → P k)
    (s128 : ∀ k : Fin 242, 128 ≤ k.val → k.val < 136 → P k)
    (s136 : ∀ k : Fin 242, 136 ≤ k.val → k.val < 144 → P k)
    (s144 : ∀ k : Fin 242, 144 ≤ k.val → k.val < 152 → P k)
    (s152 : ∀ k : Fin 242, 152 ≤ k.val → k.val < 160 → P k)
    (s160 : ∀ k : Fin 242, 160 ≤ k.val → k.val < 168 → P k)
    (s168 : ∀ k : Fin 242, 168 ≤ k.val → k.val < 176 → P k)
    (s176 : ∀ k : Fin 242, 176 ≤ k.val → k.val < 184 → P k)
    (s184 : ∀ k : Fin 242, 184 ≤ k.val → k.val < 192 → P k)
    (s192 : ∀ k : Fin 242, 192 ≤ k.val → k.val < 200 → P k)
    (s200 : ∀ k : Fin 242, 200 ≤ k.val → k.val < 208 → P k)
    (s208 : ∀ k : Fin 242, 208 ≤ k.val → k.val < 216 → P k)
    (s216 : ∀ k : Fin 242, 216 ≤ k.val → k.val < 224 → P k)
    (s224 : ∀ k : Fin 242, 224 ≤ k.val → k.val < 232 → P k)
    (s232 : ∀ k : Fin 242, 232 ≤ k.val → k.val < 240 → P k)
    (s240 : ∀ k : Fin 242, 240 ≤ k.val → k.val < 242 → P k)
    : ∀ k : Fin 242, P k := by
  intro k
  by_cases h8 : k.val < 8
  · exact s000 k (by omega) h8
  by_cases h16 : k.val < 16
  · exact s008 k (by omega) h16
  by_cases h24 : k.val < 24
  · exact s016 k (by omega) h24
  by_cases h32 : k.val < 32
  · exact s024 k (by omega) h32
  by_cases h40 : k.val < 40
  · exact s032 k (by omega) h40
  by_cases h48 : k.val < 48
  · exact s040 k (by omega) h48
  by_cases h56 : k.val < 56
  · exact s048 k (by omega) h56
  by_cases h64 : k.val < 64
  · exact s056 k (by omega) h64
  by_cases h72 : k.val < 72
  · exact s064 k (by omega) h72
  by_cases h80 : k.val < 80
  · exact s072 k (by omega) h80
  by_cases h88 : k.val < 88
  · exact s080 k (by omega) h88
  by_cases h96 : k.val < 96
  · exact s088 k (by omega) h96
  by_cases h104 : k.val < 104
  · exact s096 k (by omega) h104
  by_cases h112 : k.val < 112
  · exact s104 k (by omega) h112
  by_cases h120 : k.val < 120
  · exact s112 k (by omega) h120
  by_cases h128 : k.val < 128
  · exact s120 k (by omega) h128
  by_cases h136 : k.val < 136
  · exact s128 k (by omega) h136
  by_cases h144 : k.val < 144
  · exact s136 k (by omega) h144
  by_cases h152 : k.val < 152
  · exact s144 k (by omega) h152
  by_cases h160 : k.val < 160
  · exact s152 k (by omega) h160
  by_cases h168 : k.val < 168
  · exact s160 k (by omega) h168
  by_cases h176 : k.val < 176
  · exact s168 k (by omega) h176
  by_cases h184 : k.val < 184
  · exact s176 k (by omega) h184
  by_cases h192 : k.val < 192
  · exact s184 k (by omega) h192
  by_cases h200 : k.val < 200
  · exact s192 k (by omega) h200
  by_cases h208 : k.val < 208
  · exact s200 k (by omega) h208
  by_cases h216 : k.val < 216
  · exact s208 k (by omega) h216
  by_cases h224 : k.val < 224
  · exact s216 k (by omega) h224
  by_cases h232 : k.val < 232
  · exact s224 k (by omega) h232
  by_cases h240 : k.val < 240
  · exact s232 k (by omega) h240
  exact s240 k (by omega) k.isLt

#print axioms neutralNF744AllFin242Of31OriginalIndexZeroShards

end WeilDefect
