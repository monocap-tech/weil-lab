import WeilDefect.Arithmetic.ActualZetaOriginalCriticalSolveCustody

namespace WeilDefect
noncomputable section
open Finset

/-! NF606: residual certificate for the HISTORICAL physical solve.
The near-identity test is on DᵀHD, not the collar Gram.
All hypotheses are real inequalities. No interval solver or external
receipt is introduced as a Lean axiom. -/

def neutralNF606Apply {n : ℕ} (A : Fin n → Fin n → ℝ)
    (x : Fin n → ℝ) (i : Fin n) : ℝ :=
  ∑ j, A i j * x j

def neutralNF606Defect {n : ℕ} (A : Fin n → Fin n → ℝ)
    (i j : Fin n) : ℝ := (if i=j then 1 else 0)-A i j

theorem neutralNF606Defect_apply {n : ℕ} (A : Fin n → Fin n → ℝ)
    (x : Fin n → ℝ) (i : Fin n) :
    neutralNF606Apply (neutralNF606Defect A) x i =
      x i-neutralNF606Apply A x i := by
  unfold neutralNF606Apply neutralNF606Defect
  simp_rw [sub_mul]
  rw [sum_sub_distrib]
  simp

theorem neutralNF606Apply_sub {n : ℕ} (A : Fin n → Fin n → ℝ)
    (x y : Fin n → ℝ) (i : Fin n) :
    neutralNF606Apply A (fun j => x j-y j) i =
      neutralNF606Apply A x i-neutralNF606Apply A y i := by
  unfold neutralNF606Apply
  simp_rw [mul_sub]
  rw [sum_sub_distrib]

theorem neutralNF606Row_bound {n : ℕ} (A : Fin n → Fin n → ℝ)
    (x : Fin n → ℝ) (M : ℝ) (hm : ∀ j, |x j| ≤ M) (i : Fin n) :
    |neutralNF606Apply A x i| ≤ (∑ j, |A i j|)*M := by
  unfold neutralNF606Apply
  apply (abs_sum_le_sum_abs _ _).trans
  rw [sum_mul]
  apply sum_le_sum
  intro j _
  rw [abs_mul]
  exact mul_le_mul_of_nonneg_left (hm j) (abs_nonneg _)

/-- The inverse need not be evaluated to validate its solution.
A residual r and uniform row defect ≤ 1/100 imply error ≤ 2r.
The proof uses the largest error coordinate of the exact solution. -/
theorem neutralNF606Residual_bound {n : ℕ}
    (A : Fin n → Fin n → ℝ) (y y0 rhs : Fin n → ℝ)
    (r : ℝ) (hr : 0≤r)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect A i j|) ≤ 1/100)
    (hsolve : ∀ i, neutralNF606Apply A y i=rhs i)
    (hres : ∀ i, |rhs i-neutralNF606Apply A y0 i| ≤ r)
    (i : Fin n) :
    |y i-y0 i| ≤ 2*r := by
  let e := fun j => y j-y0 j
  obtain ⟨k,_,hk⟩ := Finset.exists_max_image (Finset.univ : Finset (Fin n))
    (fun j => |e j|) ⟨i,Finset.mem_univ _⟩
  have hmax (j : Fin n) : |e j| ≤ |e k| := hk j (Finset.mem_univ _)
  have hd : e k = (rhs k-neutralNF606Apply A y0 k)+
      neutralNF606Apply (neutralNF606Defect A) e k := by
    rw [neutralNF606Defect_apply]
    have he : neutralNF606Apply A e k =
        rhs k-neutralNF606Apply A y0 k := by
      dsimp only [e]
      rw [neutralNF606Apply_sub,hsolve]
    linarith only [he]
  have hb := (neutralNF606Row_bound (neutralNF606Defect A) e _ hmax k).trans
    (mul_le_mul_of_nonneg_right (hrow k) (abs_nonneg _))
  have hv : |e k| ≤ r+(1/100:ℝ)*|e k| := by
    calc
      _ = |(rhs k-neutralNF606Apply A y0 k)+
            neutralNF606Apply (neutralNF606Defect A) e k| := congrArg abs hd
      _ ≤ _ := (abs_add_le _ _).trans (add_le_add (hres k) hb)
  exact (hmax i).trans (by linarith only [hv,hr])

/-- Push the transformed residual radius through the *actual*
dyadic frame, with one row-specific cost for each physical coefficient. -/
theorem neutralNF606Selected_box_of_residual
    (A D : Fin 242 → Fin 242 → ℝ)
    (y y0 rhs : Fin 242 → ℝ) (r : ℝ) (hr : 0≤r)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect A i j|) ≤ 1/100)
    (hsolve : ∀ i, neutralNF606Apply A y i=rhs i)
    (hres : ∀ i, |rhs i-neutralNF606Apply A y0 i| ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i|+
      (∑ j, |D i j|)*(2*r) ≤ neutralNF587SelectedRadius i) :
    neutralNF587SourceInFrozenBox (neutralNF606Apply D y) neutralNF604OriginalCritical := by
  apply neutralNF604Box_of_selected
  intro i
  have he (j : Fin 242) : |y j-y0 j| ≤ 2*r :=
    neutralNF606Residual_bound A y y0 rhs r hr hrow hsolve hres j
  have hD := neutralNF606Row_bound D (fun j => y j-y0 j) (2*r) he i
  rw [neutralNF606Apply_sub] at hD
  calc
    _ = |(neutralNF606Apply D y0 i-neutralNF587SelectedMid i)+
          (neutralNF606Apply D y i-neutralNF606Apply D y0 i)| := by congr 1 <;> ring
    _ ≤ _ := (abs_add_le _ _).trans (add_le_add le_rfl hD)
    _ ≤ _ := hpay i

end
end WeilDefect
