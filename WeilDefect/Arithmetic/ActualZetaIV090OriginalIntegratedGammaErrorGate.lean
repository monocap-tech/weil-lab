import WeilDefect.Arithmetic.ActualZetaIV089OriginalGammaQuadraticTailGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped FourierTransform

/-! IV090: exact integrated original Gamma error, conditional on the
second absolute paper-convention Fourier moment. The moment is not
inferred from compact C² regularity alone. -/

def neutralIV090MomentProfile (k : ℝ → ℂ) (r : ℝ) : ℝ :=
  r^2 * ‖Zeta23.paperFT k (r : ℂ)‖

def neutralIV090GammaErrorIntegrand (N : ℕ) (k : ℝ → ℂ) (r : ℝ) : ℂ :=
  Zeta23.paperFT k (r : ℂ) *
    ((Zeta23.EF.gammaBracket r - neutralIV071GammaFinite N r : ℝ) : ℂ)

/-- Explicit pointwise absolute integrand bound on the literal source. -/
theorem neutralIV090ErrorIntegrand_bound (N : ℕ) (k : ℝ → ℂ) (r : ℝ) :
    ‖neutralIV090GammaErrorIntegrand N k r‖ ≤
      (1 / ((N : ℝ) + 1)^2) * neutralIV090MomentProfile k r := by
  obtain ⟨h0,h1⟩ := neutralIV089GammaRemainder_bound N r
  unfold neutralIV090GammaErrorIntegrand neutralIV090MomentProfile
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg h0]
  calc
    _ ≤ ‖Zeta23.paperFT k (r : ℂ)‖ * neutralIV089TailEnvelope N r :=
      mul_le_mul_of_nonneg_left h1 (norm_nonneg _)
    _ = _ := by
      unfold neutralIV089TailEnvelope
      ring

/-- Integrability of the original infinite Gamma spectral product,
using exactly the source decay theorem and source log-growth result. -/
theorem neutralIV090GammaProduct_integrable_compactC2
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {L : ℝ} (hL : 0 ≤ L)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L) :
    Integrable (fun r : ℝ => Zeta23.paperFT k (r : ℂ) *
      (Zeta23.EF.gammaBracket r : ℂ)) := by
  have hkc : HasCompactSupport k :=
    Zeta23.hasCompactSupport_of_support_subset_abs hsupp
  have hki : Integrable k :=
    hk.continuous.integrable_of_hasCompactSupport hkc
  have hc : Continuous (fun r : ℝ => Zeta23.paperFT k (r : ℂ)) :=
    (Zeta23.WeilEF.differentiable_paperFT hk.continuous hkc).continuous.comp
      Complex.continuous_ofReal
  let C : ℝ := 2 * Real.exp L *
    ((∫ u : ℝ, ‖k u‖) + (∫ u : ℝ, ‖deriv (deriv k) u‖))
  have hC : 0 ≤ C := by
    have h1 : 0 ≤ ∫ u : ℝ, ‖k u‖ :=
      integral_nonneg (fun u => norm_nonneg (k u))
    have h2 : 0 ≤ ∫ u : ℝ, ‖deriv (deriv k) u‖ :=
      integral_nonneg (fun u => norm_nonneg (deriv (deriv k) u))
    dsimp [C]
    positivity
  have hb (r : ℝ) : ‖Zeta23.paperFT k (r : ℂ)‖ ≤ C/(1+r^2) := by
    simpa only [C, Complex.ofReal_im, abs_zero, Complex.ofReal_re] using
      (Zeta23.WeilEF.norm_paperFT_le_uniform hk hki hL hsupp
        (z := (r : ℂ)) (by simp))
  exact neutralIV081GammaProduct_integrable _ hc hC hb

