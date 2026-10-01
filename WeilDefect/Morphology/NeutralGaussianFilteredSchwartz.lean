import WeilDefect.Morphology.NeutralGaussianSchwartzSeed
import Mathlib.Analysis.Fourier.Convolution
import Mathlib.Analysis.Fourier.Inversion

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped Convolution FourierTransform SchwartzMap Topology

/-- The compactly supported physical representative is globally L1. -/
theorem neutralPhysicalRepresentative_integrable
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    Integrable carrier.h volume := by
  exact
    (neutralPhysicalRepresentative_integrableOn carrier).integrable_of_forall_notMem_eq_zero
      (fun x hx => carrier.representative_eq_zero_of_not_mem hx)

/--
Frequency-side Schwartz realization of the filtered mode.

The carrier Fourier transform is only used as a temperate multiplier; the
Gaussian Fourier transform supplies the Schwartz factor.
-/
def movingGaussianFrequencyProductSchwartz
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    𝓢(ℝ, ℂ) :=
  SchwartzMap.smulLeftCLM ℂ
    (𝓕 carrier.h)
    (𝓕 (movingGaussianPhysicalKernelSchwartz Ck R hR))

@[simp]
theorem movingGaussianFrequencyProductSchwartz_apply
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (ξ : ℝ) :
    movingGaussianFrequencyProductSchwartz Ck R hR carrier ξ
      =
    𝓕
      (carrier.h ⋆[ContinuousLinearMap.mul ℂ ℂ]
        (movingGaussianPhysicalKernelSchwartz Ck R hR : ℝ → ℂ)) ξ := by
  rw [movingGaussianFrequencyProductSchwartz]
  rw [SchwartzMap.smulLeftCLM_apply_apply
    (neutralPhysicalRepresentative_fourier_hasTemperateGrowth carrier)]
  simp only [smul_eq_mul]
  rw [SchwartzMap.fourier_coe]
  symm
  exact Real.fourier_mul_convolution_eq
    (neutralPhysicalRepresentative_integrable carrier)
    (movingGaussianPhysicalKernelSchwartz Ck R hR).integrable
    ξ

/-- The moving filtered mode bundled in Schwartz space via Fourier inversion. -/
def movingGaussianFilteredModeSchwartz
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    𝓢(ℝ, ℂ) :=
  𝓕⁻ (movingGaussianFrequencyProductSchwartz Ck R hR carrier)

/--
The bundled Schwartz realization equals the whole-line convolution of the
physical representative with the moving Gaussian kernel.
-/
theorem movingGaussianFilteredModeSchwartz_eq_convolution
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (x : ℝ) :
    movingGaussianFilteredModeSchwartz Ck R hR carrier x
      =
    (carrier.h ⋆[ContinuousLinearMap.mul ℂ ℂ]
      (movingGaussianPhysicalKernelSchwartz Ck R hR : ℝ → ℂ)) x := by
  let k : 𝓢(ℝ, ℂ) := movingGaussianPhysicalKernelSchwartz Ck R hR
  let conv : ℝ → ℂ :=
    carrier.h ⋆[ContinuousLinearMap.mul ℂ ℂ] (k : ℝ → ℂ)
  let freq : 𝓢(ℝ, ℂ) :=
    movingGaussianFrequencyProductSchwartz Ck R hR carrier
  have hh : Integrable carrier.h volume :=
    neutralPhysicalRepresentative_integrable carrier
  have hk : Integrable (k : ℝ → ℂ) volume := k.integrable
  have hconvInt : Integrable conv volume := by
    exact hh.integrable_convolution (ContinuousLinearMap.mul ℂ ℂ) hk
  have hbounded :
      BddAbove (Set.range fun y : ℝ => ‖k y‖) :=
    ⟨SchwartzMap.seminorm ℝ 0 0 k,
      fun _ ⟨y, hy⟩ => hy ▸ SchwartzMap.norm_le_seminorm ℝ k y⟩
  have hconvCont : Continuous conv := by
    exact hbounded.continuous_convolution_right_of_integrable
      (ContinuousLinearMap.mul ℂ ℂ) hh k.continuous
  have hfreqEq :
      ∀ ξ : ℝ, freq ξ = 𝓕 conv ξ := by
    intro ξ
    simpa [freq, conv, k] using
      movingGaussianFrequencyProductSchwartz_apply
        Ck R hR carrier ξ
  have hfourierInt : Integrable (𝓕 conv) volume := by
    exact freq.integrable.congr
      (Eventually.of_forall fun ξ => hfreqEq ξ)
  have hinv :
      𝓕⁻ (𝓕 conv) = conv :=
    hconvCont.fourierInv_fourier_eq hconvInt hfourierInt
  calc
    movingGaussianFilteredModeSchwartz Ck R hR carrier x
        = 𝓕⁻ (freq : ℝ → ℂ) x := by
            rw [movingGaussianFilteredModeSchwartz]
            rw [SchwartzMap.fourierInv_coe]
    _ = 𝓕⁻ (𝓕 conv) x := by
          have hfuneq : (freq : ℝ → ℂ) = 𝓕 conv := funext hfreqEq
          rw [hfuneq]
    _ = conv x := by rw [hinv]
    _ =
      (carrier.h ⋆[ContinuousLinearMap.mul ℂ ℂ]
        (movingGaussianPhysicalKernelSchwartz Ck R hR : ℝ → ℂ)) x := rfl

/--
The Schwartz realization is pointwise exactly the existing F-3 filtered mode.
-/
@[simp]
theorem movingGaussianFilteredModeSchwartz_apply
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (x : ℝ) :
    movingGaussianFilteredModeSchwartz Ck R hR carrier x
      =
    movingGaussianFilteredMode Ck R carrier x := by
  rw [movingGaussianFilteredModeSchwartz_eq_convolution]
  unfold movingGaussianFilteredMode
  simp_rw [← movingGaussianPhysicalKernelSchwartz_apply Ck R hR]
  rw [MeasureTheory.convolution_def]
  simp only [ContinuousLinearMap.mul_apply']
  symm
  exact setIntegral_eq_integral_of_ae_compl_eq_zero
    (Eventually.of_forall fun y hy => by
      rw [carrier.representative_eq_zero_of_not_mem hy, zero_mul])

end

end WeilDefect
