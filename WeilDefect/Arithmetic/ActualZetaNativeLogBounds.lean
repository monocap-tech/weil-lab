import WeilDefect.Arithmetic.ActualZetaArchimedeanTransport
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_StirlingVert_digamma_stirling

namespace WeilDefect
noncomputable section
open scoped BigOperators
set_option maxHeartbeats 800000

/-- Certified vertical Stirling gives a real logarithmic error bound.
This estimate is independent of a Weil-symbol temperate-growth premise. -/
theorem neutralActualZetaDigamma_log_error {z : ℂ}
    (hz : 0 < z.re) (hi : 1 ≤ |z.im|) :
    |(Complex.digamma z).re - Real.log ‖z‖| ≤ 4 := by
  have hn : 1 ≤ ‖z‖ := hi.trans (Complex.abs_im_le_norm z)
  have hs := Zeta23.StirlingVert.digamma_stirling hz (by linarith)
  have hsq : 1 ≤ z.im ^ 2 := by nlinarith [sq_abs z.im]
  have hb : 3 / z.im ^ 2 ≤ (3 : ℝ) :=
    (div_le_iff₀ (by positivity)).mpr (by linarith)
  have hh : ‖(1 / 2 : ℂ) / z‖ ≤ 1 := by
    rw [norm_div, show ‖(1 / 2 : ℂ)‖ = (1 / 2 : ℝ) by norm_num]
    exact (div_le_iff₀ (by linarith)).mpr (by linarith)
  have he : ‖Complex.digamma z - Complex.log z‖ ≤ 4 := by
    calc
      _ = ‖(Complex.digamma z - Complex.log z + (1 / 2 : ℂ) / z)
          - (1 / 2 : ℂ) / z‖ := by congr 1; ring
      _ ≤ ‖Complex.digamma z - Complex.log z + (1 / 2 : ℂ) / z‖
          + ‖(1 / 2 : ℂ) / z‖ := norm_sub_le _ _
      _ ≤ 4 := by linarith
  have hr := Complex.abs_re_le_norm (Complex.digamma z - Complex.log z)
  simpa only [Complex.sub_re, Complex.log_re] using hr.trans he

