import WeilDefect.Arithmetic.ActualZetaIV106E4PrimeCoefficients
import WeilDefect.Arithmetic.ActualZetaIV106E5TranslationFibers
import WeilDefect.Arithmetic.ActualZetaIV106E6PairedLagMatrices
import WeilDefect.Arithmetic.ActualZetaIV106E7PrimeCutoff
import WeilDefect.Arithmetic.ActualZetaIV106E8OriginalCorrelation

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators Matrix SchwartzMap

def neutralIV106E9Lag (v : ℝ → ℂ) (s : ℝ) : ℝ :=
  ∫ x : ℝ, (star (v x)*v (x+s)).re

def neutralIV106E9Mass (v : ℝ → ℂ) : ℝ :=
  ∫ x : ℝ, ‖v x‖^2

/-- Padded physical chain bound, with an explicit pointwise matrix premise. -/
theorem neutralIV106E9Physical2 (v : ℝ → ℂ) (hv : Continuous v)
    (l b s L c1 : ℝ) (hs : 0 < s) (hlb : l ≤ b)
    (hb : b ≤ l+2*s) (hout : ∀ x ∉ Set.Icc l b, v x = 0)
    (hmat : ∀ z : Fin 2 → ℂ,
      (∑ i, ∑ j, neutralIV106E6LagMatrix2 c1 i j*(star (z i)*z j).re) ≤
        L*∑ i, ‖z i‖^2) :
    2*(c1*neutralIV106E9Lag v (s)) ≤ L*neutralIV106E9Mass v := by
  let z (t : ℝ) (i : Fin 2) : ℂ := v (t+(l+(i.val:ℝ)*s))
  let f1 (t : ℝ) : ℝ := (star (z t 0)*z t 1).re
  have hf1 : Continuous f1 := by dsimp [f1,z]; fun_prop
  have hI1 : (∫ t in (0:ℝ)..s, f1 t) =
      neutralIV106E9Lag v (s) := by
    have h1 := neutralIV106E5Shift v hv l b s 2 1 hlb (by simpa using hb) hout
    have h2 := neutralIV106E5Truncate v l b s 2 1 hs (by simpa using hb) hout
    have he := h2.symm.trans h1
    norm_num [Finset.sum_range_succ, f1, z, neutralIV106E9Lag] at he ⊢
    exact he
  let M (t : ℝ) : ℝ := ∑ i : Fin 2, ‖z t i‖^2
  let F (t : ℝ) : ℝ := 2*(c1*f1 t)
  have hM : Continuous M := by
    simp only [M,Fin.sum_univ_succ,Fin.sum_univ_zero,z]
    fun_prop
  have hF : Continuous F := by
    dsimp [F]
    fun_prop
  have hm : (∫ t in (0:ℝ)..s, M t) = neutralIV106E9Mass v := by
    have h := neutralIV106E5Mass v hv l b s 2 hlb (by simpa using hb) hout
    norm_num [M,z,Fin.sum_univ_succ,Finset.sum_range_succ,neutralIV106E9Mass] at h ⊢
    exact h
  have hP : (∫ t in (0:ℝ)..s, F t) = 2*(c1*neutralIV106E9Lag v (s)) := by
    dsimp [F]
    rw [intervalIntegral.integral_const_mul]
    have hC1 : Continuous (fun t => c1*f1 t) := continuous_const.mul hf1
    simp only [intervalIntegral.integral_const_mul, hI1]
  apply neutralIV106E6Integral_receiver F M s L _ _ hs.le hF hM _ hP hm
  intro t ht
  have h := hmat (z t)
  rw [neutralIV106E6Lag2] at h
  exact h

