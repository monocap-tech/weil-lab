import WeilDefect.Arithmetic.ActualZetaIV082CompactC2FourierL1Gate
import WeilDefect.Arithmetic.ActualZetaIV079GammaDominatedLimitGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped FourierTransform Topology

/-!
IV083 — exact source-preserving compact-C² Gamma attachment.

The finite pairing is the already certified IV078 theorem. The
infinite-limit DCT theorem is the IV079 candidate and the genuine
original gammaBracket weighted L¹ is the IV081/IV082 candidate.

Dependencies are copied as byte-identical source into this branch;
no candidate dependency counts as a receipt before native compilation
and a strict direct axiom audit. No pole terms, signed prime-power
terms, positivity, Phase IV adoption, or RH are claimed.

Frozen original Phase IV source SHA:
165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- The literal original NF599 finite Gamma pairing for authentic
compact-C² tests, without separately assuming Fourier L¹. -/
theorem neutralIV083FiniteGamma_pairing_compactC2
    (N : ℕ) (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {Lam : ℝ} (hLam : 0 ≤ Lam)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    (1 / (2 * Real.pi) : ℂ) *
      (∫ r : ℝ, Zeta23.paperFT k (r : ℂ) *
        (neutralIV071GammaFinite N r : ℂ)) =
      neutralIV078FiniteSpatial N k := by
  have hkc : HasCompactSupport k :=
    Zeta23.hasCompactSupport_of_support_subset_abs hsupp
  have hki : Integrable k :=
    hk.continuous.integrable_of_hasCompactSupport hkc
  exact neutralIV078FiniteGamma_pairing N k hk.continuous hki
    (neutralIV082Fourier_integrable_compactC2 k hk hLam hsupp)

/-- The IV079 original-source DCT dominating envelope is integrable
for every original compact-C² physical test; neither ordinary
Fourier L¹ nor Gamma-weighted L¹ is an added hypothesis. -/
theorem neutralIV083GammaEnvelope_integrable_compactC2
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {Lam : ℝ} (hLam : 0 ≤ Lam)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    Integrable (neutralIV079GammaEnvelope k) := by
  change Integrable (neutralIV081GammaEnvelope
    (fun r : ℝ => Zeta23.paperFT k (r : ℂ)))
  exact neutralIV082GammaEnvelope_integrable_compactC2
    k hk hLam hsupp

/-- For original compact-C² tests, the finite physical NF599 Gamma
sums converge to the spectral integral of the literal original
Zeta23.EF.gammaBracket. All Fourier and weighted integrability
premises of IV079 are discharged by original-source theorems.
This is Gamma only, NOT the complete signed Weil form. -/
theorem neutralIV083FiniteSpatial_tendsto_compactC2
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {Lam : ℝ} (hLam : 0 ≤ Lam)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ Lam) :
    Filter.Tendsto (fun N : ℕ => neutralIV078FiniteSpatial N k)
      Filter.atTop
      (𝓝 ((1 / (2 * Real.pi) : ℂ) *
        (∫ r : ℝ, Zeta23.paperFT k (r : ℂ) *
          (Zeta23.EF.gammaBracket r : ℂ)))) := by
  have hkc : HasCompactSupport k :=
    Zeta23.hasCompactSupport_of_support_subset_abs hsupp
  have hki : Integrable k :=
    hk.continuous.integrable_of_hasCompactSupport hkc
  exact neutralIV079FiniteSpatial_tendsto k hk.continuous hki
    (neutralIV082Fourier_integrable_compactC2 k hk hLam hsupp)
    (neutralIV083GammaEnvelope_integrable_compactC2 k hk hLam hsupp)

#print axioms neutralIV083FiniteGamma_pairing_compactC2
#print axioms neutralIV083GammaEnvelope_integrable_compactC2
#print axioms neutralIV083FiniteSpatial_tendsto_compactC2

end
end WeilDefect
