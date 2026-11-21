import WeilDefect.Arithmetic.PI016ImportedFiniteGamma
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory

/-!
PI017 explicit minimal hypothesis interface for the finite Gamma pairing.

Theorem CANDIDATE. It uses actual imported Zeta23.paperFT and literal
PI007/PI008/PI015/PI016 objects, on a compatible Lean source graph.

This theorem is intentionally CONDITIONAL on TWO independent Fourier
inversion statements:
  (1) the inverse transform of h evaluated at zero;
  (2) the inverse convolution/product pairing with the even kernel K_N.
The finite symbol identity itself is supplied by PI016; it is NOT
duplicated as a theorem hypothesis. No Masullo trace assertion is assumed.

In particular, this does not pretend PI017 has proved the two hypotheses,
the 1/(2π) normalization, or the full IV011 Gamma limit.
A source file is not an accepted Lean kernel result without a genuine
direct compiled olean and strict #print axioms receipt.
-/

/-- Literal source-typed finite Gamma spectral pairing. -/
def pi017FiniteArchPair (N : ℕ) (h : ℝ → ℂ) : ℂ :=
  (1 / (2 * (Real.pi : ℂ))) *
    ∫ r : ℝ,
      Zeta23.paperFT h (r : ℂ) *
        (pi008FiniteDigammaSymbol N r : ℂ)

/-- Exact contact coefficient, including harmonic and Gamma constants. -/
def pi017FiniteContactCoefficient (N : ℕ) : ℂ :=
  (pi015FiniteHarmonic N : ℂ) -
    (Real.eulerMascheroniConstant : ℂ) -
    (Real.log Real.pi : ℂ)

/-- The finite Weil Gamma pairing reduces to TWO explicitly named
Fourier-inversion obligations. The contact term is NOT dropped for
h(0) ≠ 0. A proof of this implication is useful, but is NOT a
proof of the two assumptions nor of the original IV011 expression. -/
theorem pi017FiniteArchPair_of_two_fourier_inversions
    (N : ℕ) (h : ℝ → ℂ)
    (hF : Integrable (fun r : ℝ => Zeta23.paperFT h (r : ℂ)))
    (hFK : Integrable (fun r : ℝ =>
      Zeta23.paperFT h (r : ℂ) *
        Zeta23.paperFT
          (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ)))
    (hAtZero :
      (1 / (2 * (Real.pi : ℂ))) *
        (∫ r : ℝ, Zeta23.paperFT h (r : ℂ)) = h 0)
    (hKernelPair :
      (1 / (2 * (Real.pi : ℂ))) *
        (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
          Zeta23.paperFT
            (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ)) =
        ∫ u : ℝ, h u * (pi007FiniteGammaKernel N u : ℂ)) :
    pi017FiniteArchPair N h =
      pi017FiniteContactCoefficient N * h 0 -
        ∫ u : ℝ, h u * (pi007FiniteGammaKernel N u : ℂ) := by
  let c : ℂ := pi017FiniteContactCoefficient N
  have hpointwise (r : ℝ) :
      Zeta23.paperFT h (r : ℂ) *
          (pi008FiniteDigammaSymbol N r : ℂ) =
        Zeta23.paperFT h (r : ℂ) * c -
          Zeta23.paperFT h (r : ℂ) *
            Zeta23.paperFT
              (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ) := by
    rw [pi016FiniteGammaSymbol_eq_importedPaperFT]
    dsimp [c, pi017FiniteContactCoefficient]
    ring
  calc
    pi017FiniteArchPair N h =
        (1 / (2 * (Real.pi : ℂ))) *
          (∫ r : ℝ,
             Zeta23.paperFT h (r : ℂ) * c -
               Zeta23.paperFT h (r : ℂ) *
                 Zeta23.paperFT
                   (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ)) := by
      unfold pi017FiniteArchPair
      congr 1
      apply integral_congr_ae
      filter_upwards [] with r
      exact hpointwise r
    _ = c * ((1 / (2 * (Real.pi : ℂ))) *
        (∫ r : ℝ, Zeta23.paperFT h (r : ℂ))) -
          (1 / (2 * (Real.pi : ℂ))) *
            (∫ r : ℝ, Zeta23.paperFT h (r : ℂ) *
              Zeta23.paperFT
                (fun u : ℝ => (pi007FiniteGammaKernel N u : ℂ)) (r : ℂ)) := by
      rw [integral_sub (hF.mul_const c) hFK, integral_mul_const]
      ring
    _ = pi017FiniteContactCoefficient N * h 0 -
          ∫ u : ℝ, h u * (pi007FiniteGammaKernel N u : ℂ) := by
      rw [hAtZero, hKernelPair]
      rfl

#print axioms pi017FiniteArchPair_of_two_fourier_inversions

end
end WeilDefect
