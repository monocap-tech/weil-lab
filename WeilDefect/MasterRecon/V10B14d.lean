import WeilDefect.MasterRecon.V10B14a
import WeilDefect.MasterRecon.V10B14c
import WeilDefect.MasterRecon.V10B13b

/-! Exact physical compression and approximate arithmetic operator.
All three lower-order terms are kept in the same middle operator. -/
namespace WeilDefect.MasterRecon.V10B14d

open MeasureTheory
open scoped FourierTransform InnerProduct
open V08I (FullL2 logCarrier physicalInclusion)
open V10B8e (residual realMultiplier)
open V10B8c (evalRestricted)
open V10B14c (pullback)

noncomputable def fourierCLM : FullL2 →L[ℂ] FullL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).toContinuousLinearMap

noncomputable def physicalDefect (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    FullL2 →L[ℂ] FullL2 :=
  pullback fourierCLM (realMultiplier residual hd C hC) +
    (evalRestricted t (1/2) ht).adjoint.comp (evalRestricted t (-1/2) ht) +
    (evalRestricted t (-1/2) ht).adjoint.comp (evalRestricted t (1/2) ht) -
    V10B8d.physicalPrime t

theorem exact_compression (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    V10B8h.arithmeticOperator t ht hd C hC =
      1+pullback (physicalInclusion t) (physicalDefect t ht hd C hC) := by
  unfold V10B8h.arithmeticOperator V10B8e.archOperator V10B8e.correction
    V10B8e.spectralPhysical V10B8c.poleOperator V10B8c.eval
    V10B8d.primeOperator physicalDefect pullback fourierCLM
  simp only [ContinuousLinearMap.adjoint_comp]
  ext g : 1
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.add_apply,
    ContinuousLinearMap.sub_apply,ContinuousLinearMap.one_apply,map_add,map_sub]
  abel

theorem fourier_norm : ‖fourierCLM‖ ≤ 1 := by
  apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
  intro f
  simpa only [fourierCLM,one_mul] using ((Lp.fourierTransformₗᵢ ℝ ℂ).norm_map f).le

theorem physicalDefect_norm (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (hC0 : 0 ≤ C) :
    ‖physicalDefect t ht hd C hC‖ ≤ V10B14a.defectBudget t C := by
  let B := realMultiplier residual hd C hC
  let E := evalRestricted t (1/2) ht
  let F := evalRestricted t (-1/2) ht
  have hB : ‖B‖ ≤ C :=
    ContinuousLinearMap.opNorm_le_bound _ hC0 (V10B8e.realMultiplier_bound residual hd C hC)
  have h₁ := (ContinuousLinearMap.opNorm_comp_le fourierCLM.adjoint (B.comp fourierCLM)).trans
    (mul_le_mul_of_nonneg_left (ContinuousLinearMap.opNorm_comp_le B fourierCLM) (norm_nonneg _))
  rw [ContinuousLinearMap.adjoint.norm_map] at h₁
  have harch : ‖pullback fourierCLM B‖ ≤ C := by
    change ‖fourierCLM.adjoint.comp (B.comp fourierCLM)‖ ≤ C
    refine h₁.trans ?_
    calc
      _ ≤ 1*(‖B‖*1) := mul_le_mul fourier_norm
        (mul_le_mul_of_nonneg_left fourier_norm (norm_nonneg B)) (by positivity) zero_le_one
      _ = ‖B‖ := by ring
      _ ≤ C := hB
  have hE := V10B14a.eval_norm_half t ht (1/2) (by norm_num)
  have hF := V10B14a.eval_norm_half t ht (-1/2) (by norm_num)
  have he : ‖E‖ ≤ Real.sqrt (2*t*Real.exp t) := hE
  have hf : ‖F‖ ≤ Real.sqrt (2*t*Real.exp t) := hF
  have hEF := mul_le_mul he hf (norm_nonneg _) (Real.sqrt_nonneg _)
  rw [← pow_two,Real.sq_sqrt (by positivity)] at hEF
  have h₂ := ContinuousLinearMap.opNorm_comp_le E.adjoint F
  have h₃ := ContinuousLinearMap.opNorm_comp_le F.adjoint E
  rw [ContinuousLinearMap.adjoint.norm_map] at h₂ h₃
  change ‖pullback fourierCLM B+E.adjoint.comp F+F.adjoint.comp E-
    V10B8d.physicalPrime t‖ ≤ _
  unfold V10B14a.defectBudget
  have h₄ := norm_add_le (pullback fourierCLM B) (E.adjoint.comp F)
  have h₅ := norm_add_le (pullback fourierCLM B+E.adjoint.comp F) (F.adjoint.comp E)
  have h₆ := norm_sub_le (pullback fourierCLM B+E.adjoint.comp F+F.adjoint.comp E)
    (V10B8d.physicalPrime t)
  nlinarith only [harch,hEF,h₂,h₃,h₄,h₅,h₆,V10B14a.prime_norm t]

noncomputable def approximateArithmetic (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R)
    (n : ℕ) (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    logCarrier t →L[ℂ] logCarrier t :=
  1+pullback (V10B13a.approximation t R ht hR n) (physicalDefect t ht hd C hC)

theorem arithmetic_action_error (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (hn : (2*Real.pi*R)*t/((n:ℝ)+1) ≤ 1/2)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (hC0 : 0 ≤ C) :
    ‖V10B8h.arithmeticOperator t ht hd C hC-approximateArithmetic t R ht hR n hd C hC‖ ≤
      V10B14a.defectBudget t C*V10B13b.errorBound t R hR n*
        (2*‖physicalInclusion t‖+V10B13b.errorBound t R hR n) := by
  rw [exact_compression]
  unfold approximateArithmetic
  have he := V10B13a.approximation_error t R ht hR n hn
  have he0 := V10B13b.errorBound_nonneg t R ht hR n
  have h := V10B14c.principal_error (physicalInclusion t)
    (V10B13a.approximation t R ht hR n) (physicalDefect t ht hd C hC)
    (V10B13b.errorBound t R hR n) he
  exact h.trans (mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_right (physicalDefect_norm t ht hd C hC hC0) he0) (by positivity))

end WeilDefect.MasterRecon.V10B14d

#print axioms WeilDefect.MasterRecon.V10B14d.exact_compression
#print axioms WeilDefect.MasterRecon.V10B14d.fourier_norm
#print axioms WeilDefect.MasterRecon.V10B14d.physicalDefect_norm
#print axioms WeilDefect.MasterRecon.V10B14d.arithmetic_action_error
