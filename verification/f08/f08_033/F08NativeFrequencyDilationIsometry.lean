import WeilDefect.Generated.F08.NativeFrequencyDilation

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal

/-!
F08-033: source-native same-volume L² dilation norm preservation.

The original native RealComplexL2 frequency dilation is already constructed
in F08-030 from the genuine pushed-forward measure. Here the nontrivial
one-dimensional Jacobian and the sqrt(|λ|) normalization are *cancelled*.

This file does NOT establish strong L² continuity, Fourier scaling,
physical support, the weighted logarithmic carrier identity/density,
literal signed Weil identity, F42 positivity, or RH.
-/

/-- The exact 1-dimensional Haar-Jacobian factor (including λ < 0). -/
theorem f08_033_jacobianFactor (lam : ℝ) :
    abs ((lam ^ Module.finrank ℝ ℝ)⁻¹) = (abs lam)⁻¹ := by
  simp [Module.finrank_self]

/-- The positive sqrt normalization cancels the inverse Jacobian. -/
theorem f08_033_sqrtJacobian_cancel (lam : ℝ) (hlam : lam ≠ 0) :
    Real.sqrt (abs lam) * ((abs lam)⁻¹) ^ (1 / (2 : ℝ)) = 1 := by
  have hpos : 0 < abs lam := abs_pos.mpr hlam
  calc
    _ = Real.sqrt (abs lam) * Real.sqrt ((abs lam)⁻¹) := by
      rw [Real.sqrt_eq_rpow]
    _ = Real.sqrt (abs lam) * (Real.sqrt (abs lam))⁻¹ := by
      rw [Real.sqrt_inv]
    _ = 1 := mul_inv_cancel₀ (Real.sqrt_ne_zero'.mpr hpos)

/-- Genuine original RealComplexL2 same-volume scaling is norm preserving.
This uses the full native F08-027/029/030 source chain, NOT a surrogate. -/
theorem f08_033_nativeFrequencyDilation_isometry
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    ‖f08_030_nativeFrequencyDilation lam hlam k‖ = ‖k‖ := by
  have hhalf : (1 / (2 : ℝ≥0∞)).toReal = (1 / (2 : ℝ)) := by
    norm_num
  calc
    ‖f08_030_nativeFrequencyDilation lam hlam k‖ =
        Real.sqrt (abs lam) *
          ENNReal.toReal
            ((ENNReal.ofReal (abs ((lam ^ Module.finrank ℝ ℝ)⁻¹))) ^
                ((1 / (2 : ℝ≥0∞)).toReal) •
              eLpNorm (fun ξ : ℝ => k ξ) 2 volume) :=
      f08_030_nativeFrequencyDilation_norm_exact lam hlam k
    _ = (Real.sqrt (abs lam) * ((abs lam)⁻¹) ^ (1 / (2 : ℝ))) *
          ‖k‖ := by
      rw [Lp.norm_def]
      rw [f08_033_jacobianFactor lam]
      rw [ENNReal.smul_def, ENNReal.toReal_mul, ENNReal.toReal_rpow]
      rw [hhalf, ENNReal.toReal_ofReal (by positivity)]
      ring
    _ = ‖k‖ := by
      rw [f08_033_sqrtJacobian_cancel lam hlam]
      simp

#print axioms f08_033_jacobianFactor
#print axioms f08_033_sqrtJacobian_cancel
#print axioms f08_033_nativeFrequencyDilation_isometry

end
end WeilDefect
