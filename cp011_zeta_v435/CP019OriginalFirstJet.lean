module

public import Zeta.Gram.Averaging
public import CP018HardyJet
public import Mathlib.Analysis.Complex.RealDeriv

/-!
CP019: reuse the ACTUALLY PUBLISHED original theta derivative rather than
reconstructing it from the original theta value approximation.

Primary source:
  smmercuri/zeta@c06b4e.../Zeta/Gram/Averaging.lean
  actual kernel-source theorem hasDerivAt_riemannSiegelTheta
  θ'(t) = (Re digamma(1/4+it/2) - log π)/2, t>0.

This new module derives a genuine FIRST DERIVATIVE of the actual source
Zeta.hardyZ by the ORIGINAL θ derivative + complex zeta holomorphy and
complex/real chain rules. This is source theory, not a numerical error
enclosure and is NOT NEW LEAN KERNEL ACCEPTED until real 4.35 compile.

The SECOND derivative identity, CP018 complex jet interval boxes, and
actual numerical root #53 remain separate obligations.
-/

@[expose] public section

namespace CP019OriginalFirstJet

open Set

/-- Original published Riemann-Siegel theta derivative, re-expressed
in the exact scalar shape used by CP018. This reuses
hasDerivAt_riemannSiegelTheta and does NOT differentiate a value bound. -/
theorem original_theta_deriv_eq_digamma {t : ℝ} (ht : 0 < t) :
    deriv riemannSiegelTheta t =
      ((Complex.digamma (1 / 4 + Complex.I * ((t : ℂ) / 2))).re -
        Real.log Real.pi) / 2 := by
  rw [(hasDerivAt_riemannSiegelTheta ht).deriv]
  ring

/-- Entire original source first Hardy Z derivative:
Z'(t)=Re(e^(iθ(t)) i [θ'(t)ζ(1/2+it)+ζ'(1/2+it)]), for t>0.
No theta / zeta / EM numerical approximation is used in the proof.

This is a new Lean SOURCE CANDIDATE pending original 4.35 compilation,
though all referenced original upstream foundational derivatives exist. -/
theorem original_hardyZ_hasDerivAt_first_source_jet {t : ℝ} (ht : 0 < t) :
    HasDerivAt Zeta.hardyZ
      ((Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ)) *
        Complex.I *
        (((((Complex.digamma (1 / 4 + Complex.I * ((t : ℂ) / 2))).re -
          Real.log Real.pi) / 2 : ℝ) : ℂ)
          * riemannZeta (1 / 2 + Complex.I * (t : ℂ))
          + deriv riemannZeta (1 / 2 + Complex.I * (t : ℂ)))).re) t := by
  let dθ : ℝ :=
    ((Complex.digamma (1 / 4 + Complex.I * ((t : ℂ) / 2))).re -
      Real.log Real.pi) / 2
  have htheta : HasDerivAt riemannSiegelTheta dθ t := by
    convert hasDerivAt_riemannSiegelTheta ht using 1 <;> simp [dθ] <;> ring
  have hthetaC :
      HasDerivAt (fun u : ℝ => (riemannSiegelTheta u : ℂ)) (dθ : ℂ) t :=
    htheta.ofReal_comp
  have hphase :
      HasDerivAt
        (fun u : ℝ =>
          Complex.exp (Complex.I * (riemannSiegelTheta u : ℂ)))
        (Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ)) *
          (Complex.I * (dθ : ℂ))) t := by
    simpa using (hthetaC.const_mul Complex.I).cexp
  have hne : (1 / 2 + Complex.I * (t : ℂ)) ≠ (1 : ℂ) := by
    intro h
    have hreal := congrArg Complex.re h
    norm_num at hreal
  have hline : HasDerivAt
      (fun u : ℂ => (1 / 2 : ℂ) + Complex.I * u)
      Complex.I (t : ℂ) := by
    simpa using
      (((hasDerivAt_id (t : ℂ)).const_mul Complex.I).const_add (1 / 2 : ℂ))
  have hzetaC :
      HasDerivAt
        (fun u : ℂ => riemannZeta (1 / 2 + Complex.I * u))
        (deriv riemannZeta (1 / 2 + Complex.I * (t : ℂ)) * Complex.I)
        (t : ℂ) :=
    (differentiableAt_riemannZeta hne).hasDerivAt.comp (t : ℂ) hline
  have hzeta :
      HasDerivAt
        (fun u : ℝ => riemannZeta (1 / 2 + Complex.I * (u : ℂ)))
        (deriv riemannZeta (1 / 2 + Complex.I * (t : ℂ)) * Complex.I) t :=
    hzetaC.comp_ofReal
  have hprod := hphase.mul hzeta
  have hre := Complex.reCLM.hasFDerivAt.comp_hasDerivAt t hprod
  simp only [Complex.reCLM_apply, Function.comp_apply] at hre
  have hring :
      Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ)) *
          (Complex.I * (dθ : ℂ)) *
          riemannZeta (1 / 2 + Complex.I * (t : ℂ))
        + Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ)) *
          (deriv riemannZeta (1 / 2 + Complex.I * (t : ℂ)) * Complex.I)
      =
      Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ)) *
        Complex.I *
        ((dθ : ℂ) * riemannZeta (1 / 2 + Complex.I * (t : ℂ)) +
          deriv riemannZeta (1 / 2 + Complex.I * (t : ℂ))) := by
    ring
  rw [hring] at hre
  simpa [Zeta.hardyZ, dθ] using hre

/-- Actual first original Hardy-Z derivative formula with no new
analytic hypothesis; the complex jet equality follows from original
theta differentiability and original holomorphic zeta. -/
theorem original_hardyZ_deriv_eq_first_source_jet {t : ℝ} (ht : 0 < t) :
    deriv Zeta.hardyZ t =
      ((Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ)) *
        Complex.I *
        (((((Complex.digamma (1 / 4 + Complex.I * ((t : ℂ) / 2))).re -
          Real.log Real.pi) / 2 : ℝ) : ℂ)
          * riemannZeta (1 / 2 + Complex.I * (t : ℂ))
          + deriv riemannZeta (1 / 2 + Complex.I * (t : ℂ)))).re) :=
  (original_hardyZ_hasDerivAt_first_source_jet ht).deriv

end CP019OriginalFirstJet

#print axioms CP019OriginalFirstJet.original_theta_deriv_eq_digamma
#print axioms CP019OriginalFirstJet.original_hardyZ_hasDerivAt_first_source_jet
#print axioms CP019OriginalFirstJet.original_hardyZ_deriv_eq_first_source_jet
