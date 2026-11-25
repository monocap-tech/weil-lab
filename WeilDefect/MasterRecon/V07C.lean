import WeilDefect.MasterRecon.V07B
import Mathlib.Analysis.InnerProductSpace.ProdL2
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-! V07C: the actual two-channel displacement and ordinate phase blocks,
and their uniform infinite direct sums. Critical-line coordinates can be
padded by a zero second coordinate and displacement zero; the actual zeta
index identification and exponential covariance of the sum are separate. -/
namespace WeilDefect.MasterRecon.V07C

open scoped ENNReal InnerProduct ComplexConjugate

abbrev Pair := WithLp 2 (ℂ × ℂ)

noncomputable def swapBlock : Pair →L[ℂ] Pair :=
  ({ toFun := fun x => WithLp.toLp 2 ((WithLp.ofLp x).2, (WithLp.ofLp x).1)
     map_add' := fun x y => by rfl
     map_smul' := fun a x => by rfl } : Pair →ₗ[ℂ] Pair).mkContinuous 1 (by
       intro x
       change ‖WithLp.toLp 2 ((WithLp.ofLp x).2, (WithLp.ofLp x).1)‖ ≤ 1 * ‖x‖
       rw [one_mul, WithLp.prod_norm_eq_of_L2, WithLp.prod_norm_eq_of_L2]
       change Real.sqrt (‖(WithLp.ofLp x).2‖ ^ 2 + ‖(WithLp.ofLp x).1‖ ^ 2) ≤
         Real.sqrt (‖(WithLp.ofLp x).1‖ ^ 2 + ‖(WithLp.ofLp x).2‖ ^ 2)
       rw [add_comm])

theorem swapBlock_apply (x : Pair) :
    swapBlock x = WithLp.toLp 2 ((WithLp.ofLp x).2, (WithLp.ofLp x).1) := rfl

theorem swapBlock_norm (x : Pair) : ‖swapBlock x‖ = ‖x‖ := by
  rw [swapBlock_apply, WithLp.prod_norm_eq_of_L2, WithLp.prod_norm_eq_of_L2]
  change Real.sqrt (‖(WithLp.ofLp x).2‖ ^ 2 + ‖(WithLp.ofLp x).1‖ ^ 2) =
    Real.sqrt (‖(WithLp.ofLp x).1‖ ^ 2 + ‖(WithLp.ofLp x).2‖ ^ 2)
  rw [add_comm]

theorem swapBlock_symmetric (x y : Pair) :
    inner ℂ (swapBlock x) y = inner ℂ x (swapBlock y) := by
  simp only [swapBlock_apply, WithLp.prod_inner_apply, WithLp.ofLp_toLp]
  rw [add_comm]

noncomputable def displacementBlock (d : ℝ) : Pair →L[ℂ] Pair :=
  (d : ℂ) • swapBlock

theorem displacementBlock_norm_le (d : ℝ) :
    ‖displacementBlock d‖ ≤ |d| := by
  apply ContinuousLinearMap.opNorm_le_bound _ (abs_nonneg d)
  intro x
  change ‖(d : ℂ) • swapBlock x‖ ≤ |d| * ‖x‖
  rw [norm_smul, Complex.norm_real, Real.norm_eq_abs, swapBlock_norm]

theorem displacementBlock_symmetric (d : ℝ) (x y : Pair) :
    inner ℂ (displacementBlock d x) y = inner ℂ x (displacementBlock d y) := by
  change inner ℂ ((d : ℂ) • swapBlock x) y =
    inner ℂ x ((d : ℂ) • swapBlock y)
  rw [inner_smul_left, inner_smul_right, swapBlock_symmetric]
  simp

variable {ι : Type*}
abbrev Coeff (ι : Type*) := lp (fun _ : ι => Pair) 2

noncomputable def displacement (d : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2) :
    Coeff ι →L[ℂ] Coeff ι :=
  V07B.blockLift (fun i => displacementBlock (d i)) (1 / 2) (by norm_num)
    (fun i => (displacementBlock_norm_le (d i)).trans (hd i))

theorem displacement_apply (d : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2)
    (x : Coeff ι) (i : ι) :
    displacement d hd x i = displacementBlock (d i) (x i) := rfl

theorem displacement_norm_le (d : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2) :
    ‖displacement d hd‖ ≤ 1 / 2 :=
  V07B.blockLift_norm_le _ _ _ _

theorem displacement_selfAdjoint (d : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2) :
    (displacement d hd).adjoint = displacement d hd := by
  symm
  apply (ContinuousLinearMap.eq_adjoint_iff _ _).2
  exact V07B.blockLift_symmetric _ _ _ _ (fun i => displacementBlock_symmetric (d i))

noncomputable def ordinatePhase (g a : ℝ) : ℂ :=
  Complex.exp ((g : ℂ) * Complex.I * (a : ℂ))

theorem ordinatePhase_norm (g a : ℝ) : ‖ordinatePhase g a‖ = 1 := by
  unfold ordinatePhase
  rw [Complex.norm_exp]
  simp [Complex.mul_re, Complex.mul_im]

noncomputable def phaseBlock (q : ℂ) : Pair →L[ℂ] Pair :=
  q • (1 : Pair →L[ℂ] Pair)

theorem phaseBlock_apply (q : ℂ) (x : Pair) : phaseBlock q x = q • x := by
  rfl

theorem phaseBlock_norm_le (q : ℂ) (hq : ‖q‖ = 1) : ‖phaseBlock q‖ ≤ 1 := by
  apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
  intro x
  rw [phaseBlock_apply, norm_smul, hq]

theorem phaseBlock_cancel (q : ℂ) (hq : ‖q‖ = 1)
    (E : Pair →L[ℂ] Pair) (x y : Pair) :
    inner ℂ (E (phaseBlock q x)) (phaseBlock q y) = inner ℂ (E x) y := by
  rw [phaseBlock_apply, phaseBlock_apply, E.map_smul, inner_smul_left, inner_smul_right]
  have h : star q * q = 1 := by
    change (starRingEnd ℂ) q * q = 1
    rw [Complex.conj_mul', hq]
    norm_num
  rw [← mul_assoc, h, one_mul]

noncomputable def phase (g : ι → ℝ) (a : ℝ) : Coeff ι →L[ℂ] Coeff ι :=
  V07B.blockLift (fun i => phaseBlock (ordinatePhase (g i) a)) 1 zero_le_one
    (fun i => phaseBlock_norm_le _ (ordinatePhase_norm _ _))

theorem phase_cancel (g : ι → ℝ) (a : ℝ)
    (E : ι → Pair →L[ℂ] Pair) (c : ℝ) (hc : 0 ≤ c)
    (hE : ∀ i, ‖E i‖ ≤ c) (x y : Coeff ι) :
    inner ℂ (V07B.blockLift E c hc hE (phase g a x)) (phase g a y) =
      inner ℂ (V07B.blockLift E c hc hE x) y := by
  exact V07B.block_pairing_transfer _ _ _ _ _ _ _ _ _ _ _ _
    (fun i => phaseBlock_cancel _ (ordinatePhase_norm _ _) (E i)) x y

end WeilDefect.MasterRecon.V07C

#print axioms WeilDefect.MasterRecon.V07C.swapBlock_apply
#print axioms WeilDefect.MasterRecon.V07C.swapBlock_norm
#print axioms WeilDefect.MasterRecon.V07C.swapBlock_symmetric
#print axioms WeilDefect.MasterRecon.V07C.displacementBlock_norm_le
#print axioms WeilDefect.MasterRecon.V07C.displacementBlock_symmetric
#print axioms WeilDefect.MasterRecon.V07C.displacement_apply
#print axioms WeilDefect.MasterRecon.V07C.displacement_norm_le
#print axioms WeilDefect.MasterRecon.V07C.displacement_selfAdjoint
#print axioms WeilDefect.MasterRecon.V07C.ordinatePhase_norm
#print axioms WeilDefect.MasterRecon.V07C.phaseBlock_apply
#print axioms WeilDefect.MasterRecon.V07C.phaseBlock_norm_le
#print axioms WeilDefect.MasterRecon.V07C.phaseBlock_cancel
#print axioms WeilDefect.MasterRecon.V07C.phase_cancel
