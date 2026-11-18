import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts

namespace WeilDefect
noncomputable section
open MeasureTheory intervalIntegral

/-! NF606: an exact analytic primitive for the original unweighted
physical Gram entries. All original products use nonnegative
polynomial degrees; no sine integral or negative-power singular
branch is needed for this H,V. Complex λ includes oscillators,
the real sinh pole, and all products of them. -/

def neutralNF606ExpMoment (a b : ℝ) (z : ℂ) (n : ℕ) : ℂ :=
  ∫ x in a..b, (x:ℂ)^n * Complex.exp (z*(x:ℂ))

theorem neutralNF606Exp_hasDerivAt (z : ℂ) (x : ℝ) :
    HasDerivAt (fun t : ℝ => Complex.exp (z*(t:ℂ)))
      (z*Complex.exp (z*(x:ℂ))) x := by
  have hi := ((hasDerivAt_id x).ofReal_comp).const_mul z
  have h := (Complex.hasDerivAt_exp (z*(x:ℂ))).scomp x hi
  simpa only [id_eq,Complex.ofReal_one,mul_one,Function.comp_apply,smul_eq_mul] using h

theorem neutralNF606ExpMoment_zero_degree (a b : ℝ) (z : ℂ) :
    z*neutralNF606ExpMoment a b z 0 =
      Complex.exp (z*(b:ℂ))-Complex.exp (z*(a:ℂ)) := by
  have h := intervalIntegral.integral_eq_sub_of_hasDerivAt
    (a := a) (b := b)
    (fun x _ => neutralNF606Exp_hasDerivAt z x)
    (show IntervalIntegrable (fun x : ℝ => z*Complex.exp (z*(x:ℂ))) volume a b
      from (show Continuous (fun x : ℝ => z*Complex.exp (z*(x:ℂ))) by fun_prop).intervalIntegrable _ _)
  rw [intervalIntegral.integral_const_mul] at h
  simpa [neutralNF606ExpMoment] using h

theorem neutralNF606ExpMoment_succ (a b : ℝ) (z : ℂ) (n : ℕ) :
    z*neutralNF606ExpMoment a b z (n+1) =
      (b:ℂ)^(n+1)*Complex.exp (z*(b:ℂ)) -
      (a:ℂ)^(n+1)*Complex.exp (z*(a:ℂ)) -
      (n+1:ℂ)*neutralNF606ExpMoment a b z n := by
  let u := fun x : ℝ => (x:ℂ)^(n+1)
  let u' := fun x : ℝ => (n+1:ℂ)*(x:ℂ)^n
  let v := fun x : ℝ => Complex.exp (z*(x:ℂ))
  let v' := fun x : ℝ => z*v x
  have hu (x : ℝ) : HasDerivAt u (u' x) x := by
    dsimp [u,u']
    have h := ((hasDerivAt_id x).pow (n+1)).ofReal_comp
    simpa [Nat.cast_succ] using h
  have hv (x : ℝ) : HasDerivAt v (v' x) x := neutralNF606Exp_hasDerivAt z x
  have hui : IntervalIntegrable u' volume a b :=
    (show Continuous u' by dsimp [u']; fun_prop).intervalIntegrable _ _
  have hvi : IntervalIntegrable v' volume a b :=
    (show Continuous v' by dsimp [v',v]; fun_prop).intervalIntegrable _ _
  have h := intervalIntegral.integral_mul_deriv_eq_deriv_mul
    (fun x _ => hu x) (fun x _ => hv x) hui hvi
  change (∫ x in a..b, (x:ℂ)^(n+1)*(z*Complex.exp (z*(x:ℂ)))) =
    (b:ℂ)^(n+1)*Complex.exp (z*(b:ℂ))-
    (a:ℂ)^(n+1)*Complex.exp (z*(a:ℂ))-
    ∫ x in a..b, ((n+1:ℂ)*(x:ℂ)^n)*Complex.exp (z*(x:ℂ)) at h
  simp_rw [show ∀ x : ℝ, (x:ℂ)^(n+1)*(z*Complex.exp (z*(x:ℂ))) =
    z*((x:ℂ)^(n+1)*Complex.exp (z*(x:ℂ))) by intro x; ring,
    mul_assoc,intervalIntegral.integral_const_mul] at h
  exact h

/-- At λ=0 there is no division by a small frequency. -/
theorem neutralNF606ExpMoment_zero_frequency (a b : ℝ) (n : ℕ) :
    neutralNF606ExpMoment a b 0 n =
      ((b:ℂ)^(n+1)-(a:ℂ)^(n+1))/(n+1:ℂ) := by
  have hd (x : ℝ) : HasDerivAt
      (fun t : ℝ => (t:ℂ)^(n+1)/(n+1:ℂ)) ((x:ℂ)^n) x := by
    have hp : HasDerivAt (fun t : ℝ => (t:ℂ)^(n+1)) ((n+1:ℂ)*(x:ℂ)^n) x := by
      simpa [Nat.cast_succ] using (((hasDerivAt_id x).pow (n+1)).ofReal_comp)
    have h := hp.div_const (n+1:ℂ)
    convert h using 1
    simp only [Nat.cast_succ,Nat.add_sub_cancel,mul_one]
    have hn : (n+1:ℂ) ≠ 0 := by exact_mod_cast (Nat.succ_ne_zero n)
    field_simp
  have h := intervalIntegral.integral_eq_sub_of_hasDerivAt
    (a := a) (b := b) (fun x _ => hd x)
    (show IntervalIntegrable (fun x : ℝ => (x:ℂ)^n) volume a b
      from (show Continuous (fun x : ℝ => (x:ℂ)^n) by fun_prop).intervalIntegrable _ _)
  unfold neutralNF606ExpMoment
  simp only [zero_mul,Complex.exp_zero,mul_one]
  rw [h]
  ring

/-- Products of exponential-polynomial modes reduce to the same
single primitive; any zero combined frequency uses the above
separate polynomial integral. -/
theorem neutralNF606ExpMoment_product (a b : ℝ) (z w : ℂ) (m n : ℕ) :
    (∫ x in a..b, ((x:ℂ)^m*Complex.exp (z*(x:ℂ)))*
      ((x:ℂ)^n*Complex.exp (w*(x:ℂ)))) =
    neutralNF606ExpMoment a b (z+w) (m+n) := by
  unfold neutralNF606ExpMoment
  apply intervalIntegral.integral_congr
  intro x _
  dsimp only
  rw [pow_add,add_mul,Complex.exp_add]
  ring

end
end WeilDefect
