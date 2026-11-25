import WeilDefect.Generated.F08.NativeDilationLinearIsometry

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology

/-!
F08-038: actual native complex L² strong-continuity transfer from any dense
class. This is an unconditional *implication* whose premise is strong
convergence on a dense class. It is not an assertion of the unproved
compactly supported Schwartz convergence theorem.

The original source Uλ is the F08-030 normalized nonzero frequency
dilation in the genuine RealComplexL2. The triangle estimate is
the original F08-035 kernel-certified approximation bound, and
has no external abstract substitute or change of carriers.

Full λ→1 continuity requires the remaining compact-core DCT step.
Logarithmic weighted convergence, physically supported core density,
the entire signed original Weil form, positivity and RH remain open.
-/

/-- The genuine nonzero frequency parameters with the ordinary
subtype topology and no illicit definition at zero. -/
abbrev f08_038_nonzeroScale := {lam : ℝ // lam ≠ 0}

/-- Native frequency dilation is strongly continuous at scale one
whenever its actual action on a dense set has that limit. The premise
must later be discharged for a concrete native compact Schwartz core. -/
theorem f08_038_nativeL2_tendsto_of_dense_core
    (s : Set RealComplexL2) (hs : Dense s)
    (hcore : ∀ g ∈ s,
      Tendsto
        (fun lam : f08_038_nonzeroScale =>
          f08_030_nativeFrequencyDilation lam.1 lam.2 g)
        (𝓝 (⟨1, one_ne_zero⟩ : f08_038_nonzeroScale)) (𝓝 g))
    (k : RealComplexL2) :
    Tendsto
      (fun lam : f08_038_nonzeroScale =>
        f08_030_nativeFrequencyDilation lam.1 lam.2 k)
      (𝓝 (⟨1, one_ne_zero⟩ : f08_038_nonzeroScale)) (𝓝 k) := by
  rw [Metric.tendsto_nhds]
  intro ε hε
  obtain ⟨g, hg, hkg⟩ := hs.exists_dist_lt k
    (by positivity : 0 < ε / 4)
  have hkg' : ‖k - g‖ < ε / 4 := by
    simpa only [dist_eq_norm] using hkg
  have hgsmall := (Metric.tendsto_nhds.mp (hcore g hg)) (ε / 2)
    (by positivity)
  filter_upwards [hgsmall] with lam hlam
  change dist (f08_030_nativeFrequencyDilation lam.1 lam.2 k) k < ε
  rw [dist_eq_norm]
  have hcore_norm :
      ‖f08_030_nativeFrequencyDilation lam.1 lam.2 g - g‖ < ε / 2 := by
    simpa only [dist_eq_norm] using hlam
  calc
    ‖f08_030_nativeFrequencyDilation lam.1 lam.2 k - k‖ ≤
        2 * ‖k - g‖ +
          ‖f08_030_nativeFrequencyDilation lam.1 lam.2 g - g‖ :=
      f08_035_nativeFrequencyDilation_approximation_bound lam.1 lam.2 k g
    _ < ε := by linarith

#print axioms f08_038_nativeL2_tendsto_of_dense_core

end
end WeilDefect
