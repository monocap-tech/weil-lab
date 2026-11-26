import WeilDefect.MasterRecon.V08I

/-! V08J: the closed spectral carrier realizes exactly the supported
physical L² logarithmic form domain, not merely a subspace of it. -/
namespace WeilDefect.MasterRecon.V08J

open MeasureTheory Set Filter
open scoped ENNReal Topology FourierTransform

noncomputable abbrev FullL2 := V08I.FullL2
open V08I

noncomputable def weightRoot (u : ℝ) : ℂ :=
  (Real.sqrt (logWeight u) : ℂ)

theorem weightRoot_measurable : Measurable weightRoot := by
  unfold weightRoot
  exact Complex.continuous_ofReal.measurable.comp
    (Real.continuous_sqrt.measurable.comp logWeight_continuous.measurable)

theorem inverseWeight_weightRoot (u : ℝ) :
    inverseWeight u * weightRoot u = 1 := by
  have h : Real.sqrt (logWeight u) ≠ 0 :=
    (Real.sqrt_pos.2 (logWeight_pos u)).ne'
  unfold inverseWeight weightRoot
  exact_mod_cast inv_mul_cancel₀ h

theorem physicalInclusion_injective (t : ℝ) :
    Function.Injective (physicalInclusion t) := by
  intro g h he
  have hz : physicalInclusion t (g - h) = 0 := by
    rw [map_sub, he, sub_self]
  have hn := logCarrier_energy t (g - h)
  rw [hz, FourierTransform.fourier_zero] at hn
  have hzero : (fun u : ℝ => logWeight u * ‖(0 : FullL2) u‖ ^ 2) =ᵐ[volume]
      (fun _ => (0 : ℝ)) := by
    filter_upwards [Lp.coeFn_zero ℂ 2 (volume : Measure ℝ)] with u hu
    change (0 : FullL2) u = 0 at hu
    simp [hu]
  rw [integral_congr_ae hzero, integral_zero] at hn
  have hnorm : ‖g - h‖ = 0 := by
    nlinarith [norm_nonneg (g - h)]
  exact sub_eq_zero.mp (norm_eq_zero.mp hnorm)

theorem weightedSpectrum_mem (f : FullL2)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) :
    MemLp (fun u => weightRoot u * (𝓕 f : FullL2) u) 2 volume := by
  have hm : AEStronglyMeasurable (fun u => weightRoot u * (𝓕 f : FullL2) u)
      volume := weightRoot_measurable.aestronglyMeasurable.mul
        (Lp.aestronglyMeasurable (𝓕 f : FullL2))
  apply (memLp_two_iff_integrable_sq_norm hm).2
  apply hf.congr
  filter_upwards with u
  change logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2 =
    ‖weightRoot u * (𝓕 f : FullL2) u‖ ^ 2
  rw [norm_mul, mul_pow, weightRoot, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _), Real.sq_sqrt (logWeight_pos u).le]

noncomputable def weightedSpectrum (f : FullL2)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) : FullL2 :=
  (weightedSpectrum_mem f hf).toLp (fun u => weightRoot u * (𝓕 f : FullL2) u)

theorem weightedSpectrum_ae (f : FullL2)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) :
    (weightedSpectrum f hf : ℝ → ℂ) =ᵐ[volume]
      fun u => weightRoot u * (𝓕 f : FullL2) u :=
  MemLp.coeFn_toLp (weightedSpectrum_mem f hf)

theorem unweight_weightedSpectrum (f : FullL2)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) :
    unweight (weightedSpectrum f hf) = (𝓕 f : FullL2) := by
  apply Lp.ext
  filter_upwards [multiplier_ae inverseWeight inverseWeight_measurable _
    inverseWeight_bound (weightedSpectrum f hf), weightedSpectrum_ae f hf] with u h₁ h₂
  change unweight (weightedSpectrum f hf) u = _
  change unweight (weightedSpectrum f hf) u = inverseWeight u * weightedSpectrum f hf u at h₁
  rw [h₁, h₂, ← mul_assoc, inverseWeight_weightRoot, one_mul]

