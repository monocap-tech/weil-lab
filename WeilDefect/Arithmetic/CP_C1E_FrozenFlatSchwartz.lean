import WeilDefect.Arithmetic.CP_C1D_OriginalNineProbeCompatibility
import Mathlib.Analysis.SpecialFunctions.SmoothTransition
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP-C1(E) — exact original CP001 flat bump, not a generic bump surrogate.

Mathematically the exact CP001 profile is
 φ(u) = exp(1-1/(1-u²)) for |u|<1 and 0 otherwise.

The SAME profile equals exp(1)*expNegInvGlue(1-u²). Mathlib proves
expNegInvGlue.contDiff, allowing the original fixed function to be
packaged directly as a complex Schwartz test after support verification.

The radius of each old bump is exactly 1/2000, not 1/1000.
These are source proof CANDIDATES, not new Lean kernel acceptance.
-/

def neutralCPC1EFlatProfile (u : ℝ) : ℝ :=
  Real.exp 1 * expNegInvGlue (1 - u ^ 2)

/-- Literal original piecewise profile, pointwise for every real u. -/
theorem neutralCPC1EFlatProfile_eq_frozen (u : ℝ) :
    neutralCPC1EFlatProfile u =
      if |u| < 1 then Real.exp (1 - 1 / (1 - u ^ 2)) else 0 := by
  by_cases hu : |u| < 1
  · have hlt := abs_lt.mp hu
    have hpos : 0 < 1 - u ^ 2 := by
      have hp : 0 < (1 - u) * (1 + u) :=
        mul_pos (by linarith [hlt.2]) (by linarith [hlt.1])
      nlinarith [hp]
    have hn : ¬ (1 - u ^ 2 ≤ 0) := not_le.mpr hpos
    rw [if_pos hu]
    simp only [neutralCPC1EFlatProfile, expNegInvGlue, if_neg hn]
    rw [← Real.exp_add]
    congr 1
    ring
  · have habs : 1 ≤ |u| := le_of_not_gt hu
    have hsq : 1 ≤ u ^ 2 := by
      rcases le_total 0 u with hpos | hneg
      · rw [abs_of_nonneg hpos] at habs
        nlinarith
      · rw [abs_of_nonpos hneg] at habs
        nlinarith
    have hnonpos : 1 - u ^ 2 ≤ 0 := by linarith
    rw [if_neg hu]
    simp [neutralCPC1EFlatProfile,
      expNegInvGlue.zero_of_nonpos hnonpos]

theorem neutralCPC1EFlatProfile_contDiff :
    ContDiff ℝ (⊤ : ℕ∞) neutralCPC1EFlatProfile := by
  change ContDiff ℝ (⊤ : ℕ∞)
    (fun u : ℝ => Real.exp 1 * expNegInvGlue (1 - u ^ 2))
  exact contDiff_const.mul
    (expNegInvGlue.contDiff.comp
      (contDiff_const.sub (contDiff_id.pow 2)))

theorem neutralCPC1EFlatProfile_zero :
    neutralCPC1EFlatProfile 0 = 1 := by
  rw [neutralCPC1EFlatProfile_eq_frozen]
  norm_num

theorem neutralCPC1EFlatProfile_zero_outside
    (u : ℝ) (hu : 1 ≤ |u|) :
    neutralCPC1EFlatProfile u = 0 := by
  rw [neutralCPC1EFlatProfile_eq_frozen]
  simp [not_lt.mpr hu]

def neutralCPC1EFlatReal (c r : ℝ) (x : ℝ) : ℝ :=
  neutralCPC1EFlatProfile ((x - c) / r)

theorem neutralCPC1EFlatReal_center (c r : ℝ) :
    neutralCPC1EFlatReal c r c = 1 := by
  simpa [neutralCPC1EFlatReal] using neutralCPC1EFlatProfile_zero

