import WeilDefect.Arithmetic.ActualZetaGreenPacketDensity

namespace WeilDefect
noncomputable section
open ContinuousLinearMap InnerProductSpace
open scoped InnerProduct
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false
local instance : DecidableEq NeutralActualZetaDivisorCoordinate := Classical.decEq _

/-- The actual graph inner product keeps the physical logarithmic coordinate
and both full, unnormalized divisor coefficient vectors. -/
theorem neutralActualZetaHilbertSource_inner_coordinates (a : ℝ)
    (f g : NeutralActualZetaHilbertSourceDomain a) :
    inner ℂ f g =
      inner ℂ (neutralActualZetaHilbertSourcePhysical a f)
        (neutralActualZetaHilbertSourcePhysical a g) +
      inner ℂ (neutralActualZetaPositiveAnalysis a (neutralActualZetaHilbertToSource a f))
        (neutralActualZetaPositiveAnalysis a (neutralActualZetaHilbertToSource a g)) +
      inner ℂ (neutralActualZetaNegativeAnalysis a (neutralActualZetaHilbertToSource a f))
        (neutralActualZetaNegativeAnalysis a (neutralActualZetaHilbertToSource a g)) := by
  change inner ℂ f.val g.val =
    inner ℂ f.val.fst g.val.fst +
    inner ℂ f.val.snd.fst g.val.snd.fst +
    inner ℂ f.val.snd.snd g.val.snd.snd
  simp only [WithLp.prod_inner_apply, WithLp.ofLp_fst, WithLp.ofLp_snd, add_assoc]

/-- Concrete packet test, with source coordinates of the same actual unit
Green packet and no discarded negative or multiplicity coordinates. -/
theorem neutralActualZetaGreenPacket_test_coordinates (a : ℝ) (ha : 0 < a)
    (f : NeutralActualZetaHilbertSourceDomain a)
    (q : NeutralActualZetaDivisorCoordinate) :
    inner ℂ f (neutralActualZetaGreenPacketColumn a ha q) =
      inner ℂ (neutralActualZetaHilbertSourcePhysical a f)
        (neutralCanonicalToLogHilbert
          (neutralActualZetaGreenCanonical a ha (lp.single 2 q 1))) +
      inner ℂ (neutralActualZetaPositiveAnalysis a (neutralActualZetaHilbertToSource a f))
        (neutralActualZetaPositiveAnalysis a
          (neutralActualZetaGreenSourceLift a ha (lp.single 2 q 1))) +
      inner ℂ (neutralActualZetaNegativeAnalysis a (neutralActualZetaHilbertToSource a f))
        (neutralActualZetaNegativeAnalysis a
          (neutralActualZetaGreenSourceLift a ha (lp.single 2 q 1))) := by
  rw [neutralActualZetaHilbertSource_inner_coordinates]
  simp only [neutralActualZetaGreenPacketColumn,
    neutralActualZetaGreenHilbertSourcePhysical,
    neutralActualZetaGreenHilbertSourceLift_custody]

/-- Actual bounded graph sampling operator: adjoint of the already proved
bounded Green graph synthesis, rather than an added representation input. -/
def neutralActualZetaGreenGraphAnalysis (a : ℝ) (ha : 0 < a) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  ContinuousLinearMap.adjoint (𝕜 := ℂ)
    (E := NeutralActualZetaGreenCoefficients) (F := NeutralActualZetaHilbertSourceDomain a)
    (neutralActualZetaGreenHilbertSourceContinuous a ha)

theorem neutralActualZetaGreenGraphAnalysis_duality (a : ℝ) (ha : 0 < a)
    (f : NeutralActualZetaHilbertSourceDomain a) (v : NeutralActualZetaGreenCoefficients) :
    inner ℂ (neutralActualZetaGreenGraphAnalysis a ha f) v =
      inner ℂ f (neutralActualZetaGreenHilbertSourceLift a ha v) :=
  (neutralActualZetaGreenHilbertSourceContinuous a ha).adjoint_inner_left v f

/-- The kernel is exactly the orthogonal complement of the certified Green
graph subspace. This theorem does not assert that the kernel is zero. -/
theorem neutralActualZetaGreenGraphAnalysis_ker (a : ℝ) (ha : 0 < a) :
    (neutralActualZetaGreenGraphAnalysis a ha).ker =
      (neutralActualZetaGreenClosedSubmodule a ha).toSubmoduleᗮ := by
  change (ContinuousLinearMap.adjoint (𝕜 := ℂ)
    (E := NeutralActualZetaGreenCoefficients) (F := NeutralActualZetaHilbertSourceDomain a)
    (neutralActualZetaGreenHilbertSourceContinuous a ha)).ker =
      (neutralActualZetaGreenHilbertSourceLinear a ha).range.topologicalClosureᗮ
  rw [Submodule.orthogonal_closure]
  exact (neutralActualZetaGreenHilbertSourceContinuous a ha).orthogonal_range.symm

/-- Vanishing actual graph analysis is equivalent to every concrete packet
test vanishing. It is an exact obstruction, not a density hypothesis. -/
theorem neutralActualZetaGreenGraphAnalysis_eq_zero_iff_packets
    (a : ℝ) (ha : 0 < a) (f : NeutralActualZetaHilbertSourceDomain a) :
    neutralActualZetaGreenGraphAnalysis a ha f = 0 ↔
      ∀ q : NeutralActualZetaDivisorCoordinate,
        inner ℂ f (neutralActualZetaGreenPacketColumn a ha q) = 0 := by
  change f ∈ (neutralActualZetaGreenGraphAnalysis a ha).ker ↔ _
  rw [neutralActualZetaGreenGraphAnalysis_ker, Submodule.mem_orthogonal']
  exact neutralActualZetaGreenGraphClosure_orthogonal_packets_iff a ha f

/-- Membership is exactly orthogonality to all actual graph-analysis kernel
vectors. The retained vector must still satisfy these concrete equations. -/
theorem neutralActualZetaGreenGraphClosure_mem_iff_analysis_kernel
    (a : ℝ) (ha : 0 < a) (f : NeutralActualZetaHilbertSourceDomain a) :
    f ∈ neutralActualZetaGreenGraphClosure a ha ↔
      ∀ g : NeutralActualZetaHilbertSourceDomain a,
        neutralActualZetaGreenGraphAnalysis a ha g = 0 → inner ℂ f g = 0 := by
  have h := (ContinuousLinearMap.adjoint (𝕜 := ℂ)
    (E := NeutralActualZetaGreenCoefficients) (F := NeutralActualZetaHilbertSourceDomain a)
    (neutralActualZetaGreenHilbertSourceContinuous a ha)).orthogonal_ker
  rw [adjoint_adjoint] at h
  change (neutralActualZetaGreenGraphAnalysis a ha).kerᗮ =
    (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule at h
  change f ∈ (neutralActualZetaGreenClosedSubmodule a ha).toSubmodule ↔ _
  rw [← h, Submodule.mem_orthogonal']
  rfl

end
end WeilDefect
