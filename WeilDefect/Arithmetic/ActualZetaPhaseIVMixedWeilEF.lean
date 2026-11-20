import WeilDefect.Arithmetic.ActualZetaPhaseIVExactMixedGraph
import WeilDefect.Arithmetic.ActualZetaSmoothCorrelationRegularity
import Mathlib.Analysis.InnerProductSpace.l2Space

namespace WeilDefect
noncomputable section
open InnerProductSpace MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
IV004 — Recover the exact TWO-ARGUMENT literal zeta Weil explicit formula
from the pre-existing authentic full-multiplicity P/N source graph.

The EF is evaluated on (physical v, physical u), since
neutralIV003GraphMixed a u v is linear in its FIRST argument, whereas
neutralWindowCorrelation a f g is conjugate-linear in f and linear in g.

The only analytical input to the main theorem is C² regularity of that
literal WINDOWED mixed correlation. This follows automatically from
an a.e. compact C² representative of the SECOND correlation input.

This does not identify arbitrary unwindowed Schwartz tests with graph
vectors, change a, prove any mixed positivity inequality, or prove RH.
-/

/-- The authentic mixed EF, not a newly invented quadratic oracle.
Argument order is chosen to preserve first-slot complex linearity. -/
def neutralIV004WindowedMixedEF (a : ℝ)
    (u v : NeutralActualZetaSourceDomain a) : ℂ :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a
      (neutralNF598GraphPhysical a v)
      (neutralNF598GraphPhysical a u))

/-- The complete, multiplicity-preserving ZERO-SIDE mixed P/N difference
is twice the literal mixed EF. The second partner product is reindexed
by the already proved actual-divisor conjugate-pair equivalence.

