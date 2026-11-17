import WeilDefect.Arithmetic.ActualZetaOriginalLogStripGraphLimit
import WeilDefect.Arithmetic.ActualZetaCorrelationFourierAgreement
import Mathlib.Analysis.SpecialFunctions.JapaneseBracket
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform Filter InnerProductSpace
open scoped FourierTransform ComplexConjugate

/-!
NF575: the original NF524/NF528 strip estimate pays the physical
logarithmic energy too. A separate H^(1/4) formalization is not
necessary once the strip estimate itself is established.
-/

def neutralNF575ContinuumWeight (ξ : ℝ) : ℝ :=
  (1 + |ξ|) ^ (-(5/4) : ℝ)

def neutralNF575LogConstant : ℝ :=
  4 * (Real.exp 1 + 1) ^ (1/4 : ℝ)

def neutralNF575StripConstant : ℝ :=
  1 + 4 * (2 + 2 * Real.pi) ^ (1/4 : ℝ)

theorem neutralNF575ContinuumWeight_integrable :
    Integrable neutralNF575ContinuumWeight volume := by
  simpa only [neutralNF575ContinuumWeight, Real.norm_eq_abs] using
    (integrable_one_add_norm (E := ℝ) (μ := (volume : Measure ℝ))
      (r := (5/4 : ℝ)) (by norm_num))

private theorem neutralNF575LogAffine_le
    (a b ξ : ℝ) (ha : 0 < a) (hb : 0 ≤ b) :
    Real.log (a+b*|ξ|) ≤
      (4*(a+b)^(1/4:ℝ)) * (1+|ξ|)^(1/4:ℝ) := by
  have hab : 0 ≤ a+b := by linarith
  have hx : 0 ≤ a+b*|ξ| := by positivity
  have hle : a+b*|ξ| ≤ (a+b)*(1+|ξ|) := by
    nlinarith [mul_nonneg ha.le (abs_nonneg ξ)]
  have hpow := Real.rpow_le_rpow hx hle (by norm_num : 0 ≤ (1/4:ℝ))
  calc
    _ ≤ (a+b*|ξ|)^(1/4:ℝ)/(1/4:ℝ) :=
      Real.log_le_rpow_div hx (by norm_num)
    _ ≤ ((a+b)*(1+|ξ|))^(1/4:ℝ)/(1/4:ℝ) :=
      div_le_div_of_nonneg_right hpow (by norm_num)
    _ = _ := by
      rw [Real.mul_rpow hab (by positivity)]
      ring

theorem neutralNF575LogWeight_le (ξ : ℝ) :
    logarithmicFourierWeight ξ ≤
      neutralNF575LogConstant * (1+|ξ|)^(1/4:ℝ) := by
  unfold logarithmicFourierWeight neutralNF575LogConstant
  simpa only [one_mul] using
    neutralNF575LogAffine_le (Real.exp 1) 1 ξ (Real.exp_pos _) zero_le_one

theorem neutralNF575RealStrip_le (ξ : ℝ) :
    neutralNF574StripEnvelope (-2*Real.pi*ξ) ≤
      neutralNF575StripConstant * (1+|ξ|)^(-(3/4):ℝ) := by
  have hp : 0 < Real.pi := Real.pi_pos
  have h2p : 1 ≤ 2*Real.pi := by linarith [Real.pi_gt_three]
  have hr : 0 < 1+|ξ| := by positivity
  have hr1 : (1:ℝ) ≤ 1+|ξ| := by linarith [abs_nonneg ξ]
  have hp1 : (1:ℝ) ≤ (1+|ξ|)^(1/4:ℝ) := by
    have h := Real.rpow_le_rpow (by norm_num : (0:ℝ)≤1) hr1
      (by norm_num : (0:ℝ)≤1/4)
    simpa using h
  have habs : |-2*Real.pi*ξ| = 2*Real.pi*|ξ| := by
    rw [abs_mul, abs_of_neg (by linarith : -2*Real.pi<0)]
    ring
  have hden : 1+|ξ| ≤ 1+2*Real.pi*|ξ| := by
    nlinarith [mul_nonneg (sub_nonneg.mpr h2p) (abs_nonneg ξ)]
  have hlog := neutralNF575LogAffine_le 2 (2*Real.pi) ξ (by norm_num) (by positivity)
  have hnum : 1+Real.log (2+2*Real.pi*|ξ|) ≤
      neutralNF575StripConstant*(1+|ξ|)^(1/4:ℝ) := by
    unfold neutralNF575StripConstant
    linarith only [hlog,hp1]
  unfold neutralNF574StripEnvelope
  rw [habs]
  calc
    _ ≤ (neutralNF575StripConstant * (1+|ξ|)^(1/4:ℝ)) /
        (1+2*Real.pi*|ξ|) := div_le_div_of_nonneg_right hnum (by positivity)
    _ ≤ (neutralNF575StripConstant * (1+|ξ|)^(1/4:ℝ))/(1+|ξ|) :=
      div_le_div_of_nonneg_left (by unfold neutralNF575StripConstant; positivity)
        hr hden
    _ = _ := by
      rw [mul_div_assoc, ← Real.rpow_one (1+|ξ|), ← Real.rpow_sub hr]
      norm_num

