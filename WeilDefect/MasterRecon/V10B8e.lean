import WeilDefect.MasterRecon.V10B8c
import WeilDefect.MasterRecon.V10B8d
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma

/-! V10B8e: the Archimedean principal symbol and compact remainder.
The classical uniform digamma remainder estimate is an explicit premise.
This module does not assert the original explicit formula or signed positivity. -/
namespace WeilDefect.MasterRecon.V10B8e

open MeasureTheory Complex
open scoped FourierTransform InnerProduct ComplexConjugate
open V08I (FullL2 logCarrier physicalInclusion logWeight)

noncomputable def gammaSymbol (u : ℝ) : ℝ :=
  (Complex.digamma (1/4+I*((-(2*Real.pi*u):ℝ):ℂ)/2)).re - Real.log Real.pi

noncomputable def residual (u : ℝ) : ℝ :=
  gammaSymbol u - logWeight u

def ResidualEstimate : Prop :=
  Measurable residual ∧ ∃ C : ℝ, 0 ≤ C ∧ ∀ u, |residual u| ≤ C

noncomputable def spectralPhysical (t : ℝ) : logCarrier t →L[ℂ] FullL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).toContinuousLinearEquiv.toContinuousLinearMap.comp (physicalInclusion t)

theorem spectralPhysical_norm (t : ℝ) (g : logCarrier t) :
    ‖spectralPhysical t g‖ = ‖physicalInclusion t g‖ := by
  change ‖(𝓕 (physicalInclusion t g) : FullL2)‖ = _
  exact Lp.norm_fourier_eq _

theorem spectralPhysical_compact (t : ℝ) (ht : 0 ≤ t) :
    IsCompactOperator (spectralPhysical t) :=
  (V08K.physicalInclusion_compact t ht).clm_comp
    (Lp.fourierTransformₗᵢ ℝ ℂ).toContinuousLinearMap

noncomputable def realMultiplier (d : ℝ → ℝ) (hd : Measurable d)
    (C : ℝ) (hC : ∀ u, |d u| ≤ C) : FullL2 →L[ℂ] FullL2 :=
  V08I.multiplier (fun u => (d u:ℂ)) (Complex.continuous_ofReal.measurable.comp hd) C
    (fun u => by simpa [Complex.norm_real,Real.norm_eq_abs] using hC u)

theorem realMultiplier_ae (d : ℝ → ℝ) (hd : Measurable d)
    (C : ℝ) (hC : ∀ u, |d u| ≤ C) (f : FullL2) :
    (realMultiplier d hd C hC f : ℝ → ℂ) =ᵐ[volume] fun u => (d u:ℂ)*f u :=
  V08I.multiplier_ae _ _ _ _ f

theorem realMultiplier_bound (d : ℝ → ℝ) (hd : Measurable d)
    (C : ℝ) (hC : ∀ u, |d u| ≤ C) (f : FullL2) :
    ‖realMultiplier d hd C hC f‖ ≤ C*‖f‖ :=
  V08I.mulValue_bound (fun u => (d u:ℂ)) (Complex.continuous_ofReal.measurable.comp hd) C
    (fun u => by simpa [Complex.norm_real,Real.norm_eq_abs] using hC u) f

