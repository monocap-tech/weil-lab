import WeilDefect.Arithmetic.ActualZetaOriginalCollarArchLower
import WeilDefect.Arithmetic.ActualZetaOriginalRealOddSchwartzFullSource
import WeilDefect.Arithmetic.ActualZetaOriginalSupportCoercivityTransfer

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-! NF600: attach the whole literal EF to the normalized physical
Fourier integral and the two bounded arithmetic terms. No sampled
gamma truncation, no unproved positivity of the zero-side form. -/

def neutralNF600Arch (s : 𝓢(ℝ,ℂ)) : ℝ :=
  ∫ ξ : ℝ, Zeta23.EF.gammaBracket (-2*Real.pi*ξ)*neutralNF600Density s ξ

theorem neutralNF600Arch_integrable (s : 𝓢(ℝ,ℂ)) :
    Integrable (fun ξ => Zeta23.EF.gammaBracket (-2*Real.pi*ξ)*neutralNF600Density s ξ) := by
  obtain ⟨D,hD,hb⟩ := neutralActualZetaArchimedeanSymbol_bound
  let v := 𝓕 s
  obtain ⟨M,hM0,hM⟩ := v.decay 0 0
  have hi0 : Integrable (fun ξ : ℝ => ‖v ξ‖) := v.integrable.norm
  have hi1 : Integrable (fun ξ : ℝ => ‖ξ‖ * ‖v ξ‖) := by
    simpa only [pow_one] using v.integrable_pow_mul volume 1
  have hi := (hi0.add hi1).const_mul (D*M)
  apply hi.mono' (by
    unfold neutralNF600Density
    exact (neutralActualZetaGammaBracket_continuous.comp (by fun_prop)).aestronglyMeasurable.mul
      ((v.continuous.norm.pow 2).aestronglyMeasurable))
  filter_upwards [] with ξ
  have hξ : ‖v ξ‖ ≤ M := by simpa using hM ξ
  have hg := hb ξ
  rw [← neutralActualZetaGammaBracket_mathlib] at hg
  change ‖Zeta23.EF.gammaBracket (-2*Real.pi*ξ)*‖v ξ‖^2‖ ≤
    D*M*(‖v ξ‖+‖ξ‖*‖v ξ‖)
  rw [norm_mul,Real.norm_eq_abs,abs_of_nonneg (sq_nonneg ‖v ξ‖)]
  rw [Real.norm_eq_abs] at hg
  calc
    _ ≤ (D*(1+‖ξ‖))*‖v ξ‖^2 := mul_le_mul_of_nonneg_right hg (sq_nonneg _)
    _ ≤ (D*(1+‖ξ‖))*(M*‖v ξ‖) := by
      apply mul_le_mul_of_nonneg_left _ (by positivity)
      nlinarith only [mul_le_mul_of_nonneg_right hξ (norm_nonneg (v ξ))]
    _ = _ := by ring

theorem neutralNF600Correlation_spectral (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x=0) (ξ : ℝ) :
    Zeta23.paperFT (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume))
      ((-2*Real.pi*ξ:ℝ):ℂ) = (neutralNF600Density s ξ:ℂ) := by
  have h := neutralNF573WindowEvaluation_eq_raw_of_ae (11/10:ℝ)
    (s.toLp 2 volume) (fun x => s x) (neutralNF573OriginalCollar_window_ae s hs)
    ((-2*Real.pi*ξ:ℝ):ℂ)
  rw [← neutralRawTransform_eq_paperFT,neutralWindowCorrelation_rawTransform,
    Complex.conj_ofReal,h,neutralRawTransform_fourier]
  rw [← SchwartzMap.fourier_coe]
  unfold neutralNF600Density
  exact Complex.conj_mul' _

theorem neutralNF600LiteralArch_eq (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x=0) :
    ((1/(2*Real.pi):ℂ)*∫ r : ℝ,
      Zeta23.paperFT (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume))
        (r:ℂ)*(Zeta23.EF.gammaBracket r:ℂ)).re = neutralNF600Arch s := by
  let F : ℝ → ℂ := fun r =>
    Zeta23.paperFT (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume))
      (r:ℂ)*(Zeta23.EF.gammaBracket r:ℂ)
  have h := Measure.integral_comp_mul_left F (-2*Real.pi)
  have habs : |(-2*Real.pi)⁻¹|=1/(2*Real.pi) := by
    rw [show -2*Real.pi=-(2*Real.pi) by ring,inv_neg,abs_neg,abs_of_pos (inv_pos.mpr (by positivity))]
    simp only [one_div]
  rw [habs,Complex.real_smul] at h
  have hc : (1/(2*Real.pi):ℂ)=((1/(2*Real.pi):ℝ):ℂ) := by push_cast; rfl
  change ((1/(2*Real.pi):ℂ)*∫ r,F r).re = _
  rw [hc,← h]
  have he : (fun ξ : ℝ => F ((-2*Real.pi)*ξ)) =
      fun ξ => ((Zeta23.EF.gammaBracket (-2*Real.pi*ξ)*neutralNF600Density s ξ:ℝ):ℂ) := by
    funext ξ
    dsimp only [F]
    rw [neutralNF600Correlation_spectral s hs,Complex.ofReal_mul,mul_comm]
  rw [he,← Complex.ofRealCLM.integral_comp_comm (neutralNF600Arch_integrable s)]
  rfl


end
end WeilDefect