/-- Padded physical chain bound, with an explicit pointwise matrix premise. -/
theorem neutralIV106E9Physical3 (v : ℝ → ℂ) (hv : Continuous v)
    (l b s L c1 c2 : ℝ) (hs : 0 < s) (hlb : l ≤ b)
    (hb : b ≤ l+3*s) (hout : ∀ x ∉ Set.Icc l b, v x = 0)
    (hmat : ∀ z : Fin 3 → ℂ,
      (∑ i, ∑ j, neutralIV106E6LagMatrix3 c1 c2 i j*(star (z i)*z j).re) ≤
        L*∑ i, ‖z i‖^2) :
    2*(c1*neutralIV106E9Lag v (s)+c2*neutralIV106E9Lag v (2*s)) ≤ L*neutralIV106E9Mass v := by
  let z (t : ℝ) (i : Fin 3) : ℂ := v (t+(l+(i.val:ℝ)*s))
  let f1 (t : ℝ) : ℝ := (star (z t 0)*z t 1).re+(star (z t 1)*z t 2).re
  let f2 (t : ℝ) : ℝ := (star (z t 0)*z t 2).re
  have hf1 : Continuous f1 := by dsimp [f1,z]; fun_prop
  have hI1 : (∫ t in (0:ℝ)..s, f1 t) =
      neutralIV106E9Lag v (s) := by
    have h1 := neutralIV106E5Shift v hv l b s 3 1 hlb (by simpa using hb) hout
    have h2 := neutralIV106E5Truncate v l b s 3 1 hs (by simpa using hb) hout
    have he := h2.symm.trans h1
    norm_num [Finset.sum_range_succ, f1, z, neutralIV106E9Lag] at he ⊢
    exact he
  have hf2 : Continuous f2 := by dsimp [f2,z]; fun_prop
  have hI2 : (∫ t in (0:ℝ)..s, f2 t) =
      neutralIV106E9Lag v (2*s) := by
    have h1 := neutralIV106E5Shift v hv l b s 3 2 hlb (by simpa using hb) hout
    have h2 := neutralIV106E5Truncate v l b s 3 2 hs (by simpa using hb) hout
    have he := h2.symm.trans h1
    norm_num [Finset.sum_range_succ, f2, z, neutralIV106E9Lag] at he ⊢
    exact he
  let M (t : ℝ) : ℝ := ∑ i : Fin 3, ‖z t i‖^2
  let F (t : ℝ) : ℝ := 2*(c1*f1 t+c2*f2 t)
  have hM : Continuous M := by
    simp only [M,Fin.sum_univ_succ,Fin.sum_univ_zero,z]
    fun_prop
  have hF : Continuous F := by
    dsimp [F]
    fun_prop
  have hm : (∫ t in (0:ℝ)..s, M t) = neutralIV106E9Mass v := by
    have h := neutralIV106E5Mass v hv l b s 3 hlb (by simpa using hb) hout
    norm_num [M,z,Fin.sum_univ_succ,Finset.sum_range_succ,neutralIV106E9Mass] at h ⊢
    exact h
  have hP : (∫ t in (0:ℝ)..s, F t) = 2*(c1*neutralIV106E9Lag v (s)+c2*neutralIV106E9Lag v (2*s)) := by
    dsimp [F]
    rw [intervalIntegral.integral_const_mul]
    have hC1 : Continuous (fun t => c1*f1 t) := continuous_const.mul hf1
    have hC2 : Continuous (fun t => c2*f2 t) := continuous_const.mul hf2
    rw [intervalIntegral.integral_add (hC1.intervalIntegrable (μ := volume) 0 s)
      (hC2.intervalIntegrable (μ := volume) 0 s)]
    simp only [intervalIntegral.integral_const_mul, hI1, hI2]
  apply neutralIV106E6Integral_receiver F M s L _ _ hs.le hF hM _ hP hm
  intro t ht
  have h := hmat (z t)
  rw [neutralIV106E6Lag3] at h
  exact h

