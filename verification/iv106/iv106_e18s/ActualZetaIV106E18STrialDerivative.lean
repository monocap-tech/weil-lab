import WeilDefect.Arithmetic.ActualZetaIV106E18K2PhysicalMoments

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter
open scoped Topology

/-- Fourth derivative of the exact seed, not a fitted profile. -/
def neutralIV106E18SB4 (t : ℝ) : ℝ :=
  120*t*(1-t)^5 - 1200*t^2*(1-t)^4 +
  2400*t^3*(1-t)^3 - 1200*t^4*(1-t)^2 + 120*t^5*(1-t)

def neutralIV106E18SDPoly (h t : ℝ) : ℝ :=
  neutralIV106E18SB4 t - h^2/4*neutralIV106E18K1B2 t

theorem neutralIV106E18SJet (h t : ℝ) :
    HasDerivAt (neutralIV106E18K1Poly h) (neutralIV106E18SDPoly h t) t := by
  have ht : HasDerivAt (fun x : ℝ => x) 1 t := hasDerivAt_id t
  have hu : HasDerivAt (fun x : ℝ => 1-x) (-1) t := by
    convert (hasDerivAt_const t (1:ℝ)).sub ht using 1 <;>
      first | rfl | (funext x; rfl) | norm_num
  have h3 : HasDerivAt neutralIV106E18K1B3 (neutralIV106E18SB4 t) t := by
    unfold neutralIV106E18K1B3 neutralIV106E18SB4
    convert (((((ht.pow 2).mul (hu.pow 5)).const_mul 60).sub
      (((ht.pow 3).mul (hu.pow 4)).const_mul 300)).add
      (((ht.pow 4).mul (hu.pow 3)).const_mul 300)).sub
      (((ht.pow 5).mul (hu.pow 2)).const_mul 60) using 1 <;>
      first | rfl | (funext x; simp only [Pi.pow_apply,Pi.mul_apply,Pi.add_apply,Pi.sub_apply,id_eq]; ring) |
        (simp only [Pi.pow_apply,Pi.mul_apply,Pi.add_apply,Pi.sub_apply,id_eq]; ring)
  exact h3.sub ((neutralIV106E18K1Jets t).2.1.const_mul (h^2/4))

theorem neutralIV106E18SDPoly_endpoints (h : ℝ) :
    neutralIV106E18SDPoly h 0 = 0 ∧ neutralIV106E18SDPoly h 1 = 0 := by
  norm_num [neutralIV106E18SDPoly,neutralIV106E18SB4,neutralIV106E18K1B2]

def neutralIV106E18SClip (t : ℝ) : ℝ := max 0 (min 1 t)

