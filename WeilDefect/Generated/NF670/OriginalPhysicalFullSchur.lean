import WeilDefect.Generated.NF670.OriginalPhysicalFullQuadratic
import WeilDefect.Generated.NF670.OriginalPhysicalRieszResponse

namespace WeilDefect

/-!
NF670: fully source-attached 242-original-generator physical Gram
Schur identity. The certified 15-dimensional A block has a uniquely
defined exact Riesz response U for all 227 complementary oscillators.

The complete original physical quadratic form equals a certified
nonnegative A-energy plus one authentic complementary Schur energy.
This statement has no "assume the cross response exists" hypothesis.

The Schur remainder is NOT claimed nonnegative by this module.
-/

noncomputable section

/-- Fully unconditional exact physical quadratic decomposition,
using original NF606 unweighted integral entries in all 242 source
directions and the constructed authentic 15-source Riesz response. -/
theorem nf670OriginalFullSchurIdentity (z : Fin 242 → ℝ) :
    neutralNF661Quadratic neutralNF606PhysicalH z =
      neutralNF661Quadratic nf669OriginalA
        (fun i => z (neutralNF661Source i) +
          nf670ActualRieszResponse
            (fun j => z (nf669ComplementSource j)) i) +
      nf670ActualSchurEnergy
        (fun j => z (nf669ComplementSource j)) := by
  rw [nf670FullPhysicalGram_allCoefficients]
  exact neutralNF669Schur_completion
    nf669OriginalA nf669OriginalB nf669OriginalC
    nf669OriginalA_symm nf670ActualRieszResponse
    nf670ActualRiesz_crossIdentity
    (fun i => z (neutralNF661Source i))
    (fun j => z (nf669ComplementSource j))

/-- Actual source-bound criterion: full physical Gram nonnegativity
is *equivalent* to the cofinite Schur nonnegativity. Unlike a
hypothetical generic Schur result, its cross response is established
by original NF665 physical Gram coercivity. -/
theorem nf670OriginalFullNonnegative_iff_schur :
    (∀ z : Fin 242 → ℝ,
      0 ≤ neutralNF661Quadratic neutralNF606PhysicalH z) ↔
    (∀ y : Fin 227 → ℝ,
      0 ≤ nf670ActualSchurEnergy y) := by
  constructor
  · intro hFull y
    apply nf670ActualPhysical_schur_necessary
    · intro x y
      have h := hFull (nf670AssembleOriginal x y)
      rw [nf670FullPhysicalGram_blockEnergy] at h
      exact h
    · exact y
  · intro hSchur z
    rw [nf670FullPhysicalGram_allCoefficients]
    exact nf670ActualPhysical_block_nonnegative_of_schur
      hSchur
      (fun i => z (neutralNF661Source i))
      (fun j => z (nf669ComplementSource j))

#print axioms nf670OriginalFullSchurIdentity
#print axioms nf670OriginalFullNonnegative_iff_schur

end
end WeilDefect
