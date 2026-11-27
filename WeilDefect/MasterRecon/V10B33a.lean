import Mathlib.RingTheory.Polynomial.ShiftedLegendre
import Mathlib.Analysis.Calculus.Deriv.Polynomial
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

/-! V10B33a: native shifted Legendre convention and repeated integration
by parts. Endpoint vanishing is explicit; no spherical-series identity
or completeness is assumed by the repeated integration receiver. -/
namespace WeilDefect.MasterRecon.V10B33a

open MeasureTheory Set Polynomial
open scoped BigOperators

noncomputable def legendre (j : ℕ) (z : ℝ) : ℝ :=
  (-1:ℝ)^j * aeval z (shiftedLegendre j)

theorem legendre_reflect (j : ℕ) (z : ℝ) :
    legendre j (1-z) = (-1:ℝ)^j * legendre j z := by
  unfold legendre
  rw [shiftedLegendre_eval_symm j (1-z),show 1-(1-z)=z by ring]
  ring

theorem rodrigues_eval (j : ℕ) (z : ℝ) :
    (j.factorial:ℝ)*legendre j z =
      (-1:ℝ)^j * aeval z ((Polynomial.derivative^[j])
        ((Polynomial.X:ℤ[X])^j*(1-Polynomial.X)^j)) := by
  have h := congrArg (fun p : ℤ[X] => (aeval z p : ℝ))
    (factorial_mul_shiftedLegendre_eq j)
  simp only [map_mul,map_natCast] at h
  unfold legendre
  rw [← h]
  ring

theorem repeated_parts (n : ℕ) (u v : ℕ → ℝ → ℝ)
    (hu : ∀ k, Continuous (u k)) (hv : ∀ k, Continuous (v k))
    (hdu : ∀ k x, HasDerivAt (u k) (u (k+1) x) x)
    (hdv : ∀ k x, HasDerivAt (v k) (v (k+1) x) x)
    (hzero : ∀ k<n, v k 0=0 ∧ v k 1=0) :
    (∫ x in (0:ℝ)..1, u 0 x*v n x) =
      (-1:ℝ)^n*(∫ x in (0:ℝ)..1, u n x*v 0 x) := by
  induction n generalizing u with
  | zero => simp
  | succ n ih =>
    have hz := hzero n (Nat.lt_succ_self n)
    have hp := intervalIntegral.integral_mul_deriv_eq_deriv_mul
      (a := (0:ℝ)) (b := 1)
      (fun x _ => hdu 0 x) (fun x _ => hdv n x)
      ((hu 1).intervalIntegrable volume 0 1)
      ((hv (n+1)).intervalIntegrable volume 0 1)
    have hrec := ih (fun k => u (k+1)) (fun k => hu (k+1))
      (fun k x => hdu (k+1) x) (fun k hk => hzero k (hk.trans (Nat.lt_succ_self n)))
    change (∫ x in (0:ℝ)..1, u 1 x*v n x) =
      (-1:ℝ)^n*(∫ x in (0:ℝ)..1, u (n+1) x*v 0 x) at hrec
    rw [hp,hz.1,hz.2,mul_zero,mul_zero,sub_self,zero_sub,hrec,pow_succ]
    ring

theorem exp_parts (n : ℕ) (a b : ℝ) (v : ℕ → ℝ → ℝ)
    (hv : ∀ k, Continuous (v k))
    (hdv : ∀ k x, HasDerivAt (v k) (v (k+1) x) x)
    (hzero : ∀ k<n, v k 0=0 ∧ v k 1=0) :
    (∫ x in (0:ℝ)..1, Real.exp (a*x+b)*v n x) =
      (-a)^n*(∫ x in (0:ℝ)..1, Real.exp (a*x+b)*v 0 x) := by
  let u : ℕ → ℝ → ℝ := fun k x => a^k*Real.exp (a*x+b)
  have hu : ∀ k, Continuous (u k) := by intro k; dsimp [u]; fun_prop
  have hdu : ∀ k x, HasDerivAt (u k) (u (k+1) x) x := by
    intro k x
    have h := (Real.hasDerivAt_exp (a*x+b)).comp x
      (((hasDerivAt_id x).const_mul a).add_const b)
    convert h.const_mul (a^k) using 1 <;> simp [u,pow_succ] <;> ring
  have h := repeated_parts n u v hu hv hdu hdv hzero
  dsimp only [u] at h
  simp only [pow_zero,one_mul] at h
  have he : (fun x => a^n*Real.exp (a*x+b)*v 0 x) =
      fun x => a^n*(Real.exp (a*x+b)*v 0 x) := by funext x; ring
  rw [he,intervalIntegral.integral_const_mul] at h
  rw [h,neg_pow]
  ring

end WeilDefect.MasterRecon.V10B33a

#print axioms WeilDefect.MasterRecon.V10B33a.legendre_reflect
#print axioms WeilDefect.MasterRecon.V10B33a.rodrigues_eval
#print axioms WeilDefect.MasterRecon.V10B33a.repeated_parts
#print axioms WeilDefect.MasterRecon.V10B33a.exp_parts
