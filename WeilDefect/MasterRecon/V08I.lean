import WeilDefect.MasterRecon.V08H

/-! V08I: complete logarithmic carrier as a closed kernel in spectral
L². The frequency coordinate is Mathlib's ξ, so the angular logarithmic
weight is exactly log(2 + |2πξ|). -/
namespace WeilDefect.MasterRecon.V08I

open MeasureTheory Set Filter
open scoped ENNReal Topology FourierTransform

noncomputable abbrev FullL2 := V08H.FullL2

theorem multiplier_mem (m : ℝ → ℂ) (hm : Measurable m) (B : ℝ)
    (hb : ∀ u, ‖m u‖ ≤ B) (f : FullL2) :
    MemLp (fun u => m u * f u) 2 volume := by
  apply (Lp.memLp f).of_le_mul
    (hm.aestronglyMeasurable.mul (Lp.aestronglyMeasurable f))
  filter_upwards with u
  change ‖m u * f u‖ ≤ B * ‖f u‖
  rw [norm_mul]
  exact mul_le_mul_of_nonneg_right (hb u) (norm_nonneg _)

noncomputable def mulValue (m : ℝ → ℂ) (hm : Measurable m) (B : ℝ)
    (hb : ∀ u, ‖m u‖ ≤ B) (f : FullL2) : FullL2 :=
  (multiplier_mem m hm B hb f).toLp (fun u => m u * f u)

theorem mulValue_ae (m : ℝ → ℂ) (hm : Measurable m) (B : ℝ)
    (hb : ∀ u, ‖m u‖ ≤ B) (f : FullL2) :
    (mulValue m hm B hb f : ℝ → ℂ) =ᵐ[volume] fun u => m u * f u :=
  MemLp.coeFn_toLp (multiplier_mem m hm B hb f)

theorem mulValue_bound (m : ℝ → ℂ) (hm : Measurable m) (B : ℝ)
    (hb : ∀ u, ‖m u‖ ≤ B) (f : FullL2) :
    ‖mulValue m hm B hb f‖ ≤ B * ‖f‖ := by
  apply Lp.norm_le_mul_norm_of_ae_le_mul
  filter_upwards [mulValue_ae m hm B hb f] with u hu
  rw [hu, norm_mul]
  exact mul_le_mul_of_nonneg_right (hb u) (norm_nonneg _)

noncomputable def multiplier (m : ℝ → ℂ) (hm : Measurable m) (B : ℝ)
    (hb : ∀ u, ‖m u‖ ≤ B) : FullL2 →L[ℂ] FullL2 :=
  ({
    toFun := mulValue m hm B hb
    map_add' := fun f g => by
      apply Lp.ext
      filter_upwards [mulValue_ae m hm B hb (f + g),
        mulValue_ae m hm B hb f, mulValue_ae m hm B hb g, Lp.coeFn_add f g,
        Lp.coeFn_add (mulValue m hm B hb f) (mulValue m hm B hb g)]
        with u h₁ h₂ h₃ h₄ h₅
      change mulValue m hm B hb (f + g) u =
        (mulValue m hm B hb f + mulValue m hm B hb g) u
      rw [h₁, show (f + g) u = f u + g u from h₄,
        show (mulValue m hm B hb f + mulValue m hm B hb g) u =
          mulValue m hm B hb f u + mulValue m hm B hb g u from h₅, h₂, h₃, mul_add]
    map_smul' := fun c f => by
      apply Lp.ext
      filter_upwards [mulValue_ae m hm B hb (c • f),
        mulValue_ae m hm B hb f, Lp.coeFn_smul c f,
        Lp.coeFn_smul c (mulValue m hm B hb f)] with u h₁ h₂ h₃ h₄
      change mulValue m hm B hb (c • f) u = (c • mulValue m hm B hb f) u
      rw [h₁, show (c • f) u = c * f u from h₃,
        show (c • mulValue m hm B hb f) u = c * mulValue m hm B hb f u from h₄, h₂]
      ring
  } : FullL2 →ₗ[ℂ] FullL2).mkContinuous B (mulValue_bound m hm B hb)

