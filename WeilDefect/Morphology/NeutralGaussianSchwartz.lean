import WeilDefect.Morphology.NeutralGaussianPairing
import Mathlib.Analysis.Fourier.FourierTransformDeriv

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped FourierTransform SchwartzMap Topology

/--
Compact support of the physical F-1 representative upgrades its L1
integrability to integrability of every polynomial norm moment.

No smoothness of the representative is used.
-/
theorem neutralPhysicalRepresentative_polynomialNorm_integrable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (n : ℕ) :
    Integrable
      (fun x : ℝ => ‖x‖ ^ n * ‖carrier.h x‖) volume := by
  have hbase :
      IntegrableOn carrier.h (Set.Icc (-c) c) volume :=
    neutralPhysicalRepresentative_integrableOn carrier
  have hweight :
      Continuous (fun x : ℝ => ‖x‖ ^ n) := by
    fun_prop
  have hnormOn :
      IntegrableOn
        (fun x : ℝ => ‖carrier.h x‖)
        (Set.Icc (-c) c) volume :=
    hbase.norm
  have hon :
      IntegrableOn
        (fun x : ℝ => ‖carrier.h x‖ * ‖x‖ ^ n)
        (Set.Icc (-c) c) volume :=
    hnormOn.mul_continuousOn hweight.continuousOn isCompact_Icc
  have hon' :
      IntegrableOn
        (fun x : ℝ => ‖x‖ ^ n * ‖carrier.h x‖)
        (Set.Icc (-c) c) volume := by
    simpa [mul_comm] using hon
  exact hon'.integrable_of_forall_notMem_eq_zero
    (fun x hx => by
      rw [carrier.representative_eq_zero_of_not_mem hx]
      simp)

/--
Equivalent scalar-moment form used by the one-dimensional Fourier derivative
API.
-/
theorem neutralPhysicalRepresentative_polynomialSmul_integrable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (n : ℕ) :
    Integrable
      (fun x : ℝ => x ^ n • carrier.h x) volume := by
  have hmeas :
      AEStronglyMeasurable
        (fun x : ℝ => x ^ n • carrier.h x) volume := by
    exact
      (show AEStronglyMeasurable (fun x : ℝ => x ^ n) volume from
        (by fun_prop : Continuous (fun x : ℝ => x ^ n)).aestronglyMeasurable).smul
          carrier.h_memLp.aestronglyMeasurable
  rw [← integrable_norm_iff hmeas]
  simpa [norm_smul, Real.norm_eq_abs] using
    neutralPhysicalRepresentative_polynomialNorm_integrable carrier n

/--
The Fourier transform of the compactly supported F-1 representative is
smooth to every order, despite the representative itself being only L2/L1.
-/
theorem neutralPhysicalRepresentative_fourier_contDiff
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    ContDiff ℝ ⊤ (𝓕 carrier.h) := by
  have h :
      ContDiff ℝ (↑(⊤ : ℕ∞)) (𝓕 carrier.h) := by
    apply Real.contDiff_fourier (N := (⊤ : ℕ∞))
    intro n hn
    exact neutralPhysicalRepresentative_polynomialNorm_integrable carrier n
  simpa using h

end

end WeilDefect
