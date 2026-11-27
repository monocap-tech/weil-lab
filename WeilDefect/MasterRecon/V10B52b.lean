import WeilDefect.MasterRecon.V10B52a
import WeilDefect.MasterRecon.V10B50a

/-! V10B52b: realize the polynomial functional on the actual log
carrier, using the original restricted L1 input and moment integrability. -/
namespace WeilDefect.MasterRecon.V10B52b
open MeasureTheory Polynomial
open scoped BigOperators
open WeilDefect.MasterRecon.V08I (logCarrier physicalInclusion)
open WeilDefect.MasterRecon.V08K (supportMeasure restrictPhysical)
open WeilDefect.MasterRecon.V10B50a
open WeilDefect.MasterRecon.V10B52a

theorem monomial_integrable (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t) (j : ℕ) :
    Integrable (fun x : ℝ => (x:ℂ)^j*physicalInclusion t g x) (supportMeasure t) := by
  have h := V08E.moment_integrable (supportMeasure t) t
    (V08K.supportMeasure_bound t) j (V10B13a.input t g)
  apply h.congr
  have h₁ := V08F.physicalL1Inclusion_ae (supportMeasure t)
    (restrictPhysical t (physicalInclusion t g))
  have h₂ := V08K.restrictPhysical_ae t (physicalInclusion t g)
  filter_upwards [h₁,h₂] with x hx hy
  change (x:ℂ)^j*(V08F.physicalL1Inclusion (supportMeasure t)
    (restrictPhysical t (physicalInclusion t g))) x = _
  rw [hx,hy]

theorem polynomial_integrable (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t)
    (p : ℝ[X]) :
    Integrable (fun x : ℝ => (Complex.ofReal (p.eval x))*physicalInclusion t g x)
      (supportMeasure t) := by
  induction p using Polynomial.induction_on' with
  | add p q hp hq =>
    simpa only [Polynomial.eval_add,Complex.ofReal_add,add_mul] using hp.add hq
  | monomial n a =>
    have h := (monomial_integrable t ht g n).const_mul (a:ℂ)
    simpa only [Polynomial.eval_monomial,Complex.ofReal_mul,Complex.ofReal_pow,mul_assoc] using h

noncomputable def pairing (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t) :
    ℝ[X] →ₗ[ℝ] ℂ where
  toFun p := ∫ x, (Complex.ofReal (p.eval x))*physicalInclusion t g x ∂supportMeasure t
  map_add' p q := by
    simp only [Polynomial.eval_add,Complex.ofReal_add,add_mul]
    exact integral_add (polynomial_integrable t ht g p)
      (polynomial_integrable t ht g q)
  map_smul' a p := by
    change (∫ x, (Complex.ofReal ((a • p).eval x))*physicalInclusion t g x ∂supportMeasure t) =
      a • (∫ x, (Complex.ofReal (p.eval x))*physicalInclusion t g x ∂supportMeasure t)
    rw [Algebra.smul_def,Polynomial.algebraMap_apply,Algebra.algebraMap_self_apply]
    simp only [Polynomial.eval_mul,Polynomial.eval_C,Complex.ofReal_mul,mul_assoc]
    rw [← integral_smul]
    apply integral_congr_ae
    filter_upwards with x
    rw [Complex.real_smul]

theorem pairing_monomial (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t) (j : ℕ) :
    pairing t ht g ((X:ℝ[X])^j) = V10B13a.moment t ht j g := by
  rw [moment_literal]
  change (∫ x, (Complex.ofReal (((X:ℝ[X])^j).eval x))*physicalInclusion t g x
    ∂supportMeasure t) = _
  simp only [Polynomial.eval_pow,Polynomial.eval_X,Complex.ofReal_pow]

theorem pairing_legendre (g : logCarrier (1/4)) (j : ℕ) :
    pairing (1/4) (by norm_num) g (physicalRow j) =
      ∫ x, (V10B33a.legendre j (2*x+1/2):ℂ)*physicalInclusion (1/4) g x
        ∂supportMeasure (1/4) := by
  change (∫ x, (Complex.ofReal ((physicalRow j).eval x))*physicalInclusion (1/4) g x
    ∂supportMeasure (1/4)) = _
  simp only [physicalRow_eval]

theorem original_moment_kernel (g : logCarrier (1/4)) :
    (∀ j<15, V10B13a.moment (1/4) (by norm_num) j g=0) ↔
      (∀ j<15, (∫ x, (V10B33a.legendre j (2*x+1/2):ℂ)*
        physicalInclusion (1/4) g x ∂supportMeasure (1/4))=0) := by
  have h := physical_moment_kernel (pairing (1/4) (by norm_num) g) 15
  simpa only [pairing_monomial,pairing_legendre] using h

end WeilDefect.MasterRecon.V10B52b

#print axioms WeilDefect.MasterRecon.V10B52b.monomial_integrable
#print axioms WeilDefect.MasterRecon.V10B52b.polynomial_integrable
#print axioms WeilDefect.MasterRecon.V10B52b.pairing_monomial
#print axioms WeilDefect.MasterRecon.V10B52b.pairing_legendre
#print axioms WeilDefect.MasterRecon.V10B52b.original_moment_kernel
