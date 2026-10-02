import WeilDefect.Morphology.NeutralDigammaEulerHolomorphic
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.Convex.PathConnected

namespace WeilDefect

noncomputable section

open Set
open scoped BigOperators Topology

/-- Positive real part excludes all actual Gamma poles. -/
theorem neutralRightHalf_ne_neg_nat {z : ℂ} (hz : 0 < z.re) (n : ℕ) :
    z ≠ -(n : ℂ) := by
  intro h
  have hr := congrArg Complex.re h
  simp only [Complex.neg_re, Complex.natCast_re] at hr
  have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  linarith

theorem neutralDigamma_rightHalf_differentiableOn :
    DifferentiableOn ℂ Complex.digamma {z : ℂ | 0 < z.re} := by
  have ho : IsOpen {z : ℂ | 0 < z.re} :=
    isOpen_lt continuous_const Complex.continuous_re
  have hg : DifferentiableOn ℂ Complex.Gamma {z : ℂ | 0 < z.re} := by
    intro z hz
    exact (Complex.differentiableAt_Gamma z
      (neutralRightHalf_ne_neg_nat hz)).differentiableWithinAt
  change DifferentiableOn ℂ (fun z => deriv Complex.Gamma z / Complex.Gamma z) _
  exact (hg.deriv ho).div hg (fun z hz =>
    Complex.Gamma_ne_zero (neutralRightHalf_ne_neg_nat hz))

theorem neutralDigamma_eulerSeries_ofReal {x : ℝ} (hx : 0 < x) :
    Complex.digamma (x : ℂ) = neutralDigammaEulerSeries (x : ℂ) :=
  neutralDigamma_ofReal_eq_complex_euler_series hx

/-- The full actual positive-real equality has an accumulation point in
the holomorphy domain. -/
theorem neutralDigamma_euler_equality_accumulation :
    (1 : ℂ) ∈ closure ({z | Complex.digamma z = neutralDigammaEulerSeries z} \ {1}) := by
  have hr : (1 : ℝ) ∈ closure (Ioi (1 : ℝ)) := by
    simpa only [closure_Ioi, mem_Ici] using (le_refl (1 : ℝ))
  have hc : (1 : ℂ) ∈ closure (Complex.ofReal '' Ioi (1 : ℝ)) :=
    image_closure_subset_closure_image Complex.continuous_ofReal ⟨1, hr, rfl⟩
  apply closure_mono (s := Complex.ofReal '' Ioi (1 : ℝ)) _ hc
  rintro z ⟨x, hx, rfl⟩
  change (1 : ℝ) < x at hx
  refine ⟨neutralDigamma_eulerSeries_ofReal (by linarith), ?_⟩
  simp only [mem_singleton_iff]
  intro h
  have hreal := congrArg Complex.re h
  simp only [Complex.ofReal_re, Complex.one_re] at hreal
  linarith

/-- Actual complex digamma equals the independent Euler candidate on the
whole right half-plane, by analytic uniqueness and the full real anchor. -/
theorem neutralDigamma_eq_eulerSeries {z : ℂ} (hz : 0 < z.re) :
    Complex.digamma z = neutralDigammaEulerSeries z := by
  have ho : IsOpen {w : ℂ | 0 < w.re} :=
    isOpen_lt continuous_const Complex.continuous_re
  have hlin : IsLinearMap ℝ Complex.re :=
    { map_add := Complex.add_re
      map_smul := by intro a w; simp }
  have hc : IsPreconnected {w : ℂ | 0 < w.re} :=
    (convex_halfSpace_gt hlin 0).isPreconnected
  exact (neutralDigamma_rightHalf_differentiableOn.analyticOnNhd ho).eqOn_of_preconnected_of_mem_closure
      (neutralDigamma_eulerSeries_differentiableOn.analyticOnNhd ho)
      hc (by norm_num) neutralDigamma_euler_equality_accumulation hz

/-- Actual right-half-plane Euler representation with a genuine HasSum. -/
theorem neutralDigamma_rightHalf_euler_hasSum {z : ℂ} (hz : 0 < z.re) :
    HasSum (fun n => neutralDigammaEulerTerm n z)
      (Complex.digamma z + (Real.eulerMascheroniConstant : ℂ)) := by
  convert (neutralDigamma_euler_summable hz).hasSum using 1
  rw [neutralDigamma_eq_eulerSeries hz]
  unfold neutralDigammaEulerSeries
  ring

end

end WeilDefect
