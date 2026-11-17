import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramPhysicalIntegral
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
NF571 — reality and conjugation of the ACTUAL original correction.

This file depends on the already compiled NF549 exact physical
Gram integral, not NF551 parity or the pending NF566–NF569
independence chain. The original sources and canonical cutoff
are real. Their conjugation compatibility therefore descends
through the actual physical moments and the actual Gram. For
the inverse, strict positivity remains an explicit premise.
No real projection or alternative correction is introduced.
-/

def neutralNF571ConjugateCoefficients (d : Fin 242 → ℂ) :
    Fin 242 → ℂ := fun i => conj (d i)

theorem neutralNF571OriginalComplexGenerator_conj
    (i : Fin 242) (x : ℝ) :
    conj (neutralNF546OriginalComplexGenerator i x) =
      neutralNF546OriginalComplexGenerator i x := by
  simp [neutralNF546OriginalComplexGenerator]

/-- Pointwise conjugation preserves the exact full-window source,
including outside-window zero extension. -/
theorem neutralNF571OriginalWindowGenerator_conj
    (i : Fin 242) (x : ℝ) :
    conj (neutralNF546OriginalWindowGenerator i x) =
      neutralNF546OriginalWindowGenerator i x := by
  by_cases hx : x ∈ neutralNF546OriginalFullPhysicalWindow
  · simpa only [neutralNF546OriginalWindowGenerator,
      Set.indicator_of_mem hx] using
      neutralNF571OriginalComplexGenerator_conj i x
  · simp [neutralNF546OriginalWindowGenerator, Set.indicator_of_notMem hx]

theorem neutralNF571CanonicalCutoff_conj (x : ℝ) :
    conj (neutralNF548ComplexEvenCollarCutoff x) =
      neutralNF548ComplexEvenCollarCutoff x := by
  simp [neutralNF548ComplexEvenCollarCutoff]

/-- The same genuine canonical finite synthesis commutes with
coefficient conjugation. This is independent of invertibility. -/
theorem neutralNF571CanonicalSynthesis_conj
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF544BumpSynthesis neutralNF548CanonicalOriginalColumns
      (neutralNF571ConjugateCoefficients d)) x =
        conj ((neutralNF544BumpSynthesis
          neutralNF548CanonicalOriginalColumns d) x) := by
  rw [neutralNF549CanonicalSynthesis_pointwise,
    neutralNF549CanonicalSynthesis_pointwise]
  simp only [map_mul, map_sum, neutralNF571CanonicalCutoff_conj,
    neutralNF571OriginalComplexGenerator_conj,
    neutralNF571ConjugateCoefficients]

/-- The exact physical moment map intertwines conjugation on
Schwartz tests whenever their pointwise values are conjugate.
This uses its actual accepted continuum integral, not sampled
Gram entries or pointwise choices of arbitrary L² classes. -/
theorem neutralNF571OriginalPhysicalMoment_conj
    (s t : 𝓢(ℝ, ℂ)) (ht : ∀ x : ℝ, t x = conj (s x))
    (i : Fin 242) :
    neutralNF546OriginalSelectedMoments (t.toLp 2 volume) i =
      conj (neutralNF546OriginalSelectedMoments (s.toLp 2 volume) i) := by
  rw [neutralNF549OriginalPhysicalMoment_eq_integral,
    neutralNF549OriginalPhysicalMoment_eq_integral, ← integral_conj]
  apply integral_congr_ae
  filter_upwards [] with x
  simp only [ht, map_mul, neutralNF571OriginalWindowGenerator_conj]