No positivity of the signed P/N difference is assumed or inferred. -/
theorem neutralIV004SourceMixed_fullDivisorSum (a : ℝ)
    (u v : NeutralActualZetaSourceDomain a)
    (hreg : ContDiff ℝ 2
      (neutralWindowCorrelation a
        (neutralNF598GraphPhysical a v)
        (neutralNF598GraphPhysical a u))) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralActualZetaPositiveAnalysis a v q) *
          neutralActualZetaPositiveAnalysis a u q -
        conj (neutralActualZetaNegativeAnalysis a v q) *
          neutralActualZetaNegativeAnalysis a u q) =
      2 * neutralIV004WindowedMixedEF a u v := by
  let F : NeutralActualZetaDivisorCoordinate → ℂ := fun q =>
    conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate q))
        (neutralNF598GraphPhysical a v)) *
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralNF598GraphPhysical a u)
  let R : NeutralActualZetaDivisorCoordinate → ℂ := fun q =>
    conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (neutralNF598GraphPhysical a v)) *
      neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralNF598GraphPhysical a u)
  have hF : Summable F := by
    dsimp [F]
    convert neutralActualZetaDivisor_rawTransform_summable_of_contDiff
      (neutralWindowCorrelation a
        (neutralNF598GraphPhysical a v)
        (neutralNF598GraphPhysical a u))
      hreg
      (neutralWindowCorrelation_hasCompactSupport a
        (neutralNF598GraphPhysical a v)
        (neutralNF598GraphPhysical a u)) using 1
    funext q
    exact (neutralWindowCorrelation_rawTransform a
      (neutralNF598GraphPhysical a v)
      (neutralNF598GraphPhysical a u)
      (neutralActualZetaDivisorOrdinate q)).symm
  have hRF (q : NeutralActualZetaDivisorCoordinate) :
      R q = F (neutralActualZetaDivisorPairEquiv q) := by
    change R q = F (neutralActualZetaDivisorPair q)
    dsimp [R, F]
    rw [neutralActualZetaDivisorOrdinate_pair]
    simp only [starRingEnd_apply, star_star]
  have hR : Summable R := by
    apply (neutralActualZetaDivisorPairEquiv.summable_iff.mpr hF).congr
    intro q
    exact (hRF q).symm
  have hRsum : (∑' q, R q) = (∑' q, F q) := by
    calc
      (∑' q, R q) =
          ∑' q, F (neutralActualZetaDivisorPairEquiv q) :=
        tsum_congr hRF
      _ = ∑' q, F q := neutralActualZetaDivisorPairEquiv.tsum_eq F
  have hFsum : (∑' q, F q) = neutralIV004WindowedMixedEF a u v :=
    neutralActualZetaWindowCorrelation_literature_of_contDiff a
      (neutralNF598GraphPhysical a v)
      (neutralNF598GraphPhysical a u) hreg
  have hterm (q : NeutralActualZetaDivisorCoordinate) :
      (conj (neutralActualZetaPositiveAnalysis a v q) *
          neutralActualZetaPositiveAnalysis a u q -
        conj (neutralActualZetaNegativeAnalysis a v q) *
          neutralActualZetaNegativeAnalysis a u q) = F q + R q :=
    neutralIV003GraphMixed_coordinate a v u q
  calc
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralActualZetaPositiveAnalysis a v q) *
          neutralActualZetaPositiveAnalysis a u q -
        conj (neutralActualZetaNegativeAnalysis a v q) *
          neutralActualZetaNegativeAnalysis a u q) =
        ∑' q, (F q + R q) := tsum_congr hterm
    _ = (∑' q, F q) + (∑' q, R q) := hF.tsum_add hR
    _ = 2 * (∑' q, F q) := by rw [hRsum]; ring
    _ = 2 * neutralIV004WindowedMixedEF a u v := by rw [hFsum]

/-- Exact full-divisor signed Hermitian mixed pairing = literal TWO-ARGUMENT
Weil EF. This uses the ℓ² inner-product summation law, the real existing
P/N source graph, the genuine partner involution, and the actual complete
zeta explicit formula — not diagonal positivity or a new finite Gram. -/
theorem neutralIV004GraphMixed_eq_literature_of_C2 (a : ℝ)
    (u v : NeutralActualZetaSourceDomain a)
    (hreg : ContDiff ℝ 2
      (neutralWindowCorrelation a
        (neutralNF598GraphPhysical a v)
        (neutralNF598GraphPhysical a u))) :
    neutralIV003GraphMixed a u v =
      neutralIV004WindowedMixedEF a u v := by
  have hP : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralActualZetaPositiveAnalysis a v q) *
        neutralActualZetaPositiveAnalysis a u q) := by
    have h := (lp.hasSum_inner
      (neutralActualZetaPositiveAnalysis a v)
      (neutralActualZetaPositiveAnalysis a u)).summable
    simpa only [RCLike.inner_apply', starRingEnd_apply] using h
  have hN : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralActualZetaNegativeAnalysis a v q) *
        neutralActualZetaNegativeAnalysis a u q) := by
    have h := (lp.hasSum_inner
      (neutralActualZetaNegativeAnalysis a v)
      (neutralActualZetaNegativeAnalysis a u)).summable
    simpa only [RCLike.inner_apply', starRingEnd_apply] using h
  unfold neutralIV003GraphMixed
  rw [lp.inner_eq_tsum, lp.inner_eq_tsum]
  simp only [RCLike.inner_apply', starRingEnd_apply]
  rw [← hP.tsum_sub hN,
      neutralIV004SourceMixed_fullDivisorSum a u v hreg]
  ring

/-- One a.e. compact C² representative, of the SECOND mixed-correlation
input, suffices to remove the C² premise. This is NOT the extra premise
that every arbitrary Schwartz vector already has a full source-graph lift. -/
theorem neutralIV004GraphMixed_eq_literature_of_smoothRepresentative
    (a : ℝ) (u v : NeutralActualZetaSourceDomain a)
    (ψ : ℝ → ℂ)
    (hψ : ContDiff ℝ 2 ψ)
    (hψc : HasCompactSupport ψ)
    (hψae : neutralWindowRepresentative a
      (neutralNF598GraphPhysical a u) =ᵐ[volume] ψ) :
    neutralIV003GraphMixed a u v =
      neutralIV004WindowedMixedEF a u v :=
  neutralIV004GraphMixed_eq_literature_of_C2 a u v
    (neutralWindowCorrelation_contDiff_of_ae_smoothSecond a
      (neutralNF598GraphPhysical a v)
      (neutralNF598GraphPhysical a u)
      ψ hψ hψc hψae)

/-- The actual mixed EF dictionary for two source-graph lifts physically
equal to arbitrary COMPLEX Schwartz tests in the frozen original collars.
No real-odd premise occurs in the identity; full graph LIFTS still must be
supplied separately for the chosen tests. -/
theorem neutralIV004OriginalCollarsMixedEF
    (u v : NeutralActualZetaSourceDomain (11/10:ℝ))
    (s t : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (_ht : ∀ x, x ∉ neutralNF543OriginalCollars → t x = 0)
    (hu : neutralNF598GraphPhysical (11/10) u = s.toLp 2 volume)
    (hv : neutralNF598GraphPhysical (11/10) v = t.toLp 2 volume) :
    neutralIV003GraphMixed (11/10) u v =
      Zeta23.EF.literatureRHS
        (neutralWindowCorrelation (11/10)
          (t.toLp 2 volume) (s.toLp 2 volume)) := by
  have hc : HasCompactSupport (fun x : ℝ => s x) := by
    apply HasCompactSupport.intro (K := Set.Icc (-(11/10:ℝ)) (11/10:ℝ)) isCompact_Icc
    intro x hx
    apply hs x
    intro he
    apply hx
    rcases he with hl | hr
    · exact ⟨hl.1.le, by linarith [hl.2]⟩
    · exact ⟨by linarith [hr.1], hr.2.le⟩
  have hrep : neutralWindowRepresentative (11/10:ℝ)
      (neutralNF598GraphPhysical (11/10) u) =ᵐ[volume] (fun x => s x) := by
    rw [hu]
    exact neutralNF573OriginalCollar_window_ae s hs
  have h := neutralIV004GraphMixed_eq_literature_of_smoothRepresentative
    (11/10:ℝ) u v (fun x => s x) (s.smooth 2) hc hrep
  simpa only [neutralIV004WindowedMixedEF, hu, hv] using h

#print axioms neutralIV004SourceMixed_fullDivisorSum
#print axioms neutralIV004GraphMixed_eq_literature_of_C2
#print axioms neutralIV004GraphMixed_eq_literature_of_smoothRepresentative
#print axioms neutralIV004OriginalCollarsMixedEF

end WeilDefect
