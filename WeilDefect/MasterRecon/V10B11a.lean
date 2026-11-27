import WeilDefect.MasterRecon.V10B10b
import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.LinearAlgebra.FiniteDimensional.Basic

/-! Compact-defect finite-dimensional reduction. The finite space is
obtained from a finite norm cover of the compact image, not a truncation
of the arithmetic zero index. -/
namespace WeilDefect.MasterRecon.V10B11a

open Set Metric
open scoped InnerProduct NNReal

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

theorem compact_cover (K : H →L[ℂ] H) (hK : IsCompactOperator K)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ S : Set H, S.Finite ∧ ∀ x : H, ‖x‖ ≤ 1 →
      ∃ z ∈ S, ‖K x-z‖ < ε := by
  have hc : IsCompactOperator K.toLinearMap := hK
  obtain ⟨C,hC,himage⟩ := hc.image_closedBall_subset_compact 1
  obtain ⟨S,hS,hcov⟩ := Metric.totallyBounded_iff.mp hC.totallyBounded ε hε
  refine ⟨S,hS,?_⟩
  intro x hx
  have hmem : K x ∈ C := himage ⟨x,by simpa [mem_closedBall,dist_zero_right] using hx,rfl⟩
  have h := hcov hmem
  simp only [mem_iUnion,mem_ball] at h
  obtain ⟨z,hz,hxz⟩ := h
  exact ⟨z,hz,by simpa [dist_eq_norm] using hxz⟩

theorem compact_tail_quadratic (K : H →L[ℂ] H) (hK : IsCompactOperator K)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ S : Submodule ℂ H, FiniteDimensional ℂ S ∧
      ∀ x ∈ Sᗮ, |(inner ℂ (K x) x).re| ≤ ε*‖x‖^2 := by
  obtain ⟨C,hC,hcov⟩ := compact_cover K hK ε hε
  let S := Submodule.span ℂ C
  refine ⟨S,FiniteDimensional.span_of_finite ℂ hC,?_⟩
  intro x hx
  by_cases hz : x = 0
  · simp [hz]
  have hp : 0 < ‖x‖ := norm_pos_iff.mpr hz
  let a : ℂ := ((‖x‖)⁻¹:ℝ)
  let u := a • x
  have ha : ‖a‖ = ‖x‖⁻¹ := by
    dsimp [a]
    rw [Complex.norm_real,Real.norm_eq_abs,abs_of_pos (inv_pos.mpr hp)]
  have hu : ‖u‖ = 1 := by dsimp [u]; rw [norm_smul,ha,inv_mul_cancel₀ hp.ne']
  have hU : u ∈ Sᗮ := Sᗮ.smul_mem a hx
  obtain ⟨z,hzC,huz⟩ := hcov u hu.le
  have hzS : z ∈ S := Submodule.subset_span hzC
  have ho : inner ℂ z u = 0 := hU z hzS
  have hi : inner ℂ (K u-z) u = inner ℂ (K u) u := by rw [inner_sub_left,ho,sub_zero]
  have hn := norm_inner_le_norm (𝕜 := ℂ) (K u-z) u
  rw [hi,hu,mul_one] at hn
  have hr := (Complex.abs_re_le_norm (inner ℂ (K u) u)).trans (hn.trans huz.le)
  have hxrep : x = (‖x‖:ℂ) • u := by
    dsimp [u,a]
    rw [smul_smul]
    rw [mul_inv_cancel₀ hp.ne',one_smul]
  calc
    |(inner ℂ (K x) x).re| = ‖x‖^2 * |(inner ℂ (K u) u).re| := by
      conv_lhs => rw [hxrep,K.map_smul,inner_smul_left,inner_smul_right]
      simp only [Complex.conj_ofReal,← mul_assoc,← Complex.ofReal_mul,Complex.re_ofReal_mul,abs_mul]
      rw [abs_of_nonneg (norm_nonneg x)]
      ring
    _ ≤ ε*‖x‖^2 := by
      simpa only [mul_comm] using mul_le_mul_of_nonneg_left hr (sq_nonneg ‖x‖)

theorem finite_exceptional_sector (G K : H →L[ℂ] H) (hK : IsCompactOperator K)
    (hG : G = 1+K) :
    ∃ S : Submodule ℂ H, FiniteDimensional ℂ S ∧
      ∀ x ∈ Sᗮ, (1/2:ℝ)*‖x‖^2 ≤ (inner ℂ (G x) x).re := by
  obtain ⟨S,hS,htail⟩ := compact_tail_quadratic K hK (1/2) (by norm_num)
  refine ⟨S,hS,?_⟩
  intro x hx
  have h := htail x hx
  have hl := (abs_le.mp h).1
  rw [hG,ContinuousLinearMap.add_apply,ContinuousLinearMap.one_apply,
    inner_add_left,Complex.add_re]
  have hxnorm : (inner ℂ x x).re = ‖x‖^2 := inner_self_eq_norm_sq (𝕜 := ℂ) x
  rw [hxnorm]
  linarith

theorem finite_negative_subspace_injective (G : H →L[ℂ] H) (S W : Submodule ℂ H)
    [S.HasOrthogonalProjection]
    (htail : ∀ x ∈ Sᗮ, (1/2:ℝ)*‖x‖^2 ≤ (inner ℂ (G x) x).re)
    (hneg : ∀ x ∈ W, (inner ℂ (G x) x).re ≤ 0) :
    Function.Injective (S.orthogonalProjectionOnto.comp W.subtypeL) := by
  intro x y hxy
  have hz : S.orthogonalProjectionOnto ((x: H)-(y:H)) = 0 := by
    change S.orthogonalProjectionOnto (x:H) = S.orthogonalProjectionOnto (y:H) at hxy
    rw [map_sub,hxy,sub_self]
  have ho := S.orthogonalProjectionOnto_eq_zero_iff.mp hz
  have hh := htail ((x:H)-(y:H)) ho
  have hn := hneg _ (W.sub_mem x.property y.property)
  have he : ‖(x:H)-(y:H)‖ = 0 := by nlinarith [norm_nonneg ((x:H)-(y:H))]
  exact Subtype.ext (sub_eq_zero.mp (norm_eq_zero.mp he))

end WeilDefect.MasterRecon.V10B11a

#print axioms WeilDefect.MasterRecon.V10B11a.compact_cover
#print axioms WeilDefect.MasterRecon.V10B11a.compact_tail_quadratic
#print axioms WeilDefect.MasterRecon.V10B11a.finite_exceptional_sector
#print axioms WeilDefect.MasterRecon.V10B11a.finite_negative_subspace_injective
