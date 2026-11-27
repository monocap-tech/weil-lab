import WeilDefect.MasterRecon.V10B23a
import WeilDefect.MasterRecon.V10B22c

/-! V10B23b: identify the integrated multiplier by local distributional
uniqueness. No a priori L² integrability of the unbounded symbol product
is needed: it follows from its equality with the Bochner Fourier image. -/
namespace WeilDefect.MasterRecon.V10B23b

open MeasureTheory Set Filter Complex
open scoped InnerProduct FourierTransform SchwartzMap ContDiff ComplexConjugate
open V08I (FullL2)
open V10B22b (U symbol integratedAction)
open V10B21c (actionTerm)
open V10B23a (argument)

def SeriesSupply : Prop := ∀ u : ℝ, V10B20a.PartialFraction (argument u)

noncomputable def integratedSymbol (u : ℝ) : ℂ :=
  ((V10B8e.gammaSymbol u+Real.log Real.pi+Real.eulerMascheroniConstant:ℝ):ℂ)

noncomputable def archAction (f : FullL2) : FullL2 :=
  integratedAction f-(Real.log Real.pi+Real.eulerMascheroniConstant) • f

theorem integratedSymbol_continuous : Continuous integratedSymbol := by
  unfold integratedSymbol
  exact Complex.continuous_ofReal.comp
    ((V10B8f.gammaSymbol_continuous.add continuous_const).add continuous_const)

theorem symbol_measurable : Measurable (fun z : ℝ × ℝ => symbol z.1 z.2) := by
  unfold symbol V10B21c.denominator V10B22b.phase
  fun_prop

theorem integrated_multiplier_ae (f : FullL2) (hf : Integrable (fun x : ℝ => f x))
    (hD : IntegrableOn (actionTerm f) (Ioi 0)) (hS : SeriesSupply) :
    (U (integratedAction f) : ℝ → ℂ) =ᵐ[volume]
      fun u => integratedSymbol u * (U f) u := by
  let F : ℝ → ℂ := 𝓕 (f : ℝ → ℂ)
  have hF : Continuous F := V08H.classical_fourier_continuous _ hf
  have hFa : (U f : ℝ → ℂ) =ᵐ[volume] F := V08H.l2_fourier_integral_ae f hf
  have he : (U (integratedAction f) : ℝ → ℂ) =ᵐ[volume]
      fun u => integratedSymbol u*F u := by
    apply ae_eq_of_integral_contDiff_smul_eq
    · exact (Lp.memLp (U (integratedAction f))).locallyIntegrable (by norm_num)
    · exact (integratedSymbol_continuous.mul hF).locallyIntegrable
    intro g hg hgc
    have hgc' : HasCompactSupport (Complex.ofRealCLM ∘ g) := hgc.comp_left rfl
    have hg' : ContDiff ℝ ∞ (Complex.ofRealCLM ∘ g) := by fun_prop
    let φ : 𝓢(ℝ,ℂ) := hgc'.toSchwartzMap hg'
    let k : FullL2 := φ.toLp 2 volume
    have hφ (u : ℝ) : φ u = (g u:ℂ) := rfl
    have hKa : (k : ℝ → ℂ) =ᵐ[volume] φ := φ.coeFn_toLp 2 volume
    have h := V10B22c.spectral_pairing_fubini f k hf hD F φ
      hF.stronglyMeasurable φ.continuous.stronglyMeasurable hFa hKa
      symbol_measurable.stronglyMeasurable integratedSymbol
      (fun u => V10B23a.literal_symbol_integral u (hS u))
    calc
      _ = inner ℂ k (U (integratedAction f)) := by
        rw [L2.inner_def]
        apply integral_congr_ae
        filter_upwards [hKa] with u hu
        rw [RCLike.inner_apply',hu,hφ,Complex.conj_ofReal,Complex.real_smul]
      _ = ∫ u, conj (φ u)*(integratedSymbol u*F u) := h
      _ = _ := by
        apply integral_congr_ae
        filter_upwards with u
        rw [hφ,Complex.conj_ofReal,Complex.real_smul]
  filter_upwards [he,hFa] with u hu hf'
  rw [hu,hf']

theorem arch_multiplier_ae (f : FullL2) (hf : Integrable (fun x : ℝ => f x))
    (hD : IntegrableOn (actionTerm f) (Ioi 0)) (hS : SeriesSupply) :
    (U (archAction f) : ℝ → ℂ) =ᵐ[volume]
      fun u => (V10B8e.gammaSymbol u:ℂ)*(U f) u := by
  have h : U (archAction f) =
      U (integratedAction f)-(Real.log Real.pi+Real.eulerMascheroniConstant) • U f := by
    unfold archAction
    simp only [map_sub,map_smul_of_tower]
  rw [h]
  filter_upwards [Lp.coeFn_sub (U (integratedAction f))
      ((Real.log Real.pi+Real.eulerMascheroniConstant) • U f),
    Lp.coeFn_smul (Real.log Real.pi+Real.eulerMascheroniConstant) (U f),
    integrated_multiplier_ae f hf hD hS] with u h₁ h₂ h₃
  rw [h₁,h₂,h₃]
  unfold integratedSymbol
  simp only [Complex.real_smul,Complex.ofReal_add]
  ring

theorem arch_multiplier_memLp (f : FullL2) (hf : Integrable (fun x : ℝ => f x))
    (hD : IntegrableOn (actionTerm f) (Ioi 0)) (hS : SeriesSupply) :
    MemLp (fun u : ℝ => (V10B8e.gammaSymbol u:ℂ)*(U f) u) 2 volume :=
  (Lp.memLp (U (archAction f))).ae_eq (arch_multiplier_ae f hf hD hS)

end WeilDefect.MasterRecon.V10B23b

#print axioms WeilDefect.MasterRecon.V10B23b.integratedSymbol_continuous
#print axioms WeilDefect.MasterRecon.V10B23b.symbol_measurable
#print axioms WeilDefect.MasterRecon.V10B23b.integrated_multiplier_ae
#print axioms WeilDefect.MasterRecon.V10B23b.arch_multiplier_ae
#print axioms WeilDefect.MasterRecon.V10B23b.arch_multiplier_memLp
