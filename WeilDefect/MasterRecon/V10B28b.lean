import WeilDefect.MasterRecon.V10B28a

/-! V10B28b: discharge one-sided integrability on the pilot interval
from bounded Lipschitz trial data and the frozen kernel enclosure. -/
namespace WeilDefect.MasterRecon.V10B28b

open MeasureTheory Set
open V10B28a (reflect diffTerm regTerm)
open V10B24b (zeroExtend h)

theorem reflected_bounded (L B : ℝ) (p : ℝ → ℂ)
    (hb : ∀ y ∈ Icc 0 L, ‖p y‖ ≤ B) :
    ∀ y ∈ Icc 0 L, ‖reflect L p y‖ ≤ B := by
  intro y hy
  exact hb (L-y) ⟨by linarith [hy.2],by linarith [hy.1]⟩

theorem reflected_lipschitz (L K : ℝ) (p : ℝ → ℂ)
    (hl : ∀ y ∈ Icc 0 L, ∀ z ∈ Icc 0 L, ‖p y-p z‖ ≤ K*|y-z|) :
    ∀ y ∈ Icc 0 L, ∀ z ∈ Icc 0 L, ‖reflect L p y-reflect L p z‖ ≤ K*|y-z| := by
  intro y hy z hz
  have h := hl (L-y) ⟨by linarith [hy.2],by linarith [hy.1]⟩
    (L-z) ⟨by linarith [hz.2],by linarith [hz.1]⟩
  simpa only [reflect,show L-y-(L-z)= -(y-z) by ring,abs_neg] using h

