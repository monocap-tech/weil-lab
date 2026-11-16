import WeilDefect.Arithmetic.ActualZetaOriginalJ242SourceFunctions
import WeilDefect.Arithmetic.ActualZetaOriginalCollar242GramInverse
import Mathlib.MeasureTheory.Function.LpSpace.Indicator
import Mathlib.Analysis.InnerProductSpace.LinearMap
import Mathlib.Analysis.Normed.Group.Bounded
import Mathlib.Topology.Algebra.Module.ContinuousLinearMap.PiProd

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
NF546: the actual ORIGINAL NF407/NF505 242 selected generators are
now mapped into the genuine physical L² space, then assembled into
the linear 242-component physical moment map used by NF543/NF544.

The first 241 functions use the exact original source frequency and
monomial order; index 241 is exactly the sinh(x/2) pole. No surrogate
polynomial or abstract moment map is substituted.

The physical L² class of j_i is zero-extended from the ORIGINAL
window [-11/10,11/10], not from the strict NF528 test collars E.
This is essential: the source moments are physically evaluated on
the original full carrier, although corrected tests vanish outside E.
-/

/-- The unmodified ORIGINAL physical window, not the two thin E
test collars. -/
def neutralNF546OriginalFullPhysicalWindow : Set ℝ :=
  Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ)

/-- Embed the genuine SOURCE real J242 generator as a complex
function, preserving its exact sine/cosine/sinh formula. -/
def neutralNF546OriginalComplexGenerator (i : Fin 242) (x : ℝ) : ℂ :=
  (nf545OriginalSelectedRealGenerator i x : ℂ)

/-- Original full-window zero extension of the real-analytic
source generator. The function is not claimed globally smooth
across the window endpoints; this is a physical L² class. -/
def neutralNF546OriginalWindowGenerator (i : Fin 242) : ℝ → ℂ :=
  neutralNF546OriginalFullPhysicalWindow.indicator
    (neutralNF546OriginalComplexGenerator i)

/-- Each exact original selected generator is continuous before
truncation, including its unchanged sinh pole. -/
theorem neutralNF546OriginalComplexGenerator_continuous (i : Fin 242) :
    Continuous (neutralNF546OriginalComplexGenerator i) := by
  unfold neutralNF546OriginalComplexGenerator nf545OriginalSelectedRealGenerator
  split_ifs <;> dsimp <;> fun_prop

/-- The window-truncated original analytic generator has compact
support, including possible jumps at the original endpoints. -/
theorem neutralNF546OriginalWindowGenerator_hasCompactSupport (i : Fin 242) :
    HasCompactSupport (neutralNF546OriginalWindowGenerator i) := by
  apply HasCompactSupport.of_support_subset_isCompact
    (show IsCompact neutralNF546OriginalFullPhysicalWindow from
      isCompact_Icc)
  intro x hx
  by_contra hout
  apply hx
  simp [neutralNF546OriginalWindowGenerator,
    Set.indicator_of_notMem hout]

/-- Elementary but nontrivial physical admission: the ORIGINAL
window-truncated j_i belongs to genuine complex L². This avoids
assuming the moment functionals exist or fabricating a Gram. -/
theorem neutralNF546OriginalWindowGenerator_memLp (i : Fin 242) :
    MemLp (neutralNF546OriginalWindowGenerator i) 2 volume := by
  have hcontinuous := neutralNF546OriginalComplexGenerator_continuous i
  have hmeas : MeasurableSet neutralNF546OriginalFullPhysicalWindow := by
    exact measurableSet_Icc
  have hAE : AEStronglyMeasurable
      (neutralNF546OriginalWindowGenerator i) volume := by
    exact hcontinuous.aestronglyMeasurable.indicator hmeas
  obtain ⟨C, hC⟩ :=
    (show IsCompact neutralNF546OriginalFullPhysicalWindow from
      isCompact_Icc).exists_bound_of_continuousOn'
      hcontinuous.continuousOn
  have hbound (x : ℝ) :
      ‖neutralNF546OriginalWindowGenerator i x‖ ≤ max C 0 := by
    by_cases hx : x ∈ neutralNF546OriginalFullPhysicalWindow
    · have hc := (hC x hx).trans (le_max_left C 0)
      simpa [neutralNF546OriginalWindowGenerator,
        Set.indicator_of_mem hx] using hc
    · simp [neutralNF546OriginalWindowGenerator,
        Set.indicator_of_notMem hx]
  exact (neutralNF546OriginalWindowGenerator_hasCompactSupport i).memLp_of_bound
    hAE (max C 0) (Filter.Eventually.of_forall hbound)

