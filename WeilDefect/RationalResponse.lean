import WeilDefect.PairGeometry

namespace WeilDefect

open Filter Set
open scoped Topology

/-- Finite rational response attached to residues v at locations rho. -/
noncomputable def rationalResponse {n : ℕ}
    (rho v : Fin n → ℂ) (z : ℂ) : ℂ :=
  ∑ i : Fin n, v i / (z - rho i)

/-- First residue moment. -/
noncomputable def residueFirstMoment {n : ℕ}
    (rho v : Fin n → ℂ) : ℂ :=
  ∑ i : Fin n, rho i * v i

/-- Finite norm-weight controlling the cubic Laurent remainder. -/
noncomputable def residueSecondMomentNorm {n : ℕ}
    (rho v : Fin n → ℂ) : ℝ :=
  ∑ i : Fin n, ‖v i‖ * ‖rho i‖ ^ 2

/--
Exact one-pole Laurent identity through order two.
-/
theorem inv_sub_laurent_two
    (z rho : ℂ)
    (hz : z ≠ 0)
    (hzrho : z ≠ rho) :
    1 / (z - rho)
      =
    1 / z + rho / z ^ 2
      + rho ^ 2 / (z ^ 2 * (z - rho)) := by
  field_simp [hz, sub_ne_zero.mpr hzrho]
  ring

/--
Exact finite Laurent decomposition of the rational response.
-/
theorem rationalResponse_laurent_two
    {n : ℕ}
    (rho v : Fin n → ℂ)
    (z : ℂ)
    (hz : z ≠ 0)
    (hzrho : ∀ i, z ≠ rho i) :
    rationalResponse rho v z
      =
      (∑ i : Fin n, v i) / z
        + residueFirstMoment rho v / z ^ 2
        + ∑ i : Fin n,
            v i * rho i ^ 2 / (z ^ 2 * (z - rho i)) := by
  unfold rationalResponse residueFirstMoment
  calc
    (∑ i : Fin n, v i / (z - rho i))
        =
      ∑ i : Fin n,
        v i * (1 / z + rho i / z ^ 2
          + rho i ^ 2 / (z ^ 2 * (z - rho i))) := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [← inv_sub_laurent_two z (rho i) hz (hzrho i)]
      ring
    _ =
      (∑ i : Fin n, v i) / z
        + (∑ i : Fin n, rho i * v i) / z ^ 2
        + ∑ i : Fin n,
            v i * rho i ^ 2 / (z ^ 2 * (z - rho i)) := by
      simp only [Finset.sum_add_distrib]
      rw [Finset.sum_div, Finset.sum_div]
      congr 1
      · apply Finset.sum_congr rfl
        intro i hi
        ring
      · apply Finset.sum_congr rfl
        intro i hi
        ring

/--
Zero residue moment removes the inverse-linear Laurent term exactly.
-/
theorem rationalResponse_zero_moment_expansion
    {n : ℕ}
    (rho v : Fin n → ℂ)
    (z : ℂ)
    (hv0 : (∑ i : Fin n, v i) = 0)
    (hz : z ≠ 0)
    (hzrho : ∀ i, z ≠ rho i) :
    rationalResponse rho v z
      =
      residueFirstMoment rho v / z ^ 2
        + ∑ i : Fin n,
            v i * rho i ^ 2 / (z ^ 2 * (z - rho i)) := by
  rw [rationalResponse_laurent_two rho v z hz hzrho, hv0, zero_div, zero_add]

