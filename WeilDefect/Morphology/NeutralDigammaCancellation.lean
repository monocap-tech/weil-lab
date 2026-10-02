import WeilDefect.Morphology.NeutralDigammaEulerIdentity

namespace WeilDefect

noncomputable section

open Filter MeasureTheory
open scoped BigOperators Topology SchwartzMap

/-- Actual Euler representation on the source line, mapped to real parts. -/
theorem neutralDigammaLine_real_euler_hasSum (t : ℝ) :
    HasSum (fun n : ℕ => 1 / ((n : ℝ)+1) - neutralGaussReciprocal n t)
      ((Complex.digamma (neutralDigammaLine t)).re + Real.eulerMascheroniConstant) := by
  have hz : 0 < (neutralDigammaLine t).re := by simp [neutralDigammaLine]
  have h := (neutralDigamma_rightHalf_euler_hasSum hz).mapL Complex.reCLM
  have ht : ∀ n : ℕ, (neutralDigammaEulerTerm n (neutralDigammaLine t)).re =
      1 / ((n : ℝ)+1) - neutralGaussReciprocal n t := by
    intro n
    unfold neutralDigammaEulerTerm
    rw [Complex.sub_re, one_div, one_div, neutralDigammaLine_inv_re]
    congr 1
    rw [← Complex.ofReal_natCast, ← Complex.ofReal_one, ← Complex.ofReal_add,
      ← Complex.ofReal_inv, Complex.ofReal_re, one_div]
  simpa only [Complex.reCLM_apply, ht, Complex.add_re, Complex.ofReal_re] using h

/-- Zero-frequency subtraction cancels the Euler regularization exactly. -/
theorem neutralDigammaLine_centered_reciprocal_hasSum (t : ℝ) :
    HasSum (fun n : ℕ => neutralGaussReciprocal n t - neutralGaussReciprocal n 0)
      ((Complex.digamma (neutralDigammaLine 0)).re -
        (Complex.digamma (neutralDigammaLine t)).re) := by
  have h := (neutralDigammaLine_real_euler_hasSum 0).sub
    (neutralDigammaLine_real_euler_hasSum t)
  convert h using 1
  · funext n
    ring
  · ring

/-- The certified actual increment series cancels the initial centered value. -/
theorem neutralCenteredDigammaSymbol_step_hasSum_neg_initial (ξ : ℝ) :
    HasSum (fun n : ℕ => neutralCenteredDigammaSymbol (n+1) ξ -
      neutralCenteredDigammaSymbol n ξ) (-neutralCenteredDigammaSymbol 0 ξ) := by
  have h := (neutralDigammaLine_centered_reciprocal_hasSum (2*Real.pi*ξ)).mapL
    Complex.ofRealCLM
  simp only [Complex.ofRealCLM_apply] at h
  simp_rw [neutralCenteredDigammaSymbol_step]
  convert h using 1
  unfold neutralCenteredDigammaSymbol neutralShiftedDigammaSymbol
  simp only [Nat.cast_zero, add_zero, mul_zero, Complex.ofReal_sub]
  ring

/-- Actual pointwise residual cancellation; no representation premise remains. -/
theorem neutralCenteredDigammaLimit_zero (ξ : ℝ) :
    neutralCenteredDigammaLimit ξ = 0 := by
  unfold neutralCenteredDigammaLimit
  rw [(neutralCenteredDigammaSymbol_step_hasSum_neg_initial ξ).tsum_eq]
  ring

theorem neutralCenteredDigammaSymbol_tendsto_zero (ξ : ℝ) :
    Tendsto (fun N : ℕ => neutralCenteredDigammaSymbol N ξ) atTop (𝓝 0) :=
  (neutralCenteredDigammaSymbol_zero_limit_iff ξ).mpr
    (neutralCenteredDigammaLimit_zero ξ)

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The represented residual pairing is zero on every Schwartz test. -/
theorem neutralCenteredDigammaResidualPairing_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) : neutralCenteredDigammaResidualPairing carrier u = 0 := by
  simp [neutralCenteredDigammaResidualPairing, neutralCenteredDigammaLimit_zero]

/-- Zero convergence of the actual action, consuming the certified dominated
pairing transfer. Its existing full-symbol growth premise is retained. -/
theorem neutralCenteredDigammaAction_tendsto_zero
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) :
    Tendsto (fun N : ℕ => TemperedDistribution.fourierMultiplierCLM ℂ
      (neutralCenteredDigammaSymbol N) carrier.temperedMode u) atTop (𝓝 0) := by
  simpa only [neutralCenteredDigammaResidualPairing_zero] using
    neutralCenteredDigammaAction_residual_tendsto carrier a hSymbol u

end

end WeilDefect
