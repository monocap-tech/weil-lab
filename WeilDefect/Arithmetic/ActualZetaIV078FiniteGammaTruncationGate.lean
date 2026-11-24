import WeilDefect.Arithmetic.ActualZetaIV077FiniteGammaPairingGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped FourierTransform

/-!
IV078 — exact original finite Gamma source truncation in physical space.

This module imports the literal IV071 finite Gamma definition:
 gammaBracket 0 + NF599Gain (1/4) + sum_{n<N} NF599Gain (n+5/4).
Its only new Fourier inputs are the IV077 original NF599
single-gain identity and the established paper inversion at zero.

All statements are genuinely finite N. No infinite Gamma limit,
complete prime/pole signed Weil identity, positivity, or RH claim.
Frozen Phase IV source: 165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- Physical contribution from one genuine NF599 gain. -/
def neutralIV078SingleSpatial (a : ℝ) (h : ℝ → ℂ) : ℂ :=
  h 0 / (a : ℂ) -
    ∫ u : ℝ, h u * neutralIV074Kernel (2 * a) u

/-- Physical expression corresponding to the literal finite original
Gamma truncation, including its authentic gammaBracket 0. -/
def neutralIV078FiniteSpatial (N : ℕ) (h : ℝ → ℂ) : ℂ :=
  (Zeta23.EF.gammaBracket 0 : ℂ) * h 0 +
    neutralIV078SingleSpatial (1 / 4) h +
    ∑ n ∈ Finset.range N,
      neutralIV078SingleSpatial ((n : ℝ) + 1 + 1 / 4) h

/-- One actual source NF599 gain is integrable against the original
paperFT under precisely Fourier L¹, using its certified resolvent split. -/
theorem neutralIV078Gain_spectral_integrable
    (a : ℝ) (ha : 0 < a) (h : ℝ → ℂ)
    (hF : Integrable (𝓕 h)) :
    Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) * (neutralNF599Gain a r : ℂ)) := by
  have hp : Integrable (fun r : ℝ => Zeta23.paperFT h (r : ℂ)) :=
    neutralIV077PaperFT_integrable h hF
  have hc : Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) * ((1 / a : ℝ) : ℂ)) := hp.mul_const _
  have hr : Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) *
        (neutralIV074Rational (2 * a) r : ℂ)) :=
    neutralIV077PaperFT_rational_integrable a ha h hF
  convert hc.sub hr using 1
  funext r
  rw [neutralIV077NF599Gain_eq_rational a r ha]
  push_cast
  simp only [Pi.sub_apply]
  ring

/-- The literal finite Gamma truncation is L¹ when weighted by the
actual original-source paperFT. The proof uses finite induction rather
than any unlicensed infinite integral/sum interchange. -/
theorem neutralIV078Finite_spectral_integrable
    (N : ℕ) (h : ℝ → ℂ) (hF : Integrable (𝓕 h)) :
    Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) *
        (neutralIV071GammaFinite N r : ℂ)) := by
  induction N with
  | zero =>
      have hp : Integrable (fun r : ℝ => Zeta23.paperFT h (r : ℂ)) :=
        neutralIV077PaperFT_integrable h hF
      have hc : Integrable (fun r : ℝ =>
          Zeta23.paperFT h (r : ℂ) *
            ((Zeta23.EF.gammaBracket 0 : ℝ) : ℂ)) := hp.mul_const _
      have hg : Integrable (fun r : ℝ =>
          Zeta23.paperFT h (r : ℂ) *
            (neutralNF599Gain (1 / 4) r : ℂ)) :=
        neutralIV078Gain_spectral_integrable (1 / 4) (by norm_num) h hF
      convert hc.add hg using 1
      funext r
      simp only [neutralIV071GammaFinite, Finset.range_zero, Finset.sum_empty, add_zero]
      push_cast
      simp only [Pi.add_apply]
      ring
  | succ N ih =>
      have ha : 0 < (N : ℝ) + 1 + 1 / 4 := by positivity
      have hg : Integrable (fun r : ℝ =>
          Zeta23.paperFT h (r : ℂ) *
            (neutralNF599Gain ((N : ℝ) + 1 + 1 / 4) r : ℂ)) :=
        neutralIV078Gain_spectral_integrable _ ha h hF
      convert ih.add hg using 1
      funext r
      rw [neutralIV071GammaFinite_succ]
      push_cast
      simp only [Pi.add_apply]
      ring

/-- The source-normalized finite physical expression has the same
one-mode-at-a-time recursion as the actual IV071 Gamma truncation. -/
theorem neutralIV078FiniteSpatial_succ
    (N : ℕ) (h : ℝ → ℂ) :
    neutralIV078FiniteSpatial (N + 1) h =
      neutralIV078FiniteSpatial N h +
        neutralIV078SingleSpatial ((N : ℝ) + 1 + 1 / 4) h := by
  simp only [neutralIV078FiniteSpatial, Finset.sum_range_succ]
  ring

