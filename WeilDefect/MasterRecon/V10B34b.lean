import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul

/-! V10B34b: direct beta-moment contraction for the exponential weight.
This does not assume the infinite Legendre expansion or the spherical
coefficient recurrence. -/
namespace WeilDefect.MasterRecon.V10B34b
open MeasureTheory Set

noncomputable def w (x : ℝ) : ℝ := x*(1-x)
noncomputable def e (a b x : ℝ) : ℝ := Real.exp (a*x+b)
noncomputable def moment (j : ℕ) (a b : ℝ) : ℝ :=
  ∫ x in (0:ℝ)..1, e a b x*w x^j
noncomputable def skew (j : ℕ) (a b : ℝ) : ℝ :=
  ∫ x in (0:ℝ)..1, e a b x*(2*x-1)*w x^j

theorem skew_nonneg (j : ℕ) (a b : ℝ) (ha : 0 ≤ a) :
    0 ≤ skew j a b := by
  let f : ℝ → ℝ := fun x => e a b x*(2*x-1)*w x^j
  have hc : Continuous f := by dsimp [f,e,w]; fun_prop
  have hcr : Continuous (fun x => f (1-x)) := by fun_prop
  have hr : (∫ x in (0:ℝ)..1, f (1-x)) = ∫ x in (0:ℝ)..1, f x := by
    simpa using intervalIntegral.integral_comp_sub_left (a := (0:ℝ)) (b := 1) f 1
  have h : 0 ≤ ∫ x in (0:ℝ)..1, f x + f (1-x) := by
    apply intervalIntegral.integral_nonneg (by norm_num)
    intro x hx
    have hw : 0 ≤ w x := mul_nonneg hx.1 (sub_nonneg.mpr hx.2)
    have hsym : w (1-x) = w x := by unfold w; ring
    have he : f x+f (1-x) = (e a b x-e a b (1-x))*(2*x-1)*w x^j := by
      dsimp [f]
      rw [hsym]
      ring
    rw [he]
    apply mul_nonneg _ (pow_nonneg hw _)
    by_cases hx' : x ≤ 1/2
    · apply mul_nonneg_of_nonpos_of_nonpos
      · apply sub_nonpos.mpr
        unfold e
        apply Real.exp_le_exp.mpr
        have hh : a*x ≤ a*(1-x) := mul_le_mul_of_nonneg_left (by linarith) ha
        linarith
      · linarith
    · apply mul_nonneg
      · apply sub_nonneg.mpr
        unfold e
        apply Real.exp_le_exp.mpr
        have hh : a*(1-x) ≤ a*x := mul_le_mul_of_nonneg_left (by linarith) ha
        linarith
      · linarith
  rw [intervalIntegral.integral_add (hc.intervalIntegrable 0 1)
    (hcr.intervalIntegrable 0 1),hr] at h
  change 0 ≤ ∫ x in (0:ℝ)..1, f x
  linarith

theorem moment_step (j : ℕ) (a b : ℝ) (ha : 0 ≤ a) :
    (4*(j:ℝ)+6)*moment (j+1) a b ≤ ((j:ℝ)+1)*moment j a b := by
  let u : ℝ → ℝ := e a b
  let v : ℝ → ℝ := fun x => (2*x-1)*w x^(j+1)
  let v' : ℝ → ℝ := fun x => (4*(j:ℝ)+6)*w x^(j+1)-((j:ℝ)+1)*w x^j
  have hu (x : ℝ) : HasDerivAt u (a*u x) x := by
    have h := (Real.hasDerivAt_exp (a*x+b)).comp x
      (((hasDerivAt_id x).const_mul a).add_const b)
    convert h using 1 <;> first | rfl | (simp [u,e,Function.comp_def] <;> ring)
  have hw (x : ℝ) : HasDerivAt w (1-2*x) x := by
    have h := (hasDerivAt_id x).mul ((hasDerivAt_const x (1:ℝ)).sub (hasDerivAt_id x))
    convert h using 1 <;> first | rfl | (simp [w,Pi.mul_apply] <;> ring)
  have hv (x : ℝ) : HasDerivAt v (v' x) x := by
    have h := (((hasDerivAt_id x).const_mul 2).sub_const 1).mul ((hw x).pow (j+1))
    convert h using 1
    all_goals first | rfl | (simp [v,v',w,pow_succ,Pi.mul_apply,Pi.pow_apply] <;> ring)
  have huc : Continuous (fun x => a*u x) := by dsimp [u,e]; fun_prop
  have hvc : Continuous v' := by dsimp [v',w]; fun_prop
  have hp := intervalIntegral.integral_mul_deriv_eq_deriv_mul
    (a := (0:ℝ)) (b := 1) (fun x _ => hu x) (fun x _ => hv x)
    (huc.intervalIntegrable 0 1) (hvc.intervalIntegrable 0 1)
  have hzero : v 0=0 ∧ v 1=0 := by simp [v,w,pow_succ]
  have hL : (fun x => u x*v' x) =
      fun x => (4*(j:ℝ)+6)*(e a b x*w x^(j+1))-((j:ℝ)+1)*(e a b x*w x^j) := by
    funext x
    dsimp [u,v']
    ring
  have hR : (fun x => (a*u x)*v x) = fun x => a*(e a b x*(2*x-1)*w x^(j+1)) := by
    funext x
    dsimp [u,v]
    ring
  have h1 : Continuous (fun x => (4*(j:ℝ)+6)*(e a b x*w x^(j+1))) := by
    unfold e w; fun_prop
  have h2 : Continuous (fun x => ((j:ℝ)+1)*(e a b x*w x^j)) := by
    unfold e w; fun_prop
  rw [hL,hR,hzero.1,hzero.2,mul_zero,mul_zero,sub_self,zero_sub,
    intervalIntegral.integral_sub (h1.intervalIntegrable 0 1)
      (h2.intervalIntegrable 0 1),
    intervalIntegral.integral_const_mul,intervalIntegral.integral_const_mul,
    intervalIntegral.integral_const_mul] at hp
  change (4*(j:ℝ)+6)*moment (j+1) a b-((j:ℝ)+1)*moment j a b =
    -(a*skew (j+1) a b) at hp
  linarith [mul_nonneg ha (skew_nonneg (j+1) a b ha)]

end WeilDefect.MasterRecon.V10B34b

#print axioms WeilDefect.MasterRecon.V10B34b.skew_nonneg
#print axioms WeilDefect.MasterRecon.V10B34b.moment_step
