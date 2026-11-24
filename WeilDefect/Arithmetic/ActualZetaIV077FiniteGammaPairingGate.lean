import WeilDefect.Arithmetic.ActualZetaIV076L1PositiveFrequencyGate
import WeilDefect.Arithmetic.ActualZetaIV071GammaFinitePrelude
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped FourierTransform

/-!
IV077 — literal NF599 first-mode Gamma pairing, source-preserving.
IV071 is carried byte-for-byte from its separately verified sibling
draft commit acf0d64e54f3dbfde814258889faac608df9bcc5.
IV076 supplies genuine general-L¹ positive-frequency Fubini.
No assertion is made about the infinite Gamma limit, either crossed
pole, the signed prime powers, global Weil positivity, or RH.
Frozen original Phase IV source:
165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- Original paper positive-frequency Fourier transform on the real line
is L¹ when the Mathlib Fourier transform is L¹. This uses the exact
source dictionary and the nonzero -1/(2π) dilation. -/
theorem neutralIV077PaperFT_integrable
    (h : ℝ → ℂ) (hF : Integrable (𝓕 h)) :
    Integrable (fun r : ℝ => Zeta23.paperFT h (r : ℂ)) := by
  have hn : (-1 / (2 * Real.pi) : ℝ) ≠ 0 := by positivity
  have hcomp : Integrable
      (fun r : ℝ => (𝓕 h) ((-1 / (2 * Real.pi)) * r)) :=
    hF.comp_mul_left' hn
  convert hcomp using 1
  funext r
  rw [Zeta23.EF.paperFT_ofReal_eq_fourier_Zeta23_EF_paper_inversion]
  congr 1
  ring

/-- Existing literal original Fourier inversion at the physical origin.
The constant in the NF599 gain must use this; h∈L¹ alone would not
justify pointwise Fourier inversion at zero. -/
theorem neutralIV077PaperFT_inversion_zero
    (h : ℝ → ℂ) (hc : Continuous h)
    (hh : Integrable h) (hF : Integrable (𝓕 h)) :
    (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, Zeta23.paperFT h (r : ℂ)) = h 0 := by
  simpa using (Zeta23.EF.paper_inversion hc hh hF 0).symm

/-- Actual NF599 gain re-expressed with the previously certified IV074
Lorentzian: source's α is exactly 2a, with NO substitute Gamma symbol. -/
theorem neutralIV077NF599Gain_eq_rational
    (a r : ℝ) (ha : 0 < a) :
    neutralNF599Gain a r =
      1 / a - neutralIV074Rational (2 * a) r := by
  rw [neutralIV071GammaGain_rationalResolvent a r ha]
  unfold neutralIV074Rational
  have hden : (2 * a) ^ 2 + r ^ 2 = 4 * a ^ 2 + r ^ 2 := by ring
  rw [hden]
  ring

/-- The original Lorentzian at α=2a is nonnegative and bounded by 1/a.
Only the rational weight, not the arbitrary mixed correlation, is
subject to this bound. -/
theorem neutralIV077Rational_bound
    (a r : ℝ) (ha : 0 < a) :
    0 ≤ neutralIV074Rational (2 * a) r ∧
      neutralIV074Rational (2 * a) r ≤ 1 / a := by
  unfold neutralIV074Rational
  have hd : 0 < (2 * a) ^ 2 + r ^ 2 := by positivity
  constructor
  · exact div_nonneg (by positivity) hd.le
  · apply (div_le_iff₀ hd).2
    calc
      2 * (2 * a) ≤ ((2 * a) ^ 2 + r ^ 2) / a :=
        (le_div_iff₀ ha).2 (by nlinarith [sq_nonneg r])
      _ = (1 / a) * ((2 * a) ^ 2 + r ^ 2) := by ring

