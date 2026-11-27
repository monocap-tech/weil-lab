import WeilDefect.MasterRecon.V10B52a
import WeilDefect.MasterRecon.V10B47c
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

/-! V10B66a: direct endpoint-inclusive Fourier decay of the exact
recovered physical polynomial trials. No digamma-series supply, residual
bound, or vanishing at the support endpoints is required. -/
namespace WeilDefect.MasterRecon.V10B66a
open MeasureTheory Polynomial Set
open scoped BigOperators
open V10B45a (v)
open V10B52a (physicalRow physicalRow_eval)
open V10B47c (trial)

noncomputable def phase (a x : ℝ) : ℂ :=
  Complex.exp ((Complex.ofReal (a*x))*Complex.I)

theorem phase_norm (a x : ℝ) : ‖phase a x‖ = 1 := by
  exact Complex.norm_exp_ofReal_mul_I _

theorem phase_deriv (a x : ℝ) :
    HasDerivAt (phase a) (phase a x*((a:ℂ)*Complex.I)) x := by
  have hr : HasDerivAt (fun y : ℝ => a*y) a x := by
    simpa only [id_eq,mul_one] using (hasDerivAt_id x).const_mul a
  exact (hr.ofReal_comp.mul_const Complex.I).cexp

theorem fourier_parts (p p' : ℝ → ℂ) (hp : Continuous p)
    (hp' : Continuous p') (hd : ∀ x, HasDerivAt p (p' x) x) (a : ℝ) :
    ((a:ℂ)*Complex.I)*(∫ x in (-1/4:ℝ)..(1/4), p x*phase a x) =
      p (1/4)*phase a (1/4)-p (-1/4)*phase a (-1/4) -
        ∫ x in (-1/4:ℝ)..(1/4), p' x*phase a x := by
  have hc : Continuous (phase a) := by unfold phase; fun_prop
  have hv : Continuous (fun x => phase a x*((a:ℂ)*Complex.I)) :=
    hc.mul continuous_const
  have h := intervalIntegral.integral_mul_deriv_eq_deriv_mul
    (a := (-1/4:ℝ)) (b := (1/4:ℝ))
    (fun x _ => hd x) (fun x _ => phase_deriv a x)
    (hp'.intervalIntegrable _ _) (hv.intervalIntegrable _ _)
  have he : (fun x : ℝ => p x*(phase a x*((a:ℂ)*Complex.I))) =
      fun x => ((a:ℂ)*Complex.I)*(p x*phase a x) := by
    funext x
    ring
  rw [he,intervalIntegral.integral_const_mul] at h
  exact h

theorem fourier_decay (p p' : ℝ → ℂ) (hp : Continuous p)
    (hp' : Continuous p') (hd : ∀ x, HasDerivAt p (p' x) x) (a : ℝ) :
    |a| * ‖∫ x in (-1/4:ℝ)..(1/4), p x*phase a x‖ ≤
      ‖p (1/4)‖+‖p (-1/4)‖+∫ x in (-1/4:ℝ)..(1/4), ‖p' x‖ := by
  have h := congrArg norm (fourier_parts p p' hp hp' hd a)
  simp only [norm_mul,Complex.norm_real,Real.norm_eq_abs,Complex.norm_I,mul_one] at h
  rw [h]
  calc
    _ ≤ ‖p (1/4)*phase a (1/4)-p (-1/4)*phase a (-1/4)‖ +
        ‖∫ x in (-1/4:ℝ)..(1/4), p' x*phase a x‖ := norm_sub_le _ _
    _ ≤ _ := by
      apply add_le_add
      · simpa only [norm_mul,phase_norm,mul_one] using
          norm_sub_le (p (1/4)*phase a (1/4)) (p (-1/4)*phase a (-1/4))
      · simpa only [norm_mul,phase_norm,mul_one] using
          (intervalIntegral.norm_integral_le_integral_norm
            (f := fun x : ℝ => p' x*phase a x)
            (by norm_num : (-1/4:ℝ) ≤ 1/4))

noncomputable def trialPoly (col : Fin 16) : ℝ[X] :=
  ∑ j ∈ Finset.range 160, C (v col j:ℝ)*physicalRow j

theorem trialPoly_eval (col : Fin 16) (x : ℝ) :
    (trialPoly col).eval x = trial col (2*x+1/2) := by
  unfold trialPoly trial
  simp only [Polynomial.eval_finsetSum,Polynomial.eval_mul,Polynomial.eval_C,
    physicalRow_eval]

theorem trial_fourier_decay (col : Fin 16) (a : ℝ) :
    |a| * ‖∫ x in (-1/4:ℝ)..(1/4),
      (trial col (2*x+1/2):ℂ)*phase a x‖ ≤
      ‖(trialPoly col).eval (1/4)‖+‖(trialPoly col).eval (-1/4)‖+
        ∫ x in (-1/4:ℝ)..(1/4), ‖(trialPoly col).derivative.eval x‖ := by
  let p : ℝ → ℂ := fun x => Complex.ofReal ((trialPoly col).eval x)
  let p' : ℝ → ℂ := fun x => Complex.ofReal ((trialPoly col).derivative.eval x)
  have hp : Continuous p := Complex.continuous_ofReal.comp (trialPoly col).continuous
  have hp' : Continuous p' :=
    Complex.continuous_ofReal.comp (trialPoly col).derivative.continuous
  have hd : ∀ x, HasDerivAt p (p' x) x := fun x =>
    ((trialPoly col).hasDerivAt x).ofReal_comp
  have h := fourier_decay p p' hp hp' hd a
  simpa only [p,p',Complex.norm_real,trialPoly_eval] using h

end WeilDefect.MasterRecon.V10B66a

#print axioms WeilDefect.MasterRecon.V10B66a.phase_norm
#print axioms WeilDefect.MasterRecon.V10B66a.phase_deriv
#print axioms WeilDefect.MasterRecon.V10B66a.fourier_parts
#print axioms WeilDefect.MasterRecon.V10B66a.fourier_decay
#print axioms WeilDefect.MasterRecon.V10B66a.trialPoly_eval
#print axioms WeilDefect.MasterRecon.V10B66a.trial_fourier_decay
