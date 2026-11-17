import WeilDefect.Arithmetic.ActualZetaOriginalJ242GlobalIndependence
import WeilDefect.Arithmetic.ActualZetaOriginalJ242AnalyticIdentity

namespace WeilDefect
noncomputable section
open scoped ComplexConjugate

/-!
NF569 — terminal connection to the ORIGINAL NF550/NF551
physical weighted-square and analytic collar identity chain.

Only if the imported exact real/complex global independence
and physical modules compile is this an unconditional theorem
of the original canonical Gram. It makes no coercivity or
signed Weil positivity assertion beyond this finite Gram.
-/

/-- Discharge the actual NF551 source independence premise,
using the identical original NF545 source embedded in ℂ.
The NF569 untruncated combination is definitionally the
NF550 original source combination. -/
theorem neutralNF569OriginalJ242GlobalIndependence :
    NeutralNF551OriginalJ242GlobalIndependence := by
  intro d hzero
  apply neutralNF569OriginalComplexCombination_globalIndependence
  intro x
  simpa only [neutralNF569OriginalComplexCombination,
    neutralNF550OriginalSourceCombination,
    neutralNF546OriginalComplexGenerator] using hzero x

/-- The original fixed positive collar separates the actual
242 source functions, via NF551 genuine analytic continuation. -/
theorem neutralNF569OriginalCollarSeparatesJ242 :
    NeutralNF550OriginalCollarSeparatesJ242 :=
  neutralNF551OriginalJ242GlobalIndependence_implies_collar
    neutralNF569OriginalJ242GlobalIndependence

/-- Strict positivity of the original fixed canonical weighted
Gram, with no source independence premise, once all imported
proofs are accepted. This is ONLY the finite correction Gram:
not the full Weil form, the original cofinite 1/10 bound, or RH. -/
theorem neutralNF569CanonicalOriginalGram_pos :
    ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re :=
  neutralNF551OriginalGlobalIndependence_implies_Gram_pos
    neutralNF569OriginalJ242GlobalIndependence

end
end WeilDefect
