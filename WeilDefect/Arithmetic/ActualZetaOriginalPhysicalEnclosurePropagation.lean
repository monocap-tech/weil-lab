import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSolveResidual

namespace WeilDefect
noncomputable section
open Finset

/-! NF613: isolate exact propagation of entry enclosures through the
literal historical physical system. All centers/radii may be
rational casts, but analytic containment is a separate premise. -/

theorem neutralNF613WeightedError {n : ℕ}
    (u x m e : Fin n → ℝ) (h : ∀ j, |x j-m j| ≤ e j) :
    |(∑ j, u j*x j)-(∑ j, u j*m j)| ≤ ∑ j, |u j| *e j := by
  rw [← Finset.sum_sub_distrib]
  simp_rw [← mul_sub]
  apply (abs_sum_le_sum_abs _ _).trans
  apply Finset.sum_le_sum
  intro j _
  rw [abs_mul]
  exact mul_le_mul_of_nonneg_left (h j) (abs_nonneg _)

def neutralNF613GramCenter (D H0 : Fin 242 → Fin 242 → ℝ) (i j : Fin 242) : ℝ :=
  ∑ k, D k i * (∑ l, H0 k l * D l j)

def neutralNF613GramRadius (D EH : Fin 242 → Fin 242 → ℝ) (i j : Fin 242) : ℝ :=
  ∑ k, |D k i| * (∑ l, |D l j| * EH k l)

theorem neutralNF613Gram_enclosure (D H0 EH : Fin 242 → Fin 242 → ℝ)
    (hH : ∀ k l, |neutralNF606PhysicalH k l-H0 k l| ≤ EH k l)
    (i j : Fin 242) :
    |neutralNF606TransformedH D i j-neutralNF613GramCenter D H0 i j| ≤
      neutralNF613GramRadius D EH i j := by
  unfold neutralNF606TransformedH neutralNF613GramCenter neutralNF613GramRadius
  apply neutralNF613WeightedError
  intro k
  simp_rw [mul_comm (neutralNF606PhysicalH k _) (D _ j),
    mul_comm (H0 k _) (D _ j)]
  exact neutralNF613WeightedError (fun l => D l j) (neutralNF606PhysicalH k)
    (H0 k) (EH k) (hH k)

def neutralNF613RHSCenter (D : Fin 242 → Fin 242 → ℝ)
    (V0 : Fin 242 → Fin 4 → ℝ) (i : Fin 242) : ℝ :=
  ∑ k, D k i * (∑ j : Fin 4, V0 k j * neutralNF606PhysicalW j)

def neutralNF613RHSRadius (D : Fin 242 → Fin 242 → ℝ)
    (EV : Fin 242 → Fin 4 → ℝ) (i : Fin 242) : ℝ :=
  ∑ k, |D k i| * (∑ j : Fin 4, |neutralNF606PhysicalW j| * EV k j)

theorem neutralNF613RHS_enclosure (D : Fin 242 → Fin 242 → ℝ)
    (V0 EV : Fin 242 → Fin 4 → ℝ)
    (hV : ∀ k j, |neutralNF606PhysicalV k j-V0 k j| ≤ EV k j)
    (i : Fin 242) :
    |neutralNF606TransformedRHS D i-neutralNF613RHSCenter D V0 i| ≤
      neutralNF613RHSRadius D EV i := by
  unfold neutralNF606TransformedRHS neutralNF613RHSCenter neutralNF613RHSRadius
  apply neutralNF613WeightedError
  intro k
  simp_rw [mul_comm (neutralNF606PhysicalV k _) (neutralNF606PhysicalW _),
    mul_comm (V0 k _) (neutralNF606PhysicalW _)]
  exact neutralNF613WeightedError neutralNF606PhysicalW (neutralNF606PhysicalV k)
    (V0 k) (EV k) (hV k)

/-- More general than the particular absolute-product propagation
above: a tighter source-native enclosure of A may also be used. -/
theorem neutralNF613Rows_of_enclosures (D A0 EA : Fin 242 → Fin 242 → ℝ)
    (hA : ∀ i j, |neutralNF606TransformedH D i j-A0 i j| ≤ EA i j)
    (hcheck : ∀ i, (∑ j, (|neutralNF606Defect A0 i j| + EA i j)) ≤ 1/100)
    (i : Fin 242) :
    (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100 := by
  apply le_trans _ (hcheck i)
  apply Finset.sum_le_sum
  intro j _
  have he : neutralNF606Defect (neutralNF606TransformedH D) i j =
      neutralNF606Defect A0 i j-(neutralNF606TransformedH D i j-A0 i j) := by
    unfold neutralNF606Defect
    ring
  rw [he]
  calc
    _ ≤ |neutralNF606Defect A0 i j| + |neutralNF606TransformedH D i j-A0 i j| := by
      simpa only [sub_eq_add_neg,abs_neg] using
        (abs_add_le (neutralNF606Defect A0 i j) (-(neutralNF606TransformedH D i j-A0 i j)))
    _ ≤ _ := add_le_add le_rfl (hA i j)

theorem neutralNF613Residual_of_enclosures (D A0 EA : Fin 242 → Fin 242 → ℝ)
    (b0 Eb y0 : Fin 242 → ℝ) (r : ℝ)
    (hA : ∀ i j, |neutralNF606TransformedH D i j-A0 i j| ≤ EA i j)
    (hb : ∀ i, |neutralNF606TransformedRHS D i-b0 i| ≤ Eb i)
    (hcheck : ∀ i, |b0 i-neutralNF606Apply A0 y0 i| +Eb i+
      (∑ j, |y0 j| *EA i j) ≤ r)
    (i : Fin 242) :
    |neutralNF606TransformedRHS D i-
      neutralNF606Apply (neutralNF606TransformedH D) y0 i| ≤ r := by
  have hdiff :
      |neutralNF606Apply (neutralNF606TransformedH D) y0 i-
        neutralNF606Apply A0 y0 i| ≤ ∑ j, |y0 j| *EA i j := by
    unfold neutralNF606Apply
    simp_rw [mul_comm (neutralNF606TransformedH D i _) (y0 _),
      mul_comm (A0 i _) (y0 _)]
    exact neutralNF613WeightedError y0 (neutralNF606TransformedH D i)
      (A0 i) (EA i) (hA i)
  have he : neutralNF606TransformedRHS D i-
      neutralNF606Apply (neutralNF606TransformedH D) y0 i =
      ((b0 i-neutralNF606Apply A0 y0 i)+(neutralNF606TransformedRHS D i-b0 i))-
        (neutralNF606Apply (neutralNF606TransformedH D) y0 i-
          neutralNF606Apply A0 y0 i) := by ring
  rw [he]
  have hab (x y : ℝ) : |x-y| ≤ |x| + |y| := by
    simpa only [sub_eq_add_neg,abs_neg] using abs_add_le x (-y)
  apply (hab _ _).trans
  exact (add_le_add ((abs_add_le _ _).trans (add_le_add le_rfl (hb i))) hdiff).trans (hcheck i)

end
end WeilDefect
