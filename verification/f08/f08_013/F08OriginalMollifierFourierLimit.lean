import WeilDefect.Generated.F08.OriginalNormalizedMollifier
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped FourierTransform Topology

/-!
F08-013: Pointwise Fourier convergence of ACTUAL F08-011 normalized smooth
compact physical complex mollifiers, in the original real-log coordinate.

The original source's ordinary Fourier sign and 2π coefficient are retained.
This supplies F08-005's pointwise-to-one multiplier hypothesis for any
sequence of genuine bumps whose radii shrink to zero. No weighted L²
physical/Plancherel identification, strong dilation or entire dense core
is asserted here.
-/

/-- The exact negative-2π Fourier character has a linear Lipschitz phase
error when the real physical log coordinate is inside [-ε,ε]. -/
theorem f08_013_original_fourier_phase_error
    (x ξ ε : ℝ) (hx : |x| ≤ ε) :
    ‖((𝐞 (-(x * ξ))) : ℂ) - 1‖ ≤
      (2 * Real.pi * |ξ|) * ε := by
  have hbase :
      ‖Complex.exp (((2 * Real.pi * (-(x * ξ)) : ℝ) : ℂ) * Complex.I) - 1‖ ≤
      |2 * Real.pi * (-(x * ξ))| := by
    simpa only [mul_comm Complex.I, Real.norm_eq_abs] using
      (Real.norm_exp_I_mul_ofReal_sub_one_le
        (x := 2 * Real.pi * (-(x * ξ))))
  have hreal : |2 * Real.pi * (-(x * ξ))| ≤
      (2 * Real.pi * |ξ|) * ε := by
    calc
      |2 * Real.pi * (-(x * ξ))| =
          (2 * Real.pi * |ξ|) * |x| := by
        simp only [abs_neg, abs_mul, abs_of_pos Real.pi_pos]
        norm_num
        ring
      _ ≤ (2 * Real.pi * |ξ|) * ε :=
        mul_le_mul_of_nonneg_left hx (by positivity)
  rw [Real.fourierChar_apply]
  exact hbase.trans hreal

/-- For the *actual* complex-valued smooth physical bump, the Fourier
character error can be paid by the source-certified compact support radius
and the exact nonnegative L¹ norm of that same bump. -/
theorem f08_013_original_mollifier_character_error
    (φ : ContDiffBump (0 : ℝ)) (ξ x : ℝ) :
    ‖(𝐞 (-(x * ξ))) • (f08_011_complexMollifier φ x) -
        f08_011_complexMollifier φ x‖ ≤
      ((2 * Real.pi * |ξ|) * φ.rOut) *
        ‖f08_011_complexMollifier φ x‖ := by
  by_cases hx : x ∈ Function.support (f08_011_complexMollifier φ)
  · have hxabs : |x| ≤ φ.rOut :=
      abs_le.mpr (f08_011_complexMollifier_support φ hx)
    have hp := f08_013_original_fourier_phase_error x ξ φ.rOut hxabs
    calc
      ‖(𝐞 (-(x * ξ))) • (f08_011_complexMollifier φ x) -
          f08_011_complexMollifier φ x‖ =
          ‖((𝐞 (-(x * ξ))) : ℂ) - 1‖ *
            ‖f08_011_complexMollifier φ x‖ := by
        calc
          _ = ‖(((𝐞 (-(x * ξ))) : ℂ) - 1) *
                f08_011_complexMollifier φ x‖ := by
            simp only [Circle.smul_def, smul_eq_mul]
            congr 1
            ring
          _ = _ := norm_mul _ _
      _ ≤ _ := mul_le_mul_of_nonneg_right hp (norm_nonneg _)
  · have hz : f08_011_complexMollifier φ x = 0 :=
      Function.notMem_support.mp hx
    simp [hz]

