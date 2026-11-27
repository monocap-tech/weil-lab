import WeilDefect.MasterRecon.V08K
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.PiL2

/-! V10B13a: explicit moment truncation of the certified compact
physical inclusion. The radius is in Mathlib Fourier coordinates. -/
namespace WeilDefect.MasterRecon.V10B13a

open MeasureTheory Set Filter
open scoped FourierTransform InnerProduct BigOperators ENNReal
open V08I (FullL2 logCarrier physicalInclusion logWeight)
open V08K (supportMeasure restrictPhysical)
local instance bandCompact (R : ℝ) : CompactSpace (V08E.Band R) :=
  compactSpace_Icc (-R) R

noncomputable def input (t : ℝ) : logCarrier t →L[ℂ] V08E.PhysicalL1 (supportMeasure t) :=
  (V08F.physicalL1Inclusion (supportMeasure t)).comp
    ((restrictPhysical t).comp (physicalInclusion t))

noncomputable def moment (t : ℝ) (ht : 0 ≤ t) (j : ℕ) : logCarrier t →L[ℂ] ℂ :=
  (V08E.moment (supportMeasure t) t ht (V08K.supportMeasure_bound t) j).comp (input t)

noncomputable def bandPolynomial (t R : ℝ) (ht : 0 ≤ t) (n : ℕ) :
    logCarrier t →L[ℂ] C(V08E.Band (2*Real.pi*R),ℂ) :=
  ∑ j ∈ Finset.range n, (moment t ht j).smulRight (V08E.frequencyMonomial (2*Real.pi*R) j)

noncomputable def out (R : ℝ) (hR : 0 ≤ R) :
    C(V08E.Band (2*Real.pi*R),ℂ) →L[ℂ] FullL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).symm.toContinuousLinearEquiv.toContinuousLinearMap.comp
    ((V08G.zeroBandCLM volume R hR isCompact_Icc.measure_lt_top.ne).comp
      (ContinuousMap.compCLM ℂ ℂ (V08K.scaleBand R)))

noncomputable def approximation (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ) :
    logCarrier t →L[ℂ] FullL2 :=
  (out R hR).comp (bandPolynomial t R ht n)

