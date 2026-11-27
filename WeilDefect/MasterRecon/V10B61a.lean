import WeilDefect.MasterRecon.V10B52b
import WeilDefect.MasterRecon.V10B47c

/-! Literal pole-row attachment at t=1/4. Uses the existing normalized
load, not a new trial bank. The original retained-bank definition is
attached separately, without presuming its conditional tail estimate. -/
namespace WeilDefect.MasterRecon.V10B61a
open MeasureTheory Polynomial
open scoped BigOperators
open V08I (logCarrier physicalInclusion)
open V08K (supportMeasure restrictPhysical)
open V10B33a (legendre)
open V10B46a (f I I_pos)
open V10B52a (physicalRow physicalRow_eval)
open V10B52b (pairing pairing_legendre polynomial_integrable)
open V10B39b (project)
open V10B40a (oddPart deflate)
open V10B47c (load)

noncomputable def coeff (j : ℕ) : ℝ :=
  (2*(j:ℝ)+1)*(∫ z in (0:ℝ)..1, oddPart f z*legendre j z)

noncomputable def projectionPoly : ℝ[X] :=
  ∑ j ∈ Finset.range 14, C (coeff j)*physicalRow j

theorem projection_eval (x : ℝ) :
    projectionPoly.eval x = project legendre (fun j => 2*(j:ℝ)+1) 14
      (oddPart f) (2*x+1/2) := by
  unfold projectionPoly project coeff
  simp only [Polynomial.eval_finsetSum,Polynomial.eval_mul,Polynomial.eval_C,
    physicalRow_eval]

theorem projection_pair_zero (g : logCarrier (1/4))
    (h : ∀ j<15, V10B13a.moment (1/4) (by norm_num) j g=0) :
    pairing (1/4) (by norm_num) g projectionPoly = 0 := by
  have hl := (V10B52b.original_moment_kernel g).mp h
  unfold projectionPoly
  rw [map_sum]
  apply Finset.sum_eq_zero
  intro j hj
  have he : C (coeff j)*physicalRow j = coeff j • physicalRow j := by
    rw [Algebra.smul_def,Polynomial.algebraMap_apply,Algebra.algebraMap_self_apply]
  rw [he,map_smul,pairing_legendre,hl j (by have := Finset.mem_range.mp hj; omega),smul_zero]

