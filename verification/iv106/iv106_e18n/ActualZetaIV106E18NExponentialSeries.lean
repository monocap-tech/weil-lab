import WeilDefect.Arithmetic.ActualZetaIV106E18ESeparatedPairing
import WeilDefect.Arithmetic.ActualZetaIV106E18K1PolynomialMoments
import Mathlib.Analysis.SpecificLimits.Normed

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap Convolution BigOperators Topology

def neutralIV106E18NRate (n : ℕ) : ℝ := 2*(n:ℝ)+1/2

def neutralIV106E18NWeight (f : ℝ → ℂ) (s : ℝ) : ℂ :=
  ∫ x, f x*(Real.exp (s*x):ℂ)

def neutralIV106E18NTerm (u f : ℝ → ℂ) (n : ℕ) : ℂ :=
  -(neutralIV106E18NWeight u (-neutralIV106E18NRate n) *
    neutralIV106E18NWeight f (neutralIV106E18NRate n))

theorem neutralIV106E18NWeighted_integrable (f : ℝ → ℂ)
    (hf : Continuous f) (hc : HasCompactSupport f) (s : ℝ) :
    Integrable (fun x => f x*(Real.exp (s*x):ℂ)) := by
  have h : Continuous (fun x => f x*(Real.exp (s*x):ℂ)) := hf.mul (by fun_prop)
  apply h.integrable_of_hasCompactSupport
  exact hc.mul_right

/-- Finite factoring only, with exact signed ordering on nonzero supports. -/
theorem neutralIV106E18NFinite (u : 𝓢(ℝ,ℂ)) (f : ℝ → ℂ)
    (hf : Continuous f) (hfc : HasCompactSupport f)
    (huc : HasCompactSupport (u : ℝ → ℂ))
    (horder : ∀ x y, u x ≠ 0 → f y ≠ 0 → y ≤ x) (N : ℕ) :
    -(∫ x, u x * neutralIV106E18DConvolution f N x) =
      ∑ n ∈ Finset.range N, neutralIV106E18NTerm u f n := by
  have hfi : Integrable f volume := hf.integrable_of_hasCompactSupport hfc
  have hpoint (x : ℝ) :
      u x * neutralIV106E18DConvolution f N x =
      ∑ n ∈ Finset.range N,
        (u x*(Real.exp (-neutralIV106E18NRate n*x):ℂ)) *
          neutralIV106E18NWeight f (neutralIV106E18NRate n) := by
    by_cases hx : u x = 0
    · simp [hx]
    unfold neutralIV106E18DConvolution
    rw [MeasureTheory.convolution_def]
    simp only [ContinuousLinearMap.mul_apply',neutralFiniteGaussKernelComplex_eq_sum,
      Finset.mul_sum]
    rw [integral_finsetSum (Finset.range N)]
    · rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro n hn
      have he : (∫ y, f y*neutralLaplaceKernel (2*(n:ℝ)+1/2) (x-y)) =
          (Real.exp (-neutralIV106E18NRate n*x):ℂ) *
            neutralIV106E18NWeight f (neutralIV106E18NRate n) := by
        unfold neutralIV106E18NWeight
        rw [← integral_const_mul]
        apply integral_congr_ae
        filter_upwards [] with y
        by_cases hy : f y = 0
        · simp [hy]
        unfold neutralLaplaceKernel neutralIV106E18NRate
        rw [abs_of_nonneg (sub_nonneg.mpr (horder x y hx hy)),
          show -(2*(n:ℝ)+1/2)*(x-y) =
            -(2*(n:ℝ)+1/2)*x+(2*(n:ℝ)+1/2)*y by ring,
          Real.exp_add,Complex.ofReal_mul]
        ring
      rw [he]
      ring
    · intro n hn
      apply neutralIV106E18EKernel_integrable f _ hfi
        (show Continuous (neutralLaplaceKernel (2*(n:ℝ)+1/2)) by
          unfold neutralLaplaceKernel; fun_prop) 1
      intro z
      simp only [neutralLaplaceKernel,Complex.norm_real,Real.norm_eq_abs,
        abs_of_pos (Real.exp_pos _)]
      rw [← Real.exp_zero]
      exact Real.exp_le_exp.mpr (mul_nonpos_of_nonpos_of_nonneg (by positivity) (abs_nonneg _))
  simp_rw [hpoint]
  rw [integral_finsetSum (Finset.range N)]
  · simp only [integral_mul_const,neutralIV106E18NTerm,neutralIV106E18NWeight,Finset.sum_neg_distrib]
  · intro n hn
    exact (neutralIV106E18NWeighted_integrable u u.continuous huc
      (-neutralIV106E18NRate n)).mul_const _

