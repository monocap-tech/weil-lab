import WeilDefect.Arithmetic.ActualZetaIV108OriginalDirectionalResponseBudget
import WeilDefect.Arithmetic.ActualZetaIV109OriginalPhysicalCrossRow
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped ComplexConjugate SchwartzMap FourierTransform

def neutralIV123EvenMoment (a : ℝ) (f : RealComplexL2) : ℂ :=
  (sourceWindowMoment a (1/2) f + sourceWindowMoment a (-(1/2)) f) / 2

def neutralIV123OddMoment (a : ℝ) (f : RealComplexL2) : ℂ :=
  (sourceWindowMoment a (1/2) f - sourceWindowMoment a (-(1/2)) f) / 2

theorem neutralIV123Pole_algebra (p m q n : ℂ) :
    conj m * q + conj p * n =
      2 * conj ((p+m)/2) * ((q+n)/2) -
      2 * conj ((p-m)/2) * ((q-n)/2) := by
  simp only [map_div₀, map_add, map_sub, map_ofNat]
  ring

theorem neutralIV123Pole_mixed (a : ℝ) (f g : NeutralLogHilbertCarrier a) :
    inner ℂ f (neutralLogPoleOperator a g) =
      2 * conj (neutralIV123EvenMoment a (neutralLogPhysical f.val)) *
        neutralIV123EvenMoment a (neutralLogPhysical g.val) -
      2 * conj (neutralIV123OddMoment a (neutralLogPhysical f.val)) *
        neutralIV123OddMoment a (neutralLogPhysical g.val) := by
  rw [neutralLogPoleOperator_mixed]
  exact neutralIV123Pole_algebra _ _ _ _

theorem neutralIV123Pole_null_right (a : ℝ) (f g : NeutralLogHilbertCarrier a)
    (hp : sourceWindowMoment a (1/2) (neutralLogPhysical g.val) = 0)
    (hm : sourceWindowMoment a (-(1/2)) (neutralLogPhysical g.val) = 0) :
    inner ℂ f (neutralLogPoleOperator a g) = 0 := by
  rw [neutralLogPoleOperator_mixed, hp, hm]
  simp

theorem neutralIV123Pole_diagonal (a : ℝ) (f : NeutralLogHilbertCarrier a) :
    (inner ℂ f (neutralLogPoleOperator a f)).re =
      2 * ((neutralIV123EvenMoment a (neutralLogPhysical f.val)).re ^ 2 +
        (neutralIV123EvenMoment a (neutralLogPhysical f.val)).im ^ 2) -
      2 * ((neutralIV123OddMoment a (neutralLogPhysical f.val)).re ^ 2 +
        (neutralIV123OddMoment a (neutralLogPhysical f.val)).im ^ 2) := by
  rw [neutralIV123Pole_mixed]
  simp only [Complex.sub_re, Complex.mul_re, Complex.mul_im,
    Complex.conj_re, Complex.conj_im, Complex.ofNat_re, Complex.ofNat_im]
  ring

theorem neutralIV123Original_mixed (a : ℝ) (ha : 0 ≤ a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Mixed a u v =
      (∫ ξ : ℝ, conj ((𝓕 (u.toLp 2 volume) : RealComplexL2) ξ) *
        (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
        (𝓕 (v.toLp 2 volume) : RealComplexL2) ξ) +
      2 * conj (neutralIV123EvenMoment a (u.toLp 2 volume)) *
        neutralIV123EvenMoment a (v.toLp 2 volume) -
      2 * conj (neutralIV123OddMoment a (u.toLp 2 volume)) *
        neutralIV123OddMoment a (v.toLp 2 volume) := by
  rw [neutralIV103Mixed_native a ha u v hu hv,
    neutralActualZetaLogWeilFormOperator_mixed, neutralIV123Pole_mixed,
    neutralIV102Lift_physical, neutralIV102Lift_physical]
  ring

#print axioms neutralIV123Pole_algebra
#print axioms neutralIV123Pole_mixed
#print axioms neutralIV123Pole_null_right
#print axioms neutralIV123Pole_diagonal
#print axioms neutralIV123Original_mixed

end
end WeilDefect
