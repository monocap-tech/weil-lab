import WeilDefect.Arithmetic.ActualZetaIV106E18DDirectPairing
import WeilDefect.Morphology.NeutralGaussExteriorLimit

namespace WeilDefect
noncomputable section
open MeasureTheory Filter FourierTransform
open scoped FourierTransform SchwartzMap Topology BigOperators RealInnerProductSpace

/-- Fourier flip for L1 input and inverse Schwartz test, without a distribution. -/
theorem neutralIV106E18EFlip (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) :
    (∫ x, u x * f x) = ∫ ξ, (𝓕⁻ u) ξ * 𝓕 f ξ := by
  have hh := VectorFourier.integral_bilin_fourierIntegral_eq_flip
    (ContinuousLinearMap.mul ℂ ℂ) (L := innerₗ ℝ) (μ := volume) (ν := volume)
    Real.continuous_fourierChar continuous_inner (𝓕⁻ u).integrable hf
  have hh' : (∫ x, 𝓕 ((𝓕⁻ u : 𝓢(ℝ,ℂ)) : ℝ → ℂ) x * f x) =
      ∫ ξ, (𝓕⁻ u) ξ * 𝓕 f ξ := by
    change (∫ x, VectorFourier.fourierIntegral Real.fourierChar volume (innerₗ ℝ)
      ((𝓕⁻ u : 𝓢(ℝ,ℂ)) : ℝ → ℂ) x * f x) =
      ∫ ξ, (𝓕⁻ u) ξ * VectorFourier.fourierIntegral Real.fourierChar volume
        (innerₗ ℝ) f ξ
    simpa [ContinuousLinearMap.mul_apply'] using! hh
  rw [← SchwartzMap.fourier_coe, FourierTransform.fourier_fourierInv_eq] at hh'
  exact hh'

theorem neutralIV106E18EFreq_integrable (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) :
    Integrable (fun ξ => (𝓕⁻ u) ξ * 𝓕 f ξ) := by
  have hc : Continuous (𝓕 f) :=
    VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar continuous_inner hf
  apply ((𝓕⁻ u).integrable.norm.mul_const (∫ x, ‖f x‖)).mono'
    ((𝓕⁻ u).continuous.aestronglyMeasurable.mul hc.aestronglyMeasurable)
  filter_upwards [] with ξ
  rw [norm_mul]
  apply mul_le_mul_of_nonneg_left _ (norm_nonneg _)
  rw [Real.fourier_real_eq]
  exact (norm_integral_le_integral_norm _).trans_eq (by simp)

/-- The finite centered contact term vanishes exactly, not asymptotically. -/
theorem neutralIV106E18EContact (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) (hu : ∀ x, u x * f x = 0) (N : ℕ) :
    (∫ ξ, (𝓕⁻ u) ξ * (𝓕 f ξ *
      (neutralIV106E18DPartial N ξ : ℂ))) =
      -(∫ x, u x * neutralIV106E18DConvolution f N x) := by
  let c : ℂ := (∑ n ∈ Finset.range N, neutralGaussReciprocal n 0 : ℝ)
  have hbase := neutralIV106E18EFreq_integrable f hf u
  have hconv : Integrable (neutralIV106E18DConvolution f N) :=
    hf.integrable_convolution (ContinuousLinearMap.mul ℂ ℂ)
      (neutralFiniteGaussKernelComplex_integrable N)
  have hfreq := neutralIV106E18EFreq_integrable _ hconv u
  have heq (ξ : ℝ) : 𝓕 (neutralIV106E18DConvolution f N) ξ =
      𝓕 f ξ * (∑ n ∈ Finset.range N, neutralGaussReciprocal n (2*Real.pi*ξ) : ℝ) := by
    rw [neutralIV106E18DConvolution, Real.fourier_mul_convolution_eq hf
      (neutralFiniteGaussKernelComplex_integrable N), neutralFiniteGaussKernelComplex_fourier]
  have hzero : (∫ ξ, (𝓕⁻ u) ξ * 𝓕 f ξ) = 0 := by
    rw [← neutralIV106E18EFlip f hf u]
    simp [hu]
  have hsplit (ξ : ℝ) : (𝓕⁻ u) ξ * (𝓕 f ξ *
      (neutralIV106E18DPartial N ξ : ℂ)) =
      c * ((𝓕⁻ u) ξ * 𝓕 f ξ) -
      (𝓕⁻ u) ξ * 𝓕 (neutralIV106E18DConvolution f N) ξ := by
    rw [heq]
    unfold neutralIV106E18DPartial
    rw [Finset.sum_sub_distrib, Complex.ofReal_sub]
    dsimp [c]
    ring
  simp_rw [hsplit]
  rw [integral_sub (hbase.const_mul c) hfreq, integral_const_mul, hzero,
    ← neutralIV106E18EFlip _ hconv u]
  ring

/-- Bounded continuous kernels genuinely integrate against arbitrary L1 inputs. -/
theorem neutralIV106E18EKernel_integrable (f k : ℝ → ℂ)
    (hf : Integrable f) (hk : Continuous k) (C : ℝ)
    (hb : ∀ z, ‖k z‖ ≤ C) (x : ℝ) :
    Integrable (fun y => f y * k (x-y)) := by
  apply (hf.norm.mul_const C).mono'
    (hf.aestronglyMeasurable.mul
      (hk.comp (continuous_const.sub continuous_id)).aestronglyMeasurable)
  filter_upwards [] with y
  rw [norm_mul]
  exact mul_le_mul_of_nonneg_left (hb _) (norm_nonneg _)

theorem neutralIV106E18EFinite_bound (N : ℕ) (z : ℝ) :
    ‖neutralFiniteGaussKernelComplex N z‖ ≤ N := by
  have h₁ : Real.exp (-|z|/2) ≤ 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by linarith [abs_nonneg z])
  have h₂ : Real.exp (-2*|z|) ≤ 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by linarith [abs_nonneg z])
  have hsum : (∑ n ∈ Finset.range N, (Real.exp (-2*|z|))^n) ≤ (N : ℝ) := by
    calc
      _ ≤ ∑ _n ∈ Finset.range N, (1 : ℝ) :=
        Finset.sum_le_sum (fun n _ => pow_le_one₀ (Real.exp_nonneg _) h₂)
      _ = _ := by simp
  rw [neutralFiniteGaussKernelComplex, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (neutralFiniteGaussKernel_nonneg N z)]
  unfold neutralFiniteGaussKernel
  exact (mul_le_mul_of_nonneg_right h₁
    (Finset.sum_nonneg (fun _ _ => by positivity))).trans (by simpa using hsum)

