import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalUniformPayments

namespace WeilDefect
open Finset

/-! NF625: finite rational payment gates. Centers, frame and
candidate are arbitrary rational proposals, not trusted numerical
values. The analytic enclosure hypotheses are supplied separately.
A subsequent integer implementation can replace these reference
formulas only via an exact equality theorem. -/

structure NF625PaymentData where
  D : Fin 242 → Fin 242 → ℚ
  H0 : Fin 242 → Fin 242 → ℚ
  V0 : Fin 242 → Fin 4 → ℚ
  y0 : Fin 242 → ℚ
  eH : ℚ
  eV : ℚ
  r : ℚ

def neutralNF625W (j : Fin 4) : ℚ :=
  (neutralNF604OriginalT4Numerators[j.val]! : ℚ)/2^20 -
    neutralNF604OriginalCriticalQ j

def neutralNF625Mid (i : Fin 242) : ℚ :=
  neutralNF589DyadicQ neutralNF587SelectedDyads[i.val]!.1

def neutralNF625Rad (i : Fin 242) : ℚ :=
  |neutralNF589DyadicQ neutralNF587SelectedDyads[i.val]!.2|

def NF625PaymentData.A (p : NF625PaymentData) (i j : Fin 242) : ℚ :=
  ∑ k, p.D k i * (∑ l, p.H0 k l * p.D l j)

def NF625PaymentData.b (p : NF625PaymentData) (i : Fin 242) : ℚ :=
  ∑ k, p.D k i * (∑ j : Fin 4, p.V0 k j * neutralNF625W j)

def NF625PaymentData.c (p : NF625PaymentData) (i : Fin 242) : ℚ :=
  ∑ k, |p.D k i|

def NF625PaymentData.row (p : NF625PaymentData) (i : Fin 242) : ℚ :=
  (∑ j, |(if i=j then (1:ℚ) else 0)-p.A i j|) +
    p.c i * ((∑ j, p.c j)*p.eH)

def NF625PaymentData.residual (p : NF625PaymentData) (i : Fin 242) : ℚ :=
  |p.b i-(∑ j, p.A i j*p.y0 j)| +
    p.c i * ((∑ j : Fin 4, |neutralNF625W j|)*p.eV) +
    p.c i * ((∑ j, |p.y0 j| * p.c j)*p.eH)

def NF625PaymentData.payment (p : NF625PaymentData) (i : Fin 242) : ℚ :=
  |(∑ j, p.D i j*p.y0 j)-neutralNF625Mid i| +
    (∑ j, |p.D i j|)*(2*p.r)

def NF625PaymentData.rowCheck (p : NF625PaymentData) (i : Fin 242) : Bool :=
  decide (p.row i ≤ 1/100 ∧ p.residual i ≤ p.r ∧
    p.payment i ≤ neutralNF625Rad i)

def NF625PaymentData.check (p : NF625PaymentData) : Bool :=
  decide (0≤p.r ∧ 0≤p.eH ∧ 0≤p.eV) &&
    (List.finRange 242).all p.rowCheck

noncomputable section

theorem neutralNF625W_cast (j : Fin 4) :
    (neutralNF625W j:ℝ) = neutralNF606PhysicalW j := by
  unfold neutralNF625W neutralNF606PhysicalW
  push_cast
  rw [neutralNF604Critical_cast]

theorem neutralNF625Mid_cast (i : Fin 242) :
    (neutralNF625Mid i:ℝ) = neutralNF587SelectedMid i := by
  unfold neutralNF625Mid neutralNF587SelectedMid
  exact neutralNF589Dyadic_cast _

theorem neutralNF625Rad_cast (i : Fin 242) :
    (neutralNF625Rad i:ℝ) = neutralNF587SelectedRadius i := by
  unfold neutralNF625Rad neutralNF587SelectedRadius
  rw [Rat.cast_abs,neutralNF589Dyadic_cast]

def NF625PaymentData.DR (p : NF625PaymentData) : Fin 242 → Fin 242 → ℝ :=
  fun i j => (p.D i j:ℝ)

def NF625PaymentData.HR (p : NF625PaymentData) : Fin 242 → Fin 242 → ℝ :=
  fun i j => (p.H0 i j:ℝ)

def NF625PaymentData.VR (p : NF625PaymentData) : Fin 242 → Fin 4 → ℝ :=
  fun i j => (p.V0 i j:ℝ)

