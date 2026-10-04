import WeilDefect.Screening.CarrierFactorization
import WeilDefect.Arithmetic.ActualZetaGreenCopyObservability

namespace WeilDefect
noncomputable section
open ContinuousLinearMap InnerProductSpace CarrierAudit
open scoped InnerProduct ComplexOrder
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false

/-- Actual Green observation completion uses the graph-image seminorm,
keeping the raw coefficient space available separately for energy accounting. -/
abbrev NeutralActualZetaObservationCarrier (a : ℝ) (ha : 0 < a) :=
  ObservationCarrier (neutralActualZetaGreenHilbertSourceContinuous a ha)

/-- WD-T10's actual positive-energy completion on the lawful full source graph. -/
abbrev NeutralActualZetaPositiveEnergyCarrier (a : ℝ) :=
  ObservationCarrier (neutralActualZetaHilbertPositiveAnalysis a)

/-- Positive energy restricted to the already certified Green graph domain. -/
def neutralActualZetaGreenPositiveObservation (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaGreenGraphDomain a ha →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (neutralActualZetaHilbertPositiveAnalysis a).comp
    (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule.subtypeL

abbrev NeutralActualZetaGreenPositiveEnergyCarrier (a : ℝ) (ha : 0 < a) :=
  ObservationCarrier (neutralActualZetaGreenPositiveObservation a ha)

/-- Background restricted to the same certified Green graph domain. -/
def neutralActualZetaGreenBackgroundObservation (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaGreenGraphDomain a ha →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (neutralActualZetaHilbertBackgroundAnalysis a s).comp
    (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule.subtypeL

/-- The graph-observation completion is exactly the existing certified Green
closed submodule, not the entire source graph. -/
theorem neutralActualZetaObservationClosure_eq (a : ℝ) (ha : 0 < a) :
    observationClosure (neutralActualZetaGreenHilbertSourceContinuous a ha) =
      neutralActualZetaGreenClosedSubmodule a ha := rfl

theorem neutralActualZetaPositiveQuotient_norm (a : ℝ)
    (f : NeutralActualZetaHilbertSourceDomain a) :
    quotientObservationNorm (neutralActualZetaHilbertPositiveAnalysis a)
      (Submodule.Quotient.mk f) = ‖neutralActualZetaHilbertPositiveAnalysis a f‖ :=
  quotientObservationNorm_mk _ _

/-- Exact two-stage quotient obstruction before completion. No injectivity
of positive observations on actual Green vectors is inferred. -/
theorem neutralActualZetaSynthesis_positive_kernel_comparison (a : ℝ) (ha : 0 < a) :
    (neutralActualZetaGreenHilbertSourceContinuous a ha).ker ≤
      ((neutralActualZetaHilbertPositiveAnalysis a).comp
        (neutralActualZetaGreenHilbertSourceContinuous a ha)).ker ∧
    ((neutralActualZetaGreenHilbertSourceContinuous a ha).ker =
      ((neutralActualZetaHilbertPositiveAnalysis a).comp
        (neutralActualZetaGreenHilbertSourceContinuous a ha)).ker ↔
      ∀ v : NeutralActualZetaGreenCoefficients,
        neutralActualZetaHilbertPositiveAnalysis a
          (neutralActualZetaGreenHilbertSourceLift a ha v) = 0 →
        neutralActualZetaGreenHilbertSourceLift a ha v = 0) :=
  synthesis_positive_kernel_comparison _ _

/-- Same-vector recovery from the positive completion is equivalent to a
new positive-energy lower bound in the full Green graph norm. -/
theorem neutralActualZetaGreenPositive_recovery_iff (a : ℝ) (ha : 0 < a) :
    (∃ T : NeutralActualZetaGreenPositiveEnergyCarrier a ha →L[ℂ]
        NeutralActualZetaGreenGraphDomain a ha,
      ∀ f, T (observationMap (neutralActualZetaGreenPositiveObservation a ha) f) = f) ↔
    ∃ c : ℝ, ∀ f : NeutralActualZetaGreenGraphDomain a ha,
      ‖f‖ ≤ c * ‖neutralActualZetaHilbertPositiveAnalysis a f.val‖ :=
  bounded_inverse_iff_coercivity _

/-- Exact actual positivity test: no shifted mass term is included. -/
theorem neutralActualZetaBackground_domination_iff_nonnegative (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∀ f : NeutralActualZetaHilbertSourceDomain a,
      ‖neutralActualZetaHilbertBackgroundAnalysis a s f‖ ≤
        ‖neutralActualZetaHilbertPositiveAnalysis a f‖) ↔
    ∀ f : NeutralActualZetaHilbertSourceDomain a,
      0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f) := by
  change (∀ f, ‖neutralActualZetaHilbertBackgroundAnalysis a s f‖ ≤
    ‖neutralActualZetaHilbertPositiveAnalysis a f‖) ↔
    ∀ f, 0 ≤ ‖neutralActualZetaHilbertPositiveAnalysis a f‖ ^ 2 -
      ‖neutralActualZetaHilbertBackgroundAnalysis a s f‖ ^ 2
  constructor
  · intro h f
    nlinarith [h f, norm_nonneg (neutralActualZetaHilbertPositiveAnalysis a f),
      norm_nonneg (neutralActualZetaHilbertBackgroundAnalysis a s f)]
  · intro h f
    nlinarith [h f, norm_nonneg (neutralActualZetaHilbertPositiveAnalysis a f),
      norm_nonneg (neutralActualZetaHilbertBackgroundAnalysis a s f)]

theorem neutralActualZetaBackground_domination_iff_order (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∀ f : NeutralActualZetaHilbertSourceDomain a,
      ‖neutralActualZetaHilbertBackgroundAnalysis a s f‖ ≤
        ‖neutralActualZetaHilbertPositiveAnalysis a f‖) ↔
    (neutralActualZetaHilbertBackgroundAnalysis a s)† ∘L
        neutralActualZetaHilbertBackgroundAnalysis a s ≤
      (neutralActualZetaHilbertPositiveAnalysis a)† ∘L
        neutralActualZetaHilbertPositiveAnalysis a :=
  domination_iff_covariance_order _ _

/-- The actual positive completion admits the background contraction exactly
when the actual unshifted effective-background form is nonnegative. -/
theorem neutralActualZetaBackground_factorization_iff (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∀ f : NeutralActualZetaHilbertSourceDomain a,
      0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f)) ↔
    ∃! T : NeutralActualZetaPositiveEnergyCarrier a →L[ℂ] NeutralActualZetaGreenCoefficients,
      ‖T‖ ≤ 1 ∧ ∀ f,
        T (observationMap (neutralActualZetaHilbertPositiveAnalysis a) f) =
          neutralActualZetaHilbertBackgroundAnalysis a s f :=
  (neutralActualZetaBackground_domination_iff_nonnegative a s).symm.trans
    (domination_iff_unique_contraction _ _)

/-- Failure is witnessed by an actual lawful graph vector with strictly
negative unshifted background form, not by a missing representation wrapper. -/
theorem neutralActualZetaBackground_no_factor_iff_negative (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    (¬ ∃ T : NeutralActualZetaPositiveEnergyCarrier a →L[ℂ] NeutralActualZetaGreenCoefficients,
      ‖T‖ ≤ 1 ∧ ∀ f,
        T (observationMap (neutralActualZetaHilbertPositiveAnalysis a) f) =
          neutralActualZetaHilbertBackgroundAnalysis a s f) ↔
    ∃ f : NeutralActualZetaHilbertSourceDomain a,
      neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f) < 0 :=
  no_contraction_iff_negative_witness _ _

/-- Exact kernel obligation follows from the required positivity test. -/
theorem neutralActualZetaBackground_kernel_of_nonnegative (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (h : ∀ f : NeutralActualZetaHilbertSourceDomain a,
      0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f)) :
    (neutralActualZetaHilbertPositiveAnalysis a).ker ≤
      (neutralActualZetaHilbertBackgroundAnalysis a s).ker :=
  domination_kernel _ _ ((neutralActualZetaBackground_domination_iff_nonnegative a s).mpr h)

/-- Actual WD-T10 input and effective covariance are constructed from the
precisely isolated positivity hypothesis, with the same lawful domain and no
retained-vector, density, simplicity or spectral-operator assumptions. -/
theorem neutralActualZetaBackground_wdt10_of_nonnegative (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (h : ∀ f : NeutralActualZetaHilbertSourceDomain a,
      0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f)) :
    ∃ X : NeutralActualZetaGreenCoefficients →L[ℂ] NeutralActualZetaPositiveEnergyCarrier a,
      ‖X‖ ≤ 1 ∧
      (neutralActualZetaHilbertBackgroundAnalysis a s)† =
        -((observationMap (neutralActualZetaHilbertPositiveAnalysis a))† ∘L X) ∧
      (observationMap (neutralActualZetaHilbertPositiveAnalysis a))† ∘L
          observationMap (neutralActualZetaHilbertPositiveAnalysis a) -
        (neutralActualZetaHilbertBackgroundAnalysis a s)† ∘L
          neutralActualZetaHilbertBackgroundAnalysis a s =
        WDT10.effectivePositive
            ((observationMap (neutralActualZetaHilbertPositiveAnalysis a))†) X ∘L
          (WDT10.effectivePositive
            ((observationMap (neutralActualZetaHilbertPositiveAnalysis a))†) X)† :=
  domination_gives_wdt10_factor _ _
    ((neutralActualZetaBackground_domination_iff_nonnegative a s).mpr h)

/-- Positive coefficient completion preserves the actual signed source
operator, hence every same-domain null equation. No retained membership is used. -/
theorem neutralActualZetaPositiveCarrier_source_operator (a : ℝ) :
    neutralActualZetaHilbertSourceOperator a =
      (observationMap (neutralActualZetaHilbertPositiveAnalysis a))† ∘L
        observationMap (neutralActualZetaHilbertPositiveAnalysis a) -
      (neutralActualZetaHilbertNegativeAnalysis a)† ∘L
        neutralActualZetaHilbertNegativeAnalysis a := by
  rw [observation_covariance]
  rfl

/-- Minimal relevant-domain version: background contraction on the Green
positive completion is equivalent to unshifted positivity only on that graph. -/
theorem neutralActualZetaGreenBackground_factorization_iff (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    (∀ f : NeutralActualZetaGreenGraphDomain a ha,
      0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f.val)) ↔
    ∃! T : NeutralActualZetaGreenPositiveEnergyCarrier a ha →L[ℂ]
        NeutralActualZetaGreenCoefficients,
      ‖T‖ ≤ 1 ∧ ∀ f,
        T (observationMap (neutralActualZetaGreenPositiveObservation a ha) f) =
          neutralActualZetaGreenBackgroundObservation a ha s f := by
  have he :
      (∀ f : NeutralActualZetaGreenGraphDomain a ha,
        0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
          (neutralActualZetaHilbertToSource a f.val)) ↔
      ∀ f : NeutralActualZetaGreenGraphDomain a ha,
        ‖neutralActualZetaGreenBackgroundObservation a ha s f‖ ≤
          ‖neutralActualZetaGreenPositiveObservation a ha f‖ := by
    change (∀ f : NeutralActualZetaGreenGraphDomain a ha,
      0 ≤ ‖neutralActualZetaGreenPositiveObservation a ha f‖ ^ 2 -
        ‖neutralActualZetaGreenBackgroundObservation a ha s f‖ ^ 2) ↔ _
    constructor
    · intro h f
      nlinarith [h f, norm_nonneg (neutralActualZetaGreenPositiveObservation a ha f),
        norm_nonneg (neutralActualZetaGreenBackgroundObservation a ha s f)]
    · intro h f
      nlinarith [h f, norm_nonneg (neutralActualZetaGreenPositiveObservation a ha f),
        norm_nonneg (neutralActualZetaGreenBackgroundObservation a ha s f)]
  exact he.trans (domination_iff_unique_contraction _ _)

set_option backward.isDefEq.respectTransparency true in
/-- After the exact positivity test, WD-T10 factors the actual background
operator itself, not merely a replacement representation. -/
theorem neutralActualZetaBackground_operator_wdt10 (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (h : ∀ f : NeutralActualZetaHilbertSourceDomain a,
      0 ≤ neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f)) :
    ∃ X : NeutralActualZetaGreenCoefficients →L[ℂ] NeutralActualZetaPositiveEnergyCarrier a,
      ‖X‖ ≤ 1 ∧
      (neutralActualZetaHilbertBackgroundAnalysis a s)† =
        -((observationMap (neutralActualZetaHilbertPositiveAnalysis a))† ∘L X) ∧
      neutralActualZetaHilbertBackgroundOperator a s =
        WDT10.effectivePositive
            ((observationMap (neutralActualZetaHilbertPositiveAnalysis a))†) X ∘L
          (WDT10.effectivePositive
            ((observationMap (neutralActualZetaHilbertPositiveAnalysis a))†) X)† := by
  apply Exists.imp _ (neutralActualZetaBackground_wdt10_of_nonnegative a s h)
  intro X hX
  refine ⟨hX.1, hX.2.1, ?_⟩
  have hc := hX.2.2
  rw [observation_covariance] at hc
  exact hc

end
end WeilDefect
