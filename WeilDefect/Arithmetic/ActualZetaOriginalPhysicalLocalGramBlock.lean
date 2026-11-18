import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentBank
import WeilDefect.Arithmetic.ActualZetaOriginalDirectedRounding

namespace WeilDefect

/-! NF649: local analytic table custody is sufficient for a physical
entry. Neither full bank truth nor global source coverage is required.
Every consumed key and degree still passes the original lookup gate. -/

noncomputable section

theorem neutralNF649Lookup_sound (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ)
    (hbank : ∀ i < bank.size, ∀ n < (neutralNF624BankRead bank i).rows.size,
      ‖neutralNF620J (neutralNF624BankRead bank i).key.value n -
        (neutralNF617MomentRead (neutralNF624BankRead bank i).rows n).value‖ ≤
        (neutralNF617MomentRead (neutralNF624BankRead bank i).rows n).rad)
    (k : NF616Frequency) (n : ℕ)
    (hc : neutralNF624LookupCheck bank idx k n=true) :
    (neutralNF624Lookup bank idx k n).Contains (neutralNF620J k.value n) := by
  by_cases hz : k.h=0 ∧ k.f=0
  · have he : k.value=0 := k.zero_value hz.1 hz.2
    rw [he]
    simp only [neutralNF624Lookup,if_pos hz]
    exact neutralNF622ZeroMoment_sound n neutralNF616Q neutralNF616Q_pos
  · let i := idx k.canonical
    let t := neutralNF624BankRead bank i
    have hv : i<bank.size ∧ t.key=k.canonical ∧ n<t.rows.size := by
      unfold neutralNF624LookupCheck at hc
      rw [if_neg hz] at hc
      exact of_decide_eq_true hc
    have ht := NF617MomentRow.enclosure_sound (neutralNF617MomentRead t.rows n) _
      (hbank i hv.1 n hv.2.2)
    change (neutralNF617MomentRead t.rows n).enclosure.Contains
      (neutralNF620J t.key.value n) at ht
    rw [hv.2.1] at ht
    simp only [neutralNF624Lookup,if_neg hz]
    exact neutralNF622Restore_sound k n _ ht

end

def neutralNF649HPairCheck (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i j : Fin 242) (s t : Bool) : Bool :=
  let a := neutralNF624SelectedSpec i s
  let b := neutralNF624SelectedSpec j t
  neutralNF624LookupCheck bank idx (a.key.add b.key) (a.degree+b.degree)

def neutralNF649HCheck (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i j : Fin 242) : Bool :=
  neutralNF649HPairCheck bank idx i j true true &&
    (neutralNF649HPairCheck bank idx i j true false &&
      (neutralNF649HPairCheck bank idx i j false true &&
        neutralNF649HPairCheck bank idx i j false false))

theorem neutralNF649HCheck_pairs (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i j : Fin 242)
    (hc : neutralNF649HCheck bank idx i j=true) :
    ∀ s t, neutralNF649HPairCheck bank idx i j s t=true := by
  simp only [neutralNF649HCheck,Bool.and_eq_true] at hc
  intro s t
  cases s <;> cases t
  · exact hc.2.2.2
  · exact hc.2.2.1
  · exact hc.2.1
  · exact hc.1

def neutralNF649WidenH (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ) (i j : Fin 242) (b : NF591Ball) : Bool :=
  let a := neutralNF624HBall (neutralNF624Lookup bank idx) neutralNF616Q i j
  decide (|a.mid-b.mid|+a.rad≤b.rad)

noncomputable section

theorem neutralNF649H_of_local (bank : Array NF624KeyTable)
    (idx : NF616Frequency → ℕ)
    (hbank : ∀ i < bank.size, ∀ n < (neutralNF624BankRead bank i).rows.size,
      ‖neutralNF620J (neutralNF624BankRead bank i).key.value n -
        (neutralNF617MomentRead (neutralNF624BankRead bank i).rows n).value‖ ≤
        (neutralNF617MomentRead (neutralNF624BankRead bank i).rows n).rad)
    (i j : Fin 242) (b : NF591Ball)
    (hc : neutralNF649HCheck bank idx i j=true)
    (hw : neutralNF649WidenH bank idx i j b=true) :
    b.Contains (neutralNF606PhysicalH i j) := by
  have hp := neutralNF649HCheck_pairs bank idx i j hc
  have hh : (neutralNF624HBall (neutralNF624Lookup bank idx)
      neutralNF616Q i j).Contains (neutralNF606PhysicalH i j) := by
    apply neutralNF622H_of_specs _ _ neutralNF616Q_pos i j _ _
      (neutralNF624SelectedSpec_term i) (neutralNF624SelectedSpec_term j)
    intro s t
    exact neutralNF649Lookup_sound bank idx hbank _ _ (hp s t)
  have hwide : (neutralNF624HBall (neutralNF624Lookup bank idx)
      neutralNF616Q i j).Widens b := by
    change |(neutralNF624HBall (neutralNF624Lookup bank idx)
      neutralNF616Q i j).mid - b.mid| +
      (neutralNF624HBall (neutralNF624Lookup bank idx)
        neutralNF616Q i j).rad ≤ b.rad
    change decide (|(neutralNF624HBall (neutralNF624Lookup bank idx)
      neutralNF616Q i j).mid - b.mid| +
      (neutralNF624HBall (neutralNF624Lookup bank idx)
        neutralNF616Q i j).rad ≤ b.rad) = true at hw
    exact of_decide_eq_true hw
  exact NF591Ball.contains_widen hh hwide

end
end WeilDefect
