import Mathlib.NumberTheory.LSeries.SumCoeff
import Mathlib.NumberTheory.LSeries.Dirichlet
import Mathlib.NumberTheory.Harmonic.ZetaAsymp
import Mathlib.Analysis.MellinTransform
import Mathlib.MeasureTheory.Function.Floor
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

/-! V10B7c: one-term Euler summation using native Mathlib 4.34.
The centered floor remainder is bounded and supported away from zero.
Its Mellin transform supplies the analytic continuation; the pole is
removed before invoking the identity principle. -/
namespace WeilDefect.MasterRecon.V10B7c

open Set Filter MeasureTheory Asymptotics Complex
open scoped Topology BigOperators

noncomputable def remainder (x : ℝ) : ℂ :=
  ((⌊x⌋₊ : ℝ) + 1/2 - x : ℝ)

theorem remainder_bound (x : ℝ) (hx : 1 < x) : ‖remainder x‖ ≤ 1 := by
  unfold remainder
  rw [Complex.norm_real,Real.norm_eq_abs]
  have h₁ := Nat.floor_le (show 0 ≤ x by linarith)
  have h₂ := Nat.lt_floor_add_one x
  apply abs_le.mpr
  constructor <;> linarith

theorem remainder_measurable : Measurable remainder := by
  unfold remainder
  fun_prop

noncomputable def cutRemainder : ℝ → ℂ := (Ioi (1:ℝ)).indicator remainder

theorem cut_bound (x : ℝ) : ‖cutRemainder x‖ ≤ 1 := by
  by_cases hx : x ∈ Ioi (1:ℝ)
  · simpa [cutRemainder,hx] using remainder_bound x hx
  · simp [cutRemainder,hx]

theorem cut_measurable : Measurable cutRemainder :=
  remainder_measurable.indicator measurableSet_Ioi

theorem cut_locallyIntegrable : LocallyIntegrableOn cutRemainder (Ioi (0:ℝ)) := by
  rw [locallyIntegrableOn_iff isOpen_Ioi.isLocallyClosed]
  intro K _ hK
  have h : IntegrableOn (fun _ : ℝ => (1:ℝ)) K :=
    integrableOn_const hK.measure_lt_top.ne
  exact h.mono' cut_measurable.aestronglyMeasurable
    (Filter.Eventually.of_forall (fun x => cut_bound x))

theorem cut_top : cutRemainder =O[atTop] (fun x : ℝ => x ^ (-(0:ℝ))) := by
  apply isBigO_of_le
  intro x
  simpa using cut_bound x

theorem cut_bottom (b : ℝ) :
    cutRemainder =O[𝓝[>] (0:ℝ)] (fun x : ℝ => x ^ (-b)) := by
  refine IsBigO.of_bound 1 ?_
  have h : ∀ᶠ x : ℝ in 𝓝 (0:ℝ), x < 1 :=
    isOpen_Iio.mem_nhds (by norm_num)
  filter_upwards [h.filter_mono nhdsWithin_le_nhds] with x hx
  have hz : cutRemainder x = 0 := by simp [cutRemainder,not_lt_of_ge hx.le]
  rw [hz,norm_zero,one_mul]
  exact norm_nonneg _

noncomputable def J (s : ℂ) : ℂ :=
  ∫ x in Ioi (1:ℝ), (x:ℂ)^(-(s+1))*remainder x

theorem J_eq_mellin (s : ℂ) : J s = mellin cutRemainder (-s) := by
  unfold J mellin
  simp only [smul_eq_mul,cutRemainder]
  have he : (fun x : ℝ => (x:ℂ)^(-s-1)*(Ioi (1:ℝ)).indicator remainder x) =
      (Ioi (1:ℝ)).indicator (fun x : ℝ => (x:ℂ)^(-(s+1))*remainder x) := by
    funext x
    by_cases hx : x ∈ Ioi (1:ℝ) <;>
      simp [hx,show -s-1 = -(s+1) by ring]
  rw [he,setIntegral_indicator measurableSet_Ioi]
  congr 1
  exact (inter_eq_right.mpr (Ioi_subset_Ioi (by norm_num : (0:ℝ) ≤ 1))).symm