/-- A one-sided support bound for the positive exponential weight. -/
theorem neutralIV106E18NWeight_upper (f : ℝ → ℂ) (hf : Continuous f)
    (hc : HasCompactSupport f) (a s : ℝ) (hs : 0 ≤ s)
    (ha : ∀ x, f x ≠ 0 → x ≤ a) :
    ‖neutralIV106E18NWeight f s‖ ≤
      Real.exp (s*a)*(∫ x, ‖f x‖) := by
  unfold neutralIV106E18NWeight
  calc
    _ ≤ ∫ x, ‖f x*(Real.exp (s*x):ℂ)‖ := norm_integral_le_integral_norm _
    _ ≤ ∫ x, Real.exp (s*a)*‖f x‖ := by
      apply integral_mono_ae (neutralIV106E18NWeighted_integrable f hf hc s).norm
        ((hf.integrable_of_hasCompactSupport hc : Integrable f volume).norm.const_mul (Real.exp (s*a)))
      filter_upwards [] with x
      by_cases hx : f x = 0
      · simp [hx]
      simp only [norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_pos (Real.exp_pos _)]
      rw [mul_comm (Real.exp (s*a))]
      exact mul_le_mul_of_nonneg_left
        (Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_left (ha x hx) hs)) (norm_nonneg _)
    _ = _ := by rw [integral_const_mul]

theorem neutralIV106E18NWeight_lower (u : ℝ → ℂ) (hu : Continuous u)
    (hc : HasCompactSupport u) (b s : ℝ) (hs : s ≤ 0)
    (hb : ∀ x, u x ≠ 0 → b ≤ x) :
    ‖neutralIV106E18NWeight u s‖ ≤
      Real.exp (s*b)*(∫ x, ‖u x‖) := by
  unfold neutralIV106E18NWeight
  calc
    _ ≤ ∫ x, ‖u x*(Real.exp (s*x):ℂ)‖ := norm_integral_le_integral_norm _
    _ ≤ ∫ x, Real.exp (s*b)*‖u x‖ := by
      apply integral_mono_ae (neutralIV106E18NWeighted_integrable u hu hc s).norm
        ((hu.integrable_of_hasCompactSupport hc : Integrable u volume).norm.const_mul (Real.exp (s*b)))
      filter_upwards [] with x
      by_cases hx : u x = 0
      · simp [hx]
      simp only [norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_pos (Real.exp_pos _)]
      rw [mul_comm (Real.exp (s*b))]
      exact mul_le_mul_of_nonneg_left
        (Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left (hb x hx) hs)) (norm_nonneg _)
    _ = _ := by rw [integral_const_mul]

/-- Each factorized term is absolutely bounded by a single geometric majorant.
No growth estimates of separate row or column weights are needed. -/
theorem neutralIV106E18NTerm_bound (u f : ℝ → ℂ)
    (hu : Continuous u) (huc : HasCompactSupport u)
    (hf : Continuous f) (hfc : HasCompactSupport f)
    (a b : ℝ) (hab : a < b)
    (hleft : ∀ y, f y ≠ 0 → y ≤ a)
    (hright : ∀ x, u x ≠ 0 → b ≤ x) (n : ℕ) :
    ‖neutralIV106E18NTerm u f n‖ ≤
      ((∫ x, ‖u x‖)*(∫ y, ‖f y‖)) * (Real.exp (-2*(b-a)))^n := by
  let r := neutralIV106E18NRate n
  have hr : 0 ≤ r := by dsimp [r,neutralIV106E18NRate]; positivity
  have hU := neutralIV106E18NWeight_lower u hu huc b (-r) (neg_nonpos.mpr hr) hright
  have hF := neutralIV106E18NWeight_upper f hf hfc a r hr hleft
  have hnU : 0 ≤ ∫ x, ‖u x‖ := integral_nonneg fun _ => norm_nonneg _
  have hnF : 0 ≤ ∫ y, ‖f y‖ := integral_nonneg fun _ => norm_nonneg _
  unfold neutralIV106E18NTerm
  rw [norm_neg,norm_mul]
  change ‖neutralIV106E18NWeight u (-r)‖ * ‖neutralIV106E18NWeight f r‖ ≤ _
  calc
    _ ≤ (Real.exp (-r*b)*(∫ x, ‖u x‖)) *
        (Real.exp (r*a)*(∫ y, ‖f y‖)) :=
      mul_le_mul hU hF (norm_nonneg _) (by positivity)
    _ = ((∫ x, ‖u x‖)*(∫ y, ‖f y‖)) * Real.exp (-r*(b-a)) := by
      rw [show -r*(b-a) = -r*b+r*a by ring,Real.exp_add]
      ring
    _ ≤ _ := by
      apply mul_le_mul_of_nonneg_left _ (mul_nonneg hnU hnF)
      rw [← Real.exp_nat_mul]
      apply Real.exp_le_exp.mpr
      dsimp [r,neutralIV106E18NRate]
      nlinarith only [hab]

