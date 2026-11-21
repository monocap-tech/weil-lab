import WeilDefect.Arithmetic.PI016ImportedPaperFTCore
import WeilDefect.Arithmetic.PI015FiniteGammaSymbolBridge

namespace WeilDefect
noncomputable section

open scoped BigOperators

/-!
PI016 complete finite classical Fourier-Gamma DICTIONARY, now phrased
with the **actual** upstream Zeta23.paperFT and the **literal** PI007
and PI008 objects in ONE Lean/Mathlib 4.34 source graph.

This module is a CANDIDATE, not an accepted Lean theorem. In particular:
- The genuine upstream Zeta23.Defs source (unchanged bytes) must compile
  under v4.34.0 first; upstream's own pinned toolchain is v4.33.0-rc2.
- The earlier PI013/PI014/PI015 source candidates must compile too.
- The finite inverse 1/(2π) pairing, divergent contact compensation
  and infinite Gamma limit are NOT established in this file.
- The original IV011 source lives on a separate IV stack.
- There is no claim about Masullo's operator or RH.
-/

/-- The actual imported Zeta23 Fourier transform of the literal
PI007 kernel is exactly the actual PI014 local Fourier integral. -/
theorem pi016ImportedPaperFT_eq_localModel (N : ℕ) (r : ℝ) :
    Zeta23.paperFT
      (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ) =
    pi014PaperFTModel N r := by
  rw [pi016ImportedPaperFT_pi007_unfold]
  rfl

/-- True source-named finite Fourier equality for PI007's physical
kernel and PI008's original finite Gamma rational atoms. -/
theorem pi016ImportedPaperFT_finiteGammaSum (N : ℕ) (r : ℝ) :
    Zeta23.paperFT
      (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ) =
    ∑ n ∈ Finset.range N, (pi008GammaRationalAtom n r : ℂ) := by
  rw [pi016ImportedPaperFT_eq_localModel]
  exact pi014PaperFTModel_finite N r

/-- Source-correct FINITE Gamma multiplier identity. The constant
H_N - gamma - log(pi) remains present; the source 'paperFT' is
actually imported, not recreated under a lookalike namespace. -/
theorem pi016FiniteGammaSymbol_eq_importedPaperFT (N : ℕ) (r : ℝ) :
    (pi008FiniteDigammaSymbol N r : ℂ) =
      (pi015FiniteHarmonic N : ℂ) -
      (Real.eulerMascheroniConstant : ℂ) -
      (Real.log Real.pi : ℂ) -
      Zeta23.paperFT
        (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ) := by
  rw [pi016ImportedPaperFT_eq_localModel]
  exact pi015FiniteSymbol_eq_localFourier N r

#print axioms pi016ImportedPaperFT_eq_localModel
#print axioms pi016ImportedPaperFT_finiteGammaSum
#print axioms pi016FiniteGammaSymbol_eq_importedPaperFT

end
end WeilDefect
