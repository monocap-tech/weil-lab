import WeilDefect.MasterRecon.V10B25a
import Mathlib.MeasureTheory.Integral.IntegralEqImproper
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

/-! V10B26b: actual scalar integrability and identification of the
finite-cutoff limit with the restricted Lebesgue integrals. -/
namespace WeilDefect.MasterRecon.V10B26b

open MeasureTheory Set Filter
open scoped Topology
open V10B24b (den b)

theorem den_upper (r : ℝ) : den r ≤ 2*r := by
  unfold den
  linarith [Real.add_one_le_exp (-2*r)]

theorem den_lower (r : ℝ) (hr : 0 < r) :
    2*r ≤ (1+2*r)*den r := by
  have h := mul_le_mul_of_nonneg_right (Real.add_one_le_exp (2*r))
    (Real.exp_pos (-2*r)).le
  rw [← Real.exp_add,show 2*r+(-2*r)=0 by ring,Real.exp_zero] at h
  unfold den
  nlinarith only [h]

theorem b_rewrite (r : ℝ) (hr : 0 < r) : b r = 2/den r-2 := by
  have hd := (V10B24b.den_pos r hr).ne'
  unfold b
  field_simp [hd]
  unfold den
  ring

theorem near_bound (r : ℝ) (hr : 0 < r) : |b r-1/r| ≤ 2 := by
  have hd := V10B24b.den_pos r hr
  have h1 : 1/r ≤ 2/den r := by
    apply (div_le_div_iff₀ hr hd).mpr
    simpa only [one_mul] using den_upper r
  have h2 : 2/den r ≤ 1/r+2 := by
    rw [show 1/r+2=(1+2*r)/r by field_simp [hr.ne']]
    exact (div_le_div_iff₀ hd hr).mpr (den_lower r hr)
  rw [b_rewrite r hr]
  exact abs_le.mpr ⟨by linarith,by linarith⟩

theorem near_integrable (L : ℝ) :
    IntegrableOn (fun r : ℝ => b r-1/r) (Ioc 0 L) := by
  have hi : IntegrableOn (fun _ : ℝ => (2:ℝ)) (Ioc 0 L) :=
    integrableOn_const (measure_Ioc_lt_top.ne)
  have hm : Measurable (fun r : ℝ => b r-1/r) := by unfold b den; fun_prop
  apply hi.mono' hm.aestronglyMeasurable
  rw [ae_restrict_iff' measurableSet_Ioc]
  exact Eventually.of_forall fun r hr => by
    simpa [Real.norm_eq_abs] using near_bound r hr.1

theorem far_bound (L r : ℝ) (hL : 0 < L) (hr : L ≤ r) :
    |b r| ≤ (2/den L)*Real.exp (-2*r) := by
  have hden : den L ≤ den r := by
    unfold den
    have h := Real.exp_le_exp.mpr (show -2*r ≤ -2*L by linarith)
    linarith
  have hdp := V10B24b.den_pos L hL
  have hdr := V10B24b.den_pos r (hL.trans_le hr)
  unfold b
  rw [abs_of_nonneg (by positivity)]
  calc
    _ ≤ (2*Real.exp (-2*r))/den L :=
      div_le_div_of_nonneg_left (by positivity) hdp hden
    _ = _ := by ring

theorem far_integrable (L : ℝ) (hL : 0 < L) :
    IntegrableOn b (Ioi L) := by
  have h := (integrableOn_exp_mul_Ioi (a := (-2:ℝ)) (by norm_num) L).const_mul (2/den L)
  have hm : Measurable b := by unfold b den; fun_prop
  apply h.mono' hm.aestronglyMeasurable
  rw [ae_restrict_iff' measurableSet_Ioi]
  exact Eventually.of_forall fun r hr => by
    simpa [Real.norm_eq_abs] using far_bound L r hL hr.le

theorem near_cutoff {α : Type*} {l : Filter α} [l.IsCountablyGenerated]
    (L : ℝ) (a : α → ℝ) (ha : Tendsto a l (𝓝 0))
    (hcut : ∀ᶠ i in l, 0 ≤ a i ∧ a i ≤ L) :
    Tendsto (fun i => ∫ r in a i..L, b r-1/r) l
      (𝓝 (∫ r in Ioc (0:ℝ) L, b r-1/r)) := by
  let μ := (volume : Measure ℝ).restrict (Ioc 0 L)
  have hφ : AECover μ l (fun i => Ioi (a i)) := by
    constructor
    · rw [ae_restrict_iff' measurableSet_Ioc]
      exact Eventually.of_forall fun r hr => ha.eventually (eventually_lt_nhds hr.1)
    · intro i
      exact measurableSet_Ioi
  refine (hφ.integral_tendsto_of_countably_generated (near_integrable L)).congr' ?_
  filter_upwards [hcut] with i hi
  rw [intervalIntegral.integral_of_le hi.2,Measure.restrict_restrict measurableSet_Ioi]
  have he : Ioi (a i) ∩ Ioc (0:ℝ) L = Ioc (a i) L := by
    ext r
    simp only [mem_inter_iff,mem_Ioi,mem_Ioc]
    constructor
    · exact fun h => ⟨h.1,h.2.2⟩
    · exact fun h => ⟨h.1,hi.1.trans_lt h.1,h.2⟩
  rw [he]

theorem scalar_constant {α : Type*} {l : Filter α} [l.NeBot] [l.IsCountablyGenerated]
    (L : ℝ) (hL : 0 < L) (a T : α → ℝ)
    (ha : Tendsto a l (𝓝[≠] 0)) (hT : Tendsto T l atTop)
    (hcut : ∀ᶠ i in l, 0 < a i ∧ a i ≤ L ∧ L ≤ T i) :
    (∫ r in Ioc (0:ℝ) L, b r-1/r)+(∫ r in Ioi L, b r) = -Real.log (2*L) := by
  have hnear := near_cutoff L a (ha.mono_right nhdsWithin_le_nhds)
    (hcut.mono fun _ h => ⟨h.1.le,h.2.1⟩)
  have hfar := intervalIntegral_tendsto_integral_Ioi L (far_integrable L hL) hT
  exact tendsto_nhds_unique (hnear.add hfar)
    (V10B25a.cutoff_limit L hL a T ha hT hcut)

end WeilDefect.MasterRecon.V10B26b

#print axioms WeilDefect.MasterRecon.V10B26b.den_upper
#print axioms WeilDefect.MasterRecon.V10B26b.den_lower
#print axioms WeilDefect.MasterRecon.V10B26b.b_rewrite
#print axioms WeilDefect.MasterRecon.V10B26b.near_bound
#print axioms WeilDefect.MasterRecon.V10B26b.near_integrable
#print axioms WeilDefect.MasterRecon.V10B26b.far_bound
#print axioms WeilDefect.MasterRecon.V10B26b.far_integrable
#print axioms WeilDefect.MasterRecon.V10B26b.near_cutoff
#print axioms WeilDefect.MasterRecon.V10B26b.scalar_constant
