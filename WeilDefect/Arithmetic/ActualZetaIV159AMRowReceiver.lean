import WeilDefect.Arithmetic.ActualZetaIV158AMSymmetry

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- A row block is a direct check of the original literal row predicate. -/
def neutralIV159RowBlock (b : ℕ) : Bool :=
  (List.range 8).all (fun j => neutralIV146RowOK (8*b+j))

theorem neutralIV159Row_at (b j : ℕ) (hj : j < 8)
    (hb : neutralIV159RowBlock b = true) :
    0 < neutralIV146Value ((8*b+j:ℕ):ℤ) ∧
      1000000 * neutralIV146Row (8*b+j) <
        7979648 * 1000000000 * neutralIV146Value ((8*b+j:ℕ):ℤ) := by
  unfold neutralIV159RowBlock at hb
  have hh := (List.all_eq_true.mp hb) j (List.mem_range.mpr hj)
  exact of_decide_eq_true hh

theorem neutralIV159HalfRows
    (hb : ∀ b : ℕ, b < 1024 → neutralIV159RowBlock b = true)
    (i : ℕ) (hi : i < 8192) :
    0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ) := by
  have hh := neutralIV159Row_at (i/8) (i%8) (by omega) (hb (i/8) (by omega))
  rw [show 8*(i/8)+i%8=i by omega] at hh
  exact hh

#print axioms neutralIV159Row_at
#print axioms neutralIV159HalfRows
end WeilDefect
