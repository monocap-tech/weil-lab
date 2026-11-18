import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeGeometry
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier
import Mathlib.MeasureTheory.Integral.Bochner.Set

namespace WeilDefect
noncomputable section
open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform ENNReal

/-! NF600: work directly in Mathlib's unitary Fourier coordinate.
Use the larger interval (-5,5), not the variable radius 30/(2π).
Its length is exactly 10, while outside it |2πξ| >= 30.
This preserves the historical 1/25 low-mass bound without a
change of variables in a restricted integral. -/

def neutralNF600Mass (s : 𝓢(ℝ,ℂ)) : ℝ := ‖s.toLp 2 volume‖^2

def neutralNF600Density (s : 𝓢(ℝ,ℂ)) (ξ : ℝ) : ℝ :=
  ‖𝓕 s ξ‖^2

def neutralNF600LowBand : Set ℝ := Ioo (-5:ℝ) 5

theorem neutralNF600Mass_eq_integral (s : 𝓢(ℝ,ℂ)) :
    neutralNF600Mass s = ∫ x, ‖s x‖^2 := by
  unfold neutralNF600Mass
  rw [SchwartzMap.norm_toLp' (by norm_num) (by norm_num)]
  simp only [ENNReal.toReal_ofNat,Real.rpow_two]
  rw [show (2:ℝ)⁻¹=1/2 by norm_num,← Real.sqrt_eq_rpow,
    Real.sq_sqrt (integral_nonneg fun x => sq_nonneg ‖s x‖)]

theorem neutralNF600Density_integrable (s : 𝓢(ℝ,ℂ)) :
    Integrable (neutralNF600Density s) :=
  (memLp_two_iff_integrable_sq_norm (𝓕 s).continuous.aestronglyMeasurable).mp
    ((𝓕 s).memLp 2 volume)

theorem neutralNF600Density_mass (s : 𝓢(ℝ,ℂ)) :
    ∫ ξ, neutralNF600Density s ξ = neutralNF600Mass s := by
  rw [neutralNF600Mass_eq_integral]
  exact SchwartzMap.integral_norm_sq_fourier s

theorem neutralNF600L1_bound (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    ‖s.toLp 1 volume‖ ≤ Real.sqrt (neutralNF600Mass s) * Real.sqrt (1/250) := by
  let E := neutralNF543OriginalCollars
  let μ := volume.restrict E
  have hm : volume E < ∞ := by
    rw [show volume E = ENNReal.ofReal (1/250:ℝ) from neutralNF600Collars_volume]
    exact ENNReal.ofReal_lt_top
  letI : IsFiniteMeasure μ := ⟨by simpa [μ] using hm⟩
  have h2 : MemLp (fun x : ℝ => s x) (ENNReal.ofReal 2) μ := by
    simpa using (s.memLp 2 volume).mono_measure Measure.restrict_le_self
  have h1 : MemLp (fun _ : ℝ => (1:ℂ)) (ENNReal.ofReal 2) μ := memLp_const _
  have hh := integral_mul_norm_le_Lp_mul_Lq
    (μ := μ) (p := 2) (q := 2) Real.HolderConjugate.two_two h2 h1
  simp only [norm_one,mul_one,Real.rpow_two,one_pow,← Real.sqrt_eq_rpow] at hh
  have hvol : (∫ _ : ℝ, (1:ℝ) ∂μ)=1/250 := by
    change (∫ _ : ℝ in E, (1:ℝ)) = _
    rw [setIntegral_const]
    simp [measureReal_def,E,neutralNF600Collars_volume]
  have hi1 : (∫ x : ℝ, ‖s x‖ ∂μ) = ∫ x : ℝ, ‖s x‖ := by
    change (∫ x in E, ‖s x‖) = _
    rw [← integral_indicator neutralNF600Collars_measurable]
    congr 1
    funext x
    by_cases hx : x∈E
    · exact Set.indicator_of_mem hx _
    · rw [Set.indicator_of_notMem hx,hs x hx]
      simp
  have hi2 : (∫ x : ℝ, ‖s x‖^2 ∂μ) = neutralNF600Mass s := by
    rw [neutralNF600Mass_eq_integral]
    change (∫ x in E, ‖s x‖^2) = _
    rw [← integral_indicator neutralNF600Collars_measurable]
    congr 1
    funext x
    by_cases hx : x∈E
    · exact Set.indicator_of_mem hx _
    · rw [Set.indicator_of_notMem hx,hs x hx]
      simp
  rw [hi1,hi2,hvol] at hh
  rw [SchwartzMap.norm_toLp_one]
  exact hh

theorem neutralNF600Density_bound (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) (ξ : ℝ) :
    neutralNF600Density s ξ ≤ neutralNF600Mass s/250 := by
  have h := (SchwartzMap.norm_fourier_apply_le_toLp_one s ξ).trans
    (neutralNF600L1_bound s hs)
  have hm : 0 ≤ neutralNF600Mass s := by unfold neutralNF600Mass; positivity
  have hq := pow_le_pow_left₀ (norm_nonneg _) h 2
  unfold neutralNF600Density
  calc
    _ ≤ (Real.sqrt (neutralNF600Mass s)*Real.sqrt (1/250))^2 := hq
    _ = _ := by rw [mul_pow,Real.sq_sqrt hm,Real.sq_sqrt (by norm_num)]; ring

theorem neutralNF600LowMass (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    (∫ ξ in neutralNF600LowBand, neutralNF600Density s ξ) ≤
      neutralNF600Mass s/25 := by
  have hm : volume neutralNF600LowBand = 10 := by
    unfold neutralNF600LowBand
    rw [Real.volume_Ioo]
    norm_num
  have hi : IntegrableOn (fun _ : ℝ => neutralNF600Mass s/250) neutralNF600LowBand :=
    integrableOn_const (by rw [hm]; norm_num)
  calc
    _ ≤ ∫ ξ in neutralNF600LowBand, neutralNF600Mass s/250 :=
      setIntegral_mono_on (neutralNF600Density_integrable s).integrableOn hi
        measurableSet_Ioo (fun ξ _ => neutralNF600Density_bound s hs ξ)
    _ = _ := by
      rw [setIntegral_const]
      simp [measureReal_def,hm]
      ring

theorem neutralNF600HighFrequency (ξ : ℝ) (hξ : ξ ∉ neutralNF600LowBand) :
    30 ≤ |-2*Real.pi*ξ| := by
  have h : 5 ≤ |ξ| := by
    by_contra! h
    exact hξ (abs_lt.mp h)
  rw [abs_mul,abs_mul,abs_of_neg (by norm_num : (-2:ℝ)<0),abs_of_pos Real.pi_pos]
  have hp := mul_le_mul (show (3:ℝ)≤Real.pi from Real.pi_gt_three.le) h
    (by norm_num) Real.pi_pos.le
  linarith


end
end WeilDefect
