module

public import CP018EightCell
public import Zeta.Gamma.LogGammaBranch

/-!
CP018 genuine ORIGINAL source exact complex-jet interface.

At t>0, the original Hardy-Z definition and the original logGamma
right-half branch imply the following analytic identities (by ordinary
complex and real differentiation):

  s(t) = 1/2 + i t; w(t) = 1/4 + i t/2
  θ'(t) = (Re digamma(w(t)) - log π)/2
  θ''(t) = -Im ((deriv digamma)(w(t))) / 4
  Z'(t) = Re[e^(iθ) i (θ' ζ(s)+ζ'(s))]
  Z''(t)= Re[e^(iθ) (
              -(θ')²ζ(s)-2θ'ζ'(s)-ζ''(s)+i θ''ζ(s))]

IMPORTANT: The ACTUAL source original HardyZ.lean proves only a VALUE
error bound for its Euler-Maclaurin approximant. It does not export
any of these derivative equalities or error enclosures as accepted Lean
theorems. Hence this formal module defines source-exact FORMULAE and
exposes the missing derivative-identity hypothesis explicitly.

The 8 interval-box obligations preserve cancellation within the single
complex expression for Z''. Bounding the separate norms of ζ,ζ',ζ''
naively would generally be too loose to establish curvature <4.

SOURCE mathematical interface candidate only. NO accepted new Lean
kernel evidence, uniform interval boxes, source zeta derivative error
or narrowed zero-existence certificate.
-/

@[expose] public section

open Set

namespace CP018HardyJet

private abbrev a : ℝ := (149500 : ℝ) / 1000
private abbrev b : ℝ := (15005353 : ℝ) / 100000

private noncomputable def s (t : ℝ) : ℂ :=
  1 / 2 + Complex.I * (t : ℂ)

private noncomputable def w (t : ℝ) : ℂ :=
  1 / 4 + Complex.I * ((t : ℂ) / 2)

/-- Exact first derivative of Riemann-Siegel theta, MATHEMATICAL formula.
The formal equality with the original θ'(t) remains an explicit
separate unproved local-source derivative-bridge obligation. -/
noncomputable def thetaPrimeJet (t : ℝ) : ℝ :=
  ((Complex.digamma (w t)).re - Real.log Real.pi) / 2

/-- Exact second derivative of theta by the digamma derivative.
No invented named trigamma theorem is imported. -/
noncomputable def thetaSecondJet (t : ℝ) : ℝ :=
  -((deriv Complex.digamma (w t)).im) / 4

/-- Complex phase from the actual frozen original source Hardy-Z. -/
private noncomputable def phase (t : ℝ) : ℂ :=
  Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ))

/-- The formal source-first complex jet, respecting θ'(t),ζ'(s(t)).
Its equality with actual deriv Zeta.hardyZ needs source chain-rule
certification independently of source VALUE approximant remainder. -/
noncomputable def sourceFirstJet (t : ℝ) : ℝ :=
  (phase t * Complex.I *
    (((thetaPrimeJet t : ℝ) : ℂ) * riemannZeta (s t) +
      deriv riemannZeta (s t))).re

/-- The formal source-second complex jet, retaining phase cancellation
across theta/ζ derivatives before interval enclosure. -/
noncomputable def sourceSecondJet (t : ℝ) : ℝ :=
  (phase t * (
      - (((thetaPrimeJet t : ℝ) : ℂ) ^ 2) * riemannZeta (s t)
      - 2 * ((thetaPrimeJet t : ℝ) : ℂ) * deriv riemannZeta (s t)
      - deriv (deriv riemannZeta) (s t)
      + Complex.I * ((thetaSecondJet t : ℝ) : ℂ) * riemannZeta (s t))).re

/-- A SOURCE-TRUE mathematical interval-box contract with EIGHT
INDEPENDENT whole-cell enclosures. The exact equality Z''=sourceSecondJet
is deliberately an EXPLICIT premise because original published HardyZ
source has only a value-remainder theorem. No unsound differentiation
of a function-value inequality is attempted.

This produces a UNIFORM curvature bound from eight verified interval
enclosures once genuine source derivative-identity and box certificates
are separately available. -/
theorem uniform_curvature_of_eight_source_jet_boxes
    (hidentity :
      ∀ t ∈ Icc a b,
        deriv (deriv Zeta.hardyZ) t = sourceSecondJet t)
    (hboxes :
      ∀ j : Fin 8, ∀ t ∈ Icc a b,
        |t - CP018EightCell.center j| ≤ (b - a) / 16 →
          |sourceSecondJet t| ≤ 4) :
    ∀ t ∈ Icc a b,
      |deriv (deriv Zeta.hardyZ) t| ≤ 4 := by
  intro t ht
  obtain ⟨j, hj⟩ := CP018EightCell.eight_center_cover t ht
  rw [hidentity t ht]
  exact hboxes j t ht (by simpa using hj)

/-- This pins the OTHER derivative target to ONE real scalar analytic
source-jet enclosure, independent of the eight whole-cell curvature
boxes. Actual source first-jet equality remains explicit, not inferred
from the published HardyZ value error bound. -/
theorem genuine_anchor_of_first_jet_certificate
    (hidentity : deriv Zeta.hardyZ a = sourceFirstJet a)
    (hjet_bound : (12 : ℝ) / 5 ≤ sourceFirstJet a) :
    (12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a := by
  rw [hidentity]
  exact hjet_bound

end CP018HardyJet

#print axioms CP018HardyJet.uniform_curvature_of_eight_source_jet_boxes
#print axioms CP018HardyJet.genuine_anchor_of_first_jet_certificate
