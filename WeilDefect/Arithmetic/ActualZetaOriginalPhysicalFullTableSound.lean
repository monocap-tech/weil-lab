import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentTableSound
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalReceiptParameters

namespace WeilDefect
noncomputable section

/-! NF620: the whole executable array gate, rather than separately
supplied row hypotheses, is sufficient for its analytic enclosures.
No computational truth premise is silently inserted. -/

theorem neutralNF620NonzeroTableCheck_sound
    (p : NF591Ball) (hp : p.Contains Real.pi)
    (k : NF616Frequency) (Q N : ℕ)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ))
    (rows : Array NF617MomentRow)
    (hc : neutralNF617NonzeroTableCheck p k Q N rows = true)
    (n : ℕ) (hn : n<rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) k.value n-
      (neutralNF617MomentRead rows n).value‖ ≤
        (neutralNF617MomentRead rows n).rad := by
  unfold neutralNF617NonzeroTableCheck at hc
  simp only [Bool.and_eq_true] at hc
  have hparts := hc
  have hparam : 0<Q ∧ 0<N ∧ |k.h| ≤ 1 ∧ 0<k.lower ∧ 0<rows.size :=
    of_decide_eq_true hparts.1
  apply neutralNF618MomentRows_sound p hp k hparam.2.2.1 hparam.2.2.2.1
    Q N hparam.1 (by omega) hfee rows
  · intro m hm
    exact (List.all_eq_true.mp hparts.2) m (List.mem_range.mpr hm)
  · exact hn

theorem neutralNF620HighPrecisionTable_sound
    (k : NF616Frequency) (rows : Array NF617MomentRow)
    (hc : neutralNF617NonzeroTableCheck
      (neutralNF592PiBall neutralNF616Q neutralNF616AtanN)
      k neutralNF616Q neutralNF616ExpN rows = true)
    (n : ℕ) (hn : n<rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) k.value n-
      (neutralNF617MomentRead rows n).value‖ ≤
        (neutralNF617MomentRead rows n).rad :=
  neutralNF620NonzeroTableCheck_sound _ neutralNF616Pi_sound k
    neutralNF616Q neutralNF616ExpN neutralNF616ExpFee rows hc n hn

end
end WeilDefect
