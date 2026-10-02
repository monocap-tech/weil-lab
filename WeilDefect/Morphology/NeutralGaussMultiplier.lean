import WeilDefect.Morphology.NeutralFiniteGaussConvolution
import Mathlib.MeasureTheory.Integral.ExpDecay
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

namespace WeilDefect

noncomputable section

open MeasureTheory Filter
open scoped FourierTransform SchwartzMap ContDiff Topology BigOperators RealInnerProductSpace

/-- Exponential decay gives all actual polynomial norm moments. -/
theorem neutralLaplaceKernel_polynomialNorm_integrable {b : ℝ} (hb : 0 < b) (n : ℕ) :
    Integrable (fun x : ℝ => ‖x‖^n * ‖neutralLaplaceKernel b x‖) volume := by
  have hp : IntegrableOn (fun x : ℝ => Real.exp (-b*x) * x^n) (Set.Ici 0) volume :=
    integrableOn_exp_neg_mul_of_isBigO_exp
      ((by fun_prop : Continuous (fun x : ℝ => x^n)).continuousOn.locallyIntegrableOn
        measurableSet_Ici)
      (isLittleO_pow_exp_pos_mul_atTop n (half_pos hb)).isBigO (by linarith)
  let g : ℝ → ℝ := (Set.Ici 0).indicator (fun x => Real.exp (-b*x) * x^n)
  have hg : Integrable g volume := (integrable_indicator_iff measurableSet_Ici).mpr hp
  have hs := hg.add hg.comp_neg
  apply hs.norm.mono' (by unfold neutralLaplaceKernel; fun_prop)
  filter_upwards with x
  by_cases hx : x = 0
  · subst x
    simp [g, neutralLaplaceKernel, Complex.norm_real, Real.norm_eq_abs]
    cases n <;> norm_num
  · by_cases hxp : 0 < x
    · have hxn : ¬ 0 ≤ -x := by linarith
      simp [g, Pi.add_apply, neutralLaplaceKernel, Complex.norm_exp, Real.norm_eq_abs,
        abs_of_pos hxp, hxp.le, hxn, mul_comm]
    · have hxm : x < 0 := lt_of_le_of_ne (le_of_not_gt hxp) hx
      have hxnn : 0 ≤ -x := by linarith
      simp [g, Pi.add_apply, neutralLaplaceKernel, Complex.norm_exp, Real.norm_eq_abs,
        abs_of_neg hxm, not_le.mpr hxm, hxnn, mul_comm]

/-- General moment-based Fourier multiplier regularity; no physical smoothness. -/
theorem neutralMomentFourier_temperate {f : ℝ → ℂ}
    (hm : ∀ n : ℕ, Integrable (fun x : ℝ => ‖x‖^n * ‖f x‖) volume)
    (hf : AEStronglyMeasurable f volume) : Function.HasTemperateGrowth (𝓕 f) := by
  have hsm (n : ℕ) : Integrable (fun x : ℝ => x^n • f x) volume := by
    have hmeas : AEStronglyMeasurable (fun x : ℝ => x^n • f x) volume :=
      (by fun_prop : Continuous (fun x : ℝ => x^n)).aestronglyMeasurable.smul hf
    rw [← integrable_norm_iff hmeas]
    simpa [norm_smul, Real.norm_eq_abs] using hm n
  refine ⟨Real.contDiff_fourier (N := (⊤ : ℕ∞)) (fun n _ => hm n), ?_⟩
  intro n
  let g : ℝ → ℂ := fun x => (-2*Real.pi*Complex.I*x)^n • f x
  refine ⟨0, ∫ x : ℝ, ‖g x‖, ?_⟩
  intro ξ
  have hd : iteratedDeriv n (𝓕 f) = 𝓕 g := by
    simpa [g] using Real.iteratedDeriv_fourier (f := f) (N := (⊤ : ℕ∞))
      (n := n) (fun m _ => hsm m) le_top
  rw [norm_iteratedFDeriv_eq_norm_iteratedDeriv, hd]
  simp only [pow_zero, mul_one]
  rw [Real.fourier_real_eq]
  exact (norm_integral_le_integral_norm _).trans_eq (by simp [g])