theorem multiplier_ae (m : ℝ → ℂ) (hm : Measurable m) (B : ℝ)
    (hb : ∀ u, ‖m u‖ ≤ B) (f : FullL2) :
    (multiplier m hm B hb f : ℝ → ℂ) =ᵐ[volume] fun u => m u * f u :=
  mulValue_ae m hm B hb f

noncomputable def logWeight (u : ℝ) : ℝ :=
  Real.log (2 + |2 * Real.pi * u|)

theorem logWeight_lower (u : ℝ) : Real.log 2 ≤ logWeight u := by
  unfold logWeight
  apply Real.log_le_log (by norm_num)
  linarith [abs_nonneg (2 * Real.pi * u)]

theorem logWeight_pos (u : ℝ) : 0 < logWeight u :=
  (Real.log_pos (by norm_num : (1 : ℝ) < 2)).trans_le (logWeight_lower u)

theorem logWeight_continuous : Continuous logWeight := by
  unfold logWeight
  apply Continuous.log (by fun_prop)
  intro u
  linarith [abs_nonneg (2 * Real.pi * u)]

noncomputable def inverseWeight (u : ℝ) : ℂ :=
  ((Real.sqrt (logWeight u))⁻¹ : ℝ)

theorem inverseWeight_measurable : Measurable inverseWeight := by
  unfold inverseWeight
  exact Complex.continuous_ofReal.measurable.comp
    (Real.continuous_sqrt.measurable.comp logWeight_continuous.measurable).inv

theorem inverseWeight_bound (u : ℝ) :
    ‖inverseWeight u‖ ≤ (Real.sqrt (Real.log 2))⁻¹ := by
  have h : 0 < Real.sqrt (logWeight u) := Real.sqrt_pos.2 (logWeight_pos u)
  rw [inverseWeight, Complex.norm_real, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr h)]
  exact inv_anti₀ (Real.sqrt_pos.2 (Real.log_pos (by norm_num : (1 : ℝ) < 2)))
    (Real.sqrt_le_sqrt (logWeight_lower u))

noncomputable def unweight : FullL2 →L[ℂ] FullL2 :=
  multiplier inverseWeight inverseWeight_measurable _
    inverseWeight_bound

noncomputable def outsideMask (t : ℝ) : ℝ → ℂ :=
  (Set.Icc (-t) t)ᶜ.indicator (fun _ => (1 : ℂ))

theorem outsideMask_measurable (t : ℝ) : Measurable (outsideMask t) :=
  measurable_const.indicator measurableSet_Icc.compl

theorem outsideMask_bound (t u : ℝ) : ‖outsideMask t u‖ ≤ 1 := by
  unfold outsideMask
  by_cases h : u ∈ (Set.Icc (-t) t)ᶜ <;> simp [h]

noncomputable def physicalMap : FullL2 →L[ℂ] FullL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).symm.toContinuousLinearEquiv.toContinuousLinearMap.comp unweight

noncomputable def supportConstraint (t : ℝ) : FullL2 →L[ℂ] FullL2 :=
  (multiplier (outsideMask t) (outsideMask_measurable t) 1 (outsideMask_bound t)).comp physicalMap

noncomputable def logCarrier (t : ℝ) : Submodule ℂ FullL2 :=
  (supportConstraint t).ker

theorem logCarrier_closed (t : ℝ) : IsClosed (logCarrier t : Set FullL2) :=
  (supportConstraint t).isClosed_ker

noncomputable instance logCarrier_complete (t : ℝ) : CompleteSpace (logCarrier t) :=
  (logCarrier_closed t).completeSpace_coe

noncomputable def physicalInclusion (t : ℝ) : logCarrier t →L[ℂ] FullL2 :=
  physicalMap.comp (logCarrier t).subtypeL

theorem physicalInclusion_support (t : ℝ) (g : logCarrier t) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-t) t → physicalInclusion t g x = 0 := by
  have hzero : supportConstraint t (g : FullL2) = 0 := g.property
  have h := multiplier_ae (outsideMask t) (outsideMask_measurable t) 1
    (outsideMask_bound t) (physicalMap (g : FullL2))
  change (supportConstraint t (g : FullL2) : ℝ → ℂ) =ᵐ[volume]
    fun x => outsideMask t x * physicalMap (g : FullL2) x at h
  rw [hzero] at h
  filter_upwards [h, (Lp.coeFn_zero ℂ 2 (volume : Measure ℝ))] with x hx h0
  intro hxout
  change physicalMap (g : FullL2) x = 0
  change (0 : FullL2) x = outsideMask t x * physicalMap (g : FullL2) x at hx
  change (0 : FullL2) x = 0 at h0
  rw [h0, outsideMask, Set.indicator_of_mem (show x ∈ (Set.Icc (-t) t)ᶜ from hxout),
    one_mul] at hx
  exact hx.symm

