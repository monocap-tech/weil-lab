import WeilDefect.Generated.F08.OriginalPhysicalDilationScaling
import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement

namespace WeilDefect
noncomputable section

open MeasureTheory FourierTransform
open scoped FourierTransform ENNReal

/-- A genuine native L² vector with bounded a.e. support is L¹. -/
theorem f08_062_supportedNativeL2_integrable (a : ℝ) (f : RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) :
    Integrable (f : ℝ → ℂ) volume := by
  have hi : Integrable (neutralWindowRepresentative a f) :=
    by simpa using neutralWindowRepresentative_twist_integrable a f 0
  apply hi.congr
  filter_upwards [hf] with x hx
  by_cases h : x ∈ Set.Icc (-a) a
  · simp [neutralWindowRepresentative, h]
  · simp [neutralWindowRepresentative, h, hx h]

/-- Exact Fourier normalization of inward physical dilation for the
original supported L² carrier, with no assumed Fourier covariance. -/
theorem f08_062_originalPhysicalDilation_fourier
    (a lam : ℝ) (hlam : 0 < lam) (f : RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) :
    (𝓕 (f08_060_originalPhysicalDilation lam hlam f) : RealComplexL2) =
      f08_030_nativeFrequencyDilation lam (ne_of_gt hlam) (𝓕 f : RealComplexL2) := by
  let d := f08_060_originalPhysicalDilation lam hlam f
  let s := lam⁻¹
  have hs : 0 < s := inv_pos.mpr hlam
  let z : ℂ := Complex.ofReal (Real.sqrt s)
  have hfa : Integrable (f : ℝ → ℂ) volume :=
    f08_062_supportedNativeL2_integrable a f hf
  have hda : Integrable (d : ℝ → ℂ) volume :=
    f08_062_supportedNativeL2_integrable (lam * a) d
      (f08_060_originalPhysicalDilation_supported a lam hlam f hf)
  have hd : (d : ℝ → ℂ) =ᵐ[volume] z • (fun x : ℝ => f (s * x)) := by
    have H := f08_030_nativeFrequencyDilation_ae s (ne_of_gt hs) f
    simpa only [d, f08_060_originalPhysicalDilation, z, abs_of_pos hs, Pi.smul_apply] using H
  have hsc : Real.sqrt s * lam = Real.sqrt lam := by
    dsimp [s]
    rw [Real.sqrt_inv]
    have hp : 0 < Real.sqrt lam := Real.sqrt_pos.2 hlam
    calc
      (Real.sqrt lam)⁻¹ * lam = (Real.sqrt lam)⁻¹ * (Real.sqrt lam) ^ 2 := by
        rw [Real.sq_sqrt hlam.le]
      _ = Real.sqrt lam := by field_simp
  have hordinary (xi : ℝ) :
      𝓕 (d : ℝ → ℂ) xi =
        (Complex.ofReal (Real.sqrt lam)) • 𝓕 (f : ℝ → ℂ) (lam * xi) := by
    rw [Real.fourier_congr_ae hd xi, fourier_smul]
    change z • 𝓕 (fun x : ℝ => f (s * x)) xi = _
    rw [f08_060_originalFourier_comp_mul s hs f xi]
    have hsi : s⁻¹ = lam := by simp [s]
    rw [hsi]
    change z • (Complex.ofReal lam) • 𝓕 (f : ℝ → ℂ) (lam * xi) = _
    rw [smul_smul]
    have hz : z * Complex.ofReal lam = Complex.ofReal (Real.sqrt lam) := by
      dsimp [z]
      rw [← Complex.ofReal_mul, hsc]
    rw [hz]
  have hac : f08_027_scaledFrequencyMeasure lam ≪ (volume : Measure ℝ) := by
    rw [f08_027_scaledFrequencyMeasure_jacobian lam (ne_of_gt hlam)]
    exact Measure.smul_absolutelyContinuous
  have hscaled :=
    (f08_027_scale_measurePreserving lam).quasiMeasurePreserving.ae_eq_comp
      (hac.ae_eq (neutralIntegrableL2_fourier_ae f hfa))
  change (𝓕 d : RealComplexL2) = _
  apply Lp.ext_iff.mpr
  filter_upwards [neutralIntegrableL2_fourier_ae d hda, hscaled,
    f08_030_nativeFrequencyDilation_ae lam (ne_of_gt hlam) (𝓕 f : RealComplexL2)] with xi h1 h2 h3
  change (𝓕 f : RealComplexL2) (lam * xi) = 𝓕 (f : ℝ → ℂ) (lam * xi) at h2
  rw [h1, h3, h2, abs_of_pos hlam]
  exact hordinary xi

#print axioms f08_062_supportedNativeL2_integrable
#print axioms f08_062_originalPhysicalDilation_fourier

end
end WeilDefect
