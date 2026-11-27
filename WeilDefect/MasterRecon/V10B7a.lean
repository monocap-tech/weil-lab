import WeilDefect.MasterRecon.V09D
import WeilDefect.MasterRecon.V10B6g
import Mathlib.Analysis.Complex.JensenFormula

/-! V10B7a: a native multiplicity-sensitive local-count receiver.
The radius choice follows the standard right-half-strip Jensen argument
(see Zeta23/RvM/LocalCount.lean, inspected mirror revision 77f832c).
We use Mathlib 4.34's Jensen inequality directly, not the upstream
4.33-rc2 dependency or its rescaled zero-count theorem. -/
namespace WeilDefect.MasterRecon.V10B7a

open Set Metric MeromorphicOn
open scoped BigOperators

theorem window_finite (a b : ℝ) : (V09D.stripWindow a b).Finite := by
  apply (isCompact_closedBall (0:ℂ) (1+|a|+|b|)).inter_riemannZetaZeros_finite.subset
  intro z hz
  rcases hz with ⟨⟨hzero,hr0,hr1⟩,ha,hb⟩
  refine ⟨?_,hzero⟩
  rw [mem_closedBall,dist_zero_right]
  apply (Complex.norm_le_abs_re_add_abs_im z).trans
  rw [abs_of_pos hr0]
  have hi : |z.im| ≤ |a|+|b| := by
    apply abs_le.mpr
    constructor <;> linarith [neg_abs_le a,le_abs_self b,abs_nonneg a,abs_nonneg b]
  linarith

noncomputable def window (a b : ℝ) : Finset ℂ :=
  (window_finite a b).toFinset

theorem mem_window (a b : ℝ) (z : ℂ) :
    z ∈ window a b ↔ z ∈ V09D.stripWindow a b :=
  Set.Finite.mem_toFinset _

theorem count_window (a b : ℝ) :
    V09D.count a b = ∑ z ∈ window a b, V09D.mult z := by
  unfold V09D.count window
  exact finsum_mem_eq_finite_toFinset_sum V09D.mult (window_finite a b)

theorem count_mono_window {a b c d : ℝ} (ha : c ≤ a) (hb : b ≤ d) :
    V09D.count a b ≤ V09D.count c d := by
  rw [count_window,count_window]
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro z hz
    have h := (mem_window a b z).mp hz
    exact (mem_window c d z).mpr ⟨h.1,ha.trans_lt h.2.1,h.2.2.trans hb⟩
  · intros
    positivity

noncomputable def rightWindow (a b : ℝ) : Finset ℂ := by
  classical
  exact (window a b).filter (fun z => (1:ℝ)/2 ≤ z.re)

theorem mem_rightWindow (a b : ℝ) (z : ℂ) :
    z ∈ rightWindow a b ↔ z ∈ V09D.stripWindow a b ∧ (1:ℝ)/2 ≤ z.re := by
  classical
  simp [rightWindow,mem_window]

noncomputable def rightCount (a b : ℝ) : ℕ :=
  ∑ z ∈ rightWindow a b, V09D.mult z

