import WeilDefect.Arithmetic.ActualZetaIV150AMConcreteCaps
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt

namespace WeilDefect
noncomputable section

/-- Actual arithmetic weight, with no numerical replacement of von Mangoldt. -/
def neutralIV151Weight (n : ℕ) : ℝ :=
  ArithmeticFunction.vonMangoldt n / Real.sqrt (n:ℝ)

theorem neutralIV151Weight_nonneg (n : ℕ) : 0 ≤ neutralIV151Weight n :=
  div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _)

theorem neutralIV151PrimePower (p k : ℕ) (hp : p.Prime) (hk : k ≠ 0) :
    ArithmeticFunction.vonMangoldt (p^k) = Real.log (p:ℝ) := by
  rw [ArithmeticFunction.vonMangoldt_apply_pow hk,
      ArithmeticFunction.vonMangoldt_apply_prime hp]

theorem neutralIV151Actual_2 :
    (Int.floor (Real.log (2:ℝ)*4096) = 2839 ∧
      Int.floor (-Real.log (2:ℝ)*4096) = -2840) ∧
    (0 ≤ neutralIV151Weight 2 ∧ neutralIV151Weight 2 < (490129072/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_2.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 2 = Real.log (2:ℝ) := by
    rw [show (2:ℕ) = 2^1 by decide]
    exact neutralIV151PrimePower 2 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_2.2

theorem neutralIV151Actual_3 :
    (Int.floor (Real.log (3:ℝ)*4096) = 4499 ∧
      Int.floor (-Real.log (3:ℝ)*4096) = -4500) ∧
    (0 ≤ neutralIV151Weight 3 ∧ neutralIV151Weight 3 < (634284101/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_3.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 3 = Real.log (3:ℝ) := by
    rw [show (3:ℕ) = 3^1 by decide]
    exact neutralIV151PrimePower 3 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_3.2

theorem neutralIV151Actual_4 :
    (Int.floor (Real.log (4:ℝ)*4096) = 5678 ∧
      Int.floor (-Real.log (4:ℝ)*4096) = -5679) ∧
    (0 ≤ neutralIV151Weight 4 ∧ neutralIV151Weight 4 < (346573591/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_4.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 4 = Real.log (2:ℝ) := by
    rw [show (4:ℕ) = 2^2 by decide]
    exact neutralIV151PrimePower 2 2 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_4.2

theorem neutralIV151Actual_5 :
    (Int.floor (Real.log (5:ℝ)*4096) = 6592 ∧
      Int.floor (-Real.log (5:ℝ)*4096) = -6593) ∧
    (0 ≤ neutralIV151Weight 5 ∧ neutralIV151Weight 5 < (719762516/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_5.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 5 = Real.log (5:ℝ) := by
    rw [show (5:ℕ) = 5^1 by decide]
    exact neutralIV151PrimePower 5 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_5.2

theorem neutralIV151Actual_7 :
    (Int.floor (Real.log (7:ℝ)*4096) = 7970 ∧
      Int.floor (-Real.log (7:ℝ)*4096) = -7971) ∧
    (0 ≤ neutralIV151Weight 7 ∧ neutralIV151Weight 7 < (735484905/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_7.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 7 = Real.log (7:ℝ) := by
    rw [show (7:ℕ) = 7^1 by decide]
    exact neutralIV151PrimePower 7 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_7.2

theorem neutralIV151Actual_8 :
    (Int.floor (Real.log (8:ℝ)*4096) = 8517 ∧
      Int.floor (-Real.log (8:ℝ)*4096) = -8518) ∧
    (0 ≤ neutralIV151Weight 8 ∧ neutralIV151Weight 8 < (245064536/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_8.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 8 = Real.log (2:ℝ) := by
    rw [show (8:ℕ) = 2^3 by decide]
    exact neutralIV151PrimePower 2 3 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_8.2

theorem neutralIV151Actual_9 :
    (Int.floor (Real.log (9:ℝ)*4096) = 8999 ∧
      Int.floor (-Real.log (9:ℝ)*4096) = -9000) ∧
    (0 ≤ neutralIV151Weight 9 ∧ neutralIV151Weight 9 < (366204097/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_9.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 9 = Real.log (3:ℝ) := by
    rw [show (9:ℕ) = 3^2 by decide]
    exact neutralIV151PrimePower 3 2 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_9.2

theorem neutralIV151Actual_11 :
    (Int.floor (Real.log (11:ℝ)*4096) = 9821 ∧
      Int.floor (-Real.log (11:ℝ)*4096) = -9822) ∧
    (0 ≤ neutralIV151Weight 11 ∧ neutralIV151Weight 11 < (722992628/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_11.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 11 = Real.log (11:ℝ) := by
    rw [show (11:ℕ) = 11^1 by decide]
    exact neutralIV151PrimePower 11 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_11.2

theorem neutralIV151Actual_13 :
    (Int.floor (Real.log (13:ℝ)*4096) = 10506 ∧
      Int.floor (-Real.log (13:ℝ)*4096) = -10507) ∧
    (0 ≤ neutralIV151Weight 13 ∧ neutralIV151Weight 13 < (711388956/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_13.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 13 = Real.log (13:ℝ) := by
    rw [show (13:ℕ) = 13^1 by decide]
    exact neutralIV151PrimePower 13 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_13.2

theorem neutralIV151Actual_16 :
    (Int.floor (Real.log (16:ℝ)*4096) = 11356 ∧
      Int.floor (-Real.log (16:ℝ)*4096) = -11357) ∧
    (0 ≤ neutralIV151Weight 16 ∧ neutralIV151Weight 16 < (173286796/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_16.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 16 = Real.log (2:ℝ) := by
    rw [show (16:ℕ) = 2^4 by decide]
    exact neutralIV151PrimePower 2 4 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_16.2

theorem neutralIV151Actual_17 :
    (Int.floor (Real.log (17:ℝ)*4096) = 11604 ∧
      Int.floor (-Real.log (17:ℝ)*4096) = -11605) ∧
    (0 ≤ neutralIV151Weight 17 ∧ neutralIV151Weight 17 < (687155170/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_17.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 17 = Real.log (17:ℝ) := by
    rw [show (17:ℕ) = 17^1 by decide]
    exact neutralIV151PrimePower 17 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_17.2

theorem neutralIV151Actual_19 :
    (Int.floor (Real.log (19:ℝ)*4096) = 12060 ∧
      Int.floor (-Real.log (19:ℝ)*4096) = -12061) ∧
    (0 ≤ neutralIV151Weight 19 ∧ neutralIV151Weight 19 < (675500630/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_19.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 19 = Real.log (19:ℝ) := by
    rw [show (19:ℕ) = 19^1 by decide]
    exact neutralIV151PrimePower 19 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_19.2

theorem neutralIV151Actual_23 :
    (Int.floor (Real.log (23:ℝ)*4096) = 12842 ∧
      Int.floor (-Real.log (23:ℝ)*4096) = -12843) ∧
    (0 ≤ neutralIV151Weight 23 ∧ neutralIV151Weight 23 < (653795740/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_23.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 23 = Real.log (23:ℝ) := by
    rw [show (23:ℕ) = 23^1 by decide]
    exact neutralIV151PrimePower 23 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_23.2

theorem neutralIV151Actual_25 :
    (Int.floor (Real.log (25:ℝ)*4096) = 13184 ∧
      Int.floor (-Real.log (25:ℝ)*4096) = -13185) ∧
    (0 ≤ neutralIV151Weight 25 ∧ neutralIV151Weight 25 < (321887583/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_25.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 25 = Real.log (5:ℝ) := by
    rw [show (25:ℕ) = 5^2 by decide]
    exact neutralIV151PrimePower 5 2 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_25.2

theorem neutralIV151Actual_27 :
    (Int.floor (Real.log (27:ℝ)*4096) = 13499 ∧
      Int.floor (-Real.log (27:ℝ)*4096) = -13500) ∧
    (0 ≤ neutralIV151Weight 27 ∧ neutralIV151Weight 27 < (211428034/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_27.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 27 = Real.log (3:ℝ) := by
    rw [show (27:ℕ) = 3^3 by decide]
    exact neutralIV151PrimePower 3 3 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_27.2

theorem neutralIV151Actual_29 :
    (Int.floor (Real.log (29:ℝ)*4096) = 13792 ∧
      Int.floor (-Real.log (29:ℝ)*4096) = -13793) ∧
    (0 ≤ neutralIV151Weight 29 ∧ neutralIV151Weight 29 < (625291138/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_29.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 29 = Real.log (29:ℝ) := by
    rw [show (29:ℕ) = 29^1 by decide]
    exact neutralIV151PrimePower 29 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_29.2

theorem neutralIV151Actual_31 :
    (Int.floor (Real.log (31:ℝ)*4096) = 14065 ∧
      Int.floor (-Real.log (31:ℝ)*4096) = -14066) ∧
    (0 ≤ neutralIV151Weight 31 ∧ neutralIV151Weight 31 < (616762310/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_31.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 31 = Real.log (31:ℝ) := by
    rw [show (31:ℕ) = 31^1 by decide]
    exact neutralIV151PrimePower 31 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_31.2

theorem neutralIV151Actual_32 :
    (Int.floor (Real.log (32:ℝ)*4096) = 14195 ∧
      Int.floor (-Real.log (32:ℝ)*4096) = -14196) ∧
    (0 ≤ neutralIV151Weight 32 ∧ neutralIV151Weight 32 < (122532268/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_32.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 32 = Real.log (2:ℝ) := by
    rw [show (32:ℕ) = 2^5 by decide]
    exact neutralIV151PrimePower 2 5 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_32.2

theorem neutralIV151Actual_37 :
    (Int.floor (Real.log (37:ℝ)*4096) = 14790 ∧
      Int.floor (-Real.log (37:ℝ)*4096) = -14791) ∧
    (0 ≤ neutralIV151Weight 37 ∧ neutralIV151Weight 37 < (593631249/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_37.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 37 = Real.log (37:ℝ) := by
    rw [show (37:ℕ) = 37^1 by decide]
    exact neutralIV151PrimePower 37 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_37.2

theorem neutralIV151Actual_41 :
    (Int.floor (Real.log (41:ℝ)*4096) = 15210 ∧
      Int.floor (-Real.log (41:ℝ)*4096) = -15211) ∧
    (0 ≤ neutralIV151Weight 41 ∧ neutralIV151Weight 41 < (579962520/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_41.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 41 = Real.log (41:ℝ) := by
    rw [show (41:ℕ) = 41^1 by decide]
    exact neutralIV151PrimePower 41 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_41.2

theorem neutralIV151Actual_43 :
    (Int.floor (Real.log (43:ℝ)*4096) = 15405 ∧
      Int.floor (-Real.log (43:ℝ)*4096) = -15406) ∧
    (0 ≤ neutralIV151Weight 43 ∧ neutralIV151Weight 43 < (573577641/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_43.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 43 = Real.log (43:ℝ) := by
    rw [show (43:ℕ) = 43^1 by decide]
    exact neutralIV151PrimePower 43 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_43.2

theorem neutralIV151Actual_47 :
    (Int.floor (Real.log (47:ℝ)*4096) = 15770 ∧
      Int.floor (-Real.log (47:ℝ)*4096) = -15771) ∧
    (0 ≤ neutralIV151Weight 47 ∧ neutralIV151Weight 47 < (561601748/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_47.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 47 = Real.log (47:ℝ) := by
    rw [show (47:ℕ) = 47^1 by decide]
    exact neutralIV151PrimePower 47 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_47.2

theorem neutralIV151Actual_49 :
    (Int.floor (Real.log (49:ℝ)*4096) = 15940 ∧
      Int.floor (-Real.log (49:ℝ)*4096) = -15941) ∧
    (0 ≤ neutralIV151Weight 49 ∧ neutralIV151Weight 49 < (277987165/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_49.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 49 = Real.log (7:ℝ) := by
    rw [show (49:ℕ) = 7^2 by decide]
    exact neutralIV151PrimePower 7 2 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_49.2

theorem neutralIV151Actual_53 :
    (Int.floor (Real.log (53:ℝ)*4096) = 16262 ∧
      Int.floor (-Real.log (53:ℝ)*4096) = -16263) ∧
    (0 ≤ neutralIV151Weight 53 ∧ neutralIV151Weight 53 < (545361537/1000000000:ℝ)) := by
  refine ⟨neutralIV150Prime_53.1, neutralIV151Weight_nonneg _, ?_⟩
  have he : ArithmeticFunction.vonMangoldt 53 = Real.log (53:ℝ) := by
    rw [show (53:ℕ) = 53^1 by decide]
    exact neutralIV151PrimePower 53 1 (by decide) (by decide)
  unfold neutralIV151Weight
  rw [he]
  exact neutralIV150Prime_53.2

#print axioms neutralIV151Weight_nonneg
#print axioms neutralIV151PrimePower
#print axioms neutralIV151Actual_2
#print axioms neutralIV151Actual_3
#print axioms neutralIV151Actual_4
#print axioms neutralIV151Actual_5
#print axioms neutralIV151Actual_7
#print axioms neutralIV151Actual_8
#print axioms neutralIV151Actual_9
#print axioms neutralIV151Actual_11
#print axioms neutralIV151Actual_13
#print axioms neutralIV151Actual_16
#print axioms neutralIV151Actual_17
#print axioms neutralIV151Actual_19
#print axioms neutralIV151Actual_23
#print axioms neutralIV151Actual_25
#print axioms neutralIV151Actual_27
#print axioms neutralIV151Actual_29
#print axioms neutralIV151Actual_31
#print axioms neutralIV151Actual_32
#print axioms neutralIV151Actual_37
#print axioms neutralIV151Actual_41
#print axioms neutralIV151Actual_43
#print axioms neutralIV151Actual_47
#print axioms neutralIV151Actual_49
#print axioms neutralIV151Actual_53

end
end WeilDefect
