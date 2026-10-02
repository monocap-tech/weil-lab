import WeilDefect.Morphology.NeutralDigammaRealComplexAnchor
import Mathlib.Analysis.Complex.LocallyUniformLimit

namespace WeilDefect

noncomputable section

open scoped BigOperators Topology

/-- Independent regularized Euler term, before identification with digamma. -/
def neutralDigammaEulerTerm (n : ℕ) (z : ℂ) : ℂ :=
  1 / ((n : ℂ)+1) - 1 / (z+(n : ℂ))

/-- The holomorphic candidate; equality with actual digamma is a separate obligation. -/
def neutralDigammaEulerSeries (z : ℂ) : ℂ :=
  -(Real.eulerMascheroniConstant : ℂ) + ∑' n, neutralDigammaEulerTerm n z

theorem neutralDigamma_euler_term_bound {z : ℂ} {a : ℝ}
    (ha : 0 < a) (haz : a ≤ z.re) (ha1 : a ≤ 1) (n : ℕ) :
    ‖neutralDigammaEulerTerm n z‖ ≤
      (‖z-1‖ / a) * (1 / ((n : ℝ)+1)^2) := by
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have hs : 0 < (n : ℝ)+1 := by positivity
  have ht : 0 < z.re+(n : ℝ) := by linarith
  have hz : z+(n : ℂ) ≠ 0 := Complex.ne_zero_of_re_pos (by simpa using ht)
  have hnz : (n : ℂ)+1 ≠ 0 := Complex.ne_zero_of_re_pos (by simpa using hs)
  have he : neutralDigammaEulerTerm n z =
      (z-1) / (((n : ℂ)+1)*(z+(n : ℂ))) := by
    unfold neutralDigammaEulerTerm
    field_simp
    ring
  have hlow : a*((n : ℝ)+1) ≤ z.re+(n : ℝ) := by
    nlinarith [mul_nonneg (sub_nonneg.mpr ha1) hn]
  have hnorm : z.re+(n : ℝ) ≤ ‖z+(n : ℂ)‖ := by
    simpa using Complex.re_le_norm (z+(n : ℂ))
  have hden : a*((n : ℝ)+1)^2 ≤ ((n : ℝ)+1)*‖z+(n : ℂ)‖ := by
    nlinarith [mul_le_mul_of_nonneg_left (hlow.trans hnorm) hs.le]
  have hcast : ‖(n : ℂ)+1‖ = (n : ℝ)+1 := by
    rw [← Complex.ofReal_natCast, ← Complex.ofReal_one, ← Complex.ofReal_add]
    exact Complex.norm_of_nonneg hs.le
  rw [he, norm_div, norm_mul, hcast]
  calc
    _ ≤ ‖z-1‖ / (a*((n : ℝ)+1)^2) :=
      div_le_div_of_nonneg_left (norm_nonneg _) (by positivity) hden
    _ = _ := by field_simp [ha.ne', hs.ne']

theorem neutralDigamma_euler_majorant_summable (C : ℝ) :
    Summable (fun n : ℕ => C * (1 / ((n : ℝ)+1)^2)) := by
  have hs : Summable (fun n : ℕ => 1 / ((n : ℝ)+1)^2) := by
    simpa only [Nat.cast_add, Nat.cast_one] using
      (summable_nat_add_iff (f := fun n : ℕ => 1 / (n : ℝ)^2) 1).mpr
        (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < (2 : ℕ)))
  exact hs.mul_left C

theorem neutralDigamma_euler_summable {z : ℂ} (hz : 0 < z.re) :
    Summable (fun n => neutralDigammaEulerTerm n z) := by
  exact (neutralDigamma_euler_majorant_summable (‖z-1‖ / min z.re 1)).of_norm_bounded
    (fun n => neutralDigamma_euler_term_bound (lt_min hz zero_lt_one)
      (min_le_left _ _) (min_le_right _ _) n)

/-- Holomorphy on bounded open subsets separated from the imaginary axis,
by an independent summable norm majorant. -/
theorem neutralDigamma_euler_tsum_differentiableOn {a R : ℝ}
    (ha : 0 < a) (ha1 : a ≤ 1) :
    DifferentiableOn ℂ (fun z => ∑' n, neutralDigammaEulerTerm n z)
      {z : ℂ | a < z.re ∧ ‖z-1‖ < R} := by
  have ho : IsOpen {z : ℂ | a < z.re ∧ ‖z-1‖ < R} :=
    (isOpen_lt continuous_const Complex.continuous_re).inter
      (isOpen_lt (continuous_id.sub continuous_const).norm continuous_const)
  refine Complex.differentiableOn_tsum_of_summable_norm
    (F := fun n z => neutralDigammaEulerTerm n z)
    (neutralDigamma_euler_majorant_summable (R / a)) ?_ ho ?_
  · intro n z hz
    have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
    have hne : z+(n : ℂ) ≠ 0 := Complex.ne_zero_of_re_pos (by
      simp only [Complex.add_re, Complex.natCast_re]
      linarith [hz.1])
    change DifferentiableWithinAt ℂ
      (fun w : ℂ => 1 / ((n : ℂ)+1) - 1 / (w+(n : ℂ))) _ z
    exact ((differentiableAt_const (1 / ((n : ℂ)+1))).sub
      ((differentiableAt_const (1 : ℂ)).div
        (differentiableAt_id.add_const (n : ℂ)) hne)).differentiableWithinAt
  · intro n z hz
    exact (neutralDigamma_euler_term_bound ha hz.1.le ha1 n).trans (by
      gcongr
      exact hz.2.le)

/-- The independently constructed Euler candidate is holomorphic throughout
the right half-plane. This does not yet identify actual complex digamma. -/
theorem neutralDigamma_eulerSeries_differentiableOn :
    DifferentiableOn ℂ neutralDigammaEulerSeries {z : ℂ | 0 < z.re} := by
  intro z hz
  change 0 < z.re at hz
  let a := min z.re 1 / 2
  have ha : 0 < a := div_pos (lt_min hz zero_lt_one) (by norm_num)
  have ha1 : a ≤ 1 := by dsimp [a]; linarith [min_le_right z.re 1]
  have haz : a < z.re := by dsimp [a]; linarith [min_le_left z.re 1]
  have ho : IsOpen {w : ℂ | a < w.re ∧ ‖w-1‖ < ‖z-1‖+1} :=
    (isOpen_lt continuous_const Complex.continuous_re).inter
      (isOpen_lt (continuous_id.sub continuous_const).norm continuous_const)
  have hm : z ∈ {w : ℂ | a < w.re ∧ ‖w-1‖ < ‖z-1‖+1} :=
    ⟨haz, by linarith⟩
  have hd := (neutralDigamma_euler_tsum_differentiableOn
    (R := ‖z-1‖+1) ha ha1).differentiableAt (ho.mem_nhds hm)
  exact ((differentiableAt_const _).add hd).differentiableWithinAt

end

end WeilDefect
