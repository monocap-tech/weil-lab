import WeilDefect.MasterRecon.V10B8f
import Mathlib.NumberTheory.ZetaValues
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.Analysis.Real.Pi.Bounds

/-! V10B15a: explicit central digamma enclosure.
The partial-fraction identity is received from Zeta23/GammaFacts/Series.lean
at mirror revision 77f832c86fbb3e5336b949dae0fdcae26baea87c,
blob 2c6cf90050c2e6d5cbef0745d0445e3a8d02394a.
It is a theorem parameter, not an adopted dependency. -/
namespace WeilDefect.MasterRecon.V10B15a

open Complex MeasureTheory
open scoped BigOperators

def CentralSeries : Prop :=
  ∀ v : ℝ, |v| ≤ 1/2 →
    let z : ℂ := 1/4+I*(v:ℂ)
    HasSum (fun n : ℕ => 1/((n:ℂ)+1)-1/(z+n+1))
      (Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z)

theorem central_term (z : ℂ) (hz : 0 ≤ z.re) (hn : ‖z‖ ≤ 1) (n : ℕ) :
    ‖1/((n:ℂ)+1)-1/(z+n+1)‖ ≤ 1/((n:ℝ)+1)^2 := by
  let a : ℂ := (n:ℂ)+1
  have ha : ‖a‖ = (n:ℝ)+1 := by
    dsimp [a]
    rw [← Complex.ofReal_natCast,← Complex.ofReal_one,← Complex.ofReal_add,Complex.norm_real,
      Real.norm_eq_abs,abs_of_nonneg (by positivity)]
  have hb : (n:ℝ)+1 ≤ ‖z+a‖ := by
    have h := Complex.abs_re_le_norm (z+a)
    have h' := le_abs_self (z+a).re
    have hr : (z+a).re = z.re+(n:ℝ)+1 := by simp [a]; ring
    rw [hr] at h h'
    linarith
  have ha0 : a ≠ 0 := by intro h; rw [h,norm_zero] at ha; linarith [Nat.cast_nonneg (α := ℝ) n]
  have hb0 : z+a ≠ 0 := by intro h; rw [h,norm_zero] at hb; linarith [Nat.cast_nonneg (α := ℝ) n]
  have he : 1/a-1/(z+a) = z/(a*(z+a)) := by field_simp [ha0,hb0]; ring
  change ‖1/a-1/(z+n+1)‖ ≤ _
  rw [show z+(n:ℂ)+1 = z+a by dsimp [a]; ring,he,norm_div,norm_mul,ha]
  apply (div_le_div_iff₀ (by positivity : 0 < ((n:ℝ)+1)*‖z+a‖) (by positivity)).mpr
  have h := mul_le_mul_of_nonneg_left hb (show 0 ≤ (n:ℝ)+1 by positivity)
  have h' := mul_le_mul_of_nonneg_right hn (sq_nonneg ((n:ℝ)+1))
  nlinarith only [h,h']

theorem reciprocal_square_budget :
    HasSum (fun n : ℕ => 1/((n:ℝ)+1)^2) (Real.pi^2/6) := by
  have h := (hasSum_nat_add_iff' 1).mpr hasSum_zeta_two
  simpa using h

theorem central_digamma (hs : CentralSeries) (v : ℝ) (hv : |v| ≤ 1/2) :
    ‖Complex.digamma ((1/4:ℂ)+I*(v:ℂ))‖ ≤ 7 := by
  let z : ℂ := 1/4+I*(v:ℂ)
  have hr : z.re = 1/4 := by simp [z,Complex.div_re]; norm_num
  have hi : z.im = v := by simp [z,Complex.div_im]
  have hn : ‖z‖ ≤ 1 := by
    have h := Complex.norm_le_abs_re_add_abs_im z
    rw [hr,hi,abs_of_nonneg (by norm_num : (0:ℝ) ≤ 1/4)] at h
    linarith
  have hlow : (1/4:ℝ) ≤ ‖z‖ := by
    have h := Complex.abs_re_le_norm z
    rw [hr,abs_of_nonneg (by norm_num : (0:ℝ) ≤ 1/4)] at h
    exact h
  have hInv : ‖1/z‖ ≤ 4 := by
    rw [norm_div,norm_one]
    exact (div_le_iff₀ (by linarith : 0 < ‖z‖)).mpr (by linarith)
  let f : ℕ → ℂ := fun n => 1/((n:ℂ)+1)-1/(z+n+1)
  have hsum : HasSum f (Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z) := hs v hv
  have hterm : ∀ n, ‖f n‖ ≤ 1/((n:ℝ)+1)^2 := central_term z (by rw [hr]; norm_num) hn
  have hnorm : Summable (fun n => ‖f n‖) :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hterm reciprocal_square_budget.summable
  have hbound := (norm_tsum_le_tsum_norm hnorm).trans
    (hnorm.tsum_le_tsum hterm reciprocal_square_budget.summable)
  rw [hsum.tsum_eq,reciprocal_square_budget.tsum_eq] at hbound
  have hpi : Real.pi^2/6 ≤ 2 := by
    have hp := Real.pi_lt_d2
    have h := mul_nonneg (show 0 ≤ 3.15-Real.pi by linarith) (show 0 ≤ 3.15+Real.pi by positivity)
    nlinarith only [h]
  have hγ : ‖(Real.eulerMascheroniConstant:ℂ)‖ ≤ 1 := by
    rw [Complex.norm_real,Real.norm_eq_abs,abs_of_pos (by linarith [Real.one_half_lt_eulerMascheroniConstant])]
    linarith [Real.eulerMascheroniConstant_lt_two_thirds]
  change ‖Complex.digamma z‖ ≤ 7
  have he : Complex.digamma z = (Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z)-
      (Real.eulerMascheroniConstant:ℂ)-1/z := by ring
  conv_lhs => rw [he]
  have h₁ := norm_sub_le (Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z)
    (Real.eulerMascheroniConstant:ℂ)
  have h₂ := norm_sub_le (Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z-
    (Real.eulerMascheroniConstant:ℂ)) (1/z)
  linarith

noncomputable def globalBudget : ℝ := 20+|Real.log Real.pi|+Real.log 6

theorem central_residual (hs : CentralSeries) (u : ℝ) (hu : |-Real.pi*u| ≤ 1/2) :
    |V10B8e.residual u| ≤ globalBudget := by
  let v := -Real.pi*u
  have hv : |v| ≤ 1/2 := hu
  have hψ := (Complex.abs_re_le_norm _).trans (central_digamma hs v hv)
  have hlog : Real.log (2+2*|v|) ≤ Real.log 6 :=
    Real.log_le_log (by positivity) (by linarith)
  have hlog0 : 0 ≤ Real.log (2+2*|v|) := Real.log_nonneg (by linarith [abs_nonneg v])
  rw [V10B8e.residual,V10B8f.gammaSymbol_reparam,V10B8f.weight_reparam]
  change |(Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re-Real.log Real.pi-Real.log (2+2*|v|)| ≤ _
  have h := abs_sub_le ((Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re-Real.log Real.pi)
    (Real.log (2+2*|v|))
  have h' := abs_sub_le ((Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re) (Real.log Real.pi)
  rw [abs_of_nonneg hlog0] at h
  unfold globalBudget
  linarith

theorem explicit_residual (hS : CentralSeries) (hV : V10B8f.VerticalStirling) :
    Measurable V10B8e.residual ∧ 0 ≤ globalBudget ∧
      ∀ u, |V10B8e.residual u| ≤ globalBudget := by
  refine ⟨V10B8f.residual_continuous.measurable,?_ ,?_⟩
  · unfold globalBudget
    have h : 0 ≤ Real.log 6 := Real.log_nonneg (by norm_num)
    positivity
  · intro u
    by_cases hu : |-Real.pi*u| ≤ 1/2
    · exact central_residual hS u hu
    · exact V10B8f.tail_residual hV u (le_of_not_ge hu)

end WeilDefect.MasterRecon.V10B15a

#print axioms WeilDefect.MasterRecon.V10B15a.central_term
#print axioms WeilDefect.MasterRecon.V10B15a.reciprocal_square_budget
#print axioms WeilDefect.MasterRecon.V10B15a.central_digamma
#print axioms WeilDefect.MasterRecon.V10B15a.central_residual
#print axioms WeilDefect.MasterRecon.V10B15a.explicit_residual
