import WeilDefect.Arithmetic.ActualZetaIV106C3ActualCore
import Mathlib.Topology.Algebra.Module.ContinuousLinearMap.PiProd

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped SchwartzMap InnerProduct ComplexConjugate BigOperators

def neutralIV106C3Cell (a : ℝ) (N : ℕ) (i : Fin N) : Set ℝ :=
  Set.Icc (-a + (i.val : ℝ)*(2*a/(N:ℝ)))
    (-a + ((i.val : ℝ)+1)*(2*a/(N:ℝ)))

def neutralIV106C3CellIndicator (a : ℝ) (N : ℕ) (i : Fin N) : ℝ → ℂ :=
  (neutralIV106C3Cell a N i).indicator (fun _ => (1 : ℂ))

theorem neutralIV106C3Cell_memLp (a : ℝ) (N : ℕ) (i : Fin N) :
    MemLp (neutralIV106C3CellIndicator a N i) 2 volume := by
  unfold neutralIV106C3CellIndicator
  have hm : MeasurableSet (neutralIV106C3Cell a N i) := measurableSet_Icc
  apply (memLp_two_iff_integrable_sq_norm
    (aestronglyMeasurable_const.indicator hm)).mpr
  have hi : IntegrableOn (fun _ : ℝ => (1:ℝ))
      (neutralIV106C3Cell a N i) volume := by
    unfold neutralIV106C3Cell
    exact continuous_const.integrableOn_Icc
  apply (hi.integrable_indicator hm).congr
  filter_upwards [] with x
  by_cases hx : x ∈ neutralIV106C3Cell a N i <;> simp [hx]

def neutralIV106C3CellColumn (a : ℝ) (N : ℕ) (i : Fin N) : RealComplexL2 :=
  (neutralIV106C3Cell_memLp a N i).toLp (neutralIV106C3CellIndicator a N i)

