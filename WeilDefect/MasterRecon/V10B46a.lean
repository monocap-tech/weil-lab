import WeilDefect.MasterRecon.V10B34a

/-! V10B46a: coarse exponential pairing comparison by direct Rodrigues
moment domination. No differentiated moment recurrence or series. -/
namespace WeilDefect.MasterRecon.V10B46a
open MeasureTheory Set
open WeilDefect.MasterRecon.V10B33a
open WeilDefect.MasterRecon.V10B34a

noncomputable def f (x : ℝ) := Real.exp ((1/4:ℝ)*x-1/8)
noncomputable def w (x : ℝ) := x*(1-x)
noncomputable def J (j : ℕ) := ∫ x in (0:ℝ)..1, f x*w x^j
noncomputable def I (j : ℕ) := ∫ x in (0:ℝ)..1, f x*legendre j x

theorem w_bounds (x : ℝ) (hx : x ∈ Icc (0:ℝ) 1) :
    0 ≤ w x ∧ w x ≤ 1/4 := by
  constructor
  · exact mul_nonneg hx.1 (sub_nonneg.mpr hx.2)
  · unfold w
    nlinarith only [sq_nonneg (x-1/2)]

theorem J_add_bound (j k : ℕ) : J (j+k) ≤ (1/4:ℝ)^k*J j := by
  unfold J
  rw [← intervalIntegral.integral_const_mul]
  have hc : ∀ n : ℕ, Continuous (fun x : ℝ => f x*w x^n) := by
    intro n
    unfold f w
    fun_prop
  apply intervalIntegral.integral_mono_on (by norm_num)
    ((hc (j+k)).intervalIntegrable 0 1)
    ((continuous_const.mul (hc j)).intervalIntegrable 0 1)
  intro x hx
  change f x*w x^(j+k) ≤ (1/4:ℝ)^k*(f x*w x^j)
  obtain ⟨hw0,hw1⟩ := w_bounds x hx
  rw [pow_add]
  have h := mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hw0 hw1 k)
    (mul_nonneg (Real.exp_pos _).le (pow_nonneg hw0 j))
  calc
    f x*(w x^j*w x^k) = (f x*w x^j)*w x^k := by ring
    _ ≤ (f x*w x^j)*(1/4:ℝ)^k := h
    _ = _ := by ring

theorem I_rodrigues (j : ℕ) :
    I j = ((1/4:ℝ)^j/(j.factorial:ℝ))*J j := by
  unfold I J f w
  have h := exp_projection j (1/4) (-1/8)
  simpa only [sub_eq_add_neg,mul_pow,mul_assoc] using h

theorem I_pos (j : ℕ) : 0<I j := by
  unfold I f
  simpa only [sub_eq_add_neg] using exp_projection_pos j (1/4) (-1/8) (by norm_num)

theorem J_nonneg (j : ℕ) : 0 ≤ J j := by
  apply intervalIntegral.integral_nonneg (by norm_num)
  intro x hx
  exact mul_nonneg (Real.exp_pos _).le (pow_nonneg (w_bounds x hx).1 _)

theorem I_add_bound (j k : ℕ) : I (j+k) ≤ (1/16:ℝ)^k*I j := by
  have hf : (0:ℝ)<(j.factorial:ℝ) := by exact_mod_cast Nat.factorial_pos j
  have hg : (0:ℝ)<((j+k).factorial:ℝ) := by exact_mod_cast Nat.factorial_pos (j+k)
  have hfg : (j.factorial:ℝ) ≤ ((j+k).factorial:ℝ) := by
    exact_mod_cast Nat.factorial_le (Nat.le_add_right j k)
  have hc : (1/4:ℝ)^(j+k)/((j+k).factorial:ℝ) ≤
      (1/4:ℝ)^(j+k)/(j.factorial:ℝ) :=
    div_le_div_of_nonneg_left (by positivity) hf hfg
  rw [I_rodrigues,I_rodrigues]
  calc
    _ ≤ ((1/4:ℝ)^(j+k)/((j+k).factorial:ℝ))*((1/4:ℝ)^k*J j) :=
      mul_le_mul_of_nonneg_left (J_add_bound j k) (by positivity)
    _ ≤ ((1/4:ℝ)^(j+k)/(j.factorial:ℝ))*((1/4:ℝ)^k*J j) :=
      mul_le_mul_of_nonneg_right hc (mul_nonneg (by positivity) (J_nonneg j))
    _ = _ := by
      rw [pow_add,show (1/16:ℝ)=(1/4)*(1/4) by norm_num,mul_pow]
      ring

theorem small_power (k : ℕ) : (1/16:ℝ)^k ≤ 1 := by
  induction k with
  | zero => norm_num
  | succ k ih =>
    rw [pow_succ]
    calc
      _ ≤ 1*(1/16:ℝ) := mul_le_mul_of_nonneg_right ih (by norm_num)
      _ ≤ 1 := by norm_num

theorem high_pair_ratio (j : ℕ) (hj : 17≤j) :
    0 ≤ I j/I 15 ∧ I j/I 15 ≤ 1/256 := by
  constructor
  · exact div_nonneg (I_pos j).le (I_pos 15).le
  · obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le hj
    have h := I_add_bound 15 (2+k)
    have he : 15+(2+k)=17+k := by omega
    rw [he] at h
    apply (div_le_iff₀ (I_pos 15)).mpr
    apply h.trans
    apply mul_le_mul_of_nonneg_right _ (I_pos 15).le
    rw [pow_add]
    norm_num only [show (1/16:ℝ)^2=1/256 by norm_num]
    exact (mul_le_mul_of_nonneg_left (small_power k) (by norm_num)).trans_eq (by ring)

end WeilDefect.MasterRecon.V10B46a

#print axioms WeilDefect.MasterRecon.V10B46a.w_bounds
#print axioms WeilDefect.MasterRecon.V10B46a.J_add_bound
#print axioms WeilDefect.MasterRecon.V10B46a.I_rodrigues
#print axioms WeilDefect.MasterRecon.V10B46a.I_pos
#print axioms WeilDefect.MasterRecon.V10B46a.J_nonneg
#print axioms WeilDefect.MasterRecon.V10B46a.I_add_bound
#print axioms WeilDefect.MasterRecon.V10B46a.small_power
#print axioms WeilDefect.MasterRecon.V10B46a.high_pair_ratio
