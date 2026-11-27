import WeilDefect.MasterRecon.V10B13a
import WeilDefect.MasterRecon.V10B12a

/-! V10B13b: a finite bank of moment representers controls the tail
directly in the physical norm. The signed physical defect is a premise;
no explicit formula or positivity claim is imported here. -/
namespace WeilDefect.MasterRecon.V10B13b

open Set
open scoped InnerProduct BigOperators
open V08I (logCarrier physicalInclusion)
open V10B13a (moment approximation remainderBound input out)
open V10B12a (energy)

noncomputable def retained (t : ℝ) (ht : 0 ≤ t) (n : ℕ) :
    Submodule ℂ (logCarrier t) :=
  Submodule.span ℂ (Set.range (fun j : Fin n => (moment t ht j.val).adjoint 1))

theorem retained_finite (t : ℝ) (ht : 0 ≤ t) (n : ℕ) :
    FiniteDimensional ℂ (retained t ht n) :=
  FiniteDimensional.span_of_finite ℂ (Set.finite_range _)

theorem retained_moment_zero (t : ℝ) (ht : 0 ≤ t) (n : ℕ)
    (g : logCarrier t) (hg : g ∈ (retained t ht n)ᗮ) (j : ℕ) (hj : j < n) :
    moment t ht j g = 0 := by
  have hm : (moment t ht j).adjoint 1 ∈ retained t ht n :=
    Submodule.subset_span ⟨⟨j,hj⟩,rfl⟩
  have ho := hg _ hm
  rw [ContinuousLinearMap.adjoint_inner_left,Complex.inner_apply] at ho
  simpa using ho

noncomputable def errorBound (t R : ℝ) (hR : 0 ≤ R) (n : ℕ) : ℝ :=
  (Real.sqrt (Real.log (2+R)))⁻¹ + ‖out R hR‖*remainderBound t R n*‖input t‖

theorem errorBound_nonneg (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ) :
    0 ≤ errorBound t R hR n := by
  unfold errorBound remainderBound
  positivity

theorem physical_tail (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (hn : (2*Real.pi*R)*t/((n:ℝ)+1) ≤ 1/2)
    (g : logCarrier t) (hg : g ∈ (retained t ht n)ᗮ) :
    ‖physicalInclusion t g‖ ≤ errorBound t R hR n * ‖g‖ := by
  have hz := V10B13a.approximation_zero t R ht hR n g
    (fun j hj => retained_moment_zero t ht n g hg j hj)
  have h := ((physicalInclusion t-approximation t R ht hR n).le_opNorm g).trans
    (mul_le_mul_of_nonneg_right (V10B13a.approximation_error t R ht hR n hn) (norm_nonneg g))
  rw [ContinuousLinearMap.sub_apply,hz,sub_zero] at h
  exact h

theorem physical_defect_tail (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (hn : (2*Real.pi*R)*t/((n:ℝ)+1) ≤ 1/2)
    (G : logCarrier t →L[ℂ] logCarrier t)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ g, ‖g‖^2-M*‖physicalInclusion t g‖^2 ≤ energy G g)
    (g : logCarrier t) (hg : g ∈ (retained t ht n)ᗮ) :
    (1-M*(errorBound t R hR n)^2)*‖g‖^2 ≤ energy G g := by
  have hb := physical_tail t R ht hR n hn g hg
  have hsq := (sq_le_sq₀ (norm_nonneg _) (by
    exact mul_nonneg (errorBound_nonneg t R ht hR n) (norm_nonneg _))).mpr hb
  rw [mul_pow] at hsq
  have hm := mul_le_mul_of_nonneg_left hsq hM
  nlinarith only [hdef g,hm]

end WeilDefect.MasterRecon.V10B13b

#print axioms WeilDefect.MasterRecon.V10B13b.retained_finite
#print axioms WeilDefect.MasterRecon.V10B13b.retained_moment_zero
#print axioms WeilDefect.MasterRecon.V10B13b.errorBound_nonneg
#print axioms WeilDefect.MasterRecon.V10B13b.physical_tail
#print axioms WeilDefect.MasterRecon.V10B13b.physical_defect_tail
