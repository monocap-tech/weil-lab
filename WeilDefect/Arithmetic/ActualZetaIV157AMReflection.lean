import WeilDefect.Arithmetic.ActualZetaIV153AMPointwiseSum

namespace WeilDefect

/-- Reflect a two-cell maximum about the center of an integer window. -/
theorem neutralIV157Mirror_max (H : ℤ → ℕ) (N i j : ℤ)
    (h : ∀ k, H (N-k) = H k) :
    max (H ((N-i)+j)) (H ((N-i)+j+1)) =
      max (H (i+(-j-1))) (H (i+(-j-1)+1)) := by
  have h₁ : H (N-i+j) = H (i+(-j-1)+1) := by
    calc
      _ = H (N-(i+(-j-1)+1)) := by congr 1 <;> ring
      _ = _ := h _
  have h₂ : H (N-i+j+1) = H (i+(-j-1)) := by
    calc
      _ = H (N-(i+(-j-1))) := by congr 1 <;> ring
      _ = _ := h _
  rw [h₁,h₂]
  exact max_comm _ _

/-- The two literal shifts for each prime are exchanged by reflection. -/
theorem neutralIV157Mirror_pair (N i j : ℤ) (u : ℕ)
    (h : ∀ k, neutralIV146Value (N-k) = neutralIV146Value k) :
    neutralIV153CellTerm (N-i) (j,u) +
      neutralIV153CellTerm (N-i) (-j-1,u) =
    neutralIV153CellTerm i (j,u) +
      neutralIV153CellTerm i (-j-1,u) := by
  unfold neutralIV153CellTerm
  simp only [Prod.fst, Prod.snd]
  rw [neutralIV157Mirror_max neutralIV146Value N i j h,
      neutralIV157Mirror_max neutralIV146Value N i (-j-1) h]
  rw [show -(-j-1)-1=j by ring]
  exact Nat.add_comm _ _

theorem neutralIV157Mirror_list (N i : ℤ) (L : List (ℕ × ℤ × ℕ))
    (h : ∀ k, neutralIV146Value (N-k) = neutralIV146Value k) :
    ((L.flatMap (fun r => [(r.2.1,r.2.2),(-r.2.1-1,r.2.2)])).map
        (neutralIV153CellTerm (N-i))).sum =
    ((L.flatMap (fun r => [(r.2.1,r.2.2),(-r.2.1-1,r.2.2)])).map
        (neutralIV153CellTerm i)).sum := by
  induction L with
  | nil => simp
  | cons r L ih =>
    simp only [List.flatMap_cons, List.map_append, List.sum_append, List.map_cons,
      List.map_nil, List.sum_cons, List.sum_nil, add_zero]
    rw [ih]
    have hp := neutralIV157Mirror_pair N i r.2.1 r.2.2 h
    omega

/-- Reflection of the actual integer row, conditional on exact
zero-extended weight reflection. -/
theorem neutralIV157Mirror_row (i : ℕ) (hi : i < 16384)
    (h : ∀ k : ℤ, neutralIV146Value (16383-k) = neutralIV146Value k) :
    neutralIV146Row (16383-i) = neutralIV146Row i := by
  rw [neutralIV153Row_sum, neutralIV153Row_sum, ← neutralIV152Shift_bank]
  have he : ((16383-i:ℕ):ℤ) = 16383-(i:ℤ) := by omega
  rw [he]
  exact neutralIV157Mirror_list 16383 (i:ℤ) neutralIV152PrimeRows h

/-- Half-bank suffices once zero-extended symmetry is certified. -/
theorem neutralIV157Half_bank
    (h : ∀ k : ℤ, neutralIV146Value (16383-k) = neutralIV146Value k)
    (hb : ∀ i : ℕ, i < 8192 →
      0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ))
    (i : ℕ) (hi : i < 16384) :
    0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ) := by
  by_cases hl : i < 8192
  · exact hb i hl
  have hj : 16383-i < 8192 := by omega
  have he : ((16383-i:ℕ):ℤ) = 16383-(i:ℤ) := by omega
  have hh := hb (16383-i) hj
  rw [he, h, neutralIV157Mirror_row i hi h] at hh
  exact hh

#print axioms neutralIV157Mirror_max
#print axioms neutralIV157Mirror_pair
#print axioms neutralIV157Mirror_list
#print axioms neutralIV157Mirror_row
#print axioms neutralIV157Half_bank
end WeilDefect
