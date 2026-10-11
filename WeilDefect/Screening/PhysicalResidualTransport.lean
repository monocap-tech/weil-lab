import Mathlib.Analysis.InnerProductSpace.Basic
import WeilDefect.Screening.CanonicalCertificateTransport

namespace WeilDefect.CanonicalCertificate


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

/-- A squared inclusion budget transports directly, without choosing a
square root. This is the interface for the sharper supported budget. -/
theorem riesz_error_sq_le_of_squared_inclusion
    {D H : Type*} [NormedAddCommGroup D] [InnerProductSpace ℂ D]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (i : D → H) (e : D) (f : H) (ρ : ℝ)
    (hρ : 0 ≤ ρ)
    (hi : ∀ h, ‖i h‖ ^ 2 ≤ ρ * ‖h‖ ^ 2)
    (hweak : ∀ h, inner ℂ e h = inner ℂ f (i h)) :
    ‖e‖ ^ 2 ≤ ρ * ‖f‖ ^ 2 := by
  have hbound : ‖e‖ ^ 2 ≤ ‖f‖ * ‖i e‖ := by
    calc
      _ = ‖inner ℂ e e‖ := by
        rw [inner_self_eq_norm_sq_to_K (𝕜 := ℂ), norm_pow,
          RCLike.norm_ofReal, abs_norm]
      _ = ‖inner ℂ f (i e)‖ := congrArg norm (hweak e)
      _ ≤ ‖f‖ * ‖i e‖ := norm_inner_le_norm _ _
  have hsquared : (‖e‖ ^ 2) ^ 2 ≤
      (ρ * ‖f‖ ^ 2) * ‖e‖ ^ 2 := by
    calc
      _ ≤ (‖f‖ * ‖i e‖) ^ 2 :=
        pow_le_pow_left₀ (sq_nonneg ‖e‖) hbound 2
      _ = ‖f‖ ^ 2 * ‖i e‖ ^ 2 := by ring
      _ ≤ ‖f‖ ^ 2 * (ρ * ‖e‖ ^ 2) :=
        mul_le_mul_of_nonneg_left (hi e) (sq_nonneg ‖f‖)
      _ = (ρ * ‖f‖ ^ 2) * ‖e‖ ^ 2 := by ring
  by_cases he : e = 0
  · subst e
    simpa using mul_nonneg hρ (sq_nonneg ‖f‖)
  · have hepos : 0 < ‖e‖ ^ 2 := sq_pos_of_pos (norm_pos_iff.mpr he)
    nlinarith

/-- Source and trial-action identities imply the whole residual identity.
The operator formula (including endpoint terms) must be attached separately. -/
theorem weak_residual_of_source_and_action
    {D H : Type*} [NormedAddCommGroup D] [InnerProductSpace ℂ D]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (i : D → H) (r v : D) (p action : H)
    (hsource : ∀ h, inner ℂ r h = inner ℂ p (i h))
    (haction : ∀ h, inner ℂ v h = inner ℂ action (i h)) :
    ∀ h, inner ℂ (r - v) h = inner ℂ (p - action) (i h) := by
  intro h
  simp only [inner_sub_left, hsource h, haction h]

end WeilDefect.CanonicalCertificate
