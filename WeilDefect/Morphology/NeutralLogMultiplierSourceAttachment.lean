import WeilDefect.Morphology.NeutralLogPoleSourceAttachment

namespace WeilDefect

noncomputable section

open MeasureTheory ContinuousLinearMap
open scoped InnerProduct ComplexConjugate FourierTransform

private theorem boundedLogMultiplyMemLp
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) (f : RealComplexL2) :
    MemLp (fun x => m x * f x) 2 volume := by
  have hh : ∀ᵐ x ∂volume, ‖(fun x => m x * f x) x‖ ≤ B * ‖f x‖ := by
    filter_upwards [] with x
    simpa only [norm_mul] using mul_le_mul_of_nonneg_right (hb x) (norm_nonneg (f x))
  exact (Lp.memLp f).of_le_mul (hm.mul (Lp.aestronglyMeasurable f)) hh

private def boundedLogMultiplyLinear
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) : RealComplexL2 →ₗ[ℂ] RealComplexL2 where
  toFun f := (boundedLogMultiplyMemLp m hm B hb f).toLp (fun x => m x * f x)
  map_add' f g := by
    apply Lp.ext
    filter_upwards [(boundedLogMultiplyMemLp m hm B hb (f+g)).coeFn_toLp,
      (boundedLogMultiplyMemLp m hm B hb f).coeFn_toLp,
      (boundedLogMultiplyMemLp m hm B hb g).coeFn_toLp,
      Lp.coeFn_add f g,
      Lp.coeFn_add ((boundedLogMultiplyMemLp m hm B hb f).toLp _)
        ((boundedLogMultiplyMemLp m hm B hb g).toLp _)] with x hfg hf hg hadd hout
    simp only [hfg, hout, Pi.add_apply, hf, hg, hadd, mul_add]
  map_smul' z f := by
    apply Lp.ext
    filter_upwards [(boundedLogMultiplyMemLp m hm B hb (z • f)).coeFn_toLp,
      (boundedLogMultiplyMemLp m hm B hb f).coeFn_toLp,
      Lp.coeFn_smul z f,
      Lp.coeFn_smul z ((boundedLogMultiplyMemLp m hm B hb f).toLp _)]
      with x hzf hf hz hout
    change (boundedLogMultiplyMemLp m hm B hb (z • f)).toLp _ x =
      (z • (boundedLogMultiplyMemLp m hm B hb f).toLp _) x
    rw [hzf, hout, hz]
    simp only [Pi.smul_apply, smul_eq_mul]
    rw [hf]
    ring

private theorem boundedLogMultiplyLinear_norm_le
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) (f : RealComplexL2) :
    ‖boundedLogMultiplyLinear m hm B hb f‖ ≤ B * ‖f‖ := by
  apply Lp.norm_le_mul_norm_of_ae_le_mul
  filter_upwards [(boundedLogMultiplyMemLp m hm B hb f).coeFn_toLp] with x hx
  change ‖(boundedLogMultiplyMemLp m hm B hb f).toLp _ x‖ ≤ B * ‖f x‖
  rw [hx, norm_mul]
  exact
    mul_le_mul_of_nonneg_right (hb x) (norm_nonneg (f x))

private def boundedLogMultiply
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) : RealComplexL2 →L[ℂ] RealComplexL2 :=
  (boundedLogMultiplyLinear m hm B hb).mkContinuous B (boundedLogMultiplyLinear_norm_le m hm B hb)

private theorem boundedLogMultiply_coe
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) (f : RealComplexL2) :
    (boundedLogMultiply m hm B hb f : ℝ → ℂ) =ᵐ[volume] fun x => m x * f x :=
  (boundedLogMultiplyMemLp m hm B hb f).coeFn_toLp


/-- Actual normalized Weil multiplier in weighted form coordinates. -/
def neutralLogSymbolRatio (a ξ : ℝ) : ℂ :=
  ((rightLimitCompactWeilSymbolMathlib a ξ / logarithmicFourierWeight ξ : ℝ) : ℂ)

theorem neutralLogSymbolRatio_measurable
    (a : ℝ) (ha : RightLimitWeilSymbolTemperatePremise a) :
    AEStronglyMeasurable (neutralLogSymbolRatio a) volume := by
  have hc : Continuous (rightLimitCompactWeilSymbolMathlib a) :=
    Complex.continuous_re.comp ha.hasTemperateGrowth.1.continuous
  exact (Complex.continuous_ofReal.comp (hc.div logarithmicFourierWeight_continuous
    (fun ξ => ne_of_gt (lt_of_lt_of_le zero_lt_one
      (one_le_logarithmicFourierWeight ξ))))).aestronglyMeasurable

theorem neutralLogSymbolRatio_bound
    (a lowerC upperC shift : ℝ) (h0 : 0 ≤ lowerC)
    (hl : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
      rightLimitCompactWeilSymbolMathlib a ξ + shift)
    (hu : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
      upperC * logarithmicFourierWeight ξ) (ξ : ℝ) :
    ‖neutralLogSymbolRatio a ξ‖ ≤ |upperC| + |shift| := by
  have hw : 0 < logarithmicFourierWeight ξ :=
    lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight ξ)
  simp only [neutralLogSymbolRatio, Complex.norm_real, Real.norm_eq_abs,
    abs_div, abs_of_pos hw]
  exact (div_le_iff₀ hw).mpr
    (rightLimitWeil_absoluteSymbolBound lowerC upperC shift h0 hl hu ξ)

