import WeilDefect.MasterRecon.V08F
import Mathlib.MeasureTheory.Function.LpSpace.Indicator
import Mathlib.MeasureTheory.Function.L2Space

/-! V08G: zero extension of compact band operators to the full
frequency L² space, with an exact spectral squared tail identity.
No physical Plancherel assertion is made here. -/
namespace WeilDefect.MasterRecon.V08G

open MeasureTheory Set Filter
open scoped ENNReal Topology

abbrev Band := V08E.Band
local instance bandCompact (R : ℝ) : CompactSpace (Band R) :=
  compactSpace_Icc (-R) R

noncomputable def clampBand (R : ℝ) (hR : 0 ≤ R) (u : ℝ) : Band R :=
  ⟨max (-R) (min R u), le_max_left _ _,
    max_le (by linarith) (min_le_left _ _)⟩

theorem clampBand_continuous (R : ℝ) (hR : 0 ≤ R) :
    Continuous (clampBand R hR) := by
  apply Continuous.subtype_mk
  fun_prop

theorem clampBand_eq (R : ℝ) (hR : 0 ≤ R) (u : ℝ)
    (hu : u ∈ Set.Icc (-R) R) :
    (clampBand R hR u : ℝ) = u := by
  change max (-R) (min R u) = u
  rw [min_eq_right hu.2, max_eq_right hu.1]

noncomputable def zeroBand (R : ℝ) (hR : 0 ≤ R) (g : C(Band R, ℂ)) : ℝ → ℂ :=
  (Set.Icc (-R) R).indicator (fun u => g (clampBand R hR u))

theorem zeroBand_mem (ν : Measure ℝ) (R : ℝ) (hR : 0 ≤ R)
    (hν : ν (Set.Icc (-R) R) ≠ ∞) (g : C(Band R, ℂ)) :
    MemLp (zeroBand R hR g) 2 ν := by
  letI : IsFiniteMeasure (ν.restrict (Set.Icc (-R) R)) :=
    ⟨by rw [Measure.restrict_apply_univ]; exact lt_top_iff_ne_top.mpr hν⟩
  unfold zeroBand
  apply (memLp_indicator_iff_restrict measurableSet_Icc).2
  apply MemLp.of_bound (g.continuous.comp (clampBand_continuous R hR)).aestronglyMeasurable ‖g‖
  exact Eventually.of_forall fun u => g.norm_coe_le_norm _

noncomputable def zeroBandValue (ν : Measure ℝ) (R : ℝ) (hR : 0 ≤ R)
    (hν : ν (Set.Icc (-R) R) ≠ ∞) (g : C(Band R, ℂ)) : Lp ℂ 2 ν :=
  (zeroBand_mem ν R hR hν g).toLp (zeroBand R hR g)

theorem zeroBandValue_ae (ν : Measure ℝ) (R : ℝ) (hR : 0 ≤ R)
    (hν : ν (Set.Icc (-R) R) ≠ ∞) (g : C(Band R, ℂ)) :
    (zeroBandValue ν R hR hν g : ℝ → ℂ) =ᵐ[ν] zeroBand R hR g :=
  MemLp.coeFn_toLp (zeroBand_mem ν R hR hν g)

theorem zeroBandValue_bound (ν : Measure ℝ) (R : ℝ) (hR : 0 ≤ R)
    (hν : ν (Set.Icc (-R) R) ≠ ∞) (g : C(Band R, ℂ)) :
    ‖zeroBandValue ν R hR hν g‖ ≤
      (ν.real (Set.Icc (-R) R)) ^ (1 / (2 : ℝ≥0∞).toReal) * ‖g‖ := by
  let k : Lp ℂ 2 ν := indicatorConstLp 2 measurableSet_Icc hν (‖g‖ : ℂ)
  have h : ‖zeroBandValue ν R hR hν g‖ ≤ ‖k‖ := by
    apply Lp.norm_le_norm_of_ae_le
    filter_upwards [zeroBandValue_ae ν R hR hν g,
      (indicatorConstLp_coeFn (p := 2) (hs := measurableSet_Icc) (hμs := hν)
        (c := (‖g‖ : ℂ)))] with u hu hk
    change ‖zeroBandValue ν R hR hν g u‖ ≤ ‖k u‖
    rw [hu, show k u = _ from hk]
    unfold zeroBand
    by_cases hmem : u ∈ Set.Icc (-R) R
    · simp only [Set.indicator_of_mem hmem, Complex.norm_real, Real.norm_eq_abs,
        abs_of_nonneg (norm_nonneg g)]
      exact g.norm_coe_le_norm _
    · simp [Set.indicator_of_notMem hmem]
  have hk : ‖k‖ ≤ ‖(‖g‖ : ℂ)‖ * ν.real (Set.Icc (-R) R) ^ (1 / (2 : ℝ≥0∞).toReal) :=
    norm_indicatorConstLp_le
  refine h.trans (hk.trans_eq ?_)
  simp [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (norm_nonneg g), mul_comm]

