import WeilDefect.Arithmetic.ActualZetaIV106W02PrimitivePole
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.LaxMilgram

namespace WeilDefect
noncomputable section
open InnerProductSpace ContinuousLinearMap
open scoped InnerProductSpace

section ComplexCoercive
variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]

/-- Quantitative norm bound, valid for complex coercive operators without symmetry. -/
theorem neutralIV106W02I_norm_bound (C : E →L[ℂ] E)
    (hc : ∀ q, (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (C q)).re) (q : E) :
    ‖q‖ ≤ 17 * ‖C q‖ := by
  by_cases hq : q = 0
  · simp [hq]
  · have hp : 0 < ‖q‖ := norm_pos_iff.mpr hq
    have hb : (1/17:ℝ)*‖q‖*‖q‖ ≤ ‖C q‖*‖q‖ := by
      calc
        _ = (1/17:ℝ)*‖q‖^2 := by ring
        _ ≤ (inner ℂ q (C q)).re := hc q
        _ ≤ ‖inner ℂ q (C q)‖ :=
          (le_abs_self _).trans (Complex.abs_re_le_norm _)
        _ ≤ ‖q‖*‖C q‖ := norm_inner_le_norm _ _
        _ = _ := mul_comm _ _
    have h := (mul_le_mul_iff_right₀ hp).mp hb
    linarith only [h]

theorem neutralIV106W02I_anti (C : E →L[ℂ] E)
    (hc : ∀ q, (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (C q)).re) :
    AntilipschitzWith (17 : ℝ≥0) C := by
  apply ContinuousLinearMap.antilipschitz_of_bound C
  intro q
  simpa using neutralIV106W02I_norm_bound C hc q

theorem neutralIV106W02I_ker (C : E →L[ℂ] E)
    (hc : ∀ q, (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (C q)).re) :
    C.ker = ⊥ := by
  rw [LinearMap.ker_eq_bot]
  exact (neutralIV106W02I_anti C hc).injective

theorem neutralIV106W02I_range (C : E →L[ℂ] E)
    (hc : ∀ q, (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (C q)).re) :
    C.range = ⊤ := by
  have hclosed : IsClosed (C.range : Set E) :=
    (neutralIV106W02I_anti C hc).isClosed_range C.uniformContinuous
  letI : CompleteSpace C.range := hclosed.completeSpace_coe
  rw [← C.range.orthogonal_orthogonal]
  rw [Submodule.eq_top_iff']
  intro v w hw
  have hz : inner ℂ w (C w) = 0 :=
    (C.range.mem_orthogonal' w).mp hw (C w) ⟨w, rfl⟩
  have hm := hc w
  rw [hz, Complex.zero_re] at hm
  have hn : ‖w‖ = 0 := by nlinarith [norm_nonneg w]
  have hwzero : w = 0 := norm_eq_zero.mp hn
  simp [hwzero]

def neutralIV106W02I_equiv (C : E →L[ℂ] E)
    (hc : ∀ q, (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (C q)).re) : E ≃L[ℂ] E :=
  ContinuousLinearEquiv.ofBijective C (neutralIV106W02I_ker C hc)
    (neutralIV106W02I_range C hc)

theorem neutralIV106W02I_inverse_norm (C : E →L[ℂ] E)
    (hc : ∀ q, (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (C q)).re) :
    ‖((neutralIV106W02I_equiv C hc).symm : E →L[ℂ] E)‖ ≤ 17 := by
  apply ContinuousLinearMap.opNorm_le_bound _ (by norm_num)
  intro y
  have h := neutralIV106W02I_norm_bound C hc ((neutralIV106W02I_equiv C hc).symm y)
  simpa [neutralIV106W02I_equiv] using h
end ComplexCoercive

abbrev neutralIV106W02IH := NeutralLogHilbertCarrier (11/10:ℝ)
def neutralIV106W02IK : Submodule ℂ neutralIV106W02IH :=
  neutralIV106W02PCellMap.ker

instance neutralIV106W02IK_complete : CompleteSpace neutralIV106W02IK := by
  have hc : IsClosed (neutralIV106W02IK : Set neutralIV106W02IH) := by
    change IsClosed {q : neutralIV106W02IH | neutralIV106W02PCellMap q = 0}
    exact isClosed_eq neutralIV106W02PCellMap.continuous continuous_const
  exact hc.completeSpace_coe

def neutralIV106W02IC : neutralIV106W02IK →L[ℂ] neutralIV106W02IK :=
  neutralIV106W02IK.orthogonalProjectionOnto.comp
    ((neutralActualZetaLogWeilFormOperator (11/10:ℝ)).comp neutralIV106W02IK.subtypeL)

theorem neutralIV106W02I_pair (q r : neutralIV106W02IK) :
    inner ℂ q (neutralIV106W02IC r) =
      inner ℂ (q : neutralIV106W02IH)
        (neutralActualZetaLogWeilFormOperator (11/10:ℝ) (r : neutralIV106W02IH)) := by
  exact neutralIV106W02IK.inner_orthogonalProjectionOnto_eq_of_mem_left q _

theorem neutralIV106W02I_coercive (q : neutralIV106W02IK) :
    (1/17:ℝ)*‖q‖^2 ≤ (inner ℂ q (neutralIV106W02IC q)).re := by
  rw [neutralIV106W02I_pair]
  exact neutralIV106W02PClosedLog17 q.val q.property

def neutralIV106W02IActualEquiv : neutralIV106W02IK ≃L[ℂ] neutralIV106W02IK :=
  neutralIV106W02I_equiv neutralIV106W02IC neutralIV106W02I_coercive

def neutralIV106W02IActualInverse : neutralIV106W02IK →L[ℂ] neutralIV106W02IK :=
  neutralIV106W02IActualEquiv.symm

theorem neutralIV106W02I_right (y : neutralIV106W02IK) :
    neutralIV106W02IC (neutralIV106W02IActualInverse y) = y := by
  exact neutralIV106W02IActualEquiv.apply_symm_apply y

theorem neutralIV106W02I_left (q : neutralIV106W02IK) :
    neutralIV106W02IActualInverse (neutralIV106W02IC q) = q := by
  exact neutralIV106W02IActualEquiv.symm_apply_apply q

theorem neutralIV106W02I_bound : ‖neutralIV106W02IActualInverse‖ ≤ 17 :=
  neutralIV106W02I_inverse_norm neutralIV106W02IC neutralIV106W02I_coercive

#print axioms neutralIV106W02I_norm_bound
#print axioms neutralIV106W02I_anti
#print axioms neutralIV106W02I_ker
#print axioms neutralIV106W02I_range
#print axioms neutralIV106W02I_inverse_norm
#print axioms neutralIV106W02I_pair
#print axioms neutralIV106W02I_coercive
#print axioms neutralIV106W02I_right
#print axioms neutralIV106W02I_left
#print axioms neutralIV106W02I_bound
end
end WeilDefect
