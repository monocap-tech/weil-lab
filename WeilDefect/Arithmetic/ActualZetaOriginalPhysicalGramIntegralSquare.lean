import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramCoercivityClosure
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

namespace WeilDefect

/-!
NF671: exact finite continuous-source real Gram quadratic equals an
interval integral of the square of the full source combination.

This proves full Gram PSD without interval rounding, eigenvalue
estimation, the original NF658 witness, or a Schur sign premise.
The interval order is an explicit assumption; a zero-length interval
would only yield the non-strict statement.
-/

noncomputable section
open MeasureTheory Finset

def neutralNF671IntegralGram {n : ℕ}
    (g : Fin n → ℝ → ℝ) (a b : ℝ) (i j : Fin n) : ℝ :=
  ∫ t in a..b, g i t * g j t

def neutralNF671SourceCombination {n : ℕ}
    (g : Fin n → ℝ → ℝ) (c : Fin n → ℝ) (t : ℝ) : ℝ :=
  ∑ i : Fin n, c i * g i t

/-- Every weighted pair-product of continuous real sources is
integrable on a finite physical interval. -/
theorem neutralNF671Pair_intervalIntegrable {n : ℕ}
    (g : Fin n → ℝ → ℝ) (hg : ∀ i, Continuous (g i))
    (c : Fin n → ℝ) (a b : ℝ) (i j : Fin n) :
    IntervalIntegrable
      (fun t : ℝ => (c i * g i t) * (c j * g j t))
      volume a b := by
  have hc : Continuous
      (fun t : ℝ => (c i * g i t) * (c j * g j t)) := by
    fun_prop
  exact hc.intervalIntegrable a b

/-- Exact original-style finite Gram identity: no a.e. substitution
and no change of the selected analytic source functions. -/
theorem neutralNF671IntegralGram_energy_eq_square {n : ℕ}
    (g : Fin n → ℝ → ℝ) (hg : ∀ i, Continuous (g i))
    (a b : ℝ) (c : Fin n → ℝ) :
    neutralNF661Quadratic (neutralNF671IntegralGram g a b) c =
      ∫ t in a..b, (neutralNF671SourceCombination g c t)^2 := by
  unfold neutralNF661Quadratic neutralNF671IntegralGram
  calc
    (∑ i : Fin n, ∑ j : Fin n,
      (∫ t in a..b, g i t * g j t) * c i * c j) =
      ∑ i : Fin n, ∑ j : Fin n,
        ∫ t in a..b, (c i * g i t) * (c j * g j t) := by
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      calc
        (∫ t in a..b, g i t * g j t) * c i * c j =
          ∫ t in a..b, (g i t * g j t) * (c i * c j) := by
            rw [intervalIntegral.integral_mul_const]
            ring
        _ = ∫ t in a..b, (c i * g i t) * (c j * g j t) := by
          apply intervalIntegral.integral_congr
          intro t _
          ring
    _ = ∑ i : Fin n,
          ∫ t in a..b,
            ∑ j : Fin n, (c i * g i t) * (c j * g j t) := by
      apply Finset.sum_congr rfl
      intro i _
      symm
      exact intervalIntegral.integral_finset_sum
        (s := (Finset.univ : Finset (Fin n)))
        (fun j _ => neutralNF671Pair_intervalIntegrable g hg c a b i j)
    _ = ∫ t in a..b,
          ∑ i : Fin n, ∑ j : Fin n,
            (c i * g i t) * (c j * g j t) := by
      symm
      apply intervalIntegral.integral_finset_sum
        (s := (Finset.univ : Finset (Fin n)))
      intro i _
      have hci : Continuous
          (fun t : ℝ => ∑ j : Fin n,
            (c i * g i t) * (c j * g j t)) := by
        fun_prop
      exact hci.intervalIntegrable a b
    _ = ∫ t in a..b,
          (neutralNF671SourceCombination g c t)^2 := by
      apply intervalIntegral.integral_congr
      intro t _
      unfold neutralNF671SourceCombination
      calc
        (∑ i : Fin n, ∑ j : Fin n,
          (c i * g i t) * (c j * g j t)) =
          ∑ i : Fin n,
            (c i * g i t) *
              (∑ j : Fin n, c j * g j t) := by
          apply Finset.sum_congr rfl
          intro i _
          rw [Finset.mul_sum]
        _ = (∑ i : Fin n, c i * g i t) *
              (∑ j : Fin n, c j * g j t) := by
          rw [Finset.sum_mul]
        _ = (∑ i : Fin n, c i * g i t)^2 := by
          ring

/-- Every finite continuous real Gram on a correctly oriented
physical interval is positive semidefinite, including degenerate
families. This is stronger in scope than the 15-source interval-box
certificate, but weaker in conclusion than strict coercivity. -/
theorem neutralNF671IntegralGram_nonnegative {n : ℕ}
    (g : Fin n → ℝ → ℝ) (hg : ∀ i, Continuous (g i))
    (a b : ℝ) (hab : a ≤ b) (c : Fin n → ℝ) :
    0 ≤ neutralNF661Quadratic (neutralNF671IntegralGram g a b) c := by
  rw [neutralNF671IntegralGram_energy_eq_square g hg a b c]
  exact intervalIntegral.integral_nonneg_of_forall hab
    (fun t => sq_nonneg (neutralNF671SourceCombination g c t))

#print axioms neutralNF671Pair_intervalIntegrable
#print axioms neutralNF671IntegralGram_energy_eq_square
#print axioms neutralNF671IntegralGram_nonnegative

end
end WeilDefect