theorem diff_bound (L x B K r : ℝ) (p : ℝ → ℂ) (hx : x ∈ Ioo 0 L)
    (hr : r ∈ Ioc 0 L) (hB : 0 ≤ B) (hK : 0 ≤ K)
    (hb : ∀ y ∈ Icc 0 L, ‖p y‖ ≤ B)
    (hl : ∀ y ∈ Icc 0 L, ∀ z ∈ Icc 0 L, ‖p y-p z‖ ≤ K*|y-z|) :
    ‖diffTerm L p x r‖ ≤ K/2+B/(2*x) := by
  have hx' : x ∈ Icc 0 L := ⟨hx.1.le,hx.2.le⟩
  unfold diffTerm
  rw [norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg (by positivity : 0 ≤ 1/(2*r))]
  by_cases hh : r ≤ x
  · rw [V10B27b.left_difference_inside L x r p hx ⟨hr.1,hh⟩]
    have h' := hl x hx' (x-r) ⟨by linarith,by linarith [hr.1,hx.2]⟩
    rw [show x-(x-r)=r by ring,abs_of_pos hr.1] at h'
    calc
      _ ≤ (1/(2*r))*(K*r) := mul_le_mul_of_nonneg_left h' (by positivity)
      _ = K/2 := by field_simp [hr.1.ne']
      _ ≤ _ := le_add_of_nonneg_right (by positivity)
  · rw [V10B27b.left_difference_outside L x r p hx ⟨lt_of_not_ge hh,hr.2⟩]
    have hd : 1/(2*r) ≤ 1/(2*x) := by
      apply one_div_le_one_div_of_le (by positivity)
      linarith
    calc
      _ ≤ (1/(2*x))*B := mul_le_mul hd (hb x hx') (norm_nonneg _) (by positivity)
      _ = B/(2*x) := by ring
      _ ≤ _ := le_add_of_nonneg_left (by positivity)

theorem diff_integrable (L x B K : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hx : x ∈ Ioo 0 L) (hB : 0 ≤ B) (hK : 0 ≤ K)
    (hb : ∀ y ∈ Icc 0 L, ‖p y‖ ≤ B)
    (hl : ∀ y ∈ Icc 0 L, ∀ z ∈ Icc 0 L, ‖p y-p z‖ ≤ K*|y-z|) :
    IntegrableOn (diffTerm L p x) (Ioc 0 L) := by
  have hz : Measurable (zeroExtend L p) := hp.indicator measurableSet_Icc
  have hm : Measurable (diffTerm L p x) := by unfold diffTerm; fun_prop
  have hi : IntegrableOn (fun _ : ℝ => K/2+B/(2*x)) (Ioc 0 L) :=
    integrableOn_const measure_Ioc_lt_top.ne
  apply hi.mono' hm.aestronglyMeasurable
  rw [ae_restrict_iff' measurableSet_Ioc]
  exact Eventually.of_forall fun r hr => diff_bound L x B K r p hx hr hB hK hb hl

theorem kernel_bound_two (r : ℝ) (hr : 0 < r) (hrL : r ≤ 1/2) : |h r| ≤ 2 := by
  have hq : |V10B27a.q r| ≤ 1 :=
    (V10B27a.eval_bound V10B27a.qCoeffs r (by rwa [abs_of_pos hr])).trans V10B27a.q_budget
  calc
    |h r| = |(h r-V10B27a.q r)+V10B27a.q r| := by congr 1; ring
    _ ≤ |h r-V10B27a.q r|+|V10B27a.q r| := abs_add_le _ _
    _ ≤ 1/(2:ℝ)^28+1 := add_le_add (V10B27a.frozen_kernel_bound r hr hrL) hq
    _ ≤ 2 := by norm_num

theorem reg_integrable (L x B : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hx : x ∈ Ioo 0 L) (hL : L ≤ 1/2) (hB : 0 ≤ B)
    (hb : ∀ y ∈ Icc 0 L, ‖p y‖ ≤ B) :
    IntegrableOn (regTerm L p x) (Ioc 0 L) := by
  have hz : Measurable (zeroExtend L p) := hp.indicator measurableSet_Icc
  have hh : Measurable h := by unfold h V10B24b.k V10B24b.den; fun_prop
  have hm : Measurable (regTerm L p x) := by unfold regTerm; fun_prop
  have hi : IntegrableOn (fun _ : ℝ => 2*B) (Ioc 0 L) :=
    integrableOn_const measure_Ioc_lt_top.ne
  apply hi.mono' hm.aestronglyMeasurable
  rw [ae_restrict_iff' measurableSet_Ioc]
  refine Eventually.of_forall fun r hr => ?_
  have hb' : ‖zeroExtend L p (x-r)‖ ≤ B := by
    by_cases h : x-r ∈ Icc 0 L
    · unfold zeroExtend
      rw [indicator_of_mem h]
      exact hb _ h
    · unfold zeroExtend
      rw [indicator_of_notMem h,norm_zero]
      exact hB
  unfold regTerm
  rw [norm_mul,Complex.norm_real,Real.norm_eq_abs]
  exact mul_le_mul (kernel_bound_two r hr.1 (hr.2.trans hL)) hb' (norm_nonneg _) (by norm_num)

theorem pilot_restricted_action (x B K : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hx : x ∈ Ioo 0 (1/2:ℝ)) (hB : 0 ≤ B) (hK : 0 ≤ K)
    (hb : ∀ y ∈ Icc 0 (1/2:ℝ), ‖p y‖ ≤ B)
    (hl : ∀ y ∈ Icc 0 (1/2:ℝ), ∀ z ∈ Icc 0 (1/2:ℝ), ‖p y-p z‖ ≤ K*|y-z|)
    (hc : (∫ r in Ioc (0:ℝ) (1/2:ℝ), V10B24b.b r-1/r)+
      (∫ r in Ioi (1/2:ℝ), V10B24b.b r) = -Real.log (2*(1/2:ℝ))) :
    (∫ r in Ioi (0:ℝ), V10B24b.physicalTerm (1/2) p x r) = V10B28a.model (1/2) p x := by
  have hxr := V10B28a.reflect_inside (1/2) x hx
  have hpr : Measurable (reflect (1/2) p) := hp.comp (by fun_prop : Measurable (fun y : ℝ => 1/2-y))
  have hbr := reflected_bounded (1/2) B p hb
  have hlr := reflected_lipschitz (1/2) K p hl
  exact V10B28a.restricted_action (1/2) x p hx
    (diff_integrable _ _ B K p hp hx hB hK hb hl)
    (diff_integrable _ _ B K _ hpr hxr hB hK hbr hlr)
    (reg_integrable _ _ B p hp hx le_rfl hB hb)
    (reg_integrable _ _ B _ hpr hxr le_rfl hB hbr) hc

end WeilDefect.MasterRecon.V10B28b

#print axioms WeilDefect.MasterRecon.V10B28b.reflected_bounded
#print axioms WeilDefect.MasterRecon.V10B28b.reflected_lipschitz
#print axioms WeilDefect.MasterRecon.V10B28b.diff_bound
#print axioms WeilDefect.MasterRecon.V10B28b.diff_integrable
#print axioms WeilDefect.MasterRecon.V10B28b.kernel_bound_two
#print axioms WeilDefect.MasterRecon.V10B28b.reg_integrable
#print axioms WeilDefect.MasterRecon.V10B28b.pilot_restricted_action
