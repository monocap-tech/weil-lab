import WeilDefect.Arithmetic.ActualZetaPhaseIVComplexSchwartzFullSource
import WeilDefect.Arithmetic.ActualZetaPhaseIVMixedWeilEF

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap

/-!
IV005 composite bridge. This file deliberately imports the PENDING
IV004 mixed arithmetic dictionary. Its certification depends on an
independent strict kernel/axiom audit of the IV004 source and IV005
complex graph-lift chain. It asserts an EF identity, NOT positivity.

Unlike NF573, there is NO reality/oddness restriction on either test.
Unlike NF600, there is NO fixed 11/10 two-collar geometry: a is any
window containing the two complex Schwartz supports.
-/

/-- Every pair of arbitrary complex Schwartz tests with support in
the SAME finite window admits two actual full-divisor graph lifts,
whose source mixed form agrees exactly with the original complete
two-argument literal Weil explicit formula.

The support and window stay explicit; there is no conclusion here
about invariance across different windows or sign of the mixed EF. -/
theorem neutralIV005AnyComplexPair_mixedEF
    (a : ℝ) (s t : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-a) a → t x = 0) :
    ∃ u v : NeutralActualZetaSourceDomain a,
      neutralNF598GraphPhysical a u = s.toLp 2 volume ∧
      neutralNF598GraphPhysical a v = t.toLp 2 volume ∧
      neutralIV003GraphMixed a u v =
        Zeta23.EF.literatureRHS
          (neutralWindowCorrelation a
            (t.toLp 2 volume) (s.toLp 2 volume)) := by
  obtain ⟨u,hu⟩ := neutralIV005ComplexSchwartz_fullSource a s hs
  obtain ⟨v,hv⟩ := neutralIV005ComplexSchwartz_fullSource a t ht
  change neutralNF598GraphPhysical a u = s.toLp 2 volume at hu
  change neutralNF598GraphPhysical a v = t.toLp 2 volume at hv
  have hc : HasCompactSupport (fun x : ℝ => s x) := by
    apply HasCompactSupport.intro (K := Set.Icc (-a) a) isCompact_Icc
    intro x hx
    exact hs x hx
  have hreg : ContDiff ℝ 2
      (neutralWindowCorrelation a
        (t.toLp 2 volume) (s.toLp 2 volume)) :=
    neutralWindowCorrelation_contDiff_of_ae_smoothSecond a
      (t.toLp 2 volume) (s.toLp 2 volume)
      (fun x => s x) (s.smooth 2) hc
      (neutralIV005WindowSchwartz_ae a s hs)
  have heq := neutralIV004GraphMixed_eq_literature_of_C2 a u v
    (by simpa only [hu,hv] using hreg)
  refine ⟨u,v,hu,hv,?_⟩
  simpa only [neutralIV004WindowedMixedEF,hu,hv] using heq

#print axioms neutralIV005AnyComplexPair_mixedEF

end
end WeilDefect