def neutralIV106E18EGap (f : ℝ → ℂ) (δ : ℝ) : ℝ → ℂ :=
  f ⋆[ContinuousLinearMap.mul ℂ ℂ] archimedeanGapKernelComplex δ

theorem neutralIV106E18EGap_continuous (f : ℝ → ℂ) (hf : Integrable f)
    {δ : ℝ} (hδ : 0 < δ) :
    Continuous (neutralIV106E18EGap f δ) := by
  have hb : BddAbove (Set.range (fun z => ‖archimedeanGapKernelComplex δ z‖)) := by
    refine ⟨1 / (1 - Real.exp (-2*δ)), ?_⟩
    rintro _ ⟨z, rfl⟩
    exact archimedeanGapKernelComplex_norm_bound hδ z
  exact hb.continuous_convolution_right_of_integrable (ContinuousLinearMap.mul ℂ ℂ)
    hf (archimedeanGapKernelComplex_continuous hδ)

theorem neutralIV106E18EGap_bound (f : ℝ → ℂ) (hf : Integrable f)
    {δ : ℝ} (hδ : 0 < δ) (x : ℝ) :
    ‖neutralIV106E18EGap f δ x‖ ≤
      (1 / (1 - Real.exp (-2*δ))) * (∫ y, ‖f y‖) := by
  let C : ℝ := 1 / (1 - Real.exp (-2*δ))
  have hi := neutralIV106E18EKernel_integrable f _ hf
    (archimedeanGapKernelComplex_continuous hδ) C
    (archimedeanGapKernelComplex_norm_bound hδ) x
  unfold neutralIV106E18EGap
  rw [MeasureTheory.convolution_def]
  simp only [ContinuousLinearMap.mul_apply']
  calc
    _ ≤ ∫ y, ‖f y * archimedeanGapKernelComplex δ (x-y)‖ :=
      norm_integral_le_integral_norm _
    _ ≤ ∫ y, C * ‖f y‖ := by
      apply integral_mono_ae hi.norm (hf.norm.const_mul C)
      filter_upwards [] with y
      rw [norm_mul, mul_comm C]
      exact mul_le_mul_of_nonneg_left
        (archimedeanGapKernelComplex_norm_bound hδ _) (norm_nonneg _)
    _ = _ := by rw [integral_const_mul]

/-- Uniform tail error at each point of the nonzero test support. -/
theorem neutralIV106E18EPoint_error (f : ℝ → ℂ) (hf : Integrable f)
    {δ : ℝ} (hδ : 0 < δ) (N : ℕ) (x : ℝ)
    (hsep : ∀ y, f y ≠ 0 → δ ≤ |x-y|) :
    ‖neutralIV106E18DConvolution f N x + neutralIV106E18EGap f δ x‖ ≤
      ((1 / (1 - Real.exp (-2*δ))) * (Real.exp (-2*δ))^N) *
        (∫ y, ‖f y‖) := by
  let B : ℝ := (1 / (1 - Real.exp (-2*δ))) * (Real.exp (-2*δ))^N
  have hk : Continuous (neutralFiniteGaussKernelComplex N) := by
    unfold neutralFiniteGaussKernelComplex neutralFiniteGaussKernel
    fun_prop
  have hi := neutralIV106E18EKernel_integrable f _ hf hk (N : ℝ)
    (neutralIV106E18EFinite_bound N) x
  have hg := neutralIV106E18EKernel_integrable f _ hf
    (archimedeanGapKernelComplex_continuous hδ) _
    (archimedeanGapKernelComplex_norm_bound hδ) x
  have hd : 0 < 1 - Real.exp (-2*δ) := by
    have h := archimedeanGapKernel_denominator_pos hδ (0 : ℝ)
    simpa [max_eq_left hδ.le] using h
  have hB : 0 ≤ B := by dsimp [B]; positivity
  unfold neutralIV106E18DConvolution neutralIV106E18EGap
  simp only [MeasureTheory.convolution_def, ContinuousLinearMap.mul_apply']
  rw [← integral_add hi hg]
  calc
    _ ≤ ∫ y, ‖f y * neutralFiniteGaussKernelComplex N (x-y) +
      f y * archimedeanGapKernelComplex δ (x-y)‖ := norm_integral_le_integral_norm _
    _ ≤ ∫ y, B * ‖f y‖ := by
      apply integral_mono_ae (hi.add hg).norm (hf.norm.const_mul B)
      filter_upwards [] with y
      simp only [Pi.add_apply]
      by_cases hy : f y = 0
      · simp [hy]
      · rw [← mul_add, norm_mul, mul_comm B]
        exact mul_le_mul_of_nonneg_left
          (neutralFiniteGaussKernel_gap_error N hδ (hsep y hy)) (norm_nonneg _)
    _ = _ := by rw [integral_const_mul]

theorem neutralIV106E18EPhysical_limit (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) {δ : ℝ} (hδ : 0 < δ)
    (hsep : ∀ x y, u x ≠ 0 → f y ≠ 0 → δ ≤ |x-y|) :
    Tendsto (fun N => -(∫ x, u x * neutralIV106E18DConvolution f N x))
      atTop (𝓝 (∫ x, u x * neutralIV106E18EGap f δ x)) := by
  let C : ℝ := (1 / (1 - Real.exp (-2*δ))) * (∫ y, ‖f y‖)
  have hg : Integrable (fun x => u x * neutralIV106E18EGap f δ x) := by
    apply (u.integrable.norm.mul_const C).mono'
      (u.continuous.aestronglyMeasurable.mul
        (neutralIV106E18EGap_continuous f hf hδ).aestronglyMeasurable)
    filter_upwards [] with x
    rw [norm_mul]
    exact mul_le_mul_of_nonneg_left
      (neutralIV106E18EGap_bound f hf hδ x) (norm_nonneg _)
  have hf' (N : ℕ) : Integrable (fun x => u x * neutralIV106E18DConvolution f N x) := by
    have hq : Integrable (neutralIV106E18DConvolution f N) :=
      hf.integrable_convolution (ContinuousLinearMap.mul ℂ ℂ)
        (neutralFiniteGaussKernelComplex_integrable N)
    apply (hq.norm.const_mul (SchwartzMap.seminorm ℝ 0 0 u)).mono'
      (u.continuous.aestronglyMeasurable.mul hq.aestronglyMeasurable)
    filter_upwards [] with x
    rw [norm_mul]
    exact mul_le_mul_of_nonneg_right (SchwartzMap.norm_le_seminorm ℝ u x) (norm_nonneg _)
  have herr (N : ℕ) :
      ‖(∫ x, u x * neutralIV106E18DConvolution f N x) +
        ∫ x, u x * neutralIV106E18EGap f δ x‖ ≤
      (((1 / (1 - Real.exp (-2*δ))) * (Real.exp (-2*δ))^N) *
        (∫ y, ‖f y‖)) * (∫ x, ‖u x‖) := by
    let B : ℝ := ((1 / (1 - Real.exp (-2*δ))) * (Real.exp (-2*δ))^N) *
      (∫ y, ‖f y‖)
    rw [← integral_add (hf' N) hg]
    calc
      _ ≤ ∫ x, ‖u x * neutralIV106E18DConvolution f N x +
          u x * neutralIV106E18EGap f δ x‖ := norm_integral_le_integral_norm _
      _ ≤ ∫ x, B * ‖u x‖ := by
        apply integral_mono_ae ((hf' N).add hg).norm (u.integrable.norm.const_mul B)
        filter_upwards [] with x
        simp only [Pi.add_apply]
        by_cases hx : u x = 0
        · simp [hx]
        · rw [← mul_add, norm_mul, mul_comm B]
          exact mul_le_mul_of_nonneg_left
            (neutralIV106E18EPoint_error f hf hδ N x (fun y hy => hsep x y hx hy))
            (norm_nonneg _)
      _ = _ := by rw [integral_const_mul]
  have hr : Real.exp (-2*δ) < 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_lt_exp.mpr (by linarith)
  have hp := tendsto_pow_atTop_nhds_zero_of_lt_one (Real.exp_nonneg (-2*δ)) hr
  have hb : Tendsto (fun N : ℕ =>
      (((1 / (1 - Real.exp (-2*δ))) * (Real.exp (-2*δ))^N) *
        (∫ y, ‖f y‖)) * (∫ x, ‖u x‖)) atTop (𝓝 0) := by
    simpa using ((tendsto_const_nhds.mul hp).mul_const
      (∫ y, ‖f y‖)).mul_const (∫ x, ‖u x‖)
  have hn : Tendsto (fun N => ‖(∫ x, u x * neutralIV106E18DConvolution f N x) +
      ∫ x, u x * neutralIV106E18EGap f δ x‖) atTop (𝓝 0) :=
    squeeze_zero (fun _ => norm_nonneg _) herr hb
  have ht : Tendsto (fun N => ∫ x, u x * neutralIV106E18DConvolution f N x)
      atTop (𝓝 (-(∫ x, u x * neutralIV106E18EGap f δ x))) := by
    apply tendsto_iff_norm_sub_tendsto_zero.mpr
    simpa only [sub_neg_eq_add] using hn
  simpa only [neg_neg] using ht.neg

/-- Literal separated integral with the singular kernel only evaluated off
the diagonal on the nonzero product support. -/
theorem neutralIV106E18ELiteral (f : ℝ → ℂ) (hf : Integrable f)
    (u : 𝓢(ℝ,ℂ)) {δ : ℝ} (hδ : 0 < δ)
    (hsep : ∀ x y, u x ≠ 0 → f y ≠ 0 → δ ≤ |x-y|) :
    (∫ ξ, (𝓕⁻ u) ξ * (𝓕 f ξ *
      ((compactWindowArchimedeanSymbol (2*Real.pi*ξ) -
        compactWindowArchimedeanSymbol 0 : ℝ) : ℂ))) =
    ∫ x, u x * (∫ y, f y *
      ((-(Real.exp (-|x-y|/2) / (1 - Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  have hu (x : ℝ) : u x * f x = 0 := by
    by_cases hx : u x = 0
    · simp [hx]
    by_cases hy : f x = 0
    · simp [hy]
    have h := hsep x x hx hy
    simp at h
    linarith
  rw [neutralIV106E18DLimit_receiver f hf u _
    (neutralIV106E18EContact f hf u hu)
    (neutralIV106E18EPhysical_limit f hf u hδ hsep)]
  apply integral_congr_ae
  filter_upwards [] with x
  by_cases hx : u x = 0
  · simp [hx]
  congr 1
  unfold neutralIV106E18EGap
  rw [MeasureTheory.convolution_def]
  simp only [ContinuousLinearMap.mul_apply']
  apply integral_congr_ae
  filter_upwards [] with y
  by_cases hy : f y = 0
  · simp [hy]
  rw [archimedeanGapKernelComplex_eq_offDiagonal (hsep x y hx hy)]

#print axioms neutralIV106E18EFlip
#print axioms neutralIV106E18EFreq_integrable
#print axioms neutralIV106E18EContact
#print axioms neutralIV106E18EKernel_integrable
#print axioms neutralIV106E18EFinite_bound
#print axioms neutralIV106E18EGap_continuous
#print axioms neutralIV106E18EGap_bound
#print axioms neutralIV106E18EPoint_error
#print axioms neutralIV106E18EPhysical_limit
#print axioms neutralIV106E18ELiteral
end
end WeilDefect
