import Mathlib.Analysis.InnerProductSpace.Basic
import WeilDefect.Screening.CanonicalCertificateTransport

namespace WeilDefect.CanonicalCertificate

open scoped InnerProduct

/-- A physical representation of the *whole* weak residual controls its
Riesz error. The identity is required for every canonical test vector.
No completeness or finite-dimensional approximation premise is needed. -/
theorem riesz_error_le_physical_residual
    {D H : Type*} [NormedAddCommGroup D] [InnerProductSpace ℂ D]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (i : D → H) (e : D) (f : H) (k : ℝ)
    (hk : 0 ≤ k)
    (hi : ∀ h, ‖i h‖ ≤ k * ‖h‖)
    (hweak : ∀ h, inner ℂ e h = inner ℂ f (i h)) :
    ‖e‖ ≤ k * ‖f‖ := by
  have hself : ‖inner ℂ e e‖ = ‖e‖ ^ 2 := by
    rw [inner_self_eq_norm_sq_to_K (𝕜 := ℂ), norm_pow,
      RCLike.norm_ofReal, abs_norm]
  have hbound : ‖e‖ ^ 2 ≤ (k * ‖f‖) * ‖e‖ := by
    calc
      _ = ‖inner ℂ e e‖ := hself.symm
      _ = ‖inner ℂ f (i e)‖ := congrArg norm (hweak e)
      _ ≤ ‖f‖ * ‖i e‖ := norm_inner_le_norm _ _
      _ ≤ ‖f‖ * (k * ‖e‖) := mul_le_mul_of_nonneg_left (hi e) (norm_nonneg f)
      _ = (k * ‖f‖) * ‖e‖ := by ring
  by_cases he : ‖e‖ = 0
  · rw [he]
    exact mul_nonneg hk (norm_nonneg f)
  · have hp : 0 < ‖e‖ := lt_of_le_of_ne (norm_nonneg e) (Ne.symm he)
    apply (mul_le_mul_right hp).mp
    nlinarith [hbound]

/-- Squared form of the whole weak-residual theorem, with an exact
inclusion-norm-squared budget suitable for RC32/RC36. -/
theorem riesz_error_sq_le_physical_residual
    {D H : Type*} [NormedAddCommGroup D] [InnerProductSpace ℂ D]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (i : D → H) (e : D) (f : H) (k ρ : ℝ)
    (hk : 0 ≤ k) (hkρ : k ^ 2 ≤ ρ)
    (hi : ∀ h, ‖i h‖ ≤ k * ‖h‖)
    (hweak : ∀ h, inner ℂ e h = inner ℂ f (i h)) :
    ‖e‖ ^ 2 ≤ ρ * ‖f‖ ^ 2 := by
  have h := riesz_error_le_physical_residual i e f k hk hi hweak
  calc
    ‖e‖ ^ 2 ≤ (k * ‖f‖) ^ 2 := pow_le_pow_left₀ (norm_nonneg e) h 2
    _ = k ^ 2 * ‖f‖ ^ 2 := by ring
    _ ≤ ρ * ‖f‖ ^ 2 := mul_le_mul_of_nonneg_right hkρ (sq_nonneg ‖f‖)

end WeilDefect.CanonicalCertificate