theorem J_differentiable (s : ℂ) (hs : 0 < s.re) :
    DifferentiableAt ℂ J s := by
  have h : DifferentiableAt ℂ (mellin cutRemainder) (-s) := by
    apply mellin_differentiableAt_of_isBigO_rpow (a := 0) (b := -s.re-1)
      cut_locallyIntegrable cut_top
    · simp [hs]
    · exact cut_bottom _
    · simp
  have hcomp := h.comp s (differentiableAt_id.neg)
  have he : J = fun s => mellin cutRemainder (-s) := funext J_eq_mellin
  rw [he]
  exact hcomp

theorem power_integrable (s : ℂ) (hs : 0 < s.re) :
    IntegrableOn (fun x : ℝ => (x:ℂ)^(-(s+1))) (Ioi (1:ℝ)) :=
  integrableOn_Ioi_cpow_of_lt (by simp [Complex.add_re]; linarith) (by norm_num)

theorem remainder_integrable (s : ℂ) (hs : 0 < s.re) :
    IntegrableOn (fun x : ℝ => (x:ℂ)^(-(s+1))*remainder x) (Ioi (1:ℝ)) := by
  have h := (power_integrable s hs).norm
  apply h.mono'
  · exact ((continuousOn_of_forall_continuousAt (fun x hx =>
      Complex.continuousAt_ofReal_cpow_const _ _ (Or.inr (by linarith [hx] : x ≠ 0))))
      .aestronglyMeasurable measurableSet_Ioi).mul remainder_measurable.aestronglyMeasurable
  · filter_upwards [ae_restrict_mem measurableSet_Ioi] with x hx
    rw [norm_mul]
    simpa using mul_le_mul_of_nonneg_left (remainder_bound x hx) (norm_nonneg ((x:ℂ)^(-(s+1))))

theorem J_bound (s : ℂ) (hs : 0 < s.re) : ‖J s‖ ≤ 1/s.re := by
  unfold J
  have hpow : IntegrableOn (fun x : ℝ => x ^ (-s.re-1)) (Ioi (1:ℝ)) :=
    integrableOn_Ioi_rpow_of_lt (by linarith) (by norm_num)
  calc
    _ ≤ ∫ x in Ioi (1:ℝ), ‖(x:ℂ)^(-(s+1))*remainder x‖ :=
      norm_integral_le_integral_norm _
    _ ≤ ∫ x in Ioi (1:ℝ), x ^ (-s.re-1) := by
      apply integral_mono_of_nonneg (Filter.Eventually.of_forall (fun _ => norm_nonneg _)) hpow
      filter_upwards [ae_restrict_mem measurableSet_Ioi] with x hx
      rw [norm_mul,Complex.norm_cpow_eq_rpow_re_of_pos (by linarith [hx] : 0 < x)]
      simp only [Complex.neg_re,Complex.add_re,Complex.one_re,neg_add_rev]
      have he : -(s.re+1) = -s.re-1 := by ring
      rw [show -1 + -s.re = -s.re-1 by ring]
      simpa using mul_le_mul_of_nonneg_left (remainder_bound x hx) (Real.rpow_nonneg (by linarith [hx]) _)
    _ = _ := by
      rw [integral_Ioi_rpow_of_lt (by linarith : -s.re-1 < -1) (by norm_num : (0:ℝ) < 1),Real.one_rpow]
      ring

theorem dirichlet_floor (s : ℂ) (hs : 1 < s.re) :
    riemannZeta s = s * ∫ x in Ioi (1:ℝ), (⌊x⌋₊:ℂ)*(x:ℂ)^(-(s+1)) := by
  have ho : (fun n : ℕ => ∑ k ∈ Finset.Icc 1 n, (1:ℂ)) =O[atTop]
      (fun n : ℕ => (n:ℝ)^(1:ℝ)) := by
    apply isBigO_of_le
    intro n
    simp
  have h := LSeries_eq_mul_integral (1 : ℕ → ℂ) (r := 1) (by norm_num) hs
    (LSeriesSummable_one_iff.mpr hs) ho
  rw [LSeries_one_eq_riemannZeta hs] at h
  simpa using h

