import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalCorrectionFullSource
import WeilDefect.Arithmetic.ActualZetaOriginalJ242CanonicalGramPositivity

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-! NF586: remove the finite Gram premise from the earlier
full-source graph correction. The graph sequence must still
realize the actual physical seed; its convergence is not inferred
from finite moment agreement. -/

theorem neutralNF586CanonicalGraphRightInverse_exists :
    ∃ R : (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11/10:ℝ),
      (∀ d, neutralNF573OriginalGraphPhysical (R d) =
        (neutralNF548CanonicalRightInverse neutralNF569CanonicalOriginalGram_pos d).toLp 2 volume) ∧
      (∀ d, neutralNF573OriginalGraphMoments (R d) = d) :=
  neutralNF573OriginalGraphRightInverse_exists neutralNF569CanonicalOriginalGram_pos

def neutralNF586CorrectedTest
    (ell : RealComplexL2) (s : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  neutralNF543Correct neutralNF546OriginalSelectedMoments
    (neutralNF548CanonicalRightInverse neutralNF569CanonicalOriginalGram_pos) ell s

/-- One bounded canonical correction works for the entire actual
convergent sequence. It realizes the same physical corrected
Schwartz functions and exactly matches every selected moment. -/
theorem neutralNF586OriginalGraph_correctedSequence
    (ell : NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : ℕ → 𝓢(ℝ,ℂ))
    (g : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ))
    (hell : ∀ᵐ x ∂volume, conj (neutralNF573OriginalGraphPhysical ell x) =
      neutralNF573OriginalGraphPhysical ell x)
    (hs : ∀ n, neutralNF573OriginalGraphPhysical (g n) = (s n).toLp 2 volume)
    (hreal : ∀ n x, conj (s n x) = s n x)
    (hodd : ∀ n x, s n (-x) = -s n x)
    (hsupp : ∀ n x, x ∉ neutralNF543OriginalCollars → s n x = 0)
    (hlim : Tendsto g atTop (nhds ell)) :
    let f := fun n => neutralNF586CorrectedTest (neutralNF573OriginalGraphPhysical ell) (s n)
    ∃ F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ),
      (∀ n, neutralNF573OriginalGraphPhysical (F n) = (f n).toLp 2 volume) ∧
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments (neutralNF573OriginalGraphPhysical ell)) ∧
      Tendsto F atTop (nhds ell) := by
  obtain ⟨R,hR,hmR⟩ := neutralNF586CanonicalGraphRightInverse_exists
  let F := fun n => neutralNF543CorrectGraph neutralNF573OriginalGraphMoments R ell (g n)
  have hF (n : ℕ) := neutralNF573OriginalGraphCorrectedSeed_physical
    neutralNF569CanonicalOriginalGram_pos R hR ell (g n) (s n) (hs n)
  have hf (n : ℕ) := neutralNF572OriginalCanonicalRealOddCorrectedTest
    (neutralNF573OriginalGraphPhysical ell) hell (s n) (hreal n) (hodd n) (hsupp n)
  refine ⟨F, hF, ?_, ?_, ?_, ?_, ?_⟩
  · intro n x
    exact (hf n).1 x
  · intro n x
    exact (hf n).2.1 x
  · intro n x hx
    exact (hf n).2.2.1 x hx
  · intro n
    exact (hf n).2.2.2.1
  · exact neutralNF573OriginalGraphCorrection_preservesConvergence R ell g hlim

end
end WeilDefect