/-- In the literal source paper convention, the Fourier transform
times the actual Lorentzian is L¹; the available Fourier-L¹ premise
is the one already required for pointwise source inversion. -/
theorem neutralIV077PaperFT_rational_integrable
    (a : ℝ) (ha : 0 < a)
    (h : ℝ → ℂ) (hF : Integrable (𝓕 h)) :
    Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) *
        (neutralIV074Rational (2 * a) r : ℂ)) := by
  have hpaper := neutralIV077PaperFT_integrable h hF
  have hcontinuous_real :
      Continuous (fun r : ℝ => neutralIV074Rational (2 * a) r) := by
    unfold neutralIV074Rational
    apply Continuous.div₀
    · fun_prop
    · fun_prop
    · intro r
      have hd : 0 < (2 * a) ^ 2 + r ^ 2 := by positivity
      exact ne_of_gt hd
  have hweight : AEStronglyMeasurable
      (fun r : ℝ => (neutralIV074Rational (2 * a) r : ℂ)) volume :=
    (Complex.continuous_ofReal.comp hcontinuous_real).aestronglyMeasurable
  apply hpaper.mul_bdd hweight
  filter_upwards [] with r
  have hb := neutralIV077Rational_bound a r ha
  simpa [Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg hb.1] using hb.2

/-- First genuine mixed physical NF599 Gamma gain, with the *source*
definition neutralNF599Gain and source literal Zeta23.paperFT.
This is still one finite gain, not the infinite Gamma symbol. -/
theorem neutralIV077NF599Gain_pairing
    (a : ℝ) (ha : 0 < a)
    (h : ℝ → ℂ) (hc : Continuous h)
    (hh : Integrable h) (hF : Integrable (𝓕 h)) :
    (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
        (neutralNF599Gain a r : ℂ)) =
      h 0 / (a : ℂ) -
        ∫ u : ℝ, h u * neutralIV074Kernel (2 * a) u := by
  have hp : Integrable (fun r : ℝ => Zeta23.paperFT h (r : ℂ)) :=
    neutralIV077PaperFT_integrable h hF
  have hr : Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) *
        (neutralIV074Rational (2 * a) r : ℂ)) :=
    neutralIV077PaperFT_rational_integrable a ha h hF
  have hconst : Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) * ((1 / a : ℝ) : ℂ)) := hp.mul_const _
  have hinv := neutralIV077PaperFT_inversion_zero h hc hh hF
  have hpair := neutralIV076L1_pairing_positive (2 * a) (by linarith) h hh
  calc
    _ = (1 / (2 * Real.pi) : ℂ) *
          (∫ r : ℝ,
            Zeta23.paperFT h (r : ℂ) * ((1 / a : ℝ) : ℂ) -
            Zeta23.paperFT h (r : ℂ) *
              (neutralIV074Rational (2 * a) r : ℂ)) := by
      congr 1
      apply integral_congr_ae
      filter_upwards [] with r
      rw [neutralIV077NF599Gain_eq_rational a r ha]
      push_cast
      ring
    _ = (1 / (2 * Real.pi) : ℂ) *
          ((∫ r : ℝ, Zeta23.paperFT h (r : ℂ) * ((1 / a : ℝ) : ℂ)) -
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              (neutralIV074Rational (2 * a) r : ℂ))) := by
      rw [integral_sub hconst hr]
    _ = ((1 / (2 * Real.pi) : ℂ) *
          (∫ r : ℝ, Zeta23.paperFT h (r : ℂ))) * ((1 / a : ℝ) : ℂ) -
            (1 / (2 * Real.pi) : ℂ) *
              (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
                (neutralIV074Rational (2 * a) r : ℂ)) := by
      rw [integral_mul_const]
      ring
    _ = h 0 * ((1 / a : ℝ) : ℂ) -
          ∫ u : ℝ, h u * neutralIV074Kernel (2 * a) u := by
      rw [hinv, hpair]
    _ = h 0 / (a : ℂ) -
          ∫ u : ℝ, h u * neutralIV074Kernel (2 * a) u := by
      push_cast
      ring

#print axioms neutralIV077PaperFT_integrable
#print axioms neutralIV077PaperFT_inversion_zero
#print axioms neutralIV077NF599Gain_eq_rational
#print axioms neutralIV077Rational_bound
#print axioms neutralIV077PaperFT_rational_integrable
#print axioms neutralIV077NF599Gain_pairing

end
end WeilDefect
