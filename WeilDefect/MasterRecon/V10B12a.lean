import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Normed.Operator.Compact.Basic

/-! V10B12a: effective tail certificate. The finite-rank approximation
is an explicit input, not an assertion of effective compactness.
An arbitrary finite bank can be used; its span need not be orthonormal. -/
namespace WeilDefect.MasterRecon.V10B12a

open Set
open scoped InnerProduct BigOperators

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

def energy (G : H →L[ℂ] H) (x : H) : ℝ := (inner ℂ (G x) x).re

theorem tail_of_rank_approx (G K F : H →L[ℂ] H)
    (S : Submodule ℂ H) (hG : G = 1+K)
    (hF : ∀ x, F x ∈ S) (δ : ℝ) (hδ : ‖K-F‖ ≤ δ)
    (x : H) (hx : x ∈ Sᗮ) :
    (1-δ)*‖x‖^2 ≤ energy G x := by
  have ho : inner ℂ (F x) x = 0 := hx _ (hF x)
  have hE : inner ℂ ((K-F) x) x = inner ℂ (K x) x := by
    rw [ContinuousLinearMap.sub_apply,inner_sub_left,ho,sub_zero]
  have hn : ‖(K-F) x‖ ≤ δ*‖x‖ :=
    ((K-F).le_opNorm x).trans (mul_le_mul_of_nonneg_right hδ (norm_nonneg _))
  have hi := norm_inner_le_norm (𝕜 := ℂ) ((K-F) x) x
  rw [hE] at hi
  have hbound : ‖inner ℂ (K x) x‖ ≤ δ*‖x‖^2 := by
    calc
      _ ≤ ‖(K-F) x‖*‖x‖ := hi
      _ ≤ (δ*‖x‖)*‖x‖ := mul_le_mul_of_nonneg_right hn (norm_nonneg _)
      _ = _ := by ring
  have hre := Complex.abs_re_le_norm (inner ℂ (K x) x)
  have hneg := neg_abs_le (inner ℂ (K x) x).re
  unfold energy
  rw [hG,ContinuousLinearMap.add_apply,ContinuousLinearMap.one_apply,
    inner_add_left,Complex.add_re,inner_self_eq_norm_sq]
  linarith

theorem tail_of_compressed_approx (G K : H →L[ℂ] H) (S : Submodule ℂ H)
    [S.HasOrthogonalProjection] (hG : G = 1+K)
    (δ : ℝ) (hδ : ‖K-S.starProjection.comp K‖ ≤ δ)
    (x : H) (hx : x ∈ Sᗮ) :
    (1-δ)*‖x‖^2 ≤ energy G x :=
  tail_of_rank_approx G K (S.starProjection.comp K) S hG
    (fun z => S.starProjection_apply_mem (K z)) δ hδ x hx

theorem tail_of_factored_approx {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    (G K : H →L[ℂ] H) (S : Submodule ℂ H)
    (U : E →L[ℂ] S) (V : H →L[ℂ] E) (hG : G = 1+K)
    (δ : ℝ) (hδ : ‖K-S.subtypeL.comp (U.comp V)‖ ≤ δ)
    (x : H) (hx : x ∈ Sᗮ) :
    (1-δ)*‖x‖^2 ≤ energy G x :=
  tail_of_rank_approx G K (S.subtypeL.comp (U.comp V)) S hG
    (fun z => (U (V z)).property) δ hδ x hx

theorem finite_span (n : ℕ) (v : Fin n → H) :
    FiniteDimensional ℂ (Submodule.span ℂ (Set.range v)) :=
  FiniteDimensional.span_of_finite ℂ (Set.finite_range v)

end WeilDefect.MasterRecon.V10B12a

#print axioms WeilDefect.MasterRecon.V10B12a.tail_of_rank_approx
#print axioms WeilDefect.MasterRecon.V10B12a.tail_of_compressed_approx
#print axioms WeilDefect.MasterRecon.V10B12a.tail_of_factored_approx
#print axioms WeilDefect.MasterRecon.V10B12a.finite_span
