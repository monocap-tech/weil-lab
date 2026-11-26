import WeilDefect.Arithmetic.ActualZetaIV126OriginalCellPartition
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap FourierTransform BigOperators

/-- Physical L1/L2 comparison without a separate Holder convention. -/
theorem neutralIV127Interval_mass (f : ℝ → ℝ) (hf : Continuous f)
    (a : ℝ) (ha : 0 < a) :
    (∫ x in (-a)..a, f x)^2 ≤ 2*a*(∫ x in (-a)..a, (f x)^2) := by
  let L : ℝ := ∫ x in (-a)..a, f x
  let t : ℝ := L/(2*a)
  have h : 0 ≤ ∫ x in (-a)..a, (f x-t)^2 :=
    intervalIntegral.integral_nonneg_of_forall (by linarith) (fun x => sq_nonneg _)
  have h1 : IntervalIntegrable (fun x => f x^2) volume (-a) a :=
    (hf.pow 2).intervalIntegrable _ _
  have h2 : IntervalIntegrable (fun x => 2*t*f x) volume (-a) a :=
    (continuous_const.mul hf).intervalIntegrable _ _
  have h3 : IntervalIntegrable (fun _ : ℝ => t^2) volume (-a) a :=
    continuous_const.intervalIntegrable _ _
  have he : (∫ x in (-a)..a, (f x-t)^2) =
      (∫ x in (-a)..a, f x^2) - 2*t*L + (2*a)*t^2 := by
    calc
      _ = ∫ x in (-a)..a, (f x^2 - 2*t*f x)+t^2 := by
        apply intervalIntegral.integral_congr
        intro x hx
        ring
      _ = _ := by
        rw [intervalIntegral.integral_add (h1.sub h2) h3,
          intervalIntegral.integral_sub h1 h2, intervalIntegral.integral_const_mul,
          intervalIntegral.integral_const]
        change _ - 2*t*L + (a-(-a))*t^2 = _
        ring
  rw [he] at h
  have hh := mul_nonneg (show 0 ≤ 2*a by positivity) h
  dsimp [t] at hh
  have hne : 2*a ≠ 0 := by positivity
  field_simp at hh
  change L^2 ≤ _
  nlinarith only [hh, ha]

/-- The physical mass is exactly the supported interval squared mass. -/
theorem neutralIV127Window_mass (a : ℝ) (ha : 0 ≤ a) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    (∫ x in (-a)..a, ‖v x‖^2) = ‖v.toLp 2 volume‖^2 := by
  rw [intervalIntegral.integral_of_le (by linarith : -a ≤ a),
    ← integral_Icc_eq_integral_Ioc]
  rw [setIntegral_eq_integral_of_forall_compl_eq_zero
    (fun x hx => by rw [hv x hx]; simp)]
  rw [← neutralPhysicalL2_norm_sq]
  apply integral_congr_ae
  filter_upwards [v.coeFn_toLp 2 volume] with x hx
  rw [hx]

