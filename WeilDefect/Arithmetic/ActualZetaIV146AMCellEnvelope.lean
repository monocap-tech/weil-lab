import WeilDefect.Arithmetic.ActualZetaIV146AMCellRows
import WeilDefect.Arithmetic.ActualZetaIV145AMCellSchur

namespace WeilDefect
noncomputable section

/-- Zero-extended half-open physical cells. At the right endpoint 2
the index is 16384 and the weight is zero. -/
def neutralIV146PhysicalWeight (x : ℝ) : ℝ :=
  (neutralIV146Value (Int.floor ((x+2)*4096)) : ℝ)

/-- No point sampling: a translated point belongs to one of two cells. -/
theorem neutralIV146Floor_add (a b : ℝ) :
    Int.floor (a+b) = Int.floor a + Int.floor b ∨
    Int.floor (a+b) = Int.floor a + Int.floor b + 1 := by
  have ha := Int.floor_le a
  have hb := Int.floor_le b
  have ha' := Int.lt_floor_add_one a
  have hb' := Int.lt_floor_add_one b
  have hl : ((Int.floor a + Int.floor b : ℤ) : ℝ) ≤ a+b := by
    push_cast
    linarith
  have hu : a+b < ((Int.floor a + Int.floor b + 2 : ℤ) : ℝ) := by
    push_cast
    linarith
  have h₁ := Int.le_floor.mpr hl
  have h₂ := Int.floor_lt.mpr hu
  omega

theorem neutralIV146CellEnvelope (x s : ℝ) (i j : ℤ)
    (hi : Int.floor ((x+2)*4096) = i)
    (hj : Int.floor (s*4096) = j) :
    neutralIV146PhysicalWeight (x+s) ≤
      (max (neutralIV146Value (i+j)) (neutralIV146Value (i+j+1)) : ℝ) := by
  unfold neutralIV146PhysicalWeight
  rw [show (x+s+2)*4096 = (x+2)*4096+s*4096 by ring]
  rcases neutralIV146Floor_add ((x+2)*4096) (s*4096) with h | h
  · rw [h, hi, hj]
    exact_mod_cast le_max_left (neutralIV146Value (i+j)) (neutralIV146Value (i+j+1))
  · rw [h, hi, hj]
    exact_mod_cast le_max_right (neutralIV146Value (i+j)) (neutralIV146Value (i+j+1))

theorem neutralIV146RealRow (i : ℕ) (hi : i < 16384) :
    0 < (neutralIV146Value (i:ℤ) : ℝ) ∧
    (neutralIV146Row i : ℝ) /
      (1000000000 * (neutralIV146Value (i:ℤ) : ℝ)) < (7979648/1000000:ℝ) := by
  obtain ⟨hp, hr⟩ := neutralIV146AllRows i hi
  have hp' : 0 < (neutralIV146Value (i:ℤ) : ℝ) := by exact_mod_cast hp
  have hr' : (1000000:ℝ) * (neutralIV146Row i : ℝ) <
      7979648 * 1000000000 * (neutralIV146Value (i:ℤ) : ℝ) := by
    exact_mod_cast hr
  refine ⟨hp', (div_lt_iff₀ (mul_pos (by norm_num) hp')).2 ?_⟩
  linarith [hr']

#print axioms neutralIV146Floor_add
#print axioms neutralIV146CellEnvelope
#print axioms neutralIV146RealRow

end
end WeilDefect
