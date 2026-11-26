import WeilDefect.Arithmetic.ActualZetaIV106E3WeightedChains
import Mathlib

namespace WeilDefect
noncomputable section
open scoped BigOperators Matrix

/-- Rational upper bounds using range reduction and Mathlib's certified log remainder. -/
theorem neutralIV106E4Log_upper :
    Real.log 2 ≤ (693147181/1000000000:ℝ) ∧
    Real.log 3 ≤ (1098612289/1000000000:ℝ) ∧
    Real.log 5 ≤ (1609437913/1000000000:ℝ) ∧
    Real.log 7 ≤ (1945910150/1000000000:ℝ) := by
  have h2 := Real.log_div_le_sum_range_add (x := (1/3:ℝ)) (by norm_num) (by norm_num) 12
  have h3 := Real.log_div_le_sum_range_add (x := (1/5:ℝ)) (by norm_num) (by norm_num) 12
  have h5 := Real.log_div_le_sum_range_add (x := (1/9:ℝ)) (by norm_num) (by norm_num) 12
  have h7 := Real.log_div_le_sum_range_add (x := (3/11:ℝ)) (by norm_num) (by norm_num) 12
  norm_num [Finset.sum_range_succ] at h2 h3 h5 h7
  have e3 : Real.log 3 = Real.log 2 + Real.log (3/2) := by
    rw [← Real.log_mul (by norm_num) (by norm_num)]
    norm_num
  have e5 : Real.log 5 = 2*Real.log 2 + Real.log (5/4) := by
    rw [← Real.log_pow, ← Real.log_mul (by norm_num) (by norm_num)]
    norm_num
  have e7 : Real.log 7 = 2*Real.log 2 + Real.log (7/4) := by
    rw [← Real.log_pow, ← Real.log_mul (by norm_num) (by norm_num)]
    norm_num
  rw [e3,e5,e7]
  exact ⟨by linarith only [h2], by linarith only [h2,h3],
    by linarith only [h2,h5], by linarith only [h2,h7]⟩

/-- Positive denominator comparison for a log divided by a square root. -/
theorem neutralIV106E4Coefficient_receiver (p n U d c : ℝ)
    (hn : 0 < n) (hd : 0 ≤ d) (hs : d^2 ≤ n)
    (hlog : Real.log p ≤ U) (hc : 0 ≤ c) (hb : U ≤ c*d) :
    Real.log p / Real.sqrt n ≤ c := by
  have hroot := (Real.le_sqrt hd hn.le).mpr hs
  apply (div_le_iff₀ (Real.sqrt_pos.2 hn)).mpr
  exact hlog.trans (hb.trans (mul_le_mul_of_nonneg_left hroot hc))

