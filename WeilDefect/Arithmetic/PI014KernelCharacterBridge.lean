import WeilDefect.Arithmetic.PI007FiniteGammaKernel
import WeilDefect.Arithmetic.PI013FiniteFourierSum
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped BigOperators

/-!
PI014 local finite-kernel × positive Fourier character proof candidates.

This module uses literal PI007/PI013 objects, with the exact positive
angular Fourier sign from the inspected upstream Zeta23.paperFT definition.

IMPORTANT: Zeta23 is NOT imported. The PI branch's lakefile.toml has only
Mathlib v4.34.0, and the external Zeta23 package has a different declared
Mathlib commit. The bridge to actual Zeta23.paperFT is a separate import,
version-reconciliation and compilation obligation.

No #print axioms record is a PASS until the CI supplies real .olean receipts.
-/

/-- The positive-exponent angular Fourier character of the source paper. -/
def pi014PositiveFourierCharacter (r u : ℝ) : ℂ :=
  Complex.exp (Complex.I * (r : ℂ) * (u : ℂ))

/-- Literal PI007 physical real kernel, cast to complex and multiplied by
the exact positive-exponent angular Fourier character. -/
def pi014KernelCharacter (N : ℕ) (r u : ℝ) : ℂ :=
  (pi007FiniteGammaKernel N u : ℂ) * pi014PositiveFourierCharacter r u

/-- Separate the real damping and positive Fourier character of ONE
literal PI011 complex atom. -/
theorem pi014PhysicalAtom_factor (n : ℕ) (r u : ℝ) :
    pi011PhysicalFourierAtom (pi013GammaDamping n) r u =
      (Real.exp (-pi013GammaDamping n * |u|) : ℂ) *
        pi014PositiveFourierCharacter r u := by
  unfold pi011PhysicalFourierAtom pi014PositiveFourierCharacter
  rw [Complex.exp_add]
  congr 1
  · rw [← Complex.ofReal_exp]
    congr 1
    push_cast
    ring

/-- Identify the exact finite sum of genuine PI011 physical complex
Fourier exponentials with PI007's physical real finite kernel times the
original source-positive character. -/
theorem pi014FiniteDamped_eq_kernelCharacter
    (N : ℕ) (r u : ℝ) :
    pi013FiniteDampedFourier N r u =
      pi014KernelCharacter N r u := by
  have hfactor (n : ℕ) :
      pi011PhysicalFourierAtom (pi013GammaDamping n) r u =
        (Real.exp (-pi013GammaDamping n * |u|) : ℂ) *
          pi014PositiveFourierCharacter r u :=
    pi014PhysicalAtom_factor n r u
  calc
    pi013FiniteDampedFourier N r u =
        ∑ n ∈ Finset.range N,
          (Real.exp (-pi013GammaDamping n * |u|) : ℂ) *
            pi014PositiveFourierCharacter r u := by
      unfold pi013FiniteDampedFourier
      apply Finset.sum_congr rfl
      intro n hn
      exact hfactor n
    _ = (∑ n ∈ Finset.range N,
          (Real.exp (-pi013GammaDamping n * |u|) : ℂ)) *
            pi014PositiveFourierCharacter r u := by
      rw [Finset.sum_mul]
    _ = ((pi007FiniteGammaKernel N u : ℝ) : ℂ) *
          pi014PositiveFourierCharacter r u := by
      congr 1
      unfold pi007FiniteGammaKernel
      rw [← Complex.ofReal_sum]
      push_cast
      apply Finset.sum_congr rfl
      intro n hn
      rw [pi013GammaDamping_eq]
    _ = pi014KernelCharacter N r u := rfl

/-- The finite literal PI007 kernel Fourier pairing, using the
source's exact Fourier-character definition, but NOT yet importing the
external Zeta23 symbol. -/
def pi014PaperFTModel (N : ℕ) (r : ℝ) : ℂ :=
  ∫ u : ℝ, pi014KernelCharacter N r u

/-- Source-syntax-exact model Fourier transform equals the genuine
PI013 finite Gamma atom sum. -/
theorem pi014PaperFTModel_finite (N : ℕ) (r : ℝ) :
    pi014PaperFTModel N r =
      ∑ n ∈ Finset.range N, (pi008GammaRationalAtom n r : ℂ) := by
  have hfun :
      pi014KernelCharacter N r =
      pi013FiniteDampedFourier N r := by
    funext u
    exact (pi014FiniteDamped_eq_kernelCharacter N r u).symm
  unfold pi014PaperFTModel
  rw [hfun]
  exact pi013FiniteFourierIntegral N r

#print axioms pi014PhysicalAtom_factor
#print axioms pi014FiniteDamped_eq_kernelCharacter
#print axioms pi014PaperFTModel_finite

end
end WeilDefect