/-- Padded physical chain bound, with an explicit pointwise matrix premise. -/
theorem neutralIV106E9Physical4 (v : ℝ → ℂ) (hv : Continuous v)
    (l b s L c1 c2 c3 : ℝ) (hs : 0 < s) (hlb : l ≤ b)
    (hb : b ≤ l+4*s) (hout : ∀ x ∉ Set.Icc l b, v x = 0)
    (hmat : ∀ z : Fin 4 → ℂ,
      (∑ i, ∑ j, neutralIV106E6LagMatrix4 c1 c2 c3 i j*(star (z i)*z j).re) ≤
        L*∑ i, ‖z i‖^2) :
    2*(c1*neutralIV106E9Lag v (s)+c2*neutralIV106E9Lag v (2*s)+c3*neutralIV106E9Lag v (3*s)) ≤ L*neutralIV106E9Mass v := by
  let z (t : ℝ) (i : Fin 4) : ℂ := v (t+(l+(i.val:ℝ)*s))
  let f1 (t : ℝ) : ℝ := (star (z t 0)*z t 1).re+(star (z t 1)*z t 2).re+(star (z t 2)*z t 3).re
  let f2 (t : ℝ) : ℝ := (star (z t 0)*z t 2).re+(star (z t 1)*z t 3).re
  let f3 (t : ℝ) : ℝ := (star (z t 0)*z t 3).re
  have hf1 : Continuous f1 := by dsimp [f1,z]; fun_prop
  have hI1 : (∫ t in (0:ℝ)..s, f1 t) =
      neutralIV106E9Lag v (s) := by
    have h1 := neutralIV106E5Shift v hv l b s 4 1 hlb (by simpa using hb) hout
    have h2 := neutralIV106E5Truncate v l b s 4 1 hs (by simpa using hb) hout
    have he := h2.symm.trans h1
    norm_num [Finset.sum_range_succ, f1, z, neutralIV106E9Lag] at he ⊢
    exact he
  have hf2 : Continuous f2 := by dsimp [f2,z]; fun_prop
  have hI2 : (∫ t in (0:ℝ)..s, f2 t) =
      neutralIV106E9Lag v (2*s) := by
    have h1 := neutralIV106E5Shift v hv l b s 4 2 hlb (by simpa using hb) hout
    have h2 := neutralIV106E5Truncate v l b s 4 2 hs (by simpa using hb) hout
    have he := h2.symm.trans h1
    norm_num [Finset.sum_range_succ, f2, z, neutralIV106E9Lag] at he ⊢
    exact he
  have hf3 : Continuous f3 := by dsimp [f3,z]; fun_prop
  have hI3 : (∫ t in (0:ℝ)..s, f3 t) =
      neutralIV106E9Lag v (3*s) := by
    have h1 := neutralIV106E5Shift v hv l b s 4 3 hlb (by simpa using hb) hout
    have h2 := neutralIV106E5Truncate v l b s 4 3 hs (by simpa using hb) hout
    have he := h2.symm.trans h1
    norm_num [Finset.sum_range_succ, f3, z, neutralIV106E9Lag] at he ⊢
    exact he
  let M (t : ℝ) : ℝ := ∑ i : Fin 4, ‖z t i‖^2
  let F (t : ℝ) : ℝ := 2*(c1*f1 t+c2*f2 t+c3*f3 t)
  have hM : Continuous M := by
    simp only [M,Fin.sum_univ_succ,Fin.sum_univ_zero,z]
    fun_prop
  have hF : Continuous F := by
    dsimp [F]
    fun_prop
  have hm : (∫ t in (0:ℝ)..s, M t) = neutralIV106E9Mass v := by
    have h := neutralIV106E5Mass v hv l b s 4 hlb (by simpa using hb) hout
    norm_num [M,z,Fin.sum_univ_succ,Finset.sum_range_succ,neutralIV106E9Mass] at h ⊢
    exact h
  have hP : (∫ t in (0:ℝ)..s, F t) = 2*(c1*neutralIV106E9Lag v (s)+c2*neutralIV106E9Lag v (2*s)+c3*neutralIV106E9Lag v (3*s)) := by
    dsimp [F]
    rw [intervalIntegral.integral_const_mul]
    have hC1 : Continuous (fun t => c1*f1 t) := continuous_const.mul hf1
    have hC2 : Continuous (fun t => c2*f2 t) := continuous_const.mul hf2
    have hC3 : Continuous (fun t => c3*f3 t) := continuous_const.mul hf3
    rw [intervalIntegral.integral_add ((hC1.add hC2).intervalIntegrable (μ := volume) 0 s)
      (hC3.intervalIntegrable (μ := volume) 0 s)]
    rw [intervalIntegral.integral_add (hC1.intervalIntegrable (μ := volume) 0 s)
      (hC2.intervalIntegrable (μ := volume) 0 s)]
    simp only [intervalIntegral.integral_const_mul, hI1, hI2, hI3]
  apply neutralIV106E6Integral_receiver F M s L _ _ hs.le hF hM _ hP hm
  intro t ht
  have h := hmat (z t)
  rw [neutralIV106E6Lag4] at h
  exact h