/-- Infinite-series attachment by the previously certified physical limit,
not by an unjustified exchange across the singular diagonal. -/
theorem neutralIV106E18NSeries (u : 𝓢(ℝ,ℂ)) (f : ℝ → ℂ)
    (huc : HasCompactSupport (u : ℝ → ℂ))
    (hf : Continuous f) (hfc : HasCompactSupport f)
    (a b : ℝ) (hab : a < b)
    (hleft : ∀ y, f y ≠ 0 → y ≤ a)
    (hright : ∀ x, u x ≠ 0 → b ≤ x) :
    HasSum (neutralIV106E18NTerm u f)
      (∫ x, u x*(∫ y, f y*
        ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ):ℂ))) := by
  have hr : Real.exp (-2*(b-a)) < 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_lt_exp.mpr (by linarith)
  have hs : Summable (neutralIV106E18NTerm u f) :=
    ((summable_geometric_of_lt_one (Real.exp_nonneg _) hr).mul_left
      ((∫ x, ‖u x‖)*(∫ y, ‖f y‖))).of_norm_bounded
        (neutralIV106E18NTerm_bound u f u.continuous huc hf hfc a b hab hleft hright)
  have hsep : ∀ x y, u x ≠ 0 → f y ≠ 0 → b-a ≤ |x-y| := by
    intro x y hx hy
    exact (show b-a ≤ x-y by linarith [hright x hx,hleft y hy]).trans (le_abs_self _)
  have ht := neutralIV106E18EPhysical_limit f
    (hf.integrable_of_hasCompactSupport hfc) u (δ := b-a) (sub_pos.mpr hab) hsep
  have he : (∫ x, u x * neutralIV106E18EGap f (b-a) x) =
      ∫ x, u x*(∫ y, f y*
        ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ):ℂ)) := by
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
  rw [he] at ht
  simp_rw [neutralIV106E18NFinite u f hf hfc huc
    (fun x y hx hy => by linarith [hright x hx,hleft y hy])] at ht
  have heq := tendsto_nhds_unique hs.hasSum.tendsto_sum_nat ht
  rw [← heq]
  exact hs.hasSum

/-- The positive polynomial seed has positive exponential integral at every rate. -/
theorem neutralIV106E18NSeed_pos (q : ℝ) :
    0 < ∫ t in (0:ℝ)..1, Real.exp (q*t)*neutralIV106E18K1B t := by
  let g : ℝ → ℝ := fun t => Real.exp (q*t)*neutralIV106E18K1B t
  have hg : Continuous g := by dsimp [g,neutralIV106E18K1B]; fun_prop
  rw [intervalIntegral.integral_of_le (by norm_num : (0:ℝ) ≤ 1)]
  change 0 < ∫ t in Set.Ioc (0:ℝ) 1, g t
  have hi : IntegrableOn g (Set.Ioc (0:ℝ) 1) volume :=
    (intervalIntegrable_iff_integrableOn_Ioc_of_le (by norm_num : (0:ℝ) ≤ 1)).mp
      (hg.intervalIntegrable (μ := volume) 0 1)
  have hn : 0 ≤ᵐ[volume.restrict (Set.Ioc (0:ℝ) 1)] g := by
    filter_upwards [ae_restrict_mem measurableSet_Ioc] with x hx
    change 0 ≤ g x
    dsimp [g,neutralIV106E18K1B]
    exact mul_nonneg (Real.exp_pos _).le
      (mul_nonneg (pow_nonneg hx.1.le _) (pow_nonneg (sub_nonneg.mpr hx.2) _))
  apply (setIntegral_pos_iff_support_of_nonneg_ae hn hi).mpr
  have hsub : Set.Ioo (0:ℝ) 1 ⊆ Function.support g ∩ Set.Ioc (0:ℝ) 1 := by
    intro x hx
    refine ⟨?_,⟨hx.1,hx.2.le⟩⟩
    change g x ≠ 0
    dsimp [g,neutralIV106E18K1B]
    exact (mul_pos (Real.exp_pos _)
      (mul_pos (pow_pos hx.1 _) (pow_pos (sub_pos.mpr hx.2) _))).ne'
  have hp : 0 < volume (Set.Ioo (0:ℝ) 1) := by rw [Real.volume_Ioo]; norm_num
  exact hp.trans_le (measure_mono hsub)

/-- The unit-cell exponential transform has a strictly positive negative
coefficient above the pole rate, with no numerical quadrature. -/
theorem neutralIV106E18NPolynomial_sign (h s : ℝ) (hh : 0 < h) (hs : 1/2 < s) :
    0 < -(∫ t in (0:ℝ)..1, Real.exp ((s*h)*t)*neutralIV106E18K1Poly h t) := by
  rw [neutralIV106E18K1Transform,← neg_mul]
  apply mul_pos _ (neutralIV106E18NSeed_pos (s*h))
  have hq : h/2 < s*h := by nlinarith only [mul_pos (sub_pos.mpr hs) hh]
  have hq0 : 0 < s*h := by positivity
  have hd : 0 < (s*h)^2-h^2/4 := by nlinarith only [mul_pos (sub_pos.mpr hq) (show 0 < s*h+h/2 by positivity)]
  nlinarith only [mul_pos hq0 hd]

#print axioms neutralIV106E18NWeighted_integrable
#print axioms neutralIV106E18NFinite
#print axioms neutralIV106E18NWeight_upper
#print axioms neutralIV106E18NWeight_lower
#print axioms neutralIV106E18NTerm_bound
#print axioms neutralIV106E18NSeries
#print axioms neutralIV106E18NSeed_pos
#print axioms neutralIV106E18NPolynomial_sign
end
end WeilDefect
