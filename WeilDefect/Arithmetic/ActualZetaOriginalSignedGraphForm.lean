import WeilDefect.Arithmetic.ActualZetaOriginalRealOddSchwartzFullSource

namespace WeilDefect
noncomputable section
open MeasureTheory Filter InnerProductSpace
open scoped SchwartzMap ComplexConjugate ENNReal

/-! NF598: attach the signed actual all-divisor quadratic to the
complete graph, not just to Green lifts. The factor 1/2 is forced by
the two partner terms in the genuine P/N difference. No sign is
asserted by this identity. -/

def neutralNF598GraphPhysical (a : ℝ) (u : NeutralActualZetaSourceDomain a) :
    RealComplexL2 :=
  neutralLogPhysical (neutralActualZetaSourcePhysical a u).val

def neutralNF598GraphWeil (a : ℝ) (u : NeutralActualZetaSourceDomain a) : ℝ :=
  (‖neutralActualZetaPositiveAnalysis a u‖^2 -
    ‖neutralActualZetaNegativeAnalysis a u‖^2)/2

theorem neutralNF598GraphWeil_continuous (a : ℝ) :
    Continuous (neutralNF598GraphWeil a) := by
  unfold neutralNF598GraphWeil
  exact (((neutralActualZetaPositiveAnalysis a).continuous.norm.pow 2).sub
    ((neutralActualZetaNegativeAnalysis a).continuous.norm.pow 2)).div_const 2

theorem neutralNF598GraphPhysical_continuous (a : ℝ) :
    Continuous (neutralNF598GraphPhysical a) := by
  change Continuous (fun u : NeutralActualZetaSourceDomain a =>
    neutralLogPhysical (neutralActualZetaSourcePhysical a u).val)
  exact neutralLogPhysical.continuous.comp
    (continuous_subtype_val.comp (neutralActualZetaSourcePhysical a).continuous)

/-- This diagonal identity is pointwise, including every divisor copy.
Unlike the previously established Green-source identity it requires no
Green representation whatsoever. -/
theorem neutralNF598GraphWeil_coordinate (a : ℝ)
    (u : NeutralActualZetaSourceDomain a) (q : NeutralActualZetaDivisorCoordinate) :
    ‖neutralActualZetaPositiveAnalysis a u q‖^2 -
        ‖neutralActualZetaNegativeAnalysis a u q‖^2 =
      2*(conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) (neutralNF598GraphPhysical a u)) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralNF598GraphPhysical a u)).re := by
  let f := neutralActualZetaSourcePhysical a u
  have h := neutralLogPairSource_mixed_difference a (neutralActualZetaDivisorOrdinate q) f f
  have hs := neutralActualZetaSourceAnalysis_sampling a u q
  change neutralActualZetaPositiveAnalysis a u q =
    inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f ∧
    neutralActualZetaNegativeAnalysis a u q =
    inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f at hs
  simp only [← hs.1,← hs.2] at h
  have hr := congrArg Complex.re h
  simp only [Complex.sub_re,Complex.add_re,Complex.conj_mul',
    ← Complex.ofReal_pow,Complex.ofReal_re] at hr
  change _ = (conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate q)) (neutralNF598GraphPhysical a u)) *
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralNF598GraphPhysical a u)).re +
    (conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralNF598GraphPhysical a u)) *
      neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q))
        (neutralNF598GraphPhysical a u)).re at hr
  rw [hr]
  simp only [Complex.mul_re,Complex.conj_re,Complex.conj_im]
  ring

