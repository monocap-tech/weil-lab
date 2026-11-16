import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Algebra.Polynomial.Degree.Operations
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
NF553 — standalone Hermite polynomial-degree obstruction, and exact real
node separation. These are general algebraic facts toward the ORIGINAL NF552
242 odd-initial-jet source certificate.

Critical boundary: this module does NOT prove that vanishing original
odd jets implies the original 68-node Hermite product divides the
dual degree-<242 polynomial; it is only the generic terminal degree
obstruction once that genuine derivative-to-root-multiplicity bridge is made.

It depends on Mathlib, not on pending NF546-551 source modules.
-/

/-- A nonzero real polynomial of degree strictly below 242 cannot
be divisible by a polynomial whose degree is exactly 242.
This is the final algebraic stop in the dual Hermite certificate. -/
theorem neutralNF553HermiteDegreeObstruction
    (p h : Polynomial ℝ)
    (hsmall : p.natDegree < 242)
    (hfull : h.natDegree = 242)
    (hdiv : h ∣ p) : p = 0 := by
  by_contra hp
  have hbound : h.natDegree ≤ p.natDegree :=
    Polynomial.natDegree_le_of_dvd hdiv hp
  omega

/-- A strictly positive frequency has a strictly positive square node. -/
theorem neutralNF553PositiveSquareNode
    (ω : ℝ) (hω : 0 < ω) : 0 < ω ^ 2 :=
  pow_pos hω 2

/-- Squaring is injective on the strictly positive real frequencies.
The original oscillator source frequencies are all positive. -/
theorem neutralNF553PositiveSquareNodeInjective
    {u v : ℝ} (hu : 0 < u) (hv : 0 < v)
    (h : u ^ 2 = v ^ 2) : u = v := by
  have hprod : (u - v) * (u + v) = 0 := by
    nlinarith [h]
  rcases mul_eq_zero.mp hprod with hdiff | hsum
  · linarith
  · linarith

/-- The genuine sinh pole enters the odd-jet transform at
the NEGATIVE real t-node -1/4. It cannot collide with any
real squared oscillator frequency, including zero. -/
theorem neutralNF553GenuinePoleNodeSeparated
    (ω : ℝ) : ω ^ 2 ≠ -(1 / 4 : ℝ) := by
  intro h
  nlinarith [sq_nonneg ω]

end
end WeilDefect
