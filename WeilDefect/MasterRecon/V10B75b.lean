import WeilDefect.MasterRecon.V10B75a

/-! V10B75b: restrict the actual physical action to the support interval,
with no assertion of a historical convolution or numerical matrix identity. -/
namespace WeilDefect.MasterRecon.V10B75b
open MeasureTheory Set
open scoped InnerProduct FourierTransform
open V08I (FullL2 logCarrier physicalInclusion)
open V08K (supportMeasure restrictPhysical)
open V10B69a (J dividedTrial)
open V10B74b (physicalAction)
open V10B8e (archOperator)

theorem supported_pair (a : FullL2) (w : logCarrier (1/4)) :
    inner ℂ a (physicalInclusion (1/4) w) =
      inner ℂ (restrictPhysical (1/4) a) (J w) := by
  rw [L2.inner_def,L2.inner_def]
  calc
    _ = ∫ x in Icc (-(1/4):ℝ) (1/4),
        inner ℂ (a x) (physicalInclusion (1/4) w x) := by
      rw [← integral_indicator measurableSet_Icc]
      apply integral_congr_ae
      filter_upwards [V08I.physicalInclusion_support (1/4) w] with x hx
      by_cases hm : x ∈ Icc (-(1/4):ℝ) (1/4)
      · rw [Set.indicator_of_mem hm]
      · rw [Set.indicator_of_notMem hm,hx hm,inner_zero_right]
    _ = _ := by
      change (∫ x, inner ℂ (a x) (physicalInclusion (1/4) w x)
        ∂supportMeasure (1/4)) = _
      apply integral_congr_ae
      have hw := V08K.restrictPhysical_ae (1/4) (physicalInclusion (1/4) w)
      change (J w : ℝ → ℂ) =ᵐ[supportMeasure (1/4)] physicalInclusion (1/4) w at hw
      filter_upwards [V08K.restrictPhysical_ae (1/4) a,hw] with x hx hy
      rw [hx,hy]

noncomputable def archLoad (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (j : Fin 16) :
    V08F.PhysicalL2 (supportMeasure (1/4)) :=
  restrictPhysical (1/4) (physicalAction hd C hC j)

theorem arch_restricted_pair (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (j : Fin 16)
    (w : logCarrier (1/4)) :
    inner ℂ (archOperator (1/4) hd C hC (dividedTrial j)) w =
      inner ℂ (archLoad hd C hC j) (J w) := by
  rw [V10B75a.arch_physical_pair]
  exact supported_pair _ w

end WeilDefect.MasterRecon.V10B75b

#print axioms WeilDefect.MasterRecon.V10B75b.supported_pair
#print axioms WeilDefect.MasterRecon.V10B75b.arch_restricted_pair
