import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSolveExistence

namespace WeilDefect
noncomputable section
open Finset

/-! NF612: the row certificate on DᵀHD forces the square frame D
and its transpose to be invertible. No extra determinant receipt
is needed. This is generic in D; historic dyads remain external
to this theorem. -/

def neutralNF612Transpose {n : ℕ} (D : Fin n → Fin n → ℝ) :
    Fin n → Fin n → ℝ := fun i j => D j i

def neutralNF612RHS (i : Fin 242) : ℝ :=
  ∑ j : Fin 4, neutralNF606PhysicalV i j * neutralNF606PhysicalW j

theorem neutralNF612Transformed_apply (D : Fin 242 → Fin 242 → ℝ)
    (y : Fin 242 → ℝ) :
    neutralNF606Apply (neutralNF606TransformedH D) y =
      neutralNF606Apply (neutralNF612Transpose D)
        (neutralNF606Apply neutralNF606PhysicalH (neutralNF606Apply D y)) := by
  funext i
  unfold neutralNF606Apply neutralNF606TransformedH neutralNF612Transpose
  simp_rw [Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro k _
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro l _
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro j _
  ring

theorem neutralNF612Transformed_rhs (D : Fin 242 → Fin 242 → ℝ) :
    neutralNF606TransformedRHS D =
      neutralNF606Apply (neutralNF612Transpose D) neutralNF612RHS := by
  rfl

theorem neutralNF612Injective_iff_surjective {n : ℕ}
    (D : Fin n → Fin n → ℝ) :
    Function.Injective (neutralNF606Apply D) ↔
      Function.Surjective (neutralNF606Apply D) := by
  change Function.Injective (neutralNF611LinearApply D) ↔
    Function.Surjective (neutralNF611LinearApply D)
  first
  | exact LinearMap.injective_iff_surjective
  | exact LinearMap.injective_iff_surjective (neutralNF611LinearApply D)
  | exact FiniteDimensional.injective_iff_surjective
  | exact FiniteDimensional.injective_iff_surjective (neutralNF611LinearApply D)

theorem neutralNF612Frame_bijective (D : Fin 242 → Fin 242 → ℝ)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100) :
    Function.Bijective (neutralNF606Apply D) ∧
      Function.Bijective (neutralNF606Apply (neutralNF612Transpose D)) := by
  have hA : Function.Injective (neutralNF606Apply (neutralNF606TransformedH D)) :=
    neutralNF611LinearApply_injective _ hrow
  have hi : Function.Injective (neutralNF606Apply D) := by
    intro x y h
    apply hA
    rw [neutralNF612Transformed_apply,neutralNF612Transformed_apply,h]
  have ht : Function.Surjective (neutralNF606Apply (neutralNF612Transpose D)) := by
    intro b
    obtain ⟨y,hy⟩ := (neutralNF612Injective_iff_surjective _).mp hA b
    refine ⟨neutralNF606Apply neutralNF606PhysicalH (neutralNF606Apply D y),?_⟩
    rw [← neutralNF612Transformed_apply]
    exact hy
  exact ⟨⟨hi,(neutralNF612Injective_iff_surjective D).mp hi⟩,
    ⟨(neutralNF612Injective_iff_surjective _).mpr ht,ht⟩⟩

/-- The transformed equation is exactly the untransformed equation
at a=D y, not merely a projected necessary condition. -/
theorem neutralNF612Physical_equiv (D : Fin 242 → Fin 242 → ℝ)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100)
    (y : Fin 242 → ℝ) :
    (∀ i, neutralNF606Apply (neutralNF606TransformedH D) y i =
        neutralNF606TransformedRHS D i) ↔
      neutralNF606Apply neutralNF606PhysicalH (neutralNF606Apply D y) = neutralNF612RHS := by
  constructor
  · intro h
    apply (neutralNF612Frame_bijective D hrow).2.1
    rw [← neutralNF612Transformed_apply,← neutralNF612Transformed_rhs]
    exact funext h
  · intro h i
    have he : neutralNF606Apply (neutralNF606TransformedH D) y =
        neutralNF606TransformedRHS D := by
      rw [neutralNF612Transformed_apply,neutralNF612Transformed_rhs,h]
    exact congrFun he i

theorem neutralNF612PhysicalH_bijective (D : Fin 242 → Fin 242 → ℝ)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100) :
    Function.Bijective (neutralNF606Apply neutralNF606PhysicalH) := by
  have hD := (neutralNF612Frame_bijective D hrow).1
  have hi : Function.Injective (neutralNF606Apply neutralNF606PhysicalH) := by
    intro a b h
    obtain ⟨x,hx⟩ := hD.2 a
    obtain ⟨y,hy⟩ := hD.2 b
    have hxy : x=y := by
      apply (show Function.Injective (neutralNF606Apply (neutralNF606TransformedH D)) from
        neutralNF611LinearApply_injective _ hrow)
      rw [neutralNF612Transformed_apply,neutralNF612Transformed_apply,hx,hy,h]
    calc
      a = neutralNF606Apply D x := hx.symm
      _ = neutralNF606Apply D y := congrArg (neutralNF606Apply D) hxy
      _ = b := hy
  exact ⟨hi,(neutralNF612Injective_iff_surjective _).mp hi⟩

theorem neutralNF612OriginalPhysicalSolve (D : Fin 242 → Fin 242 → ℝ)
    (y0 : Fin 242 → ℝ) (r : ℝ) (hr : 0≤r)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100)
    (hres : ∀ i, |neutralNF606TransformedRHS D i -
      neutralNF606Apply (neutralNF606TransformedH D) y0 i| ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i|+
      (∑ j, |D i j|)*(2*r) ≤ neutralNF587SelectedRadius i) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  obtain ⟨y,⟨hy,hbox⟩,_⟩ := neutralNF611PhysicalSolve_box D y0 r hr hrow hres hpay
  have he := (neutralNF612Physical_equiv D hrow y).mp hy
  refine ⟨neutralNF606Apply D y,⟨he,hbox⟩,?_⟩
  intro a ha
  exact (neutralNF612PhysicalH_bijective D hrow).1 (ha.1.trans he.symm)

end
end WeilDefect
