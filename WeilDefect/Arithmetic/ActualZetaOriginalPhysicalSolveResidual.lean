import WeilDefect.Arithmetic.ActualZetaOriginalSolveResidualCustody
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

namespace WeilDefect
noncomputable section
open MeasureTheory Finset

/-! NF606: the exact UNWEIGHTED full-interval physical moment
system used by the historic NF407 exporter. These are not the
cutoff-weighted canonical moment matrices of the collar correction.
The numeric input attachment is still a separate obligation. -/

def neutralNF606PhysicalH (i j : Fin 242) : ℝ :=
  ∫ x in (-(11/10:ℝ))..(11/10:ℝ),
    nf545OriginalSelectedRealGenerator i x * nf545OriginalSelectedRealGenerator j x

def neutralNF606PhysicalV (i : Fin 242) (j : Fin 4) : ℝ :=
  ∫ x in (-(11/10:ℝ))..(11/10:ℝ),
    nf545OriginalSelectedRealGenerator i x * neutralNF587CriticalGenerator j x

def neutralNF606PhysicalW (j : Fin 4) : ℝ :=
  (neutralNF604OriginalT4Numerators[j.val]! : ℝ)/2^20 -
    neutralNF604OriginalCritical j

def neutralNF606TransformedH (D : Fin 242 → Fin 242 → ℝ)
    (i j : Fin 242) : ℝ :=
  ∑ k, D k i * (∑ l, neutralNF606PhysicalH k l * D l j)

def neutralNF606TransformedRHS (D : Fin 242 → Fin 242 → ℝ)
    (i : Fin 242) : ℝ :=
  ∑ k, D k i * (∑ j : Fin 4, neutralNF606PhysicalV k j * neutralNF606PhysicalW j)

theorem neutralNF606PhysicalH_symm (i j : Fin 242) :
    neutralNF606PhysicalH i j = neutralNF606PhysicalH j i := by
  unfold neutralNF606PhysicalH
  apply intervalIntegral.integral_congr
  intro x _
  ring

/-- Real attachment for the historical physical system. The
frame D must be bound to its exact historical dyads separately.
The equation is an actual real solution condition; existence,
uniqueness and certified entry enclosures are not assumed away. -/
theorem neutralNF606OriginalBox_of_physical_residual
    (D : Fin 242 → Fin 242 → ℝ) (y y0 : Fin 242 → ℝ)
    (r : ℝ) (hr : 0≤r)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100)
    (hsolve : ∀ i, neutralNF606Apply (neutralNF606TransformedH D) y i =
      neutralNF606TransformedRHS D i)
    (hres : ∀ i, |neutralNF606TransformedRHS D i -
      neutralNF606Apply (neutralNF606TransformedH D) y0 i| ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i|+
      (∑ j, |D i j|)*(2*r) ≤ neutralNF587SelectedRadius i) :
    neutralNF587SourceInFrozenBox (neutralNF606Apply D y) neutralNF604OriginalCritical :=
  neutralNF606Selected_box_of_residual (neutralNF606TransformedH D) D
    y y0 (neutralNF606TransformedRHS D) r hr hrow hsolve hres hpay

end
end WeilDefect
