import WeilDefect.Arithmetic.ActualZetaOriginalNF407FrozenData
import WeilDefect.Arithmetic.ActualZetaOriginalJ242GlobalCombinationJets
import Mathlib.Analysis.Calculus.ContDiff.Deriv

namespace WeilDefect
noncomputable section
open scoped ContDiff

/-! NF587: the literal source space is the historical NF407 physical
U, before any collar restriction. Retain 242 selected and 4 critical
coefficients, and the raw dyadic interval box, NOT solely the midpoint.
The identification of the true reconstructed coefficient vector with
this box is a separate certificate obligation. -/

set_option maxRecDepth 10000 in
theorem neutralNF587FrozenNodes_eq_original :
    neutralNF587FrozenNodes = nf545OriginalSelectedOscillatorNodes := by
  decide +kernel

theorem neutralNF587SelectedDyads_size :
    neutralNF587SelectedDyads.size = 242 := by
  rfl

theorem neutralNF587CriticalDyads_size :
    neutralNF587CriticalDyads.size = 4 := by
  rfl

theorem neutralNF587CriticalFrequencies_size :
    neutralNF587CriticalFrequencies.size = 32 := by
  rfl

def neutralNF587Dyadic (p : ℤ × ℤ) : ℝ :=
  (p.1 : ℝ) * (2 : ℝ) ^ p.2

def neutralNF587SelectedMid (j : Fin 242) : ℝ :=
  neutralNF587Dyadic neutralNF587SelectedDyads[j.val]!.1

def neutralNF587SelectedRadius (j : Fin 242) : ℝ :=
  |neutralNF587Dyadic neutralNF587SelectedDyads[j.val]!.2|

def neutralNF587CriticalMid (j : Fin 4) : ℝ :=
  neutralNF587Dyadic neutralNF587CriticalDyads[j.val]!.1

def neutralNF587CriticalRadius (j : Fin 4) : ℝ :=
  |neutralNF587Dyadic neutralNF587CriticalDyads[j.val]!.2|

/-- Four exact original critical shapes: 32 sine terms plus the
genuine sinh pole, with the authentic sign of each coefficient. -/
def neutralNF587CriticalGenerator (j : Fin 4) (x : ℝ) : ℝ :=
  (∑ k : Fin 32,
    ((neutralNF587CriticalSines[j.val]![k.val]! : ℚ) : ℝ) *
      Real.sin (2 * Real.pi * (neutralNF587CriticalFrequencies[k.val]! : ℝ) * x)) +
    (neutralNF587CriticalPoles[j.val]! : ℝ) * Real.sinh (x / 2)

/-- The actual ungrouped 246-source formula. Regrouping equal nodes
is merely algebra; the original 242 rows and four probes remain
the primitive inputs, preserving correlated coefficient choices. -/
def neutralNF587Source (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (x : ℝ) : ℝ :=
  neutralNF569OriginalRealCombination a x +
    ∑ j : Fin 4, b j * neutralNF587CriticalGenerator j x

def neutralNF587SourceInFrozenBox (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) : Prop :=
  (∀ j, |a j-neutralNF587SelectedMid j| ≤ neutralNF587SelectedRadius j) ∧
  (∀ j, |b j-neutralNF587CriticalMid j| ≤ neutralNF587CriticalRadius j)

theorem neutralNF587Midpoint_inFrozenBox :
    neutralNF587SourceInFrozenBox neutralNF587SelectedMid neutralNF587CriticalMid := by
  constructor
  · intro j
    rw [sub_self, abs_zero]
    exact abs_nonneg _
  · intro j
    rw [sub_self, abs_zero]
    exact abs_nonneg _

theorem neutralNF587CriticalGenerator_contDiff (j : Fin 4) :
    ContDiff ℝ 1 (neutralNF587CriticalGenerator j) := by
  unfold neutralNF587CriticalGenerator
  apply ContDiff.add
  · apply ContDiff.sum
    intro k hk
    fun_prop
  · fun_prop

/-- C¹ regularity is unconditional for EVERY possible coefficient
vector in the box (indeed, every real vector). No numerical arithmetic
or Taylor coefficient enclosure is needed for this fact. -/
theorem neutralNF587Source_contDiff (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    ContDiff ℝ 1 (neutralNF587Source a b) := by
  unfold neutralNF587Source neutralNF569OriginalRealCombination
  apply ContDiff.add
  · apply ContDiff.sum
    intro j hj
    apply ContDiff.mul contDiff_const
    rw [contDiff_iff_contDiffAt]
    exact fun x => neutralNF569OriginalRealGenerator_contDiffAt j 1 x
  · apply ContDiff.sum
    intro j hj
    exact contDiff_const.mul (neutralNF587CriticalGenerator_contDiff j)

theorem neutralNF587Source_measurable (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    Measurable (neutralNF587Source a b) :=
  (neutralNF587Source_contDiff a b).continuous.measurable

theorem neutralNF587Source_derivative_continuous (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    Continuous (deriv (neutralNF587Source a b)) :=
  (neutralNF587Source_contDiff a b).continuous_deriv_one

theorem neutralNF587Source_hasDerivAt (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (x : ℝ) :
    HasDerivAt (neutralNF587Source a b) (deriv (neutralNF587Source a b) x) x :=
  ((neutralNF587Source_contDiff a b).differentiable_one x).hasDerivAt

end
end WeilDefect
