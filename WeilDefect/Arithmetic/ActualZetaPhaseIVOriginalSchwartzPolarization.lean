import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalMixedHermitian
import WeilDefect.Arithmetic.ActualZetaPhaseIVFiniteLocalSpan
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV009 — actual ORIGINAL finite-complex-Schwartz-sum polarization.

This source directly bridges the authentic NF533/NF534 all-divisor
two-argument explicit formula to the physical diagonal arithmetic Weil
value of an arbitrary finite complex Schwartz superposition.

Conjugation is in the FIRST input; every divisor MULTIPLICITY COPY
is retained, including genuinely nonreal original zeta ordinates.
The finite/infinite summation interchange uses separately proved
absolute divisor summability of each supported smooth mixed pair.

This is a candidate original source proof, not an axiom, an abstract
Hermitian matrix model, or a presumption of positivity. Kernel and
source/axiom audit remain mandatory.

The final local corollary is restricted to the EXISTING frozen original
two-collar geometry, not new supports or global Weil positivity.
-/

/-- Exact physical complex-Schwartz superposition being tested. -/
def neutralIV009PhysicalSchwartzSum {n : ℕ}
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ) : 𝓢(ℝ, ℂ) :=
  ∑ i : Fin n, u i • s i

/-- Original fixed support is stable under a finite complex sum. -/
theorem neutralIV009PhysicalSchwartzSum_supported
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) :
    ∀ x : ℝ, x ∉ Set.Icc (-a) a →
      neutralIV009PhysicalSchwartzSum s u x = 0 := by
  intro x hx
  have hz (i : Fin n) : s i x = 0 := hs i x hx
  simp [neutralIV009PhysicalSchwartzSum, hz]

/-- The ACTUAL original complex-frequency window evaluation is
complex-linear on arbitrary finite Schwartz superpositions.
This is proved through its pre-existing exact physical L² inner-product
realization and the genuine complex-linear Schwartz→L² inclusion. -/
theorem neutralIV009WindowEvaluation_finiteLinear
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ) (z : ℂ) :
    neutralWindowEvaluation a z
        ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume) =
      ∑ i : Fin n, u i *
        neutralWindowEvaluation a z ((s i).toLp 2 volume) := by
  have hLp :
      (neutralIV009PhysicalSchwartzSum s u).toLp 2 volume =
        ∑ i : Fin n, u i • (s i).toLp 2 volume := by
    change
      (SchwartzMap.toLpCLM ℂ ℂ 2 volume)
          (∑ i : Fin n, u i • s i) =
        ∑ i : Fin n, u i •
          (SchwartzMap.toLpCLM ℂ ℂ 2 volume) (s i)
    simp only [map_sum, map_smul]
  calc
    neutralWindowEvaluation a z
        ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume) =
      inner ℂ (neutralExponentialColumnL2 a (conj z))
        ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume) :=
          neutralWindowEvaluation_eq_inner a z _
    _ = inner ℂ (neutralExponentialColumnL2 a (conj z))
        (∑ i : Fin n, u i • (s i).toLp 2 volume) := by
          rw [hLp]
    _ = ∑ i : Fin n, u i *
        neutralWindowEvaluation a z ((s i).toLp 2 volume) := by
          simp only [inner_sum, inner_smul_right,
            ← neutralWindowEvaluation_eq_inner]

/-- Single original full-multiplicity mixed divisor summand. -/
def neutralIV009OriginalPairTerm
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (q : NeutralActualZetaDivisorCoordinate) : ℂ :=
  conj (neutralWindowEvaluation a
      (conj (neutralActualZetaDivisorOrdinate q))
      (f.toLp 2 volume)) *
    neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
      (g.toLp 2 volume)

