import WeilDefect.Arithmetic.ActualZetaIV100OriginalAffineCollarPacking
import Mathlib.Analysis.Convolution

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped Convolution SchwartzMap

/-- The literal sliding window in IV097 is the convolution of its actual
choice-defined normalized bump with this fixed indicator. -/
def neutralIV106E18MBox : ℝ → ℝ :=
  (Icc (-(1/2000:ℝ)) (1/2000)).indicator (fun _ => 1)

theorem neutralIV106E18MBox_integrable : Integrable neutralIV106E18MBox := by
  unfold neutralIV106E18MBox
  exact (continuous_const.integrableOn_Icc).integrable_indicator measurableSet_Icc

theorem neutralIV106E18MBox_mass :
    (∫ x, neutralIV106E18MBox x) = 1/1000 := by
  unfold neutralIV106E18MBox
  rw [integral_indicator measurableSet_Icc, integral_Icc_eq_integral_Ioc,
    ← intervalIntegral.integral_of_le (by norm_num : -(1/2000:ℝ) ≤ 1/2000),
    intervalIntegral.integral_const]
  norm_num

theorem neutralIV106E18MPlateau_nonneg (x : ℝ) :
    0 ≤ neutralIV097Plateau x := by
  unfold neutralIV097Plateau
  apply intervalIntegral.integral_nonneg (by linarith)
  intro t ht
  exact (neutralIV097Rho_bounds t).1

