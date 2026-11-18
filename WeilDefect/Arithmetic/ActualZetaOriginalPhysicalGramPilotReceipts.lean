import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramPilotAssembly
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalOscillatorPilots

namespace WeilDefect
noncomputable section

/-! NF619: the opposite real-sign mixed key is checked separately.
The exact J(-z) identity then avoids two further moment receipts.
The complete entry bounds use both original source terms, not
only a single positive-sign exponential contribution. -/

def neutralNF619MixedMinus : NF616Frequency := ⟨-1/2,37/64⟩

def neutralNF619MixedMinusRows : Array NF617MomentRow :=
  #[⟨-49886081731885688585833176103982357/10^35,
    -14043467082935807939230485585476647/10^35,1/10^33⟩]

set_option maxRecDepth 100000
set_option maxHeartbeats 10000000

theorem neutralNF619MixedMinus_check :
    neutralNF618RowGate neutralNF619MixedMinus neutralNF619MixedMinusRows 0 = true := by
  decide +kernel

theorem neutralNF619MixedMinus_sound :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) neutralNF619MixedMinus.value 0-
      (neutralNF617MomentRead neutralNF619MixedMinusRows 0).value‖ ≤
        (neutralNF617MomentRead neutralNF619MixedMinusRows 0).rad := by
  apply neutralNF618MomentRows_sound neutralNF618Pi neutralNF618Pi_sound
    neutralNF619MixedMinus (by decide) (by decide) neutralNF618Q neutralNF618N
    neutralNF618Q_pos (by decide) neutralNF618ExpFee neutralNF619MixedMinusRows
  · intro m hm
    change m<1 at hm
    have he : m=0 := by omega
    subst m
    exact neutralNF619MixedMinus_check
  · decide

theorem neutralNF619Osc_value :
    neutralNF618Osc.value = 2*neutralNF619Z := by
  unfold neutralNF618Osc NF616Frequency.value neutralNF615Lambda neutralNF619Z neutralNF619W
  push_cast
  ring

theorem neutralNF619Mixed_value :
    neutralNF618Mixed.value = neutralNF619Z+1/2 := by
  unfold neutralNF618Mixed NF616Frequency.value neutralNF615Lambda neutralNF619Z neutralNF619W
  push_cast
  ring

theorem neutralNF619MixedMinus_value :
    neutralNF619MixedMinus.value = neutralNF619Z-1/2 := by
  unfold neutralNF619MixedMinus NF616Frequency.value neutralNF615Lambda neutralNF619Z neutralNF619W
  push_cast
  ring

def neutralNF619OscGramReceipt : NF591Ball :=
  ⟨11/10-(neutralNF617MomentRead neutralNF618OscRows 0).re/2,
    (neutralNF617MomentRead neutralNF618OscRows 0).rad/2⟩

def neutralNF619MixedGramReceipt : NF591Ball :=
  ⟨((neutralNF617MomentRead neutralNF618MixedRows 0).im-
    (neutralNF617MomentRead neutralNF619MixedMinusRows 0).im)/2,
    ((neutralNF617MomentRead neutralNF618MixedRows 0).rad+
      (neutralNF617MomentRead neutralNF619MixedMinusRows 0).rad)/2⟩

theorem NF617MomentRow.value_re (q : NF617MomentRow) : q.value.re = (q.re:ℝ) := by
  simp [NF617MomentRow.value,Complex.add_re,Complex.mul_re]

theorem NF617MomentRow.value_im (q : NF617MomentRow) : q.value.im = (q.im:ℝ) := by
  simp [NF617MomentRow.value,Complex.add_im,Complex.mul_im]

theorem neutralNF619OscGram_certified :
    neutralNF619OscGramReceipt.Contains (neutralNF606PhysicalH (0:Fin 242) (0:Fin 242)) := by
  have h := neutralNF618Osc_sound 0 (by decide)
  rw [neutralNF619Osc_value] at h
  have h' := neutralNF619OscGram_of_moment _ _ h
  simpa only [neutralNF619OscGramReceipt,NF591Ball.Contains,
    NF617MomentRow.value_re,Rat.cast_sub,Rat.cast_div,Rat.cast_ofNat] using h'

theorem neutralNF619MixedGram_certified :
    neutralNF619MixedGramReceipt.Contains (neutralNF606PhysicalH (0:Fin 242) (241:Fin 242)) := by
  have hp := neutralNF618Mixed_sound
  have hm := neutralNF619MixedMinus_sound
  rw [neutralNF619Mixed_value] at hp
  rw [neutralNF619MixedMinus_value] at hm
  have h := neutralNF619MixedGram_of_moments _ _ _ _ hp hm
  simpa only [neutralNF619MixedGramReceipt,NF591Ball.Contains,NF617MomentRow.value_im,
    Rat.cast_sub,Rat.cast_add,Rat.cast_div,Rat.cast_ofNat] using h

end
end WeilDefect
