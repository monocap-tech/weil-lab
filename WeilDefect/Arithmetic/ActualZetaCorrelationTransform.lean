import WeilDefect.Arithmetic.ActualZetaSourceDecomposition
import Mathlib.Analysis.Convolution

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped ComplexConjugate Convolution
set_option maxHeartbeats 800000

/-- Exact compact representative obtained by restricting the physical L² function. -/
def neutralWindowRepresentative (a : ℝ) (f : RealComplexL2) : ℝ → ℂ :=
  (Set.Icc (-a) a).indicator f

/-- Mixed compact correlation: the first input is conjugated and reflected. -/
def neutralWindowCorrelation (a : ℝ) (f g : RealComplexL2) (t : ℝ) : ℂ :=
  ∫ s : ℝ, neutralWindowRepresentative a g s *
    conj (neutralWindowRepresentative a f (s - t))

/-- Full-line raw transform, in the project's positive-exponent convention. -/
def neutralRawTransform (k : ℝ → ℂ) (z : ℂ) : ℂ :=
  ∫ t : ℝ, k t * Complex.exp (Complex.I * z * (t : ℂ))

/-- Window restriction preserves the constructed supported Green vector almost everywhere. -/
theorem neutralActualZetaGreenSynthesis_windowRepresentative_ae
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    neutralWindowRepresentative a (neutralActualZetaGreenSynthesis a v) =ᵐ[volume]
      neutralActualZetaGreenSynthesis a v := by
  filter_upwards [neutralActualZetaGreenSynthesis_supported a ha v] with x hx
  by_cases hm : x ∈ Set.Icc (-a) a
  · simp [neutralWindowRepresentative, hm]
  · simp [neutralWindowRepresentative, hm, hx hm]

/-- Exponential weighting remains integrable for every complex parameter,
because the raw L² input is restricted to a finite compact window. -/
theorem neutralWindowRepresentative_twist_integrable (a : ℝ) (f : RealComplexL2) (z : ℂ) :
    Integrable (fun x : ℝ => neutralWindowRepresentative a f x *
      Complex.exp (Complex.I * z * (x : ℂ))) := by
  have hf := (f.memLp.locallyIntegrable (by norm_num : (1 : ℝ≥0∞) ≤ 2)).integrableOn_isCompact
    (isCompact_Icc : IsCompact (Set.Icc (-a) a))
  have he : Continuous (fun x : ℝ => Complex.exp (Complex.I * z * (x : ℂ))) := by fun_prop
  have hi := (hf.mul_continuousOn he.continuousOn isCompact_Icc).integrable_indicator
    measurableSet_Icc
  apply hi.congr
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;> simp [neutralWindowRepresentative, hx]

private theorem windowRepresentative_integrable (a : ℝ) (f : RealComplexL2) :
    Integrable (neutralWindowRepresentative a f) := by
  simpa using neutralWindowRepresentative_twist_integrable a f 0

private theorem rawTransform_window (a : ℝ) (f : RealComplexL2) (z : ℂ) :
    neutralRawTransform (neutralWindowRepresentative a f) z = neutralWindowEvaluation a z f := by
  unfold neutralRawTransform neutralWindowEvaluation
  rw [← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-a) a <;> simp [neutralWindowRepresentative, hx]

/-- The correlation vanishes outside the doubled window, pointwise. -/
theorem neutralWindowCorrelation_supported (a : ℝ) (f g : RealComplexL2) (t : ℝ)
    (ht : t ∉ Set.Icc (-(2 * a)) (2 * a)) : neutralWindowCorrelation a f g t = 0 := by
  unfold neutralWindowCorrelation
  apply integral_eq_zero_of_ae
  filter_upwards [] with s
  by_cases hs : s ∈ Set.Icc (-a) a
  · have hst : s - t ∉ Set.Icc (-a) a := by
      intro h
      apply ht
      constructor <;> linarith [hs.1, hs.2, h.1, h.2]
    simp [neutralWindowRepresentative, hst]
  · simp [neutralWindowRepresentative, hs]

theorem neutralWindowCorrelation_hasCompactSupport (a : ℝ) (f g : RealComplexL2) :
    HasCompactSupport (neutralWindowCorrelation a f g) :=
  HasCompactSupport.intro isCompact_Icc (neutralWindowCorrelation_supported a f g)

