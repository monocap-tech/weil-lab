import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWiderThreeCellPrime9Coercivity
import Mathlib.Analysis.Distribution.SchwartzSpace.CompactSupport
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric
open scoped SchwartzMap ComplexConjugate

/-!
IV021 — GENUINE original THREE-CELL Schwartz PARTITION.

IV020 targeted the signed original one-tenth lower bound for
every direct physical sum S+v•t with old S in the unchanged
NF543 strict TWO collars and new t supported in the doubled
radius [99/500,101/500] around c=1/5. It did NOT show that
every Schwartz function f supported in the THREE-CELL UNION
admits an actual decomposition of this kind.

IV021 constructs a true Mathlib ContDiffBump cutoff beta:
  beta(x)=1 on the entire NEW closed central interval;
  beta(x)=0 on both historical ORIGINAL strict NF543 collars;
  0<beta.rIn=1/20<beta.rOut=1/10.

Multiply every genuine complex Schwartz f by this REAL smooth
compact cutoff via the Mathlib CONTINUOUS Schwartz multiplication
map, rather than multiplying by a discontinuous interval
indicator. Set t=beta*f and S=f-t. The literal support conditions
and f=S+t are proved directly in the real physical variable x.

Thus the IV020 authenticated original positive-direct-sum theorem
applies to EVERY genuine complex Schwartz f supported on the
entire three-cell union, not only a selected old finite
coefficient vector. Original prime n=9, both poles, complete
Gamma symbol and unchanged signed Weil expression remain
identical. No outside coercivity, global positivity or RH.
Kernel acceptance depends on a real Lean .olean and strict
standard-axiom audit of all source anchors.
-/

/-- Canonical smooth real plateau cutoff with inner radius
1/20 and outer radius 1/10 around the actual central source
coordinate 1/5. Both radii exceed the new support radius
1/500 but the outer ball is disjoint from the two true
original support collars around ±11/10. -/
def neutralIV021PhysicalCutoff : ContDiffBump (1/5:ℝ) :=
  ⟨(1/20:ℝ), (1/10:ℝ), by norm_num, by norm_num⟩

/-- Exact original physical two-collar vanishing of the
Schwartz-preserving real smooth plateau. -/
theorem neutralIV021Cutoff_old_zero
    (x : ℝ) (hx : x ∈ neutralNF543OriginalCollars) :
    neutralIV021PhysicalCutoff x = 0 := by
  have hd :
      neutralIV021PhysicalCutoff.rOut ≤
        dist x (1/5:ℝ) := by
    change (1/10:ℝ) ≤ dist x (1/5:ℝ)
    rw [Real.dist_eq]
    rcases hx with hL | hR
    · rw [abs_of_neg (by linarith [hL.2])]
      linarith [hL.2]
    · rw [abs_of_pos (by linarith [hR.1])]
      linarith [hR.1]
  exact neutralIV021PhysicalCutoff.zero_of_le_dist hd

/-- The same cutoff is identically ONE on the WHOLE literal
closed new interval, including both interval endpoints. -/
theorem neutralIV021Cutoff_new_one
    (x : ℝ) (hx : x ∈ neutralIV020WidePhysicalInterval) :
    neutralIV021PhysicalCutoff x = 1 := by
  apply neutralIV021PhysicalCutoff.one_of_mem_closedBall
  have hdist : dist x (1/5:ℝ) ≤ (1/20:ℝ) := by
    rw [Real.dist_eq]
    unfold neutralIV020WidePhysicalInterval at hx
    apply abs_le.mpr
    constructor <;> linarith [hx.1,hx.2]
  simpa only [Metric.mem_closedBall] using hdist

/-- Smooth compact support implies genuinely TEMPERATE
multiplication. This is the analytic reason splitting a
Schwartz f with this cutoff stays inside the actual
complex Schwartz space; a raw characteristic function would
not be differentiable and would fail this step. -/
theorem neutralIV021Cutoff_hasTemperateGrowth :
    (fun x : ℝ => neutralIV021PhysicalCutoff x).HasTemperateGrowth := by
  exact neutralIV021PhysicalCutoff.hasCompactSupport.hasTemperateGrowth
    neutralIV021PhysicalCutoff.contDiff