theorem approximation_zero (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (g : logCarrier t) (hg : ∀ j < n, moment t ht j g = 0) :
    approximation t R ht hR n g = 0 := by
  unfold approximation bandPolynomial
  rw [ContinuousLinearMap.comp_apply,ContinuousLinearMap.sum_apply]
  have he : (∑ j ∈ Finset.range n, (moment t ht j).smulRight
      (V08E.frequencyMonomial (2*Real.pi*R) j) g) = 0 := by
    apply Finset.sum_eq_zero
    intro j hj
    rw [ContinuousLinearMap.smulRight_apply,hg j (Finset.mem_range.mp hj),zero_smul]
  rw [he,map_zero]

noncomputable def remainderBound (t R : ℝ) (n : ℕ) : ℝ :=
  2*((2*Real.pi*R)*t)^n/(n.factorial:ℝ)

theorem band_error (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (hn : (2*Real.pi*R)*t/((n:ℝ)+1) ≤ 1/2) (g : logCarrier t) :
    ‖V08E.boundedFourier (supportMeasure t) t (2*Real.pi*R) ht
      (V08K.supportMeasure_bound t) (input t g) - bandPolynomial t R ht n g‖ ≤
      remainderBound t R n * ‖input t g‖ := by
  let f := input t g
  have hf : Integrable (fun x : ℝ => f x) (supportMeasure t) :=
    memLp_one_iff_integrable.mp (Lp.memLp f)
  apply (ContinuousMap.norm_le _ (by unfold remainderBound; positivity)).mpr
  intro u
  rw [ContinuousMap.sub_apply,V08E.boundedFourier_integral _ _ _ ht (by positivity)
    (V08K.supportMeasure_bound t)]
  have hp : bandPolynomial t R ht n g u =
      ∫ x, V08D.kernelPolynomial n (u:ℝ) x * f x ∂supportMeasure t := by
    unfold bandPolynomial
    simp only [ContinuousLinearMap.sum_apply,ContinuousMap.sum_apply,
      ContinuousLinearMap.smulRight_apply,ContinuousMap.smul_apply,smul_eq_mul]
    simp only [moment,ContinuousLinearMap.comp_apply,V08E.moment_apply]
    conv_rhs => enter [1,x]; rw [V08D.kernelPolynomial_separated,Finset.sum_mul]
    rw [integral_finset_sum]
    · apply Finset.sum_congr rfl
      intro j hj
      change (∫ x, (x:ℂ)^j*f x ∂supportMeasure t) *
        V08E.frequencyMonomial (2*Real.pi*R) j u = _
      rw [mul_comm,← integral_const_mul]
      apply integral_congr_ae
      filter_upwards with x
      unfold V08E.frequencyMonomial
      ring
    · intro j hj
      exact (V08E.moment_integrable (supportMeasure t) t
        (V08K.supportMeasure_bound t) j f).const_mul _
  rw [hp]
  have hker : Integrable (fun x => V08D.fourierKernel (u:ℝ) x*f x) (supportMeasure t) := by
    apply hf.bdd_mul (by unfold V08D.fourierKernel; fun_prop) (c := 1)
    filter_upwards with x
    unfold V08D.fourierKernel
    simp [Complex.norm_exp,Complex.mul_re,Complex.mul_im]
  have hpoly : Integrable (fun x => V08D.kernelPolynomial n (u:ℝ) x*f x) (supportMeasure t) := by
    simp only [V08D.kernelPolynomial_separated,Finset.sum_mul]
    apply integrable_finset_sum
    intro j hj
    simpa only [mul_assoc] using (V08E.moment_integrable (supportMeasure t) t
      (V08K.supportMeasure_bound t) j f).const_mul
        ((-Complex.I*((u:ℝ):ℂ))^j/(j.factorial:ℂ))
  rw [← integral_sub hker hpoly,L1.norm_eq_integral_norm,← integral_const_mul]
  apply norm_integral_le_of_norm_le (hf.norm.const_mul _)
  filter_upwards [V08K.supportMeasure_bound t] with x hx
  rw [← sub_mul,norm_mul]
  apply mul_le_mul_of_nonneg_right _ (norm_nonneg _)
  simpa only [remainderBound, mul_comm,div_eq_mul_inv,mul_assoc,mul_left_comm] using
    V08D.kernel_remainder n (2*Real.pi*R) t (u:ℝ) x (abs_le.mpr u.property) hx hn

theorem cutoff_error (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (g : logCarrier t) :
    ‖physicalInclusion t g-V08K.physicalCutoff t R ht hR g‖ ≤
      (Real.sqrt (Real.log (2+R)))⁻¹*‖g‖ := by
  let f : ℝ → ℂ := fun u => (𝓕 (physicalInclusion t g) : FullL2) u
  have hF : Integrable (fun u => ‖f u‖^2) :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable
      (𝓕 (physicalInclusion t g) : FullL2))).mp (Lp.memLp _)
  have hdom (u : ℝ) : Real.log (2+|u|)*‖f u‖^2 ≤ logWeight u*‖f u‖^2 :=
    mul_le_mul_of_nonneg_right (V08K.logWeight_dominates u) (sq_nonneg _)
  have hw : Integrable (fun u => Real.log (2+|u|)*‖f u‖^2) := by
    apply (V08I.logCarrier_energy_integrable t g).mono_nonneg
    · exact (Continuous.log (by fun_prop) (by intro u; positivity)).aestronglyMeasurable.mul hF.aestronglyMeasurable
    · exact Eventually.of_forall fun u => mul_nonneg (Real.log_nonneg (by linarith [abs_nonneg u])) (sq_nonneg _)
    · exact Eventually.of_forall hdom
  have h := V08C.log_tail_bound volume f R hR hF hw
  have he := integral_mono hw (V08I.logCarrier_energy_integrable t g) hdom
  rw [← V08I.logCarrier_energy t g] at he
  have hp : 0 < Real.log (2+R) := Real.log_pos (by linarith)
  rw [← V08K.physicalCutoff_tail t R ht hR g] at h
  apply (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp
  rw [mul_pow,inv_pow,Real.sq_sqrt hp.le,← div_eq_inv_mul]
  exact h.trans (div_le_div_of_nonneg_right he hp.le)

theorem approximation_error (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (hn : (2*Real.pi*R)*t/((n:ℝ)+1) ≤ 1/2) :
    ‖physicalInclusion t-approximation t R ht hR n‖ ≤
      (Real.sqrt (Real.log (2+R)))⁻¹ +
        ‖out R hR‖*remainderBound t R n*‖input t‖ := by
  apply ContinuousLinearMap.opNorm_le_bound _ (by unfold remainderBound; positivity)
  intro g
  let P := V08K.physicalCutoff t R ht hR
  let J := physicalInclusion t
  let F := approximation t R ht hR n
  have hsplit : (J-F) g = (J g-P g)+(P g-F g) := by simp only [ContinuousLinearMap.sub_apply]; abel
  have hband : ‖P g-F g‖ ≤ ‖out R hR‖*(remainderBound t R n*‖input t g‖) := by
    let v := V08E.boundedFourier (supportMeasure t) t (2*Real.pi*R) ht
      (V08K.supportMeasure_bound t) (input t g)-bandPolynomial t R ht n g
    have he : P g-F g = out R hR v := by
      rw [map_sub]
      rfl
    rw [he]
    exact ((out R hR).le_opNorm v).trans
      (mul_le_mul_of_nonneg_left (band_error t R ht hR n hn g) (norm_nonneg _))
  rw [hsplit]
  have hb := mul_le_mul_of_nonneg_left ((input t).le_opNorm g)
    (show 0 ≤ ‖out R hR‖*remainderBound t R n by unfold remainderBound; positivity)
  nlinarith only [norm_add_le (J g-P g) (P g-F g),cutoff_error t R ht hR g,hband,hb]

end WeilDefect.MasterRecon.V10B13a

#print axioms WeilDefect.MasterRecon.V10B13a.approximation_zero
#print axioms WeilDefect.MasterRecon.V10B13a.band_error
#print axioms WeilDefect.MasterRecon.V10B13a.cutoff_error
#print axioms WeilDefect.MasterRecon.V10B13a.approximation_error
