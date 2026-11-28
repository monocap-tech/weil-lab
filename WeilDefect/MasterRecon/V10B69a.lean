import WeilDefect.MasterRecon.V10B68a
import WeilDefect.MasterRecon.V10B8d

/-! Exact normalized trial and physical lower-order A/R attachment.
Neither historical matrix generation nor Archimedean action is assumed. -/
namespace WeilDefect.MasterRecon.V10B69a
open MeasureTheory Set
open scoped BigOperators InnerProduct ComplexConjugate
open V08I (logCarrier physicalInclusion)
open V08K (supportMeasure restrictPhysical)
open V10B45a (denom)
open V10B67a (carrierTrial supportedTrial)
open V10B8c (eval vector poleOperator)

noncomputable def D : ℂ := (denom:ℂ)

theorem D_ne : D ≠ 0 := by
  unfold D
  exact_mod_cast (Nat.ne_of_gt V10B45a.denom_pos)

noncomputable def dividedTrial (j : Fin 16) : logCarrier (1/4) :=
  D⁻¹ • carrierTrial j

theorem divided_physical (j : Fin 16) :
    (physicalInclusion (1/4) (dividedTrial j) : ℝ → ℂ) =ᵐ[volume]
      fun x => D⁻¹ * supportedTrial j x := by
  unfold dividedTrial
  rw [map_smul]
  filter_upwards [Lp.coeFn_smul D⁻¹ (physicalInclusion (1/4) (carrierTrial j)),
    V10B67a.carrierTrial_ae j] with x hx hy
  rw [hx,hy,smul_eq_mul]

theorem divided_section (g : logCarrier (1/4)) :
    ∃ a : Fin 16 → ℂ, g-(∑ j, a j • dividedTrial j) ∈ V10B17b.retainedᗮ := by
  obtain ⟨a,ha⟩ := V10B68a.physical_section g
  refine ⟨fun j => a j*D,?_⟩
  have he : (∑ j, (a j*D) • dividedTrial j) = ∑ j, a j • carrierTrial j := by
    apply Finset.sum_congr rfl
    intro j _
    rw [dividedTrial,smul_smul,mul_assoc,mul_inv_cancel₀ D_ne,mul_one]
  rw [he]
  exact ha

noncomputable def J : logCarrier (1/4) →L[ℂ] V08F.PhysicalL2 (supportMeasure (1/4)) :=
  (restrictPhysical (1/4)).comp (physicalInclusion (1/4))

theorem J_bound (g : logCarrier (1/4)) :
    ‖J g‖ ≤ (Real.sqrt (Real.log 2))⁻¹*‖g‖ := by
  calc
    ‖J g‖ ≤ ‖physicalInclusion (1/4) g‖ :=
      norm_Lp_toLp_restrict_le (Icc (-(1/4):ℝ) (1/4)) _
    _ ≤ _ := by
      change ‖(Lp.fourierTransformₗᵢ ℝ ℂ).symm (V08I.unweight (g:V08I.FullL2))‖ ≤ _
      rw [(Lp.fourierTransformₗᵢ ℝ ℂ).symm.norm_map]
      exact V08I.mulValue_bound _ _ _ _ (g:V08I.FullL2)

theorem prime_free : V10B8d.physicalPrime (1/4) = 0 := by
  have he : Real.exp (2*(1/4:ℝ)) < 2 := by
    rw [← Real.exp_log (by norm_num : (0:ℝ)<2)]
    exact Real.exp_lt_exp.mpr (by linarith [Real.log_two_gt_d9])
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
  simp [V10B8d.primeWeight]

theorem prime_operator_zero : V10B8d.primeOperator (1/4) = 0 := by
  unfold V10B8d.primeOperator
  rw [prime_free]
  simp

noncomputable def poleLoad (v : logCarrier (1/4)) :
    V08F.PhysicalL2 (supportMeasure (1/4)) :=
  (eval (1/4) (-1/2) (by norm_num) v) • vector (1/4) (1/2) (by norm_num) +
  (eval (1/4) (1/2) (by norm_num) v) • vector (1/4) (-1/2) (by norm_num)

theorem pole_physical_pair (v w : logCarrier (1/4)) :
    inner ℂ (poleOperator (1/4) (by norm_num) v) w = inner ℂ (poleLoad v) (J w) := by
  rw [V10B8c.pole_pairing]
  unfold poleLoad
  simp only [inner_add_left,inner_smul_left]
  rfl

theorem row_annihilates_tail (i : Fin 16) (w : logCarrier (1/4))
    (hw : w ∈ V10B17b.retainedᗮ) :
    inner ℂ (V10B68a.rowVector i) (J w) = 0 := by
  have h := (V10B68a.ker_retained w).mpr hw
  change V10B68a.L w = 0 at h
  have hi := congrFun h i
  change V10B68a.rowCLM i w = 0 at hi
  unfold V10B68a.rowCLM at hi
  change ((2*V10B68a.factor i:ℝ):ℂ)*inner ℂ (V10B68a.rowVector i) (J w)=0 at hi
  have hn : ((2*V10B68a.factor i:ℝ):ℂ) ≠ 0 := by
    exact_mod_cast (mul_pos (by norm_num : (0:ℝ)<2) (V10B68a.factor_pos i)).ne'
  exact (mul_eq_zero.mp hi).resolve_left hn

theorem row_subtraction_invariant
    (r : V08F.PhysicalL2 (supportMeasure (1/4))) (a : Fin 16 → ℂ)
    (w : logCarrier (1/4)) (hw : w ∈ V10B17b.retainedᗮ) :
    inner ℂ (r-∑ i, a i • V10B68a.rowVector i) (J w) = inner ℂ r (J w) := by
  rw [inner_sub_left,sum_inner]
  simp only [inner_smul_left,row_annihilates_tail _ w hw,mul_zero,Finset.sum_const_zero,sub_zero]

end WeilDefect.MasterRecon.V10B69a

#print axioms WeilDefect.MasterRecon.V10B69a.D_ne
#print axioms WeilDefect.MasterRecon.V10B69a.divided_physical
#print axioms WeilDefect.MasterRecon.V10B69a.divided_section
#print axioms WeilDefect.MasterRecon.V10B69a.J_bound
#print axioms WeilDefect.MasterRecon.V10B69a.prime_free
#print axioms WeilDefect.MasterRecon.V10B69a.prime_operator_zero
#print axioms WeilDefect.MasterRecon.V10B69a.pole_physical_pair
#print axioms WeilDefect.MasterRecon.V10B69a.row_annihilates_tail
#print axioms WeilDefect.MasterRecon.V10B69a.row_subtraction_invariant
