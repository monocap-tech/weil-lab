import WeilDefect.Arithmetic.ActualZetaCanonicalNativeEnergy
import WeilDefect.Arithmetic.ActualZetaHilbertSourceGraph

namespace WeilDefect
noncomputable section
open MeasureTheory ContinuousLinearMap
open scoped InnerProduct ComplexConjugate FourierTransform
set_option maxHeartbeats 800000

private theorem nativeMultiplyMemLp
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) (f : RealComplexL2) :
    MemLp (fun x => m x * f x) 2 volume := by
  have hh : ∀ᵐ x ∂volume, ‖(fun x => m x * f x) x‖ ≤ B * ‖f x‖ := by
    filter_upwards [] with x
    simpa only [norm_mul] using mul_le_mul_of_nonneg_right (hb x) (norm_nonneg (f x))
  exact (Lp.memLp f).of_le_mul (hm.mul (Lp.aestronglyMeasurable f)) hh

private def nativeMultiplyLinear
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) : RealComplexL2 →ₗ[ℂ] RealComplexL2 where
  toFun f := (nativeMultiplyMemLp m hm B hb f).toLp (fun x => m x * f x)
  map_add' f g := by
    apply Lp.ext
    filter_upwards [(nativeMultiplyMemLp m hm B hb (f+g)).coeFn_toLp,
      (nativeMultiplyMemLp m hm B hb f).coeFn_toLp,
      (nativeMultiplyMemLp m hm B hb g).coeFn_toLp,
      Lp.coeFn_add f g,
      Lp.coeFn_add ((nativeMultiplyMemLp m hm B hb f).toLp _)
        ((nativeMultiplyMemLp m hm B hb g).toLp _)] with x hfg hf hg hadd hout
    simp only [hfg, hout, Pi.add_apply, hf, hg, hadd, mul_add]
  map_smul' z f := by
    apply Lp.ext
    filter_upwards [(nativeMultiplyMemLp m hm B hb (z • f)).coeFn_toLp,
      (nativeMultiplyMemLp m hm B hb f).coeFn_toLp,
      Lp.coeFn_smul z f,
      Lp.coeFn_smul z ((nativeMultiplyMemLp m hm B hb f).toLp _)]
      with x hzf hf hz hout
    change (nativeMultiplyMemLp m hm B hb (z • f)).toLp _ x =
      (z • (nativeMultiplyMemLp m hm B hb f).toLp _) x
    rw [hzf, hout, hz]
    simp only [Pi.smul_apply, smul_eq_mul]
    rw [hf]
    ring

private theorem nativeMultiplyLinear_norm_le
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) (f : RealComplexL2) :
    ‖nativeMultiplyLinear m hm B hb f‖ ≤ B * ‖f‖ := by
  apply Lp.norm_le_mul_norm_of_ae_le_mul
  filter_upwards [(nativeMultiplyMemLp m hm B hb f).coeFn_toLp] with x hx
  change ‖(nativeMultiplyMemLp m hm B hb f).toLp _ x‖ ≤ B * ‖f x‖
  rw [hx, norm_mul]
  exact
    mul_le_mul_of_nonneg_right (hb x) (norm_nonneg (f x))

private def nativeMultiply
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) : RealComplexL2 →L[ℂ] RealComplexL2 :=
  (nativeMultiplyLinear m hm B hb).mkContinuous B (nativeMultiplyLinear_norm_le m hm B hb)

private theorem nativeMultiply_coe
    (m : ℝ → ℂ) (hm : AEStronglyMeasurable m volume)
    (B : ℝ) (hb : ∀ x, ‖m x‖ ≤ B) (f : RealComplexL2) :
    (nativeMultiply m hm B hb f : ℝ → ℂ) =ᵐ[volume] fun x => m x * f x :=
  (nativeMultiplyMemLp m hm B hb f).coeFn_toLp



/-- Actual ratio measurability is proved from zeroth-order continuity. -/
theorem neutralActualZetaLogSymbolRatio_measurable (a : ℝ) :
    AEStronglyMeasurable (neutralLogSymbolRatio a) volume := by
  exact (Complex.continuous_ofReal.comp
    ((neutralActualZetaNativeSymbol_continuous a).div
      logarithmicFourierWeight_continuous (fun ξ => ne_of_gt
        (lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight ξ))))).aestronglyMeasurable

theorem neutralActualZetaLogSymbolRatio_bound (a ξ : ℝ) :
    ‖neutralLogSymbolRatio a ξ‖ ≤ 1 + neutralActualZetaNativeLogError a := by
  have hw : 0 < logarithmicFourierWeight ξ :=
    lt_of_lt_of_le zero_lt_one (one_le_logarithmicFourierWeight ξ)
  simp only [neutralLogSymbolRatio, Complex.norm_real, Real.norm_eq_abs,
    abs_div, abs_of_pos hw]
  exact (div_le_iff₀ hw).mpr (neutralActualZetaNativeSymbol_abs_log_le a ξ)

