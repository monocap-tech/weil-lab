import WeilDefect.MasterRecon.V10B8b
import WeilDefect.MasterRecon.V10B8f

/-! Literal Archimedean diagonal, with the negative angular-frequency
substitution and its Jacobian made explicit. -/
namespace WeilDefect.MasterRecon.V10B8g

open MeasureTheory Complex Filter
open scoped FourierTransform InnerProduct ComplexConjugate
open V08I (logCarrier physicalInclusion FullL2 logWeight)
open V10B8e (gammaSymbol residual spectralPhysical correction archOperator)

theorem paperFT_scaled (f : ℝ → ℂ) (u : ℝ) :
    V10B8a.paperFT f ((-(2*Real.pi*u):ℝ):ℂ) = 𝓕 f u := by
  rw [V10B8a.paperFT_mellin,← V08H.angularFourier_scaled]
  rw [← V09B.mellin_imaginary_axis]
  congr 1
  push_cast
  ring

theorem paperFT_physical_ae (t : ℝ) (g : logCarrier t) (f : ℝ → ℂ)
    (hae : (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f) :
    (fun u : ℝ => V10B8a.paperFT f ((-(2*Real.pi*u):ℝ):ℂ)) =ᵐ[volume]
      (spectralPhysical t g : ℝ → ℂ) := by
  have hi := V08K.supported_integrable t _ (V08I.physicalInclusion_support t g)
  filter_upwards [V08H.l2_fourier_integral_ae (physicalInclusion t g) hi] with u hu
  change _ = (𝓕 (physicalInclusion t g) : FullL2) u
  rw [hu,← paperFT_scaled, V10B8a.paperFT_mellin,V10B8a.paperFT_mellin]
  exact V10B8a.mellin_congr_ae _ _ hae.symm _

theorem correction_integral (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (g : logCarrier t) :
    inner ℂ (correction t hd C hC g) g =
      ∫ u : ℝ, (residual u:ℂ)*(‖spectralPhysical t g u‖^2:ℝ) := by
  unfold correction
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]
  rw [L2.inner_def]
  apply integral_congr_ae
  filter_upwards [V10B8e.realMultiplier_ae residual hd C hC (spectralPhysical t g)] with u hu
  rw [hu,inner_smul_left]
  change conj (residual u:ℂ)*inner ℂ (spectralPhysical t g u) (spectralPhysical t g u) = _
  rw [Complex.conj_ofReal,inner_self_eq_norm_sq_to_K]
  rfl

theorem arch_integral (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (g : logCarrier t) :
    inner ℂ (archOperator t hd C hC g) g =
      ∫ u : ℝ, (gammaSymbol u:ℂ)*(‖spectralPhysical t g u‖^2:ℝ) := by
  let F := spectralPhysical t g
  have hw : Integrable (fun u : ℝ => logWeight u * ‖F u‖^2) :=
    V08I.logCarrier_energy_integrable t g
  have hdi : Integrable (fun u : ℝ => (residual u:ℂ)*(‖F u‖^2:ℝ)) := by
    have h := L2.integrable_inner (𝕜 := ℂ) (V10B8e.realMultiplier residual hd C hC F) F
    apply h.congr
    filter_upwards [V10B8e.realMultiplier_ae residual hd C hC F] with u hu
    rw [hu,inner_smul_left,Complex.conj_ofReal,inner_self_eq_norm_sq_to_K]
    rfl
  have hwc : Integrable (fun u : ℝ => (logWeight u:ℂ)*(‖F u‖^2:ℝ)) := by
    simpa only [Complex.ofReal_mul] using Complex.ofRealCLM.integrable_comp hw
  unfold archOperator
  rw [ContinuousLinearMap.add_apply,ContinuousLinearMap.one_apply,inner_add_left,
    inner_self_eq_norm_sq_to_K,correction_integral,
    V08I.logCarrier_energy]
  change ((∫ u, logWeight u * ‖F u‖^2):ℝ):ℂ + _ = _
  rw [← integral_ofReal,← integral_add]
  · apply integral_congr_ae
    filter_upwards with u
    simp only [Complex.ofReal_mul,residual,Complex.ofReal_sub]
    ring
  · simpa only [Complex.ofReal_mul] using hwc
  · exact hdi

theorem angular_integral (k : ℝ → ℂ) :
    (1/(2*Real.pi):ℂ) * (∫ r : ℝ, V10B8a.paperFT k r *
      (V10B8b.gammaBracket r:ℂ)) =
    ∫ u : ℝ, V10B8a.paperFT k ((-(2*Real.pi*u):ℝ):ℂ)*(gammaSymbol u:ℂ) := by
  let H : ℝ → ℂ := fun r => V10B8a.paperFT k r*(V10B8b.gammaBracket r:ℂ)
  have hfun : (fun u : ℝ => V10B8a.paperFT k ((-(2*Real.pi*u):ℝ):ℂ)*
      (gammaSymbol u:ℂ)) = fun u => H ((-(2*Real.pi))*u) := by
    funext u
    simp only [H,V10B8b.gammaBracket,gammaSymbol,neg_mul]
  rw [hfun,Measure.integral_comp_mul_left H]
  have he : |(-(2*Real.pi))⁻¹| = (2*Real.pi)⁻¹ := by
    rw [inv_neg,abs_neg,abs_of_pos (by positivity)]
  rw [he,Complex.real_smul]
  push_cast
  rfl

theorem arch_literal (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (g : logCarrier t) (f : ℝ → ℂ)
    (hf : Continuous f) (hfc : HasCompactSupport f)
    (hae : (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f) :
    inner ℂ (archOperator t hd C hC g) g =
      (1/(2*Real.pi):ℂ)*(∫ r : ℝ,
        V10B8a.paperFT (V10B8a.weilTest f f) r*(V10B8b.gammaBracket r:ℂ)) := by
  rw [arch_integral,angular_integral]
  apply integral_congr_ae
  filter_upwards [paperFT_physical_ae t g f hae] with u hu
  rw [V10B8a.paperFT_weilTest hf hf hfc hfc,Complex.conj_ofReal,hu]
  have h : spectralPhysical t g u * conj (spectralPhysical t g u) =
      (‖spectralPhysical t g u‖^2:ℝ) := by
    apply Complex.ext
    · simp only [Complex.mul_re,Complex.conj_re,Complex.conj_im,Complex.ofReal_re,
        Complex.sq_norm,Complex.normSq_apply]
      ring
    · simp [Complex.mul_im]
      ring
  rw [h,mul_comm]

end WeilDefect.MasterRecon.V10B8g

#print axioms WeilDefect.MasterRecon.V10B8g.paperFT_scaled
#print axioms WeilDefect.MasterRecon.V10B8g.paperFT_physical_ae
#print axioms WeilDefect.MasterRecon.V10B8g.correction_integral
#print axioms WeilDefect.MasterRecon.V10B8g.arch_integral
#print axioms WeilDefect.MasterRecon.V10B8g.angular_integral
#print axioms WeilDefect.MasterRecon.V10B8g.arch_literal
