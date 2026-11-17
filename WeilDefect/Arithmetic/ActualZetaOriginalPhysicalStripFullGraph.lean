import WeilDefect.Arithmetic.ActualZetaOriginalStripLogConvergence
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointLogGeometry
import WeilDefect.Arithmetic.ActualZetaOriginalLogStripGraphLimit

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped ComplexConjugate

/-!
NF575: physical L² convergence and a common endpoint-log strip
majorant now suffice for complete graph convergence, without
having to assume the logarithmic Hilbert convergence separately.
The actual supported target and seed estimates remain explicit.
-/

theorem neutralNF575OriginalPhysicalSequence_fullGraph_of_strip
    (f : RealComplexL2) (g : ℕ → RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0)
    (hg : ∀ n, ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → g n x = 0)
    (hl2 : Tendsto g atTop (nhds f))
    (M : ℝ) (hM : 0 ≤ M)
    (hft : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z f‖ ≤ M*neutralNF575StripEnvelope z.re)
    (hgt : ∀ n (z : ℂ), |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z (g n)‖ ≤ M*neutralNF575StripEnvelope z.re) :
    ∃ (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (G : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) K).val = f ∧
      (∀ n, neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) (G n)).val = g n) ∧
      Tendsto G atTop (nhds K) := by
  obtain ⟨k,v,hk,hv,hconv⟩ :=
    neutralNF575PhysicalSequence_logLimit_of_strip (11/10:ℝ) f g
      hf hg hl2 M hM hft hgt
  have hkt : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z (neutralLogPhysical k.val)‖ ≤
        M*neutralNF574StripEnvelope z.re := by
    intro z hz
    rw [hk]
    exact hft z hz
  have hvt : ∀ n (z : ℂ), |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z (neutralLogPhysical (v n).val)‖ ≤
        M*neutralNF574StripEnvelope z.re := by
    intro n z hz
    rw [hv n]
    exact hgt n z hz
  obtain ⟨K,G,hK,hG,hlim⟩ :=
    neutralNF574OriginalFullSourceLimit_of_stripEnvelope k v hconv M hM hkt hvt
  refine ⟨K,G,?_,?_,hlim⟩
  · rw [hK,hk]
  · intro n
    rw [hG n,hv n]

/-- The historical NF523 bound on the ORIGINAL U400 source is
2·10⁻⁷. The source identity and proof of that bound in Lean
are retained input obligations, not inferred from a JSON receipt. -/
def neutralNF575OriginalEndpointL2
    (U : ℝ → ℝ) (hm : Measurable U)
    (hU : ∀ x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ),
      |U x| ≤ 2/10^7) : RealComplexL2 :=
  (neutralNF575OriginalEndpoint_memLp U hm (2/10^7)
    (by norm_num) hU).toLp (neutralNF575OriginalEndpoint U)

/-- Actual endpoint formula specialization. The physical target
is the literal nonsmooth log with the original collar boundaries.
A common full strip estimate and ordinary L² convergence of the
same real-odd collar seeds now suffice for complete graph entry and
convergence. No H^(1/4) or logarithmic-energy input is required.
The hypothesis that U is the frozen analytic source, and the
source-specific analytic strip estimates, must still be supplied. -/
theorem neutralNF575OriginalEndpoint_fullGraph_of_seedEstimates
    (U : ℝ → ℝ) (hm : Measurable U)
    (hU : ∀ x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ),
      |U x| ≤ 2/10^7)
    (g : ℕ → RealComplexL2)
    (hg : ∀ n, ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
      g n x = 0)
    (hl2 : Tendsto g atTop (nhds (neutralNF575OriginalEndpointL2 U hm hU)))
    (M : ℝ) (hM : 0 ≤ M)
    (hft : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z
        (neutralNF575OriginalEndpointL2 U hm hU)‖ ≤ M*neutralNF575StripEnvelope z.re)
    (hgt : ∀ n (z : ℂ), |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z (g n)‖ ≤ M*neutralNF575StripEnvelope z.re) :
    ∃ (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (G : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) K).val =
        neutralNF575OriginalEndpointL2 U hm hU ∧
      (∀ n, neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) (G n)).val = g n) ∧
      Tendsto G atTop (nhds K) := by
  apply neutralNF575OriginalPhysicalSequence_fullGraph_of_strip
    (neutralNF575OriginalEndpointL2 U hm hU) g _ hg hl2 M hM hft hgt
  exact (neutralNF575OriginalEndpoint_L2_properties U
    (neutralNF575OriginalEndpoint_memLp U hm (2/10^7)
      (by norm_num) hU)).1

end
end WeilDefect
