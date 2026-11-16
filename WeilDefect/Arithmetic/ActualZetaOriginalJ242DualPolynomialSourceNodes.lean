import WeilDefect.Arithmetic.ActualZetaOriginalJ242ExponentialSignature
import WeilDefect.Arithmetic.ActualZetaOriginalJ242HermiteDegreeObstruction
import Mathlib.Algebra.Polynomial.Degree.Operations
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF557 — exact ORIGINAL 242-dimensional dual polynomial and source-specific
67 positive distinct normalized squared-frequency nodes.

Earlier NF553-556 established the generic polynomial degree obstruction,
Hermite jet multiplicity, quadratic substitution factorization, and the
candidate exact quadratic root-multiplicity equality. This file begins
the *source-specific* assembly without assuming global original J242
independence or importing still-unaccepted NF548-551 modules.

The actual source frequencies are ω_f=2πf, where f is the unchanged
NF407 rational frequency and π>0. The normalized squared-frequency
nodes f² are checked exactly by the original Lean source list; multiplying
them by positive (2π)² yields the true positive squared nodes.

The genuine sinh pole is the additional negative t-node -1/4. It is
NOT replaced with a rational oscillator.
-/

/-- The precise dual polynomial associated with a real left-kernel
vector of the ORIGINAL 242 odd-initial-jet matrix:
p_a(T)=Σ_(0≤n<242) (-1)^n a_n T^n.
The authentic odd jet orders are 1,3,...,483. -/
def neutralNF557OriginalDualPolynomial (a : Fin 242 → ℝ) : Polynomial ℝ :=
  ∑ i : Fin 242, Polynomial.monomial i.val ((-1 : ℝ) ^ i.val * a i)

/-- The original finite dual polynomial has degree strictly below
242, independently of coefficient cancellation. This is the degree
hypothesis needed by NF553's accepted no-degree-242-divisor gate. -/
theorem neutralNF557OriginalDualPolynomial_natDegree_lt
    (a : Fin 242 → ℝ) :
    (neutralNF557OriginalDualPolynomial a).natDegree < 242 := by
  unfold neutralNF557OriginalDualPolynomial
  have hbound :
      (∑ i : Fin 242,
        Polynomial.monomial i.val ((-1 : ℝ) ^ i.val * a i)).natDegree ≤ 241 := by
    apply Polynomial.natDegree_sum_le_of_forall_le
    intro i hi
    have hi' : i.val ≤ 241 := by omega
    exact (Polynomial.natDegree_monomial_le _).trans hi'
  omega

/-- Normalize the exactly pinned original 67 positive rational
frequency blocks by squaring each f, without expanding or modifying
the original multiplicity/order list. -/
def neutralNF557OriginalRationalSquareNodes : List ℚ :=
  nf545OriginalSelectedFrequencyGroups.map fun group => group.1 ^ 2

/-- The ORIGINAL NF407 oscillator source supplies exactly 67
normalized squared-frequency nodes. -/
theorem neutralNF557OriginalRationalSquareNodes_length :
    neutralNF557OriginalRationalSquareNodes.length = 67 := by
  simpa [neutralNF557OriginalRationalSquareNodes] using
    nf545OriginalFrequencyGroupCount

/-- Exact SOURCE-CHECKED normalized squared oscillator nodes remain
pairwise distinct; no numerical π or sampled Gram is involved. -/
theorem neutralNF557OriginalRationalSquareNodes_nodup :
    neutralNF557OriginalRationalSquareNodes.Nodup := by
  decide +kernel

/-- Every exact original normalized squared oscillator node is
strictly positive. In the physical real transform the factor
(2π)² is also positive. -/
theorem neutralNF557OriginalRationalSquareNodes_positive :
    neutralNF557OriginalRationalSquareNodes.Forall
      (fun q => (0 : ℚ) < q) := by
  decide +kernel

/-- The separate original pole node -1/4 cannot be among the
normalized strictly positive rational oscillator squares.
The actual squared oscillator nodes are additionally scaled
by the strictly positive real factor (2π)². -/
theorem neutralNF557OriginalPoleNotNormalizedOscillator :
    (-(1 / 4 : ℚ)) ∉ neutralNF557OriginalRationalSquareNodes := by
  decide +kernel

/-- The actual real squared oscillator nodes of the unchanged source:
t_f=(2π)² f²=4π²f². This is an exact real list, not a
numerical frequency approximation. -/
def neutralNF557OriginalRealSquaredNodes : List ℝ :=
  neutralNF557OriginalRationalSquareNodes.map
    (fun q : ℚ => (2 * Real.pi) ^ 2 * (q : ℝ))

/-- Actual original real squared-frequency nodes are pairwise
distinct: exact rational nodup survives injective scaling by the
strictly positive (2π)². -/
theorem neutralNF557OriginalRealSquaredNodes_nodup :
    neutralNF557OriginalRealSquaredNodes.Nodup := by
  have hc : (2 * Real.pi) ^ 2 ≠ (0 : ℝ) := by positivity
  have hinj :
      Function.Injective (fun q : ℚ => (2 * Real.pi) ^ 2 * (q : ℝ)) := by
    intro a b hab
    have hab' : (a : ℝ) = (b : ℝ) := mul_left_cancel₀ hc hab
    exact_mod_cast hab'
  exact neutralNF557OriginalRationalSquareNodes_nodup.map hinj

/-- The exact unchanged source multiplicities supply all 241
oscillator Hermite conditions, plus one true sinh-pole condition:
the dual polynomial root budget is exactly 242. -/
theorem neutralNF557OriginalHermiteMultiplicityBudget :
    (nf545OriginalSelectedFrequencyGroups.map Prod.snd).sum + 1 = 242 := by
  rw [nf545OriginalOscillatorDimension]
  norm_num

end
end WeilDefect
