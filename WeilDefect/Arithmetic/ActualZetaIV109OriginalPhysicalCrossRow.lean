import WeilDefect.Arithmetic.ActualZetaIV103OriginalSchwartzSpectralAttachment
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- A smooth original row has squared-symbol integrability, unlike an
arbitrary member of the one-logarithm form domain. -/
theorem neutralIV109Weight_sq_le (ξ : ℝ) :
    logarithmicFourierWeight ξ ^ 2 ≤
      (2 * (Real.exp 1)^2 + 2) * (Real.exp 1 + 1 + ξ^2) := by
  have he : 0 < Real.exp 1 := Real.exp_pos _
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ)
  have hb : logarithmicFourierWeight ξ ≤ Real.exp 1 + |ξ| := by
    unfold logarithmicFourierWeight
    exact Real.log_le_self (by positivity)
  have hs := pow_le_pow_left₀ hw hb 2
  have hmid : (Real.exp 1 + |ξ|)^2 ≤ 2*(Real.exp 1)^2 + 2*ξ^2 := by
    nlinarith only [sq_nonneg (Real.exp 1 - |ξ|), sq_abs ξ]
  have hC : 0 ≤ 2*(Real.exp 1)^2+2 := by positivity
  have hh : 2*(Real.exp 1)^2 + 2*ξ^2 ≤
      (2*(Real.exp 1)^2+2)*(Real.exp 1+1+ξ^2) := by
    nlinarith only [mul_nonneg hC he.le,
      mul_nonneg (sq_nonneg (Real.exp 1)) (sq_nonneg ξ)]
  exact hs.trans (hmid.trans hh)

