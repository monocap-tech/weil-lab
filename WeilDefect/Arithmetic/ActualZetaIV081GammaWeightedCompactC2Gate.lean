import WeilDefect.Arithmetic.ActualZetaIV077FiniteGammaPairingGate
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_WeilEF_gammaR_bracket
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_WeilEF_integrable_mul_logDeriv_GammaR_of_decay
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_WeilEF_norm_paperFT_le_uniform
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_WeilEF_differentiable_paperFT
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_norm_paperFT_mul_sq_le
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Complex
open scoped FourierTransform

/-!
IV081 — original Zeta23 gammaBracket's *weighted Fourier L¹*, based
DIRECTLY on existing original-source certified Zeta23.WeilEF GammaR
bracket, log-growth integrability, and compact C² paperFT decay.

This is the missing explicit weight from the conditional IV079
Gamma dominated convergence result. Deliberately branched from fully
certified IV077 (46 named kernel receipts), independent of IV078/079
draft CI. Does NOT assert Fourier-L¹ from compact C²; the source
Mathlib Fourier L¹ assumption remains explicit.

No source replacement, any signed prime/pole original Weil claim,
positivity, or RH. Frozen Phase IV SHA:
165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- The precise original gammaBracket equals the original proved
Gamma_R logarithmic-derivative pair on the critical line. -/
theorem neutralIV081GammaBracket_eq_GammaR (r : ℝ) :
    (Zeta23.EF.gammaBracket r : ℂ) =
      logDeriv Complex.Gammaℝ ((1 / 2 : ℂ) + (r : ℂ) * Complex.I) +
      logDeriv Complex.Gammaℝ ((1 / 2 : ℂ) - (r : ℂ) * Complex.I) := by
  have harg : (1 / 4 : ℂ) + Complex.I * (r : ℂ) / 2 =
      (1 / 4 : ℂ) + (r : ℂ) / 2 * Complex.I := by ring
  simpa only [Zeta23.EF.gammaBracket, harg] using
    (Zeta23.WeilEF.gammaR_bracket r).symm

/-- Original source: positive Gamma_R shift is integrable against
any continuous O(1/(1+r²)) test Fourier profile. -/
theorem neutralIV081GammaPlus_integrable
    (φ : ℝ → ℂ) (hφc : Continuous φ) {C : ℝ}
    (hC : 0 ≤ C) (hbound : ∀ r, ‖φ r‖ ≤ C / (1 + r ^ 2)) :
    Integrable (fun r : ℝ => φ r *
      logDeriv Complex.Gammaℝ ((1 / 2 : ℂ) + (r : ℂ) * Complex.I)) := by
  simpa using
    (Zeta23.WeilEF.integrable_mul_logDeriv_GammaR_of_decay
      hφc hC hbound (by norm_num : (1 / 2 : ℝ) ≤ 1 / 2)
        (by norm_num : (1 / 2 : ℝ) ≤ 3 / 2))

/-- Negative-frequency original Gamma_R shift, by an *exact*
real-line change r→-r, without any evenness assumption on φ. -/
theorem neutralIV081GammaMinus_integrable
    (φ : ℝ → ℂ) (hφc : Continuous φ) {C : ℝ}
    (hC : 0 ≤ C) (hbound : ∀ r, ‖φ r‖ ≤ C / (1 + r ^ 2)) :
    Integrable (fun r : ℝ => φ r *
      logDeriv Complex.Gammaℝ ((1 / 2 : ℂ) - (r : ℂ) * Complex.I)) := by
  have hnegc : Continuous (fun t : ℝ => φ (-t)) :=
    hφc.comp continuous_neg
  have hnegb : ∀ t : ℝ, ‖φ (-t)‖ ≤ C / (1 + t ^ 2) := by
    intro t
    simpa only [neg_sq] using hbound (-t)
  have hraw : Integrable (fun t : ℝ => φ (-t) *
      logDeriv Complex.Gammaℝ ((1 / 2 : ℂ) + (t : ℂ) * Complex.I)) :=
    neutralIV081GammaPlus_integrable (fun t : ℝ => φ (-t)) hnegc hC hnegb
  have hcomp := hraw.comp_mul_left' (show (-1 : ℝ) ≠ 0 by norm_num)
  convert hcomp using 1
  funext r
  simp only [neg_one_mul, neg_neg]
  congr 1
  ring