theorem count_le_twice_right (a b : ℝ)
    (hr : ∀ z, V09D.stripZero z → V09D.stripZero (V10A.reflect z))
    (hm : ∀ z, V09D.stripZero z → V09D.mult (V10A.reflect z) = V09D.mult z) :
    V09D.count a b ≤ 2 * rightCount a b := by
  classical
  let S := window a b
  let R := rightWindow a b
  let L := S.filter (fun z => ¬ (1:ℝ)/2 ≤ z.re)
  let e : ℂ ↪ ℂ := ⟨V10A.reflect,fun x y h => by
    have h' := congrArg V10A.reflect h
    simpa only [V10A.reflect_involution] using h'⟩
  have hsub : L.map e ⊆ R := by
    intro z hz
    obtain ⟨w,hw,rfl⟩ := Finset.mem_map.mp hz
    have hwS := (mem_window a b w).mp (Finset.mem_filter.mp hw).1
    have hwL := (Finset.mem_filter.mp hw).2
    apply (mem_rightWindow a b _).mpr
    change V10A.reflect w ∈ V09D.stripWindow a b ∧ (1:ℝ)/2 ≤ (V10A.reflect w).re
    refine ⟨⟨hr w hwS.1,?_,?_⟩,?_⟩
    · simpa only [V10A.reflect_im] using hwS.2.1
    · simpa only [V10A.reflect_im] using hwS.2.2
    · rw [V10A.reflect_re]
      linarith [lt_of_not_ge hwL]
  have hL : (∑ z ∈ L, V09D.mult z) ≤ ∑ z ∈ R, V09D.mult z := by
    calc
      _ = ∑ z ∈ L.map e, V09D.mult z := by
        rw [Finset.sum_map]
        apply Finset.sum_congr rfl
        intro z hz
        exact (hm z ((mem_window a b z).mp (Finset.mem_filter.mp hz).1).1).symm
      _ ≤ _ := Finset.sum_le_sum_of_subset_of_nonneg hsub (fun _ _ _ => Nat.zero_le _)
  have he : (∑ z ∈ R, V09D.mult z) + (∑ z ∈ L, V09D.mult z) =
      ∑ z ∈ S, V09D.mult z := by
    exact Finset.sum_filter_add_sum_filter_not S (fun z => (1:ℝ)/2 ≤ z.re) V09D.mult
  rw [count_window,rightCount]
  change (∑ z ∈ S, V09D.mult z) ≤ 2 * (∑ z ∈ R, V09D.mult z)
  omega

noncomputable def center (t : ℝ) : ℂ :=
  2 + ((t+1/2 : ℝ):ℂ)*Complex.I

theorem center_re (t : ℝ) : (center t).re = 2 := by
  simp [center,Complex.add_re,Complex.mul_re]

theorem center_im (t : ℝ) : (center t).im = t+1/2 := by
  simp [center,Complex.add_im,Complex.mul_im]

theorem right_window_in_disk (t : ℝ) (z : ℂ) (hz : z ∈ rightWindow t (t+1)) :
    z ∈ closedBall (center t) (8/5:ℝ) := by
  have h := (mem_rightWindow t (t+1) z).mp hz
  have hr := h.2
  have hr' := h.1.1.2.2
  have hi := h.1.2.1
  have hi' := h.1.2.2
  rw [mem_closedBall,dist_eq_norm]
  have hsq : ‖z-center t‖^2 ≤ (8/5:ℝ)^2 := by
    rw [Complex.sq_norm,Complex.normSq_apply,Complex.sub_re,Complex.sub_im,center_re,center_im]
    nlinarith [mul_nonneg (show 0 ≤ z.re-1/2 by linarith) (show 0 ≤ 7/2-z.re by linarith),
      mul_nonneg (show 0 ≤ z.im-t by linarith) (show 0 ≤ t+1-z.im by linarith)]
  nlinarith [norm_nonneg (z-center t)]

theorem outer_disk_geometry (t : ℝ) (ht : 4 ≤ |t|) (z : ℂ)
    (hz : z ∈ closedBall (center t) (9/5:ℝ)) :
    (1/5:ℝ) ≤ z.re ∧ 1 ≤ ‖z-1‖ ∧ |z.im|+3 ≤ |t|+6 := by
  have hn : ‖z-center t‖ ≤ (9/5:ℝ) := by simpa [mem_closedBall,dist_eq_norm] using hz
  have hr := (Complex.abs_re_le_norm (z-center t)).trans hn
  have hi := (Complex.abs_im_le_norm (z-center t)).trans hn
  rw [Complex.sub_re,center_re] at hr
  rw [Complex.sub_im,center_im] at hi
  have hc : |t| ≤ |t+1/2|+1/2 := by
    have h := abs_add_le (t+1/2) (-(1/2):ℝ)
    rw [show t+1/2+(-(1/2):ℝ) = t by ring] at h
    norm_num at h
    exact h
  have hl := abs_add_le (t+1/2-z.im) z.im
  rw [show t+1/2-z.im+z.im = t+1/2 by ring,abs_sub_comm] at hl
  have hnorm : |z.im| ≤ ‖z-1‖ := by
    simpa [Complex.sub_im] using Complex.abs_im_le_norm (z-1)
  have hu := abs_add_le (z.im-(t+1/2)) (t+1/2)
  rw [sub_add_cancel] at hu
  have hu' := abs_add_le t (1/2:ℝ)
  norm_num at hu'
  exact ⟨by linarith [(abs_le.mp hr).1],by linarith,
    by linarith⟩