/-- The original slow strip bound already has finite log energy.
The actual negative-exponent 2π Fourier convention is paid exactly. -/
theorem neutralNF575EnergyEnvelope_le (M : ℝ) (hM : 0 ≤ M)
    (ξ : ℝ) (v : ℂ)
    (hv : ‖v‖ ≤ M * neutralNF574StripEnvelope (-2*Real.pi*ξ)) :
    logarithmicFourierWeight ξ * ‖v‖^2 ≤
      (neutralNF575LogConstant * (M*neutralNF575StripConstant)^2) *
        neutralNF575ContinuumWeight ξ := by
  have hr : 0 < 1+|ξ| := by positivity
  have hw : 0 ≤ logarithmicFourierWeight ξ :=
    (by norm_num : (0:ℝ)≤1).trans (one_le_logarithmicFourierWeight ξ)
  have hv' := hv.trans (mul_le_mul_of_nonneg_left (neutralNF575RealStrip_le ξ) hM)
  have hv'' := pow_le_pow_left₀ (norm_nonneg v) hv' 2
  calc
    _ ≤ (neutralNF575LogConstant*(1+|ξ|)^(1/4:ℝ)) *
        (M*(neutralNF575StripConstant*(1+|ξ|)^(-(3/4):ℝ)))^2 :=
      mul_le_mul (neutralNF575LogWeight_le ξ) hv'' (sq_nonneg _)
        (by unfold neutralNF575LogConstant; positivity)
    _ = _ := by
      unfold neutralNF575ContinuumWeight
      have hpow : ((1+|ξ|)^(-(3/4):ℝ))^2 = (1+|ξ|)^(-(3/2):ℝ) := by
        rw [← Real.rpow_natCast_mul (by positivity : 0 ≤ 1+|ξ|)]
        norm_num
      rw [show M*(neutralNF575StripConstant*(1+|ξ|)^(-(3/4):ℝ)) =
        (M*neutralNF575StripConstant)*(1+|ξ|)^(-(3/4):ℝ) by ring,
        mul_pow,hpow]
      calc
        _ = (neutralNF575LogConstant*(M*neutralNF575StripConstant)^2) *
            ((1+|ξ|)^(1/4:ℝ)*(1+|ξ|)^(-(3/2):ℝ)) := by ring
        _ = _ := by rw [← Real.rpow_add hr]; norm_num

/-- Supported physical L² Fourier coordinate equals the literal window
sample at -2πξ a.e. Generalizes the already proved Green-image dictionary
to the nonsmooth original physical target, with no Green assumption. -/
theorem neutralNF575SupportedFourier_ae (a : ℝ) (f : RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0) :
    (𝓕 f : RealComplexL2) =ᵐ[volume]
      fun ξ => neutralWindowEvaluation a ((-2*Real.pi*ξ : ℝ) : ℂ) f := by
  have hrep : neutralWindowRepresentative a f =ᵐ[volume] (f : ℝ → ℂ) := by
    filter_upwards [hf] with x hx
    by_cases hs : x ∈ Set.Icc (-a) a
    · simp [neutralWindowRepresentative,hs]
    · simp [neutralWindowRepresentative,hs,hx hs]
  have hi : Integrable (f : ℝ → ℂ) := by
    have ht : Integrable (neutralWindowRepresentative a f) := by
      simpa using neutralWindowRepresentative_twist_integrable a f 0
    exact ht.congr hrep
  filter_upwards [neutralIntegrableL2_fourier_ae f hi] with ξ hξ
  calc
    _ = (𝓕 (f : ℝ → ℂ)) ξ := hξ
    _ = (𝓕 (neutralWindowRepresentative a f)) ξ :=
      Real.fourier_congr_ae hrep.symm ξ
    _ = _ := neutralWindowRepresentative_fourier a f ξ

/-- The actual weighted carrier can be constructed from the same physical
vector and its historical strip estimate, without a quadratic moment. -/
theorem neutralNF575LogEnergy_of_strip (a : ℝ) (f : RealComplexL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0)
    (M : ℝ) (hM : 0 ≤ M)
    (ht : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation a z f‖ ≤ M*neutralNF574StripEnvelope z.re) :
    Integrable (fun ξ => logarithmicFourierWeight ξ *
      ‖(𝓕 f : RealComplexL2) ξ‖^2) volume := by
  refine (neutralNF575ContinuumWeight_integrable.const_mul
    (neutralNF575LogConstant*(M*neutralNF575StripConstant)^2)).mono' ?_ ?_
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f : RealComplexL2)).norm.pow 2)
  · filter_upwards [neutralNF575SupportedFourier_ae a f hs] with ξ hξ
    rw [Real.norm_eq_abs,abs_of_nonneg (mul_nonneg
      (zero_le_one.trans (one_le_logarithmicFourierWeight ξ)) (sq_nonneg _)),hξ]
    apply neutralNF575EnergyEnvelope_le M hM
    simpa only [Complex.ofReal_re] using ht ((-2*Real.pi*ξ : ℝ):ℂ)
      (by simp)

def neutralNF575StripLogCarrier (a : ℝ) (f : RealComplexL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0)
    (M : ℝ) (hM : 0 ≤ M)
    (ht : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation a z f‖ ≤ M*neutralNF574StripEnvelope z.re) :
    NeutralLogHilbertCarrier a :=
  neutralCanonicalToLogHilbert ⟨f,hs,neutralNF575LogEnergy_of_strip a f hs M hM ht⟩

theorem neutralNF575StripLogCarrier_physical (a : ℝ) (f : RealComplexL2)
    (hs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → f x = 0)
    (M : ℝ) (hM : 0 ≤ M)
    (ht : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation a z f‖ ≤ M*neutralNF574StripEnvelope z.re) :
    neutralLogPhysical (neutralNF575StripLogCarrier a f hs M hM ht).val = f :=
  neutralLogPhysical_weighted _

end
end WeilDefect
