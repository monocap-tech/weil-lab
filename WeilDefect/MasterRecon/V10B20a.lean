import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.MeasureTheory.Integral.Gamma
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.NumberTheory.ZetaValues

/-! V10B20a: scalar physical digamma integral from the pinned
partial fraction identity. No external theorem is silently imported.
The operator-valued Bochner translation attachment is a separate gate. -/
namespace WeilDefect.MasterRecon.V10B20a

open Complex MeasureTheory Set
open scoped BigOperators

def PartialFraction (z : ℂ) : Prop :=
  HasSum (fun n : ℕ => 1/((n:ℂ)+1)-1/(z+n+1))
    (Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z)

noncomputable def term (z : ℂ) (n : ℕ) (r : ℝ) : ℂ :=
  Complex.exp (-((n:ℂ)+1)*(r:ℂ)) * (1-Complex.exp (-z*(r:ℂ)))

theorem term_integrable (z : ℂ) (hz : 0 < z.re) (n : ℕ) :
    IntegrableOn (term z n) (Ioi (0:ℝ)) := by
  have h₁ := integrableOn_exp_mul_complex_Ioi
    (a := -((n:ℂ)+1)) (by simp only [Complex.neg_re,Complex.add_re,Complex.natCast_re,Complex.one_re]; linarith [Nat.cast_nonneg (α := ℝ) n] : (-((n:ℂ)+1)).re < 0) 0
  have h₂ := integrableOn_exp_mul_complex_Ioi
    (a := -(z+(n:ℂ)+1)) (by simp; linarith [Nat.cast_nonneg (α := ℝ) n]) 0
  apply (h₁.sub h₂).congr
  filter_upwards with r
  change Complex.exp (-((n:ℂ)+1)*(r:ℂ))-Complex.exp (-(z+n+1)*(r:ℂ)) = term z n r
  unfold term
  rw [mul_sub,mul_one,← Complex.exp_add]
  congr 2
  ring

theorem term_integral (z : ℂ) (hz : 0 < z.re) (n : ℕ) :
    (∫ r in Ioi (0:ℝ), term z n r) =
      1/((n:ℂ)+1)-1/(z+n+1) := by
  have h₁ : (-((n:ℂ)+1)).re < 0 := by
    simp only [Complex.neg_re,Complex.add_re,Complex.natCast_re,Complex.one_re]
    linarith [Nat.cast_nonneg (α := ℝ) n]
  have h₂ : (-(z+(n:ℂ)+1)).re < 0 := by simp; linarith [Nat.cast_nonneg (α := ℝ) n]
  have he : term z n = fun r : ℝ =>
      Complex.exp (-((n:ℂ)+1)*(r:ℂ))-Complex.exp (-(z+n+1)*(r:ℂ)) := by
    funext r
    unfold term
    rw [mul_sub,mul_one,← Complex.exp_add]
    congr 2
    ring
  rw [he,integral_sub (integrableOn_exp_mul_complex_Ioi h₁ 0)
    (integrableOn_exp_mul_complex_Ioi h₂ 0),
    integral_exp_mul_complex_Ioi h₁ 0,integral_exp_mul_complex_Ioi h₂ 0]
  simp only [Complex.ofReal_zero,mul_zero,Complex.exp_zero,neg_div,div_neg,neg_neg,one_div] <;> ring

theorem exp_difference (z : ℂ) (hz : 0 ≤ z.re) (r : ℝ) (hr : 0 ≤ r) :
    ‖1-Complex.exp (-z*(r:ℂ))‖ ≤ 2*‖z‖*r := by
  let w := -z*(r:ℂ)
  have hw : ‖w‖ = ‖z‖*r := by
    dsimp [w]
    rw [norm_mul,norm_neg,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hr]
  by_cases h : ‖w‖ ≤ 1
  · have h' := Complex.norm_exp_sub_one_le h
    rw [norm_sub_rev,hw] at h'
    exact h'.trans (le_of_eq (by ring))
  · have hRe : w.re ≤ 0 := by
      dsimp [w]
      simp only [Complex.mul_re,Complex.neg_re,Complex.neg_im,Complex.ofReal_re,
        Complex.ofReal_im,mul_zero,sub_zero]
      nlinarith
    have hE : ‖Complex.exp w‖ ≤ 1 := by
      rw [Complex.norm_exp,← Real.exp_zero]
      exact Real.exp_le_exp.mpr hRe
    have h' := norm_sub_le (1:ℂ) (Complex.exp w)
    rw [norm_one,hw] at *
    change ‖1-Complex.exp w‖ ≤ _
    nlinarith

theorem term_norm_bound (z : ℂ) (hz : 0 ≤ z.re) (n : ℕ) (r : ℝ) (hr : 0 ≤ r) :
    ‖term z n r‖ ≤ (2*‖z‖)*r*Real.exp (-((n:ℝ)+1)*r) := by
  unfold term
  rw [norm_mul,Complex.norm_exp]
  have he : (-((n:ℂ)+1)*(r:ℂ)).re = -((n:ℝ)+1)*r := by simp
  rw [he]
  have h := mul_le_mul_of_nonneg_left (exp_difference z hz r hr) (Real.exp_pos (-((n:ℝ)+1)*r)).le
  nlinarith only [h]

