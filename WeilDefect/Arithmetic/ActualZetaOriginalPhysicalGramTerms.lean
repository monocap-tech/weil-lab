import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTermDictionary
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSolveResidual

namespace WeilDefect
noncomputable section
open MeasureTheory Finset intervalIntegral

/-! NF607: finite two-exponential blocks, with the 32 original
critical sine coefficients and genuine hyperbolic term retained.
No negative-power or Si primitive enters the physical solve. -/

def neutralNF607Pair (t u : NF607Term) : ℂ :=
  t.coeff*u.coeff*neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ)
    (t.exponent+u.exponent) (t.degree+u.degree)

def neutralNF607SelectedH (i j : Fin 242) : ℂ :=
  neutralNF607Pair (neutralNF607SelectedTerm i true) (neutralNF607SelectedTerm j true) +
  neutralNF607Pair (neutralNF607SelectedTerm i true) (neutralNF607SelectedTerm j false) +
  neutralNF607Pair (neutralNF607SelectedTerm i false) (neutralNF607SelectedTerm j true) +
  neutralNF607Pair (neutralNF607SelectedTerm i false) (neutralNF607SelectedTerm j false)

theorem neutralNF607Term_continuous (t : NF607Term) : Continuous t.eval := by
  unfold NF607Term.eval
  fun_prop

theorem neutralNF607Pair_eq (t u : NF607Term) :
    neutralNF607Pair t u =
      ∫ x in (-(11/10:ℝ))..(11/10:ℝ), t.eval x*u.eval x :=
  (neutralNF607Term_product _ _ t u).symm

theorem neutralNF607SelectedH_eq (i j : Fin 242) :
    neutralNF607SelectedH i j = (neutralNF606PhysicalH i j:ℂ) := by
  let a := neutralNF607SelectedTerm i true
  let b := neutralNF607SelectedTerm i false
  let c := neutralNF607SelectedTerm j true
  let d := neutralNF607SelectedTerm j false
  have h (t u : NF607Term) : IntervalIntegrable (fun x => t.eval x*u.eval x)
      volume (-(11/10:ℝ)) (11/10:ℝ) :=
    ((neutralNF607Term_continuous t).mul (neutralNF607Term_continuous u)).intervalIntegrable _ _
  change neutralNF607Pair a c+neutralNF607Pair a d+
    neutralNF607Pair b c+neutralNF607Pair b d = _
  simp only [neutralNF607Pair_eq]
  rw [← intervalIntegral.integral_add (h a c) (h a d),
    ← intervalIntegral.integral_add ((h a c).add (h a d)) (h b c),
    ← intervalIntegral.integral_add (((h a c).add (h a d)).add (h b c)) (h b d)]
  have he : (fun x : ℝ => a.eval x*c.eval x+a.eval x*d.eval x+
      b.eval x*c.eval x+b.eval x*d.eval x) =
      (fun x => ((nf545OriginalSelectedRealGenerator i x*
        nf545OriginalSelectedRealGenerator j x:ℝ):ℂ)) := by
    funext x
    calc
      _ = (a.eval x+b.eval x)*(c.eval x+d.eval x) := by ring
      _ = _ := by
        rw [show a.eval x+b.eval x = _ from neutralNF607SelectedTerm_sum i x,
          show c.eval x+d.eval x = _ from neutralNF607SelectedTerm_sum j x,
          Complex.ofReal_mul]
  rw [he]
  unfold neutralNF606PhysicalH
  exact integral_ofReal

end
end WeilDefect