/-- Original finite Gamma source, with gammaBracket 0 and its true
NF599 gains, paired exactly to physical space for each N. -/
theorem neutralIV078FiniteGamma_pairing
    (N : ℕ) (h : ℝ → ℂ) (hc : Continuous h)
    (hh : Integrable h) (hF : Integrable (𝓕 h)) :
    (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
        (neutralIV071GammaFinite N r : ℂ)) =
      neutralIV078FiniteSpatial N h := by
  induction N with
  | zero =>
      have hp : Integrable (fun r : ℝ => Zeta23.paperFT h (r : ℂ)) :=
        neutralIV077PaperFT_integrable h hF
      have hconst : Integrable (fun r : ℝ =>
          Zeta23.paperFT h (r : ℂ) *
            ((Zeta23.EF.gammaBracket 0 : ℝ) : ℂ)) := hp.mul_const _
      have hgain : Integrable (fun r : ℝ =>
          Zeta23.paperFT h (r : ℂ) *
            (neutralNF599Gain (1 / 4) r : ℂ)) :=
        neutralIV078Gain_spectral_integrable (1 / 4) (by norm_num) h hF
      have hgamma0 :
          (1 / (2 * Real.pi) : ℂ) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              ((Zeta23.EF.gammaBracket 0 : ℝ) : ℂ)) =
            (Zeta23.EF.gammaBracket 0 : ℂ) * h 0 := by
        rw [integral_mul_const]
        calc
          _ = ((1 / (2 * Real.pi) : ℂ) *
              (∫ r : ℝ, Zeta23.paperFT h (r : ℂ))) *
                (Zeta23.EF.gammaBracket 0 : ℂ) := by ring
          _ = (Zeta23.EF.gammaBracket 0 : ℂ) * h 0 := by
            rw [neutralIV077PaperFT_inversion_zero h hc hh hF]
            ring
      have hmode :
          (1 / (2 * Real.pi) : ℂ) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              (neutralNF599Gain (1 / 4) r : ℂ)) =
            neutralIV078SingleSpatial (1 / 4) h := by
        simpa only [neutralIV078SingleSpatial] using
          neutralIV077NF599Gain_pairing (1 / 4) (by norm_num) h hc hh hF
      calc
        _ = (1 / (2 * Real.pi) : ℂ) *
          (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              ((Zeta23.EF.gammaBracket 0 : ℝ) : ℂ) +
            Zeta23.paperFT h (r : ℂ) *
              (neutralNF599Gain (1 / 4) r : ℂ)) := by
            congr 1
            apply integral_congr_ae
            filter_upwards [] with r
            simp only [neutralIV071GammaFinite, Finset.range_zero,
              Finset.sum_empty, add_zero]
            push_cast
            ring
        _ = (1 / (2 * Real.pi) : ℂ) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              ((Zeta23.EF.gammaBracket 0 : ℝ) : ℂ)) +
          (1 / (2 * Real.pi) : ℂ) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              (neutralNF599Gain (1 / 4) r : ℂ)) := by
            rw [integral_add hconst hgain]
            ring
        _ = neutralIV078FiniteSpatial 0 h := by
          rw [hgamma0, hmode]
          simp [neutralIV078FiniteSpatial]
  | succ N ih =>
      let a : ℝ := (N : ℝ) + 1 + 1 / 4
      have ha : 0 < a := by dsimp [a]; positivity
      have hprev : Integrable (fun r : ℝ =>
          Zeta23.paperFT h (r : ℂ) *
            (neutralIV071GammaFinite N r : ℂ)) :=
        neutralIV078Finite_spectral_integrable N h hF
      have hgain : Integrable (fun r : ℝ =>
          Zeta23.paperFT h (r : ℂ) *
            (neutralNF599Gain a r : ℂ)) :=
        neutralIV078Gain_spectral_integrable a ha h hF
      have hmode :
          (1 / (2 * Real.pi) : ℂ) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              (neutralNF599Gain a r : ℂ)) =
            neutralIV078SingleSpatial a h := by
        simpa only [neutralIV078SingleSpatial] using
          neutralIV077NF599Gain_pairing a ha h hc hh hF
      calc
        _ = (1 / (2 * Real.pi) : ℂ) *
          (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              (neutralIV071GammaFinite N r : ℂ) +
            Zeta23.paperFT h (r : ℂ) *
              (neutralNF599Gain a r : ℂ)) := by
            congr 1
            apply integral_congr_ae
            filter_upwards [] with r
            rw [neutralIV071GammaFinite_succ]
            dsimp [a]
            push_cast
            ring
        _ = (1 / (2 * Real.pi) : ℂ) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              (neutralIV071GammaFinite N r : ℂ)) +
          (1 / (2 * Real.pi) : ℂ) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              (neutralNF599Gain a r : ℂ)) := by
            rw [integral_add hprev hgain]
            ring
        _ = neutralIV078FiniteSpatial N h + neutralIV078SingleSpatial a h := by
          rw [ih, hmode]
        _ = neutralIV078FiniteSpatial (N + 1) h := by
          dsimp [a]
          exact (neutralIV078FiniteSpatial_succ N h).symm

#print axioms neutralIV078Gain_spectral_integrable
#print axioms neutralIV078Finite_spectral_integrable
#print axioms neutralIV078FiniteSpatial_succ
#print axioms neutralIV078FiniteGamma_pairing

end
end WeilDefect