theorem neutralCPC1EFlatReal_zero_outside
    (c r : ℝ) (hr : 0 < r) (x : ℝ)
    (hx : x ∉ Set.Icc (c - r) (c + r)) :
    neutralCPC1EFlatReal c r x = 0 := by
  apply neutralCPC1EFlatProfile_zero_outside
  change 1 ≤ |(x - c) / r|
  rw [abs_div, abs_of_pos hr]
  apply (le_div_iff₀ hr).2
  by_contra h
  have hs : |x - c| < r := lt_of_not_ge h
  have hlohi := abs_lt.mp hs
  exact hx ⟨by linarith [hlohi.1], by linarith [hlohi.2]⟩

theorem neutralCPC1EFlatReal_contDiff (c r : ℝ) :
    ContDiff ℝ (⊤ : ℕ∞) (neutralCPC1EFlatReal c r) := by
  have hAffine : ContDiff ℝ (⊤ : ℕ∞)
      (fun x : ℝ => (x - c) * r⁻¹) :=
    (contDiff_id.sub contDiff_const).mul contDiff_const
  change ContDiff ℝ (⊤ : ℕ∞)
    (fun x : ℝ => neutralCPC1EFlatProfile ((x - c) / r))
  simpa only [div_eq_mul_inv] using
    neutralCPC1EFlatProfile_contDiff.comp hAffine

def neutralCPC1EFlatComplex (c r : ℝ) (x : ℝ) : ℂ :=
  (neutralCPC1EFlatReal c r x : ℂ)

theorem neutralCPC1EFlatComplex_contDiff (c r : ℝ) :
    ContDiff ℝ (⊤ : ℕ∞) (neutralCPC1EFlatComplex c r) := by
  exact Complex.ofRealCLM.contDiff.comp
    (neutralCPC1EFlatReal_contDiff c r)

theorem neutralCPC1EFlatComplex_hasCompactSupport
    (c r : ℝ) (hr : 0 < r) :
    HasCompactSupport (neutralCPC1EFlatComplex c r) := by
  apply HasCompactSupport.intro (K := Set.Icc (c-r) (c+r)) isCompact_Icc
  intro x hx
  change (neutralCPC1EFlatReal c r x : ℂ) = 0
  exact_mod_cast neutralCPC1EFlatReal_zero_outside c r hr x hx

def neutralCPC1EFlatSchwartz (c r : ℝ) (hr : 0 < r) :
    𝓢(ℝ, ℂ) :=
  (neutralCPC1EFlatComplex_hasCompactSupport c r hr).toSchwartzMap
    (neutralCPC1EFlatComplex_contDiff c r)

theorem neutralCPC1EFlatSchwartz_apply
    (c r : ℝ) (hr : 0 < r) (x : ℝ) :
    neutralCPC1EFlatSchwartz c r hr x =
      neutralCPC1EFlatComplex c r x := by
  rfl

theorem neutralCPC1EFlatSchwartz_center
    (c r : ℝ) (hr : 0 < r) :
    neutralCPC1EFlatSchwartz c r hr c = 1 := by
  rw [neutralCPC1EFlatSchwartz_apply]
  change (neutralCPC1EFlatReal c r c : ℂ) = 1
  rw [neutralCPC1EFlatReal_center]
  norm_num

theorem neutralCPC1EFlatSchwartz_zero_outside
    (c r : ℝ) (hr : 0 < r) (x : ℝ)
    (hx : x ∉ Set.Icc (c - r) (c + r)) :
    neutralCPC1EFlatSchwartz c r hr x = 0 := by
  rw [neutralCPC1EFlatSchwartz_apply]
  change (neutralCPC1EFlatReal c r x : ℂ) = 0
  rw [neutralCPC1EFlatReal_zero_outside c r hr x hx]
  norm_num

