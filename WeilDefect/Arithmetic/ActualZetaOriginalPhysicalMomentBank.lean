import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSourceSpecs
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFullTableSound

namespace WeilDefect

/-! NF624: an untrusted lookup index may propose a slot, but the
checker validates its bounds, the exact rational key, and the
requested degree. No default receipt can silently enter an entry. -/

structure NF624KeyTable where
  key : NF616Frequency
  rows : Array NF617MomentRow

def neutralNF624BankRead (bank : Array NF624KeyTable) (i : ℕ) : NF624KeyTable :=
  bank[i]?.getD ⟨⟨0,0⟩,#[]⟩

def neutralNF624BankCheck (bank : Array NF624KeyTable) : Bool :=
  (List.range bank.size).all (fun i =>
    let t := neutralNF624BankRead bank i
    neutralNF617NonzeroTableCheck
      (neutralNF592PiBall neutralNF616Q neutralNF616AtanN)
      t.key neutralNF616Q neutralNF616ExpN t.rows)

def neutralNF624LookupCheck (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (k : NF616Frequency) (n : ℕ) : Bool :=
  if k.h=0 ∧ k.f=0 then true else
    let i := idx k.canonical
    let t := neutralNF624BankRead bank i
    decide (i<bank.size ∧ t.key=k.canonical ∧ n<t.rows.size)

def neutralNF624Lookup (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) : NF622Moments :=
  fun k n =>
    if k.h=0 ∧ k.f=0 then NF591Rect.realQ (neutralNF617ZeroMoment n) neutralNF616Q
    else
      let t := neutralNF624BankRead bank (idx k.canonical)
      neutralNF622Restore k n (neutralNF617MomentRead t.rows n).enclosure

noncomputable section

theorem neutralNF624Lookup_sound (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (hbank : neutralNF624BankCheck bank = true)
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
    have ht : neutralNF617NonzeroTableCheck
        (neutralNF592PiBall neutralNF616Q neutralNF616AtanN)
        t.key neutralNF616Q neutralNF616ExpN t.rows = true := by
      unfold neutralNF624BankCheck at hbank
      exact (List.all_eq_true.mp hbank) i (List.mem_range.mpr hvalid.1)
    have h := neutralNF620HighPrecisionTable_sound t.key t.rows ht n hvalid.2.2
    have h' := NF617MomentRow.enclosure_sound _ _ h
    rw [hvalid.2.1] at h'
    simp only [neutralNF624Lookup,if_neg hz]
    exact neutralNF622Restore_sound k n _ h'

/-- Coverage concerns actual source pairs, not a count or a hash
of an independently enumerated inventory. -/
def neutralNF624Coverage (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) : Prop :=
  (∀ (i j : Fin 242) (s t : Bool),
    let a := neutralNF624SelectedSpec i s
    let b := neutralNF624SelectedSpec j t
    neutralNF624LookupCheck bank idx (a.key.add b.key) (a.degree+b.degree)=true) ∧
  (∀ (i : Fin 242) (j : Fin 4) (k : Fin 33) (s t : Bool),
    let a := neutralNF624SelectedSpec i s
    let b := neutralNF624CriticalSpec j k t
    neutralNF624LookupCheck bank idx (a.key.add b.key) (a.degree+b.degree)=true)

theorem neutralNF624AllMoments_of_bank (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (hbank : neutralNF624BankCheck bank = true)
    (hc : neutralNF624Coverage bank idx) :
    neutralNF624AllMomentsSound (neutralNF624Lookup bank idx) := by
  constructor
  · intro i j s t
    exact neutralNF624Lookup_sound bank idx hbank _ _ (hc.1 i j s t)
  · intro i j k s t
    exact neutralNF624Lookup_sound bank idx hbank _ _ (hc.2 i j k s t)

theorem neutralNF624H_of_bank (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (hbank : neutralNF624BankCheck bank = true)
    (hc : neutralNF624Coverage bank idx) (i j : Fin 242) :
    (neutralNF624HBall (neutralNF624Lookup bank idx) neutralNF616Q i j).Contains
      (neutralNF606PhysicalH i j) :=
  neutralNF624HBall_sound _ _ neutralNF616Q_pos
    (neutralNF624AllMoments_of_bank bank idx hbank hc) i j

theorem neutralNF624V_of_bank (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (hbank : neutralNF624BankCheck bank = true)
    (hc : neutralNF624Coverage bank idx) (i : Fin 242) (j : Fin 4) :
    (neutralNF624VBall (neutralNF624Lookup bank idx) neutralNF616Q i j).Contains
      (neutralNF606PhysicalV i j) :=
  neutralNF624VBall_sound _ _ neutralNF616Q_pos
    (neutralNF624AllMoments_of_bank bank idx hbank hc) i j

end
end WeilDefect
