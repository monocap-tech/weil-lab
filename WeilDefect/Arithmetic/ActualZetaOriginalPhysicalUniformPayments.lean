import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEntryAttachment

namespace WeilDefect
noncomputable section
open Finset

/-! NF623: uniform entry radii reduce outward propagation through
the exact historical frame to column masses. This avoids an additional
dense interval-radius matrix multiplication. No numerical bound or
historical coordinate containment is asserted without its premise. -/

def neutralNF623ColMass (D : Fin 242 → Fin 242 → ℝ) (i : Fin 242) : ℝ :=
  ∑ k, |D k i|

def neutralNF623RowMass (D : Fin 242 → Fin 242 → ℝ) (i : Fin 242) : ℝ :=
  ∑ j, |D i j|

def neutralNF623WMass : ℝ :=
  ∑ j : Fin 4, |neutralNF606PhysicalW j|

theorem neutralNF623GramRadius_eq (D : Fin 242 → Fin 242 → ℝ)
    (e : ℝ) (i j : Fin 242) :
    neutralNF613GramRadius D (fun _ _ => e) i j =
      neutralNF623ColMass D i * (neutralNF623ColMass D j * e) := by
  unfold neutralNF613GramRadius neutralNF623ColMass
  simp only [Finset.sum_mul]

theorem neutralNF623RHSRadius_eq (D : Fin 242 → Fin 242 → ℝ)
    (e : ℝ) (i : Fin 242) :
    neutralNF613RHSRadius D (fun _ _ => e) i =
      neutralNF623ColMass D i * (neutralNF623WMass * e) := by
  unfold neutralNF613RHSRadius neutralNF623ColMass neutralNF623WMass
  simp only [Finset.sum_mul]

theorem neutralNF623RowRadius_eq (D : Fin 242 → Fin 242 → ℝ)
    (e : ℝ) (i : Fin 242) :
    (∑ j, neutralNF613GramRadius D (fun _ _ => e) i j) =
      neutralNF623ColMass D i * ((∑ j, neutralNF623ColMass D j) * e) := by
  simp only [neutralNF623GramRadius_eq,Finset.sum_mul,Finset.mul_sum]

theorem neutralNF623ResidualRadius_eq (D : Fin 242 → Fin 242 → ℝ)
    (e : ℝ) (y0 : Fin 242 → ℝ) (i : Fin 242) :
    (∑ j, |y0 j| * neutralNF613GramRadius D (fun _ _ => e) i j) =
      neutralNF623ColMass D i * ((∑ j, |y0 j| * neutralNF623ColMass D j) * e) := by
  simp only [neutralNF623GramRadius_eq,Finset.sum_mul,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  ring

/-- Exact center products plus two scalar entry-error budgets suffice
for the actual original physical system. The proof is purely a
specialization of the accepted literal physical enclosure attachment. -/
theorem neutralNF623OriginalPhysicalSolve_of_uniform_entries
    (D H0 : Fin 242 → Fin 242 → ℝ)
    (V0 : Fin 242 → Fin 4 → ℝ)
    (eH eV : ℝ)
    (y0 : Fin 242 → ℝ) (r : ℝ) (hr : 0≤r)
    (hH : ∀ k l, |neutralNF606PhysicalH k l-H0 k l| ≤ eH)
    (hV : ∀ k j, |neutralNF606PhysicalV k j-V0 k j| ≤ eV)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF613GramCenter D H0) i j|) +
      neutralNF623ColMass D i * ((∑ j, neutralNF623ColMass D j)*eH) ≤ 1/100)
    (hres : ∀ i, |neutralNF613RHSCenter D V0 i-
      neutralNF606Apply (neutralNF613GramCenter D H0) y0 i| +
      neutralNF623ColMass D i * (neutralNF623WMass*eV) +
      neutralNF623ColMass D i * ((∑ j, |y0 j| *neutralNF623ColMass D j)*eH) ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i| +
      neutralNF623RowMass D i*(2*r) ≤ neutralNF587SelectedRadius i) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  apply neutralNF613OriginalPhysicalSolve_of_entries D H0 (fun _ _ => eH)
    V0 (fun _ _ => eV) y0 r hr hH hV
  · intro i
    rw [Finset.sum_add_distrib,neutralNF623RowRadius_eq]
    exact hrow i
  · intro i
    rw [neutralNF623RHSRadius_eq,neutralNF623ResidualRadius_eq]
    exact hres i
  · exact hpay

end
end WeilDefect
