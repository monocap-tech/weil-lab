import WeilDefect.MasterRecon.V10B34a
import WeilDefect.MasterRecon.V10B34b
import WeilDefect.MasterRecon.V10B32b

/-! V10B35a: literal exponential Legendre coefficients and direct
two-degree decay, without the spherical series or completeness. -/
namespace WeilDefect.MasterRecon.V10B35a
open MeasureTheory Set
open WeilDefect.MasterRecon.V10B34a
open WeilDefect.MasterRecon.V10B34b
open WeilDefect.MasterRecon.V10B32b

noncomputable def coeff (j : ℕ) (a b : ℝ) : ℝ :=
  ((2*(j:ℝ)+1)*a^j/(j.factorial:ℝ))*moment j a b

noncomputable def normalized (k : ℕ) : ℝ :=
  coeff (15+2*k) (1/4) (-1/8) / coeff 15 (1/4) (-1/8)

theorem moment_pos (j : ℕ) (a b : ℝ) : 0 < moment j a b := by
  unfold moment
  apply intervalIntegral.integral_pos (by norm_num : (0:ℝ)<1)
  · apply Continuous.continuousOn
    unfold e w
    fun_prop
  · intro x hx
    exact mul_nonneg (Real.exp_pos _).le (pow_nonneg
      (mul_nonneg hx.1.le (sub_nonneg.mpr hx.2)) _)
  · refine ⟨1/2, by constructor <;> norm_num, ?_⟩
    exact mul_pos (Real.exp_pos _) (pow_pos (by norm_num [w]) _)

theorem coeff_pos (j : ℕ) (a b : ℝ) (ha : 0 < a) :
    0 < coeff j a b := by
  unfold coeff
  have hf : 0 < (j.factorial:ℝ) := by exact_mod_cast Nat.factorial_pos j
  exact mul_pos (by positivity) (moment_pos j a b)

theorem coeff_literal (j : ℕ) (a b : ℝ) :
    coeff j a b = (2*(j:ℝ)+1)*
      (∫ x in (0:ℝ)..1, Real.exp (a*x+b)*V10B33a.legendre j x) := by
  rw [exp_projection]
  unfold coeff moment e w
  simp only [mul_pow]
  have h : (fun x : ℝ => Real.exp (a*x+b)*(x^j*(1-x)^j)) =
      fun x => Real.exp (a*x+b)*x^j*(1-x)^j := by funext x; ring
  rw [h]
  ring

