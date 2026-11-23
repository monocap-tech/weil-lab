import WeilDefect.Arithmetic.CP_C1FG_FrozenTargetAndRadiusGlue
import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeBound
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP-C1(H1): genuine NF600 original-collar orientation at +log9 and -log9.
Two pointwise theorems only. Original CP001 Schwartz specialization and
integral transport are separate H2 obligations. This source does not
establish a sign for the full pole-prime-Gamma Weil form or RH.
-/

private def cpHLeftCollar : Set ℝ := Ioo (-(11/10:ℝ)) (-(11/10:ℝ)+1/500)
private def cpHRightCollar : Set ℝ := Ioo ((11/10:ℝ)-1/500) (11/10:ℝ)

private theorem cpHcollars_disjoint (x : ℝ)
    (hxL : x ∈ cpHLeftCollar) (hxR : x ∈ cpHRightCollar) : False := by
  dsimp [cpHLeftCollar, cpHRightCollar] at hxL hxR
  linarith [hxL.2, hxR.1]

private theorem cpHleft_old (x : ℝ) (hx : x ∈ cpHLeftCollar) :
    x ∈ neutralNF543OriginalCollars := Or.inl hx

private theorem cpHright_old (x : ℝ) (hx : x ∈ cpHRightCollar) :
    x ∈ neutralNF543OriginalCollars := Or.inr hx

/-- At positive log9 shift only R(x) and L(x-log9) can contribute.
This uses the original NF600 geometric orientation, not a toy matrix. -/
theorem neutralCPC1H_positiveShift_pointwise
    (L R : ℝ → ℂ)
    (hL : ∀ x : ℝ, x ∉ cpHLeftCollar → L x = 0)
    (hR : ∀ x : ℝ, x ∉ cpHRightCollar → R x = 0)
    (v : ℂ) (x : ℝ) :
    (L x + v * R x) * conj (L (x - Real.log 9) + v * R (x - Real.log 9)) =
      v * (R x * conj (L (x - Real.log 9))) := by
  by_cases hx : x ∈ neutralNF543OriginalCollars
  · by_cases hy : x - Real.log 9 ∈ neutralNF543OriginalCollars
    · have horient := neutralNF600Log9_cross
        (x - Real.log 9) x hy hx (by ring)
      have hLx : L x = 0 := hL x (by
        intro hl
        exact cpHcollars_disjoint x hl horient.2)
      have hRy : R (x - Real.log 9) = 0 := hR _ (by
        intro hr
        exact cpHcollars_disjoint (x - Real.log 9) horient.1 hr)
      simp [hLx, hRy, mul_assoc]
    · have hLy : L (x - Real.log 9) = 0 := hL _ (by
        intro h
        exact hy (cpHleft_old _ h))
      have hRy : R (x - Real.log 9) = 0 := hR _ (by
        intro h
        exact hy (cpHright_old _ h))
      simp [hLy, hRy]
  · have hLx : L x = 0 := hL x (by
      intro h
      exact hx (cpHleft_old _ h))
    have hRx : R x = 0 := hR x (by
      intro h
      exact hx (cpHright_old _ h))
    simp [hLx, hRx]

/-- At negative log9 shift the phase is conjugated, not copied. -/
theorem neutralCPC1H_negativeShift_pointwise
    (L R : ℝ → ℂ)
    (hL : ∀ x : ℝ, x ∉ cpHLeftCollar → L x = 0)
    (hR : ∀ x : ℝ, x ∉ cpHRightCollar → R x = 0)
    (v : ℂ) (x : ℝ) :
    (L x + v * R x) * conj (L (x + Real.log 9) + v * R (x + Real.log 9)) =
      conj v * (L x * conj (R (x + Real.log 9))) := by
  by_cases hx : x ∈ neutralNF543OriginalCollars
  · by_cases hy : x + Real.log 9 ∈ neutralNF543OriginalCollars
    · have horient := neutralNF600Log9_cross
        x (x + Real.log 9) hx hy (by ring)
      have hRx : R x = 0 := hR x (by
        intro hr
        exact cpHcollars_disjoint x horient.1 hr)
      have hLy : L (x + Real.log 9) = 0 := hL _ (by
        intro hl
        exact cpHcollars_disjoint (x + Real.log 9) hl horient.2)
      simp [hRx, hLy, map_mul, mul_assoc, mul_left_comm, mul_comm]
    · have hLy : L (x + Real.log 9) = 0 := hL _ (by
        intro h
        exact hy (cpHleft_old _ h))
      have hRy : R (x + Real.log 9) = 0 := hR _ (by
        intro h
        exact hy (cpHright_old _ h))
      simp [hLy, hRy]
  · have hLx : L x = 0 := hL x (by
      intro h
      exact hx (cpHleft_old _ h))
    have hRx : R x = 0 := hR x (by
      intro h
      exact hx (cpHright_old _ h))
    simp [hLx, hRx]

#print axioms neutralNF600Log9_cross
#print axioms neutralCPC1H_positiveShift_pointwise
#print axioms neutralCPC1H_negativeShift_pointwise

end
end WeilDefect
