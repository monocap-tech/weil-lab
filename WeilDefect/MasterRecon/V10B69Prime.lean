import WeilDefect.MasterRecon.V10B69a

/-! Suspended prime-zero root, relocated byte-exact from V10B69R2.
Not included in V10B70's independent native audit. -/
namespace WeilDefect.MasterRecon.V10B69a
open MeasureTheory Set
open scoped BigOperators InnerProduct ComplexConjugate
open V08I (logCarrier physicalInclusion)
open V08K (supportMeasure restrictPhysical)
open V10B45a (denom)
open V10B67a (carrierTrial supportedTrial)
open V10B8c (eval vector poleOperator)

theorem prime_free : V10B8d.physicalPrime (1/4) = 0 := by
  have he : Real.exp (2*(1/4:ℝ)) < 2 := by
    calc
      _ < Real.exp (Real.log 2) := Real.exp_lt_exp.mpr (by linarith [Real.log_two_gt_d9])
      _ = 2 := Real.exp_log (by norm_num)
  have hn : ⌊Real.exp (2*(1/4:ℝ))⌋₊ < 2 :=
    (Nat.floor_lt (Real.exp_pos _).le).mpr (by exact_mod_cast he)
  unfold V10B8d.physicalPrime V10B8d.primeBank
  apply Finset.sum_eq_zero
  intro n hn'
  have h := Finset.mem_Ioc.mp hn'
  have hn'' : n = 1 := by
    have hh : n ≤ ⌊Real.exp (2*(1/4:ℝ))⌋₊ := h.2
    omega
  subst n
  have hz : V10B8d.primeWeight 1 = 0 := by simp [V10B8d.primeWeight]
  rw [hz,Complex.ofReal_zero]
  ext f : 1
  change (0:ℂ) • (V10B8d.shiftPair (Real.log (1:ℝ)) f) = 0
  exact zero_smul ℂ _

theorem prime_operator_zero : V10B8d.primeOperator (1/4) = 0 := by
  unfold V10B8d.primeOperator
  rw [prime_free]
  simp

end WeilDefect.MasterRecon.V10B69a

#print axioms WeilDefect.MasterRecon.V10B69a.prime_free
#print axioms WeilDefect.MasterRecon.V10B69a.prime_operator_zero
