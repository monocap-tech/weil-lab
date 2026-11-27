import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-! RETURN108-S: exact scalar weight comparison for the two pinned
logarithmic carriers. These are literal copies of the expressions,
not imported IV091 declarations: the old graph modules are absent on
this branch. Same-physical-vector carrier construction is separate. -/
namespace WeilDefect.MasterReturn.LogWeightComparison

noncomputable def ivWeight (x : ℝ) : ℝ := Real.log (Real.exp 1 + |x|)
noncomputable def reconWeight (x : ℝ) : ℝ := Real.log (2 + |2 * Real.pi * x|)

noncomputable def cRI : ℝ := Real.log (2 + 2 * Real.pi)
noncomputable def cIR : ℝ := Real.log (Real.exp 1 + (2 * Real.pi)⁻¹)

theorem ivWeight_lower (x : ℝ) : 1 ≤ ivWeight x := by
  unfold ivWeight
  rw [Real.le_log_iff_exp_le (by positivity)]
  exact le_add_of_nonneg_right (abs_nonneg x)

theorem reconWeight_lower (x : ℝ) : Real.log 2 ≤ reconWeight x := by
  unfold reconWeight
  exact Real.log_le_log (by norm_num) (le_add_of_nonneg_right (abs_nonneg _))

theorem recon_le_iv_add (x : ℝ) : reconWeight x ≤ ivWeight x + cRI := by
  have hp : 0 < 2 * Real.pi := by positivity
  have he : 1 ≤ Real.exp 1 := by
    simpa using Real.exp_le_exp.mpr (by norm_num : (0:ℝ) ≤ 1)
  have h : 2 + (2*Real.pi)*|x| ≤
      (Real.exp 1 + |x|)*(2+2*Real.pi) := by
    nlinarith [mul_nonneg (sub_nonneg.mpr he) hp.le, abs_nonneg x]
  unfold reconWeight ivWeight cRI
  rw [abs_mul, abs_of_pos hp, ← Real.log_mul (by positivity : Real.exp 1 + |x| ≠ 0)
    (by positivity : 2 + 2 * Real.pi ≠ 0)]
  exact Real.log_le_log (by positivity) h

theorem iv_le_recon_add (x : ℝ) : ivWeight x ≤ reconWeight x + cIR := by
  let p : ℝ := 2*Real.pi
  have hp : 0 < p := by dsimp [p]; positivity
  have hpinv : p*p⁻¹ = 1 := mul_inv_cancel₀ hp.ne'
  have he : 0 < Real.exp 1 := Real.exp_pos _
  have h : Real.exp 1 + |x| ≤ (2+p*|x|)*(Real.exp 1+p⁻¹) := by
    calc
      _ ≤ 2*Real.exp 1 + (p*|x|)*Real.exp 1 + 2*p⁻¹ + |x| := by
        linarith [mul_nonneg (mul_nonneg hp.le (abs_nonneg x)) he.le,
          inv_nonneg.mpr hp.le]
      _ = _ := by
        calc
          _ = 2*Real.exp 1 + (p*|x|)*Real.exp 1 + 2*p⁻¹ + (p*p⁻¹)*|x| := by rw [hpinv, one_mul]
          _ = _ := by ring
  unfold ivWeight reconWeight cIR
  rw [abs_mul, abs_of_pos (show 0 < 2*Real.pi from hp),
    ← Real.log_mul (by positivity : 2 + 2 * Real.pi * |x| ≠ 0)
      (by positivity : Real.exp 1 + (2 * Real.pi)⁻¹ ≠ 0)]
  exact Real.log_le_log (by positivity) h

theorem bounded_weight_difference (x : ℝ) :
    |reconWeight x - ivWeight x| ≤ max cRI cIR := by
  apply abs_le.mpr
  constructor
  · linarith [iv_le_recon_add x, le_max_right cRI cIR]
  · linarith [recon_le_iv_add x, le_max_left cRI cIR]

end WeilDefect.MasterReturn.LogWeightComparison

#print axioms WeilDefect.MasterReturn.LogWeightComparison.ivWeight_lower
#print axioms WeilDefect.MasterReturn.LogWeightComparison.reconWeight_lower
#print axioms WeilDefect.MasterReturn.LogWeightComparison.recon_le_iv_add
#print axioms WeilDefect.MasterReturn.LogWeightComparison.iv_le_recon_add
#print axioms WeilDefect.MasterReturn.LogWeightComparison.bounded_weight_difference
