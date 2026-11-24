import WeilDefect.Arithmetic.ActualZetaIV080GammaLinearEnvelopeGate
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_norm_paperFT_mul_sq_le
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Complex

/-!
IV084: direct physical attachment of the literal original source pole
evaluations. Independent of IV081, IV082 and IV083.
No replacement of a mixed pole form by a square, no carrier
identification, no prime attachment, positivity or RH.
-/

/-- The original paperFT evaluated at the positive imaginary pole. -/
theorem neutralIV084PolePlus_physical (k : ℝ → ℂ) :
    Zeta23.paperFT k (Complex.I / 2) =
      ∫ u : ℝ, k u * Complex.exp (-(u : ℂ) / 2) := by
  unfold Zeta23.paperFT
  apply integral_congr_ae
  filter_upwards [] with u
  have he : Complex.I * (Complex.I / 2) * (u : ℂ) =
      -(u : ℂ) / 2 := by
    calc
      _ = (Complex.I * Complex.I) * (u : ℂ) / 2 := by ring
      _ = _ := by rw [Complex.I_mul_I]; ring
  rw [he]

/-- The original paperFT evaluated at the negative imaginary pole. -/
theorem neutralIV084PoleMinus_physical (k : ℝ → ℂ) :
    Zeta23.paperFT k (-Complex.I / 2) =
      ∫ u : ℝ, k u * Complex.exp ((u : ℂ) / 2) := by
  unfold Zeta23.paperFT
  apply integral_congr_ae
  filter_upwards [] with u
  have he : Complex.I * (-Complex.I / 2) * (u : ℂ) =
      (u : ℂ) / 2 := by
    calc
      _ = -(Complex.I * Complex.I) * (u : ℂ) / 2 := by ring
      _ = _ := by rw [Complex.I_mul_I]; ring
  rw [he]

/-- Both source pole integrands are integrable for the compact
continuous test class, with no Fourier-L1 assumption. -/
theorem neutralIV084PoleIntegrands_integrable
    (k : ℝ → ℂ) (hk : Continuous k) {Lam : ℝ}
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    Integrable (fun u : ℝ => k u * Complex.exp (-(u : ℂ) / 2)) ∧
    Integrable (fun u : ℝ => k u * Complex.exp ((u : ℂ) / 2)) := by
  have hm (s : ℝ) : Integrable (fun u : ℝ =>
      k u * Complex.exp ((s : ℂ) * (u : ℂ))) := by
    have hc : Continuous (fun u : ℝ =>
        k u * Complex.exp ((s : ℂ) * (u : ℂ))) := by fun_prop
    have hs : HasCompactSupport (fun u : ℝ =>
        k u * Complex.exp ((s : ℂ) * (u : ℂ))) := by
      apply Zeta23.hasCompactSupport_of_support_subset_abs
      show ∀ u : ℝ, (fun u : ℝ => k u * Complex.exp ((s : ℂ) * (u : ℂ))) u ≠ 0 → |u| ≤ Lam
      intro u hu
      apply hsupp u
      intro hz
      apply hu
      simp [hz]
    exact hc.integrable_of_hasCompactSupport hs
  constructor
  · convert hm (-1 / 2) using 1
    funext u
    have he : -(u : ℂ) / 2 = ((-1 / 2 : ℝ) : ℂ) * (u : ℂ) := by
      push_cast
      ring
    rw [he]
  · convert hm (1 / 2) using 1
    funext u
    have he : (u : ℂ) / 2 = ((1 / 2 : ℝ) : ℂ) * (u : ℂ) := by
      push_cast
      ring
    rw [he]

/-- The sum of the two literal original pole evaluations is one
physical integral, retaining both signs. -/
theorem neutralIV084PoleSum_physical
    (k : ℝ → ℂ) (hk : Continuous k) {Lam : ℝ}
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    Zeta23.paperFT k (Complex.I / 2) +
      Zeta23.paperFT k (-Complex.I / 2) =
      ∫ u : ℝ, k u *
        (Complex.exp (-(u : ℂ) / 2) + Complex.exp ((u : ℂ) / 2)) := by
  obtain ⟨hm, hp⟩ := neutralIV084PoleIntegrands_integrable k hk hsupp
  rw [neutralIV084PolePlus_physical, neutralIV084PoleMinus_physical]
  rw [← integral_add hm hp]
  apply integral_congr_ae
  filter_upwards [] with u
  simp only [Pi.add_apply, mul_add]

#print axioms neutralIV084PolePlus_physical
#print axioms neutralIV084PoleMinus_physical
#print axioms neutralIV084PoleIntegrands_integrable
#print axioms neutralIV084PoleSum_physical

end
end WeilDefect