theorem pointwise_load (x : ℝ) :
    (62*I 15)*load (2*x+1/2) =
      Real.exp ((1/2:ℝ)*x)-Real.exp ((-1/2:ℝ)*x)-2*projectionPoly.eval x := by
  rw [projection_eval]
  unfold load deflate oddPart f
  rw [show (1/4:ℝ)*(2*x+1/2)+(-1:ℝ)/8=(1/2:ℝ)*x by ring,
    show (1/4:ℝ)*(1-(2*x+1/2))+(-1:ℝ)/8=(-1/2:ℝ)*x by ring]
  field_simp [(I_pos 15).ne'] <;> ring

theorem exp_integrable (g : logCarrier (1/4)) (a : ℝ) :
    Integrable (fun x : ℝ => (Real.exp (a*x):ℂ)*physicalInclusion (1/4) g x)
      (supportMeasure (1/4)) := by
  let r := restrictPhysical (1/4) (physicalInclusion (1/4) g)
  have h : Integrable (fun x : ℝ => r x) (supportMeasure (1/4)) :=
    memLp_one_iff_integrable.mp (V08F.physicalL1_mem _ r)
  have hc : Continuous (fun x : ℝ => (Real.exp (a*x):ℂ)) := by fun_prop
  have hp := h.bdd_mul hc.aestronglyMeasurable (c := Real.exp (|a|*(1/4)))
    (by
      filter_upwards [V08K.supportMeasure_bound (1/4)] with x hx
      rw [Complex.norm_real,Real.norm_eq_abs,abs_of_pos (Real.exp_pos _)]
      apply Real.exp_le_exp.mpr
      calc
        a*x ≤ |a*x| := le_abs_self _
        _ = |a|*|x| := abs_mul _ _
        _ ≤ _ := mul_le_mul_of_nonneg_left hx (abs_nonneg _))
  apply hp.congr
  filter_upwards [V08K.restrictPhysical_ae (1/4) (physicalInclusion (1/4) g)] with x hx
  change (Real.exp (a*x):ℂ)*r x = _
  rw [show r x = physicalInclusion (1/4) g x from hx]

theorem literal_pole_identity (g : logCarrier (1/4))
    (h : ∀ j<15, V10B13a.moment (1/4) (by norm_num) j g=0) :
    (V10B8c.eval (1/4) (1/2) (by norm_num) -
      V10B8c.eval (1/4) (-1/2) (by norm_num)) g =
      (Complex.ofReal (62*I 15)) *
        (∫ x, (Complex.ofReal (load (2*x+1/2)))*physicalInclusion (1/4) g x
          ∂supportMeasure (1/4)) := by
  let μ := supportMeasure (1/4)
  let u : ℝ → ℂ := fun x => (Real.exp ((1/2:ℝ)*x):ℂ)*physicalInclusion (1/4) g x
  let v : ℝ → ℂ := fun x => (Real.exp ((-1/2:ℝ)*x):ℂ)*physicalInclusion (1/4) g x
  let p : ℝ → ℂ := fun x => (Complex.ofReal (projectionPoly.eval x))*physicalInclusion (1/4) g x
  have hu : Integrable u μ := exp_integrable g (1/2)
  have hv : Integrable v μ := exp_integrable g (-1/2)
  have hp : Integrable p μ := polynomial_integrable (1/4) (by norm_num) g projectionPoly
  have hz : (∫ x, p x ∂μ) = 0 := projection_pair_zero g h
  rw [V10B50a.pole_literal]
  change (∫ x, u x ∂μ) - (∫ x, v x ∂μ) = _
  rw [← integral_const_mul]
  calc
    _ = (∫ x, u x - v x ∂μ) - (2:ℂ)*(∫ x, p x ∂μ) := by
      rw [integral_sub hu hv,hz,mul_zero,sub_zero]
    _ = ∫ x, (u x-v x)-(2:ℂ)*p x ∂μ := by
      rw [← integral_const_mul]
      exact (integral_sub (hu.sub hv) (hp.const_mul (2:ℂ))).symm
    _ = _ := by
      apply integral_congr_ae
      filter_upwards with x
      have he := congrArg Complex.ofReal (pointwise_load x)
      push_cast at he
      dsimp [u,v,p]
      rw [← mul_assoc,he]
      ring

theorem literal_pole_zero_iff (g : logCarrier (1/4))
    (h : ∀ j<15, V10B13a.moment (1/4) (by norm_num) j g=0) :
    (V10B8c.eval (1/4) (1/2) (by norm_num) -
      V10B8c.eval (1/4) (-1/2) (by norm_num)) g = 0 ↔
      (∫ x, (Complex.ofReal (load (2*x+1/2)))*physicalInclusion (1/4) g x
        ∂supportMeasure (1/4)) = 0 := by
  rw [literal_pole_identity g h]
  have hn : Complex.ofReal (62*I 15) ≠ 0 := by
    exact_mod_cast (mul_ne_zero (by norm_num : (62:ℝ) ≠ 0) (I_pos 15).ne')
  exact mul_eq_zero_iff_left hn

end WeilDefect.MasterRecon.V10B61a

#print axioms WeilDefect.MasterRecon.V10B61a.projection_eval
#print axioms WeilDefect.MasterRecon.V10B61a.projection_pair_zero
#print axioms WeilDefect.MasterRecon.V10B61a.pointwise_load
#print axioms WeilDefect.MasterRecon.V10B61a.exp_integrable
#print axioms WeilDefect.MasterRecon.V10B61a.literal_pole_identity
#print axioms WeilDefect.MasterRecon.V10B61a.literal_pole_zero_iff
