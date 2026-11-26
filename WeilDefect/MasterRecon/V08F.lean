import WeilDefect.MasterRecon.V08E
import Mathlib.MeasureTheory.Function.LpSpace.ContinuousFunctions

/-! V08F: finite-measure physical L² → L¹ inclusion and compact
bounded-band Fourier operator with genuine L² input/output. The
frequency measure is on the compact interval subtype. Plancherel and
zero extension to the full frequency line are separate obligations. -/
namespace WeilDefect.MasterRecon.V08F

open MeasureTheory Set Filter
open scoped ENNReal Topology

abbrev Band := V08E.Band
local instance bandCompact (R : ℝ) : CompactSpace (Band R) :=
  compactSpace_Icc (-R) R

noncomputable abbrev PhysicalL2 (μ : Measure ℝ) := Lp ℂ 2 μ

theorem physicalL1_mem (μ : Measure ℝ) [IsFiniteMeasure μ]
    (f : PhysicalL2 μ) : MemLp (fun x => f x) 1 μ :=
  (Lp.memLp f).mono_exponent (by norm_num)

noncomputable def physicalL1Value (μ : Measure ℝ) [IsFiniteMeasure μ]
    (f : PhysicalL2 μ) : V08E.PhysicalL1 μ :=
  (physicalL1_mem μ f).toLp (fun x => f x)

theorem physicalL1Value_ae (μ : Measure ℝ) [IsFiniteMeasure μ]
    (f : PhysicalL2 μ) :
    (physicalL1Value μ f : ℝ → ℂ) =ᵐ[μ] f :=
  MemLp.coeFn_toLp (physicalL1_mem μ f)

theorem physicalL1Value_bound (μ : Measure ℝ) [IsFiniteMeasure μ]
    (f : PhysicalL2 μ) :
    ‖physicalL1Value μ f‖ ≤
      (μ Set.univ ^ (1 / 2 : ℝ)).toReal * ‖f‖ := by
  have h := eLpNorm_le_eLpNorm_mul_rpow_measure_univ
    (p := 1) (q := 2) (by norm_num : (1 : ℝ≥0∞) ≤ 2)
    (Lp.aestronglyMeasurable f)
  have he : (1 / (1 : ℝ≥0∞).toReal - 1 / (2 : ℝ≥0∞).toReal : ℝ) =
      1 / 2 := by norm_num
  rw [he] at h
  have hm : μ Set.univ ^ (1 / 2 : ℝ) ≠ ∞ :=
    ENNReal.rpow_ne_top_of_nonneg (by norm_num) (ne_of_lt (measure_univ_lt_top))
  have hn := ENNReal.toReal_mono
    (ENNReal.mul_ne_top (Lp.eLpNorm_ne_top f) hm) h
  rw [ENNReal.toReal_mul] at hn
  unfold physicalL1Value
  rw [Lp.norm_toLp, Lp.norm_def, mul_comm]
  exact hn

noncomputable def physicalL1Inclusion (μ : Measure ℝ) [IsFiniteMeasure μ] :
    PhysicalL2 μ →L[ℂ] V08E.PhysicalL1 μ :=
  ({
    toFun := physicalL1Value μ
    map_add' := fun f g => by
      apply Lp.ext
      filter_upwards [physicalL1Value_ae μ (f + g),
        physicalL1Value_ae μ f, physicalL1Value_ae μ g,
        Lp.coeFn_add f g,
        Lp.coeFn_add (physicalL1Value μ f) (physicalL1Value μ g)] with x h₁ h₂ h₃ h₄ h₅
      change physicalL1Value μ (f + g) x =
        (physicalL1Value μ f + physicalL1Value μ g) x
      calc
        _ = (f + g) x := h₁
        _ = f x + g x := h₄
        _ = physicalL1Value μ f x + physicalL1Value μ g x := by rw [h₂, h₃]
        _ = _ := h₅.symm
    map_smul' := fun c f => by
      apply Lp.ext
      filter_upwards [physicalL1Value_ae μ (c • f), physicalL1Value_ae μ f,
        Lp.coeFn_smul c f, Lp.coeFn_smul c (physicalL1Value μ f)] with x h₁ h₂ h₃ h₄
      change physicalL1Value μ (c • f) x = (c • physicalL1Value μ f) x
      calc
        _ = (c • f) x := h₁
        _ = c * f x := h₃
        _ = c * physicalL1Value μ f x := by rw [h₂]
        _ = _ := h₄.symm
  } : PhysicalL2 μ →ₗ[ℂ] V08E.PhysicalL1 μ).mkContinuous
    ((μ Set.univ ^ (1 / 2 : ℝ)).toReal) (physicalL1Value_bound μ)

