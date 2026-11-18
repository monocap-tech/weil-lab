import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBankIndex

namespace WeilDefect

/-! NF627: source coverage only reads keys and row counts.
It can be checked on a compact metadata bank without reducing
the 2600-digit coordinate proposals. A separate exact shape
comparison transfers coverage to the actual numerical bank. -/

def neutralNF627ShapeAt (bank : Array NF624KeyTable) (i : ℕ) :
    NF616Frequency × ℕ :=
  let t := neutralNF624BankRead bank i
  (t.key,t.rows.size)

def neutralNF627ShapeCheck (bank meta : Array NF624KeyTable) : Bool :=
  decide (bank.size=meta.size) &&
  (List.range bank.size).all (fun i =>
    decide (neutralNF627ShapeAt bank i=neutralNF627ShapeAt meta i))

def neutralNF627ShapeMatches (bank meta : Array NF624KeyTable) : Prop :=
  bank.size=meta.size ∧
  ∀ i < bank.size, neutralNF627ShapeAt bank i=neutralNF627ShapeAt meta i

theorem neutralNF627ShapeCheck_sound (bank meta : Array NF624KeyTable)
    (hc : neutralNF627ShapeCheck bank meta=true) :
    neutralNF627ShapeMatches bank meta := by
  unfold neutralNF627ShapeCheck at hc
  simp only [Bool.and_eq_true] at hc
  refine ⟨of_decide_eq_true hc.1,?_⟩
  intro i hi
  exact of_decide_eq_true ((List.all_eq_true.mp hc.2) i (List.mem_range.mpr hi))

theorem neutralNF627LookupCheck_shape (bank meta : Array NF624KeyTable)
    (h : neutralNF627ShapeMatches bank meta)
    (idx : NF616Frequency → ℕ) (k : NF616Frequency) (n : ℕ) :
    neutralNF624LookupCheck bank idx k n =
      neutralNF624LookupCheck meta idx k n := by
  by_cases hz : k.h=0 ∧ k.f=0
  · simp [neutralNF624LookupCheck,hz]
  · let i := idx k.canonical
    by_cases hi : i<bank.size
    · have hm : i<meta.size := by rw [← h.1]; exact hi
      have he := h.2 i hi
      have hk : (neutralNF624BankRead bank i).key =
          (neutralNF624BankRead meta i).key := congrArg Prod.fst he
      have hn : (neutralNF624BankRead bank i).rows.size =
          (neutralNF624BankRead meta i).rows.size := congrArg Prod.snd he
      unfold neutralNF624LookupCheck
      simp only [if_neg hz]
      change decide (i<bank.size ∧ (neutralNF624BankRead bank i).key=k.canonical ∧
        n<(neutralNF624BankRead bank i).rows.size) =
        decide (i<meta.size ∧ (neutralNF624BankRead meta i).key=k.canonical ∧
        n<(neutralNF624BankRead meta i).rows.size)
      rw [h.1,hk,hn]
    · have hm : ¬i<meta.size := by rw [← h.1]; exact hi
      unfold neutralNF624LookupCheck
      simp only [if_neg hz]
      change decide (i<bank.size ∧ (neutralNF624BankRead bank i).key=k.canonical ∧
        n<(neutralNF624BankRead bank i).rows.size) =
        decide (i<meta.size ∧ (neutralNF624BankRead meta i).key=k.canonical ∧
        n<(neutralNF624BankRead meta i).rows.size)
      simp [hi,hm]

theorem neutralNF627Coverage_of_shape (bank meta : Array NF624KeyTable)
    (hshape : neutralNF627ShapeCheck bank meta=true)
    (hcov : neutralNF624CoverageCheck meta (neutralNF624Index meta)=true) :
    neutralNF624Coverage bank (neutralNF624Index meta) := by
  have he := neutralNF627ShapeCheck_sound bank meta hshape
  have hc := neutralNF624CoverageCheck_sound meta (neutralNF624Index meta) hcov
  constructor
  · intro i j s t
    rw [neutralNF627LookupCheck_shape bank meta he]
    exact hc.1 i j s t
  · intro i j k s t
    rw [neutralNF627LookupCheck_shape bank meta he]
    exact hc.2 i j k s t

noncomputable section

theorem neutralNF627AllMoments_of_metadata
    (bank meta : Array NF624KeyTable)
    (hbank : neutralNF624BankCheck bank=true)
    (hshape : neutralNF627ShapeCheck bank meta=true)
    (hcov : neutralNF624CoverageCheck meta (neutralNF624Index meta)=true) :
    neutralNF624AllMomentsSound
      (neutralNF624Lookup bank (neutralNF624Index meta)) :=
  neutralNF624AllMoments_of_bank bank (neutralNF624Index meta) hbank
    (neutralNF627Coverage_of_shape bank meta hshape hcov)

end
end WeilDefect