theorem floor_split (s : ℂ) (hs : 1 < s.re) :
    (∫ x in Ioi (1:ℝ), (⌊x⌋₊:ℂ)*(x:ℂ)^(-(s+1))) =
      J s + (∫ x in Ioi (1:ℝ), (x:ℂ)^(-s)) -
        (1/2:ℂ)*(∫ x in Ioi (1:ℝ), (x:ℂ)^(-(s+1))) := by
  have hJ := remainder_integrable s (by linarith)
  have hX : IntegrableOn (fun x : ℝ => (x:ℂ)^(-s)) (Ioi (1:ℝ)) :=
    integrableOn_Ioi_cpow_of_lt (by simp; linarith) (by norm_num)
  have hP := (power_integrable s (by linarith)).const_mul (1/2:ℂ)
  rw [← integral_const_mul,← integral_sub (hJ.add hX) hP,← integral_add hJ hX]
  apply setIntegral_congr_fun measurableSet_Ioi
  intro x hx
  have hx0 : (x:ℂ) ≠ 0 := by exact_mod_cast (by linarith [hx] : x ≠ 0)
  have he : (x:ℂ)^(-s) = (x:ℂ)^(-(s+1))*(x:ℂ) := by
    rw [← Complex.cpow_one (x:ℂ),← Complex.cpow_add _ _ hx0]
    congr 1
    ring
  rw [he]
  unfold remainder
  push_cast
  ring

theorem euler_on_convergence (s : ℂ) (hs : 1 < s.re) :
    riemannZeta s = 1/2 + 1/(s-1) + s*J s := by
  rw [dirichlet_floor s hs,floor_split s hs,
    integral_Ioi_cpow_of_lt (by simp; linarith) (by norm_num : (0:ℝ) < 1),
    integral_Ioi_cpow_of_lt (by simp [Complex.add_re]; linarith) (by norm_num : (0:ℝ) < 1)]
  have hs0 : s ≠ 0 := Complex.ne_zero_of_re_pos (by linarith)
  have hs1 : s ≠ 1 := by
    intro h
    simp [h] at hs
  simp only [Complex.ofReal_one,Complex.one_cpow]
  field_simp
  ring

def halfPlane : Set ℂ := {s | 0 < s.re}

noncomputable def poleRemovedEuler (s : ℂ) : ℂ :=
  1+(s-1)*(1/2+s*J s)

theorem poleRemovedEuler_analytic : AnalyticOnNhd ℂ poleRemovedEuler halfPlane := by
  have ho : IsOpen halfPlane := isOpen_lt continuous_const Complex.continuous_re
  apply DifferentiableOn.analyticOnNhd _ ho
  intro s hs
  have hj := J_differentiable s hs
  unfold poleRemovedEuler
  exact ((differentiableAt_const _).add
    ((differentiableAt_id.sub_const _).mul
      ((differentiableAt_const _).add (differentiableAt_id.mul hj)))).differentiableWithinAt