/-- Real diagonal of the actual literal Weil formula on ANY graph vector
with a C² physical correlation. Complete actual multiplicity is retained. -/
theorem neutralNF598GraphWeil_eq_literature (a : ℝ)
    (u : NeutralActualZetaSourceDomain a)
    (hreg : ContDiff ℝ 2 (neutralWindowCorrelation a
      (neutralNF598GraphPhysical a u) (neutralNF598GraphPhysical a u))) :
    neutralNF598GraphWeil a u =
      (Zeta23.EF.literatureRHS (neutralWindowCorrelation a
        (neutralNF598GraphPhysical a u) (neutralNF598GraphPhysical a u))).re := by
  let f := neutralNF598GraphPhysical a u
  let T : NeutralActualZetaDivisorCoordinate → ℂ := fun q =>
    conj (neutralWindowEvaluation a (conj (neutralActualZetaDivisorOrdinate q)) f) *
      neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) f
  have hT : Summable T := by
    convert neutralActualZetaDivisor_rawTransform_summable_of_contDiff
      (neutralWindowCorrelation a f f) hreg
      (neutralWindowCorrelation_hasCompactSupport a f f) using 1
    funext q
    exact (neutralWindowCorrelation_rawTransform a f f
      (neutralActualZetaDivisorOrdinate q)).symm
  have hEF : (∑' q, T q) = Zeta23.EF.literatureRHS (neutralWindowCorrelation a f f) :=
    neutralActualZetaWindowCorrelation_literature_of_contDiff a f f hreg
  have hp : HasSum (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralActualZetaPositiveAnalysis a u q‖^2)
      (‖neutralActualZetaPositiveAnalysis a u‖^2) := by
    simpa only [ENNReal.toReal_ofNat,Real.rpow_two] using
      lp.hasSum_norm (by norm_num : 0 < (2:ℝ≥0∞).toReal)
        (neutralActualZetaPositiveAnalysis a u)
  have hn : HasSum (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralActualZetaNegativeAnalysis a u q‖^2)
      (‖neutralActualZetaNegativeAnalysis a u‖^2) := by
    simpa only [ENNReal.toReal_ofNat,Real.rpow_two] using
      lp.hasSum_norm (by norm_num : 0 < (2:ℝ≥0∞).toReal)
        (neutralActualZetaNegativeAnalysis a u)
  have hr := Complex.reCLM.hasSum hT.hasSum
  rw [hEF] at hr
  have hs : HasSum (fun q : NeutralActualZetaDivisorCoordinate =>
      2*(T q).re) (2*(Zeta23.EF.literatureRHS (neutralWindowCorrelation a f f)).re) :=
    hr.mul_left 2
  have he : (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖neutralActualZetaPositiveAnalysis a u q‖^2 -
        ‖neutralActualZetaNegativeAnalysis a u q‖^2) = fun q => 2*(T q).re := by
    funext q
    exact neutralNF598GraphWeil_coordinate a u q
  have hd := hp.sub hn
  rw [he] at hd
  have hv := hd.unique hs
  unfold neutralNF598GraphWeil
  change _ = (Zeta23.EF.literatureRHS (neutralWindowCorrelation a f f)).re
  linarith only [hv]

/-- Smooth supported tests have the exact correlation regularity needed
by the literal EF, independently of how the graph vector was constructed. -/
theorem neutralNF598GraphWeil_eq_smooth (u : NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (hp : neutralNF598GraphPhysical (11/10) u = s.toLp 2 volume) :
    neutralNF598GraphWeil (11/10) u =
      (Zeta23.EF.literatureRHS
        (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume))).re := by
  have hc : HasCompactSupport (fun x : ℝ => s x) := by
    apply HasCompactSupport.intro (K := Set.Icc (-(11/10:ℝ)) (11/10:ℝ)) isCompact_Icc
    intro x hx
    apply hs x
    intro he
    apply hx
    rcases he with hl | hr
    · exact ⟨hl.1.le,by linarith [hl.2]⟩
    · exact ⟨by linarith [hr.1],hr.2.le⟩
  have hreg : ContDiff ℝ 2 (neutralWindowCorrelation (11/10:ℝ)
      (s.toLp 2 volume) (s.toLp 2 volume)) :=
    neutralWindowCorrelation_contDiff_of_ae_smoothSecond (11/10:ℝ)
      (s.toLp 2 volume) (s.toLp 2 volume) (fun x => s x)
      (s.smooth 2) hc (neutralNF573OriginalCollar_window_ae s hs)
  have h := neutralNF598GraphWeil_eq_literature (11/10) u (by rw [hp]; exact hreg)
  simpa only [hp] using h

end
end WeilDefect