/-- Without assuming positive definiteness, the ACTUAL original
weighted Gram commutes with pointwise coefficient conjugation. -/
theorem neutralNF571CanonicalGram_conj (d : Fin 242 → ℂ) :
    neutralNF548CanonicalOriginalWeightedGram
      (neutralNF571ConjugateCoefficients d) =
    neutralNF571ConjugateCoefficients
      (neutralNF548CanonicalOriginalWeightedGram d) := by
  funext i
  change neutralNF548CanonicalOriginalWeightedGram
      (neutralNF571ConjugateCoefficients d) i =
    conj (neutralNF548CanonicalOriginalWeightedGram d i)
  rw [neutralNF549CanonicalGram_entry_integral,
    neutralNF549CanonicalGram_entry_integral, ← integral_conj]
  apply integral_congr_ae
  filter_upwards [] with x
  simp only [map_mul, neutralNF571OriginalWindowGenerator_conj,
    neutralNF571CanonicalSynthesis_conj]

/-- An injective original Gram has an inverse commuting with
conjugation. Uniqueness is crucial: no second inverse or real
projection is used. -/
theorem neutralNF571CanonicalGramInverse_conj
    (hG : Function.Injective
      (neutralNF544PhysicalGram neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns))
    (d : Fin 242 → ℂ) :
    (neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns hG).symm
      (neutralNF571ConjugateCoefficients d) =
    neutralNF571ConjugateCoefficients
      ((neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns hG).symm d) := by
  let E := neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
    neutralNF548CanonicalOriginalColumns hG
  change E.symm (neutralNF571ConjugateCoefficients d) =
    neutralNF571ConjugateCoefficients (E.symm d)
  apply E.injective
  calc
    E (E.symm (neutralNF571ConjugateCoefficients d)) =
        neutralNF571ConjugateCoefficients d := E.apply_symm_apply _
    _ = neutralNF571ConjugateCoefficients (E (E.symm d)) :=
      congrArg neutralNF571ConjugateCoefficients (E.apply_symm_apply d).symm
    _ = E (neutralNF571ConjugateCoefficients (E.symm d)) := by
      change neutralNF571ConjugateCoefficients
          (neutralNF548CanonicalOriginalWeightedGram (E.symm d)) =
        neutralNF548CanonicalOriginalWeightedGram
          (neutralNF571ConjugateCoefficients (E.symm d))
      exact (neutralNF571CanonicalGram_conj (E.symm d)).symm

/-- The unchanged NF548 correction, conditional on its strict
positivity, commutes with conjugation pointwise. The inverse
coefficients are the very same NF544 Gram inverse. -/
theorem neutralNF571CanonicalRightInverse_conj
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF548CanonicalRightInverse hpos
        (neutralNF571ConjugateCoefficients d)) x =
      conj ((neutralNF548CanonicalRightInverse hpos d) x) := by
  let hG := neutralNF544PhysicalGram_injective_of_pos
    neutralNF546OriginalSelectedMoments
    neutralNF548CanonicalOriginalColumns hpos
  let E := neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
    neutralNF548CanonicalOriginalColumns hG
  change (neutralNF544BumpSynthesis neutralNF548CanonicalOriginalColumns
      (E.symm (neutralNF571ConjugateCoefficients d))) x =
    conj ((neutralNF544BumpSynthesis
      neutralNF548CanonicalOriginalColumns (E.symm d)) x)
  have hE : E.symm (neutralNF571ConjugateCoefficients d) =
      neutralNF571ConjugateCoefficients (E.symm d) :=
    neutralNF571CanonicalGramInverse_conj hG d
  rw [hE]
  exact neutralNF571CanonicalSynthesis_conj (E.symm d) x

/-- Real moment data produce a real-valued actual correction.
No post-hoc averaging is necessary. Positivity remains explicit. -/
theorem neutralNF571CanonicalRightInverse_realData
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (d : Fin 242 → ℂ) (hd : ∀ i, conj (d i) = d i) (x : ℝ) :
    conj ((neutralNF548CanonicalRightInverse hpos d) x) =
      (neutralNF548CanonicalRightInverse hpos d) x := by
  have hc : neutralNF571ConjugateCoefficients d = d := funext hd
  have h := neutralNF571CanonicalRightInverse_conj hpos d x
  rw [hc] at h
  exact h.symm

end
end WeilDefect
