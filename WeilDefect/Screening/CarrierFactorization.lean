import WeilDefect.Screening.ResidualBudget
import Mathlib.Analysis.Normed.Operator.Extend

namespace WeilDefect.CarrierAudit
noncomputable section
open ContinuousLinearMap InnerProductSpace
open scoped InnerProduct ComplexOrder
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false

variable {D E F C : Type*}
variable [NormedAddCommGroup D] [InnerProductSpace ℂ D] [CompleteSpace D]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
variable [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
variable [NormedAddCommGroup C] [InnerProductSpace ℂ C] [CompleteSpace C]

/-- Completion for the observation seminorm, concretely realized as the
closed range. This does not use the original-domain quotient norm. -/
def observationClosure (A : D →L[ℂ] E) : ClosedSubmodule ℂ E :=
  ⟨A.range.topologicalClosure, A.range.isClosed_topologicalClosure⟩

abbrev ObservationCarrier (A : D →L[ℂ] E) := (observationClosure A).toSubmodule

instance observationCarrier_innerProduct (A : D →L[ℂ] E) :
    InnerProductSpace ℂ (ObservationCarrier A) :=
  Submodule.innerProductSpace (𝕜 := ℂ) (E := E) (observationClosure A).toSubmodule

instance observationCarrier_complete (A : D →L[ℂ] E) :
    CompleteSpace (ObservationCarrier A) :=
  (observationClosure A).isClosed.completeSpace_coe

/-- Same-vector observation map into its actual completed image. -/
def observationMap (A : D →L[ℂ] E) : D →L[ℂ] ObservationCarrier A :=
  A.codRestrict (observationClosure A).toSubmodule
    (fun f => A.range.le_topologicalClosure ⟨f, rfl⟩)

theorem observationMap_norm (A : D →L[ℂ] E) (f : D) :
    ‖observationMap A f‖ = ‖A f‖ := rfl

/-- Algebraic quotient identifies exactly the same-observation classes.
Its norm must be specified separately. -/
def quotientEquivRange (A : D →L[ℂ] E) :
    (D ⧸ A.ker) ≃ₗ[ℂ] A.range := A.toLinearMap.quotKerEquivRange

def quotientObservationNorm (A : D →L[ℂ] E) (q : D ⧸ A.ker) : ℝ :=
  ‖quotientEquivRange A q‖

theorem quotientObservationNorm_mk (A : D →L[ℂ] E) (f : D) :
    quotientObservationNorm A (Submodule.Quotient.mk f) = ‖A f‖ := by
  change ‖(A.toLinearMap.quotKerEquivRange (Submodule.Quotient.mk f) : E)‖ = ‖A f‖
  rw [LinearMap.quotKerEquivRange_apply_mk]

theorem observationMap_dense (A : D →L[ℂ] E) : DenseRange (observationMap A) := by
  intro y
  change y ∈ closure (Set.range (observationMap A))
  rw [IsInducing.subtypeVal.closure_eq_preimage_closure_image]
  have hi : ((↑) : ObservationCarrier A → E) '' Set.range (observationMap A) =
      Set.range A := by
    ext x
    constructor
    · rintro ⟨z, ⟨f, rfl⟩, rfl⟩
      exact ⟨f, rfl⟩
    · rintro ⟨f, rfl⟩
      exact ⟨observationMap A f, Set.mem_range_self f, rfl⟩
  rw [hi]
  exact y.property

/-- Kernel inclusion is exactly algebraic descent, with no assertion of
boundedness or positivity. -/
theorem kernel_iff_algebraic_descent (A : D →L[ℂ] E) (B : D →L[ℂ] F) :
    A.ker ≤ B.ker ↔
      ∃ L : (D ⧸ A.ker) →ₗ[ℂ] F, ∀ f : D, L (Submodule.Quotient.mk f) = B f := by
  constructor
  · intro h
    exact ⟨A.ker.liftQ B.toLinearMap h, fun f => rfl⟩
  · rintro ⟨L, hL⟩ f hf
    change B f = 0
    rw [← hL f, Submodule.Quotient.mk_eq_zero.mpr hf, L.map_zero]

theorem domination_kernel (A : D →L[ℂ] E) (B : D →L[ℂ] F)
    (h : ∀ f, ‖B f‖ ≤ ‖A f‖) : A.ker ≤ B.ker := by
  intro f hf
  change B f = 0
  apply norm_le_zero_iff.mp
  simpa only [hf, norm_zero] using h f

/-- Minimal completion theorem: unit domination is necessary and sufficient
for a unique contraction on the actual completed positive range.
No Douglas theorem premise or range-closedness premise is required. -/
theorem domination_iff_unique_contraction (A : D →L[ℂ] E) (B : D →L[ℂ] F) :
    (∀ f, ‖B f‖ ≤ ‖A f‖) ↔
      ∃! T : ObservationCarrier A →L[ℂ] F,
        ‖T‖ ≤ 1 ∧ ∀ f, T (observationMap A f) = B f := by
  constructor
  · intro h
    let T := B.toLinearMap.extendOfNorm (observationMap A).toLinearMap
    have hd : DenseRange (observationMap A).toLinearMap := observationMap_dense A
    have hb : ∀ f, ‖B.toLinearMap f‖ ≤ 1 * ‖(observationMap A).toLinearMap f‖ := by
      intro f
      simpa only [one_mul, observationMap_norm] using h f
    have hn : ‖T‖ ≤ 1 := LinearMap.opNorm_extendOfNorm_le hd zero_le_one hb
    have ht : ∀ f, T (observationMap A f) = B f :=
      fun f => LinearMap.extendOfNorm_eq hd ⟨1, hb⟩ f
    refine ⟨T, ⟨hn, ht⟩, ?_⟩
    intro U hU
    apply ContinuousLinearMap.ext
    have he := hd.equalizer U.continuous T.continuous
      (funext fun f => (hU.2 f).trans (ht f).symm)
    exact fun y => congrFun he y
  · rintro ⟨T, ⟨hn, ht⟩, _⟩ f
    rw [← ht f]
    exact (T.le_opNorm _).trans (by
      simpa only [one_mul, observationMap_norm] using
        mul_le_mul_of_nonneg_right hn (norm_nonneg (observationMap A f)))

/-- The operator inequality is the same unshifted domination test. -/
theorem domination_iff_covariance_order (A : D →L[ℂ] E) (B : D →L[ℂ] F) :
    (∀ f, ‖B f‖ ≤ ‖A f‖) ↔ B† ∘L B ≤ A† ∘L A := by
  have hi (f : D) :
      ((A† ∘L A - B† ∘L B).reApplyInnerSelf f) =
        ‖A f‖ ^ 2 - ‖B f‖ ^ 2 := by
    simp only [ContinuousLinearMap.reApplyInnerSelf_apply, sub_apply, comp_apply,
      inner_sub_left, adjoint_inner_left, inner_self_eq_norm_sq_to_K,
      Complex.sub_re, Complex.ofReal_re]
  rw [ContinuousLinearMap.le_def, ContinuousLinearMap.isPositive_def']
  have hs : IsSelfAdjoint (A† ∘L A - B† ∘L B) :=
    (ContinuousLinearMap.isPositive_adjoint_comp_self A).isSelfAdjoint.sub
      (ContinuousLinearMap.isPositive_adjoint_comp_self B).isSelfAdjoint
  constructor
  · intro h
    refine ⟨hs, fun f => ?_⟩
    rw [hi]
    nlinarith [h f, norm_nonneg (A f), norm_nonneg (B f)]
  · rintro ⟨_, h⟩ f
    have hf := h f
    rw [hi] at hf
    nlinarith [norm_nonneg (A f), norm_nonneg (B f)]

/-- Positivity is exactly the missing input; a failing vector rules out
every induced contraction on the positive completion. -/
theorem no_contraction_iff_negative_witness (A : D →L[ℂ] E) (B : D →L[ℂ] F) :
    (¬ ∃ T : ObservationCarrier A →L[ℂ] F,
      ‖T‖ ≤ 1 ∧ ∀ f, T (observationMap A f) = B f) ↔
    ∃ f, ‖A f‖ ^ 2 - ‖B f‖ ^ 2 < 0 := by
  classical
  have he : (∃ T : ObservationCarrier A →L[ℂ] F,
      ‖T‖ ≤ 1 ∧ ∀ f, T (observationMap A f) = B f) ↔ ∀ f, ‖B f‖ ≤ ‖A f‖ := by
    constructor
    · rintro ⟨T, hn, ht⟩ f
      rw [← ht f]
      exact (T.le_opNorm _).trans (by
        simpa only [one_mul, observationMap_norm] using
          mul_le_mul_of_nonneg_right hn (norm_nonneg (observationMap A f)))
    · intro h
      exact ((domination_iff_unique_contraction A B).mp h).exists
  rw [he, not_forall]
  constructor
  · rintro ⟨f, hf⟩
    exact ⟨f, by nlinarith [lt_of_not_ge hf, norm_nonneg (A f), norm_nonneg (B f)]⟩
  · rintro ⟨f, hf⟩
    exact ⟨f, by nlinarith [norm_nonneg (A f), norm_nonneg (B f)]⟩

/-- Completing in the observation norm need not preserve the original
domain norm. A bounded inverse exists exactly when coercivity is proved. -/
theorem bounded_inverse_iff_coercivity (A : D →L[ℂ] E) :
    (∃ T : ObservationCarrier A →L[ℂ] D, ∀ f, T (observationMap A f) = f) ↔
      ∃ c : ℝ, ∀ f, ‖f‖ ≤ c * ‖A f‖ := by
  constructor
  · rintro ⟨T, ht⟩
    exact ⟨‖T‖, fun f => by
      simpa only [ht f, observationMap_norm] using T.le_opNorm (observationMap A f)⟩
  · rintro ⟨c, hc⟩
    have hd : DenseRange (observationMap A).toLinearMap := observationMap_dense A
    have hb : ∀ f, ‖(LinearMap.id : D →ₗ[ℂ] D) f‖ ≤
        c * ‖(observationMap A).toLinearMap f‖ := by
      simpa only [LinearMap.id_apply, observationMap_norm] using hc
    exact ⟨(LinearMap.id : D →ₗ[ℂ] D).extendOfNorm (observationMap A).toLinearMap,
      fun f => LinearMap.extendOfNorm_eq hd ⟨c, hb⟩ f⟩

/-- Observational synthesis quotient and positive quotient have nested
kernels, with equality requiring positive injectivity on the synthesis range. -/
theorem synthesis_positive_kernel_comparison (G : C →L[ℂ] D) (A : D →L[ℂ] E) :
    G.ker ≤ (A.comp G).ker ∧
      (G.ker = (A.comp G).ker ↔ ∀ v, A (G v) = 0 → G v = 0) := by
  have hk : G.ker ≤ (A.comp G).ker := by
    intro v hv
    change A (G v) = 0
    rw [hv, A.map_zero]
  refine ⟨hk, ?_⟩
  constructor
  · intro he v hv
    have hm : v ∈ (A.comp G).ker := hv
    rw [← he] at hm
    exact hm
  · intro h
    apply le_antisymm hk
    intro v hv
    exact h v hv

/-- Actual adjoint translation to WD-T10, preserving all same-domain vectors
and deriving the factor rather than assuming a Douglas representation. -/
theorem domination_gives_wdt10_factor (A : D →L[ℂ] E) (B : D →L[ℂ] F)
    (h : ∀ f, ‖B f‖ ≤ ‖A f‖) :
    ∃ X : F →L[ℂ] ObservationCarrier A,
      ‖X‖ ≤ 1 ∧ B† = -((observationMap A)† ∘L X) ∧
      (observationMap A)† ∘L observationMap A - B† ∘L B =
        WDT10.effectivePositive (observationMap A)† X ∘L
          (WDT10.effectivePositive (observationMap A)† X)† := by
  obtain ⟨T, ⟨hn, ht⟩, _⟩ := (domination_iff_unique_contraction A B).mp h
  have hb : B = T.comp (observationMap A) :=
    ContinuousLinearMap.ext (fun f => (ht f).symm)
  have hadj := congrArg (fun U : D →L[ℂ] F => U†) hb
  simp only [adjoint_comp] at hadj
  have hx : ‖-T†‖ ≤ 1 := by
    simpa only [norm_neg, ContinuousLinearMap.adjoint.norm_map] using hn
  have hfac : B† = -((observationMap A)† ∘L (-T†)) := by
    simpa only [comp_neg, neg_neg] using hadj
  refine ⟨-T†, hx, hfac, ?_⟩
  simpa only [adjoint_adjoint] using
    WDT10.wd_t10_background_covariance_elimination (observationMap A)† B† (-T†) hx hfac

/-- Kernel inclusion alone cannot buy a unit background budget. -/
theorem kernel_inclusion_not_domination :
    let A : ℂ →L[ℂ] ℂ := ContinuousLinearMap.id ℂ ℂ
    let B : ℂ →L[ℂ] ℂ := (2 : ℂ) • ContinuousLinearMap.id ℂ ℂ
    A.ker ≤ B.ker ∧ ¬ (∀ f, ‖B f‖ ≤ ‖A f‖) := by
  dsimp
  constructor
  · intro f hf
    change (2 : ℂ) • f = 0
    rw [show f = 0 from hf, smul_zero]
  · intro h
    have hh := h (1 : ℂ)
    norm_num [ContinuousLinearMap.smul_apply, ContinuousLinearMap.id_apply, norm_smul] at hh

end
end WeilDefect.CarrierAudit
