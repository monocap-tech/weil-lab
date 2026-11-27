import WeilDefect.MasterRecon.V10B41a
import Mathlib.Data.Rat.Cast.Order

/-! V10B41b: independently identify both integer coefficient banks with
explicit finite rational formulas. The Taylor bank uses the binomial
expansion; the Legendre bank uses the factorial form of the finite
centered projection. These are exact rational statements, not an
attachment to the original frozen archive. -/
namespace WeilDefect.MasterRecon.V10B41b
open scoped BigOperators
open WeilDefect.MasterRecon.V10B41a

def tFormula (k : ℕ) : ℚ :=
  ∑ l ∈ Finset.range (64-k),
    (-1:ℚ)^l * ((k+l).choose k:ℚ) * (2:ℚ)^k /
      ((8:ℚ)^(k+l)*((k+l).factorial:ℚ))

def aTerm (j m : ℕ) : ℚ :=
  (2*(j:ℚ)+1)*(2:ℚ)^j*((j+m).factorial:ℚ) /
    ((8:ℚ)^(j+2*m)*(m.factorial:ℚ)*((2*j+2*m+1).factorial:ℚ))

def aFormula (j n : ℕ) : ℚ :=
  ∑ m ∈ Finset.range n, aTerm j m

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem tFormula_check (k : Fin 64) :
    (t k:ℚ) = (scale:ℚ)*tFormula k := by
  fin_cases k <;> decide

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem aFormula_check (j : Fin 64) :
    (a j:ℚ) = (scale:ℚ)*aFormula j ((64-(j:ℕ)+1)/2) := by
  fin_cases j <;> decide

theorem tFormula_real (k : Fin 64) :
    (t k:ℝ)/(scale:ℝ) = (tFormula k:ℝ) := by
  have h : (t k:ℝ)=(scale:ℝ)*(tFormula k:ℝ) := by
    exact_mod_cast tFormula_check k
  have hs : (scale:ℝ)≠0 := by exact_mod_cast scale_pos.ne'
  apply (div_eq_iff hs).mpr
  rw [h,mul_comm]

theorem aFormula_real (j : Fin 64) :
    (a j:ℝ)/(scale:ℝ) = (aFormula j ((64-(j:ℕ)+1)/2):ℝ) := by
  have h : (a j:ℝ)=(scale:ℝ)*(aFormula j ((64-(j:ℕ)+1)/2):ℝ) := by
    exact_mod_cast aFormula_check j
  have hs : (scale:ℝ)≠0 := by exact_mod_cast scale_pos.ne'
  apply (div_eq_iff hs).mpr
  rw [h,mul_comm]

end WeilDefect.MasterRecon.V10B41b

#print axioms WeilDefect.MasterRecon.V10B41b.tFormula_check
#print axioms WeilDefect.MasterRecon.V10B41b.aFormula_check
#print axioms WeilDefect.MasterRecon.V10B41b.tFormula_real
#print axioms WeilDefect.MasterRecon.V10B41b.aFormula_real
