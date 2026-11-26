import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators

/-- Transfer a pointwise weighted majorant through the integral.
The signed change of variables and majorant construction are separate
premises; neither is asserted for the physical supersolution here. -/
theorem neutralIV152Integral_majorant (f g w : ℝ → ℝ) (C : ℝ)
    (hf : Integrable f) (hg : Integrable g) (hw : Integrable w)
    (hfg : ∀ᵐ x ∂volume, f x ≤ g x)
    (hgw : ∀ᵐ x ∂volume, g x ≤ C*w x) :
    (∫ x, f x) ≤ C * ∫ x, w x := by
  calc
    (∫ x, f x) ≤ ∫ x, g x := integral_mono_ae hf hg hfg
    _ ≤ ∫ x, C*w x := integral_mono_ae hg (hw.const_mul C) hgw
    _ = _ := by rw [integral_const_mul]

#print axioms neutralIV152Integral_majorant
end
end WeilDefect