theorem neutralIV106C3Cell_pair (a : ℝ) (N : ℕ) (i : Fin N) (f : RealComplexL2) :
    inner ℂ (neutralIV106C3CellColumn a N i) f =
      ∫ x in neutralIV106C3Cell a N i, f x := by
  rw [L2.inner_def, ← integral_indicator (show MeasurableSet (neutralIV106C3Cell a N i) from measurableSet_Icc)]
  apply integral_congr_ae
  filter_upwards [(neutralIV106C3Cell_memLp a N i).coeFn_toLp] with x hx
  change inner ℂ ((neutralIV106C3Cell_memLp a N i).toLp _ x) (f x) = _
  rw [hx]
  by_cases h : x ∈ neutralIV106C3Cell a N i <;>
    simp [neutralIV106C3CellIndicator, h, RCLike.inner_apply']

def neutralIV106C3PhysicalRow (a : ℝ) (r : RealComplexL2) :
    NeutralLogHilbertCarrier a →L[ℂ] ℂ :=
  (InnerProductSpace.toDual ℂ RealComplexL2 r).comp (neutralLogPhysicalInclusion a)

theorem neutralIV106C3PhysicalRow_eq (a : ℝ) (r : RealComplexL2)
    (q : NeutralLogHilbertCarrier a) :
    neutralIV106C3PhysicalRow a r q = inner ℂ r (neutralLogPhysical q.val) := rfl

abbrev neutralIV106C3Index (N k : ℕ) := Fin N ⊕ (Unit ⊕ (Fin k ⊕ Fin k))

def neutralIV106C3Constraints (N k : ℕ) (hk : 0 < k) :
    NeutralLogHilbertCarrier (11/10:ℝ) →L[ℂ] (neutralIV106C3Index N k → ℂ) :=
  ContinuousLinearMap.pi fun j =>
    match j with
    | .inl i => neutralIV106C3PhysicalRow _ (neutralIV106C3CellColumn (11/10:ℝ) N i)
    | .inr (.inl _) => neutralLogMoment (11/10:ℝ) (1/2) -
        neutralLogMoment (11/10:ℝ) (-(1/2))
    | .inr (.inr (.inl i)) => neutralIV106C3PhysicalRow _
        ((neutralIV100Carrier k hk i).toLp 2 volume)
    | .inr (.inr (.inr i)) => neutralIV106C3PhysicalRow _
        (neutralIV105CResponse k hk i)

theorem neutralIV106C3Constraints_zero_iff (N k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) :
    neutralIV106C3Constraints N k hk q = 0 ↔
      (∀ i : Fin N, (∫ x in neutralIV106C3Cell (11/10:ℝ) N i,
        neutralLogPhysical q.val x) = 0) ∧
      sourceWindowMoment (11/10:ℝ) (1/2) (neutralLogPhysical q.val) =
        sourceWindowMoment (11/10:ℝ) (-(1/2)) (neutralLogPhysical q.val) ∧
      (∀ i : Fin k, inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
        (neutralLogPhysical q.val) = 0) ∧
      (∀ i : Fin k, inner ℂ (neutralIV105CResponse k hk i)
        (neutralLogPhysical q.val) = 0) := by
  constructor
  · intro h
    refine ⟨?_, ?_, ?_, ?_⟩
    · intro i
      have hi := congrFun h (Sum.inl i)
      change neutralIV106C3PhysicalRow _ (neutralIV106C3CellColumn (11/10:ℝ) N i) q = 0 at hi
      rwa [neutralIV106C3PhysicalRow_eq, neutralIV106C3Cell_pair] at hi
    · have hi := congrFun h (Sum.inr (Sum.inl ()))
      change neutralLogMoment (11/10:ℝ) (1/2) q -
        neutralLogMoment (11/10:ℝ) (-(1/2)) q = 0 at hi
      rw [neutralLogMoment_eq, neutralLogMoment_eq] at hi
      exact sub_eq_zero.mp hi
    · intro i
      exact congrFun h (Sum.inr (Sum.inr (Sum.inl i)))
    · intro i
      exact congrFun h (Sum.inr (Sum.inr (Sum.inr i)))
  · rintro ⟨hc,hp,hm,hr⟩
    funext j
    rcases j with i | j
    · change neutralIV106C3PhysicalRow _ (neutralIV106C3CellColumn (11/10:ℝ) N i) q = 0
      rw [neutralIV106C3PhysicalRow_eq, neutralIV106C3Cell_pair, hc i]
    · rcases j with u | j
      · change neutralLogMoment (11/10:ℝ) (1/2) q -
          neutralLogMoment (11/10:ℝ) (-(1/2)) q = 0
        rw [neutralLogMoment_eq, neutralLogMoment_eq, hp, sub_self]
      · rcases j with i | i
        · exact hm i
        · exact hr i

theorem neutralIV106C3Packed_from_rows (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hm : ∀ i : Fin k, inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
      (v.toLp 2 volume) = 0) : neutralIV101MassComplement k hk v := by
  intro c
  rw [neutralIV104Packed_toLp, sum_inner]
  simp only [inner_smul_left, hm, mul_zero, Finset.sum_const_zero]

theorem neutralIV106C3Actual_kernel_closure (N k : ℕ) (hk : 0 < k) :
    closure ((neutralIV106C3Core (11/10:ℝ) : Set (NeutralLogHilbertCarrier (11/10:ℝ))) ∩
      {q | neutralIV106C3Constraints N k hk q = 0}) =
      {q | neutralIV106C3Constraints N k hk q = 0} :=
  neutralIV106C3Closure _ (neutralIV106C3Core_dense _ (by norm_num)) _

#print axioms neutralIV106C3Cell_memLp
#print axioms neutralIV106C3Cell_pair
#print axioms neutralIV106C3PhysicalRow_eq
#print axioms neutralIV106C3Constraints_zero_iff
#print axioms neutralIV106C3Packed_from_rows
#print axioms neutralIV106C3Actual_kernel_closure
end
end WeilDefect
