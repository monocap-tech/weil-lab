import WeilDefect.Arithmetic.ActualZetaGreenGraphPackets

namespace WeilDefect
noncomputable section
open ContinuousLinearMap InnerProductSpace
open scoped InnerProduct
set_option maxHeartbeats 800000
set_option synthInstance.maxHeartbeats 200000
set_option backward.isDefEq.respectTransparency false
local instance : DecidableEq NeutralActualZetaDivisorCoordinate := Classical.decEq _

/-- Actual unit-coordinate Green packet, with every divisor multiplicity copy
retained as its own index. -/
def neutralActualZetaGreenPacketColumn (a : ℝ) (ha : 0 < a)
    (q : NeutralActualZetaDivisorCoordinate) : NeutralActualZetaHilbertSourceDomain a :=
  neutralActualZetaGreenHilbertSourceLift a ha (lp.single 2 q 1)

/-- Finite linear combinations of the actual packet columns. -/
def neutralActualZetaGreenPacketSpan (a : ℝ) (ha : 0 < a) :
    Submodule ℂ (NeutralActualZetaHilbertSourceDomain a) :=
  Submodule.span ℂ (Set.range (neutralActualZetaGreenPacketColumn a ha))

/-- The closed span uses the full source graph topology. -/
def neutralActualZetaGreenPacketClosedSpan (a : ℝ) (ha : 0 < a) :
    ClosedSubmodule ℂ (NeutralActualZetaHilbertSourceDomain a) :=
  ⟨(neutralActualZetaGreenPacketSpan a ha).topologicalClosure,
    (neutralActualZetaGreenPacketSpan a ha).isClosed_topologicalClosure⟩

theorem neutralActualZetaGreenPacket_single_scalar (a : ℝ) (ha : 0 < a)
    (q : NeutralActualZetaDivisorCoordinate) (c : ℂ) :
    neutralActualZetaGreenHilbertSourceLift a ha (lp.single 2 q c) =
      c • neutralActualZetaGreenPacketColumn a ha q := by
  change (neutralActualZetaGreenHilbertSourceLinear a ha) (lp.single 2 q c) =
    c • (neutralActualZetaGreenHilbertSourceLinear a ha) (lp.single 2 q 1)
  rw [← (neutralActualZetaGreenHilbertSourceLinear a ha).map_smul,
    ← lp.single_smul]
  simp only [smul_eq_mul, mul_one]

/-- The graph-topology packet sum places every actual Green lift in the
closed finite packet span. No full-domain density is assumed. -/
theorem neutralActualZetaGreenHilbertSourceLift_mem_packetClosedSpan
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaGreenHilbertSourceLift a ha v ∈
      neutralActualZetaGreenPacketClosedSpan a ha := by
  rw [← (neutralActualZetaGreenHilbertSource_hasSum_packets a ha v).tsum_eq]
  apply tsum_mem (neutralActualZetaGreenPacketClosedSpan a ha).isClosed
  intro q
  rw [neutralActualZetaGreenPacket_single_scalar]
  apply (neutralActualZetaGreenPacketClosedSpan a ha).toSubmodule.smul_mem
  exact (neutralActualZetaGreenPacketSpan a ha).le_topologicalClosure
    (Submodule.subset_span (Set.mem_range_self q))

/-- Exact equality with the previously certified closed graph subspace,
rather than a density assertion in the entire source graph. -/
theorem neutralActualZetaGreenPacketClosedSpan_eq (a : ℝ) (ha : 0 < a) :
    neutralActualZetaGreenPacketClosedSpan a ha =
      neutralActualZetaGreenClosedSubmodule a ha := by
  apply le_antisymm
  · change (neutralActualZetaGreenPacketSpan a ha).topologicalClosure ≤
      (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule
    apply Submodule.topologicalClosure_minimal
    · apply Submodule.span_le.mpr
      rintro x ⟨q, rfl⟩
      exact neutralActualZetaGreenHilbertSourceLift_mem_closure a ha (lp.single 2 q 1)
    · exact (neutralActualZetaGreenClosedSubmodule a ha).isClosed
  · change (neutralActualZetaGreenHilbertSourceLinear a ha).range.topologicalClosure ≤
      (neutralActualZetaGreenPacketClosedSpan a ha).toSubmodule
    apply Submodule.topologicalClosure_minimal
    · rintro x ⟨v, rfl⟩
      exact neutralActualZetaGreenHilbertSourceLift_mem_packetClosedSpan a ha v
    · exact (neutralActualZetaGreenPacketClosedSpan a ha).isClosed

theorem neutralActualZetaGreenPacketClosedSpan_coe (a : ℝ) (ha : 0 < a) :
    (neutralActualZetaGreenPacketClosedSpan a ha :
      Set (NeutralActualZetaHilbertSourceDomain a)) =
      neutralActualZetaGreenGraphClosure a ha := by
  rw [neutralActualZetaGreenPacketClosedSpan_eq,
    neutralActualZetaGreenClosedSubmodule_coe]

/-- Orthogonality to the full certified Green graph closure is equivalent
to orthogonality to each actual packet column. This gives concrete tests for
its orthogonal complement; it does not prove that complement is zero. -/
theorem neutralActualZetaGreenGraphClosure_orthogonal_packets_iff
    (a : ℝ) (ha : 0 < a) (f : NeutralActualZetaHilbertSourceDomain a) :
    (∀ g ∈ neutralActualZetaGreenGraphClosure a ha, inner ℂ f g = 0) ↔
      (∀ q : NeutralActualZetaDivisorCoordinate,
        inner ℂ f (neutralActualZetaGreenPacketColumn a ha q) = 0) := by
  constructor
  · intro h q
    exact h _ (neutralActualZetaGreenHilbertSourceLift_mem_closure a ha (lp.single 2 q 1))
  · intro h g hg
    have hspan : neutralActualZetaGreenPacketSpan a ha ≤
        (innerSL ℂ f).ker := by
      apply Submodule.span_le.mpr
      rintro x ⟨q, rfl⟩
      exact h q
    have hc : IsClosed ((innerSL ℂ f).ker :
        Set (NeutralActualZetaHilbertSourceDomain a)) :=
      isClosed_eq (innerSL ℂ f).continuous continuous_const
    have hcl := (neutralActualZetaGreenPacketSpan a ha).topologicalClosure_minimal hspan hc
    have hm : g ∈ neutralActualZetaGreenPacketClosedSpan a ha := by
      rw [← neutralActualZetaGreenPacketClosedSpan_coe a ha] at hg
      exact hg
    exact hcl hm

end
end WeilDefect
