import WeilDefect.Generated.F08.NativeL2PushforwardNorm

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped ENNReal

/-!
F08-030: the first actual same-volume original complex-L² dilation map.

Unlike F08-027, this has source and target both equal to the genuine
RealComplexL2. The essential normalization is inserted *before*
the F08-027 measure-preserving pullback. The two independent stages
use genuine Lp equivalence classes, not raw-function or L² surrogates.

This first slice proves its actual almost-everywhere representative
and its exact inherited norm formula. It does NOT yet simplify the
norm to prove isometry, strong continuity, weighted Hilbert carrier
convergence, fixed-support smooth core, signed Weil form, or RH.
-/

/-- Genuine original source-carrier L² frequency dilation, obtained
by a normalized change of measure and then the actual native
measure-preserving pullback. This is meaningful for λ ≠ 0. -/
def f08_030_nativeFrequencyDilation
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) : RealComplexL2 :=
  f08_027_nativeFrequencyPullback lam
    ((Complex.ofReal (Real.sqrt (abs lam))) •
      f08_029_volumeLpToPushforward lam hlam k)

/-- The true native same-volume object has precisely the normalized
dilation formula almost everywhere in the original Lebesgue measure.
The equality is obtained via the *quasi-measure-preserving* transfer
of the genuine L² equivalence-class representation. -/
theorem f08_030_nativeFrequencyDilation_ae
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    (f08_030_nativeFrequencyDilation lam hlam k : ℝ → ℂ)
      =ᵐ[volume] fun ξ => (Complex.ofReal (Real.sqrt (abs lam))) • k (lam * ξ) := by
  let z : ℂ := Complex.ofReal (Real.sqrt (abs lam))
  let q : Lp ℂ 2 (f08_027_scaledFrequencyMeasure lam) :=
    f08_029_volumeLpToPushforward lam hlam k
  have hscaled :
      ((z • q : Lp ℂ 2 (f08_027_scaledFrequencyMeasure lam)) : ℝ → ℂ)
        =ᵐ[f08_027_scaledFrequencyMeasure lam] fun ξ => z • k ξ := by
    filter_upwards [Lp.coeFn_smul z q,
      f08_029_volumeLpToPushforward_ae lam hlam k] with ξ hs hk
    exact hs.trans (congrArg (fun t : ℂ => z • t) hk)
  have hcomp :=
    (f08_027_scale_measurePreserving lam).quasiMeasurePreserving.ae_eq_comp hscaled
  have hbase := f08_027_nativeFrequencyPullback_ae lam (z • q)
  change
    (f08_030_nativeFrequencyDilation lam hlam k : ℝ → ℂ)
      =ᵐ[volume] fun ξ => z • k (lam * ξ)
  exact hbase.trans (by simpa only [Function.comp_def] using hcomp)

/-- The genuine same-volume dilation's norm is the correctly
normalized original L² pushforward norm, with no claim of an
isometry until the exact scalar cancellation has been proved. -/
theorem f08_030_nativeFrequencyDilation_norm
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    ‖f08_030_nativeFrequencyDilation lam hlam k‖ =
      Real.sqrt (abs lam) *
        ‖f08_029_volumeLpToPushforward lam hlam k‖ := by
  unfold f08_030_nativeFrequencyDilation
  rw [(f08_027_nativeFrequencyPullback lam).norm_map, norm_smul]
  rw [Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _)]

/-- Source-exact unsimplified normalized L² norm formula, inherited
from the actual F08-029 extended-norm Jacobian. The outstanding
real-algebra cancellation is a separate isometry theorem target. -/
theorem f08_030_nativeFrequencyDilation_norm_exact
    (lam : ℝ) (hlam : lam ≠ 0) (k : RealComplexL2) :
    ‖f08_030_nativeFrequencyDilation lam hlam k‖ =
      Real.sqrt (abs lam) *
        ENNReal.toReal
          ((ENNReal.ofReal (abs ((lam ^ Module.finrank ℝ ℝ)⁻¹))) ^
              ((1 / (2 : ℝ≥0∞)).toReal) •
            eLpNorm (fun ξ : ℝ => k ξ) 2 volume) := by
  rw [f08_030_nativeFrequencyDilation_norm,
    f08_029_volumeLpToPushforward_norm]

#print axioms f08_030_nativeFrequencyDilation_ae
#print axioms f08_030_nativeFrequencyDilation_norm
#print axioms f08_030_nativeFrequencyDilation_norm_exact

end
end WeilDefect
