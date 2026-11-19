import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramIntegralSquare
import WeilDefect.Generated.NF670.OriginalPhysicalFullSchur

namespace WeilDefect

/-!
NF671: close the qualitative nonnegativity of the ORIGINAL full
242-generator unweighted physical moment Gram, by exact equality
with an integral of the square of the authentic original source sum.

This is the integral-defined NF606 H on the ORIGINAL interval
[-11/10,11/10]; oscillator and sinh-pole sources remain unchanged.

The Schur positivity consequence uses the exact NF670 Riesz response
and full quadratic reindexing, and is not a numerical Schur enclosure.
Strict quantitative 227-source Schur coercivity remains OPEN.
-/

noncomputable section
open MeasureTheory Finset

/-- Every unchanged original selected real source generator is
continuous, including the genuine pole generator 241. -/
theorem nf671OriginalRealSource_continuous (i : Fin 242) :
    Continuous (nf545OriginalSelectedRealGenerator i) := by
  by_cases hi : i.val < 241
  · simp only [nf545OriginalSelectedRealGenerator, dif_pos hi]
    by_cases he : Even (nf545OriginalOscillatorNodeAt ⟨i.val, hi⟩).2
    · simp only [if_pos he]
      fun_prop
    · simp only [if_neg he]
      fun_prop
  · simp only [nf545OriginalSelectedRealGenerator, dif_neg hi]
    fun_prop

/-- The authentic original NF606 full 242-source physical H equals
the generic Gram of the exact unchanged analytic selected generators;
there is no box, discrete surrogate or transformed operator here. -/
theorem nf671OriginalPhysicalH_eq_integralGram :
    neutralNF606PhysicalH =
      neutralNF671IntegralGram nf545OriginalSelectedRealGenerator
        (-(11 / 10 : ℝ)) (11 / 10 : ℝ) := rfl

/-- Exact original unweighted full 242-source integral-square identity.
This is a real physical quadratic form, not a signed Weil identity. -/
theorem nf671OriginalPhysicalH_energy_eq_square
    (z : Fin 242 → ℝ) :
    neutralNF661Quadratic neutralNF606PhysicalH z =
      ∫ t in (-(11 / 10 : ℝ))..(11 / 10 : ℝ),
        (∑ i : Fin 242,
          z i * nf545OriginalSelectedRealGenerator i t)^2 := by
  rw [nf671OriginalPhysicalH_eq_integralGram]
  exact neutralNF671IntegralGram_energy_eq_square
    nf545OriginalSelectedRealGenerator
    nf671OriginalRealSource_continuous
    (-(11 / 10 : ℝ)) (11 / 10 : ℝ) z

/-- UNCONDITIONAL PSD of the original full physical 242-source Gram.
This is qualitative (0 ≤ energy), not a c>0 uniform eigenvalue
certificate, and not the signed global Weil form. -/
theorem nf671OriginalFullPhysicalGram_nonnegative
    (z : Fin 242 → ℝ) :
    0 ≤ neutralNF661Quadratic neutralNF606PhysicalH z := by
  rw [nf671OriginalPhysicalH_energy_eq_square]
  apply intervalIntegral.integral_nonneg_of_forall (by norm_num)
  intro t
  exact sq_nonneg _

/-- The exact actual 15+227 physical block energy is nonnegative
for any original source coefficients, by the integral square proof. -/
theorem nf671ActualPhysicalBlock_nonnegative
    (x : Fin 15 → ℝ) (y : Fin 227 → ℝ) :
    0 ≤ neutralNF669BlockEnergy
      nf669OriginalA nf669OriginalB nf669OriginalC x y := by
  have h := nf671OriginalFullPhysicalGram_nonnegative
    (nf670AssembleOriginal x y)
  rw [nf670FullPhysicalGram_blockEnergy] at h
  exact h

/-- This is the central NF671 Schur closure: the original 227-source
complementary remainder is nonnegative, without assuming it and
without introducing a rounded cofinite eigenvalue certificate.

The crucial identity is the NF670 exact Riesz response to ORIGINAL B,
not an arbitrary blockwise inverse hypothesis. -/
theorem nf671ActualPhysicalSchur_nonnegative
    (y : Fin 227 → ℝ) :
    0 ≤ nf670ActualSchurEnergy y := by
  exact (nf670OriginalFullNonnegative_iff_schur).mp
    nf671OriginalFullPhysicalGram_nonnegative y

/-- Fully source-attached original physical Schur square completion:
the positive A part and nonnegative authentic cofinite Schur part are
both now available; no strict 227-source quantitative margin follows. -/
theorem nf671OriginalFullSchur_twoNonnegative
    (z : Fin 242 → ℝ) :
    0 ≤ neutralNF661Quadratic nf669OriginalA
      (fun i => z (neutralNF661Source i) +
        nf670ActualRieszResponse
          (fun j => z (nf669ComplementSource j)) i)
      ∧
    0 ≤ nf670ActualSchurEnergy
      (fun j => z (nf669ComplementSource j)) := by
  constructor
  · exact nf670ActualA_nonnegative _
  · exact nf671ActualPhysicalSchur_nonnegative _

#print axioms nf671OriginalRealSource_continuous
#print axioms nf671OriginalPhysicalH_eq_integralGram
#print axioms nf671OriginalPhysicalH_energy_eq_square
#print axioms nf671OriginalFullPhysicalGram_nonnegative
#print axioms nf671ActualPhysicalBlock_nonnegative
#print axioms nf671ActualPhysicalSchur_nonnegative
#print axioms nf671OriginalFullSchur_twoNonnegative

end
end WeilDefect
