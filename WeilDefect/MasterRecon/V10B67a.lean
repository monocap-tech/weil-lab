import WeilDefect.MasterRecon.V10B66a
import WeilDefect.MasterRecon.V08K
import Mathlib.Analysis.SpecialFunctions.JapaneseBracket
import Mathlib.MeasureTheory.Function.LpSeminorm.Indicator

/-! Exact endpoint-inclusive trials in the actual logarithmic carrier.
The weight is the original angular-normalized log(2+|2*pi*u|).
No Archimedean multiplier, digamma series, or residual bound is assumed. -/
namespace WeilDefect.MasterRecon.V10B67a
open MeasureTheory Set Polynomial
open scoped ENNReal FourierTransform
open V08I (FullL2 logCarrier physicalInclusion logWeight)
open V10B47c (trial)
open V10B66a (phase phase_norm trialPoly trialPoly_eval trial_fourier_decay)

theorem weight_growth (u : ℝ) :
    logWeight u ≤ 6*(1+‖u‖)^(1/2:ℝ) := by
  let y : ℝ := 2+|2*Real.pi*u|
  let r : ℝ := 1+‖u‖
  have hy : 0 < y := by dsimp [y]; positivity
  have hr : 0 < r := by dsimp [r]; positivity
  have hπ : 2*Real.pi ≤ 8 := by linarith [Real.pi_lt_d2]
  have hyr : y ≤ 8*r := by
    dsimp [y,r]
    rw [abs_mul,abs_of_pos (by positivity : 0 < 2*Real.pi)]
    nlinarith [mul_nonneg (sub_nonneg.mpr hπ) (abs_nonneg u)]
  have hs : Real.sqrt y ≤ 3*Real.sqrt r := by
    calc
      _ ≤ Real.sqrt (8*r) := Real.sqrt_le_sqrt hyr
      _ = Real.sqrt 8*Real.sqrt r := Real.sqrt_mul (by norm_num) r
      _ ≤ _ := mul_le_mul_of_nonneg_right
        (by rw [Real.sqrt_le_left (by norm_num : (0:ℝ) ≤ 3)]; norm_num)
        (Real.sqrt_nonneg r)
  have hl := Real.log_le_sub_one_of_pos (Real.sqrt_pos.2 hy)
  rw [Real.log_sqrt hy.le] at hl
  change Real.log y ≤ 6*r^(1/2:ℝ)
  rw [← Real.sqrt_eq_rpow]
  linarith

theorem weighted_of_decay (F : ℝ → ℂ) (hm : AEStronglyMeasurable F volume)
    (C : ℝ) (hC : 0 ≤ C)
    (hd : ∀ᵐ u ∂volume, (1+‖u‖)*‖F u‖ ≤ C) :
    Integrable (fun u => logWeight u * ‖F u‖^2) := by
  have hi : Integrable (fun u : ℝ => (1+‖u‖)^(-(3/2):ℝ)) :=
    integrable_one_add_norm (E := ℝ) (μ := volume) (r := (3/2:ℝ)) (by simp; norm_num)
  apply (hi.const_mul (6*C^2)).mono'
    (V08I.logWeight_continuous.measurable.aestronglyMeasurable.mul (hm.norm.pow 2))
  filter_upwards [hd] with u hu
  let r : ℝ := 1+‖u‖
  have hr : 0 < r := by dsimp [r]; positivity
  have hn : ‖F u‖ ≤ C/r := (le_div_iff₀ hr).mpr (by simpa [r,mul_comm] using hu)
  have hsq : ‖F u‖^2 ≤ (C/r)^2 := by
    exact pow_le_pow_left₀ (norm_nonneg _) hn 2
  change ‖logWeight u * ‖F u‖^2‖ ≤ 6*C^2*r^(-(3/2):ℝ)
  rw [Real.norm_eq_abs,abs_of_nonneg
    (mul_nonneg (V08I.logWeight_pos u).le (sq_nonneg _))]
  change logWeight u * ‖F u‖^2 ≤ 6*C^2*r^(-(3/2):ℝ)
  calc
    _ ≤ 6*r^(1/2:ℝ)*‖F u‖^2 :=
      mul_le_mul_of_nonneg_right (weight_growth u) (sq_nonneg _)
    _ ≤ 6*r^(1/2:ℝ)*(C/r)^2 :=
      mul_le_mul_of_nonneg_left hsq (by positivity)
    _ = 6*C^2*(r^(1/2:ℝ)/r^2) := by rw [div_pow]; ring
    _ = _ := by
      rw [← Real.rpow_natCast r 2,← Real.rpow_sub hr] <;> norm_num