theorem neutralFiniteGaussSymbol_temperate (N : ℕ) :
    Function.HasTemperateGrowth
      (fun ξ : ℝ => ((∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) : ℂ)) := by
  have hk : Function.HasTemperateGrowth (𝓕 (neutralFiniteGaussKernelComplex N)) := by
    apply neutralMomentFourier_temperate
    · intro k
      have hs := integrable_finsetSum (Finset.range N)
        (fun n _ => neutralLaplaceKernel_polynomialNorm_integrable
          (b := 2*(n : ℝ)+1/2) (by positivity) k)
      apply hs.mono' (by
        have hc : Continuous (neutralFiniteGaussKernelComplex N) := by
          unfold neutralFiniteGaussKernelComplex neutralFiniteGaussKernel
          fun_prop
        exact (by fun_prop : Continuous (fun x : ℝ => ‖x‖^k)).aestronglyMeasurable.mul
          hc.norm.aestronglyMeasurable)
      filter_upwards with x
      simp only [neutralFiniteGaussKernelComplex_eq_sum]
      rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (pow_nonneg (norm_nonneg x) k)
        (norm_nonneg _))]
      calc
        ‖x‖^k * ‖∑ n ∈ Finset.range N, neutralLaplaceKernel (2*(n : ℝ)+1/2) x‖
          ≤ ‖x‖^k * ∑ n ∈ Finset.range N, ‖neutralLaplaceKernel (2*(n : ℝ)+1/2) x‖ :=
            mul_le_mul_of_nonneg_left (norm_sum_le _ _) (pow_nonneg (norm_nonneg x) k)
        _ = _ := by rw [Finset.mul_sum]
    · exact (neutralFiniteGaussKernelComplex_integrable N).aestronglyMeasurable
  have heq : 𝓕 (neutralFiniteGaussKernelComplex N) =
      fun ξ : ℝ => ((∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) : ℂ) :=
    funext (neutralFiniteGaussKernelComplex_fourier N)
  rwa [heq] at hk

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The existing tempered multiplier consumes the actual finite physical convolution. -/
theorem neutralFiniteGaussMultiplier_physical_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (N : ℕ)
    (u : SchwartzMap ℝ ℂ) :
    TemperedDistribution.fourierMultiplierCLM ℂ
      (fun ξ : ℝ => ((∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) : ℂ))
      carrier.temperedMode u = ∫ x, u x * neutralFiniteGaussConvolution carrier N x := by
  let m : ℝ → ℂ := fun ξ => ((∑ n ∈ Finset.range N,
    neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) : ℂ)
  let v : SchwartzMap ℝ ℂ := SchwartzMap.smulLeftCLM ℂ m (𝓕⁻ u)
  rw [TemperedDistribution.fourierMultiplierCLM_apply_apply,
    neutralPhysical_temperedMode_apply, neutralFiniteGaussConvolution_weak_fourier]
  have ht : (∫ x, 𝓕 v x * carrier.h x) = ∫ ξ, v ξ * 𝓕 carrier.h ξ := by
    change (∫ x, VectorFourier.fourierIntegral Real.fourierChar volume
      (innerₗ ℝ) (v : ℝ → ℂ) x * carrier.h x) =
      ∫ ξ, v ξ * VectorFourier.fourierIntegral Real.fourierChar volume (innerₗ ℝ) carrier.h ξ
    simpa [ContinuousLinearMap.mul_apply'] using!
      VectorFourier.integral_bilin_fourierIntegral_eq_flip (ContinuousLinearMap.mul ℂ ℂ)
        (L := innerₗ ℝ) (μ := volume) (ν := volume)
        Real.continuous_fourierChar continuous_inner v.integrable
        (neutralPhysicalRepresentative_integrable carrier)
  change (∫ x, 𝓕 v x * carrier.h x) = _
  rw [ht]
  apply integral_congr_ae
  filter_upwards with ξ
  dsimp [v]
  rw [SchwartzMap.smulLeftCLM_apply_apply (neutralFiniteGaussSymbol_temperate N)]
  simp only [smul_eq_mul]
  ring

end

end WeilDefect
