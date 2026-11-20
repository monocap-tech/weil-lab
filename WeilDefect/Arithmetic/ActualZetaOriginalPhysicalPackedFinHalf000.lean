import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedFinChunk000
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedFinChunk008

namespace WeilDefect

/-! NF726: independently compiled two-chunk lemma for exact physical coordinates [0,128).
This is a pure finite-index statement, with no numerical matrix hypothesis. -/

theorem neutralNF726Half000
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
    (i : Fin 242) (hhi : i.val < 128) : P i := by
  by_cases hmid : i.val < 64
  · exact neutralNF724Chunk000 P
      h000
      h001
      h002
      h003
      h004
      h005
      h006
      h007
      i (by omega) hmid
  · exact neutralNF724Chunk008 P
      h008
      h009
      h010
      h011
      h012
      h013
      h014
      h015
      i (by omega) hhi

#print axioms neutralNF726Half000

end WeilDefect
