import Mathlib.MeasureTheory.Integral.Gamma
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.NumberTheory.ZetaValues

/-! V10B20b: exact endpoint log moments using x=exp(-r).
The mixed moment is reduced to a summable rational series, with its
finite harmonic partial-fraction identity exposed separately. -/
namespace WeilDefect.MasterRecon.V10B20b

open MeasureTheory Set Filter
open scoped BigOperators

noncomputable def H (n : ℕ) : ℝ := ∑ j ∈ Finset.range n, 1/((j:ℝ)+1)
noncomputable def H₂ (n : ℕ) : ℝ := ∑ j ∈ Finset.range n, 1/((j:ℝ)+1)^2

theorem exp_neg_image : (fun r : ℝ => Real.exp (-r)) '' Ioi 0 = Ioo 0 1 := by
  ext x
  constructor
  · rintro ⟨r,hr,rfl⟩
    exact ⟨Real.exp_pos _,by rw [← Real.exp_zero]; exact Real.exp_lt_exp.mpr (by linarith [show 0<r from hr])⟩
  · intro hx
    refine ⟨-Real.log x,?_ ,?_⟩
    · exact neg_pos.mpr (Real.log_neg hx.1 hx.2)
    · change Real.exp (-(-Real.log x)) = x
      rw [neg_neg,Real.exp_log hx.1]

