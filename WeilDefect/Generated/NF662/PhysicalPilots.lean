import WeilDefect.Generated.NF658.Complete
import WeilDefect.Generated.NF658.TransformPilot
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramRealIntervalTransport

namespace WeilDefect

/-!
NF662 first authentic-entry attachment pilots. These attach the original
NF658 64-digit Lean-certified physical enclosures to the exact NF661 source
indices and to the compact integer arrays. The complete 120-entry lower
triangle remains to be compiled as a separate generated proof bank.
-/

def nf662PhysicalCompactBall (i j : Fin 15) : NF591Ball :=
  ⟨(nf658Get nf658Centers i j : ℚ) / (10 ^ 64 : ℚ),
    (nf658Get nf658Radii i j : ℚ) / (10 ^ 64 : ℚ)⟩

theorem nf662Ball_oscillator_eq :
    nf662PhysicalCompactBall 0 0 = nf658H000_000Ball := by
  decide +kernel

theorem nf662Ball_poleCross_eq :
    nf662PhysicalCompactBall 14 0 = nf658H241_000Ball := by
  decide +kernel

theorem nf662Ball_poleDiag_eq :
    nf662PhysicalCompactBall 14 14 = nf658H241_241Ball := by
  decide +kernel

theorem nf662OriginalOscillator_contains :
    (nf662PhysicalCompactBall 0 0).Contains
      (neutralNF661PhysicalH 0 0) := by
  rw [nf662Ball_oscillator_eq]
  simpa [neutralNF661PhysicalH, neutralNF661Source] using
    nf658H000_000Contains

theorem nf662OriginalPoleCross_contains :
    (nf662PhysicalCompactBall 14 0).Contains
      (neutralNF661PhysicalH 14 0) := by
  rw [nf662Ball_poleCross_eq]
  simpa [neutralNF661PhysicalH, neutralNF661Source] using
    nf658H241_000Contains

theorem nf662OriginalPoleDiagonal_contains :
    (nf662PhysicalCompactBall 14 14).Contains
      (neutralNF661PhysicalH 14 14) := by
  rw [nf662Ball_poleDiag_eq]
  simpa [neutralNF661PhysicalH, neutralNF661Source] using
    nf658H241_241Contains

/-- A separate all-indices numerical symmetry gate, independent of the
real-analytic symmetry of the physical H integral. -/
theorem nf662CompactBalls_symm :
    ∀ i j : Fin 15, nf662PhysicalCompactBall i j =
      nf662PhysicalCompactBall j i := by
  decide +kernel

theorem nf662OriginalUpperPoleCross_contains :
    (nf662PhysicalCompactBall 0 14).Contains
      (neutralNF661PhysicalH 0 14) := by
  rw [nf662CompactBalls_symm 0 14,
    neutralNF661PhysicalH_symm 0 14]
  exact nf662OriginalPoleCross_contains

#print axioms nf662OriginalPoleCross_contains
#print axioms nf662OriginalUpperPoleCross_contains

end WeilDefect
