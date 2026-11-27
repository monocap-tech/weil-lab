import WeilDefect.MasterRecon.V10B26a

/-! V10B26c: literal real kernel identity and uniform series reserves.
The finite rational residual and polynomial norm remain explicit inputs. -/
namespace WeilDefect.MasterRecon.V10B26c

open scoped BigOperators
open V10B24b (h k den)
open V10B25b (D N)
open V10B26a (expPoly denPoly numPoly)

theorem literal_kernel (r : ℝ) (hr : 0 < r) : h r = N r/D r := by
  have hs : 0 < Real.sinh r := hr.trans_le (Real.self_le_sinh_iff.mpr hr.le)
  have hd := V10B24b.den_pos r hr
  have he : den r*Real.exp r = 2*Real.sinh r := by
    unfold den
    rw [Real.sinh_eq,sub_mul,one_mul,← Real.exp_add,show -2*r+r = -r by ring]
    ring
  have hk : k r = Real.exp (r/2)/(2*Real.sinh r) := by
    unfold k
    apply (div_eq_div_iff hd.ne' (by positivity : 2*Real.sinh r ≠ 0)).mpr
    rw [← he,mul_left_comm (Real.exp (-r/2)) (den r),← Real.exp_add,show -r/2+r=r/2 by ring]
    ring
  unfold h N D
  rw [hk]
  field_simp [hr.ne',hs.ne']
  <;> ring

theorem uniform_num (r : ℝ) (hr : 0 < r) (hrh : r ≤ 1/2) :
    |N r-numPoly r| ≤ 1/((2:ℝ)^28*(Nat.factorial 30:ℝ)) := by
  have hp := pow_le_pow_left₀ hr.le hrh 29
  refine (V10B26a.num_tail r hr hrh).trans ?_
  calc
    r^29/(Nat.factorial 30:ℝ) ≤ (1/2:ℝ)^29/(Nat.factorial 30:ℝ) :=
      div_le_div_of_nonneg_right hp (by positivity)
    _ ≤ _ := by norm_num [Nat.factorial]

theorem uniform_den (r : ℝ) (hr : 0 < r) (hrh : r ≤ 1/2) :
    |D r-denPoly r| ≤ 1/((2:ℝ)^28*(Nat.factorial 30:ℝ)) := by
  have hp := pow_le_pow_left₀ hr.le hrh 30
  refine (V10B26a.den_tail r hr hrh).trans ?_
  calc
    2*r^30/(Nat.factorial 31:ℝ) ≤ 2*(1/2:ℝ)^30/(Nat.factorial 31:ℝ) :=
      div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left hp (by norm_num)) (by positivity)
    _ ≤ _ := by norm_num [Nat.factorial]

theorem frozen_budget (r q : ℝ) (hr : 0 < r) (hrh : r ≤ 1/2)
    (hq : |q| ≤ 1)
    (hres : |numPoly r-denPoly r*q| ≤ 1/(10:ℝ)^22) :
    |h r-q| ≤ 1/(2:ℝ)^28 := by
  rw [literal_kernel r hr]
  have he := V10B25b.analytic_receiver r q (numPoly r) (denPoly r)
    (1/((2:ℝ)^28*(Nat.factorial 30:ℝ)))
    (1/((2:ℝ)^28*(Nat.factorial 30:ℝ))) 1 (1/(10:ℝ)^22) hr
    (uniform_num r hr hrh) (uniform_den r hr hrh) hq hres
  refine he.trans ?_
  norm_num [Nat.factorial]

end WeilDefect.MasterRecon.V10B26c

#print axioms WeilDefect.MasterRecon.V10B26c.literal_kernel
#print axioms WeilDefect.MasterRecon.V10B26c.uniform_num
#print axioms WeilDefect.MasterRecon.V10B26c.uniform_den
#print axioms WeilDefect.MasterRecon.V10B26c.frozen_budget
