import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentTableSound

namespace WeilDefect
noncomputable section

/-! NF618: three concrete degrees on two genuine source keys.
The 35-digit rational centers are untrusted proposals; each
kernel check validates the outward recurrence residual. -/

def neutralNF618Q : ℕ := 10^40
def neutralNF618N : ℕ := 48
def neutralNF618Pi : NF591Ball := neutralNF592PiBall neutralNF618Q neutralNF618N

theorem neutralNF618Q_pos : 0<neutralNF618Q := by norm_num [neutralNF618Q]

theorem neutralNF618ExpFee :
    2/(Nat.factorial neutralNF618N:ℝ) ≤ 1/(neutralNF618Q:ℝ) := by
  have h : 2*neutralNF618Q ≤ Nat.factorial neutralNF618N := by decide +kernel
  apply (div_le_div_iff₀ (by positivity : (0:ℝ)<Nat.factorial neutralNF618N)
    (by exact_mod_cast neutralNF618Q_pos : (0:ℝ)<neutralNF618Q)).mpr
  have h' : (2:ℝ)*(neutralNF618Q:ℝ) ≤ (Nat.factorial neutralNF618N:ℝ) := by exact_mod_cast h
  simpa using h'

theorem neutralNF618AtanFee (p : ℕ) (hp : 0<p)
    (h : neutralNF618Q ≤ p^97*97) :
    (1/(p:ℝ))^97/97 ≤ 1/(neutralNF618Q:ℝ) := by
  have hp' : (0:ℝ)<p := by exact_mod_cast hp
  have hq : (0:ℝ)<neutralNF618Q := by exact_mod_cast neutralNF618Q_pos
  rw [div_pow,one_pow,div_div]
  apply one_div_le_one_div_of_le hq
  exact_mod_cast h

theorem neutralNF618Pi_sound : neutralNF618Pi.Contains Real.pi := by
  apply neutralNF592PiBall_sound _ _ neutralNF618Q_pos
  · change (1/5:ℝ)^(2*48+1)/(2*(48:ℝ)+1) ≤ _
    norm_num only [show (2*48+1:ℕ)=97 by decide,show (2*(48:ℝ)+1)=97 by norm_num]
    exact neutralNF618AtanFee 5 (by decide) (by decide +kernel)
  · change (1/239:ℝ)^(2*48+1)/(2*(48:ℝ)+1) ≤ _
    norm_num only [show (2*48+1:ℕ)=97 by decide,show (2*(48:ℝ)+1)=97 by norm_num]
    exact neutralNF618AtanFee 239 (by decide) (by decide +kernel)

def neutralNF618Osc : NF616Frequency := ⟨0,37/32⟩
def neutralNF618Mixed : NF616Frequency := ⟨1/2,37/64⟩

def neutralNF618OscRows : Array NF617MomentRow :=
  #[⟨27269882293080879354289005834393638/10^35,0,1/10^33⟩,
    ⟨0,7902701562810619635220000592690864/10^35,1/10^33⟩]

def neutralNF618MixedRows : Array NF617MomentRow :=
  #[⟨-49886081731885688585833176103982357/10^35,
    14043467082935807939230485585476647/10^35,1/10^33⟩]

def neutralNF618RowGate (k : NF616Frequency) (rows : Array NF617MomentRow)
    (n : ℕ) : Bool :=
  neutralNF617MomentRowCheck (neutralNF617Cache neutralNF618Pi k neutralNF618Q neutralNF618N)
    k.lower neutralNF618Q rows n

set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

theorem neutralNF618Osc0_check :
    neutralNF618RowGate neutralNF618Osc neutralNF618OscRows 0 = true := by
  decide +kernel

theorem neutralNF618Osc1_check :
    neutralNF618RowGate neutralNF618Osc neutralNF618OscRows 1 = true := by
  decide +kernel

theorem neutralNF618Mixed0_check :
    neutralNF618RowGate neutralNF618Mixed neutralNF618MixedRows 0 = true := by
  decide +kernel

