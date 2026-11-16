import WeilDefect.Arithmetic.ActualZetaOriginalJ242QuadraticRootFactor
import Mathlib.Algebra.Polynomial.RingDivision

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF556 — exact quadratic root multiplicity transfer for the original
NF407 odd-source 68-node Hermite reduction.

The ORIGINAL odd-derivative dual is F(X)=X*p(X^2). For every real
positive oscillator ω, the root multiplicity of F at ω equals that
of p at ω^2. The proof factors the actual polynomial at the root,
uses the independently compiled NF555 quadratic factor and nonzero
cofactor, and invokes Mathlib's rootMultiplicity_mul.

This is a GENERIC polynomial theorem; the source-specific odd-jet
derivative bridge, 67-node product divisor, complex independence and
canonical weighted Gram positivity remain separate formal obligations.
-/

/-- A positive-frequency original odd-dual cofactor contributes no
additional root multiplicity at the oscillator's positive root. -/
theorem neutralNF556OriginalDualQuadraticSplitMultiplicity
    (ω : ℝ) (hω : 0 < ω) (q : Polynomial ℝ) (r : ℕ)
    (hq : eval (ω ^ 2) q ≠ 0) :
    rootMultiplicity ω
      ((X - C ω) ^ r * (X * (X + C ω) ^ r * q.comp (X ^ 2))) = r := by
  have hco : eval ω
      (X * (X + C ω) ^ r * q.comp (X ^ 2)) ≠ 0 :=
    neutralNF555OriginalDualQuadraticCofactor_nonzero ω hω q r hq
  have hnotroot :
      ¬ (X * (X + C ω) ^ r * q.comp (X ^ 2)).IsRoot ω := by
    exact hco
  have hcozero :
      rootMultiplicity ω (X * (X + C ω) ^ r * q.comp (X ^ 2)) = 0 :=
    Polynomial.rootMultiplicity_eq_zero hnotroot
  have hfactor :
      ((X : Polynomial ℝ) - C ω) ^ r ≠ 0 := by
    exact pow_ne_zero _ (Polynomial.X_sub_C_ne_zero ω)
  have hcoPoly :
      (X * (X + C ω) ^ r * q.comp (X ^ 2)) ≠ 0 := by
    intro heq
    exact hco (by simp [heq])
  have hwhole :
      ((X - C ω) ^ r * (X * (X + C ω) ^ r * q.comp (X ^ 2))) ≠ 0 :=
    mul_ne_zero hfactor hcoPoly
  rw [Polynomial.rootMultiplicity_mul hwhole,
    Polynomial.rootMultiplicity_X_sub_C_pow, hcozero]
  omega

/-- EXACT generic 68-node source bridge:
For ω>0 and p≠0, root multiplicity of the original odd-source
polynomial X*p(X²) at ω agrees with root multiplicity of p at
the original squared oscillator node ω².

No hypothetical source independence, numeric Gram or special
value of π is used. -/
theorem neutralNF556OriginalDualQuadraticRootMultiplicity
    (p : Polynomial ℝ) (hp : p ≠ 0) (ω : ℝ) (hω : 0 < ω) :
    rootMultiplicity ω (X * p.comp (X ^ 2)) =
      rootMultiplicity (ω ^ 2) p := by
  obtain ⟨q, hpq, hnotdiv⟩ :=
    Polynomial.exists_eq_pow_rootMultiplicity_mul_and_not_dvd p hp (ω ^ 2)
  have hq : eval (ω ^ 2) q ≠ 0 := by
    intro hzero
    apply hnotdiv
    exact Polynomial.dvd_iff_isRoot.mpr hzero
  have hfirst :
      (X : Polynomial ℝ) * p.comp (X ^ 2) =
        X * (((X - C (ω ^ 2)) ^ rootMultiplicity (ω ^ 2) p * q).comp
          (X ^ 2)) :=
    congrArg (fun v : Polynomial ℝ => X * v.comp (X ^ 2)) hpq
  have hsplit :
      (X : Polynomial ℝ) * p.comp (X ^ 2) =
      (X - C ω) ^ rootMultiplicity (ω ^ 2) p *
        (X * (X + C ω) ^ rootMultiplicity (ω ^ 2) p * q.comp (X ^ 2)) := by
    exact hfirst.trans
      (neutralNF555OriginalDualQuadraticFactorization
        ω q (rootMultiplicity (ω ^ 2) p))
  rw [hsplit]
  exact neutralNF556OriginalDualQuadraticSplitMultiplicity
    ω hω q (rootMultiplicity (ω ^ 2) p) hq

end
end WeilDefect
