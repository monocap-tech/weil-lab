import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEnclosurePropagation
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSystemEquiv

namespace WeilDefect
noncomputable section
open Finset

/-- Only the literal H,V entry enclosures and finite real arithmetic
remain for the intrinsic physical coefficient containment. -/
theorem neutralNF613OriginalPhysicalSolve_of_entries
    (D H0 EH : Fin 242 → Fin 242 → ℝ)
    (V0 EV : Fin 242 → Fin 4 → ℝ)
    (y0 : Fin 242 → ℝ) (r : ℝ) (hr : 0≤r)
    (hH : ∀ k l, |neutralNF606PhysicalH k l-H0 k l| ≤ EH k l)
    (hV : ∀ k j, |neutralNF606PhysicalV k j-V0 k j| ≤ EV k j)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF613GramCenter D H0) i j|+
      neutralNF613GramRadius D EH i j) ≤ 1/100)
    (hres : ∀ i, |neutralNF613RHSCenter D V0 i-
      neutralNF606Apply (neutralNF613GramCenter D H0) y0 i|+
      neutralNF613RHSRadius D EV i+
        (∑ j, |y0 j|*neutralNF613GramRadius D EH i j) ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i|+
      (∑ j, |D i j|)*(2*r) ≤ neutralNF587SelectedRadius i) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  have hA := neutralNF613Gram_enclosure D H0 EH hH
  have hb := neutralNF613RHS_enclosure D V0 EV hV
  exact neutralNF612OriginalPhysicalSolve D y0 r hr
    (neutralNF613Rows_of_enclosures D _ _ hA hrow)
    (neutralNF613Residual_of_enclosures D _ _ _ _ y0 r hA hb hres) hpay

end
end WeilDefect
