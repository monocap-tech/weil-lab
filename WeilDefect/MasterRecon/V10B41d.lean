import WeilDefect.MasterRecon.V10B41b

/-! V10B41d: exact rational budget for the finite low-deflation route.
This certifies numeric inequalities only; analytic attachment and
identification with the original frozen archive are separate. -/
namespace WeilDefect.MasterRecon.V10B41d
open scoped BigOperators
open WeilDefect.MasterRecon.V10B41a
open WeilDefect.MasterRecon.V10B41b

def eps : ℚ := 65/((8:ℚ)^64*((64:ℕ).factorial:ℚ)*64)
def D : ℚ := (a 15:ℚ)/(scale:ℚ)
def dLower : ℚ := (7/8)*aTerm 15 0
def dError : ℚ := 31*(4:ℚ)^15*eps
def lowNorm : ℚ := ∑ j ∈ Finset.range 14, (2*(j:ℚ)+1)*(16:ℚ)^j
def c (k : ℕ) : ℚ := (a (15+2*k):ℚ)/(a 15:ℚ)
def frozen (n k : ℕ) : ℚ :=
  if k<10 then aFormula (15+2*k) n/aFormula 15 n else 0
def loadNorm : ℚ := ∑ k ∈ Finset.range 25, (4:ℚ)^(15+2*k)*|c k|
def comparison (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range 25, (4:ℚ)^(15+2*k)*|c k-frozen n k|
def projectionReserve : ℚ := eps*(1+lowNorm)/dLower
def denominatorReserve : ℚ := dError/dLower*loadNorm

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem positive_denominator : 0<dLower ∧ dLower≤D-dError := by
  norm_num [projectionReserve, denominatorReserve, comparison, loadNorm, frozen, c, dLower, D,
    dError, lowNorm, eps, aFormula, aTerm, a, aBank, scale, Finset.sum_range_succ, Nat.factorial]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem projection_reserve : projectionReserve < 1/(10:ℚ)^100 := by
  norm_num [projectionReserve, denominatorReserve, comparison, loadNorm, frozen, c, dLower, D,
    dError, lowNorm, eps, aFormula, aTerm, a, aBank, scale, Finset.sum_range_succ, Nat.factorial]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem denominator_reserve : denominatorReserve < 1/(10:ℚ)^97 := by
  norm_num [projectionReserve, denominatorReserve, comparison, loadNorm, frozen, c, dLower, D,
    dError, lowNorm, eps, aFormula, aTerm, a, aBank, scale, Finset.sum_range_succ, Nat.factorial]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem budget16 : projectionReserve+denominatorReserve+comparison 16 < 1/(10:ℚ)^30 := by
  norm_num [projectionReserve, denominatorReserve, comparison, loadNorm, frozen, c, dLower, D,
    dError, lowNorm, eps, aFormula, aTerm, a, aBank, scale, Finset.sum_range_succ, Nat.factorial]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
theorem budget17 : projectionReserve+denominatorReserve+comparison 17 < 1/(10:ℚ)^30 := by
  norm_num [projectionReserve, denominatorReserve, comparison, loadNorm, frozen, c, dLower, D,
    dError, lowNorm, eps, aFormula, aTerm, a, aBank, scale, Finset.sum_range_succ, Nat.factorial]

end WeilDefect.MasterRecon.V10B41d

#print axioms WeilDefect.MasterRecon.V10B41d.positive_denominator
#print axioms WeilDefect.MasterRecon.V10B41d.projection_reserve
#print axioms WeilDefect.MasterRecon.V10B41d.denominator_reserve
#print axioms WeilDefect.MasterRecon.V10B41d.budget16
#print axioms WeilDefect.MasterRecon.V10B41d.budget17
