import WeilDefect.MasterRecon.V10B67a

/-! V10B73a: minimal square-log spectral domain gate.
No Bochner construction, residual estimate, or digamma-series supply is used. -/
namespace WeilDefect.MasterRecon.V10B73a
open MeasureTheory Set Polynomial
open scoped ENNReal FourierTransform
open V08I (FullL2 logWeight)
open V10B47c (trial)
open V10B66a (phase phase_norm trialPoly trial_fourier_decay)
open V10B67a (trialL2 trialTransform trial_fourier_literal)

theorem square_weight_growth (u : ℝ) :
    logWeight u ^ 2 ≤ 48*(1+‖u‖)^(1/2:ℝ) := by
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
  have hsy : 0 < Real.sqrt y := Real.sqrt_pos.2 hy
  have hl := Real.log_le_sub_one_of_pos (Real.sqrt_pos.2 hsy)
  rw [Real.log_sqrt hsy.le,Real.log_sqrt hy.le] at hl
  have hlog : Real.log y ≤ 4*Real.sqrt (Real.sqrt y) := by linarith
  have hnon : 0 ≤ Real.log y := (V08I.logWeight_pos u).le
  have hsq := pow_le_pow_left₀ hnon hlog 2
  rw [mul_pow,Real.sq_sqrt hsy.le] at hsq
  change Real.log y ^ 2 ≤ 48*r^(1/2:ℝ)
  rw [← Real.sqrt_eq_rpow]
  calc
    _ ≤ (4:ℝ)^2*Real.sqrt y := hsq
    _ ≤ 48*Real.sqrt r := by linarith only [hs]

theorem square_weighted_of_decay (F : ℝ → ℂ) (hm : AEStronglyMeasurable F volume)
    (C : ℝ) (hC : 0 ≤ C)
    (hd : ∀ᵐ u ∂volume, (1+‖u‖)*‖F u‖ ≤ C) :
    Integrable (fun u => logWeight u ^ 2 * ‖F u‖^2) := by
  have hi : Integrable (fun u : ℝ => (1+‖u‖)^(-(3/2):ℝ)) :=
    integrable_one_add_norm (E := ℝ) (μ := volume) (r := (3/2:ℝ)) (by simp; norm_num)
  apply (hi.const_mul (48*C^2)).mono'
    ((V08I.logWeight_continuous.measurable.aestronglyMeasurable.pow 2).mul (hm.norm.pow 2))
  filter_upwards [hd] with u hu
  let r : ℝ := 1+‖u‖
  have hr : 0 < r := by dsimp [r]; positivity
  have hn : ‖F u‖ ≤ C/r := (le_div_iff₀ hr).mpr (by simpa [r,mul_comm] using hu)
  have hsq : ‖F u‖^2 ≤ (C/r)^2 := by
    exact pow_le_pow_left₀ (norm_nonneg _) hn 2
  change ‖logWeight u ^ 2 * ‖F u‖^2‖ ≤ 48*C^2*r^(-(3/2):ℝ)
  rw [Real.norm_eq_abs,abs_of_nonneg
    (mul_nonneg (sq_nonneg _) (sq_nonneg _))]
  change logWeight u ^ 2 * ‖F u‖^2 ≤ 48*C^2*r^(-(3/2):ℝ)
  calc
    _ ≤ 48*r^(1/2:ℝ)*‖F u‖^2 :=
      mul_le_mul_of_nonneg_right (square_weight_growth u) (sq_nonneg _)
    _ ≤ 48*r^(1/2:ℝ)*(C/r)^2 :=
      mul_le_mul_of_nonneg_left hsq (by positivity)
    _ = 48*C^2*(r^(1/2:ℝ)/r^2) := by rw [div_pow]; ring
    _ = _ := by
      rw [← Real.rpow_natCast r 2,← Real.rpow_sub hr] <;> norm_num

theorem trial_decay (col : Fin 16) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ᵐ u ∂volume,
      (1+‖u‖)*‖(𝓕 (trialL2 col) : FullL2) u‖ ≤ K := by
  let B : ℝ := ∫ x in (-1/4:ℝ)..(1/4), ‖trial col (2*x+1/2)‖
  let D : ℝ := ‖(trialPoly col).eval (1/4)‖+‖(trialPoly col).eval (-1/4)‖+
    ∫ x in (-1/4:ℝ)..(1/4), ‖(trialPoly col).derivative.eval x‖
  have hB : 0 ≤ B := intervalIntegral.integral_nonneg (by norm_num) (fun _ _ => norm_nonneg _)
  have hD : 0 ≤ D := by
    dsimp [D]
    have h := intervalIntegral.integral_nonneg (μ := volume) (by norm_num : (-1/4:ℝ) ≤ 1/4)
      (f := fun x => ‖(trialPoly col).derivative.eval x‖) (fun _ _ => norm_nonneg _)
    exact add_nonneg
      (add_nonneg (abs_nonneg ((trialPoly col).eval (1/4)))
        (abs_nonneg ((trialPoly col).eval (-1/4)))) h
  refine ⟨B+D,add_nonneg hB hD,?_⟩
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

theorem trial_square_weighted (col : Fin 16) :
    Integrable (fun u => logWeight u ^ 2 * ‖(𝓕 (trialL2 col) : FullL2) u‖^2) := by
  obtain ⟨K,hK,hdecay⟩ := trial_decay col
  exact square_weighted_of_decay _ (Lp.aestronglyMeasurable _) K hK hdecay

end WeilDefect.MasterRecon.V10B73a

#print axioms WeilDefect.MasterRecon.V10B73a.square_weight_growth
#print axioms WeilDefect.MasterRecon.V10B73a.square_weighted_of_decay
#print axioms WeilDefect.MasterRecon.V10B73a.trial_decay
#print axioms WeilDefect.MasterRecon.V10B73a.trial_square_weighted
