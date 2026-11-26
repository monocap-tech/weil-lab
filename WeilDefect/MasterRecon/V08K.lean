import WeilDefect.MasterRecon.V08J
import WeilDefect.MasterRecon.V08C

/-! V08K: compactness of the actual supported logarithmic physical
inclusion, using the certified compact band integral and Plancherel. -/
namespace WeilDefect.MasterRecon.V08K

open MeasureTheory Set Filter
open scoped ENNReal Topology FourierTransform
open V08I

noncomputable abbrev FullL2 := V08I.FullL2
abbrev Band := V08E.Band
local instance bandCompact (R : ℝ) : CompactSpace (Band R) :=
  compactSpace_Icc (-R) R

noncomputable def supportMeasure (t : ℝ) : Measure ℝ :=
  volume.restrict (Set.Icc (-t) t)

noncomputable instance supportMeasure_finite (t : ℝ) : IsFiniteMeasure (supportMeasure t) :=
  ⟨by unfold supportMeasure
      rw [Measure.restrict_apply_univ]
      exact isCompact_Icc.measure_lt_top⟩

theorem supportMeasure_bound (t : ℝ) :
    ∀ᵐ x ∂supportMeasure t, |x| ≤ t := by
  exact (ae_restrict_mem measurableSet_Icc).mono fun _ hx => abs_le.mpr hx

noncomputable def restrictPhysical (t : ℝ) :
    FullL2 →L[ℂ] V08F.PhysicalL2 (supportMeasure t) :=
  LpToLpRestrictCLM ℝ ℂ ℂ volume 2 (Set.Icc (-t) t)

theorem restrictPhysical_ae (t : ℝ) (f : FullL2) :
    (restrictPhysical t f : ℝ → ℂ) =ᵐ[supportMeasure t] f :=
  LpToLpRestrictCLM_coeFn ℂ (Set.Icc (-t) t) f

theorem supported_integrable (t : ℝ) (f : FullL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-t) t → f x = 0) :
    Integrable (fun x : ℝ => f x) := by
  have h : MemLp (fun x : ℝ => f x) 1 (supportMeasure t) :=
    ((Lp.memLp f).restrict (Set.Icc (-t) t)).mono_exponent (by norm_num)
  have hi := (memLp_indicator_iff_restrict measurableSet_Icc).2 h
  apply (memLp_one_iff_integrable.mp hi).congr
  filter_upwards [hs] with x hx
  by_cases hmem : x ∈ Set.Icc (-t) t
  · simp [Set.indicator_of_mem hmem]
  · simp [Set.indicator_of_notMem hmem, hx hmem]

theorem restricted_angular_integral (t : ℝ) (f : FullL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-t) t → f x = 0) (u : ℝ) :
    (∫ x, V08D.fourierKernel u x * restrictPhysical t f x ∂supportMeasure t) =
      V08H.angularFourier (f : ℝ → ℂ) u := by
  calc
    _ = ∫ x, V08D.fourierKernel u x * f x ∂supportMeasure t := by
      apply integral_congr_ae
      filter_upwards [restrictPhysical_ae t f] with x hx
      rw [hx]
    _ = _ := by
      unfold supportMeasure V08H.angularFourier
      rw [← integral_indicator measurableSet_Icc]
      apply integral_congr_ae
      filter_upwards [hs] with x hx
      by_cases hmem : x ∈ Set.Icc (-t) t
      · simp [Set.indicator_of_mem hmem]
      · simp [Set.indicator_of_notMem hmem, hx hmem]

noncomputable def scaleBand (R : ℝ) : C(Band R, Band (2 * Real.pi * R)) :=
  ⟨fun u => ⟨2 * Real.pi * (u : ℝ), abs_le.mp (by
    rw [abs_mul, abs_of_nonneg (by positivity : 0 ≤ 2 * Real.pi)]
    exact mul_le_mul_of_nonneg_left (abs_le.mpr u.property) (by positivity))⟩,
    by apply Continuous.subtype_mk; fun_prop⟩

noncomputable def spectralCutoff (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) :
    logCarrier t →L[ℂ] FullL2 :=
  (V08G.zeroBandCLM volume R hR isCompact_Icc.measure_lt_top.ne).comp
    ((ContinuousMap.compCLM ℂ ℂ (scaleBand R)).comp
      ((V08E.boundedFourier (supportMeasure t) t (2 * Real.pi * R) ht
        (supportMeasure_bound t)).comp
        ((V08F.physicalL1Inclusion (supportMeasure t)).comp
          ((restrictPhysical t).comp (physicalInclusion t)))))

