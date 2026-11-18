import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBoundaryReceipts
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMixedTerms

namespace WeilDefect
noncomputable section

/-! NF616: exact rational frequency keys, derived from the same
selected/critical terms already attached to the physical H and V. -/

structure NF616Frequency where
  h : ℚ
  f : ℚ
  deriving DecidableEq, Repr

def NF616Frequency.value (k : NF616Frequency) : ℂ :=
  neutralNF615Lambda k.h k.f

def NF616Frequency.add (k l : NF616Frequency) : NF616Frequency :=
  ⟨k.h+l.h,k.f+l.f⟩

def neutralNF616Signed (s : Bool) (v : ℚ) : ℚ :=
  if s then v else -v

def neutralNF616OscKey (f : ℚ) (s : Bool) : NF616Frequency :=
  ⟨0, neutralNF616Signed s f⟩

def neutralNF616PoleKey (s : Bool) : NF616Frequency :=
  ⟨neutralNF616Signed s (1/2),0⟩

def neutralNF616SelectedKey (j : Fin 242) (s : Bool) : NF616Frequency :=
  if hj : j.val<241 then
    neutralNF616OscKey (nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩).1 s
  else neutralNF616PoleKey s

def neutralNF616CriticalKey (k : Fin 33) (s : Bool) : NF616Frequency :=
  if k.val<32 then neutralNF616OscKey neutralNF587CriticalFrequencies[k.val]! s
  else neutralNF616PoleKey s

theorem neutralNF616Osc_sin (f : ℚ) (n : ℕ) (s : Bool) :
    (neutralNF607SinTerm (2*(Real.pi:ℂ)*(f:ℂ)) n s).exponent =
      (neutralNF616OscKey f s).value := by
  cases s <;> simp [neutralNF607SinTerm,neutralNF616OscKey,
    neutralNF616Signed,NF616Frequency.value,neutralNF615Lambda] <;>
    push_cast <;> ring

theorem neutralNF616Osc_cos (f : ℚ) (n : ℕ) (s : Bool) :
    (neutralNF607CosTerm (2*(Real.pi:ℂ)*(f:ℂ)) n s).exponent =
      (neutralNF616OscKey f s).value := by
  cases s <;> simp [neutralNF607CosTerm,neutralNF616OscKey,
    neutralNF616Signed,NF616Frequency.value,neutralNF615Lambda] <;>
    push_cast <;> ring

theorem neutralNF616Pole (s : Bool) :
    (neutralNF607SinhTerm s).exponent = (neutralNF616PoleKey s).value := by
  cases s <;> norm_num [neutralNF607SinhTerm,neutralNF616PoleKey,
    neutralNF616Signed,NF616Frequency.value,neutralNF615Lambda]

theorem neutralNF616SelectedKey_exact (j : Fin 242) (s : Bool) :
    (neutralNF607SelectedTerm j s).exponent = (neutralNF616SelectedKey j s).value := by
  unfold neutralNF607SelectedTerm neutralNF616SelectedKey
  by_cases hj : j.val<241
  · simp only [dif_pos hj]
    split_ifs
    · exact neutralNF616Osc_sin _ _ _
    · exact neutralNF616Osc_cos _ _ _
  · simp only [dif_neg hj]
    exact neutralNF616Pole s

theorem neutralNF616CriticalKey_exact (j : Fin 4) (k : Fin 33) (s : Bool) :
    (neutralNF607CriticalTerm j k s).exponent =
      (neutralNF616CriticalKey k s).value := by
  unfold neutralNF607CriticalTerm neutralNF616CriticalKey
  by_cases hk : k.val<32
  · simp only [dif_pos hk,if_pos hk]
    exact neutralNF616Osc_sin _ _ _
  · simp only [dif_neg hk,if_neg hk]
    exact neutralNF616Pole s

theorem NF616Frequency.add_value (k l : NF616Frequency) :
    (k.add l).value = k.value+l.value := by
  unfold NF616Frequency.add NF616Frequency.value neutralNF615Lambda
  push_cast
  ring

theorem neutralNF616SelectedKey_h (j : Fin 242) (s : Bool) :
    |(neutralNF616SelectedKey j s).h| ≤ 1/2 := by
  unfold neutralNF616SelectedKey
  split_ifs <;> cases s <;>
    norm_num [neutralNF616OscKey,neutralNF616PoleKey,neutralNF616Signed]

theorem neutralNF616CriticalKey_h (k : Fin 33) (s : Bool) :
    |(neutralNF616CriticalKey k s).h| ≤ 1/2 := by
  unfold neutralNF616CriticalKey
  split_ifs <;> cases s <;>
    norm_num [neutralNF616OscKey,neutralNF616PoleKey,neutralNF616Signed]

theorem NF616Frequency.add_h (k l : NF616Frequency)
    (hk : |k.h| ≤ 1/2) (hl : |l.h| ≤ 1/2) :
    |(k.add l).h| ≤ 1 := by
  change |k.h+l.h| ≤ 1
  exact (abs_add_le _ _).trans (by linarith)

theorem neutralNF616SelectedPair_key (i j : Fin 242) (s t : Bool) :
    let k := (neutralNF616SelectedKey i s).add (neutralNF616SelectedKey j t)
    (neutralNF607SelectedTerm i s).exponent+(neutralNF607SelectedTerm j t).exponent =
      k.value ∧ |k.h| ≤ 1 := by
  dsimp only
  rw [NF616Frequency.add_value,neutralNF616SelectedKey_exact,neutralNF616SelectedKey_exact]
  exact ⟨rfl,NF616Frequency.add_h _ _ (neutralNF616SelectedKey_h i s)
    (neutralNF616SelectedKey_h j t)⟩

theorem neutralNF616MixedPair_key (i : Fin 242) (j : Fin 4) (k : Fin 33) (s t : Bool) :
    let p := (neutralNF616SelectedKey i s).add (neutralNF616CriticalKey k t)
    (neutralNF607SelectedTerm i s).exponent+(neutralNF607CriticalTerm j k t).exponent =
      p.value ∧ |p.h| ≤ 1 := by
  dsimp only
  rw [NF616Frequency.add_value,neutralNF616SelectedKey_exact,neutralNF616CriticalKey_exact]
  exact ⟨rfl,NF616Frequency.add_h _ _ (neutralNF616SelectedKey_h i s)
    (neutralNF616CriticalKey_h k t)⟩

end
end WeilDefect