theorem neutralIV106E18MPlateau_convolution (x : ℝ) :
    neutralIV097Plateau x =
      (neutralIV097Rho ⋆[ContinuousLinearMap.mul ℝ ℝ] neutralIV106E18MBox)
        (x-1099/1000) := by
  unfold neutralIV097Plateau
  rw [intervalIntegral.integral_of_le (by linarith),
    ← integral_Icc_eq_integral_Ioc, ← integral_indicator measurableSet_Icc]
  rw [MeasureTheory.convolution_def]
  apply integral_congr_ae
  filter_upwards [] with t
  simp only [ContinuousLinearMap.mul_apply']
  by_cases ht : t ∈ Icc (x-1099/1000-1/2000) (x-1099/1000+1/2000)
  · have hb : x-1099/1000-t ∈ Icc (-(1/2000:ℝ)) (1/2000) :=
      ⟨by linarith [ht.2],by linarith [ht.1]⟩
    rw [Set.indicator_of_mem ht,neutralIV106E18MBox,Set.indicator_of_mem hb,mul_one]
  · have hb : x-1099/1000-t ∉ Icc (-(1/2000:ℝ)) (1/2000) := by
      intro hh
      exact ht ⟨by linarith [hh.2],by linarith [hh.1]⟩
    rw [Set.indicator_of_notMem ht,neutralIV106E18MBox,Set.indicator_of_notMem hb,mul_zero]

/-- Exact L1 mass, not L2 mass and not a numerical evaluation of the bump. -/
theorem neutralIV106E18MPlateau_mass :
    (∫ x, neutralIV097Plateau x) = 1/1000 := by
  simp_rw [neutralIV106E18MPlateau_convolution]
  rw [show (fun x : ℝ =>
      (neutralIV097Rho ⋆[ContinuousLinearMap.mul ℝ ℝ] neutralIV106E18MBox)
        (x-1099/1000)) =
      (fun x : ℝ =>
      (neutralIV097Rho ⋆[ContinuousLinearMap.mul ℝ ℝ] neutralIV106E18MBox)
        (x+(-(1099/1000:ℝ)))) by rfl]
  rw [integral_add_right_eq_self,
    integral_convolution (L := ContinuousLinearMap.mul ℝ ℝ)
      (show Integrable neutralIV097Rho volume from neutralIV097Bump.integrable_normed)
      neutralIV106E18MBox_integrable]
  change (∫ x, neutralIV097Rho x) * (∫ x, neutralIV106E18MBox x) = _
  rw [show (∫ x, neutralIV097Rho x) = 1 from neutralIV097Bump.integral_normed,
    neutralIV106E18MBox_mass,one_mul]

/-- The real profile underlying the actual packed carrier. -/
def neutralIV106E18MProfile (k : ℕ) (i : Fin k) (x : ℝ) : ℝ :=
  neutralIV097Plateau ((k:ℝ)*x+neutralIV100PackShift k i.val)

theorem neutralIV106E18MCarrier_real (k : ℕ) (hk : 0 < k) (i : Fin k) (x : ℝ) :
    neutralIV100Carrier k hk i x = (neutralIV106E18MProfile k i x : ℂ) := rfl

theorem neutralIV106E18MProfile_nonneg (k : ℕ) (i : Fin k) (x : ℝ) :
    0 ≤ neutralIV106E18MProfile k i x := neutralIV106E18MPlateau_nonneg _

theorem neutralIV106E18MProfile_mass (k : ℕ) (hk : 0 < k) (i : Fin k) :
    (∫ x, neutralIV106E18MProfile k i x) = 1/(1000*(k:ℝ)) := by
  unfold neutralIV106E18MProfile
  rw [neutralIV100Affine_integral _ _ _ (by exact_mod_cast hk),
    neutralIV106E18MPlateau_mass]
  ring

/-- Exact translation by one affine collar cell per row, all profiles
being copies of the same certified choice-defined plateau. -/
theorem neutralIV106E18MProfile_translate (k : ℕ) (hk : 0 < k) (i : Fin k) (x : ℝ) :
    neutralIV106E18MProfile k i x =
      neutralIV106E18MProfile k ⟨0,hk⟩
        (x-(i.val:ℝ)*(3/(2000*(k:ℝ)))) := by
  unfold neutralIV106E18MProfile neutralIV100PackShift
  congr 1
  have hkr : (k:ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hk)
  simp only [Nat.cast_zero]
  field_simp [hkr] <;> ring

theorem neutralIV106E18MProfile_compact (k : ℕ) (hk : 0 < k) (i : Fin k) :
    HasCompactSupport (neutralIV106E18MProfile k i) := by
  apply HasCompactSupport.intro
    (K := Icc (4393/4000:ℝ) (4399/4000)) isCompact_Icc
  intro x hx
  have hz : (3/4000:ℝ) ≤ |(k:ℝ)*x+neutralIV100PackShift k i.val-1099/1000| := by
    by_contra hn
    obtain ⟨hl,hu⟩ := neutralIV100Pack_containment k i.val hk i.isLt x (lt_of_not_ge hn)
    exact hx ⟨by linarith,by linarith⟩
  exact neutralIV097Plateau_zero _ hz

/-- Exponential row factors are strictly positive for every real rate.
Only the actual normalized bump's nonnegativity and inner plateau are used. -/
theorem neutralIV106E18MProfile_weight_pos (k : ℕ) (hk : 0 < k) (i : Fin k) (s : ℝ) :
    0 < ∫ x, neutralIV106E18MProfile k i x * Real.exp (s*x) := by
  have hc : Continuous (neutralIV106E18MProfile k i) :=
    neutralIV097Plateau_smooth.continuous.comp (by fun_prop)
  have hcont : Continuous (fun x => neutralIV106E18MProfile k i x * Real.exp (s*x)) :=
    hc.mul (by fun_prop)
  have hcomp : HasCompactSupport (fun x => neutralIV106E18MProfile k i x * Real.exp (s*x)) :=
    (neutralIV106E18MProfile_compact k hk i).mul_right (f' := fun x => Real.exp (s*x))
  have hkr : (0:ℝ) < (k:ℝ) := by exact_mod_cast hk
  let x₀ := (1099/1000-neutralIV100PackShift k i.val)/(k:ℝ)
  have hx : neutralIV106E18MProfile k i x₀ = 1 := by
    unfold neutralIV106E18MProfile
    apply neutralIV097Plateau_one
    have he : (k:ℝ)*x₀+neutralIV100PackShift k i.val-1099/1000 = 0 := by
      dsimp [x₀]
      field_simp [hkr.ne'] <;> ring
    rw [he,abs_zero]
    norm_num
  apply integral_pos_of_integrable_nonneg_nonzero (x := x₀) hcont
    (hcont.integrable_of_hasCompactSupport hcomp)
    (fun x => mul_nonneg (neutralIV106E18MProfile_nonneg k i x) (Real.exp_pos _).le)
  rw [hx,one_mul]
  exact (Real.exp_pos _).ne'

/-- Translation turns the weighted integral into a geometric row factor. -/
theorem neutralIV106E18MProfile_weight_translate (k : ℕ) (hk : 0 < k)
    (i : Fin k) (s : ℝ) :
    (∫ x, neutralIV106E18MProfile k i x * Real.exp (s*x)) =
      Real.exp (s*((i.val:ℝ)*(3/(2000*(k:ℝ))))) *
        (∫ x, neutralIV106E18MProfile k ⟨0,hk⟩ x * Real.exp (s*x)) := by
  let d : ℝ := (i.val:ℝ)*(3/(2000*(k:ℝ)))
  let F : ℝ → ℝ := fun x => neutralIV106E18MProfile k i x * Real.exp (s*x)
  calc
    _ = ∫ x, F (x+d) := (integral_add_right_eq_self F d).symm
    _ = ∫ x, Real.exp (s*d) *
        (neutralIV106E18MProfile k ⟨0,hk⟩ x * Real.exp (s*x)) := by
      apply integral_congr_ae
      filter_upwards [] with x
      dsimp [F]
      rw [neutralIV106E18MProfile_translate k hk i]
      change neutralIV106E18MProfile k ⟨0,hk⟩ (x+d-d) * Real.exp (s*(x+d)) = _
      rw [add_sub_cancel_right, mul_add,Real.exp_add]
      ring
    _ = _ := by rw [integral_const_mul]

#print axioms neutralIV106E18MBox_integrable
#print axioms neutralIV106E18MBox_mass
#print axioms neutralIV106E18MPlateau_nonneg
#print axioms neutralIV106E18MPlateau_convolution
#print axioms neutralIV106E18MPlateau_mass
#print axioms neutralIV106E18MCarrier_real
#print axioms neutralIV106E18MProfile_nonneg
#print axioms neutralIV106E18MProfile_mass
#print axioms neutralIV106E18MProfile_translate
#print axioms neutralIV106E18MProfile_compact
#print axioms neutralIV106E18MProfile_weight_pos
#print axioms neutralIV106E18MProfile_weight_translate
end
end WeilDefect