/-- The canonical new-cell component is a genuine complex
Schwartz function, defined through Mathlib's continuous
real-scalar multiplication operator on complex Schwartz
functions. Its source is not a fabricated linear projection. -/
def neutralIV021NewCellPart (f : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  SchwartzMap.smulLeftCLM ℂ
    (fun x : ℝ => neutralIV021PhysicalCutoff x) f

/-- Literal physical value of the Schwartz-preserving multiplier. -/
theorem neutralIV021NewCellPart_apply
    (f : 𝓢(ℝ,ℂ)) (x : ℝ) :
    neutralIV021NewCellPart f x =
      neutralIV021PhysicalCutoff x • f x := by
  exact SchwartzMap.smulLeftCLM_apply_apply
    neutralIV021Cutoff_hasTemperateGrowth f x

/-- The retained old-cell part is the genuine Schwartz
DIFFERENCE of the source f and its smooth new-cell component. -/
def neutralIV021OldCellPart (f : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  f - neutralIV021NewCellPart f

/-- Exact physical decomposition of EVERY complex Schwartz f
supported in the real original widened THREE-CELL union.
We prove the actual old and new pointwise vanishing predicates,
not an unproved partition-of-unity axiom.

There is NO finite dimensionality constraint or chosen
basis: the decomposition works for the full Schwartz class. -/
theorem neutralIV021EveryThreeCellSchwartz_decomposes
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → f x = 0) :
    neutralNF735InOriginalCollars (neutralIV021OldCellPart f) ∧
    (∀ x : ℝ,
      x ∉ neutralIV020WidePhysicalInterval →
        neutralIV021NewCellPart f x = 0) ∧
    f = neutralIV021OldCellPart f + neutralIV021NewCellPart f := by
  have hOld :
      neutralNF735InOriginalCollars
        (neutralIV021OldCellPart f) := by
    intro x hx
    by_cases hn : x ∈ neutralIV020WidePhysicalInterval
    · simp [neutralIV021OldCellPart,
        neutralIV021NewCellPart_apply,
        neutralIV021Cutoff_new_one x hn]
    · have hfzero : f x = 0 := hf x (by
        intro h
        exact h.elim hx hn)
      simp [neutralIV021OldCellPart,
        neutralIV021NewCellPart_apply, hfzero]
  have hNew :
      ∀ x : ℝ, x ∉ neutralIV020WidePhysicalInterval →
        neutralIV021NewCellPart f x = 0 := by
    intro x hx
    rw [neutralIV021NewCellPart_apply]
    by_cases hold : x ∈ neutralNF543OriginalCollars
    · rw [neutralIV021Cutoff_old_zero x hold]
      simp
    · have hfzero : f x = 0 := hf x (by
        intro h
        exact h.elim hold hx)
      simp [hfzero]
  refine ⟨hOld,hNew,?_⟩
  change f = (f - neutralIV021NewCellPart f) +
    neutralIV021NewCellPart f
  exact (sub_add_cancel f (neutralIV021NewCellPart f)).symm

/-- An EXACT prime-side dictionary for an ARBITRARY whole
three-cell-supported Schwartz input. This is stronger than
IV020's special old+new direct-sum statement: the new smooth
physical partition proves that no additional prime modes
enter from a general function on the entire three-cell union.
The surviving original NF600 n=9 old-old term is retained. -/
theorem neutralIV021EveryThreeCell_originalPrime_eq_old
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → f x = 0) :
    neutralIV011OriginalMixedPrime (11/10:ℝ) f f =
      neutralIV011OriginalMixedPrime (11/10:ℝ)
        (neutralIV021OldCellPart f)
        (neutralIV021OldCellPart f) := by
  obtain ⟨hOld,hNew,hSplit⟩ :=
    neutralIV021EveryThreeCellSchwartz_decomposes f hf
  have hnewInterval :
      ∀ x : ℝ,
        x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
          ((1/5:ℝ)+(1/500:ℝ)) →
            neutralIV021NewCellPart f x = 0 := by
    simpa only [neutralIV020WidePhysicalInterval,
      show (1/5:ℝ)-(1/500:ℝ)=99/500 by norm_num,
      show (1/5:ℝ)+(1/500:ℝ)=101/500 by norm_num] using hNew
  have hp := neutralIV020WideExpandedPrime_eq_old
    (neutralIV021OldCellPart f)
    (neutralIV021NewCellPart f) (1:ℂ)
    hOld hnewInterval
  simpa only [one_smul, ←hSplit] using hp

/-- MAIN IV021 original signed-support result TARGET:
ALL COMPLEX SCHWARTZ FUNCTIONS supported in the true original
two strict collars PLUS the new doubled-radius central cell
satisfy the genuine Zeta23 original signed Weil quadratic
coercivity bound of 1/10.

No old-source representation, finite coefficient family,
mixed-Schur inequality, diagonal sign, or external prime
estimate is required. The direct actual decomposition and
IV020 ORIGINAL n=9 source transfer/one-tenth coercivity
supply every one of those obligations.

This remains a candidate until a genuine pinned Lean kernel
build and strict original-source standard-axiom audit PASS.
It proves neither positivity on every Schwartz support nor RH. -/
theorem neutralIV021WholeThreeCellOriginalWeil_oneTenth
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → f x = 0) :
    (1/10:ℝ) * neutralNF600Mass f ≤
      (neutralIV010Diagonal (11/10:ℝ) f).re := by
  obtain ⟨hOld,hNew,hSplit⟩ :=
    neutralIV021EveryThreeCellSchwartz_decomposes f hf
  have hnewInterval :
      ∀ x : ℝ,
        x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
          ((1/5:ℝ)+(1/500:ℝ)) →
            neutralIV021NewCellPart f x = 0 := by
    simpa only [neutralIV020WidePhysicalInterval,
      show (1/5:ℝ)-(1/500:ℝ)=99/500 by norm_num,
      show (1/5:ℝ)+(1/500:ℝ)=101/500 by norm_num] using hNew
  have hOriginal :=
    neutralIV020WideOriginalOldPlusNew_oneTenth_coercive
      (neutralIV021OldCellPart f)
      (neutralIV021NewCellPart f) (1:ℂ)
      hOld hnewInterval
  simpa only [one_smul, ←hSplit] using hOriginal

#print axioms neutralIV020WideThreeCell_volume
#print axioms neutralIV020WideOriginalOldPlusNew_oneTenth_coercive
#print axioms neutralIV020WideExpandedPrime_eq_old
#print axioms neutralNF600Prime_bound_actual
#print axioms neutralIV021Cutoff_old_zero
#print axioms neutralIV021Cutoff_new_one
#print axioms neutralIV021Cutoff_hasTemperateGrowth
#print axioms neutralIV021NewCellPart_apply
#print axioms neutralIV021EveryThreeCellSchwartz_decomposes
#print axioms neutralIV021EveryThreeCell_originalPrime_eq_old
#print axioms neutralIV021WholeThreeCellOriginalWeil_oneTenth

end
end WeilDefect
