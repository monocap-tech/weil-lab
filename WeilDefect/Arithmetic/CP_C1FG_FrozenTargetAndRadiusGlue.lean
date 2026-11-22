import WeilDefect.Arithmetic.CP_C1E_FrozenFlatSchwartz
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP-C1(F/G): frozen actual-source target interface and two-radius gluing.

Every frozen test is the exactly prescribed original CP001 flat Schwartz
function from kernel-accepted CP-C1(E). The original signed mixed arithmetic
form and the COMPLETE original zeta-divisor form are the IV007/IV008 objects.
The nine readings here are HYPOTHESES on an independently supplied Hermitian
target T. They have not been verified for an independent spectral model.

The old two probes are literally identical in either frozen central-radius
family. Both the arithmetic and divisor old 2x2 blocks therefore agree
across radii by definition, not from a numerical enclosure.

This file makes NO nonnegativity, RH, finite-height zero-roster,
finite spectral-error bound, or support-independent transfer assertion.
SOURCE CANDIDATE until genuine Lean4.34 and strict standard-axiom receipts.
-/

/-- The certified exact frozen source has the complete-divisor target
dictionary whenever an independent Hermitian matrix satisfies ALL NINE
original real physical diagonal/+1/i phase equations. No such external
equations are assumed to be verified in this theorem. -/
theorem neutralCPC1F_frozenDivisor_eq_target_of_nine_readings
    (r : ℝ) (hr : 0 < r) (hrmax : r ≤ 1 / 500)
    (T : Fin 3 → Fin 3 → ℂ)
    (hHerm : ∀ i j : Fin 3, conj (T i j) = T j i)
    (hDiag : ∀ i : Fin 3,
      (T i i).re =
        neutralCPC1DPhysicalEnergy (11/10)
          (neutralCPC1EFrozenFamily r hr i))
    (hPlus : ∀ i j : Fin 3, i < j →
      (T i j).re =
        (neutralCPC1DPhysicalEnergy (11/10)
            (neutralCPC1EFrozenFamily r hr i +
              neutralCPC1EFrozenFamily r hr j) -
          neutralCPC1DPhysicalEnergy (11/10)
            (neutralCPC1EFrozenFamily r hr i) -
          neutralCPC1DPhysicalEnergy (11/10)
            (neutralCPC1EFrozenFamily r hr j)) / 2)
    (hPhase : ∀ i j : Fin 3, i < j →
      (T i j).im =
        -(neutralCPC1DPhysicalEnergy (11/10)
            (neutralCPC1EFrozenFamily r hr i +
              Complex.I • neutralCPC1EFrozenFamily r hr j) -
          neutralCPC1DPhysicalEnergy (11/10)
            (neutralCPC1EFrozenFamily r hr i) -
          neutralCPC1DPhysicalEnergy (11/10)
            (neutralCPC1EFrozenFamily r hr j)) / 2) :
    (fun i j : Fin 3 =>
      neutralIV007OriginalDivisorEntry (11/10)
        (neutralCPC1EFrozenFamily r hr) i j) = T := by
  calc
    (fun i j : Fin 3 =>
      neutralIV007OriginalDivisorEntry (11/10)
        (neutralCPC1EFrozenFamily r hr) i j) =
        (fun i j : Fin 3 =>
          neutralIV007OriginalMixedEntry (11/10)
            (neutralCPC1EFrozenFamily r hr) i j) :=
          (neutralCPC1EFrozenOriginal_matrix_eq_completeDivisor
            r hr hrmax).symm
    _ = T :=
      neutralCPC1D_original_eq_target_of_nine_phase_readings
        (11/10) (neutralCPC1EFrozenFamily r hr)
        (neutralCPC1EFrozenFamily_supportedOriginal r hr hrmax)
        T hHerm hDiag hPlus hPhase

