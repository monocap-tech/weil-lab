import WeilDefect.Arithmetic.ActualZetaIV106E19BFullObservation

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap

abbrev neutralIV106E19BH := NeutralLogHilbertCarrier (11/10:ℝ)

/-- Actual response coordinates, with the identical C3C indexing. -/
def neutralIV106E19BResponse (k : ℕ) (hk : 0 < k) :
    neutralIV106E19BH →L[ℂ] (Fin k → ℂ) :=
  ContinuousLinearMap.pi fun i =>
    (ContinuousLinearMap.proj (Sum.inr (Sum.inr (Sum.inr i)) :
      neutralIV106C3Index 665 k)).comp (neutralIV106C3Constraints 665 k hk)

/-- All non-response rows of the terminal kernel, as exact equations. -/
def neutralIV106E19BBase (k : ℕ) (hk : 0 < k) (p : neutralIV106E19BH) : Prop :=
  (∀ i : Fin 665, neutralIV106C3Constraints 665 k hk p (Sum.inl i) = 0) ∧
  neutralIV106C3Constraints 665 k hk p (Sum.inr (Sum.inl ())) = 0 ∧
  (∀ i : Fin k, neutralIV106C3Constraints 665 k hk p
    (Sum.inr (Sum.inr (Sum.inl i))) = 0)

theorem neutralIV106E19BBase_sub (k : ℕ) (hk : 0 < k)
    (p q : neutralIV106E19BH)
    (hp : neutralIV106E19BBase k hk p) (hq : neutralIV106E19BBase k hk q) :
    neutralIV106E19BBase k hk (p-q) := by
  unfold neutralIV106E19BBase at *
  rw [map_sub]
  refine ⟨fun i => ?_, ?_, fun i => ?_⟩
  · change _ - _ = 0
    rw [hp.1 i,hq.1 i,sub_zero]
  · change _ - _ = 0
    rw [hp.2.1,hq.2.1,sub_zero]
  · change _ - _ = 0
    rw [hp.2.2 i,hq.2.2 i,sub_zero]

/-- A right inverse for the actual response rows produces a full-kernel
correction only if its image satisfies every non-response row. This
explicit premise is not implied by an invertible response matrix. -/
theorem neutralIV106E19BKernel_correct (k : ℕ) (hk : 0 < k)
    (Q : (Fin k → ℂ) →ₗ[ℂ] neutralIV106E19BH)
    (hQ : ∀ z, neutralIV106E19BResponse k hk (Q z) = z)
    (hbase : ∀ z, neutralIV106E19BBase k hk (Q z))
    (p : neutralIV106E19BH) (hp : neutralIV106E19BBase k hk p) :
    neutralIV106C3Constraints 665 k hk
      (p-Q (neutralIV106E19BResponse k hk p)) = 0 := by
  let q := p-Q (neutralIV106E19BResponse k hk p)
  have hb := neutralIV106E19BBase_sub k hk p _ hp (hbase _)
  have hr : neutralIV106E19BResponse k hk q = 0 := by
    dsimp only [q]
    rw [map_sub,hQ,sub_self]
  change neutralIV106C3Constraints 665 k hk q = 0
  funext j
  rcases j with i | j
  · exact hb.1 i
  · rcases j with u | j
    · cases u
      exact hb.2.1
    · rcases j with i | i
      · exact hb.2.2 i
      · exact congrFun hr i

#print axioms neutralIV106E19BBase_sub
#print axioms neutralIV106E19BKernel_correct
end
end WeilDefect
