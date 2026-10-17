import WeilDefect.Morphology.NeutralLogMetricCapL2
import Mathlib.MeasureTheory.Measure.Interval
import Mathlib.MeasureTheory.Function.LpSeminorm.Indicator

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-- The two endpoints have zero volume, so the actual candidate is L2
on the closed cap as well. This asserts no endpoint convergence. -/
theorem neutralLogMetricEndpointCandidate_memLp_two_closed
    (B M L : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) :
    MemLp (neutralLogMetricEndpointCandidate B v) 2
      (volume.restrict (Icc (-B) B)) := by
  have he : volume.restrict (Ioo (-B) B) = volume.restrict (Icc (-B) B) :=
    Measure.restrict_congr_set (Ioo_ae_eq_Icc' (by simp) (by simp))
  rw [← he]
  exact neutralLogMetricEndpointCandidate_memLp_two B M L hB hL v hv hbound hmod

/-- The cap candidate extended by zero to the full physical line. -/
def neutralLogMetricEndpointZeroExtension (B : ℝ) (v : ℝ → ℂ) : ℝ → ℂ :=
  (Icc (-B) B).indicator (neutralLogMetricEndpointCandidate B v)

theorem neutralLogMetricEndpointZeroExtension_eq_zero
    (B : ℝ) (v : ℝ → ℂ) (x : ℝ) (hx : x ∉ Icc (-B) B) :
    neutralLogMetricEndpointZeroExtension B v x = 0 := by
  exact indicator_of_notMem hx _

/-- Full-line L2 membership of the actual zero-extended candidate. -/
theorem neutralLogMetricEndpointZeroExtension_memLp_two
    (B M L : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) :
    MemLp (neutralLogMetricEndpointZeroExtension B v) 2 volume := by
  apply (memLp_indicator_iff_restrict measurableSet_Icc).mpr
  exact neutralLogMetricEndpointCandidate_memLp_two_closed B M L hB hL v hv hbound hmod

/-- A physical L2 representative of the candidate, without an action or
spectral identity premise. Those identities still require proof. -/
def neutralLogMetricEndpointCandidateL2
    (B M L : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) : RealComplexL2 :=
  (neutralLogMetricEndpointZeroExtension_memLp_two B M L hB hL v hv hbound hmod).toLp
    (neutralLogMetricEndpointZeroExtension B v)

theorem neutralLogMetricEndpointCandidateL2_coe
    (B M L : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) :
    (neutralLogMetricEndpointCandidateL2 B M L hB hL v hv hbound hmod : ℝ → ℂ) =ᵐ[volume]
      neutralLogMetricEndpointZeroExtension B v :=
  (neutralLogMetricEndpointZeroExtension_memLp_two B M L hB hL v hv hbound hmod).coeFn_toLp

end
end WeilDefect