theorem neutralNF618Osc_sound (n : ℕ) (hn : n<neutralNF618OscRows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) neutralNF618Osc.value n-
      (neutralNF617MomentRead neutralNF618OscRows n).value‖ ≤
        (neutralNF617MomentRead neutralNF618OscRows n).rad := by
  apply neutralNF618MomentRows_sound neutralNF618Pi neutralNF618Pi_sound
    neutralNF618Osc (by decide) (by decide) neutralNF618Q neutralNF618N
    neutralNF618Q_pos (by decide) neutralNF618ExpFee neutralNF618OscRows
  · intro m hm
    change m<2 at hm
    change neutralNF618RowGate neutralNF618Osc neutralNF618OscRows m = true
    interval_cases m
    · exact neutralNF618Osc0_check
    · exact neutralNF618Osc1_check
  · exact hn

theorem neutralNF618Mixed_sound :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) neutralNF618Mixed.value 0-
      (neutralNF617MomentRead neutralNF618MixedRows 0).value‖ ≤
        (neutralNF617MomentRead neutralNF618MixedRows 0).rad := by
  apply neutralNF618MomentRows_sound neutralNF618Pi neutralNF618Pi_sound
    neutralNF618Mixed (by decide) (by decide) neutralNF618Q neutralNF618N
    neutralNF618Q_pos (by decide) neutralNF618ExpFee neutralNF618MixedRows
  · intro m hm
    change m<1 at hm
    have he : m=0 := by omega
    subst m
    exact neutralNF618Mixed0_check
  · decide

/-- Key custody: these are actual exponent sums for the original
first oscillator and retained sinh mode. -/
theorem neutralNF618Osc_key :
    (neutralNF616SelectedKey (0:Fin 242) true).add
      (neutralNF616SelectedKey (0:Fin 242) true) = neutralNF618Osc := by
  decide +kernel

theorem neutralNF618OscSucc_key :
    (neutralNF616SelectedKey (0:Fin 242) true).add
      (neutralNF616SelectedKey (1:Fin 242) true) = neutralNF618Osc := by
  decide +kernel

theorem neutralNF618Mixed_key :
    (neutralNF616SelectedKey (0:Fin 242) true).add
      (neutralNF616SelectedKey (241:Fin 242) true) = neutralNF618Mixed := by
  decide +kernel

theorem neutralNF618Osc_actual :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ)
      ((neutralNF607SelectedTerm (0:Fin 242) true).exponent+
        (neutralNF607SelectedTerm (0:Fin 242) true).exponent) 0-
      (neutralNF617MomentRead neutralNF618OscRows 0).value‖ ≤
      (neutralNF617MomentRead neutralNF618OscRows 0).rad := by
  have he := (neutralNF616SelectedPair_key (0:Fin 242) (0:Fin 242) true true).1
  rw [neutralNF618Osc_key] at he
  rw [he]
  exact neutralNF618Osc_sound 0 (by decide)

theorem neutralNF618OscSucc_actual :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ)
      ((neutralNF607SelectedTerm (0:Fin 242) true).exponent+
        (neutralNF607SelectedTerm (1:Fin 242) true).exponent) 1-
      (neutralNF617MomentRead neutralNF618OscRows 1).value‖ ≤
      (neutralNF617MomentRead neutralNF618OscRows 1).rad := by
  have he := (neutralNF616SelectedPair_key (0:Fin 242) (1:Fin 242) true true).1
  rw [neutralNF618OscSucc_key] at he
  rw [he]
  exact neutralNF618Osc_sound 1 (by decide)

theorem neutralNF618Mixed_actual :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ)
      ((neutralNF607SelectedTerm (0:Fin 242) true).exponent+
        (neutralNF607SelectedTerm (241:Fin 242) true).exponent) 0-
      (neutralNF617MomentRead neutralNF618MixedRows 0).value‖ ≤
      (neutralNF617MomentRead neutralNF618MixedRows 0).rad := by
  have he := (neutralNF616SelectedPair_key (0:Fin 242) (241:Fin 242) true true).1
  rw [neutralNF618Mixed_key] at he
  rw [he]
  exact neutralNF618Mixed_sound

end
end WeilDefect
