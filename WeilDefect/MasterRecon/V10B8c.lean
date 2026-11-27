import WeilDefect.MasterRecon.V08K
import WeilDefect.MasterRecon.V09B
import WeilDefect.MasterRecon.V10B8a
import Mathlib.Analysis.InnerProductSpace.Adjoint

/-! V10B8c: compact pole receiver through the physical inclusion.
The two real Mellin functionals are represented in restricted L²;
their cross terms are not assumed positive. -/
namespace WeilDefect.MasterRecon.V10B8c

open MeasureTheory Set Complex
open scoped InnerProduct ComplexConjugate
open V08I (logCarrier physicalInclusion FullL2)

noncomputable def expVector (a x : ℝ) : ℂ := (Real.exp (a*x):ℂ)

theorem expVector_mem (t a : ℝ) (ht : 0 ≤ t) :
    MemLp (expVector a) 2 (V08K.supportMeasure t) := by
  have hc : Continuous (expVector a) := by unfold expVector; fun_prop
  apply MemLp.of_bound hc.aestronglyMeasurable (Real.exp (|a| *t))
  filter_upwards [V08K.supportMeasure_bound t] with x hx
  unfold expVector
  rw [Complex.norm_real,Real.norm_eq_abs,abs_of_pos (Real.exp_pos _)]
  apply Real.exp_le_exp.mpr
  calc
    a*x ≤ |a*x| := le_abs_self _
    _ = |a| *|x| := abs_mul _ _
    _ ≤ _ := mul_le_mul_of_nonneg_left hx (abs_nonneg _)

noncomputable def vector (t a : ℝ) (ht : 0 ≤ t) :
    V08F.PhysicalL2 (V08K.supportMeasure t) :=
  (expVector_mem t a ht).toLp (expVector a)

noncomputable def evalRestricted (t a : ℝ) (ht : 0 ≤ t) : FullL2 →L[ℂ] ℂ :=
  (innerSL ℂ (vector t a ht)).comp (V08K.restrictPhysical t)

theorem evalRestricted_eq (t a : ℝ) (ht : 0 ≤ t) (f : FullL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0) :
    evalRestricted t a ht f = V07A.mellin (f : ℝ → ℂ) (a:ℂ) := by
  unfold evalRestricted V07A.mellin
  rw [ContinuousLinearMap.comp_apply,innerSL_apply_apply,L2.inner_def]
  calc
    _ = ∫ x, Complex.exp ((a:ℂ)*(x:ℂ))*f x ∂V08K.supportMeasure t := by
      apply integral_congr_ae
      filter_upwards [MemLp.coeFn_toLp (expVector_mem t a ht),
        V08K.restrictPhysical_ae t f] with x hx hy
      change inner ℂ (vector t a ht x) (V08K.restrictPhysical t f x) = _
      rw [show vector t a ht x = expVector a x from hx,hy]
      change conj (expVector a x) * f x = _
      simp [expVector,← Complex.ofReal_mul,← Complex.ofReal_exp]
    _ = _ := by
      change (∫ x in Icc (-t) t, Complex.exp ((a:ℂ)*(x:ℂ))*f x) = _
      rw [← integral_indicator measurableSet_Icc]
      apply integral_congr_ae
      filter_upwards [hs] with x hx
      by_cases hm : x ∈ Icc (-t) t
      · rw [Set.indicator_of_mem hm]
      · rw [Set.indicator_of_notMem hm,hx hm,mul_zero]

noncomputable def eval (t a : ℝ) (ht : 0 ≤ t) : logCarrier t →L[ℂ] ℂ :=
  (evalRestricted t a ht).comp (physicalInclusion t)

theorem eval_eq (t a : ℝ) (ht : 0 ≤ t) (g : logCarrier t) :
    eval t a ht g = V07A.mellin (physicalInclusion t g : ℝ → ℂ) (a:ℂ) :=
  evalRestricted_eq t a ht _ (V08I.physicalInclusion_support t g)

noncomputable def poleOperator (t : ℝ) (ht : 0 ≤ t) : logCarrier t →L[ℂ] logCarrier t :=
  (eval t (1/2) ht).adjoint ∘L (eval t (-1/2) ht) +
  (eval t (-1/2) ht).adjoint ∘L (eval t (1/2) ht)

theorem pole_selfAdjoint (t : ℝ) (ht : 0 ≤ t) :
    (poleOperator t ht).adjoint = poleOperator t ht := by
  unfold poleOperator
  rw [map_add,ContinuousLinearMap.adjoint_comp,
    ContinuousLinearMap.adjoint_comp,ContinuousLinearMap.adjoint_adjoint,
    ContinuousLinearMap.adjoint_adjoint]
  exact add_comm _ _

theorem pole_pairing (t : ℝ) (ht : 0 ≤ t) (g h : logCarrier t) :
    inner ℂ (poleOperator t ht g) h =
      conj (eval t (-1/2) ht g)*eval t (1/2) ht h +
      conj (eval t (1/2) ht g)*eval t (-1/2) ht h := by
  unfold poleOperator
  rw [ContinuousLinearMap.add_apply,inner_add_left]
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]
  rfl

theorem pole_compact (t : ℝ) (ht : 0 ≤ t) : IsCompactOperator (poleOperator t ht) := by
  have he (a : ℝ) : IsCompactOperator (eval t a ht) :=
    (V08K.physicalInclusion_compact t ht).clm_comp (evalRestricted t a ht)
  exact ((he (-1/2)).clm_comp (eval t (1/2) ht).adjoint).add
    ((he (1/2)).clm_comp (eval t (-1/2) ht).adjoint)

theorem pole_autocorr (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t)
    (f : ℝ → ℂ) (hf : Continuous f) (hfc : HasCompactSupport f)
    (hae : (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f) :
    inner ℂ (poleOperator t ht g) g =
      V10B8a.paperFT (V10B8a.weilTest f f) (I/2) +
      V10B8a.paperFT (V10B8a.weilTest f f) (-I/2) := by
  have hp : I*(I/2) = ((-1/2:ℝ):ℂ) := by
    rw [← mul_div_assoc,Complex.I_mul_I]
    norm_num
  have hm : I*(-I/2) = ((1/2:ℝ):ℂ) := by
    rw [← mul_div_assoc,mul_neg,Complex.I_mul_I]
    norm_num
  have hcp : conj (I/2:ℂ) = -I/2 := by simp [map_ofNat]
  have hcm : conj (-I/2:ℂ) = I/2 := by simp [map_ofNat]
  simp only [pole_pairing,eval_eq,V10B8a.mellin_congr_ae _ f hae,
    V10B8a.paperFT_weilTest hf hf hfc hfc,V10B8a.paperFT_mellin,hcp,hcm,hp,hm]
  ring

end WeilDefect.MasterRecon.V10B8c

#print axioms WeilDefect.MasterRecon.V10B8c.expVector_mem
#print axioms WeilDefect.MasterRecon.V10B8c.evalRestricted_eq
#print axioms WeilDefect.MasterRecon.V10B8c.eval_eq
#print axioms WeilDefect.MasterRecon.V10B8c.pole_selfAdjoint
#print axioms WeilDefect.MasterRecon.V10B8c.pole_pairing
#print axioms WeilDefect.MasterRecon.V10B8c.pole_compact
#print axioms WeilDefect.MasterRecon.V10B8c.pole_autocorr
