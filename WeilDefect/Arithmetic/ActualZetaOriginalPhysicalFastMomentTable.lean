import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFullTableSound
import WeilDefect.Arithmetic.ActualZetaOriginalCachedModeJets

namespace WeilDefect

/-! NF621: evaluator-only optimization, using the original certified
cached exponential recurrence. The computed rational rectangles must
be exactly the same as those in the accepted boundary soundness proof. -/

def neutralNF621RealEndpoint (h : ℚ) (Q N : ℕ) : NF591Rect :=
  let a := neutralNF593SmallExp (NF591Rect.realQ (h*11/20) Q) Q N
  a.mulQ a Q

theorem neutralNF621RealEndpoint_eq (h : ℚ) (Q N : ℕ) :
    neutralNF621RealEndpoint h Q N = neutralNF615RealEndpoint h Q N := by
  simp only [neutralNF621RealEndpoint,neutralNF615RealEndpoint,neutralNF593SmallExp_eq]

def neutralNF621Endpoint (p : NF591Ball) (h f : ℚ) (Q N : ℕ) : NF591Rect :=
  (neutralNF621RealEndpoint h Q N).mulQ (neutralNF593Phase p f Q N) Q

theorem neutralNF621Endpoint_eq (p : NF591Ball) (h f : ℚ) (Q N : ℕ) :
    neutralNF621Endpoint p h f Q N = neutralNF615Endpoint p h f Q N := by
  simp only [neutralNF621Endpoint,neutralNF615Endpoint,neutralNF621RealEndpoint_eq,
    neutralNF593Phase_eq]

def neutralNF621Cache (p : NF591Ball) (k : NF616Frequency) (Q N : ℕ) :
    NF617MomentCache :=
  ⟨neutralNF615LambdaRect p k.h k.f Q,
   neutralNF621Endpoint p k.h k.f Q N,
   neutralNF621Endpoint p (-k.h) (-k.f) Q N⟩

theorem neutralNF621Cache_eq (p : NF591Ball) (k : NF616Frequency) (Q N : ℕ) :
    neutralNF621Cache p k Q N = neutralNF617Cache p k Q N := by
  simp only [neutralNF621Cache,neutralNF617Cache,neutralNF621Endpoint_eq]

def neutralNF621FastTableCheck (p : NF591Ball) (k : NF616Frequency)
    (Q N : ℕ) (rows : Array NF617MomentRow) : Bool :=
  let δ := k.lower
  let c := neutralNF621Cache p k Q N
  decide (0<Q ∧ 0<N ∧ |k.h| ≤ 1 ∧ 0<δ ∧ 0<rows.size) &&
    (List.range rows.size).all (neutralNF617MomentRowCheck c δ Q rows)

theorem neutralNF621FastTableCheck_eq (p : NF591Ball) (k : NF616Frequency)
    (Q N : ℕ) (rows : Array NF617MomentRow) :
    neutralNF621FastTableCheck p k Q N rows =
      neutralNF617NonzeroTableCheck p k Q N rows := by
  simp only [neutralNF621FastTableCheck,neutralNF617NonzeroTableCheck,neutralNF621Cache_eq]

noncomputable section

theorem neutralNF621FastHighPrecision_sound (k : NF616Frequency)
    (rows : Array NF617MomentRow)
    (hc : neutralNF621FastTableCheck
      (neutralNF592PiBall neutralNF616Q neutralNF616AtanN)
      k neutralNF616Q neutralNF616ExpN rows = true)
    (n : ℕ) (hn : n<rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) k.value n-
      (neutralNF617MomentRead rows n).value‖ ≤
        (neutralNF617MomentRead rows n).rad := by
  rw [neutralNF621FastTableCheck_eq] at hc
  exact neutralNF620HighPrecisionTable_sound k rows hc n hn

end
end WeilDefect
