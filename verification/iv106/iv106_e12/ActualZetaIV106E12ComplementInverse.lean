import WeilDefect.Arithmetic.ActualZetaIV106E11ClosedKernelMargin
import Mathlib.Analysis.InnerProductSpace.LaxMilgram

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate

/-- Complex Hilbert coercivity implies a norm lower bound; no spectral
or self-adjointness assumption is necessary. -/
theorem neutralIV106E12Bounded_below {H : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (A : H →L[ℂ] H) (α : ℝ) (hα : 0 < α)
    (hA : ∀ x, α*‖x‖^2 ≤ (inner ℂ x (A x)).re) (x : H) :
    α*‖x‖ ≤ ‖A x‖ := by
  by_cases hx : x = 0
  · simp [hx]
  · have hn : 0 < ‖x‖ := norm_pos_iff.mpr hx
    apply (mul_le_mul_iff_left₀ hn).mp
    calc
      α*‖x‖*‖x‖ = α*‖x‖^2 := by ring
      _ ≤ (inner ℂ x (A x)).re := hA x
      _ ≤ |(inner ℂ x (A x)).re| := le_abs_self _
      _ ≤ ‖inner ℂ x (A x)‖ := Complex.abs_re_le_norm _
      _ ≤ ‖x‖*‖A x‖ := norm_inner_le_norm _ _
      _ = ‖A x‖*‖x‖ := mul_comm _ _

/-- The norm lower bound supplies injectivity and closed range. -/
theorem neutralIV106E12Antilipschitz {H : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (A : H →L[ℂ] H) (α : ℝ) (hα : 0 < α)
    (hA : ∀ x, α*‖x‖^2 ≤ (inner ℂ x (A x)).re) :
    AntilipschitzWith α⁻¹.toNNReal A := by
  refine ContinuousLinearMap.antilipschitz_of_bound A ?_
  simp_rw [Real.coe_toNNReal', max_eq_left_of_lt (inv_pos.mpr hα), ←
    inv_mul_le_iff₀ (inv_pos.mpr hα), inv_inv]
  exact neutralIV106E12Bounded_below A α hα hA

/-- Closed range plus coercivity rules out every orthogonal obstruction. -/
theorem neutralIV106E12Range {H : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (A : H →L[ℂ] H) (α : ℝ) (hα : 0 < α)
    (hA : ∀ x, α*‖x‖^2 ≤ (inner ℂ x (A x)).re) :
    A.range = ⊤ := by
  have hclosed := (neutralIV106E12Antilipschitz A α hα hA).isClosed_range A.uniformContinuous
  letI : CompleteSpace A.range := hclosed.completeSpace_coe
  rw [← A.range.orthogonal_orthogonal]
  rw [Submodule.eq_top_iff']
  intro v w hw
  have hz : inner ℂ w (A w) = 0 :=
    inner_eq_zero_symm.mp (hw (A w) ⟨w,rfl⟩)
  have h := hA w
  rw [hz, Complex.zero_re] at h
  have hw0 : w = 0 := by
    by_contra hn
    exact (not_lt_of_ge h) (mul_pos hα (pow_pos (norm_pos_iff.mpr hn) 2))
  simp [hw0]

/-- An actual continuous linear equivalence and its quantitative inverse norm. -/
theorem neutralIV106E12Inverse {H : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (A : H →L[ℂ] H) (α : ℝ) (hα : 0 < α)
    (hA : ∀ x, α*‖x‖^2 ≤ (inner ℂ x (A x)).re) :
    ∃ e : H ≃L[ℂ] H, e.toContinuousLinearMap = A ∧
      ‖e.symm.toContinuousLinearMap‖ ≤ α⁻¹ := by
  have hi : A.ker = ⊥ := LinearMap.ker_eq_bot.mpr
    (neutralIV106E12Antilipschitz A α hα hA).injective
  have hr := neutralIV106E12Range A α hα hA
  let e := ContinuousLinearEquiv.ofBijective A hi hr
  refine ⟨e, rfl, ?_⟩
  apply ContinuousLinearMap.opNorm_le_bound _ (inv_nonneg.mpr hα.le)
  intro y
  have h := neutralIV106E12Bounded_below A α hα hA (e.symm y)
  have he : A (e.symm y) = y :=
    ContinuousLinearEquiv.ofBijective_apply_symm_apply A hi hr y
  rw [he] at h
  change ‖e.symm y‖ ≤ α⁻¹*‖y‖
  rw [← div_eq_inv_mul]
  exact (le_div_iff₀ hα).mpr (by simpa only [mul_comm] using h)

def neutralIV106E12Kernel (k : ℕ) (hk : 0 < k) :
    Submodule ℂ (NeutralLogHilbertCarrier (11/10:ℝ)) :=
  (neutralIV106C3Constraints 665 k hk).ker

theorem neutralIV106E12Kernel_closed (k : ℕ) (hk : 0 < k) :
    IsClosed (neutralIV106E12Kernel k hk : Set (NeutralLogHilbertCarrier (11/10:ℝ))) := by
  change IsClosed {q | neutralIV106C3Constraints 665 k hk q = 0}
  exact isClosed_eq (neutralIV106C3Constraints 665 k hk).continuous continuous_const

noncomputable instance neutralIV106E12Kernel_complete (k : ℕ) (hk : 0 < k) :
    CompleteSpace (neutralIV106E12Kernel k hk) :=
  (neutralIV106E12Kernel_closed k hk).completeSpace_coe

/-- Orthogonal compression, not an assumed invariant restriction. -/
def neutralIV106E12Compressed (k : ℕ) (hk : 0 < k) :
    neutralIV106E12Kernel k hk →L[ℂ] neutralIV106E12Kernel k hk :=
  (ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL) ∘L
    (neutralActualZetaLogWeilFormOperator (11/10)) ∘L
      (neutralIV106E12Kernel k hk).subtypeL

theorem neutralIV106E12Compressed_margin (k : ℕ) (hk : 0 < k)
    (x : neutralIV106E12Kernel k hk) :
    neutralIV106E11Alpha*‖x‖^2 ≤
      (inner ℂ x (neutralIV106E12Compressed k hk x)).re := by
  have hx : neutralIV106C3Constraints 665 k hk x.val = 0 := x.property
  have h := neutralIV106E11Closed_log k hk x.val hx
  change neutralIV106E11Alpha*‖x‖^2 ≤
    (inner ℂ x ((ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL)
      (neutralActualZetaLogWeilFormOperator (11/10) x.val))).re
  rw [adjoint_inner_right]
  exact h

/-- The genuine compressed complementary inverse, with its certified norm target. -/
theorem neutralIV106E12Actual_inverse (k : ℕ) (hk : 0 < k) :
    ∃ e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk,
      e.toContinuousLinearMap = neutralIV106E12Compressed k hk ∧
      ‖e.symm.toContinuousLinearMap‖ ≤ neutralIV106E11Alpha⁻¹ :=
  neutralIV106E12Inverse _ _ neutralIV106E11Alpha_pos
    (neutralIV106E12Compressed_margin k hk)

#print axioms neutralIV106E12Bounded_below
#print axioms neutralIV106E12Antilipschitz
#print axioms neutralIV106E12Range
#print axioms neutralIV106E12Inverse
#print axioms neutralIV106E12Kernel_closed
#print axioms neutralIV106E12Compressed_margin
#print axioms neutralIV106E12Actual_inverse
end
end WeilDefect