/-- Genuine original source gammaBracket paired with the Fourier
profile is integrable. Both signed Gamma_R components are controlled
by the existing *proved* original-source log-growth theorem. -/
theorem neutralIV081GammaProduct_integrable
    (φ : ℝ → ℂ) (hφc : Continuous φ) {C : ℝ}
    (hC : 0 ≤ C) (hbound : ∀ r, ‖φ r‖ ≤ C / (1 + r ^ 2)) :
    Integrable (fun r : ℝ =>
      φ r * (Zeta23.EF.gammaBracket r : ℂ)) := by
  have hp := neutralIV081GammaPlus_integrable φ hφc hC hbound
  have hm := neutralIV081GammaMinus_integrable φ hφc hC hbound
  convert hp.add hm using 1
  funext r
  simp only [Pi.add_apply]
  rw [neutralIV081GammaBracket_eq_GammaR]
  ring

/-- Exact source weighted Gamma domination envelope from IV079,
repeated literally here to permit an independent IV077-based native
verification of the missing weighted-integrability gate. -/
def neutralIV081GammaEnvelope (φ : ℝ → ℂ) (r : ℝ) : ℝ :=
  ‖φ r‖ *
    (|Zeta23.EF.gammaBracket 0| + |Zeta23.EF.gammaBracket r|)

/-- The formerly assumed Gamma weighted L¹ is a theorem once the
Fourier profile has ordinary L¹, continuity and original C²-type
O(1/(1+r²)) decay. -/
theorem neutralIV081GammaEnvelope_integrable_of_decay
    (φ : ℝ → ℂ) (hφc : Continuous φ)
    (hφ : Integrable φ) {C : ℝ}
    (hC : 0 ≤ C) (hbound : ∀ r, ‖φ r‖ ≤ C / (1 + r ^ 2)) :
    Integrable (neutralIV081GammaEnvelope φ) := by
  have hprod := neutralIV081GammaProduct_integrable φ hφc hC hbound
  have hgammanorm : Integrable
      (fun r : ℝ => ‖φ r‖ * |Zeta23.EF.gammaBracket r|) := by
    convert hprod.norm using 1
    funext r
    simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs]
  have hconst : Integrable
      (fun r : ℝ => ‖φ r‖ * |Zeta23.EF.gammaBracket 0|) :=
    hφ.norm.mul_const _
  convert hconst.add hgammanorm using 1
  funext r
  unfold neutralIV081GammaEnvelope
  ring

/-- Original compact C² test with *literal* paperFT and actual
gammaBracket: this discharges precisely IV079's missing weighted-L¹
condition, given the ordinary Fourier-L¹ needed for source inversion.
Uses the already proved Zeta23 WeilEF Fourier decay, not a new bound. -/
theorem neutralIV081GammaEnvelope_integrable_compactC2
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {Lam : ℝ} (hLam : 0 ≤ Lam)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam)
    (hF : Integrable (𝓕 k)) :
    Integrable (neutralIV081GammaEnvelope
      (fun r : ℝ => Zeta23.paperFT k (r : ℂ))) := by
  have hkc : HasCompactSupport k :=
    Zeta23.hasCompactSupport_of_support_subset_abs hsupp
  have hki : Integrable k :=
    hk.continuous.integrable_of_hasCompactSupport hkc
  have hcont : Continuous
      (fun r : ℝ => Zeta23.paperFT k (r : ℂ)) :=
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
  exact neutralIV081GammaEnvelope_integrable_of_decay
    (fun r : ℝ => Zeta23.paperFT k (r : ℂ))
      hcont (neutralIV077PaperFT_integrable k hF) hC0 hdecay

#print axioms neutralIV081GammaBracket_eq_GammaR
#print axioms neutralIV081GammaPlus_integrable
#print axioms neutralIV081GammaMinus_integrable
#print axioms neutralIV081GammaProduct_integrable
#print axioms neutralIV081GammaEnvelope_integrable_of_decay
#print axioms neutralIV081GammaEnvelope_integrable_compactC2

end
end WeilDefect
