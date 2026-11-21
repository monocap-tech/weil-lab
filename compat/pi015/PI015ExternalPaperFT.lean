import Zeta23.Defs

noncomputable section

open MeasureTheory

/-!
PI015 upstream-only Zeta23 source custody pilot.

This file MUST be compiled with the ACTUAL upstream:
- repository anthropics/formal-math, commit 16a5ce41304fcdaea4e0be7c132e1c361dc26da5
- subproject zeta23/
- Lean 4.33.0-rc2 (zeta23/lean-toolchain)
- Mathlib rev 51e6992efd06126df61a496bebf8f49482a4e129, the tag v4.33.0-rc2.

Unlike the local PI014 model, this module imports the genuine
Zeta23.Defs and unfolds its actual paperFT constant.

It deliberately DOES NOT import Weil-Lab PI007 or PI014 modules, which
are on a distinct Lean/Mathlib source stack. Thus it cannot by itself
certify a cross-compiler equality. No global trace theorem is assumed.

COMPILER STATUS: pending direct upstream exact-source job.
-/

/-- The imported source definition of paperFT, not a locally invented
replacement. This confirms the positive angular Fourier convention. -/
theorem pi015ImportedZeta23PaperFT_unfold (f : ℝ → ℂ) (z : ℂ) :
    Zeta23.paperFT f z =
      ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ)) := by
  rfl

/-- The same original source definition specialized to real angular
frequency, without a 2π forward factor or reversed exponent. -/
theorem pi015ImportedZeta23PaperFT_real (f : ℝ → ℂ) (r : ℝ) :
    Zeta23.paperFT f (r : ℂ) =
      ∫ u : ℝ, f u *
        Complex.exp (Complex.I * (r : ℂ) * (u : ℂ)) := by
  rfl

#print axioms pi015ImportedZeta23PaperFT_unfold
#print axioms pi015ImportedZeta23PaperFT_real
