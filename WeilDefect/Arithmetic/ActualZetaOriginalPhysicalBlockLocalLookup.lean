import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalShapedBank

namespace WeilDefect

/-! NF691: keep the same mathematical lookup as NF624 but reduce only
the compact index and selected payload chunk. The full array is
still the object of the coverage and mathematical validity theorems. -/

def neutralNF691Read (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) (i : ℕ) : NF624KeyTable :=
  if i<size then neutralNF690Table read payload i else ⟨⟨0,0⟩,#[]⟩

theorem neutralNF691Read_eq (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) (i : ℕ) :
    neutralNF624BankRead (neutralNF690Bank read size payload) i =
      neutralNF691Read read size payload i := by
  by_cases hi : i<size
  · rw [neutralNF690Bank_read read size payload i hi]
    simp [neutralNF691Read,hi]
  · have hb : ¬ i < (neutralNF690Bank read size payload).size := by
      rw [neutralNF690Bank_size]
      exact hi
    simp [neutralNF624BankRead,neutralNF691Read,hi,getElem?_neg,hb]

def neutralNF691Lookup (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) : NF622Moments :=
  fun k n =>
    if k.h=0 ∧ k.f=0 then NF591Rect.realQ (neutralNF617ZeroMoment n) neutralNF616Q
    else
      let t := neutralNF691Read read size payload
        (neutralNF687Index read size k.canonical)
      neutralNF622Restore k n (neutralNF617MomentRead t.rows n).enclosure

theorem neutralNF691Lookup_eq (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) :
    neutralNF624Lookup (neutralNF690Bank read size payload)
      (neutralNF624Index (neutralNF690Bank read size payload)) =
      neutralNF691Lookup read size payload := by
  rw [neutralNF690Bank_index]
  funext k n
  unfold neutralNF624Lookup neutralNF691Lookup
  by_cases hz : k.h=0 ∧ k.f=0
  · simp only [if_pos hz]
  · simp only [if_neg hz, neutralNF691Read_eq]

#print axioms neutralNF691Read_eq
#print axioms neutralNF691Lookup_eq

end WeilDefect
