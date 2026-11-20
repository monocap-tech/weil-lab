import Mathlib.Tactic

namespace WeilDefect

/-!
Canonical NF735 (original NF734 Phase-IV branch): typing audit, entirely source-independent.
These are small mathematical interface checks, NOT a proof of global Weil
positivity, not a claim about the actual original zeta quadratic form.

(1) Density + continuity + nonnegativity on the dense carrier WOULD suffice.
(2) Nonnegativity on separate local test directions DOES NOT imply
    nonnegativity on their linear combinations.
-/

/-- The precise abstract extension principle: positivity transfers from
a *dense* set under continuity. Both hypotheses must be discharged in
the intended Weil test-function topology, not in the physical L2 norm
unless its continuity is independently proved. -/
theorem neutralNF734Nonnegative_of_dense_continuous
    {X : Type*} [TopologicalSpace X]
    (Q : X → ℝ) (hQ : Continuous Q)
    (S : Set X) (hS : Dense S)
    (hpos : ∀ x ∈ S, 0 ≤ Q x) :
    ∀ x : X, 0 ≤ Q x := by
  have hc : IsClosed {x : X | 0 ≤ Q x} :=
    isClosed_le continuous_const hQ
  have hs : S ⊆ {x : X | 0 ≤ Q x} := by
    intro x hx
    exact hpos x hx
  have hclose : closure S ⊆ {x : X | 0 ≤ Q x} :=
    closure_minimal hs hc
  intro x
  apply hclose
  rw [hS.closure_eq]
  exact Set.mem_univ x

/-- An explicit real quadratic form, positive on EACH of the two
coordinate axes, but negative on their sum. Thus support-by-support
positivity cannot be glued without mixed Weil-form control. -/
def neutralNF734CrossModel (v : Fin 2 → ℝ) : ℝ :=
  (v 0)^2 + (v 1)^2 - 3 * (v 0) * (v 1)

theorem neutralNF734Cross_left_nonnegative (x : ℝ) :
    0 ≤ neutralNF734CrossModel (fun i => if i = 0 then x else 0) := by
  simpa [neutralNF734CrossModel] using (sq_nonneg x)

theorem neutralNF734Cross_right_nonnegative (y : ℝ) :
    0 ≤ neutralNF734CrossModel (fun i => if i = 1 then y else 0) := by
  simpa [neutralNF734CrossModel] using (sq_nonneg y)

theorem neutralNF734Cross_sum_negative :
    neutralNF734CrossModel (fun _ : Fin 2 => (1 : ℝ)) < 0 := by
  norm_num [neutralNF734CrossModel]

#print axioms neutralNF734Nonnegative_of_dense_continuous
#print axioms neutralNF734Cross_left_nonnegative
#print axioms neutralNF734Cross_right_nonnegative
#print axioms neutralNF734Cross_sum_negative

end WeilDefect
