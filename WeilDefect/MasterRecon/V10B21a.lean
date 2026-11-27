import WeilDefect.MasterRecon.V10B20b
import Mathlib.Data.Nat.Choose.Sum

/-! Right endpoint log moments by finite reflection. No differentiation
under the beta integral is needed. The binomial sum is an alternative
exact receiver for polynomial Gram generation. -/
namespace WeilDefect.MasterRecon.V10B21a

open MeasureTheory Set
open scoped BigOperators

theorem reflection_image :
    (fun x : ℝ => 1-x) '' Ioo 0 1 = Ioo 0 1 := by
  ext x
  constructor
  · rintro ⟨y,hy,rfl⟩
    exact ⟨by linarith [hy.2],by linarith [hy.1]⟩
  · intro hx
    exact ⟨1-x,⟨by linarith [hx.2],by linarith [hx.1]⟩,by ring⟩

theorem reflect_integral (f : ℝ → ℝ) :
    (∫ x in Ioo (0:ℝ) 1, f x) = ∫ x in Ioo (0:ℝ) 1, f (1-x) := by
  conv_lhs => rw [← reflection_image]
  have h := integral_image_eq_integral_abs_deriv_smul
    (f := fun x : ℝ => 1-x) (f' := fun _ => -1)
    (measurableSet_Ioo (a := (0:ℝ)) (b := 1))
    (fun x _ => ((hasDerivAt_const x (1:ℝ)).sub (hasDerivAt_id x)).hasDerivWithinAt)
    (fun x _ y _ h => by linarith) f
  simpa using h

theorem binomial_reflection (k : ℕ) (x : ℝ) :
    (1-x)^k = ∑ j ∈ Finset.range (k+1), ((-1:ℝ)^j*(k.choose j:ℝ))*x^j := by
  rw [show 1-x = -x+1 by ring,add_pow]
  apply Finset.sum_congr rfl
  intro j _
  rw [one_pow,mul_one,neg_pow]
  ring

theorem reflected_moment (k m : ℕ) :
    (∫ x in Ioo (0:ℝ) 1, x^k*(-Real.log (1-x))^m) =
      ∑ j ∈ Finset.range (k+1),
        ((-1:ℝ)^j*(k.choose j:ℝ))*((m.factorial:ℝ)/((j:ℝ)+1)^(m+1)) := by
  rw [reflect_integral (fun x : ℝ => x^k*(-Real.log (1-x))^m)]
  have he : (fun x : ℝ => (1-x)^k*(-Real.log (1-(1-x)))^m) =
      fun x => ∑ j ∈ Finset.range (k+1),
        ((-1:ℝ)^j*(k.choose j:ℝ))*(x^j*(-Real.log x)^m) := by
    funext x
    rw [show 1-(1-x)=x by ring,binomial_reflection,Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [he,integral_finset_sum]
  · apply Finset.sum_congr rfl
    intro j _
    rw [integral_const_mul,V10B20b.log_moment]
  · intro j _
    exact (V10B20b.log_moment_integrable j m).const_mul _

theorem reflected_moment_integrable (k m : ℕ) :
    IntegrableOn (fun x : ℝ => x^k*(-Real.log (1-x))^m) (Ioo 0 1) := by
  have h := integrableOn_image_iff_integrableOn_abs_deriv_smul
    (f := fun x : ℝ => 1-x) (f' := fun _ => -1)
    (measurableSet_Ioo (a := (0:ℝ)) (b := 1))
    (fun x _ => ((hasDerivAt_const x (1:ℝ)).sub (hasDerivAt_id x)).hasDerivWithinAt)
    (fun x _ y _ h => by linarith)
    (fun x : ℝ => x^k*(-Real.log (1-x))^m)
  rw [reflection_image] at h
  apply h.mpr
  simp only [abs_neg,abs_one,one_smul]
  have he : (fun x : ℝ => (1-x)^k*(-Real.log (1-(1-x)))^m) =
      fun x => ∑ j ∈ Finset.range (k+1),
        ((-1:ℝ)^j*(k.choose j:ℝ))*(x^j*(-Real.log x)^m) := by
    funext x
    rw [show 1-(1-x)=x by ring,binomial_reflection,Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [he]
  exact integrable_finset_sum _ (fun j _ => (V10B20b.log_moment_integrable j m).const_mul _)

end WeilDefect.MasterRecon.V10B21a

#print axioms WeilDefect.MasterRecon.V10B21a.reflection_image
#print axioms WeilDefect.MasterRecon.V10B21a.reflect_integral
#print axioms WeilDefect.MasterRecon.V10B21a.binomial_reflection
#print axioms WeilDefect.MasterRecon.V10B21a.reflected_moment
#print axioms WeilDefect.MasterRecon.V10B21a.reflected_moment_integrable