noncomputable def polynomialValue (col : Fin 16) (x : ℝ) : ℂ :=
  Complex.ofReal ((trialPoly col).eval x)

noncomputable def supportedTrial (col : Fin 16) : ℝ → ℂ :=
  (Icc (-1/4:ℝ) (1/4)).indicator (polynomialValue col)

theorem supported_mem (col : Fin 16) : MemLp (supportedTrial col) 2 volume := by
  unfold supportedTrial
  rw [memLp_indicator_iff_restrict measurableSet_Icc]
  have hc : Continuous (polynomialValue col) :=
    Complex.continuous_ofReal.comp (trialPoly col).continuous
  apply (memLp_two_iff_integrable_sq_norm hc.aestronglyMeasurable).mpr
  exact (hc.norm.pow 2).integrableOn_Icc

noncomputable def trialL2 (col : Fin 16) : FullL2 :=
  (supported_mem col).toLp (supportedTrial col)

theorem trialL2_ae (col : Fin 16) :
    (trialL2 col : ℝ → ℂ) =ᵐ[volume] supportedTrial col :=
  MemLp.coeFn_toLp (supported_mem col)

theorem trialL2_support (col : Fin 16) :
    ∀ᵐ x ∂volume, x ∉ Icc (-(1/4):ℝ) (1/4) → trialL2 col x=0 := by
  filter_upwards [trialL2_ae col] with x hx
  intro hout
  have hout' : x ∉ Icc (-1/4:ℝ) (1/4) := by
    simpa only [neg_div] using hout
  rw [hx,supportedTrial,indicator_of_notMem hout']

noncomputable def trialTransform (col : Fin 16) (u : ℝ) : ℂ :=
  ∫ x in (-1/4:ℝ)..(1/4), (trial col (2*x+1/2):ℂ)*phase (-(2*Real.pi)*u) x

theorem trial_fourier_literal (col : Fin 16) :
    ((𝓕 (trialL2 col) : FullL2) : ℝ → ℂ) =ᵐ[volume] trialTransform col := by
  have hf := V08K.supported_integrable (1/4) (trialL2 col) (trialL2_support col)
  refine (V08H.l2_fourier_integral_ae (trialL2 col) hf).trans ?_
  filter_upwards with u
  rw [← V08H.angularFourier_scaled]
  unfold V08H.angularFourier trialTransform
  calc
    _ = ∫ x, V08D.fourierKernel (2*Real.pi*u) x * supportedTrial col x := by
      apply integral_congr_ae
      filter_upwards [trialL2_ae col] with x hx
      rw [hx]
    _ = ∫ x in Icc (-1/4:ℝ) (1/4),
        (trial col (2*x+1/2):ℂ)*phase (-(2*Real.pi)*u) x := by
      rw [← integral_indicator measurableSet_Icc]
      apply integral_congr_ae
      filter_upwards with x
      by_cases hx : x ∈ Icc (-1/4:ℝ) (1/4)
      · rw [supportedTrial,indicator_of_mem hx,indicator_of_mem hx,
          polynomialValue,trialPoly_eval,V08D.fourierKernel,phase]
        rw [mul_comm]
        congr 1
        push_cast
        ring
      · rw [supportedTrial,indicator_of_notMem hx,indicator_of_notMem hx,mul_zero]
    _ = _ := by rw [integral_Icc_eq_integral_Ioc,← intervalIntegral.integral_of_le (by norm_num)]

theorem trial_weighted (col : Fin 16) :
    Integrable (fun u => logWeight u * ‖(𝓕 (trialL2 col) : FullL2) u‖^2) := by
  let B : ℝ := ∫ x in (-1/4:ℝ)..(1/4), ‖trial col (2*x+1/2)‖
  let D : ℝ := ‖(trialPoly col).eval (1/4)‖+‖(trialPoly col).eval (-1/4)‖+
    ∫ x in (-1/4:ℝ)..(1/4), ‖(trialPoly col).derivative.eval x‖
  have hB : 0 ≤ B := intervalIntegral.integral_nonneg (by norm_num) (fun _ _ => norm_nonneg _)
  have hD : 0 ≤ D := by
    dsimp [D]
    have h := intervalIntegral.integral_nonneg (μ := volume) (by norm_num : (-1/4:ℝ) ≤ 1/4)
      (f := fun x => ‖(trialPoly col).derivative.eval x‖) (fun _ _ => norm_nonneg _)
    exact add_nonneg (add_nonneg (norm_nonneg _) (norm_nonneg _)) h
  apply weighted_of_decay _ (Lp.aestronglyMeasurable _) (B+D) (add_nonneg hB hD)
  filter_upwards [trial_fourier_literal col] with u hu
  rw [hu]
  have hb : ‖trialTransform col u‖ ≤ B := by
    unfold trialTransform
    simpa only [B,norm_mul,phase_norm,mul_one,Complex.norm_real] using
      (intervalIntegral.norm_integral_le_integral_norm
        (f := fun x : ℝ => (trial col (2*x+1/2):ℂ)*phase (-(2*Real.pi)*u) x)
        (by norm_num : (-1/4:ℝ) ≤ 1/4))
  have hd := trial_fourier_decay col (-(2*Real.pi)*u)
  change |-(2*Real.pi)*u| * ‖trialTransform col u‖ ≤ D at hd
  rw [abs_mul,abs_neg,abs_of_pos (by positivity : 0 < 2*Real.pi)] at hd
  have hπ : 1 ≤ 2*Real.pi := by linarith [Real.pi_gt_three]
  have hh : ‖u‖*‖trialTransform col u‖ ≤ D := by
    rw [Real.norm_eq_abs]
    calc
      _ ≤ (2*Real.pi*|u|)*‖trialTransform col u‖ := by
        apply mul_le_mul_of_nonneg_right _ (norm_nonneg _)
        simpa using mul_le_mul_of_nonneg_right hπ (abs_nonneg u)
      _ ≤ _ := hd
  rw [add_mul,one_mul]
  exact add_le_add hb hh

noncomputable def carrierTrial (col : Fin 16) : logCarrier (1/4) :=
  V08J.liftPhysical (1/4) (trialL2 col) (trialL2_support col) (trial_weighted col)

theorem carrierTrial_physical (col : Fin 16) :
    physicalInclusion (1/4) (carrierTrial col) = trialL2 col :=
  V08J.physicalInclusion_lift _ _ _ _

theorem carrierTrial_ae (col : Fin 16) :
    (physicalInclusion (1/4) (carrierTrial col) : ℝ → ℂ) =ᵐ[volume] supportedTrial col := by
  rw [carrierTrial_physical]
  exact trialL2_ae col

end WeilDefect.MasterRecon.V10B67a

#print axioms WeilDefect.MasterRecon.V10B67a.weight_growth
#print axioms WeilDefect.MasterRecon.V10B67a.weighted_of_decay
#print axioms WeilDefect.MasterRecon.V10B67a.supported_mem
#print axioms WeilDefect.MasterRecon.V10B67a.trialL2_ae
#print axioms WeilDefect.MasterRecon.V10B67a.trialL2_support
#print axioms WeilDefect.MasterRecon.V10B67a.trial_fourier_literal
#print axioms WeilDefect.MasterRecon.V10B67a.trial_weighted
#print axioms WeilDefect.MasterRecon.V10B67a.carrierTrial_physical
#print axioms WeilDefect.MasterRecon.V10B67a.carrierTrial_ae
