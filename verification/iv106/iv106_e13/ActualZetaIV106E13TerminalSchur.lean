import WeilDefect.Arithmetic.ActualZetaIV106E12ComplementInverse
import Mathlib.Analysis.InnerProductSpace.Projection.FiniteDimensional

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate

/-- A real diagonal for a complex-linear form forces real symmetry of
its mixed terms, by polarization with the imaginary unit. -/
theorem neutralIV106E13Real_symm {H : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (W : H →L[ℂ] H) (h : ∀ x, (inner ℂ x (W x)).im = 0)
    (x y : H) : (inner ℂ x (W y)).re = (inner ℂ y (W x)).re := by
  have hp := h (x + Complex.I • y)
  simp only [map_add, map_smul, inner_add_left, inner_add_right,
    inner_smul_left, inner_smul_right, Complex.add_im, Complex.mul_im,
    Complex.conj_I, Complex.I_re, Complex.I_im, Complex.neg_re, Complex.neg_im,
    zero_mul, one_mul, neg_mul, mul_zero, mul_one, zero_add, add_zero,
    h] at hp
  linarith

theorem neutralIV106E13Native_symm (a : ℝ)
    (x y : NeutralLogHilbertCarrier a) :
    (inner ℂ x (neutralActualZetaLogWeilFormOperator a y)).re =
    (inner ℂ y (neutralActualZetaLogWeilFormOperator a x)).re := by
  apply neutralIV106E13Real_symm
  intro z
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_im]