theorem physicalL1Inclusion_ae (μ : Measure ℝ) [IsFiniteMeasure μ]
    (f : PhysicalL2 μ) :
    (physicalL1Inclusion μ f : ℝ → ℂ) =ᵐ[μ] f :=
  physicalL1Value_ae μ f

theorem physicalL1Inclusion_norm (μ : Measure ℝ) [IsFiniteMeasure μ] :
    ‖physicalL1Inclusion μ‖ ≤ (μ Set.univ ^ (1 / 2 : ℝ)).toReal :=
  ContinuousLinearMap.opNorm_le_bound _ ENNReal.toReal_nonneg
    (physicalL1Value_bound μ)

noncomputable def bandFourierL2 (μ : Measure ℝ) [IsFiniteMeasure μ]
    (t R : ℝ) (ν : Measure (Band R)) [IsFiniteMeasure ν]
    (ht0 : 0 ≤ t) (ht : ∀ᵐ x ∂μ, |x| ≤ t) :
    PhysicalL2 μ →L[ℂ] Lp ℂ 2 ν :=
  (ContinuousMap.toLp 2 ν ℂ).comp
    ((V08E.boundedFourier μ t R ht0 ht).comp (physicalL1Inclusion μ))

theorem bandFourierL2_compact (μ : Measure ℝ) [IsFiniteMeasure μ]
    (t R : ℝ) (ν : Measure (Band R)) [IsFiniteMeasure ν]
    (ht0 : 0 ≤ t) (hR : 0 ≤ R) (ht : ∀ᵐ x ∂μ, |x| ≤ t) :
    IsCompactOperator (bandFourierL2 μ t R ν ht0 ht) := by
  have h := V08E.boundedFourier_compact μ t R ht0 hR ht
  exact (h.comp_clm (physicalL1Inclusion μ)).clm_comp (ContinuousMap.toLp 2 ν ℂ)

theorem bandFourierL2_integral (μ : Measure ℝ) [IsFiniteMeasure μ]
    (t R : ℝ) (ν : Measure (Band R)) [IsFiniteMeasure ν]
    (ht0 : 0 ≤ t) (hR : 0 ≤ R) (ht : ∀ᵐ x ∂μ, |x| ≤ t)
    (f : PhysicalL2 μ) :
    (bandFourierL2 μ t R ν ht0 ht f : Band R → ℂ) =ᵐ[ν]
      fun u => ∫ x, V08D.fourierKernel (u : ℝ) x * f x ∂μ := by
  let g := physicalL1Inclusion μ f
  let F := V08E.boundedFourier μ t R ht0 ht g
  change (ContinuousMap.toLp 2 ν ℂ F : Band R → ℂ) =ᵐ[ν] _
  refine (ContinuousMap.coeFn_toLp (p := 2) (𝕜 := ℂ) ν F).trans ?_
  filter_upwards with u
  change V08E.boundedFourier μ t R ht0 ht g u = _
  rw [V08E.boundedFourier_integral μ t R ht0 hR ht]
  apply integral_congr_ae
  filter_upwards [physicalL1Inclusion_ae μ f] with x hx
  change V08D.fourierKernel (u : ℝ) x * g x = _
  rw [show g x = f x from hx]

end WeilDefect.MasterRecon.V08F

#print axioms WeilDefect.MasterRecon.V08F.physicalL1_mem
#print axioms WeilDefect.MasterRecon.V08F.physicalL1Value_ae
#print axioms WeilDefect.MasterRecon.V08F.physicalL1Value_bound
#print axioms WeilDefect.MasterRecon.V08F.physicalL1Inclusion_ae
#print axioms WeilDefect.MasterRecon.V08F.physicalL1Inclusion_norm
#print axioms WeilDefect.MasterRecon.V08F.bandFourierL2_compact
#print axioms WeilDefect.MasterRecon.V08F.bandFourierL2_integral