def NF625PaymentData.yR (p : NF625PaymentData) : Fin 242 → ℝ :=
  fun i => (p.y0 i:ℝ)

theorem NF625PaymentData.A_cast (p : NF625PaymentData) (i j : Fin 242) :
    (p.A i j:ℝ) = neutralNF613GramCenter p.DR p.HR i j := by
  unfold A neutralNF613GramCenter DR HR
  push_cast <;> rfl

theorem NF625PaymentData.b_cast (p : NF625PaymentData) (i : Fin 242) :
    (p.b i:ℝ) = neutralNF613RHSCenter p.DR p.VR i := by
  unfold b neutralNF613RHSCenter DR VR
  push_cast
  simp only [neutralNF625W_cast]

theorem NF625PaymentData.c_cast (p : NF625PaymentData) (i : Fin 242) :
    (p.c i:ℝ) = neutralNF623ColMass p.DR i := by
  unfold c neutralNF623ColMass DR
  push_cast <;> rfl

theorem NF625PaymentData.row_cast (p : NF625PaymentData) (i : Fin 242) :
    (p.row i:ℝ) =
      (∑ j, |neutralNF606Defect (neutralNF613GramCenter p.DR p.HR) i j|) +
      neutralNF623ColMass p.DR i *
        ((∑ j, neutralNF623ColMass p.DR j)*(p.eH:ℝ)) := by
  unfold row neutralNF606Defect
  push_cast
  simp only [p.A_cast,p.c_cast]
  congr 1
  apply Finset.sum_congr rfl
  intro j _
  split_ifs <;> norm_num

theorem NF625PaymentData.residual_cast (p : NF625PaymentData) (i : Fin 242) :
    (p.residual i:ℝ) =
      |neutralNF613RHSCenter p.DR p.VR i-
        neutralNF606Apply (neutralNF613GramCenter p.DR p.HR) p.yR i| +
      neutralNF623ColMass p.DR i * (neutralNF623WMass*(p.eV:ℝ)) +
      neutralNF623ColMass p.DR i *
        ((∑ j, |p.yR j| * neutralNF623ColMass p.DR j)*(p.eH:ℝ)) := by
  unfold residual neutralNF606Apply neutralNF623WMass yR
  push_cast
  simp only [p.A_cast,p.b_cast,p.c_cast,neutralNF625W_cast]

theorem NF625PaymentData.payment_cast (p : NF625PaymentData) (i : Fin 242) :
    (p.payment i:ℝ) =
      |neutralNF606Apply p.DR p.yR i-neutralNF587SelectedMid i| +
        neutralNF623RowMass p.DR i*(2*(p.r:ℝ)) := by
  unfold payment neutralNF606Apply neutralNF623RowMass DR yR
  push_cast
  rw [neutralNF625Mid_cast]

theorem NF625PaymentData.check_sound (p : NF625PaymentData)
    (hc : p.check=true)
    (hH : ∀ i j, |neutralNF606PhysicalH i j-p.HR i j| ≤ (p.eH:ℝ))
    (hV : ∀ i j, |neutralNF606PhysicalV i j-p.VR i j| ≤ (p.eV:ℝ)) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  unfold check at hc
  simp only [Bool.and_eq_true] at hc
  have hparam : 0≤p.r ∧ 0≤p.eH ∧ 0≤p.eV := of_decide_eq_true hc.1
  have hrow (i : Fin 242) : p.row i≤1/100 ∧ p.residual i≤p.r ∧
      p.payment i≤neutralNF625Rad i := by
    have h := (List.all_eq_true.mp hc.2) i (by simp)
    exact of_decide_eq_true h
  apply neutralNF623OriginalPhysicalSolve_of_uniform_entries p.DR p.HR p.VR
    (p.eH:ℝ) (p.eV:ℝ) p.yR (p.r:ℝ) (by exact_mod_cast hparam.1) hH hV
  · intro i
    rw [← p.row_cast]
    have he : (p.row i:ℝ) ≤ ((1/100:ℚ):ℝ) := Rat.cast_le.mpr (hrow i).1
    norm_num at he ⊢
    exact he
  · intro i
    rw [← p.residual_cast]
    exact_mod_cast (hrow i).2.1
  · intro i
    rw [← p.payment_cast,← neutralNF625Rad_cast]
    exact_mod_cast (hrow i).2.2

end
end WeilDefect
