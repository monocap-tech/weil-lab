import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalCoverageRows

namespace WeilDefect

/-! NF682: use the maximal monomial of each of the 67 original
oscillator groups and the genuine sinh pole. The representative map
is untrusted until its exact key/degree domination checks pass. -/

theorem neutralNF682Lookup_mono
    (bank : Array NF624KeyTable) (idx : NF616Frequency → ℕ)
    (k : NF616Frequency) (n m : ℕ) (hle : n ≤ m)
    (h : neutralNF624LookupCheck bank idx k m = true) :
    neutralNF624LookupCheck bank idx k n = true := by
  by_cases hz : k.h = 0 ∧ k.f = 0
  · simp [neutralNF624LookupCheck, hz]
  · simp only [neutralNF624LookupCheck, if_neg hz] at h ⊢
    have hh : idx k.canonical < bank.size ∧
        (neutralNF624BankRead bank (idx k.canonical)).key = k.canonical ∧
        m < (neutralNF624BankRead bank (idx k.canonical)).rows.size :=
      of_decide_eq_true h
    exact decide_eq_true ⟨hh.1, hh.2.1, lt_of_le_of_lt hle hh.2.2⟩

theorem neutralNF682CriticalKeyDegree (j : Fin 4) (k : Fin 33) (t : Bool) :
    (neutralNF624CriticalSpec j k t).key =
      (neutralNF624CriticalSpec 0 k t).key ∧
    (neutralNF624CriticalSpec j k t).degree =
      (neutralNF624CriticalSpec 0 k t).degree := by
  by_cases hk : k.val < 32 <;>
    simp [neutralNF624CriticalSpec, hk, NF622TermSpec.scale]

def neutralNF682DomRow (top : Fin 68 → Fin 242)
    (g : Fin 242 → Fin 68) (i : Fin 242) : Bool :=
  neutralNF624Signs.all (fun s =>
    let a := neutralNF624SelectedSpec i s
    let b := neutralNF624SelectedSpec (top (g i)) s
    decide (a.key = b.key ∧ a.degree ≤ b.degree))

def neutralNF682SelectedAt (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (top : Fin 68 → Fin 242)
    (i j : Fin 68) : Bool :=
  neutralNF624Signs.all (fun s =>
    neutralNF624Signs.all (neutralNF624SelectedCoverageRow bank idx (top i) (top j) s))

def neutralNF682MixedAt (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (top : Fin 68 → Fin 242)
    (i : Fin 68) (k : Fin 33) : Bool :=
  neutralNF624Signs.all (fun s =>
    neutralNF624Signs.all (neutralNF624MixedCoverageRow bank idx (top i) 0 k s))

def neutralNF682GroupRow (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (top : Fin 68 → Fin 242)
    (i : Fin 68) : Bool :=
  ((List.finRange 68).all (neutralNF682SelectedAt bank idx top i)) &&
    ((List.finRange 33).all (neutralNF682MixedAt bank idx top i))

theorem neutralNF682Coverage_of_groups
    (bank : Array NF624KeyTable) (idx : NF616Frequency → ℕ)
    (top : Fin 68 → Fin 242) (g : Fin 242 → Fin 68)
    (hdom : ∀ i, neutralNF682DomRow top g i = true)
    (hrows : ∀ i, neutralNF682GroupRow bank idx top i = true) :
    neutralNF624Coverage bank idx := by
  have hd (i : Fin 242) (s : Bool) :
      (neutralNF624SelectedSpec i s).key =
        (neutralNF624SelectedSpec (top (g i)) s).key ∧
      (neutralNF624SelectedSpec i s).degree ≤
        (neutralNF624SelectedSpec (top (g i)) s).degree := by
    have hh := hdom i
    unfold neutralNF682DomRow at hh
    exact of_decide_eq_true
      ((List.all_eq_true.mp hh) s (neutralNF624Sign_mem s))
  have hr (i : Fin 68) :
      ((List.finRange 68).all (neutralNF682SelectedAt bank idx top i)) = true ∧
      ((List.finRange 33).all (neutralNF682MixedAt bank idx top i)) = true := by
    simpa only [neutralNF682GroupRow, Bool.and_eq_true] using hrows i
  constructor
  · intro i j s t
    change neutralNF624LookupCheck bank idx
      ((neutralNF624SelectedSpec i s).key.add (neutralNF624SelectedSpec j t).key)
      ((neutralNF624SelectedSpec i s).degree + (neutralNF624SelectedSpec j t).degree) = true
    have hj := (List.all_eq_true.mp (hr (g i)).1) (g j) (by simp)
    unfold neutralNF682SelectedAt at hj
    have hs := (List.all_eq_true.mp hj) s (neutralNF624Sign_mem s)
    have ht := (List.all_eq_true.mp hs) t (neutralNF624Sign_mem t)
    rw [(hd i s).1, (hd j t).1]
    exact neutralNF682Lookup_mono bank idx _ _ _
      (Nat.add_le_add (hd i s).2 (hd j t).2) ht
  · intro i j k s t
    change neutralNF624LookupCheck bank idx
      ((neutralNF624SelectedSpec i s).key.add (neutralNF624CriticalSpec j k t).key)
      ((neutralNF624SelectedSpec i s).degree + (neutralNF624CriticalSpec j k t).degree) = true
    have hk := (List.all_eq_true.mp (hr (g i)).2) k (by simp)
    unfold neutralNF682MixedAt at hk
    have hs := (List.all_eq_true.mp hk) s (neutralNF624Sign_mem s)
    have ht := (List.all_eq_true.mp hs) t (neutralNF624Sign_mem t)
    have hc := neutralNF682CriticalKeyDegree j k t
    rw [(hd i s).1, hc.1, hc.2]
    exact neutralNF682Lookup_mono bank idx _ _ _
      (Nat.add_le_add_right (hd i s).2 _) ht

theorem neutralNF682CoverageCheck_of_coverage
    (bank : Array NF624KeyTable) (idx : NF616Frequency → ℕ)
    (h : neutralNF624Coverage bank idx) :
    neutralNF624CoverageCheck bank idx = true := by
  unfold neutralNF624CoverageCheck
  simp only [Bool.and_eq_true]
  constructor
  · apply List.all_eq_true.mpr
    intro i _
    apply List.all_eq_true.mpr
    intro j _
    apply List.all_eq_true.mpr
    intro s _
    apply List.all_eq_true.mpr
    intro t _
    exact h.1 i j s t
  · apply List.all_eq_true.mpr
    intro i _
    apply List.all_eq_true.mpr
    intro j _
    apply List.all_eq_true.mpr
    intro k _
    apply List.all_eq_true.mpr
    intro s _
    apply List.all_eq_true.mpr
    intro t _
    exact h.2 i j k s t

#print axioms neutralNF682Lookup_mono
#print axioms neutralNF682CriticalKeyDegree
#print axioms neutralNF682Coverage_of_groups
#print axioms neutralNF682CoverageCheck_of_coverage

end WeilDefect
