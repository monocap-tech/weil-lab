import WeilDefect.Arithmetic.ActualZetaOriginalJ242PhysicalMomentMap
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ContDiff ComplexConjugate

/-!
NF547: ELIMINATE the arbitrary 242 Schwartz-column FAMILY b
from the original NF546 moment/Gram gate. For each of the TRUE
original analytic j_i, take its product with ONE fixed physical
strict-two-collar C∞ cutoff χ. No surrogate 242 moment directions.

The explicit χ is still assumed smooth, compact, and E-supported;
the strict Gram positivity is still an explicit hypothesis.
This file does NOT assert that the original source-weighted Gram is
yet Lean-certified positive or that χ has been explicitly implemented.
-/

/-- True source generator, before the full-window L² truncation, is
smooth of ALL orders. Each of its 241 original sine/cosine monomial
rows and the genuine sinh pole is handled in the same source formula. -/
theorem neutralNF547OriginalComplexGenerator_smooth (i : Fin 242) :
    ContDiff ℝ ∞ (neutralNF546OriginalComplexGenerator i) := by
  have hreal : ContDiff ℝ ∞ (nf545OriginalSelectedRealGenerator i) := by
    unfold nf545OriginalSelectedRealGenerator
    by_cases hi : i.val < 241
    · simp only [dif_pos hi]
      by_cases he : Even (nf545OriginalOscillatorNodeAt ⟨i.val, hi⟩).2
      · simp only [if_pos he]
        fun_prop
      · simp only [if_neg he]
        fun_prop
    · simp only [dif_neg hi]
      fun_prop
  change ContDiff ℝ ∞
    (fun x : ℝ => Complex.ofRealCLM (nf545OriginalSelectedRealGenerator i x))
  exact Complex.ofRealCLM.contDiff.comp hreal

/-- The ACTUAL original generator j_i times ONE smooth correction
cutoff χ. Its Schwartz class follows from C∞ and compact support;
the original source formula is unchanged. -/
def neutralNF547OriginalWeightedColumn
    (χ : ℝ → ℂ) (hχsmooth : ContDiff ℝ ∞ χ)
    (hχcompact : HasCompactSupport χ)
    (i : Fin 242) : 𝓢(ℝ, ℂ) :=
  (hχcompact.mul_right).toSchwartzMap
    (hχsmooth.mul (neutralNF547OriginalComplexGenerator_smooth i))

/-- These are genuine χ*j_i, pointwise, not abstract or numerical
column surrogates. -/
theorem neutralNF547OriginalWeightedColumn_apply
    (χ : ℝ → ℂ) (hχsmooth : ContDiff ℝ ∞ χ)
    (hχcompact : HasCompactSupport χ)
    (i : Fin 242) (x : ℝ) :
    neutralNF547OriginalWeightedColumn χ hχsmooth hχcompact i x =
      χ x * neutralNF546OriginalComplexGenerator i x := by
  rfl

/-- The ORIGINAL strict terminal collars, with unchanged B and δ,
support every genuine χ*j_i correction direction. -/
theorem neutralNF547OriginalWeightedColumn_supported
    (χ : ℝ → ℂ) (hχsmooth : ContDiff ℝ ∞ χ)
    (hχcompact : HasCompactSupport χ)
    (hχsupport : ∀ x : ℝ,
      x ∉ neutralNF543OriginalCollars → χ x = 0)
    (i : Fin 242) (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    neutralNF547OriginalWeightedColumn χ hχsmooth hχcompact i x = 0 := by
  rw [neutralNF547OriginalWeightedColumn_apply, hχsupport x hx]
  simp

/-- All 242 GENUINE source columns from ONE common χ, not a freely
supplied correction family. This is exactly the NF528 prescription. -/
def neutralNF547OriginalWeightedColumns
    (χ : ℝ → ℂ) (hχsmooth : ContDiff ℝ ∞ χ)
    (hχcompact : HasCompactSupport χ) :
    Fin 242 → 𝓢(ℝ, ℂ) :=
  neutralNF547OriginalWeightedColumn χ hχsmooth hχcompact

/-- The ACTUAL original source's weighted 242×242 physical Gram
endomorphism: fixed original selected j_i and smooth χ*j_j. -/
def neutralNF547OriginalWeightedGram
    (χ : ℝ → ℂ) (hχsmooth : ContDiff ℝ ∞ χ)
    (hχcompact : HasCompactSupport χ) :
    Module.End ℂ (Fin 242 → ℂ) :=
  neutralNF546OriginalPhysicalGram
    (neutralNF547OriginalWeightedColumns χ hχsmooth hχcompact)

/-- The TRUE original 242-source Gram positivity gate now assumes
only one smooth supported χ and positivity for the concretely
constructed real source j_i Gram. No arbitrary M or b remains.
From this condition NF543/544 admit a SAME-SOURCE corrected
physical L² representative to the authentic logarithmic Hilbert
carrier, with ALL 242 original moments matched exactly. -/
theorem neutralNF547OriginalWeightedGram_correctedLogCarrier
    (χ : ℝ → ℂ)
    (hχsmooth : ContDiff ℝ ∞ χ)
    (hχcompact : HasCompactSupport χ)
    (hχsupport : ∀ x : ℝ,
      x ∉ neutralNF543OriginalCollars → χ x = 0)
    (hGram : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) *
          (neutralNF547OriginalWeightedGram
            χ hχsmooth hχcompact d) i).re)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ,
      x ∉ neutralNF543OriginalCollars → g x = 0) :
    ∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val =
        (neutralNF543Correct neutralNF546OriginalSelectedMoments
          (neutralNF544GramRightInverse
            neutralNF546OriginalSelectedMoments
            (neutralNF547OriginalWeightedColumns
              χ hχsmooth hχcompact)
            (neutralNF544PhysicalGram_injective_of_pos
              neutralNF546OriginalSelectedMoments
              (neutralNF547OriginalWeightedColumns
                χ hχsmooth hχcompact) hGram))
          ell g).toLp 2 volume ∧
      neutralNF546OriginalSelectedMoments
        ((neutralNF543Correct neutralNF546OriginalSelectedMoments
          (neutralNF544GramRightInverse
            neutralNF546OriginalSelectedMoments
            (neutralNF547OriginalWeightedColumns
              χ hχsmooth hχcompact)
            (neutralNF544PhysicalGram_injective_of_pos
              neutralNF546OriginalSelectedMoments
              (neutralNF547OriginalWeightedColumns
                χ hχsmooth hχcompact) hGram))
          ell g).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments ell := by
  exact neutralNF546OriginalJ242Gram_correctedLogCarrier
    (neutralNF547OriginalWeightedColumns χ hχsmooth hχcompact)
    hGram
    (fun i x hx =>
      neutralNF547OriginalWeightedColumn_supported
        χ hχsmooth hχcompact hχsupport i x hx)
    ell g hg

end
end WeilDefect
