import WeilDefect.Arithmetic.ActualZetaIV095OriginalUniformCollarSectorGate
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier
import Mathlib.Analysis.Fourier.FourierTransformDeriv
import Mathlib.Analysis.Calculus.BumpFunction.Normed
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- Original Schwartz derivative energy, not a Green-coefficient norm. -/
def neutralIV096DerivativeEnergy (s : 𝓢(ℝ,ℂ)) : ℝ :=
  ∫ x : ℝ, ‖deriv (s : ℝ → ℂ) x‖^2

/-- Exact real-frequency dictionary on the original smooth collar. -/
theorem neutralIV096WindowEval_fourier (s : 𝓢(ℝ,ℂ))
    (hs : neutralNF735InOriginalCollars s) (r : ℝ) :
    neutralWindowEvaluation (11/10:ℝ) (r : ℂ) (s.toLp 2 volume) =
      (𝓕 (s : ℝ → ℂ)) (-r / (2 * Real.pi)) := by
  rw [neutralNF573WindowEvaluation_eq_raw_of_ae _ _ _
      (neutralNF573OriginalCollar_window_ae s hs),
    neutralRawTransform_fourier]
  have harg : -2 * Real.pi * (-r / (2 * Real.pi)) = r := by
    field_simp [Real.pi_ne_zero] <;> ring
  rw [harg]

/-- Angular Fourier derivative identity in squared norms. -/
theorem neutralIV096Derivative_fourier_sq (s : 𝓢(ℝ,ℂ)) (r : ℝ) :
    ‖(𝓕 (deriv (s : ℝ → ℂ))) (-r / (2 * Real.pi))‖^2 =
      r^2 * ‖(𝓕 (s : ℝ → ℂ)) (-r / (2 * Real.pi))‖^2 := by
  have hi : Integrable (deriv (s : ℝ → ℂ)) :=
    (SchwartzMap.derivCLM ℂ ℂ s).integrable
  rw [fourier_deriv s.integrable s.differentiable hi]
  simp only [smul_eq_mul, norm_mul, Complex.norm_I, mul_one, Complex.norm_real,
    Real.norm_eq_abs]
  have he : (2 * Real.pi)^2 * (-r / (2 * Real.pi))^2 = r^2 := by
    field_simp [Real.pi_ne_zero] <;> ring
  have hc : ‖(2 : ℂ)‖ = 2 := by norm_num
  simp only [hc, abs_of_pos Real.pi_pos, mul_pow, sq_abs]
  nlinarith only [congrArg (fun x : ℝ => x *
    ‖(𝓕 (s : ℝ → ℂ)) (-r / (2 * Real.pi))‖^2) he]

/-- The angular derivative density is integrable and has exactly the
physical derivative energy, with its 1/(2*pi) Jacobian. -/
theorem neutralIV096AngularDerivative_data (s : 𝓢(ℝ,ℂ)) :
    Integrable (fun r : ℝ => (1 / (2 * Real.pi)) *
      ‖(𝓕 (deriv (s : ℝ → ℂ))) (-r / (2 * Real.pi))‖^2) ∧
    (∫ r : ℝ, (1 / (2 * Real.pi)) *
      ‖(𝓕 (deriv (s : ℝ → ℂ))) (-r / (2 * Real.pi))‖^2) =
      neutralIV096DerivativeEnergy s := by
  let d := SchwartzMap.derivCLM ℂ ℂ s
  let F := (𝓕 d : 𝓢(ℝ,ℂ))
  have hF : Integrable (fun ξ : ℝ => ‖F ξ‖^2) :=
    (memLp_two_iff_integrable_sq_norm F.continuous.aestronglyMeasurable).mp (F.memLp 2 volume)
  have hn : (-(1 / (2 * Real.pi)) : ℝ) ≠ 0 := by
    exact neg_ne_zero.mpr (div_ne_zero one_ne_zero (mul_ne_zero (by norm_num) Real.pi_ne_zero))
  have harg (r : ℝ) : -(1 / (2 * Real.pi)) * r = -r / (2 * Real.pi) := by ring
  have hcoe (ξ : ℝ) : F ξ = (𝓕 (deriv (s : ℝ → ℂ))) ξ := rfl
  constructor
  · apply ((hF.comp_mul_left' hn).const_mul (1 / (2 * Real.pi))).congr
    filter_upwards [] with r
    rw [harg, hcoe]
  · simp_rw [← hcoe, ← harg]
    rw [integral_const_mul, Measure.integral_comp_mul_left]
    have habs : |(-(1 / (2 * Real.pi)) : ℝ)⁻¹| = 2 * Real.pi := by
      rw [inv_neg, abs_neg, one_div, inv_inv, abs_of_pos (by positivity)]
    rw [habs, smul_eq_mul]
    change (1 / (2 * Real.pi)) * ((2 * Real.pi) * ∫ ξ : ℝ, ‖F ξ‖^2) =
      neutralIV096DerivativeEnergy s
    rw [show (∫ ξ : ℝ, ‖F ξ‖^2) = neutralIV096DerivativeEnergy s from
      SchwartzMap.integral_norm_sq_fourier d]
    field_simp [Real.pi_ne_zero]

/-- Effective original diagonal tail on the smooth collar carrier:
this pays the quantitative Fourier-moment bridge separately from IV092. -/
theorem neutralIV096CollarTail_derivative_bound
    (M N : ℕ) (s : 𝓢(ℝ,ℂ)) (hs : neutralNF735InOriginalCollars s)
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ)) :
    neutralIV095DiagonalTail M N s ≤
      neutralIV096DerivativeEnergy s / ((N : ℝ)+1)^2 := by
  obtain ⟨hi, he⟩ := neutralIV095DiagonalTail_data M N s hs hM
  obtain ⟨hd, hdint⟩ := neutralIV096AngularDerivative_data s
  let A : ℝ := 1 / ((N : ℝ)+1)^2
  rw [he]
  calc
    _ ≤ ∫ r : ℝ, A * ((1 / (2 * Real.pi)) *
        ‖(𝓕 (deriv (s : ℝ → ℂ))) (-r / (2 * Real.pi))‖^2) := by
      apply integral_mono hi (hd.const_mul A)
      intro r
      unfold neutralIV095TailProfile
      rw [neutralIV096WindowEval_fourier s hs r, neutralIV096Derivative_fourier_sq]
      have hb := (neutralIV089GammaRemainder_bound N r).2
      have h := mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hb (show 0 ≤ 1 / (2 * Real.pi) by positivity))
        (sq_nonneg ‖(𝓕 (s : ℝ → ℂ)) (-r / (2 * Real.pi))‖)
      unfold neutralIV089TailEnvelope at h
      convert h using 1 <;> dsimp [A] <;> ring
    _ = _ := by rw [integral_const_mul, hdint]; dsimp [A]; ring

