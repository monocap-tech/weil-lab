import WeilDefect.Arithmetic.ActualZetaOriginalJ242Actual67BlockCoverage
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

/-- Fundamental FINITE root budget: at 67 distinct real nodes and one
separate pole, the sum of lower bounds on root multiplicities cannot
exceed the degree of any nonzero real polynomial.

The positive m_g hypothesis forces each specified node into p.roots,
so the multiset root counts can be summed without double counting.
The pole is also a genuine root, and contributes one more count. -/
theorem neutralNF568Distinct67PlusPole_rootCountBound
    (p : Polynomial ℝ) (hp : p ≠ 0)
    (nodes : Fin 67 → ℝ) (hinj : Function.Injective nodes)
    (pole : ℝ) (hsep : ∀ g : Fin 67, nodes g ≠ pole)
    (m : Fin 67 → ℕ) (hmpos : ∀ g, 0 < m g)
    (hroots : ∀ g, m g ≤ Polynomial.rootMultiplicity (nodes g) p)
    (hpole : p.eval pole = 0) :
    (∑ g : Fin 67, m g) + 1 ≤ p.natDegree := by
  classical
  let s : Finset ℝ := Finset.univ.image nodes
  have hpole_not_mem : pole ∉ s := by
    intro hmem
    obtain ⟨g, _, heq⟩ := Finset.mem_image.mp hmem
    exact hsep g heq
  have hpole_mem_roots : pole ∈ p.roots :=
    (Polynomial.mem_roots hp).mpr hpole
  have hpole_count : 1 ≤ p.roots.count pole :=
    Multiset.count_pos.mpr hpole_mem_roots
  have hnodes_count (g : Fin 67) :
      m g ≤ p.roots.count (nodes g) := by
    simpa only [Polynomial.count_roots] using hroots g
  have hnodes_mem_roots (g : Fin 67) : nodes g ∈ p.roots := by
    apply Multiset.count_pos.mp
    exact lt_of_lt_of_le (hmpos g) (hnodes_count g)
  have hsubset : insert pole s ⊆ p.roots.toFinset := by
    intro x hx
    rcases Finset.mem_insert.mp hx with rfl | hx
    · exact Multiset.mem_toFinset.mpr hpole_mem_roots
    · obtain ⟨g, _, rfl⟩ := Finset.mem_image.mp hx
      exact Multiset.mem_toFinset.mpr (hnodes_mem_roots g)
  have hsum : (∑ g : Fin 67, m g) ≤
      ∑ g : Fin 67, p.roots.count (nodes g) :=
    Finset.sum_le_sum (fun g _ => hnodes_count g)
  calc
    (∑ g : Fin 67, m g) + 1 ≤
        (∑ g : Fin 67, p.roots.count (nodes g)) +
          p.roots.count pole :=
      Nat.add_le_add hsum hpole_count
    _ = ∑ x ∈ insert pole s, p.roots.count x := by
      rw [Finset.sum_insert hpole_not_mem]
      rw [Finset.sum_image hinj.injOn]
      omega
    _ ≤ ∑ x ∈ p.roots.toFinset, p.roots.count x := by
      apply Finset.sum_le_sum_of_subset_of_nonneg hsubset
      intro x hx hxnot
      exact Nat.zero_le _
    _ = p.roots.card :=
      Multiset.toFinset_sum_count_eq _
    _ ≤ p.natDegree :=
      Polynomial.card_roots' p

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