theorem physicalInclusion_fourier_ae (t : ℝ) (g : logCarrier t) :
    ((𝓕 (physicalInclusion t g) : FullL2) : ℝ → ℂ) =ᵐ[volume]
      fun u => inverseWeight u * (g : FullL2) u := by
  have h : (𝓕 (physicalInclusion t g) : FullL2) = unweight (g : FullL2) := by
    change (Lp.fourierTransformₗᵢ ℝ ℂ)
      ((Lp.fourierTransformₗᵢ ℝ ℂ).symm (unweight (g : FullL2))) = _
    exact (Lp.fourierTransformₗᵢ ℝ ℂ).apply_symm_apply _
  rw [h]
  exact multiplier_ae inverseWeight inverseWeight_measurable _ inverseWeight_bound _

theorem logCarrier_energy_ae (t : ℝ) (g : logCarrier t) :
    (fun u => logWeight u * ‖(𝓕 (physicalInclusion t g) : FullL2) u‖ ^ 2) =ᵐ[volume]
      fun u => ‖(g : FullL2) u‖ ^ 2 := by
  filter_upwards [physicalInclusion_fourier_ae t g] with u hu
  rw [hu, norm_mul, inverseWeight, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos (inv_pos.mpr (Real.sqrt_pos.2 (logWeight_pos u))), mul_pow, inv_pow,
    Real.sq_sqrt (logWeight_pos u).le]
  field_simp [(logWeight_pos u).ne']

theorem logCarrier_energy (t : ℝ) (g : logCarrier t) :
    ‖g‖ ^ 2 = ∫ u, logWeight u * ‖(𝓕 (physicalInclusion t g) : FullL2) u‖ ^ 2 := by
  change ‖(g : FullL2)‖ ^ 2 = _
  rw [V08G.l2_norm_sq_integral volume]
  exact integral_congr_ae (logCarrier_energy_ae t g).symm

theorem logCarrier_energy_integrable (t : ℝ) (g : logCarrier t) :
    Integrable (fun u => logWeight u * ‖(𝓕 (physicalInclusion t g) : FullL2) u‖ ^ 2) := by
  apply Integrable.congr _ (logCarrier_energy_ae t g).symm
  exact (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable (g : FullL2))).1
    (Lp.memLp (g : FullL2))

end WeilDefect.MasterRecon.V08I

#print axioms WeilDefect.MasterRecon.V08I.multiplier_mem
#print axioms WeilDefect.MasterRecon.V08I.mulValue_ae
#print axioms WeilDefect.MasterRecon.V08I.mulValue_bound
#print axioms WeilDefect.MasterRecon.V08I.multiplier_ae
#print axioms WeilDefect.MasterRecon.V08I.logWeight_lower
#print axioms WeilDefect.MasterRecon.V08I.logWeight_pos
#print axioms WeilDefect.MasterRecon.V08I.logWeight_continuous
#print axioms WeilDefect.MasterRecon.V08I.inverseWeight_measurable
#print axioms WeilDefect.MasterRecon.V08I.inverseWeight_bound
#print axioms WeilDefect.MasterRecon.V08I.outsideMask_measurable
#print axioms WeilDefect.MasterRecon.V08I.outsideMask_bound
#print axioms WeilDefect.MasterRecon.V08I.logCarrier_closed
#print axioms WeilDefect.MasterRecon.V08I.logCarrier_complete
#print axioms WeilDefect.MasterRecon.V08I.physicalInclusion_support
#print axioms WeilDefect.MasterRecon.V08I.physicalInclusion_fourier_ae
#print axioms WeilDefect.MasterRecon.V08I.logCarrier_energy_ae
#print axioms WeilDefect.MasterRecon.V08I.logCarrier_energy
#print axioms WeilDefect.MasterRecon.V08I.logCarrier_energy_integrable