/-- Both frozen old physical functions are literally the same under
either new central-radius choice. The central function may differ. -/
theorem neutralCPC1G_frozenOldPair_same
    (r₁ r₂ : ℝ) (hr₁ : 0 < r₁) (hr₂ : 0 < r₂) :
    neutralCPC1EFrozenFamily r₁ hr₁ (0 : Fin 3) =
        neutralCPC1EFrozenFamily r₂ hr₂ (0 : Fin 3) ∧
    neutralCPC1EFrozenFamily r₁ hr₁ (1 : Fin 3) =
        neutralCPC1EFrozenFamily r₂ hr₂ (1 : Fin 3) := by
  constructor <;> rfl

/-- The four genuinely physical diagonal, +1 and i-phase readings
on the two frozen OLD tests are identical across either radius. -/
theorem neutralCPC1G_frozenFourOldReadings_same
    (r₁ r₂ : ℝ) (hr₁ : 0 < r₁) (hr₂ : 0 < r₂) :
    neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₁ hr₁ (0 : Fin 3)) =
      neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₂ hr₂ (0 : Fin 3)) ∧
    neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₁ hr₁ (1 : Fin 3)) =
      neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₂ hr₂ (1 : Fin 3)) ∧
    neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₁ hr₁ (0 : Fin 3) +
         neutralCPC1EFrozenFamily r₁ hr₁ (1 : Fin 3)) =
      neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₂ hr₂ (0 : Fin 3) +
         neutralCPC1EFrozenFamily r₂ hr₂ (1 : Fin 3)) ∧
    neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₁ hr₁ (0 : Fin 3) +
         Complex.I • neutralCPC1EFrozenFamily r₁ hr₁ (1 : Fin 3)) =
      neutralCPC1DPhysicalEnergy (11/10)
        (neutralCPC1EFrozenFamily r₂ hr₂ (0 : Fin 3) +
         Complex.I • neutralCPC1EFrozenFamily r₂ hr₂ (1 : Fin 3)) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> rfl

/-- The actual signed original Weil old two-bump arithmetic block is
independent of the central test radius. This is NOT target compatibility. -/
theorem neutralCPC1G_frozenOriginalOldBlock_same
    (r₁ r₂ : ℝ) (hr₁ : 0 < r₁) (hr₂ : 0 < r₂)
    (i j : Fin 3) (hi : i = 0 ∨ i = 1) (hj : j = 0 ∨ j = 1) :
    neutralIV007OriginalMixedEntry (11/10)
        (neutralCPC1EFrozenFamily r₁ hr₁) i j =
      neutralIV007OriginalMixedEntry (11/10)
        (neutralCPC1EFrozenFamily r₂ hr₂) i j := by
  rcases hi with rfl | rfl <;> rcases hj with rfl | rfl <;> rfl

/-- The complete, untruncated original zeta-divisor old 2x2 block
also agrees between the two frozen three-bump compressions. -/
theorem neutralCPC1G_frozenDivisorOldBlock_same
    (r₁ r₂ : ℝ) (hr₁ : 0 < r₁) (hr₂ : 0 < r₂)
    (i j : Fin 3) (hi : i = 0 ∨ i = 1) (hj : j = 0 ∨ j = 1) :
    neutralIV007OriginalDivisorEntry (11/10)
        (neutralCPC1EFrozenFamily r₁ hr₁) i j =
      neutralIV007OriginalDivisorEntry (11/10)
        (neutralCPC1EFrozenFamily r₂ hr₂) i j := by
  rcases hi with rfl | rfl <;> rcases hj with rfl | rfl <;> rfl

#print axioms neutralCPC1EFrozenOriginal_matrix_eq_completeDivisor
#print axioms neutralCPC1D_original_eq_target_of_nine_phase_readings
#print axioms neutralCPC1F_frozenDivisor_eq_target_of_nine_readings
#print axioms neutralCPC1G_frozenOldPair_same
#print axioms neutralCPC1G_frozenFourOldReadings_same
#print axioms neutralCPC1G_frozenOriginalOldBlock_same
#print axioms neutralCPC1G_frozenDivisorOldBlock_same

end
end WeilDefect
