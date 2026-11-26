import WeilDefect.Arithmetic.ActualZetaIV146AMCellData
import WeilDefect.Arithmetic.ActualZetaIV151AMActualCaps

namespace WeilDefect
noncomputable section

/-- Zero-extended half-open physical cells. At the right endpoint 2
the index is 16384 and the weight is zero. -/
def neutralIV152PhysicalWeight (x : ℝ) : ℝ :=
  (neutralIV146Value (Int.floor ((x+2)*4096)) : ℝ)

/-- No point sampling: a translated point belongs to one of two cells. -/
theorem neutralIV152Floor_add (a b : ℝ) :
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

theorem neutralIV152CellEnvelope (x s : ℝ) (i j : ℤ)
    (hi : Int.floor ((x+2)*4096) = i)
    (hj : Int.floor (s*4096) = j) :
    neutralIV152PhysicalWeight (x+s) ≤
      (max (neutralIV146Value (i+j)) (neutralIV146Value (i+j+1)) : ℝ) := by
  unfold neutralIV152PhysicalWeight
  rw [show (x+s+2)*4096 = (x+2)*4096+s*4096 by ring]
  rcases neutralIV152Floor_add ((x+2)*4096) (s*4096) with h | h
  · rw [h, hi, hj]
    exact_mod_cast le_max_left (neutralIV146Value (i+j)) (neutralIV146Value (i+j+1))
  · rw [h, hi, hj]
    exact_mod_cast le_max_right (neutralIV146Value (i+j)) (neutralIV146Value (i+j+1))

/-- Prime number, positive translation floor, and integer coefficient cap.
The negative shift floor is -j-1, not -j. -/
def neutralIV152PrimeRows : List (ℕ × ℤ × ℕ) := [
  (2, 2839, 490129072),
  (3, 4499, 634284101),
  (4, 5678, 346573591),
  (5, 6592, 719762516),
  (7, 7970, 735484905),
  (8, 8517, 245064536),
  (9, 8999, 366204097),
  (11, 9821, 722992628),
  (13, 10506, 711388956),
  (16, 11356, 173286796),
  (17, 11604, 687155170),
  (19, 12060, 675500630),
  (23, 12842, 653795740),
  (25, 13184, 321887583),
  (27, 13499, 211428034),
  (29, 13792, 625291138),
  (31, 14065, 616762310),
  (32, 14195, 122532268),
  (37, 14790, 593631249),
  (41, 15210, 579962520),
  (43, 15405, 573577641),
  (47, 15770, 561601748),
  (49, 15940, 277987165),
  (53, 16262, 545361537)
]

theorem neutralIV152Shift_bank :
    neutralIV152PrimeRows.flatMap (fun r =>
      [(r.2.1,r.2.2),(-r.2.1-1,r.2.2)]) = neutralIV146Shifts := by decide

theorem neutralIV152Prime_bank :
    (neutralIV152PrimeRows.map Prod.fst).toFinset =
      ({2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53} : Finset ℕ) := by decide

theorem neutralIV152Actual_caps (r : ℕ × ℤ × ℕ)
    (hr : r ∈ neutralIV152PrimeRows) :
    (Int.floor (Real.log (r.1:ℝ)*4096) = r.2.1 ∧
      Int.floor (-Real.log (r.1:ℝ)*4096) = -r.2.1-1) ∧
    (0 ≤ neutralIV151Weight r.1 ∧
      neutralIV151Weight r.1 < (r.2.2:ℝ)/1000000000) := by
  simp only [neutralIV152PrimeRows, List.mem_cons, List.not_mem_nil, or_false] at hr
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact neutralIV151Actual_2
  · exact neutralIV151Actual_3
  · exact neutralIV151Actual_4
  · exact neutralIV151Actual_5
  · exact neutralIV151Actual_7
  · exact neutralIV151Actual_8
  · exact neutralIV151Actual_9
  · exact neutralIV151Actual_11
  · exact neutralIV151Actual_13
  · exact neutralIV151Actual_16
  · exact neutralIV151Actual_17
  · exact neutralIV151Actual_19
  · exact neutralIV151Actual_23
  · exact neutralIV151Actual_25
  · exact neutralIV151Actual_27
  · exact neutralIV151Actual_29
  · exact neutralIV151Actual_31
  · exact neutralIV151Actual_32
  · exact neutralIV151Actual_37
  · exact neutralIV151Actual_41
  · exact neutralIV151Actual_43
  · exact neutralIV151Actual_47
  · exact neutralIV151Actual_49
  · exact neutralIV151Actual_53

/-- Literal row summands bound the actual translated weight, without
a discretization assumption on the real coordinate x. -/
theorem neutralIV152Pair_envelope (r : ℕ × ℤ × ℕ)
    (hr : r ∈ neutralIV152PrimeRows) (x : ℝ) :
    let i := Int.floor ((x+2)*4096)
    neutralIV151Weight r.1 *
        (neutralIV152PhysicalWeight (x+Real.log (r.1:ℝ)) +
         neutralIV152PhysicalWeight (x-Real.log (r.1:ℝ))) ≤
      ((r.2.2:ℝ)/1000000000) *
        ((max (neutralIV146Value (i+r.2.1))
              (neutralIV146Value (i+r.2.1+1)) : ℝ) +
         (max (neutralIV146Value (i+(-r.2.1-1)))
              (neutralIV146Value (i+(-r.2.1-1)+1)) : ℝ)) := by
  dsimp only
  obtain ⟨⟨hp,hm⟩,h0,hu⟩ := neutralIV152Actual_caps r hr
  have ep := neutralIV152CellEnvelope x (Real.log (r.1:ℝ)) _ _ rfl hp
  have em := neutralIV152CellEnvelope x (-Real.log (r.1:ℝ)) _ _ rfl hm
  rw [← sub_eq_add_neg] at em
  apply le_trans (mul_le_mul_of_nonneg_left (add_le_add ep em) h0)
  apply mul_le_mul_of_nonneg_right hu.le
  positivity

theorem neutralIV152Physical_nonneg (x : ℝ) : 0 ≤ neutralIV152PhysicalWeight x := by
  unfold neutralIV152PhysicalWeight
  positivity

#print axioms neutralIV152Floor_add
#print axioms neutralIV152CellEnvelope
#print axioms neutralIV152Shift_bank
#print axioms neutralIV152Prime_bank
#print axioms neutralIV152Actual_caps
#print axioms neutralIV152Pair_envelope
#print axioms neutralIV152Physical_nonneg

end
end WeilDefect
