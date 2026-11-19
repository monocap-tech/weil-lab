import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMatrixProductReceipts
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedProducts
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLiteralRowProjection

namespace WeilDefect

/-!
NF704: assemble the original integer center cache from bounded receipt
checks.  This is an exact reduction, not a numerical certificate for the
original matrices.  Symmetry of the proposed A is a separate hypothesis,
as are symmetry of H and the complete HD product identities.
-/

/-- A dot-product block can be attached to the global HD gate without
re-evaluating the dot product, once the operand and result projections
have been supplied. -/
theorem neutralNF704HD_of_packed_receipt
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (i : Fin 242) {m : ℕ} (ix : Fin m → Fin 242)
    (x : Fin 242 → ℤ) (Y : Fin m → Fin 242 → ℤ) (z : Fin m → ℤ)
    (hx : x = s.H i)
    (hy : ∀ j, Y j = fun k => s.D k (ix j))
    (hz : ∀ j, z j = c.HD i (ix j))
    (hp : ∀ j, neutralNF626Dot x (Y j) = z j) :
    ∀ j, c.HDGate s i (ix j) = true := by
  intro j
  exact neutralNF681HDGate_of_projection s c i (ix j)
    x (Y j) (z j) hx (hy j) (hz j) (hp j).symm

/-- The packed A receipt is computed with HD column first, so use the
commutativity of the integer dot product to attach to the incumbent gate. -/
theorem neutralNF704Dot_comm (x y : Fin 242 → ℤ) :
    neutralNF626Dot x y = neutralNF626Dot y x := by
  unfold neutralNF626Dot
  apply Finset.sum_congr rfl
  intro k _
  exact mul_comm _ _

theorem neutralNF704A_of_packed_receipt
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (j : Fin 242) {m : ℕ} (ix : Fin m → Fin 242)
    (x : Fin 242 → ℤ) (Y : Fin m → Fin 242 → ℤ) (z : Fin m → ℤ)
    (hx : x = fun k => c.HD k j)
    (hy : ∀ i, Y i = fun k => s.D k (ix i))
    (hz : ∀ i, z i = c.A (ix i) j)
    (hp : ∀ i, neutralNF626Dot x (Y i) = z i) :
    ∀ i, c.AGate s (ix i) j = true := by
  intro i
  exact neutralNF681AGate_of_projection s c (ix i) j
    (Y i) x (z i) (hy i) hx (hz i)
    ((hp i).symm.trans (neutralNF704Dot_comm x (Y i)))

/-- Actual DᵀHD dot products are symmetric if the exact HD identities
hold everywhere and the input center H is symmetric.  The conclusion
does not assume correctness of any proposed A entry. -/
theorem neutralNF704ADot_symm
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hH : ∀ i j, s.H i j = s.H j i)
    (hHD : ∀ i j, c.HD i j =
      neutralNF626Dot (s.H i) (fun k => s.D k j))
    (i j : Fin 242) :
    neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) =
      neutralNF626Dot (fun k => s.D k j) (fun k => c.HD k i) := by
  calc
    neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) =
        ∑ k : Fin 242, ∑ l : Fin 242,
          s.D k i * (s.H k l * s.D l j) := by
      simp_rw [hHD, neutralNF626Dot, Finset.mul_sum]
    _ = ∑ l : Fin 242, ∑ k : Fin 242,
          s.D k i * (s.H k l * s.D l j) := Finset.sum_comm
    _ = ∑ l : Fin 242, ∑ k : Fin 242,
          s.D l j * (s.H l k * s.D k i) := by
      apply Finset.sum_congr rfl
      intro l _
      apply Finset.sum_congr rfl
      intro k _
      rw [hH k l]
      ring
    _ = neutralNF626Dot (fun k => s.D k j) (fun k => c.HD k i) := by
      simp_rw [hHD, neutralNF626Dot, Finset.mul_sum]

/-- Exactly the lower triangle of A suffices.  No upper triangular
product equality is taken on trust. -/
theorem neutralNF704A_of_lower
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hH : ∀ i j, s.H i j = s.H j i)
    (hA : ∀ i j, c.A i j = c.A j i)
    (hHD : ∀ i j, c.HD i j =
      neutralNF626Dot (s.H i) (fun k => s.D k j))
    (hLower : ∀ i j, j.val ≤ i.val →
      c.A i j = neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j)) :
    ∀ i j, c.A i j =
      neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) := by
  intro i j
  by_cases h : j.val ≤ i.val
  · exact hLower i j h
  · have h' : i.val ≤ j.val := by omega
    calc
      c.A i j = c.A j i := hA i j
      _ = neutralNF626Dot (fun k => s.D k j) (fun k => c.HD k i) :=
        hLower j i h'
      _ = neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) :=
        (neutralNF704ADot_symm s c hH hHD i j).symm

/-- Assemble the complete original cache truth from the incumbent
Boolean gates, replacing only the redundant upper A checks by a proof. -/
theorem neutralNF704Cache_of_triangular
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hH : ∀ i j, s.H i j = s.H j i)
    (hA : ∀ i j, c.A i j = c.A j i)
    (hw : s.wCheck = true)
    (hHD : ∀ i j, c.HDGate s i j = true)
    (hLower : ∀ i j, j.val ≤ i.val → c.AGate s i j = true)
    (hVec : ∀ i, c.vectorGate s i = true) :
    c.check s = true := by
  have hHD' : ∀ i j, c.HD i j =
      neutralNF626Dot (s.H i) (fun k => s.D k j) := by
    intro i j
    exact of_decide_eq_true (hHD i j)
  have hLower' : ∀ i j, j.val ≤ i.val →
      c.A i j = neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) := by
    intro i j hij
    exact of_decide_eq_true (hLower i j hij)
  apply neutralNF681CacheCheck_of_valid c s
  refine ⟨?_, hHD', neutralNF704A_of_lower s c hH hA hHD' hLower', ?_⟩
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp hw) j (by simp))
  · intro i
    exact of_decide_eq_true (hVec i)

/-- With matching symmetry on the receipt row and the full payment,
the H-column projection follows algebraically from the H-row projection. -/
theorem neutralNF704OriginalRow_of_symmetric_projection
    (M : NF622Moments) (p q : NF625PaymentData) (i : Fin 242)
    (hp : ∀ j, p.H0 i j = p.H0 j i)
    (hq : ∀ j, q.H0 i j = q.H0 j i)
    (hrow : ∀ j, p.H0 i j = q.H0 i j)
    (hV : ∀ j : Fin 4, p.V0 i j = q.V0 i j)
    (hEH : p.eH = q.eH) (hEV : p.eV = q.eV)
    (hgate : neutralNF674OriginalRowCheck M p i = true) :
    neutralNF674OriginalRowCheck M q i = true := by
  apply neutralNF675OriginalRow_true_of_projection M p q i
    hrow ?_ hV hEH hEV hgate
  intro j
  exact (hp j).symm.trans ((hrow j).trans (hq j))

#print axioms neutralNF704HD_of_packed_receipt
#print axioms neutralNF704Dot_comm
#print axioms neutralNF704A_of_packed_receipt
#print axioms neutralNF704ADot_symm
#print axioms neutralNF704A_of_lower
#print axioms neutralNF704Cache_of_triangular
#print axioms neutralNF704OriginalRow_of_symmetric_projection

end WeilDefect