/-- Absolute convergence for the actual mixed all-copy zeta divisor
summand comes from the source NF533 explicit-formula regularity theorem
and the genuine smooth supported window representative, not a hypothesis
asserted at the terminal infinite-sum interchange. -/
theorem neutralIV009OriginalPairTerm_summable
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0) :
    Summable (neutralIV009OriginalPairTerm a f g) := by
  have hreg :
      ContDiff ℝ 2
        (neutralWindowCorrelation a (f.toLp 2 volume) (g.toLp 2 volume)) :=
    neutralWindowCorrelation_contDiff_of_ae_smoothSecond a
      (f.toLp 2 volume) (g.toLp 2 volume)
      (fun x : ℝ => g x) (g.smooth 2)
      (neutralIV008SchwartzWindow_hasCompactSupport a g hg)
      (neutralIV006Schwartz_window_ae a g hg)
  have hsource := neutralActualZetaDivisor_rawTransform_summable_of_contDiff
    (neutralWindowCorrelation a (f.toLp 2 volume) (g.toLp 2 volume))
    hreg (neutralWindowCorrelation_hasCompactSupport a _ _)
  simpa only [neutralIV009OriginalPairTerm,
    neutralWindowCorrelation_rawTransform] using hsource

/-- The ORIGINAL first-antilinear/second-linear Weil summand, multiplied
by the two finite-family coefficients. -/
def neutralIV009WeightedPairTerm {n : ℕ}
    (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (i j : Fin n) (q : NeutralActualZetaDivisorCoordinate) : ℂ :=
  conj (u i) * neutralIV009OriginalPairTerm a (s i) (s j) q * u j

/-- Exact complex-valued pointwise finite Gram expansion, with
the correct conjugation of FIRST-SLOT complex coefficients. -/
theorem neutralIV009OriginalDivisorTerm_finiteExpansion
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ) (q : NeutralActualZetaDivisorCoordinate) :
    neutralIV009OriginalPairTerm a
        (neutralIV009PhysicalSchwartzSum s u)
        (neutralIV009PhysicalSchwartzSum s u) q =
      ∑ i : Fin n, ∑ j : Fin n,
        neutralIV009WeightedPairTerm a s u i j q := by
  let z := neutralActualZetaDivisorOrdinate q
  let A (i : Fin n) :=
    neutralWindowEvaluation a (conj z) ((s i).toLp 2 volume)
  let B (j : Fin n) :=
    neutralWindowEvaluation a z ((s j).toLp 2 volume)
  change
    conj (neutralWindowEvaluation a (conj z)
      ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)) *
      neutralWindowEvaluation a z
        ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume) =
    ∑ i : Fin n, ∑ j : Fin n,
      conj (u i) * (conj (A i) * B j) * u j
  rw [neutralIV009WindowEvaluation_finiteLinear a s u (conj z),
    neutralIV009WindowEvaluation_finiteLinear a s u z]
  simp only [map_sum, map_mul]
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro i _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  dsimp [A, B]
  ring

/-- The terminal EXACT all-multiplicity original mixed divisor
quadratic sum equals the authentic original divisor-series diagonal
of the physical Schwartz superposition.

