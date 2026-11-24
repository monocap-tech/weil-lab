import WeilDefect.Arithmetic.ActualZetaIV078FiniteGammaTruncationGate
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped FourierTransform Topology

/-!
IV079 — literal original finite NF599 Gamma to original infinite
gammaBracket spectral integral under EXACT WEIGHTED SOURCE domination.

The gamma symbols here are the unmodified actual Zeta23.EF.gammaBracket
and source-defined neutralIV071GammaFinite. The weighted L¹ premise
is EXPLICIT, not asserted or inferred from ordinary Fourier L¹.
The missing theorem remains verifying that premise for original
compact C² mixed correlations.

Upstream IV077 / IV078 must pass full native strict CI before this
dependent candidate can count. Frozen original source:
165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- The true original finite source Gamma symbol is never below the
literal value gammaBracket 0. Every genuine NF599 gain is nonnegative. -/
theorem neutralIV079GammaFinite_lower
    (N : ℕ) (r : ℝ) :
    Zeta23.EF.gammaBracket 0 ≤ neutralIV071GammaFinite N r := by
  have hfirst : 0 ≤ neutralNF599Gain (1 / 4) r :=
    neutralNF599Gain_nonneg _ _ (by norm_num)
  have htail : 0 ≤ ∑ n ∈ Finset.range N,
      neutralNF599Gain ((n : ℝ) + 1 + 1 / 4) r :=
    Finset.sum_nonneg (fun n _ =>
      neutralNF599Gain_nonneg _ _ (by positivity))
  unfold neutralIV071GammaFinite
  linarith

/-- Pointwise N-uniform absolute envelope from two *certified source*
inequalities, without introducing a substitute Gamma multiplier. -/
theorem neutralIV079GammaFinite_abs_le
    (N : ℕ) (r : ℝ) :
    |neutralIV071GammaFinite N r| ≤
      |Zeta23.EF.gammaBracket 0| + |Zeta23.EF.gammaBracket r| := by
  have hlow := neutralIV079GammaFinite_lower N r
  have hhigh := neutralIV071GammaFinite_le N r
  have h0 := neg_abs_le (Zeta23.EF.gammaBracket 0)
  have hr := le_abs_self (Zeta23.EF.gammaBracket r)
  have h00 := abs_nonneg (Zeta23.EF.gammaBracket 0)
  have hrr := abs_nonneg (Zeta23.EF.gammaBracket r)
  apply abs_le.mpr
  constructor <;> linarith

/-- The exact integrable source envelope; its integrability is an
explicit theorem hypothesis and is NOT derived from bare Fourier L¹. -/
def neutralIV079GammaEnvelope (h : ℝ → ℂ) (r : ℝ) : ℝ :=
  ‖Zeta23.paperFT h (r : ℂ)‖ *
    (|Zeta23.EF.gammaBracket 0| + |Zeta23.EF.gammaBracket r|)

/-- Source gamma finite truncations multiplied by the original paperFT
are bounded uniformly in the truncation index by the same source
envelope, with no symmetry requirement on h. -/
theorem neutralIV079Finite_integrand_bound
    (N : ℕ) (h : ℝ → ℂ) (r : ℝ) :
    ‖Zeta23.paperFT h (r : ℂ) *
        (neutralIV071GammaFinite N r : ℂ)‖ ≤
      neutralIV079GammaEnvelope h r := by
  have hGamma := neutralIV079GammaFinite_abs_le N r
  simpa only [neutralIV079GammaEnvelope, norm_mul, Complex.norm_real,
    Real.norm_eq_abs] using
      mul_le_mul_of_nonneg_left hGamma
        (norm_nonneg (Zeta23.paperFT h (r : ℂ)))

/-- The actual gamma finite truncation integrand converges pointwise
to the literal original infinite Gamma symbol's integrand.
This is only pointwise; IV079GammaIntegral_tendsto performs DCT. -/
theorem neutralIV079Finite_integrand_tendsto
    (h : ℝ → ℂ) (r : ℝ) :
    Tendsto (fun N : ℕ =>
      Zeta23.paperFT h (r : ℂ) *
        (neutralIV071GammaFinite N r : ℂ))
      atTop
      (𝓝 (Zeta23.paperFT h (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ))) := by
  have hreal := neutralIV071GammaFinite_tendsto r
  have hcomplex :
      Tendsto (fun N : ℕ => (neutralIV071GammaFinite N r : ℂ))
        atTop (𝓝 (Zeta23.EF.gammaBracket r : ℂ)) :=
    (Complex.continuous_ofReal.tendsto _).comp hreal
  exact hcomplex.const_mul _

/-- Conditional genuine source infinite Gamma integral exchange:
dominated convergence is valid once the EXACT source-weighted
Fourier L¹ envelope is integrable. Nothing about the original compact
C² test class has been assumed here. -/
theorem neutralIV079GammaIntegral_tendsto
    (h : ℝ → ℂ)
    (hF : Integrable (𝓕 h))
    (hweighted : Integrable (neutralIV079GammaEnvelope h)) :
    Tendsto (fun N : ℕ =>
      ∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
        (neutralIV071GammaFinite N r : ℂ))
      atTop
      (𝓝 (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
        (Zeta23.EF.gammaBracket r : ℂ))) := by
  exact tendsto_integral_of_dominated_convergence
    (neutralIV079GammaEnvelope h)
    (fun N => (neutralIV078Finite_spectral_integrable N h hF).aestronglyMeasurable)
    hweighted
    (fun N => ae_of_all _ (fun r => neutralIV079Finite_integrand_bound N h r))
    (ae_of_all _ (fun r => neutralIV079Finite_integrand_tendsto h r))

/-- Under explicit source-weighted Fourier L¹, the ACTUAL IV078
finite physical Gamma expressions converge to the literal original
infinite Gamma spectral integral. The source-gamma weighted hypothesis
must be discharged independently for the original test class. -/
theorem neutralIV079FiniteSpatial_tendsto
    (h : ℝ → ℂ) (hc : Continuous h)
    (hh : Integrable h) (hF : Integrable (𝓕 h))
    (hweighted : Integrable (neutralIV079GammaEnvelope h)) :
    Tendsto (fun N : ℕ => neutralIV078FiniteSpatial N h)
      atTop
      (𝓝 ((1 / (2 * Real.pi) : ℂ) *
        (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
          (Zeta23.EF.gammaBracket r : ℂ)))) := by
  have hlim := (neutralIV079GammaIntegral_tendsto h hF hweighted).const_mul
    (1 / (2 * Real.pi) : ℂ)
  have heq (N : ℕ) :
      neutralIV078FiniteSpatial N h =
        (1 / (2 * Real.pi) : ℂ) *
          (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
            (neutralIV071GammaFinite N r : ℂ)) :=
    (neutralIV078FiniteGamma_pairing N h hc hh hF).symm
  convert hlim using 1
  funext N
  exact heq N

#print axioms neutralIV079GammaFinite_lower
#print axioms neutralIV079GammaFinite_abs_le
#print axioms neutralIV079Finite_integrand_bound
#print axioms neutralIV079Finite_integrand_tendsto
#print axioms neutralIV079GammaIntegral_tendsto
#print axioms neutralIV079FiniteSpatial_tendsto

end
end WeilDefect