variable (a : ℝ) (ha : RightLimitWeilSymbolTemperatePremise a)
  (lowerC upperC shift : ℝ) (h0 : 0 ≤ lowerC)
  (hl : ∀ ξ, lowerC * logarithmicFourierWeight ξ ≤
    rightLimitCompactWeilSymbolMathlib a ξ + shift)
  (hu : ∀ ξ, rightLimitCompactWeilSymbolMathlib a ξ + shift ≤
    upperC * logarithmicFourierWeight ξ)

/-- Bounded multiplication is constructed from the retained comparison;
no new absolute bound or representation field is assumed. -/
def neutralLogSymbolMultiplication : RealComplexL2 →L[ℂ] RealComplexL2 :=
  boundedLogMultiply (neutralLogSymbolRatio a) (neutralLogSymbolRatio_measurable a ha)
    (|upperC| + |shift|) (neutralLogSymbolRatio_bound a lowerC upperC shift h0 hl hu)

/-- Compress the actual ratio to the concrete supported weighted subspace. -/
def neutralLogMultiplierOperator :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  ((neutralLogHilbertSubmodule a).toSubmodule.subtypeL)† ∘L
    neutralLogSymbolMultiplication a ha lowerC upperC shift h0 hl hu ∘L
      (neutralLogHilbertSubmodule a).toSubmodule.subtypeL

theorem neutralLogMultiplierOperator_mixed (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogMultiplierOperator a ha lowerC upperC shift h0 hl hu g) =
      ∫ ξ, conj ((𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (neutralLogPhysical g.val) : RealComplexL2) ξ := by
  change inner ℂ f
    (((neutralLogHilbertSubmodule a).toSubmodule.subtypeL)†
      (neutralLogSymbolMultiplication a ha lowerC upperC shift h0 hl hu g.val)) = _
  rw [adjoint_inner_right]
  change inner ℂ f.val
    (neutralLogSymbolMultiplication a ha lowerC upperC shift h0 hl hu g.val) = _
  rw [L2.inner_def]
  have hef : neutralLogWeightedL2 (neutralLogHilbertToCanonical f) = f.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse f)
  have heg : neutralLogWeightedL2 (neutralLogHilbertToCanonical g) = g.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse g)
  have hm := neutralLogWeightedL2_mixed_ae
    (neutralLogHilbertToCanonical f) (neutralLogHilbertToCanonical g)
  rw [hef, heg] at hm
  apply integral_congr_ae
  filter_upwards [hm, boundedLogMultiply_coe (neutralLogSymbolRatio a)
    (neutralLogSymbolRatio_measurable a ha) (|upperC|+|shift|)
    (neutralLogSymbolRatio_bound a lowerC upperC shift h0 hl hu) g.val]
    with ξ hmix hmul
  change conj (f.val ξ) *
    (neutralLogSymbolMultiplication a ha lowerC upperC shift h0 hl hu g.val ξ) = _
  change (boundedLogMultiply (neutralLogSymbolRatio a)
    (neutralLogSymbolRatio_measurable a ha) (|upperC|+|shift|)
    (neutralLogSymbolRatio_bound a lowerC upperC shift h0 hl hu) g.val) ξ = _ at hmul
  rw [hmul]
  calc
    _ = neutralLogSymbolRatio a ξ * (conj (f.val ξ) * g.val ξ) := by ring
    _ = neutralLogSymbolRatio a ξ *
        (conj ((𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) *
          (logarithmicFourierWeight ξ : ℂ) *
          (𝓕 (neutralLogPhysical g.val) : RealComplexL2) ξ) := by
      exact congrArg (fun z => neutralLogSymbolRatio a ξ * z) hmix
    _ = _ := by
      have hw : (logarithmicFourierWeight ξ : ℂ) ≠ 0 := by
        exact_mod_cast ne_of_gt (lt_of_lt_of_le zero_lt_one
          (one_le_logarithmicFourierWeight ξ))
      unfold neutralLogSymbolRatio
      rw [Complex.ofReal_div]
      field_simp
      <;> ring

/-- Actual multiplier-plus-pole realization in the form Hilbert norm. -/
def neutralLogWeilFormOperator :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  neutralLogMultiplierOperator a ha lowerC upperC shift h0 hl hu +
    neutralLogPoleOperator a

theorem neutralLogWeilFormOperator_mixed (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogWeilFormOperator a ha lowerC upperC shift h0 hl hu g) =
      (∫ ξ, conj ((𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (neutralLogPhysical g.val) : RealComplexL2) ξ) +
      (conj (sourceWindowMoment a (-(1/2)) (neutralLogPhysical f.val)) *
        sourceWindowMoment a (1/2) (neutralLogPhysical g.val) +
      conj (sourceWindowMoment a (1/2) (neutralLogPhysical f.val)) *
        sourceWindowMoment a (-(1/2)) (neutralLogPhysical g.val)) := by
  simp only [neutralLogWeilFormOperator, ContinuousLinearMap.add_apply,
    inner_add_right, neutralLogMultiplierOperator_mixed, neutralLogPoleOperator_mixed]

end

end WeilDefect
