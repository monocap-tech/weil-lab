import Mathlib

/-! MASTER-RECON-V03.
Elementary contraction/dense-range proof of the strong Picard limit.
All hypotheses connecting these abstract maps to actual positive resolvents
are explicit; no new axioms and no spectral theorem is assumed. -/

namespace WeilDefect.MasterRecon.V03

open Filter
open scoped Topology BigOperators

variable {H : Type*} [NormedAddCommGroup H] [NormedSpace ℂ H]

/-- A left inverse of T + ηI gives the two required scaled-resolvent laws. -/
theorem scaled_inverse_laws
    (T R : H →L[ℂ] H) (η : ℂ)
    (hR : ∀ x, R (T x + η • x) = x) :
    (∀ x, T x = 0 → η • R x = x) ∧
    (∀ y, η • R (T y) = η • (y - η • R y)) := by
  constructor
  · intro x hx
    simpa only [hx, zero_add, map_smul] using hR x
  · intro y
    have he : R (T y) + η • R y = y := by
      simpa only [map_add, map_smul] using hR y
    have he' : R (T y) = y - η • R y := eq_sub_of_add_eq he
    rw [he']

/-- Quantitative convergence estimate on a single approximate range element.
B is the scaled resolvent, Q is the kernel projection. -/
theorem strong_error_bound
    (T Q B : H →L[ℂ] H) (η : ℝ) (hη : 0 ≤ η)
    (hB : ∀ z, ‖B z‖ ≤ ‖z‖)
    (hfix : ∀ x, B (Q x) = Q x)
    (hres : ∀ y, B (T y) = (η : ℂ) • (y - B y))
    (x y : H) :
    ‖B x - Q x‖ ≤ ‖x - Q x - T y‖ + η * (2 * ‖y‖) := by
  have he : B x - Q x = B (x - Q x - T y) + B (T y) := by
    rw [map_sub, map_sub, hfix]
    abel
  have hr : ‖B (T y)‖ ≤ η * (2 * ‖y‖) := by
    rw [hres, norm_smul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hη]
    apply mul_le_mul_of_nonneg_left _ hη
    calc
      ‖y - B y‖ ≤ ‖y‖ + ‖B y‖ := norm_sub_le _ _
      _ ≤ 2 * ‖y‖ := by linarith [hB y]
  rw [he]
  exact (norm_add_le _ _).trans (add_le_add (hB _) hr)

/-- Sequential strong convergence, without closed range.
The approximation premise is exactly x - Qx ∈ closure(range T).
No uniform rate or norm convergence on the full Hilbert space is claimed. -/
theorem strong_limit_of_range_approx
    (T Q : H →L[ℂ] H) (B : ℕ → H →L[ℂ] H)
    (η : ℕ → ℝ) (hη : ∀ n, 0 ≤ η n)
    (hη0 : Tendsto η atTop (𝓝 0))
    (hB : ∀ n z, ‖B n z‖ ≤ ‖z‖)
    (hfix : ∀ n x, B n (Q x) = Q x)
    (hres : ∀ n y, B n (T y) = (η n : ℂ) • (y - B n y))
    (happrox : ∀ x : H, ∀ ε : ℝ, 0 < ε →
      ∃ y : H, ‖x - Q x - T y‖ < ε)
    (x : H) :
    Tendsto (fun n => B n x) atTop (𝓝 (Q x)) := by
  apply Metric.tendsto_nhds.mpr
  intro ε hε
  obtain ⟨y, hy⟩ := happrox x (ε / 2) (by positivity)
  have ht : Tendsto (fun n => η n * (2 * ‖y‖)) atTop (𝓝 0) := by
    simpa using hη0.mul (tendsto_const_nhds (x := 2 * ‖y‖))
  have hev := (Metric.tendsto_nhds.mp ht) (ε / 2) (by positivity)
  filter_upwards [hev] with n hn
  have hn' : η n * (2 * ‖y‖) < ε / 2 := by
    simpa [Real.dist_eq, sub_zero, abs_of_nonneg (mul_nonneg (hη n) (by positivity))] using hn
  rw [dist_eq_norm]
  have hb := strong_error_bound T Q (B n) (η n) (hη n)
    (hB n) (hfix n) (hres n) x y
  linarith

section FiniteCompression

variable {K : Type*} [NormedAddCommGroup K] [NormedSpace ℂ K]
variable {ι : Type*} [Fintype ι]

/-- A finite-coordinate norm estimate in the original domain norm.
The finite expansion and its coordinate bound are explicit premises;
for an orthonormal basis the latter follows from Cauchy–Schwarz. -/
theorem finite_coordinate_opNorm_bound
    (L : K →L[ℂ] H) (e : ι → K)
    (hexp : ∀ x : K, ∃ a : ι → ℂ,
      x = ∑ i, a i • e i ∧ ∀ i, ‖a i‖ ≤ ‖x‖) :
    ‖L‖ ≤ ∑ i, ‖L (e i)‖ := by
  apply L.opNorm_le_bound (Finset.sum_nonneg fun i _ => norm_nonneg _)
  intro x
  obtain ⟨a, ha, hb⟩ := hexp x
  calc
    ‖L x‖ = ‖∑ i, a i • L (e i)‖ := by
      conv_lhs => rw [ha]
      simp only [map_sum, map_smul]
    _ ≤ ∑ i, ‖a i • L (e i)‖ := norm_sum_le _ _
    _ ≤ ∑ i, ‖x‖ * ‖L (e i)‖ := by
      apply Finset.sum_le_sum
      intro i hi
      rw [norm_smul]
      exact mul_le_mul_of_nonneg_right (hb i) (norm_nonneg _)
    _ = (∑ i, ‖L (e i)‖) * ‖x‖ := by
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl (fun i _ => mul_comm _ _)

end FiniteCompression

end WeilDefect.MasterRecon.V03

#print axioms WeilDefect.MasterRecon.V03.scaled_inverse_laws
#print axioms WeilDefect.MasterRecon.V03.strong_error_bound
#print axioms WeilDefect.MasterRecon.V03.strong_limit_of_range_approx
#print axioms WeilDefect.MasterRecon.V03.finite_coordinate_opNorm_bound
