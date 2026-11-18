import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentBank

namespace WeilDefect

/-! NF624: check coverage against the real source pairs by finite
enumeration. An arbitrary proposed index is safe only after this
check; key equality and degree checks are not delegated to a hash. -/

def neutralNF624SelectedCoverageRow (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i j : Fin 242) (s t : Bool) : Bool :=
  let a := neutralNF624SelectedSpec i s
  let b := neutralNF624SelectedSpec j t
  neutralNF624LookupCheck bank idx (a.key.add b.key) (a.degree+b.degree)

def neutralNF624MixedCoverageRow (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i : Fin 242) (j : Fin 4) (k : Fin 33)
    (s t : Bool) : Bool :=
  let a := neutralNF624SelectedSpec i s
  let b := neutralNF624CriticalSpec j k t
  neutralNF624LookupCheck bank idx (a.key.add b.key) (a.degree+b.degree)

def neutralNF624Signs : List Bool := [true,false]

def neutralNF624CoverageCheck (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) : Bool :=
  ((List.finRange 242).all (fun i =>
    (List.finRange 242).all (fun j =>
      neutralNF624Signs.all (fun s =>
        neutralNF624Signs.all (neutralNF624SelectedCoverageRow bank idx i j s))))) &&
  ((List.finRange 242).all (fun i =>
    (List.finRange 4).all (fun j =>
      (List.finRange 33).all (fun k =>
        neutralNF624Signs.all (fun s =>
          neutralNF624Signs.all (neutralNF624MixedCoverageRow bank idx i j k s))))))

theorem neutralNF624Sign_mem (s : Bool) : s ∈ neutralNF624Signs := by
  cases s <;> simp [neutralNF624Signs]

theorem neutralNF624CoverageCheck_sound (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ)
    (hc : neutralNF624CoverageCheck bank idx = true) :
    neutralNF624Coverage bank idx := by
  unfold neutralNF624CoverageCheck at hc
  simp only [Bool.and_eq_true] at hc
  constructor
  · intro i j s t
    have hi := (List.all_eq_true.mp hc.1) i (by simp)
    have hj := (List.all_eq_true.mp hi) j (by simp)
    have hs := (List.all_eq_true.mp hj) s (neutralNF624Sign_mem s)
    exact (List.all_eq_true.mp hs) t (neutralNF624Sign_mem t)
  · intro i j k s t
    have hi := (List.all_eq_true.mp hc.2) i (by simp)
    have hj := (List.all_eq_true.mp hi) j (by simp)
    have hk := (List.all_eq_true.mp hj) k (by simp)
    have hs := (List.all_eq_true.mp hk) s (neutralNF624Sign_mem s)
    exact (List.all_eq_true.mp hs) t (neutralNF624Sign_mem t)

end WeilDefect