theorem neutralIV106E18SClip_derivative
    (P Q : ℝ → ℝ) (hP : ∀ t, HasDerivAt P (Q t) t)
    (hQ0 : Q 0 = 0) (hQ1 : Q 1 = 0) (t : ℝ) :
    HasDerivAt (fun x => P (neutralIV106E18SClip x))
      (Q (neutralIV106E18SClip t)) t := by
  have hl (x : ℝ) (hx : x ≤ 0) : P (neutralIV106E18SClip x) = P 0 := by
    simp [neutralIV106E18SClip,min_eq_right (show x ≤ 1 by linarith),max_eq_left hx]
  have hr (x : ℝ) (hx : 1 ≤ x) : P (neutralIV106E18SClip x) = P 1 := by
    simp [neutralIV106E18SClip,min_eq_left hx]
  have hm (x : ℝ) (hx : x ∈ Icc (0:ℝ) 1) :
      P (neutralIV106E18SClip x) = P x := by
    simp [neutralIV106E18SClip,min_eq_right hx.2,max_eq_right hx.1]
  rcases lt_trichotomy t 0 with h | rfl | h
  · have hc : neutralIV106E18SClip t = 0 := by
      simp [neutralIV106E18SClip,min_eq_right (show t ≤ 1 by linarith),max_eq_left h.le]
    rw [hc,hQ0]
    apply (hasDerivAt_const t (P 0)).congr_of_eventuallyEq
    filter_upwards [Iio_mem_nhds h] with x hx
    exact hl x hx.le
  · have hc : neutralIV106E18SClip 0 = 0 := by norm_num [neutralIV106E18SClip]
    rw [hc,hQ0]
    have hL : HasDerivWithinAt (fun x => P (neutralIV106E18SClip x)) 0 (Iic 0) 0 :=
      (hasDerivAt_const (0:ℝ) (P 0)).hasDerivWithinAt.congr_of_mem hl (by simp)
    have hM : HasDerivWithinAt (fun x => P (neutralIV106E18SClip x)) 0 (Icc 0 1) 0 := by
      have hh := (hP 0).hasDerivWithinAt (s := Icc (0:ℝ) 1)
      rw [hQ0] at hh
      exact hh.congr_of_mem hm (by norm_num)
    apply (hL.union hM).hasDerivAt
    apply mem_of_superset (Iio_mem_nhds (by norm_num : (0:ℝ)<1))
    intro x hx
    by_cases hx0 : x ≤ 0
    · exact Or.inl hx0
    · exact Or.inr ⟨le_of_not_ge hx0,hx.le⟩
  · rcases lt_trichotomy t 1 with h' | rfl | h'
    · have hc : neutralIV106E18SClip t = t := by
        simp [neutralIV106E18SClip,min_eq_right h'.le,max_eq_right h.le]
      rw [hc]
      apply (hP t).congr_of_eventuallyEq
      filter_upwards [Ioo_mem_nhds h h'] with x hx
      exact hm x ⟨hx.1.le,hx.2.le⟩
    · have hc : neutralIV106E18SClip 1 = 1 := by norm_num [neutralIV106E18SClip]
      rw [hc,hQ1]
      have hR : HasDerivWithinAt (fun x => P (neutralIV106E18SClip x)) 0 (Ici 1) 1 :=
        (hasDerivAt_const (1:ℝ) (P 1)).hasDerivWithinAt.congr_of_mem hr (by simp)
      have hM : HasDerivWithinAt (fun x => P (neutralIV106E18SClip x)) 0 (Icc 0 1) 1 := by
        have hh := (hP 1).hasDerivWithinAt (s := Icc (0:ℝ) 1)
        rw [hQ1] at hh
        exact hh.congr_of_mem hm (by norm_num)
      apply (hM.union hR).hasDerivAt
      apply mem_of_superset (Ioi_mem_nhds (by norm_num : (0:ℝ)<1))
      intro x hx
      by_cases hx1 : x ≤ 1
      · exact Or.inl ⟨hx.le,hx1⟩
      · exact Or.inr (le_of_not_ge hx1)
    · have hc : neutralIV106E18SClip t = 1 := by
        simp [neutralIV106E18SClip,min_eq_left h'.le]
      rw [hc,hQ1]
      apply (hasDerivAt_const t (P 1)).congr_of_eventuallyEq
      filter_upwards [Ioi_mem_nhds h'] with x hx
      exact hr x hx.le

/-- Actual derivative of the literal clipped trial, including the affine
Jacobian and both joins. -/
def neutralIV106E18SDTrial (l h x : ℝ) : ℂ :=
  (neutralIV106E18SDPoly h (neutralIV106E18SClip ((x-l)/h))/h : ℝ)

theorem neutralIV106E18STrial_derivative (l h : ℝ) (hh : 0 < h) (x : ℝ) :
    HasDerivAt (neutralIV106E18ITrial l h) (neutralIV106E18SDTrial l h x) x := by
  have hd := neutralIV106E18SClip_derivative (neutralIV106E18K1Poly h)
    (neutralIV106E18SDPoly h) (neutralIV106E18SJet h)
    (neutralIV106E18SDPoly_endpoints h).1 (neutralIV106E18SDPoly_endpoints h).2 ((x-l)/h)
  have ha : HasDerivAt (fun y : ℝ => (y-l)/h) (1/h) x := by
    simpa using ((hasDerivAt_id x).sub_const l).div_const h
  have he := (hd.comp x ha).ofReal_comp
  convert he using 1
  · funext y
    simp only [neutralIV106E18ITrial,neutralIV106E18SClip,neutralIV106E18K2Poly_eq,Function.comp_apply]
  · simp [neutralIV106E18SDTrial,div_eq_mul_inv]

theorem neutralIV106E18SDTrial_continuous (l h : ℝ) :
    Continuous (neutralIV106E18SDTrial l h) := by
  unfold neutralIV106E18SDTrial neutralIV106E18SDPoly neutralIV106E18SB4
    neutralIV106E18K1B2 neutralIV106E18SClip
  fun_prop

theorem neutralIV106E18SDTrial_outside (l h : ℝ) (hh : 0 < h)
    (x : ℝ) (hx : x ∉ Icc l (l+h)) : neutralIV106E18SDTrial l h x = 0 := by
  by_cases hl : x < l
  · have h0 : (x-l)/h ≤ 0 := div_nonpos_of_nonpos_of_nonneg (by linarith) hh.le
    simp [neutralIV106E18SDTrial,neutralIV106E18SClip,min_eq_right (show (x-l)/h ≤ 1 by linarith),
      max_eq_left h0,(neutralIV106E18SDPoly_endpoints h).1]
  · have hr : l+h < x := by
      by_contra! hn
      exact hx ⟨le_of_not_gt hl,hn⟩
    have h1 : 1 ≤ (x-l)/h := (le_div_iff₀ hh).mpr (by linarith)
    simp [neutralIV106E18SDTrial,neutralIV106E18SClip,min_eq_left h1,
      (neutralIV106E18SDPoly_endpoints h).2]

theorem neutralIV106E18SDTrial_memLp (l h : ℝ) (hh : 0 < h) :
    MemLp (neutralIV106E18SDTrial l h) 2 volume := by
  apply (neutralIV106E18SDTrial_continuous l h).memLp_of_hasCompactSupport
  exact HasCompactSupport.intro (K := Icc l (l+h)) isCompact_Icc
    (neutralIV106E18SDTrial_outside l h hh)

#print axioms neutralIV106E18SJet
#print axioms neutralIV106E18SDPoly_endpoints
#print axioms neutralIV106E18SClip_derivative
#print axioms neutralIV106E18STrial_derivative
#print axioms neutralIV106E18SDTrial_continuous
#print axioms neutralIV106E18SDTrial_outside
#print axioms neutralIV106E18SDTrial_memLp
end
end WeilDefect
