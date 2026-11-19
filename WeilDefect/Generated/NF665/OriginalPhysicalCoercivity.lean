import WeilDefect.Generated.NF664.OriginalTransformedCoercivity
import WeilDefect.Generated.NF665.OriginalPreconditionerFrame

namespace WeilDefect

/-!
NF665 terminal local physical Gram theorem candidate.

This invokes no new numerical witness: the original H is defined by
the NF606 physical integral, the 15-source set is 0..13 and 241, the
NF658 compact balls are source certificates, the NF659 integer gate
is kernel-verified, and the transformed real coercivity is the
NF664 theorem. All dependencies must pass a full Lean compiler and
axiom audit before the terminal theorem can be considered closed.
-/

noncomputable section

theorem nf665OriginalK_eq_prior :
    nf665OriginalRealK = nf662OriginalPreconditionerReal := by
  rfl

/-- The 10^-60 target is guaranteed by the already certified exact
NF659 integer gate; the proof does not run a new floating-point solve. -/
theorem nf665OriginalExactMarginGate :
    ((1 : ℝ) / (10 ^ 60 : ℝ)) *
      ((nf659KNormSq : ℝ) / (10 ^ 64 : ℝ)^2) ≤
      (nf658MinMargin : ℝ) / (10 ^ 64 : ℝ)^3 := by
  let S : ℝ := 10 ^ 64
  let R : ℝ := 10 ^ 60
  have hS : 0 < S := by
    dsimp [S]
    positivity
  have hR : 0 < R := by
    dsimp [R]
    positivity
  have hInteger :
      S * (nf659KNormSq : ℝ) <
        (nf658MinMargin : ℝ) * R := by
    dsimp [S, R]
    exact_mod_cast nf659ExactCoercivityGate
  change ((1 : ℝ) / R) *
      ((nf659KNormSq : ℝ) / S^2) ≤
      (nf658MinMargin : ℝ) / S^3
  calc
    ((1 : ℝ) / R) * ((nf659KNormSq : ℝ) / S^2) =
        (nf659KNormSq : ℝ) / (R * S^2) := by
      field_simp [ne_of_gt hR, ne_of_gt hS] <;> ring
    _ ≤ (nf658MinMargin : ℝ) / S^3 := by
      apply (div_le_div_iff₀
        (mul_pos hR (pow_pos hS 2)) (pow_pos hS 3)).2
      calc
        (nf659KNormSq : ℝ) * S^3 =
            (S * (nf659KNormSq : ℝ)) * S^2 := by ring
        _ ≤ ((nf658MinMargin : ℝ) * R) * S^2 :=
          mul_le_mul_of_nonneg_right (le_of_lt hInteger) (sq_nonneg S)
        _ = (nf658MinMargin : ℝ) * (R * S^2) := by ring

/-- The original integral-defined 15-generator physical Gram is
strictly coercive with an exact 10^-60 bound. THIS THEOREM IS A PROOF
TARGET UNTIL ITS FULL SOURCE BUILD AND AXIOM AUDIT PASS. -/
theorem nf665OriginalPhysical_coercivity :
    ∀ x : Fin 15 → ℝ,
      ((1 : ℝ) / (10 ^ 60 : ℝ)) *
        neutralNF661SqNorm x ≤
        neutralNF661Quadratic neutralNF661PhysicalH x := by
  have hMargin : ∀ y : Fin 15 → ℝ,
      ((nf658MinMargin : ℝ) / (10 ^ 64 : ℝ)^3) *
        neutralNF661SqNorm y ≤
      neutralNF661Quadratic
        (neutralNF664ActualPhysicalB nf662OriginalPreconditionerReal) y :=
    nf664AuthenticatedOriginalTransformedCoercivity
  have hCongruence : ∀ y : Fin 15 → ℝ,
      neutralNF661Quadratic
        (neutralNF664ActualPhysicalB nf662OriginalPreconditionerReal) y =
      neutralNF661Quadratic neutralNF661PhysicalH
        (neutralNF665TransposeAction nf662OriginalPreconditionerReal y) := by
    intro y
    rw [← nf665OriginalK_eq_prior]
    exact nf665OriginalPhysical_congruence y
  have hNorm : ∀ y : Fin 15 → ℝ,
      neutralNF661SqNorm
        (neutralNF665TransposeAction nf662OriginalPreconditionerReal y) ≤
      ((nf659KNormSq : ℝ) / (10 ^ 64 : ℝ)^2) *
        neutralNF661SqNorm y := by
    intro y
    rw [← nf665OriginalK_eq_prior]
    exact nf665OriginalK_normBound y
  have hOnto : ∀ x : Fin 15 → ℝ,
      ∃ y : Fin 15 → ℝ,
      neutralNF665TransposeAction nf662OriginalPreconditionerReal y = x := by
    intro x
    rw [← nf665OriginalK_eq_prior]
    exact nf665OriginalK_surjective x
  exact neutralNF661Coercivity_of_preconditioned
    neutralNF661PhysicalH
    (neutralNF664ActualPhysicalB nf662OriginalPreconditionerReal)
    (neutralNF665TransposeAction nf662OriginalPreconditionerReal)
    ((nf658MinMargin : ℝ) / (10 ^ 64 : ℝ)^3)
    ((nf659KNormSq : ℝ) / (10 ^ 64 : ℝ)^2)
    ((1 : ℝ) / (10 ^ 60 : ℝ))
    (by positivity) hMargin hCongruence hNorm hOnto
    nf665OriginalExactMarginGate

#print axioms nf665OriginalExactMarginGate
#print axioms nf665OriginalPhysical_coercivity

end
end WeilDefect