/-- All seven literal prime-power coefficient upper bounds. -/
theorem neutralIV106E4Coefficients :
    Real.log 2 / Real.sqrt 2 ≤ (490130/1000000:ℝ) ∧
    Real.log 2 / Real.sqrt 4 ≤ (346574/1000000:ℝ) ∧
    Real.log 2 / Real.sqrt 8 ≤ (245065/1000000:ℝ) ∧
    Real.log 3 / Real.sqrt 3 ≤ (634285/1000000:ℝ) ∧
    Real.log 3 / Real.sqrt 9 ≤ (366205/1000000:ℝ) ∧
    Real.log 5 / Real.sqrt 5 ≤ (719763/1000000:ℝ) ∧
    Real.log 7 / Real.sqrt 7 ≤ (735485/1000000:ℝ) := by
  obtain ⟨h2,h3,h5,h7⟩ := neutralIV106E4Log_upper
  refine ⟨?_,?_,?_,?_,?_,?_,?_⟩
  · exact neutralIV106E4Coefficient_receiver 2 2 (693147181/1000000000)
      (1414213562/1000000000) (490130/1000000) (by norm_num) (by norm_num)
      (by norm_num) h2 (by norm_num) (by norm_num)
  · exact neutralIV106E4Coefficient_receiver 2 4 (693147181/1000000000)
      (2000000000/1000000000) (346574/1000000) (by norm_num) (by norm_num)
      (by norm_num) h2 (by norm_num) (by norm_num)
  · exact neutralIV106E4Coefficient_receiver 2 8 (693147181/1000000000)
      (2828427124/1000000000) (245065/1000000) (by norm_num) (by norm_num)
      (by norm_num) h2 (by norm_num) (by norm_num)
  · exact neutralIV106E4Coefficient_receiver 3 3 (1098612289/1000000000)
      (1732050807/1000000000) (634285/1000000) (by norm_num) (by norm_num)
      (by norm_num) h3 (by norm_num) (by norm_num)
  · exact neutralIV106E4Coefficient_receiver 3 9 (1098612289/1000000000)
      (3000000000/1000000000) (366205/1000000) (by norm_num) (by norm_num)
      (by norm_num) h3 (by norm_num) (by norm_num)
  · exact neutralIV106E4Coefficient_receiver 5 5 (1609437913/1000000000)
      (2236067977/1000000000) (719763/1000000) (by norm_num) (by norm_num)
      (by norm_num) h5 (by norm_num) (by norm_num)
  · exact neutralIV106E4Coefficient_receiver 7 7 (1945910150/1000000000)
      (2645751311/1000000000) (735485/1000000) (by norm_num) (by norm_num)
      (by norm_num) h7 (by norm_num) (by norm_num)

def neutralIV106E4Matrix2 : Matrix (Fin 4) (Fin 4) ℝ :=
  !![0,490130/1000000,346574/1000000,245065/1000000; 490130/1000000,0,490130/1000000,346574/1000000; 346574/1000000,490130/1000000,0,490130/1000000; 245065/1000000,346574/1000000,490130/1000000,0]

def neutralIV106E4Weight2 : Fin 4 → ℝ := ![864,1000,1000,864]

theorem neutralIV106E4Rows2 :
    (∀ i j, 0 ≤ neutralIV106E4Matrix2 i j) ∧
    (∀ i j, neutralIV106E4Matrix2 i j = neutralIV106E4Matrix2 j i) ∧
    (∀ i, 0 < neutralIV106E4Weight2 i) ∧
    (∀ i, ∑ j, neutralIV106E4Matrix2 i j *
      (neutralIV106E4Weight2 j / neutralIV106E4Weight2 i) ≤ (1214000/1000000:ℝ)) := by
  refine ⟨?_,?_,?_,?_⟩
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix2]
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix2]
  · intro i; fin_cases i <;> norm_num [neutralIV106E4Weight2]
  · intro i; fin_cases i <;> norm_num [Fin.sum_univ_succ, neutralIV106E4Matrix2, neutralIV106E4Weight2]

def neutralIV106E4Matrix3 : Matrix (Fin 3) (Fin 3) ℝ :=
  !![0,634285/1000000,366205/1000000; 634285/1000000,0,634285/1000000; 366205/1000000,634285/1000000,0]

def neutralIV106E4Weight3 : Fin 3 → ℝ := ![1000,1155,1000]

theorem neutralIV106E4Rows3 :
    (∀ i j, 0 ≤ neutralIV106E4Matrix3 i j) ∧
    (∀ i j, neutralIV106E4Matrix3 i j = neutralIV106E4Matrix3 j i) ∧
    (∀ i, 0 < neutralIV106E4Weight3 i) ∧
    (∀ i, ∑ j, neutralIV106E4Matrix3 i j *
      (neutralIV106E4Weight3 j / neutralIV106E4Weight3 i) ≤ (1099000/1000000:ℝ)) := by
  refine ⟨?_,?_,?_,?_⟩
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix3]
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix3]
  · intro i; fin_cases i <;> norm_num [neutralIV106E4Weight3]
  · intro i; fin_cases i <;> norm_num [Fin.sum_univ_succ, neutralIV106E4Matrix3, neutralIV106E4Weight3]