theorem log_moment (k m : ℕ) :
    (∫ x in Ioo (0:ℝ) 1, x^k*(-Real.log x)^m) =
      (m.factorial:ℝ)/((k:ℝ)+1)^(m+1) := by
  rw [← exp_neg_image]
  rw [integral_image_eq_integral_abs_deriv_smul (f := fun r : ℝ => Real.exp (-r))
    (f' := fun r => Real.exp (-r)*(-1)) measurableSet_Ioi
    (fun r _ => ((Real.hasDerivAt_exp (-r)).comp r (hasDerivAt_neg r)).hasDerivWithinAt)
    (fun r _ s _ h => neg_injective (Real.exp_injective h))]
  have he : (fun r : ℝ => |Real.exp (-r)*(-1)| •
      (Real.exp (-r)^k*(-Real.log (Real.exp (-r)))^m)) =
      fun r : ℝ => r^m*Real.exp (-((k:ℝ)+1)*r) := by
    funext r
    rw [abs_mul,abs_of_pos (Real.exp_pos _),abs_neg,abs_one,mul_one,smul_eq_mul,
      Real.log_exp,neg_neg,← Real.exp_nat_mul]
    calc
      _ = r^m*(Real.exp (-r)*Real.exp ((k:ℝ)*(-r))) := by ring
      _ = _ := by rw [← Real.exp_add]; congr 2; ring
  rw [he]
  have h := Real.integral_rpow_mul_exp_neg_mul_Ioi
    (a := (m:ℝ)+1) (by positivity) (show 0 < (k:ℝ)+1 by positivity)
  rw [Real.Gamma_nat_eq_factorial] at h
  have hm : (m:ℝ)+1 = ((m+1:ℕ):ℝ) := by push_cast; rfl
  have hpow : (m:ℝ)+1-1 = (m:ℝ) := by ring
  rw [hpow,Real.rpow_natCast,hm,Real.rpow_natCast,div_pow,one_pow] at h
  simpa only [div_eq_mul_inv,one_div,mul_comm,neg_mul,mul_one] using h

theorem log_moment_integrable (k m : ℕ) :
    IntegrableOn (fun x : ℝ => x^k*(-Real.log x)^m) (Ioo 0 1) :=
  Integrable.of_integral_ne_zero (by rw [log_moment]; positivity)

theorem log_left (k : ℕ) :
    (∫ x in Ioo (0:ℝ) 1, x^k*Real.log x) = -1/((k:ℝ)+1)^2 := by
  have h := log_moment k 1
  simp only [pow_one,Nat.factorial_one,Nat.cast_one,Nat.reduceAdd,mul_neg,integral_neg] at h
  simpa only [neg_div] using neg_eq_iff_eq_neg.mp h

theorem log_left_sq (k : ℕ) :
    (∫ x in Ioo (0:ℝ) 1, x^k*Real.log x^2) = 2/((k:ℝ)+1)^3 := by
  simpa [Nat.factorial,neg_sq] using log_moment k 2

noncomputable def mixedTerm (k j : ℕ) (x : ℝ) : ℝ :=
  x^(k+j+1)*(-Real.log x)/((j:ℝ)+1)

theorem mixed_term_integral (k j : ℕ) :
    (∫ x in Ioo (0:ℝ) 1, mixedTerm k j x) =
      1/(((j:ℝ)+1)*((k:ℝ)+(j:ℝ)+2)^2) := by
  unfold mixedTerm
  rw [integral_div]
  have h := log_moment (k+j+1) 1
  simp only [pow_one,Nat.factorial_one,Nat.cast_one,Nat.reduceAdd] at h
  rw [h]
  push_cast
  field_simp [show (j:ℝ)+1 ≠ 0 by positivity,show (k:ℝ)+(j:ℝ)+2 ≠ 0 by positivity]
  <;> ring

theorem mixed_partial_fraction (n m : ℝ) (hn : 0 < n) (hm : 0 < m) :
    1/(m*(n+m)^2) = (1/n^2)*(1/m-1/(m+n))-(1/n)*(1/(m+n)^2) := by
  field_simp [hn.ne',hm.ne',show m+n ≠ 0 by positivity,show n+m ≠ 0 by positivity]
  <;> ring

theorem mixed_series_integral (k : ℕ) :
    (∫ x in Ioo (0:ℝ) 1, x^k*Real.log x*Real.log (1-x)) =
      ∑' j : ℕ, 1/(((j:ℝ)+1)*((k:ℝ)+(j:ℝ)+2)^2) := by
  have hi (j : ℕ) : IntegrableOn (mixedTerm k j) (Ioo (0:ℝ) 1) := by
    unfold mixedTerm
    change Integrable _ (volume.restrict (Ioo (0:ℝ) 1))
    simpa only [div_eq_mul_inv,pow_one,mul_comm] using
      (log_moment_integrable (k+j+1) 1).const_mul (((j:ℝ)+1)⁻¹)
  have hn (j : ℕ) : (∫ x in Ioo (0:ℝ) 1, ‖mixedTerm k j x‖) =
      1/(((j:ℝ)+1)*((k:ℝ)+(j:ℝ)+2)^2) := by
    rw [← mixed_term_integral k j]
    apply setIntegral_congr_fun measurableSet_Ioo
    intro x hx
    change ‖mixedTerm k j x‖ = mixedTerm k j x
    rw [Real.norm_eq_abs,abs_of_nonneg]
    unfold mixedTerm
    have hl : 0 ≤ -Real.log x := neg_nonneg.mpr (Real.log_nonpos hx.1.le hx.2.le)
    exact div_nonneg (mul_nonneg (pow_nonneg hx.1.le _) hl) (by positivity)
  have hs : Summable (fun j : ℕ => ∫ x in Ioo (0:ℝ) 1, ‖mixedTerm k j x‖) := by
    simp_rw [hn]
    have h : Summable (fun j : ℕ => (1:ℝ)/((j:ℝ)+1)^2) := by
      simpa using ((hasSum_nat_add_iff' 1).mpr hasSum_zeta_two).summable
    apply Summable.of_nonneg_of_le (fun _ => by positivity) _ h
    intro j
    apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
    have h1 : (j:ℝ)+1 ≤ (k:ℝ)+(j:ℝ)+2 := by linarith [Nat.cast_nonneg (α := ℝ) k]
    have h2 := pow_le_pow_left₀ (by positivity) h1 2
    have h3 := mul_le_mul_of_nonneg_right (show (1:ℝ) ≤ (j:ℝ)+1 by linarith [Nat.cast_nonneg (α := ℝ) j])
      (sq_nonneg ((k:ℝ)+(j:ℝ)+2))
    nlinarith only [h2,h3]
  rw [← show (∑' j : ℕ, ∫ x in Ioo (0:ℝ) 1, mixedTerm k j x) =
      ∑' j : ℕ, 1/(((j:ℝ)+1)*((k:ℝ)+(j:ℝ)+2)^2) by simp_rw [mixed_term_integral]]
  rw [integral_tsum_of_summable_integral_norm hi hs]
  apply setIntegral_congr_fun measurableSet_Ioo
  intro x hx
  have hh := Real.hasSum_pow_div_log_of_abs_lt_one (by rw [abs_of_pos hx.1]; exact hx.2 : |x| < 1)
  have h := hh.mul_left (x^k*(-Real.log x))
  have he (j : ℕ) : x^k*(-Real.log x)*(x^(j+1)/((j:ℝ)+1)) = mixedTerm k j x := by
    unfold mixedTerm
    rw [show k+j+1 = k+(j+1) by omega,pow_add]
    ring
  rw [show (fun j : ℕ => x^k*(-Real.log x)*(x^(j+1)/((j:ℝ)+1))) = (fun j => mixedTerm k j x) from funext (fun j => he j)] at h
  change x^k*Real.log x*Real.log (1-x) = ∑' j : ℕ, mixedTerm k j x
  rw [h.tsum_eq]
  ring

end WeilDefect.MasterRecon.V10B20b

#print axioms WeilDefect.MasterRecon.V10B20b.exp_neg_image
#print axioms WeilDefect.MasterRecon.V10B20b.log_moment
#print axioms WeilDefect.MasterRecon.V10B20b.log_moment_integrable
#print axioms WeilDefect.MasterRecon.V10B20b.log_left
#print axioms WeilDefect.MasterRecon.V10B20b.log_left_sq
#print axioms WeilDefect.MasterRecon.V10B20b.mixed_term_integral
#print axioms WeilDefect.MasterRecon.V10B20b.mixed_partial_fraction
#print axioms WeilDefect.MasterRecon.V10B20b.mixed_series_integral
