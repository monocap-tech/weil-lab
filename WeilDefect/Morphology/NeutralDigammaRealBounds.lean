import WeilDefect.Morphology.NeutralGaussExteriorWeak
import Mathlib.Analysis.SpecialFunctions.Gamma.BohrMollerup
import Mathlib.Analysis.Convex.Deriv

namespace WeilDefect

noncomputable section

open scoped Topology

/-- Derivative of the actual positive-real log Gamma is the real digamma. -/
theorem neutralLogGamma_hasDerivAt {x : ℝ} (hx : 0 < x) :
    HasDerivAt (fun y : ℝ => Real.log (Real.Gamma y))
      (Complex.digamma (x : ℂ)).re x := by
  have hs (m : ℕ) : (x : ℂ) ≠ -(m : ℂ) := by
    intro h
    have hr := congrArg Complex.re h
    simp only [Complex.ofReal_re, Complex.neg_re, Complex.natCast_re] at hr
    have hm : (0 : ℝ) ≤ m := Nat.cast_nonneg m
    linarith
  have hg : HasDerivAt Real.Gamma (deriv Complex.Gamma (x : ℂ)).re x := by
    simpa only [Complex.Gamma_ofReal, Complex.ofReal_re] using
      (Complex.differentiableAt_Gamma (x : ℂ) hs).hasDerivAt.real_of_complex
  have hlog := hg.log (ne_of_gt (Real.Gamma_pos_of_pos hx))
  have heq : (Complex.digamma (x : ℂ)).re =
      (deriv Complex.Gamma (x : ℂ)).re / Real.Gamma x := by
    simp [Complex.digamma_def, logDeriv_apply, Complex.Gamma_ofReal,
      Complex.div_re, Complex.normSq_apply]
  rwa [← heq] at hlog

/-- The Gamma recurrence gives the exact adjacent logarithmic slope. -/
theorem neutralLogGamma_unit_slope {x : ℝ} (hx : 0 < x) :
    slope (fun y : ℝ => Real.log (Real.Gamma y)) x (x+1) = Real.log x := by
  rw [slope_def_field, Real.Gamma_add_one (ne_of_gt hx),
    Real.log_mul (ne_of_gt hx) (ne_of_gt (Real.Gamma_pos_of_pos hx))]
  ring

/-- An independent actual-digamma upper bound from log-convexity. -/
theorem neutralDigamma_real_le_log {x : ℝ} (hx : 0 < x) :
    (Complex.digamma (x : ℂ)).re ≤ Real.log x := by
  have h := Real.convexOn_log_Gamma.le_slope_of_hasDerivAt hx
    (show 0 < x+1 by linarith) (show x < x+1 by linarith)
    (neutralLogGamma_hasDerivAt hx)
  simpa only [Function.comp_def, neutralLogGamma_unit_slope hx] using h

/-- An independent lower bound; the predecessor must remain positive. -/
theorem neutralDigamma_log_sub_one_le {x : ℝ} (hx : 1 < x) :
    Real.log (x-1) ≤ (Complex.digamma (x : ℂ)).re := by
  have hp : 0 < x-1 := by linarith
  have h := Real.convexOn_log_Gamma.slope_le_of_hasDerivAt hp
    (show 0 < x by linarith) (show x-1 < x by linarith)
    (neutralLogGamma_hasDerivAt (by linarith : 0 < x))
  have hs : slope (fun y : ℝ => Real.log (Real.Gamma y)) (x-1) x =
      Real.log (x-1) := by
    convert neutralLogGamma_unit_slope hp using 1 <;> ring
  change slope (fun y : ℝ => Real.log (Real.Gamma y)) (x-1) x ≤ _ at h
  rwa [hs] at h

/-- The exact shifted source symbol at zero frequency has explicit bounds.
This controls its scalar contact value, not its frequency-dependent remainder. -/
theorem neutralShiftedDigammaSymbol_zero_bounds {N : ℕ} (hN : 1 ≤ N) :
    Real.log ((N : ℝ)-3/4) - Real.log Real.pi ≤ (neutralShiftedDigammaSymbol N 0).re ∧
    (neutralShiftedDigammaSymbol N 0).re ≤ Real.log ((N : ℝ)+1/4) - Real.log Real.pi := by
  have hn : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have heq : (neutralShiftedDigammaSymbol N 0).re =
      (Complex.digamma (((N : ℝ)+1/4 : ℝ) : ℂ)).re - Real.log Real.pi := by
    simp [neutralShiftedDigammaSymbol, neutralDigammaLine, add_comm]
  rw [heq]
  have hl := neutralDigamma_log_sub_one_le (x := (N : ℝ)+1/4) (by linarith)
  have hu := neutralDigamma_real_le_log (x := (N : ℝ)+1/4) (by linarith)
  have he : (N : ℝ)+1/4-1 = (N : ℝ)-3/4 := by ring
  rw [he] at hl
  constructor <;> linarith

end

end WeilDefect