/-- The EXACT CP001 family, with old half-width 1/2000. -/
def neutralCPC1EFrozenFamily
    (r : ℝ) (hr : 0 < r) : Fin 3 → 𝓢(ℝ, ℂ) :=
  ![neutralCPC1EFlatSchwartz (-1099 / 1000) (1 / 2000) (by norm_num),
    neutralCPC1EFlatSchwartz (1099 / 1000) (1 / 2000) (by norm_num),
    neutralCPC1EFlatSchwartz (1 / 5) r hr]

theorem neutralCPC1EFrozenFamily_supportedOriginal
    (r : ℝ) (hr : 0 < r) (hrmax : r ≤ 1 / 500) :
    ∀ i : Fin 3, ∀ x : ℝ,
      x ∉ Set.Icc (-11/10) (11/10) →
        neutralCPC1EFrozenFamily r hr i x = 0 := by
  intro i x hx
  fin_cases i
  · have hsmall : x ∉ Set.Icc (-1099/1000 - 1/2000)
        (-1099/1000 + 1/2000) := by
      intro h
      exact hx ⟨by linarith [h.1], by linarith [h.2]⟩
    simpa [neutralCPC1EFrozenFamily] using
      (neutralCPC1EFlatSchwartz_zero_outside
        (-1099/1000) (1/2000) (by norm_num) x hsmall)
  · have hsmall : x ∉ Set.Icc (1099/1000 - 1/2000)
        (1099/1000 + 1/2000) := by
      intro h
      exact hx ⟨by linarith [h.1], by linarith [h.2]⟩
    simpa [neutralCPC1EFrozenFamily] using
      (neutralCPC1EFlatSchwartz_zero_outside
        (1099/1000) (1/2000) (by norm_num) x hsmall)
  · have hsmall : x ∉ Set.Icc (1/5 - r) (1/5 + r) := by
      intro h
      exact hx ⟨by linarith [h.1,hrmax], by linarith [h.2,hrmax]⟩
    simpa [neutralCPC1EFrozenFamily] using
      (neutralCPC1EFlatSchwartz_zero_outside (1/5) r hr x hsmall)

/-- Genuine frozen physical source vs complete, untruncated divisor. -/
theorem neutralCPC1EFrozenOriginal_matrix_eq_completeDivisor
    (r : ℝ) (hr : 0 < r) (hrmax : r ≤ 1 / 500) :
    (fun i j : Fin 3 => neutralIV007OriginalMixedEntry (11/10)
       (neutralCPC1EFrozenFamily r hr) i j) =
    (fun i j : Fin 3 => neutralIV007OriginalDivisorEntry (11/10)
       (neutralCPC1EFrozenFamily r hr) i j) := by
  exact neutralCPC1C_originalFiniteThree_matrix_eq_divisor
    (11/10) (neutralCPC1EFrozenFamily r hr)
    (neutralCPC1EFrozenFamily_supportedOriginal r hr hrmax)

#print axioms neutralCPC1C_originalFiniteThree_matrix_eq_divisor
#print axioms neutralCPC1D_original_eq_target_of_nine_phase_readings
#print axioms neutralCPC1EFlatProfile_eq_frozen
#print axioms neutralCPC1EFlatProfile_contDiff
#print axioms neutralCPC1EFlatProfile_zero
#print axioms neutralCPC1EFlatProfile_zero_outside
#print axioms neutralCPC1EFlatReal_center
#print axioms neutralCPC1EFlatReal_zero_outside
#print axioms neutralCPC1EFlatReal_contDiff
#print axioms neutralCPC1EFlatComplex_contDiff
#print axioms neutralCPC1EFlatComplex_hasCompactSupport
#print axioms neutralCPC1EFlatSchwartz_apply
#print axioms neutralCPC1EFlatSchwartz_center
#print axioms neutralCPC1EFlatSchwartz_zero_outside
#print axioms neutralCPC1EFrozenFamily_supportedOriginal
#print axioms neutralCPC1EFrozenOriginal_matrix_eq_completeDivisor

end
end WeilDefect
