import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory

/-- One-sided integral Cauchy--Schwarz using a nonnegative square, avoiding rpow. -/
theorem neutralIV106D4IntervalCS (v : ℝ → ℂ) (hv : Continuous v)
    (l r : ℝ) (hlr : l ≤ r) :
    ‖∫ t in l..r, v t‖^2 ≤ (r-l) * (∫ t in l..r, ‖v t‖^2) := by
  rcases hlr.eq_or_lt with h | h
  · subst r
    simp
  let H : ℝ := r-l
  let m : ℝ := ∫ t in l..r, ‖v t‖
  let E : ℝ := ∫ t in l..r, ‖v t‖^2
  have hH : 0 < H := sub_pos.mpr h
  have hf : Continuous (fun t => ‖v t‖^2) := hv.norm.pow 2
  have hg : Continuous (fun t => (2*H*m)*‖v t‖) := continuous_const.mul hv.norm
  have hp : Continuous (fun t => H^2*‖v t‖^2) := continuous_const.mul hf
  have hsub : Continuous (fun t => H^2*‖v t‖^2-(2*H*m)*‖v t‖) := hp.sub hg
  have hz : 0 ≤ ∫ t in l..r, (H*‖v t‖-m)^2 :=
    intervalIntegral.integral_nonneg_of_forall h.le (fun t => sq_nonneg _)
  have he : (∫ t in l..r, (H*‖v t‖-m)^2) = H^2*E-H*m^2 := by
    calc
      _ = ∫ t in l..r, (H^2*‖v t‖^2-(2*H*m)*‖v t‖)+m^2 := by
        apply intervalIntegral.integral_congr
        intro t ht
        ring
      _ = H^2*E-H*m^2 := by
        rw [intervalIntegral.integral_add
          (hsub.intervalIntegrable (μ := volume) l r)
          (continuous_const.intervalIntegrable (μ := volume) l r),
          intervalIntegral.integral_sub
          (hp.intervalIntegrable (μ := volume) l r)
          (hg.intervalIntegrable (μ := volume) l r),
          intervalIntegral.integral_const_mul, intervalIntegral.integral_const_mul,
          intervalIntegral.integral_const, smul_eq_mul]
        change H^2*E-2*H*m*m+H*m^2 = _
        ring
  rw [he] at hz
  have hmul : H*m^2 ≤ H*(H*E) := by nlinarith only [hz]
  have hm : m^2 ≤ H*E := (mul_le_mul_left hH).mp hmul
  have hn : ‖∫ t in l..r, v t‖ ≤ m :=
    intervalIntegral.norm_integral_le_integral_norm h.le
  exact (pow_le_pow_left₀ (norm_nonneg _) hn 2).trans hm

/-- Integrate the exact quadratic cell envelope by an explicit antiderivative. -/
theorem neutralIV106D4Envelope (l r : ℝ) (hlr : l < r) :
    (∫ x in l..r, (x-l)*(r-x)/(r-l)) = (r-l)^2/6 := by
  let F : ℝ → ℝ := fun x => (x-l)^2/2-(x-l)^3/(3*(r-l))
  have hd (x : ℝ) : HasDerivAt F ((x-l)*(r-x)/(r-l)) x := by
    have hx := (hasDerivAt_id x).sub_const l
    have h := ((hx.pow 2).div_const 2).sub ((hx.pow 3).div_const (3*(r-l)))
    convert h using 1 <;> field_simp [sub_ne_zero.mpr (ne_of_gt hlr)] <;> ring
  have hc : Continuous (fun x : ℝ => (x-l)*(r-x)/(r-l)) :=
    (((continuous_id.sub continuous_const).mul
      (continuous_const.sub continuous_id)).div_const _)
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hd x)
    (hc.intervalIntegrable (μ := volume) l r)]
  dsimp [F]
  field_simp [sub_ne_zero.mpr (ne_of_gt hlr)]
  <;> ring

/-- Direct pointwise bound on the actual cell primitive. -/
theorem neutralIV106D4Point (v : ℝ → ℂ) (hv : Continuous v)
    (l r x : ℝ) (hlr : l < r) (hl : l ≤ x) (hr : x ≤ r)
    (hm : (∫ t in l..r, v t) = 0) :
    ‖∫ t in l..x, v t‖^2 ≤
      ((x-l)*(r-x)/(r-l))*(∫ t in l..r, ‖v t‖^2) := by
  have hL := neutralIV106D4IntervalCS v hv l x hl
  have hR := neutralIV106D4IntervalCS v hv x r hr
  have he := intervalIntegral.integral_add_adjacent_intervals
    (hv.intervalIntegrable (μ := volume) l x)
    (hv.intervalIntegrable (μ := volume) x r)
  rw [hm] at he
  have hneg : (∫ t in x..r, v t) = -(∫ t in l..x, v t) :=
    eq_neg_of_add_eq_zero_right he
  rw [hneg, norm_neg] at hR
  have h1 := mul_le_mul_of_nonneg_left hL (sub_nonneg.mpr hr)
  have h2 := mul_le_mul_of_nonneg_left hR (sub_nonneg.mpr hl)
  have hc : Continuous (fun t => ‖v t‖^2) := hv.norm.pow 2
  have hsum := intervalIntegral.integral_add_adjacent_intervals
    (hc.intervalIntegrable (μ := volume) l x)
    (hc.intervalIntegrable (μ := volume) x r)
  rw [div_mul_eq_mul_div]
  apply (le_div_iff₀ (sub_pos.mpr hlr)).mpr
  rw [← hsum]
  nlinarith only [h1, h2]

#print axioms neutralIV106D4IntervalCS
#print axioms neutralIV106D4Envelope
#print axioms neutralIV106D4Point
end
end WeilDefect
