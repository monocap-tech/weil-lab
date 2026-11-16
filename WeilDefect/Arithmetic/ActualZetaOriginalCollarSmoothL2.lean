import WeilDefect.Arithmetic.ActualZetaSmoothCorrelationRegularity
import Mathlib.MeasureTheory.Function.LpSpace.Indicator

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped ComplexConjugate

/-!
NF535: the ACTUAL physical L² class of a strict smooth collar test.
Do not infer any pointwise smoothness of an arbitrary quotient representative.
-/

/-- The unchanged original endpoint-collar geometry (B=11/10, δ=1/500).
These are the two strict original physical support collars, not a new
arithmetic source or synthesized replacement. -/
def neutralOriginalEndpointCollars : Set ℝ :=
  Set.Ioo (-(11 / 10 : ℝ)) (-(11 / 10 : ℝ) + 1 / 500) ∪
  Set.Ioo ((11 / 10 : ℝ) - 1 / 500) (11 / 10 : ℝ)

theorem neutralOriginalEndpointCollars_subset_window :
    neutralOriginalEndpointCollars ⊆
      Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ) := by
  intro x hx
  rcases hx with hx | hx
  · exact ⟨hx.1.le, by linarith [hx.2]⟩
  · exact ⟨by linarith [hx.1], hx.2.le⟩

/-- Produce the genuine physical L² class of any compact C² test supported
inside the already-defined full window. The physical representative agrees
with the test *almost everywhere*, not at every point. -/
theorem neutralSmoothWindow_toActualPhysicalL2
    (a : ℝ) (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ 2 ψ) (hc : HasCompactSupport ψ)
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → ψ x = 0) :
    ∃ g : RealComplexL2,
      neutralWindowRepresentative a g =ᵐ[volume] ψ := by
  let hmem : MemLp ψ 2 volume :=
    hψ.continuous.memLp_of_hasCompactSupport hc
  refine ⟨hmem.toLp ψ, ?_⟩
  filter_upwards [hmem.coeFn_toLp] with x hx
  by_cases hwin : x ∈ Set.Icc (-a) a
  · simpa [neutralWindowRepresentative, hwin] using hx
  · simp [neutralWindowRepresentative, hwin, hs x hwin]

/-- A literal strict test on the original NF527 endpoint collars produces
the authentic L² window input, without any Green span or arithmetic
source alteration. This exists for every such test. -/
theorem neutralOriginalCollarSmooth_toActualPhysicalL2
    (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ 2 ψ) (hc : HasCompactSupport ψ)
    (hs : ∀ x : ℝ, x ∉ neutralOriginalEndpointCollars → ψ x = 0) :
    ∃ g : RealComplexL2,
      neutralWindowRepresentative (11 / 10 : ℝ) g =ᵐ[volume] ψ := by
  apply neutralSmoothWindow_toActualPhysicalL2 (11 / 10 : ℝ) ψ hψ hc
  intro x hx
  apply hs x
  intro hE
  exact hx (neutralOriginalEndpointCollars_subset_window hE)

/-- The same genuine physical input immediately passes the actual
multiplicity-preserving zero-side formula against EVERY physical L² first
test. This uses the a.e. convolution theorem; the formula contains both
the original polar terms, all prime powers and the complete gamma bracket.
No global sign claim or RH enters. -/
theorem neutralOriginalCollarSmooth_hasAuthenticWeilEF
    (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ 2 ψ) (hc : HasCompactSupport ψ)
    (hs : ∀ x : ℝ, x ∉ neutralOriginalEndpointCollars → ψ x = 0) :
    ∃ g : RealComplexL2,
      (neutralWindowRepresentative (11 / 10 : ℝ) g =ᵐ[volume] ψ) ∧
      (∀ f : RealComplexL2,
        (∑' q : NeutralActualZetaDivisorCoordinate,
          conj (neutralWindowEvaluation (11 / 10 : ℝ)
            (conj (neutralActualZetaDivisorOrdinate q)) f) *
            neutralWindowEvaluation (11 / 10 : ℝ)
              (neutralActualZetaDivisorOrdinate q) g) =
          Zeta23.EF.literatureRHS
            (neutralWindowCorrelation (11 / 10 : ℝ) f g)) := by
  obtain ⟨g, hg⟩ := neutralOriginalCollarSmooth_toActualPhysicalL2 ψ hψ hc hs
  refine ⟨g, hg, ?_⟩
  intro f
  exact neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond
      (11 / 10 : ℝ) f g ψ hψ hc hg

end
end WeilDefect