Every infinite-sum commute is justified by original source-specific
summability for each smooth supported pair, not merely formality. -/
theorem neutralIV009FiniteMixedEnergy_eq_originalDivisorDiagonal
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) :
    neutralIV007OriginalMixedEnergy a s u =
      ∑' q : NeutralActualZetaDivisorCoordinate,
        neutralIV009OriginalPairTerm a
          (neutralIV009PhysicalSchwartzSum s u)
          (neutralIV009PhysicalSchwartzSum s u) q := by
  classical
  have hterm (i j : Fin n) :
      Summable (neutralIV009WeightedPairTerm a s u i j) := by
    exact
      ((neutralIV009OriginalPairTerm_summable a (s i) (s j) (hs j)).mul_left
        (conj (u i))).mul_right (u j)
  have hrow (i : Fin n) :
      Summable (fun q : NeutralActualZetaDivisorCoordinate =>
        ∑ j : Fin n, neutralIV009WeightedPairTerm a s u i j q) := by
    apply summable_sum (s := (Finset.univ : Finset (Fin n)))
      (f := fun j q => neutralIV009WeightedPairTerm a s u i j q)
    intro j _
    exact hterm i j
  have hcoef (i j : Fin n) :
      (∑' q : NeutralActualZetaDivisorCoordinate,
         neutralIV009WeightedPairTerm a s u i j q) =
      conj (u i) * neutralIV007OriginalDivisorEntry a s i j * u j := by
    unfold neutralIV009WeightedPairTerm
      neutralIV007OriginalDivisorEntry neutralIV009OriginalPairTerm
    rw [tsum_mul_right, tsum_mul_left]
  have hcomm :
      (∑ i : Fin n, ∑ j : Fin n,
        ∑' q : NeutralActualZetaDivisorCoordinate,
          neutralIV009WeightedPairTerm a s u i j q) =
      (∑' q : NeutralActualZetaDivisorCoordinate,
        ∑ i : Fin n, ∑ j : Fin n,
          neutralIV009WeightedPairTerm a s u i j q) := by
    calc
      _ = ∑ i : Fin n, ∑' q : NeutralActualZetaDivisorCoordinate,
        ∑ j : Fin n, neutralIV009WeightedPairTerm a s u i j q := by
          apply Finset.sum_congr rfl
          intro i _
          exact (Summable.tsum_finsetSum
            (s := (Finset.univ : Finset (Fin n)))
            (f := fun j q => neutralIV009WeightedPairTerm a s u i j q)
            (by intro j _; exact hterm i j)).symm
      _ = ∑' q : NeutralActualZetaDivisorCoordinate,
        ∑ i : Fin n, ∑ j : Fin n,
          neutralIV009WeightedPairTerm a s u i j q := by
            exact (Summable.tsum_finsetSum
              (s := (Finset.univ : Finset (Fin n)))
              (f := fun i q =>
                ∑ j : Fin n, neutralIV009WeightedPairTerm a s u i j q)
              (by intro i _; exact hrow i)).symm
  calc
    neutralIV007OriginalMixedEnergy a s u =
        ∑ i : Fin n, ∑ j : Fin n,
          ∑' q : NeutralActualZetaDivisorCoordinate,
            neutralIV009WeightedPairTerm a s u i j q := by
              unfold neutralIV007OriginalMixedEnergy
              apply Finset.sum_congr rfl
              intro i _
              apply Finset.sum_congr rfl
              intro j _
              calc
                conj (u i) * neutralIV007OriginalMixedEntry a s i j * u j =
                    conj (u i) * neutralIV007OriginalDivisorEntry a s i j * u j := by
                      rw [← neutralIV008OriginalMixedEntry_eq_divisor a s hs i j]
                _ = ∑' q : NeutralActualZetaDivisorCoordinate,
                    neutralIV009WeightedPairTerm a s u i j q := (hcoef i j).symm
    _ = ∑' q : NeutralActualZetaDivisorCoordinate,
        ∑ i : Fin n, ∑ j : Fin n,
          neutralIV009WeightedPairTerm a s u i j q := hcomm
    _ = ∑' q : NeutralActualZetaDivisorCoordinate,
        neutralIV009OriginalPairTerm a
          (neutralIV009PhysicalSchwartzSum s u)
          (neutralIV009PhysicalSchwartzSum s u) q := by
            apply tsum_congr
            intro q
            exact (neutralIV009OriginalDivisorTerm_finiteExpansion a s u q).symm

/-- EXACT original physical Schwartz-sum polarization:
the complete ORIGINAL two-argument zeta explicit formula of the
physical diagonal sum equals the FULL finite mixed arithmetic energy.
No sesquilinearity of literatureRHS is postulated; the proof routes
through the authentic absolutely convergent all-multiplicity divisor. -/
theorem neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0) :
    neutralIV007OriginalMixedEnergy a s u =
      Zeta23.EF.literatureRHS
        (neutralWindowCorrelation a
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)) := by
  let S := neutralIV009PhysicalSchwartzSum s u
  have hS : ∀ x : ℝ, x ∉ Set.Icc (-a) a → S x = 0 :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs
  have hEF :
      (∑' q : NeutralActualZetaDivisorCoordinate,
        neutralIV009OriginalPairTerm a S S q) =
      Zeta23.EF.literatureRHS
        (neutralWindowCorrelation a (S.toLp 2 volume) (S.toLp 2 volume)) := by
    exact neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond
      a (S.toLp 2 volume) (S.toLp 2 volume) (fun x : ℝ => S x)
      (S.smooth 2)
      (neutralIV008SchwartzWindow_hasCompactSupport a S hS)
      (neutralIV006Schwartz_window_ae a S hS)
  exact (neutralIV009FiniteMixedEnergy_eq_originalDivisorDiagonal a s u hs).trans hEF