theorem exp_moment (a : ℝ) (ha : 0 < a) :
    (∫ r in Ioi (0:ℝ), r*Real.exp (-a*r)) = 1/a^2 := by
  have h := Real.integral_rpow_mul_exp_neg_mul_Ioi (a := (2:ℝ)) (by norm_num) ha
  have hg : Real.Gamma (2:ℝ) = 1 := by simpa using Real.Gamma_nat_eq_factorial 1
  rw [hg,mul_one] at h
  rw [show (2:ℝ)-1=1 by norm_num] at h
  simpa only [Real.rpow_one,Real.rpow_two,div_pow,one_pow,neg_mul,mul_comm] using h

theorem norm_summable (z : ℂ) (hz : 0 < z.re) :
    Summable (fun n : ℕ => ∫ r in Ioi (0:ℝ), ‖term z n r‖) := by
  have hs : Summable (fun n : ℕ => (1:ℝ)/((n:ℝ)+1)^2) := by
    simpa using ((hasSum_nat_add_iff' 1).mpr hasSum_zeta_two).summable
  apply Summable.of_nonneg_of_le (fun _ => integral_nonneg fun _ => norm_nonneg _)
    _ (show Summable (fun n : ℕ => (2*‖z‖)*(1/((n:ℝ)+1)^2)) from hs.mul_left _)
  intro n
  let a : ℝ := (n:ℝ)+1
  have ha : 0 < a := by dsimp [a]; positivity
  have hi : IntegrableOn (fun r : ℝ => r*Real.exp (-a*r)) (Ioi (0:ℝ)) :=
    Integrable.of_integral_ne_zero (by rw [exp_moment a ha]; positivity)
  calc
    _ ≤ ∫ r in Ioi (0:ℝ), (2*‖z‖)*(r*Real.exp (-a*r)) := by
      apply setIntegral_mono_on (term_integrable z hz n).norm (hi.const_mul _) measurableSet_Ioi
      intro r hr
      simpa only [a,mul_assoc] using term_norm_bound z hz.le n r (le_of_lt hr)
    _ = _ := by rw [integral_const_mul,exp_moment a ha]

theorem scalar_series_integral (z : ℂ) (hz : 0 < z.re) (hs : PartialFraction z) :
    (∫ r in Ioi (0:ℝ), ∑' n : ℕ, term z n r) =
      Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z := by
  rw [← integral_tsum_of_summable_integral_norm (term_integrable z hz) (norm_summable z hz)]
  simp_rw [term_integral z hz]
  exact hs.tsum_eq

theorem pointwise_geometric (z : ℂ) (r : ℝ) (hr : 0 < r) :
    (∑' n : ℕ, term z n r) =
      Complex.exp (-(r:ℂ))*(1-Complex.exp (-z*(r:ℂ)))/
        (1-Complex.exp (-(r:ℂ))) := by
  let q := Complex.exp (-(r:ℂ))
  have hq : ‖q‖ < 1 := by
    dsimp [q]
    rw [Complex.norm_exp,Complex.neg_re,Complex.ofReal_re,← Real.exp_zero]
    exact Real.exp_lt_exp.mpr (by linarith)
  have he (n : ℕ) : term z n r = q^n*(q*(1-Complex.exp (-z*(r:ℂ)))) := by
    unfold term q
    rw [← Complex.exp_nat_mul,← mul_assoc,← Complex.exp_add]
    congr 2
    ring
  simp_rw [he]
  rw [tsum_mul_right,(hasSum_geometric_of_norm_lt_one hq).tsum_eq]
  rw [div_eq_mul_inv]
  ring

theorem scalar_integral_receiver (z : ℂ) (hz : 0 < z.re) (hs : PartialFraction z) :
    (∫ r in Ioi (0:ℝ), Complex.exp (-(r:ℂ))*(1-Complex.exp (-z*(r:ℂ)))/
        (1-Complex.exp (-(r:ℂ)))) =
      Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z := by
  rw [← scalar_series_integral z hz hs]
  apply setIntegral_congr_fun measurableSet_Ioi
  intro r hr
  exact (pointwise_geometric z r hr).symm

end WeilDefect.MasterRecon.V10B20a

#print axioms WeilDefect.MasterRecon.V10B20a.term_integrable
#print axioms WeilDefect.MasterRecon.V10B20a.term_integral
#print axioms WeilDefect.MasterRecon.V10B20a.exp_difference
#print axioms WeilDefect.MasterRecon.V10B20a.term_norm_bound
#print axioms WeilDefect.MasterRecon.V10B20a.exp_moment
#print axioms WeilDefect.MasterRecon.V10B20a.norm_summable
#print axioms WeilDefect.MasterRecon.V10B20a.scalar_series_integral
#print axioms WeilDefect.MasterRecon.V10B20a.pointwise_geometric
#print axioms WeilDefect.MasterRecon.V10B20a.scalar_integral_receiver