def neutralIV106E4Matrix5 : Matrix (Fin 2) (Fin 2) ℝ :=
  !![0,719763/1000000; 719763/1000000,0]

def neutralIV106E4Weight5 : Fin 2 → ℝ := ![1,1]

theorem neutralIV106E4Rows5 :
    (∀ i j, 0 ≤ neutralIV106E4Matrix5 i j) ∧
    (∀ i j, neutralIV106E4Matrix5 i j = neutralIV106E4Matrix5 j i) ∧
    (∀ i, 0 < neutralIV106E4Weight5 i) ∧
    (∀ i, ∑ j, neutralIV106E4Matrix5 i j *
      (neutralIV106E4Weight5 j / neutralIV106E4Weight5 i) ≤ (719763/1000000:ℝ)) := by
  refine ⟨?_,?_,?_,?_⟩
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix5]
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix5]
  · intro i; fin_cases i <;> norm_num [neutralIV106E4Weight5]
  · intro i; fin_cases i <;> norm_num [Fin.sum_univ_succ, neutralIV106E4Matrix5, neutralIV106E4Weight5]

def neutralIV106E4Matrix7 : Matrix (Fin 2) (Fin 2) ℝ :=
  !![0,735485/1000000; 735485/1000000,0]

def neutralIV106E4Weight7 : Fin 2 → ℝ := ![1,1]

theorem neutralIV106E4Rows7 :
    (∀ i j, 0 ≤ neutralIV106E4Matrix7 i j) ∧
    (∀ i j, neutralIV106E4Matrix7 i j = neutralIV106E4Matrix7 j i) ∧
    (∀ i, 0 < neutralIV106E4Weight7 i) ∧
    (∀ i, ∑ j, neutralIV106E4Matrix7 i j *
      (neutralIV106E4Weight7 j / neutralIV106E4Weight7 i) ≤ (735485/1000000:ℝ)) := by
  refine ⟨?_,?_,?_,?_⟩
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix7]
  · intro i j; fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E4Matrix7]
  · intro i; fin_cases i <;> norm_num [neutralIV106E4Weight7]
  · intro i; fin_cases i <;> norm_num [Fin.sum_univ_succ, neutralIV106E4Matrix7, neutralIV106E4Weight7]

/-- Entrywise domination by a rational upper matrix transfers its row bound
to the actual symmetric matrix. -/
theorem neutralIV106E4Dominated_chain {ι : Type*} [Fintype ι]
    (A B : ι → ι → ℝ) (w : ι → ℝ) (z : ι → ℂ) (L : ℝ)
    (hA : ∀ i j, 0 ≤ A i j) (hs : ∀ i j, A i j = A j i)
    (hAB : ∀ i j, A i j ≤ B i j) (hw : ∀ i, 0 < w i)
    (hr : ∀ i, ∑ j, B i j*(w j/w i) ≤ L) :
    (∑ i, ∑ j, A i j*(star (z i)*z j).re) ≤ L*∑ i, ‖z i‖^2 := by
  apply neutralIV106E3Complex_chain A w z L hA hs hw
  intro i
  refine le_trans (Finset.sum_le_sum (fun j _ => ?_)) (hr i)
  exact mul_le_mul_of_nonneg_right (hAB i j) (div_nonneg (hw j).le (hw i).le)

#print axioms neutralIV106E4Log_upper
#print axioms neutralIV106E4Coefficient_receiver
#print axioms neutralIV106E4Coefficients
#print axioms neutralIV106E4Rows2
#print axioms neutralIV106E4Rows3
#print axioms neutralIV106E4Rows5
#print axioms neutralIV106E4Rows7
#print axioms neutralIV106E4Dominated_chain
end
end WeilDefect
