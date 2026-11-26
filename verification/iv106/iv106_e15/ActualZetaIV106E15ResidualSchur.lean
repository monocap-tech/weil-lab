import WeilDefect.Arithmetic.ActualZetaIV106E14SchurRows

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate BigOperators

/-- A sharp quadratic error bound using only the coercivity constant,
not the full operator norm. -/
theorem neutralIV106E15Residual_energy {H : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (A : H →L[ℂ] H) (α : ℝ) (hα : 0 < α)
    (hA : ∀ x, α*‖x‖^2 ≤ (inner ℂ x (A x)).re) (d : H) :
    0 ≤ (inner ℂ d (A d)).re ∧
    (inner ℂ d (A d)).re ≤ α⁻¹*‖A d‖^2 := by
  constructor
  · exact (mul_nonneg hα.le (sq_nonneg _)).trans (hA d)
  · have hb := neutralIV106E12Bounded_below A α hα hA d
    have hn : ‖d‖ ≤ α⁻¹*‖A d‖ := by
      rw [← div_eq_inv_mul]
      exact (le_div_iff₀ hα).mpr (by simpa only [mul_comm] using hb)
    calc
      _ ≤ |(inner ℂ d (A d)).re| := le_abs_self _
      _ ≤ ‖inner ℂ d (A d)‖ := Complex.abs_re_le_norm _
      _ ≤ ‖d‖*‖A d‖ := norm_inner_le_norm _ _
      _ ≤ (α⁻¹*‖A d‖)*‖A d‖ :=
        mul_le_mul_of_nonneg_right hn (norm_nonneg _)
      _ = _ := by ring

def neutralIV106E15RHS (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) : neutralIV106E12Kernel k hk :=
  (ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL)
    (neutralActualZetaLogWeilFormOperator (11/10) y.val)

def neutralIV106E15Residual (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk) :
    neutralIV106E12Kernel k hk :=
  neutralIV106E15RHS k hk y - neutralIV106E12Compressed k hk t

/-- Residual equals the compressed operator applied to the trial error. -/
theorem neutralIV106E15Residual_eq (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk) :
    neutralIV106E15Residual k hk y t =
      neutralIV106E12Compressed k hk (neutralIV106E13Response k hk e y - t) := by
  unfold neutralIV106E15Residual neutralIV106E15RHS
  rw [map_sub, ← he]
  simp [neutralIV106E13Response]

theorem neutralIV106E15Compression_energy (k : ℕ) (hk : 0 < k)
    (x : neutralIV106E12Kernel k hk) :
    (inner ℂ x (neutralIV106E12Compressed k hk x)).re =
      neutralIV106E13Energy x.val := by
  unfold neutralIV106E13Energy
  change (inner ℂ x ((ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL)
    (neutralActualZetaLogWeilFormOperator (11/10) x.val))).re = _
  rw [adjoint_inner_right]
  rfl

/-- Exact two-sided Schur enclosure from any trial in the genuine kernel. -/
theorem neutralIV106E15Enclosure (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk) :
    neutralIV106E13Energy (y.val-t.val) -
      neutralIV106E11Alpha⁻¹*‖neutralIV106E15Residual k hk y t‖^2 ≤
        neutralIV106E13Schur k hk e y ∧
    neutralIV106E13Schur k hk e y ≤ neutralIV106E13Energy (y.val-t.val) := by
  let d := neutralIV106E13Response k hk e y - t
  have hc := neutralIV106E13Actual_completion k hk e he (-t) y
  have hc' : neutralIV106E13Energy (y.val-t.val) =
      neutralIV106E13Energy d.val + neutralIV106E13Schur k hk e y := by
    simpa [d, sub_eq_add_neg, add_comm] using hc
  have h := neutralIV106E15Residual_energy (neutralIV106E12Compressed k hk)
    neutralIV106E11Alpha neutralIV106E11Alpha_pos
    (neutralIV106E12Compressed_margin k hk) d
  rw [neutralIV106E15Compression_energy, ← neutralIV106E15Residual_eq k hk e he y t] at h
  exact ⟨by linarith only [hc',h.2], by linarith only [hc',h.1]⟩

/-- Residual contraction uses the ambient norm and needs no exact
orthogonal projection computation. -/
theorem neutralIV106E15Ambient_residual (k : ℕ) (hk : 0 < k)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk) :
    ‖neutralIV106E15Residual k hk y t‖ ≤
      ‖neutralActualZetaLogWeilFormOperator (11/10) (y.val-t.val)‖ := by
  let K := neutralIV106E12Kernel k hk
  let W := neutralActualZetaLogWeilFormOperator (11/10)
  have hr : neutralIV106E15Residual k hk y t =
      (ContinuousLinearMap.adjoint K.subtypeL) (W (y.val-t.val)) := by
    simp [neutralIV106E15Residual, neutralIV106E15RHS,
      neutralIV106E12Compressed, K, W, map_sub]
  rw [hr]
  have hn : ‖ContinuousLinearMap.adjoint K.subtypeL‖ ≤ 1 := by
    rw [ContinuousLinearMap.norm_adjoint_eq]
    apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
    intro x
    simp
  exact ((ContinuousLinearMap.adjoint K.subtypeL).le_opNorm _).trans
    (by simpa using mul_le_mul_of_nonneg_right hn (norm_nonneg (W (y.val-t.val))))

/-- A uniform trial lower energy dominates the true Schur form, and
therefore suffices for global native positivity. -/
theorem neutralIV106E15Trial_receiver (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (t : neutralIV106E13Finite k hk → neutralIV106E12Kernel k hk)
    (h : ∀ y, neutralIV106E11Alpha⁻¹*‖neutralIV106E15Residual k hk y (t y)‖^2 ≤
      neutralIV106E13Energy (y.val-(t y).val)) :
    ∀ q : neutralIV106E13H, 0 ≤ neutralIV106E13Energy q := by
  apply (neutralIV106E13Nonnegative_iff k hk e he).mpr
  intro y
  exact (sub_nonneg.mpr (h y)).trans (neutralIV106E15Enclosure k hk e he y (t y)).1

/-- A negative trial energy is already a negative Schur witness,
independent of the residual error. -/
theorem neutralIV106E15Negative_receiver (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (y : neutralIV106E13Finite k hk) (t : neutralIV106E12Kernel k hk)
    (h : neutralIV106E13Energy (y.val-t.val) < 0) :
    neutralIV106E13Schur k hk e y < 0 :=
  (neutralIV106E15Enclosure k hk e he y t).2.trans_lt h

#print axioms neutralIV106E15Residual_energy
#print axioms neutralIV106E15Residual_eq
#print axioms neutralIV106E15Compression_energy
#print axioms neutralIV106E15Enclosure
#print axioms neutralIV106E15Ambient_residual
#print axioms neutralIV106E15Trial_receiver
#print axioms neutralIV106E15Negative_receiver
end
end WeilDefect