/--
Far from every pole, each cubic remainder term has the uniform pointwise
bound needed for WD-T27.
-/
theorem rationalResponse_remainder_term_bound
    (v rho z : ℂ)
    (hz : z ≠ 0)
    (hfar : 2 * ‖rho‖ ≤ ‖z‖) :
    ‖v * rho ^ 2 / (z ^ 2 * (z - rho))‖
      ≤
    2 * (‖v‖ * ‖rho‖ ^ 2) / ‖z‖ ^ 3 := by
  have hzpos : 0 < ‖z‖ := norm_pos_iff.mpr hz
  have hrle : ‖rho‖ ≤ ‖z‖ / 2 := by linarith
  have hsub :
      ‖z‖ / 2 ≤ ‖z - rho‖ := by
    have htri : ‖z‖ - ‖rho‖ ≤ ‖z - rho‖ := norm_sub_norm_le z rho
    linarith
  have hsubpos : 0 < ‖z - rho‖ := lt_of_lt_of_le (half_pos hzpos) hsub
  rw [norm_div, norm_mul, norm_pow, norm_mul, norm_pow]
  have hden :
      ‖z‖ ^ 2 * (‖z‖ / 2)
        ≤ ‖z‖ ^ 2 * ‖z - rho‖ := by
    gcongr
  calc
    ‖v‖ * ‖rho‖ ^ 2 / (‖z‖ ^ 2 * ‖z - rho‖)
        ≤
      ‖v‖ * ‖rho‖ ^ 2 / (‖z‖ ^ 2 * (‖z‖ / 2)) := by
        gcongr
    _ = 2 * (‖v‖ * ‖rho‖ ^ 2) / ‖z‖ ^ 3 := by
      field_simp [hzpos.ne']
      ring

/--
Quantitative cubic remainder estimate for a finite zero-moment response.
-/
theorem rationalResponse_zero_moment_remainder_bound
    {n : ℕ}
    (rho v : Fin n → ℂ)
    (z : ℂ)
    (hv0 : (∑ i : Fin n, v i) = 0)
    (hz : z ≠ 0)
    (hfar : ∀ i, 2 * ‖rho i‖ ≤ ‖z‖) :
    ‖rationalResponse rho v z - residueFirstMoment rho v / z ^ 2‖
      ≤
    2 * residueSecondMomentNorm rho v / ‖z‖ ^ 3 := by
  have hzrho : ∀ i, z ≠ rho i := by
    intro i hzr
    subst z
    have hzpos : 0 < ‖rho i‖ := by
      apply norm_pos_iff.mpr
      intro hr0
      subst rho
      exact hz rfl
    have := hfar i
    linarith
  rw [rationalResponse_zero_moment_expansion rho v z hv0 hz hzrho]
  simp only [add_sub_cancel_left]
  calc
    ‖∑ i : Fin n,
        v i * rho i ^ 2 / (z ^ 2 * (z - rho i))‖
        ≤
      ∑ i : Fin n,
        ‖v i * rho i ^ 2 / (z ^ 2 * (z - rho i))‖ := by
          exact norm_sum_le _ _
    _ ≤
      ∑ i : Fin n,
        (2 * (‖v i‖ * ‖rho i‖ ^ 2) / ‖z‖ ^ 3) := by
          apply Finset.sum_le_sum
          intro i hi
          exact rationalResponse_remainder_term_bound
            (v i) (rho i) z hz (hfar i)
    _ = 2 * residueSecondMomentNorm rho v / ‖z‖ ^ 3 := by
      unfold residueSecondMomentNorm
      rw [← Finset.sum_div]
      congr 1
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i hi
      ring

/--
WD-T27 / ZW1-T8, quantitative form.

For a finite zero-moment residue vector, the response equals its first-moment
inverse-square term plus a uniformly cubic remainder once z lies at least twice
as far from the origin as every pole.
-/
theorem wd_t27_universal_inverse_square_far_decay
    {n : ℕ}
    (rho v : Fin n → ℂ)
    (z : ℂ)
    (hv0 : (∑ i : Fin n, v i) = 0)
    (hz : z ≠ 0)
    (hfar : ∀ i, 2 * ‖rho i‖ ≤ ‖z‖) :
    ‖rationalResponse rho v z - residueFirstMoment rho v / z ^ 2‖
      ≤
    2 * residueSecondMomentNorm rho v / ‖z‖ ^ 3 :=
  rationalResponse_zero_moment_remainder_bound rho v z hv0 hz hfar

end WeilDefect
