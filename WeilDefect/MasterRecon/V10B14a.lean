import WeilDefect.MasterRecon.V10B8h

/-! Explicit lower-order arithmetic constants, retaining the certified
uniform Archimedean residual as a parameter. No numerical positivity. -/
namespace WeilDefect.MasterRecon.V10B14a

open MeasureTheory Set Complex
open scoped InnerProduct BigOperators ComplexConjugate
open V08I (FullL2 logCarrier physicalInclusion)
open V10B8c (vector evalRestricted)
open V10B8d (primeBank primeWeight physicalPrime)

theorem restrict_norm (t : ℝ) (f : FullL2) :
    ‖V08K.restrictPhysical t f‖ ≤ ‖f‖ :=
  norm_Lp_toLp_restrict_le (Icc (-t) t) f

theorem vector_sq_bound (t a : ℝ) (ht : 0 ≤ t) :
    ‖vector t a ht‖^2 ≤ (2*t)*Real.exp (2 * |a| * t) := by
  let μ := V08K.supportMeasure t
  have hi : Integrable (fun x => ‖vector t a ht x‖^2) μ :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable (vector t a ht))).mp
      (Lp.memLp (vector t a ht))
  have hc : Integrable (fun _ : ℝ => Real.exp (2 * |a| * t)) μ := integrable_const _
  rw [V08G.l2_norm_sq_integral μ]
  calc
    _ ≤ ∫ x, Real.exp (2 * |a| * t) ∂μ := by
      apply integral_mono_ae hi hc
      filter_upwards [MemLp.coeFn_toLp (V10B8c.expVector_mem t a ht),
        V08K.supportMeasure_bound t] with x hx hx'
      rw [show vector t a ht x = V10B8c.expVector a x from hx]
      unfold V10B8c.expVector
      rw [Complex.norm_real,Real.norm_eq_abs,abs_of_pos (Real.exp_pos _),← Real.exp_nat_mul]
      apply Real.exp_le_exp.mpr
      have h := mul_le_mul_of_nonneg_left hx' (abs_nonneg a)
      have ha := le_abs_self (a * x)
      rw [abs_mul] at ha
      norm_num
      linarith
    _ = _ := by
      rw [integral_const,smul_eq_mul]
      simp [μ,V08K.supportMeasure,Measure.real,Real.volume_Icc,sub_neg_eq_add,ht]
      ring

theorem eval_norm_half (t : ℝ) (ht : 0 ≤ t) (a : ℝ) (ha : |a| = 1/2) :
    ‖evalRestricted t a ht‖ ≤ Real.sqrt (2*t*Real.exp t) := by
  have hs := vector_sq_bound t a ht
  rw [ha,show 2*(1/2:ℝ)*t = t by ring] at hs
  have hv : ‖vector t a ht‖ ≤ Real.sqrt (2*t*Real.exp t) := by
    apply (sq_le_sq₀ (norm_nonneg _) (Real.sqrt_nonneg _)).mp
    rwa [Real.sq_sqrt (by positivity)]
  apply ContinuousLinearMap.opNorm_le_bound _ (Real.sqrt_nonneg _)
  intro f
  change ‖inner ℂ (vector t a ht) (V08K.restrictPhysical t f)‖ ≤ _
  exact (norm_inner_le_norm _ _).trans
    (mul_le_mul hv (restrict_norm t f) (norm_nonneg _) (Real.sqrt_nonneg _))

noncomputable def primeBudget (t : ℝ) : ℝ :=
  2*(∑ n ∈ primeBank t, primeWeight n)

theorem primeWeight_nonneg (n : ℕ) : 0 ≤ primeWeight n :=
  div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _)

theorem primeBudget_nonneg (t : ℝ) : 0 ≤ primeBudget t := by
  unfold primeBudget
  exact mul_nonneg (by norm_num) (Finset.sum_nonneg fun n _ => primeWeight_nonneg n)

