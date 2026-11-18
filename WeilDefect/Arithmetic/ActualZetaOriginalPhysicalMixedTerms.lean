import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramTerms

namespace WeilDefect
noncomputable section
open MeasureTheory Finset intervalIntegral

/-! NF607: the critical family is not an anonymous new oscillator
basis. Use exactly the 32 + pole terms of each original probe,
with their authentic rational weights. -/

def neutralNF607CriticalBlock (j : Fin 4) (k : Fin 33) (x : ℝ) : ℂ :=
  (neutralNF607CriticalTerm j k true).eval x +
    (neutralNF607CriticalTerm j k false).eval x

theorem neutralNF607CriticalBlock_eq (j : Fin 4) (k : Fin 33) (x : ℝ) :
    neutralNF607CriticalBlock j k x =
      if hk : k.val < 32 then
        ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℂ) *
          Complex.sin (2*(Real.pi:ℂ)*(neutralNF587CriticalFrequencies[k.val]! : ℂ)*(x:ℂ))
      else
        (neutralNF587CriticalPoles[j.val]! : ℂ)*Complex.sinh ((x:ℂ)/2) := by
  unfold neutralNF607CriticalBlock neutralNF607CriticalTerm
  by_cases hk : k.val<32
  · simp only [dif_pos hk]
    let w : ℂ := 2*(Real.pi:ℂ)*(neutralNF587CriticalFrequencies[k.val]! : ℂ)
    let c : ℂ := ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℂ)
    have h := neutralNF607SinTerm_sum w 0 x
    simp only [pow_zero,one_mul] at h
    calc
      _ = c*((neutralNF607SinTerm w 0 true).eval x+
          (neutralNF607SinTerm w 0 false).eval x) := by
        unfold NF607Term.eval
        dsimp only
        ring
      _ = _ := by rw [h]
  · simp only [dif_neg hk]
    let c : ℂ := (neutralNF587CriticalPoles[j.val]! : ℂ)
    calc
      _ = c*((neutralNF607SinhTerm true).eval x+
          (neutralNF607SinhTerm false).eval x) := by
        unfold NF607Term.eval
        dsimp only
        ring
      _ = _ := by rw [neutralNF607SinhTerm_sum]

theorem neutralNF607Critical_sum (j : Fin 4) (x : ℝ) :
    (∑ k : Fin 33, neutralNF607CriticalBlock j k x) =
      (neutralNF587CriticalGenerator j x:ℂ) := by
  rw [← neutralNF588CriticalComplex_ofReal,Fin.sum_univ_castSucc]
  unfold neutralNF588CriticalComplex
  simp only [neutralNF607CriticalBlock_eq,Fin.val_castSucc,Fin.val_last,
    Fin.isLt,dif_pos,show ¬(32:ℕ)<32 by omega,dif_neg]

def neutralNF607MixedBlock (i : Fin 242) (j : Fin 4) (k : Fin 33) : ℂ :=
  neutralNF607Pair (neutralNF607SelectedTerm i true) (neutralNF607CriticalTerm j k true) +
  neutralNF607Pair (neutralNF607SelectedTerm i true) (neutralNF607CriticalTerm j k false) +
  neutralNF607Pair (neutralNF607SelectedTerm i false) (neutralNF607CriticalTerm j k true) +
  neutralNF607Pair (neutralNF607SelectedTerm i false) (neutralNF607CriticalTerm j k false)

def neutralNF607MixedV (i : Fin 242) (j : Fin 4) : ℂ :=
  ∑ k : Fin 33, neutralNF607MixedBlock i j k

theorem neutralNF607MixedBlock_eq (i : Fin 242) (j : Fin 4) (k : Fin 33) :
    neutralNF607MixedBlock i j k =
      ∫ x in (-(11/10:ℝ))..(11/10:ℝ),
        (nf545OriginalSelectedRealGenerator i x:ℂ)*neutralNF607CriticalBlock j k x := by
  let a := neutralNF607SelectedTerm i true
  let b := neutralNF607SelectedTerm i false
  let c := neutralNF607CriticalTerm j k true
  let d := neutralNF607CriticalTerm j k false
  have h (t u : NF607Term) : IntervalIntegrable (fun x => t.eval x*u.eval x)
      volume (-(11/10:ℝ)) (11/10:ℝ) :=
    ((neutralNF607Term_continuous t).mul (neutralNF607Term_continuous u)).intervalIntegrable _ _
  change neutralNF607Pair a c+neutralNF607Pair a d+
    neutralNF607Pair b c+neutralNF607Pair b d = _
  simp only [neutralNF607Pair_eq]
  rw [← intervalIntegral.integral_add (h a c) (h a d),
    ← intervalIntegral.integral_add ((h a c).add (h a d)) (h b c),
    ← intervalIntegral.integral_add (((h a c).add (h a d)).add (h b c)) (h b d)]
  apply intervalIntegral.integral_congr
  intro x _
  change a.eval x*c.eval x+a.eval x*d.eval x+b.eval x*c.eval x+b.eval x*d.eval x =
    (nf545OriginalSelectedRealGenerator i x:ℂ)*(c.eval x+d.eval x)
  rw [← neutralNF607SelectedTerm_sum i x]
  change _ = (a.eval x+b.eval x)*(c.eval x+d.eval x)
  ring

theorem neutralNF607MixedV_eq (i : Fin 242) (j : Fin 4) :
    neutralNF607MixedV i j = (neutralNF606PhysicalV i j:ℂ) := by
  unfold neutralNF607MixedV
  simp only [neutralNF607MixedBlock_eq]
  rw [← intervalIntegral.integral_finsetSum]
  · unfold neutralNF606PhysicalV
    rw [← intervalIntegral.integral_ofReal]
    apply intervalIntegral.integral_congr
    intro x _
    change (∑ k : Fin 33, (nf545OriginalSelectedRealGenerator i x:ℂ)*
      neutralNF607CriticalBlock j k x) =
        ((nf545OriginalSelectedRealGenerator i x*neutralNF587CriticalGenerator j x:ℝ):ℂ)
    rw [← mul_sum,neutralNF607Critical_sum,Complex.ofReal_mul]
  · intro k _
    have ha : Continuous (fun x : ℝ => (nf545OriginalSelectedRealGenerator i x:ℂ)) := by
      rw [show (fun x : ℝ => (nf545OriginalSelectedRealGenerator i x:ℂ)) =
          fun x => (neutralNF607SelectedTerm i true).eval x+
            (neutralNF607SelectedTerm i false).eval x from
        funext (fun x => (neutralNF607SelectedTerm_sum i x).symm)]
      exact (neutralNF607Term_continuous _).add (neutralNF607Term_continuous _)
    have hb : Continuous (neutralNF607CriticalBlock j k) :=
      (neutralNF607Term_continuous _).add (neutralNF607Term_continuous _)
    exact (ha.mul hb).intervalIntegrable _ _

end
end WeilDefect
