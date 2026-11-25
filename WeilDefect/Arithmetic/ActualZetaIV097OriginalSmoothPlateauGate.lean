import WeilDefect.Arithmetic.ActualZetaIV096OriginalEffectiveCollarCutoffGate
import Mathlib.Analysis.Calculus.ContDiff.Deriv
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ContDiff

def neutralIV097Bump : ContDiffBump (0 : ℝ) where
  rIn := 1/8000
  rOut := 1/4000
  rIn_pos := by norm_num
  rIn_lt_rOut := by norm_num

def neutralIV097Rho : ℝ → ℝ := neutralIV097Bump.normed volume

/-- The exact normalization denominator is bounded below by the
length of the inner unit plateau. -/
theorem neutralIV097Bump_mass_lower :
    (1/4000:ℝ) ≤ ∫ x : ℝ, neutralIV097Bump x := by
  let J := Icc (-(1/8000:ℝ)) (1/8000)
  have hle : (∫ x in J, neutralIV097Bump x) ≤ ∫ x : ℝ, neutralIV097Bump x :=
    integral_mono_measure Measure.restrict_le_self
      (Filter.Eventually.of_forall neutralIV097Bump.nonneg') neutralIV097Bump.integrable
  have he : (∫ x in J, neutralIV097Bump x) = (1/4000:ℝ) := by
    calc
      _ = ∫ x in J, (1:ℝ) := by
        apply setIntegral_congr_fun measurableSet_Icc
        intro x hx
        apply neutralIV097Bump.one_of_mem_closedBall
        change dist x (0:ℝ) ≤ (1/8000:ℝ)
        rw [Real.dist_eq, sub_zero]
        exact abs_le.mpr hx
      _ = _ := by
        dsimp [J]
        rw [integral_Icc_eq_integral_Ioc, ← intervalIntegral.integral_of_le (by norm_num : -(1/8000:ℝ) ≤ 1/8000),
          intervalIntegral.integral_const]
        norm_num
  rw [he] at hle
  exact hle

theorem neutralIV097Rho_bounds (x : ℝ) :
    0 ≤ neutralIV097Rho x ∧ neutralIV097Rho x ≤ 4000 := by
  refine ⟨neutralIV097Bump.nonneg_normed x, ?_⟩
  change neutralIV097Bump x / (∫ t : ℝ, neutralIV097Bump t) ≤ 4000
  have hp : 0 < ∫ t : ℝ, neutralIV097Bump t :=
    lt_of_lt_of_le (by norm_num : (0:ℝ) < 1/4000) neutralIV097Bump_mass_lower
  apply (div_le_iff₀ hp).mpr
  have hb : neutralIV097Bump x ≤ 1 := neutralIV097Bump.le_one
  linarith [neutralIV097Bump_mass_lower]

theorem neutralIV097Rho_zero (x : ℝ) (hx : (1/4000:ℝ) ≤ |x|) :
    neutralIV097Rho x = 0 := by
  have hz : neutralIV097Bump x = 0 := by
    apply neutralIV097Bump.zero_of_le_dist
    simpa only [Real.dist_eq, sub_zero] using hx
  simp [neutralIV097Rho, ContDiffBump.normed, hz]

def neutralIV097Plateau (x : ℝ) : ℝ :=
  ∫ t in (x-1099/1000-1/2000)..(x-1099/1000+1/2000), neutralIV097Rho t

def neutralIV097PlateauDerivative (x : ℝ) : ℝ :=
  neutralIV097Rho (x-1099/1000+1/2000) -
    neutralIV097Rho (x-1099/1000-1/2000)

/-- Exact FTC on the sliding integral, with no numerical evaluation. -/
theorem neutralIV097Plateau_hasDerivAt (x : ℝ) :
    HasDerivAt neutralIV097Plateau (neutralIV097PlateauDerivative x) x := by
  let F : ℝ → ℝ := fun y => ∫ t in (0:ℝ)..y, neutralIV097Rho t
  have hc : Continuous neutralIV097Rho := neutralIV097Bump.continuous_normed
  have hF (y : ℝ) : HasDerivAt F (neutralIV097Rho y) y :=
    intervalIntegral.integral_hasDerivAt_right (hc.intervalIntegrable _ _)
      hc.aestronglyMeasurable.stronglyMeasurableAtFilter hc.continuousAt
  have hu : HasDerivAt (fun y : ℝ => y-1099/1000+1/2000) 1 x := by
    simpa using (((hasDerivAt_id x).sub_const (1099/1000:ℝ)).add_const (1/2000:ℝ))
  have hl : HasDerivAt (fun y : ℝ => y-1099/1000-1/2000) 1 x := by
    simpa using (((hasDerivAt_id x).sub_const (1099/1000:ℝ)).sub_const (1/2000:ℝ))
  have h := ((hF _).comp x hu).sub ((hF _).comp x hl)
  have he : (fun y : ℝ => F (y-1099/1000+1/2000) -
      F (y-1099/1000-1/2000)) = neutralIV097Plateau := by
    funext y
    exact intervalIntegral.integral_interval_sub_left
      (hc.intervalIntegrable _ _) (hc.intervalIntegrable _ _)
  change HasDerivAt (fun y : ℝ => F (y-1099/1000+1/2000) -
      F (y-1099/1000-1/2000)) _ x at h
  rw [he] at h
  simpa only [mul_one, neutralIV097PlateauDerivative] using h

theorem neutralIV097Plateau_smooth : ContDiff ℝ ∞ neutralIV097Plateau := by
  apply contDiff_infty_iff_deriv.mpr
  refine ⟨fun x => (neutralIV097Plateau_hasDerivAt x).differentiableAt, ?_⟩
  have he : deriv neutralIV097Plateau = neutralIV097PlateauDerivative :=
    funext fun x => (neutralIV097Plateau_hasDerivAt x).deriv
  rw [he]
  have h : ContDiff ℝ ∞ neutralIV097Rho := neutralIV097Bump.contDiff_normed
  unfold neutralIV097PlateauDerivative
  exact (h.comp (by fun_prop)).sub (h.comp (by fun_prop))

/-- Exact outer support and inner plateau at the original right collar. -/
theorem neutralIV097Plateau_zero (x : ℝ) (hx : (3/4000:ℝ) ≤ |x-1099/1000|) :
    neutralIV097Plateau x = 0 := by
  unfold neutralIV097Plateau
  have horder : x-1099/1000-1/2000 ≤ x-1099/1000+1/2000 := by linarith
  calc
    _ = ∫ t in (x-1099/1000-1/2000)..(x-1099/1000+1/2000), (0:ℝ) := by
      apply intervalIntegral.integral_congr
      rw [uIcc_of_le horder]
      intro t ht
      apply neutralIV097Rho_zero
      rcases le_total 0 (x-1099/1000) with h | h
      · rw [abs_of_nonneg h] at hx
        exact (show (1/4000:ℝ) ≤ t by linarith [ht.1]).trans (le_abs_self t)
      · rw [abs_of_nonpos h] at hx
        exact (show (1/4000:ℝ) ≤ -t by linarith [ht.2]).trans (neg_le_abs t)
    _ = 0 := by simp

theorem neutralIV097Plateau_one (x : ℝ) (hx : |x-1099/1000| ≤ (1/4000:ℝ)) :
    neutralIV097Plateau x = 1 := by
  unfold neutralIV097Plateau
  rw [intervalIntegral.integral_eq_integral_of_support_subset]
  · exact neutralIV097Bump.integral_normed
  · intro t ht
    have ht' : |t| < (1/4000:ℝ) := by
      by_contra h
      exact ht (neutralIV097Rho_zero t (le_of_not_gt h))
    have htx := abs_lt.mp ht'
    have hxx := abs_le.mp hx
    exact ⟨by linarith [htx.1,hxx.2], by linarith [htx.2,hxx.1]⟩

theorem neutralIV097PlateauDerivative_bounds (x : ℝ) :
    |neutralIV097PlateauDerivative x| ≤ 4000 := by
  have h1 := neutralIV097Rho_bounds (x-1099/1000+1/2000)
  have h2 := neutralIV097Rho_bounds (x-1099/1000-1/2000)
  unfold neutralIV097PlateauDerivative
  exact abs_le.mpr ⟨by linarith [h1.1,h2.2], by linarith [h1.2,h2.1]⟩

theorem neutralIV097PlateauDerivative_zero (x : ℝ)
    (hx : (3/4000:ℝ) ≤ |x-1099/1000|) :
    neutralIV097PlateauDerivative x = 0 := by
  have hz (t : ℝ) (ht : |t| ≤ (1/2000:ℝ)) :
      neutralIV097Rho (x-1099/1000+t) = 0 := by
    apply neutralIV097Rho_zero
    have hh := abs_sub_abs_le_abs_sub (x-1099/1000) (-t)
    rw [abs_neg, sub_neg_eq_add] at hh
    linarith
  unfold neutralIV097PlateauDerivative
  rw [hz (1/2000) (by norm_num), show x-1099/1000-1/2000 =
    x-1099/1000+(-(1/2000:ℝ)) by ring, hz _ (by norm_num)]
  ring

def neutralIV097ComplexPlateau : ℝ → ℂ := fun x => (neutralIV097Plateau x : ℂ)

theorem neutralIV097ComplexPlateau_compact : HasCompactSupport neutralIV097ComplexPlateau := by
  apply HasCompactSupport.intro (K := Icc (1099/1000-3/4000:ℝ) (1099/1000+3/4000)) isCompact_Icc
  intro x hx
  have hh : (3/4000:ℝ) ≤ |x-1099/1000| := by
    by_contra h
    have ha := abs_lt.mp (lt_of_not_ge h)
    exact hx ⟨by linarith [ha.1], by linarith [ha.2]⟩
  simp [neutralIV097ComplexPlateau, neutralIV097Plateau_zero x hh]

def neutralIV097Schwartz : 𝓢(ℝ,ℂ) :=
  neutralIV097ComplexPlateau_compact.toSchwartzMap
    (Complex.ofRealCLM.contDiff.comp neutralIV097Plateau_smooth)

theorem neutralIV097Schwartz_collars : neutralNF735InOriginalCollars neutralIV097Schwartz := by
  intro x hx
  have hh : (3/4000:ℝ) ≤ |x-1099/1000| := by
    by_contra h
    have ha := abs_lt.mp (lt_of_not_ge h)
    apply hx
    unfold neutralNF543OriginalCollars
    right
    constructor <;> linarith [ha.1,ha.2]
  change (neutralIV097Plateau x : ℂ) = 0
  simp [neutralIV097Plateau_zero x hh]

theorem neutralIV097Schwartz_derivative (x : ℝ) :
    deriv (neutralIV097Schwartz : ℝ → ℂ) x = (neutralIV097PlateauDerivative x : ℂ) := by
  exact (neutralIV097Plateau_hasDerivAt x).ofReal_comp.deriv

/-- Genuine physical L2 mass, computed by integration of the same
Schwartz representative, rather than by a coefficient norm. -/
theorem neutralIV097Schwartz_mass_lower :
    (1/2000:ℝ) ≤ ‖neutralIV097Schwartz.toLp 2 volume‖^2 := by
  let s := neutralIV097Schwartz
  let f := s.toLp 2 volume
  have hI : Integrable (fun x : ℝ => ‖s x‖^2) :=
    (memLp_two_iff_integrable_sq_norm s.continuous.aestronglyMeasurable).mp (s.memLp 2 volume)
  have hinner := inner_self_eq_norm_sq_to_K (𝕜 := ℂ) f
  rw [MeasureTheory.L2.inner_def] at hinner
  simp only [inner_self_eq_norm_sq_to_K] at hinner
  rw [integral_complex_ofReal] at hinner
  have hm : (∫ x : ℝ, ‖f x‖^2) = ‖f‖^2 := by exact_mod_cast hinner
  have hs : (∫ x : ℝ, ‖s x‖^2) = ‖f‖^2 := by
    rw [← hm]
    apply integral_congr_ae
    filter_upwards [s.coeFn_toLp 2 volume] with x hx
    change f x = s x at hx
    rw [hx]
  let J := Icc (1099/1000-1/4000:ℝ) (1099/1000+1/4000)
  have hl : (∫ x in J, ‖s x‖^2) ≤ ∫ x : ℝ, ‖s x‖^2 :=
    integral_mono_measure Measure.restrict_le_self
      (Filter.Eventually.of_forall fun x => sq_nonneg ‖s x‖) hI
  have he : (∫ x in J, ‖s x‖^2) = (1/2000:ℝ) := by
    calc
      _ = ∫ x in J, (1:ℝ) := by
        apply setIntegral_congr_fun measurableSet_Icc
        intro x hx
        have hh : |x-1099/1000| ≤ (1/4000:ℝ) :=
          abs_le.mpr ⟨by linarith [hx.1], by linarith [hx.2]⟩
        change ‖(neutralIV097Plateau x : ℂ)‖^2 = 1
        simp [neutralIV097Plateau_one x hh]
      _ = _ := by
        dsimp [J]
        rw [integral_Icc_eq_integral_Ioc, ← intervalIntegral.integral_of_le
          (by norm_num : (1099/1000-1/4000:ℝ) ≤ 1099/1000+1/4000),
          intervalIntegral.integral_const]
        norm_num
  rw [he, hs] at hl
  exact hl

/-- Actual derivative energy <= 4000² times the exact outer support
length 3/2000, with no unstated analytical premises. -/
theorem neutralIV097Schwartz_energy_upper :
    neutralIV096DerivativeEnergy neutralIV097Schwartz ≤ 24000 := by
  let g : ℝ → ℝ := fun x => ‖deriv (neutralIV097Schwartz : ℝ → ℂ) x‖^2
  let J := Icc (1099/1000-3/4000:ℝ) (1099/1000+3/4000)
  let d := SchwartzMap.derivCLM ℂ ℂ neutralIV097Schwartz
  have hg : Integrable g :=
    (memLp_two_iff_integrable_sq_norm d.continuous.aestronglyMeasurable).mp (d.memLp 2 volume)
  have hJ : Integrable (J.indicator (fun _ : ℝ => (4000:ℝ)^2)) := by
    apply (integrableOn_const (by simp [J, Real.volume_Icc])).integrable_indicator measurableSet_Icc
  have hpoint (x : ℝ) : g x ≤ J.indicator (fun _ : ℝ => (4000:ℝ)^2) x := by
    dsimp only [g]
    rw [neutralIV097Schwartz_derivative, Complex.norm_real, Real.norm_eq_abs]
    by_cases hx : x ∈ J
    · rw [Set.indicator_of_mem hx]
      exact pow_le_pow_left₀ (abs_nonneg _) (neutralIV097PlateauDerivative_bounds x) 2
    · rw [Set.indicator_of_notMem hx]
      have hh : (3/4000:ℝ) ≤ |x-1099/1000| := by
        by_contra h
        have ha := abs_lt.mp (lt_of_not_ge h)
        exact hx ⟨by linarith [ha.1], by linarith [ha.2]⟩
      simp [neutralIV097PlateauDerivative_zero x hh]
  change (∫ x : ℝ, g x) ≤ 24000
  calc
    _ ≤ ∫ x : ℝ, J.indicator (fun _ : ℝ => (4000:ℝ)^2) x :=
      integral_mono hg hJ hpoint
    _ = _ := by
      rw [integral_indicator measurableSet_Icc]
      dsimp [J]
      rw [integral_Icc_eq_integral_Ioc, ← intervalIntegral.integral_of_le
        (by norm_num : (1099/1000-3/4000:ℝ) ≤ 1099/1000+3/4000),
        intervalIntegral.integral_const]
      norm_num

/-- Terminal concrete finite margin: all IV096 analytic budget
premises paid on the explicit original plateau. -/
theorem neutralIV097Schwartz_cutoff20000 (N : ℕ) (hN : 20000 ≤ N) :
    (1/5:ℝ) * ‖neutralIV097Schwartz.toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal 10 N neutralIV097Schwartz :=
  neutralIV096Collar_cutoff20000 neutralIV097Schwartz neutralIV097Schwartz_collars
    neutralIV097Schwartz_mass_lower neutralIV097Schwartz_energy_upper N hN

#print axioms neutralIV097Bump_mass_lower
#print axioms neutralIV097Rho_bounds
#print axioms neutralIV097Rho_zero
#print axioms neutralIV097Plateau_hasDerivAt
#print axioms neutralIV097Plateau_smooth
#print axioms neutralIV097Plateau_zero
#print axioms neutralIV097Plateau_one
#print axioms neutralIV097PlateauDerivative_bounds
#print axioms neutralIV097PlateauDerivative_zero
#print axioms neutralIV097ComplexPlateau_compact
#print axioms neutralIV097Schwartz_collars
#print axioms neutralIV097Schwartz_derivative
#print axioms neutralIV097Schwartz_mass_lower
#print axioms neutralIV097Schwartz_energy_upper
#print axioms neutralIV097Schwartz_cutoff20000

end
end WeilDefect
