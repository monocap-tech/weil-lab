import WeilDefect.Arithmetic.ActualZetaSelectedBackground

namespace WeilDefect
noncomputable section
open Filter Topology

/-!
NF529 -- source-graph topology only.

These elementary continuous-operator results work on the COMPLETE actual
two-source graph. They do not assert that any zeta smooth test satisfies
a positive lower bound. The explicit-formula/support-localized input
remains a distinct, uncompiled NF527/NF528 obligation.
-/

/-- The signed two-source quadratic is continuous in the complete graph norm.
No Green-packet density or native Weil multiplier identity is invoked. -/
theorem neutralActualZetaSourceQuadratic_continuous (a : ℝ) :
    Continuous (neutralActualZetaSourceQuadratic a) := by
  have hp : Continuous (fun f : NeutralActualZetaSourceDomain a =>
      ‖neutralActualZetaNormalizedPositiveAnalysis a f‖ ^ 2) :=
    ((continuous_norm.comp
      (neutralActualZetaNormalizedPositiveAnalysis a).continuous).pow 2)
  have hn : Continuous (fun f : NeutralActualZetaSourceDomain a =>
      ‖neutralActualZetaNormalizedNegativeAnalysis a f‖ ^ 2) :=
    ((continuous_norm.comp
      (neutralActualZetaNormalizedNegativeAnalysis a).continuous).pow 2)
  exact hp.sub hn

/-- For any real c, the full-graph superlevel condition Q >= c ||physical||²
is a closed subset. This is a topological transfer theorem, not a new sign
certificate for any individual physical source. -/
theorem neutralActualZetaSourceQuadratic_lower_bound_closed (a c : ℝ) :
    IsClosed {f : NeutralActualZetaSourceDomain a |
      c * ‖neutralActualZetaSourcePhysical a f‖ ^ 2 ≤
        neutralActualZetaSourceQuadratic a f} := by
  have hp : Continuous (fun f : NeutralActualZetaSourceDomain a =>
      ‖neutralActualZetaSourcePhysical a f‖ ^ 2) :=
    ((continuous_norm.comp
      (neutralActualZetaSourcePhysical a).continuous).pow 2)
  exact isClosed_le (continuous_const.mul hp)
    (neutralActualZetaSourceQuadratic_continuous a)

/-- A lower bound on ANY set of source vectors extends unchanged to its
complete graph closure. This isolates the NF528 source-specific limit step. -/
theorem neutralActualZetaSourceQuadratic_lower_bound_closure
    (a c : ℝ) (S : Set (NeutralActualZetaSourceDomain a))
    (hS : ∀ f ∈ S,
      c * ‖neutralActualZetaSourcePhysical a f‖ ^ 2 ≤
        neutralActualZetaSourceQuadratic a f)
    (f : NeutralActualZetaSourceDomain a) (hf : f ∈ closure S) :
    c * ‖neutralActualZetaSourcePhysical a f‖ ^ 2 ≤
      neutralActualZetaSourceQuadratic a f := by
  have hsub : S ⊆ {f : NeutralActualZetaSourceDomain a |
      c * ‖neutralActualZetaSourcePhysical a f‖ ^ 2 ≤
        neutralActualZetaSourceQuadratic a f} := by
    intro g hg
    exact hS g hg
  exact (closure_minimal hsub
    (neutralActualZetaSourceQuadratic_lower_bound_closed a c)) hf

/-- A strictly positive c and nonzero physical coordinate make a closed
lower bound a strictly positive actual signed source quadratic. -/
theorem neutralActualZetaSourceQuadratic_pos_of_physical_nonzero
    (a c : ℝ) (hc : 0 < c) (f : NeutralActualZetaSourceDomain a)
    (hf : c * ‖neutralActualZetaSourcePhysical a f‖ ^ 2 ≤
        neutralActualZetaSourceQuadratic a f)
    (hne : neutralActualZetaSourcePhysical a f ≠ 0) :
    0 < neutralActualZetaSourceQuadratic a f := by
  have hn : 0 < ‖neutralActualZetaSourcePhysical a f‖ :=
    norm_pos_iff.mpr hne
  exact lt_of_lt_of_le (mul_pos hc (sq_pos_of_pos hn)) hf

end
end WeilDefect