theorem zeta_disk_analytic (t : ℝ) (ht : 4 ≤ |t|) :
    AnalyticOnNhd ℂ riemannZeta (closedBall (center t) (9/5:ℝ)) := by
  intro z hz
  have hn := (outer_disk_geometry t ht z hz).2.1
  have h1 : z ≠ 1 := by
    intro he
    rw [he,sub_self,norm_zero] at hn
    norm_num at hn
  exact analyticOn_riemannZeta z (by simpa using h1)

theorem right_count_le_divisor (t : ℝ) (ht : 4 ≤ |t|) :
    (rightCount t (t+1) : ℤ) ≤
      ∑ᶠ z, divisor riemannZeta (closedBall (center t) (8/5:ℝ)) z := by
  classical
  let S := rightWindow t (t+1)
  let D := divisor riemannZeta (closedBall (center t) (8/5:ℝ))
  have ha : AnalyticOnNhd ℂ riemannZeta (closedBall (center t) (8/5:ℝ)) :=
    (zeta_disk_analytic t ht).mono (closedBall_subset_closedBall (by norm_num))
  have hd : (Function.support D).Finite := D.finiteSupport (isCompact_closedBall _ _)
  let U := S ∪ hd.toFinset
  have hU : Function.support D ⊆ U := by
    intro z hz
    exact Finset.mem_union_right _ (hd.mem_toFinset.mpr hz)
  have hterm : ∀ z ∈ S, (V09D.mult z : ℤ) = D z := by
    intro z hz
    have hwin := (mem_rightWindow t (t+1) z).mp hz
    have h1 : z ≠ 1 := by
      intro h
      have hh := hwin.1.1.2.2
      rw [h,Complex.one_re] at hh
      exact lt_irrefl _ hh
    obtain ⟨n,hn⟩ := ENat.ne_top_iff_exists.mp (V10B6g.zeta_order_finite z h1)
    change (V09D.mult z : ℤ) = divisor riemannZeta (closedBall (center t) (8/5:ℝ)) z
    rw [ha.divisor_apply (right_window_in_disk t z hz)]
    simp [V09D.mult,← hn]
  change (rightCount t (t+1) : ℤ) ≤ ∑ᶠ z,D z
  rw [finsum_eq_sum_of_support_subset D (s := U) hU]
  calc
    (rightCount t (t+1) : ℤ) = ∑ z ∈ S, (V09D.mult z : ℤ) := by
      simp [rightCount,S]
    _ = ∑ z ∈ S, D z := Finset.sum_congr rfl hterm
    _ ≤ ∑ z ∈ U, D z := Finset.sum_le_sum_of_subset_of_nonneg
      (Finset.subset_union_left) (fun z _ _ => ha.divisor_nonneg z)

def HalfPlaneGrowth : Prop :=
  ∃ C : ℝ, 1 ≤ C ∧ ∀ z : ℂ, (1/5:ℝ) ≤ z.re → 1 ≤ ‖z-1‖ →
    ‖riemannZeta z‖ ≤ C*(|z.im|+3)

def CenterLower : Prop :=
  ∀ t : ℝ, (1/3:ℝ) ≤ ‖riemannZeta (center t)‖

