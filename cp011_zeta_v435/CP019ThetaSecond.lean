module

public import Zeta.Gram.Averaging
public import Zeta.Gamma.TrigammaDecay
public import CP018HardyJet

/-!
CP019 genuine second theta derivative source theorem candidate.

Original smmercuri/zeta Zeta/Gram/Averaging.lean ALREADY proves
hasDerivAt_riemannSiegelTheta, and original
Zeta/Gamma/TrigammaDecay.lean ALREADY proves the REAL digamma
derivative along the vertical quarter line as a private lemma
inside its monotonicity theorem.

The new proof makes the true second phase derivative explicit and
public: θ''(t) = -Im (ψ'(1/4+it/2))/4 for positive t.
This is an ANALYTIC IDENTITY, not a numerical or interval enclosure,
and remains a NEW Lean SOURCE CANDIDATE until actual v4.35 acceptance.
-/

@[expose] public section

namespace CP019ThetaSecond

open Filter

/-- Actual original complex digamma derivative along the quarter
vertical line, recovered from the original source's TrigammaDecay
proof pattern. No extraneous analytic assumption. -/
theorem hasDerivAt_re_digamma_quarter_vertical (t : ℝ) :
    HasDerivAt
      (fun u : ℝ =>
        (Complex.digamma
          (1 / 4 + Complex.I * ((u : ℂ) / 2))).re)
      (-(1 / 2) *
        (deriv Complex.digamma
          (1 / 4 + Complex.I * ((t : ℂ) / 2))).im) t := by
  have hre :
      0 < (1 / 4 + Complex.I * ((t : ℂ) / 2)).re := by
    simp
  have haff :
      HasDerivAt
        (fun z : ℂ => (1 / 4 : ℂ) + Complex.I * (z / 2))
        (Complex.I * (1 / 2)) (t : ℂ) :=
      (((hasDerivAt_id (t : ℂ)).div_const 2).const_mul Complex.I).const_add
        (1 / 4)
  have hcomp :=
    ((differentiableAt_digamma hre).hasDerivAt.comp (t : ℂ)
      haff).comp_ofReal
  have hg := Complex.reCLM.hasFDerivAt.comp_hasDerivAt t hcomp
  simp only [Complex.reCLM_apply, Function.comp_apply] at hg
  rw [show
    (deriv Complex.digamma (1 / 4 + Complex.I * ((t : ℂ) / 2)) *
      (Complex.I * (1 / 2))).re =
    -(1 / 2) * (deriv Complex.digamma
      (1 / 4 + Complex.I * ((t : ℂ) / 2))).im by
    simp [Complex.mul_re]
    ring] at hg
  exact hg

/-- Actual second derivative of the frozen original
Riemann-Siegel theta function, t>0. -/
theorem original_riemannSiegelTheta_second_deriv
    {t : ℝ} (ht : 0 < t) :
    deriv (deriv riemannSiegelTheta) t =
      -((deriv Complex.digamma
        (1 / 4 + Complex.I * ((t : ℂ) / 2))).im) / 4 := by
  let w : ℂ := 1 / 4 + Complex.I * ((t : ℂ) / 2)
  have hd : HasDerivAt
      (fun u : ℝ =>
        1 / 2 * (Complex.digamma
          (1 / 4 + Complex.I * ((u : ℂ) / 2))).re -
        1 / 2 * Real.log Real.pi)
      (-(1 / 4) * (deriv Complex.digamma w).im) t := by
    convert ((hasDerivAt_re_digamma_quarter_vertical t).const_mul
      (1 / 2 : ℝ)).sub_const (1 / 2 * Real.log Real.pi)
      using 1 <;> simp [w] <;> ring
  have hEq :
      (fun u : ℝ => deriv riemannSiegelTheta u) =ᶠ[nhds t]
      (fun u : ℝ =>
        1 / 2 * (Complex.digamma
          (1 / 4 + Complex.I * ((u : ℂ) / 2))).re -
        1 / 2 * Real.log Real.pi) := by
    filter_upwards [isOpen_Ioi.mem_nhds ht] with u hu
    exact (hasDerivAt_riemannSiegelTheta hu).deriv
  have hReal : HasDerivAt
      (fun u : ℝ => deriv riemannSiegelTheta u)
      (-(1 / 4) * (deriv Complex.digamma w).im) t :=
    hd.congr_of_eventuallyEq hEq.symm
  simpa [w, div_eq_mul_inv] using hReal.deriv

/-- Remove one more original-source CP018 jet equality assumption:
the exact trigamma phase-second-jet formula now coincides with the
true ordinary second derivative of the original theta. -/
theorem original_phase_second_jet_matches_source
    {t : ℝ} (ht : 0 < t) :
    CP018HardyJet.thetaSecondJet t =
      deriv (deriv riemannSiegelTheta) t := by
  rw [original_riemannSiegelTheta_second_deriv ht]
  rfl

end CP019ThetaSecond

#print axioms CP019ThetaSecond.hasDerivAt_re_digamma_quarter_vertical
#print axioms CP019ThetaSecond.original_riemannSiegelTheta_second_deriv
#print axioms CP019ThetaSecond.original_phase_second_jet_matches_source
