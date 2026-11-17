import WeilDefect.Arithmetic.ActualZetaOriginalJ242GlobalIndependence
import WeilDefect.Arithmetic.ActualZetaOriginalJ242AnalyticIdentity
import WeilDefect.Arithmetic.ActualZetaOriginalJ242RealPhysicalCorrectedTest

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped ComplexConjugate SchwartzMap

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

/-- NF570: the actual NF548 canonical right inverse of the true
242 moment map, with its genuine strict collar support and original
odd parity. There is no extra separation or positivity premise.
Compiler acceptance still depends on the full NF569 source chain. -/
theorem neutralNF570Original242OddSupportedRightInverse :
    ∃ R : NeutralNF543RightInverse,
      (∀ d : Fin 242 → ℂ,
        neutralNF546OriginalSelectedMoments
          ((R d).toLp 2 volume) = d) ∧
      (∀ (d : Fin 242 → ℂ) (x : ℝ),
        x ∉ neutralNF543OriginalCollars → (R d) x = 0) ∧
      (∀ (d : Fin 242 → ℂ) (x : ℝ),
        (R d) (-x) = -(R d) x) := by
  refine ⟨neutralNF548CanonicalRightInverse
    neutralNF569CanonicalOriginalGram_pos, ?_, ?_, ?_⟩
  · exact neutralNF548CanonicalRightInverse_correct
      neutralNF569CanonicalOriginalGram_pos
  · exact neutralNF548CanonicalRightInverse_supported
      neutralNF569CanonicalOriginalGram_pos
  · exact neutralNF551CanonicalRightInverse_odd
      neutralNF569CanonicalOriginalGram_pos

/-- Terminal finite-source interface: the unchanged canonical
correction of an a.e.-real physical target by an odd real
collar test is itself real and odd, exactly moment matched,
supported in E, and admitted to the true log carrier.
There is no explicit Gram or independence premise. As a proof
candidate, it still requires the entire imported chain to pass. -/
theorem neutralNF572OriginalCanonicalRealOddCorrectedTest
    (ell : RealComplexL2)
    (hell : ∀ᵐ x ∂volume, conj (ell x) = ell x)
    (g : 𝓢(ℝ, ℂ))
    (hreal : ∀ x : ℝ, conj (g x) = g x)
    (hodd : ∀ x : ℝ, g (-x) = -g x)
    (hsupp : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0) :
    let f := neutralNF543Correct neutralNF546OriginalSelectedMoments
      (neutralNF548CanonicalRightInverse neutralNF569CanonicalOriginalGram_pos)
      ell g
    (∀ x : ℝ, conj (f x) = f x) ∧
    (∀ x : ℝ, f (-x) = -f x) ∧
    (∀ x : ℝ, x ∉ neutralNF543OriginalCollars → f x = 0) ∧
    neutralNF546OriginalSelectedMoments (f.toLp 2 volume) =
      neutralNF546OriginalSelectedMoments ell ∧
    (∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val = f.toLp 2 volume) :=
  neutralNF572OriginalCorrectedTest_realOddSupported
    neutralNF569CanonicalOriginalGram_pos ell hell g hreal hodd hsupp

end
end WeilDefect
