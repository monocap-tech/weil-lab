import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBlockLocalCoverage

namespace WeilDefect

/-! NF690: bank shape is enforced by its constructor, independently
of proof of the actual numerical payload. Padding cannot certify a
moment: every analytic table theorem remains required. -/

def neutralNF690FitRows (n : ℕ) (rows : Array NF617MomentRow) :
    Array NF617MomentRow :=
  Array.ofFn (fun j : Fin n => neutralNF617MomentRead rows j.val)

def neutralNF690Table (read : ℕ → NF687Shape)
    (payload : ℕ → Array NF617MomentRow) (i : ℕ) : NF624KeyTable :=
  ⟨(read i).1, neutralNF690FitRows (read i).2 (payload i)⟩

def neutralNF690Bank (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) : Array NF624KeyTable :=
  Array.ofFn (fun i : Fin size => neutralNF690Table read payload i.val)

theorem neutralNF690FitRows_size (n : ℕ) (rows : Array NF617MomentRow) :
    (neutralNF690FitRows n rows).size = n := by
  simp [neutralNF690FitRows]

theorem neutralNF690FitRows_eq (n : ℕ) (rows : Array NF617MomentRow)
    (h : rows.size = n) : neutralNF690FitRows n rows = rows := by
  apply Array.ext
  · simp [neutralNF690FitRows, h]
  · intro i hi hj
    simp [neutralNF690FitRows, neutralNF617MomentRead,
      Array.getElem?_eq_getElem, hj]

theorem neutralNF690Bank_size (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) :
    (neutralNF690Bank read size payload).size = size := by
  simp [neutralNF690Bank]

theorem neutralNF690Bank_read (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) (i : ℕ) (hi : i < size) :
    neutralNF624BankRead (neutralNF690Bank read size payload) i =
      neutralNF690Table read payload i := by
  have hb : i < (neutralNF690Bank read size payload).size := by
    simpa [neutralNF690Bank_size] using hi
  unfold neutralNF624BankRead
  rw [Array.getElem?_eq_getElem hb]
  simp [neutralNF690Bank]

theorem neutralNF690Bank_shape (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) (i : ℕ) (hi : i<size) :
    neutralNF627ShapeAt (neutralNF690Bank read size payload) i = read i := by
  unfold neutralNF627ShapeAt
  rw [neutralNF690Bank_read read size payload i hi]
  simp [neutralNF690Table, neutralNF690FitRows_size]

theorem neutralNF690Bank_index (read : ℕ → NF687Shape) (size : ℕ)
    (payload : ℕ → Array NF617MomentRow) :
    neutralNF624Index (neutralNF690Bank read size payload) =
      neutralNF687Index read size :=
  neutralNF687Index_eq _ _ _ (neutralNF690Bank_size read size payload)
    (neutralNF690Bank_shape read size payload)

/-- Do not silently identify different numerical rows merely because
their key and length match. The analytic receipt transfers only
when the full literal row array and the actual key agree. -/
theorem neutralNF690Table_eq (read : ℕ → NF687Shape)
    (payload : ℕ → Array NF617MomentRow) (i : ℕ)
    (t : NF624KeyTable)
    (hk : (read i).1 = t.key) (hr : payload i = t.rows)
    (hn : (read i).2 = t.rows.size) :
    neutralNF690Table read payload i = t := by
  cases t with
  | mk k rows =>
    unfold neutralNF690Table
    change (read i).1 = k at hk
    change payload i = rows at hr
    change (read i).2 = rows.size at hn
    rw [hk,hr,neutralNF690FitRows_eq _ _ hn.symm]

noncomputable section

/-- Accept the exact mathematical conclusion of the already certified
NF648 local table route. This does not assert a reference Boolean. -/
def neutralNF690TableSound (t : NF624KeyTable) : Prop :=
  ∀ n : ℕ, n < t.rows.size →
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) t.key.value n -
      (neutralNF617MomentRead t.rows n).value‖ ≤
      (neutralNF617MomentRead t.rows n).rad

theorem neutralNF690Lookup_sound (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ)
    (hbank : ∀ i < bank.size, neutralNF690TableSound (neutralNF624BankRead bank i))
    (k : NF616Frequency) (n : ℕ)
    (hc : neutralNF624LookupCheck bank idx k n = true) :
    (neutralNF624Lookup bank idx k n).Contains (neutralNF620J k.value n) := by
  by_cases hz : k.h=0 ∧ k.f=0
  · have he : k.value=0 := k.zero_value hz.1 hz.2
    rw [he]
    simp only [neutralNF624Lookup,if_pos hz]
    exact neutralNF622ZeroMoment_sound n neutralNF616Q neutralNF616Q_pos
  · let i := idx k.canonical
    let t := neutralNF624BankRead bank i
    have hvalid : i<bank.size ∧ t.key=k.canonical ∧ n<t.rows.size := by
      unfold neutralNF624LookupCheck at hc
      rw [if_neg hz] at hc
      exact of_decide_eq_true hc
    have h := hbank i hvalid.1 n hvalid.2.2
    have h' := NF617MomentRow.enclosure_sound _ _ h
    rw [hvalid.2.1] at h'
    simp only [neutralNF624Lookup,if_neg hz]
    exact neutralNF622Restore_sound k n _ h'

theorem neutralNF690AllMoments_of_tables (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ)
    (hbank : ∀ i < bank.size, neutralNF690TableSound (neutralNF624BankRead bank i))
    (hc : neutralNF624Coverage bank idx) :
    neutralNF624AllMomentsSound (neutralNF624Lookup bank idx) := by
  constructor
  · intro i j s t
    exact neutralNF690Lookup_sound bank idx hbank _ _ (hc.1 i j s t)
  · intro i j k s t
    exact neutralNF690Lookup_sound bank idx hbank _ _ (hc.2 i j k s t)

end

#print axioms neutralNF690FitRows_eq
#print axioms neutralNF690Bank_size
#print axioms neutralNF690Bank_read
#print axioms neutralNF690Bank_shape
#print axioms neutralNF690Bank_index
#print axioms neutralNF690Table_eq
#print axioms neutralNF690Lookup_sound
#print axioms neutralNF690AllMoments_of_tables

end WeilDefect
