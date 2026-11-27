import WeilDefect.MasterRecon.V10B13a

/-! Exact logarithmic cutoff weight, without replacing the angular
frequency by the smaller unscaled frequency. -/
namespace WeilDefect.MasterRecon.V10B15b

open MeasureTheory Set Filter
open scoped FourierTransform InnerProduct
open V08I (FullL2 logCarrier physicalInclusion logWeight)

theorem weight_on_tail (R : ℝ) (hR : 0 ≤ R) (u : ℝ) (hu : R < |u|) :
    Real.log (2+2*Real.pi*R) ≤ logWeight u := by
  unfold logWeight
  rw [abs_mul,abs_of_nonneg (by positivity : 0 ≤ 2*Real.pi)]
  apply Real.log_le_log (by positivity)
  have h := mul_le_mul_of_nonneg_left hu.le (show 0 ≤ 2*Real.pi by positivity)
  linarith

theorem cutoff_sq (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (g : logCarrier t) :
    ‖physicalInclusion t g-V08K.physicalCutoff t R ht hR g‖^2 ≤
      ‖g‖^2/Real.log (2+2*Real.pi*R) := by
  let f : ℝ → ℂ := fun u => (𝓕 (physicalInclusion t g) : FullL2) u
  let A : Set ℝ := {u | R < |u|}
  let L := Real.log (2+2*Real.pi*R)
  have hL : 0 < L := by dsimp [L]; apply Real.log_pos; nlinarith [Real.pi_pos]
  have hA : MeasurableSet A := measurableSet_lt measurable_const measurable_id.abs
  have hf : Integrable (fun u => ‖f u‖^2) :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable
      (𝓕 (physicalInclusion t g) : FullL2))).mp (Lp.memLp _)
  have hw : Integrable (fun u => logWeight u*‖f u‖^2) :=
    V08I.logCarrier_energy_integrable t g
  have h₁ : (∫ u in A, L*‖f u‖^2) ≤ ∫ u in A, logWeight u*‖f u‖^2 := by
    apply setIntegral_mono_on (hf.const_mul L).integrableOn hw.integrableOn hA
    intro u hu
    exact mul_le_mul_of_nonneg_right (weight_on_tail R hR u hu) (sq_nonneg _)
  have h₂ : (∫ u in A, logWeight u*‖f u‖^2) ≤ ∫ u, logWeight u*‖f u‖^2 :=
    setIntegral_le_integral hw (Eventually.of_forall fun u =>
      mul_nonneg (V08I.logWeight_pos u).le (sq_nonneg _))
  rw [integral_const_mul] at h₁
  have he : (∫ u, logWeight u*‖f u‖^2) = ‖g‖^2 :=
    (V08I.logCarrier_energy t g).symm
  rw [he] at h₂
  rw [V08K.physicalCutoff_tail]
  exact (le_div_iff₀ hL).mpr (by linarith [h₁.trans h₂])

theorem cutoff_norm (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (g : logCarrier t) :
    ‖physicalInclusion t g-V08K.physicalCutoff t R ht hR g‖ ≤
      (Real.sqrt (Real.log (2+2*Real.pi*R)))⁻¹*‖g‖ := by
  have hL : 0 < Real.log (2+2*Real.pi*R) := by
    apply Real.log_pos
    nlinarith [Real.pi_pos]
  apply (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp
  rw [mul_pow,inv_pow,Real.sq_sqrt hL.le,← div_eq_inv_mul]
  exact cutoff_sq t R ht hR g

theorem orthogonal_error {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (a b : H) (A B : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B)
    (ha : ‖a‖ ≤ A) (hb : ‖b‖ ≤ B) (ho : inner ℂ a b = 0) :
    ‖a+b‖ ≤ Real.sqrt (A^2+B^2) := by
  have h := norm_add_sq_eq_norm_sq_add_norm_sq_of_inner_eq_zero a b ho
  apply (sq_le_sq₀ (norm_nonneg _) (Real.sqrt_nonneg _)).mp
  rw [h,Real.sq_sqrt (by positivity)]
  exact add_le_add ((sq_le_sq₀ (norm_nonneg _) hA).mpr ha)
    ((sq_le_sq₀ (norm_nonneg _) hB).mpr hb)

end WeilDefect.MasterRecon.V10B15b

#print axioms WeilDefect.MasterRecon.V10B15b.weight_on_tail
#print axioms WeilDefect.MasterRecon.V10B15b.cutoff_sq
#print axioms WeilDefect.MasterRecon.V10B15b.cutoff_norm
#print axioms WeilDefect.MasterRecon.V10B15b.orthogonal_error
