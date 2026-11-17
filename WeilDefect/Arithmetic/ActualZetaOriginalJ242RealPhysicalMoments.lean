import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramPhysicalIntegral
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-- Reality of the actual full-window zero-extended source. Independent
of all pending inverse, parity and analytic independence proofs. -/
theorem neutralNF572OriginalWindowGenerator_conj
    (i : Fin 242) (x : ℝ) :
    conj (neutralNF546OriginalWindowGenerator i x) =
      neutralNF546OriginalWindowGenerator i x := by
  by_cases hx : x ∈ neutralNF546OriginalFullPhysicalWindow
  · simp [neutralNF546OriginalWindowGenerator, Set.indicator_of_mem hx,
      neutralNF546OriginalComplexGenerator]
  · simp [neutralNF546OriginalWindowGenerator, Set.indicator_of_notMem hx]

/-- Extend the exact NF549 Schwartz moment integral to the
genuine arbitrary physical L² target. This is an a.e. L²
identity, not a pointwise equality of equivalence classes. -/
theorem neutralNF572OriginalMoment_eq_physicalIntegral
    (ell : RealComplexL2) (i : Fin 242) :
    neutralNF546OriginalSelectedMoments ell i =
      ∫ x : ℝ, conj (neutralNF546OriginalWindowGenerator i x) *
        ell x ∂volume := by
  change inner ℂ (neutralNF546OriginalSelectedPhysicalL2 i) ell = _
  rw [MeasureTheory.L2.inner_def]
  apply integral_congr_ae
  filter_upwards [neutralNF546OriginalSelectedPhysicalL2_ae i] with x hi
  simp only [hi, RCLike.inner_apply, mul_comm]

/-- Actual real physical L² targets have real original J242
moments. The source window and its original sinh generator
remain unchanged. -/
theorem neutralNF572OriginalRealPhysicalMoments
    (ell : RealComplexL2)
    (hell : ∀ᵐ x ∂volume, conj (ell x) = ell x)
    (i : Fin 242) :
    conj (neutralNF546OriginalSelectedMoments ell i) =
      neutralNF546OriginalSelectedMoments ell i := by
  rw [neutralNF572OriginalMoment_eq_physicalIntegral, ← integral_conj]
  apply integral_congr_ae
  filter_upwards [hell] with x hx
  simp only [map_mul, neutralNF572OriginalWindowGenerator_conj, hx]

/-- Pointwise reality of a smooth test gives real moments,
using its actual a.e. physical representative. -/
theorem neutralNF572OriginalRealSchwartzMoments
    (g : 𝓢(ℝ, ℂ)) (hg : ∀ x : ℝ, conj (g x) = g x)
    (i : Fin 242) :
    conj (neutralNF546OriginalSelectedMoments (g.toLp 2 volume) i) =
      neutralNF546OriginalSelectedMoments (g.toLp 2 volume) i := by
  apply neutralNF572OriginalRealPhysicalMoments
  filter_upwards [g.coeFn_toLp 2 volume] with x hx
  rw [hx, hg x]

/-- The literal NF543 target-minus-test moment defect is real.
This does not require a Gram inverse. -/
theorem neutralNF572OriginalMomentDefect_real
    (ell : RealComplexL2)
    (hell : ∀ᵐ x ∂volume, conj (ell x) = ell x)
    (g : 𝓢(ℝ, ℂ)) (hg : ∀ x : ℝ, conj (g x) = g x)
    (i : Fin 242) :
    conj ((neutralNF546OriginalSelectedMoments ell -
      neutralNF546OriginalSelectedMoments (g.toLp 2 volume)) i) =
    (neutralNF546OriginalSelectedMoments ell -
      neutralNF546OriginalSelectedMoments (g.toLp 2 volume)) i := by
  simp only [Pi.sub_apply, map_sub,
    neutralNF572OriginalRealPhysicalMoments ell hell i,
    neutralNF572OriginalRealSchwartzMoments g hg i]

end
end WeilDefect
