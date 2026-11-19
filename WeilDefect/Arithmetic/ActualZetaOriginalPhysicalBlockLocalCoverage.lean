import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFrequencyBlockCoverage

namespace WeilDefect

/-! NF687: exact coverage on a compact key/degree reader. Neither
the proposed search index nor an external source hash proves coverage.
The reader must be attached to the shape of the actual numerical bank. -/

abbrev NF687Shape := NF616Frequency × ℕ

def neutralNF687Search (read : ℕ → NF687Shape) (size : ℕ)
    (k : NF616Frequency) : ℕ → ℕ → ℕ → ℕ
  | 0, _, _ => size
  | fuel+1, lo, hi =>
    if lo < hi then
      let m := (lo+hi)/2
      let t := (read m).1
      if t=k then m
      else if neutralNF624KeyLT t k then
        neutralNF687Search read size k fuel (m+1) hi
      else neutralNF687Search read size k fuel lo m
    else size

def neutralNF687Index (read : ℕ → NF687Shape) (size : ℕ)
    (k : NF616Frequency) : ℕ :=
  neutralNF687Search read size k 16 0 size

def neutralNF687LookupCheck (read : ℕ → NF687Shape) (size : ℕ)
    (idx : NF616Frequency → ℕ) (k : NF616Frequency) (n : ℕ) : Bool :=
  if k.h=0 ∧ k.f=0 then true else
    let i := idx k.canonical
    decide (i<size ∧ (read i).1=k.canonical ∧ n<(read i).2)

theorem neutralNF687Lookup_eq (bank : Array NF624KeyTable)
    (read : ℕ → NF687Shape) (size : ℕ)
    (hs : bank.size=size)
    (hr : ∀ i<size, neutralNF627ShapeAt bank i=read i)
    (idx : NF616Frequency → ℕ) (k : NF616Frequency) (n : ℕ) :
    neutralNF624LookupCheck bank idx k n =
      neutralNF687LookupCheck read size idx k n := by
  by_cases hz : k.h=0 ∧ k.f=0
  · simp [neutralNF624LookupCheck,neutralNF687LookupCheck,hz]
  · let i := idx k.canonical
    simp only [neutralNF624LookupCheck,neutralNF687LookupCheck,if_neg hz]
    change decide (i<bank.size ∧ (neutralNF624BankRead bank i).key=k.canonical ∧
      n<(neutralNF624BankRead bank i).rows.size) =
      decide (i<size ∧ (read i).1=k.canonical ∧ n<(read i).2)
    by_cases hi : i<size
    · have he := hr i hi
      have hk := congrArg Prod.fst he
      have hn := congrArg Prod.snd he
      change (neutralNF624BankRead bank i).key=(read i).1 at hk
      change (neutralNF624BankRead bank i).rows.size=(read i).2 at hn
      rw [hs,hk,hn]
    · simp [hs,hi]

def neutralNF687SelectedAt (read : ℕ → NF687Shape) (size : ℕ)
    (idx : NF616Frequency → ℕ) (top : Fin 68 → Fin 242)
    (i j : Fin 68) : Bool :=
  neutralNF624Signs.all (fun s => neutralNF624Signs.all (fun t =>
    let a := neutralNF624SelectedSpec (top i) s
    let b := neutralNF624SelectedSpec (top j) t
    neutralNF687LookupCheck read size idx (a.key.add b.key) (a.degree+b.degree)))

def neutralNF687MixedAt (read : ℕ → NF687Shape) (size : ℕ)
    (idx : NF616Frequency → ℕ) (top : Fin 68 → Fin 242)
    (i : Fin 68) (k : Fin 33) : Bool :=
  neutralNF624Signs.all (fun s => neutralNF624Signs.all (fun t =>
    let a := neutralNF624SelectedSpec (top i) s
    let b := neutralNF624CriticalSpec 0 k t
    neutralNF687LookupCheck read size idx (a.key.add b.key) (a.degree+b.degree)))

def neutralNF687GroupRow (read : ℕ → NF687Shape) (size : ℕ)
    (idx : NF616Frequency → ℕ) (top : Fin 68 → Fin 242) (i : Fin 68) : Bool :=
  ((List.finRange 68).all (neutralNF687SelectedAt read size idx top i)) &&
    ((List.finRange 33).all (neutralNF687MixedAt read size idx top i))

theorem neutralNF687Coverage_of_groups
    (bank : Array NF624KeyTable) (read : ℕ → NF687Shape) (size : ℕ)
    (hs : bank.size=size)
    (hr : ∀ i<size, neutralNF627ShapeAt bank i=read i)
    (idx : NF616Frequency → ℕ) (top : Fin 68 → Fin 242) (g : Fin 242 → Fin 68)
    (hdom : ∀ i, neutralNF682DomRow top g i=true)
    (hrows : ∀ i, neutralNF687GroupRow read size idx top i=true) :
    neutralNF624Coverage bank idx := by
  apply neutralNF682Coverage_of_groups bank idx top g hdom
  intro i
  have h := hrows i
  unfold neutralNF687GroupRow at h
  unfold neutralNF682GroupRow
  simp only [Bool.and_eq_true] at h ⊢
  constructor
  · apply List.all_eq_true.mpr
    intro j hj
    have hj' := (List.all_eq_true.mp h.1) j hj
    unfold neutralNF687SelectedAt at hj'
    unfold neutralNF682SelectedAt
    apply List.all_eq_true.mpr
    intro s hs'
    have hs'' := (List.all_eq_true.mp hj') s hs'
    apply List.all_eq_true.mpr
    intro t ht
    have hh := (List.all_eq_true.mp hs'') t ht
    unfold neutralNF624SelectedCoverageRow
    rw [neutralNF687Lookup_eq bank read size hs hr idx]
    exact hh
  · apply List.all_eq_true.mpr
    intro k hk
    have hk' := (List.all_eq_true.mp h.2) k hk
    unfold neutralNF687MixedAt at hk'
    unfold neutralNF682MixedAt
    apply List.all_eq_true.mpr
    intro s hs'
    have hs'' := (List.all_eq_true.mp hk') s hs'
    apply List.all_eq_true.mpr
    intro t ht
    have hh := (List.all_eq_true.mp hs'') t ht
    unfold neutralNF624MixedCoverageRow
    rw [neutralNF687Lookup_eq bank read size hs hr idx]
    exact hh

#print axioms neutralNF687Lookup_eq
#print axioms neutralNF687Coverage_of_groups

end WeilDefect
