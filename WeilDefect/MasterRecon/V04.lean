import Mathlib
import Mathlib.Analysis.InnerProductSpace.Positive

/-! MASTER-RECON V04: actual positive-resolvent construction and
closed-range-complement identity. No finite-dimensional assumption. -/

namespace WeilDefect.MasterRecon.V04

open scoped InnerProduct NNReal

variable {H K : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]

/-- The energy coercivity estimate of T + ηI. -/
theorem shifted_energy_lower
    (T : H →L[ℂ] H) (hT : T.IsPositive) (η : ℝ≥0) (x : H) :
    ‖x‖ ^ 2 * (η : ℝ) ≤
      (inner ℂ (T x + ((η : ℝ) : ℂ) • x) x).re := by
  have h := hT.re_inner_nonneg_left x
  have hs : (inner ℂ (((η : ℝ) : ℂ) • x) x).re =
      (η : ℝ) * ‖x‖ ^ 2 := by
    rw [inner_smul_left, inner_self_eq_norm_sq_to_K]
    simp [Complex.mul_re, pow_two]
  rw [inner_add_left, Complex.add_re, hs]
  linarith

/-- Existence of the inverse via the Hilbert coercivity theorem. -/
theorem positive_shift_isUnit
    (T : H →L[ℂ] H) (hT : T.IsPositive)
    (η : ℝ≥0) (hη : 0 < η) :
    IsUnit (T + ((η : ℝ) : ℂ) • (1 : H →L[ℂ] H)) := by
  apply ContinuousLinearMap.isUnit_of_forall_le_norm_inner_map _ hη
  intro x
  have h := shifted_energy_lower T hT η x
  have he : (T + ((η : ℝ) : ℂ) • (1 : H →L[ℂ] H)) x =
      T x + ((η : ℝ) : ℂ) • x := by
    simp
  rw [he]
  exact h.trans (Complex.re_le_norm _)

/-- A right inverse of a positive shift gives the required contraction. -/
theorem scaled_inverse_contraction
    (T R : H →L[ℂ] H) (hT : T.IsPositive) (η : ℝ≥0)
    (hR : ∀ x, T (R x) + ((η : ℝ) : ℂ) • R x = x) (x : H) :
    ‖((η : ℝ) : ℂ) • R x‖ ≤ ‖x‖ := by
  have h := shifted_energy_lower T hT η (R x)
  rw [hR x] at h
  have hcs := re_inner_le_norm (𝕜 := ℂ) x (R x)
  rw [norm_smul, show ‖((η : ℝ) : ℂ)‖ = (η : ℝ) by simp [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (show 0 ≤ (η : ℝ) from η.coe_nonneg)]]
  by_cases hz : ‖R x‖ = 0
  · simp [hz]
  · have hp : 0 < ‖R x‖ := lt_of_le_of_ne (norm_nonneg _) (Ne.symm hz)
    apply (mul_le_mul_right₀ hp).mp
    nlinarith

/-- The exact coefficient range closure, not an assertion of closed range. -/
theorem gram_range_closure
    (S : H →L[ℂ] K) :
    (S† ∘L S).range.topologicalClosure = S.kerᗮ := by
  have h := (S† ∘L S).orthogonal_ker
  rw [ContinuousLinearMap.adjoint_comp, ContinuousLinearMap.adjoint_adjoint,
    ContinuousLinearMap.ker_adjoint_comp_self] at h
  exact h.symm


/-- Explicit two-sided inverse, in exactly the application convention of V02/V03. -/
theorem positive_shift_inverse
    (T : H →L[ℂ] H) (hT : T.IsPositive)
    (η : ℝ≥0) (hη : 0 < η) :
    ∃ R : H →L[ℂ] H,
      (∀ x, R (T x + ((η : ℝ) : ℂ) • x) = x) ∧
      (∀ x, T (R x) + ((η : ℝ) : ℂ) • R x = x) ∧
      (∀ x, ‖((η : ℝ) : ℂ) • R x‖ ≤ ‖x‖) := by
  obtain ⟨u, hu⟩ := positive_shift_isUnit T hT η hη
  let R : H →L[ℂ] H := ↑(u⁻¹)
  have hl : ∀ x, R (T x + ((η : ℝ) : ℂ) • x) = x := by
    intro x
    have h := congrArg (fun f : H →L[ℂ] H => f x) u.inv_mul
    change R ((↑u : H →L[ℂ] H) x) = x at h
    rw [hu] at h
    simpa using h
  have hr : ∀ x, T (R x) + ((η : ℝ) : ℂ) • R x = x := by
    intro x
    have h := congrArg (fun f : H →L[ℂ] H => f x) u.mul_inv
    change (↑u : H →L[ℂ] H) (R x) = x at h
    rw [hu] at h
    simpa using h
  exact ⟨R, hl, hr, scaled_inverse_contraction T R hT η hr⟩

/-- The range approximation premise in V03 for the actual kernel projection. -/
theorem gram_range_approximation
    (S : H →L[ℂ] K) [S.ker.HasOrthogonalProjection]
    (x : H) (ε : ℝ) (hε : 0 < ε) :
    ∃ y : H, ‖x - S.ker.starProjection x - (S† ∘L S) y‖ < ε := by
  have h : x - S.ker.starProjection x ∈ S.kerᗮ :=
    Submodule.sub_starProjection_mem_orthogonal x
  rw [← gram_range_closure S] at h
  change x - S.ker.starProjection x ∈ closure (Set.range (S† ∘L S)) at h
  obtain ⟨z, ⟨y, rfl⟩, hz⟩ := Metric.mem_closure_iff.mp h ε hε
  exact ⟨y, by simpa [dist_eq_norm, norm_sub_rev] using hz⟩

end WeilDefect.MasterRecon.V04

#print axioms WeilDefect.MasterRecon.V04.shifted_energy_lower
#print axioms WeilDefect.MasterRecon.V04.positive_shift_isUnit
#print axioms WeilDefect.MasterRecon.V04.scaled_inverse_contraction
#print axioms WeilDefect.MasterRecon.V04.gram_range_closure

#print axioms WeilDefect.MasterRecon.V04.positive_shift_inverse
#print axioms WeilDefect.MasterRecon.V04.gram_range_approximation