theorem physicalMap_weightedSpectrum (f : FullL2)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) :
    physicalMap (weightedSpectrum f hf) = f := by
  change (Lp.fourierTransformₗᵢ ℝ ℂ).symm (unweight (weightedSpectrum f hf)) = f
  rw [unweight_weightedSpectrum]
  exact (Lp.fourierTransformₗᵢ ℝ ℂ).symm_apply_apply f

theorem weightedSpectrum_supported (t : ℝ) (f : FullL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-t) t → f x = 0)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) :
    weightedSpectrum f hf ∈ logCarrier t := by
  change supportConstraint t (weightedSpectrum f hf) = 0
  apply Lp.ext
  have hm := multiplier_ae (outsideMask t) (outsideMask_measurable t) 1
    (outsideMask_bound t) (physicalMap (weightedSpectrum f hf))
  change (supportConstraint t (weightedSpectrum f hf) : ℝ → ℂ) =ᵐ[volume]
    fun x => outsideMask t x * physicalMap (weightedSpectrum f hf) x at hm
  rw [physicalMap_weightedSpectrum f hf] at hm
  filter_upwards [hm, hs, Lp.coeFn_zero ℂ 2 (volume : Measure ℝ)] with x hx hxs h0
  change supportConstraint t (weightedSpectrum f hf) x = (0 : FullL2) x
  change (0 : FullL2) x = 0 at h0
  rw [hx, h0, outsideMask]
  by_cases h : x ∈ Set.Icc (-t) t
  · have hn : x ∉ (Set.Icc (-t) t)ᶜ := by simpa using h
    rw [Set.indicator_of_notMem hn, zero_mul]
  · rw [Set.indicator_of_mem (show x ∈ (Set.Icc (-t) t)ᶜ from h), hxs h, mul_zero]

noncomputable def liftPhysical (t : ℝ) (f : FullL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-t) t → f x = 0)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) : logCarrier t :=
  ⟨weightedSpectrum f hf, weightedSpectrum_supported t f hs hf⟩

theorem physicalInclusion_lift (t : ℝ) (f : FullL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-t) t → f x = 0)
    (hf : Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2)) :
    physicalInclusion t (liftPhysical t f hs hf) = f :=
  physicalMap_weightedSpectrum f hf

theorem physicalInclusion_range_iff (t : ℝ) (f : FullL2) :
    (∃ g : logCarrier t, physicalInclusion t g = f) ↔
      (∀ᵐ x ∂volume, x ∉ Set.Icc (-t) t → f x = 0) ∧
      Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖ ^ 2) := by
  constructor
  · rintro ⟨g, rfl⟩
    exact ⟨physicalInclusion_support t g, logCarrier_energy_integrable t g⟩
  · rintro ⟨hs, hf⟩
    exact ⟨liftPhysical t f hs hf, physicalInclusion_lift t f hs hf⟩

end WeilDefect.MasterRecon.V08J

#print axioms WeilDefect.MasterRecon.V08J.weightRoot_measurable
#print axioms WeilDefect.MasterRecon.V08J.inverseWeight_weightRoot
#print axioms WeilDefect.MasterRecon.V08J.physicalInclusion_injective
#print axioms WeilDefect.MasterRecon.V08J.weightedSpectrum_mem
#print axioms WeilDefect.MasterRecon.V08J.weightedSpectrum_ae
#print axioms WeilDefect.MasterRecon.V08J.unweight_weightedSpectrum
#print axioms WeilDefect.MasterRecon.V08J.physicalMap_weightedSpectrum
#print axioms WeilDefect.MasterRecon.V08J.weightedSpectrum_supported
#print axioms WeilDefect.MasterRecon.V08J.physicalInclusion_lift
#print axioms WeilDefect.MasterRecon.V08J.physicalInclusion_range_iff