/-- Literal native Fourier normalization, with no phase or support premise
beyond the original supported Schwartz test. -/
theorem neutralIV127Fourier_window (a : ℝ) (ha : 0 ≤ a) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) (ξ : ℝ) :
    (𝓕 v : 𝓢(ℝ,ℂ)) ξ =
      ∫ x in (-a)..a, neutralIV126Phase ((-2*Real.pi*ξ)*x)*v x := by
  rw [← SchwartzMap.fourier_coe, Real.fourier_eq']
  simp only [smul_eq_mul]
  rw [intervalIntegral.integral_of_le (by linarith : -a ≤ a),
    ← integral_Icc_eq_integral_Ioc]
  rw [setIntegral_eq_integral_of_forall_compl_eq_zero
    (fun x hx => by rw [hv x hx, mul_zero])]
  apply integral_congr_ae
  filter_upwards [] with x
  unfold neutralIV126Phase
  congr 1
  congr 1
  simp only [Real.inner_apply]
  push_cast
  ring

def neutralIV127CellNull (a : ℝ) (N : ℕ) (v : 𝓢(ℝ,ℂ)) : Prop :=
  ∀ j < N, (∫ x in Set.Ioc
    (neutralIV126Node (-a) (2*a/(N:ℝ)) j)
    (neutralIV126Node (-a) (2*a/(N:ℝ)) (j+1)), v x) = 0

def neutralIV127Leakage (a : ℝ) (N : ℕ) (T : ℝ) : ℝ :=
  16*Real.pi^2*a*(2*a/(N:ℝ))^2*T^3/3

theorem neutralIV127Fourier_sq (a : ℝ) (ha : 0 < a) (N : ℕ) (hN : 0 < N)
    (v : 𝓢(ℝ,ℂ)) (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (hm : neutralIV127CellNull a N v) (ξ : ℝ) :
    ‖(𝓕 v : 𝓢(ℝ,ℂ)) ξ‖^2 ≤
      (8*Real.pi^2*a*(2*a/(N:ℝ))^2*‖v.toLp 2 volume‖^2)*ξ^2 := by
  have h := neutralIV126Window_payment v a (-2*Real.pi*ξ) N ha.le hN hm
  rw [← neutralIV127Fourier_window a ha.le v hv ξ] at h
  have hs := pow_le_pow_left₀ (norm_nonneg _) h 2
  have hc := neutralIV127Interval_mass (fun x => ‖v x‖) v.continuous.norm a ha
  rw [neutralIV127Window_mass a ha.le v hv] at hc
  have hp := mul_le_mul_of_nonneg_left hc (sq_nonneg (|-2*Real.pi*ξ| * (2*a/(N:ℝ))))
  calc
    _ ≤ ((|-2*Real.pi*ξ| * (2*a/(N:ℝ))) *
        (∫ x in (-a)..a, ‖v x‖))^2 := hs
    _ = (|-2*Real.pi*ξ| * (2*a/(N:ℝ)))^2 *
        (∫ x in (-a)..a, ‖v x‖)^2 := by ring
    _ ≤ _ := by
      convert hp using 1
      rw [mul_pow, sq_abs]
      ring

theorem neutralIV127LowBand (a : ℝ) (ha : 0 < a) (N : ℕ) (hN : 0 < N)
    (v : 𝓢(ℝ,ℂ)) (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (hm : neutralIV127CellNull a N v) (T : ℝ) (hT : 0 ≤ T) :
    (∫ ξ in Set.Ioc (-T) T, ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2) ≤
      neutralIV127Leakage a N T * ‖v.toLp 2 volume‖^2 := by
  have h := neutralIV126LowBand_ae v T _ hT
    (neutralIV126Fourier_ae_bound v _ (neutralIV127Fourier_sq a ha N hN v hv hm))
  unfold neutralIV127Leakage
  convert h using 1 <;> ring

/-- Actual cell-null tail coercivity, with only the scalar margin test left. -/
theorem neutralIV127Schur_cellNull (k : ℕ) (hk : 0 < k) (N : ℕ) (hN : 0 < N)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hm : neutralIV127CellNull (11/10:ℝ) N v)
    (T eta : ℝ) (hT : 0 ≤ T)
    (hmargin : eta ≤ (1-neutralIV127Leakage (11/10:ℝ) N T)*Real.log (Real.exp 1+T) -
      (neutralActualZetaNativeLogError (11/10:ℝ) +
       neutralPhysicalPoleEnergyConstant (11/10:ℝ) +
       neutralIV124PhysicalBudget k hk)) :
    eta * ‖v.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk v :=
  neutralIV125Schur_of_leakage k hk v hv T _ eta hT
    (neutralIV127LowBand _ (by norm_num) N hN v hv hm T hT) hmargin

#print axioms neutralIV127Interval_mass
#print axioms neutralIV127Window_mass
#print axioms neutralIV127Fourier_window
#print axioms neutralIV127Fourier_sq
#print axioms neutralIV127LowBand
#print axioms neutralIV127Schur_cellNull

end
end WeilDefect
