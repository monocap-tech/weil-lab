import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalCorrectionContinuity

namespace WeilDefect
noncomputable section
open MeasureTheory Filter Module
open scoped SchwartzMap ComplexConjugate
set_option maxHeartbeats 6000000
set_option maxRecDepth 10000

/-- The graph-level corrected seed is exactly the original physical
Schwartz correction, provided the seed realizes that same Schwartz
test. This prevents treating an unrelated graph sequence as a
certificate for the canonical physical correction. -/
theorem neutralNF573OriginalGraphCorrectedSeed_physical
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (R : (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (hR : ∀ d, neutralNF573OriginalGraphPhysical (R d) =
      (neutralNF548CanonicalRightInverse hpos d).toLp 2 volume)
    (ell g : NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (s : 𝓢(ℝ, ℂ))
    (hs : neutralNF573OriginalGraphPhysical g = s.toLp 2 volume) :
    neutralNF573OriginalGraphPhysical
      (neutralNF543CorrectGraph neutralNF573OriginalGraphMoments R ell g) =
      (neutralNF543Correct neutralNF546OriginalSelectedMoments
        (neutralNF548CanonicalRightInverse hpos)
        (neutralNF573OriginalGraphPhysical ell) s).toLp 2 volume := by
  let d : Fin 242 → ℂ :=
    neutralNF573OriginalGraphMoments ell - neutralNF573OriginalGraphMoments g
  have hd : d = neutralNF546OriginalSelectedMoments (neutralNF573OriginalGraphPhysical ell) -
      neutralNF546OriginalSelectedMoments (s.toLp 2 volume) := by
    change neutralNF546OriginalSelectedMoments (neutralNF573OriginalGraphPhysical ell) -
      neutralNF546OriginalSelectedMoments (neutralNF573OriginalGraphPhysical g) = _
    rw [hs]
  calc
    _ = neutralNF573OriginalGraphPhysical g +
          neutralNF573OriginalGraphPhysical (R d) := by
      change neutralNF573OriginalGraphPhysical (g + R d) = _
      exact map_add neutralNF573OriginalGraphPhysical _ _
    _ = s.toLp 2 volume + (neutralNF548CanonicalRightInverse hpos d).toLp 2 volume := by
      rw [hs,hR]
    _ = (s + neutralNF548CanonicalRightInverse hpos d).toLp 2 volume :=
      (map_add (SchwartzMap.toLpCLM ℂ ℂ 2 volume) s
        (neutralNF548CanonicalRightInverse hpos d)).symm
    _ = _ := by
      rw [hd]
      rfl

end
end WeilDefect
