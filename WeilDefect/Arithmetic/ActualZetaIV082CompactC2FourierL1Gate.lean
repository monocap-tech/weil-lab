import WeilDefect.Arithmetic.ActualZetaIV081GammaWeightedCompactC2Gate
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Complex
open scoped FourierTransform

/-!
IV082 — discharge the ORDINARY Fourier-L¹ premise for the actual
Zeta23 EF compact-C² test class, without assuming Fourier L¹.

Uses original-source Zeta23.WeilEF.norm_paperFT_le_uniform and
differentiable_paperFT, plus the Mathlib proved integrable
(1+r²)⁻¹. The final source-weighted theorem is dependent on the
uncertified IV081 compact-C² Gamma-weighted theorem.

This module does NOT assert any infinite Gamma spectral/physical
interchange, positivity, prime/pole identity or RH.

Frozen Phase IV source SHA:
165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- Authentic paper-convention transform is ordinary L¹ for each
original C_c² physical test, without an L¹ Fourier hypothesis. -/
theorem neutralIV082PaperFT_integrable_compactC2
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {Lam : ℝ} (hLam : 0 ≤ Lam)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    Integrable (fun r : ℝ => Zeta23.paperFT k (r : ℂ)) := by
  have hkc : HasCompactSupport k :=
    Zeta23.hasCompactSupport_of_support_subset_abs hsupp
  have hki : Integrable k :=
    hk.continuous.integrable_of_hasCompactSupport hkc
  have hcont : Continuous (fun r : ℝ =>
      Zeta23.paperFT k (r : ℂ)) :=
    (Zeta23.WeilEF.differentiable_paperFT hk.continuous hkc).continuous.comp
      Complex.continuous_ofReal
  let C : ℝ :=
    2 * Real.exp Lam *
      ((∫ u : ℝ, ‖k u‖) +
       (∫ u : ℝ, ‖deriv (deriv k) u‖))
  have hC0 : 0 ≤ C := by
    have h1 : 0 ≤ ∫ u : ℝ, ‖k u‖ :=
      integral_nonneg (fun u => norm_nonneg (k u))
    have h2 : 0 ≤ ∫ u : ℝ, ‖deriv (deriv k) u‖ :=
      integral_nonneg (fun u => norm_nonneg (deriv (deriv k) u))
    dsimp [C]
    positivity
  have hdecay (r : ℝ) :
      ‖Zeta23.paperFT k (r : ℂ)‖ ≤ C / (1 + r ^ 2) := by
    simpa only [C, Complex.ofReal_im, abs_zero, Complex.ofReal_re]
      using (Zeta23.WeilEF.norm_paperFT_le_uniform hk hki hLam hsupp
        (z := (r : ℂ)) (by simp))
  have hmaj : Integrable (fun r : ℝ =>
      C * ((1 + r ^ 2 : ℝ)⁻¹)) :=
    (integrable_inv_one_add_sq).const_mul C
  apply Integrable.mono' hmaj hcont.aestronglyMeasurable
  filter_upwards [] with r
  have hb := hdecay r
  simpa only [div_eq_mul_inv] using hb

/-- Genuine Mathlib Fourier L¹ recovered from the source paperFT by
the exact original Fourier dictionary, with nonzero -2π dilation. -/
theorem neutralIV082Fourier_integrable_compactC2
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {Lam : ℝ} (hLam : 0 ≤ Lam)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    Integrable (𝓕 k) := by
  have hpaper :=
    neutralIV082PaperFT_integrable_compactC2 k hk hLam hsupp
  have hnonzero : (-(2 * Real.pi) : ℝ) ≠ 0 := by
    exact neg_ne_zero.mpr (mul_ne_zero (by norm_num) Real.pi_ne_zero)
  have hcomp : Integrable (fun w : ℝ =>
      Zeta23.paperFT k (((-(2 * Real.pi)) * w : ℝ) : ℂ)) :=
    hpaper.comp_mul_left' hnonzero
  convert hcomp using 1
  funext w
  rw [Zeta23.EF.paperFT_ofReal_eq_fourier_Zeta23_EF_paper_inversion]
  congr 1
  field_simp

/-- No auxiliary weighted-L¹ or Fourier-L¹ premise survives for the
authentic compact-C² original EF test. This attaches independent
IV082 Fourier L¹ to source-reusing IV081 Gamma integrability.
Entirely source literal: paperFT and gammaBracket are unchanged. -/
theorem neutralIV082GammaEnvelope_integrable_compactC2
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {Lam : ℝ} (hLam : 0 ≤ Lam)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    Integrable (neutralIV081GammaEnvelope
      (fun r : ℝ => Zeta23.paperFT k (r : ℂ))) := by
  exact neutralIV081GammaEnvelope_integrable_compactC2
    k hk hLam hsupp
      (neutralIV082Fourier_integrable_compactC2 k hk hLam hsupp)

#print axioms neutralIV082PaperFT_integrable_compactC2
#print axioms neutralIV082Fourier_integrable_compactC2
#print axioms neutralIV082GammaEnvelope_integrable_compactC2

end
end WeilDefect
