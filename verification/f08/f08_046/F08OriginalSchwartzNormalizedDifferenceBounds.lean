import WeilDefect.Generated.F08.CompactSchwartzCommonScaledSupport

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap

/-!
F08-046: uniform size estimate for the *exact* original F08-030
normalized Schwartz frequency dilation representative at λ near 1.

For 1/2 ≤ λ ≤ 3/2, the normalization is
  Complex.ofReal (Real.sqrt (abs λ)) • g (λ * ξ).
The true source Schwartz seminorm supplies the global bound M,
not a new surrogate norm. The support theorem F08-045 will separately
force the difference to vanish outside a fixed common interval.

The present theorem alone does not construct an integrable indicator,
prove dominated convergence or give L² strong convergence.
Physically compact support, logarithmic Weil form-core positivity
and RH remain entirely separate obligations.
-/

/-- Uniform actual Schwartz representative difference bound on the
fixed scale interval around the identity. -/
theorem f08_046_originalSchwartz_normalizedDifferenceBound
    (g : 𝓢(ℝ, ℂ)) :
    ∃ M : ℝ, 0 ≤ M ∧
      ∀ lam ξ : ℝ,
        (1 / 2 : ℝ) ≤ lam →
        lam ≤ (3 / 2 : ℝ) →
          ‖(Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ) - g ξ‖ ≤
            (Real.sqrt (3 / 2 : ℝ) + 1) * M := by
  obtain ⟨M, hM, hg⟩ := f08_042_originalSchwartz_globalBound g
  refine ⟨M, hM, ?_⟩
  intro lam ξ hlam_low hlam_high
  have hlam_nonneg : 0 ≤ lam := by linarith
  have hsqrt : Real.sqrt (abs lam) ≤ Real.sqrt (3 / 2 : ℝ) := by
    apply Real.sqrt_le_sqrt
    simpa only [abs_of_nonneg hlam_nonneg] using hlam_high
  have hfac :
      ‖Complex.ofReal (Real.sqrt (abs lam))‖ ≤ Real.sqrt (3 / 2 : ℝ) := by
    rw [Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (Real.sqrt_nonneg _)]
    exact hsqrt
  have hscaled :
      ‖(Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ)‖ ≤
        Real.sqrt (3 / 2 : ℝ) * M := by
    rw [norm_smul]
    calc
      ‖Complex.ofReal (Real.sqrt (abs lam))‖ * ‖g (lam * ξ)‖ ≤
          Real.sqrt (3 / 2 : ℝ) * ‖g (lam * ξ)‖ :=
        mul_le_mul_of_nonneg_right hfac (norm_nonneg _)
      _ ≤ Real.sqrt (3 / 2 : ℝ) * M :=
        mul_le_mul_of_nonneg_left (hg _) (Real.sqrt_nonneg _)
  calc
    ‖(Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ) - g ξ‖ ≤
        ‖(Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ)‖ + ‖g ξ‖ :=
      norm_sub_le _ _
    _ ≤ Real.sqrt (3 / 2 : ℝ) * M + M :=
      add_le_add hscaled (hg ξ)
    _ = (Real.sqrt (3 / 2 : ℝ) + 1) * M := by ring

/-- A single real scalar dominates the exact *squared norm*
of the original normalized Schwartz representative difference,
uniformly over all frequencies and near-identity real scales.
The integrable common-support indicator is a separate next step. -/
theorem f08_046_originalSchwartz_normalizedDifferenceSquareBound
    (g : 𝓢(ℝ, ℂ)) :
    ∃ M : ℝ, 0 ≤ M ∧
      ∀ lam ξ : ℝ,
        (1 / 2 : ℝ) ≤ lam →
        lam ≤ (3 / 2 : ℝ) →
          ‖(Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ) - g ξ‖ ^ 2 ≤
            ((Real.sqrt (3 / 2 : ℝ) + 1) * M) ^ 2 := by
  obtain ⟨M, hM, hbound⟩ :=
    f08_046_originalSchwartz_normalizedDifferenceBound g
  refine ⟨M, hM, ?_⟩
  intro lam ξ hlam_low hlam_high
  have hle := hbound lam ξ hlam_low hlam_high
  have hleft :
      0 ≤ ‖(Complex.ofReal (Real.sqrt (abs lam))) • g (lam * ξ) - g ξ‖ :=
    norm_nonneg _
  have hright : 0 ≤ (Real.sqrt (3 / 2 : ℝ) + 1) * M := by
    apply mul_nonneg
    · exact add_nonneg (Real.sqrt_nonneg _) (by norm_num)
    · exact hM
  have hproduct := mul_nonneg (sub_nonneg.mpr hle) (add_nonneg hright hleft)
  nlinarith

#print axioms f08_046_originalSchwartz_normalizedDifferenceBound
#print axioms f08_046_originalSchwartz_normalizedDifferenceSquareBound

end
end WeilDefect
