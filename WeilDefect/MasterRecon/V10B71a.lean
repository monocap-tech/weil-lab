import WeilDefect.MasterRecon.V10B69a
import WeilDefect.MasterRecon.V10B23c
import Mathlib.Analysis.Calculus.MeanValue

/-! Exact physical action interface on the divided trial bank.
SeriesSupply and residual-symbol bounds remain explicit. Prime vanishing
is not used. No historical matrix-generation premise is consumed. -/
namespace WeilDefect.MasterRecon.V10B71a
open MeasureTheory Set Polynomial
open scoped InnerProduct BigOperators ComplexConjugate
open V08I (FullL2 logCarrier physicalInclusion)
open V08K (supportMeasure restrictPhysical)
open V10B69a (D dividedTrial J poleLoad)
open V10B66a (trialPoly)
open V10B67a (polynomialValue supportedTrial)
open V10B23b (SeriesSupply archAction)
open V10B8e (residual archOperator)

noncomputable def p (j : Fin 16) (x : ℝ) : ℂ :=
  D⁻¹ * polynomialValue j x

theorem divided_supported (j : Fin 16) :
    (physicalInclusion (1/4) (dividedTrial j) : ℝ → ℂ) =ᵐ[volume]
      V10B21b.supported (-(1/4)) (1/4) (p j) := by
  filter_upwards [V10B69a.divided_physical j] with x hx
  rw [hx]
  unfold supportedTrial V10B21b.supported p
  rw [neg_div]
  by_cases hm : x ∈ Icc (-1/4:ℝ) (1/4)
  · rw [indicator_of_mem hm,indicator_of_mem hm]
  · rw [indicator_of_notMem hm,indicator_of_notMem hm,mul_zero]