/-- Exact cancellation of both pole terms and the entire arithmetic
sum at a sufficient fixed cutoff. Only the original Gamma error remains. -/
theorem neutralIV090WeilError_eq_integral
    (M N : ℕ) (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {L : ℝ} (hL : 0 ≤ L)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L)
    (hM : Real.exp L < (M : ℝ)) :
    Zeta23.EF.literatureRHS k - neutralIV086PhysicalWeilFinite M N k =
      (1 / (2 * Real.pi) : ℂ) *
        (∫ r : ℝ, neutralIV090GammaErrorIntegrand N k r) := by
  have hi := neutralIV090GammaProduct_integrable_compactC2 k hk hL hsupp
  have hf := neutralIV078Finite_spectral_integrable N k
    (neutralIV082Fourier_integrable_compactC2 k hk hL hsupp)
  have he : (∫ r : ℝ, neutralIV090GammaErrorIntegrand N k r) =
      (∫ r : ℝ, Zeta23.paperFT k (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ)) -
      (∫ r : ℝ, Zeta23.paperFT k (r : ℂ) *
        (neutralIV071GammaFinite N r : ℂ)) := by
    rw [← integral_sub hi hf]
    apply integral_congr_ae
    filter_upwards [] with r
    simp only [neutralIV090GammaErrorIntegrand, Complex.ofReal_sub, Pi.sub_apply]
    ring
  rw [neutralIV085LiteratureRHS_finitePrime k hsupp M hM,
    neutralIV086PhysicalWeilFinite_eq_spectral M N k hk hL hsupp, he]
  ring

/-- Effective original signed Weil truncation error. All source
terms other than Gamma cancel exactly. No positivity is asserted. -/
theorem neutralIV090WeilError_bound
    (M N : ℕ) (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {L : ℝ} (hL : 0 ≤ L)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L)
    (hM : Real.exp L < (M : ℝ))
    (hmom : Integrable (neutralIV090MomentProfile k)) :
    ‖Zeta23.EF.literatureRHS k - neutralIV086PhysicalWeilFinite M N k‖ ≤
      (1 / (2 * Real.pi)) *
        ((1 / ((N : ℝ) + 1)^2) *
          ∫ r : ℝ, neutralIV090MomentProfile k r) := by
  have hi := neutralIV090GammaProduct_integrable_compactC2 k hk hL hsupp
  have hf := neutralIV078Finite_spectral_integrable N k
    (neutralIV082Fourier_integrable_compactC2 k hk hL hsupp)
  have he : Integrable (neutralIV090GammaErrorIntegrand N k) := by
    apply (hi.sub hf).congr
    filter_upwards [] with r
    simp only [neutralIV090GammaErrorIntegrand, Complex.ofReal_sub, Pi.sub_apply]
    ring
  have hmaj := hmom.const_mul (1 / ((N : ℝ) + 1)^2)
  have hb : ‖∫ r : ℝ, neutralIV090GammaErrorIntegrand N k r‖ ≤
      (1 / ((N : ℝ) + 1)^2) * ∫ r : ℝ, neutralIV090MomentProfile k r := by
    calc
      _ ≤ ∫ r : ℝ, ‖neutralIV090GammaErrorIntegrand N k r‖ :=
        norm_integral_le_integral_norm _
      _ ≤ ∫ r : ℝ, (1 / ((N : ℝ) + 1)^2) *
          neutralIV090MomentProfile k r :=
        integral_mono he.norm hmaj (neutralIV090ErrorIntegrand_bound N k)
      _ = _ := integral_const_mul _ _
  rw [neutralIV090WeilError_eq_integral M N k hk hL hsupp hM, norm_mul]
  have hc : ‖(1 / (2 * Real.pi) : ℂ)‖ = (1 / (2 * Real.pi) : ℝ) := by
    have hcast : ((1 / (2 * Real.pi) : ℝ) : ℂ) =
        (1 / (2 * Real.pi) : ℂ) := by push_cast <;> rfl
    rw [← hcast, Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (by positivity)]
  rw [hc]
  exact mul_le_mul_of_nonneg_left hb (by positivity)

#print axioms neutralIV090ErrorIntegrand_bound
#print axioms neutralIV090GammaProduct_integrable_compactC2
#print axioms neutralIV090WeilError_eq_integral
#print axioms neutralIV090WeilError_bound

end
end WeilDefect