theorem realMultiplier_symmetric (d : ℝ → ℝ) (hd : Measurable d)
    (C : ℝ) (hC : ∀ u, |d u| ≤ C) (f g : FullL2) :
    inner ℂ (realMultiplier d hd C hC f) g =
      inner ℂ f (realMultiplier d hd C hC g) := by
  rw [L2.inner_def,L2.inner_def]
  apply integral_congr_ae
  filter_upwards [realMultiplier_ae d hd C hC f,realMultiplier_ae d hd C hC g] with u hf hg
  simp only [RCLike.inner_apply']
  rw [hf,hg,map_mul,Complex.conj_ofReal]
  ring

theorem realMultiplier_selfAdjoint (d : ℝ → ℝ) (hd : Measurable d)
    (C : ℝ) (hC : ∀ u, |d u| ≤ C) :
    (realMultiplier d hd C hC).adjoint = realMultiplier d hd C hC := by
  ext f : 1
  apply ext_inner_right ℂ
  intro g
  rw [ContinuousLinearMap.adjoint_inner_left]
  exact (realMultiplier_symmetric d hd C hC f g).symm

noncomputable def correction (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) : logCarrier t →L[ℂ] logCarrier t :=
  (spectralPhysical t).adjoint ∘L realMultiplier residual hd C hC ∘L spectralPhysical t

theorem correction_compact (t : ℝ) (ht : 0 ≤ t) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    IsCompactOperator (correction t hd C hC) :=
  (spectralPhysical_compact t ht).clm_comp
    ((spectralPhysical t).adjoint ∘L realMultiplier residual hd C hC)

theorem correction_selfAdjoint (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    (correction t hd C hC).adjoint = correction t hd C hC := by
  unfold correction
  rw [ContinuousLinearMap.adjoint_comp,ContinuousLinearMap.adjoint_comp,
    ContinuousLinearMap.adjoint_adjoint,realMultiplier_selfAdjoint]
  ext g : 1
  rfl

theorem correction_bound (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (g : logCarrier t) :
    ‖inner ℂ (correction t hd C hC g) g‖ ≤ C*‖physicalInclusion t g‖^2 := by
  unfold correction
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]
  calc
    _ ≤ ‖realMultiplier residual hd C hC (spectralPhysical t g)‖ *
        ‖spectralPhysical t g‖ := norm_inner_le_norm _ _
    _ ≤ (C*‖spectralPhysical t g‖)*‖spectralPhysical t g‖ :=
      mul_le_mul_of_nonneg_right (realMultiplier_bound residual hd C hC _) (norm_nonneg _)
    _ = _ := by rw [spectralPhysical_norm]; ring

noncomputable def archOperator (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) : logCarrier t →L[ℂ] logCarrier t :=
  1+correction t hd C hC

theorem arch_selfAdjoint (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    (archOperator t hd C hC).adjoint = archOperator t hd C hC := by
  unfold archOperator
  rw [map_add,correction_selfAdjoint]
  congr 1
  ext g : 1
  apply ext_inner_right ℂ
  intro h
  rw [ContinuousLinearMap.adjoint_inner_left]
  simp only [ContinuousLinearMap.one_apply]

theorem arch_lower (t : ℝ) (hd : Measurable residual)
    (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (g : logCarrier t) :
    ‖g‖^2 ≤ (inner ℂ (archOperator t hd C hC g) g).re +
      C*‖physicalInclusion t g‖^2 := by
  have hb := correction_bound t hd C hC g
  have hr := Complex.abs_re_le_norm (inner ℂ (correction t hd C hC g) g)
  have hl := neg_abs_le (inner ℂ (correction t hd C hC g) g).re
  unfold archOperator
  rw [ContinuousLinearMap.add_apply,ContinuousLinearMap.one_apply,inner_add_left,
    Complex.add_re]
  have hn : (inner ℂ g g).re = ‖g‖^2 := inner_self_eq_norm_sq (𝕜 := ℂ) g
  rw [hn]
  linarith

end WeilDefect.MasterRecon.V10B8e

#print axioms WeilDefect.MasterRecon.V10B8e.spectralPhysical_norm
#print axioms WeilDefect.MasterRecon.V10B8e.spectralPhysical_compact
#print axioms WeilDefect.MasterRecon.V10B8e.realMultiplier_ae
#print axioms WeilDefect.MasterRecon.V10B8e.realMultiplier_bound
#print axioms WeilDefect.MasterRecon.V10B8e.realMultiplier_symmetric
#print axioms WeilDefect.MasterRecon.V10B8e.realMultiplier_selfAdjoint
#print axioms WeilDefect.MasterRecon.V10B8e.correction_compact
#print axioms WeilDefect.MasterRecon.V10B8e.correction_selfAdjoint
#print axioms WeilDefect.MasterRecon.V10B8e.correction_bound
#print axioms WeilDefect.MasterRecon.V10B8e.arch_selfAdjoint
#print axioms WeilDefect.MasterRecon.V10B8e.arch_lower