/-- Quantitative original real Fourier error for the genuine positive
unit-mass C-infinity complex bump: |Fourier rho(ξ)-1| ≤ 2π|ξ| rOut.
No abstract multiplier is introduced. -/
theorem f08_013_original_mollifier_fourier_error_bound
    (φ : ContDiffBump (0 : ℝ)) (ξ : ℝ) :
    ‖(𝓕 (f08_011_complexMollifier φ)) ξ - 1‖ ≤
      (2 * Real.pi * |ξ|) * φ.rOut := by
  let ρ : ℝ → ℂ := f08_011_complexMollifier φ
  let c : ℝ := (2 * Real.pi * |ξ|) * φ.rOut
  have hρ : Integrable ρ volume :=
    f08_011_complexMollifier_integrable φ
  have hchar : Integrable (fun x : ℝ => 𝐞 (-(x * ξ)) • ρ x) volume := by
    convert (Real.fourierIntegral_convergent_iff ξ).2 hρ using 1
    ext x
    change (𝐞 (-(x * ξ))) • ρ x = (𝐞 (-(ξ * x))) • ρ x
    rw [mul_comm ξ x]
  have heq : (𝓕 ρ) ξ - 1 =
      ∫ x : ℝ, ((𝐞 (-(x * ξ))) • ρ x - ρ x) ∂volume := by
    rw [Real.fourier_real_eq ρ ξ, ← f08_011_complexMollifier_integral φ]
    exact (integral_sub hchar hρ).symm
  have hmajor : Integrable (fun x : ℝ => c * ‖ρ x‖) volume :=
    hρ.norm.const_mul c
  have hbound : ∀ᵐ x : ℝ ∂volume,
      ‖(𝐞 (-(x * ξ))) • ρ x - ρ x‖ ≤ c * ‖ρ x‖ := by
    filter_upwards [] with x
    exact f08_013_original_mollifier_character_error φ ξ x
  rw [heq]
  calc
    ‖∫ x : ℝ, ((𝐞 (-(x * ξ))) • ρ x - ρ x) ∂volume‖ ≤
        ∫ x : ℝ, c * ‖ρ x‖ ∂volume :=
      norm_integral_le_of_norm_le hmajor hbound
    _ = c * ∫ x : ℝ, ‖ρ x‖ ∂volume := integral_const_mul _ _
    _ = (2 * Real.pi * |ξ|) * φ.rOut := by
      rw [show (∫ x : ℝ, ‖ρ x‖ ∂volume) = 1 from
        f08_011_complexMollifier_integral_norm φ]
      simp [c]

/-- The genuine F08-011 physical complex mollifiers satisfy pointwise
Fourier convergence if their actual positive support radii tend to zero.
This is exactly the missing F08-005 multiplier-limit prerequisite. -/
theorem f08_013_original_mollifier_fourier_tendsto_one
    (φ : ℕ → ContDiffBump (0 : ℝ))
    (hr : Tendsto (fun n => (φ n).rOut) atTop (𝓝 (0 : ℝ)))
    (ξ : ℝ) :
    Tendsto (fun n => (𝓕 (f08_011_complexMollifier (φ n))) ξ)
      atTop (𝓝 (1 : ℂ)) := by
  apply tendsto_iff_norm_sub_tendsto_zero.mpr
  apply squeeze_zero (fun n => norm_nonneg _)
    (fun n => f08_013_original_mollifier_fourier_error_bound (φ n) ξ)
  simpa using
    (tendsto_const_nhds.mul hr :
      Tendsto (fun n => ((2 * Real.pi * |ξ|) * (φ n).rOut))
        atTop (𝓝 ((2 * Real.pi * |ξ|) * (0 : ℝ))))

#print axioms f08_013_original_fourier_phase_error
#print axioms f08_013_original_mollifier_character_error
#print axioms f08_013_original_mollifier_fourier_error_bound
#print axioms f08_013_original_mollifier_fourier_tendsto_one

end
end WeilDefect
