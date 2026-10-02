import WeilDefect.Morphology.NeutralDigammaRealAnchor
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.Topology.Algebra.InfiniteSum.Module

namespace WeilDefect

noncomputable section

open scoped BigOperators

/-- Uniqueness after restricting actual complex Gamma to the real axis. -/
theorem neutralGamma_deriv_ofReal {x : ℝ} (hx : 0 < x) :
    deriv Complex.Gamma (x : ℂ) = ((deriv Real.Gamma x : ℝ) : ℂ) := by
  have hc := (Complex.differentiableAt_Gamma (x : ℂ)
    (neutralPositiveReal_ne_neg_nat hx)).hasDerivAt.comp_ofReal
  have hr := (Real.differentiableAt_Gamma (s := x) (fun n => by
    have hn : (0 : ℝ) ≤ n := Nat.cast_nonneg n
    linarith)).hasDerivAt.ofReal_comp
  have hc' : HasDerivAt (fun y : ℝ => (Real.Gamma y : ℂ))
      (deriv Complex.Gamma (x : ℂ)) x := by
    simpa only [Complex.Gamma_ofReal] using hc
  exact hc'.unique hr

/-- Actual digamma is the real Gamma logarithmic derivative at x>0. -/
theorem neutralDigamma_ofReal_eq_real_quotient {x : ℝ} (hx : 0 < x) :
    Complex.digamma (x : ℂ) = (deriv Real.Gamma x / Real.Gamma x : ℝ) := by
  rw [Complex.digamma_def, logDeriv_apply, neutralGamma_deriv_ofReal hx,
    Complex.Gamma_ofReal, Complex.ofReal_div]

/-- The imaginary part vanishes by actual derivative comparison. -/
theorem neutralDigamma_ofReal_im_zero {x : ℝ} (hx : 0 < x) :
    (Complex.digamma (x : ℂ)).im = 0 := by
  rw [neutralDigamma_ofReal_eq_real_quotient hx]
  exact Complex.ofReal_im _

theorem neutralDigamma_ofReal_eq_re {x : ℝ} (hx : 0 < x) :
    Complex.digamma (x : ℂ) = ((Complex.digamma (x : ℂ)).re : ℂ) := by
  apply Complex.ext
  · simp
  · simp [neutralDigamma_ofReal_im_zero hx]

/-- Full complex HasSum on the positive real axis. This supplies equality,
not just equality of real parts, for a later complex identity theorem. -/
theorem neutralDigamma_ofReal_euler_hasSum {x : ℝ} (hx : 0 < x) :
    HasSum (fun n : ℕ => (1 : ℂ) / ((n : ℂ)+1) - 1 / ((x : ℂ)+(n : ℂ)))
      (Complex.digamma (x : ℂ) + (Real.eulerMascheroniConstant : ℂ)) := by
  have h := (neutralDigamma_real_euler_hasSum hx).mapL Complex.ofRealCLM
  rw [neutralDigamma_ofReal_eq_re hx]
  simpa only [Complex.ofRealCLM_apply, Complex.ofReal_add, Complex.ofReal_sub,
    Complex.ofReal_div, Complex.ofReal_natCast, Complex.ofReal_one] using h

/-- Actual full complex Euler-series anchor at every positive real point. -/
theorem neutralDigamma_ofReal_eq_complex_euler_series {x : ℝ} (hx : 0 < x) :
    Complex.digamma (x : ℂ) = -(Real.eulerMascheroniConstant : ℂ) +
      ∑' n : ℕ, ((1 : ℂ) / ((n : ℂ)+1) - 1 / ((x : ℂ)+(n : ℂ))) := by
  rw [(neutralDigamma_ofReal_euler_hasSum hx).tsum_eq]
  ring

end

end WeilDefect
