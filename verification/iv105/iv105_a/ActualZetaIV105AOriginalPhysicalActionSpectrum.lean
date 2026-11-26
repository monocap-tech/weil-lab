import WeilDefect.Arithmetic.ActualZetaIV103OriginalSchwartzSpectralAttachment
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- A square envelope for the actual logarithmic weight. -/
theorem neutralIV105AWeight_sq_le (ξ : ℝ) :
    logarithmicFourierWeight ξ ^ 2 ≤
      (2 * (Real.exp 1 ^ 2 + 1)) * (Real.exp 1 + 1 + ξ ^ 2) := by
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have he : 0 ≤ Real.exp 1 := (Real.exp_pos _).le
  have hl : logarithmicFourierWeight ξ ≤ Real.exp 1 + |ξ| := by
    unfold logarithmicFourierWeight
    exact Real.log_le_self (add_nonneg he (abs_nonneg ξ))
  calc
    _ ≤ (Real.exp 1 + |ξ|) ^ 2 := pow_le_pow_left₀ hw hl 2
    _ ≤ 2 * (Real.exp 1 ^ 2 + ξ ^ 2) := by
      nlinarith only [sq_nonneg (Real.exp 1 - |ξ|), sq_abs ξ]
    _ ≤ (2 * (Real.exp 1 ^ 2 + 1)) * (1 + ξ ^ 2) := by
      nlinarith only [mul_nonneg (sq_nonneg (Real.exp 1)) (sq_nonneg ξ)]
    _ ≤ _ := mul_le_mul_of_nonneg_left (by linarith) (by positivity)

/-- Actual signed symbol times the physical Fourier image is square integrable.
No physical strong-action bound is postulated. -/
theorem neutralIV105ASpectrum_memLp (a : ℝ) (s : 𝓢(ℝ,ℂ)) :
    MemLp (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
      (𝓕 (s.toLp 2 volume) : RealComplexL2) ξ) 2 volume := by
  let F : RealComplexL2 := 𝓕 (s.toLp 2 volume)
  let D : ℝ := 1 + neutralActualZetaNativeLogError a
  let B : ℝ := 2 * (Real.exp 1 ^ 2 + 1)
  have hD : 0 ≤ D := by
    dsimp [D]
    linarith [(neutralActualZetaNativeLogError_spec a).1]
  have hB : 0 ≤ B := by dsimp [B]; positivity
  have hm : AEStronglyMeasurable
      (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) * F ξ) volume :=
    (Complex.continuous_ofReal.comp
      (neutralActualZetaNativeSymbol_continuous a)).aestronglyMeasurable.mul
        (Lp.aestronglyMeasurable F)
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hMoment := (neutralSchwartzPhysical_quadraticFourierMoment s).const_mul (D^2*B)
  apply hMoment.mono'
  · exact hm.norm.pow 2
  · filter_upwards [] with ξ
    have hs : |rightLimitCompactWeilSymbolMathlib a ξ| ≤
        D * logarithmicFourierWeight ξ :=
      neutralActualZetaNativeSymbol_abs_log_le a ξ
    have h1 := pow_le_pow_left₀ (abs_nonneg _) hs 2
    have h2 := mul_le_mul_of_nonneg_left (neutralIV105AWeight_sq_le ξ) (sq_nonneg D)
    have h3 : |rightLimitCompactWeilSymbolMathlib a ξ| ^ 2 ≤
        (D^2*B) * (Real.exp 1 + 1 + ξ^2) := by
      calc
        _ ≤ (D * logarithmicFourierWeight ξ)^2 := h1
        _ = D^2 * logarithmicFourierWeight ξ ^ 2 := by ring
        _ ≤ D^2 * (B * (Real.exp 1 + 1 + ξ^2)) := h2
        _ = _ := by ring
    rw [Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _), norm_mul,
      Complex.norm_real, Real.norm_eq_abs, mul_pow]
    change _ ≤ (D^2*B) * ((Real.exp 1 + 1 + ξ^2) * ‖F ξ‖^2)
    rw [← mul_assoc]
    exact mul_le_mul_of_nonneg_right h3 (sq_nonneg _)

def neutralIV105ASpectrum (a : ℝ) (s : 𝓢(ℝ,ℂ)) : RealComplexL2 :=
  (neutralIV105ASpectrum_memLp a s).toLp _

theorem neutralIV105ASpectrum_ae (a : ℝ) (s : 𝓢(ℝ,ℂ)) :
    (neutralIV105ASpectrum a s : ℝ → ℂ) =ᵐ[volume]
      fun ξ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (s.toLp 2 volume) : RealComplexL2) ξ :=
  (neutralIV105ASpectrum_memLp a s).coeFn_toLp

/-- Exact signed multiplier pairing in the physical Fourier L2 metric. -/
theorem neutralIV105ASpectrum_pair (a : ℝ) (u v : 𝓢(ℝ,ℂ)) :
    inner ℂ (neutralIV105ASpectrum a u) (𝓕 (v.toLp 2 volume) : RealComplexL2) =
      ∫ ξ, conj ((𝓕 (u.toLp 2 volume) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ := by
  rw [MeasureTheory.L2.inner_def]
  apply integral_congr_ae
  filter_upwards [neutralIV105ASpectrum_ae a u] with ξ hξ
  simp only [RCLike.inner_apply', hξ, map_mul, Complex.conj_ofReal]
  ring

/-- Exact original mixed form, retaining the actual crossed-pole operator. -/
theorem neutralIV105AMixed_spectrum_pole (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Mixed a u v =
      inner ℂ (neutralIV105ASpectrum a u) (𝓕 (v.toLp 2 volume) : RealComplexL2) +
      inner ℂ (neutralIV102Lift a u hu)
        (neutralLogPoleOperator a (neutralIV102Lift a v hv)) := by
  rw [neutralIV103Mixed_native a ha u v hu hv,
    neutralActualZetaLogWeilFormOperator_mixed,
    neutralIV102Lift_physical, neutralIV102Lift_physical,
    neutralIV105ASpectrum_pair]

#print axioms neutralIV105AWeight_sq_le
#print axioms neutralIV105ASpectrum_memLp
#print axioms neutralIV105ASpectrum_ae
#print axioms neutralIV105ASpectrum_pair
#print axioms neutralIV105AMixed_spectrum_pole
end
end WeilDefect