theorem neutralIV106E9Group2 (v : ℝ → ℂ) (hv : Continuous v)
    (hout : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), v x = 0) :
    2*((Real.log 2/Real.sqrt 2)*neutralIV106E9Lag v (Real.log 2)+(Real.log 2/Real.sqrt 4)*neutralIV106E9Lag v (2*Real.log 2)+(Real.log 2/Real.sqrt 8)*neutralIV106E9Lag v (3*Real.log 2)) ≤
      (1214/1000:ℝ)*neutralIV106E9Mass v := by
  obtain ⟨h2,h4,h8,h3,h9,h5,h7⟩ := neutralIV106E4Coefficients
  obtain ⟨hc2,hc3,hc5,hc7⟩ := neutralIV106E7Cover
  have hs : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hb : (11/10:ℝ) ≤ -(11/10:ℝ)+4*Real.log 2 := by linarith only [hc2]
  apply neutralIV106E9Physical4 v hv (-(11/10)) (11/10) (Real.log 2)
    (1214/1000) (Real.log 2/Real.sqrt 2) (Real.log 2/Real.sqrt 4) (Real.log 2/Real.sqrt 8) hs (by norm_num) hb hout
  intro z
  obtain ⟨_,_,hw,hr⟩ := neutralIV106E4Rows2
  apply neutralIV106E4Dominated_chain (neutralIV106E6LagMatrix4 (Real.log 2/Real.sqrt 2) (Real.log 2/Real.sqrt 4) (Real.log 2/Real.sqrt 8))
    neutralIV106E4Matrix2 neutralIV106E4Weight2 z (1214/1000)
  · intro i j
    fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E6LagMatrix4] <;> positivity
  · intro i j
    fin_cases i <;> fin_cases j <;> rfl
  · intro i j
    fin_cases i <;> fin_cases j <;>
      norm_num [neutralIV106E6LagMatrix4,neutralIV106E4Matrix2] <;>
      first | assumption | linarith only [h2,h4,h8]
  · exact hw
  · convert hr using 1 <;> norm_num

theorem neutralIV106E9Group3 (v : ℝ → ℂ) (hv : Continuous v)
    (hout : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), v x = 0) :
    2*((Real.log 3/Real.sqrt 3)*neutralIV106E9Lag v (Real.log 3)+(Real.log 3/Real.sqrt 9)*neutralIV106E9Lag v (2*Real.log 3)) ≤
      (1099/1000:ℝ)*neutralIV106E9Mass v := by
  obtain ⟨h2,h4,h8,h3,h9,h5,h7⟩ := neutralIV106E4Coefficients
  obtain ⟨hc2,hc3,hc5,hc7⟩ := neutralIV106E7Cover
  have hs : 0 < Real.log 3 := Real.log_pos (by norm_num)
  have hb : (11/10:ℝ) ≤ -(11/10:ℝ)+3*Real.log 3 := by linarith only [hc3]
  apply neutralIV106E9Physical3 v hv (-(11/10)) (11/10) (Real.log 3)
    (1099/1000) (Real.log 3/Real.sqrt 3) (Real.log 3/Real.sqrt 9) hs (by norm_num) hb hout
  intro z
  obtain ⟨_,_,hw,hr⟩ := neutralIV106E4Rows3
  apply neutralIV106E4Dominated_chain (neutralIV106E6LagMatrix3 (Real.log 3/Real.sqrt 3) (Real.log 3/Real.sqrt 9))
    neutralIV106E4Matrix3 neutralIV106E4Weight3 z (1099/1000)
  · intro i j
    fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E6LagMatrix3] <;> positivity
  · intro i j
    fin_cases i <;> fin_cases j <;> rfl
  · intro i j
    fin_cases i <;> fin_cases j <;>
      norm_num [neutralIV106E6LagMatrix3,neutralIV106E4Matrix3] <;>
      first | assumption | linarith only [h3,h9]
  · exact hw
  · convert hr using 1 <;> norm_num