def neutralIV109SpectralRow (a : ℝ) (u : 𝓢(ℝ,ℂ)) (ξ : ℝ) : ℂ :=
  (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
    (𝓕 (u.toLp 2 volume) : RealComplexL2) ξ

theorem neutralIV109SpectralRow_memLp (a : ℝ) (u : 𝓢(ℝ,ℂ)) :
    MemLp (neutralIV109SpectralRow a u) 2 volume := by
  have hm : AEStronglyMeasurable (neutralIV109SpectralRow a u) volume :=
    (Complex.continuous_ofReal.comp
      (neutralActualZetaNativeSymbol_continuous a)).aestronglyMeasurable.mul
      (Lp.aestronglyMeasurable _)
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  let C : ℝ := (1+neutralActualZetaNativeLogError a)^2
  let H : ℝ := 2*(Real.exp 1)^2+2
  apply ((neutralSchwartzPhysical_quadraticFourierMoment u).const_mul (C*H)).mono'
  · exact hm.norm.pow 2
  · filter_upwards [] with ξ
    have h1 := pow_le_pow_left₀ (abs_nonneg _)
      (neutralActualZetaNativeSymbol_abs_log_le a ξ) 2
    have h2 : |rightLimitCompactWeilSymbolMathlib a ξ|^2 ≤
        C*H*(Real.exp 1+1+ξ^2) := by
      calc
        _ ≤ C*logarithmicFourierWeight ξ^2 := by
          simpa only [C, mul_pow] using h1
        _ ≤ C*(H*(Real.exp 1+1+ξ^2)) :=
          mul_le_mul_of_nonneg_left (neutralIV109Weight_sq_le ξ) (sq_nonneg _)
        _ = _ := by ring
    simp only [neutralIV109SpectralRow, norm_mul, Complex.norm_real,
      Real.norm_eq_abs, mul_pow, abs_mul,
      abs_of_nonneg (sq_nonneg (|rightLimitCompactWeilSymbolMathlib a ξ|)),
      abs_of_nonneg (sq_nonneg ‖(𝓕 (u.toLp 2 volume) : RealComplexL2) ξ‖)]
    calc
      _ ≤ (C*H*(Real.exp 1+1+ξ^2))*‖(𝓕 (u.toLp 2 volume) : RealComplexL2) ξ‖^2 :=
        mul_le_mul_of_nonneg_right h2 (sq_nonneg _)
      _ = _ := by ring

def neutralIV109SpectralRowL2 (a : ℝ) (u : 𝓢(ℝ,ℂ)) : RealComplexL2 :=
  (neutralIV109SpectralRow_memLp a u).toLp (neutralIV109SpectralRow a u)

theorem neutralIV109SpectralRow_pair (a : ℝ) (u v : 𝓢(ℝ,ℂ)) :
    inner ℂ (neutralIV109SpectralRowL2 a u) (𝓕 (v.toLp 2 volume) : RealComplexL2) =
      ∫ ξ : ℝ, conj ((𝓕 (u.toLp 2 volume) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ := by
  simp only [L2.inner_def, RCLike.inner_apply']
  apply integral_congr_ae
  filter_upwards [(neutralIV109SpectralRow_memLp a u).coeFn_toLp] with ξ hξ
  change conj (neutralIV109SpectralRowL2 a u ξ) * _ = _
  rw [show neutralIV109SpectralRowL2 a u ξ = neutralIV109SpectralRow a u ξ from hξ]
  simp only [neutralIV109SpectralRow, map_mul, Complex.conj_ofReal]
  ring

/-- Exact fixed-row physical continuity constant; no residual regularity
beyond its stated original support is used in the bound. -/
def neutralIV109RowConstant (a : ℝ) (u : 𝓢(ℝ,ℂ)) : ℝ :=
  ‖neutralIV109SpectralRowL2 a u‖ +
  ‖sourceWindowMoment a (-(1/2)) (u.toLp 2 volume)‖ *
    ‖neutralMomentColumnL2 a (1/2)‖ +
  ‖sourceWindowMoment a (1/2) (u.toLp 2 volume)‖ *
    ‖neutralMomentColumnL2 a (-(1/2))‖

theorem neutralIV109RowConstant_nonneg (a : ℝ) (u : 𝓢(ℝ,ℂ)) :
    0 ≤ neutralIV109RowConstant a u := by
  unfold neutralIV109RowConstant
  positivity

theorem neutralIV109Mixed_physical_bound (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    ‖neutralIV101Mixed a u v‖ ≤ neutralIV109RowConstant a u * ‖v.toLp 2 volume‖ := by
  rw [neutralIV103Mixed_native a ha u v hu hv,
    neutralActualZetaLogWeilFormOperator_mixed, neutralLogPoleOperator_mixed,
    neutralIV102Lift_physical, neutralIV102Lift_physical,
    ← neutralIV109SpectralRow_pair]
  have h0 := norm_inner_le_norm (𝕜 := ℂ) (neutralIV109SpectralRowL2 a u)
    (𝓕 (v.toLp 2 volume) : RealComplexL2)
  rw [Lp.norm_fourier_eq] at h0
  have h1 : ‖sourceWindowMoment a (1/2) (v.toLp 2 volume)‖ ≤
      ‖neutralMomentColumnL2 a (1/2)‖ * ‖v.toLp 2 volume‖ := by
    rw [← neutralMomentColumnL2_inner]
    exact norm_inner_le_norm _ _
  have h2 : ‖sourceWindowMoment a (-(1/2)) (v.toLp 2 volume)‖ ≤
      ‖neutralMomentColumnL2 a (-(1/2))‖ * ‖v.toLp 2 volume‖ := by
    rw [← neutralMomentColumnL2_inner]
    exact norm_inner_le_norm _ _
  have h3 := mul_le_mul_of_nonneg_left h1
    (norm_nonneg (sourceWindowMoment a (-(1/2)) (u.toLp 2 volume)))
  have h4 := mul_le_mul_of_nonneg_left h2
    (norm_nonneg (sourceWindowMoment a (1/2) (u.toLp 2 volume)))
  refine (norm_add_le _ _).trans ?_
  have hp := norm_add_le
    (conj (sourceWindowMoment a (-(1/2)) (u.toLp 2 volume)) *
      sourceWindowMoment a (1/2) (v.toLp 2 volume))
    (conj (sourceWindowMoment a (1/2) (u.toLp 2 volume)) *
      sourceWindowMoment a (-(1/2)) (v.toLp 2 volume))
  simp only [norm_mul, Complex.norm_conj] at hp
  unfold neutralIV109RowConstant
  rw [add_mul, add_mul]
  nlinarith only [h0, h3, h4, hp]

/-- Unconditional Garding transfer to the literal Schwartz diagonal. -/
theorem neutralIV109Original_garding (a : ℝ) (ha : 0 ≤ a) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    ‖neutralIV102Lift a v hv‖^2 ≤ neutralIV101Q a v +
      (neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
        ‖v.toLp 2 volume‖^2 :=
  neutralIV102Original_garding_of_attachment a v hv
    (neutralIV103Mixed_native a ha v v hv hv)

#print axioms neutralIV109Weight_sq_le
#print axioms neutralIV109SpectralRow_memLp
#print axioms neutralIV109SpectralRow_pair
#print axioms neutralIV109RowConstant_nonneg
#print axioms neutralIV109Mixed_physical_bound
#print axioms neutralIV109Original_garding

end
end WeilDefect