theorem poly_bounds (j : Fin 16) :
    ∃ B K : ℝ, 0 ≤ B ∧ 0 ≤ K ∧
      (∀ x ∈ Icc (-(1/4):ℝ) (1/4), ‖p j x‖ ≤ B) ∧
      (∀ x ∈ Icc (-(1/4):ℝ) (1/4), ∀ y ∈ Icc (-(1/4):ℝ) (1/4),
        ‖p j x-p j y‖ ≤ K*|x-y|) := by
  let q := trialPoly j
  let S := Icc (-(1/4):ℝ) (1/4)
  have hs : IsCompact S := isCompact_Icc
  have hne : S.Nonempty := ⟨0,by norm_num [S]⟩
  obtain ⟨b,hb,hmax⟩ := hs.exists_isMaxOn hne q.continuous.norm.continuousOn
  obtain ⟨k,hk,hmax'⟩ := hs.exists_isMaxOn hne q.derivative.continuous.norm.continuousOn
  refine ⟨‖D⁻¹‖*‖q.eval b‖,‖D⁻¹‖*‖q.derivative.eval k‖,
    by positivity,by positivity,?_,?_⟩
  · intro x hx
    unfold p polynomialValue
    rw [norm_mul,Complex.norm_real]
    exact mul_le_mul_of_nonneg_left (hmax hx) (norm_nonneg _)
  · intro x hx y hy
    have hd : ‖q.eval x-q.eval y‖ ≤ ‖q.derivative.eval k‖*‖x-y‖ :=
      Convex.norm_image_sub_le_of_norm_hasDerivWithin_le
        (fun z _ => (q.hasDerivAt z).hasDerivWithinAt)
        (fun z hz => hmax' hz) (convex_Icc _ _) hy hx
    unfold p polynomialValue
    rw [← mul_sub,norm_mul,← Complex.ofReal_sub,Complex.norm_real]
    rw [Real.norm_eq_abs] at hd
    calc
      _ ≤ ‖D⁻¹‖*(‖q.derivative.eval k‖*|x-y|) :=
        mul_le_mul_of_nonneg_left hd (norm_nonneg _)
      _ = _ := by ring

theorem divided_action_integrable (j : Fin 16) :
    IntegrableOn (V10B21c.actionTerm (physicalInclusion (1/4) (dividedTrial j))) (Ioi 0) := by
  obtain ⟨B,K,hB,hK,hb,hl⟩ := poly_bounds j
  exact V10B22a.supported_action_integrable (-(1/4)) (1/4) B K
    (by norm_num) hB hK (p j) hb hl _ (divided_supported j)

theorem restricted_inner (f : FullL2) (w : logCarrier (1/4)) :
    inner ℂ f (physicalInclusion (1/4) w) =
      inner ℂ (restrictPhysical (1/4) f) (J w) := by
  rw [L2.inner_def,L2.inner_def]
  calc
    _ = ∫ x, inner ℂ (f x) (physicalInclusion (1/4) w x)
        ∂supportMeasure (1/4) := by
      unfold supportMeasure
      rw [← integral_indicator measurableSet_Icc]
      apply integral_congr_ae
      filter_upwards [V08I.physicalInclusion_support (1/4) w] with x hx
      by_cases hm : x ∈ Icc (-(1/4):ℝ) (1/4)
      · rw [indicator_of_mem hm]
      · rw [indicator_of_notMem hm,hx hm,inner_zero_right]
    _ = _ := by
      apply integral_congr_ae
      filter_upwards [V08K.restrictPhysical_ae (1/4) f,
        V08K.restrictPhysical_ae (1/4) (physicalInclusion (1/4) w)] with x hx hy
      change inner ℂ (f x) (physicalInclusion (1/4) w x) =
        inner ℂ (restrictPhysical (1/4) f x) (restrictPhysical (1/4) (physicalInclusion (1/4) w) x)
      rw [hx,hy]

noncomputable def archLoad (j : Fin 16) : V08F.PhysicalL2 (supportMeasure (1/4)) :=
  restrictPhysical (1/4) (archAction (physicalInclusion (1/4) (dividedTrial j)))

theorem arch_physical_pair (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (hS : SeriesSupply)
    (j : Fin 16) (w : logCarrier (1/4)) :
    inner ℂ (archOperator (1/4) hd C hC (dividedTrial j)) w =
      inner ℂ (archLoad j) (J w) := by
  rw [V10B23c.carrier_arch_pairing (1/4) hd C hC _ _ (divided_action_integrable j) hS]
  exact restricted_inner _ w

noncomputable def fullLoad (j : Fin 16) : V08F.PhysicalL2 (supportMeasure (1/4)) :=
  archLoad j + poleLoad (dividedTrial j)

theorem full_physical_pair (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (hS : SeriesSupply)
    (j : Fin 16) (w : logCarrier (1/4)) :
    inner ℂ ((archOperator (1/4) hd C hC + V10B8c.poleOperator (1/4) (by norm_num))
      (dividedTrial j)) w = inner ℂ (fullLoad j) (J w) := by
  rw [ContinuousLinearMap.add_apply,inner_add_left,arch_physical_pair hd C hC hS,
    V10B69a.pole_physical_pair,fullLoad,inner_add_left]

theorem corrected_physical_pair (hd : Measurable residual) (C : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (hS : SeriesSupply)
    (j : Fin 16) (a : Fin 16 → ℂ) (w : logCarrier (1/4))
    (hw : w ∈ V10B17b.retainedᗮ) :
    inner ℂ ((archOperator (1/4) hd C hC + V10B8c.poleOperator (1/4) (by norm_num))
      (dividedTrial j)) w =
      inner ℂ (fullLoad j-∑ i, a i • V10B68a.rowVector i) (J w) := by
  rw [V10B69a.row_subtraction_invariant _ _ w hw]
  exact full_physical_pair hd C hC hS j w

end WeilDefect.MasterRecon.V10B71a

#print axioms WeilDefect.MasterRecon.V10B71a.divided_supported
#print axioms WeilDefect.MasterRecon.V10B71a.poly_bounds
#print axioms WeilDefect.MasterRecon.V10B71a.divided_action_integrable
#print axioms WeilDefect.MasterRecon.V10B71a.restricted_inner
#print axioms WeilDefect.MasterRecon.V10B71a.arch_physical_pair
#print axioms WeilDefect.MasterRecon.V10B71a.full_physical_pair
#print axioms WeilDefect.MasterRecon.V10B71a.corrected_physical_pair