/-- The actual native archimedean symbol differs from the canonical
logarithmic weight by a globally bounded real function. -/
theorem neutralActualZetaArchimedean_log_bound :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ ξ : ℝ,
      |compactWindowArchimedeanSymbol (2 * Real.pi * ξ)
        - logarithmicFourierWeight ξ| ≤ C := by
  have htail : ∀ ξ : ℝ, 1 ≤ |ξ| →
      |compactWindowArchimedeanSymbol (2 * Real.pi * ξ)
        - logarithmicFourierWeight ξ| ≤
        4 + |Real.log Real.pi| + |Real.log (Real.exp 1 + 1)|
          + |Real.log (Real.pi + 1)| := by
    intro ξ hξ
    let z : ℂ := 1 / 4 + Complex.I * ((Real.pi * ξ : ℝ) : ℂ)
    have hre : z.re = 1 / 4 := by simp [z]
    have him : z.im = Real.pi * ξ := by simp [z]
    have hpi : 1 ≤ Real.pi := by linarith [Real.pi_gt_three]
    have hab : |z.im| = Real.pi * |ξ| := by
      rw [him, abs_mul, abs_of_pos Real.pi_pos]
    have hi : 1 ≤ |z.im| := by rw [hab]; nlinarith
    have hnorm : |ξ| ≤ ‖z‖ := by
      have h := Complex.abs_im_le_norm z
      rw [hab] at h
      nlinarith [abs_nonneg ξ]
    have hn : 1 ≤ ‖z‖ := hξ.trans hnorm
    have hnpos : 0 < ‖z‖ := by linarith
    have hupper : ‖z‖ ≤ 1 / 4 + Real.pi * |ξ| := by
      have h := norm_add_le (1 / 4 : ℂ)
        (Complex.I * ((Real.pi * ξ : ℝ) : ℂ))
      simpa only [z, norm_mul, Complex.norm_I, one_mul, Complex.norm_real,
        Real.norm_eq_abs, abs_mul, abs_of_pos Real.pi_pos,
        show ‖(1 / 4 : ℂ)‖ = (1 / 4 : ℝ) by norm_num] using h
    let x : ℝ := Real.exp 1 + |ξ|
    have hx : 0 < x := by dsimp [x]; positivity
    have he : 1 ≤ Real.exp 1 := Real.one_le_exp.mpr (by norm_num)
    have hlo : x ≤ (Real.exp 1 + 1) * ‖z‖ := by
      dsimp [x]
      nlinarith [mul_le_mul_of_nonneg_left hn (Real.exp_nonneg 1)]
    have hup : ‖z‖ ≤ (Real.pi + 1) * x := by
      dsimp [x]
      nlinarith [mul_nonneg Real.pi_pos.le (Real.exp_nonneg 1),
        abs_nonneg ξ]
    have hl := Real.log_le_log hx hlo
    rw [Real.log_mul (by positivity) hnpos.ne'] at hl
    have hu := Real.log_le_log hnpos hup
    rw [Real.log_mul (by positivity) hx.ne'] at hu
    have hlog : |Real.log ‖z‖ - Real.log x| ≤
        |Real.log (Real.exp 1 + 1)| + |Real.log (Real.pi + 1)| := by
      apply abs_le.mpr
      constructor <;> linarith [le_abs_self (Real.log (Real.exp 1 + 1)),
        le_abs_self (Real.log (Real.pi + 1)),
        abs_nonneg (Real.log (Real.exp 1 + 1)),
        abs_nonneg (Real.log (Real.pi + 1))]
    have hd := neutralActualZetaDigamma_log_error (z := z)
      (by rw [hre]; norm_num) hi
    have hz : ((1 : ℂ) / 4) + Complex.I * (((2 * Real.pi * ξ : ℝ) : ℂ) / 2)
        = z := by dsimp [z]; push_cast; ring
    unfold compactWindowArchimedeanSymbol logarithmicFourierWeight
    rw [hz]
    change |(Complex.digamma z).re - Real.log Real.pi - Real.log x| ≤ _
    have h := abs_add_le ((Complex.digamma z).re - Real.log ‖z‖)
      (Real.log ‖z‖ - Real.log x)
    have h' := abs_sub_le ((Complex.digamma z).re - Real.log x) (Real.log Real.pi)
    have heq : (Complex.digamma z).re - Real.log ‖z‖ +
        (Real.log ‖z‖ - Real.log x) = (Complex.digamma z).re - Real.log x := by ring
    rw [heq] at h
    have heq' : (Complex.digamma z).re - Real.log x - Real.log Real.pi =
        (Complex.digamma z).re - Real.log Real.pi - Real.log x := by ring
    rw [heq'] at h'
    linarith
  have hc : Continuous (fun ξ : ℝ =>
      compactWindowArchimedeanSymbol (2 * Real.pi * ξ)) := by
    have h := neutralActualZetaGammaBracket_continuous.comp
      (continuous_const.mul continuous_id : Continuous (fun ξ : ℝ => 2 * Real.pi * ξ))
    simpa only [neutralActualZetaGammaBracket_native] using h
  have hcont : Continuous (fun ξ : ℝ =>
      |compactWindowArchimedeanSymbol (2 * Real.pi * ξ)
        - logarithmicFourierWeight ξ|) :=
    (hc.sub logarithmicFourierWeight_continuous).abs
  obtain ⟨B, hB⟩ := isCompact_Icc.bddAbove_image hcont.continuousOn
  let T : ℝ := 4 + |Real.log Real.pi| + |Real.log (Real.exp 1 + 1)|
    + |Real.log (Real.pi + 1)|
  refine ⟨max 0 (max B T), le_max_left _ _, ?_⟩
  intro ξ
  by_cases hξ : 1 ≤ |ξ|
  · exact (htail ξ hξ).trans ((le_max_right B T).trans (le_max_right 0 (max B T)))
  · have hm : ξ ∈ Set.Icc (-1 : ℝ) 1 := by
      have h := abs_le.mp (le_of_lt (lt_of_not_ge hξ))
      exact h
    exact (hB ⟨ξ, hm, rfl⟩).trans
      ((le_max_left B T).trans (le_max_right 0 (max B T)))

/-- Absolute coefficient mass of the unchanged threshold-correct finite prime set. -/
def neutralActualZetaPrimeSymbolBound (a : ℝ) : ℝ :=
  ∑ n ∈ rightLimitPrimePowerFinset a, |compactWindowPrimeCoefficient n|

theorem neutralActualZetaPrimeSymbolBound_nonneg (a : ℝ) :
    0 ≤ neutralActualZetaPrimeSymbolBound a :=
  Finset.sum_nonneg (fun _ _ => abs_nonneg _)

/-- The actual finite prime symbol is uniformly bounded, including threshold primes. -/
theorem neutralActualZetaPrimeSymbol_abs_le (a t : ℝ) :
    |rightLimitPrimeSymbol a t| ≤ neutralActualZetaPrimeSymbolBound a := by
  unfold rightLimitPrimeSymbol neutralActualZetaPrimeSymbolBound
  calc
    _ ≤ ∑ n ∈ rightLimitPrimePowerFinset a,
        |compactWindowPrimeCoefficient n * Real.cos (t * Real.log (n : ℝ))| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ _ := Finset.sum_le_sum (fun n _ => by
      rw [abs_mul]
      have h := mul_le_mul_of_nonneg_left (Real.abs_cos_le_one (t * Real.log (n : ℝ)))
        (abs_nonneg (compactWindowPrimeCoefficient n))
      simpa only [mul_one] using h)

/-- Unconditional logarithmic envelope for the actual native Weil symbol.
No source positivity or all-derivative temperate-growth assumption occurs. -/
theorem neutralActualZetaNativeSymbol_log_bound (a : ℝ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ ξ : ℝ,
      |rightLimitCompactWeilSymbolMathlib a ξ - logarithmicFourierWeight ξ| ≤ C := by
  obtain ⟨B, hB, hb⟩ := neutralActualZetaArchimedean_log_bound
  refine ⟨B + neutralActualZetaPrimeSymbolBound a,
    add_nonneg hB (neutralActualZetaPrimeSymbolBound_nonneg a), ?_⟩
  intro ξ
  have h := abs_sub_le
    (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) - logarithmicFourierWeight ξ)
    (rightLimitPrimeSymbol a (2 * Real.pi * ξ))
  have hp := neutralActualZetaPrimeSymbol_abs_le a (2 * Real.pi * ξ)
  unfold rightLimitCompactWeilSymbolMathlib rightLimitCompactWeilSymbol
  have he : compactWindowArchimedeanSymbol (2 * Real.pi * ξ) -
      rightLimitPrimeSymbol a (2 * Real.pi * ξ) - logarithmicFourierWeight ξ =
      (compactWindowArchimedeanSymbol (2 * Real.pi * ξ) - logarithmicFourierWeight ξ) -
        rightLimitPrimeSymbol a (2 * Real.pi * ξ) := by ring
  rw [he]
  exact h.trans (add_le_add (hb ξ) hp)

/-- Concrete shifted coercivity and upper form bound for the native symbol.
This is not unshifted background positivity or a WD-T10 factorization. -/
theorem neutralActualZetaNativeSymbol_shifted_log_bounds (a : ℝ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ ξ : ℝ,
      logarithmicFourierWeight ξ ≤ rightLimitCompactWeilSymbolMathlib a ξ + C ∧
      rightLimitCompactWeilSymbolMathlib a ξ + C ≤
        (1 + 2 * C) * logarithmicFourierWeight ξ := by
  obtain ⟨C, hC, hb⟩ := neutralActualZetaNativeSymbol_log_bound a
  refine ⟨C, hC, ?_⟩
  intro ξ
  have h := abs_le.mp (hb ξ)
  have hw := one_le_logarithmicFourierWeight ξ
  have hm := mul_le_mul_of_nonneg_left hw hC
  constructor <;> nlinarith

end
end WeilDefect