/-- Effective finite signed margin from an actual derivative-energy budget. -/
theorem neutralIV096Collar_effective_margin
    (M N : ℕ) (s : 𝓢(ℝ,ℂ)) (hs : neutralNF735InOriginalCollars s)
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ))
    (hbudget : neutralIV096DerivativeEnergy s ≤
      ((N : ℝ)+1)^2 * ((1/5:ℝ) * ‖s.toLp 2 volume‖^2)) :
    (1/5:ℝ) * ‖s.toLp 2 volume‖^2 ≤ neutralIV095FiniteDiagonal M N s := by
  have hf := neutralNF600SmoothCollarLower s hs
  have ht := neutralIV096CollarTail_derivative_bound M N s hs hM
  have hb : neutralIV096DerivativeEnergy s / ((N : ℝ)+1)^2 ≤
      (1/5:ℝ) * ‖s.toLp 2 volume‖^2 := by
    apply (div_le_iff₀ (by positivity)).mpr
    simpa only [mul_comm] using hbudget
  change neutralNF598SmoothWeil s - neutralIV095FiniteDiagonal M N s ≤ _ at ht
  linarith

/-- Rational clearance for the planned plateau: mass >= 1/2000,
energy <= 24000, N >= 20000. The analytic plateau bounds are explicit
premises here, not numerically evaluated or assumed as axioms. -/
theorem neutralIV096PlateauBudget (m e : ℝ) (N : ℕ)
    (hm : (1/2000:ℝ) ≤ m) (he : e ≤ 24000) (hN : 20000 ≤ N) :
    e ≤ ((N : ℝ)+1)^2 * ((1/5:ℝ) * m) := by
  have hn : (20000:ℝ) ≤ (N : ℝ) := by exact_mod_cast hN
  have hsq : (20001:ℝ)^2 ≤ ((N : ℝ)+1)^2 :=
    pow_le_pow_left₀ (by norm_num) (by linarith) 2
  calc
    e ≤ 24000 := he
    _ ≤ (20001:ℝ)^2 * ((1/5:ℝ) * (1/2000)) := by norm_num
    _ ≤ ((N : ℝ)+1)^2 * ((1/5:ℝ) * (1/2000)) :=
      mul_le_mul_of_nonneg_right hsq (by norm_num)
    _ ≤ _ := mul_le_mul_of_nonneg_left
      (mul_le_mul_of_nonneg_left hm (by norm_num)) (sq_nonneg _)

/-- Numerical cutoff receiver for the actual smooth form. -/
theorem neutralIV096Collar_cutoff20000
    (s : 𝓢(ℝ,ℂ)) (hs : neutralNF735InOriginalCollars s)
    (hm : (1/2000:ℝ) ≤ ‖s.toLp 2 volume‖^2)
    (he : neutralIV096DerivativeEnergy s ≤ 24000)
    (N : ℕ) (hN : 20000 ≤ N) :
    (1/5:ℝ) * ‖s.toLp 2 volume‖^2 ≤ neutralIV095FiniteDiagonal 10 N s := by
  have hM : Real.exp (2*(11/10:ℝ)) < (10:ℝ) := by
    calc
      _ < Real.exp (Real.log (10:ℝ)) := by
        apply Real.exp_lt_exp.mpr
        rw [Real.log_ten_eq]
        linarith [Real.log_two_gt_d9, Real.log_five_gt_d9]
      _ = _ := Real.exp_log (by norm_num)
  exact neutralIV096Collar_effective_margin 10 N s hs (by exact_mod_cast hM)
    (neutralIV096PlateauBudget _ _ N hm he hN)

#print axioms neutralIV096WindowEval_fourier
#print axioms neutralIV096Derivative_fourier_sq
#print axioms neutralIV096AngularDerivative_data
#print axioms neutralIV096CollarTail_derivative_bound
#print axioms neutralIV096Collar_effective_margin
#print axioms neutralIV096PlateauBudget
#print axioms neutralIV096Collar_cutoff20000

end
end WeilDefect
