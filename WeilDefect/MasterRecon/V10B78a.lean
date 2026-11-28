import WeilDefect.MasterRecon.V10B76b
import WeilDefect.MasterRecon.V10B77c

/-! V10B78a: instantiate the exact spectral route using the now
unconditional scalar estimates. No prime-zero or historical numerical
matrix provenance is consumed. -/
namespace WeilDefect.MasterRecon.V10B78a
open MeasureTheory Set
open scoped InnerProduct BigOperators FourierTransform
open V08I (FullL2 logCarrier)
open V08K (supportMeasure)
open V10B69a (J dividedTrial)
open V10B76a (residual_measurable)
open V10B77c (residual_uniform_24)

noncomputable def arch : logCarrier (1/4) →L[ℂ] logCarrier (1/4) :=
  V10B8e.archOperator (1/4) residual_measurable 24 residual_uniform_24

noncomputable def archPole : logCarrier (1/4) →L[ℂ] logCarrier (1/4) :=
  arch + V10B8c.poleOperator (1/4) (by norm_num)

noncomputable def action (j : Fin 16) : FullL2 :=
  V10B74b.physicalAction residual_measurable 24 residual_uniform_24 j

noncomputable def archLoad (j : Fin 16) : V08F.PhysicalL2 (supportMeasure (1/4)) :=
  V10B75b.archLoad residual_measurable 24 residual_uniform_24 j

noncomputable def load (j : Fin 16) : V08F.PhysicalL2 (supportMeasure (1/4)) :=
  V10B76b.fullLoad residual_measurable 24 residual_uniform_24 j

noncomputable def correctedLoad (j : Fin 16) (a : Fin 16 → ℂ) :
    V08F.PhysicalL2 (supportMeasure (1/4)) :=
  load j - ∑ i, a i • V10B68a.rowVector i

theorem action_fourier_ae (j : Fin 16) :
    ((𝓕 (action j) : FullL2) : ℝ → ℂ) =ᵐ[volume]
      fun u => (V10B8e.gammaSymbol u : ℂ)*V10B74a.F j u :=
  V10B74b.physicalAction_fourier_ae residual_measurable 24 residual_uniform_24 j

theorem arch_pair (j : Fin 16) (w : logCarrier (1/4)) :
    inner ℂ (arch (dividedTrial j)) w = inner ℂ (archLoad j) (J w) :=
  V10B75b.arch_restricted_pair residual_measurable 24 residual_uniform_24 j w

theorem full_pair (j : Fin 16) (w : logCarrier (1/4)) :
    inner ℂ (archPole (dividedTrial j)) w = inner ℂ (load j) (J w) :=
  V10B76b.full_physical_pair residual_measurable 24 residual_uniform_24 j w

theorem corrected_pair (j : Fin 16) (a : Fin 16 → ℂ)
    (w : logCarrier (1/4)) (hw : w ∈ V10B17b.retainedᗮ) :
    inner ℂ (archPole (dividedTrial j)) w = inner ℂ (correctedLoad j a) (J w) :=
  V10B76b.corrected_physical_pair residual_measurable 24 residual_uniform_24 j a w hw

theorem trial_entry_pair (i j : Fin 16) :
    inner ℂ (archPole (dividedTrial i)) (dividedTrial j) =
      inner ℂ (load i) (J (dividedTrial j)) :=
  full_pair i (dividedTrial j)

end WeilDefect.MasterRecon.V10B78a

#print axioms WeilDefect.MasterRecon.V10B78a.action_fourier_ae
#print axioms WeilDefect.MasterRecon.V10B78a.arch_pair
#print axioms WeilDefect.MasterRecon.V10B78a.full_pair
#print axioms WeilDefect.MasterRecon.V10B78a.corrected_pair
#print axioms WeilDefect.MasterRecon.V10B78a.trial_entry_pair