/-- Actual bounded multiplication on weighted L2, using only proved bounds. -/
def neutralActualZetaLogSymbolMultiplication (a : ℝ) : RealComplexL2 →L[ℂ] RealComplexL2 :=
  nativeMultiply (neutralLogSymbolRatio a) (neutralActualZetaLogSymbolRatio_measurable a)
    (1 + neutralActualZetaNativeLogError a) (neutralActualZetaLogSymbolRatio_bound a)

theorem neutralActualZetaLogSymbolMultiplication_coe (a : ℝ) (f : RealComplexL2) :
    (neutralActualZetaLogSymbolMultiplication a f : ℝ → ℂ) =ᵐ[volume]
      fun ξ => neutralLogSymbolRatio a ξ * f ξ :=
  nativeMultiply_coe _ _ _ _ f

theorem neutralActualZetaLogSymbolMultiplication_norm_le (a : ℝ) (f : RealComplexL2) :
    ‖neutralActualZetaLogSymbolMultiplication a f‖ ≤
      (1 + neutralActualZetaNativeLogError a) * ‖f‖ :=
  nativeMultiplyLinear_norm_le (neutralLogSymbolRatio a)
    (neutralActualZetaLogSymbolRatio_measurable a) (1 + neutralActualZetaNativeLogError a)
    (neutralActualZetaLogSymbolRatio_bound a) f

/-- Compress the actual ratio to the complete supported logarithmic carrier.
This is a form-norm operator, not an ordinary physical L2 spectral operator. -/
def neutralActualZetaLogMultiplierOperator (a : ℝ) :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  (ContinuousLinearMap.adjoint (𝕜 := ℂ)
    (E := NeutralLogHilbertCarrier a) (F := RealComplexL2)
    (neutralLogHilbertSubmodule a).toSubmodule.subtypeL) ∘L
  neutralActualZetaLogSymbolMultiplication a ∘L
    (neutralLogHilbertSubmodule a).toSubmodule.subtypeL