theorem coeff_step (j : ℕ) (a b : ℝ) (ha : 0 ≤ a) :
    coeff (j+1) a b ≤ (a/(2*(2*(j:ℝ)+1)))*coeff j a b := by
  have hf : 0 < (j.factorial:ℝ) := by exact_mod_cast Nat.factorial_pos j
  have hj : 0 < (j:ℝ)+1 := by positivity
  have hd : 0 < 4*(j:ℝ)+6 := by positivity
  have hs : moment (j+1) a b ≤ (((j:ℝ)+1)/(4*(j:ℝ)+6))*moment j a b := by
    rw [div_mul_eq_mul_div]
    apply (le_div_iff₀ hd).mpr
    simpa only [mul_comm] using moment_step j a b ha
  unfold coeff
  rw [Nat.factorial_succ]
  push_cast
  calc
    _ ≤ ((2*((j:ℝ)+1)+1)*a^(j+1)/(((j:ℝ)+1)*(j.factorial:ℝ)))*
        ((((j:ℝ)+1)/(4*(j:ℝ)+6))*moment j a b) :=
      mul_le_mul_of_nonneg_left hs (by positivity)
    _ = _ := by
      rw [pow_succ]
      have hd' : 0 < 2*(2*(j:ℝ)+1) := by positivity
      field_simp [hf.ne',hj.ne',hd.ne',hd'.ne'] <;> ring

theorem coeff_step_two (j : ℕ) (a b : ℝ) (ha : 0 ≤ a) :
    coeff (j+2) a b ≤
      (a^2/(4*(2*(j:ℝ)+1)*(2*(j:ℝ)+3)))*coeff j a b := by
  have h₁ := coeff_step j a b ha
  have h₂ := coeff_step (j+1) a b ha
  have h₃ := mul_le_mul_of_nonneg_left h₁
    (show 0 ≤ a/(2*(2*((j+1:ℕ):ℝ)+1)) by positivity)
  calc
    _ ≤ (a/(2*(2*((j+1:ℕ):ℝ)+1)))*
      ((a/(2*(2*(j:ℝ)+1)))*coeff j a b) := h₂.trans h₃
    _ = _ := by
      push_cast
      have h₄ : 0 < 2*(j:ℝ)+1 := by positivity
      have h₅ : 0 < 2*(j:ℝ)+3 := by positivity
      field_simp [h₄.ne',h₅.ne'] <;> ring

theorem normalized_pos (k : ℕ) : 0 < normalized k :=
  div_pos (coeff_pos _ _ _ (by norm_num)) (coeff_pos _ _ _ (by norm_num))

theorem normalized_zero : normalized 0 = 1 := by
  unfold normalized
  norm_num only [mul_zero,add_zero]
  exact div_self (coeff_pos 15 (1/4) (-1/8) (by norm_num)).ne'

theorem normalized_step (k : ℕ) :
    normalized (k+1) ≤ (1/65000:ℝ)*normalized k := by
  let j : ℕ := 15+2*k
  have hj : 15 ≤ j := by dsimp [j]; omega
  have h := coeff_step_two j (1/4) (-1/8) (by norm_num)
  have h₁ : coeff (j+2) (1/4) (-1/8) ≤
      (1/(64*(2*(j:ℝ)+1)*(2*(j:ℝ)+3)))*coeff j (1/4) (-1/8) := by
    convert h using 1 <;> ring
  have h₂ := ratio_bound j hj 1 1 (by norm_num) (by norm_num) (by norm_num)
  norm_num only [div_self one_ne_zero,mul_one] at h₂
  have hd := (coeff_pos 15 (1/4) (-1/8) (by norm_num)).le
  have he := h₁.trans (mul_le_mul_of_nonneg_right h₂
    (coeff_pos j (1/4) (-1/8) (by norm_num)).le)
  have hh := div_le_div_of_nonneg_right he hd
  unfold normalized
  rw [show 15+2*(k+1)=j+2 by dsimp [j]; omega]
  change coeff (j+2) (1/4) (-1/8) / coeff 15 (1/4) (-1/8) ≤
    (1/65000:ℝ)*(coeff j (1/4) (-1/8)/coeff 15 (1/4) (-1/8))
  simpa only [mul_div_assoc] using hh

theorem normalized_tail :
    (∑' k : ℕ, normalized (10+k)) < 1/(10:ℝ)^25 := by
  exact (outer_tail normalized (1/65000) (by norm_num) (by norm_num)
    (fun k => (normalized_pos k).le) (le_of_eq normalized_zero)
    normalized_step 10).trans_lt frozen_ratio_tail

end WeilDefect.MasterRecon.V10B35a

#print axioms WeilDefect.MasterRecon.V10B35a.moment_pos
#print axioms WeilDefect.MasterRecon.V10B35a.coeff_pos
#print axioms WeilDefect.MasterRecon.V10B35a.coeff_literal
#print axioms WeilDefect.MasterRecon.V10B35a.coeff_step
#print axioms WeilDefect.MasterRecon.V10B35a.coeff_step_two
#print axioms WeilDefect.MasterRecon.V10B35a.normalized_pos
#print axioms WeilDefect.MasterRecon.V10B35a.normalized_zero
#print axioms WeilDefect.MasterRecon.V10B35a.normalized_step
#print axioms WeilDefect.MasterRecon.V10B35a.normalized_tail
