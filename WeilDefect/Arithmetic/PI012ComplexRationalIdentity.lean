import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-!
PI012 independent complex rational Fourier coefficient proof CANDIDATE.
Does not import Zeta23, original IV011, or Masullo. Real source names
are attached only in the separately compiled PI012SourceFourierAtom file.

No compiler/axiom PASS is asserted until the actual dedicated CI receipts.
-/

/-- The alpha-square plus frequency-square denominator is strictly positive. -/
theorem pi012Denominator_pos (α r : ℝ) (hα : 0 < α) :
    0 < α ^ 2 + r ^ 2 := by
  have hh : 0 < α * α := mul_pos hα hα
  nlinarith [sq_nonneg r]

/-- The left conjugate frequency shift is nonzero if alpha is positive. -/
theorem pi012ComplexShiftMinus_ne_zero (α r : ℝ) (hα : 0 < α) :
    (α : ℂ) - Complex.I * (r : ℂ) ≠ 0 := by
  intro h
  have hre := congrArg Complex.re h
  have hzero : α = 0 := by
    simpa [Complex.mul_re] using hre
  exact (ne_of_gt hα) hzero

/-- The right conjugate frequency shift is nonzero if alpha is positive. -/
theorem pi012ComplexShiftPlus_ne_zero (α r : ℝ) (hα : 0 < α) :
    (α : ℂ) + Complex.I * (r : ℂ) ≠ 0 := by
  intro h
  have hre := congrArg Complex.re h
  have hzero : α = 0 := by
    simpa [Complex.mul_re] using hre
  exact (ne_of_gt hα) hzero

/-- Pure field identity, requiring only the actual nonzero factors. -/
theorem pi012ReciprocalPair (a b : ℂ)
    (hm : a - b ≠ 0) (hp : a + b ≠ 0) :
    (1 : ℂ) / (a - b) + (1 : ℂ) / (a + b) =
      (2 * a) / (a ^ 2 - b ^ 2) := by
  have hden : a ^ 2 - b ^ 2 ≠ 0 := by
    have hh : (a - b) * (a + b) ≠ 0 := mul_ne_zero hm hp
    convert hh using 1 <;> ring
  field_simp [hm, hp, hden]
  <;> ring

/-- Multiplying the imaginary frequency by i changes its square's sign. -/
theorem pi012ImaginaryShift_sq (r : ℝ) :
    (Complex.I * (r : ℂ)) ^ 2 = - (r : ℂ) ^ 2 := by
  calc
    _ = Complex.I ^ 2 * (r : ℂ) ^ 2 := by ring
    _ = - (r : ℂ) ^ 2 := by simp [Complex.I_sq]

/-- Exact complex Fourier reciprocal identity with no lost 2pi or sign. -/
theorem pi012FourierReciprocalClosed (α r : ℝ) (hα : 0 < α) :
    (1 : ℂ) / ((α : ℂ) - Complex.I * (r : ℂ)) +
    (1 : ℂ) / ((α : ℂ) + Complex.I * (r : ℂ)) =
      (2 * (α : ℂ)) / ((α : ℂ) ^ 2 + (r : ℂ) ^ 2) := by
  have hm := pi012ComplexShiftMinus_ne_zero α r hα
  have hp := pi012ComplexShiftPlus_ne_zero α r hα
  calc
    _ = (2 * (α : ℂ)) / ((α : ℂ) ^ 2 - (Complex.I * (r : ℂ)) ^ 2) :=
      pi012ReciprocalPair _ _ hm hp
    _ = (2 * (α : ℂ)) / ((α : ℂ) ^ 2 + (r : ℂ) ^ 2) := by
      rw [pi012ImaginaryShift_sq]
      ring

#print axioms pi012Denominator_pos
#print axioms pi012ComplexShiftMinus_ne_zero
#print axioms pi012ComplexShiftPlus_ne_zero
#print axioms pi012ReciprocalPair
#print axioms pi012ImaginaryShift_sq
#print axioms pi012FourierReciprocalClosed

end
end WeilDefect
