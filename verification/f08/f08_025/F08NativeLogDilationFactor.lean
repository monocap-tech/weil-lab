import WeilDefect.Morphology.NeutralCanonicalFormDomain
import WeilDefect.Generated.F08.LogWeightDilation

namespace WeilDefect
noncomputable section

open Filter
open scoped Topology

/-!
F08-025 first kernel slice: the exact frequency-coordinate correction factor
for inward physical dilation in the original log(e + |ξ|) form norm.

This uses the actual original source weight and the already independently
accepted F08-001 scalar dilation estimate. It is NOT a proof of native
RealComplexL2 rescaling, strong L2 dilation continuity, supported smooth
form-core density, the original signed Weil pairing, F42, or RH.
-/

/-- Multiplicative correction between the unweighted unitary frequency
dilation and the original log-weighted Fourier coordinate. -/
def f08_025_logDilationFactor (lam xi : ℝ) : ℝ :=
  Real.sqrt
    (logarithmicFourierWeight xi /
      logarithmicFourierWeight (lam * xi))

theorem f08_025_logDilationFactor_nonneg (lam xi : ℝ) :
    0 ≤ f08_025_logDilationFactor lam xi := by
  exact Real.sqrt_nonneg _

theorem f08_025_logDilationFactor_one (xi : ℝ) :
    f08_025_logDilationFactor 1 xi = 1 := by
  have hw : logarithmicFourierWeight xi ≠ 0 :=
    ne_of_gt (lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight xi))
  simp [f08_025_logDilationFactor, hw]

/-- Actual original F08-001 dilation bound, specialized to the correction
factor squared; no new abstract or strengthened weight is introduced. -/
theorem f08_025_logDilationFactor_sq_le
    (lam xi : ℝ) (hlo : (1 / 2 : ℝ) ≤ lam) (hhi : lam ≤ 1) :
    f08_025_logDilationFactor lam xi ^ 2 ≤ 1 + Real.log 2 := by
  have hpos : 0 < lam := by linarith
  have hscale : lam * xi / lam = xi := by
    field_simp [ne_of_gt hpos]
  have hw := f08_logarithmicFourierWeight_dilation_uniform
    lam (lam * xi) hlo hhi
  rw [hscale] at hw
  have hden : 0 < logarithmicFourierWeight (lam * xi) :=
    lt_of_lt_of_le zero_lt_one
      (one_le_logarithmicFourierWeight (lam * xi))
  have hnum : 0 ≤ logarithmicFourierWeight xi :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight xi)
  have hqnonneg :
      0 ≤ logarithmicFourierWeight xi /
        logarithmicFourierWeight (lam * xi) :=
    div_nonneg hnum hden.le
  have hq :
      logarithmicFourierWeight xi /
          logarithmicFourierWeight (lam * xi) ≤ 1 + Real.log 2 :=
    (div_le_iff₀ hden).mpr hw
  unfold f08_025_logDilationFactor
  rwa [Real.sq_sqrt hqnonneg]

/-- Continuity of the genuine logarithmic coordinate correction factor at
physical scale 1, without invoking supported smooth-core density. -/
theorem f08_025_logDilationFactor_continuousAt_one (xi : ℝ) :
    ContinuousAt (fun lam : ℝ => f08_025_logDilationFactor lam xi) 1 := by
  have hcden :
      Continuous (fun lam : ℝ =>
        logarithmicFourierWeight (lam * xi)) :=
    logarithmicFourierWeight_continuous.comp
      (continuous_id.mul continuous_const)
  have hden (lam : ℝ) :
      logarithmicFourierWeight (lam * xi) ≠ 0 :=
    ne_of_gt (lt_of_lt_of_le zero_lt_one
      (one_le_logarithmicFourierWeight (lam * xi)))
  have hc :
      Continuous (fun lam : ℝ =>
        logarithmicFourierWeight xi /
          logarithmicFourierWeight (lam * xi)) :=
    continuous_const.div hcden hden
  exact (Real.continuous_sqrt.comp hc).continuousAt

theorem f08_025_logDilationFactor_tendsto_one (xi : ℝ) :
    Tendsto (fun lam : ℝ => f08_025_logDilationFactor lam xi)
      (𝓝 (1 : ℝ)) (𝓝 (1 : ℝ)) := by
  have h := (f08_025_logDilationFactor_continuousAt_one xi).tendsto
  rw [f08_025_logDilationFactor_one xi] at h
  exact h

#print axioms f08_025_logDilationFactor_nonneg
#print axioms f08_025_logDilationFactor_one
#print axioms f08_025_logDilationFactor_sq_le
#print axioms f08_025_logDilationFactor_continuousAt_one
#print axioms f08_025_logDilationFactor_tendsto_one

end
end WeilDefect