noncomputable def zeroBandCLM (ν : Measure ℝ) (R : ℝ) (hR : 0 ≤ R)
    (hν : ν (Set.Icc (-R) R) ≠ ∞) : C(Band R, ℂ) →L[ℂ] Lp ℂ 2 ν :=
  ({
    toFun := zeroBandValue ν R hR hν
    map_add' := fun f g => by
      apply Lp.ext
      filter_upwards [zeroBandValue_ae ν R hR hν (f + g),
        zeroBandValue_ae ν R hR hν f, zeroBandValue_ae ν R hR hν g,
        Lp.coeFn_add (zeroBandValue ν R hR hν f) (zeroBandValue ν R hR hν g)]
        with u h₁ h₂ h₃ h₄
      change zeroBandValue ν R hR hν (f + g) u =
        (zeroBandValue ν R hR hν f + zeroBandValue ν R hR hν g) u
      rw [h₁, show (zeroBandValue ν R hR hν f + zeroBandValue ν R hR hν g) u =
        zeroBandValue ν R hR hν f u + zeroBandValue ν R hR hν g u from h₄, h₂, h₃]
      unfold zeroBand
      by_cases hu : u ∈ Set.Icc (-R) R <;> simp [hu]
    map_smul' := fun c f => by
      apply Lp.ext
      filter_upwards [zeroBandValue_ae ν R hR hν (c • f),
        zeroBandValue_ae ν R hR hν f, Lp.coeFn_smul c (zeroBandValue ν R hR hν f)]
        with u h₁ h₂ h₃
      change zeroBandValue ν R hR hν (c • f) u = (c • zeroBandValue ν R hR hν f) u
      rw [h₁, show (c • zeroBandValue ν R hR hν f) u =
        c * zeroBandValue ν R hR hν f u from h₃, h₂]
      unfold zeroBand
      by_cases hu : u ∈ Set.Icc (-R) R <;> simp [hu, smul_eq_mul]
  } : C(Band R, ℂ) →ₗ[ℂ] Lp ℂ 2 ν).mkContinuous
    ((ν.real (Set.Icc (-R) R)) ^ (1 / (2 : ℝ≥0∞).toReal))
    (zeroBandValue_bound ν R hR hν)

noncomputable def fullBandFourier (μ : Measure ℝ) [IsFiniteMeasure μ]
    (ν : Measure ℝ) (t R : ℝ) (ht0 : 0 ≤ t) (hR : 0 ≤ R)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (hν : ν (Set.Icc (-R) R) ≠ ∞) :
    V08F.PhysicalL2 μ →L[ℂ] Lp ℂ 2 ν :=
  (zeroBandCLM ν R hR hν).comp
    ((V08E.boundedFourier μ t R ht0 ht).comp (V08F.physicalL1Inclusion μ))

theorem fullBandFourier_compact (μ : Measure ℝ) [IsFiniteMeasure μ]
    (ν : Measure ℝ) (t R : ℝ) (ht0 : 0 ≤ t) (hR : 0 ≤ R)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (hν : ν (Set.Icc (-R) R) ≠ ∞) :
    IsCompactOperator (fullBandFourier μ ν t R ht0 hR ht hν) := by
  have h := V08E.boundedFourier_compact μ t R ht0 hR ht
  exact (h.comp_clm (V08F.physicalL1Inclusion μ)).clm_comp (zeroBandCLM ν R hR hν)

