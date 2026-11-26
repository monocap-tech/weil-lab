import WeilDefect.Arithmetic.ActualZetaIV157AMSymmetryPilot

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- Zero-extension is an identity about the actual chunked lookup. -/
theorem neutralIV158Outside (i : ℤ) (hi : i < 0 ∨ 16384 ≤ i) :
    neutralIV146Value i = 0 := by
  rcases hi with hn | hp
  · simp [neutralIV146Value, hn]
  · have hn : ¬ i < 0 := by omega
    have hc : (i.toNat / 128) ≥ 128 := by omega
    have hs : neutralIV146HChunks.size = 128 := by decide
    have ho : neutralIV146HChunks.size ≤ i.toNat / 128 := by omega
    unfold neutralIV146Value
    rw [if_neg hn, Array.getElem?_eq_none ho]
    simp

/-- Extension of finite half-bank symmetry to every signed index. -/
theorem neutralIV158Extend
    (h : ∀ i : ℕ, i < 8192 →
      neutralIV146Value (i:ℤ) = neutralIV146Value (16383-(i:ℤ)))
    (k : ℤ) :
    neutralIV146Value (16383-k) = neutralIV146Value k := by
  by_cases hl : k < 0
  · rw [neutralIV158Outside k (Or.inl hl),
      neutralIV158Outside (16383-k) (Or.inr (by omega))]
  by_cases hu : 16384 ≤ k
  · rw [neutralIV158Outside k (Or.inr hu),
      neutralIV158Outside (16383-k) (Or.inl (by omega))]
  by_cases hm : k < 8192
  · have he : (k.toNat:ℤ) = k := Int.toNat_of_nonneg (by omega)
    have hh := h k.toNat (by omega)
    rw [he] at hh
    exact hh.symm
  · have he : ((16383-k).toNat:ℤ) = 16383-k := Int.toNat_of_nonneg (by omega)
    have hh := h (16383-k).toNat (by omega)
    rw [he, show 16383-(16383-k)=k by ring] at hh
    exact hh

/-- Convert a finite symmetry block to its individual literal equalities. -/
theorem neutralIV158Sym_at (b j : ℕ) (hj : j < 64)
    (hb : neutralIV157SymBlock b = true) :
    neutralIV146Value ((64*b+j:ℕ):ℤ) =
      neutralIV146Value (16383-((64*b+j:ℕ):ℤ)) := by
  unfold neutralIV157SymBlock at hb
  have hh := (List.all_eq_true.mp hb) j (List.mem_range.mpr hj)
  simpa using hh

/-- Conditional half-window assembly, with every finite block supplied. -/
theorem neutralIV158Symmetry
    (hb : ∀ b : ℕ, b < 128 → neutralIV157SymBlock b = true)
    (k : ℤ) : neutralIV146Value (16383-k) = neutralIV146Value k := by
  apply neutralIV158Extend _ k
  intro i hi
  have hh := neutralIV158Sym_at (i/64) (i%64) (by omega) (hb (i/64) (by omega))
  rw [show 64*(i/64)+i%64=i by omega] at hh
  exact hh

#print axioms neutralIV158Outside
#print axioms neutralIV158Extend
#print axioms neutralIV158Sym_at
#print axioms neutralIV158Symmetry
end WeilDefect
