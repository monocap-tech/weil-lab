import WeilDefect.Generated.F08.NativeFrequencyDilationIsometry
import Mathlib.Analysis.Fourier.FourierTransform

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal FourierTransform

/-- Genuine inward physical dilation, using the inverse scale in the
original native normalized dilation. -/
def f08_060_originalPhysicalDilation
    (lam : ℝ) (hlam : 0 < lam) (f : RealComplexL2) : RealComplexL2 :=
  f08_030_nativeFrequencyDilation lam⁻¹ (inv_ne_zero (ne_of_gt hlam)) f

/-- Exact original support transport, in native L² a.e. semantics. -/
theorem f08_060_originalPhysicalDilation_supported
    (a lam : ℝ) (hlam : 0 < lam) (f : RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-(lam * a)) (lam * a) →
      f08_060_originalPhysicalDilation lam hlam f x = 0 := by
  let s : ℝ := lam⁻¹
  have hs : 0 < s := inv_pos.mpr hlam
  have hwin : (f : ℝ → ℂ) =ᵐ[volume] (Set.Icc (-a) a).indicator (f : ℝ → ℂ) := by
    filter_upwards [hf] with x hx
    by_cases h : x ∈ Set.Icc (-a) a
    · simp [Set.indicator_of_mem h]
    · rw [Set.indicator_of_notMem h, hx h]
  have hac : f08_027_scaledFrequencyMeasure s ≪ (volume : Measure ℝ) := by
    rw [f08_027_scaledFrequencyMeasure_jacobian s (ne_of_gt hs)]
    exact Measure.smul_absolutelyContinuous
  have hcomp := (f08_027_scale_measurePreserving s).quasiMeasurePreserving.ae_eq_comp
    (hac.ae_eq hwin)
  have hd := f08_030_nativeFrequencyDilation_ae s (ne_of_gt hs) f
  filter_upwards [hcomp, hd] with x hx hy
  intro hout
  have hnot : s * x ∉ Set.Icc (-a) a := by
    intro hmem
    have he : lam * (s * x) = x := by
      dsimp [s]
      field_simp
    apply hout
    constructor
    · calc
        -(lam * a) = lam * (-a) := by ring
        _ ≤ lam * (s * x) := mul_le_mul_of_nonneg_left hmem.1 hlam.le
        _ = x := he
    · calc
        x = lam * (s * x) := he.symm
        _ ≤ lam * a := mul_le_mul_of_nonneg_left hmem.2 hlam.le
  change f (s * x) = (Set.Icc (-a) a).indicator (f : ℝ → ℂ) (s * x) at hx
  have hz : f (s * x) = 0 := hx.trans (Set.indicator_of_notMem hnot _)
  change f08_030_nativeFrequencyDilation s (ne_of_gt hs) f x = 0
  rw [hy, hz, smul_zero]

/-- Exact change of variables in the ordinary original Fourier integral
for an arbitrary genuine native L² representative. The formula keeps
the actual -2π phase and the positive scale Jacobian. -/
theorem f08_060_originalFourier_comp_mul
    (s : ℝ) (hs : 0 < s) (f : RealComplexL2) (xi : ℝ) :
    𝓕 (fun x : ℝ => f (s * x)) xi =
      s⁻¹ • (𝓕 (f : ℝ → ℂ)) (s⁻¹ * xi) := by
  let G : ℝ → ℂ := fun y =>
    Complex.exp (↑(-2 * Real.pi * y * (s⁻¹ * xi)) * Complex.I) • f y
  have hphase : Continuous (fun y : ℝ =>
      Complex.exp (↑(-2 * Real.pi * y * (s⁻¹ * xi)) * Complex.I)) := by
    fun_prop
  have hG : AEStronglyMeasurable G volume :=
    hphase.aestronglyMeasurable.smul (Lp.aestronglyMeasurable f)
  have hj : f08_027_scaledFrequencyMeasure s =
      ENNReal.ofReal s⁻¹ • (volume : Measure ℝ) := by
    rw [f08_027_scaledFrequencyMeasure_jacobian s (ne_of_gt hs),
      f08_033_jacobianFactor, abs_of_pos hs]
  have hac : f08_027_scaledFrequencyMeasure s ≪ (volume : Measure ℝ) := by
    rw [hj]
    exact Measure.smul_absolutelyContinuous
  have hm : AEStronglyMeasurable G (f08_027_scaledFrequencyMeasure s) :=
    hG.mono_ac hac
  have hmap : (∫ y, G y ∂f08_027_scaledFrequencyMeasure s) =
      ∫ x : ℝ, G (s * x) ∂volume :=
    integral_map (measurable_const_mul s).aemeasurable hm
  rw [hj, integral_smul_measure, ENNReal.toReal_ofReal (inv_nonneg.mpr hs.le)] at hmap
  rw [Real.fourier_real_eq_integral_exp_smul, Real.fourier_real_eq_integral_exp_smul]
  calc
    _ = ∫ x : ℝ, G (s * x) ∂volume := by
      apply integral_congr_ae
      apply Filter.Eventually.of_forall
      intro x
      dsimp [G]
      have he : -2 * Real.pi * x * xi =
          -2 * Real.pi * (s * x) * (s⁻¹ * xi) := by
        field_simp [ne_of_gt hs] <;> ring
      rw [he]
    _ = s⁻¹ • (∫ y, G y ∂volume) := hmap.symm
    _ = _ := rfl

#print axioms f08_060_originalPhysicalDilation_supported
#print axioms f08_060_originalFourier_comp_mul

end
end WeilDefect
