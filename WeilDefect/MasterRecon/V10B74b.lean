import WeilDefect.MasterRecon.V10B74a
import WeilDefect.MasterRecon.V10B8e

/-! V10B74b: exact spectral Archimedean action for the divided trial bank.
The bounded measurable residual premise remains explicit. -/
namespace WeilDefect.MasterRecon.V10B74b
open MeasureTheory Set
open scoped ENNReal FourierTransform
open V08I (FullL2 logWeight)
open V10B74a (F principalSpectrum principalSpectrum_ae)
open V10B8e (gammaSymbol residual realMultiplier spectralPhysical)
open V10B69a (dividedTrial)

noncomputable def gammaSpectrum (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (j : Fin 16) : FullL2 :=
  principalSpectrum j + realMultiplier residual hd C hC (F j)

theorem gammaSpectrum_ae (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (j : Fin 16) :
    (gammaSpectrum hd C hC j : ℝ → ℂ) =ᵐ[volume]
      fun u => (gammaSymbol u : ℂ)*F j u := by
  unfold gammaSpectrum
  filter_upwards [Lp.coeFn_add (principalSpectrum j) (realMultiplier residual hd C hC (F j)),
    principalSpectrum_ae j, V10B8e.realMultiplier_ae residual hd C hC (F j)] with u hs hl hr
  change (principalSpectrum j + realMultiplier residual hd C hC (F j)) u =
    (gammaSymbol u : ℂ)*F j u
  change (principalSpectrum j + realMultiplier residual hd C hC (F j)) u =
    principalSpectrum j u + realMultiplier residual hd C hC (F j) u at hs
  have hsym : logWeight u + residual u = gammaSymbol u := by
    unfold residual
    ring
  rw [hs,hl,hr,← add_mul,← Complex.ofReal_add,hsym]

theorem actual_spectrum (j : Fin 16) :
    F j = spectralPhysical (1/4) (dividedTrial j) := rfl

noncomputable def physicalAction (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (j : Fin 16) : FullL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).symm (gammaSpectrum hd C hC j)

theorem physicalAction_fourier (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (j : Fin 16) :
    (𝓕 (physicalAction hd C hC j) : FullL2) = gammaSpectrum hd C hC j :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).apply_symm_apply _

theorem physicalAction_fourier_ae (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (j : Fin 16) :
    ((𝓕 (physicalAction hd C hC j) : FullL2) : ℝ → ℂ) =ᵐ[volume]
      fun u => (gammaSymbol u : ℂ)*F j u := by
  rw [physicalAction_fourier]
  exact gammaSpectrum_ae hd C hC j

end WeilDefect.MasterRecon.V10B74b

#print axioms WeilDefect.MasterRecon.V10B74b.gammaSpectrum_ae
#print axioms WeilDefect.MasterRecon.V10B74b.actual_spectrum
#print axioms WeilDefect.MasterRecon.V10B74b.physicalAction_fourier
#print axioms WeilDefect.MasterRecon.V10B74b.physicalAction_fourier_ae
