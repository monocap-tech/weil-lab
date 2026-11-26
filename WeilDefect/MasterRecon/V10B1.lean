import WeilDefect.MasterRecon.V10A2
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus

/-! V10B1: elementary unit-interval point evaluation via the fundamental
theorem applied to squared real components. The derivative majorant
avoids a separate Cauchy–Schwarz integral lemma. -/
namespace WeilDefect.MasterRecon.V10B1

open Set MeasureTheory
open scoped Interval

theorem ordered_oscillation (g D B : ℝ → ℝ)
    (hd : ∀ x, HasDerivAt g (D x) x)
    (hD : Continuous D) (hB : Continuous B)
    (hbound : ∀ x, |D x| ≤ B x)
    (a b p q : ℝ) (hap : a ≤ p) (hpq : p ≤ q) (hqb : q ≤ b) :
    |g q - g p| ≤ ∫ x in a..b, B x := by
  have hf : (∫ x in p..q, D x) = g q - g p :=
    intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hd x)
      (hD.intervalIntegrable p q)
  have hn := intervalIntegral.norm_integral_le_integral_norm
    (f := D) (μ := volume) hpq
  rw [hf, Real.norm_eq_abs] at hn
  have hm : (∫ x in p..q, ‖D x‖) ≤ ∫ x in p..q, B x :=
    intervalIntegral.integral_mono_on hpq
      (hD.norm.intervalIntegrable p q) (hB.intervalIntegrable p q)
      (fun x _ => by simpa only [Real.norm_eq_abs] using hbound x)
  have hnon : ∀ x, 0 ≤ B x := fun x => (abs_nonneg _).trans (hbound x)
  exact hn.trans (hm.trans
    (intervalIntegral.integral_mono_interval hap hpq hqb
      (ae_of_all _ hnon) (hB.intervalIntegrable a b)))

theorem unit_eval_majorant (g D B : ℝ → ℝ)
    (hg : Continuous g) (hd : ∀ x, HasDerivAt g (D x) x)
    (hD : Continuous D) (hB : Continuous B)
    (hbound : ∀ x, |D x| ≤ B x)
    (a p : ℝ) (hp : p ∈ Icc a (a + 1)) :
    g p ≤ (∫ x in a..a+1, g x) + ∫ x in a..a+1, B x := by
  let M : ℝ := ∫ x in a..a+1, B x
  have hpoint : ∀ q ∈ Icc a (a + 1), g p ≤ g q + M := by
    intro q hq
    rcases le_total p q with h | h
    · have hh := ordered_oscillation g D B hd hD hB hbound
        a (a+1) p q hp.1 h hq.2
      have hn := (abs_le.mp hh).1
      dsimp [M]
      linarith
    · have hh := ordered_oscillation g D B hd hD hB hbound
        a (a+1) q p hq.1 h hp.2
      have hn := (abs_le.mp hh).2
      dsimp [M]
      linarith
  have hmono := intervalIntegral.integral_mono_on
    (by linarith : a ≤ a+1)
    (continuous_const.intervalIntegrable a (a+1) :
      IntervalIntegrable (fun _ : ℝ => g p) volume a (a+1))
    ((hg.add continuous_const).intervalIntegrable a (a+1)) hpoint
  change (∫ _x in a..a+1, g p) ≤ ∫ x in a..a+1, (g x + M) at hmono
  rw [intervalIntegral.integral_add (hg.intervalIntegrable a (a+1))
    (continuous_const.intervalIntegrable a (a+1))] at hmono
  simpa [intervalIntegral.integral_const, sub_add_cancel_left, M] using hmono

