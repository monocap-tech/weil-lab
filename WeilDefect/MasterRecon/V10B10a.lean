import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.Normed.Operator.Compact.Basic
import Mathlib.Topology.MetricSpace.Antilipschitz
import Mathlib.Topology.Algebra.Module.ContinuousLinearMap.Restrict

/-! Generic normalization on the actual positive-channel range.
No arithmetic hypotheses, and no assumption that the negative channel
is compact. The normalized map is unique on this range. -/
namespace WeilDefect.MasterRecon.V10B10a

open Set
open scoped NNReal InnerProduct

variable {H E F : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E]
variable [NormedAddCommGroup F] [InnerProductSpace ℂ F]

theorem lower_norm (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) (x : H) :
    ‖x‖ ≤ (Real.sqrt (b:ℝ))⁻¹ * ‖A x‖ := by
  have hp : 0 < Real.sqrt (b:ℝ) := Real.sqrt_pos.2 (by exact_mod_cast hb)
  have hs : (Real.sqrt (b:ℝ)*‖x‖)^2 ≤ ‖A x‖^2 := by
    rw [mul_pow,Real.sq_sqrt (by positivity)]
    simpa only [mul_comm] using h x
  have hh := (sq_le_sq₀ (by positivity : 0 ≤ Real.sqrt (b:ℝ)*‖x‖) (norm_nonneg _)).mp hs
  rw [← div_eq_inv_mul]
  exact (le_div_iff₀ hp).mpr (by simpa only [mul_comm] using hh)

theorem positive_injective (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) : Function.Injective A := by
  intro x y he
  have hh := lower_norm A b hb h (x-y)
  rw [map_sub,he,sub_self,norm_zero,mul_zero] at hh
  exact sub_eq_zero.mp (norm_eq_zero.mp (le_antisymm hh (norm_nonneg _)))

theorem positive_range_closed (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) :
    IsClosed (A.range : Set E) := by
  let c : ℝ≥0 := ⟨(Real.sqrt (b:ℝ))⁻¹,by positivity⟩
  have ha : AntilipschitzWith c A := by
    apply AntilipschitzWith.of_le_mul_dist
    intro x y
    rw [dist_eq_norm,dist_eq_norm,← map_sub]
    exact lower_norm A b hb h (x-y)
  exact ha.isClosed_range A.uniformContinuous

noncomputable def rangeEquiv (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) : H ≃ₗ[ℂ] A.range :=
  LinearEquiv.ofInjective A.toLinearMap (positive_injective A b hb h)

noncomputable def receiver (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) : A.range →L[ℂ] H :=
  (rangeEquiv A b hb h).symm.toLinearMap.mkContinuous (Real.sqrt (b:ℝ))⁻¹
    (fun y => by
      obtain ⟨x,rfl⟩ := (rangeEquiv A b hb h).surjective y
      change ‖(rangeEquiv A b hb h).symm (rangeEquiv A b hb h x)‖ ≤
        (Real.sqrt (b:ℝ))⁻¹ * ‖A x‖
      rw [LinearEquiv.symm_apply_apply]
      exact lower_norm A b hb h x)

theorem receiver_left (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) (x : H) :
    receiver A b hb h (A.rangeRestrict x) = x :=
  (rangeEquiv A b hb h).symm_apply_apply x

theorem receiver_right (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) (y : A.range) :
    A.rangeRestrict (receiver A b hb h y) = y :=
  (rangeEquiv A b hb h).apply_symm_apply y

theorem receiver_bound (A : H →L[ℂ] E) (b : ℝ≥0) (hb : 0 < b)
    (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) :
    ‖receiver A b hb h‖ ≤ (Real.sqrt (b:ℝ))⁻¹ := by
  apply ContinuousLinearMap.opNorm_le_bound _ (by positivity)
  intro y
  have hh := lower_norm A b hb h (receiver A b hb h y)
  have he := congrArg Subtype.val (receiver_right A b hb h y)
  change A (receiver A b hb h y) = (y:E) at he
  rw [he] at hh
  exact hh

noncomputable def normalized (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) :
    A.range →L[ℂ] F :=
  B.comp (receiver A b hb h)

theorem normalized_apply (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) (x : H) :
    normalized A B b hb h (A.rangeRestrict x) = B x := by
  simp only [normalized,ContinuousLinearMap.comp_apply,receiver_left]

theorem normalized_unique (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2)
    (D : A.range →L[ℂ] F) (hD : ∀ x, D (A.rangeRestrict x) = B x) :
    D = normalized A B b hb h := by
  ext y : 1
  rw [← receiver_right A b hb h y,hD,normalized_apply]

theorem normalized_bound (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) :
    ‖normalized A B b hb h‖ ≤ ‖B‖*(Real.sqrt (b:ℝ))⁻¹ := by
  apply ContinuousLinearMap.opNorm_le_bound _ (by positivity)
  intro y
  unfold normalized
  rw [ContinuousLinearMap.comp_apply]
  exact (B.le_opNorm _).trans (by
    rw [mul_assoc]
    apply mul_le_mul_of_nonneg_left _ (norm_nonneg B)
    exact ((receiver A b hb h).le_opNorm y).trans
      (mul_le_mul_of_nonneg_right (receiver_bound A b hb h) (norm_nonneg y)))

theorem contraction_iff (A : H →L[ℂ] E) (B : H →L[ℂ] F)
    (b : ℝ≥0) (hb : 0 < b) (h : ∀ x, ‖x‖^2*(b:ℝ) ≤ ‖A x‖^2) :
    ‖normalized A B b hb h‖ ≤ 1 ↔ ∀ x, ‖B x‖^2 ≤ ‖A x‖^2 := by
  constructor
  · intro hc x
    have hh := (normalized A B b hb h).le_opNorm (A.rangeRestrict x)
    rw [normalized_apply] at hh
    change ‖B x‖ ≤ ‖normalized A B b hb h‖ * ‖A x‖ at hh
    have he := hh.trans (by simpa only [one_mul] using
      mul_le_mul_of_nonneg_right hc (norm_nonneg (A x)))
    exact (sq_le_sq₀ (norm_nonneg _) (norm_nonneg _)).mpr he
  · intro hd
    apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
    intro y
    obtain ⟨x,rfl⟩ := (rangeEquiv A b hb h).surjective y
    change ‖normalized A B b hb h (A.rangeRestrict x)‖ ≤ 1*‖A x‖
    rw [normalized_apply,one_mul]
    exact (sq_le_sq₀ (norm_nonneg _) (norm_nonneg _)).mp (hd x)

end WeilDefect.MasterRecon.V10B10a

#print axioms WeilDefect.MasterRecon.V10B10a.lower_norm
#print axioms WeilDefect.MasterRecon.V10B10a.positive_injective
#print axioms WeilDefect.MasterRecon.V10B10a.positive_range_closed
#print axioms WeilDefect.MasterRecon.V10B10a.receiver_left
#print axioms WeilDefect.MasterRecon.V10B10a.receiver_right
#print axioms WeilDefect.MasterRecon.V10B10a.receiver_bound
#print axioms WeilDefect.MasterRecon.V10B10a.normalized_apply
#print axioms WeilDefect.MasterRecon.V10B10a.normalized_unique
#print axioms WeilDefect.MasterRecon.V10B10a.normalized_bound
#print axioms WeilDefect.MasterRecon.V10B10a.contraction_iff
