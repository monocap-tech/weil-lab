import WeilDefect.MasterRecon.V08G
import Mathlib.Analysis.Fourier.LpSpace
import Mathlib.MeasureTheory.Measure.Haar.NormedSpace

/-! V08H: attach the classical Fourier integral to the actual Mathlib
Plancherel isometry on L¹ ∩ L², then reconcile the angular-frequency
kernel and the 1/(2π) energy normalization. -/
namespace WeilDefect.MasterRecon.V08H

open MeasureTheory Set Filter
open scoped ENNReal Topology FourierTransform SchwartzMap ContDiff

noncomputable abbrev FullL2 := Lp ℂ 2 (volume : Measure ℝ)

theorem classical_fourier_pairing (f g : ℝ → ℂ)
    (hf : Integrable f) (hg : Integrable g) :
    (∫ u, 𝓕 g u * f u) = ∫ x, g x * 𝓕 f x := by
  simpa only [smul_eq_mul] using
    (show (∫ u, 𝓕 g u • f u) = ∫ x, g x • 𝓕 f x by
      simpa using! VectorFourier.integral_fourierIntegral_smul_eq_flip
        (L := innerₗ ℝ) Real.continuous_fourierChar continuous_inner hg hf)

theorem classical_fourier_continuous (f : ℝ → ℂ) (hf : Integrable f) :
    Continuous (𝓕 f) := by
  exact VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar
    (innerSL ℝ).continuous₂ hf

theorem l2_fourier_pairing (f : FullL2) (g : 𝓢(ℝ, ℂ)) :
    (∫ u, g u * (𝓕 f : FullL2) u) =
      ∫ x, (𝓕 g) x * f x := by
  have h := congrArg (fun T : 𝓢'(ℝ, ℂ) => T g)
    (Lp.fourier_toTemperedDistribution_eq f)
  simpa only [TemperedDistribution.fourier_apply,
    Lp.toTemperedDistribution_apply, smul_eq_mul] using h.symm

/-- The integral and Plancherel transform agree almost everywhere.
The proof uses locally integrable distributional uniqueness, not a
postulated L¹–L² compatibility axiom. -/
theorem l2_fourier_integral_ae (f : FullL2)
    (hf : Integrable (fun x : ℝ => f x)) :
    ((𝓕 f : FullL2) : ℝ → ℂ) =ᵐ[volume] 𝓕 (f : ℝ → ℂ) := by
  apply ae_eq_of_integral_contDiff_smul_eq
  · exact (Lp.memLp (𝓕 f : FullL2)).locallyIntegrable (by norm_num)
  · exact (classical_fourier_continuous (f : ℝ → ℂ) hf).locallyIntegrable
  intro g hg hgc
  have hg₁ : HasCompactSupport (Complex.ofRealCLM ∘ g) := hgc.comp_left rfl
  have hg₂ : ContDiff ℝ ∞ (Complex.ofRealCLM ∘ g) := by fun_prop
  let φ : 𝓢(ℝ, ℂ) := hg₁.toSchwartzMap hg₂
  have hφ (x : ℝ) : φ x = (g x : ℂ) := rfl
  calc
    (∫ u, g u • (𝓕 f : FullL2) u) =
        ∫ u, φ u * (𝓕 f : FullL2) u := by
      apply integral_congr_ae
      filter_upwards with u
      rw [hφ, Complex.real_smul]
    _ = ∫ x, (𝓕 φ) x * f x := l2_fourier_pairing f φ
    _ = ∫ u, φ u * 𝓕 (f : ℝ → ℂ) u := by
      exact classical_fourier_pairing (f : ℝ → ℂ) (φ : ℝ → ℂ)
        hf φ.integrable
    _ = ∫ u, g u • 𝓕 (f : ℝ → ℂ) u := by
      apply integral_congr_ae
      filter_upwards with u
      rw [hφ, Complex.real_smul]

noncomputable def angularFourier (f : ℝ → ℂ) (u : ℝ) : ℂ :=
  ∫ x, V08D.fourierKernel u x * f x

theorem angularFourier_scaled (f : ℝ → ℂ) (u : ℝ) :
    angularFourier f (2 * Real.pi * u) = 𝓕 f u := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  unfold angularFourier
  apply integral_congr_ae
  filter_upwards with x
  rw [V08D.fourierKernel, smul_eq_mul]
  congr 1
  push_cast
  ring

theorem angularFourier_plancherel (f : FullL2)
    (hf : Integrable (fun x : ℝ => f x)) :
    ‖f‖ ^ 2 =
      (2 * Real.pi)⁻¹ * ∫ u, ‖angularFourier (f : ℝ → ℂ) u‖ ^ 2 := by
  calc
    ‖f‖ ^ 2 = ‖(𝓕 f : FullL2)‖ ^ 2 := by rw [Lp.norm_fourier_eq]
    _ = ∫ u, ‖(𝓕 f : FullL2) u‖ ^ 2 := V08G.l2_norm_sq_integral volume _
    _ = ∫ u, ‖𝓕 (f : ℝ → ℂ) u‖ ^ 2 := by
      apply integral_congr_ae
      filter_upwards [l2_fourier_integral_ae f hf] with u hu
      rw [hu]
    _ = ∫ u, ‖angularFourier (f : ℝ → ℂ) (2 * Real.pi * u)‖ ^ 2 := by
      simp_rw [angularFourier_scaled]
    _ = _ := by
      rw [Measure.integral_comp_mul_left (fun u => ‖angularFourier (f : ℝ → ℂ) u‖ ^ 2)]
      rw [abs_of_nonneg (inv_nonneg.mpr (by positivity : 0 ≤ 2 * Real.pi)), smul_eq_mul]

end WeilDefect.MasterRecon.V08H

#print axioms WeilDefect.MasterRecon.V08H.classical_fourier_pairing
#print axioms WeilDefect.MasterRecon.V08H.classical_fourier_continuous
#print axioms WeilDefect.MasterRecon.V08H.l2_fourier_pairing
#print axioms WeilDefect.MasterRecon.V08H.l2_fourier_integral_ae
#print axioms WeilDefect.MasterRecon.V08H.angularFourier_scaled
#print axioms WeilDefect.MasterRecon.V08H.angularFourier_plancherel
