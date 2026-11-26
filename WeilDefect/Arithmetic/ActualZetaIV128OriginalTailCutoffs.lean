import WeilDefect.Arithmetic.ActualZetaIV127OriginalLeakageClosure
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap FourierTransform

/-- Rewrite the leakage allowance as a fixed numerator divided by N squared. -/
theorem neutralIV128Leakage_formula (a T : ℝ) (N : ℕ) :
    neutralIV127Leakage a N T =
      (16*Real.pi^2*a*(2*a)^2*T^3/3)/(N:ℝ)^2 := by
  unfold neutralIV127Leakage
  rw [div_pow]
  ring

/-- For every fixed nonnegative radius and band, sufficiently many cells
make the explicit leakage allowance at most one half. -/
theorem neutralIV128HalfLeakage_exists (a T : ℝ) (ha : 0 ≤ a) (hT : 0 ≤ T) :
    ∃ N : ℕ, 0 < N ∧ neutralIV127Leakage a N T ≤ 1/2 := by
  let K : ℝ := 16*Real.pi^2*a*(2*a)^2*T^3/3
  have hK : 0 ≤ K := by dsimp [K]; positivity
  obtain ⟨N, hN⟩ := exists_nat_gt (2*K+1)
  have hn1 : 1 < (N:ℝ) := by linarith
  have hn : 0 < N := by
    have hp : 0 < (N:ℝ) := by linarith
    exact_mod_cast hp
  have hn0 : 0 < (N:ℝ) := by exact_mod_cast hn
  have hsq : 2*K ≤ (N:ℝ)^2 := by
    have hmul := mul_nonneg (sub_nonneg.mpr hn1.le) hn0.le
    nlinarith only [hmul, hN]
  refine ⟨N, hn, ?_⟩
  rw [neutralIV128Leakage_formula]
  change K/(N:ℝ)^2 ≤ 1/2
  apply (div_le_iff₀ (pow_pos hn0 2)).2
  linarith only [hsq]

/-- Explicit exponential frequency selection and Archimedean integer selection.
No sign or size hypothesis on the error budget M is necessary. -/
theorem neutralIV128Margin_exists (a M eta : ℝ) (ha : 0 ≤ a) :
    ∃ T : ℝ, 0 < T ∧ ∃ N : ℕ, 0 < N ∧
      neutralIV127Leakage a N T ≤ 1/2 ∧
      eta < (1-neutralIV127Leakage a N T)*Real.log (Real.exp 1+T)-M := by
  let L : ℝ := 2*(|M|+|eta|+1)
  let T : ℝ := Real.exp L
  have hT : 0 < T := Real.exp_pos _
  obtain ⟨N, hN, hLeak⟩ := neutralIV128HalfLeakage_exists a T ha hT.le
  have hLog : L ≤ Real.log (Real.exp 1+T) := by
    have hle : T ≤ Real.exp 1+T := by
      have hp := Real.exp_pos (1:ℝ)
      linarith
    have h := Real.log_le_log hT hle
    dsimp [T] at h
    rw [Real.log_exp] at h
    exact h
  have hL : 0 ≤ L := by dsimp [L]; positivity
  have hLog0 : 0 ≤ Real.log (Real.exp 1+T) := hL.trans hLog
  have hpay := mul_le_mul_of_nonneg_right
    (show (1/2:ℝ) ≤ 1-neutralIV127Leakage a N T by linarith) hLog0
  have habsM := le_abs_self M
  have habsEta := le_abs_self eta
  refine ⟨T, hT, N, hN, hLeak, ?_⟩
  dsimp [L] at hLog
  linarith only [hpay, hLog, habsM, habsEta]

/-- Remove the scalar-margin premise from the actual packed Schur receiver.
For each prescribed finite coercivity level, one finite cell count works
simultaneously for every supported cell-null Schwartz test. -/
theorem neutralIV128Schur_coercive_tail_exists (k : ℕ) (hk : 0 < k) (eta : ℝ) :
    ∃ N : ℕ, 0 < N ∧ ∀ (v : 𝓢(ℝ,ℂ)),
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      neutralIV127CellNull (11/10:ℝ) N v →
      eta*‖v.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk v := by
  let M : ℝ := neutralActualZetaNativeLogError (11/10:ℝ) +
    neutralPhysicalPoleEnergyConstant (11/10:ℝ) + neutralIV124PhysicalBudget k hk
  obtain ⟨T, hT, N, hN, _, hmargin⟩ :=
    neutralIV128Margin_exists (11/10:ℝ) M eta (by norm_num)
  refine ⟨N, hN, ?_⟩
  intro v hv hm
  exact neutralIV127Schur_cellNull k hk N hN v hv hm T eta hT.le hmargin.le

#print axioms neutralIV128Leakage_formula
#print axioms neutralIV128HalfLeakage_exists
#print axioms neutralIV128Margin_exists
#print axioms neutralIV128Schur_coercive_tail_exists

end
end WeilDefect
