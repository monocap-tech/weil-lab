import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Arctan

/-! V10B32a: literal scalar constant enclosures using native log remainder
and harmonic Euler--Mascheroni brackets. Machin identity is native;
the finite arctangent remainder and exact endpoint computations are
explicit inputs to the final enclosure receiver. -/
namespace WeilDefect.MasterRecon.V10B32a

open scoped BigOperators

noncomputable def logArg (x : ℝ) := (x-1)/(x+1)
noncomputable def logSum (n : ℕ) (x : ℝ) : ℝ :=
  2*∑ j ∈ Finset.range n, (logArg x)^(2*j+1)/(2*j+1:ℝ)
noncomputable def logErr (n : ℕ) (x : ℝ) : ℝ :=
  2*(logArg x)^(2*n+1)/(1-(logArg x)^2)

theorem log_arg_range (x : ℝ) (hx : 1 ≤ x) :
    0 ≤ logArg x ∧ logArg x < 1 := by
  have hp : 0 < x+1 := by linarith
  unfold logArg
  exact ⟨div_nonneg (by linarith) hp.le,(div_lt_iff₀ hp).mpr (by linarith)⟩

theorem log_bracket (n : ℕ) (x : ℝ) (hx : 1 ≤ x) :
    logSum n x ≤ Real.log x ∧ Real.log x ≤ logSum n x+logErr n x := by
  obtain ⟨ha,hb⟩ := log_arg_range x hx
  have hc : (1+logArg x)/(1-logArg x)=x := by
    unfold logArg
    have hp : x+1 ≠ 0 := by linarith
    field_simp [hp] <;> ring
  have hlo := Real.sum_range_le_log_div ha hb n
  have hhi := Real.log_div_le_sum_range_add ha hb n
  rw [hc] at hlo hhi
  unfold logSum logErr
  linarith

theorem gamma_bracket (n : ℕ) (hn : 0<n) :
    (harmonic n:ℝ)-Real.log ((n:ℝ)+1) ≤ Real.eulerMascheroniConstant ∧
      Real.eulerMascheroniConstant ≤ (harmonic n:ℝ)-Real.log (n:ℝ) := by
  constructor
  · exact (Real.eulerMascheroniSeq_lt_eulerMascheroniConstant n).le
  · simpa only [Real.eulerMascheroniSeq',if_neg hn.ne'] using
      (Real.eulerMascheroniConstant_lt_eulerMascheroniSeq' n).le

theorem machin : Real.pi = 16*Real.arctan (1/5)-4*Real.arctan (1/239) := by
  have h := Real.four_mul_arctan_inv_5_sub_arctan_inv_239
  simp only [one_div] 
  linarith

theorem machin_bracket (a b c d : ℝ)
    (ha : a ≤ Real.arctan (1/5)) (hb : Real.arctan (1/5) ≤ b)
    (hc : c ≤ Real.arctan (1/239)) (hd : Real.arctan (1/239) ≤ d) :
    16*a-4*d ≤ Real.pi ∧ Real.pi ≤ 16*b-4*c := by
  rw [machin]
  constructor <;> linarith

theorem combined_bracket (gl gu pl pu : ℝ)
    (hg₁ : gl ≤ Real.eulerMascheroniConstant)
    (hg₂ : Real.eulerMascheroniConstant ≤ gu)
    (hp₁ : pl ≤ Real.log Real.pi) (hp₂ : Real.log Real.pi ≤ pu) :
    -gu-pu ≤ -Real.eulerMascheroniConstant-Real.log Real.pi ∧
      -Real.eulerMascheroniConstant-Real.log Real.pi ≤ -gl-pl := by
  constructor <;> linarith

theorem midpoint_bound (a b c : ℝ) (ha : a≤c) (hb : c≤b) :
    |c-(a+b)/2| ≤ (b-a)/2 := abs_le.mpr ⟨by linarith,by linarith⟩

end WeilDefect.MasterRecon.V10B32a

#print axioms WeilDefect.MasterRecon.V10B32a.log_arg_range
#print axioms WeilDefect.MasterRecon.V10B32a.log_bracket
#print axioms WeilDefect.MasterRecon.V10B32a.gamma_bracket
#print axioms WeilDefect.MasterRecon.V10B32a.machin
#print axioms WeilDefect.MasterRecon.V10B32a.machin_bracket
#print axioms WeilDefect.MasterRecon.V10B32a.combined_bracket
#print axioms WeilDefect.MasterRecon.V10B32a.midpoint_bound