theorem poleRemoved_eq (s : ℂ) (hs : 0 < s.re) :
    poleRemovedEuler s = riemannZeta₁ s := by
  have hconv : Convex ℝ halfPlane := by
    intro x hx y hy a b ha hb hab
    change 0 < (a • x+b • y).re
    rw [Complex.add_re,Complex.smul_re,Complex.smul_re]
    have hax : 0 ≤ a*x.re := mul_nonneg ha hx.le
    have hby : 0 ≤ b*y.re := mul_nonneg hb hy.le
    rcases eq_or_lt_of_le ha with h | h
    · have hb' : 0 < b := by linarith
      linarith [mul_pos hb' hy]
    · linarith [mul_pos h hx]
  have hnear : ∀ᶠ z : ℂ in 𝓝 (2:ℂ), 1 < z.re :=
    (isOpen_lt continuous_const Complex.continuous_re).mem_nhds (by norm_num)
  have he : poleRemovedEuler =ᶠ[𝓝 (2:ℂ)] riemannZeta₁ := by
    filter_upwards [hnear] with z hz
    have h1 : z ≠ 1 := by intro h; simp [h] at hz
    have h := riemannZeta_eq_inv_sub_mul h1
    rw [euler_on_convergence z hz] at h
    unfold poleRemovedEuler
    field_simp at h ⊢
    linear_combination -h
  exact (poleRemovedEuler_analytic.eqOn_of_preconnected_of_eventuallyEq
    differentiable_riemannZeta₁.analyticOnNhd hconv.isPreconnected
    (by norm_num [halfPlane] : (2:ℂ) ∈ halfPlane) he) hs

theorem euler_halfPlane (s : ℂ) (hs : 0 < s.re) (h1 : s ≠ 1) :
    riemannZeta s = 1/2+1/(s-1)+s*J s := by
  have h := poleRemoved_eq s hs
  rw [riemannZeta_eq_inv_sub_mul h1,← h]
  unfold poleRemovedEuler
  field_simp
  ring

theorem elementary_growth (s : ℂ) (hs : 0 < s.re) (h1 : s ≠ 1) :
    ‖riemannZeta s‖ ≤ 1/2+1/‖1-s‖+‖s‖/s.re := by
  rw [euler_halfPlane s hs h1]
  calc
    _ ≤ ‖(1/2:ℂ)‖+‖1/(s-1)‖+‖s*J s‖ :=
      (norm_add_le _ _).trans (add_le_add_right (norm_add_le _ _) _)
    _ ≤ _ := by
      have hhalf : ‖(1/2:ℂ)‖ = (1/2:ℝ) := by
        rw [show (1/2:ℂ) = ((1/2:ℝ):ℂ) by norm_num,Complex.norm_real,Real.norm_eq_abs]
        norm_num
      rw [hhalf,norm_div,norm_one,norm_sub_rev,norm_mul]
      have h := mul_le_mul_of_nonneg_left (J_bound s hs) (norm_nonneg s)
      rw [mul_one_div] at h
      linarith

end WeilDefect.MasterRecon.V10B7c

#print axioms WeilDefect.MasterRecon.V10B7c.remainder_bound
#print axioms WeilDefect.MasterRecon.V10B7c.remainder_measurable
#print axioms WeilDefect.MasterRecon.V10B7c.cut_bound
#print axioms WeilDefect.MasterRecon.V10B7c.cut_measurable
#print axioms WeilDefect.MasterRecon.V10B7c.cut_locallyIntegrable
#print axioms WeilDefect.MasterRecon.V10B7c.cut_top
#print axioms WeilDefect.MasterRecon.V10B7c.cut_bottom
#print axioms WeilDefect.MasterRecon.V10B7c.J_eq_mellin
#print axioms WeilDefect.MasterRecon.V10B7c.J_differentiable
#print axioms WeilDefect.MasterRecon.V10B7c.power_integrable
#print axioms WeilDefect.MasterRecon.V10B7c.remainder_integrable
#print axioms WeilDefect.MasterRecon.V10B7c.J_bound
#print axioms WeilDefect.MasterRecon.V10B7c.dirichlet_floor
#print axioms WeilDefect.MasterRecon.V10B7c.floor_split
#print axioms WeilDefect.MasterRecon.V10B7c.euler_on_convergence
#print axioms WeilDefect.MasterRecon.V10B7c.poleRemovedEuler_analytic
#print axioms WeilDefect.MasterRecon.V10B7c.poleRemoved_eq
#print axioms WeilDefect.MasterRecon.V10B7c.euler_halfPlane
#print axioms WeilDefect.MasterRecon.V10B7c.elementary_growth
