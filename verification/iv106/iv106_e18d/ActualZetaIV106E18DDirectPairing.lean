import WeilDefect.Morphology.NeutralDigammaCancellation
import WeilDefect.Morphology.NeutralFiniteGaussConvolution
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace WeilDefect
noncomputable section
open MeasureTheory Filter FourierTransform
open scoped FourierTransform SchwartzMap Topology BigOperators RealInnerProductSpace

/-- Center each finite reciprocal sum before taking its frequency limit. -/
def neutralIV106E18DPartial (N : ℕ) (ξ : ℝ) : ℝ :=
  ∑ n ∈ Finset.range N, (neutralGaussReciprocal n 0 -
    neutralGaussReciprocal n (2*Real.pi*ξ))

theorem neutralIV106E18DPartial_tendsto (ξ : ℝ) :
    Tendsto (fun N => neutralIV106E18DPartial N ξ) atTop
      (𝓝 (compactWindowArchimedeanSymbol (2*Real.pi*ξ) -
        compactWindowArchimedeanSymbol 0)) := by
  have h := (neutralDigammaLine_centered_reciprocal_hasSum (2*Real.pi*ξ)).neg
  have he : (fun n : ℕ => -(neutralGaussReciprocal n (2*Real.pi*ξ) -
      neutralGaussReciprocal n 0)) =
      fun n => neutralGaussReciprocal n 0 - neutralGaussReciprocal n (2*Real.pi*ξ) := by
    funext n
    ring
  rw [he] at h
  unfold neutralIV106E18DPartial
  convert h.tendsto_sum_nat using 1
  unfold compactWindowArchimedeanSymbol neutralDigammaLine
  ring

theorem neutralIV106E18DPartial_bound (N : ℕ) (ξ : ℝ) :
    0 ≤ neutralIV106E18DPartial N ξ ∧
      neutralIV106E18DPartial N ξ ≤
        64*Real.pi^2*neutralCenteredDigammaCubicMass*ξ^2 := by
  have hs : Summable (fun n : ℕ => 64*(2*Real.pi*ξ/2)^2 / ((n:ℝ)+1)^3) := by
    simpa only [div_eq_mul_inv, one_mul] using
      neutralCenteredDigammaCubic_summable.mul_left (64*(2*Real.pi*ξ/2)^2)
  constructor
  · exact Finset.sum_nonneg (fun n _ =>
      (neutralGaussReciprocal_centered_bound n (2*Real.pi*ξ)).1)
  · unfold neutralIV106E18DPartial
    calc
      _ ≤ ∑ n ∈ Finset.range N, 64*(2*Real.pi*ξ/2)^2 / ((n:ℝ)+1)^3 :=
        Finset.sum_le_sum (fun n _ =>
          (neutralGaussReciprocal_centered_bound n (2*Real.pi*ξ)).2)
      _ ≤ ∑' n : ℕ, 64*(2*Real.pi*ξ/2)^2 / ((n:ℝ)+1)^3 :=
        hs.sum_le_tsum (Finset.range N) (fun n _ => by positivity)
      _ = _ := by
        simp only [neutralCenteredDigammaCubicMass, div_eq_mul_inv, one_mul, tsum_mul_left]
        ring

/-- Finite physical convolution for arbitrary L1 input, with the literal
normalization from the already proved finite Gauss kernel transform. -/
def neutralIV106E18DConvolution (f : ℝ → ℂ) (N : ℕ) : ℝ → ℂ :=
  f ⋆[ContinuousLinearMap.mul ℂ ℂ] neutralFiniteGaussKernelComplex N

