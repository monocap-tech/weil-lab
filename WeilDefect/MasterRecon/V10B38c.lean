import WeilDefect.MasterRecon.V10B35a
import WeilDefect.MasterRecon.V10B37b

/-! V10B38c: a uniform all-degree majorant for the literal exponential
Legendre expansion, rather than merely the high odd tail. -/
namespace WeilDefect.MasterRecon.V10B38c
open WeilDefect.MasterRecon.V10B33a
open WeilDefect.MasterRecon.V10B35a
open WeilDefect.MasterRecon.V10B37b

noncomputable def A (j : ℕ) := coeff j (1/4) (-1/8)
noncomputable def majorant (j : ℕ) := (4:ℝ)^j*A j

theorem A_nonneg (j : ℕ) : 0 ≤ A j :=
  (coeff_pos j (1/4) (-1/8) (by norm_num)).le

theorem majorant_step (j : ℕ) :
    majorant (j+1) ≤ (1/2:ℝ)*majorant j := by
  have h := coeff_step j (1/4) (-1/8) (by norm_num)
  change A (j+1) ≤ ((1/4:ℝ)/(2*(2*(j:ℝ)+1)))*A j at h
  have hd : (0:ℝ) < 2*(2*(j:ℝ)+1) := by positivity
  have hratio : (1/4:ℝ)/(2*(2*(j:ℝ)+1)) ≤ 1/8 := by
    apply (div_le_iff₀ hd).mpr
    have hj : 0 ≤ (j:ℝ) := by positivity
    linarith
  have h' := h.trans (mul_le_mul_of_nonneg_right hratio (A_nonneg j))
  unfold majorant
  calc
    _ ≤ (4:ℝ)^(j+1)*((1/8:ℝ)*A j) :=
      mul_le_mul_of_nonneg_left h' (by positivity)
    _ = _ := by rw [pow_succ]; ring

theorem majorant_geometric (j : ℕ) :
    majorant j ≤ (1/2:ℝ)^j*A 0 := by
  induction j with
  | zero => simp [majorant]
  | succ j ih =>
    calc
      _ ≤ (1/2:ℝ)*majorant j := majorant_step j
      _ ≤ (1/2:ℝ)*((1/2:ℝ)^j*A 0) :=
        mul_le_mul_of_nonneg_left ih (by norm_num)
      _ = _ := by rw [pow_succ]; ring

theorem expansion_term_bound (j : ℕ) (z : ℝ) (hz : z ∈ Set.Icc (0:ℝ) 1) :
    |A j*legendre j z| ≤ (1/2:ℝ)^j*A 0 := by
  rw [abs_mul,abs_of_nonneg (A_nonneg j)]
  calc
    _ ≤ A j*(4:ℝ)^j :=
      mul_le_mul_of_nonneg_left (legendre_uniform_envelope j z hz) (A_nonneg j)
    _ = majorant j := by unfold majorant; ring
    _ ≤ _ := majorant_geometric j

end WeilDefect.MasterRecon.V10B38c

#print axioms WeilDefect.MasterRecon.V10B38c.A_nonneg
#print axioms WeilDefect.MasterRecon.V10B38c.majorant_step
#print axioms WeilDefect.MasterRecon.V10B38c.majorant_geometric
#print axioms WeilDefect.MasterRecon.V10B38c.expansion_term_bound
