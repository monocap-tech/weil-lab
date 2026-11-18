import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerCenters

namespace WeilDefect
open Finset

/-! NF641: exact symmetry of the transformed center matrix follows
from the exact integer HD identities and symmetry of H. No symmetry
of HD is asserted. Check only the lower triangle of A and equality
of the proposed upper triangle to its transpose. -/

theorem neutralNF641GramInt_symm (s : NF626ScaledInputs)
    (hH : ∀ k l, s.H k l=s.H l k) (i j : Fin 242) :
    (∑ k, s.D k i*(∑ l, s.H k l*s.D l j)) =
      ∑ k, s.D k j*(∑ l, s.H k l*s.D l i) := by
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro k _
  apply Finset.sum_congr rfl
  intro l _
  rw [hH l k]
  ring

theorem neutralNF641DotHD_symm (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hH : ∀ k l, s.H k l=s.H l k)
    (hHD : ∀ i j, c.HD i j=neutralNF626Dot (s.H i) (fun k => s.D k j))
    (i j : Fin 242) :
    neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) =
      neutralNF626Dot (fun k => s.D k j) (fun k => c.HD k i) := by
  unfold neutralNF626Dot at *
  simp only [hHD]
  exact neutralNF641GramInt_symm s hH i j

def neutralNF641HSymRow (s : NF626ScaledInputs) (i : Fin 242) : Bool :=
  (List.finRange 242).all (fun j => decide (s.H i j=s.H j i))

def neutralNF641AGate (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i j : Fin 242) : Bool :=
  if j.val ≤ i.val then c.AGate s i j
  else decide (c.A i j=c.A j i)

def neutralNF641ARow (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : Bool :=
  (List.finRange 242).all (neutralNF641AGate c s i)

theorem neutralNF641A_of_triangle (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hH : ∀ i j,s.H i j=s.H j i)
    (hHD : ∀ i j,c.HD i j=neutralNF626Dot (s.H i) (fun k => s.D k j))
    (hA : ∀ i,neutralNF641ARow c s i=true) :
    ∀ i j,c.A i j=neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) := by
  have hg (i j : Fin 242) : neutralNF641AGate c s i j=true :=
    (List.all_eq_true.mp (hA i)) j (by simp)
  have hl (i j : Fin 242) (h : j.val ≤ i.val) :
      c.A i j=neutralNF626Dot (fun k => s.D k i) (fun k => c.HD k j) := by
    have hh := hg i j
    simp only [neutralNF641AGate,if_pos h] at hh
    exact of_decide_eq_true hh
  intro i j
  by_cases h : j.val ≤ i.val
  · exact hl i j h
  · have hh := hg i j
    simp only [neutralNF641AGate,if_neg h] at hh
    have he : c.A i j=c.A j i := of_decide_eq_true hh
    rw [he,hl j i (by omega),neutralNF641DotHD_symm c s hH hHD j i]

theorem neutralNF641Cache_of_triangle (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hw : s.wCheck=true)
    (hh : ∀ i,neutralNF641HSymRow s i=true)
    (hd : ∀ i,(List.finRange 242).all (c.HDGate s i)=true)
    (ha : ∀ i,neutralNF641ARow c s i=true)
    (hv : ∀ i,c.vectorGate s i=true) : c.Valid s := by
  have hH (i j : Fin 242) : s.H i j=s.H j i :=
    of_decide_eq_true ((List.all_eq_true.mp (hh i)) j (by simp))
  have hHD (i j : Fin 242) : c.HD i j=neutralNF626Dot (s.H i) (fun k => s.D k j) :=
    of_decide_eq_true ((List.all_eq_true.mp (hd i)) j (by simp))
  refine ⟨?_,hHD,neutralNF641A_of_triangle c s hH hHD ha,?_⟩
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp hw) j (by simp))
  · intro i
    exact of_decide_eq_true (hv i)

end WeilDefect