/-- Exact native mixed form on every vector of the complete logarithmic carrier. -/
theorem neutralActualZetaLogMultiplierOperator_mixed
    (a : ℝ) (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaLogMultiplierOperator a g) =
      ∫ ξ, conj ((𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (neutralLogPhysical g.val) : RealComplexL2) ξ := by
  change inner ℂ f
    ((ContinuousLinearMap.adjoint (𝕜 := ℂ)
      (E := NeutralLogHilbertCarrier a) (F := RealComplexL2)
      (neutralLogHilbertSubmodule a).toSubmodule.subtypeL)
      (neutralActualZetaLogSymbolMultiplication a g.val)) = _
  rw [adjoint_inner_right]
  change inner ℂ f.val (neutralActualZetaLogSymbolMultiplication a g.val) = _
  rw [L2.inner_def]
  have hef : neutralLogWeightedL2 (neutralLogHilbertToCanonical f) = f.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse f)
  have heg : neutralLogWeightedL2 (neutralLogHilbertToCanonical g) = g.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse g)
  have hm := neutralLogWeightedL2_mixed_ae
    (neutralLogHilbertToCanonical f) (neutralLogHilbertToCanonical g)
  rw [hef, heg] at hm
  apply integral_congr_ae
  filter_upwards [hm, neutralActualZetaLogSymbolMultiplication_coe a g.val]
    with ξ hmix hmul
  simp only [RCLike.inner_apply']
  rw [hmul]
  calc
    _ = neutralLogSymbolRatio a ξ * (conj (f.val ξ) * g.val ξ) := by ring
    _ = neutralLogSymbolRatio a ξ *
        (conj ((𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) *
          (logarithmicFourierWeight ξ : ℂ) *
          (𝓕 (neutralLogPhysical g.val) : RealComplexL2) ξ) :=
      congrArg (fun z => neutralLogSymbolRatio a ξ * z) hmix
    _ = _ := by
      have hw : (logarithmicFourierWeight ξ : ℂ) ≠ 0 := by
        exact_mod_cast ne_of_gt (lt_of_lt_of_le zero_lt_one
          (one_le_logarithmicFourierWeight ξ))
      unfold neutralLogSymbolRatio
      rw [Complex.ofReal_div]
      field_simp [hw] <;> ring

theorem neutralActualZetaLogMultiplierOperator_diagonal
    (a : ℝ) (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaLogMultiplierOperator a f) =
      ((∫ ξ, rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2 : ℝ) : ℂ) := by
  rw [neutralActualZetaLogMultiplierOperator_mixed]
  calc
    _ = ∫ ξ, ((rightLimitCompactWeilSymbolMathlib a ξ *
        ‖(𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ‖ ^ 2 : ℝ) : ℂ) := by
      apply integral_congr_ae
      filter_upwards [] with ξ
      calc
        _ = (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
          (conj ((𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) *
            (𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) := by ring
        _ = _ := by simp only [Complex.conj_mul', Complex.ofReal_mul, Complex.ofReal_pow]
    _ = _ := integral_complex_ofReal

/-- Unconditional actual multiplier-plus-Hermitian-cross-pole form operator. -/
def neutralActualZetaLogWeilFormOperator (a : ℝ) :
    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier a :=
  neutralActualZetaLogMultiplierOperator a + neutralLogPoleOperator a

theorem neutralActualZetaLogWeilFormOperator_mixed
    (a : ℝ) (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaLogWeilFormOperator a g) =
      (∫ ξ, conj ((𝓕 (neutralLogPhysical f.val) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (neutralLogPhysical g.val) : RealComplexL2) ξ) +
      inner ℂ f (neutralLogPoleOperator a g) := by
  simp only [neutralActualZetaLogWeilFormOperator, ContinuousLinearMap.add_apply,
    inner_add_right, neutralActualZetaLogMultiplierOperator_mixed]

/-- The bounded form operator has the previously certified canonical quadratic. -/
theorem neutralActualZetaLogWeilFormOperator_diagonal
    (a : ℝ) (f : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralActualZetaLogWeilFormOperator a f) =
      (neutralActualZetaCanonicalNativeQuadratic a (neutralLogHilbertToCanonical f) : ℂ) := by
  simp only [neutralActualZetaLogWeilFormOperator, ContinuousLinearMap.add_apply,
    inner_add_right, neutralActualZetaLogMultiplierOperator_diagonal,
    neutralLogPoleOperator_diagonal, neutralActualZetaCanonicalNativeQuadratic,
    neutralLogHilbertToCanonical, Complex.ofReal_add]

/-- Genuine mixed form continuity in the logarithmic Hilbert norm. -/
theorem neutralActualZetaLogWeilFormOperator_mixed_bound
    (a : ℝ) (f g : NeutralLogHilbertCarrier a) :
    ‖inner ℂ f (neutralActualZetaLogWeilFormOperator a g)‖ ≤
      ‖neutralActualZetaLogWeilFormOperator a‖ * ‖f‖ * ‖g‖ := by
  calc
    _ ≤ ‖f‖ * ‖neutralActualZetaLogWeilFormOperator a g‖ := norm_inner_le_norm _ _
    _ ≤ ‖f‖ * (‖neutralActualZetaLogWeilFormOperator a‖ * ‖g‖) :=
      mul_le_mul_of_nonneg_left
        ((neutralActualZetaLogWeilFormOperator a).le_opNorm g) (norm_nonneg _)
    _ = _ := by ring

/-- The certified native Gårding estimate now belongs to an actual bounded form operator. -/
theorem neutralActualZetaLogWeilFormOperator_garding
    (a : ℝ) (f : NeutralLogHilbertCarrier a) :
    ‖f‖ ^ 2 ≤ (inner ℂ f (neutralActualZetaLogWeilFormOperator a f)).re +
      (neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
        ‖neutralLogPhysical f.val‖ ^ 2 := by
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re]
  have h := neutralActualZetaCanonicalNativeQuadratic_garding a
    (neutralLogHilbertToCanonical f)
  have he : neutralLogWeightedL2 (neutralLogHilbertToCanonical f) = f.val :=
    congrArg Subtype.val (neutralLogHilbertToCanonical_rightInverse f)
  rw [he] at h
  exact h

/-- The actual full-divisor zero form equals this unconditional operator's
mixed form on both unchanged canonical Green images. -/
theorem neutralActualZetaGreenZeroForm_native_operator
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenZeroForm a v w =
      inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
        (neutralActualZetaLogWeilFormOperator a
          (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) := by
  rw [neutralActualZetaGreenZeroForm_native_mixed a ha v w,
    neutralActualZetaLogWeilFormOperator_mixed,
    neutralActualZetaGreenCanonical_physical, neutralActualZetaGreenCanonical_physical]

/-- Full-divisor source normalization survives the same mixed operator attachment. -/
theorem neutralActualZetaGreenSourceForms_native_operator
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenPositiveForm a ha v w -
      neutralActualZetaGreenNegativeForm a ha v w =
    2 * inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
      (neutralActualZetaLogWeilFormOperator a
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha w))) := by
  rw [← neutralActualZetaGreenZeroForm_source_decomposition a ha v w,
    neutralActualZetaGreenZeroForm_native_operator a ha v w]

/-- The lawful Hilbert source covariance and native form operator agree on
the certified Green diagonal, with their distinct domains kept explicit. -/
theorem neutralActualZetaGreenHilbertSource_native_operator_diagonal
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    inner ℂ (neutralActualZetaGreenHilbertSourceLift a ha v)
      (neutralActualZetaHilbertSourceOperator a
        (neutralActualZetaGreenHilbertSourceLift a ha v)) =
    inner ℂ (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))
      (neutralActualZetaLogWeilFormOperator a
        (neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v))) := by
  rw [neutralActualZetaGreenHilbertSourceOperator_diagonal,
    ← neutralActualZetaGreenZeroForm_native_operator a ha v v]
  apply Complex.ext
  · rfl
  · exact (neutralActualZetaGreenZeroForm_diagonal_im a v).symm

end
end WeilDefect
