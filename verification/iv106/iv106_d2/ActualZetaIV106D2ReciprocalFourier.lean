import WeilDefect.Arithmetic.ActualZetaCanonicalNativeEnergy
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier
import Mathlib.Analysis.Fourier.LpSpace
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped SchwartzMap FourierTransform LineDeriv InnerProduct

/-- Exact Schwartz Fourier multiplier for the derivative in direction one. -/
theorem neutralIV106D2Fourier_deriv (V : 𝓢(ℝ,ℂ)) (ξ : ℝ) :
    (𝓕 (∂_{(1 : ℝ)} V)) ξ =
      (2 * (Real.pi : ℂ) * Complex.I) * ((ξ : ℂ) * (𝓕 V) ξ) := by
  have h := congrArg (fun s : 𝓢(ℝ,ℂ) => s ξ)
    (SchwartzMap.fourier_lineDerivOp_eq V (1 : ℝ))
  have ht : (fun x : ℝ => inner ℝ x (1 : ℝ)).HasTemperateGrowth :=
    ((innerSL ℝ).flip (1 : ℝ)).hasTemperateGrowth
  simpa [SchwartzMap.smul_apply, SchwartzMap.smulLeftCLM_apply_apply ht,
    RCLike.inner_apply, smul_eq_mul] using h

/-- Pointwise reciprocal identity away from the null frequency. -/
theorem neutralIV106D2Reciprocal_point (V v : 𝓢(ℝ,ℂ))
    (hd : ∂_{(1 : ℝ)} V = v) (ξ : ℝ) (hξ : ξ ≠ 0) :
    ‖(𝓕 v) ξ‖^2 / ξ^2 = (2*Real.pi)^2 * ‖(𝓕 V) ξ‖^2 := by
  have h := neutralIV106D2Fourier_deriv V ξ
  rw [hd] at h
  rw [h, norm_mul, norm_mul, norm_mul, norm_mul]
  simp only [Complex.norm_I, Complex.norm_real, Complex.norm_ofNat,
    Real.norm_eq_abs, abs_of_pos Real.pi_pos, mul_one]
  rw [div_eq_iff (pow_ne_zero _ hξ)]
  rw [← sq_abs ξ]
  ring

/-- Actual L2 reciprocal moment, using the same Schwartz primitive. -/
theorem neutralIV106D2Reciprocal_ae (V v : 𝓢(ℝ,ℂ))
    (hd : ∂_{(1 : ℝ)} V = v) :
    ∀ᵐ ξ ∂volume, ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2 / ξ^2 =
      (2*Real.pi)^2 * ‖(𝓕 (V.toLp 2 volume) : RealComplexL2) ξ‖^2 := by
  rw [SchwartzMap.toLp_fourier_eq, SchwartzMap.toLp_fourier_eq]
  have hz : ∀ᵐ ξ : ℝ ∂volume, ξ ≠ 0 := by
    rw [ae_iff]
    simpa using (measure_singleton (0:ℝ) : volume ({0}:Set ℝ) = 0)
  filter_upwards [hz, (𝓕 v).coeFn_toLp 2 volume,
    (𝓕 V).coeFn_toLp 2 volume] with ξ hξ hv hV
  rw [hv, hV]
  exact neutralIV106D2Reciprocal_point V v hd ξ hξ

theorem neutralIV106D2Reciprocal_energy (V v : 𝓢(ℝ,ℂ))
    (hd : ∂_{(1 : ℝ)} V = v) :
    (∫ ξ : ℝ, ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2 / ξ^2) =
      (2*Real.pi)^2 * ‖V.toLp 2 volume‖^2 := by
  rw [integral_congr_ae (neutralIV106D2Reciprocal_ae V v hd),
    integral_const_mul, ← neutralPhysicalL2_norm_sq, Lp.norm_fourier_eq]

/-- Transfer a primitive-energy estimate to the actual Fourier moment. -/
theorem neutralIV106D2Reciprocal_bound (V v : 𝓢(ℝ,ℂ)) (h : ℝ)
    (hd : ∂_{(1 : ℝ)} V = v)
    (hm : ‖V.toLp 2 volume‖^2 ≤ h^2/6 * ‖v.toLp 2 volume‖^2) :
    (∫ ξ : ℝ, ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2 / ξ^2) ≤
      (2*Real.pi^2/3)*h^2*‖v.toLp 2 volume‖^2 := by
  rw [neutralIV106D2Reciprocal_energy V v hd]
  calc
    _ ≤ (2*Real.pi)^2 * (h^2/6 * ‖v.toLp 2 volume‖^2) :=
      mul_le_mul_of_nonneg_left hm (sq_nonneg _)
    _ = _ := by ring

#print axioms neutralIV106D2Fourier_deriv
#print axioms neutralIV106D2Reciprocal_point
#print axioms neutralIV106D2Reciprocal_ae
#print axioms neutralIV106D2Reciprocal_energy
#print axioms neutralIV106D2Reciprocal_bound
end
end WeilDefect
