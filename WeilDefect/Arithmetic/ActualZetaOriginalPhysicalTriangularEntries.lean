import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBooleanClosure

namespace WeilDefect

/-! NF629: one independent analytic widening comparison per
unordered Gram entry, plus exact symmetry of the proposed centers.
No symmetry of the interval evaluator itself is assumed. -/

def neutralNF629HGate (M : NF622Moments) (p : NF625PaymentData)
    (i j : Fin 242) : Bool :=
  if j.val ≤ i.val then neutralNF625EntryHCheck M p i j
  else decide (p.H0 i j = p.H0 j i)

def neutralNF629EntryRow (M : NF622Moments) (p : NF625PaymentData)
    (i : Fin 242) : Bool :=
  (List.finRange 242).all (neutralNF629HGate M p i) &&
  (List.finRange 4).all (neutralNF625EntryVCheck M p i)

noncomputable section

theorem neutralNF629EntryRows_sound (M : NF622Moments) (p : NF625PaymentData)
    (hM : neutralNF624AllMomentsSound M)
    (hc : ∀ i, neutralNF629EntryRow M p i = true) :
    (∀ i j, |neutralNF606PhysicalH i j-p.HR i j| ≤ (p.eH:ℝ)) ∧
    (∀ i j, |neutralNF606PhysicalV i j-p.VR i j| ≤ (p.eV:ℝ)) := by
  have hh (i j : Fin 242) :
      neutralNF629HGate M p i j = true := by
    have hi := hc i
    simp only [neutralNF629EntryRow,Bool.and_eq_true] at hi
    exact (List.all_eq_true.mp hi.1) j (by simp)
  have hl (i j : Fin 242) (hj : j.val ≤ i.val) :
      |neutralNF606PhysicalH i j-p.HR i j| ≤ (p.eH:ℝ) := by
    have he := hh i j
    simp only [neutralNF629HGate,if_pos hj] at he
    have hw : (neutralNF624HBall M neutralNF616Q i j).Widens
        ⟨p.H0 i j,p.eH⟩ := by
      unfold NF591Ball.Widens
      exact of_decide_eq_true he
    exact NF591Ball.contains_widen
      (neutralNF624HBall_sound M neutralNF616Q neutralNF616Q_pos hM i j) hw
  constructor
  · intro i j
    by_cases hj : j.val ≤ i.val
    · exact hl i j hj
    · have he := hh i j
      simp only [neutralNF629HGate,if_neg hj] at he
      have hs : p.H0 i j = p.H0 j i := of_decide_eq_true he
      have hsR : p.HR i j = p.HR j i := by
        unfold NF625PaymentData.HR
        rw [hs]
      rw [neutralNF606PhysicalH_symm i j,hsR]
      exact hl j i (by omega)
  · intro i j
    have hi := hc i
    simp only [neutralNF629EntryRow,Bool.and_eq_true] at hi
    have he := (List.all_eq_true.mp hi.2) j (by simp)
    have hw : (neutralNF624VBall M neutralNF616Q i j).Widens
        ⟨p.V0 i j,p.eV⟩ := by
      unfold NF591Ball.Widens
      exact of_decide_eq_true he
    exact NF591Ball.contains_widen
      (neutralNF624VBall_sound M neutralNF616Q neutralNF616Q_pos hM i j) hw

end
end WeilDefect
