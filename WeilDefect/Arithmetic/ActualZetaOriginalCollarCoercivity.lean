import WeilDefect.Arithmetic.ActualZetaOriginalCollarArchLower
import WeilDefect.Arithmetic.ActualZetaOriginalCollarPoleBound
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
  have hi := (v.integrable.norm.add (v.integrable_pow_mul volume 1)).const_mul (D*M)
  apply hi.mono' (by
    unfold neutralNF600Density
    exact (neutralActualZetaGammaBracket_continuous.comp (by fun_prop)).aestronglyMeasurable.mul
      ((v.continuous.norm.pow 2).aestronglyMeasurable))
  filter_upwards [] with ξ
  have hξ : ‖v ξ‖ ≤ M := by simpa using hM ξ
  have hg := hb ξ
  rw [← neutralActualZetaGammaBracket_mathlib] at hg
  simp only [neutralNF600Density,norm_mul,Real.norm_eq_abs,abs_of_nonneg (sq_nonneg _),
    Pi.add_apply,pow_one]
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
  rw [← neutralRawTransform_eq_paperFT,neutralWindowCorrelation_rawTransform,
    Complex.conj_ofReal,neutralNF573WindowEvaluation_eq_raw_of_ae _ _ _
      (neutralNF573OriginalCollar_window_ae s hs),neutralRawTransform_fourier]
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

theorem neutralNF600SmoothWeil_split (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x=0) :
    neutralNF598SmoothWeil s =
      neutralNF600Arch s-(neutralNF600Prime s).re+(neutralNF600Pole s).re := by
  unfold neutralNF598SmoothWeil Zeta23.EF.literatureRHS
  simp only [Complex.add_re,Complex.sub_re]
  have h := neutralNF600LiteralArch_eq s hs
  unfold neutralNF600Prime neutralNF600Pole
  simp only [Complex.add_re] at *
  linarith only [h]

/-- Strong local signed margin, not full-space Weil positivity. -/
theorem neutralNF600SmoothCollarLower :
    neutralNF599SmoothCollarLower (2/5) := by
  intro s hs
  have ha := neutralNF600ArchLower s hs (neutralNF600Arch_integrable s)
  have hp := neutralNF600Prime_bound_actual s hs
  have hq := neutralNF600Pole_bound s hs
  rw [neutralNF600SmoothWeil_split s hs]
  change (2/5:ℝ)*neutralNF600Mass s ≤ _
  change (104/125:ℝ)*neutralNF600Mass s ≤ neutralNF600Arch s at ha
  linarith only [ha,hp,hq,le_abs_self (neutralNF600Prime s).re,neg_abs_le (neutralNF600Pole s).re]

theorem neutralNF600NF407GraphLower (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      (2/5:ℝ)*‖neutralNF598GraphPhysical (11/10) K‖^2 ≤
        neutralNF598GraphWeil (11/10) K :=
  neutralNF599NF407GraphLower a b (2/5) neutralNF600SmoothCollarLower

end
end WeilDefect
