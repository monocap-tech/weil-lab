import WeilDefect.Arithmetic.ActualZetaIV106E2GammaEnvelope
import WeilDefect.Arithmetic.ActualZetaIV106E7PrimeCutoff

namespace WeilDefect
noncomputable section
open scoped BigOperators

/-- A global explicit lower envelope, not a bound on a chosen existential witness. -/
theorem neutralIV106E17AGamma_shift (ξ : ℝ) :
    logarithmicFourierWeight ξ ≤ compactWindowArchimedeanSymbol (2*Real.pi*ξ)+12 := by
  have he : 1 ≤ Real.exp 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by norm_num)
  have h2 := Real.log_le_sub_one_of_pos (by norm_num : (0:ℝ)<2)
  have hp := Real.log_le_sub_one_of_pos Real.pi_pos
  have hp4 := Real.pi_lt_four
  have hanchor := neutralIV106E2Quarter (Real.pi*ξ)
  rw [neutralActualZetaDigamma_quarter_re] at hanchor
  have hsym : ((1:ℂ)/4)+Complex.I*(((2*Real.pi*ξ:ℝ):ℂ)/2) =
      1/4+Complex.I*((Real.pi*ξ:ℝ):ℂ) := by push_cast; ring
  have hg := Real.eulerMascheroniConstant_lt_two_thirds
  by_cases hξ : |ξ| ≤ 1
  · have hl := Real.log_le_log (show 0 < Real.exp 1 + |ξ| by positivity)
      (show Real.exp 1 + |ξ| ≤ 2*Real.exp 1 by linarith)
    rw [Real.log_mul (by norm_num : (2:ℝ) ≠ 0) (Real.exp_pos _).ne', Real.log_exp] at hl
    unfold logarithmicFourierWeight compactWindowArchimedeanSymbol
    rw [hsym]
    linarith only [hl,h2,hp,hp4,hanchor,hg]
  · have hξ1 : 1 ≤ |ξ| := (lt_of_not_ge hξ).le
    have hn : ξ ≠ 0 := by intro h; simp [h] at hξ1
    have hl := Real.log_le_log (show 0 < Real.exp 1 + |ξ| by positivity)
      (show Real.exp 1 + |ξ| ≤ (2*Real.exp 1)*|ξ| by
        nlinarith [mul_nonneg (sub_nonneg.mpr he) (sub_nonneg.mpr hξ1)])
    rw [Real.log_mul (by positivity : 2*Real.exp 1 ≠ 0) (abs_ne_zero.mpr hn),
      Real.log_mul (by norm_num : (2:ℝ) ≠ 0) (Real.exp_pos _).ne', Real.log_exp] at hl
    have hpi : 3 < Real.pi := Real.pi_gt_three
    have hsq : 1 ≤ ξ^2 := by nlinarith [sq_abs ξ,abs_nonneg ξ]
    have hp2 : 9 ≤ Real.pi^2 := by nlinarith
    have hd : 9 ≤ Real.pi^2*ξ^2 := by
      nlinarith [mul_le_mul_of_nonneg_left hsq (sq_nonneg Real.pi)]
    have hr : 25/(8*Real.pi^2*ξ^2) ≤ (1:ℝ) := by
      apply (div_le_iff₀ (by positivity)).mpr
      nlinarith only [hd]
    have hh := neutralIV106E2Global ξ hn
    unfold logarithmicFourierWeight
    linarith only [hl,h2,hr,hh]

/-- Uniform prime loss using the seven literal coefficient bounds. -/
theorem neutralIV106E17APrime_bound :
    neutralActualZetaPrimeSymbolBound (11/10:ℝ) ≤ 8 := by
  obtain ⟨h2,h4,h8,h3,h9,h5,h7⟩ := neutralIV106E4Coefficients
  obtain ⟨hm2,hm3,hm4,hm5,hm7,hm8,hm9⟩ := neutralIV106E7Mangoldt
  unfold neutralActualZetaPrimeSymbolBound
  rw [neutralIV106E7Inventory]
  simp [Finset.sum_insert, compactWindowPrimeCoefficient,
    hm2,hm3,hm4,hm5,hm7,hm8,hm9] 
  <;> try (simp only [abs_of_nonneg (show 0 ≤ Real.log (2:ℝ) by positivity),
    abs_of_nonneg (show 0 ≤ Real.log (3:ℝ) by positivity),
    abs_of_nonneg (show 0 ≤ Real.log (5:ℝ) by positivity),
    abs_of_nonneg (show 0 ≤ Real.log (7:ℝ) by positivity)])
  <;> try (rw [abs_of_nonneg (by positivity), abs_of_nonneg (by positivity),
      abs_of_nonneg (by positivity), abs_of_nonneg (by positivity),
      abs_of_nonneg (by positivity), abs_of_nonneg (by positivity),
      abs_of_nonneg (by positivity)])
  <;> linarith only [h2,h4,h8,h3,h9,h5,h7]

theorem neutralIV106E17ASymbol_shift (ξ : ℝ) :
    logarithmicFourierWeight ξ ≤ rightLimitCompactWeilSymbolMathlib (11/10) ξ + 20 := by
  have hg := neutralIV106E17AGamma_shift ξ
  have hp := (abs_le.mp ((neutralActualZetaPrimeSymbol_abs_le (11/10) (2*Real.pi*ξ)).trans
    neutralIV106E17APrime_bound)).2
  unfold rightLimitCompactWeilSymbolMathlib rightLimitCompactWeilSymbol
  linarith only [hg,hp]

#print axioms neutralIV106E17AGamma_shift
#print axioms neutralIV106E17APrime_bound
#print axioms neutralIV106E17ASymbol_shift
end
end WeilDefect