theorem spectralCutoff_compact (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) :
    IsCompactOperator (spectralCutoff t R ht hR) := by
  have h := V08E.boundedFourier_compact (supportMeasure t) t (2 * Real.pi * R)
    ht (by positivity) (supportMeasure_bound t)
  exact ((h.comp_clm ((V08F.physicalL1Inclusion (supportMeasure t)).comp
    ((restrictPhysical t).comp (physicalInclusion t)))).clm_comp
      (ContinuousMap.compCLM ℂ ℂ (scaleBand R))).clm_comp
        (V08G.zeroBandCLM volume R hR isCompact_Icc.measure_lt_top.ne)

theorem spectralCutoff_ae (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R)
    (g : logCarrier t) :
    (spectralCutoff t R ht hR g : ℝ → ℂ) =ᵐ[volume]
      (Set.Icc (-R) R).indicator (fun u => (𝓕 (physicalInclusion t g) : FullL2) u) := by
  let f := physicalInclusion t g
  let r := restrictPhysical t f
  let l := V08F.physicalL1Inclusion (supportMeasure t) r
  let F := V08E.boundedFourier (supportMeasure t) t (2 * Real.pi * R) ht
    (supportMeasure_bound t) l
  let G : C(Band R, ℂ) := F.comp (scaleBand R)
  have hf := supported_integrable t f (physicalInclusion_support t g)
  change (V08G.zeroBandValue volume R hR isCompact_Icc.measure_lt_top.ne G : ℝ → ℂ) =ᵐ[volume] _
  refine (V08G.zeroBandValue_ae volume R hR isCompact_Icc.measure_lt_top.ne G).trans ?_
  filter_upwards [V08H.l2_fourier_integral_ae f hf] with u hu
  unfold V08G.zeroBand
  by_cases hm : u ∈ Set.Icc (-R) R
  · rw [Set.indicator_of_mem hm, Set.indicator_of_mem hm]
    change V08E.boundedFourier (supportMeasure t) t (2 * Real.pi * R) ht
      (supportMeasure_bound t) l (scaleBand R (V08G.clampBand R hR u)) =
        (𝓕 f : FullL2) u
    rw [V08E.boundedFourier_integral (supportMeasure t) t (2 * Real.pi * R) ht
      (by positivity) (supportMeasure_bound t)]
    change (∫ x, V08D.fourierKernel (2 * Real.pi * (V08G.clampBand R hR u : ℝ)) x *
      l x ∂supportMeasure t) = _
    rw [V08G.clampBand_eq R hR u hm]
    calc
      _ = ∫ x, V08D.fourierKernel (2 * Real.pi * u) x * r x ∂supportMeasure t := by
        apply integral_congr_ae
        filter_upwards [V08F.physicalL1Inclusion_ae (supportMeasure t) r] with x hx
        rw [show l x = r x from hx]
      _ = V08H.angularFourier (f : ℝ → ℂ) (2 * Real.pi * u) :=
        restricted_angular_integral t f (physicalInclusion_support t g) _
      _ = _ := (V08H.angularFourier_scaled (f : ℝ → ℂ) u).trans hu.symm
  · simp [Set.indicator_of_notMem hm]

noncomputable def physicalCutoff (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) :
    logCarrier t →L[ℂ] FullL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).symm.toContinuousLinearEquiv.toContinuousLinearMap.comp
    (spectralCutoff t R ht hR)

theorem physicalCutoff_compact (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) :
    IsCompactOperator (physicalCutoff t R ht hR) :=
  (spectralCutoff_compact t R ht hR).clm_comp
    (Lp.fourierTransformₗᵢ ℝ ℂ).symm.toContinuousLinearEquiv.toContinuousLinearMap

