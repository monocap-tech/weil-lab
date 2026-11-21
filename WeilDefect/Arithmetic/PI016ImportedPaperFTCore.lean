import WeilDefect.Arithmetic.PI007FiniteGammaKernel
import Zeta23.Defs

namespace WeilDefect
noncomputable section

open MeasureTheory

/-!
PI016 source-exact COMMON-COMPILER Fourier import pilot.

Unlike PI014 and PI015's local model, this module imports the **actual**
upstream Zeta23.Defs source, compiled byte-for-byte under the same
Lean/Mathlib 4.34.0 environment as the literal PI007 kernel.

The unchanged source Zeta23/Defs.lean is NOT in the PI repository or
in the default Lake graph. The PI016 compatibility workflow must
retrieve and verify git blob 8024700cbfefb54d763b487afa84c03fef58a550,
compile it into an actual local Zeta23/Defs.olean, and then compile this
module with standard-only #print axioms.

No statement in this file may be advertised as a compiler PASS before
the exact external source, both .olean files and all axiom logs are verified.

This is the minimal common-graph interface. It does NOT import PI013,
PI014 or PI015, and it does NOT assert the Fourier/Gamma finite sum.
-/

/-- Actual imported Zeta23.paperFT of the literal PI007 physical kernel,
with the source's positive angular Fourier character and no extra 2π. -/
theorem pi016ImportedPaperFT_pi007_unfold (N : ℕ) (r : ℝ) :
    Zeta23.paperFT
      (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ) =
    ∫ u : ℝ, (pi007FiniteGammaKernel N u : ℂ) *
      Complex.exp (Complex.I * (r : ℂ) * (u : ℂ)) := by
  rfl

/-- The original upstream complex-frequency definition, without silently
changing the Fourier convention. -/
theorem pi016ImportedPaperFT_pi007_complex (N : ℕ) (z : ℂ) :
    Zeta23.paperFT
      (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) z =
    ∫ u : ℝ, (pi007FiniteGammaKernel N u : ℂ) *
      Complex.exp (Complex.I * z * (u : ℂ)) := by
  rfl

#print axioms pi016ImportedPaperFT_pi007_unfold
#print axioms pi016ImportedPaperFT_pi007_complex

end
end WeilDefect
