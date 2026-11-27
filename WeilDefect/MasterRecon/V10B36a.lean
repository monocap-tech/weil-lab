import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.Calculus.Deriv.Pow

/-! V10B36a: universal centered beta identities obtained by polynomial
reflection and the fundamental theorem of calculus. No spherical series
or numerical integration is used. -/
namespace WeilDefect.MasterRecon.V10B36a
open MeasureTheory Set

noncomputable def y (x : ℝ) := 2*x-1
noncomputable def w (x : ℝ) := x*(1-x)
noncomputable def B (j m : ℕ) : ℝ :=
  ∫ x in (0:ℝ)..1, y x^(2*m)*w x^j

theorem odd_vanish (j m : ℕ) :
    (∫ x in (0:ℝ)..1, y x^(2*m+1)*w x^j) = 0 := by
  let f : ℝ → ℝ := fun x => y x^(2*m+1)*w x^j
  have hr : (∫ x in (0:ℝ)..1, f (1-x)) = ∫ x in (0:ℝ)..1, f x := by
    simpa using intervalIntegral.integral_comp_sub_left (a := (0:ℝ)) (b := 1) f 1
  have he : (fun x => f (1-x)) = fun x => -f x := by
    funext x
    have hy : y (1-x) = -y x := by unfold y; ring
    have hw : w (1-x) = w x := by unfold w; ring
    dsimp [f]
    rw [hy,hw,neg_pow,pow_succ,pow_mul]
    norm_num <;> ring
  rw [he,intervalIntegral.integral_neg] at hr
  change (∫ x in (0:ℝ)..1, f x) = 0
  linarith

theorem B_split (j m : ℕ) :
    4*B (j+1) m = B j m-B j (m+1) := by
  unfold B
  have h : (fun x : ℝ => 4*(y x^(2*m)*w x^(j+1))) =
    fun x => y x^(2*m)*w x^j-y x^(2*(m+1))*w x^j := by
    funext x
    rw [show 2*(m+1)=2*m+2 by omega,pow_add,pow_succ]
    have hw : 4*w x=1-y x^2 := by unfold w y; ring
    linear_combination (y x^(2*m)*w x^j)*hw
  rw [← intervalIntegral.integral_const_mul,h]
  apply intervalIntegral.integral_sub <;>
    apply Continuous.intervalIntegrable <;> unfold y w <;> fun_prop

theorem B_boundary (j m : ℕ) :
    (2*(2*(m:ℝ)+1))*B (j+1) m = ((j:ℝ)+1)*B j (m+1) := by
  let f : ℝ → ℝ := fun x => y x^(2*m+1)*w x^(j+1)
  let g : ℝ → ℝ := fun x =>
    (2*(2*(m:ℝ)+1))*(y x^(2*m)*w x^(j+1)) -
      ((j:ℝ)+1)*(y x^(2*(m+1))*w x^j)
  have hy (x : ℝ) : HasDerivAt y 2 x := by
    convert ((hasDerivAt_id x).const_mul 2).sub_const 1 using 1
    norm_num [y]
  have hw (x : ℝ) : HasDerivAt w (-y x) x := by
    have h := (hasDerivAt_id x).mul ((hasDerivAt_const x (1:ℝ)).sub (hasDerivAt_id x))
    convert h using 1 <;> simp [w,y] <;> ring
  have hd (x : ℝ) : HasDerivAt f (g x) x := by
    have h := ((hy x).pow (2*m+1)).mul ((hw x).pow (j+1))
    convert h using 1
    dsimp [g]
    simp only [Nat.add_sub_cancel, Nat.cast_add, Nat.cast_mul, Nat.cast_one]
    rw [show 2*(m+1)=2*m+2 by omega,pow_add]
    ring
  have hc : Continuous g := by dsimp [g,y,w]; fun_prop
  have h := intervalIntegral.integral_eq_sub_of_hasDerivAt
    (a := (0:ℝ)) (b := 1) (fun x _ => hd x) (hc.intervalIntegrable 0 1)
  have h0 : f 0=0 := by simp [f,w,pow_succ]
  have h1 : f 1=0 := by simp [f,w,pow_succ]
  have hc1 : Continuous (fun x : ℝ => (2*(2*(m:ℝ)+1))*(y x^(2*m)*w x^(j+1))) := by
    unfold y w; fun_prop
  have hc2 : Continuous (fun x : ℝ => ((j:ℝ)+1)*(y x^(2*(m+1))*w x^j)) := by
    unfold y w; fun_prop
  dsimp only [g] at h
  rw [h0,h1,sub_self,intervalIntegral.integral_sub
    (hc1.intervalIntegrable 0 1) (hc2.intervalIntegrable 0 1),
    intervalIntegral.integral_const_mul,intervalIntegral.integral_const_mul] at h
  change (2*(2*(m:ℝ)+1))*B (j+1) m-((j:ℝ)+1)*B j (m+1)=0 at h
  exact sub_eq_zero.mp h

theorem B_m_step (j m : ℕ) :
    (2*(j:ℝ)+2*(m:ℝ)+3)*B j (m+1) = (2*(m:ℝ)+1)*B j m := by
  have h := B_split j m
  have h' := B_boundary j m
  have h'' := congrArg (fun x : ℝ => (2*(m:ℝ)+1)*x) h
  dsimp at h''
  linear_combination h'' - 2*h'

theorem B_j_step (j : ℕ) :
    (4*(j:ℝ)+6)*B (j+1) 0 = ((j:ℝ)+1)*B j 0 := by
  have h := B_split j 0
  have h' := B_boundary j 0
  norm_num at h'
  have h'' := congrArg (fun x : ℝ => ((j:ℝ)+1)*x) h
  dsimp at h''
  linear_combination h'' + h'

theorem B_zero : B 0 0 = 1 := by simp [B]

end WeilDefect.MasterRecon.V10B36a

#print axioms WeilDefect.MasterRecon.V10B36a.odd_vanish
#print axioms WeilDefect.MasterRecon.V10B36a.B_split
#print axioms WeilDefect.MasterRecon.V10B36a.B_boundary
#print axioms WeilDefect.MasterRecon.V10B36a.B_m_step
#print axioms WeilDefect.MasterRecon.V10B36a.B_j_step
#print axioms WeilDefect.MasterRecon.V10B36a.B_zero
