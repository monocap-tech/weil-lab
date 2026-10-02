import WeilDefect.Morphology.NeutralLaplaceFourier
import Mathlib.Analysis.Fourier.Convolution

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped BigOperators Convolution FourierTransform SchwartzMap

def neutralFiniteGaussKernelComplex (N : ℕ) (x : ℝ) : ℂ :=
  Complex.ofReal (neutralFiniteGaussKernel N x)

theorem neutralFiniteGaussKernelComplex_eq_sum (N : ℕ) (x : ℝ) :
    neutralFiniteGaussKernelComplex N x =
      ∑ n ∈ Finset.range N, neutralLaplaceKernel (2*(n : ℝ)+1/2) x := by
  unfold neutralFiniteGaussKernelComplex neutralFiniteGaussKernel
  rw [Finset.mul_sum]
  simp only [Complex.ofReal_sum]
  apply Finset.sum_congr rfl
  intro n hn
  unfold neutralLaplaceKernel
  congr 1
  rw [← Real.exp_nat_mul, ← Real.exp_add]
  congr 1
  ring

theorem neutralFiniteGaussKernelComplex_integrable (N : ℕ) :
    Integrable (neutralFiniteGaussKernelComplex N) volume := by
  simp_rw [neutralFiniteGaussKernelComplex_eq_sum]
  exact integrable_finsetSum _ (fun n _ => neutralLaplaceKernel_integrable (by positivity))

/-- Finite interchange is justified by genuine integrability of every term. -/
theorem neutralFiniteGaussKernelComplex_fourier (N : ℕ) (ξ : ℝ) :
    𝓕 (neutralFiniteGaussKernelComplex N) ξ =
      (∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  simp_rw [neutralFiniteGaussKernelComplex_eq_sum, Finset.smul_sum]
  rw [integral_finsetSum (Finset.range N)]
  · simp_rw [← Real.fourier_real_eq_integral_exp_smul, neutralGaussReciprocal_fourier]
    simp only [Complex.ofReal_sum]
  · intro n hn
    exact (Real.fourierIntegral_convergent_iff ξ).mpr
      (neutralLaplaceKernel_integrable (by positivity))

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

def neutralFiniteGaussConvolution
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ) : ℝ → ℂ :=
  carrier.h ⋆[ContinuousLinearMap.mul ℂ ℂ] neutralFiniteGaussKernelComplex N

theorem neutralFiniteGaussConvolution_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ) :
    Integrable (neutralFiniteGaussConvolution carrier N) volume :=
  (neutralPhysicalRepresentative_integrable carrier).integrable_convolution
    (ContinuousLinearMap.mul ℂ ℂ) (neutralFiniteGaussKernelComplex_integrable N)

/-- Actual rough-carrier transfer; no pointwise boundedness of the carrier. -/
theorem neutralFiniteGaussConvolution_fourier
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ) (ξ : ℝ) :
    𝓕 (neutralFiniteGaussConvolution carrier N) ξ =
      𝓕 carrier.h ξ *
        (∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) := by
  rw [neutralFiniteGaussConvolution, Real.fourier_mul_convolution_eq
    (neutralPhysicalRepresentative_integrable carrier)
    (neutralFiniteGaussKernelComplex_integrable N), neutralFiniteGaussKernelComplex_fourier]

theorem neutralFiniteGaussConvolution_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ)
    (u : SchwartzMap ℝ ℂ) :
    Integrable (fun x => u x * neutralFiniteGaussConvolution carrier N x) volume := by
  have hq := neutralFiniteGaussConvolution_integrable carrier N
  apply (hq.norm.const_mul (SchwartzMap.seminorm ℝ 0 0 u)).mono'
    (u.continuous.aestronglyMeasurable.mul hq.aestronglyMeasurable)
  filter_upwards with x
  rw [norm_mul]
  exact mul_le_mul_of_nonneg_right (SchwartzMap.norm_le_seminorm ℝ u x) (norm_nonneg _)

/-- Weak transfer on every Schwartz test, with the inverse-test sign fixed
by Fourier inversion and a lawful L1 Fubini theorem. -/
theorem neutralFiniteGaussConvolution_weak_fourier
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ)
    (u : SchwartzMap ℝ ℂ) :
    (∫ x, u x * neutralFiniteGaussConvolution carrier N x) =
      ∫ ξ, 𝓕⁻ u ξ * (𝓕 carrier.h ξ *
        (∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ)) := by
  have h := VectorFourier.integral_bilin_fourierIntegral_eq_flip
    (ContinuousLinearMap.mul ℂ ℂ) (L := innerₗ ℝ ℝ)
    Real.continuous_fourierChar continuous_inner (𝓕⁻ u).integrable
    (neutralFiniteGaussConvolution_integrable carrier N)
  have hu : 𝓕 (fun x : ℝ => 𝓕⁻ u x) = (u : ℝ → ℂ) := by
    rw [← SchwartzMap.fourier_coe, FourierTransform.fourier_fourierInv_eq]
  simpa only [ContinuousLinearMap.mul_apply', ← SchwartzMap.fourierInv_coe,
    hu, neutralFiniteGaussConvolution_fourier] using h

end

end WeilDefect
