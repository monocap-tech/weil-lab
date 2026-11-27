import WeilDefect.MasterRecon.V10B36a

/-! V10B37a: factorial-only solution of the centered beta recurrences.
No double-factorial API or infinite expansion is required. -/
namespace WeilDefect.MasterRecon.V10B37a
open WeilDefect.MasterRecon.V10B36a

noncomputable def F (j m : ℕ) : ℝ :=
  (j.factorial:ℝ)*((2*m).factorial:ℝ)*((j+m).factorial:ℝ) /
    ((m.factorial:ℝ)*((2*j+2*m+1).factorial:ℝ))

theorem F_zero : F 0 0 = 1 := by norm_num [F]

theorem F_j_step (j : ℕ) :
    (4*(j:ℝ)+6)*F (j+1) 0 = ((j:ℝ)+1)*F j 0 := by
  unfold F
  simp only [mul_zero,add_zero,Nat.factorial_zero,Nat.cast_one,mul_one,one_mul]
  rw [show 2*(j+1)+1= (2*j+1)+1+1 by omega]
  simp only [Nat.factorial_succ,Nat.cast_mul,Nat.cast_add,Nat.cast_one]
  have h : (0:ℝ)<((2*j+1).factorial:ℝ) := by exact_mod_cast Nat.factorial_pos (2*j+1)
  -- factorial_succ also expands the common odd factorial; the resulting
  -- denominator factors are all strictly positive.
  have h' : (0:ℝ)<((2*j).factorial:ℝ) := by exact_mod_cast Nat.factorial_pos (2*j)
  push_cast at *
  field_simp <;> ring

theorem F_m_step (j m : ℕ) :
    (2*(j:ℝ)+2*(m:ℝ)+3)*F j (m+1) = (2*(m:ℝ)+1)*F j m := by
  unfold F
  rw [show 2*(m+1)=2*m+1+1 by omega,
      show j+(m+1)=j+m+1 by omega,
      show 2*j+(2*m+1+1)+1=(2*j+2*m+1)+1+1 by omega]
  simp only [Nat.factorial_succ,Nat.cast_mul,Nat.cast_add,Nat.cast_one]
  have h : (0:ℝ)<((m.factorial:ℝ)) := by exact_mod_cast Nat.factorial_pos m
  have h' : (0:ℝ)<((2*j+2*m).factorial:ℝ) := by exact_mod_cast Nat.factorial_pos (2*j+2*m)
  push_cast at *
  field_simp <;> ring

theorem B_closed (j m : ℕ) : B j m = F j m := by
  have h0 : ∀ n : ℕ, B n 0 = F n 0 := by
    intro n
    induction n with
    | zero => rw [B_zero,F_zero]
    | succ n ih =>
      have h := B_j_step n
      have h' := F_j_step n
      rw [ih] at h
      have hp : 0 < 4*(n:ℝ)+6 := by positivity
      exact (mul_left_cancel₀ hp.ne' (h.trans h'.symm))
  induction m with
  | zero => exact h0 j
  | succ m ih =>
    have h := B_m_step j m
    have h' := F_m_step j m
    rw [ih] at h
    have hp : 0 < 2*(j:ℝ)+2*(m:ℝ)+3 := by positivity
    exact mul_left_cancel₀ hp.ne' (h.trans h'.symm)

end WeilDefect.MasterRecon.V10B37a

#print axioms WeilDefect.MasterRecon.V10B37a.F_zero
#print axioms WeilDefect.MasterRecon.V10B37a.F_j_step
#print axioms WeilDefect.MasterRecon.V10B37a.F_m_step
#print axioms WeilDefect.MasterRecon.V10B37a.B_closed
