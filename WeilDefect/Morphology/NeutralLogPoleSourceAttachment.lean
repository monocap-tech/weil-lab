import WeilDefect.Morphology.NeutralLogHilbertCarrier
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.LinearMap

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap InnerProductSpace
open scoped InnerProduct ComplexConjugate

/-- The actual physical inclusion of the complete form carrier. -/
def neutralLogPhysicalInclusion (a : ℝ) :
    NeutralLogHilbertCarrier a →L[ℂ] RealComplexL2 :=
  neutralLogPhysical ∘L (neutralLogHilbertSubmodule a).toSubmodule.subtypeL

/-- Compact-window exponential column, with no operator-domain premise. -/
def neutralMomentColumn (a s : ℝ) (x : ℝ) : ℂ :=
  (Set.Icc (-a) a).indicator (fun x => (Real.exp (s*x) : ℂ)) x

theorem neutralMomentColumn_memLp (a s : ℝ) :
    MemLp (neutralMomentColumn a s) 2 volume := by
  have hc : Continuous (fun x : ℝ => (Real.exp (s*x) : ℂ)) := by fun_prop
  have hm : AEStronglyMeasurable (neutralMomentColumn a s) volume :=
    hc.aestronglyMeasurable.indicator measurableSet_Icc
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hi : IntegrableOn (fun x : ℝ => ‖(Real.exp (s*x) : ℂ)‖ ^ 2)
      (Set.Icc (-a) a) volume :=
    (hc.norm.pow 2).continuousOn.integrableOn_isCompact isCompact_Icc
  apply (hi.integrable_indicator measurableSet_Icc).congr
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;>
    simp [neutralMomentColumn, hx]

def neutralMomentColumnL2 (a s : ℝ) : RealComplexL2 :=
  (neutralMomentColumn_memLp a s).toLp (neutralMomentColumn a s)

theorem neutralMomentColumnL2_inner (a s : ℝ) (f : RealComplexL2) :
    inner ℂ (neutralMomentColumnL2 a s) f = sourceWindowMoment a s f := by
  rw [L2.inner_def]
  change (∫ x : ℝ, inner ℂ (neutralMomentColumnL2 a s x) (f x)) =
    ∫ x in Set.Icc (-a) a, f x * (Real.exp (s*x) : ℂ)
  rw [← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [(neutralMomentColumn_memLp a s).coeFn_toLp] with x hx
  change inner ℂ ((neutralMomentColumn_memLp a s).toLp (neutralMomentColumn a s) x)
    (f x) = _
  rw [hx]
  by_cases hmem : x ∈ Set.Icc (-a) a
  · simp [neutralMomentColumn, hmem, RCLike.inner_apply', mul_comm]
  · simp [neutralMomentColumn, hmem, RCLike.inner_apply']

/-- The retained source moment is an actual continuous linear functional,
constructed from its concrete L2 column. -/
def neutralSourceWindowMomentCLM (a s : ℝ) : RealComplexL2 →L[ℂ] ℂ :=
  InnerProductSpace.toDual ℂ RealComplexL2 (neutralMomentColumnL2 a s)

theorem neutralSourceWindowMomentCLM_eq (a s : ℝ) (f : RealComplexL2) :
    neutralSourceWindowMomentCLM a s f = sourceWindowMoment a s f :=
  neutralMomentColumnL2_inner a s f

/-- Actual adjoint source column in the complete logarithmic Hilbert space. -/
def neutralLogMomentSource (a s : ℝ) : NeutralLogHilbertCarrier a :=
  ((neutralLogPhysicalInclusion a)†) (neutralMomentColumnL2 a s)

theorem neutralLogMomentSource_inner (a s : ℝ) (f : NeutralLogHilbertCarrier a) :
    inner ℂ (neutralLogMomentSource a s) f =
      sourceWindowMoment a s (neutralLogPhysical f.val) := by
  rw [neutralLogMomentSource, adjoint_inner_left,
    neutralMomentColumnL2_inner]
  rfl

def neutralLogMoment (a s : ℝ) : NeutralLogHilbertCarrier a →L[ℂ] ℂ :=
  neutralSourceWindowMomentCLM a s ∘L neutralLogPhysicalInclusion a

theorem neutralLogMoment_eq (a s : ℝ) (f : NeutralLogHilbertCarrier a) :
    neutralLogMoment a s f = sourceWindowMoment a s (neutralLogPhysical f.val) :=
  neutralSourceWindowMomentCLM_eq a s _

/-- Concrete Hermitian cross-pole operator on the correct form carrier.
Its two terms are cross terms, not positive squares of separate moments. -/
def neutralLogPoleOperator (a : ℝ) :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  rankOne ℂ (neutralLogMomentSource a (-(1/2))) (neutralLogMomentSource a (1/2)) +
    rankOne ℂ (neutralLogMomentSource a (1/2)) (neutralLogMomentSource a (-(1/2)))

theorem neutralLogPoleOperator_mixed (a : ℝ) (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogPoleOperator a g) =
      conj (sourceWindowMoment a (-(1/2)) (neutralLogPhysical f.val)) *
        sourceWindowMoment a (1/2) (neutralLogPhysical g.val) +
      conj (sourceWindowMoment a (1/2) (neutralLogPhysical f.val)) *
        sourceWindowMoment a (-(1/2)) (neutralLogPhysical g.val) := by
  change inner ℂ f
    (inner ℂ (neutralLogMomentSource a (1/2)) g •
      neutralLogMomentSource a (-(1/2)) +
    inner ℂ (neutralLogMomentSource a (-(1/2))) g •
      neutralLogMomentSource a (1/2)) = _
  rw [inner_add_right]
  simp only [inner_smul_right (𝕜 := ℂ)]
  rw [
    ← inner_conj_symm f (neutralLogMomentSource a (-(1/2))),
    ← inner_conj_symm f (neutralLogMomentSource a (1/2))]
  simp only [neutralLogMomentSource_inner]
  ring

theorem neutralLogPoleOperator_diagonal (a : ℝ) (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogPoleOperator a f) =
      ((2 * (conj (sourceWindowMoment a (-(1/2)) (neutralLogPhysical f.val)) *
        sourceWindowMoment a (1/2) (neutralLogPhysical f.val)).re : ℝ) : ℂ) := by
  rw [neutralLogPoleOperator_mixed, sourcePoleCrossTerms_diagonal]

end

end WeilDefect
