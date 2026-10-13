import WeilDefect.Arithmetic.ActualZetaCarrierAudit

namespace WeilDefect
noncomputable section
open ContinuousLinearMap InnerProductSpace Filter MeasureTheory FourierTransform
open scoped InnerProduct Topology BigOperators FourierTransform ComplexConjugate
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false
local instance : DecidableEq NeutralActualZetaDivisorCoordinate := Classical.decEq _

/-- A finite raw-copy coefficient packet. Copies remain available for exact
energy accounting; this definition does not count them as independent tests. -/
def neutralActualZetaFiniteCoefficients
    (t : Finset NeutralActualZetaDivisorCoordinate)
    (c : NeutralActualZetaDivisorCoordinate → ℂ) : NeutralActualZetaGreenCoefficients :=
  ∑ q ∈ t, lp.single 2 q (c q)

/-- The existing unshifted actual background quadratic evaluated on the
unchanged Green lift. No positivity or retained membership is presumed. -/
def neutralActualZetaGreenBackgroundTest (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (v : NeutralActualZetaGreenCoefficients) : ℝ :=
  neutralActualZetaEffectiveBackgroundQuadratic a s
    (neutralActualZetaGreenSourceLift a ha v)

theorem neutralActualZetaGreenBackgroundTest_hilbert (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenBackgroundTest a ha s v =
      ‖neutralActualZetaHilbertPositiveAnalysis a
        (neutralActualZetaGreenHilbertSourceContinuous a ha v)‖ ^ 2 -
      ‖neutralActualZetaHilbertBackgroundAnalysis a s
        (neutralActualZetaGreenHilbertSourceContinuous a ha v)‖ ^ 2 := by
  change neutralActualZetaEffectiveBackgroundQuadratic a s
    (neutralActualZetaGreenSourceLift a ha v) =
    neutralActualZetaEffectiveBackgroundQuadratic a s
      (neutralActualZetaHilbertToSource a
        (neutralActualZetaGreenHilbertSourceLift a ha v))
  rw [neutralActualZetaGreenHilbertSourceLift_custody]

theorem neutralActualZetaGreenBackgroundTest_continuous (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    Continuous (neutralActualZetaGreenBackgroundTest a ha s) := by
  have hp := ((neutralActualZetaHilbertPositiveAnalysis a).continuous.comp
    (neutralActualZetaGreenHilbertSourceContinuous a ha).continuous).norm.pow 2
  have hb := ((neutralActualZetaHilbertBackgroundAnalysis a s).continuous.comp
    (neutralActualZetaGreenHilbertSourceContinuous a ha).continuous).norm.pow 2
  have he : neutralActualZetaGreenBackgroundTest a ha s = fun v =>
      ‖neutralActualZetaHilbertPositiveAnalysis a
        (neutralActualZetaGreenHilbertSourceContinuous a ha v)‖ ^ 2 -
      ‖neutralActualZetaHilbertBackgroundAnalysis a s
        (neutralActualZetaGreenHilbertSourceContinuous a ha v)‖ ^ 2 :=
    funext (neutralActualZetaGreenBackgroundTest_hilbert a ha s)
  rw [he]
  exact hp.sub hb

/-- Positivity on the certified completion is exactly positivity on actual
Green lifts, by continuity in the full source graph topology. -/
theorem neutralActualZetaGreenBackground_nonnegative_iff_lifts
    (a : ℝ) (ha : 0 < a) (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∀ f : NeutralActualZetaGreenGraphDomain a ha,
      0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f.val)) ↔
    ∀ v : NeutralActualZetaGreenCoefficients,
      0 ≤ neutralActualZetaGreenBackgroundTest a ha s v := by
  constructor
  · intro h v
    have hv := h (CarrierAudit.observationMap
      (neutralActualZetaGreenHilbertSourceContinuous a ha) v)
    change 0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
      (neutralActualZetaHilbertToSource a
        (neutralActualZetaGreenHilbertSourceLift a ha v)) at hv
    rw [neutralActualZetaGreenHilbertSourceLift_custody] at hv
    exact hv
  · intro h f
    let Q : NeutralActualZetaHilbertSourceDomain a → ℝ := fun x =>
      ‖neutralActualZetaHilbertPositiveAnalysis a x‖ ^ 2 -
      ‖neutralActualZetaHilbertBackgroundAnalysis a s x‖ ^ 2
    have hQ : Continuous Q :=
      ((neutralActualZetaHilbertPositiveAnalysis a).continuous.norm.pow 2).sub
        ((neutralActualZetaHilbertBackgroundAnalysis a s).continuous.norm.pow 2)
    have hc : IsClosed {x : NeutralActualZetaHilbertSourceDomain a | 0 ≤ Q x} :=
      isClosed_le continuous_const hQ
    have hs : Set.range (neutralActualZetaGreenHilbertSourceContinuous a ha) ⊆
        {x : NeutralActualZetaHilbertSourceDomain a | 0 ≤ Q x} := by
      rintro x ⟨v, rfl⟩
      change 0 ≤ ‖neutralActualZetaHilbertPositiveAnalysis a
        (neutralActualZetaGreenHilbertSourceContinuous a ha v)‖ ^ 2 -
        ‖neutralActualZetaHilbertBackgroundAnalysis a s
          (neutralActualZetaGreenHilbertSourceContinuous a ha v)‖ ^ 2
      rw [← neutralActualZetaGreenBackgroundTest_hilbert]
      exact h v
    have hf : f.val ∈ closure
        (Set.range (neutralActualZetaGreenHilbertSourceContinuous a ha)) := f.property
    exact closure_minimal hs hc hf

/-- Finite raw-copy tests are sufficient for every actual coefficient vector.
The proof uses the certified l2 truncation limit, not copy-count observability. -/
theorem neutralActualZetaGreenBackground_lifts_iff_finite
    (a : ℝ) (ha : 0 < a) (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∀ v : NeutralActualZetaGreenCoefficients,
      0 ≤ neutralActualZetaGreenBackgroundTest a ha s v) ↔
    ∀ (t : Finset NeutralActualZetaDivisorCoordinate)
      (c : NeutralActualZetaDivisorCoordinate → ℂ),
      0 ≤ neutralActualZetaGreenBackgroundTest a ha s
        (neutralActualZetaFiniteCoefficients t c) := by
  constructor
  · intro h t c
    exact h _
  · intro h v
    have hv : Tendsto
        (fun t : Finset NeutralActualZetaDivisorCoordinate =>
          neutralActualZetaFiniteCoefficients t (fun q => v q))
        atTop (𝓝 v) := lp.hasSum_single ENNReal.ofNat_ne_top v
    have hq := (neutralActualZetaGreenBackgroundTest_continuous a ha s).continuousAt.tendsto.comp hv
    exact ge_of_tendsto hq (Eventually.of_forall fun t => h t (fun q => v q))

/-- Exact finite test criterion for the unique WD-T10 background contraction
on the relevant positive completion. No extra representation input remains. -/
theorem neutralActualZetaGreenBackground_factorization_iff_finite
    (a : ℝ) (ha : 0 < a) (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∃! T : NeutralActualZetaGreenPositiveEnergyCarrier a ha →L[ℂ]
        NeutralActualZetaGreenCoefficients,
      ‖T‖ ≤ 1 ∧ ∀ f,
        T (CarrierAudit.observationMap (neutralActualZetaGreenPositiveObservation a ha) f) =
          neutralActualZetaGreenBackgroundObservation a ha s f) ↔
    ∀ (t : Finset NeutralActualZetaDivisorCoordinate)
      (c : NeutralActualZetaDivisorCoordinate → ℂ),
      0 ≤ neutralActualZetaGreenBackgroundTest a ha s
        (neutralActualZetaFiniteCoefficients t c) :=
  (neutralActualZetaGreenBackground_factorization_iff a ha s).symm.trans
    ((neutralActualZetaGreenBackground_nonnegative_iff_lifts a ha s).trans
      (neutralActualZetaGreenBackground_lifts_iff_finite a ha s))

/-- Every failure has a finite actual-packet certificate, even if initially
detected only at a graph-completion vector. No such certificate is asserted. -/
theorem neutralActualZetaGreenBackground_negative_iff_finite
    (a : ℝ) (ha : 0 < a) (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∃ f : NeutralActualZetaGreenGraphDomain a ha,
      neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f.val) < 0) ↔
    ∃ (t : Finset NeutralActualZetaDivisorCoordinate)
      (c : NeutralActualZetaDivisorCoordinate → ℂ),
      neutralActualZetaGreenBackgroundTest a ha s
        (neutralActualZetaFiniteCoefficients t c) < 0 := by
  have h := (neutralActualZetaGreenBackground_nonnegative_iff_lifts a ha s).trans
    (neutralActualZetaGreenBackground_lifts_iff_finite a ha s)
  have hn := not_congr h
  push Not at hn
  exact hn

/-- No unit background factor exists exactly when a finite actual packet
has negative unshifted background energy. -/
theorem neutralActualZetaGreenBackground_no_factor_iff_finite_negative
    (a : ℝ) (ha : 0 < a) (s : Finset NeutralActualZetaDivisorCoordinate) :
    (¬ ∃ T : NeutralActualZetaGreenPositiveEnergyCarrier a ha →L[ℂ]
        NeutralActualZetaGreenCoefficients,
      ‖T‖ ≤ 1 ∧ ∀ f,
        T (CarrierAudit.observationMap (neutralActualZetaGreenPositiveObservation a ha) f) =
          neutralActualZetaGreenBackgroundObservation a ha s f) ↔
    ∃ (t : Finset NeutralActualZetaDivisorCoordinate)
      (c : NeutralActualZetaDivisorCoordinate → ℂ),
      neutralActualZetaGreenBackgroundTest a ha s
        (neutralActualZetaFiniteCoefficients t c) < 0 :=
  (CarrierAudit.no_contraction_iff_negative_witness
    (neutralActualZetaGreenPositiveObservation a ha)
    (neutralActualZetaGreenBackgroundObservation a ha s)).trans
      (neutralActualZetaGreenBackground_negative_iff_finite a ha s)

/-- The finite test is the already certified native multiplier-plus-pole
form plus exactly the selected negative energy, with raw multiplicity custody. -/
theorem neutralActualZetaGreenBackgroundTest_native (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenBackgroundTest a ha s v =
      (∫ ξ : ℝ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) +
      2 * (conj (sourceWindowMoment a (-(1/2)) (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a v)).re +
      (1 / 2 : ℝ) * ∑ q ∈ s,
        ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))‖ ^ 2 :=
  neutralActualZetaGreenEffectiveBackground_native a ha s v

end
end WeilDefect