/-- Genuine full-window L² representative of each of the 242 ORIGINAL
selected physical functions. -/
def neutralNF546OriginalSelectedPhysicalL2 (i : Fin 242) : RealComplexL2 :=
  (neutralNF546OriginalWindowGenerator_memLp i).toLp
    (neutralNF546OriginalWindowGenerator i)

/-- Unlike the abstract NF543 M, this is the actual physical source
moment map built explicitly from the unchanged J242 L² vectors.
Inner product is conjugate-linear in the fixed j_i and ℂ-linear in
the physical input, as required for exact Gram correction. -/
def neutralNF546OriginalSelectedMomentsCLM :
    RealComplexL2 →L[ℂ] (Fin 242 → ℂ) :=
  ContinuousLinearMap.pi fun i : Fin 242 =>
    innerSL ℂ (neutralNF546OriginalSelectedPhysicalL2 i)

/-- The genuine 242 original physical moments are bounded/continuous,
not merely an algebraic family. This continuity is the missing
physical-limit input for the original NF528 Gram correction. -/
def neutralNF546OriginalSelectedMoments : NeutralNF543Moments :=
  neutralNF546OriginalSelectedMomentsCLM.toLinearMap

/-- TRUE selected source moments are stable under physical L²
convergence. Full divisor source-graph convergence is a strictly
stronger obligation and is NOT inferred from this theorem. -/
theorem neutralNF546OriginalSelectedMoments_tendsto
    {ι : Type*} {l : Filter ι} (ell : RealComplexL2)
    (g : ι → RealComplexL2)
    (hg : Filter.Tendsto g l (nhds ell)) :
    Filter.Tendsto (fun s => neutralNF546OriginalSelectedMoments (g s))
      l (nhds (neutralNF546OriginalSelectedMoments ell)) := by
  exact neutralNF546OriginalSelectedMomentsCLM.continuous.continuousAt.tendsto.comp hg

/-- Each output coordinate is EXACTLY the genuine original
full-window j_i/L² pairing, not an invented ℂ-linear observation. -/
theorem neutralNF546OriginalSelectedMoments_apply
    (f : RealComplexL2) (i : Fin 242) :
    neutralNF546OriginalSelectedMoments f i =
      inner ℂ (neutralNF546OriginalSelectedPhysicalL2 i) f := by
  rfl

/-- The Gram of the ACTUAL original J242 physical moments with any
smooth correction columns. The columns are not yet asserted to
equal χ*j_i: that source-specific bump identity is a separate gate. -/
def neutralNF546OriginalPhysicalGram (b : Fin 242 → 𝓢(ℝ, ℂ)) :
    Module.End ℂ (Fin 242 → ℂ) :=
  neutralNF544PhysicalGram neutralNF546OriginalSelectedMoments b

/-- The explicit original physical J242 moments are now a CONCRETE
argument to the NF544 242-dimensional inverse construction. Only
the authentic supported correction columns and their positive
weighted Gram remain hypotheses. -/
theorem neutralNF546OriginalJ242Gram_correctedLogCarrier
    (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hGram : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF546OriginalPhysicalGram b d) i).re)
    (hb : ∀ (j : Fin 242) (x : ℝ),
      x ∉ neutralNF543OriginalCollars → (b j) x = 0)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0) :
    ∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val =
        (neutralNF543Correct neutralNF546OriginalSelectedMoments
          (neutralNF544GramRightInverse neutralNF546OriginalSelectedMoments b
            (neutralNF544PhysicalGram_injective_of_pos
              neutralNF546OriginalSelectedMoments b hGram))
          ell g).toLp 2 volume ∧
      neutralNF546OriginalSelectedMoments
        ((neutralNF543Correct neutralNF546OriginalSelectedMoments
          (neutralNF544GramRightInverse neutralNF546OriginalSelectedMoments b
            (neutralNF544PhysicalGram_injective_of_pos
              neutralNF546OriginalSelectedMoments b hGram))
          ell g).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments ell := by
  exact neutralNF544OriginalGram_correctedSmoothLogCarrier
    neutralNF546OriginalSelectedMoments b hGram hb ell g

end
end WeilDefect