theorem prime_norm (t : ℝ) : ‖physicalPrime t‖ ≤ primeBudget t := by
  apply ContinuousLinearMap.opNorm_le_bound _ (primeBudget_nonneg t)
  intro f
  unfold physicalPrime primeBudget
  rw [ContinuousLinearMap.sum_apply]
  calc
    _ ≤ ∑ n ∈ primeBank t, ‖((primeWeight n:ℂ) • V10B8d.shiftPair (Real.log n)) f‖ :=
      norm_sum_le _ _
    _ ≤ ∑ n ∈ primeBank t, primeWeight n*(2*‖f‖) := by
      apply Finset.sum_le_sum
      intro n hn
      rw [ContinuousLinearMap.smul_apply,norm_smul,Complex.norm_real,
        Real.norm_eq_abs,abs_of_nonneg (primeWeight_nonneg n)]
      exact mul_le_mul_of_nonneg_left (V10B8d.shiftPair_norm (Real.log n) f)
        (primeWeight_nonneg n)
    _ = _ := by rw [← Finset.sum_mul]; ring

noncomputable def defectBudget (t C : ℝ) : ℝ :=
  C+4*t*Real.exp t+primeBudget t

theorem defectBudget_nonneg (t C : ℝ) (ht : 0 ≤ t) (hC : 0 ≤ C) :
    0 ≤ defectBudget t C := by
  unfold defectBudget
  have h := primeBudget_nonneg t
  positivity

theorem arithmetic_defect (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (g : logCarrier t) :
    ‖g‖^2-defectBudget t C*‖physicalInclusion t g‖^2 ≤
      (inner ℂ (V10B8h.arithmeticOperator t ht hd C hC g) g).re := by
  have hp := V10B8h.pole_physical_bound t ht g
  have hd' := V10B8h.prime_physical_bound t g
  have ha := V10B8e.arch_lower t hd C hC g
  have hE := eval_norm_half t ht (1/2) (by norm_num)
  have hF := eval_norm_half t ht (-1/2) (by norm_num)
  have hEF := mul_le_mul hE hF (norm_nonneg _) (Real.sqrt_nonneg _)
  rw [← pow_two,Real.sq_sqrt (by positivity)] at hEF
  have hp' := mul_le_mul_of_nonneg_right
    (show 2*‖evalRestricted t (1/2) ht‖*‖evalRestricted t (-1/2) ht‖ ≤
      4*t*Real.exp t by nlinarith only [hEF]) (sq_nonneg ‖physicalInclusion t g‖)
  have hd'' := mul_le_mul_of_nonneg_right (prime_norm t) (sq_nonneg ‖physicalInclusion t g‖)
  have hpr := Complex.abs_re_le_norm (inner ℂ (V10B8c.poleOperator t ht g) g)
  have hdr := Complex.abs_re_le_norm (inner ℂ (V10B8d.primeOperator t g) g)
  have hpl := neg_abs_le (inner ℂ (V10B8c.poleOperator t ht g) g).re
  have hdu := le_abs_self (inner ℂ (V10B8d.primeOperator t g) g).re
  unfold V10B8h.arithmeticOperator defectBudget
  rw [ContinuousLinearMap.sub_apply,ContinuousLinearMap.add_apply,inner_sub_left,
    inner_add_left,Complex.sub_re,Complex.add_re]
  nlinarith only [hp,hd',ha,hp',hd'',hpr,hdr,hpl,hdu]

end WeilDefect.MasterRecon.V10B14a

#print axioms WeilDefect.MasterRecon.V10B14a.restrict_norm
#print axioms WeilDefect.MasterRecon.V10B14a.vector_sq_bound
#print axioms WeilDefect.MasterRecon.V10B14a.eval_norm_half
#print axioms WeilDefect.MasterRecon.V10B14a.primeWeight_nonneg
#print axioms WeilDefect.MasterRecon.V10B14a.primeBudget_nonneg
#print axioms WeilDefect.MasterRecon.V10B14a.prime_norm
#print axioms WeilDefect.MasterRecon.V10B14a.defectBudget_nonneg
#print axioms WeilDefect.MasterRecon.V10B14a.arithmetic_defect
