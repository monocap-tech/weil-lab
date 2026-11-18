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

def neutralNF627ShapeCheck (bank metadata : Array NF624KeyTable) : Bool :=
  decide (bank.size=metadata.size) &&
  (List.range bank.size).all (fun i =>
    decide (neutralNF627ShapeAt bank i=neutralNF627ShapeAt metadata i))

def neutralNF627ShapeMatches (bank metadata : Array NF624KeyTable) : Prop :=
  bank.size=metadata.size ∧
  ∀ i < bank.size, neutralNF627ShapeAt bank i=neutralNF627ShapeAt metadata i

theorem neutralNF627ShapeCheck_sound (bank metadata : Array NF624KeyTable)
    (hc : neutralNF627ShapeCheck bank metadata=true) :
    neutralNF627ShapeMatches bank metadata := by
  unfold neutralNF627ShapeCheck at hc
  simp only [Bool.and_eq_true] at hc
  refine ⟨of_decide_eq_true hc.1,?_⟩
  intro i hi
  exact of_decide_eq_true ((List.all_eq_true.mp hc.2) i (List.mem_range.mpr hi))

theorem neutralNF627LookupCheck_shape (bank metadata : Array NF624KeyTable)
    (h : neutralNF627ShapeMatches bank metadata)
    (idx : NF616Frequency → ℕ) (k : NF616Frequency) (n : ℕ) :
    neutralNF624LookupCheck bank idx k n =
      neutralNF624LookupCheck metadata idx k n := by
  by_cases hz : k.h=0 ∧ k.f=0
  · simp [neutralNF624LookupCheck,hz]
  · let i := idx k.canonical
    by_cases hi : i<bank.size
    · have hm : i < metadata.size := by rw [← h.1]; exact hi
      have he := h.2 i hi
      have hk : (neutralNF624BankRead bank i).key =
          (neutralNF624BankRead metadata i).key := congrArg Prod.fst he
      have hn : (neutralNF624BankRead bank i).rows.size =
          (neutralNF624BankRead metadata i).rows.size := congrArg Prod.snd he
      unfold neutralNF624LookupCheck
      simp only [if_neg hz]
      change decide (i<bank.size ∧ (neutralNF624BankRead bank i).key=k.canonical ∧
        n<(neutralNF624BankRead bank i).rows.size) =
        decide (i < metadata.size ∧ (neutralNF624BankRead metadata i).key=k.canonical ∧
        n<(neutralNF624BankRead metadata i).rows.size)
      rw [h.1,hk,hn]
    · have hm : ¬i < metadata.size := by rw [← h.1]; exact hi
      unfold neutralNF624LookupCheck
      simp only [if_neg hz]
      change decide (i<bank.size ∧ (neutralNF624BankRead bank i).key=k.canonical ∧
        n<(neutralNF624BankRead bank i).rows.size) =
        decide (i < metadata.size ∧ (neutralNF624BankRead metadata i).key=k.canonical ∧
        n<(neutralNF624BankRead metadata i).rows.size)
      simp [hi,hm]

theorem neutralNF627Coverage_of_shape (bank metadata : Array NF624KeyTable)
    (hshape : neutralNF627ShapeCheck bank metadata=true)
    (hcov : neutralNF624CoverageCheck metadata (neutralNF624Index metadata)=true) :
    neutralNF624Coverage bank (neutralNF624Index metadata) := by
  have he := neutralNF627ShapeCheck_sound bank metadata hshape
  have hc := neutralNF624CoverageCheck_sound metadata (neutralNF624Index metadata) hcov
  constructor
  · intro i j s t
    dsimp only
    rw [neutralNF627LookupCheck_shape bank metadata he]
    exact hc.1 i j s t
  · intro i j k s t
    dsimp only
    rw [neutralNF627LookupCheck_shape bank metadata he]
    exact hc.2 i j k s t

noncomputable section

theorem neutralNF627AllMoments_of_metadata
    (bank metadata : Array NF624KeyTable)
    (hbank : neutralNF624BankCheck bank=true)
    (hshape : neutralNF627ShapeCheck bank metadata=true)
    (hcov : neutralNF624CoverageCheck metadata (neutralNF624Index metadata)=true) :
    neutralNF624AllMomentsSound
      (neutralNF624Lookup bank (neutralNF624Index metadata)) :=
  neutralNF624AllMoments_of_bank bank (neutralNF624Index metadata) hbank
    (neutralNF627Coverage_of_shape bank metadata hshape hcov)

end
end WeilDefect
