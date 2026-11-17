import WeilDefect.Arithmetic.ActualZetaOriginalCollarFourierMass
import WeilDefect.Arithmetic.ActualZetaOriginalCollarGammaLower
import WeilDefect.Arithmetic.ActualZetaArchimedeanTransport

namespace WeilDefect
noncomputable section
open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform ENNReal

/-- The exact complete gamma-weighted Fourier integral, conditional
only on its integrability (proved separately using Schwartz decay). -/
theorem neutralNF600ArchLower (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (hi : Integrable (fun ξ => Zeta23.EF.gammaBracket (-2*Real.pi*ξ) *
      neutralNF600Density s ξ)) :
    (104/125:ℝ)*neutralNF600Mass s ≤
      ∫ ξ, Zeta23.EF.gammaBracket (-2*Real.pi*ξ)*neutralNF600Density s ξ := by
  let L := neutralNF600LowBand
  let ρ := neutralNF600Density s
  let w := fun ξ => Zeta23.EF.gammaBracket (-2*Real.pi*ξ)*ρ ξ
  have hρ := neutralNF600Density_integrable s
  have hL : MeasurableSet L := measurableSet_Ioo
  have hlo : ∫ ξ in L, (-(28/5:ℝ))*ρ ξ ≤ ∫ ξ in L, w ξ :=
    setIntegral_mono_on (hρ.const_mul _).integrableOn hi.integrableOn hL
      (fun ξ _ => mul_le_mul_of_nonneg_right (neutralNF599GammaLower _).le (sq_nonneg _))
  have hhi : ∫ ξ in Lᶜ, (11/10:ℝ)*ρ ξ ≤ ∫ ξ in Lᶜ, w ξ :=
    setIntegral_mono_on (hρ.const_mul _).integrableOn hi.integrableOn hL.compl
      (fun ξ hξ => mul_le_mul_of_nonneg_right
        (neutralNF599GammaHigh _ (neutralNF600HighFrequency ξ hξ)).le (sq_nonneg _))
  rw [integral_const_mul] at hlo hhi
  have hm := integral_add_compl hL hρ
  have hw := integral_add_compl hL hi
  change (∫ ξ in L, ρ ξ)+(∫ ξ in Lᶜ, ρ ξ)=∫ ξ,ρ ξ at hm
  rw [neutralNF600Density_mass] at hm
  have hl := neutralNF600LowMass s hs
  change (∫ ξ in L, ρ ξ) ≤ neutralNF600Mass s/25 at hl
  change (∫ ξ in L, w ξ)+(∫ ξ in Lᶜ, w ξ)=∫ ξ,w ξ at hw
  change (104/125:ℝ)*neutralNF600Mass s ≤ ∫ ξ,w ξ
  linarith only [hlo,hhi,hm,hw,hl]

end
end WeilDefect
