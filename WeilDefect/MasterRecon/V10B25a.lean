import WeilDefect.MasterRecon.V10B24b
import Mathlib.Analysis.Calculus.Deriv.Slope

/-! V10B25a: scalar endpoint cancellation. The integral convergence
attachment is kept separate from the elementary endpoint limits. -/
namespace WeilDefect.MasterRecon.V10B25a

open Filter MeasureTheory Set
open scoped Topology
open V10B24b (den b)

theorem den_deriv_zero : HasDerivAt den 2 0 := by
  have he := (Real.hasDerivAt_exp (-2*(0:ℝ))).comp 0
    ((hasDerivAt_const 0 (-2:ℝ)).mul (hasDerivAt_id (0:ℝ)))
  unfold den
  have hh := (hasDerivAt_const 0 (1:ℝ)).sub he
  change HasDerivAt (fun r : ℝ => 1-Real.exp (-2*r)) _ 0 at hh
  convert hh using 1 <;> norm_num

theorem den_ratio_limit :
    Tendsto (fun r : ℝ => den r/r) (𝓝[≠] 0) (𝓝 2) := by
  have h := den_deriv_zero.tendsto_slope_zero
  have h0 : den 0 = 0 := by simp [den]
  simpa only [zero_add,h0,sub_zero,smul_eq_mul,div_eq_mul_inv,mul_comm] using h

theorem den_at_infinity : Tendsto den atTop (𝓝 1) := by
  have h : Tendsto (fun r : ℝ => 2*r) atTop atTop := by
    apply tendsto_atTop.2
    intro a
    filter_upwards [eventually_ge_atTop (a/2)] with r hr
    linarith
  have he := Real.tendsto_exp_neg_atTop_nhds_zero.comp h
  have hh := (tendsto_const_nhds (x := (1:ℝ)) (f := atTop)).sub he
  simpa [den,Function.comp_def,sub_zero] using hh

theorem log_ratio_limit :
    Tendsto (fun r : ℝ => Real.log (den r/r)) (𝓝[≠] 0) (𝓝 (Real.log 2)) :=
  (Real.continuousAt_log (by norm_num : (2:ℝ) ≠ 0)).tendsto.comp den_ratio_limit

theorem log_den_limit : Tendsto (fun r : ℝ => Real.log (den r)) atTop (𝓝 0) := by
  simpa only [Real.log_one,Function.comp_def] using
    (Real.continuousAt_log (by norm_num : (1:ℝ) ≠ 0)).tendsto.comp den_at_infinity

theorem constant_limit (L : ℝ) (hL : 0 < L) {α : Type*} {l : Filter α}
    (a T : α → ℝ)
    (ha : Tendsto a l (𝓝[≠] 0)) (hT : Tendsto T l atTop) :
    Tendsto (fun x => Real.log (den (T x))-Real.log (den (a x)/a x)-Real.log L)
      l (𝓝 (-Real.log (2*L))) := by
  have h := ((log_den_limit.comp hT).sub (log_ratio_limit.comp ha)).sub
    (tendsto_const_nhds (x := Real.log L))
  rw [Real.log_mul (by norm_num : (2:ℝ) ≠ 0) hL.ne']
  simpa only [zero_sub,neg_add_rev,Function.comp_def,sub_eq_add_neg,add_comm,zero_add,add_zero] using h

theorem cutoff_limit (L : ℝ) (hL : 0 < L) {α : Type*} {l : Filter α}
    (a T : α → ℝ) (ha : Tendsto a l (𝓝[≠] 0)) (hT : Tendsto T l atTop)
    (hcut : ∀ᶠ x in l, 0 < a x ∧ a x ≤ L ∧ L ≤ T x) :
    Tendsto (fun x => (∫ r in a x..L, b r-1/r)+(∫ r in L..T x, b r))
      l (𝓝 (-Real.log (2*L))) := by
  apply (constant_limit L hL a T ha hT).congr'
  filter_upwards [hcut] with x hx
  exact (V10B24b.finite_constant (a x) L (T x) hx.1 hx.2.1 hx.2.2).symm

theorem pilot_cutoff_limit {α : Type*} {l : Filter α} (a T : α → ℝ)
    (ha : Tendsto a l (𝓝[≠] 0)) (hT : Tendsto T l atTop)
    (hcut : ∀ᶠ x in l, 0 < a x ∧ a x ≤ 1/2 ∧ 1/2 ≤ T x) :
    Tendsto (fun x => (∫ r in a x..(1/2:ℝ), b r-1/r)+
      (∫ r in (1/2:ℝ)..T x, b r)) l (𝓝 0) := by
  have h := cutoff_limit (1/2:ℝ) (by norm_num) a T ha hT hcut
  norm_num at h
  exact h

end WeilDefect.MasterRecon.V10B25a

#print axioms WeilDefect.MasterRecon.V10B25a.den_deriv_zero
#print axioms WeilDefect.MasterRecon.V10B25a.den_ratio_limit
#print axioms WeilDefect.MasterRecon.V10B25a.den_at_infinity
#print axioms WeilDefect.MasterRecon.V10B25a.log_ratio_limit
#print axioms WeilDefect.MasterRecon.V10B25a.log_den_limit
#print axioms WeilDefect.MasterRecon.V10B25a.constant_limit
#print axioms WeilDefect.MasterRecon.V10B25a.cutoff_limit
#print axioms WeilDefect.MasterRecon.V10B25a.pilot_cutoff_limit
