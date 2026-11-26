import WeilDefect.Arithmetic.ActualZetaIV152AMPhysicalEnvelope

namespace WeilDefect
noncomputable section

def neutralIV153CellTerm (i : ℤ) (s : ℤ × ℕ) : ℕ :=
  s.2 * max (neutralIV146Value (i+s.1)) (neutralIV146Value (i+s.1+1))

def neutralIV153PairTerm (x : ℝ) (r : ℕ × ℤ × ℕ) : ℝ :=
  neutralIV151Weight r.1 *
    (neutralIV152PhysicalWeight (x+Real.log (r.1:ℝ)) +
     neutralIV152PhysicalWeight (x-Real.log (r.1:ℝ)))

/-- A fold accumulator is precisely the sum of literal signed cell terms. -/
theorem neutralIV153Fold_sum (i : ℤ) (L : List (ℤ × ℕ)) (a : ℕ) :
    L.foldl (fun b s => b + neutralIV153CellTerm i s) a =
      a + (L.map (neutralIV153CellTerm i)).sum := by
  induction L generalizing a with
  | nil => simp
  | cons s L ih =>
    simp only [List.foldl_cons, List.map_cons, List.sum_cons]
    rw [ih]
    omega

theorem neutralIV153Row_sum (i : ℕ) :
    neutralIV146Row i =
      (neutralIV146Shifts.map (neutralIV153CellTerm (i:ℤ))).sum := by
  unfold neutralIV146Row
  change neutralIV146Shifts.foldl
    (fun a s => a + neutralIV153CellTerm (i:ℤ) s) 0 = _
  rw [neutralIV153Fold_sum, zero_add]

/-- Exact cast and division of the signed-list fold. -/
theorem neutralIV153Cast_sum (i : ℤ) (L : List (ℤ × ℕ)) :
    ((L.map (neutralIV153CellTerm i)).sum : ℝ) / 1000000000 =
      (L.map (fun s => (neutralIV153CellTerm i s : ℝ) / 1000000000)).sum := by
  induction L with
  | nil => simp
  | cons s L ih =>
    simp only [List.map_cons, List.sum_cons, Nat.cast_add, add_div, ih]

/-- Finite aggregation of every actual signed-pair inequality. -/
theorem neutralIV153Pair_sum (x : ℝ) (L : List (ℕ × ℤ × ℕ))
    (hL : ∀ r ∈ L, r ∈ neutralIV152PrimeRows) :
    (L.map (neutralIV153PairTerm x)).sum ≤
      (((L.flatMap (fun r => [(r.2.1,r.2.2),(-r.2.1-1,r.2.2)])).map
        (neutralIV153CellTerm (Int.floor ((x+2)*4096)))).sum : ℝ) /
          1000000000 := by
  rw [neutralIV153Cast_sum]
  induction L with
  | nil => simp
  | cons r L ih =>
    have hr := hL r (by simp)
    have htail : ∀ q ∈ L, q ∈ neutralIV152PrimeRows :=
      fun q hq => hL q (by simp [hq])
    have hp := neutralIV152Pair_envelope r hr x
    dsimp only at hp
    have hh : neutralIV153PairTerm x r ≤
        (neutralIV153CellTerm (Int.floor ((x+2)*4096)) (r.2.1,r.2.2) : ℝ) / 1000000000 +
        (neutralIV153CellTerm (Int.floor ((x+2)*4096)) (-r.2.1-1,r.2.2) : ℝ) / 1000000000 := by
      unfold neutralIV153PairTerm neutralIV153CellTerm
      push_cast
      convert hp using 1 <;> ring
    simp only [List.flatMap_cons, List.map_append, List.sum_append, List.map_cons,
      List.map_nil, List.sum_cons, List.sum_nil, add_zero]
    exact add_le_add hh (ih htail)

/-- Conditional row domination, with the actual row inequality supplied
explicitly. Full-bank acceptance is not assumed. -/
theorem neutralIV153Pointwise (x : ℝ) (i : ℕ)
    (hi : Int.floor ((x+2)*4096) = (i:ℤ))
    (hr : 1000000 * neutralIV146Row i <
      7979648 * 1000000000 * neutralIV146Value (i:ℤ)) :
    (neutralIV152PrimeRows.map (neutralIV153PairTerm x)).sum ≤
      (7979648/1000000:ℝ) * neutralIV152PhysicalWeight x := by
  have hp := neutralIV153Pair_sum x neutralIV152PrimeRows (fun _ h => h)
  rw [neutralIV152Shift_bank, hi, ← neutralIV153Row_sum i] at hp
  unfold neutralIV152PhysicalWeight
  rw [hi]
  have hr' : (1000000:ℝ) * (neutralIV146Row i:ℝ) <
      7979648 * 1000000000 * (neutralIV146Value (i:ℤ):ℝ) := by exact_mod_cast hr
  apply hp.trans
  linarith [hr']

#print axioms neutralIV153Fold_sum
#print axioms neutralIV153Row_sum
#print axioms neutralIV153Cast_sum
#print axioms neutralIV153Pair_sum
#print axioms neutralIV153Pointwise

end
end WeilDefect