theorem neutralIV106E9Group5 (v : ℝ → ℂ) (hv : Continuous v)
    (hout : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), v x = 0) :
    2*((Real.log 5/Real.sqrt 5)*neutralIV106E9Lag v (Real.log 5)) ≤
      (719763/1000000:ℝ)*neutralIV106E9Mass v := by
  obtain ⟨h2,h4,h8,h3,h9,h5,h7⟩ := neutralIV106E4Coefficients
  obtain ⟨hc2,hc3,hc5,hc7⟩ := neutralIV106E7Cover
  have hs : 0 < Real.log 5 := Real.log_pos (by norm_num)
  have hb : (11/10:ℝ) ≤ -(11/10:ℝ)+2*Real.log 5 := by linarith only [hc5]
  apply neutralIV106E9Physical2 v hv (-(11/10)) (11/10) (Real.log 5)
    (719763/1000000) (Real.log 5/Real.sqrt 5) hs (by norm_num) hb hout
  intro z
  obtain ⟨_,_,hw,hr⟩ := neutralIV106E4Rows5
  apply neutralIV106E4Dominated_chain (neutralIV106E6LagMatrix2 (Real.log 5/Real.sqrt 5))
    neutralIV106E4Matrix5 neutralIV106E4Weight5 z (719763/1000000)
  · intro i j
    fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E6LagMatrix2] <;> positivity
  · intro i j
    fin_cases i <;> fin_cases j <;> rfl
  · intro i j
    fin_cases i <;> fin_cases j <;>
      norm_num [neutralIV106E6LagMatrix2,neutralIV106E4Matrix5] <;>
      first | assumption | linarith only [h5]
  · exact hw
  · convert hr using 1 <;> norm_num

theorem neutralIV106E9Group7 (v : ℝ → ℂ) (hv : Continuous v)
    (hout : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), v x = 0) :
    2*((Real.log 7/Real.sqrt 7)*neutralIV106E9Lag v (Real.log 7)) ≤
      (735485/1000000:ℝ)*neutralIV106E9Mass v := by
  obtain ⟨h2,h4,h8,h3,h9,h5,h7⟩ := neutralIV106E4Coefficients
  obtain ⟨hc2,hc3,hc5,hc7⟩ := neutralIV106E7Cover
  have hs : 0 < Real.log 7 := Real.log_pos (by norm_num)
  have hb : (11/10:ℝ) ≤ -(11/10:ℝ)+2*Real.log 7 := by linarith only [hc7]
  apply neutralIV106E9Physical2 v hv (-(11/10)) (11/10) (Real.log 7)
    (735485/1000000) (Real.log 7/Real.sqrt 7) hs (by norm_num) hb hout
  intro z
  obtain ⟨_,_,hw,hr⟩ := neutralIV106E4Rows7
  apply neutralIV106E4Dominated_chain (neutralIV106E6LagMatrix2 (Real.log 7/Real.sqrt 7))
    neutralIV106E4Matrix7 neutralIV106E4Weight7 z (735485/1000000)
  · intro i j
    fin_cases i <;> fin_cases j <;> norm_num [neutralIV106E6LagMatrix2] <;> positivity
  · intro i j
    fin_cases i <;> fin_cases j <;> rfl
  · intro i j
    fin_cases i <;> fin_cases j <;>
      norm_num [neutralIV106E6LagMatrix2,neutralIV106E4Matrix7] <;>
      first | assumption | linarith only [h7]
  · exact hw
  · convert hr using 1 <;> norm_num

/-- Actual prime loss on the entire supported Schwartz core. -/
theorem neutralIV106E9Original_prime (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), v x = 0) :
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation (11/10) v v) n).re ≤
      (471031/125000:ℝ)*neutralIV106E9Mass v := by
  have h2 := neutralIV106E9Group2 v v.continuous hv
  have h3 := neutralIV106E9Group3 v v.continuous hv
  have h5 := neutralIV106E9Group5 v v.continuous hv
  have h7 := neutralIV106E9Group7 v v.continuous hv
  obtain ⟨hm2,hm3,hm4,hm5,hm7,hm8,hm9⟩ := neutralIV106E7Mangoldt
  obtain ⟨hl4,hl8,hl9⟩ := neutralIV106E7Lags
  rw [neutralIV106E7Original_sum]
  simp only [Complex.add_re]
  simp_rw [neutralIV106E8Summand (11/10) v hv]
  change _ ≤ _
  simp only [hm2,hm3,hm4,hm5,hm7,hm8,hm9,hl4,hl8,hl9]
  simp only [neutralIV106E9Lag] at h2 h3 h5 h7
  linarith only [h2,h3,h5,h7]

#print axioms neutralIV106E9Physical2
#print axioms neutralIV106E9Physical3
#print axioms neutralIV106E9Physical4
#print axioms neutralIV106E9Group2
#print axioms neutralIV106E9Group3
#print axioms neutralIV106E9Group5
#print axioms neutralIV106E9Group7
#print axioms neutralIV106E9Original_prime
end
end WeilDefect
