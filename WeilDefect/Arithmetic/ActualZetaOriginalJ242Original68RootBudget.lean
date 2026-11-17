import WeilDefect.Arithmetic.ActualZetaOriginalJ242Actual67BlockCoverage
import WeilDefect.Arithmetic.ActualZetaOriginalJ242Generic67PlusPoleRootCount
import WeilDefect.Arithmetic.ActualZetaOriginalJ242DualPolynomialSourceNodes
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF568 — the terminal SIMULTANEOUS 68-node root-count degree obstruction
for the authentic NF407 original 242-dimensional odd-derivative dual.

The old NF567 source-completeness certificate identifies exactly 67
distinct genuine positive squared frequencies t_g=(2*pi*f_g)^2,
their strictly positive historical multiplicities m_g with sum 241,
and the separate actual sinh pole at -1/4.

This file uses *Polynomial.roots*, its multiset root counts and
Mathlib's multiset root-cardinality ≤ natDegree inequality. It does
not silently sum overlapping root multiplicities: injectivity of the
67 source nodes and separation of the pole are explicit hypotheses
to the generic theorem, and proved source facts in the original
application.

The entire 68-node degree obstruction is algebraic and can compile
independently of the pending NF566 *analytic* derivative bridge or
NF550 physical Gram. No original-source independence axiom occurs.
-/

/-- In the frozen ORIGINAL NF407 source, the genuine 67 positive
squared frequencies and the separate genuine -1/4 sinh node impose
a 242-root budget, while the actual original dual has natDegree<242.

The individual multiplicity and pole-root equations are explicit
inputs; the simultaneous degree contradiction itself is CONCLUDED
unconditionally from those inputs. -/
theorem neutralNF568Original68NodeMultiplicityForcesPolynomialZero
    (p : Polynomial ℝ)
    (hdegree : p.natDegree < 242)
    (hgroups : ∀ g : Fin 67,
      (neutralNF567OriginalGroupAt g).2 ≤
        Polynomial.rootMultiplicity
          (neutralNF567OriginalGroupOmega g ^ 2) p)
    (hpole : p.eval (-(1 / 4 : ℝ)) = 0) :
    p = 0 := by
  by_contra hp
  have hbound : (∑ g : Fin 67, (neutralNF567OriginalGroupAt g).2) + 1 ≤
      p.natDegree :=
    neutralNF568Distinct67PlusPole_rootCountBound
      p hp
      (fun g : Fin 67 => neutralNF567OriginalGroupOmega g ^ 2)
      neutralNF567OriginalGroupSquaredOmega_injective
      (-(1 / 4 : ℝ))
      neutralNF567OriginalGroupSquaredOmega_ne_sinhPole
      (fun g : Fin 67 => (neutralNF567OriginalGroupAt g).2)
      neutralNF567OriginalGroupAt_multiplicity_pos
      hgroups hpole
  rw [neutralNF567OriginalAll67GroupMultiplicities_sum] at hbound
  omega

/-- Instantiation at the EXACT 242-coefficient signed dual
p_a of the original analytic NF407 J242 generator list.

Provided all 67 authentic squared-frequency multiplicity
bounds plus the real sinh negative-node root, p_a=0.
No source uniqueness, Gram positivity or RH is assumed here. -/
theorem neutralNF568OriginalDual68Roots_forcesZero
    (a : Fin 242 → ℝ)
    (hgroups : ∀ g : Fin 67,
      (neutralNF567OriginalGroupAt g).2 ≤
        Polynomial.rootMultiplicity
          (neutralNF567OriginalGroupOmega g ^ 2)
          (neutralNF557OriginalDualPolynomial a))
    (hpole : (neutralNF557OriginalDualPolynomial a).eval
      (-(1 / 4 : ℝ)) = 0) :
    neutralNF557OriginalDualPolynomial a = 0 :=
  neutralNF568Original68NodeMultiplicityForcesPolynomialZero
    (neutralNF557OriginalDualPolynomial a)
    (neutralNF557OriginalDualPolynomial_natDegree_lt a)
    hgroups hpole

end
end WeilDefect
