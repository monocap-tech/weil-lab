import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF554 — isolate the actual characteristic-zero polynomial Hermite
multiplicity theorem required by the NF553 dual proof.

This uses Mathlib's existing iterated-derivative/root-multiplicity
theorem rather than implementing or assuming a 242x242 determinant.
The difficult ORIGINAL source bridge remains: zero odd jets of all
real NF407 generators must imply these formal derivative vanishings
for the 68-node dual polynomial (at positive squared-frequency nodes
and the genuine negative pole).

No original-source global independence theorem is asserted here.
-/

/-- In characteristic zero, vanishing of the first m formal polynomial
derivatives at t forces root multiplicity at least m, provided p≠0.
This is the algebraic Hermite-jet gate for *every* positive oscillator
node in the unchanged NF407 242-dimensional source. -/
theorem neutralNF554HermiteRootMultiplicity_of_vanishingJets
    (p : Polynomial ℝ) (t : ℝ) (m : ℕ)
    (hp : p ≠ 0)
    (hjets : ∀ k : ℕ, k < m →
      ((⇑(Polynomial.derivative : Polynomial ℝ →ₗ[ℝ] Polynomial ℝ))^[k] p).IsRoot t) :
    m ≤ Polynomial.rootMultiplicity t p := by
  by_cases hm : m = 0
  · simp [hm]
  · have hmpos : 0 < m := Nat.pos_of_ne_zero hm
    have hroot :
        ∀ k ≤ m - 1,
          ((⇑(Polynomial.derivative : Polynomial ℝ →ₗ[ℝ] Polynomial ℝ))^[k] p).IsRoot t := by
      intro k hk
      exact hjets k (by omega)
    have hlt :
        m - 1 < Polynomial.rootMultiplicity t p :=
      Polynomial.lt_rootMultiplicity_of_isRoot_iterate_derivative hp hroot
    omega

/-- A polynomial vanishing in all formal derivatives through order m
cannot be nonzero if its root multiplicity is known to be below m.
This is the contrapositive certificate useful for source audits. -/
theorem neutralNF554HermiteRootMultiplicity_contra
    (p : Polynomial ℝ) (t : ℝ) (m : ℕ)
    (hsmall : Polynomial.rootMultiplicity t p < m)
    (hjets : ∀ k : ℕ, k < m →
      ((⇑(Polynomial.derivative : Polynomial ℝ →ₗ[ℝ] Polynomial ℝ))^[k] p).IsRoot t) :
    p = 0 := by
  by_contra hp
  have hroot := neutralNF554HermiteRootMultiplicity_of_vanishingJets
    p t m hp hjets
  omega

end
end WeilDefect