theorem physicalCutoff_tail (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R)
    (g : logCarrier t) :
    ‖physicalInclusion t g - physicalCutoff t R ht hR g‖ ^ 2 =
      ∫ u in {u : ℝ | R < |u|}, ‖(𝓕 (physicalInclusion t g) : FullL2) u‖ ^ 2 := by
  let U := Lp.fourierTransformₗᵢ ℝ ℂ
  have h : U (physicalCutoff t R ht hR g) = spectralCutoff t R ht hR g :=
    U.apply_symm_apply _
  have hn := U.norm_map (physicalInclusion t g - physicalCutoff t R ht hR g)
  rw [map_sub, h] at hn
  rw [← hn]
  exact V08G.spectral_tail_identity volume R (fun u => (𝓕 (physicalInclusion t g) : FullL2) u)
    (𝓕 (physicalInclusion t g)) (spectralCutoff t R ht hR g) (EventuallyEq.rfl)
    (spectralCutoff_ae t R ht hR g)

theorem logWeight_dominates (u : ℝ) : Real.log (2 + |u|) ≤ logWeight u := by
  unfold logWeight
  apply Real.log_le_log (by positivity)
  rw [abs_mul, abs_of_nonneg (by positivity : 0 ≤ 2 * Real.pi)]
  have hp : 1 ≤ 2 * Real.pi := by linarith [Real.pi_gt_three]
  have h := mul_le_mul_of_nonneg_right hp (abs_nonneg u)
  linarith

theorem physicalInclusion_compact (t : ℝ) (ht : 0 ≤ t) :
    IsCompactOperator (physicalInclusion t) := by
  let P : ℕ → logCarrier t →L[ℂ] FullL2 :=
    fun n => physicalCutoff t (Real.exp ((n : ℝ) + 1)) ht (Real.exp_pos _).le
  let F : logCarrier t → ℝ → ℂ := fun g u => (𝓕 (physicalInclusion t g) : FullL2) u
  have hF (g : logCarrier t) : Integrable (fun u => ‖F g u‖ ^ 2) :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable (𝓕 (physicalInclusion t g) : FullL2))).1
      (Lp.memLp (𝓕 (physicalInclusion t g) : FullL2))
  have hnon (u : ℝ) : 0 ≤ Real.log (2 + |u|) := Real.log_nonneg (by linarith [abs_nonneg u])
  have hdom (g : logCarrier t) (u : ℝ) :
      Real.log (2 + |u|) * ‖F g u‖ ^ 2 ≤ logWeight u * ‖F g u‖ ^ 2 :=
    mul_le_mul_of_nonneg_right (logWeight_dominates u) (sq_nonneg _)
  have hw (g : logCarrier t) : Integrable (fun u => Real.log (2 + |u|) * ‖F g u‖ ^ 2) := by
    apply (logCarrier_energy_integrable t g).mono_nonneg
    · have hm : AEStronglyMeasurable (fun u : ℝ => Real.log (2 + |u|)) volume :=
        (Continuous.log (by fun_prop) (by intro u; linarith [abs_nonneg u])).aestronglyMeasurable
      exact hm.mul (hF g).aestronglyMeasurable
    · exact Eventually.of_forall fun u => mul_nonneg (hnon u) (sq_nonneg _)
    · exact Eventually.of_forall (hdom g)
  apply V08C.compact_of_log_frequency_cutoffs volume (physicalInclusion t) P F
  · intro n
    exact physicalCutoff_compact t _ ht (Real.exp_pos _).le
  · exact hF
  · exact hw
  · intro g
    rw [logCarrier_energy t g]
    exact integral_mono (hw g) (logCarrier_energy_integrable t g) (hdom g)
  · intro n g
    exact physicalCutoff_tail t _ ht (Real.exp_pos _).le g

end WeilDefect.MasterRecon.V08K

#print axioms WeilDefect.MasterRecon.V08K.supportMeasure_bound
#print axioms WeilDefect.MasterRecon.V08K.restrictPhysical_ae
#print axioms WeilDefect.MasterRecon.V08K.supported_integrable
#print axioms WeilDefect.MasterRecon.V08K.restricted_angular_integral
#print axioms WeilDefect.MasterRecon.V08K.spectralCutoff_compact
#print axioms WeilDefect.MasterRecon.V08K.spectralCutoff_ae
#print axioms WeilDefect.MasterRecon.V08K.physicalCutoff_compact
#print axioms WeilDefect.MasterRecon.V08K.physicalCutoff_tail
#print axioms WeilDefect.MasterRecon.V08K.logWeight_dominates
#print axioms WeilDefect.MasterRecon.V08K.physicalInclusion_compact