theorem fullBandFourier_ae (μ : Measure ℝ) [IsFiniteMeasure μ]
    (ν : Measure ℝ) (t R : ℝ) (ht0 : 0 ≤ t) (hR : 0 ≤ R)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (hν : ν (Set.Icc (-R) R) ≠ ∞)
    (f : V08F.PhysicalL2 μ) :
    (fullBandFourier μ ν t R ht0 hR ht hν f : ℝ → ℂ) =ᵐ[ν]
      (Set.Icc (-R) R).indicator (fun u => ∫ x, V08D.fourierKernel u x * f x ∂μ) := by
  let g := V08F.physicalL1Inclusion μ f
  let F := V08E.boundedFourier μ t R ht0 ht g
  change (zeroBandValue ν R hR hν F : ℝ → ℂ) =ᵐ[ν] _
  refine (zeroBandValue_ae ν R hR hν F).trans ?_
  filter_upwards with u
  unfold zeroBand
  by_cases hu : u ∈ Set.Icc (-R) R
  · rw [Set.indicator_of_mem hu, Set.indicator_of_mem hu]
    change V08E.boundedFourier μ t R ht0 ht g (clampBand R hR u) = _
    rw [V08E.boundedFourier_integral μ t R ht0 hR ht, clampBand_eq R hR u hu]
    apply integral_congr_ae
    filter_upwards [V08F.physicalL1Inclusion_ae μ f] with x hx
    change V08D.fourierKernel u x * g x = _
    rw [show g x = f x from hx]
  · simp [Set.indicator_of_notMem hu]

theorem l2_norm_sq_integral (ν : Measure ℝ) (f : Lp ℂ 2 ν) :
    ‖f‖ ^ 2 = ∫ u, ‖f u‖ ^ 2 ∂ν := by
  have h := inner_self_eq_norm_sq (𝕜 := ℂ) f
  rw [L2.inner_def, ← integral_re (L2.integrable_inner (𝕜 := ℂ) f f)] at h
  simpa only [inner_self_eq_norm_sq] using h.symm

theorem spectral_tail_identity (ν : Measure ℝ) (R : ℝ)
    (F : ℝ → ℂ) (a b : Lp ℂ 2 ν)
    (ha : (a : ℝ → ℂ) =ᵐ[ν] F)
    (hb : (b : ℝ → ℂ) =ᵐ[ν] (Set.Icc (-R) R).indicator F) :
    ‖a - b‖ ^ 2 = ∫ u in {u : ℝ | R < |u|}, ‖F u‖ ^ 2 ∂ν := by
  have hs : MeasurableSet {u : ℝ | R < |u|} :=
    measurableSet_lt measurable_const measurable_id.abs
  rw [l2_norm_sq_integral, ← integral_indicator hs]
  apply integral_congr_ae
  filter_upwards [Lp.coeFn_sub a b, ha, hb] with u h₁ h₂ h₃
  change ‖(a - b) u‖ ^ 2 = _
  rw [show (a - b) u = a u - b u from h₁, h₂, h₃]
  by_cases hu : u ∈ Set.Icc (-R) R
  · have hnot : u ∉ {u : ℝ | R < |u|} :=
      fun h => (not_lt_of_ge (abs_le.mpr hu)) h
    simp [Set.indicator_of_mem hu, Set.indicator_of_notMem hnot]
  · have ht : u ∈ {u : ℝ | R < |u|} := by
      change R < |u|
      exact lt_of_not_ge (fun h => hu (abs_le.mp h))
    simp [Set.indicator_of_notMem hu, Set.indicator_of_mem ht]

end WeilDefect.MasterRecon.V08G

#print axioms WeilDefect.MasterRecon.V08G.clampBand_continuous
#print axioms WeilDefect.MasterRecon.V08G.clampBand_eq
#print axioms WeilDefect.MasterRecon.V08G.zeroBand_mem
#print axioms WeilDefect.MasterRecon.V08G.zeroBandValue_ae
#print axioms WeilDefect.MasterRecon.V08G.zeroBandValue_bound
#print axioms WeilDefect.MasterRecon.V08G.fullBandFourier_compact
#print axioms WeilDefect.MasterRecon.V08G.fullBandFourier_ae
#print axioms WeilDefect.MasterRecon.V08G.l2_norm_sq_integral
#print axioms WeilDefect.MasterRecon.V08G.spectral_tail_identity
