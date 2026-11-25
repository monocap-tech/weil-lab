import WeilDefect.Generated.F08.NativeFrequencyDilation
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology SchwartzMap

/-!
F08-040: genuine normalized frequency-side pointwise Schwartz representative
convergence for original F08-030 L² dilation as nonzero λ→1.

The F08-030 normalized L² dilation has the a.e. formula
Uλ k(ξ) = Complex.ofReal (sqrt |λ|) • k(λ ξ), not pointwise equality
for arbitrary L² equivalence classes. This theorem establishes pointwise
continuity of exactly that *representative* on a Schwartz function.

The missing separate steps are one compact-support L² integrable
dominator, the actual filtered dominated convergence of the squared
difference, and exact source-native Lp norm identification. This theorem
alone does not prove L² convergence, logarithmic form-core convergence,
the signed original Weil form or RH.
-/

abbrev f08_040_nonzeroScale := {lam : ℝ // lam ≠ 0}

/-- Pointwise convergence of the exact normalized F08-030 Schwartz
representative, with the true nonzero real scaling subtype. -/
theorem f08_040_originalSchwartzDilation_pointwise_tendsto
    (g : 𝓢(ℝ, ℂ)) (ξ : ℝ) :
    Tendsto
      (fun lam : f08_040_nonzeroScale =>
        (Complex.ofReal (Real.sqrt (abs lam.1))) • g (lam.1 * ξ))
      (𝓝 (⟨1, one_ne_zero⟩ : f08_040_nonzeroScale)) (𝓝 (g ξ)) := by
  have hscale :
      Continuous (fun lam : ℝ => Complex.ofReal (Real.sqrt (abs lam))) := by
    fun_prop
  have heval : Continuous (fun lam : ℝ => g (lam * ξ)) :=
    g.continuous.comp (continuous_id.mul continuous_const)
  have hcontinuous :
      Continuous (fun lam : ℝ =>
        (Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ)) :=
    hscale.smul heval
  have hsub :
      Continuous (fun lam : f08_040_nonzeroScale =>
        (Complex.ofReal (Real.sqrt (abs lam.1))) • g (lam.1 * ξ)) :=
    hcontinuous.comp continuous_subtype_val
  simpa using (hsub.continuousAt
    (x := (⟨1, one_ne_zero⟩ : f08_040_nonzeroScale))).tendsto

#print axioms f08_040_originalSchwartzDilation_pointwise_tendsto

end
end WeilDefect