/-- Authentic original two-collar support implies pointwise support
in the already certified physical window, without changing support. -/
theorem neutralIV009OriginalCollars_supported_window
    (s : 𝓢(ℝ, ℂ))
    (hs : neutralNF735InOriginalCollars s) :
    ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0 := by
  intro x hx
  apply hs x
  intro he
  rcases he with hleft | hright
  · exact hx ⟨hleft.1.le, by linarith [hleft.2]⟩
  · exact hx ⟨by linarith [hright.1], hright.2.le⟩

/-- Real original finite-family Gram COERCIVITY inside the SAME frozen
physical two collars, by literal Schwartz-sum polarization plus NF600/
NF738 existing source coercivity. This is NOT a new-support or global
positivity assertion; source-specific upstream Lean checks remain pending. -/
theorem neutralIV009OriginalCollars_mixedEnergy_lower
    {n : ℕ} (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i)) :
    (2/5:ℝ) *
        ‖(neutralIV009PhysicalSchwartzSum s u).toLp 2 volume‖ ^ 2 ≤
      (neutralIV007OriginalMixedEnergy (11/10:ℝ) s u).re := by
  have hwindow :
      ∀ i : Fin n, ∀ x : ℝ,
        x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s i x = 0 := by
    intro i
    exact neutralIV009OriginalCollars_supported_window (s i) (hs i)
  have hbridge := congrArg Complex.re
    (neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
      (11/10:ℝ) s u hwindow)
  have hlocal :
      (2/5:ℝ) *
          ‖(neutralIV009PhysicalSchwartzSum s u).toLp 2 volume‖ ^ 2 ≤
        neutralNF598SmoothWeil (neutralIV009PhysicalSchwartzSum s u) := by
    simpa only [neutralIV009PhysicalSchwartzSum] using
      (neutralNF738OriginalFiniteCollarSpan_coercive
        (Finset.univ : Finset (Fin n)) s u
        (by intro i _; exact hs i))
  calc
    (2/5:ℝ) *
        ‖(neutralIV009PhysicalSchwartzSum s u).toLp 2 volume‖ ^ 2 ≤
      neutralNF598SmoothWeil (neutralIV009PhysicalSchwartzSum s u) := hlocal
    _ = (neutralIV007OriginalMixedEnergy (11/10:ℝ) s u).re := by
      change
        (Zeta23.EF.literatureRHS
          (neutralWindowCorrelation (11/10:ℝ)
            ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)
            ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume))).re =
          (neutralIV007OriginalMixedEnergy (11/10:ℝ) s u).re
      exact hbridge.symm

#print axioms neutralWindowEvaluation_eq_inner
#print axioms neutralActualZetaDivisor_rawTransform_summable_of_contDiff
#print axioms neutralIV008OriginalMixedEntry_eq_divisor
#print axioms neutralNF738OriginalFiniteCollarSpan_coercive
#print axioms neutralIV009PhysicalSchwartzSum_supported
#print axioms neutralIV009WindowEvaluation_finiteLinear
#print axioms neutralIV009OriginalPairTerm_summable
#print axioms neutralIV009OriginalDivisorTerm_finiteExpansion
#print axioms neutralIV009FiniteMixedEnergy_eq_originalDivisorDiagonal
#print axioms neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
#print axioms neutralIV009OriginalCollars_supported_window
#print axioms neutralIV009OriginalCollars_mixedEnergy_lower

end
end WeilDefect
