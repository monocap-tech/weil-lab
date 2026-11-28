import WeilDefect.Arithmetic.ActualZetaIV106W02ConstrainedInverse
import Mathlib.Analysis.InnerProductSpace.Symmetric

namespace WeilDefect
noncomputable section
open InnerProductSpace ContinuousLinearMap
open scoped InnerProductSpace ComplexConjugate

section RealDiagonal
variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]

/-- Real diagonal determines Hermitian pairing on the complex carrier. -/
theorem neutralIV106W02R_symm_of_real (A : E →L[ℂ] E)
    (hd : ∀ x, ∃ r : ℝ, inner ℂ x (A x) = (r : ℂ))
    (x y : E) : inner ℂ (A x) y = inner ℂ x (A y) := by
  have hs : (A : E →ₗ[ℂ] E).IsSymmetric := by
    apply (LinearMap.isSymmetric_iff_inner_map_self_real (A : E →ₗ[ℂ] E)).2
    intro v
    obtain ⟨r, hr⟩ := hd v
    change conj (inner ℂ (A v) v) = inner ℂ (A v) v
    have hh : inner ℂ (A v) v = (r : ℂ) := by
      rw [← inner_conj_symm (A v) v, hr]
      simp
    rw [hh]
    simp
  exact hs.apply_clm x y
end RealDiagonal

abbrev neutralIV106W02RA :=
  neutralActualZetaLogWeilFormOperator (11/10:ℝ)

set_option maxHeartbeats 2000000 in
theorem neutralIV106W02R_symm (x y : neutralIV106W02IH) :
    inner ℂ (neutralIV106W02RA x) y =
      inner ℂ x (neutralIV106W02RA y) := by
  exact neutralIV106W02R_symm_of_real (E := neutralIV106W02IH)
    neutralIV106W02RA
    (fun v => ⟨_, neutralActualZetaLogWeilFormOperator_diagonal (11/10:ℝ) v⟩) x y

/-- Literal projected action on the admitted cell-null kernel, for every carrier vector. -/
def neutralIV106W02RB : neutralIV106W02IH →L[ℂ] neutralIV106W02IK :=
  neutralIV106W02IK.orthogonalProjectionOnto.comp neutralIV106W02RA

/-- Actual constrained response, using the admitted inverse, not a finite solve. -/
def neutralIV106W02RResponse : neutralIV106W02IH →L[ℂ] neutralIV106W02IK :=
  neutralIV106W02IActualInverse.comp neutralIV106W02RB

theorem neutralIV106W02R_pair (q : neutralIV106W02IK) (v : neutralIV106W02IH) :
    inner ℂ q (neutralIV106W02RB v) =
      inner ℂ (q : neutralIV106W02IH) (neutralIV106W02RA v) := by
  exact neutralIV106W02IK.inner_orthogonalProjectionOnto_eq_of_mem_left q _

set_option maxHeartbeats 2000000 in
theorem neutralIV106W02R_solve (v : neutralIV106W02IH) :
    neutralIV106W02IC (neutralIV106W02RResponse v) = neutralIV106W02RB v := by
  exact neutralIV106W02I_right (neutralIV106W02RB v)

theorem neutralIV106W02R_test (q : neutralIV106W02IK) (v : neutralIV106W02IH) :
    inner ℂ q (neutralIV106W02IC (neutralIV106W02RResponse v)) =
      inner ℂ (q : neutralIV106W02IH) (neutralIV106W02RA v) := by
  rw [neutralIV106W02R_solve, neutralIV106W02R_pair]

set_option maxHeartbeats 2000000 in
/-- Nonnegative energy of the response, with the original quantitative constant. -/
theorem neutralIV106W02R_correction (v : neutralIV106W02IH) :
    (1/17:ℝ)*‖neutralIV106W02RResponse v‖^2 ≤
      (inner ℂ (neutralIV106W02RB v) (neutralIV106W02RResponse v)).re := by
  have h := neutralIV106W02I_coercive (neutralIV106W02RResponse v)
  rw [neutralIV106W02R_solve] at h
  calc
    _ ≤ (inner ℂ (neutralIV106W02RResponse v) (neutralIV106W02RB v)).re := h
    _ = (inner ℂ (neutralIV106W02RB v) (neutralIV106W02RResponse v)).re := by
      rw [← inner_conj_symm (𝕜 := ℂ) (neutralIV106W02RB v)
        (neutralIV106W02RResponse v), Complex.conj_re]

#print axioms neutralIV106W02R_symm_of_real
#print axioms neutralIV106W02R_symm
#print axioms neutralIV106W02R_pair
#print axioms neutralIV106W02R_solve
#print axioms neutralIV106W02R_test
#print axioms neutralIV106W02R_correction
end
end WeilDefect