theorem neutralIV106E18DFinite_pair (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) (N : ℕ) :
    (∫ x, u x * neutralIV106E18DConvolution f N x) =
      ∫ ξ, (𝓕⁻ u) ξ * (𝓕 f ξ *
        (∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ)) := by
  have hg : Integrable (neutralIV106E18DConvolution f N) :=
    hf.integrable_convolution (ContinuousLinearMap.mul ℂ ℂ)
      (neutralFiniteGaussKernelComplex_integrable N)
  have hh := VectorFourier.integral_bilin_fourierIntegral_eq_flip
    (ContinuousLinearMap.mul ℂ ℂ) (L := innerₗ ℝ) (μ := volume) (ν := volume)
    Real.continuous_fourierChar continuous_inner (𝓕⁻ u).integrable hg
  have hh' : (∫ x, 𝓕 ((𝓕⁻ u : 𝓢(ℝ,ℂ)) : ℝ → ℂ) x *
      neutralIV106E18DConvolution f N x) =
      ∫ ξ, (𝓕⁻ u) ξ * 𝓕 (neutralIV106E18DConvolution f N) ξ := by
    change (∫ x, VectorFourier.fourierIntegral Real.fourierChar volume (innerₗ ℝ)
      ((𝓕⁻ u : 𝓢(ℝ,ℂ)) : ℝ → ℂ) x * neutralIV106E18DConvolution f N x) =
      ∫ ξ, (𝓕⁻ u) ξ * VectorFourier.fourierIntegral Real.fourierChar volume
        (innerₗ ℝ) (neutralIV106E18DConvolution f N) ξ
    simpa [ContinuousLinearMap.mul_apply'] using! hh
  rw [← SchwartzMap.fourier_coe, FourierTransform.fourier_fourierInv_eq] at hh'
  simp_rw [neutralIV106E18DConvolution, Real.fourier_mul_convolution_eq hf
    (neutralFiniteGaussKernelComplex_integrable N), neutralFiniteGaussKernelComplex_fourier] at hh'
  exact hh'

/-- Direct centered frequency convergence for L1 input and Schwartz test.
The only majorant is a quadratic polynomial times the inverse Schwartz test. -/
theorem neutralIV106E18DDirect_limit (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) :
    Tendsto (fun N => ∫ ξ, (𝓕⁻ u) ξ * (𝓕 f ξ *
      (neutralIV106E18DPartial N ξ : ℂ))) atTop
      (𝓝 (∫ ξ, (𝓕⁻ u) ξ * (𝓕 f ξ *
        ((compactWindowArchimedeanSymbol (2*Real.pi*ξ) -
          compactWindowArchimedeanSymbol 0 : ℝ) : ℂ)))) := by
  let p : ℝ → ℂ := fun ξ => (ξ:ℂ)^2
  have hp : Function.HasTemperateGrowth p := by dsimp [p]; fun_prop
  let v := SchwartzMap.smulLeftCLM ℂ p (𝓕⁻ u)
  let C : ℝ := 64*Real.pi^2*neutralCenteredDigammaCubicMass*(∫ x, ‖f x‖)
  have hc : 0 ≤ C := by
    dsimp [C]
    exact mul_nonneg
      (mul_nonneg (by positivity) neutralCenteredDigammaCubicMass_nonneg)
      (integral_nonneg (fun _ => norm_nonneg _))
  have hF : Continuous (𝓕 f) :=
    VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar continuous_inner hf
  apply tendsto_integral_of_dominated_convergence (fun ξ => C*‖v ξ‖)
  · intro N
    have hP : Continuous (neutralIV106E18DPartial N) := by
      unfold neutralIV106E18DPartial neutralGaussReciprocal
      fun_prop (disch := positivity)
    exact (𝓕⁻ u).continuous.aestronglyMeasurable.mul
      (hF.aestronglyMeasurable.mul
        (Complex.continuous_ofReal.comp hP).aestronglyMeasurable)
  · exact v.integrable.norm.const_mul C
  · intro N
    filter_upwards [] with ξ
    have hb := neutralIV106E18DPartial_bound N ξ
    have hnorm : ‖𝓕 f ξ‖ ≤ ∫ x, ‖f x‖ := by
      rw [Real.fourier_real_eq]
      exact (norm_integral_le_integral_norm _).trans_eq (by simp)
    simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hb.1]
    calc
      _ ≤ ‖(𝓕⁻ u) ξ‖ * ((∫ x, ‖f x‖) *
          (64*Real.pi^2*neutralCenteredDigammaCubicMass*ξ^2)) :=
        mul_le_mul_of_nonneg_left (mul_le_mul hnorm hb.2 hb.1
          (integral_nonneg (fun _ => norm_nonneg _))) (norm_nonneg _)
      _ = C*‖v ξ‖ := by
        simp only [v, SchwartzMap.smulLeftCLM_apply_apply hp, norm_smul, p,
          norm_pow, Complex.norm_real, Real.norm_eq_abs, sq_abs]
        dsimp [C]
        ring
  · filter_upwards [] with ξ
    exact tendsto_const_nhds.mul (tendsto_const_nhds.mul
      (Complex.continuous_ofReal.continuousAt.tendsto.comp
        (neutralIV106E18DPartial_tendsto ξ)))

/-- Limit comparison receiver: once the centered pairing equals the negative
finite convolution on disjoint supports and its physical limit is proved,
the literal centered Fourier pairing is identified, with no growth premise. -/
theorem neutralIV106E18DLimit_receiver (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) (P : ℂ)
    (hcontact : ∀ N, (∫ ξ, (𝓕⁻ u) ξ * (𝓕 f ξ *
      (neutralIV106E18DPartial N ξ : ℂ))) =
      -(∫ x, u x * neutralIV106E18DConvolution f N x))
    (hphysical : Tendsto (fun N => -(∫ x, u x * neutralIV106E18DConvolution f N x))
      atTop (𝓝 P)) :
    (∫ ξ, (𝓕⁻ u) ξ * (𝓕 f ξ *
        ((compactWindowArchimedeanSymbol (2*Real.pi*ξ) -
          compactWindowArchimedeanSymbol 0 : ℝ) : ℂ))) = P := by
  have h := neutralIV106E18DDirect_limit f hf u
  simp_rw [hcontact] at h
  exact tendsto_nhds_unique h hphysical

#print axioms neutralIV106E18DPartial_tendsto
#print axioms neutralIV106E18DPartial_bound
#print axioms neutralIV106E18DFinite_pair
#print axioms neutralIV106E18DDirect_limit
#print axioms neutralIV106E18DLimit_receiver
end
end WeilDefect