theorem right_count_jensen (hg : HalfPlaneGrowth) (hl : CenterLower) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ t : ℝ, 4 ≤ |t| →
      (rightCount t (t+1) : ℝ) ≤ C * Real.log (|t|+3) := by
  obtain ⟨K,hK,hgrow⟩ := hg
  let d := Real.log ((9/5:ℝ)/(8/5))
  have hd : 0 < d := Real.log_pos (by norm_num)
  have hlog3 : 0 < Real.log 3 := Real.log_pos (by norm_num)
  let C := (Real.log (3*K)/Real.log 3+2)/d
  have hlogK : 0 ≤ Real.log (3*K) := Real.log_nonneg (by linarith)
  refine ⟨C,by dsimp [C]; positivity,?_⟩
  intro t ht
  let M := K*(|t|+6)
  have hM : 1 ≤ M := by dsimp [M]; nlinarith [abs_nonneg t]
  have hcenter := hl t
  have hne : riemannZeta (center t) ≠ 0 := by
    intro h
    rw [h,norm_zero] at hcenter
    norm_num at hcenter
  have hb : ∀ z ∈ sphere (center t) (9/5:ℝ), ‖riemannZeta z‖ ≤ M := by
    intro z hz
    have hgeo := outer_disk_geometry t ht z (sphere_subset_closedBall hz)
    exact (hgrow z hgeo.1 hgeo.2.1).trans (mul_le_mul_of_nonneg_left hgeo.2.2 (by linarith))
  have hj := AnalyticOnNhd.sum_divisor_le (f := riemannZeta) (c := center t)
    (r := (8/5:ℝ)) (R := (9/5:ℝ)) (M := M) (by norm_num) (by norm_num)
    hM (by simpa only [abs_of_nonneg (by norm_num : (0:ℝ) ≤ 9/5)] using zeta_disk_analytic t ht)
    hne (by simpa only [abs_of_nonneg (by norm_num : (0:ℝ) ≤ 9/5)] using hb)
  rw [abs_of_nonneg (by norm_num : (0:ℝ) ≤ 8/5)] at hj
  have hn : (rightCount t (t+1) : ℝ) ≤
      ((∑ᶠ z, divisor riemannZeta (closedBall (center t) (8/5:ℝ)) z : ℤ) : ℝ) := by
    exact_mod_cast right_count_le_divisor t ht
  have hratio : M/‖riemannZeta (center t)‖ ≤ 3*M := by
    apply (div_le_iff₀ (norm_pos_iff.mpr hne)).mpr
    nlinarith [mul_nonneg (show 0 ≤ M by linarith) (show 0 ≤ 3*‖riemannZeta (center t)‖-1 by linarith)]
  have hlog := Real.log_le_log (show 0 < M/‖riemannZeta (center t)‖ by positivity) hratio
  have hlogt : Real.log 3 ≤ Real.log (|t|+3) := Real.log_le_log (by norm_num) (by linarith [abs_nonneg t])
  have hlog6 : Real.log (|t|+6) ≤ 2*Real.log (|t|+3) := by
    rw [← Real.log_pow]
    apply Real.log_le_log (by positivity)
    nlinarith [sq_nonneg |t|,abs_nonneg t]
  have hconstant : Real.log (3*K) ≤
      (Real.log (3*K)/Real.log 3)*Real.log (|t|+3) := by
    calc
      _ = (Real.log (3*K)/Real.log 3)*Real.log 3 := by field_simp [hlog3.ne']
      _ ≤ _ := mul_le_mul_of_nonneg_left hlogt (by positivity)
  have hmain : Real.log (M/‖riemannZeta (center t)‖) ≤
      (Real.log (3*K)/Real.log 3+2)*Real.log (|t|+3) := by
    apply hlog.trans
    rw [show 3*M = (3*K)*(|t|+6) by dsimp [M]; ring,
      Real.log_mul (by positivity) (by positivity)]
    nlinarith only [hconstant,hlog6]
  calc
    _ ≤ Real.log (M/‖riemannZeta (center t)‖)/d := hn.trans hj
    _ ≤ _ := by
      dsimp [C]
      rw [div_mul_eq_mul_div]
      exact div_le_div_of_nonneg_right hmain hd.le

theorem all_real_local_count (hg : HalfPlaneGrowth) (hl : CenterLower)
    (hr : ∀ z, V09D.stripZero z → V09D.stripZero (V10A.reflect z))
    (hm : ∀ z, V09D.stripZero z → V09D.mult (V10A.reflect z) = V09D.mult z) :
    ∃ A : ℝ, 1 ≤ A ∧ ∀ t : ℝ, (V09D.count t (t+1) : ℝ) ≤
      A*Real.log (|t|+3) := by
  obtain ⟨C,hC,hlarge⟩ := right_count_jensen hg hl
  let B : ℝ := V09D.count (-4) 5
  let A := max 1 (max (2*C) (B/Real.log 3))
  refine ⟨A,le_max_left _ _,?_⟩
  intro t
  have hlog3 : 0 < Real.log 3 := Real.log_pos (by norm_num)
  have hlogt : Real.log 3 ≤ Real.log (|t|+3) :=
    Real.log_le_log (by norm_num) (by linarith [abs_nonneg t])
  have hA1 : 2*C ≤ A := (le_max_left _ _).trans (le_max_right _ _)
  have hA2 : B/Real.log 3 ≤ A := (le_max_right _ _).trans (le_max_right _ _)
  by_cases ht : 4 ≤ |t|
  · have hh : (V09D.count t (t+1) : ℝ) ≤ 2*(rightCount t (t+1) : ℝ) := by
      exact_mod_cast count_le_twice_right t (t+1) hr hm
    calc
      _ ≤ 2*(rightCount t (t+1) : ℝ) := hh
      _ ≤ (2*C)*Real.log (|t|+3) := by linarith [hlarge t ht]
      _ ≤ _ := mul_le_mul_of_nonneg_right hA1 (hlog3.le.trans hlogt)
  · have ha := abs_le.mp (le_of_lt (lt_of_not_ge ht))
    have hsmall : (V09D.count t (t+1) : ℝ) ≤ B := by
      exact_mod_cast count_mono_window (a := t) (b := t+1) (c := -4) (d := 5)
        ha.1 (by linarith [ha.2])
    calc
      _ ≤ B := hsmall
      _ = (B/Real.log 3)*Real.log 3 := by field_simp [hlog3.ne']
      _ ≤ (B/Real.log 3)*Real.log (|t|+3) :=
        mul_le_mul_of_nonneg_left hlogt (by dsimp [B]; positivity)
      _ ≤ _ := mul_le_mul_of_nonneg_right hA2 (hlog3.le.trans hlogt)

end WeilDefect.MasterRecon.V10B7a

#print axioms WeilDefect.MasterRecon.V10B7a.window_finite
#print axioms WeilDefect.MasterRecon.V10B7a.mem_window
#print axioms WeilDefect.MasterRecon.V10B7a.count_window
#print axioms WeilDefect.MasterRecon.V10B7a.count_mono_window
#print axioms WeilDefect.MasterRecon.V10B7a.mem_rightWindow
#print axioms WeilDefect.MasterRecon.V10B7a.count_le_twice_right
#print axioms WeilDefect.MasterRecon.V10B7a.center_re
#print axioms WeilDefect.MasterRecon.V10B7a.center_im
#print axioms WeilDefect.MasterRecon.V10B7a.right_window_in_disk
#print axioms WeilDefect.MasterRecon.V10B7a.outer_disk_geometry
#print axioms WeilDefect.MasterRecon.V10B7a.zeta_disk_analytic
#print axioms WeilDefect.MasterRecon.V10B7a.right_count_le_divisor
#print axioms WeilDefect.MasterRecon.V10B7a.right_count_jensen
#print axioms WeilDefect.MasterRecon.V10B7a.all_real_local_count
