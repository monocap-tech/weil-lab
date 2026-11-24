import WeilDefect.Arithmetic.ActualZetaIV075L1FubiniGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory

/-!
IV076 — source-literal, normalized positive-frequency finite-resolvent pairing.

Depends on certified IV074 inverse of original Lorentzian and IV075
arbitrary-L¹ genuine Fubini raw pairing. The ONLY frequency reversal
uses evenness of the Lorentzian Rα; no evenness of h is presumed.
These are finite resolvents; no full original Gamma series or complete
two-pole/prime signed Weil statement is introduced.

Frozen original Phase IV source:
165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- Reattach the exact IV074 rational inversion to the IV075 literal
negative-frequency exponential (with 1/(2π) retained). -/
theorem neutralIV076Kernel_inversion_osc
    (alpha : ℝ) (ha : 0 < alpha) (u : ℝ) :
    neutralIV074Kernel alpha u =
      (1 / (2 * Real.pi) : ℂ) *
        ∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
          neutralIV075Osc r u := by
  simpa only [neutralIV075Osc] using
    neutralIV074Kernel_inversion_rational alpha ha u

/-- Arbitrary L¹ physical correlation paired with the inverse rational
resolvent, keeping the original negative-frequency paperFT on the left.
The proof is just the certified IV075 Fubini swap plus certified IV074
literal rational inversion. -/
theorem neutralIV076L1_pairing_negative
    (alpha : ℝ) (ha : 0 < alpha)
    (h : ℝ → ℂ) (hh : Integrable h) :
    (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
        Zeta23.paperFT h ((-r : ℝ) : ℂ)) =
        ∫ u : ℝ, h u * neutralIV074Kernel alpha u := by
  rw [neutralIV075Fubini_raw alpha ha h hh]
  calc
    (1 / (2 * Real.pi) : ℂ) *
        (∫ u : ℝ, h u *
          (∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
            neutralIV075Osc r u)) =
      ∫ u : ℝ, (1 / (2 * Real.pi) : ℂ) *
        (h u * (∫ r : ℝ,
          (neutralIV074Rational alpha r : ℂ) *
            neutralIV075Osc r u)) := by
          rw [integral_const_mul]
    _ = ∫ u : ℝ, h u * neutralIV074Kernel alpha u := by
      apply integral_congr_ae
      filter_upwards [] with u
      rw [neutralIV076Kernel_inversion_osc alpha ha u]
      ring

/-- Spectral frequency reversal is valid solely because the *original
rational Fourier multiplier* is even. The arbitrary L¹ function h
is NOT assumed even, real-valued, or Hermitian. -/
theorem neutralIV076Rational_frequency_reversal
    (alpha : ℝ) (h : ℝ → ℂ) :
    (∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
      Zeta23.paperFT h ((-r : ℝ) : ℂ)) =
      ∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
        Zeta23.paperFT h (r : ℂ) := by
  let f : ℝ → ℂ := fun r =>
    (neutralIV074Rational alpha r : ℂ) * Zeta23.paperFT h (r : ℂ)
  have hchange : (∫ r : ℝ, f (-r)) = ∫ r : ℝ, f r := by
    simpa using (Measure.integral_comp_mul_left f (-1))
  calc
    _ = ∫ r : ℝ, f (-r) := by
      apply integral_congr_ae
      filter_upwards [] with r
      change (neutralIV074Rational alpha r : ℂ) *
          Zeta23.paperFT h ((-r : ℝ) : ℂ) =
        (neutralIV074Rational alpha (-r) : ℂ) *
          Zeta23.paperFT h ((-r : ℝ) : ℂ)
      rw [neutralIV075Rational_even alpha r]
    _ = ∫ r : ℝ, f r := hchange
    _ = _ := rfl

/-- The exact unnormalized positive-frequency original paperFT and the
genuine physical L¹ pairing coincide with the 1/(2π) factor. The
source definition is preserved, not replaced by a synthetic Fourier
transform or a symmetric correlation assumption. -/
theorem neutralIV076L1_pairing_positive
    (alpha : ℝ) (ha : 0 < alpha)
    (h : ℝ → ℂ) (hh : Integrable h) :
    (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
        (neutralIV074Rational alpha r : ℂ)) =
      ∫ u : ℝ, h u * neutralIV074Kernel alpha u := by
  calc
    _ = (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
        Zeta23.paperFT h (r : ℂ)) := by
      congr 1
      apply integral_congr_ae
      filter_upwards [] with r
      ring
    _ = (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, (neutralIV074Rational alpha r : ℂ) *
        Zeta23.paperFT h ((-r : ℝ) : ℂ)) := by
      rw [neutralIV076Rational_frequency_reversal alpha h]
    _ = _ := neutralIV076L1_pairing_negative alpha ha h hh

#print axioms neutralIV076Kernel_inversion_osc
#print axioms neutralIV076L1_pairing_negative
#print axioms neutralIV076Rational_frequency_reversal
#print axioms neutralIV076L1_pairing_positive

end
end WeilDefect