private theorem correlation_eq_convolution (a : ℝ) (f g : RealComplexL2) :
    neutralWindowCorrelation a f g =
      (neutralWindowRepresentative a g ⋆[ContinuousLinearMap.mul ℂ ℂ]
        fun x : ℝ => conj (neutralWindowRepresentative a f (-x))) := by
  funext t
  simp only [neutralWindowCorrelation, convolution, ContinuousLinearMap.mul_apply', neg_sub]

/-- Compact correlations of the physical L² inputs are integrable. -/
theorem neutralWindowCorrelation_integrable (a : ℝ) (f g : RealComplexL2) :
    Integrable (neutralWindowCorrelation a f g) := by
  rw [correlation_eq_convolution]
  exact (windowRepresentative_integrable a g).integrable_convolution
    (ContinuousLinearMap.mul ℂ ℂ) ((windowRepresentative_integrable a f).star.comp_neg)

private theorem reflected_twist_integral (a : ℝ) (f : RealComplexL2) (z : ℂ) :
    (∫ x : ℝ, conj (neutralWindowRepresentative a f (-x) *
      Complex.exp (Complex.I * conj z * ((-x : ℝ) : ℂ)))) =
      conj (neutralWindowEvaluation a (conj z) f) := by
  rw [integral_neg_eq_self, integral_conj]
  exact congrArg (starRingEnd ℂ) (rawTransform_window a f (conj z))

/-- All-complex mixed correlation transform, proved directly for compact-window L² inputs. -/
theorem neutralWindowCorrelation_rawTransform (a : ℝ) (f g : RealComplexL2) (z : ℂ) :
    neutralRawTransform (neutralWindowCorrelation a f g) z =
      conj (neutralWindowEvaluation a (conj z) f) * neutralWindowEvaluation a z g := by
  let G : ℝ → ℂ := fun x => neutralWindowRepresentative a g x *
    Complex.exp (Complex.I * z * (x : ℂ))
  let F : ℝ → ℂ := fun x => conj (neutralWindowRepresentative a f (-x) *
    Complex.exp (Complex.I * conj z * ((-x : ℝ) : ℂ)))
  have hG : Integrable G := neutralWindowRepresentative_twist_integrable a g z
  have hF : Integrable F :=
    (neutralWindowRepresentative_twist_integrable a f (conj z)).star.comp_neg
  have hp (t : ℝ) : neutralWindowCorrelation a f g t *
      Complex.exp (Complex.I * z * (t : ℂ)) =
        (G ⋆[ContinuousLinearMap.mul ℂ ℂ] F) t := by
    simp only [neutralWindowCorrelation, convolution, ContinuousLinearMap.mul_apply']
    rw [← integral_mul_const]
    apply integral_congr_ae
    filter_upwards [] with s
    dsimp [G, F]
    rw [map_mul, ← Complex.exp_conj]
    have he : conj (Complex.I * conj z * ((-(t - s) : ℝ) : ℂ)) =
        -(Complex.I * z * ((s - t : ℝ) : ℂ)) := by
      simp only [map_mul, Complex.conj_I, starRingEnd_apply, star_star,
        Complex.conj_ofReal, neg_sub]
      ring
    rw [he]
    have he' : Complex.exp (Complex.I * z * (s : ℂ)) *
        Complex.exp (-(Complex.I * z * ((s - t : ℝ) : ℂ))) =
          Complex.exp (Complex.I * z * (t : ℂ)) := by
      rw [← Complex.exp_add]
      congr 1
      push_cast
      ring
    simp only [neg_sub]
    linear_combination -(neutralWindowRepresentative a g s *
      conj (neutralWindowRepresentative a f (s - t))) * he'
  unfold neutralRawTransform
  rw [integral_congr_ae (Filter.Eventually.of_forall hp),
    integral_convolution (ContinuousLinearMap.mul ℂ ℂ) hG hF]
  change (∫ x, G x) * (∫ x, F x) = _
  rw [show (∫ x, G x) = neutralWindowEvaluation a z g from rawTransform_window a g z,
    show (∫ x, F x) = conj (neutralWindowEvaluation a (conj z) f) from
      reflected_twist_integral a f z]
  exact mul_comm _ _

/-- The actual full-divisor transform samples of this exact mixed correlation converge absolutely. -/
theorem neutralActualZetaGreenCorrelation_samples_summable
    (a : ℝ) (ha : 0 < a) (v w : NeutralActualZetaGreenCoefficients) :
    Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralRawTransform (neutralWindowCorrelation a
        (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w))
        (neutralActualZetaDivisorOrdinate q)) := by
  simpa only [neutralWindowCorrelation_rawTransform] using
    neutralActualZetaGreenSynthesis_partner_mixed_summable a ha v w

/-- The correlation transform has exactly the already certified partner zero-side sum. -/
theorem neutralActualZetaGreenCorrelation_zeroForm
    (a : ℝ) (v w : NeutralActualZetaGreenCoefficients) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      neutralRawTransform (neutralWindowCorrelation a
        (neutralActualZetaGreenSynthesis a v) (neutralActualZetaGreenSynthesis a w))
        (neutralActualZetaDivisorOrdinate q)) = neutralActualZetaGreenZeroForm a v w := by
  simp only [neutralWindowCorrelation_rawTransform, neutralActualZetaGreenZeroForm]

end
end WeilDefect