theorem unit_eval_real (h h' : ℝ → ℝ)
    (hc : Continuous h) (hc' : Continuous h')
    (hd : ∀ x, HasDerivAt h (h' x) x)
    (a p : ℝ) (hp : p ∈ Icc a (a + 1)) :
    h p ^ 2 ≤ (∫ x in a..a+1, h x ^ 2) +
      ∫ x in a..a+1, (h x ^ 2 + h' x ^ 2) := by
  apply unit_eval_majorant (fun x => h x ^ 2)
    (fun x => 2 * h x * h' x) (fun x => h x ^ 2 + h' x ^ 2)
    (hc.pow 2) _ ((continuous_const.mul hc).mul hc')
    ((hc.pow 2).add (hc'.pow 2)) _ a p hp
  · intro x
    convert (hd x).pow 2 using 1 <;> ring
  · intro x
    apply abs_le.mpr
    constructor <;> nlinarith [sq_nonneg (h x + h' x), sq_nonneg (h x - h' x)]

theorem unit_eval_complex (h h' : ℝ → ℂ)
    (hc : Continuous h) (hc' : Continuous h')
    (hr : ∀ x, HasDerivAt (fun y => (h y).re) (h' x).re x)
    (hi : ∀ x, HasDerivAt (fun y => (h y).im) (h' x).im x)
    (a p : ℝ) (hp : p ∈ Icc a (a + 1)) :
    ‖h p‖ ^ 2 ≤ 2 * ∫ x in a..a+1, (‖h x‖ ^ 2 + ‖h' x‖ ^ 2) := by
  let r : ℝ → ℝ := fun x => (h x).re
  let s : ℝ → ℝ := fun x => (h x).im
  let r' : ℝ → ℝ := fun x => (h' x).re
  let s' : ℝ → ℝ := fun x => (h' x).im
  have cr : Continuous r := Complex.continuous_re.comp hc
  have cs : Continuous s := Complex.continuous_im.comp hc
  have cr' : Continuous r' := Complex.continuous_re.comp hc'
  have cs' : Continuous s' := Complex.continuous_im.comp hc'
  have er := unit_eval_real r r' cr cr' hr a p hp
  have es := unit_eval_real s s' cs cs' hi a p hp
  have ir : IntervalIntegrable (fun x => r x ^ 2) volume a (a+1) :=
    (cr.pow 2).intervalIntegrable a (a+1)
  have is : IntervalIntegrable (fun x => s x ^ 2) volume a (a+1) :=
    (cs.pow 2).intervalIntegrable a (a+1)
  have ir' : IntervalIntegrable (fun x => r' x ^ 2) volume a (a+1) :=
    (cr'.pow 2).intervalIntegrable a (a+1)
  have is' : IntervalIntegrable (fun x => s' x ^ 2) volume a (a+1) :=
    (cs'.pow 2).intervalIntegrable a (a+1)
  have hn : ∀ x, ‖h x‖ ^ 2 = r x ^ 2 + s x ^ 2 := by
    intro x
    simp [r, s, Complex.sq_norm, Complex.normSq_apply, pow_two]
  have hn' : ∀ x, ‖h' x‖ ^ 2 = r' x ^ 2 + s' x ^ 2 := by
    intro x
    simp [r', s', Complex.sq_norm, Complex.normSq_apply, pow_two]
  simp only [hn, hn']
  rw [intervalIntegral.integral_add (ir.add is) (ir'.add is'),
      intervalIntegral.integral_add ir is, intervalIntegral.integral_add ir' is']
  rw [intervalIntegral.integral_add ir ir'] at er
  rw [intervalIntegral.integral_add is is'] at es
  have hrn : 0 ≤ ∫ x in a..a+1, r' x ^ 2 :=
    intervalIntegral.integral_nonneg (by linarith) (fun _ _ => sq_nonneg _)
  have hsn : 0 ≤ ∫ x in a..a+1, s' x ^ 2 :=
    intervalIntegral.integral_nonneg (by linarith) (fun _ _ => sq_nonneg _)
  linarith

end WeilDefect.MasterRecon.V10B1

#print axioms WeilDefect.MasterRecon.V10B1.ordered_oscillation
#print axioms WeilDefect.MasterRecon.V10B1.unit_eval_majorant
#print axioms WeilDefect.MasterRecon.V10B1.unit_eval_real
#print axioms WeilDefect.MasterRecon.V10B1.unit_eval_complex
