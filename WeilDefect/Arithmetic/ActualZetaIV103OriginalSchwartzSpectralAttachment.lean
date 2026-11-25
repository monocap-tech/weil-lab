import WeilDefect.Arithmetic.ActualZetaIV102OriginalSchwartzMetricTransport
import WeilDefect.Arithmetic.ActualZetaArchimedeanTransport
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory InnerProductSpace FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- Exact original mixed correlation, with unchanged window and input vectors. -/
def neutralIV103Correlation (a : ℝ) (u v : 𝓢(ℝ,ℂ)) : ℝ → ℂ :=
  neutralWindowCorrelation a (u.toLp 2 volume) (v.toLp 2 volume)

def neutralIV103Spectrum (u v : 𝓢(ℝ,ℂ)) (ξ : ℝ) : ℂ :=
  conj ((𝓕 (u.toLp 2 volume) : RealComplexL2) ξ) *
    (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ

/-- No Green synthesis needed for this pointwise evaluation dictionary. -/
theorem neutralIV103Evaluation_fourier (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) (ξ : ℝ) :
    neutralWindowEvaluation a ((-2 * Real.pi * ξ : ℝ) : ℂ) (s.toLp 2 volume) =
      (𝓕 s : 𝓢(ℝ,ℂ)) ξ := by
  rw [neutralNF573WindowEvaluation_eq_raw_of_ae a _ _
    (neutralIV006Schwartz_window_ae a s hs), ← neutralRawTransform_fourier,
    ← SchwartzMap.fourier_coe]

/-- Exact real-frequency raw transform on the genuine physical L² pair. -/
theorem neutralIV103Raw_spectrum_ae (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    (fun ξ : ℝ => neutralRawTransform (neutralIV103Correlation a u v)
      ((-2 * Real.pi * ξ : ℝ) : ℂ)) =ᵐ[volume] neutralIV103Spectrum u v := by
  unfold neutralIV103Correlation neutralIV103Spectrum
  rw [SchwartzMap.toLp_fourier_eq u, SchwartzMap.toLp_fourier_eq v]
  filter_upwards [((𝓕 u : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume),
    ((𝓕 v : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume)] with ξ hξu hξv
  rw [neutralWindowCorrelation_rawTransform, Complex.conj_ofReal,
    neutralIV103Evaluation_fourier a u hu, neutralIV103Evaluation_fourier a v hv,
    hξu, hξv]

/-- Full Gamma term, with exactly the original normalization and sign. -/
theorem neutralIV103Arch_spectral (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    (1 / (2 * Real.pi) : ℂ) * (∫ r : ℝ,
      Zeta23.paperFT (neutralIV103Correlation a u v) (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ)) =
      ∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
        neutralIV103Spectrum u v ξ := by
  let F : ℝ → ℂ := fun r => Zeta23.paperFT (neutralIV103Correlation a u v)
    (r : ℂ) * (Zeta23.EF.gammaBracket r : ℂ)
  have h := Measure.integral_comp_mul_left F (-2 * Real.pi)
  have habs : |(-2 * Real.pi)⁻¹| = 1 / (2 * Real.pi) := by
    rw [show -2 * Real.pi = -(2 * Real.pi) by ring,
      inv_neg, abs_neg, abs_of_pos (inv_pos.mpr (by positivity))]
    simp only [one_div]
  rw [habs, Complex.real_smul] at h
  have he : (∫ ξ : ℝ, F ((-2 * Real.pi) * ξ)) =
      ∫ ξ : ℝ, (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) : ℂ) *
        neutralIV103Spectrum u v ξ := by
    apply integral_congr_ae
    filter_upwards [neutralIV103Raw_spectrum_ae a u v hu hv] with ξ hξ
    dsimp only [F]
    rw [← neutralRawTransform_eq_paperFT, hξ, neutralActualZetaGammaBracket_mathlib]
    exact mul_comm _ _
  have hc : (1 / (2 * Real.pi) : ℂ) = ((1 / (2 * Real.pi) : ℝ) : ℂ) := by
    push_cast
    rfl
  change (1 / (2 * Real.pi) : ℂ) * (∫ r : ℝ, F r) = _
  rw [hc]
  exact h.symm.trans he

/-- Both pole interactions transfer to the existing native carrier operator. -/
theorem neutralIV103Pole_operator (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    Zeta23.paperFT (neutralIV103Correlation a u v) (Complex.I / 2) +
      Zeta23.paperFT (neutralIV103Correlation a u v) (-Complex.I / 2) =
      inner ℂ (neutralIV102Lift a u hu)
        (neutralLogPoleOperator a (neutralIV102Lift a v hv)) := by
  have h := neutralLogHilbertCorrelation_poleOperator a
    (neutralIV102Lift a u hu) (neutralIV102Lift a v hv)
  rw [neutralIV102Lift_physical, neutralIV102Lift_physical] at h
  unfold neutralIV103Correlation
  rw [← neutralRawTransform_eq_paperFT, ← neutralRawTransform_eq_paperFT]
  convert h using 2 <;> push_cast <;> ring

#print axioms neutralIV103Evaluation_fourier
#print axioms neutralIV103Raw_spectrum_ae
#print axioms neutralIV103Arch_spectral
#print axioms neutralIV103Pole_operator

end
end WeilDefect