/-- Completion of the quadratic form after solving the response equation.
This identity requires no positivity assumption on the finite sector. -/
theorem neutralIV106E13Completion {H : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (W : H →L[ℂ] H) (x y u : H)
    (hs : ∀ p q, (inner ℂ p (W q)).re = (inner ℂ q (W p)).re)
    (hxu : (inner ℂ x (W u)).re = (inner ℂ x (W y)).re)
    (hu : (inner ℂ u (W u)).re = (inner ℂ u (W y)).re) :
    (inner ℂ (x+y) (W (x+y))).re =
      (inner ℂ (x+u) (W (x+u))).re +
      ((inner ℂ y (W y)).re - (inner ℂ u (W u)).re) := by
  simp only [map_add, inner_add_left, inner_add_right, Complex.add_re]
  linarith only [hxu,hu,hs x y,hs x u]

abbrev neutralIV106E13H := NeutralLogHilbertCarrier (11/10:ℝ)

def neutralIV106E13Finite (k : ℕ) (hk : 0 < k) : Submodule ℂ neutralIV106E13H :=
  (neutralIV106E12Kernel k hk)ᗮ

/-- The receiving sector injects into the concrete finite constraint codomain. -/
theorem neutralIV106E13Finite_dim (k : ℕ) (hk : 0 < k) :
    FiniteDimensional ℂ (neutralIV106E13Finite k hk) := by
  let T := neutralIV106C3Constraints 665 k hk
  let F := neutralIV106E13Finite k hk
  let L := T.toLinearMap.comp F.subtype
  apply FiniteDimensional.of_injective L
  apply LinearMap.ker_eq_bot.mp
  rw [Submodule.eq_bot_iff]
  intro y hy
  have hT : T y.val = 0 := hy
  have hK : y.val ∈ neutralIV106E12Kernel k hk := hT
  have horth : y.val ∈ (neutralIV106E12Kernel k hk)ᗮ := y.property
  have hz := (Submodule.mem_orthogonal _ _).mp horth y.val hK
  have hy0 : y.val = 0 := inner_self_eq_zero.mp hz
  exact Subtype.ext hy0

/-- Exact decomposition into the actual closed kernel and its orthogonal sector. -/
theorem neutralIV106E13Split (k : ℕ) (hk : 0 < k) (q : neutralIV106E13H) :
    ∃ x : neutralIV106E12Kernel k hk, ∃ y : neutralIV106E13Finite k hk,
      q = x.val + y.val := by
  let K := neutralIV106E12Kernel k hk
  have htop : q ∈ K ⊔ Kᗮ := by
    rw [K.sup_orthogonal_of_hasOrthogonalProjection]
    exact Submodule.mem_top
  obtain ⟨x,hx,y,hy,he⟩ := Submodule.mem_sup.mp htop
  exact ⟨⟨x,hx⟩,⟨y,hy⟩,he.symm⟩

/-- Use the actual complementary inverse to solve the response equation. -/
def neutralIV106E13Response (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (y : neutralIV106E13Finite k hk) : neutralIV106E12Kernel k hk :=
  e.symm ((ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL)
    (neutralActualZetaLogWeilFormOperator (11/10) y.val))

theorem neutralIV106E13Response_pair (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (x : neutralIV106E12Kernel k hk) (y : neutralIV106E13Finite k hk) :
    inner ℂ x.val (neutralActualZetaLogWeilFormOperator (11/10)
      (neutralIV106E13Response k hk e y).val) =
    inner ℂ x.val (neutralActualZetaLogWeilFormOperator (11/10) y.val) := by
  have h : neutralIV106E12Compressed k hk (neutralIV106E13Response k hk e y) =
    (ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL)
      (neutralActualZetaLogWeilFormOperator (11/10) y.val) := by
    rw [← he]
    exact e.apply_symm_apply _
  have hi := congrArg (inner ℂ x) h
  change inner ℂ x ((ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL)
    (neutralActualZetaLogWeilFormOperator (11/10)
      (neutralIV106E13Response k hk e y).val)) = _ at hi
  simpa only [adjoint_inner_right] using hi

def neutralIV106E13Energy (q : neutralIV106E13H) : ℝ :=
  (inner ℂ q (neutralActualZetaLogWeilFormOperator (11/10) q)).re

def neutralIV106E13Schur (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (y : neutralIV106E13Finite k hk) : ℝ :=
  neutralIV106E13Energy y.val -
    neutralIV106E13Energy (neutralIV106E13Response k hk e y).val

theorem neutralIV106E13Actual_completion (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (x : neutralIV106E12Kernel k hk) (y : neutralIV106E13Finite k hk) :
    neutralIV106E13Energy (x.val+y.val) =
      neutralIV106E13Energy (x.val+(neutralIV106E13Response k hk e y).val) +
        neutralIV106E13Schur k hk e y := by
  unfold neutralIV106E13Energy neutralIV106E13Schur
  exact neutralIV106E13Completion _ _ _ _
    (neutralIV106E13Native_symm _)
    (congrArg Complex.re (neutralIV106E13Response_pair k hk e he x y))
    (congrArg Complex.re (neutralIV106E13Response_pair k hk e he
      (neutralIV106E13Response k hk e y) y))

/-- Global nonnegativity is equivalent to the finite Schur obligation,
conditional on the actual complementary inverse and E11 coercivity. -/
theorem neutralIV106E13Nonnegative_iff (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk) :
    (∀ q : neutralIV106E13H, 0 ≤ neutralIV106E13Energy q) ↔
      (∀ y : neutralIV106E13Finite k hk, 0 ≤ neutralIV106E13Schur k hk e y) := by
  constructor
  · intro h y
    have hq := h ((-neutralIV106E13Response k hk e y).val+y.val)
    rw [neutralIV106E13Actual_completion k hk e he] at hq
    simpa [neutralIV106E13Energy] using hq
  · intro h q
    obtain ⟨x,y,rfl⟩ := neutralIV106E13Split k hk q
    rw [neutralIV106E13Actual_completion k hk e he]
    let z : neutralIV106E12Kernel k hk := x+neutralIV106E13Response k hk e y
    have hz : 0 ≤ neutralIV106E13Energy z.val :=
      (mul_nonneg neutralIV106E11Alpha_pos.le (sq_nonneg _)).trans
        (neutralIV106E11Closed_log k hk z.val z.property)
    exact add_nonneg hz (h y)

#print axioms neutralIV106E13Real_symm
#print axioms neutralIV106E13Native_symm
#print axioms neutralIV106E13Completion
#print axioms neutralIV106E13Finite_dim
#print axioms neutralIV106E13Split
#print axioms neutralIV106E13Response_pair
#print axioms neutralIV106E13Actual_completion
#print axioms neutralIV106E13Nonnegative_iff
end
end WeilDefect
