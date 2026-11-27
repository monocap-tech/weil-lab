import WeilDefect.MasterRecon.V10B25b
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Series
import Mathlib.Analysis.SpecificLimits.Normed

/-! V10B26a: native series and variable-power remainder bounds for
the real quotient residual. No division of a uniform error by r. -/
namespace WeilDefect.MasterRecon.V10B26a

open scoped BigOperators
open V10B25b (D N)

noncomputable def expTerm (r : ℝ) (j : ℕ) : ℝ :=
  (r/2)^j/(j.factorial:ℝ)

noncomputable def sinhTerm (r : ℝ) (j : ℕ) : ℝ :=
  r^(2*j)/((2*j+1).factorial:ℝ)

noncomputable def expPoly (r : ℝ) := ∑ j ∈ Finset.range 30, expTerm r j
noncomputable def denPoly (r : ℝ) := ∑ j ∈ Finset.range 15, sinhTerm r j

theorem exp_series (r : ℝ) : HasSum (expTerm r) (Real.exp (r/2)) := by
  rw [Real.exp_eq_exp_ℝ]
  exact expSeries_div_hasSum_exp (r/2)

theorem den_series (r : ℝ) (hr : 0 < r) : HasSum (sinhTerm r) (D r) := by
  have h := (Real.hasSum_sinh r).div_const r
  unfold D
  convert h using 1
  funext j
  unfold sinhTerm
  rw [pow_succ]
  field_simp [hr.ne']
  <;> ring

theorem geometric_tail (f : ℕ → ℝ) (v C : ℝ) (n : ℕ)
    (hf : HasSum f v) (hC : 0 ≤ C)
    (hbound : ∀ j : ℕ, |f (j+n)| ≤ C*(1/2:ℝ)^j) :
    |v-∑ j ∈ Finset.range n, f j| ≤ 2*C := by
  let g : ℕ → ℝ := fun j => C*(1/2:ℝ)^j
  have hg : HasSum g (2*C) := by
    have h := (hasSum_geometric_of_norm_lt_one (show ‖(1/2:ℝ)‖ < 1 by norm_num)).mul_left C
    convert h using 1 <;> norm_num <;> ring
  have ha : Summable (fun j : ℕ => ‖f (j+n)‖) :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) (fun j => by simpa [Real.norm_eq_abs,g] using hbound j) hg.summable
  have hs := hf.summable.sum_add_tsum_nat_add n
  rw [hf.tsum_eq] at hs
  have he : v-∑ j ∈ Finset.range n, f j = ∑' j : ℕ, f (j+n) := by linarith
  rw [he,← Real.norm_eq_abs]
  exact (norm_tsum_le_tsum_norm ha).trans (by
    rw [← hg.tsum_eq]
    exact ha.tsum_le_tsum (fun j => by simpa [Real.norm_eq_abs,g] using hbound j) hg.summable)

theorem exp_tail (r : ℝ) (hr : 0 ≤ r) (hrh : r ≤ 1/2) :
    |Real.exp (r/2)-expPoly r| ≤ 2*(r/2)^30/(Nat.factorial 30:ℝ) := by
  have h := geometric_tail (expTerm r) (Real.exp (r/2)) ((r/2)^30/(Nat.factorial 30:ℝ)) 30
    (exp_series r) (by positivity) (fun j => by
      unfold expTerm
      rw [abs_of_nonneg (by positivity),pow_add]
      have hp := pow_le_pow_left₀ (show 0 ≤ r/2 by positivity) (show r/2 ≤ (1/2:ℝ) by linarith) j
      have hf : (Nat.factorial 30:ℝ) ≤ ((j+30).factorial:ℝ) := by
        exact_mod_cast Nat.factorial_le (by omega : 30 ≤ j+30)
      calc
        _ ≤ ((1/2:ℝ)^j*(r/2)^30)/((j+30).factorial:ℝ) :=
          div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_right hp (by positivity)) (by positivity)
        _ ≤ ((1/2:ℝ)^j*(r/2)^30)/(Nat.factorial 30:ℝ) :=
          div_le_div_of_nonneg_left (by positivity) (by positivity) hf
        _ = _ := by ring)
  unfold expPoly
  convert h using 1 <;> ring

theorem den_tail (r : ℝ) (hr : 0 < r) (hrh : r ≤ 1/2) :
    |D r-denPoly r| ≤ 2*r^30/(Nat.factorial 31:ℝ) := by
  have h := geometric_tail (sinhTerm r) (D r) (r^30/(Nat.factorial 31:ℝ)) 15
    (den_series r hr) (by positivity) (fun j => by
      unfold sinhTerm
      rw [abs_of_nonneg (by positivity),show 2*(j+15)=2*j+30 by omega,pow_add,pow_mul]
      have hp := pow_le_pow_left₀ (sq_nonneg r) (show r^2 ≤ (1/2:ℝ) by nlinarith [mul_nonneg hr.le (sub_nonneg.mpr hrh)]) j
      have hf : (Nat.factorial 31:ℝ) ≤ ((2*(j+15)+1).factorial:ℝ) := by
        exact_mod_cast Nat.factorial_le (by omega : 31 ≤ 2*(j+15)+1)
      calc
        _ ≤ ((1/2:ℝ)^j*r^30)/((2*(j+15)+1).factorial:ℝ) :=
          div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_right hp (by positivity)) (by positivity)
        _ ≤ ((1/2:ℝ)^j*r^30)/(Nat.factorial 31:ℝ) :=
          div_le_div_of_nonneg_left (by positivity) (by positivity) hf
        _ = _ := by ring)
  unfold denPoly
  convert h using 1 <;> ring

noncomputable def numPoly (r : ℝ) := (expPoly r-denPoly r)/(2*r)

theorem num_tail (r : ℝ) (hr : 0 < r) (hrh : r ≤ 1/2) :
    |N r-numPoly r| ≤ r^29/(Nat.factorial 30:ℝ) := by
  have he := exp_tail r hr.le hrh
  have hd := den_tail r hr hrh
  unfold N numPoly
  rw [← sub_div,show Real.exp (r/2)-D r-(expPoly r-denPoly r)=
    (Real.exp (r/2)-expPoly r)-(D r-denPoly r) by ring,abs_div,abs_of_pos (by positivity : 0 < 2*r)]
  apply (div_le_iff₀ (by positivity : 0 < 2*r)).mpr
  have h := (abs_sub_le (Real.exp (r/2)-expPoly r) (D r-denPoly r)).trans (add_le_add he hd)
  refine h.trans ?_
  have hE : (r/2)^30 = r^30/(2:ℝ)^30 := by rw [div_pow]
  rw [hE,pow_succ r 29]
  norm_num [Nat.factorial]
  nlinarith only [show 0 ≤ r^29*r by positivity]

end WeilDefect.MasterRecon.V10B26a

#print axioms WeilDefect.MasterRecon.V10B26a.exp_series
#print axioms WeilDefect.MasterRecon.V10B26a.den_series
#print axioms WeilDefect.MasterRecon.V10B26a.geometric_tail
#print axioms WeilDefect.MasterRecon.V10B26a.exp_tail
#print axioms WeilDefect.MasterRecon.V10B26a.den_tail
#print axioms WeilDefect.MasterRecon.V10B26a.num_tail
